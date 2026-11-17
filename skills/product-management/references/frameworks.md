# GPM Frameworks

Each section is one way to answer one type of question. Every section gives the numbered
steps, the lines to say aloud in an interview, the traps, and a closing line.

Spoken-answer habits (§10) apply to every section.

**Contents:** §1 Product design · §2 Vision · §3 Analysis & metric diagnosis ·
§4 Metrics & KPIs · §5 Strategy · §6 GTM / 0-to-1 · §7 Pricing · §8 Execution trade-off ·
§9 Cross-org alignment · §10 On the call · §11 "What should X build in 5 years?" ·
§12 Worked-answer pattern

---

## §1 Product design: "Design X for Y" / "Improve X"

1. **Clarify** (30 seconds). Ask about the goal (engagement, revenue or trust), the
   platform and the constraints.
2. **Users.** List 3–4 segments. Include people with varied life experiences:
   accessibility needs, low connectivity, older users, new to tech. Pick one segment and
   say why. A good reason is that they feel the most pain and are underserved.
3. **Pains / jobs.** What is hard for this segment today? Say where the insight would come
   from: research, logs, support tickets or field visits.
4. **Ideas.** Generate 4–6 ideas, including one bold one. Ask what we uniquely have: our
   data, our distribution, our platform, our AI capability.
5. **Prioritize.** Score impact × confidence ÷ effort. Pick 1–2.
6. **Vision + MVP.** Give one line for where this goes, and define what v1 is.
7. **Metrics.** Name a north star, the supporting metrics and a guardrail (see §4).
8. **Risks + learning.** Plan the experiment, the beta and the feedback loop.

**Say:** "Let me take 30 seconds to structure this." · "I'll go users, their pain, ideas,
then pick one and measure it." · "I'll focus on [segment] because they feel the pain
most and it's underserved."

**Example angles:** restaurant search → group decisions and dietary needs · maps →
step-free routes and audio wayfinding · alarm for people with low vision → voice,
haptics, light, works offline.

**Rubric:** start from the user · articulate a vision · combine problem, tech and
business. Close with one line.

---

## §2 Product vision (3–5 years)

1. **Headline + map.** One vision sentence, then name the parts you will cover.
2. **Why now.** Give at most 3 signals, each with its source.
3. **Who.** Describe segments as *buyers*, not as user types. Pick one to lead.
4. **Their pain.** What hurts for that segment today?
5. **What we become.** 2–3 pillars, usually one each for growth, funnel and base.
6. **Roadmap.** Three horizons: Now · Next · Later. Each one is defined by milestones and
   exit criteria, not by durations. Attach calendar ranges only if the user set them.
7. **Metrics.** One north star plus a guardrail.
8. **Won't do + risks.** Non-goals (and who serves them instead), one key risk, and the
   first test.
9. **Close.** Repeat the headline. Ask: "Does that match what you see?"

**Pattern:** "<Product> becomes the default <category> for <segment> on <platform>."
Usually the growth comes from new segments and the base comes from defending existing
revenue.

---

## §3 Product analysis

### A · "Tell me about an analysis that changed a decision"

1. **Situation.** The decision at stake, and why it mattered.
2. **Question.** What we needed to know.
3. **Data + method.** The sources, the interviews, the model built.
4. **Insight.** What surprised us.
5. **Decision + result.** What changed, with a number.
6. **Lesson.** One sentence.

Keep it to 2 minutes or less, with at least 2 numbers. The lesson to aim for: *find the
metric the customer buys on, then model how each roadmap item moves it.*

### B · "Metric X dropped. Why?"

Work top-down. Do not jump to causes.

1. **Is it real?** Check tracking, logging changes, the metric's definition, seasonality,
   day-of-week effects and holidays.
2. **Where?** Internal causes: a launch, a pricing change, an outage, an experiment, a
   change in a dependency. External causes: a competitor, the market, an OS or browser
   update, the news.
3. **Who?** Break it down by segment, region, platform, tier, version, and new versus
   existing users.
4. **Which step?** Walk the funnel step by step to find the step that broke.
5. **Hypothesis → test → fix.** Rank hypotheses by likelihood × ease of checking. Name the
   query that confirms or kills each one.

**Output:** a diagnosis tree, then a hypothesis table (hypothesis · evidence for ·
evidence against · query · owner).

---

## §4 Metrics & KPIs

