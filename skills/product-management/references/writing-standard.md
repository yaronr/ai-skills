# Writing standard

Every document the team ships follows this. It combines five established methods:

- **Pyramid Principle (Minto):** answer first, then non-overlapping supporting claims; headings
  are claims.
- **Narrative memo:** full sentences, a hard length cap, data in the appendix.
- **Analytic standards (ICD 203):** key judgments with stated confidence, alternatives
  considered, signals to watch.
- **Strategy kernel (Rumelt) and where-to-play / how-to-win (Lafley & Martin).**
- **Positioning (Dunford):** alternatives → unique attributes → value → best-fit customer →
  category.

Readers have ADHD. Most read only the executive summary and the bold text. Write for
that reader.

**Contents:** 1 One document, one question · 2 Storyline first · 3 Executive summary ·
4 Body · 5 Skim layer · 6 Required lenses · 7 Length · 8 Package · 9 Claim notes · 10 Checks

---

## 1 · One document, one question, one level

Each document answers one question at one level. Anything below that level goes to
`## Appendix` or to the document that owns it, linked.

| Document | Answers | Body may NOT contain |
|---|---|---|
| Research / analysis / diagnosis | What is true, and what it means | SQL or query text, run steps, solution design, roadmap, feature lists |
| Strategy / vision | Where we play, how we win, what we bet | Feature lists, requirements, user stories, acceptance criteria, sprint or ticket detail, UI detail |
| Positioning / GTM | Who it's for, what it beats, why it wins, how it reaches them | Feature specs, requirements, campaign execution detail, full pricing tables (→ pricing doc) |
| PRD | What we build first, and how we know it works | Option scoring, market sizing, competitor deep-dives (→ strategy / research), code-level design |
| Metrics spec | How we measure | Feature specs, strategy debate |
| Risks & decisions | What could hurt us; what we decided | Re-arguing options already decided in the strategy doc |

## 2 · Storyline first

Before any drafting, write `_work/storyline.md`: one block per document.

```markdown
## 02-strategy.md · Q: <the one question>
Answer: <one sentence>
1. <claim sentence>          · Lens: <framework>  · Evidence needed: <…>
2. <claim sentence>          · Lens: <…>          · Evidence needed: <…>
3. <claim sentence>          · Lens: <…>          · Evidence needed: <…>
```

- 3–5 claims. Together they prove the answer; they don't overlap.
- Evidence that breaks a claim changes the storyline. Never patch the draft around it.

## 3 · Executive summary (opens every document, ≤400 words)

```markdown
# <Title: the answer, ≤12 words>

## Executive summary
**<Bottom line: the answer in one bold sentence.>**

- **<Lead-in claim.>** <≤2 lines: evidence with <ins>the key number</ins> (source).> 🟢 high
- **<Lead-in claim.>** <…> 🟡 moderate
- **<Lead-in claim.>** <…> 🔴 low
  (3–5 key judgments, in storyline order)

> [!IMPORTANT]
> ✅ **Decision:** <what> · from <role> · before <gate/milestone>

> [!WARNING]
> ⚠️ **Main risk:** <risk> → <mitigation>. **Reverse if** <metric, threshold, milestone>.

**Next:** 1) <action> (owner, gate) · 2) <…> · 3) <…>
```

- Order is fixed: bottom line → key judgments → decision → risk → next.
- Every judgment has a number and a confidence marker. Numbers are sourced or `Estimate`.
- Drop the decision or risk box when it doesn't apply. Never pad.
- **Plain words only.** The summary and every heading spell out each internal label
  (hypothesis, gate, decision, persona or option codes such as "H3", "G1", "D2", "P4"). A
  reader who reads only the summary must understand every word. Source tags like `[S10]`
  are fine. A code may appear in the body after it is defined in that document.
