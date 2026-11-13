# Handoff: Central bank capture map

Paste or attach this in a new chat to carry on adding to the map.

Rewritten at round 34, current through round 36. It states the current position only. Earlier versions kept round-by-round narrative, which went stale and in round 26 sent agents to re-research records already on the map. Keep it that way: when something changes, edit the statement, don't append a round note. **Where this names a country as dead or blocked, that is as of round 36 — re-derive the target list from `coverage.py` before briefing anything.**

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

Another session of the user's commits to this repo often. **Always `git fetch origin main` and rebase before pushing**; central-bank files have never conflicted, but the push will be rejected without it. If the push is refused with "not in this session's authorized repository set", attach the repo to the session first.

- `out/core.json` and `out/extra.json` are already built from the downloaded datasets. Only rerun `build_core.py` / `build_extra.py` when refreshing those datasets. Their raw downloads (about 200 MB: Romelli, Garriga, CPI, WGI, Basel, FSI, Laeven–Valencia, BIS, COFER, Swift, Ilzetzki–Reinhart–Rogoff) are not in the repo. Each source and its URL is listed in `about.html`.
- **Testing:** `python3 shot2.py "<js step>" "<js step>"` screenshots after each step into `shots/s{i}.png` and prints page errors. It loads `dist/central_bank_independence.html` directly, and app functions are scoped, so hook that file first with `agents/work/mk_t3.py` and drive through `T.` / `T3.`. Keep a clean copy and restore it afterwards: **never push a hooked build** (check with `grep -c "window.T" dist/central_bank_independence.html`, which must print 0).
- **Commits** end with the attribution lines the session supplies.

## How it is built
- `template.html` holds the layout and CSS. `app.js` holds all map logic (MapLibre GL 5 globe/flat, the shared Culprits basemaps in `basemaps.js`, `plate.js`). `about.html` is the "About and sources" text.
- `build_final.py` merges `out/*.json` with the hand-compiled files in `agents/` and injects `const D = {...}` into the template.
- **Layers:** `seq()` / `cat()` in `app.js` push objects onto `L` (`id, group, label, get(p,y), desc, src`). Values are cached; call `clearCache()` after changing what a layer depends on.
- **Top-left dropdown:** the compilation layers (the default is "Ulterior influence, all around"), corruption, independence, reach, "Whose money it is" and the exchange-rate regime. Pattern layers are **not** in this dropdown; they live in the bottom-right box, and the dropdown then reads "Chosen in the box at right".
- **Bottom-right box** (`SIDE_GROUPS`) has two sections:
  - **"Who owns, pays and pressures central banks":** multi-select checkboxes for 7 kinds of tie (`REL`: own, corrupt, people, inst, control, service, account) plus the "Filter by connections with central banks" block and a key with no title.
  - **"Patterns behind the scenes":** 20 patterns from `agents/patterns.json`.
- **Network** (`build_net.py` → `out/net.json`):
  - Nodes are parties placed at their true head office, using `agents/hq.json` and GeoNames.
  - Parties sharing an address fan out by a pixel offset only, so true positions never move.
  - Links: `{n, cb | tn, rel, role, detail, src_t, src_u}`.
  - Popups turn each link into a plain sentence (`SAY` / `sayLink` / `srcItem` in `app.js`). Add a `SAY` entry for any new `role` string.

## Where it stands (37 rounds in, 12 November 2026)

1,491 outside parties and 2,091 ties. 1,720 writeups, one for every box. 20 patterns.

| Category | Records | Places | Breadth |
|---|---|---|---|
| Corruption cases | 232 | 154 | 75% |
| External auditors | 198 | 161 | 78% |
| Banknote printers | 157 | 133 | 65% |
| Swap lines | 240 | 84 | 41% |
| Revolving door | 206 | 80 | 39% |
| Governor removals and pressure | 128 | 71 | 34% |
| Outside reserve managers | 155 | 37 | 18% |
| Gold custodians | 58 | 31 | 15% |
| Named shareholders | 228 | 9 | near-complete* |

\* Named shareholders reads low because only about ten central banks have private shareholders at all. Outside reserve managers reads low because 103 of its 155 ties are Norway's fund — and no list of which banks hire outside managers is published anywhere, so this row has no honest denominator.

`agents/work/coverage.py` computes this table from the data files and prints, per row, the places holding no record of that kind, with union codes and the ten places with no central bank separated out as "not targets". **Run it every round and build the target list from that absent list; never from prose in this document.**

## How complete the map is, as a whole

The breadth figures count *places*, not events. For the three rows the user cares most about — corruption cases, governor removals, revolving door — completeness was estimated by recapture: take cases gathered independently of the map and count how many are already on it.

- Thirty major internationally reported episodes checked by name: 28 already recorded. The two misses were arguable (Russia's Masterbank is a commercial-bank licensing scandal, Venezuela's Andrade was a treasurer not a bank official), and both countries already hold a different case.
- A blind news sweep for central bank officials facing corruption proceedings returned four people (Hungary's Matolcsy, Lebanon's Salameh, Mauritius's Seegolam, Burundi's Murengerantwari). All four already recorded.

**So: roughly 90% of cases a well-informed reader would recognise since 2000; roughly 40% of every documented instance of any size and any year.** The gap is three things, each visible in the data: cases before 2000 are thin (3 in the 1980s, 15 in the 1990s, 87 in the 2010s) because those court and press records are not online; 80 of the 135 countries with a case have exactly one, which usually means one *findable* case; and 96 of the 206 revolving-door records are American or British because the Fed and the Bank of England publish full career histories.

