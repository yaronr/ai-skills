# Deck standard

Standard and Full runs ship a slide deck beside the markdown package: `deck.html`,
rendered to `deck.pdf`. The deck is what most people see. The markdown package stays the
source of truth; the deck never says anything the package doesn't.

Start from [`assets/deck-template.html`](../assets/deck-template.html). It holds the
layout, the slide types and the exhibit parts. Don't restyle it per run; swap the colour
variables at the top for the organisation's brand if one exists.

**Contents:** 1 The cold reader · 2 Storyline · 3 Cover · 4 Slide anatomy ·
5 Exhibits · 6 Footnote · 7 Words · 8 Checks

---

## 1 · Write for the cold reader

The deck gets forwarded. Its reader has not read the package, was not in the room, and
does not know the product's internal names. Every slide must make sense to that person.

- **Name things on first use.** The cover says in one line what the product is and what
  it does. Every product, feature, segment or option name is defined the first time it
  appears in the deck, in plain words.
- **Full verbs with objects.** Say who does what to whom. Not "Lead with mid-market", but
  "Sell the invoicing product to mid-market finance teams first". Not "Ship B", but
  "Build the 'pay by bank transfer' option".
- **No package shorthand.** No option letters, hypothesis codes, segment nicknames or
  quoted internal labels on a slide unless that same slide defines them. A legend counts
  as a definition only if it is next to the marks it explains.
- **One-line subhead when the title can't carry it.** Clarity wins over the word cap:
  if a title needs a definition to make sense, put the definition in a subhead line
  under the title, not in the reader's head.
- **The test:** show the slide alone to someone outside the team. They can say what
  the slide claims, what product it is about, and what each exhibit shows. If they
  can't, the slide fails, however correct it is.

## 2 · Storyline

The deck follows the same storyline as the main document (writing standard §2). Order:

1. **Cover** (§3).
2. **Executive summary**: three bands — *Why act now?* · *What do we recommend?* ·
   *How do we start?* — and one reverse-if line.
3. **One slide per storyline claim**, in order: the problem quantified → the options →
   the pick and why it won → how sure we are (sensitivity) → how we win → the plan.
4. **Decisions needed**: who decides what, by when, and what is a one-way door.
5. **Backup** (marked as such): validation plan, detail the main slides cite.

8–15 main slides. A slide that proves no storyline claim is cut.

## 3 · Cover

The cover answers four questions before the reader turns the page:

| Line | Says | Example shape |
|---|---|---|
| **Question** | The question this deck answers, as a question | "Which customers should our invoicing product sell to first in Europe?" |
| **Trigger** | Why this was asked now: the event, request or signal | "The CEO asked after three EU prospects stalled on e-invoicing rules in one quarter." |
| **Product** | What the product is, in one plain sentence | "<Product> sends, tracks and collects B2B invoices from the accounting tool a team already uses." |
| **Answer** | The recommendation, as a full sentence | "Sell first to mid-market finance teams in countries where e-invoicing is already mandatory." |

Below them: status (draft or final), who decides, the date, and any sensitivity label.

## 4 · Slide anatomy

Every content slide has the same parts, top to bottom:

| Part | Rule |
|---|---|
| **Tracker** | The storyline step, 1–4 words ("Where the problem is"). |
| **Action title** | One full-sentence claim, 10–20 words. It is the slide's message; the exhibit proves it. |
| **Subhead** (optional) | One line defining what the title needs (§1). |
| **Exhibit** | One per slide. Chart, table, matrix, tree or flow. Side cards explain it, they don't add new claims. |
| **Takeaway** (optional) | One callout line: the implication. |
| **Footnote** | Source, date and method notes (§6). |
| **Tag** | "Preliminary", "Backup" or "Illustrative" in the top corner, when true. |

- **Frameworks are drawn, not named.** A 2×2, options matrix, metric tree or kernel is the
  exhibit. Its name goes only in the footnote ("Framework: options matrix"). No `Lens:`
  lines, no framework names in titles.
- **No emoji, no inline source tags** (`[S10]`), no markdown callout syntax. Confidence is
  a word or a coloured chip with the word in it.
- **Body text ≥14 px**, footnote ≥10 px. Leave white space; fill about two thirds.

## 5 · Exhibits explain themselves

A reader must understand an exhibit without the speaker, the package or the slide title.

- **Exhibit title** says what is measured, the unit and the scale: "Weighted score out
  of 65 (higher is better)", not "Weighted score".
- **Every axis, column, row group and series is labelled in plain words.** Group labels
  say what changes, as a phrase: "If 'buyer already uses an accounting tool' counts 1×
  instead of 3×", not `"Has tool" ×1`. The first group is named for what it is: "Our weights".
- **Label series directly** on or beside the bars or lines. Use a separate legend only
  when direct labels don't fit, and then place it above the chart.
- **Encodings get a key.** Scores, weights, Harvey balls, colour codes and arrows each
  get a one-line "How to read" under the exhibit: what full means, what the scale is, what
  colour means.
- **Options keep their full names** on every exhibit. A letter may prefix the name ("B ·
  Pay by bank transfer"), never replace it.
- **Every options or competitor table has a price column.**
- **One message.** If the exhibit shows two things, split it or cut one.

## 6 · Footnote

One small block at the bottom of every content slide:

`Source: <publisher, title> (<date>); <…>. Note: <method or caveat>. Framework: <name>.`

- Every external number on the slide has its source and date here.
- Internal analysis is cited as such ("internal option scoring, <date>").
- Arithmetic that a sceptic would check goes here or in backup, not in the body.

## 7 · Words

- Titles 10–20 words; about 100–200 words per slide in total.
- Sentences ≤20 words. Numbers instead of adjectives.
- The same names, numbers and dates as the package. If the deck needs a number the
  package lacks, add it to the package first.
- Plain words (writing standard §3): spell out every internal code.
- Dates follow the package rules: given, sourced, or "recommended, owner to confirm".

## 8 · Checks

Run both, and fix every failure before packaging:

```bash
python3 scripts/check_deck.py deck.html          # static: cover, titles, footnotes, codes, emoji
node scripts/render_deck.js deck.html deck.pdf   # renders the PDF and slide PNGs; fails on overflow
```

`render_deck.js` needs Node and Playwright (`npm i -g playwright` and a Chromium). If
neither is available, render the PDF with any headless Chrome and check each slide by eye.

Then run the **cold-read review** (`agents/cold-reader.md`): a fresh agent sees only the
slide PNGs. For each slide it states the claim, the product and what each exhibit shows,
and for the cover the question and the trigger. Any slide it can't read, or reads wrong,
fails. Fix the slide, not the reviewer's prompt.
