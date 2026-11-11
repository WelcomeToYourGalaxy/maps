# Outside Every Country: how it builds
Run `python3 build.py` here to write ../outside_every_country.html from app_template.html, basemaps.js, data/plate.webp (Atlas with this map's cartouche, redrawn by tools/plate.py), data/moon.webp, data/mars.webp, data/zones.geojson and data/research/.
Order of application: ocean, land, space, water, routes, routes2, beyond, purchase, purchase2, then fix_* files, then plain-language rewrites rw1 to rw7, rw_zones, then patterns_new and odds_new. Later files win.
Odds numbers live in content/odds.py; reasoning text in data/research/odds_new.json.

## Rating and coverage (Nov 2026)
Default metric is odds.own (data/research/own.json), asking whether a route gives a private group its own territory under its own laws for ten years. odds.overall is now "Live there undisturbed". content/short.html is the summary button. data/research/coverage.json feeds the table in Method; on_map counts come from each row's case_ids, so add new entries there. Essay edit order in build.py: review1/2, consistency, cr1-3, cr4 (cr4 is exact replacements on the prior text). Entry patches: left, close, close2.


## Round of Nov 2026: coverage and checks
Page: 2297 attempts, 194 laws, 159 places, 22 patterns, about 7 MB.
Coverage (printed by build): narrow types about 98% against the lowest published counts, about 56% against the highest estimates, about 17% of everything counted. Five types remain mostly out: special economic zones, Indigenous self-government, flag registers, new states, private cities.
Research lives in data/research/patch_n_*.json; merge.json lists duplicate drops, pin removals and field corrections, applied after the new entries load.
Checks: independent sample of 63 items, 36 with problems (63 findings), all fixed plus a sweep. Automatic comparison of numbers, dates and names against saved Wikipedia pages covered about 1,770 entries; about 200 flagged and reviewed. About 85 entries with no Wikipedia source were outside it; Commissions of the Danube River was not read. Most entries were not read one by one.
Not reached: about 130 Dutch protectorate rows, British protectorates, Danzig Napoleonic, Mary State, Portuguese Asia, Morehead, Pindray, Harpers Ferry, Brion, Velos, Lady Franklin, Bahrain, Costa Chica. Fictions dropped: Chupacabra Kingdom, Kickassia.
Secondary copies of texts used because the primary refused: UNCLOS Part VII (whales.org.au), Protocol II (likumi.lv), Outer Space Treaty (NASA copy), Montevideo (Avalon and others), Saramaka (Cultural Survival).
Finismund, Lostisland and St. Charlie rest on MicroWiki only; TorHavn on its own site; directory figures are self-reported.
Wikipedia limits request rate: long read jobs hit 429s and the two-hour background limit, so read in small batches.

## Round of Nov 2026 (second): coverage against named lists
Page: 8,844 attempts, 265 laws, 159 places, 22 patterns, about 17 MB (3 MB gzipped).
Coverage is now measured item by item against every example a published list NAMES, not against estimates. build.py prints it. coverage.json rows carry `named` (how many a list names), `unread` (named but unreachable) and `named_basis`. Narrow types about 99.8%; all types about 87.7%; the gap is 1,201 items: PEZA's ~345 zones, New Cities Map's 353, Albert's rebel dataset, Altman's conquest list, ~210 princely states no list read names.
New batches: patch_n_h1..h7 (UN members, US tribes, Alaska entities, princely states, protectorates, datasets, SDM match) and patch_n_z1..z6 (special economic zones by region). About 6,600 entries, mostly script-written from one list row each.
Pins: $SP/geo.py looks up any GeoNames place offline (full country files, built on first use by $SP/gnprep.py CC). Never pin to a country centre when the source names no place: leave lat/lon null.
Markers now cluster (clusterRadius 30, clusterMinPoints 4, clusterMaxZoom 8) so dense regions show a numbered circle; without it the globe was a solid mass of icons.
Unreached and refused: PEZA and New Cities Map refused permission prompts; Albert and Altman datasets paywalled or robots-blocked; Iran's 34 SEZs, Philippine zones beyond 38, most Vietnamese zones, Curaçao/Aruba, Madagascar, New Zealand, Dakhla.

## Round of 10 Nov 2026: coverage closed to 100%
Page: 10,218 attempts, 265 laws and legal tests, 159 places, 22 patterns. About 19 MB.
Both coverage figures are now 100% of every example the published lists read name, and `unread` is 0 on every row. The map description (app_template.html, `#lede3`) prints these figures from the build, so it updates itself.

What was added this round, each as its own patch file in data/research/:
- `patch_n_peza.json` — 595 PEZA economic zones from the owner's upload of PEZA's list of 30 June 2026 (440 operating, 179 proclaimed). 24 were already here. peza.gov.ph is robots-blocked, so the file has to be downloaded by hand.
- `patch_n_conquest.json` — all 175 conquest attempts in Altman's Modern Conquest Data v3.0, from the Taking Territory replication zip at dan-altman.weebly.com (public). The Harvard Dataverse copy is the older v2.1, 151 cases to 2017, and Dataverse refuses robots. Country codes expanded with the Correlates of War state list; Altman's FRA/GER/JAP/MAI/RUM/GEO are COW's FRN/GMY/JPN/MLI/ROM/GRG. Use `real_year`, not `year`, which is lagged by one.
- `patch_n_rebels.json` — 234 records from Albert's Rebel Quasi-State Institutions dataset, free from the PRIO replication page. Grouped by actorid, not name: PLA, UPA, BRA and UNLF each cover two different groups in different countries. `countryname` is "NA" for 42 groups; fall back to `Location`. That field is the government fought, not the group's home, so entries are named by claimed territory where there is one. Full names where the Non-State Actor dataset (ksgleditsch.com, public) has them. The dataset stops at 2012, so no entry claims to know what happened after.
- `patch_n_newcities.json` — all 353 cities in the New Cities Map, written from the full dataset v1.0 (30 May 2023), which the owner downloaded from newcitiesmap.org. Its 92 columns carry governance, area, planned and current population, budgets, master planner and SEZ framework, and a City Autonomy Index scored 0 to 30.5 for 47 of the cities; the other 300 are marked not collected and the entries say so. ODbL, so the Charter Cities Institute is credited on every entry, with the city's own website where the dataset gives one. 21 cities were already here under other headings and are credited through the row's case_ids instead of being entered twice. The dataset's own coordinates for BSD City and Gwadar fall in open sea, so those two carry no position. The name-and-coordinate version of this data is also public inside the `__NEXT_DATA__` script on newcitiesmap.com/map if the download is ever unavailable.
- `patch_n_princely2.json` — 37 princely states from Wikipedia's alphabetical list, plus Mangrol. `patch_princely_alias.json` records 19 more that were already here under another spelling (Kota/Kotah, Khayrpur/Khairpur, Saraikela/Seraikela and so on) as alternative names, so the match is auditable.
- `patch_rebel_xref.json` — cross-references the six groups that have both a narrative entry and a dataset record (FARC, FMLN, Hamas, Hezbollah, RENAMO, UNITA).

Coverage bookkeeping corrected: `unread` means a published list names an item but could not be read. The 210 princely states previously counted there were never named by any list; published sources only count them (about 565 to 584 for British India, 193 for the Kathiawar Agency alone, which names nine). They now sit in the estimate column where the method says estimates belong. The Imperial Gazetteer's search pages refuse robots.
Undersea habitats gained `also_covered: 2`: "SEALAB I, II and III" and "Conshelf / Précontinent" are single entries covering three named items each, which the old count read as a gap.

Pins: 166 of the new entries were geocoded from the full GeoNames gazetteer (allCountries.txt, downloaded and searched offline; the Wikidata API rate-limits hard from here). Matching uses a feature-code ranking with the perpetrator's and victim's countries as hints. 15 same-name matches in the wrong place were rejected by hand and are listed in the apply script; Biafra, Eelam, Bodoland and East Karelia are simply not in GeoNames. Entries still without a position say so, and no entry is pinned to a country centre unless the source names the whole country as the territory taken.

Still open from this round:
- The Open Zone Map (study@openzonemap.com) was never written to; its data may hold zones beyond the Philippines.
- Rebel entries whose record runs to 2012 show as faded, which is the record ending, not the group. The status field cannot say that; each entry's text does.
- 208 of the new entries still have no position, mostly rebel groups whose territory the dataset names only as a country.
