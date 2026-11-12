# Handoff: Central bank capture map

Paste or attach this in a new chat to carry on adding to the map.

Rewritten at round 29. Earlier versions carried round-by-round narrative that went stale and misled round 26 into re-researching records already on the map. This version states the current position only. **Where it names a country as dead or blocked, that is as of round 29 — re-derive the target list from `coverage.py` before briefing anything.**

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
- **Testing:** `python3 shot2.py "<js step>" "<js step>"` screenshots after each step into `shots/s{i}.png` and prints page errors. App functions are scoped, so inject the hook with `agents/work/mk_t3.py` first and drive through `T.` / `T3.` — e.g. `T.S.layer='cc';T.update()`. **Never push a hooked build.**
- **Commits** end with the attribution lines the session supplies.

## How it is built
- `template.html` holds the layout and CSS. `app.js` holds all map logic (MapLibre GL 5 globe/flat, the shared Culprits basemaps in `basemaps.js`, `plate.js`). `about.html` is the "About and sources" text.
- `build_final.py` merges `out/*.json` with the hand-compiled files in `agents/` and injects `const D = {...}` into the template.
- **Layers:** `seq()` / `cat()` in `app.js` push objects onto `L` (`id, group, label, get(p,y), desc, src`). Values are cached; call `clearCache()` after changing what a layer depends on.
- **Top-left dropdown:** the compilation layers (the default is "Ulterior influence, all around"), corruption, independence, reach, "Whose money it is" and the exchange-rate regime.
- **Bottom-right box** (`SIDE_GROUPS`) has two sections:
  - **"Who owns, pays and pressures central banks":** multi-select checkboxes for 7 kinds of tie (`REL`: own, corrupt, people, inst, control, service, account) plus the "Filter by connections with central banks" block and a key with no title.
  - **"Patterns behind the scenes":** 17 patterns from `agents/patterns.json`. They explain the pattern as the field describes it, from studies and inquiries; the map's records are a sample of it, and the writeup must not count or describe them. "What this means" comes from `agents/implications.json` or the pattern's own `implications`. `agents/role_info.json`, or a pattern's own `role_info`, holds the info text for each key row.
- **Network** (`build_net.py` → `out/net.json`):
  - Nodes are parties placed at their true head office, using `agents/hq.json` and GeoNames.
  - Parties sharing an address fan out by a pixel offset only, so true positions never move.
  - Links: `{n, cb | tn, rel, role, detail, src_t, src_u}`.
  - Popups turn each link into a plain sentence (`SAY` / `sayLink` / `srcItem` in `app.js`). Add a `SAY` entry for any new `role` string.

## Where it stands (after round 29, 12 November 2026)

1,491 outside parties and 2,090 ties. 1,720 writeups, one for every box.

| Category | Records | Places | Breadth |
|---|---|---|---|
| Corruption cases | 232 | 154 | 75% |
| External auditors | 198 | 160 | 78% |
| Banknote printers | 157 | 133 | 65% |
| Swap lines | 240 | 84 | 41% |
| Revolving door | 206 | 80 | 39% |
| Governor removals and pressure | 110 | 55 | 27% |
| Outside reserve managers | 154 | 36 | 17% |
| Gold custodians | 58 | 31 | 15% |
| Named shareholders | 228 | 9 | near-complete* |

\* Named shareholders reads low because only about ten central banks have private shareholders at all. Outside reserve managers reads low because 103 of its 154 ties are Norway's fund — and no list of which banks hire outside managers is published anywhere, so this row has no honest denominator.

`agents/work/coverage.py` computes this table from the data files. **Run it every round and derive the target list from its absent list; never from prose in this document.** Round 26 briefed agents from prose lists here that had gone stale, and ten of the records the agents returned were already on the map.

## How complete the map is, as a whole

The breadth figures above count *places*, not events. For the three rows the user cares most about — corruption cases, governor removals, revolving door — completeness was estimated by recapture: take cases gathered independently of the map and count how many are already on it.

- Thirty major internationally reported episodes checked by name: 28 already recorded. The two misses were arguable (Russia's Masterbank is a commercial-bank licensing scandal, Venezuela's Andrade was a treasurer not a bank official), and both countries already hold a different case.
- A blind news sweep for central bank officials facing corruption proceedings returned four people (Hungary's Matolcsy, Lebanon's Salameh, Mauritius's Seegolam, Burundi's Murengerantwari). All four already recorded.