- **Callouts stay small.** The decision box lists each decision on its own line, ≤25
  words per line, at most 3 lines. Context such as a conflict with an earlier decision
  goes in the body. The risk box is ≤60 words, and its reverse trigger is ≤30 words.
- A document under one page in total needs only the bold bottom line.

## 4 · Body

- **Headings are claims**, not topics. Bad: `## Market analysis`. Good:
  `## Mid-market churn, not acquisition, caps growth`. Never a bare framework name.
  A heading is one complete claim of ≤15 words; the title is ≤12 words.
- **Lens line.** Under each claim heading, one line naming the framework used:
  `*Lens: metric tree (frameworks §3B)*`.
- Each section proves only its own heading. Sections follow the storyline order.
- **Exhibits** (tables, trees, matrices): one message each. Title the exhibit with that
  message, and add `Source: <…>` under it.
- Close with one **quotable line**, then `## Appendix` for detail, data and queries.
- **The appendix holds only what the body cites:** evidence, arithmetic, queries, method.
  It is not storage for cut text. If the body does not link to it, delete it.

## 5 · Skim layer

A reader who sees only bold text, markers and callouts gets the story.

- **Bold lead-in** on every paragraph and key bullet. Paragraphs ≤3 lines; longer → bullets.
- **One number underlined** per paragraph at most: `<ins>9%</ins>`.
- **Markers**, the same everywhere; always the word beside the emoji:

  | Marker | Meaning |
  |---|---|
  | 🟢 high · 🟡 moderate · 🔴 low | Confidence in a judgment |
  | ▲ / ▼ | Metric up / down |
  | ✅ | Decision |
  | ⚠️ | Risk |
  | ❓ | Open question |

- **Callouts** (`> [!IMPORTANT]`, `> [!WARNING]`): at most one of each per document.
- `Assumption:` and `Estimate` labels stay as they are.

## 6 · Required lenses (GPM frameworks, shown as exhibits)

Every document shows its frameworks visibly, as exhibits with a Lens line. Use the
playbooks in [frameworks.md](frameworks.md) and [toolkit.md](toolkit.md).

| Document | Required lenses (at least these) |
|---|---|
| Research / diagnosis | Segments × JTBD (§1) or metric tree + segment decomposition (§3B); ranked hypothesis table with a one-line check each; key judgments with confidence |
| Decision analysis | §3A flow; sizing with arithmetic; sensitivity on the 2 key inputs |
| Strategy / vision | 5 Cs (§5); Rumelt kernel; where to play / how to win; 7 Powers; options matrix (3 options); NSM + guardrail; reverse trigger |
| Positioning / GTM | Competitive alternatives; Dunford positioning canvas; JTBD of the best-fit customer; ICP sequence (§6); messaging hierarchy with proof points |
| PRD | Problem with JTBD (§1); goals / non-goals; NSM + drivers + guardrail; RICE or MoSCoW for scope; one-way doors |
| Metrics spec | Metric tree; HEART/GSM where UX-heavy; experiment design (§4) |
| Pricing | Value metric; Van Westendorp or Gabor-Granger plan; packaging (§7) |

## 7 · Length

| Part | Cap |
|---|---|
| Executive summary | ≤400 words (aim 150–250) |
| Body: research, strategy, PRD, metrics, GTM | ≤1,500 words |
| Body: positioning | ≤1,200 words |
| `00-brief.md` | ≤400 words in total |
| Appendix | ≤800 words per document |
| **Whole package** (all files except `sources.md` and user stories) | ≤6,000 words |
| User stories, metric-definition tables, risk registers | No cap; keep each item compact |

The body is everything between the end of the executive summary and `## Appendix`.

- **A cap is a ceiling, not a target.** Aim for about two thirds of each cap.
- **Over a cap: cut, don't move.** Move detail to the appendix only while the appendix
  and the package stay under their caps. Otherwise delete it, or keep one line and a link
  to the source.
