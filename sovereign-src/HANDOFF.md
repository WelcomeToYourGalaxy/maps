# Outside Every Country: how it builds
Run `python3 build.py` here to write ../outside_every_country.html from app_template.html, basemaps.js, data/plate.webp (Atlas with this map's cartouche, redrawn by tools/plate.py), data/moon.webp, data/mars.webp, data/zones.geojson and data/research/.
Order of application: ocean, land, space, water, routes, routes2, beyond, purchase, purchase2, then fix_* files, then plain-language rewrites rw1 to rw7, rw_zones, then patterns_new and odds_new. Later files win.
Odds numbers live in content/odds.py; reasoning text in data/research/odds_new.json.

## Rating and coverage (Nov 2026)
Default metric is odds.own (data/research/own.json), asking whether a route gives a private group its own territory under its own laws for ten years. odds.overall is now "Live there undisturbed". content/short.html is the summary button. data/research/coverage.json feeds the table in Method; on_map counts come from each row's case_ids, so add new entries there. Essay edit order in build.py: review1/2, consistency, cr1-3, cr4 (cr4 is exact replacements on the prior text). Entry patches: left, close, close2.
