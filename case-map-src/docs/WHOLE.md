# Whole-picture text for map cases

Each case on the map already describes the harm (community, killed, outcome). It lacks a short "whole picture" paragraph: what the project, loan or programme actually delivered, so the harm sits in context. You write that paragraph.

Input: a JSON list of cases (your batch file). Output: a JSON object keyed by case id:

{"<id>": {"whole": "...", "self_reported": true|false, "searched": "what you looked at, one line", "sources_add": [{"title","publisher","year","url"}]}}

If you find nothing credible, give "whole": "" and say in "searched" what you tried. A blank means no credible information was found.

What goes in `whole` (2-4 short sentences, plain words, novice reader):
- What the project/loan/programme achieved, where documented: power generated, people served, output, revenue or taxes paid, growth, jobs, debt relief, inflation brought down, etc. Plain figures, credited to who reported them: "(Reuters)", "by the World Bank's own count".
- Where the only figures come from the lender, the company or the government that ran it, say so plainly (e.g. "by its own count; no independent check was found"), and set self_reported true. Lender-produced success figures are biased; say so when they are the only source.
- If independent reviews (auditors, evaluation offices, academics, journalists) found it fell short, give their figures.
- For austerity, debt or policy loans: what the programme was meant to do and what independent data show happened (inflation, growth, debt, poverty), with who says what.
- Do not repeat the harm already in the case. Do not judge. No opinion words, no purple prose. Show figures rather than characterising them.

Rules (non-negotiable):
- No fabrication. Every figure, date, name and quote comes from a page you actually opened with WebFetch. If a page will not open, do not use its facts. Search snippets alone are not enough.
- Disputed figures: say who says what.
- Do not use Wikipedia as the only source for a fact.
- Every source used goes in sources_add with a working URL.

Tools: WebSearch and WebFetch. The shell mostly cannot reach the web; do not retry a refused request through other commands. WebFetch has an hourly limit shared with other agents; if you hit it, wait for the next UTC hour (use a shell `sleep` in small steps if needed) and continue, using no other route.

Validate your output with python (valid JSON, every input id present). Reply briefly: counts written, blanks, and any case where sources disagree.

## `self_reported` — the ruling, settled in round 33

This brief listed "a utility's published statistics" among the independent routes. **That is wrong
where the utility is the body that ran the work**, and a round 33 writer raised the conflict itself
rather than taking the licence.

`self_reported` stays **true** where every figure comes from the lender, the borrower, the
implementing agency, the operator, or the lender's own evaluation office. An operator reporting on
its own project is self-reporting, exactly as the lender is, and an Evaluation Group review or a
Project Performance Assessment Report is still the lender's own house.

It turns **false** only for a figure from someone outside the project: a national audit office, a
statistics office, a regulator that did not run the works, academics, journalists. Press reporting
counts only where the figures are the outlet's own or a third party's — an article relaying the
operator's announcement is the operator's figure in someone else's words.

Where a paragraph's only figures come from the lender or the borrower, say so in the paragraph's own
words as well as setting the flag.

## Also from round 33

**No figure carries a date unless the document gives that date in the same sentence or table cell.**
A year taken from a page's cover, a news timestamp, a hyperlink URL, or an "as of" belonging to a
different number is invented.

**Never take a figure out of these tables by grep.** The columns survive text extraction unaligned,
with the neighbouring row's data directly above the value wanted. Print the block from the header
row to the footnote and read it. One card in a recent round read a seasonal-camp identifier as a
hectare figure.

**A completion report contradicting itself is not a source for either reading.** Round 33 found four
— a results-framework annex scoring an indicator as not achieved where the summary table scores it
achieved, a rate-of-return sentence giving 25 per cent against 12 per cent ex ante and then calling
it "considerably lower", a reservoir capacity given as 8 and 9.8 million cubic metres in one report,
a facility listed as dropped for want of funds in one table and operating to its design capacity in
another. Where the contradiction is internal to one document, use neither figure and say so; where
it is between two documents, give both and name who says what.
