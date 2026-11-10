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
  - **"Who owns, pays and pressures central banks":** multi-select checkboxes for 7 kinds of tie (`REL`: own, corrupt, people, inst, control, service, account) plus the "Filter by connections with central banks" block under the rows and a key with no title.
  - **"Patterns behind the scenes":** 17 patterns from `agents/patterns.json`. They explain the pattern as the field describes it, from studies and inquiries; the map's records are a sample of it, and the writeup must not count or describe them. "What this means" comes from `agents/implications.json` or the pattern's own `implications`. Each opens as a dropdown under its row. `agents/role_info.json`, or a pattern's own `role_info`, holds the info text for each key row.
- **Network** (`build_net.py` → `out/net.json`):
  - Nodes are parties placed at their true head office, using `agents/hq.json` and GeoNames.
  - Parties sharing an address fan out by a pixel offset only, so true positions never move.
  - Links: `{n, cb | tn, rel, role, detail, src_t, src_u}`.
  - Popups turn each link into a plain sentence (`SAY` / `sayLink` / `srcItem` in `app.js`). Add a `SAY` entry for any new `role` string.

## Data files to add to (`agents/`)
| File | Holds | Records now |
|---|---|---|
| `corruption.json` | `cases` (iso3, central_bank, category, years, people, summary, status, source_title, source_url, weak_source) and `revolving_door` | 232 cases at 135 banks; 111 revolving-door records |
| `events_gold.json` | `events`: governor firings, pressure and moves against banks, 1990s–Nov 2026; plus gold storage | 102 events in 52 countries |
| `owners.json` | `holdings` (named shareholders with shares, %, as_of, source), `bis_members`, `history` | 228 holdings; all 63 BIS members |
| `networks.json` | `links` (entity, type, hq, cb_iso3, relation, detail, source) and `g30` members | 307 links (45 printer ties, 107 reserve-manager ties); 56 G30 members |
| `parties.json` | Parties named in cases and events, with head offices | 891 links |
| `swaps.json` | Swap lines (provider, counterparty, amount, dates, status, source) | 240 (100 in force) |
| `gaps.json` | Fed and South Africa holders, Greece, Türkiye share classes, auditors, case updates | 47 auditors at 38 banks |
| `hq.json` | Head-office city and country for each party | – |
| `patterns.json`, `implications.json` | The patterns and their plain-language meanings | 17 |

Altogether the map has 1,164 parties and 1,565 ties, and `agents/writeups.json` holds 1,393 plain-language paragraphs, one for every box. `agents/work/research_log_2026-11.json` lists what was searched with no result, unopened leads, and records dropped after review.

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
| Swap lines | 240 records, 100 in force (only those are drawn) | ~70–80% |
| Governor firings and pressure | 102 in 52 countries | ~35–45% since 2019, less before |
| Corruption cases at central banks, 1990–2026 | 232 at 135 banks | ~35–45% |
| Banknote printers and their clients | 45 ties | ~20% |
| External auditors | 47 records at 38 banks | ~25% |
| Revolving door (officials to or from private finance) | 111 records in 26 countries | ~15–20% |
| Outside reserve and fund managers | 107, mostly Norway's fund | ~5% outside Norway |

Next steps, in order:
1. **Corruption cases.** Round 4 opened almost every lead that earlier rounds left. What is left: `round4.cases_*.searched_none` names banks searched with nothing found (Bahrain, Oman, Qatar, Saudi Arabia, Singapore, Taiwan, Brunei, Macao, Samoa, Fiji and others), usually from result titles alone, so they are worth a second try in the local language. San Marino's Confuorti and Buriani rulings need a court or news source; only a councillor's speech was found.
2. **Revolving door.** `round4.rd.leads_not_opened` (11) and `round4.rd.checked_none` (names whose biographies name no private employer). Still unchecked: Reserve Bank presidents before 2000, and non-US central banks other than the ECB, Bank of Japan and Bank of England.
3. **Governor dismissals.** `round4.events.leads_not_opened` (17). Several Central Banking pages are paywalled after the first paragraph.
4. **Auditors and printers.** `round4.service.not_found` (9): Egypt, Saudi Arabia, Vietnam, Bangladesh, the Philippines, Japan, Peru, Denmark and Indonesia. The Philippine and Peruvian sites block automated readers; Brazil's row is from the 2018 statements, the only ones that would open.
5. **Swap lines.** `round4.swaps.leads_not_opened` (13). The PBoC's own current table (30 September 2025) lists 32 counterparties and omits exactly the 11 lines the map marks "unknown" (Albania, Armenia, Belarus, Georgia, Kazakhstan, Morocco, Nepal, Suriname, Tajikistan, Ukraine, Uzbekistan). That is evidence they lapsed, but the table says nothing in words, so the records were left alone. A source that says so plainly would settle them.
6. **Open question for the user:** 22 cases have status `alleged` and currently count toward the scores. Acquittals, dismissals, withdrawn charges and closed investigations do not count. Ask whether unproven allegations should count.