**So: roughly 90% of cases a well-informed reader would recognise since 2000; roughly 40% of every documented instance of any size and any year.** The gap is three things, each visible in the data: cases before 2000 are thin (3 in the 1980s, 15 in the 1990s, 87 in the 2010s) because those court and press records are not online; 80 of the 135 countries with a case have exactly one, which usually means one *findable* case; and 96 of the 206 revolving-door records are American or British because the Fed and the Bank of England publish full career histories.

This is written into `about.html` under "How complete is this, and how should you read it". Keep it there in step with any change to the figures.

## How a blank is shown (added round 28)

On the two layers compiled case by case — `cc` (corruption cases) and `ev` (moves against the bank) — a country with no record takes one of three shades rather than one grey:

- **slate** `#3f505c` — no record found, press free to report (RSF bands 1–3)
- **brick** `#6a4a4a` — no record found, reporting restricted (RSF bands 4–5)
- **grey** `NODATA` — no record found, press freedom not rated (mostly micro-states)

Of the 52 places with no corruption case, 19 fall in the restricted bands, among them the UAE, Bahrain, Cuba, Egypt, Eritrea, Jordan, Saudi Arabia, Sudan and Uzbekistan. **Do not read those as clean.**

Wiring: `agents/press_freedom.json` (Reporters Without Borders World Press Freedom Index 2026 situation band per country) → `D.PRESS` / `D.PRESSM`. A layer opts in with `blank: true`. `blankKind()` and `blankColor()` choose the shade, `colorOf(l, r, d, iso)` takes the iso3 as a fourth argument, the legend prints all three rows with their own info text, and `pressNote(iso)` adds the explanatory sentence to the country box. **Any future layer compiled case by case should opt in the same way.**

## The three extraction failure modes, and the fix for each

This is the most valuable thing rounds 27–29 produced. A central bank's auditor report is usually *present* and *unreadable*, and there are exactly three reasons. Diagnose before concluding a report has no auditor's section.

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

Add `-l fra+eng`, `-l ita`, etc. for non-English documents. A 100-page scan costs about a minute.

**This runs locally and needs no browser.** Earlier rounds concluded the bottleneck was access and the fix was a browser tool. That was half right: the documents are reachable, it is the *reading* that fails, and a browser shows the same unreadable picture. Use OCR first.

## The search lesson that matters most

**When a search for a central bank's report returns only commercial banks, stop searching and fetch the bank's own publications index directly.** Eswatini, Burundi, Haiti, DR Congo and San Marino were all logged dead on the strength of searches that drowned in commercial banks with similar names — and all five publish the document openly on their own site. Country-name searches are nearly useless for this row.

Index paths that worked: `centralbank.org.sz/annual-report/` (82 PDFs), `brb.bi/etats_financiers`, `brh.ht/notes-de-presse/?act=publications`, `bcc.cd/publications/rapport-annuel`, `bcsm.sm/pubblicazioni-e-statistiche/bilanci-annuali`.

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
| `patterns.json`, `implications.json` | The 17 patterns and their plain-language meanings |
| `writeups.json` | A plain-language paragraph for every box (`p:ISO`, `n:<node name>`) |
| `work/research_log_2026-11.json` | What was searched with no result, leads not opened, records dropped after review. **Read this before researching anything.** |

## Rules the user holds to
- **No fabrication.** Every record needs a readable source URL that states the fact. Mark Wikipedia-only items `weak_source: true`. List acquittals but don't count them. Claims resting on one author go in as "claim, not confirmed."
- **Don't filter datasets.** Include everything a source publishes.
- **Plain words for a novice.** Show the case, figure or mechanism instead of characterizing it. No purple prose.
- **No "our"** — the user works alone.
- **Colors:** no orange, yellow or neon; earthy, muted palettes.
- **Behavior to keep:** tables never need sideways scrolling, chart windows open centered, markers never cluster or bunch.

## The rules that decide whether something is a record