1. **Goal.** What business or user outcome are we driving?
2. **North star.** One metric that captures the value delivered *and* leads revenue.
3. **Supporting metrics.** 2–3 inputs that move the north star, such as adoption,
   activation or retention.
4. **Guardrails.** What must not get worse: reliability, latency, margin, trust, support
   load.
5. **Leading vs lagging.** What tells us early, and what confirms it later.
6. **Targets + review.** Give the baseline, the target, the review cadence and the kill
   criteria. Write the pass and kill bars *before* the test runs.

**Rules:**

- Never answer with a single number. Always pair the north star with a counter-metric.
- Choose the metric before the roadmap.
- Useful arithmetic: doubling in 3 years needs about 26% growth a year. Revenue =
  customers × spend × retention.

**Example tree (B2B infrastructure):**

- Business: revenue or units under management, and NRR.
- Funnel: time to first value, and the % of eligible accounts that adopt.
- Engagement: weekly active workspaces, eval → production conversion, resume rate, p99
  latency.
- Guardrails: SLO attainment, gross margin per unit, tickets per unit.

See [metrics.md](metrics.md) for definitions, benchmarks and the HEART, GSM and AARRR
frameworks.

---

## §5 Product strategy

**Backbone:** clarify → assess the context → recommend.

1. **Clarify.** Restate the question. Pin down the goal, the time frame, the scope and
   what success looks like.
2. **Assess the context with the 5 Cs:**
   - **Company:** the mission, our assets, and what we uniquely have.
   - **Customers:** the segments, their needs, and who pays.
   - **Competition:** the incumbents, the startups, and the do-it-yourself option.
   - **Capabilities:** our tech, our platform and our team.
   - **Constraints:** margin, reliability, the org, and time.
3. **Options.** Lay out 3 credible paths.
4. **Recommend.** Pick one. Say the trade-off out loud.
5. **Plan.** The first 3 moves, the phasing, and who needs to be aligned.
6. **Metrics + risks.** How we will know it is working, and what would make us change
   course.

**Say:** "I'd pick [X] over [Y] because…, and I'm giving up [Z]." · "If [signal] doesn't
happen by [milestone], I'd reshape the bet."

**Anchors to look for:** gaps in our own docs or guides · what competitors shipped
recently, with dates · features we lack that a rival has.

Pick a side.

---

## §6 Go-to-market / 0-to-1 launch

1. **Market + timing.** Why now? A good answer is often that the defaults are not set yet.
2. **Customer (ICP).** Who comes first, and who comes next. Show the sequence.
3. **Value.** Today's pain → what we fix. Common answers: velocity, TCO, predictability.
4. **Positioning.** "For [who], [product] is the [category] that [benefit], unlike
   [alternative]."
5. **Pricing + packaging.** The value metric, the entry offer, and commits (see §7).
6. **Channels.** Product-led · sales attach · solution architects · marketing · partners.
   A channel only opens after you have a reference customer.
7. **Launch stages.** Allow list → preview → GA. Each stage has exit criteria.
8. **Metrics.** The north star, the funnel and the guardrails.
9. **Risks.** And the first thing to validate.

A typical ramp: 5 design partners → 10 paying customers → self-serve.

---

## §7 Pricing

1. **Value metric.** What grows as the customer gets value? Examples: seats, active
   workspaces, TB, API calls.
2. **Cost floor.** The cost of goods per unit, and the target margin.
3. **Reference prices.** Competitors, and the do-it-yourself alternative.
4. **Willingness to pay.** By segment. What is the TCO story?
5. **Packaging.** Tiers, the entry offer, commits and bundles.
6. **Predictability.** Caps, alerts, and no surprise bills.
7. **Test + iterate.** Price with design partners first, then publish.

**Rules:** Usage-based pricing drives adoption. Commits suit large, stable customers.
Avoid per-operation pricing. Know the cost floor.

**When a customer says "too expensive":** find out which part (capacity, performance or a
minimum size). Then show the TCO including idle costs, right-size the plan, tier the cold
usage, and feed what you learned into the roadmap.

See [toolkit.md](toolkit.md) for Van Westendorp and Gabor-Granger.

---

## §8 Execution trade-off: ship vs slip, scope vs quality

1. **Customer impact.** Who is hurt by each option, and how badly?
2. **Quantify.** Compare the real load to the limit. Use data, not opinion.
3. **SLOs + error budget.** This is the shared language with engineering. When the budget
   is spent, reliability comes first.
