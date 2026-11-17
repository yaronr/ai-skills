#!/usr/bin/env python3
"""Product knowledge-base helper (stdlib only).

Usage:
  kb.py init  <root> --name "Product"   scaffold core folders + files (never overwrites)
  kb.py index <root>                    rebuild INDEX.md from front matter
  kb.py lint  <root>                    report metadata, staleness and link problems
  kb.py audit <root> [--out plan.md]    classify files and propose a git-mv plan (moves nothing)
"""
import argparse
import datetime as dt
import os
import re
import sys

TYPES = {
    "vision": "strategy", "strategy": "strategy", "okr": "strategy", "roadmap": "strategy",
    "persona": "customers/personas", "segment": "customers", "account": "customers/accounts",
    "research-plan": "discovery/research", "research-synthesis": "discovery/research",
    "interview": "discovery/interviews", "feedback-digest": "discovery/feedback",
    "insight": "discovery/insights", "opportunity-tree": "discovery",
    "competitor": "market/competitors", "market": "market",
    "analysis": "analysis", "diagnosis": "analysis", "sizing": "analysis",
    "experiment": "experiments",
    "metrics-spec": "metrics", "metric-definition": "metrics",
    "decision": "decisions",
    "brief": "initiatives", "prd": "initiatives", "user-stories": "initiatives",
    "gtm": "initiatives", "launch": "initiatives", "retro": "initiatives",
    "release-notes": "launches", "meeting": "meetings", "template": "templates",
    "glossary": ".", "readme": ".", "changelog": ".", "index": ".",
}
STATUSES = {"draft", "review", "approved", "shipped", "superseded", "archived",
            "living", "planned", "running", "concluded", "frozen"}
EVERGREEN = {"vision", "strategy", "okr", "roadmap", "persona", "segment", "insight",
             "competitor", "market", "metrics-spec", "metric-definition", "opportunity-tree"}
SKIP_DIRS = {".git", "node_modules", "archive", ".venv", "__pycache__"}
SKIP_FILES = {"INDEX.md", "CHANGELOG.md", "README.md", "glossary.md"}
CORE_DIRS = ["strategy", "customers/personas", "discovery/research", "discovery/interviews",
             "discovery/feedback", "discovery/insights", "market/competitors", "analysis",
             "experiments", "metrics", "decisions", "initiatives", "templates", "archive"]

# filename/content keyword -> type, checked in order (audit heuristics)
HEURISTICS = [
    (r"\bprd\b|product requirements", "prd"),
    (r"user[-_ ]?stor|acceptance criteria|given .* when .* then", "user-stories"),
    (r"\badr\b|decision record|^decision|\bdecided\b", "decision"),
    (r"interview|transcript|call notes", "interview"),
    (r"nps|csat|support tickets?|feedback|survey|reviews?", "feedback-digest"),
    (r"insight", "insight"),
    (r"persona", "persona"),
    (r"competit|vs\.? |battlecard", "competitor"),
    (r"pricing|market siz|\btam\b|trend", "market"),
    (r"experiment|a/b|ab[-_ ]test", "experiment"),
    (r"metric|kpi|north star|dashboard", "metrics-spec"),
    (r"roadmap", "roadmap"),
    (r"vision", "vision"),
    (r"strategy|okr", "strategy"),
    (r"go[-_ ]to[-_ ]market|\bgtm\b|launch", "gtm"),
    (r"release notes|changelog", "release-notes"),
    (r"analysis|diagnos|cohort|funnel|sizing", "analysis"),
    (r"research|study|usability", "research-synthesis"),
    (r"retro|post[-_ ]?mortem", "retro"),
    (r"brief|one[-_ ]pager", "brief"),
    (r"meeting|minutes|standup|sync", "meeting"),
]

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")


def parse_fm(text):
    m = FM_RE.match(text)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        line = line.split(" #", 1)[0].rstrip()
        if not line or line.startswith("#") or ":" not in line or line.startswith(" "):
            continue
        k, v = line.split(":", 1)
        v = v.strip().strip("'\"")
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
        data[k.strip()] = v
    return data


def walk(root, exts=(".md",)):
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS and not x.startswith(".")]
        for f in sorted(files):
            if f.lower().endswith(exts):
                yield os.path.join(d, f)


def parse_date(s):
    try:
        return dt.date.fromisoformat(str(s)[:10])
    except ValueError:
        return None


