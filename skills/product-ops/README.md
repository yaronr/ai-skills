# product-ops

This skill acts as a Product Operations Manager. It runs the **product knowledge base**,
the "product repo", where every kind of product document lives: research, interviews,
customer feedback, atomic insights, competitive intel, analyses, experiments, metric
definitions, decisions, PRDs, roadmaps and launches.

## Use

- "Set up a product repo for this project"
- "Our product docs are a mess. Organize them."
- "Here are 40 support tickets and 6 interview transcripts. File them and pull out insights."
- "What do we know about churn in SMB accounts?"
- It also runs automatically from **product-management**, which calls it for a *Brief*
  before a run and to *File deliverables* after.

## Where the KB lives (it always proposes first, and asks before acting)

| Mode | When |
|---|---|
| **Manage** | A KB already exists (`product.yaml`, `product/`, `docs/product/`) |
| **Embed** | One product and one main repo: `product/` sits next to the code |
| **Dedicated** | Several repos or products, non-engineering contributors, or sensitive data: a new private repo |
| **Local** | No git yet |

## Layout (summary)

`strategy/` · `customers/` · `discovery/{research,interviews,feedback,insights}` ·
`market/` · `analysis/` · `experiments/` · `metrics/` · `decisions/` ·
`initiatives/<yyyy>-q<n>-<slug>/` · `archive/`, plus `README.md`, `INDEX.md`
(generated), `glossary.md` and `CHANGELOG.md`.

The full spec is in [references/knowledge-base.md](references/knowledge-base.md).

## Helper script

```bash
python3 scripts/kb.py init  product --name "My Product"
```
```bash
python3 scripts/kb.py audit docs --out plan.md
```
```bash
python3 scripts/kb.py index product
```
```bash
python3 scripts/kb.py lint  product
```

- `init` scaffolds the KB.
- `audit` proposes `git mv` lines and never moves anything itself.
- `index` regenerates `INDEX.md`.
- `lint` checks metadata, staleness, broken links and PII.

## Practices it draws on

- Docs-as-code.
- Atomic research nuggets.
- Evidence-linked insights.
- ADR-style decision logs.
- Opportunity solution trees.
- Evergreen knowledge kept separate from time-bound initiatives.
