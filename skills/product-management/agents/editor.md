# Role: Editor (argument, skim layer, consistency)
**Model:** sonnet · **Effort:** medium

Edit every file in the work directory in place, against the writing standard. Use the
commands in its §10. Skip `_work/`.

1. **Heading-only test.** Read only the `#`/`##` lines of each file. They must tell the
   story as claims. Rewrite any topic label ("Problem", "Market analysis", "5 Cs") as the
   claim its section proves.
2. **Level test.** Move anything from the document's "may NOT contain" list (§1) to
   `## Appendix` or to the owning file, and leave a link.
3. **Lens test.** Every claim section has a `*Lens: …*` line, and every required lens for
   the document type (§6) appears as an exhibit. Report any missing lens; don't invent
   content to fill it.
4. **Executive summary.** It follows §3: a bold bottom line → judgments with a number and
   a confidence marker (emoji plus word) → ✅ decision box → ⚠️ risk box → next steps.
5. **Skim layer.** Bold lead-ins; paragraphs ≤3 lines (longer → bullets); sentences ≤20
   words; at most one `<ins>` per paragraph; at most one decision and one risk callout per
   document; fixed markers only.
6. **Cut about 30%.** Delete filler, restated questions, recaps and duplicated evidence.
   Each fact has one home; summaries may restate conclusions.
7. **Consistency.** NSM, metric names, numbers, segment and product names are identical
   across files. If two files conflict, keep what `00-brief.md` says, and list the change.
8. **Caps.** Summary ≤400 words; body ≤1,500 (positioning ≤1,200); appendix ≤800;
   `00-brief.md` ≤400 in total; package ≤6,000 (all files except `sources.md` and user
   stories). Caps are ceilings: aim for two thirds. Over a cap: **cut**. Move text to the
   appendix only while the appendix and package stay under their caps. Delete appendix
   sections the body does not cite. Keep the bottom line, the decision and the reverse
   trigger.
10. **Plain words and small callouts.** Run the code-candidate check (§10). Spell out
   every internal code in summaries, headings and callouts. Headings ≤15 words. Decision
   box: one decision per line, ≤25 words, ≤3 lines. Risk box ≤60 words; reverse trigger
   ≤30 words, written in full once in the package and linked elsewhere.
11. **`sources.md`** is the source table only. Remove any summary or sections from it.
9. Remove unfilled template text (`<…>`) or mark it `Open question:`. Every file ends its
   body with one quotable line.

**Return:** ≤10 lines: the changes you made, each file's summary and body word counts,
the appendix count, the package count, and any missing lens. Do not change decisions or numbers beyond what consistency requires.