def cmd_init(root, name):
    os.makedirs(root, exist_ok=True)
    for d in CORE_DIRS:
        os.makedirs(os.path.join(root, d), exist_ok=True)
    today = dt.date.today().isoformat()
    files = {
        "product.yaml": f"name: {name}\nmission: TBD\nnorth_star: TBD\nguardrails: []\n"
                        f"segments: []\nowners:\n  product: TBD\ncreated: {today}\n",
        "README.md": f"# {name}: product knowledge base\n\n**Start here.** What it is, who it's "
                     "for, how we measure it, and what we're betting on now.\n\n"
                     "| Mission | North star | Guardrail | Current bets |\n|---|---|---|---|\n"
                     "| TBD | TBD | TBD | TBD |\n\n📂 [INDEX](INDEX.md) · [Glossary](glossary.md) · "
                     "[Decisions](decisions/) · [Changelog](CHANGELOG.md)\n",
        "glossary.md": "---\ntype: glossary\nstatus: living\n---\n# Glossary\n\n"
                       "Canonical names. Use these spellings everywhere.\n\n"
                       "| Term | Definition | Notes |\n|---|---|---|\n\n"
                       "## Feedback theme taxonomy\n\n| Theme | Definition |\n|---|---|\n",
        "CHANGELOG.md": f"# Changelog\n\n- {today} · KB initialized · `/`\n",
        "discovery/opportunities.md": "---\ntype: opportunity-tree\nstatus: living\n"
                                      f"updated: {today}\nreview_by: TBD\n---\n# Opportunity tree\n\n"
                                      "**Outcome:** TBD\n\n- Opportunity → solutions → assumption tests\n",
    }
    made = []
    for rel, body in files.items():
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            with open(p, "w") as fh:
                fh.write(body)
            made.append(rel)
    cmd_index(root, quiet=True)
    print(f"Initialized {root}: {len(CORE_DIRS)} folders; created {made or 'no new files'}")


