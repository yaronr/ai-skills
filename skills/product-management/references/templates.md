# Templates

Every document follows the [writing standard](writing-standard.md):

- the executive summary block (§3) first;
- claim headings, each followed by a `*Lens: …*` line (§4);
- the skim layer (§5);
- `## Appendix` last.

The templates below show the body that comes after the summary. `<claim: …>` means "write
a full-sentence claim about this", never the topic label itself.

Delete any section that does not apply. Don't pad a section to fill it.

**Contents:** 00 Brief · Research paper · Analysis / diagnosis paper · Strategy paper ·
Options matrix · Vision & roadmap · Positioning paper · GTM plan · PRD · User stories ·
Metrics spec · Decision record · PR/FAQ · Alignment one-pager · sources.md

---

## 00 · Brief = the package's executive summary (always included)

`00-brief.md` is the executive summary block for the whole package (writing standard §3),
plus these two parts. The **whole file** is ≤400 words.

```markdown
| Goal | North star | Guardrail | First milestone |
|---|---|---|---|
| <growth/engagement/…> | <metric + target> | <metric + limit> | <what · gate> |

📂 **Read next:** 01-research (why) · 02-strategy (what we bet) · 03-prd (what we build) · …
```

---

## Research paper

Answers: who has the problem, how badly, and what it means for us.

```markdown
# <The top insight, as the answer>

## Executive summary
<block>

## <claim: which segment hurts most, and why that one is ours>
*Lens: segments × JTBD (frameworks §1)*
| Segment | Size / value | Job (JTBD) | Top pain | Evidence (strength) |
|---|---|---|---|---|

## <claim: the pain that matters most, with its size>
*Lens: switching forces (push, pull, anxiety, habit)*

## <claim: what this means for the product>
*Lens: insight → evidence → implication*

## <claim: what we still don't know, and how we'll learn it>
❓ <unknown> → <interview question / log query / survey item>

> <quotable line>

## Appendix
Personas (≤3, 4 lines each) · raw evidence · method
```

## Analysis / diagnosis paper

Answers "should we do X?" (frameworks §3A) or "why did metric X move?" (§3B).

```markdown
# <Question>: <answer, or "not yet known: run N checks in order">

## Executive summary
<block>

## <claim: whether the change is real>
*Lens: data-quality checks (frameworks §3B step 1)*

## <claim: where the change sits>
*Lens: metric tree + segment decomposition*
<metric tree exhibit · decomposition table with each slice's share of the change>

## <claim: the most likely causes, ranked>
*Lens: ranked hypothesis table*
| # | Hypothesis | For | Against | Check (one line) | Owner |
|---|---|---|---|---|---|

## <claim: what we do first, and what result would change the call>
*Lens: key judgments + signals to watch*

> <quotable line>

## Appendix
Queries (SQL / pseudo-SQL) · sizing arithmetic · traps considered
```

---

## Strategy paper

Answers: where we play, how we win, and what we bet first.

```markdown
# <Recommend X: the bet in ≤12 words>

## Executive summary
<block: bottom line = X over Y because …; giving up Z>

## <claim: what is really going on (the diagnosis)>
*Lens: 5 Cs (frameworks §5) + Rumelt diagnosis*
| Company | Customers | Competition | Capabilities | Constraints |
|---|---|---|---|---|

## <claim: the three real options, and why X wins>
*Lens: options matrix*
<options matrix below>

## <claim: where we play and how we win>
*Lens: where to play / how to win · 7 Powers*
- **Where to play:** <segment / market>
- **How to win:** <advantage, and its 7 Powers type: real today or aspirational>

## <claim: the guiding policy and the first coherent moves>
*Lens: Rumelt guiding policy → coherent actions*
1) <move> (owner, exit criterion) 2) … 3) …

## <claim: how we'll know, and what would change our mind>
*Lens: NSM + guardrail · reverse trigger*

> <quotable line>

## Appendix
Who must align (teams + their win) · scoring detail · sources of the 5 Cs facts
```

## Options matrix

Title the exhibit with its message, e.g. "B wins on goal fit; C's payment scope is a
one-way door".

| Option | User need (1–5) | Goal fit (1–5) | Our strength (1–5) | Effort (S/M/L) | Risk | Score | Verdict |
|---|---|---|---|---|---|---|---|

## Vision & roadmap

```markdown
# Vision: "<Product> becomes the default <category> for <segment>."

## Executive summary
<block>

## <claim: why now>
*Lens: why-now signals (≤3, sourced)*

## <claim: the lead segment and its pain>
*Lens: segments × JTBD*

## <claim: the pillars that get us there>
*Lens: growth · funnel · base pillars (frameworks §2)*

## <claim: how the bets sequence>
*Lens: Now / Next / Later*
| Horizon | Outcome | Bets | Milestone / metric |
|---|---|---|---|

## <claim: what we won't do, and who serves it>

> <quotable line>
```

---

## Positioning paper

Answers: who it's for, what it beats, and why it wins. Body ≤1,200 words.