4. **Door type.** One-way doors (APIs, durability, the pricing model, data formats) need a
   slow decision. Two-way doors (flags, preview limits) can be decided fast.
5. **Narrow the launch.** Use published limits, quotas and an allow list.
6. **Decide + write it down.** Record the why, the owner and the date.
7. **Communicate.** Sales, solution architects and customers must know the limits.
8. **Reverse trigger.** Name the metric that would change your mind.

**Never negotiable:** durability · security · data integrity. Scope is negotiable.

**Scenarios:**

- GA is in 3 weeks and a component fails at 5× load: go GA with limits if the design
  partners fit inside them, and fix in parallel.
- A noisy neighbor appears before launch: the customer comes first. Delay if the launch
  adds risk.
- Adoption is below plan: read the funnel and fix the biggest drop.

**Life cycle:** idea → allow list → preview → GA → telemetry + feedback → iterate.
Don't ship blind, and don't slip blind.

---

## §9 Cross-org alignment

1. **Shared goal.** The outcome both teams want.
2. **Map the stakeholders.** Who decides, who is affected, and who can block. Use RACI or
   DACI.
3. **Their win.** What is in it for each team, expressed as *their* metric.
4. **Write it down.** A one-pager: the problem, the options, the proposal and the asks.
5. **Bring data.** Customer evidence beats opinion.
6. **Agree the boundary.** Who owns what, and the shared metrics.
7. **Escalate cleanly.** If stuck, escalate together, with options.
8. **Disagree and commit.** Then make it work.

Lesson: pause, explain the why, and bring people with you before you run. Name the team,
the ask and the metric.

---

## §10 On the call: habits for any spoken answer

- **Pause** 30–60 seconds. Then say the framework you will use.
- **Start from the user.** Then the business, then the tech.
- **Pick a side.** Name the trade-off.
- **Use numbers.** At least 2 per story. Say "I", not "we".
- **Keep each story to 2 minutes or less**, then stop.
- **Check in:** "Does that match what you see?"
- **Never guess a fact about your own past. Never bluff about internals:** "I'd go deep
  with engineering on that. Here's how I'd reason about it."
- **Close** each answer with one quotable line. "To summarize: …"
- **Leave 5 minutes** for your own questions.

**STAR+ for behavioral questions:** Situation · Task · Action (I) · Result (number) ·
Lesson.

---

## §11 "What should X build in 5 years?"

This also fits "You're the CEO of X", "X gets $1B, what do you do?", "5-year roadmap for
Z" and "Should X enter market Y?"

1. **Company.** The mission · current investments · strengths to build on · the **goal**
   to optimize for: new users, engagement, monetization, cost, or pure innovation. The
   goal you pick changes the answer.
2. **Ecosystem & opportunities.** The users (chosen by the goal) · their biggest gaps ·
   two trends combined · competitors and how they won. Then list **3–5 opportunity areas**
   and pick one: big user need × serves the goal × uses our strengths. Take a minute of
   silence before picking.
3. **Execution.**
   - The **narrative**: an investor pitch covering who, what gap, and why us.
   - The **roadmap**: Now / Next / Later, with a milestone and exit criteria for each
     step.
   - **Start today**: the first milestone and what unlocks the next one.
   - The **risks**, and how we stop them.

**Say:** "I'll start with what the company cares about, then the market, then how we'd
make it happen." · "I see four opportunities; I'd bet on [X] because it scores highest on
need, goal and strengths."

Options come before the pick.

---

## §12 Worked-answer pattern (combining §11 with §2, §5 and §6)

1. **Company.** The company's bets, its strengths, and a quantified goal, such as
   doubling revenue in 3 years by monetizing the base and winning new workloads.
2. **Ecosystem.** About 6 segments. Lead with the growth segment and defend the base.
   List the gaps (missing tier, bad defaults, absent from key guides), 2 trends, and the
   rivals.
3. **Pick.** Three pillars: growth · funnel · today's revenue. Adjacent ideas become
   features, not pillars.
4. **Execution.** The pitch is the vision headline. Use the three-horizon roadmap. For the
   first milestone, get design partners into production, fix the top funnel defect, and
   launch a migration offer. List the risks, each with a kill check tied to a milestone.
5. **Why A wins.** Need · goal (new spend, not spend shifted from elsewhere) · strength ·
   timing.
6. **Why not C first.** Name the runner-up and why it loses. For example, it shifts spend
   rather than adding it, or it belongs to another team, so partner on it instead.
