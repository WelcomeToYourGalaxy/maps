# Pipeline Map — handoff (15 November 2026)

Intended live page: https://welcometoyourgalaxy.github.io/maps/pipelines.html
Build output: `pipelines.html` (repo root). Sources: `pipelines-src/`. Rebuild with `python3 build.py` in this folder.

## What the map is
A MapLibre globe, in the same design as the Infiltration Map (its CSS, basemaps.js and atlas plate, read from `secret-society-src/`), of schools and programmes that pick and train young or mid-career people who go on to hold power. Lines run from each school to the capitals of countries where its former students held national office (head of state, head of government, minister, central bank governor). The owner asked for it on 15 November 2026, starting from the suppression page's paragraph on Harvard, Chicago and the LSE training Global South elites in free-trade theory, and the infiltration map's Young Global Leaders entry, with "a hint of conspiracy, like it's a nefarious process".

Size at first build: 154 schools in 9 kinds, 4,473 office-holders, 7,415 national offices, 5,583 school-person links, 190 countries, 10 patterns, 5 possible patterns.

## Files
- `seed.py` — the school list (id | kind | Wikipedia title).
- `meta1.py`–`meta4.py` — each school's box: location, founding year, who is behind it, how people get in, the writeup, sources. Writeups state only what the cited pages support.
- `patterns.py` — the ten patterns and five possible patterns (hedged claims, counted nowhere).
- `about.py` — About and Method pages.
- `app_template.html` — the app. `base.css` is the infiltration map's CSS.
- `data/records.json` — processed snapshot of the Wikidata pulls: [person QID, school id, via, list URLs, offices]. `build.py` uses it when `data/alumni/` is absent.
- `data/labels.json` (names, Wikipedia titles, birth/death years, office labels), `data/list_alumni.json` (people resolved from published Wikipedia lists), `data/juris.json` (jurisdiction to ISO3), `data/qids.json`.

## How the office-holders were found (re-run order)
1. `positions.py` — every Wikidata position that is a subclass of head of state, head of government, minister or central bank governor, with its jurisdiction (writes data/positions_raw.json, 4.4 MB, not committed).
2. `fetch_alumni.py` — for each school QID: people educated at it or any part of it (P69 with P361*), award (P166), member (P463), employer (P108), with their positions (data/alumni/, 35 MB, not committed). Employer links count only for think tanks and firms.
3. `parse_lists.py` + `resolve_lists.py` — the first linked name per row or bullet of published Wikipedia lists (IVLP, Chevening, Fulbright, Rhodes, Marshall, YGL, French-American Foundation, Atlantik-Brücke, Eisenhower, YSEALI, Mont Pelerin, Chicago Boys, SOA graduates, CGSC foreign alumni, Old Etonians), resolved to Wikidata humans and their positions. Only the first link per row: a first pass took every link and would have counted people named in descriptions ("adviser to Thatcher").
4. `labels.py`, then `build.py`.

The Wikidata Query Service rate-limits (429); scripts retry with back-off. en.wikipedia.org `action=raw` works from the shell; the Wikipedia API is rate-limited harder.

## Known gaps and next steps
- Wikidata holds little or nothing for some programmes: RSS (0), Nyerere Leadership School (no item), CEMA, Kim Il Sung school, FSB Academy (no item found), Komsomol (2), Global Shapers, BAP, Schwarzman. Their boxes say a gap in the record is not proof of none. Hand-sourced records from published reporting would fill them.
- Universities count all alumni, not only the department in the story (the Method page says so).
- Ministers are recorded less completely than heads of state or government.
- Some Wikidata education claims are odd but sourced there (e.g. Gaddafi at Fu Hsing Kang, from Wikipedia's notable-alumni list). Worth a check.
- Country boxes are data-driven (counts, top school, plain summary). The owner may want written behind-the-scenes country writeups like the infiltration map's.
- No live wire yet.
