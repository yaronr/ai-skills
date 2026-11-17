# Product Metrics Reference

**Golden rule:** never give one number alone. Pair a north star with a counter-metric
(guardrail). For example, adoption velocity must be balanced against error rate and
support volume. Aggressive monetization must be guarded by NRR and cohort retention.

**Contents:** 1 Sentiment · 2 Engagement & retention · 3 Unit economics · 4 Growth & funnel ·
5 Frameworks (HEART, GSM, NSM, AARRR, PMF) · 6 Metric-spec checklist · 7 Common traps

## 1 · Customer sentiment & experience

| Metric | Formula | Use | Trap / GPM view |
|---|---|---|---|
| **CSAT** | Positive ratings ÷ total × 100 | Ask right after an interaction (checkout, ticket closed, new flow). Target is above 80%. | High CSAT does not mean retention. It measures how the interaction felt, not whether the product became a habit. |
| **NPS** | % promoters (9–10) − % detractors (0–6) | Measure quarterly or twice a year. Predicts word of mouth. Ranges from −100 to +100. | It has no tactical detail. When NPS drops, you need qualitative follow-up or CSAT to learn *why*. |
| **CES** | Sum of ratings ÷ responses (scale of 1–7) | Use it for setup, onboarding and admin flows. | Reducing effort often does more for retention than new top-of-funnel features. |

## 2 · Engagement & retention

| Metric | Formula | Use | Trap / GPM view |
|---|---|---|---|
| **DAU/MAU (stickiness)** | DAU ÷ MAU | Shows habit formation. Benchmarks: B2B SaaS above 20%, consumer social above 50%. | Define "active" as doing the core action. Logging in does not count. |
| **Cohort retention** | Users active in month N ÷ users in the starting cohort × 100 | Plot it as a curve. If the curve flattens, that is evidence of product-market fit. If it slopes toward 0, the bucket is leaking. | Fix retention before you spend on acquisition. |
| **L-ness (L7/L28)** | Number of active days in the window | Shows how intense use is, not just whether users show up. | Use a histogram. The mean hides power users. |
| **Feature adoption** | Users of the feature ÷ eligible users | Shows whether a launch succeeded. | Adoption without repeat use is curiosity, not value. |

## 3 · Unit economics

| Metric | Formula | Use | Trap / GPM view |
|---|---|---|---|
| **NRR** | (Starting ARR + expansion − contraction − churn) ÷ starting ARR | The key growth indicator for enterprise SaaS. Good is above 110%. Best in class is above 130%. | High NRR protects you when new-customer acquisition slows. |
| **GRR** | (Starting ARR − contraction − churn) ÷ starting ARR | Shows the true floor of retention. Good is above 90%. | It cannot exceed 100%. Expansion inside NRR can hide churn, and GRR exposes it. |
| **LTV:CAC** | LTV ÷ CAC. The target is 3:1 to 4:1. | Shows how efficient go-to-market is. | A high CAC is fine during a land grab if retention is proven. It is fatal if churn is unfixed. |
| **CAC payback** | CAC ÷ (monthly ARPA × gross margin) | Below 12–18 months is good. | Bundling services into CAC distorts the number. |
| **Gross margin** | (Revenue − COGS) ÷ revenue | Above 70% is typical for SaaS. Infrastructure and AI products run lower. | AI inference cost can quietly destroy margin. Track it per unit. |
| **Burn multiple** | Net burn ÷ net new ARR | Below 1.5 is efficient. | Use it for 0-to-1 bets inside larger companies too. |
| **Rule of 40** | Growth % + profit margin % ≥ 40 | Health of a mature SaaS business. | Not meaningful in the early stage. |

## 4 · Growth & funnel

- **Activation rate:** the share of new users who reach the "aha" action within N days.
  This is the strongest early signal of retention.
- **Time to first value (TTFV):** the median time from signup to the first core outcome.
- **Conversion rate per step:** always show the absolute numbers next to the percentages.
- **Viral coefficient (K):** invites per user × invite conversion rate. A K above 1 means
  the product grows on its own.
- **Quick ratio (SaaS):** (new MRR + expansion MRR) ÷ (churned MRR + contraction MRR).
  Above 4 is strong.

## 5 · Frameworks

### HEART (UX quality of a product or suite)

| Dimension | Meaning | Example signals |
|---|---|---|
| **Happiness** | Satisfaction | CSAT, NPS, survey sentiment |
| **Engagement** | Depth of use | Frequency, intensity, duration |
| **Adoption** | New use | New users, uptake of a feature or upgrade |
| **Retention** | Repeat use | Cohort return rate, churn |
| **Task success** | Efficiency | Completion rate, time on task, error rate, CES |

Combine HEART with **Goals → Signals → Metrics (GSM)**. For each dimension you keep:

1. Write the goal: what the user achieves.
2. Name the signal: which behavior would show the goal was met.
3. Define the metric: the exact formula.

Drop any dimension that does not matter for this product.

### North Star Metric (NSM)

The NSM is the one metric that captures the value delivered to users *and* leads revenue.

| Product type | Example NSM |
|---|---|
| B2B collaboration | Messages sent within teams per week |
| Marketplace | Nights booked per month |
| Streaming | Listening time per active user |
| Developer platform | Weekly active projects running in production |
| AI assistant | Tasks completed and accepted per weekly user |

**Test the NSM:**

- Does it reflect customer value?
- Does it lead revenue rather than lag it?
- Can teams move it?
- Can it be measured weekly?

Break the NSM into 3–5 **input metrics** and give each team one of them. Connect team
OKRs directly to those inputs.

### AARRR (pirate metrics), for funnel thinking

Acquisition → Activation → Retention → Referral → Revenue. Use it to find the leakiest
stage. Fix stages from the bottom up: there is no point acquiring users into a broken
retention stage.

### Product-market fit signals

- The retention curve flattens.
- **Sean Ellis test:** at least 40% of users say they would be "very disappointed" without
  the product.
- Organic share of new users is rising.
- Sales cycles get shorter.

## 6 · Metric-spec checklist

For every metric in a spec, record:

- **Name** and the exact **formula**.
- The **numerator and denominator**.
- The **unit**: users, accounts or sessions.
- The **window** and the **segment cuts**.
- The **data source** and the owner.
- The **baseline**. If it is unknown, write "TBD, plus how to get it".
- The **target**, and the date to hit it.
- The **review cadence**.
- **Leading or lagging**.
- The **paired guardrail**.
- The **kill / pivot criterion**.

## 7 · Common traps

- **Vanity metrics:** totals, page views, sign-ups without activation.
- **Mix shift:** an aggregate metric moves because the user mix changed, not because
  behavior changed. Segment the data before concluding anything.
- **Simpson's paradox** shows up in A/B tests that span segments.
- **Novelty effect:** run tests for at least 2 full weekly cycles.
- **Goodhart's law:** once a metric becomes a target, people game it. Pair it with a
  guardrail.
- **Survivorship bias:** retention measured only on users still active looks better than
  reality.
