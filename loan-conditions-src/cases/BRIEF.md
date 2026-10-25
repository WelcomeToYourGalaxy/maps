# Brief: cases where a loan condition caused harm

You are researching cases for a global map of the conditions the IMF and the World Bank attach to their loans. A case belongs on the map only if a cited source documents that a **specific IMF or World Bank loan condition, program requirement or program target** led to the measure that harmed people or land (a price rise, a sale of a public firm or service, a tariff cut, a subsidy cut, a pay or job cut, a user fee, a land or labour law change, and so on).

## Hard rules
1. Never invent anything. Every fact must come from a source you opened. If you cannot open a source, do not cite it.
2. The link from the IMF or World Bank to the specific measure must be documented by a source: the IMF or World Bank's own documents (letters of intent, program documents, staff reports, press releases, project/loan documents), a court or government record, an academic study, or a reputable news report. Never stretch a weak or general link ("the country had an IMF program at the time") to fit a story. If the link is only that a government blamed the IMF, or only that critics claim it, either drop the case or mark it `"confidence": "contested"` and say on the card who says what. Give both sides where the IMF or Bank denies its role.
3. Harms must also be documented: deaths, injuries, arrests, job losses, price rises, people cut off, land lost, etc., each with who counted them.
4. Do not repeat any case in `existing_titles.txt` (same place and same event). A different event in the same country is fine.
5. Global: any country, any year, including Europe and rich countries (for example, IMF programs in Greece, Ireland, Portugal, Cyprus, Iceland, Latvia, Hungary, Ukraine, Korea, the UK in 1976).
6. Plain, short English for a novice reader. No flourish. Give figures and mechanisms, not adjectives. Quotes from sources: under 15 words, at most one per source; paraphrase the rest.
7. Do not use the words "brief", "I", or "sources opened" in any text field.

## Output
Write a JSON object to the file path you are given: `{"cases": [...], "dropped": [{"title": ..., "why": ...}]}`.

Each case follows exactly the shape of `example_case.json` in this folder:
- `id` (kebab-case), `title`, `place`, `iso3`, `lat`, `lng` (the place the card names; if approximate, say so in `point`), `point` (what the mark stands on), `start`, `end` (years; `end` null if ongoing)
- `mechanism`: one of `privatization` (a sale, concession, lease or contract of a public firm or service), `trade` (tariff cuts, market opening, marketing-board or export rule changes), `austerity` (price, subsidy, tax, wage, job, pension or spending cuts and the protests that followed), or `law` (a required change to labour, land, mining, investment or other law)
- `lenders`: list of `{name, role}`; `conditions`: what the condition required, with its source named
- `companies`: list of `{name, role, hq, hq_lat, hq_lng}` (empty list if none)
- `community`: what happened to people and land; `suppression`: how resistance was put down (empty string if none documented)
- `killed`: integer or null; `killed_note`: who counted
- `outcome`: what happened next
- `sources`: list of `{title, publisher, year, url}`
- `confidence`: `"documented"` or `"contested"`; `confidence_note`: why, when contested

Leave out the fields `lk`, `cp`, `rg`, `cx`.

Aim for as many strong cases as you can document in your batch, up to about 15. Quality over count.