- **Unstated ownership settles nothing.** A source naming an employer without saying it is private does not make a revolving-door record. Peru's Velarde (Banco Central Hipotecario, state-owned, ownership unstated) set this; the ECCB's Sir Errol Allen was declined on it (government-sounding bank names, ownership nowhere stated). Trinidad and Tobago was **settled negatively**: the Ministry of Finance's own listing places First Citizens under "indirectly owned".
- **Private but not financial is logged, not filed.** Slovakia's Marián Juskó to the oil refiner Slovnaft set this; Teeters (IBM), Lindsey (economic advisory) and Brimmer (own consulting firm) were logged the same way.
- **An unnamed employer is still a record.** Where a bank publishes a full dated career but withholds the firm — Kuwait's Al-Haroon, Kuwait's Al-Rumaih — file it with no party node.
- **`public_move: true`** means the only outside employer is the IMF or World Bank: listed, not counted. Sovereign wealth funds, statutory pension bodies and state-owned banks are public too; say which side of a career is private.
- **Which case statuses count.** A case stops counting only when the official was cleared, or the charge is gone and no finding stands. `acquitted`, `case dismissed`, `charge withdrawn`, `investigation closed`, `conviction annulled (time-barred)` do not count. Everything still running does, and so does a case whose ending no source states. `build_final.py` refuses to build on a status that is on neither list.
- **`alleged`** means publicly accused with no charge, inquiry or ruling. `S.alleged` decides whether those count; the tick box is on by default.
- **Union banks.** Union-wide records are keyed to the union code (`ECB`, `BCEAO`, `BEAC`, `ECCB`) and expand to every member country — for **all** kinds of tie, service ties included. Settled 11 November 2026; the old head-office rule is reversed, and merge scripts must not map `BCEAO`→`SEN`, `BEAC`→`CMR`, `ECCB`→`KNA`.
- **Staff below senior management:** the role, not the name.
- **`name_as_stated`:** set it whenever the canonical entity name differs materially from what the source prints. Taiwan's printer is the example — the release says "China Engraving & Printing Works", the works is now the Central Engraving and Printing Plant. Short forms (Crane, NSPMC, KOMSCO) don't need it.
- **A supplier is not a printer.** A source calling a firm a supplier is not a printing statement; Denmark and Trinidad were both rejected on that ground before Denmark was filed properly from the bank's own page.
- **Gold in accounts for yield is not custody.** Bolivia names six institutions holding 19.91 tonnes in gold accounts; none was filed.
- **Dedup on the firm, not the string.** Montenegro was recorded as `"Ernst&Young Montenegro" Ltd Podgorica` from a procurement report and re-found as `Ernst & Young Montenegro d.o.o.` in the signed accounts; a key of (iso3, auditor string) did not match. Normalise punctuation, spacing and legal-form suffixes before comparing.

## Run the audit every round

```bash
python3 agents/work/audit_data.py <scratchpad>/boxes.json
```

Thirteen checks the build does not make and that are invisible in the rendered map: party links resolve inside their array and to the right country; every case, career move and event has a source URL; every status is on a known list; every writeup has a box and every box a writeup; no duplicates; no bank both holding an auditor and listed unavailable. Exits non-zero on failure.

### The bug it exists for

`record_index` in `parties.json` is a **positional** pointer into the cases, revolving_door and events arrays. Removing or inserting a record shifts every later pointer, and nothing complains — the party box simply shows another country's facts under this party's heading. Round 11 removed one duplicate case; 136 links went wrong and it survived five rounds. Estonia showed a Dominican Republic prosecution, the Maldives showed Cambodia, Israel showed Jamaica.

`agents/work/fix_record_index.py` repairs it by rematching each link's `source_url` to the record it names. Idempotent. **Run after any round that removes, replaces or reorders a record.** A link whose URL matches no record is usually fine — the record's source was upgraded later — and the script leaves those alone.

**Treat a writer agent reporting that a record's heading contradicts its body as a data bug, not a writing one.** That report is the only reason this was ever found.

## Refreshing the writeups (every round)

A writeup never updates itself, and two things make old ones wrong: new records for that place, and scores shifting map-wide because the inside-influence score divides by the highest count anywhere. **157 of the 229 country paragraphs quote a headline score in words**; 8 state a count of career moves.