## Added in earlier rounds (UI)
- **Writeups:** `agents/writeups.json` holds a plain-language paragraph for every country box (`p:ISO`) and every party box (`n:<node name>`), injected as `D.WR` and shown at the top of the box (`.wr`). They were written from each box's records and checked by script for numbers and outcomes, not re-checked against web sources. **When a record changes or a party is added, refresh that entry by hand.** A country or party with no entry just shows the lists.
- **Hover:** only diamonds light their ties; lines take no hover or click. `hoverCountry(k)` lights a country's lines (`LK`, `lk()`) and the countries at the far ends (source `hov-ctry`, layer `c-hovto`).
- **Anchors:** `anchorsOf` reads multi-currency anchors, so Belarus (0.2 EUR + 0.5 RUB + 0.3 USD) draws to Moscow. Ilzetzki-Reinhart-Rogoff give "n.a." for Russia and 19 others, which is why they have no outgoing line.
- **Recenter:** `#centerBtn` runs `recenter()`; `homePadding()` removes the padding a box adds.
- **Pattern points:** `pat-end` features carry a name, `under()` returns `{pat}`, `patPointBox(name)` opens the box.
- **Index:** `selectEntity` turns ties on if the party is hidden and draws a ring (`drawSel`, source `sel-node`, layer `sel-ring`).
- **Resize:** `makeResizable(el, onStart)` adds 8 handles (`.rz-*`) to `#det` and `.win`. `#det` no longer scrolls; `#detBody` does.
- **Small places:** `build_final.py` adds real outlines from `ne10` (`D.XSHAPE`) for places missing from the boundaries file: Monaco, Tuvalu, Nauru.
- **Career-move boxes:** in `build_net.py`, when the move line doesn't name the party, the box also shows the record's summary.

## How to refresh the writeups after adding records (do this every round)
A writeup never updates itself, and two things make old ones wrong:
1. New records for that place or party.
2. **Scores shift across the whole map.** The inside-influence score counts documented cases against the highest count anywhere (`MAXCC` in `app.js`), so adding cases in one country moves the headline score of others by a point or two. After round 4, 55 paragraphs quoted a number that had moved.

The routine, after merging new records and rebuilding:
```bash
S=<scratchpad>   # mk_t3.py, t_dump.py and t_sc.py are kept in agents/work/
python3 $S/mk_t3.py /root/cb/dist/central_bank_independence.html $S/t/dump.html   # injects window.T and window.T3={detail,entityBox,L}
python3 $S/t_dump.py $S                 # writes $S/boxes.json: every box's text, keyed p:ISO and n:<name>
python3 $S/t_sc.py <old build> $S/sc_old.json && python3 $S/t_sc.py <new build> $S/sc_new.json
```
Then compare: keys in `boxes.json` with no entry in `writeups.json` are new, and any place whose rounded score changed and whose paragraph quotes the old number is stale. Give those box texts to writer agents with `scratchpad/r4/brief_writeups.md`, about 25 keys each, and merge the results into `agents/writeups.json`. Check the drafts by script for: numbers that do not appear in the box text, the phrases "the box", "the record", "does not say", "on the map", and the word "our".

## Round 4 (10 November 2026), what it added
38 corruption cases, 14 career moves, 14 governor-removal or pressure events, 6 auditors, 3 state printers and 11 swap lines, from the leads earlier rounds had left unopened. New countries on the case list: São Tomé and Príncipe, Eswatini, the Cayman Islands, the Dominican Republic, the Gambia, Libya, Madagascar, Slovenia, Trinidad and Tobago, Cambodia, Israel, South Korea and Uruguay. 185 writeups were rewritten or written fresh.