This is written into `about.html` under "How complete is this, and how should you read it". Keep it there in step with any change to the figures.

## How a blank is shown

On the two layers compiled case by case — `cc` (corruption cases) and `ev` (moves against the bank) — a country with no record takes one of three shades rather than one grey:

- **slate** `#3f505c` — no record found, press free to report (RSF bands 1–3)
- **brick** `#6a4a4a` — no record found, reporting restricted (RSF bands 4–5)
- **grey** `NODATA` — no record found, press freedom not rated (mostly micro-states)

Of the 52 places with no corruption case, 19 fall in the restricted bands, among them the UAE, Bahrain, Cuba, Egypt, Eritrea, Jordan, Saudi Arabia, Sudan and Uzbekistan. **Do not read those as clean.**

Wiring: `agents/press_freedom.json` (Reporters Without Borders World Press Freedom Index 2026 situation band per country) → `D.PRESS` / `D.PRESSM`. A layer opts in with `blank: true`. `blankKind()` and `blankColor()` choose the shade, `colorOf(l, r, d, iso)` takes the iso3 as a fourth argument, the legend prints all three rows with their own info text, and `pressNote(iso)` adds the explanatory sentence to the country box. **Any future layer compiled case by case should opt in the same way.**

## The three extraction failure modes, and the fix for each

A central bank's auditor report is usually *present* and *unreadable*, and there are exactly three reasons. Diagnose before concluding a report has no auditor's section.

**1. The page is a scan.** `pdftotext` returns under ~300 characters for those pages while the rest of the document extracts normally.

```bash
for p in $(seq 1 N); do c=$(pdftotext -f $p -l $p x.pdf - 2>/dev/null|wc -c); [ "$c" -lt 300 ] && printf "%s " $p; done
pdftoppm -r 200 -f <a> -l <b> -png x.pdf p && tesseract p-0NN.png - --psm 6
```
Settled Barbados, Bahrain, Eswatini, Burundi.

**2. Broken font encoding.** Every page extracts at normal length as punctuation soup, so no page looks blank and nothing is readable. **Test:** grep the extracted text for a word that must appear — `auditor`, `balance`. Zero hits across a 300-page annual report means broken encoding. OCR the likely range. Settled Bangladesh.

**3. The page text is a full-page embedded image.** `pdftoppm` renders the page near-white and OCR returns nothing, which looks like a genuinely blank page. **Test:** `pdfimages -list -f <a> -l <b> x.pdf` — if a page carries one large JPEG, extract and OCR *that file*, not the rendered page:

```bash
pdfimages -f <a> -l <b> -png x.pdf out/x && tesseract out/x-001.png -l ita - --psm 6
```
Settled San Marino.

Add `-l fra+eng`, `-l ita`, etc. for non-English documents. A 100-page scan costs about a minute. **This runs locally and needs no browser.** The documents are reachable; it is the *reading* that fails, and a browser shows the same unreadable picture. Use OCR first.

## Where to look when a bank's own site fails

**When a search for a central bank's report returns only commercial banks, stop searching and fetch the bank's own publications index directly.** Eswatini, Burundi, Haiti, DR Congo and San Marino were all logged dead on searches that drowned in commercial banks with similar names, and all five publish the document openly on their own site. Country-name searches are nearly useless for this row.

Index paths that worked: `centralbank.org.sz/annual-report/` (82 PDFs), `brb.bi/etats_financiers`, `brh.ht/notes-de-presse/?act=publications`, `bcc.cd/publications/rapport-annuel`, `bcsm.sm/pubblicazioni-e-statistiche/bilanci-annuali`.

**Check the national gazette before calling a bank's accounts unreachable.** Macao looked like a blocked host for three rounds. The Autoridade Monetária de Macau publishes its `Relatório e contas` in the Macao official gazette — `Boletim Oficial` II Série supplements on `images.io.gov.mo` — not on its own site, which is why the rebuilt `amcm.gov.mo` has no annual-report index. Other opaque countries may do the same. That host is refused by the sandbox proxy but reads fine through WebFetch, PDFs included.

**When the bank's own site serves nothing, a national financial newspaper reading the accounts can be the only route.** `www.bna.ao` is a script-built shell with no document list, so Angola's auditor and its largest external reserve manager both came from *Expansão* reading the BNA's `Relatório e Contas`. File those `weak_source: true` and say in the record that it rests on press reporting of the accounts rather than a copy of them.

Some hosts reset the connection at random (`centralbank.org.sz`, `rbm.mw`). **Retry the identical request two or three times before concluding anything.**

## Data files to add to (`agents/`)
| File | Holds |
|---|---|
| `corruption.json` | `cases` (iso3, central_bank, category, years, people, summary, status, source_title, source_url, weak_source) and `revolving_door` |
| `events_gold.json` | `events`: governor firings, pressure and moves against banks, 1990s–Nov 2026; plus gold storage |
| `owners.json` | `holdings` (named shareholders with shares, %, as_of, source), `bis_members`, `history` |
| `networks.json` | `links` (entity, entity_type, hq, cb_iso3, relation, detail, source) and `g30` members |
| `parties.json` | Parties named in cases and events, with head offices |
| `swaps.json` | Swap lines (provider, counterparty, amount, dates, status, source) |
| `gaps.json` | Fed and South Africa holders, Greece, Türkiye share classes, `auditors`, `auditors_unavailable`, `no_central_bank`, case updates |
| `press_freedom.json` | RSF 2026 situation band per country; drives the blank split on the case layers |
| `hq.json` | Head-office city and country for each party |
| `patterns.json`, `implications.json` | The 20 patterns and their plain-language meanings |
| `writeups.json` | A plain-language paragraph for every box (`p:ISO`, `n:<node name>`) |
| `work/research_log_2026-11.json` | What was searched with no result, leads not opened, records dropped after review. **Read this before researching anything.** |

