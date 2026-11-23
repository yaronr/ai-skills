# Product Knowledge Base (the "product repo")

The product team owns its **memory**. Every run reads from the knowledge base before it
does new research, and files what it learned back into it afterwards. Without this,
research gets redone, decisions get relitigated, and insights end up stranded in chat.

The approach combines several established practices:

- **Docs-as-code:** markdown in git, reviewed through PRs.
- **Atomic research nuggets**, after Tomer Sharon: one insight per file, linked
  to its evidence.
- **Evidence-linked insights**, as in dedicated research-repository tools.
- **Decision logs** in the ADR style of Michael Nygard.
- **Opportunity Solution Trees** (Teresa Torres).
- A split between **evergreen knowledge** and **time-bound initiatives**, borrowed from
  PARA's areas versus projects.

**Contents:** 1 Pick the home · 2 Layout · 3 Document types · 4 Metadata · 5 Workflows ·
6 Hygiene & privacy · 7 Helper script

## 1 · Pick the home (detect, then propose)

**Detect first.** Look for these signals, in this order:

1. A `product.yaml` marker anywhere in the working directory or attached repos.
2. A `product/` or `docs/product/` directory, or folders named `prd`, `research`, `specs`
   or `rfcs`.
3. Loose product documents: PRDs, interview notes, roadmaps and similar, in any format.

**Then choose a mode.** Never create a repo, or move or rename files, without the user's
OK. Show the plan first.

| Situation | Mode | Recommendation |
|---|---|---|
| A KB already exists | **Manage** | Audit it, then propose a reorganization as a move plan. Run `kb.py audit`, apply with `git mv` after approval, never delete, and archive instead. |
| One product, one main repo, and the team works in git | **Embed** | Create `product/` in that repo. Specs then live next to the code and are reviewed in the same PRs. |
| Several repos or products, non-engineering contributors, or sensitive customer data | **Dedicated** | Propose a new **private** repo named `<org>-product` or `<product>-product`. Reference it from each code repo's README. |
| No git at all, or a quick one-off | **Local** | Use `product/` in the working directory, and offer to move it into git later. |

**Make the proposal in 3 lines or fewer:** the mode, why, and what gets created. When
you can't create the repo yourself, for example because the session has no permission to
create repositories, give the exact commands the user needs to run.

## 2 · Layout

```
product/
├── product.yaml            ← marker + config: name, mission, NSM, segments, owners
├── README.md               ← START HERE (≤1 screen): what, who, NSM, current bets, links
├── INDEX.md                ← generated catalog (kb.py index) — don't hand-edit
├── CHANGELOG.md            ← one line per filing: date · what · where
├── glossary.md             ← canonical names for metrics, segments, features
│
├── strategy/               ← EVERGREEN: vision, strategy papers, positioning, OKRs, roadmap.md (living)
├── customers/
│   ├── personas/           ← ≤5 personas, evidence-linked
│   ├── segments.md         ← segment table (size, JTBD, pain, priority)
│   └── accounts/           ← key-account notes (B2B), redacted
├── discovery/
│   ├── research/           ← research plans + syntheses (one folder per study)
│   ├── interviews/         ← interview notes (redacted), one file per interview
│   ├── feedback/           ← feedback digests: support, sales, NPS/CSAT verbatims, reviews
│   ├── insights/           ← ATOMIC insights: one per file, linked to evidence
│   └── opportunities.md    ← opportunity solution tree (outcome → opportunities → solutions)
├── market/                 ← competitors/<name>.md, pricing intel, market sizing, trends
├── analysis/               ← data analyses, metric diagnoses, sizing models (+ queries)
├── experiments/            ← one file per experiment: hypothesis, design, result, decision
├── metrics/                ← metrics spec, definitions (single source), dashboard links
├── decisions/              ← NNNN-title.md decision records (append-only)
├── initiatives/            ← TIME-BOUND work, one folder each:
│   └── 2026-q4-offline-mode/   brief, PRD, stories, GTM, launch, retro
├── launches/               ← release notes, launch checklists (or inside initiatives)
├── meetings/               ← optional: reviews, customer calls (link to insights)
├── templates/              ← copies of the skill's templates for humans
└── archive/                ← superseded docs (never delete; status: superseded)
```

