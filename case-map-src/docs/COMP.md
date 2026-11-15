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

## Round 33's findings — read these before you start

**For a public body, searching for the body's own page is the wrong first move.** It caused both
failure modes in round 33. Read **the loan or credit agreement's definitions section** and **the
appraisal document's institutional-arrangements section** first; both are on disk in
`cache/<PID>/`, and each record's `appears_on` gives the project number. Three of five blanks a
writer recorded as "no page names the exact entity" were sitting in a definitions section it never
opened:
- Ahwaz Water and Wastewater Company is itself a party to its project agreement — "AHWAZ Project
  Agreement ... between IBRD and AHWAZ WATER AND WASTEWATER COMPANY" — with its own audited
  figures in the appraisal document's financial annex.
- Iraq's State Commission for Roads and Bridges is defined in the 2014 loan agreement as "the
  commission within the Ministry of Construction and Housing", and the 2023 completion report
  records its becoming the Roads and Bridges Directorate.
- A Congolese project coordination unit is described in its 2007 agreement's definitions and the
  2008 resettlement framework: a decree of September 2003, under the Ministry of Planning, three
  directorates, no environmental or social specialist.

A blank is right only when nothing describes the body. It is not right because no website does.

**The page that exists is nearly always the successor's, describing the successor.** Check every
web-sourced remit against the date range in `appears_on` before writing it in the present tense.
Round 33's instances: a ministry's remit taken off its successor's infographic; a roads agency's
creation taken off a page that calls it by a different name; a housing fund attributed to a
delegate ministry created after the case closed; a water authority described wholly in the present
tense from a statute of 1971 while two other entries in the same batch record the 1997 concessions
that took over those operations.

**No figure carries a date unless the document gives that date in the same sentence or table cell.**
Five errors in one batch were a year the document does not attach to the figure: a 99.85 per cent
stake dated to the deck's cover, a ministry split dated to a news timestamp, two statutes' years
read off hyperlink URLs, an irrigation area taking an "as of December 2024" that belongs to a
different number, and a decree's year taken from the article reporting it. Each is a plausible year
sitting one line from the figure, and invisible in a finished sentence. Publish the figure undated,
or not at all.

**Mark a draft figure as a draft.** A national audit table labelled a revenue row "(Draft)" and the
figure had been written up as settled.

**Say the name mismatch rather than smoothing it.** Where the key reads "rePlan Inc." and the
article never says "Inc.", write that. The same for an acronym the project's own documents spell
inconsistently and never define.

**A statute establishing a body is good evidence of its remit and poor evidence of what it is now.**
Attribute the powers to the Act, with its year, and say so.
