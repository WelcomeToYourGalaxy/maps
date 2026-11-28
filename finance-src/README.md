# finance.html — The Fine Print

Source for `finance.html`, built on the shared story-map engine (taken from `religion.html`).

- `story_d.py` — the current (second) edition: the customer's side of finance. It reshapes and adds to `story_a.py`, `story_b.py`, `story_c.py` (first edition)
- `data/wd/` and `data/wd_fetch.py` — financial institutions from Wikidata (the dots layer); `data/bis_hh.csv` — BIS household debt
- `records.py` — documented records and the hover glossary
- `orgs.py` — organisation directory (includes all 29 banks on the FSB's 2025 list)
- `pages.py` — title, About and Method text
- `build.py` — assembles everything into `finance.html`; checks every figure quoted from the country data against the data (paths inside are those of the build machine and need adjusting)
- `data/wb.json` — World Bank indicators downloaded from api.worldbank.org on 27 November 2026 (latest year per country)
- country series also read from `../central-bank-src/out/core.json` (Romelli index) and `extra.json` (Laeven-Valencia crises, Financial Secrecy Index 2025)
- `make_plate.py`, `plate.webp`, `cinzel.ttf` — the Atlas basemap plate with this map's cartouche (Cinzel, SIL Open Font License)
- `notes.md` — checked facts and their source links

Engine changes made in `build.py`: Atlas is the default basemap; lines between places no longer wrap across the Pacific edge; legends can carry their own labels.
