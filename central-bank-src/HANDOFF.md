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
pip install pandas openpyxl shapely pycountry --break-system-packages
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
  - **"Patterns behind the scenes":** 17 patterns from `agents/patterns.json`. They explain the pattern as the field describes it, from studies and inquiries; the map's records are a sample of it, and the writeup must not count or describe them. "What this means" comes from `agents/implications.json` or the pattern's own `implications`. Each opens as a dropdown under its row. `agents/role_info.json`, or a pattern's own `role_info`, holds the info text for each key row.
- **Network** (`build_net.py` → `out/net.json`):
  - Nodes are parties placed at their true head office, using `agents/hq.json` and GeoNames.
  - Parties sharing an address fan out by a pixel offset only, so true positions never move.
  - Links: `{n, cb | tn, rel, role, detail, src_t, src_u}`.
  - Popups turn each link into a plain sentence (`SAY` / `sayLink` / `srcItem` in `app.js`). Add a `SAY` entry for any new `role` string.

## Data files to add to (`agents/`)
| File | Holds | Records now |
|---|---|---|
| `corruption.json` | `cases` (iso3, central_bank, category, years, people, summary, status, source_title, source_url, weak_source) and `revolving_door` | 194 cases at 128 banks; 97 revolving-door records |
| `events_gold.json` | `events`: governor firings, pressure and moves against banks, 1990s–Oct 2026; plus gold storage | 88 events |
| `owners.json` | `holdings` (named shareholders with shares, %, as_of, source), `bis_members`, `history` | 228 holdings; all 63 BIS members |
| `networks.json` | `links` (entity, type, hq, cb_iso3, relation, detail, source) and `g30` members | 277 links; 56 G30 members |
| `parties.json` | Parties named in cases and events, with head offices | 740 links |
| `swaps.json` | Swap lines (provider, counterparty, amount, dates, status, source) | 229 |
| `gaps.json` | Fed and South Africa holders, Greece, Türkiye share classes, auditors, case updates | 41 auditors at 32 banks |
| `hq.json` | Head-office city and country for each party | – |
| `patterns.json`, `implications.json` | The patterns and their plain-language meanings | 17 |

Altogether the map has 977 parties and 1302 ties. `agents/work/research_log_2026-11.json` lists what was searched with no result, unopened leads, and records dropped after review.

## Rules the user holds to
- **No fabrication.** Every record needs a readable source URL that states the fact. Mark Wikipedia-only items `weak_source: true`. List acquittals but don't count them. Claims resting on one author go in as "claim, not confirmed."
- **Don't filter datasets.** Include everything a source publishes.
- **Plain words for a novice.** Show the case, figure or mechanism instead of characterizing it. No purple prose.
- **Colors:** no orange, yellow or neon; earthy, muted palettes.
- **Behavior to keep:** tables never need sideways scrolling, chart windows open centered, and markers never cluster or bunch.

## Rules added Nov 2026
- WebFetch has a shared hourly limit. Eight research agents at once used it up in minutes. Run a few at a time, each capped at about 25 fetches.
- `charge withdrawn` and `investigation closed` are also listed and not counted.
- The box under Find a place is the index (`indexItems`, `drawIndex`). The filter by connections is `netVis`/`linkOK`, with `S.netMin` and `S.netCb`.
- The details box is positioned in pixels by `openDet`, and drags by its top edge.
- Hover uses small sources of its own (`hot-lines`, `hot-nodes`); never re-filter the country layer on hover. `setP`/`setF` skip repeated paint and filter calls. Each party has one fixed spot computed in `build_net.py`: the city point, or a spot about 1 to 8 km around it, over land. Never use screen-pixel offsets; markers must not move with zoom. Clicking a stack opens a list (`stackBox`).
- For tests, the hook must use getters for consts: `get ALLREL(){return ALLREL}`, and never push it.
- Status `case dismissed` means a civil claim thrown out or a trial ended without a verdict. Like `acquitted`, it is listed and not counted.
- A record with `public_move: true` (IMF or World Bank) is listed but not counted as a move to or from private finance.
- Union banks use iso3 BEAC, BCEAO or ECCB in cases, which show on every member country. Their party links use the head-office country (CMR, SEN, KNA).
- Staff below senior management: the role instead of the name, unless the name matters to the case.
- An outsider's failed attempt against a bank is not a case. Check `events_gold.json` for firings and political prosecutions before filing them as corruption.

## Where coverage is thinnest (what to add next)
These are rough estimates. No complete count exists for any of these categories.

| Area | On the map | Rough share of what is documented |
|---|---|---|
| Datasets and indices (independence law, CPI, WGI, Basel, FSI, crises, BIS, COFER, Swift, gold, regimes) | Everything each source publishes | ~100% |
| Named shareholders | Every list a bank publishes. The other 11 Fed Reserve Banks don't publish one, and the SARB names none of its roughly 800 holders. | ~90% of what is published |
| Swap lines | 229 records (only lines known to be in force are drawn) | ~70–80% |
| Governor firings and pressure | 88 | ~30–40% since 2019, less before |
| Corruption cases at central banks, 1990–2026 | 194 at 128 banks | ~30–40% |
| Banknote printers and their clients | 43 ties | ~20% |
| External auditors | 32 banks | ~20% |
| Revolving door (officials to or from private finance) | 97 records | ~15% |
| Outside reserve and fund managers | 107, mostly Norway's fund | ~5% outside Norway |

Next steps, in order:
1. Corruption cases: open `round3.cases.leads_not_opened` in the research log, then the banks searched by title only (Bahrain, Oman, Palestine, Qatar, Saudi Arabia, Singapore, Taiwan, Brunei, Macao, Samoa, Cambodia, Fiji and others).
2. Revolving-door moves still missing: see `later_todo` in the research log, and past Fed governors and Reserve Bank presidents.
3. Governor dismissals: open `round3.events_leads` in the research log.
4. Auditors and printers: `round2.service_not_found` and `round3.service_not_found` list banks tried.
5. Swap lines: `round2.swap_leads` were opened; look for new sources. Status `unknown` lines are listed in boxes, not drawn.
