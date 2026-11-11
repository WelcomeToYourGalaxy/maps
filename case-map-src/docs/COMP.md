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

## The three faults that dominate every batch

1. **Claiming more than the cited page says.** Nationality is the commonest invention: a page saying a firm is "deeply rooted in France" does not say it is French, and a foreign-sounding name is not a source. The same goes for a headquarters city, a stock exchange listing, a founder, a product range, a country count. A ticker in logo alt text is not a stated listing. Never take a figure's year from the article's date.
2. **Describing a parent and presenting it as the subsidiary.** If no source names the company in the key, it cannot be described: leave it blank. A source describing what a firm did at a project site is not a description of the firm. Where a key names two entities and your sources cover only one, describe that one and say nothing about the other. The only exception is a documented identity link (for example an SEC filing showing one name was formerly the other).
3. **Attaching a figure or shareholding to the wrong entity.** Check that the stake, the revenue or the debt you quote belongs to the company in the key, not to a consortium it sits in, a listed arm of it, or a subsidiary in another country.

Honest blanks run 5-20% of a batch and are the right outcome.

## Also report case-data discrepancies

While reading sources you will find facts on the map's own cards (in `uses`) that the sources contradict — most often ownership that has changed since the case was written. Put these in a second file, `<output>_disc.json`, as a list of {company, what the card says, what the source says, source {title, publisher, year, url}}. Phrase corrections with dates rather than overwriting ("X held 38% at the time; the 2024 filing does not mention the mine"). Do not change anything yourself.
