# stock_market.html — The Going Price

Source for `stock_market.html`, built on the shared story-map engine (taken from `religion.html`), with the design of `environmental_law.html`.

- `story_a.py`, `story_b.py` — parts, chapters and slides; every figure is tied to the link in `src`
- `exchanges.py` — the stock exchanges layer: 138 exchanges joined from the two lists in `data/`, each placed in its headquarters city
- `orgs.py` — the directory of bodies (exchange entries are written from the exchange data)
- `records.py` — documented records and the hover glossary
- `pages.py` — title, About and Method text
- `build.py` — assembles everything into `stock_market.html` and checks every quoted figure against the data (paths inside are those of the build machine and need adjusting)
- `data/wfe.json`, `data/wfe_by.json` — World Federation of Exchanges, Market Statistics, November 2026 issue (figures for September 2026)
- `data/sse.json` — UN Sustainable Stock Exchanges initiative, Stock Exchange Database, downloaded 27 November 2026
- `data/wb.json` — World Bank indicators CM.MKT.LDOM.NO, CM.MKT.LCAP.GD.ZS, CM.MKT.LCAP.CD, CM.MKT.TRAD.GD.ZS, CM.MKT.TRNR, downloaded 27 November 2026
- `make_plate.py`, `plate.webp`, `cinzel.ttf` — the Atlas basemap plate with this map's cartouche (Cinzel, SIL Open Font License)
- `notes.md` — checked facts and their source links

Engine changes made in `build.py`: Atlas is the default basemap; lines between places do not wrap across the Pacific edge; the points layer is the exchanges, sized by listed value, with a card on hover or click; unused layer code from the template is removed.
