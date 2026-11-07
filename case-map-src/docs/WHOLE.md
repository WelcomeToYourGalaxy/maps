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
