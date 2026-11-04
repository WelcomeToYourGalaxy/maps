# Handoff: Central bank capture map

Paste or attach this in a new chat to carry on adding to the map.

## What it is
- A standalone global map titled **"Central bank capture"**. It shows who owns and steers each central bank, what it hides, the corruption inside and around it, and how far its money reaches beyond its borders.
- **Live:** https://welcometoyourgalaxy.github.io/maps/central_bank_independence.html (embedded on the Weebly site; keep this file name).
- **Repo:** `WelcomeToYourGalaxy/maps`. The built file `central_bank_independence.html` is at the root. The full build source is in `central-bank-src/` (this folder).
- **Standing instruction:** push updates straight to `main` from chat. Don't ask the user to upload anything.

## How to rebuild
The scripts use the hard-coded path `/root/cb`.

```bash
cd ~ && git clone https://github.com/WelcomeToYourGalaxy/maps && cp -r maps/central-bank-src /root/cb
cd /root/cb/geo && unzip -o cities1000.zip      # GeoNames cities, used to place head offices
pip install pandas openpyxl shapely --break-system-packages
cd /root/cb && python3 build_final.py           # also runs build_net.py; writes dist/central_bank_independence.html
cp dist/central_bank_independence.html ~/maps/   # then git add, commit, push to main
```

- `out/core.json` and `out/extra.json` are already built from the downloaded datasets. Only rerun `build_core.py` / `build_extra.py` when refreshing those datasets. Their raw downloads (about 200 MB: Romelli, Garriga, CPI, WGI, Basel, FSI, Laeven–Valencia, BIS, COFER, Swift, Ilzetzki–Reinhart–Rogoff) are not in the repo. Each source and its URL is listed in `about.html`.
- **Testing:** `python3 shot2.py "<js step>" "<js step>"` takes a screenshot after each step, saved to `shots/s{i}.png`, and prints page errors. It uses headless Chromium with swiftshader. App functions are scoped, so for tests temporarily inject `window.T={selectEntity,select,openWin,NET}` into the built file, and never push that version.
- **Commits** end with the attribution lines the session supplies.

## How it is built
- `template.html` holds the layout and CSS. `app.js` holds all map logic (MapLibre GL 5 globe/flat, the shared Culprits basemaps in `basemaps.js`, `plate.js`). `about.html` is the "About and sources" text.
- `build_final.py` merges `out/*.json` with the hand-compiled files in `agents/` and injects `const D = {...}` into the template.
- **Layers:** `seq()` / `cat()` in `app.js` push objects onto `L` (`id, group, label, get(p,y), desc, src`). Values are cached; call `clearCache()` after changing what a layer depends on.
- **Top-left dropdown:** the compilation layers (the default is "Ulterior influence, all around"), corruption, independence, reach, "Whose money it is" and the exchange-rate regime.
- **Bottom-right box** (`SIDE_GROUPS`) has two sections:
  - **"Who central banks answer to":** multi-select checkboxes for 7 kinds of tie (`REL`: own, corrupt, people, inst, control, service, account) plus a "What the map shows now" key.
  - **"Patterns behind the scenes":** 14 patterns from `agents/patterns.json`, each with a "What this means" text from `agents/implications.json`.
- **Network** (`build_net.py` → `out/net.json`):
  - Nodes are parties placed at their true head office, using `agents/hq.json` and GeoNames.
  - Parties sharing an address fan out by a pixel offset only, so true positions never move.
  - Links: `{n, cb | tn, rel, role, detail, src_t, src_u}`.
  - Popups turn each link into a plain sentence (`SAY` / `sayLink` / `srcItem` in `app.js`). Add a `SAY` entry for any new `role` string.

## Data files to add to (`agents/`)
| File | Holds | Records now |
|---|---|---|
| `corruption.json` | `cases` (iso3, central_bank, category, years, people, summary, status, source_title, source_url, weak_source) and `revolving_door` | 111 cases in 69 countries; 13 revolving-door records |
| `events_gold.json` | `events`: governor firings, pressure and moves against banks, 2019–Oct 2026; plus gold storage | 39 events |
| `owners.json` | `holdings` (named shareholders with shares, %, as_of, source), `bis_members`, `history` | 228 holdings; all 63 BIS members |
| `networks.json` | `links` (entity, type, hq, cb_iso3, relation, detail, source) and `g30` members | 277 links; 56 G30 members |
| `parties.json` | Parties named in cases and events, with head offices | 379 links |
| `swaps.json` | Swap lines (provider, counterparty, amount, dates, status, source) | 104 |
| `gaps.json` | Fed and South Africa holders, Greece, Türkiye share classes, auditors, case updates | 14 auditors |
| `hq.json` | Head-office city and country for each party | – |
| `patterns.json`, `implications.json` | The 14 patterns and their plain-language meanings | 14 |

Altogether the map has 753 parties, 990 ties, and ties for 130 of 229 places.

## Rules the user holds to
- **No fabrication.** Every record needs a readable source URL that states the fact. Mark Wikipedia-only items `weak_source: true`. List acquittals but don't count them. Claims resting on one author go in as "claim, not confirmed."
- **Don't filter datasets.** Include everything a source publishes.
- **Plain words for a novice.** Show the case, figure or mechanism instead of characterizing it. No purple prose.
- **Colors:** no orange, yellow or neon; earthy, muted palettes.
- **Behavior to keep:** tables never need sideways scrolling, chart windows open centered, and markers never cluster or bunch.

## Where coverage is thinnest (what to add next)
These are rough estimates. No complete count exists for any of these categories.

| Area | On the map | Rough share of what is documented |
|---|---|---|
| Datasets and indices (independence law, CPI, WGI, Basel, FSI, crises, BIS, COFER, Swift, gold, regimes) | Everything each source publishes | ~100% |
| Named shareholders | Every list a bank publishes. The other 11 Fed Reserve Banks don't publish one, and the SARB names none of its roughly 800 holders. | ~90% of what is published |
| Swap lines | 104 | ~50–60% |
| Governor firings and pressure, 2019–2026 | 39 | ~30–40% |
| Corruption cases at central banks, 1990–2026 | 111 in 69 countries | ~20–30% |
| Banknote printers and their clients | 16 ties | ~10% |
| External auditors | 14 banks | ~10% |
| Revolving door (officials to or from private finance) | 13 records plus 77 people ties | under 5% |
| Outside reserve and fund managers | 107, mostly Norway's fund | ~5% outside Norway |

Next steps, in order:
1. Corruption cases in the 110 or so central banks with none yet.
2. Revolving-door moves for the Fed, ECB, BoE and BoJ, and IMF/World Bank staff, starting with governors and board members.
3. Governor dismissals before 2019 and outside Türkiye and the US.
4. Auditors and banknote printers for every bank that names them in its annual report.
5. Chinese and regional swap lines.