**Why the split:**

- **Evergreen folders** answer "what do we know?" They are updated in place.
- **Initiatives** answer "what did we do and why?" They are frozen after launch.
- **Atomic insights** are the bridge: initiatives cite them, and they cite their evidence.

**Scale.** A small team can drop `meetings/`, `launches/` and `accounts/`. Don't create
an empty folder until there is something to put in it, apart from the core: `strategy`,
`discovery`, `decisions` and `initiatives`.

## 3 · Document types

| Type (`type:`) | Folder | Template (templates.md) | Lifecycle |
|---|---|---|---|
| `vision`, `strategy`, `positioning`, `okr`, `roadmap` | strategy/ | Vision & roadmap · Strategy paper · Positioning paper | Living. Review quarterly. |
| `persona`, `segment` | customers/ | Research paper | Living. Review every 6 months. |
| `research-plan`, `research-synthesis` | discovery/research/<study>/ | Research paper | Frozen after synthesis |
| `interview` | discovery/interviews/ | (see below) | Frozen |
| `feedback-digest` | discovery/feedback/ | (see below) | Monthly or per source |
| `insight` | discovery/insights/ | (see below) | Living. Confidence changes as evidence arrives. |
| `competitor`, `market` | market/ | Market analyst output | Living. Date every fact. |
| `analysis`, `diagnosis`, `sizing` | analysis/ | Analysis / diagnosis paper | Frozen |
| `experiment` | experiments/ | Experiment plan (metrics spec) | Planned → running → concluded |
| `metrics-spec`, `metric-definition` | metrics/ | Metrics spec | Living. This is the single source of truth. |
| `decision` | decisions/ | Decision record | Append-only. Supersede it, never edit it. |
| `brief`, `prd`, `user-stories`, `gtm`, `launch`, `retro` | initiatives/<slug>/ | Brief · PRD · Stories · GTM | Draft → review → approved → shipped |

**Atomic insight** (`discovery/insights/<slug>.md`):

```markdown
---
type: insight
title: Techs re-type notes from paper after losing signal
confidence: high        # high = ≥3 independent sources · medium = 2 · low = 1/anecdote
segments: [field-tech]
tags: [offline, data-loss]
evidence: [../interviews/2026-10-02-c017-field-tech.md, ../feedback/2026-10-support.md]
---
**Insight:** <one sentence>
**Evidence:** <2–4 bullets with links>
**So what:** <implication for product>
```

**Interview note:** front matter (date, participant code, segment, interviewer), then a
one-line bottom line (the most important thing learned), the context, the key quotes (verbatim), the observations, the jobs and pains, and links
to the insights it informs. Use participant **codes**, not names.

**Feedback digest** (one per source per period). Open with an executive summary (≤1
page): bottom line, the top 3 themes with counts and trend, and the recommended actions.
Then the body:

- The volume.
- The top themes, as a table: theme · count · trend · example quotes · linked insight.
- New themes.
- Recommended actions.

Use one stable **theme taxonomy**, defined in `glossary.md`, so that trends can be
compared from month to month.

## 4 · Metadata (front matter on every file)

```yaml
---
type: prd                 # from the table above
title: Offline mode PRD
status: draft             # draft | review | approved | shipped | superseded | archived
owner: pm                 # role or handle
created: 2026-11-17
updated: 2026-11-17
review_by: 2027-02-17     # evergreen docs only; triggers staleness lint
initiative: 2026-q4-offline-mode   # if applicable
segments: [field-tech]
tags: [offline, sync]
supersedes: []            # paths
sources: [sources.md#3]   # or links
---
```

**Naming conventions:**