def collect(root):
    docs = []
    for p in walk(root):
        rel = os.path.relpath(p, root)
        if os.path.basename(p) in SKIP_FILES and os.path.dirname(rel) == "":
            continue
        with open(p, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        fm = parse_fm(text) or {}
        title = fm.get("title")
        if not title:
            h = re.search(r"^#\s+(.+)$", text, re.M)
            title = h.group(1).strip() if h else os.path.basename(p)
        docs.append({"rel": rel, "fm": fm, "title": title, "text": text, "has_fm": bool(fm)})
    return docs


def cmd_index(root, quiet=False):
    docs = collect(root)
    groups = {}
    for d in docs:
        groups.setdefault(d["fm"].get("type", "untyped"), []).append(d)
    order = {"approved": 0, "living": 1, "review": 2, "draft": 3, "shipped": 4}
    lines = ["# INDEX", "", "_Generated by `kb.py index`. Do not edit by hand._", "",
             f"{len(docs)} documents · updated {dt.date.today().isoformat()}", ""]
    for t in sorted(groups):
        lines += [f"## {t} ({len(groups[t])})", "", "| Doc | Status | Updated | Owner |",
                  "|---|---|---|---|"]
        by_recent = sorted(groups[t], key=lambda d: str(d["fm"].get("updated", d["fm"].get("created", ""))),
                           reverse=True)
        for d in sorted(by_recent, key=lambda d: order.get(d["fm"].get("status", ""), 9)):
            fm = d["fm"]
            lines.append(f"| [{d['title']}]({d['rel']}) | {fm.get('status', '—')} | "
                         f"{fm.get('updated', fm.get('created', '—'))} | {fm.get('owner', '—')} |")
        lines.append("")
    with open(os.path.join(root, "INDEX.md"), "w") as fh:
        fh.write("\n".join(lines))
    if not quiet:
        print(f"INDEX.md: {len(docs)} docs in {len(groups)} types")


def cmd_lint(root):
    today = dt.date.today()
    problems = []
    for d in collect(root):
        fm, rel = d["fm"], d["rel"]
        if not d["has_fm"]:
            problems.append(("error", rel, "missing front matter"))
            continue
        t = fm.get("type")
        if t not in TYPES:
            problems.append(("error", rel, f"unknown type: {t!r}"))
        if fm.get("status") and fm["status"] not in STATUSES:
            problems.append(("warn", rel, f"unknown status: {fm['status']!r}"))
        rb = parse_date(fm.get("review_by", ""))
        if t in EVERGREEN and fm.get("status") not in ("superseded", "archived"):
            if rb and rb < today:
                problems.append(("warn", rel, f"stale: review_by {rb} passed"))
            elif not rb:
                problems.append(("info", rel, "evergreen doc without review_by"))
        if t in ("competitor", "market"):
            up = parse_date(fm.get("updated", fm.get("created", "")))
            if up and (today - up).days > 183:
                problems.append(("warn", rel, f"market facts older than 6 months ({up})"))
        if t == "insight":
            ev = fm.get("evidence") or []
            if not ev:
                problems.append(("warn", rel, "insight without evidence links"))
        for link in LINK_RE.findall(d["text"]):
            if re.match(r"^[a-z]+:", link):
                continue
            target = os.path.normpath(os.path.join(root, os.path.dirname(rel), link))
            if not os.path.exists(target):
                problems.append(("error", rel, f"broken link: {link}"))
        if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", d["text"]):
            problems.append(("warn", rel, "possible email address (PII?)"))
    rank = {"error": 0, "warn": 1, "info": 2}
    for sev, rel, msg in sorted(problems, key=lambda x: (rank[x[0]], x[1])):
        print(f"{sev:5} {rel}: {msg}")
    errs = sum(1 for p in problems if p[0] == "error")
    print(f"\n{errs} errors · {len(problems) - errs} warnings/info")
    return 1 if errs else 0


def classify(rel, text):
    fm = parse_fm(text) or {}
    if fm.get("type") in TYPES:
        return fm["type"], "front matter"
    hay = (rel + "\n" + text[:2000]).lower()
    for pat, t in HEURISTICS:
        if re.search(pat, hay, re.M):
            return t, f"matched /{pat.split('|')[0]}/"
    return None, "no match"


def cmd_audit(root, out):
    rows, plan = [], []
    exts = (".md", ".txt", ".docx", ".pdf", ".csv", ".xlsx", ".pptx", ".html")
    for p in walk(root, exts):
        rel = os.path.relpath(p, root)
        if os.path.dirname(rel) == "" and os.path.basename(p) in SKIP_FILES | {"product.yaml"}:
            continue
        text = ""
        if p.endswith((".md", ".txt", ".csv", ".html")):
            with open(p, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        t, why = classify(rel, text)
        if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text):
            why += " · ⚠ possible PII: redact before filing"
        if not t:
            rows.append((rel, "?", "—", "needs human/LLM review"))
            continue
        folder = TYPES[t]
        if folder == "initiatives":
            folder = "initiatives/<yyyy>-q<n>-<slug>"
        target = os.path.join(folder, os.path.basename(rel)) if folder != "." else rel
        ok = os.path.dirname(rel).startswith(TYPES[t]) or folder == "."
        rows.append((rel, t, "✓ in place" if ok else target, why))
        if not ok:
            plan.append(f"git mv '{rel}' '{target}'")
    lines = ["# KB audit: proposed reorganization", "",
             f"{len(rows)} files · {len(plan)} moves proposed · nothing has been moved", "",
             "| File | Type | Proposed location | Why |", "|---|---|---|---|"]
    lines += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows]
    lines += ["", "## Move plan (review, then run from the KB root)", "", "```bash"]
    lines += plan or ["# nothing to move"]
    lines += ["```", "", "Then: add front matter to untyped files, run `kb.py index` and `kb.py lint`."]
    report = "\n".join(lines)
    if out:
        with open(out, "w") as fh:
            fh.write(report)
        print(f"Wrote {out}: {len(rows)} files, {len(plan)} moves proposed")
    else:
        print(report)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init"); p.add_argument("root"); p.add_argument("--name", default="Product")
    p = sub.add_parser("index"); p.add_argument("root")
    p = sub.add_parser("lint"); p.add_argument("root")
    p = sub.add_parser("audit"); p.add_argument("root"); p.add_argument("--out")
    a = ap.parse_args()
    if a.cmd == "init":
        cmd_init(a.root, a.name)
    elif a.cmd == "index":
        cmd_index(a.root)
    elif a.cmd == "lint":
        sys.exit(cmd_lint(a.root))
    elif a.cmd == "audit":
        cmd_audit(a.root, a.out)


if __name__ == "__main__":
    main()