Note `gaps.json['no_central_bank']` is a dict with `note` and `places`, not a list. Reading it as a list silently yields the wrong filter.

## Rules the user holds to
- **No fabrication.** Every record needs a readable source URL that states the fact. Mark Wikipedia-only items `weak_source: true`. List acquittals but don't count them. Claims resting on one author go in as "claim, not confirmed."
- **Don't filter datasets.** Include everything a source publishes.
- **Plain words for a novice.** Show the case, figure or mechanism instead of characterizing it. No purple prose.
- **No "our"** — the user works alone.
- **Colors:** no orange, yellow or neon; earthy, muted palettes.
- **Behavior to keep:** tables never need sideways scrolling, chart windows open centered, markers never cluster or bunch.
- **Report each round** with the coverage percentages, broken down by row, and say why they moved as much or as little as they did.

## The rules that decide whether something is a record

- **Unstated ownership settles nothing.** A source naming an employer without saying it is private does not make a revolving-door record. Peru's Velarde (Banco Central Hipotecario, state-owned, ownership unstated) set this; the ECCB's Sir Errol Allen was declined on it. Trinidad and Tobago was **settled negatively**: the Ministry of Finance's own listing places First Citizens under "indirectly owned".
- **Private but not financial is logged, not filed.** Slovakia's Marián Juskó to the oil refiner Slovnaft set this; Teeters (IBM), Lindsey (economic advisory) and Brimmer (own consulting firm) were logged the same way.
- **An unnamed employer is still a record.** Where a bank publishes a full dated career but withholds the firm — Kuwait's Al-Haroon, Kuwait's Al-Rumaih — file it with no party node.
- **`public_move: true`** means the only outside employer is the IMF or World Bank: listed, not counted. Sovereign wealth funds, statutory pension bodies and state-owned banks are public too; say which side of a career is private.
- **Which case statuses count.** A case stops counting only when the official was cleared, or the charge is gone and no finding stands. `acquitted`, `case dismissed`, `charge withdrawn`, `investigation closed`, `conviction annulled (time-barred)` do not count. Everything still running does, and so does a case whose ending no source states. `build_final.py` refuses to build on a status that is on neither list.
- **`alleged`** means publicly accused with no charge, inquiry or ruling. `S.alleged` decides whether those count; the tick box is on by default.
- **Event kinds decide whether an event counts.** `app.js` computes `evN = (p.ev||[]).filter(i => D.EV[i].kind !== "other").length`, so an event filed with kind `other` shows in the country box but is **not counted** on the layer, in the score, or by `coverage.py`. `other` is for appointments and court rulings, which the layer deliberately excludes. Never file a real episode that way. Kinds are free text and render as written, so a new one is safe (`attempted law change` was added for South Africa). Mexico and Pakistan hold only `other` events and so render blank by design; `coverage.py` lists them under the table. Pakistan is the model for restraint here: its source says the governor cited personal reasons and reports no government pressure, so the unnamed officials who called that a cover were not enough to promote it.
- **Union banks.** Union-wide records are keyed to the union code (`ECB`, `BCEAO`, `BEAC`, `ECCB`) and expand to every member country — for **all** kinds of tie, service ties included. The old head-office rule is reversed, and merge scripts must not map `BCEAO`→`SEN`, `BEAC`→`CMR`, `ECCB`→`KNA`. In a pattern, `app.js` checks `RC[p.iso]` before the union, so a member country's own note wins over the union's.
- **Staff below senior management:** the role, not the name.
- **`name_as_stated`:** set it whenever the canonical entity name differs materially from what the source prints. Taiwan's printer is the example — the release says "China Engraving & Printing Works", the works is now the Central Engraving and Printing Plant. Short forms (Crane, NSPMC, KOMSCO) don't need it.
- **A supplier is not a printer.** A source calling a firm a supplier is not a printing statement; Denmark and Trinidad were both rejected on that ground before Denmark was filed properly from the bank's own page.
- **Gold in accounts for yield is not custody.** Bolivia names six institutions holding 19.91 tonnes in gold accounts; none was filed.
- **Dedup on the firm, not the string.** Montenegro was recorded as `"Ernst&Young Montenegro" Ltd Podgorica` from a procurement report and re-found as `Ernst & Young Montenegro d.o.o.` in the signed accounts; a key of (iso3, auditor string) did not match. Normalise punctuation, spacing and legal-form suffixes before comparing.
- **One current auditor per bank.** The map renders every auditor record as "audits the accounts of X" with no notion of a past mandate, so two records for one bank read as a joint audit. Keep the current mandate and put the handover in its `detail`. This is the only case where deleting a record is right; do not delete auditor history for any other reason.

## Run the audit every round

```bash
python3 agents/work/audit_data.py <scratchpad>/boxes.json
```

Thirteen checks the build does not make and that are invisible in the rendered map: party links resolve inside their array and to the right country; every case, career move and event has a source URL; every status is on a known list; every writeup has a box and every box a writeup; no duplicates; no bank both holding an auditor and listed unavailable. Exits non-zero on failure. It earns its keep — it caught Angola sitting in `auditors_unavailable` while also holding a new auditor record.

### The bug it exists for

