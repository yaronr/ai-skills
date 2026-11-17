# Templates

Every document starts with the **executive summary block** below: bottom line first,
then findings, then what to do, in one page at most. The templates after it show only the
body that follows the summary.

Delete any section that does not apply. Don't pad a section to fill it.

**Contents:** Executive summary block · 00 Brief · PRD · User stories · Metrics spec · Strategy memo · Options matrix ·
Decision record · GTM plan · Research synthesis · Analysis memo / diagnosis · Vision &
roadmap · PR/FAQ · Alignment one-pager · sources.md

---

## Executive summary block (starts every document)

Every document opens with this block, right under the title. Readers have ADHD: most
read only this. **Max one page: hard cap 400 words, aim for 150–250.** Detail goes in the
body below it.

```markdown
# <Title>: <bottom line in ≤12 words>

## Executive summary
**Bottom line:** <the answer or decision, 1–2 sentences>

**Key findings**
- <finding + number + (source) or Estimate>
- <finding + number>
- <finding + number>            (3–5 bullets max)

**Recommendation:** <what we do> · **Trade-off:** <what we give up>
**Decision needed:** <what> · from <role> · before <gate/milestone>
**Risks:** <top 1–3, each → mitigation> · **Reverse trigger:** <metric, threshold, milestone>
**Next steps:** 1) <action> (owner, gate) 2) … 3) …

---
<Body: the details, evidence and appendices, in the order of the findings.>
```

Rules:

- Order is fixed: bottom line first, then findings, then what to do.
- Every finding has a number. Every number is sourced or labelled `Estimate`.
- Drop a line that doesn't apply (e.g. no decision needed). Don't pad.
- A document under one page in total (an insight note, a decision record) needs only
  the **Bottom line** line.
- Check the length: `awk '/^## Executive summary/{f=1;next} /^(## |---)/{f=0} f' <file> | wc -w`.

---

## 00 · Brief = the package's executive summary (always included)

`00-brief.md` is the executive summary for the whole package. It is the block above,
covering all the documents, plus at most these two lines. The **whole file** is one page
(≤400 words).

```markdown
| Goal | North star | Guardrail | First milestone |
|---|---|---|---|
| <growth/engagement/…> | <metric + target> | <metric + limit> | <what · gate> |

📂 Details: 01-research · 02-strategy · 03-prd · 04-user-stories · 05-metrics · …
```

---

## PRD (lean)

```markdown
# PRD: <feature>: <one-line outcome>

Status: Draft · Owner: PM · Updated: <date>

## Executive summary
<block: bottom line = problem → solution → metric>

## Problem
- **Who:** <segment> (<size>)
- **Pain:** <what's hard today> (evidence: <source>)
- **Cost of inaction:** <number>

## Goals / Non-goals
| Goals (measurable) | Non-goals (and who handles them) |
|---|---|

## Solution (MVP)
- <capability 1>: <user value>
- <capability 2>
- **Not in v1:** <…>

## Key flows
1. <step> → <step> → <outcome>   (link: designer artifact)

## Requirements
| ID | Requirement | Priority (P0/P1/P2) | Notes |
|---|---|---|---|

## Non-functional
Performance · reliability (SLO) · security & privacy · accessibility (WCAG 2.2 AA) ·
i18n · cost per unit

## Metrics
North star · drivers · guardrail · instrumentation events (see 05-metrics)

## Launch
Allow list → preview → GA · exit criteria for each stage · rollback plan

## Risks · Dependencies · Open questions
| Item | Type | Owner | Mitigation · by milestone/gate |
|---|---|---|---|
```

---

## User stories

Group the stories into **epics**. For each story:

```markdown
### <ID> · <short title>   [P0 · S/M/L · Epic: <name>]
**As a** <specific persona>, **I want** <capability>, **so that** <outcome>.

**Acceptance criteria**
- **Given** <context> **When** <action> **Then** <observable result>
- **Given** <edge case> **When** … **Then** …
- **Given** <error / empty / offline state> **When** … **Then** …

Notes: analytics event `<name>` · a11y: <…> · depends on <ID>
```

**Checks:**

- The story is **INVEST**: Independent, Negotiable, Valuable, Estimable, Small, Testable.
- There are at least 3 acceptance criteria: the happy path, an edge case and an error.
- The persona is specific. "As a user" is not acceptable.
- Order the stories as a **story map**. Release 1 is the walking skeleton.

---

## Metrics spec

