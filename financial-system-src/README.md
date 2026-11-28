# financial_system.html — Other People's Money

Source for `financial_system.html`, a story map of how the financial system is built, how money and securities move through it, who runs it and what it charges. It is a separate map from `finance.html`.

Built on the shared story-map engine, taken from `religion.html` (the same design as `environmental_law.html`).

- `story_a.py` — parts 1 and 2: the parts, and the motion
- `story_b.py` — parts 3 and 4: the command, and the bill
- `orgs.py` — the directory of organisations (the 29 designated banks carry their own coordinates; the rest are placed at their headquarters city by `build.py`)
- `records.py` — documented records and the hover glossary
- `pages.py` — title, About and Method text
- `build.py` — assembles everything into `out/financial_system.html`; counts every figure quoted from the country data, adds the 141 jurisdictions of the Financial Secrecy Index 2025 to the directory, and applies a list of text corrections (paths inside are those of the build machine and need adjusting; needs `pip install geonamescache`)
- `data/wb2.json` — World Bank indicators downloaded from api.worldbank.org on 27 November 2026 (latest year per country, 2010 onward)
- `data/wd/` — eleven more classes of financial institution from Wikidata, downloaded 27 November 2026 with `data/wdq.py`; the other fifteen classes are read from `../finance-src/data/wd/`
- `data/base.json` — country names, regions and centroids used by the engine
- banking crises and secrecy scores are read from `../central-bank-src/out/extra.json`
- `make_plate.py`, `plate0.webp`, `plate.webp`, `cinzel.ttf` — the Atlas basemap plate with this map's cartouche (Cinzel, SIL Open Font License)

Engine changes made in `build.py`: Atlas is the default basemap; the dots layer is drawn from Wikidata points; lines between places do not wrap across the Pacific edge; the "most responsible" switch is relabelled for this map; the unused layer of the religion map is removed.