`record_index` in `parties.json` is a **positional** pointer into the cases, revolving_door and events arrays. Removing or inserting a record shifts every later pointer, and nothing complains — the party box simply shows another country's facts under this party's heading. Round 11 removed one duplicate case; 136 links went wrong and it survived five rounds. Estonia showed a Dominican Republic prosecution, the Maldives showed Cambodia, Israel showed Jamaica.

`agents/work/fix_record_index.py` repairs it by rematching each link's `source_url` to the record it names. Idempotent. **Run after any round that removes, replaces or reorders a record.** A link whose URL matches no record is usually fine — the record's source was upgraded later — and the script leaves those alone.

**Treat a writer agent reporting that a record's heading contradicts its body as a data bug, not a writing one.** That report is the only reason this was ever found.

## Refreshing the writeups (every round)

A writeup never updates itself, and two things make old ones wrong: new records for that place, and scores shifting map-wide because the inside-influence score divides by the highest count anywhere. **Most country paragraphs quote a headline score in words**, so a score change almost always means a rewrite.

```bash
S=<scratchpad>   # mk_t3.py, t_dump.py, t_sc.py are in agents/work/
python3 $S/mk_t3.py /root/cb/dist/central_bank_independence.html $S/t/dump.html
python3 $S/t_dump.py $S                 # writes $S/boxes.json: every box's text
python3 $S/t_sc.py $S/t/old.html $S/sc_old.json && python3 $S/t_sc.py $S/t/dump.html $S/sc_new.json
```

`t_dump.py` needs an **absolute** path. `t_sc.py` needs a **hooked** build on both sides — run `mk_t3.py` over the old build too, or it returns nothing. Keep each round's `sc_*.json` so the next round can diff against it.

Then: keys in `boxes.json` with no entry in `writeups.json` are new; a place whose rounded `all` score changed **and** whose paragraph contains that exact old figure is stale. Patterns create no boxes, so a pattern-only round needs no writeup work — confirm that rather than assume it.

For a round of three or four records, writing the paragraphs directly is faster and safer than briefing agents. The agent machinery below matters when a round adds twenty or more.

### Building an agent's input — three traps, all of which have bitten

