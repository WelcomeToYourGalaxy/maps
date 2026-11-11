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
| `corruption.json` | `cases` (iso3, central_bank, category, years, people, summary, status, source_title, source_url, weak_source) and `revolving_door` | 232 cases in 135 countries and territories; 133 revolving-door records in 44 |
| `events_gold.json` | `events`: governor firings, pressure and moves against banks, 1990s–Nov 2026; plus gold storage | 102 events in 52 countries |
| `owners.json` | `holdings` (named shareholders with shares, %, as_of, source), `bis_members`, `history` | 228 holdings; all 63 BIS members |
| `networks.json` | `links` (entity, type, hq, cb_iso3, relation, detail, source) and `g30` members | 307 links (45 printer ties, 107 reserve-manager ties); 56 G30 members |
| `parties.json` | Parties named in cases and events, with head offices | 891 links |
| `swaps.json` | Swap lines (provider, counterparty, amount, dates, status, source) | 240 (100 in force) |
| `gaps.json` | Fed and South Africa holders, Greece, Türkiye share classes, auditors, case updates | 49 auditors at 39 banks. More audit ties live in `networks.json` — check both. |
| `hq.json` | Head-office city and country for each party | – |
| `patterns.json`, `implications.json` | The patterns and their plain-language meanings | 17 |

Altogether the map has 1,184 parties and 1,597 ties, and `agents/writeups.json` holds 1,413 plain-language paragraphs, one for every box. `agents/work/research_log_2026-11.json` lists what was searched with no result, unopened leads, and records dropped after review.

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
| Revolving door (officials to or from private finance) | 133 records in 44 countries | ~15-20% |
| Outside reserve and fund managers | 107, mostly Norway's fund | ~5% outside Norway |

## What is left, and how to finish it
In the order worth doing. The first is where most of the undiscovered material is; the last two are nearly done.

### 1. Revolving door — the thinnest category, and the most findable
Round 5 found that **the best source is the central bank's own appointment release or governor profile.** They state the private employer, often with exact years, and almost every bank publishes them. Round 5 added six this way, each in one search and one fetch: Canada (Carney, thirteen years at Goldman Sachs, from the Bank of Canada's own profile), New Zealand (Orr, Westpac chief economist 2000-2003 then deputy governor, exact years from the RBNZ release), Nigeria (Cardoso, former head of Citibank in Nigeria, Reuters), Argentina (Caputo, JP Morgan and Deutsche Bank, Chequeado), Egypt (Abdalla, vice chairman and managing director of the Arab African International Bank 2002-2018, from his Financial Stability Board profile) and Czechia (Michl, Raiffeisenbank 2006-2015, Czech Television). **The FSB's member profiles are a particularly good seam** — they are official, they give years, and they cover the governors of every FSB member bank.

**So work bank by bank through governor and board-member profiles, not by searching for scandal.** Start from the banks with no record at all: everything outside the 29 in the table above. The obvious next tier is the large banks with published bios — Switzerland beyond Hildebrand, Canada's other governors, Ireland, Austria, Belgium, Poland, Hungary, Colombia, Peru, the Philippines, Thailand, Malaysia beyond the two held, Singapore, Saudi Arabia, the UAE. Also still unchecked from round 4: `round4.rd.leads_not_opened` (11), `round4.rd.checked_none` (biographies naming no private employer), and **US Reserve Bank presidents before 2000**, which is a closed, listable set and should be finishable in one round.