```markdown
# <Product> wins <best-fit customer> because <unique value>

## Executive summary
<block>

## <claim: what customers use today instead>
*Lens: competitive alternatives (including "do nothing" and DIY)*
| Alternative | Who uses it | Why they pick it | Where it fails them |
|---|---|---|---|

## <claim: what only we have>
*Lens: unique attributes → value (Dunford)*
| Unique attribute | Value it creates | Proof |
|---|---|---|

## <claim: who cares most about that value>
*Lens: best-fit customer + JTBD · ICP sequence (frameworks §6)*

## <claim: the frame that makes the value obvious>
*Lens: market category (head-on · sub-category · new)*

## <claim: the message, in one line, and its proof>
*Lens: messaging hierarchy*
**Positioning:** For <who>, <product> is the <category> that <value>, unlike <alternative>.
| Message level | Message | Proof point |
|---|---|---|
| Headline | | |
| Pillar 1–3 | | |

> <quotable line>

## Appendix
Customer quotes · competitor messaging captured (dated) · rejected framings and why
```

## GTM plan

```markdown
# GTM: <product>: <launch headline>

## Executive summary
<block: bottom line = ICP → positioning → price → channel → stages>

## <claim: who buys first, and who next>
*Lens: ICP sequence (frameworks §6)*
| ICP (first → next) | Pain today | What we fix | Alternative they use |
|---|---|---|---|

## <claim: the positioning, in one line>
*Lens: positioning statement (full detail: 02b-positioning)*

## <claim: how we charge>
*Lens: value metric · packaging (frameworks §7)*

## <claim: which channel opens which segment>
*Lens: channel → reference customer*

## <claim: how the launch stages>
*Lens: launch stages with exit criteria*
| Stage | Who | Exit criteria | Target date (user-set, recommended, or TBD) |
|---|---|---|---|
| Allow list | 5 design partners | <…> | |
| Preview | <…> | <…> | |
| GA | <…> | <…> | |

## <claim: the first thing to validate>

> <quotable line>
```

---

## PRD

Answers: what we build first, and how we know it works. Strategy lives in 02; link it.

```markdown
# PRD: <feature>: <one-line outcome>

Status: Draft · Owner: PM · Updated: <date> · Strategy: [02-strategy](02-strategy.md)

## Executive summary
<block: bottom line = problem → solution → metric>

## <claim: who hurts, how much, and the cost of inaction>
*Lens: problem + JTBD (frameworks §1)*

## <claim: what success is, and what we deliberately won't do>
*Lens: goals / non-goals*
| Goals (measurable) | Non-goals (and who handles them) |
|---|---|

## <claim: the smallest product that delivers the goal>
*Lens: MVP scope (RICE / MoSCoW)*
- **<capability>:** <user value>
- **Not in v1:** <…>

## <claim: the journeys that must work>
*Lens: key flows*
1. <step> → <step> → <outcome>   (designer artifact)

## <claim: what must be true for users to trust it>
*Lens: requirements + one-way doors*
| ID | Requirement | Priority (P0/P1/P2) | Notes |
|---|---|---|---|

## <claim: how we'll know it works>
*Lens: NSM + drivers + guardrail (see 05-metrics)*

> <quotable line>

## Appendix
Non-functional detail (SLO, security & privacy, WCAG 2.2 AA, i18n, cost per unit) ·
technical notes · launch stages (see 06-gtm or eng rollout)
```

## User stories

No body cap. Group the stories into **epics** in story-map order. Release 1 is the walking
skeleton. Open the file with a short executive summary: how many stories, what release 1
covers, and the riskiest story. For each story:

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

## Metrics spec

```markdown
# Metrics: <product/feature>: <the one metric that matters, and its target>

## Executive summary
<block>

## <claim: the north star, and why it leads revenue>
*Lens: metric tree*
NSM
├─ Driver A (leading) → team <x>
├─ Driver B → team <y>
└─ Driver C
Guardrails: <reliability> · <margin> · <trust>

## <claim: how we'll test the riskiest assumption>
*Lens: experiment design (frameworks §4)*
Hypothesis · primary metric · guardrails · MDE · sample size · runtime (sample ÷ traffic,
full weeks) · decision rule

> <quotable line>

## Appendix
| Metric | Formula | Unit · window | Baseline | Target (by milestone) | Cadence | L/L | Kill criterion |
|---|---|---|---|---|---|---|---|
HEART / GSM rows (if UX-heavy) · instrumentation events
```

---

## Decision record (ADR-style; one-way doors)

Short enough to need only a bold bottom line, no full summary block.

```markdown
# Decision: <title>: <date>
**<The decision, in one bold line.>** · Owner: <role> · Door: one-way / two-way
**Context:** <2–3 bullets with numbers>
**Options:** A · B · C (one line each)
**Why:** <reason> · **Trade-off accepted:** <…>
**Reverse trigger:** <metric, threshold, milestone>
**Communicated to:** <sales/SAs/customers/…>
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

The table only: no executive summary, no claim sections, no appendix.

```markdown
| # | Claim | Source (link) | Date accessed | Confidence |
|---|---|---|---|---|
```

Label any number you computed as **Estimate** and show the arithmetic. Never present a
guess as a sourced fact.
