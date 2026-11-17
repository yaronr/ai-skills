# PM Toolkit

These are extra frameworks beyond the core cards. Pick the one that fits the question.
Don't use a framework for its own sake.

**Contents:** Discovery · Prioritization · Strategy · Decisions & risk · Pricing research ·
Experimentation · Delivery

## Discovery: what problem, for whom

- **Jobs to Be Done (JTBD).** Write the job as: "When [situation], I want to [motivation],
  so I can [outcome]." Map the **forces of progress**: push from the current way, pull of
  the new solution, anxiety about the new, and habit of the old. People switch only when
  push + pull > anxiety + habit.
- **Opportunity Solution Tree (Teresa Torres).** Work top-down: outcome → opportunities
  (needs and pains, taken from interviews) → solutions → assumption tests. Compare
  solutions only within one opportunity. Use the tree to stop "feature factory" roadmaps.
- **Continuous discovery.** Talk to customers weekly. Interview about *past behavior*
  ("tell me about the last time…"), never about future intent.
- **The four big risks (Cagan).** Check each idea for value (will they buy or use it?),
  usability (can they?), feasibility (can we build it?) and viability (does it work for
  the business?). Test the riskiest one first.
- **Evidence sources.** Interviews · support tickets · logs and funnels · sales call notes ·
  community forums · reviews of competitors · field visits. Rate each piece of evidence as
  strong, medium or weak.

## Prioritization

- **RICE** = Reach × Impact (3, 2, 1, 0.5 or 0.25) × Confidence (100%, 80% or 50%) ÷
  Effort (person-months). Show the inputs so the scores can be argued with.
- **ICE** = Impact × Confidence × Ease, each scored 1–10. Faster than RICE. Good for
  growth experiments.
- **Impact × confidence ÷ effort.** A quick version when inputs are rough.
- **Kano model.** Sort features into must-haves (their absence causes anger),
  performance features (more is better) and delighters (unexpected joy). A product needs
  all the must-haves before it adds delighters.
- **MoSCoW.** Must, Should, Could, Won't. Use it to agree scope with stakeholders, not to
  set strategy.
- **Cost of delay / WSJF.** (Business value + time criticality + risk reduction) ÷ job
  size. Use it when timing matters.
- **Need × goal × strength.** For choosing between opportunity areas (frameworks §11).

## Strategy

- **Playing to Win (Lafley & Martin).** Five questions: winning aspiration → where to
  play → how to win → required capabilities → management systems. The two that matter
  most are *where to play* and *how to win*.
- **Rumelt's kernel.** Good strategy has three parts: a diagnosis (what is going on), a
  guiding policy (our approach) and coherent actions. Bad strategy is a list of goals with
  no diagnosis.
- **7 Powers (Helmer).** The sources of durable advantage: scale economies, network
  effects, counter-positioning, switching costs, branding, cornered resource and process
  power. Name which one you are building.
- **5 Cs.** Company, customers, competition, capabilities, constraints. See frameworks §5.
- **Porter's five forces.** Use it for questions about entering a market: buyer power,
  supplier power, substitutes, new entrants and rivalry.
- **Wardley mapping.** Map the value chain against evolution (genesis → custom → product
  → commodity). Build what differentiates you. Buy or rent commodities.
- **Platform vs product.** Ask who the developers or partners are, what the interfaces are,
  and how each side gets value.
- **Build / buy / partner.** Compare time to market, control, cost, and whether the
  capability is core.
- **Crossing the chasm.** Win one beachhead segment completely before expanding.
  References from that segment open the next one.

## Decisions & risk

- **One-way vs two-way doors.** Make reversible decisions fast and at a low level.
  Irreversible decisions need slow, senior review.
- **Pre-mortem.** "It's after launch and this failed. Why?" List the causes. Each
  big cause needs a mitigation or a tripwire.
- **Reverse trigger / kill criteria.** Write these down before launch. Name the metric,
  the threshold and the milestone.
- **DACI / RAPID.** Name who **D**rives or **D**ecides, who **A**pproves, who
  **C**ontributes and who is **I**nformed. Name exactly one decider.
- **Disagree and commit.** Once the decision is made, everyone executes fully.
- **Assumption mapping.** Plot each assumption by importance against evidence. Test the
  ones that are important and have little evidence.

## Pricing research

- **Van Westendorp.** Ask four questions: what price is too cheap, cheap, expensive, and
  too expensive? The acceptable price range is where the curves cross.
- **Gabor-Granger.** Ask about purchase intent at successive price points, then derive a
  demand curve.
- **Conjoint analysis.** Measures trade-offs between features and price. Use it for
  packaging decisions.
- **Good / better / best tiers.** Anchor with the top tier. Most buyers pick the middle.
- **Value metric.** The thing the price scales with should scale with the value the
  customer gets.

## Experimentation

- **Hypothesis format:** "We believe [change] for [segment] will move [metric] by [X] because
  [insight]. We'll know when [result] at [sample size / milestone]."
- **A/B basics.** Fix the primary metric and the guardrails before the test starts.
  Calculate the sample size (MDE, α = 0.05, power = 0.8). Run for at least one full
  business cycle. Do not peek at results early.
- **Fake door / painted door / concierge / Wizard of Oz.** Ways to test demand before you
  build.
- **Staged rollout.** Internal → allow list → 1% → 10% → 50% → GA. Each stage needs exit
  criteria.

## Delivery

- **INVEST user stories.** Each story is Independent, Negotiable, Valuable, Estimable,
  Small and Testable.
- **Acceptance criteria in Gherkin:** `Given … When … Then …`. Cover the happy path, the
  edge cases and the error states.
- **Story mapping (Patton).** Lay out the user activities left to right, then the tasks
  under each activity. Draw horizontal release slices. The first slice is the walking
  skeleton.
- **Shape Up.** Fixed time, variable scope. Shape the work, place bets in six-week
  cycles, and use appetite rather than estimates.
- **Now / Next / Later roadmap.** Organize it around outcomes, not dates. Confidence falls
  the further right you go.
- **Working Backwards (PR/FAQ).** Write the press release and the FAQ before
  building. If the press release isn't exciting, don't build it.
- **Definition of Done.** Each item includes instrumentation, docs, support readiness,
  accessibility review, privacy review and a launch checklist.