```bash
S=<scratchpad>   # mk_t3.py, t_dump.py, t_sc.py are in agents/work/
python3 $S/mk_t3.py /root/cb/dist/central_bank_independence.html $S/t/dump.html
python3 $S/t_dump.py $S                 # writes $S/boxes.json: every box's text
python3 $S/t_sc.py $S/t/old.html $S/sc_old.json && python3 $S/t_sc.py $S/t/dump.html $S/sc_new.json
```

`t_sc.py` needs a **hooked** build on both sides — run `mk_t3.py` over the old build too, or it returns nothing.

Then: keys in `boxes.json` with no entry in `writeups.json` are new; a place whose rounded `all` score changed **and** whose paragraph contains that exact old figure is stale. Most flags are false — compare the old and new `all` value and search for that figure before rewriting anything.

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

Checks numbers **and** capitalised names against the source box, plus banned phrases. Round 15 shipped six paragraphs carrying a city, a parent company and ministerial roles that appeared in no source; a numbers-only check missed all six. The script maps stroked and ligature letters (đ, ø, ł, œ) before NFKD, which does not decompose them — without that, Serbia's Zagrađanin reads as invented. It also stops on month names, spelled-out numbers and "European Union", which are reformatting the brief requires rather than leaks. Adjective forms of a country in the box (Spanish, French) still flag and are fine.

Where a box's header prose and its score panel disagree, **the panel is right** — the prose is the old paragraph being replaced.

## Research method

**The only thing that moves a percentage is a bounded set.** Rounds 5–14 averaged 4.7 records each, working one person at a time. Rounds 15–17 took 35, 34 and 33 — and the whole difference was working lists with a countable end.

Bounded sets that worked:
- **Federal Reserve History people pages** render at `federalreservehistory.org/people/<first>-<middle-initial>-<last>`. The index does NOT render. Guess the slug; try the initial-first form too (`/people/robert-heller` fails, `/people/h-robert-heller` works). 37 records across rounds 13–16. No pages exist for Stephen Axilrod, Robert Rasche, William Taylor or Betty Dukes.
- **The consolidated EUR-Lex text of ECB Decision 1999/70** lists every euro-area central bank's approved external auditor in one table. The current consolidation is `CELEX:01999D0070-20240627`; check for a newer one before assuming it is still current.
- **Central bank statutes** name who audits a bank even when the bank's own site blocks automated readers. The Philippines fell to Republic Act 7653; Vietnam to Article 47 of its State Bank law. African LII sites work well.

**Where a bank publishes no biography, the hiring firm usually does.** Nordea, Swiss Re, DSK Bank, Erste Bank Hungary, AIA Group and Société Générale each supplied a record their central bank's site did not.

**Before opening any lead, search `corruption.json` for the person's name**, and check `events_gold.json` by country before filing a firing as corruption. Round 4's leads list had four facts already on the map; round 12 opened two of seventeen event leads and both were already recorded.

**WebFetch and permission prompts.** Constructed URLs are often refused with `PROVENANCE_REQUIRED`. Run a WebSearch first and fetch only URLs the search returns. One round's agent used `curl` to bypass the prompt and recommended it as practice — not an approved method for WebFetch-sourced claims. (Downloading a PDF with curl for local OCR is a different thing and is fine.)

**Run a few agents at a time, each capped at about 25 fetches.** Eight at once exhausted the shared hourly limit in minutes.

**A vein checked and ruled out:** IMF safeguards assessments would name central banks' external auditors, but the assessments are confidential and the published policy papers aggregate without naming banks. Don't spend a round on it.

## What is left

### 1. External auditors — the row that can actually finish
160 of 206 done, union members included. `coverage.py`'s absent list is 46 codes; remove the four union codes and the ten places with no central bank and **32 countries remain**:

`AGO ARE BLR CPV CUB CUW DZA EGY ERI ETH IRN JOR KHM LAO MAC MDG MKD MRT MWI PRY PSE QAT RWA SDN STP SYR TJK TKM TWN UZB VEN YEM`

**Four of those are confirmed to print no name and are not retry targets**: the UAE (2025 report says only "an independent external auditor appointed by the Board"), Qatar (chapter 11 names nobody), Ethiopia (standalone statements open into the accounts and end at note 31), São Tomé (the Comité de Auditoria page under Lei 03/2025 confirms the committee proposes external auditors and reviews their reports, but names no firm and the site publishes no accounts). **So the ceiling is 28 more countries.**

