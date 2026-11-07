# One-line descriptions of the companies named in map cases

The map's case cards list each company with its headquarters and its role in that case, but not what the company is. Readers can't tell a Chinese state dam-builder from a family-owned palm-oil firm. You write one short description per company.

Input: a batch file of {name, uses:[{case, title, hq, role}]}. Output (your output file): {"<exact name as given>": {"desc": "...", "sources": [{"title","publisher","year","url"}]}}

The desc, 1-2 short sentences, plain words for a novice:
- What kind of firm it is and what it does (sector, main business).
- Who owns or controls it where documented: state-owned (which state), listed on which exchange, family-owned, subsidiary of which group, joint venture of whom.
- Size, in one plain figure where a reliable source gives it (revenue, employees, or output), with the year.
- If it no longer exists or was renamed or bought, say so with the year.
- Do not restate its role in the case (the card already shows that). Do not judge it. No opinion words.
- Government bodies or local agencies named as companies (e.g. a national utility): describe them the same way.

Rules (non-negotiable):
- Every fact comes from a page you actually opened with WebFetch: the company's own site or annual report, a stock exchange or regulator filing, a government register, or a reputable news outlet. Wikipedia may lead you to a source but must not be the only source.
- If you cannot find and open a credible source, give "desc": "" and a "note" saying what you tried. A blank is better than a guess.
- Where one name in the list is clearly the same firm as another (e.g. "Sinohydro" and "Sinohydro (PowerChina)"), write both, consistently.

Tools: WebSearch and WebFetch. The shell mostly cannot reach the web; do not retry a refused request through other commands. WebFetch has an hourly limit shared with other agents; if you hit it, wait for the next UTC hour and continue, using no other route.

Save progress to the output file every ~20 companies. Validate with python at the end (valid JSON, every input name present). Reply briefly with counts written and blanks.
