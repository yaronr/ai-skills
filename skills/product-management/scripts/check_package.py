#!/usr/bin/env python3
"""Check a product package against the writing standard.

Usage:
    python3 check_package.py DIR [--previous GIT_REF]

Runs every mechanical check in writing-standard §10 and prints PASS / FAIL / WARN per
check. Exit code 1 if any check fails.

With --previous, it also compares each file with its version at GIT_REF (for a revision)
and lists content that disappeared: table rows, links and bold lead-ins. That list is for
review against the "never cut" rule (§7); the script can't judge meaning.

Standard library only.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

CAPS = {"summary": 400, "body": 1500, "body_positioning": 1200, "appendix": 800,
        "brief": 400, "package": 6000, "trigger": 30, "heading": 15, "title": 12,
        "decision_lines": 3, "decision_line": 25, "risk": 60}
SKIP = ("sources.md",)
NO_CAP = ("user-stories",)

results = []


def report(status, file, check, detail=""):
    results.append(status)
    print(f"{status:<5} {file:<28} {check}{(': ' + detail) if detail else ''}")


def words(text):
    text = re.sub(r"\]\([^)]*\)", "]", text)  # count a link's text, not its URL
    return len(text.split())


def strip_front_matter(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def split(text):
    """Return (title, summary, body, appendix) blocks of a document (front matter removed)."""
    lines = strip_front_matter(text).splitlines()
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), "")
    part, parts = "head", {"head": [], "summary": [], "body": [], "appendix": []}
    for l in lines:
        if l.startswith("## Executive summary"):
            part = "summary"
            continue
        if l.startswith("## Appendix"):
            part = "appendix"
            continue
        if part == "summary" and (l.startswith("## ") or l.strip() == "---"):
            part = "body"
        parts[part].append(l)
    return title, *("\n".join(parts[k]) for k in ("summary", "body", "appendix"))


def callouts(summary_and_body, kind):
    """Return the text of each `> [!KIND]` callout."""
    out, cur = [], None
    for l in summary_and_body.splitlines():
        if l.strip().startswith(f"> [!{kind}]"):
            cur = []
            out.append(cur)
        elif cur is not None and l.startswith(">"):
            cur.append(l.lstrip("> ").strip())
        else:
            cur = None
    return [[x for x in c if x] for c in out]


CODE = re.compile(r"\b[A-Z]{1,3}[0-9]{1,2}\b")
GPU_LIKE = re.compile(r"^(A|H|B|L|T|V|P|G|M|K)[0-9]{2,3}$")  # A100, H100, L40… are names


def codes(text):
    text = re.sub(r"\[[^\]]*\]", "", text)          # source tags like [S10]
    text = re.sub(r"\([^)]*\.md[^)]*\)", "", text)  # link targets
    return sorted({c for c in CODE.findall(text) if not GPU_LIKE.match(c)})


def check_doc(path, text):
    name = path.name
    if name == "00-brief.md" or name.endswith("-brief.md"):
        n = words(strip_front_matter(text))
        report("PASS" if n <= CAPS["brief"] else "FAIL", name, "brief words", f"{n} (≤{CAPS['brief']})")
    title, summary, body, appendix = split(text)
    if not summary.strip():
        report("WARN", name, "executive summary", "missing (ok only for a sub-page document)")
        return
    tw = words(title)
    report("PASS" if tw <= CAPS["title"] else "FAIL", name, "title words", f"{tw} (≤{CAPS['title']})")
    n = words(summary)
    report("PASS" if n <= CAPS["summary"] else "FAIL", name, "summary words", f"{n} (≤{CAPS['summary']})")
    is_brief = name == "00-brief.md" or name.endswith("-brief.md")
    if not is_brief and not any(k in name for k in NO_CAP):
        cap = CAPS["body_positioning"] if "positioning" in name else CAPS["body"]
        n = words(body)
        report("PASS" if n <= cap else "FAIL", name, "body words", f"{n} (≤{cap})")
        n = words(appendix)
        report("PASS" if n <= CAPS["appendix"] else "FAIL", name, "appendix words", f"{n} (≤{CAPS['appendix']})")
    found = codes(summary)
    report("PASS" if not found else "FAIL", name, "codes in summary",
           ", ".join(found) if found else "none")
    heads = [l[3:].strip() for l in body.splitlines() if l.startswith("## ")]
    long_heads = [h for h in heads if words(h) > CAPS["heading"]]
    report("PASS" if not long_heads else "FAIL", name, "heading words",
           f"{len(long_heads)} over {CAPS['heading']}: " + " | ".join(long_heads) if long_heads else f"{len(heads)} headings ok")
    coded_heads = [h for h in heads if codes(h)]
    if coded_heads:
        report("FAIL", name, "codes in headings", " | ".join(coded_heads))
    lens = len(re.findall(r"^\*Lens: ", body, re.M))
    if heads:
        report("PASS" if lens >= len(heads) else "FAIL", name, "lens lines", f"{lens} for {len(heads)} claim sections")
    sb = summary + "\n" + body
    for kind, limit in (("IMPORTANT", 1), ("WARNING", 1)):
        boxes = callouts(sb, kind)
        if len(boxes) > limit:
            report("FAIL", name, f"{kind} callouts", f"{len(boxes)} (≤{limit})")
    for box in callouts(sb, "IMPORTANT"):
        long = [l for l in box if words(l) > CAPS["decision_line"]]
        ok = len(box) <= CAPS["decision_lines"] and not long
        report("PASS" if ok else "FAIL", name, "decision box",
               f"{len(box)} lines (≤{CAPS['decision_lines']}), {len(long)} over {CAPS['decision_line']} words")
        found = codes(" ".join(box))
        if found:
            report("FAIL", name, "codes in decision box", ", ".join(found))
    for box in callouts(sb, "WARNING"):
        n = words(" ".join(box))
        report("PASS" if n <= CAPS["risk"] else "FAIL", name, "risk box words", f"{n} (≤{CAPS['risk']})")


def check_sources(path, text):
    body = strip_front_matter(text)
    extra = [l for l in body.splitlines() if l.startswith("## ")]
    ok = "## Executive summary" not in body and not extra
    report("PASS" if ok else "FAIL", path.name, "table only",
           "ok" if ok else f"{len(extra)} sections; remove them")


def check_package(files):
    counted = [p for p in files if p.name not in SKIP and not any(k in p.name for k in NO_CAP)]
    n = sum(words(p.read_text()) for p in counted)
    report("PASS" if n <= CAPS["package"] else "FAIL", "(package)", "package words", f"{n} (≤{CAPS['package']})")
    triggers = []
    for p in files:
        for l in p.read_text().splitlines():
            if "**Reverse trigger:**" in l:
                triggers.append((p.name, words(l.split("**Reverse trigger:**", 1)[1])))
    if not triggers:
        report("WARN", "(package)", "reverse trigger", "no '**Reverse trigger:**' line (required when options are compared)")
    else:
        report("PASS" if len(triggers) == 1 else "FAIL", "(package)", "reverse trigger lines",
               f"{len(triggers)} (exactly 1, in full; link elsewhere)")
        for f, n in triggers:
            report("PASS" if n <= CAPS["trigger"] else "FAIL", f, "reverse trigger words", f"{n} (≤{CAPS['trigger']})")


def previous_version(path, ref):
    root = subprocess.run(["git", "-C", str(path.parent), "rev-parse", "--show-toplevel"],
                          capture_output=True, text=True)
    if root.returncode:
        return None
    rel = path.resolve().relative_to(Path(root.stdout.strip()).resolve())
    r = subprocess.run(["git", "-C", root.stdout.strip(), "show", f"{ref}:{rel}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def items(text):
    rows = {re.sub(r"\*", "", l.split("|")[1]).strip() for l in text.splitlines()
            if l.startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", l) and len(l.split("|")) > 2}
    links = set(re.findall(r"\]\(([^)#]+)", text))
    leads = set(re.findall(r"^(?:[-*] |\d+\. |> [-*] )?\*\*([^*\n]{3,80})\*\*", text, re.M))
    return rows, links, leads


def compare(files, ref, folder):
    print(f"\nRemoved since {ref} (review against 'never cut', writing standard §7):")
    any_removed = False
    names = {p.name for p in files}
    for p in files:
        old = previous_version(p, ref)
        if old is None:
            continue
        o_rows, o_links, o_leads = items(old)
        n_rows, n_links, n_leads = items(p.read_text())
        pkg = "\n".join(q.read_text() for q in files)
        for label, gone in (("table row", o_rows - n_rows), ("link", o_links - n_links),
                            ("bold lead-in", o_leads - n_leads)):
            for g in sorted(gone):
                if g and g not in pkg:  # still present elsewhere in the package → moved, not lost
                    any_removed = True
                    print(f"  {p.name:<26} {label}: {g[:100]}")
    if not any_removed:
        print("  nothing")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dir")
    ap.add_argument("--previous", help="git ref of the version before this revision")
    a = ap.parse_args()
    import signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    folder = Path(a.dir)
    files = sorted(p for p in folder.glob("*.md"))
    if not files:
        sys.exit(f"no .md files in {folder}")
    for p in files:
        text = p.read_text()
        if p.name in SKIP:
            check_sources(p, text)
        else:
            check_doc(p, text)
    check_package(files)
    if a.previous:
        compare(files, a.previous, folder)
    fails = results.count("FAIL")
    print(f"\n{fails} failed · {results.count('WARN')} warnings · {results.count('PASS')} passed")
    print("Not checked by script: heading-only story, level test, required lenses as exhibits, "
          "the brief's 'why it won' judgment, meaning of removed items.")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
