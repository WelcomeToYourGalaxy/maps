# Outside Every Country: how it builds
Run `python3 build.py` here to write ../outside_every_country.html from app_template.html, basemaps.js, data/plate.webp (Atlas with this map's cartouche, redrawn by tools/plate.py), data/moon.webp, data/mars.webp, data/zones.geojson and data/research/.
Order of application: ocean, land, space, water, routes, routes2, beyond, purchase, purchase2, then fix_* files, then plain-language rewrites rw1 to rw7, rw_zones, then patterns_new and odds_new. Later files win.
Odds numbers live in content/odds.py; reasoning text in data/research/odds_new.json.
