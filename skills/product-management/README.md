# product-management

This skill turns a product question into the output of a whole product team. A Group
Product Manager (GPM) runs the team as orchestrator, and specialist subagents do the
research and analysis. Each document answers one question at one level (research,
strategy, positioning, PRD, metrics). It opens with a one-page executive summary, argues
through claim headings, shows its GPM frameworks as exhibits, and can be skimmed through
bold lead-ins, confidence markers and callouts.

## Use

Ask any product question. You don't need to name the skill. Examples:

- "Should we add a free tier to our API product?"
- "Write a PRD and user stories for offline mode in our field-service app"
- "DAU dropped 8% week over week. Why?"
- "What should our music-streaming app build in the next 5 years?"
- "Write a positioning paper for our open-source observability tool"
- "Revise our offline-mode PRD based on this eng and sales feedback"

## How it works

| Phase | Who | What |
|---|---|---|
| 0 Setup check | GPM | Picks a tier (Quick, Standard or Full). Recommends the orchestrator's model and effort, and whether to use ultracode. |
| 1 Frame | GPM | Restates the question, names the goal, makes assumptions, routes to a framework |
| 2 Discover | user-researcher · market-analyst · data-analyst · strategist | Segments and JTBD, why now and competitors, sizing and metrics, options |
| 3 Decide | GPM | Lays out 3 options → 1 pick, with the trade-off and a reverse trigger |
| 3.5 Storyline | GPM or strategist (+ red-team on Full) | Per document: the question, the answer, 3–5 claims with their lenses |
| 4 Define | eng-lead · designer · gtm-lead · data-analyst → pm-writer | Specialists write claim notes; the pm-writer is the single author of every document; the designer builds the visual artifact |
| 5 Review | red-team (Opus) · editor (Sonnet) | A fresh-eyes critique, then the heading-only, level and lens tests, the skim layer and a 30% cut |
| 6 Package | GPM → product-ops | Files the work into the knowledge base (or into `product-work/`) and builds an HTML artifact |

**Model tiering.** Opus handles the judgment-heavy roles: strategy, numbers, writing the
documents and red-team review. Sonnet handles research, specialist notes and the editing
pass.

## Contents

```
SKILL.md              orchestration, routing, writing rules, quality bar
references/
  frameworks.md       §1–§12 GPM frameworks (design, vision, analysis, metrics, strategy, GTM, pricing, trade-offs, alignment, 5-year)
  metrics.md          metric definitions, formulas, benchmarks, traps; HEART, GSM, NSM, AARRR, PMF
  toolkit.md          JTBD, OST, RICE, Kano, Playing to Win, 7 Powers, pre-mortem, A/B tests, PR/FAQ…
  writing-standard.md one question per doc, storyline, executive summary, claim headings, skim layer, required lenses, caps
  templates.md        brief, research, analysis, strategy, positioning, GTM, PRD, user stories, metrics, decision record, roadmap
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
Martin, Rumelt, Helmer, Dunford, Working Backwards (PR/FAQ), INVEST and Gherkin. The
writing standard draws on Minto's Pyramid Principle, the narrative memo and ICD 203
analytic standards.