- Use `kebab-case`.
- Dated artifacts start with the date: `2026-11-17-…`.
- Decision records are numbered: `0007-…`.
- Initiatives are named `<yyyy>-q<n>-<slug>`.

## 5 · Workflows

**Brief the product team before it researches** (product-management Phase 1–2):

1. Read `README.md`, `product.yaml`, `glossary.md`, the related `insights/`, the
   `decisions/`, and the latest `strategy/` documents.
2. Pass the relevant paths to each subagent.
3. Tell agents that internal evidence beats web evidence.
4. Use the glossary names, the NSM and the segments exactly as written.
5. Never contradict an `approved` decision silently. Either follow it, or propose a
   superseding decision that gives the new evidence.

**File the team's output** (product-management Phase 6):

1. Put deliverables in `initiatives/<yyyy>-q<n>-<slug>/`. This replaces
   `product-work/` whenever a KB exists. Don't file `_work/` (the storyline and claim
   notes): it is scratch.
2. Extract each new **insight** into `discovery/insights/`, and each new **decision**
   into `decisions/NNNN-…`.
3. Put competitor facts in `market/competitors/`, and metric definitions in `metrics/`.
4. Update the living documents (roadmap, segments, opportunities) **in place**. Note
   each change in `CHANGELOG.md`.
5. Run `kb.py index` and `kb.py lint`. Fix any errors.
6. Commit the changes on a branch with a clear message. Open a PR if the repo uses PRs.

**Ingest raw input** when the user drops in notes, transcripts, tickets, CSVs or survey
exports:

1. Classify each item. Redact personal data.
2. File each one in the right place.
3. Extract atomic insights, and link each to its evidence.
4. Update the confidence of any existing insight it affects.
5. Report back: "Filed N items, M new insights, K updated", plus the top 3 changes.

**Ask the KB** ("what do we know about X?"):

- Search the front matter and the text.
- Answer with links, and say how confident you are.
- Name the gaps, and what research would close them.

## 6 · Hygiene & privacy

- **No PII in git.**
  - Replace names, emails and phone numbers with participant or account codes.
  - Keep the key that maps codes to people outside the repo, in the CRM or research tool.
  - Link to recordings. Never commit them.
- **Customer-confidential material** (contracts, pricing deals) belongs in a dedicated
  **private** repo, never an embedded one in a public repo. Flag any public repo before
  filing into it.
- **Staleness.**
  - `kb.py lint` flags evergreen docs past their `review_by` date.
  - It flags `market/` facts older than 6 months.
  - It flags insights with low confidence and no evidence links.
- **One source of truth.** Each metric is defined in exactly one place, in `metrics/`.
  Every other document links to that definition.
- **Supersede, don't edit history.** For decisions and frozen docs, write a new document
  with `supersedes:`. Set the old one's status to `superseded`.

## 7 · Helper script

`scripts/kb.py` uses only the Python standard library. Call it by the skill's own
folder (`<skill-dir>/scripts/kb.py`), not a path relative to the user's project.

| Command | Does |
|---|---|
| `python3 <skill-dir>/scripts/kb.py init <root> --name "<Product>"` | Scaffolds the core folders, `product.yaml`, README, glossary and CHANGELOG. Skips any file that already exists. |
| `python3 <skill-dir>/scripts/kb.py index <root>` | Rebuilds `INDEX.md`, grouping documents by type, then status, then recency. |
| `python3 <skill-dir>/scripts/kb.py lint <root>` | Reports missing front matter, unknown types or statuses, stale docs, broken relative links, and `evidence`/`supersedes`/`sources` paths that don't exist. |
| `python3 <skill-dir>/scripts/kb.py audit <src> --kb <root> [--out plan.md]` | Classifies the files under `<src>` and writes a runnable **move plan** into the KB at `<root>` (`mkdir -p` + `git mv`, paths relative to where you run it). Moves into `initiatives/` wait for you to pick the folder. Notes that contain a decision stay put and are listed for a new decision record. It never moves anything itself. |
