# product-management

This skill turns a product question into the output of a whole product team. A Group
Product Manager (GPM) runs the team as orchestrator, and specialist subagents do the
research, analysis and writing. Every document it produces opens with an executive
summary of one page at most: the bottom line first, then the findings, then what to do.

## Use

Ask any product question. You don't need to name the skill. Examples:

- "Should we add a free tier to our API product?"
- "Write a PRD and user stories for offline mode in our field-service app"
- "DAU dropped 8% week over week. Why?"
- "What should our music-streaming app build in the next 5 years?"
- "Revise our offline-mode PRD based on this eng and sales feedback"

## How it works

| Phase | Who | What |
|---|---|---|
| 0 Setup check | GPM | Picks a tier (Quick, Standard or Full). Recommends the orchestrator's model and effort, and whether to use ultracode. |
| 1 Frame | GPM | Restates the question, names the goal, makes assumptions, routes to a framework |
| 2 Discover | user-researcher · market-analyst · data-analyst · strategist | Segments and JTBD, why now and competitors, sizing and metrics, options |
| 3 Decide | GPM | Lays out 3 options → 1 pick, with the trade-off and a reverse trigger |
| 4 Define | pm-writer · eng-lead · designer · gtm-lead · data-analyst | PRD, user stories, feasibility and risks, flows and the visual artifact, GTM, metrics spec |
| 5 Review | red-team (Opus) · editor (Haiku) | A fresh-eyes critique, then a style and consistency pass |
| 6 Package | GPM → product-ops | Files the work into the knowledge base (or into `product-work/`) and builds an HTML artifact |

**Model tiering.** Opus handles the judgment-heavy roles: strategy, numbers and red-team
review. Sonnet handles the research and writing roles. Haiku handles the mechanical
editing pass.

## Contents

```
SKILL.md              orchestration, routing, writing rules, quality bar
references/
  frameworks.md       §1–§12 GPM frameworks (design, vision, analysis, metrics, strategy, GTM, pricing, trade-offs, alignment, 5-year)
  metrics.md          metric definitions, formulas, benchmarks, traps; HEART, GSM, NSM, AARRR, PMF
  toolkit.md          JTBD, OST, RICE, Kano, Playing to Win, 7 Powers, pre-mortem, A/B tests, PR/FAQ…
  templates.md        brief, PRD, user stories, metrics spec, strategy memo, GTM, decision record, roadmap
agents/               subagent role briefs (+ _common.md)
evals/                test cases (claude plugin eval layout)
```

## Companion skill

**[product-ops](../product-ops)** is the team's memory. Before a run it briefs the team
from the product knowledge base. After the run it files the deliverables, insights and
decisions. Install both.

## Optional dependency

**[ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** is used to
style the visual artifacts. If it is not installed, the skill falls back to the
`artifact-design` skill or to clean default styling.

## Sources

The frameworks are working playbooks built from GPM practice and a metrics reference.
They are extended with established practice: HEART/GSM, Cagan, Torres, Lafley &
Martin, Rumelt, Helmer, Working Backwards (PR/FAQ), INVEST and Gherkin.
