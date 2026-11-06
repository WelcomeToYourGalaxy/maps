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
