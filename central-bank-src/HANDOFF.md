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
| `corruption.json` | `cases` (iso3, central_bank, category, years, people, summary, status, source_title, source_url, weak_source) and `revolving_door` | 232 cases in 135 countries and territories; 138 revolving-door records in 48 |
| `events_gold.json` | `events`: governor firings, pressure and moves against banks, 1990s–Nov 2026; plus gold storage | 102 events in 52 countries |
| `owners.json` | `holdings` (named shareholders with shares, %, as_of, source), `bis_members`, `history` | 228 holdings; all 63 BIS members |
| `networks.json` | `links` (entity, type, hq, cb_iso3, relation, detail, source) and `g30` members | 307 links (45 printer ties, 107 reserve-manager ties); 56 G30 members |
| `parties.json` | Parties named in cases and events, with head offices | 891 links |
| `swaps.json` | Swap lines (provider, counterparty, amount, dates, status, source) | 240 (100 in force) |
| `gaps.json` | Fed and South Africa holders, Greece, Türkiye share classes, auditors, case updates | 49 auditors at 39 banks. More audit ties live in `networks.json` — check both. |
| `hq.json` | Head-office city and country for each party | – |
| `patterns.json`, `implications.json` | The patterns and their plain-language meanings | 17 |

Altogether the map has 1,191 parties and 1,606 ties, and `agents/writeups.json` holds 1,420 plain-language paragraphs, one for every box. `agents/work/research_log_2026-11.json` lists what was searched with no result, unopened leads, and records dropped after review.

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
- `alleged` means publicly accused with no charge filed, no inquiry reported and no court ruling. `S.alleged` decides whether those count; `ccN` and `MAXCC()` both read it, and the two score caches are keyed on it. `MAXCC` is now a function, not a constant.
- With the tick box cleared, a bank whose only cases are allegations stays on the inside layer, scored at nothing for cases, rather than dropping off it. Its writeup then carries a line saying any score in the paragraph was written with allegations counted.
- An outsider's failed attempt against a bank is not a case. Check `events_gold.json` for firings and political prosecutions before filing them as corruption.

## Where coverage is thinnest
These are rough estimates. No complete count exists for any of these categories. The same table, written for a reader, is in `about.html` under "How much of the subject is here"; **change both together.**

| Area | On the map | Rough share of what is documented |
|---|---|---|
| Datasets and indices (independence law, CPI, WGI, Basel, FSI, crises, BIS, COFER, Swift, gold, regimes) | Everything each source publishes | ~100% |
| Named shareholders | Every list a bank publishes. The other 11 Fed Reserve Banks don't publish one, and the SARB names none of its roughly 800 holders. | ~90% of what is published |
| Swap lines | 240 records, 100 in force (only those are drawn) | ~70-80% |
| Governor firings and pressure | 102 in 52 countries | ~35-45% since 2019, less before |
| Corruption cases at central banks, 1990-2026 | 232 in 135 countries and territories | ~35-45% |
| External auditors | 49 records at 39 banks in `gaps.json`, plus more in `networks.json` | ~25% |
| Banknote printers and their clients | 44 printing contracts, 1 paper maker, 1 substrate supplier | ~20% |
| Revolving door (officials to or from private finance) | 138 records in 48 countries | ~15-20% |
| Outside reserve and fund managers | 107, mostly Norway's fund | ~5% outside Norway |

## What is left, and how to finish it
In the order worth doing. The first is where most of the undiscovered material is; the last two are nearly done.

### 1. Revolving door — worked hard in rounds 5 to 10, and now the shallowest it has been
**The method that works:** go to the central bank's own governor or board page, or to the private firm's own board page, and read the career list. Do not search for scandal. Almost every record added in rounds 6 to 10 came from one search and one fetch of an official page. Where a bank publishes nothing, the firm the official joined usually does: Nordea, Swiss Re, DSK Bank and Erste Bank Hungary each supplied a record this way.

Rounds 6 to 10 took the category from 117 records in 32 countries to **138 in 48**, adding a first record at Saudi Arabia, Thailand, the Philippines, Austria, Hungary, Colombia, the UAE, Greece, Ukraine, Serbia, Norway, Ireland, Belgium, Denmark, Poland and Bulgaria.

**Before opening any lead, search `corruption.json` for the person's name.** Round 4's leads list was stale: four of its eleven entries were facts already recorded.