- **Say each thing once.** The reverse trigger, the decisions and each number are written
  in full in one place; elsewhere, restate in a few words and link. Write the full reverse
  trigger on one line that starts `**Reverse trigger:**`, ≤30 words, so the check finds it.

**Never cut (protected content).** Cutting to a cap removes repetition, filler and
detail, never the argument. These survive every cut, at least as one line in the body:

- the bottom line, the decisions and the reverse trigger;
- the evidence behind the chosen option and segment (the numbers that make the pick);
- the options matrix and its sensitivity;
- the verdict on earlier proposals or documents the question builds on: what to keep,
  what to change, and why;
- every required lens (§6).

If a cap can't be met without cutting protected content, keep the content and report the
overrun. A change of substance (a metric, a guardrail, a score, a decision) is never a
side effect of a cut: make it only on purpose, and list it in the report.

## 8 · Package

- **One fact, one home.** Evidence, tables, option grids and risk lists live in exactly
  one file; other files link to it. Executive summaries may restate conclusions.
- `00-brief.md` is the package's executive summary, plus the goal / NSM table and the file
  list. One of its key judgments says **why the pick won**: the evidence behind the chosen
  option or segment, with its number (e.g. how large or how hurt that segment is, and why
  the runner-up lost).
- `sources.md` is the source table only: no executive summary, no claim sections, no
  appendix. It is exempt from the summary, heading and lens checks.

## 9 · Claim notes (specialists → author)

Specialists don't write document sections. They return claim notes to `_work/notes/<role>.md`:

```markdown
- Claim: <one sentence>
  Evidence: <numbers + source #, or Estimate with arithmetic>
  Confidence: 🟢 high | 🟡 moderate | 🔴 low · Would change if: <signal>
```

Tables a lens needs (metric tree, competitor table, risk register) go in the notes as
exhibits. The author places them.

## 10 · Checks (editor and graders)

Run them all at once with `python3 scripts/check_package.py DIR [--previous GIT_REF]`. It
prints PASS / FAIL per check and exits 1 on any failure. With `--previous`, it lists the
table rows, links and bold lead-ins that a revision removed, for review against §7. The
commands below are the same checks, one at a time.

```bash
# Summary words (≤400)
awk '/^## Executive summary/{s=1;next} s&&/^(## |---$)/{exit} s' FILE | wc -w
# Body words (cap per §7)
awk '/^## Executive summary/{s=1;next} s==1&&/^(## |---$)/{s=2} /^## Appendix/{exit} s==2' FILE | wc -w
# Heading-only test: read this alone; it must tell the story
grep -E '^#{1,2} ' FILE
# Lens lines (one per claim section)
grep -c '^\*Lens: ' FILE
# Appendix words (≤800)
awk '/^## Appendix/{s=1;next} s' FILE | wc -w
# Package words (≤6,000; front matter counts, so keep it short)
ls DIR/*.md | grep -v -e sources.md -e user-stories | xargs cat | wc -w
# Reverse trigger words (≤30; one full line per package)
grep -h '\*\*Reverse trigger:\*\*' DIR/*.md | sed 's/.*Reverse trigger:\*\*//' | wc -w
# Code candidates in the summary (each must be spelled out; GPU or product names are fine)
awk '/^## Executive summary/{s=1;next} s&&/^(## |---$)/{exit} s' FILE | grep -v '^\s*$' | sed 's/\[S[0-9]*\]//g' | grep -oE '\b[A-Z]{1,3}[0-9]{1,2}\b' | sort -u
```

- **Heading-only test:** the `#`/`##` lines alone make the argument.
- **Level test:** nothing from the document's "may NOT contain" list is in the body.
- **Lens test:** every required lens for the document type appears as an exhibit.
- **Protected-content test:** compare with the previous version. Everything in the
  "never cut" list (§7) is still there, and every change of substance is listed.
- **Plain-words test:** the code-candidate command prints nothing that is an internal
  label.
