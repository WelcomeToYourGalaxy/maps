# Pipeline Map — handoff (15 November 2026)

Intended live page: https://welcometoyourgalaxy.github.io/maps/pipelines.html
Build output: `pipelines.html` (repo root). Sources: `pipelines-src/`. Rebuild with `python3 build.py` in this folder.

## What the map is
A MapLibre globe, in the same design as the Infiltration Map (its CSS, basemaps.js and atlas plate, read from `secret-society-src/`), of schools and programmes that pick and train young or mid-career people who go on to hold power. Lines run from each school to the capitals of countries where its former students held national office (head of state, head of government, minister, central bank governor). The owner asked for it on 15 November 2026, starting from the suppression page's paragraph on Harvard, Chicago and the LSE training Global South elites in free-trade theory, and the infiltration map's Young Global Leaders entry, with "a hint of conspiracy, like it's a nefarious process".

Size at first build: 154 schools in 9 kinds, 4,473 office-holders, 7,415 national offices, 5,583 school-person links, 190 countries, 10 patterns, 5 possible patterns.

Second build (same day): 168 documented schools, plus 7,500 "every other school in the record" (kind `rec`, grey dots, no writeup), 22,991 office-holders, 35,018 national offices, 38,079 school-person links, 198 countries, and a written "Behind the scenes" account for each of the 198 countries.

Coverage: Wikidata lists about 44,490 people in these national offices (after removing mayors). Roughly half have any school recorded; the map shows all of them. The first build showed about 10%. Programmes Wikidata does not track (visitor programmes, party schools, private fellowships) cannot be counted.

## Files
- `seed.py` — the school list (id | kind | Wikipedia title).
- `meta1.py`–`meta4.py` — each school's box: location, founding year, who is behind it, how people get in, the writeup, sources. Writeups state only what the cited pages support.
- `patterns.py` — the ten patterns and five possible patterns (hedged claims, counted nowhere). The possible patterns say what would show them; the owner asked for the 'would be refuted' sentences to be removed. The patterns' `means` text is headed 'What this means for who governs.'
- `meta5.py` — 14 schools added in the second build (officer academies, national defence colleges, École William Ponty, New Generation fellowships). `process.py` imports it as P10.
- `about.py` — About and Method pages. Method placeholders (__NS__, __NR__, __NALL__, __NACC__ …) are filled by `build.py`.
- `rec.py` — builds the record layer from `data/uni/`: every institution an office-holder attended, colleges rolled into their parent university, placed at its own coordinates or its parent's. Returns per-country totals (all holders, holders with a school).
- `universe.py`, `universe2.py` — the pulls behind the record layer: all holders of every national position, their P69 education, institution details, labels (data/uni/, ~40 MB, only the small label and lookup files are committed).
- `acc_0.py`–`acc_9.py` — the 198 country accounts: `d` paragraphs, `sch` documented school ids whose first source is added, `src` extra sources. `accounts.py` merges them; `build.py` reads it.
- `digest.py`, `view.py`, `who.py` — helpers used while writing the accounts (per-country digests of who studied where; lookups against the built page).
- `tools/plate.py` — repaints the Atlas cartouche to read PIPELINE MAP (Cinzel, `tools/Cinzel.ttf`, OFL) from `../secret-society-src/plate.webp` into `data/plate.webp`, which `build.py` inlines.
- Markers: `MK` in `app_template.html` gives each basemap its own muted marker palette (ten kinds, the record dots, and the edge colour). Documented schools are solid dots with a thin edge and a fine outer ring; record schools are small plain dots drawn beneath them. Panel swatches use the Jurassic palette when the Atlas (light) basemap is on, since the cards stay dark.
- `data/rec_snapshot.json` — processed snapshot of the record layer; `build.py` uses it when `data/uni/` raw pulls are absent.
- `app_template.html` — the app. `base.css` is the infiltration map's CSS.
- `data/records.json` — processed snapshot of the Wikidata pulls: [person QID, school id, via, list URLs, offices]. `build.py` uses it when `data/alumni/` is absent.
- `data/labels.json` (names, Wikipedia titles, birth/death years, office labels), `data/list_alumni.json` (people resolved from published Wikipedia lists), `data/juris.json` (jurisdiction to ISO3), `data/qids.json`.

## How the office-holders were found (re-run order)
1. `positions.py` — every Wikidata position that is a subclass of head of state, head of government, minister or central bank governor, with its jurisdiction (writes data/positions_raw.json, 4.4 MB, not committed).
2. `fetch_alumni.py` — for each school QID: people educated at it or any part of it (P69 with P361*), award (P166), member (P463), employer (P108), with their positions (data/alumni/, 35 MB, not committed). Employer links count only for think tanks and firms.
3. `parse_lists.py` + `resolve_lists.py` — the first linked name per row or bullet of published Wikipedia lists (IVLP, Chevening, Fulbright, Rhodes, Marshall, YGL, French-American Foundation, Atlantik-Brücke, Eisenhower, YSEALI, Mont Pelerin, Chicago Boys, SOA graduates, CGSC foreign alumni, Old Etonians), resolved to Wikidata humans and their positions. Only the first link per row: a first pass took every link and would have counted people named in descriptions ("adviser to Thatcher").
4. `universe.py`, `universe2.py` (record layer), `labels.py`, then `build.py`.

Fixes applied in `build.py`: positions whose label matches mayor/bürgermeister/city executive are dropped; Q14915624 (fictional Claire Underwood) and Q5078492 are removed; two vandalised office labels are overridden in FIXPOS; ~60 non-Latin person labels were replaced with English labels in the label files.

The Wikidata Query Service rate-limits (429); scripts retry with back-off. en.wikipedia.org `action=raw` works from the shell; the Wikipedia API is rate-limited harder.

## Known gaps and next steps
- Wikidata holds little or nothing for some programmes: RSS (0), Nyerere Leadership School (no item), CEMA, Kim Il Sung school, FSB Academy (no item found), Komsomol (2), Global Shapers, BAP, Schwarzman. Their boxes say a gap in the record is not proof of none. Hand-sourced records from published reporting would fill them.
- Universities count all alumni, not only the department in the story (the Method page says so).
- Ministers are recorded less completely than heads of state or government.
- Some Wikidata education claims are odd but sourced there (e.g. Gaddafi at Fu Hsing Kang, from Wikipedia's notable-alumni list). Worth a check.
- Country accounts are written from the record as of 15 November 2026; they will drift as Wikidata changes. Every source link was checked to resolve.
- Record-layer oddities left as recorded: a Honduran military academy placed in Timor-Leste, Belén Jesuit placed in Miami, Commonwealth realms counting Charles III, Republic of China leaders under Taiwan, Yugoslavia under Serbia. A few hundred record schools have no coordinates and appear only in lists and search.
- No live wire yet.