Still with no record at all: **Singapore, Peru, Finland, Slovakia, Croatia**, Malaysia beyond the two held. Croatia and Finland were both tried in round 10 and yielded nothing usable — the HNB's vicegovernor page names no private firm, and the only source for Sirkka Hamalainen's later board seats is Wikipedia. **US Reserve Bank presidents before 2000** is the one closed set left; three were added in round 8 by name, but the Federal Reserve History people index returns only its filter controls to an automated reader, so the rest have to be reached through each Reserve Bank's own history page.

Watch for: a move to or from the IMF or World Bank needs `public_move: true`, which lists it without counting it. Sovereign wealth funds, statutory pension bodies (Denmark's ATP) and cantonal or state-owned banks (the Geneva Cantonal Bank) are public too, so the record should say which side of a career is private. Staff below senior management go in by role, not name.

**The denominator moves.** The inside-influence score divides each country's revolving-door count by the highest count anywhere, which the United States holds. Round 8 added three US records and every other country's share fell, changing the rounded figure in Australia, Ireland and Slovakia. Any round that adds to the country holding the maximum has to re-check the whole map.

### 2. Governor dismissals — the next category worth a full round
`round4.events.leads_not_opened` (17) is still the live list. Several Central Banking pages are paywalled after the first paragraph, so prefer the bank's own release, the government gazette or a wire agency. Before filing anything here as corruption, check `events_gold.json` — a political prosecution of a governor is an event, not a case.

### 3. Auditors and printers
Still with no auditor anywhere on the map: **Egypt, Saudi Arabia, Vietnam, Bangladesh, the Philippines, Peru.** The Philippine and Peruvian sites block automated readers; Brazil's row is from the 2018 statements, the only ones that would open. **Check both `gaps.json` and `networks.json` before searching** — the two files both feed the audit ties and the old gap list only tracked one, which is why Japan, Denmark and Indonesia sat on a to-do list while already being on the map.

Where a bank has no private auditor, its law names who does audit it, and that is a record in its own right: China's National Audit Office, Korea's Board of Audit and Inspection and presidentially appointed auditor, Japan's Cabinet-appointed Auditors. Korea's Bank Act also requires an outside accounting-firm audit without naming the firm; that stays in `auditors_unavailable` until a firm is found.

### 4. Swap lines
`round4.swaps.leads_not_opened` (13). The PBoC's own current table (30 September 2025) lists 32 counterparties and omits exactly the 11 lines the map marks "unknown" (Albania, Armenia, Belarus, Georgia, Kazakhstan, Morocco, Nepal, Suriname, Tajikistan, Ukraine, Uzbekistan). That is evidence they lapsed, but the table says nothing in words, so the records were left alone. A source that says so plainly would settle all 11 at once.

### 5. Corruption cases — treat as near-exhausted by ordinary search
Round 4 opened almost every lead earlier rounds left. Round 5 retried Bahrain, Saudi Arabia, Oman, Taiwan and Singapore in Arabic, Chinese and English and found nothing on any central bank official: every hit was a commercial-bank employee, an unrelated political case, or the central bank acting as supervisor or investigator. Saudi Arabia is the clearest example — Nazaha publishes its cases and names SAMA repeatedly as the authority it cooperates with, never as the body investigated.

**Don't spend another round on local-language retries.** If this category is taken further, it needs a different kind of source: court bulletins, supreme audit institution reports, parliamentary questions, central bank annual reports' own disciplinary notes. Still with no case and not yet retried at all: UAE, Qatar, Jordan, Brunei, Macao, Samoa, Fiji. San Marino's Confuorti and Buriani rulings still need a court or news source; only a councillor's speech was found.

## Questions the user has settled (don't reopen)
- **Unproven allegations** (10 November 2026). Show both and let the reader switch. A tick box, "Count cases that are allegations alone", sits under the legend on the three case layers (`all`, `inside`, `cc`, marked `alleg: true`). It is ticked by default, so every score and writeup reads as it did before; clearing it recomputes without them. With it cleared, a bank whose only cases are allegations stays on the inside layer scored at nothing for cases rather than dropping off, and its box carries a line saying any score in the paragraph above was written with allegations counted.
- **Which statuses count** (10 November 2026). One rule: **a case stops counting only when the official was cleared, or when the charge is gone and no finding is left standing.** Anything still running counts, and so does a case whose ending no source states, because an outcome nobody can find is not a clearing. So `outcome not found` (Kenya, Serbia), `died; outcome not found` (Iraq), `tried (verdict not found)` (Russia) and `Sejm vote pending` (Poland) count; `acquitted`, `case dismissed`, `charge withdrawn`, `investigation closed` and `conviction annulled (time-barred)` (Romania) do not. Romania is the one genuine edge — Olteanu was convicted with a final five-year sentence in October 2020, the conviction was annulled as time-barred on 31 March 2023, and the court still confiscated the €1 million. It is left out because no conviction stands, and its writeup gives all three facts. **If that call is ever reversed, it is one string to move between the two lists in `app.js` (`CC_OUT`) and `build_final.py` (`CC_COUNTED` / `CC_NOT_COUNTED`).**
- `build_final.py` now refuses to build on a case status that is on neither list, so a `gaps.json` update can no longer invent a wording that counts by accident. That is what let Ghana's "charges withdrawn" count. Adding a status means deciding which list it belongs on and changing both files.

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

## What each round added

- **Round 4** (10 Nov 2026): 38 corruption cases, 14 career moves, 14 governor-removal or pressure events, 6 auditors, 3 state printers, 11 swap lines. New countries on the case list: Sao Tome and Principe, Eswatini, the Cayman Islands, the Dominican Republic, the Gambia, Libya, Madagascar, Slovenia, Trinidad and Tobago, Cambodia, Israel, South Korea, Uruguay. 185 writeups rewritten.
- **Round 5**: settled the allegations question and the undecided statuses (both under "Questions the user has settled"). Fixed the Ghana status bug and added `build_final.py`'s status guard. Korea's two statutory audits. Six revolving-door records (Canada, New Zealand, Nigeria, Argentina, Egypt, Czechia). Added "How much of the subject is here" to `about.html`.
- **Round 6**: six revolving-door records, all at banks with none — Saudi Arabia (Al-Mubarak, Rana Investment and Morgan Stanley Saudi Arabia), Thailand (Sethaput, SCB group and TMB), the Philippines (Buenaventura, Citibank and PCIB), Austria (Nowotny, BAWAG P.S.K.), Hungary (Jarai, James Capel, Samuel Montagu, MHB, ABN-AMRO, CIG Pannonia) and Colombia (Villar, IMF, `public_move`). Korea's two auditors finally got writeups.
- **Round 7**: the UAE (Saeed, First Abu Dhabi Bank), Greece (Provopoulos, Alpha, Emporiki, Piraeus), Ukraine (Gontareva, Societe Generale, ING, ICU), Serbia (Jelasic to Erste Bank Hungary), Thailand again (Veerathai, Siam Commercial Bank). Banorte dates added to the existing Ortiz record.
- **Round 8**: Norway (Tangen, AKO Capital to NBIM, with the conditions the bank attached), Ireland (Elderfield to Lloyds) and the first three pre-2000 Fed moves (Corrigan to Goldman Sachs, McDonough from First Chicago and later to Merrill Lynch, Melzer from Morgan Stanley). This is the round that moved scores map-wide.
- **Round 9**: Belgium (Dechaene, Bank Brussel Lambert, Morgan Grenfell, Deutsche Bank London), Denmark (Rohde, Realkredit Danmark and later the Nordea board), Poland (Filar, Bank Pekao).
- **Round 10**: Switzerland (Roth to the Swiss Re board in 2010) and Bulgaria (Hristov to the DSK Bank supervisory board in August 2025).

## Hard-won notes, so they are not learned twice

- **Check `corruption.json` for a person's name before opening a lead.** Round 4's leads list contained four facts already on the map.
- **The Federal Reserve History people index does not render for an automated reader.** It reports 246 profiles and returns only the filter controls. Reach presidents through each Reserve Bank's own history page instead.
- **The MAS board annex that search returns is not the MAS board.** It is the board of a payments body the authority chairs, with DBS, OCBC, UOB and Standard Chartered representatives on it. Banks sitting on that body is a different kind of tie from a revolving door and was not recorded.
- **A source that names an employer without saying it is private settles nothing.** Peru's Velarde is listed at the Banco de Industria y Construccion and the Banco Central Hipotecario, but the Banco Central Hipotecario was state-owned and the source says nothing about ownership, so Peru is still blank.
- **"In talks" is not an appointment.** RTE had Lloyds only in talks over Elderfield with all parties declining to comment; the Irish Times report two weeks later is the one cited.
- **Where a bank publishes no bio, the firm usually does.** Nordea, Swiss Re, DSK Bank and Erste Bank Hungary each supplied a record their central bank's own site did not.
- **Refresh the writeups every round.** The routine is under "How to refresh the writeups after adding records". Check each changed country's paragraph for a quoted score, and check the United States paragraph's count of recorded moves, which is written out as a number.