```markdown
# Metrics: <product/feature>
**Goal:** <outcome> · **NSM:** <metric> · **Guardrail:** <metric>

## Metric tree
NSM
├─ Driver A (leading) → team <x>
├─ Driver B → team <y>
└─ Driver C
Guardrails: <reliability> · <margin> · <trust>

## Definitions
| Metric | Formula | Unit · window | Baseline | Target (by milestone) | Cadence | L/L | Kill criterion |
|---|---|---|---|---|---|---|---|

## HEART / GSM (if UX-heavy)
| Dimension | Goal | Signal | Metric |
|---|---|---|---|

## Instrumentation
| Event | Trigger | Properties |
|---|---|---|

## Experiment plan
Hypothesis · primary metric · guardrails · MDE · sample size · runtime (sample ÷ traffic, full weeks) · decision rule
```

---

## Strategy memo

```markdown
# Strategy: <question>: Recommend <X>

## Executive summary
<block: bottom line = X over Y because …; giving up Z>

## Context (5 Cs)
| Company | Customers | Competition | Capabilities | Constraints |
|---|---|---|---|---|

## Options
(see the options matrix below)

## Recommendation
- **Where to play:** <segment/market>
- **How to win:** <advantage (7 Powers type)>
- **First 3 moves:** 1) … (owner, exit criterion) 2) … 3) …
- **Who must align:** <teams + their win>

## Metrics + what would change our mind
```

## Options matrix

| Option | User need (1–5) | Goal fit (1–5) | Our strength (1–5) | Effort | Risk | Score | Verdict |
|---|---|---|---|---|---|---|---|

---

## Decision record (ADR-style; one-way doors)

```markdown
# Decision: <title>: <date>
**Decision:** <one line> · **Owner:** <role> · **Door:** one-way / two-way
**Context:** <2–3 bullets with numbers>
**Options:** A · B · C (one line each)
**Why:** <reason> · **Trade-off accepted:** <…>
**Reverse trigger:** <metric, threshold, milestone>
**Communicated to:** <sales/SAs/customers/…>
```

---

## GTM plan

```markdown
# GTM: <product>: <launch headline>
## Executive summary
<block: bottom line = ICP → positioning → price → channel → stages>

| ICP (first → next) | Pain today | What we fix | Alternative they use |
|---|---|---|---|

**Positioning:** For <who>, <product> is the <category> that <benefit>, unlike <alt>.

**Pricing:** value metric <…> · entry offer <…> · commits <…> · predictability <caps/alerts>

**Channels:** PLG · sales attach · SAs · marketing · partners (who opens which segment)

| Stage | Who | Exit criteria | Target date (user-set, recommended, or TBD) |
|---|---|---|---|
| Allow list | 5 design partners | <…> | |
| Preview | <…> | <…> | |
| GA | <…> | <…> | |

**Metrics:** NSM · funnel · guardrails · **First thing to validate:** <…>
```

---

## Research synthesis

```markdown
# Research: <topic>: <top insight in one line>
| Segment | Size / value | Job (JTBD) | Top pain | Evidence (strength) |
|---|---|---|---|---|
**Chosen segment:** <x>, because <pain × underserved × fits goal>
**Insights** (each: insight → evidence → implication)
**Personas** (≤3, 4 lines each) · **Unknowns + how to learn**
```

## Analysis memo / diagnosis

```markdown
# <Question>: <answer in one line>
Situation → Question → Data + method → Insight → Recommendation + expected result →
Confidence + next check
(Diagnosis: Real? → Where? → Who? → Which step? → hypothesis table)
| Hypothesis | For | Against | Query to confirm | Owner |
```

---

## Vision & roadmap

```markdown
# Vision: "<Product> becomes the default <category> for <segment>."
**Why now:** ≤3 signals (sourced) · **Lead segment:** <…> · **Pain:** <…>
**Pillars:** growth <…> · funnel <…> · base <…>

| Horizon | Outcome | Bets | Milestone / metric |
|---|---|---|---|
| Now | | | |
| Next | | | |
| Later | | | |

**Won't do:** <… → who serves it> · **Key risk:** <…> · **First test:** <…>
```

## PR/FAQ (Working Backwards)

- **Headline**, then a subhead (who it is for and the benefit).
- One paragraph on the problem.
- One paragraph on the solution.
- A customer quote.
- How to get started.
- The external FAQ: about 5 questions.
- The internal FAQ: cost, risks, metrics, why now, and what we are not doing.

## Alignment one-pager

- The shared goal.
- The stakeholder map: decide / affected / can block, plus each team's win metric.
- The problem.
- The options.
- The proposal.
- The asks: team, ask and the milestone it unblocks.
- The boundary: who owns what.
- The escalation path.

---

## sources.md

```markdown
| # | Claim | Source (link) | Date accessed | Confidence |
|---|---|---|---|---|
```

Label any number you computed as **Estimate** and show the arithmetic. Never present a
guess as a sourced fact.