Watch for: a move to or from the IMF or World Bank needs `public_move: true`, which lists it without counting it. A sovereign wealth fund is a public body too, so say which side of a career is private (Orr's Westpac years are the private side, not the NZ Super Fund). Staff below senior management go in by role, not name.

### 2. Governor dismissals
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

## Round 4 (10 November 2026), what it added
38 corruption cases, 14 career moves, 14 governor-removal or pressure events, 6 auditors, 3 state printers and 11 swap lines, from the leads earlier rounds had left unopened. New countries on the case list: São Tomé and Príncipe, Eswatini, the Cayman Islands, the Dominican Republic, the Gambia, Libya, Madagascar, Slovenia, Trinidad and Tobago, Cambodia, Israel, South Korea and Uruguay. 185 writeups were rewritten or written fresh.

## Round 5 (10 November 2026), what it added
No new corruption cases. Settled the allegations question and the undecided statuses (both above). Fixed the Ghana status bug: `gaps.json` had set it to "charges withdrawn", which the not-counted list did not match, so a withdrawn case was being counted — Ghana fell from 33 to 32 all-around and 21 to 17 inside. Added `build_final.py`'s status guard. Added Korea's two statutory audits from the Bank of Korea Act, and six revolving-door records (Canada, New Zealand, Nigeria, Argentina, Egypt, Czechia) at banks that had none. Added "How much of the subject is here" to `about.html`: the coverage table written for a reader, plus the map's totals and the record count behind each row; its styling is `#info table.cov` in `template.html`, which stacks into blocks below 620px so it never scrolls sideways.

Scores that moved, all checked against a clean build of the previous code: Ghana (the bug fix), Romania (23 to 21 all-around, 11 to 7 inside, and off the case layer), and Canada, New Zealand and Nigeria by under half a point each, too little to change any rounded figure. Argentina moved 39 to 40 all-around, Egypt 30 to 31, and Czechia 6 to 7 inside. Writeups rewritten by hand: Ghana, Romania, Korea, Canada, New Zealand, Nigeria, Argentina, Egypt, Czechia.


## Round 6 (10 November 2026), what it added
Six revolving-door records, every one at a bank that had none, all found the way round 5 recommended: go to the bank's own governor page or an official profile, not to scandal searches.

- **Saudi Arabia** — Fahad Al-Mubarak, general manager of Rana Investment Company 1992-1999 and chairman and managing director of Morgan Stanley Saudi Arabia, governor 2011-2016 and again from January 2021 (Arab News profile). The first record of any kind of this sort for SAMA.
- **Thailand** — Sethaput Suthiwartnarueput, from the Bank of Thailand's own governor page: SCB Asset Management president 2008-2009, Siam Commercial Bank Group executive vice president and chief economist 2009-2011, SCB Securities managing director and head of research, TMB Bank director 2011-2012.
- **Philippines** — Rafael Buenaventura, Citibank from 1965 with more than twenty years in its senior Asian and European posts, then chief executive of the Philippine Commercial Industrial Bank, governor 1999-2005 (Philippine Star).
- **Austria** — Ewald Nowotny, chief executive of BAWAG P.S.K. 2006-2007, OeNB governor from 2008 (Forum Alpbach biography).
- **Hungary** — Zsigmond Jarai: James Capel 1990-1993, Samuel Montagu 1993-1995, Hungarian Credit Bank 1995-1997, ABN-AMRO Hungary from 1998, CIG Pannonia from 2008 (Portfolio profile). **No central bank dates are stated in the record**: that profile gives 1998-2000 for the central bank post, which is the period other accounts give for his time as finance minister, and nothing better opened. A source for his governorship dates is still wanted.
- **Colombia** — Leonardo Villar, IMF executive director November 2018 to October 2020, general manager from January 2021, from the bank's own CV. `public_move: true`, so listed and not counted.

15 new party links, 10 new party nodes. Twelve writeups written fresh (the ten firms, plus Korea's Board of Audit and Inspection and its presidentially appointed auditor, which round 5 added without writeups) and the six country writeups extended by a sentence.

Scores that moved, checked against a clean build of the previous code: Austria inside 22.80 to 23.56 and Saudi Arabia inside 15.83 to 16.59, the only two that change a rounded figure. Hungary, the Philippines and Thailand each moved about a quarter point on the all-around score with no rounded figure changing, and Colombia did not move at all. **No other country shifted**, so unlike round 4 no older writeup went stale.

Two round-4 leads turned out to be already on the map and the leads list was stale: **Philip Lowe to Barrenjoey** and **Ian Macfarlane to the ANZ board**. Check `corruption.json` for the person's name before opening a lead.

Checked and left out: **Stephen Poloz** (Enbridge, CGI and a Bay Street law firm — none of them finance); **Julio Velarde of Peru** (La Republica lists him as manager of the Banco de Industria y Construccion and the Banco Central Hipotecario and a director of the Banco de Comercio and the Banco Financiero, but does not say whether any was private, and the Banco Central Hipotecario was state-owned).

**Mario Draghi's Goldman Sachs years sit under `EMU`**, with the central bank field reading "European Central Bank / Banca d'Italia", so Italy's own box does not carry them. The Banca d'Italia's own governor page states the same facts — Vice President and Managing Director of Goldman Sachs International 2002-2005, governor 29 December 2005 to 31 October 2011 — and is the stronger source if that record is ever moved or copied to `ITA`.

### Where round 7 should start on the revolving door
Banks still with no record and with published board bios: **Ireland, Belgium, Poland, Singapore, the United Arab Emirates, Peru, Malaysia beyond the two held, Switzerland beyond Hildebrand**. Named leads: **Veerathai Santiprabhob** (Bank of Thailand governor 2015-2020, reported Siam Commercial Bank chief strategy officer before the post — his BOT governor page should state it, same as Sethaput's did), **Guillermo Ortiz to Banorte** (the Expansion page returns a server error; another source needed), and the four round-4 URLs still unopened (two Fed president appointments, the WHYY piece on a Comcast executive named to the Fed board, Escriva's Banco de Espana CV, Joaquin Vial's farewell at the Banco Central de Chile). **US Reserve Bank presidents before 2000** remains a closed, listable set on the Federal Reserve History site and should finish in one round.


## Round 7 (10 November 2026), what it added
Five more revolving-door records, four of them the first at that bank, plus dates added to one existing record.

- **United Arab Emirates** — Abdulhamid Saeed, former board member and group chief executive of First Abu Dhabi Bank, governor by federal decree on 2 April 2020 (Gulf News). First for the Central Bank of the UAE.
- **Greece** — Georgios Provopoulos: economic adviser to Alpha Bank from 1993, a management role at Emporiki Bank from 2004 through its sale to Credit Agricole, vice president and chief executive of Piraeus Bank 2006-2008, governor June 2008 to 2014 (Protothema). First for the Bank of Greece.
- **Ukraine** — Valeria Gontareva: Societe Generale, ING Bank and Investment Capital Ukraine, from her LSE profile, which names the firms but gives no roles or years. First for the National Bank of Ukraine.
- **Serbia** — Radovan Jelasic, named chairman and chief executive of Erste Bank Hungary on 10 May 2011 (Budapest Business Journal). First for the National Bank of Serbia.
- **Thailand** — Veerathai Santiprabhob, Siam Commercial Bank PCL 2000-2008, ending as executive vice president and head of the business bank, strategic planning division, from the bank's own governor page. Note the correction: his chief strategy officer title was at the **Stock Exchange of Thailand**, 2009-2013, not at SCB.
- **Mexico** — the existing Ortiz record gained the Banorte dates it was missing (board approval October 2010, effective 1 March 2011, ratified April 2013; governor 1998-2009), from Expansion.

Seven new party boxes with writeups, five country writeups extended. Rounded figures that moved: Serbia all-around 27 to 28 and inside 6 to 7, Thailand all-around 37 to 38 and inside 12 to 13, Ukraine inside 11 to 12. The UAE and Greece moved by a quarter point without changing a rounded figure. Serbia's writeup was the only one quoting a number that had to change.

### The round 4 leads list is unreliable — check before opening
Four of its eleven revolving-door entries were already recorded: **Philip Lowe to Barrenjoey, Ian Macfarlane to the ANZ board, Escriva's BBVA years and Ortiz's Banorte chairmanship.** Search `corruption.json` for the person's name before spending a fetch on a lead.

Checked and yielded nothing: **Patrick Harker** (the Philadelphia Fed's own announcement names Wharton, the University of Delaware and board seats at Pepco Holdings and Huntsman Corp, no financial firm) and **Joaquin Vial** (the Banco Central de Chile farewell page covers only his time at the bank; his reported BBVA years need another source).

### Where round 8 should start
Still with no revolving-door record and worth a governor-profile pass each: **Ireland, Belgium, Poland, Singapore, Peru, Denmark, Norway, Finland, Slovakia, Croatia, Bulgaria**, Malaysia beyond the two held and Switzerland beyond Hildebrand. **US Reserve Bank presidents before 2000** is still untouched and is still the one closed, listable set here. Two Fed appointment URLs remain unopened.


## Round 8 (10 November 2026), what it added
Five records, two of them the first at that bank, and the first pre-2000 Federal Reserve material.

- **Norway** — Nicolai Tangen, founder of the hedge fund AKO Capital in 2005, appointed chief executive of Norges Bank Investment Management on 24 March 2020, from Norges Bank's own account, which also sets out the conditions attached: he gives up all positions at AKO and the Foundation, the earnings from his interest go to the Foundation during his term, and personal trading needs the General Counsel's approval. First revolving-door record for Norges Bank. The Supervisory Council's warning about the same hire was already on the map as a case, so the two sit side by side.
- **Ireland** — Matthew Elderfield, deputy governor and financial regulator from 2010, hired by Lloyds Banking Group as director for conduct and compliance from October 2013 (Irish Times). First for the Central Bank of Ireland. Note that RTE's earlier report had Lloyds only "in talks" with all parties declining to comment; the confirmed report is the one cited.
- **United States, pre-2000** — E. Gerald Corrigan (New York Fed 1985-1993, Goldman Sachs partner from 1994), William J. McDonough (about 22 years at First Chicago, New York Fed from 1992, president 1993-2003, later vice chairman of Merrill Lynch) and Thomas C. Melzer (17 years at Morgan Stanley, managing director 1977-1984 over the Government Securities Department, St. Louis Fed president 1985-1998). All three from Federal Reserve History.

### This round moved scores across the whole map
The three Fed records raised the highest revolving-door count anywhere, which is the denominator, so every country's share of it fell a little. **Rounded all-around figures moved for Australia (23 to 22), Ireland (22 to 23) and Slovakia (25 to 24)**, and those three paragraphs quoted the old number and were corrected. The United States paragraph's count of recorded moves went from 34 to 37. Fifteen other countries moved by a point on the inside score, which no writeup quotes. **Check for this every time a record is added to the country holding the maximum.**

### The Federal Reserve History index does not render for an automated reader
Its people page reports 246 profiles but returns only the filter controls, so there is no list to work from. The three records here were found by name. To finish the pre-2000 set, work through each Reserve Bank's own history page for its list of presidents, then open only the profiles of those who came from or went to a bank, a securities firm or an asset manager.

### Where round 9 should start
Banks still with no revolving-door record: **Belgium, Poland, Singapore, Peru, Denmark, Finland, Slovakia, Croatia, Bulgaria**, Malaysia beyond the two held and Switzerland beyond Hildebrand. Then the rest of the pre-2000 Fed presidents by the method above. After that the revolving door stops being the cheapest seam and the governor-dismissal leads (17 unopened) are worth more.