1. **Split each box on `Source says: ` and send WHOLE blocks.** Never a character window. Round 17 used a window, cut records mid-sentence, and all four writer agents reported ties arriving named but undescribed — so they left them out.
2. **A record with unnamed employers has no party block** and lives in the box head, past any head cap (Kuwait's Al-Rumaih sits at character 3,866). Extend the head to reach it.
3. **Verify before dispatching.** Assert that a distinctive token from each new record appears in that key's input, and that no input ends mid-sentence. Round 16 shipped eight paragraphs written from excerpts that did not contain the new record at all.

### Facts leak between keys in the same batch

A batch file holds many keys, and an agent can pull a fact from a NEIGHBOURING key's text into the wrong paragraph. Valora is Portugal's printer and its own box names only the Banque de France release, but the paragraph arrived carrying "Austria's Oesterreichische Nationalbank", which appears in a different key in the same file. Kosovo gained a "United Nations administration regulation" the same way. `check_drafts.py` catches this because it tests each draft against ITS OWN box — so run it on every batch, and state the per-key rule in the brief.

### Checking the drafts

```bash
python3 agents/work/check_drafts.py <drafts.json> <boxes.json>
```

Checks numbers **and** capitalised names against the source box, plus banned phrases. Round 15 shipped six paragraphs carrying a city, a parent company and ministerial roles that appeared in no source; a numbers-only check missed all six. The script maps stroked and ligature letters (đ, ø, ł, œ) before NFKD, which does not decompose them — without that, Serbia's Zagrađanin reads as invented. It also stops on month names, spelled-out numbers and "European Union", which are reformatting the brief requires rather than leaks. Adjective forms of a country in the box (Spanish, French) still flag and are fine, as does a sentence-initial word like "Because" — reword rather than argue with it.

Where a box's header prose and its score panel disagree, **the panel is right** — the prose is the old paragraph being replaced.

## Research method

**The only thing that moves a percentage is a bounded set.** Rounds 5–14 averaged 4.7 records each, working one person at a time. Rounds 15–17 took 35, 34 and 33 — and the whole difference was working lists with a countable end.

**The second thing that moves a percentage is reading the absent list rather than skimming it.** The moves-against-the-bank row was stuck at 27% because it was only looking for firings, so Japan, the UK, Canada, Australia, Italy and Spain were all blank. Noticing *which* countries were missing was the entire method; the records took one search each.

Bounded sets that worked:
- **Federal Reserve History people pages** render at `federalreservehistory.org/people/<first>-<middle-initial>-<last>`. The index does NOT render. Guess the slug; try the initial-first form too (`/people/robert-heller` fails, `/people/h-robert-heller` works). 37 records across rounds 13–16. No pages exist for Stephen Axilrod, Robert Rasche, William Taylor or Betty Dukes.
- **Central bank statutes** name who audits a bank even when the bank's own site blocks automated readers. The Philippines fell to Republic Act 7653; Vietnam to Article 47 of its State Bank law. African LII sites work well. But a statute that names a *mechanism* is not a record: Egypt's article 36 and Uzbekistan's article 8 both require an external audit and name no firm, and neither was filed.

**Where a bank publishes no biography, the hiring firm usually does.** Nordea, Swiss Re, DSK Bank, Erste Bank Hungary, AIA Group and Société Générale each supplied a record their central bank's site did not.

**Before opening any lead, search `corruption.json` for the person's name**, and check `events_gold.json` by country before filing a firing as corruption. Round 4's leads list had four facts already on the map; round 12 opened two of seventeen event leads and both were already recorded.

**WebFetch and permission prompts.** Constructed URLs are often refused with `PROVENANCE_REQUIRED`, and some paths are robots-disallowed (`/api/` on most CKAN portals). Run a WebSearch first and fetch only URLs the search returns. Downloading a PDF with `curl` for local OCR is a different thing and is fine. Two sandbox limits are worth knowing: enumerating a site's undocumented API endpoints and sending a spoofed User-Agent are both refused by the environment, so site-internal APIs cannot be probed from here.

**Run a few agents at a time, each capped at about 25 fetches.** Eight at once exhausted the shared hourly limit in minutes.

**A vein checked and ruled out:** IMF safeguards assessments would name central banks' external auditors, but the assessments are confidential and the published policy papers aggregate without naming banks. Don't spend a round on it.

## What is left

### 1. External auditors — 78%, the row that can actually finish
161 of 206 done, union members included. `coverage.py` prints the list and does the subtraction: **31 countries remain**:

`ARE BLR CPV CUB CUW DZA EGY ERI ETH IRN JOR KHM LAO MAC MDG MKD MRT MWI PRY PSE QAT RWA SDN STP SYR TJK TKM TWN UZB VEN YEM`

**Five are confirmed to print no name and are not retry targets:** the UAE (2025 report says only "an independent external auditor appointed by the Board"), Qatar (chapter 11 names nobody), Ethiopia (standalone statements open into the accounts and end at note 31), São Tomé (the Comité de Auditoria page confirms the committee proposes auditors but names no firm), and Macao (the gazette report was read in full: section 3.3.3 is headed "Auditoria interna e externa" but covers only the internal audit office, and item 5 is the opinion of the AMCM's own Comissão de Fiscalização; no firm appears anywhere, and the 2004 and 2010 indexes have the same structure). **So the ceiling is 26 more countries.**

**What is blocking the rest** — these are host problems, not search problems, and OCR does not help:
- `cbe.org.eg` (Egypt) — F5 WAF, rejects plain fetch and headless Chrome with a support ID
- `centralbank.cw` + its `exch.` mirror (Curaçao) — refuses fetches; mirror's certificate does not match the hostname
- `bcm.mr` (Mauritania) and `bnr.rw` (Rwanda) — empty single-page-app shells, no links render at all
- `rbm.mw` (Malawi) — document lists built in script that does not run headless; only PDFs on any page are access-to-information forms
- `bank-of-algeria.dz`, `bcp.gov.py`, `bcv.cv`, `nbc.gov.kh`, `cbj.gov.jo`, `bcv.org.ve`, `banque-centrale.mg`, `nbt.tj`, `nbrm.mk` (Cloudflare bot check), `beac.int` (robots-disallowed)

**Jordan is the closest and is not a sandbox problem.** `opendata.gov.jo` carries the Central Bank of Jordan's "financial statements and independent auditors report" as CKAN datasets `MIGRATED-450-2018` and `MIGRATED-450-2020`, with resource UUIDs exposed (`1e1fc742-3772-494e-a843-79c79213c945`, url type `upload`, a 1.5 MiB PDF). The resource page renders through WebFetch but prints no download link; the `/api/` path is robots-disallowed; curl is reset by the peer; and the site also fails to load in a real browser through the Chrome extension. The document exists and is addressed. What is left is a mirror, a copy from elsewhere, or a fetch from inside Jordan — **do not spend another round on the browser route.**

**Taiwan stays unfiled on purpose.** The Ministry of Audit publishes a 中央政府總決算審核報告 whose consolidated balance sheet includes the central bank's deposits, but that is the government's consolidated account, not an audit of the bank's own statements. Filing it would say more than the source does.

**Still unopened:** Myanmar's law as a .docx on myanmartradeportal; Cambodia's Khmer-language site or National Audit Authority; the Uzbek Senate's record of the audit conclusion it receives each May.

**Keep the euro area current.** The records were built from the EUR-Lex consolidation `CELEX:01999D0070-20240627`, which is out of date. **Do not trust the consolidation alone: check each mandate's end year and search for the amending decision.** Three had already lapsed when checked and two had changed firm (Estonia and Latvia both moved from Ernst & Young to KPMG). **Mandates ending with FY2026, to check in 2027: Greece (EY Hellas), Portugal (PwC), Slovenia (Mazars — Ernst & Young is already approved for 2027–2029 by Council Decision (EU) 2026/423, noted in the record but not filed, because it has not started).** The search that works is the bank's own name plus "Council Decision amending 1999/70"; `data.consilium.europa.eu` serves the adoption notes when EUR-Lex has not published the final text, and `lawplayer.com` mirrors the article wording.

**Shapes to expect.** Joint audits are common and are recorded as one printed string: Bangladesh (Howladar Yunus & Co. with ACNABIN), Haiti (KPMG S.A. with Mérové-Pierre), Namibia, Lesotho, BEAC. Hybrids where a supreme audit institution is the statutory auditor but a private firm does the work: Seychelles (Grant Thornton Abu Dhabi on the Auditor General's behalf), Papua New Guinea, Trinidad and Tobago (BDO T&T). One-off international reviews rather than statutory appointments: Libya (Deloitte, both branches, 2014–2020, UN-procured) — say so in the record's own sentence. Purely local firms with no network: San Marino (Solution S.r.l.).

**Sudan is a judgement call left as unavailable.** The Central Bank of Sudan Act 2002 says the accounts shall be audited in accordance with the General Audit Chambers Act 1999 — a statute, not a body, so it was not promoted to "General Audit Chamber".

**The BCEAO's national directorates:** the all-lots award notice has been read and names a titulaire and suppléant for the head office and every directorate. Niger is separately confirmed (Mazars Niger titulaire, KMC S.A. suppléant, FY2024–2029).

**What the row shows.** The Big Four sign off on about half the records; eight networks cover roughly seven in ten; the rest are national audit offices and local firms. The countries left are disproportionately places where the auditor is a state body or unpublished, so finishing will likely push the Big Four share *down* a point or two rather than up. Take the exact figures from the data, not from this paragraph.

### 2. Banknote printers — 65%
73 absent, of which 69 are real targets. **BanknoteNews is the vein**, hit rate about a third, yield concentrated in 2023–2026 posts and in commemorative notes. Query shape: `banknotenews <country> <currency> new note confirmed "Printer"`, then fetch the newest entry per country, not the highest denomination. Many recent entries carry no `Printer:` field at all rather than "(Unknown)".

**Second vein:** the issuing bank's own new-series press release — it worked three times in four attempts (Iceland, Fiji, Seychelles) and is the only vein that states a printer plainly enough to file. Multi-bank cooperation releases are worth hunting: one joint Banque de France release with the OeNB and Banco de Portugal yielded two records at once.

**Third:** ask first whether the country's own bank runs a printing works. State works have been most of the yield three rounds running.

**Closed — do not re-run.** The customer-list sweep across De La Rue, G+D, Crane, Oberthur, IDEMIA, Veridos, Bundesdruckerei, Goznak, KOMSCO, PWPW, Orell Füssli, CBPM, Canadian Bank Note, Royal Joh. Enschedé, Thomas Greg & Sons, SPMCIL, Peruri and Pakistan Security Printing: none publishes one except Note Printing Australia, already mined. PWPW's archive and G+D's case studies are exhausted for banknotes. CBPM's nine named customers are all recorded. **The euro area is structurally closed** — do not spend a round on Finland, Slovenia, Estonia, Latvia, Lithuania, Cyprus, Malta, Croatia, Luxembourg, Italy, Greece, the Netherlands, Belgium or Ireland.

**Still live:** PWPW's *news archive* names customers one release at a time (Paraguay and the Dominican Republic came from it); G+D's *per-country case-study pages* (Armenia came from one). **The highest-value untried lead is BEAC** — one record covers six countries; its 30th-anniversary brochure and FinancialAfrik's pieces on the 2020-type series are the targets, and `beac.int` is robots-disallowed.

**Named next steps:** Zambia (diplo.news on the new kwacha launch), Costa Rica (BCCR press release of 11.11.2020), North Macedonia (the printing tender award notice), Georgia (centralbanking.com, likely paywalled), Zimbabwe (mriguide.com and zimbabwenow.co.zw mirrors; note one source is Fidelity Printers *denying* that it prints Zimbabwe dollars), Uruguay (2000s BanknoteNews commemorative entries identified but never fetched).

### 3. Moves against the bank — 34%, and the cheapest win left
**This row was only recording poor and middle-income countries**, because it was looking for firings. Pressure in a rich democracy takes another form: a threat to rewrite the bank's law, a review of its mandate, a governor quietly not reappointed, a funding squeeze, a resignation under political fire. Fourteen places went on in four rounds on that insight — Japan (Abe's threat from December 2012 to revise the 1998 Bank of Japan Law unless it adopted a 2% target, which it did on 22 January 2013), the United Kingdom (Truss's 2022 promise to review the Bank's mandate, and a later 44-MP call for a Treasury-led review), Canada (Poilievre's pledge of 11 May 2022 to fire Macklem), Australia (Lowe not reappointed on 14 July 2023 after the review his criticism produced), New Zealand (Orr's resignation of 5 March 2025, a funding deadlock with the minister and Treasury), South Africa (the Public Protector's 2017 instruction to Parliament to change the bank's constitutional mandate), Italy (Fazio forced out on 19 December 2005 while the government drafted a law to unseat a governor who held office for life) Spain (Fernández Ordóñez leaving a month early on 29 May 2012 under government fire over Bankia), Iceland (parliament restructuring the central bank on 26 February 2009 to remove a governor who had refused to resign), Germany (the 1997 plan to change the Bundesbank law and revalue its gold, which the bank's council publicly called a possible attack on its independence) and Ireland (Trichet's secret letter of 19 November 2010 making further emergency lending to Irish banks conditional on Ireland applying for a rescue programme, published only in 2014), Switzerland (Hildebrand's resignation of 9 January 2012, after his wife's dollar trades were leaked from her bank to a Swiss People's Party politician while the party campaigned against the franc ceiling), Greece (the SYRIZA government's campaign against Stournaras from spring 2015, which the ECB publicly called pressure, through to the leaked Polakis phone call of February 2019) and South Korea (finance minister Choi Kyung-hwan's open demands for rate cuts from July 2014, and the two cuts that followed).

Round 37 took four more on the same insight — Israel (finance minister Smotrich's public campaign against governor Yaron over rates, 4 September 2025: "If the governor doesn't lower interest rates, I will lower taxes"), Czechia (Zeman, 18 February 2015, refusing to appoint any board member who favoured devaluing the crown, with five of the seven seats his to fill before March 2018), Slovakia (Makuch leaving two years early on 27 November 2018 to move the choice of his successor out of the parliament expected after the 2020 election) and Portugal (the prime minister's phone call of 12 April 2016 while the bank was removing Isabel dos Santos from EuroBic).

**The absent list is now Austria, Belgium, Denmark, Finland, France, Luxembourg, Netherlands, Norway, Slovenia, Sweden.** Sweden and Denmark look likeliest — the new Sveriges Riksbank Act that went through 2019–2022, and Danish political attacks on the Nationalbank's krone peg. **France is a confirmed hard case, not an unopened one:** everything findable there is an appointment controversy, which this layer excludes — 150 economists wrote to Le Monde in September 2015 against Hollande's choice of a former BNP Paribas deputy chief executive as governor, and Villeroy de Galhau's early departure announced on 9 February 2026, which handed Macron the succession before the 2027 election, is on his own account personal with no one asking him to go. Search the governor's name plus "independence", or the country plus "central bank mandate review" — not for dismissals. Four forms now have a filed example each and are worth searching for by name: a minister demanding rate cuts in public (South Korea, Israel), a leak that makes a governor's position untenable (Switzerland), a sustained campaign in the government's own press (Greece), and a head of state stating a policy test for a seat on the board (Czechia).

### 4. Outside reserve managers — 155 ties at 37 banks, 103 of them Norway
**RAMP does NOT publish its membership**, only contradictory counts ("over 70" 2024 → "a record 95" April 2026). Each of the fourteen RAMP ties was assembled from an individual press release; roughly 80 members remain unidentified, and the same search run year by year, in Spanish, French and Portuguese too, will keep yielding them. Every bank the World Bank has named is already recorded.

**Say what the source says.** Most RAMP announcements describe advice, technical assistance or training; only Seychelles states that RAMP actually manages a portfolio. Never upgrade membership or advice into management.

**Angola is on this row and is not finished.** Gemcorp Capital held 56% of the BNA's external assets at the end of 2023, and the governor, answering the newspaper on the record, referred to the bank's *other* external managers — who are not named.

**Best remaining vein:** small open economies that publish a standalone reserves-management report. The Central Bank of Seychelles' International Reserves Management Report 2025 named three outside parties in one document.

**Known blanks — confirmed external managers, no firm named:** Botswana, the Trinidad HSF, Timor-Leste, Namibia, Ghana, Kazakhstan, Chile ("dos administradores externos", about 3%), the UAE ("the top ten globally"), the HKMA (30% externally including all listed equity), Brazil and Türkiye (both internal). OMFIF's external-managers chapter names seven firms and anonymises all 73 banks.

**Retry later:** Peru's BCRP transparency PDF (bot-protection stub), Lesotho's and Tanzania's 2024 annual reports (site errors).

### 5. Gold custodians — 15%
**The method is the note to the accounts, not the gold page.** Portugal (note 2), Belgium (note 1), Türkiye (gram-level table by location) and Mauritius (note 7) each disclosed a location table only there. Search for the statements PDF and read the gold note directly.

**Not filed on purpose:** gold *lending* (Czech National Bank, Bulgaria), and country-level answers naming no institution — Czechia's London share, Italy's "primarie banche centrali", Austria's "the U.K." and "Switzerland", Kazakhstan's "specialised foreign repositories". Sri Lanka, Nepal, Serbia, Italy, Spain, the Philippines, Argentina and Taiwan publish a gold note naming no institution: confirmed blanks. Greece is a confirmed blank — the 2024 and 2019 full notes were both read.

**Brazil is a different kind of negative:** a freedom-of-information appeal on gov.br records BACEN refusing to name the custodian on banking-secrecy grounds. Formally *withheld*, not unpublished — worth saying so in the writeup.

This is its own relation, `holds its gold reserves in custody`, with its own `SAY` sentence and `REL` entry. It is not the gold dataset in `events_gold.json`, which gives tonnage and names no custodian. **Keep storage and management apart in the wording**: a bank holding gold "as bailee" leaves ownership with the depositor.

**Still unworked and likely to disclose:** Poland, Denmark, Thailand, Malaysia, South Korea, and the Bank of England's own statistics on who holds gold accounts with it.

### 6. Revolving door and corruption cases
These cannot finish; no complete count exists anywhere. They approach completeness asymptotically.

**Revolving door method:** go to the bank's own governor or board page, or the private firm's own board page, and read the career list. Do not search for scandal. **Closed as blanks:** BCEAO and BEAC publish no board biographies; Solomon Islands has the most detailed Pacific board page found and still yields nothing because no employer is characterised; China looks like a genuine blank, its senior PBoC careers running between state bodies. **Still worth trying:** Cambodia, Laos, Myanmar, Brunei, Tonga. **The denominator moves** — the inside-influence score divides by the highest count anywhere, which the United States holds, so any round adding US records re-checks the whole map.

**Corruption cases are near-exhausted by ordinary search.** Local-language retries in Arabic and Chinese found nothing across Bahrain, Saudi Arabia, Oman, Taiwan and Singapore. Taking this further needs a different source type: court bulletins, supreme audit institution reports, parliamentary questions, central bank annual reports' own disciplinary notes.

**If the case rows are ever worked again, measure rather than estimate:** run a blind sweep across twenty countries and count how many returns were already on the map. That duplicate rate *is* the completeness figure.

## Patterns — 20, and the named gaps are closed

Five are complete because a source publishes the whole list; five are censuses of the rows above and move only when those rows move; ten are shown by example. The aim the user has stated is **a rundown of all the main currents in the field worldwide, drawn from general knowledge and research rather than only from data compiled on the map.**

The three currents once listed as missing are all in: `supervisory-capture` (Ireland, Iceland, Portugal, Germany, the United States, Lebanon), `asset-purchase-programmes` (the Fed's hiring of BlackRock, the ECB's corporate purchases, interest on reserves) and `cbdc-vendors` (Bitt, Giesecke+Devrient, the DCash outage and withdrawal).

**The rule that governs every summary:** a pattern explains the current as the field describes it, from studies and inquiries. It must not count or describe the map's own records. All twenty have now been read against that rule and three were in breach — `big-four-auditors` ("of 28 institutions whose auditor the map has traced", stale by about 170 records), `banking-crisis-waves` ("the map's own corruption file holds 15 cases", where the category holds 30) and `city-of-london-offshore` ("two central bank cases in the map's files"). All three are fixed. **Re-check any summary you edit; do not re-audit the set.**

**Keep the hedges.** The newer patterns say plainly where the evidence cuts the other way: the US study that measures supervisory leniency most carefully finds *no* support for the revolving door as its cause; BlackRock waived its fee and credited back income; the ECB's concentration in carbon-intensive firms follows a stated market-neutrality policy; the UK asset purchase scheme paid the Treasury more than it has since cost; buying software a central bank cannot write is ordinary. Those hedges are what make the patterns usable.

**Mechanics.** Roles are capped in the legend: `app.js` takes the first four distinct roles and puts the rest under "Other role", so keep a new pattern to four. Pattern links resolve through `end_pt()`: a three-letter uppercase name is read as a country code (`EMU` and `BIS` have hard-coded points), otherwise it matches an existing party node by name, otherwise it falls back to the stated city — so give `from_city` and `from_iso3` for any party not already on the map. A pattern creates no box, so it needs no writeup.

**Weaker fits, noted but not recommended:** stablecoin issuers as private money creators (Tether, Circle); gold repatriation as a political current (Germany, the Netherlands, Poland, Hungary, Venezuela — the custody data already carries the facts); climate mandates and the NGFS, contested in both directions.

## How long to finish

**Yield by round:** 35, 34, 33, 56, 50, 24, 34, 42, 40, 21, 14, 13, then 4, 3, 2, 3, then two rounds of 0 records (two patterns; four corrections), then 6, 4, 3 and 3.

The service rows are far enough along that a confirmed blank is worth as much as a find, because it stops every future round spending on the same dead country. Say so when reporting a round that produced negatives.

**Auditors: 6 to 10 more rounds** for the 26 reachable countries. What is left is mostly blocked hosts, so plan against 2 to 4 a round and expect several to need a copy of the document from somewhere other than the bank's own site.

**Ten places have no central bank at all** — Panama, Kiribati, Tuvalu, Nauru, Micronesia, the Marshall Islands, Palau, Andorra, Monaco, Liechtenstein. Listed in `gaps.json` under `no_central_bank` and left in the 206-place denominator, so every service row is understated by about five points. The reachable ceiling on those rows is 196 of 206, or 95%.

## Questions the user has settled (don't reopen)
- **Unproven allegations.** Show both and let the reader switch. A tick box, "Count cases that are allegations alone", sits under the legend on the three case layers, ticked by default.
- **Which statuses count.** Rule above. Romania is the edge case: Olteanu was convicted with a final five-year sentence in October 2020, annulled as time-barred on 31 March 2023, with the court still confiscating €1 million. Left out because no conviction stands; the writeup gives all three facts. **If reversed, it is one string to move between `CC_OUT` in `app.js` and `CC_COUNTED`/`CC_NOT_COUNTED` in `build_final.py`.**
- **Union ties expand to members**, service ties included.
- **Blanks on case layers are split by press freedom.**
- **The completeness statistics belong in `about.html`**, so a reader can judge what they are looking at.

## UI behaviour to preserve
- **Hover:** only diamonds light their ties; lines take no hover or click. Small sources of their own (`hot-lines`, `hot-nodes`); never re-filter the country layer on hover. `setP`/`setF` skip repeated paint and filter calls.
- **Markers:** each party has one fixed spot computed in `build_net.py` — the city point, or a spot 1–8 km around it, over land. Never screen-pixel offsets; markers must not move with zoom. Clicking a stack opens a list (`stackBox`).
- **Ghosts:** parties whose kind of tie is switched off stay as faint grey diamonds that can still be clicked (`net-ghost`).
- **Index:** the box under Find a place (`indexItems`, `drawIndex`). `selectEntity` turns ties on if the party is hidden and draws a ring (`drawSel`).
- **Details box:** positioned in pixels by `openDet`, drags by its top edge. `#det` does not scroll; `#detBody` does. `makeResizable(el, onStart)` adds 8 handles to `#det` and `.win`.
- **Anchors:** `anchorsOf` reads multi-currency anchors, so Belarus (0.2 EUR + 0.5 RUB + 0.3 USD) draws to Moscow. Ilzetzki–Reinhart–Rogoff give "n.a." for Russia and 19 others, which is why they have no outgoing line.
- **Small places:** `build_final.py` adds real outlines from `ne10` (`D.XSHAPE`) for Monaco, Tuvalu and Nauru.
- **Recenter:** `#centerBtn` runs `recenter()`; `homePadding()` removes the padding a box adds.

## Keep these three in step
`about.html`'s "How much of the subject is here" table, the figures in this handoff, and `coverage.py`'s own rows describe the same thing for different readers. **Change all three together**, and take the numbers from `coverage.py` and the build output rather than estimating. If a row is added in one place, add it to the other two in the same commit. When a counting rule changes, say so in all three: `coverage.py` now excludes `other` events from the moves-against-the-bank places figure, matching what `app.js` renders, and that figure dropped by three the round it was fixed.
