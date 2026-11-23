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
- A document under one page in total needs only the bold bottom line.

## 4 · Body

- **Headings are claims**, not topics. Bad: `## Market analysis`. Good:
  `## Mid-market churn, not acquisition, caps growth`. Never a bare framework name.
- **Lens line.** Under each claim heading, one line naming the framework used:
  `*Lens: metric tree (frameworks §3B)*`.
- Each section proves only its own heading. Sections follow the storyline order.
- **Exhibits** (tables, trees, matrices): one message each. Title the exhibit with that
  message, and add `Source: <…>` under it.
- Close with one **quotable line**, then `## Appendix` for detail, data and queries.

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
| Appendix, user stories, metric-definition tables, risk registers | No cap; keep each item compact |

The body is everything between the end of the executive summary and `## Appendix`.

## 8 · Package

- **One fact, one home.** Evidence, tables, option grids and risk lists live in exactly
  one file; other files link to it. Executive summaries may restate conclusions.
- `00-brief.md` is the package's executive summary, plus the goal / NSM table and the file
  list.

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

```bash
# Summary words (≤400)
awk '/^## Executive summary/{s=1;next} s&&/^(## |---$)/{exit} s' FILE | wc -w
# Body words (cap per §7)
awk '/^## Executive summary/{s=1;next} s==1&&/^(## |---$)/{s=2} /^## Appendix/{exit} s==2' FILE | wc -w
# Heading-only test: read this alone; it must tell the story
grep -E '^#{1,2} ' FILE
# Lens lines (one per claim section)
grep -c '^\*Lens: ' FILE
```

- **Heading-only test:** the `#`/`##` lines alone make the argument.
- **Level test:** nothing from the document's "may NOT contain" list is in the body.
- **Lens test:** every required lens for the document type appears as an exhibit.
