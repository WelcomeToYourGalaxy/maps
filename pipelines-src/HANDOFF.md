# Pipeline Map — handoff (15 November 2026)

Intended live page: https://welcometoyourgalaxy.github.io/maps/pipelines.html
Build output: `pipelines.html` (repo root). Sources: `pipelines-src/`. Rebuild with `python3 build.py` in this folder.

## What the map is
A MapLibre globe, in the same design as the Infiltration Map (its CSS, basemaps.js and atlas plate, read from `secret-society-src/`), of schools and programmes that pick and train young or mid-career people who go on to hold power. Lines run from each school to the capitals of countries where its former students held national office (head of state, head of government, minister, central bank governor). The owner asked for it on 15 November 2026, starting from the suppression page's paragraph on Harvard, Chicago and the LSE training Global South elites in free-trade theory, and the infiltration map's Young Global Leaders entry, with "a hint of conspiracy, like it's a nefarious process".

Size at first build: 154 schools in 9 kinds, 4,473 office-holders, 7,415 national offices, 5,583 school-person links, 190 countries, 10 patterns, 5 possible patterns.

Second build (same day) briefly added every school any office-holder attended (7,500 "record" schools). The owner rejected that: it turned the map into a map of where famous people studied. Third build: pipelines only. 189 schools, 4,985 office-holders.

Fourth build (the owner asked for a complete map of pipelines): a systematic sweep of the record for every officer academy, administration or party school and elite secondary school that produced national office-holders, keeping those a published source describes as training people for power. 258 schools and programmes, 5,557 office-holders, 191 countries, 185 country accounts.

Patterns: the officer-schools and one-door patterns were extended to cover the new schools, and their opening lines rewritten to match.

Rule for the map: a person appears only if they went through a documented school or programme. Ordinary universities stay off the map unless a source documents them as a pipeline, in which case they get a writeup in a meta file.

Coverage: Wikidata lists about 44,490 people in these national offices (after removing mayors); 4,985 (about 11%) went through a pipeline on the map. Each country box gives its own figure (DATA.TM against DATA.T).

## Files
- `seed.py` — the school list (id | kind | Wikipedia title).
- `meta1.py`–`meta4.py` — each school's box: location, founding year, who is behind it, how people get in, the writeup, sources. Writeups state only what the cited pages support.
- `patterns.py` — the ten patterns and five possible patterns (hedged claims, counted nowhere). The possible patterns say what would show them; the owner asked for the 'would be refuted' sentences to be removed. The patterns' `means` text is headed 'What this means for who governs.'
- `meta5.py` — 14 schools added in the second build (officer academies, national defence colleges, École William Ponty, New Generation fellowships). `process.py` imports it as P10.
- `about.py` — About and Method pages. Method placeholders (__NS__, __NR__, __NALL__, __NACC__ …) are filled by `build.py`.
- `meta7.py` — the sweep's 54 additions: national officer academies behind coups (Argentina, Brazil, Peru, Chile, Portugal, Honduras, Mali, Burkina Faso, Nigeria, Libya, Lebanon), foreign staff colleges (Camberley, Quetta, École de guerre, US Naval and National War Colleges, Dartmouth, Belgium's RMA, the Lenin Military-Political Academy, Ryazan, PLA NDU, Baoding, Japan's Army War College, Thailand's NDC), administration and party schools (Algeria, Mali, Morocco, Romania, Ukraine, Azerbaijan, Armenia, Ghana, Thailand, the Minsk, Hungarian and Polish party schools, Russia's diplomatic, finance, interior and state-service academies, France's colonial school and the IIAP), and elite secondary schools (Instituto Nacional, Athénée, Westminster, Gakushūin, Sisowath, Habibia, Galatasaray, Royal College Colombo, Henri-IV, Albert Sarraut, Baghdad College, Kyunggi, Assumption, Stanislas, Queen's College, Debsirin, Curepipe, Raffles, Harrison, Athens College, Adams, Umuahia, Munali, Ichikō).
  Candidates were generated from `data/rec_snapshot.json` and each was checked against its own Wikipedia article; schools with no source describing them as training for power were left off (Dominica Grammar School, St Aloysius' Malta, Chien Kuo, Victoria School, Saint-Louis de Gonzague and others). Enderûn was written up and then dropped: all its office-holders predate 1800, which `build.py` excludes.
- `meta6.py` — 21 pipelines the country accounts described, written up with sources (West Point, Mons, India's staff college, Myanmar's DSA, Spain's General Military Academy, the Venezuelan, Indonesian, Greek, Iraqi, Sudanese and Meknes officer academies, Barewa, Malay College, Robert College, Sadiki, Mangyongdae, Tunisia's ENA, Cameroon's ENAM, Belarus's presidential academy, the CPSU Academy of Social Sciences, Fourah Bay). Their people come from the record snapshot via REC_TO_DOC in `build.py`.
- `rec.py` — reads `data/uni/`: every institution an office-holder attended. Only used now for per-country totals and to supply people for documented schools (REC_TO_DOC); the record schools themselves are not shown.
- `universe.py`, `universe2.py` — the pulls behind the record layer: all holders of every national position, their P69 education, institution details, labels (data/uni/, ~40 MB, only the small label and lookup files are committed).
- `acc_0.py`–`acc_9.py` — the country accounts as first written (198): `d` paragraphs, `sch` documented school ids whose first source is added, `src` extra sources. `accounts.py` merges them and applies `acc_fix.py` (cuts sentences that rested on ordinary schools or whole-record counts), `acc_fix2.py` (trims mixed sentences, repairs openings) and `acc_rule.py` (any sentence about study must name a pipeline on the map; an account with no pipeline left is dropped). 185 remain. `build.py` reads it.
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