**What is actually blocking the rest, as of round 29** — these are host problems, not search problems, and OCR does not help:
- `cbe.org.eg` (Egypt) — F5 WAF, rejects plain fetch and headless Chrome with a support ID
- `centralbank.cw` + its `exch.` mirror (Curaçao) — refuses fetches; mirror's certificate does not match the hostname
- `bcm.mr` (Mauritania) — empty single-page-app shell, no links render at all
- `amcm.gov.mo` (Macao) — site rebuilt, old annual-report paths 404, no replacement index
- `rbm.mw` (Malawi) — document lists built in script that does not run headless; only PDFs on any page are access-to-information forms
- `bank-of-algeria.dz`, `bcp.gov.py`, `bcv.cv`, `nbc.gov.kh`, `cbj.gov.jo`, `bcv.org.ve`, `banque-centrale.mg`, `nbt.tj`, `nbrm.mk` (Cloudflare bot check), `beac.int` (robots-disallowed)

**Still unopened and worth trying:** Macao's `Boletim Oficial` II "sínteses de contas" supplements (the avisos oficiais files are insurance notices only); Taiwan's Ministry of Audit; Myanmar's law as a .docx on myanmartradeportal; Cambodia's Khmer-language site or National Audit Authority.

**Shapes to expect.** Joint audits are common and are recorded as one printed string: Bangladesh (Howladar Yunus & Co. with ACNABIN), Haiti (KPMG S.A. with Mérové-Pierre), Namibia, Lesotho, BEAC. Hybrids where a supreme audit institution is the statutory auditor but a private firm does the work: Seychelles (Grant Thornton Abu Dhabi on the Auditor General's behalf), Papua New Guinea, Trinidad and Tobago (BDO T&T). One-off international reviews rather than statutory appointments: Libya (Deloitte, both branches, 2014–2020, UN-procured) — say so in the record's own sentence. Purely local firms with no network: San Marino (Solution S.r.l.).

**Sudan is a judgement call left as unavailable.** The Central Bank of Sudan Act 2002 says the accounts shall be audited in accordance with the General Audit Chambers Act 1999 — a statute, not a body, so it was not promoted to "General Audit Chamber".

**The BCEAO's national directorates:** the all-lots award notice has been read and names a titulaire and suppléant for the head office and every directorate. Niger is separately confirmed (Mazars Niger titulaire, KMC S.A. suppléant, FY2024–2029).

**What the row shows once finished.** Of 198 auditor records, the Big Four sign off on 52% of them (KPMG 33, EY 29, Deloitte 19, PwC 19); eight networks cover 69%; the remaining 59 are national audit offices and local firms. The countries left are disproportionately places where the auditor is a state body or unpublished, so finishing will likely push the Big Four share *down* a point or two rather than up.

### 2. Banknote printers — 65%
59 countries absent. **BanknoteNews is the vein**, hit rate about a third, yield concentrated in 2023–2026 posts and in commemorative notes. Query shape: `banknotenews <country> <currency> new note confirmed "Printer"`, then fetch the newest entry per country, not the highest denomination. Many recent entries carry no `Printer:` field at all rather than "(Unknown)".

**Second vein:** the issuing bank's own new-series press release — it worked three times in four attempts (Iceland, Fiji, Seychelles) and is the only vein that states a printer plainly enough to file. Multi-bank cooperation releases are worth hunting: one joint Banque de France release with the OeNB and Banco de Portugal yielded two records at once.

**Third:** ask first whether the country's own bank runs a printing works. State works have been most of the yield three rounds running.

**Closed — do not re-run.** The customer-list sweep across De La Rue, G+D, Crane, Oberthur, IDEMIA, Veridos, Bundesdruckerei, Goznak, KOMSCO, PWPW, Orell Füssli, CBPM, Canadian Bank Note, Royal Joh. Enschedé, Thomas Greg & Sons, SPMCIL, Peruri and Pakistan Security Printing: none publishes one except Note Printing Australia, already mined. PWPW's archive and G+D's case studies are exhausted for banknotes. CBPM's nine named customers are all recorded. **The euro area is structurally closed** — do not spend a round on Finland, Slovenia, Estonia, Latvia, Lithuania, Cyprus, Malta, Croatia, Luxembourg, Italy, Greece, the Netherlands, Belgium or Ireland.

**Still live:** PWPW's *news archive* names customers one release at a time (Paraguay and the Dominican Republic came from it); G+D's *per-country case-study pages* (Armenia came from one). **The highest-value untried lead is BEAC** — one record covers six countries; its 30th-anniversary brochure and FinancialAfrik's pieces on the 2020-type series are the targets, and `beac.int` is robots-disallowed.

**Named next steps:** Zambia (diplo.news on the new kwacha launch), Costa Rica (BCCR press release of 11.11.2020), North Macedonia (the printing tender award notice), Georgia (centralbanking.com, likely paywalled), Zimbabwe (mriguide.com and zimbabwenow.co.zw mirrors; note one source is Fidelity Printers *denying* that it prints Zimbabwe dollars), Uruguay (2000s BanknoteNews commemorative entries identified but never fetched).

### 3. Outside reserve managers — 154 ties at 36 banks, 103 of them Norway
**RAMP does NOT publish its membership**, only contradictory counts ("over 70" 2024 → "a record 95" April 2026). Each of the fourteen RAMP ties was assembled from an individual press release; roughly 80 members remain unidentified, and the same search run year by year, in Spanish, French and Portuguese too, will keep yielding them. Every bank the World Bank has named is already recorded.

**Say what the source says.** Most RAMP announcements describe advice, technical assistance or training; only Seychelles states that RAMP actually manages a portfolio. Never upgrade membership or advice into management.

**Best remaining vein:** small open economies that publish a standalone reserves-management report. The Central Bank of Seychelles' International Reserves Management Report 2025 named three outside parties in one document.

**Known blanks — confirmed external managers, no firm named:** Botswana, the Trinidad HSF, Timor-Leste, Namibia, Ghana, Kazakhstan, Chile ("dos administradores externos", about 3%), the UAE ("the top ten globally"), the HKMA (30% externally including all listed equity), Brazil and Türkiye (both internal). OMFIF's external-managers chapter names seven firms and anonymises all 73 banks. Every asset-manager and Central Banking profile checked keeps the client anonymous.

**Retry later:** Peru's BCRP transparency PDF (bot-protection stub), Lesotho's and Tanzania's 2024 annual reports (site errors).

### 4. Gold custodians — 15%
**The method is the note to the accounts, not the gold page.** Portugal (note 2), Belgium (note 1), Türkiye (gram-level table by location) and Mauritius (note 7) each disclosed a location table only there. Search for the statements PDF and read the gold note directly.

**Not filed on purpose:** gold *lending* (Czech National Bank, Bulgaria), and country-level answers naming no institution — Czechia's London share, Italy's "primarie banche centrali", Austria's "the U.K." and "Switzerland", Kazakhstan's "specialised foreign repositories". Sri Lanka, Nepal, Serbia, Italy, Spain, the Philippines, Argentina and Taiwan publish a gold note naming no institution: confirmed blanks.

**Brazil is a different kind of negative:** a freedom-of-information appeal on gov.br records BACEN refusing to name the custodian on banking-secrecy grounds. Formally *withheld*, not unpublished — worth saying so in the writeup.

This is its own relation, `holds its gold reserves in custody`, with its own `SAY` sentence and `REL` entry. It is not the gold dataset in `events_gold.json`, which gives tonnage and names no custodian. **Keep storage and management apart in the wording**: a bank holding gold "as bailee" leaves ownership with the depositor.

**Still unworked and likely to disclose:** Poland, Denmark, Thailand, Malaysia, South Korea, and the Bank of England's own statistics on who holds gold accounts with it. Greece is a confirmed blank — the 2024 and 2019 full notes were both read and neither carries a location table.

### 5. Revolving door, governor removals, corruption cases
These cannot finish; no complete count exists anywhere. They approach completeness asymptotically.

**Revolving door method:** go to the bank's own governor or board page, or the private firm's own board page, and read the career list. Do not search for scandal. **Closed as blanks:** BCEAO and BEAC publish no board biographies; Solomon Islands has the most detailed Pacific board page found and still yields nothing because no employer is characterised; China looks like a genuine blank, its senior PBoC careers running between state bodies. **Still worth trying:** Cambodia, Laos, Myanmar, Brunei, Tonga. **The denominator moves** — the inside-influence score divides by the highest count anywhere, which the United States holds, so any round adding US records re-checks the whole map.

**Corruption cases are near-exhausted by ordinary search.** Local-language retries in Arabic and Chinese found nothing across Bahrain, Saudi Arabia, Oman, Taiwan and Singapore. Taking this further needs a different source type: court bulletins, supreme audit institution reports, parliamentary questions, central bank annual reports' own disciplinary notes.

**If the case rows are ever worked again, measure rather than estimate:** run a blind sweep across twenty countries and count how many returns were already on the map. That duplicate rate *is* the completeness figure.

## Patterns — the open question

Seventeen patterns: five complete because a source publishes the whole list, five that are censuses of the rows above and move only when those rows move, seven shown by example. The aim the user has stated is **a rundown of all the main currents in the field worldwide, drawn from general knowledge and research rather than only from data compiled on the map.**

Against that aim, three major currents are missing as of round 29:

1. **Asset purchases and who they enriched.** Nothing covers quantitative easing. The Fed bought corporate bonds and bond ETFs in 2020 through BlackRock's advisory arm while BlackRock was the largest manager of those same ETFs; the ECB's corporate sector purchase programme bought named companies' bonds; interest paid on reserves created by QE became multi-billion transfers from central banks to commercial banks in 2022–24.
2. **Supervisory capture.** The map has the revolving door but not the structure where a central bank supervises banks it is entangled with: the same four firms auditing both the central bank and the banks it supervises, supervisory forbearance before collapse (the Banco de Portugal/BES findings are in the data but read as a Portugal case, not a pattern), supervisors moving to supervised banks, and Basel standards negotiated with the industry through the Institute of International Finance. **The existing `big-four-auditors` pattern is the seed of this one and stops at counting firms.** This is the strongest candidate: it extends a pattern already there and the auditor data anchors it.
3. **Central bank digital currency and its vendors.** Over 100 central banks have CBDC work underway; designs differ on traceability and programmability; the building is contracted to a short list of firms (Giesecke+Devrient, Bitt, R3, Consensys, nChain).

Weaker fits, noted but not recommended: stablecoin issuers as private money creators (Tether, Circle); gold repatriation as a political current (Germany, the Netherlands, Poland, Hungary, Venezuela — the custody data already carries the facts); climate mandates and the NGFS, contested in both directions.

## How long to finish

**Yield by round:** 35, 34, 33, 56, 50, 24, 34, 42, 40, 21, 14, 13, then 4 (r27), 3 (r28), 2 (r29) — the last three being single-row auditor rounds.

**Auditors: 6 to 10 more rounds** for the 28 reachable countries. Rounds 27–29 took nine countries with OCR. What is left is mostly blocked hosts, so plan against 2 to 4 a round and expect several to need a copy of the document from somewhere other than the bank's own site.

**Ten places have no central bank at all** — Panama, Kiribati, Tuvalu, Nauru, Micronesia, the Marshall Islands, Palau, Andorra, Monaco, Liechtenstein. Listed in `gaps.json` under `no_central_bank` and left in the 206-place denominator, so every service row is understated by about five points. The reachable ceiling on those rows is 196 of 206, or 95%.

## Questions the user has settled (don't reopen)
- **Unproven allegations** (10 Nov 2026). Show both and let the reader switch. A tick box, "Count cases that are allegations alone", sits under the legend on the three case layers, ticked by default.
- **Which statuses count** (10 Nov 2026). Rule above. Romania is the edge case: Olteanu was convicted with a final five-year sentence in October 2020, annulled as time-barred on 31 March 2023, with the court still confiscating €1 million. Left out because no conviction stands; the writeup gives all three facts. **If reversed, it is one string to move between `CC_OUT` in `app.js` and `CC_COUNTED`/`CC_NOT_COUNTED` in `build_final.py`.**
- **Union ties expand to members** (11 Nov 2026), service ties included.
- **Blanks on case layers are split by press freedom** (12 Nov 2026).
- **The completeness statistics belong in `about.html`** (12 Nov 2026), so a reader can judge what they are looking at.

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
`about.html`'s "How much of the subject is here" table, the figures in this handoff, and `coverage.py`'s own rows describe the same thing for different readers. **Change all three together**, and take the numbers from `coverage.py` and the build output rather than estimating. If a row is added in one place, add it to the other two in the same commit.
