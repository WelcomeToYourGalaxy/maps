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

Another session of the user's commits to this repo often. **Always `git fetch origin main` and rebase before pushing**; central-bank files have never conflicted, but the push will be rejected without it.

- `out/core.json` and `out/extra.json` are already built from the downloaded datasets. Only rerun `build_core.py` / `build_extra.py` when refreshing those datasets. Their raw downloads (about 200 MB: Romelli, Garriga, CPI, WGI, Basel, FSI, Laeven–Valencia, BIS, COFER, Swift, Ilzetzki–Reinhart–Rogoff) are not in the repo. Each source and its URL is listed in `about.html`.
- **Testing:** `python3 shot2.py "<js step>" "<js step>"` takes a screenshot after each step, saved to `shots/s{i}.png`, and prints page errors. Headless Chromium with swiftshader. App functions are scoped, so for tests inject the hook with `agents/work/mk_t3.py`, and never push a hooked build.
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

## Where it stands (after round 26, 11 November 2026)

1,482 outside parties and 2,079 ties. 1,711 writeups, one for every box.

**Breadth is now measured with currency-union ties expanded to member countries** (see below). That change alone moved four rows without any new research, because `coverage.py` had been undercounting what the map already showed.

| Category | Records | Places | Breadth |
|---|---|---|---|
| Corruption cases | 232 | 154 | 75% |
| External auditors | 187 | 149 | 72% |
| Revolving door | 206 | 80 | 39% |
| Banknote printers | 157 | 133 | 65% |
| Swap lines | 240 | 84 | 41% |
| Governor removals and pressure | 110 | 55 | 27% |
| Outside reserve managers | 154 | 36 | 17% |
| Gold custodians | 58 | 31 | 15% |
| Named shareholders | 228 | 9 | near-complete* |

\* Named shareholders reads low because only about ten central banks have private shareholders at all. Outside reserve managers reads low because 103 of its 153 ties are Norway's fund — and no list of which banks hire outside managers is published anywhere, so this row has no honest denominator.


`agents/work/coverage.py` computes this table from the data files. Run it every round; don't estimate it.

### Round 26's process lesson — read this before briefing any agent

**Brief from `coverage.py`'s computed absent list, never from this handoff's prose lists.** Round 26 built its agent briefs from the "Unworked there" and "Never attempted" lists in this document. Those lists had gone stale: ten of the records the agents returned were already on the map (OMN, LBN, TJK, MAC, CYM, SYR and LAO printers; POL twice and DNK gold) and were caught only by the merge dedup. Three countries assigned as untried — Moldova, Azerbaijan and Kenya — already had records. Run `coverage.py` first and derive the target list from it.

**Dedup on the firm, not the string.** Montenegro was already recorded as `"Ernst&Young Montenegro" Ltd Podgorica` from the bank's procurement report; round 26's find printed the same firm as `Ernst & Young Montenegro d.o.o.` in the signed accounts, and a key of (iso3, auditor string) did not match. The signature date and partner were folded into the existing record and the duplicate dropped. Any merge that keys on an entity name should normalise punctuation, spacing and legal-form suffixes before comparing.

### What round 26 settled, closed and confirmed

**Settled.** Auditors: Georgia (KPMG Georgia LLC, FY2020, signed 23 April 2021 at Tbilisi, partner Karen Safaryan); Lebanon (KPMG from 2020, press-sourced, `weak_source`); the Bahamas (Deloitte & Touche with BDO jointly, Nassau, 16 April 2012 for FY2011); Tonga (Coopers & Lybrand, Suva, 21 September 1993, from the Tonga Government Gazette on PacLII — a private firm, not the Auditor General). Printers: Tunisia, Qatar, Bahrain, Angola, Belarus, Tonga, and a second Congo record. Gold: Romania and South Korea, both at the Bank of England, both `weak_source` and the Korean one filed as a claim, not confirmed.

**Closed for good — do not retry these routes.**
- **Cambodia.** The 2023 annual report *did* serve this time (256,690 characters, read at two offsets) and, like the 2022 report, is narrative plus statistical appendices with no financial statements and no auditor's report. NBC's published annual reports do not contain audited accounts at all. Only the Khmer-language site or the National Audit Authority remains.
- **Greece's gold note.** The athexgroup → athens.euronext.com redirect was completed, for the 2024 *and* 2019 full notes. Neither carries a location table — only an ECB valuation price. This is a real blank, not a fetch failure, and the redirect method is now proven for other Greek statements.
- **Eswatini.** The `independentnews.co.sz` upload path returns the news site's homepage, confirmed again from a fresh search. No `centralbank.org.sz` URL appears in any search result.
- **Egypt.** No CBE annual report or financial statements PDF appears in any English or Arabic search; every hit is a commercial bank. With the statute route already exhausted, only the Egyptian Official Gazette is left.
- **Jamaica's "own auditors page" route.** BOJ's corporate-governance audit page fetched fine but covers only the Internal Audit Division. The annual-report pages sit behind an anti-bot interstitial.
- **Italy, Spain, Sri Lanka, Nepal, the Philippines, Argentina and Taiwan** publish a gold note or gold page naming no institution. Confirmed blanks under the names-no-institution rule.

**Brazil is a new kind of negative.** A freedom-of-information appeal on gov.br records BACEN refusing to name the custodian of the international gold reserves on banking-secrecy grounds. Brazil's custodian is formally *withheld*, not merely unpublished — worth saying so in the writeup rather than leaving it as a silent gap.

**Printer method note.** The newest-entry-per-country rule held well: 14 of 22 BanknoteNews entries fetched carried a usable `Printer:` field, above the one-in-three this document predicted. Every miss was a post-2023 entry where the field is simply **absent** rather than marked "(Unknown)". Commemoratives were not systematically better than regular denominations. The bank's-own-currency-page vein produced nothing at all this round — BCEAO's `billets-et-pieces` page and the BNM Moldova per-denomination pages give full security-feature descriptions and no printer.

**The highest-value untried printer lead is BEAC**: one record covers six countries. Its 30th-anniversary brochure on `beac.int` and FinancialAfrik's pieces on the 2020-type series are the targets, and `beac.int` is robots-disallowed, so it is a browser job.

**New printer leads with a named next step:** Zambia (a diplo.news piece on the new kwacha series launch, and a wbs.org.ua article), Costa Rica (the BCCR press release of 11.11.2020 cited by BanknoteNews), North Macedonia (the National Bank put printing out to tender — the award notice would name the winner), Georgia (a centralbanking.com piece, likely paywalled), Zimbabwe (the Herald piece refused the fetch; mriguide.com and zimbabwenow.co.zw mirrors untried), Uruguay (its 2000s BanknoteNews commemorative entries were identified but never fetched, and that era usually carries the field).

**Hosts that joined the blocked list:** `publishing.bnet.om` (robots-disallowed, which kills every year of Oman's annual report), `bcp.gov.py` (client error on the BCP's own Memorias y Balances index), `cbu.uz`, `laoofficialgazette.gov.la` (server error, may simply have been down — worth one retry).

**Two untried routes worth naming:** Bangladesh's Order 1972 requires the *Government* to publish the bank's certified accounts in the official Gazette — that is the best remaining door, and the Order's own audit article names nobody. Macao's `Boletim Oficial` II "sínteses de contas" supplements are the likeliest home of AMCM's published accounts; the avisos oficiais files are insurance notices only.

**Malawi's statute settles a question rather than a country:** Reserve Bank of Malawi Act 2018 s.60(2) requires audit by internationally recognised public auditors appointed annually by the Board, and s.60(3)–(4) limit the Auditor General to a separate efficiency examination. The AG is explicitly *not* RBM's statutory auditor. The Public Finance Management Act 2022 excludes the Reserve Bank from its "statutory body" definition, so RBM accounts are not gazetted under it.

**The Bahamas scan wall, mapped precisely.** The 2023, 2021 and 2018 reports were each read at multiple offsets; in every one the pages between the Financial Statements divider and the Statement of Financial Position extract blank or garbled (2021 pages 46–48 come through as bare page numbers). The auditors' report in all modern CBOB PDFs is an image. 2011 is the only year that yields a name as text, and a current-year Bahamas auditor needs OCR or a browser.

## Data files to add to (`agents/`)
| File | Holds |
|---|---|
| `corruption.json` | `cases` (iso3, central_bank, category, years, people, summary, status, source_title, source_url, weak_source) and `revolving_door` |
| `events_gold.json` | `events`: governor firings, pressure and moves against banks, 1990s–Nov 2026; plus gold storage |
| `owners.json` | `holdings` (named shareholders with shares, %, as_of, source), `bis_members`, `history` |
| `networks.json` | `links` (entity, entity_type, hq, cb_iso3, relation, detail, source) and `g30` members |
| `parties.json` | Parties named in cases and events, with head offices |
| `swaps.json` | Swap lines (provider, counterparty, amount, dates, status, source) |
| `gaps.json` | Fed and South Africa holders, Greece, Türkiye share classes, `auditors`, `auditors_unavailable`, case updates |
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

- **Unstated ownership settles nothing.** A source naming an employer without saying it is private does not make a revolving-door record. Peru's Velarde (Banco Central Hipotecario, state-owned, ownership unstated) set this; the ECCB's Sir Errol Allen was declined on it in round 16 (Bank of Saint Vincent and the Grenadines, National Commercial Bank of Anguilla — government-sounding names, ownership nowhere stated). Trinidad and Tobago was **settled negatively** in round 16: the Ministry of Finance's own listing places First Citizens under "indirectly owned".
- **Private but not financial is logged, not filed.** Slovakia's Marián Juskó to the oil refiner Slovnaft set this. Round 15 logged Teeters (IBM), Lindsey (economic advisory) and Brimmer (own consulting firm) the same way.
- **An unnamed employer is still a record.** Where a bank publishes a full dated career but withholds the firm — Kuwait's Al-Haroon, Kuwait's Al-Rumaih — file it with no party node.
- **`public_move: true`** means the only outside employer is the IMF or World Bank: listed, not counted. Sovereign wealth funds, statutory pension bodies and state-owned banks are public too; say which side of a career is private.
- **Which case statuses count.** A case stops counting only when the official was cleared, or the charge is gone and no finding stands. `acquitted`, `case dismissed`, `charge withdrawn`, `investigation closed`, `conviction annulled (time-barred)` do not count. Everything still running does, and so does a case whose ending no source states. `build_final.py` refuses to build on a status that is on neither list.
- **`alleged`** means publicly accused with no charge, inquiry or ruling. `S.alleged` decides whether those count; the tick box is on by default.
- **Union banks.** Cases use iso3 `BEAC`, `BCEAO` or `ECCB` and expand to every member country. **Party-link records — auditors, printers, managers — must use the head-office country (`CMR`, `SEN`, `KNA`).** There are no boxes for the union codes, so a party link keyed to one is invisible. Round 17 made this mistake and caught it.
- **Staff below senior management:** the role, not the name.
- **`name_as_stated`:** set it whenever the canonical entity name differs materially from what the source prints. Taiwan's printer is the example — the Central Bank's release says "China Engraving & Printing Works", the works is now the Central Engraving and Printing Plant. Short forms (Crane, NSPMC, KOMSCO) don't need it.

## Run the audit every round

```bash
python3 agents/work/audit_data.py <scratchpad>/boxes.json
```

Thirteen checks the build does not make and that are invisible in the rendered map: party links resolve inside their array and to the right country; every case, career move and event has a source URL; every status is on a known list; every writeup has a box and every box a writeup; no duplicates; no bank both holding an auditor and listed unavailable. Exits non-zero on failure.

### The bug it exists for

`record_index` in `parties.json` is a **positional** pointer into the cases, revolving_door and events arrays. Removing or inserting a record shifts every later pointer, and nothing complains — the party box simply shows another country's facts under this party's heading. Round 11 removed one duplicate case; 136 links went wrong and it survived five rounds. Estonia showed a Dominican Republic prosecution, the Maldives showed Cambodia, Israel showed Jamaica, and seven links pointed past the end of the array.

`agents/work/fix_record_index.py` repairs it by rematching each link's `source_url` to the record it names. Idempotent. **Run after any round that removes, replaces or reorders a record.** A link whose URL matches no record is usually fine — the record's source was upgraded later (Bini Smaghi's was) — and the script leaves those alone.

**Treat a writer agent reporting that a record's heading contradicts its body as a data bug, not a writing one.** That report is the only reason this was ever found.

## Refreshing the writeups (every round)

A writeup never updates itself, and two things make old ones wrong: new records for that place, and scores shifting map-wide because the inside-influence score divides by the highest count anywhere. **157 of the 229 country paragraphs quote a headline score in words**; 8 state a count of career moves.

```bash
S=<scratchpad>   # mk_t3.py, t_dump.py, t_sc.py are in agents/work/
python3 $S/mk_t3.py /root/cb/dist/central_bank_independence.html $S/t/dump.html
python3 $S/t_dump.py $S                 # writes $S/boxes.json: every box's text
python3 $S/t_sc.py <old build> $S/sc_old.json && python3 $S/t_sc.py <new build> $S/sc_new.json
```

Then: keys in `boxes.json` with no entry in `writeups.json` are new; a place whose rounded `all` score changed **and** whose paragraph contains that exact old figure is stale. Most flags are false — compare the old and new `all` value and search for that figure before rewriting anything.

### Building the input — three traps, all of which have bitten

1. **Split each box on `Source says: ` and send WHOLE blocks.** Never a character window. Round 17 used a window, cut records mid-sentence, and all four writer agents reported ties arriving named but undescribed — so they left them out and the paragraphs would have omitted the very records the round added.
2. **A record with unnamed employers has no party block** and lives in the box head, past any head cap (Kuwait's Al-Rumaih sits at character 3,866). Extend the head to reach it.
3. **Verify before dispatching.** Assert that a distinctive token from each new record appears in that key's input, and that no input ends mid-sentence. Round 16 shipped eight paragraphs written from excerpts that did not contain the new record at all.

### Facts leak between keys in the same batch

A batch file holds many keys, and an agent can pull a fact from a NEIGHBOURING key's
text into the wrong paragraph. Round 18: Valora is Portugal's printer and its own box
names only the Banque de France release, but the paragraph arrived carrying
"Austria's Oesterreichische Nationalbank", which appears in a different key in the
same file. Kosovo gained a "United Nations administration regulation" the same way.
`check_drafts.py` catches this because it tests each draft against ITS OWN box — so
run it on every batch, and state the per-key rule in the agent's brief.

### Checking the drafts

```bash
python3 agents/work/check_drafts.py <drafts.json> <boxes.json>
```

Checks numbers **and** capitalised names against the source box, plus banned phrases. Round 15 shipped six paragraphs carrying a city, a parent company and ministerial roles that appeared in no source; a numbers-only check missed all six. The script maps stroked and ligature letters (đ, ø, ł, œ) before NFKD, which does not decompose them — without that, Serbia's Zagrađanin reads as invented. It also stops on month names, spelled-out numbers and "European Union", which are reformatting the brief requires rather than leaks: a box printing "14" or "27.06.2024" legitimately becomes "Fourteen" and "27 June 2024". Adjective forms of a country in the box (Spanish, French) still flag and are fine.

Where a box's header prose and its score panel disagree, **the panel is right** — the prose is the old paragraph being replaced.

## Research method

**The only thing that moves a percentage is a bounded set.** Rounds 5–14 averaged 4.7 records each, working one person at a time. Round 15 took 35, round 16 34, round 17 33 — and the whole difference was working lists with a countable end rather than searching open-endedly.

Bounded sets that worked:
- **Federal Reserve History people pages** render perfectly at `federalreservehistory.org/people/<first>-<middle-initial>-<last>`. The index does NOT render. Guess the slug; try the initial-first form too (`/people/robert-heller` fails, `/people/h-robert-heller` works). 37 records across rounds 13–16. No pages exist for Stephen Axilrod, Robert Rasche, William Taylor or Betty Dukes.
- **The consolidated EUR-Lex text of ECB Decision 1999/70** lists every euro-area central bank's approved external auditor in one table. Settled five countries at once in round 16, three more in round 17.
- **Central bank statutes** name who audits a bank even when the bank's own site blocks automated readers. The Philippines fell to Republic Act 7653 after several rounds of failing on the annual report; Vietnam to Article 47 of its State Bank law. African LII sites work well.

**Where a bank publishes no biography, the hiring firm usually does.** Nordea, Swiss Re, DSK Bank, Erste Bank Hungary, AIA Group and Société Générale each supplied a record their central bank's site did not.

**Before opening any lead, search `corruption.json` for the person's name**, and check `events_gold.json` by country before filing a firing as corruption. Round 4's leads list had four facts already on the map; round 12 opened two of seventeen event leads and both were already recorded.

**WebFetch and permission prompts.** Constructed URLs are often refused with `PROVENANCE_REQUIRED`. The pattern that works is to run a WebSearch first and fetch only URLs the search returns. One round's agent used `curl` to bypass the prompt instead and recommended it as practice — that is not an approved method; its records were spot-checked through WebFetch before use. Don't propagate it.

**Run a few agents at a time, each capped at about 25 fetches.** Eight at once exhausted the shared hourly limit in minutes.

## What is left

### 1. External auditors — the one category that can actually reach 100%
Every central bank operates under a law that names who audits it, so the answer always exists. 145 of 206 done, union members included.
**The browser reads what the fetcher cannot, and that is now the main method for auditors.** Three image-only auditor reports have been settled by opening the page in a browser and reading it: Botswana (EY, Gaborone, 2025), **Serbia** (Ernst & Young d.o.o. Beograd, signed at Belgrade on 20 March 2026 by Nikola Ribar, for the year ended 31 December 2025) and the **Maldives** (Deloitte Partners, Malé, signed by Mohamed Siraj Muneer on 29 April 2025, at pages 142–143). Each of those pages returns empty from every text extraction. Still open by this route: Brunei, Fiji's annual report, Eswatini, the Bahamas. One caveat: **Barbados serves its report as a download rather than inline, so the browser tab does not render it** — that one needs a different copy. Two URLs recorded in earlier notes (the Bahamas 2024 report, the Eswatini report on independentnews.co.sz) are now 404, so always get the URL from a fresh search.

**Three banks genuinely print no auditor's name**, each confirmed by a full read: the UAE's 2025 report says only "an independent external auditor appointed by the Board"; Qatar's chapter 11 names nobody; Ethiopia's standalone statements open straight into the accounts and end at note 31. These are not retry targets.

**Three leads closed for good.** Tajikistan's `nbt.tj/files/Audit/` is a procurement directory, not an audit archive. Paraguay's `contrataciones.gov.py` award endpoints return binary with no extractable text. `islamicmarkets.com` has no central-bank holdings beyond Bosnia.

**Bahrain joins the browser batch** (round 25): its 2023 report was read in full, both halves of 182,461 characters, and the extracted text stops exactly at the heading for the financial statements chapter. The Arabic edition behaves identically and no separate statements file exists. **Brunei was settled this way**: PricewaterhouseCoopers Services, signed by Chai Xiang Yuin on 3 June 2026 for the year ended 31 December 2025, at page 90 of the 2025 annual report.

**Hosts that now refuse every fetch**: `beac.int` (robots-disallowed, which kills Chad and Congo-Brazzaville at once, since the BEAC's 2024 general report carries the auditors' report), `boj.org.jm` (Jamaica), `nbe.gov.et/files/` (Ethiopia), `bnr.rw` (a JavaScript app with no document list), `data.opendevelopmentcambodia.net` (refused twice, the second time with "do not retry"). Each of these is a browser job, not a search job.

**Jordan has a recurring trap**: the `portal.jordan.gov.jo/OD/files/` PDFs are deposit-insurance bodies, not the central bank. Two different files have now led there.

**Haiti has a live channel**: Le Nouvelliste carries a tender for the audit of the BRH's 2025–26 to 2027–28 financial statements, which confirms the bank appoints an external auditor. The award notice would settle it — try `emploi.lenouvelliste.com/appels-offre/`.

- **The BCEAO is settled.** The all-lots award notice that five rounds could not fetch — its URL is 364 characters and WebFetch rejects it on length — **was opened in a browser and read off the rendered PDF**. It names a titulaire and a suppléant for the head office and for every national directorate. When WebFetch refuses a URL on length, a browser tool settles it in one call; stop retrying with offsets.
- **BEAC is settled but imperfectly.** Its 2015 statutory auditors' report names KPMG and Mazars Cameroun jointly, signed at Yaoundé on 11 March 2016. That PDF is a scan and the two names extract as garbled text; the record says so in its own sentence. The 2023 report on beac.int is the clean replacement, and beac.int is robots-disallowed to the fetcher — a browser tool would settle it, as it did for the BCEAO.
- **The ECB's own auditor is Baker Tilly GmbH & Co. KG Wirtschaftsprüfungsgesellschaft**, Frankfurt, signed 12 February 2025 for 2024. Keyed to `ECB`, so it reaches all 21 euro-area countries.
- **Three methods worth repeating.** The *offset re-read* should be the default second move on any annual report that appears to have no auditor's report — Somalia's sat at about character 150,000 of 239,000. *Cross-pollination* beat targeted searching: Guinea's report came out of a Mauritania search, Djibouti's out of a Comoros search, Liberia's out of a Libya search. A *monetary-policy board resolution approving the audited statements* named the firm for Ecuador, where the bank publishes no auditor's report; Latin American and some African banks publish these.
- **Brunei is one OCR pass away.** The BDCB Annual Report 2025 lists an Independent Auditor's Report at pages FS 5–FS 9 and those pages carry no extractable text — the same shape as Fiji, the Maldives and Mozambique.
- **Sudan is a judgement call.** The Central Bank of Sudan Act 2002 says the accounts shall be audited in accordance with the General Audit Chambers Act 1999. That names a statute, not a body, so it is logged unavailable rather than promoted to "General Audit Chamber".
- Dead this round: Tonga, Curaçao and Sint Maarten, San Marino, Cambodia (its 2022 annual report contains no auditor's report at all), Laos, Turkmenistan, Belarus, Madagascar, Libya, Mauritania, DR Congo, Burundi, Algeria, Cabo Verde, Palestine, Yemen, São Tomé, Venezuela, Haiti (a tender notice, no award). Iran, Cuba, Syria and Eritrea were not reached inside budget. Of the 115 left, 50 have already been tried and logged in `gaps.json`'s `auditors_unavailable`; 65 have never been tried.
- **Round 20's two new methods.** A bank's own dedicated "external auditors" web page settled Namibia (Deloitte Namibia and Grand Namibia, joint) — that page type had not been tried before and is worth looking for elsewhere. A letter of transmittal settled Seychelles where the auditor's report annex would not extract.
- **Two shapes to expect again in Commonwealth small states.** Joint audits: Namibia, and Lesotho (Moteane, Quashie & Associates with SizweNtsalubaGobodo Grant Thornton), each recorded as one printed string. Hybrids where a supreme audit institution is the statutory auditor but a private firm does the work: Seychelles (Grant Thornton Abu Dhabi on the Auditor General's behalf) and Papua New Guinea.
- **Three that need OCR, not another search.** Fiji (Reserve Bank annual report pp. 79–81), the Maldives (MMA AR2024 pp. 125–127) and Mozambique (financial statements 2018 pp. 6–9) each have the right document open at the right page, and the auditor's report page is image-only and extracts blank.
- Round 20 reached no auditor document at all for Zimbabwe, Angola, Eswatini, Macao or Bhutan. The Gambia's 2023 annual report carries no audited financial statements, only a summary account table. Malawi's 2024 statement exists online only as a Scribd upload behind a JavaScript wall. Myanmar's law failed to fetch as a PDF; a .docx on myanmartradeportal and an unofficial translation on cbm.gov.mm are untried.
- **The BCEAO's seven remaining national directorates.** Niger is done (Mazars Niger as titulaire, KMC S.A. as suppléant, FY2024–2029, from the 1 August 2024 award notice, which covers Niger alone — confirmed by an offset read of the whole 902-character page). The all-lots award notice exists but **cannot be fetched because its URL is 364 characters long and WebFetch rejects it on URL length**; a second copy under `/files/2024-01/` is 369 characters and fails identically. This is NOT a document-length problem and offsets do not help — an earlier round diagnosed it wrongly and round 19 wasted a retry on that. It needs a mirrored copy with a shorter URL, a different host, or a browser tool.
- **EUR-Lex is settled for now.** Round 18 found a newer consolidated text at `CELEX:01999D0070-20240627` — the 2021 version is what EUR-Lex serves under the old ELI path, and earlier rounds had been working from it. The 2024 text plus five later decisions gave the current auditor for the whole euro area, Croatia included. Check for a newer consolidation before assuming it is still current.
- Never attempted: Jordan, Qatar, Armenia, Georgia, Azerbaijan, Uzbekistan, Kyrgyzstan, Tajikistan, Moldova, Albania, North Macedonia, Montenegro, Paraguay, Guatemala, Belize, Guyana, Suriname, Barbados, Bahamas, Jamaica. Tried and unavailable: Ethiopia (Proclamation 591/2008 art. 8 requires an annual external auditor, names no firm), Rwanda (the fetch returned BNR Regulation 12/2017, not Law 48/2017), Bosnia (the audit chapter is a download link only).
- **Don't retry via annual report:** Croatia, Serbia, Bahrain, Botswana — their PDFs extract the narrative but drop the auditor's report page, and Botswana's is scanned images. Don't retry BEAC via beac.int (robots-disallowed); target "BEAC Etats financiers IFRS certifiés" elsewhere.
- Trinidad and Tobago is **settled** (round 25): BDO T&T replaced the Auditor General as external auditor for the year beginning 1 October 2023, after the Auditor General's Office said it could not accept the appointment. The statutory auditor remains the Auditor General; the work was done by BDO T&T, and both are in the record.
- Panama has no central bank.

### 2. Banknote printers — 62%
**BanknoteNews is the vein.** **Hit rate is about a third, not a half**, and the yield sits in 2023–2026 posts and specifically in commemorative notes — nine of fourteen records last round came from posts dated 2023 or later. **Go at the newest entry per country, not the highest denomination.** Many recent entries carry no Printer field at all rather than "(Unknown)".

 It gave 11 of 13 printer records in round 23. Its per-note entries carry a literal `Printer:` field. The query shape that works is `banknotenews <country> <currency> new note confirmed "Printer"`, then fetch the entry for the newest or highest denomination. About half read `Printer: (Unknown)`, so triage is cheap — one search, one fetch, keep or discard. **Unworked there**: COD, AGO, GIN, LSO, SOM, ERI, DJI, COM, TUN, BEAC, BCEAO, TJK, TKM, LAO, MMR, BTN, MDV, MAC, OMN, QAT, BHR, SYR, LBN, PSE, URY, SLV, CYM, ECU, BIH, MKD, MNE.

**wbs.org.ua can no longer be walked**: its index page 1 is readable but deep links and pages 2–5 are refused, so its articles must be reached through search or not at all.

**The vein to run next is the issuing bank's own new-series press release.** It worked three times in four attempts in round 21 — Iceland ("printed by De La Rue Plc. in the UK"), Fiji (De La Rue International Limited) and Seychelles. It is the only vein that produced a printer name stated plainly enough to file. **BanknoteNews** is a per-country searchable archive that routinely names printers and gave Afghanistan.

**A page already mined can have a second half.** The Tunisian piece used in round 20 only for its "prints abroad" list also names the Arab states that print domestically, with the works named — three records from one fetch (Saudi Arabia, Algeria, Jordan).

**PWPW and G+D are now closed too.** PWPW's archive returns the same four banknote customers from three different pages, all recorded; everything else it names is passports, e-ID or tachographs. G+D's case-study pages are equipment and software — cash management, inspection systems, cash centres — not printing. **The euro area is structurally closed**: Slovakia's production page names no producer, making six euro banks that state nothing. Do not spend a round on Finland, Slovenia, Estonia, Latvia, Lithuania, Cyprus, Malta, Croatia or Luxembourg.

**Blocked, not closed**: bcu.gub.uy is robots-disallowed (Uruguay); the Venezuelan and Myanmar works both returned site errors. Landqart's Bahamas page thanks four firms as partners without assigning a role, so none can be called the printer — a Central Bank of the Bahamas source would close it.

**The customer-list sweep is closed. Do not re-run it.** Round 19 found Note Printing Australia's customer page and round 20 asked whether other printers publish one. None does. Customer, reference, client and "who we work with" pages were searched at De La Rue, Giesecke+Devrient, Crane, Oberthur Fiduciaire, IDEMIA, Veridos, Bundesdruckerei, Goznak, KOMSCO, PWPW, Orell Füssli, CBPM, Canadian Bank Note, Royal Joh. Enschedé, Thomas Greg & Sons, SPMCIL, Peruri and Pakistan Security Printing. Oberthur markets "over 70 central banks among references" and names none. Canadian Bank Note names one client, New Zealand, already recorded. Banque de France prints for "more than twenty countries" and names none.

**What replaced it — two page types that do yield.** PWPW's *news archive* names customers one release at a time; Paraguay and the Dominican Republic came from it and it almost certainly holds more. Giesecke+Devrient's *per-country case-study and interview pages* are the other live vein; the Armenia record came from one, and G+D has similar pages for other countries.

**CBPM is closed.** The "Is China Printing Your Banknotes?" article names nine customers — Brazil, India, Nepal, Poland, Thailand, Bangladesh, Malaysia, Sri Lanka, Pakistan — and every one is already recorded.

**Algeria cannot be fetched at all**: bank-of-algeria.dz is robots-disallowed, so it needs a third-party source. Zimbabwe needs care — one source is Fidelity Printers *denying* that it prints Zimbabwe dollars. A Tunisian news piece says Morocco, Egypt, Saudi Arabia, Algeria, Sudan and Jordan print domestically while Tunisia, Qatar, Kuwait, Bahrain, Oman, Lebanon, Libya, Syria, Mauritania, Djibouti, Comoros and Palestine print abroad; it names no works or firm, so nothing was filed, but it says Saudi Arabia, Jordan and Algeria have their own works worth hunting and that hunting a domestic works for the others is wasted effort.

**Most central banks print their own money.** Three rounds running, state works have been most of the yield, and the row was thin partly because nobody had recorded them. For each country, ask first whether its own bank runs a printing works; its site usually answers.
**The euro area is now mostly closed.** The ECB names none of the eleven works that print euro notes and publishes no allocation table. Five banks name their own works and are recorded — Spain (IMBISA, 80% Banco de España-owned, printing roughly 12% of total euro production), Austria (OeBS), Portugal (Valora), France and Germany. Round 19 checked five more one at a time and **all five state nothing**: Italy's page describes its banknote service and printing phases but never says it prints euro notes; Greece's statements mention only circulation and the Eurosystem allocation; the Dutch bank says it moved to printers "in Germany and Great Britain" in 2011 without naming them, and Joh. Enschedé stopped printing notes at the end of 2016; Belgium's page says only that it puts notes into circulation; Ireland's Currency Centre was printing in 2018 but a parliamentary answer says the majority are "produced elsewhere". Do not re-run these five. Untried: Finland, Slovakia, Slovenia, the Baltics, Cyprus, Malta, Croatia, Luxembourg.

A single joint Banque de France release with the OeNB and Banco de Portugal yielded two records at once. **Multi-bank cooperation releases are worth hunting** for exactly this reason.

### 3. Outside reserve managers — 154 ties at 36 banks, 103 of them Norway
**The World Bank's own RAMP channel is worked out.** Every central bank it has named is already recorded (Ecuador, Kosovo, Liberia, Zimbabwe, Armenia, Cabo Verde, Bosnia, Paraguay). New names on the Global Network and "RAMP voices" pages are the Pension Agency of Georgia, the Turkic Investment Fund, Korea National Pension Service, Panama Savings Fund and the FAO — none is a central bank. Further members must come from the *member bank's* own site or newsletter.

**Central Banking's award archive is thinning for named pairings.** The 2022 BNP Paribas AM, 2023 Invesco, 2020 Amundi and 2025 Franklin Templeton asset-manager profiles describe mandates in detail but keep the client anonymous ("undisclosed central bank", "Mediterranean central bank"). The 2019 Citi custody profile names the Central Bank of Kuwait and Norges Bank only in the page's organisation metadata tags, never in readable text — not filed, but both are worth chasing from Citi's or the banks' own side.

**New known blanks**: Chile's reserves page confirms "dos administradores externos" running about 3% of the portfolio and names neither; the UK Exchange Equalisation Account names only the Bank of England as HM Treasury's agent; OMFIF's external-managers chapter names seven firms and anonymises all 73 banks surveyed; Samoa, Fiji and Vanuatu each state they manage reserves internally.

**Unresolved, not negative** — retry later: Peru's BCRP transparency PDF returned a bot-protection stub, and Lesotho's and Tanzania's 2024 annual reports failed with site errors.

**RAMP does NOT publish its membership.** It only counts, and the counts contradict each other across the World Bank's own pages: "over 70" (2024), "75th member" (April 2024), "over 80" (May 2025), "more than 90" (October 2025), "a record 95" (April 2026). Round 18's fourteen RAMP ties were each assembled from an individual press release; roughly 80 members remain unidentified, and the same search run year by year, in Spanish, French and Portuguese too, will keep yielding them.

**Say what the source says.** Most RAMP announcements describe advice, technical assistance or training; only Seychelles states that RAMP actually manages a portfolio. Never upgrade membership or advice into management.

**The best remaining vein:** small open economies that publish a standalone reserves management report. The Central Bank of Seychelles' International Reserves Management Report 2025 named three outside parties in one document.

**Named but unnamed:** Botswana, the Trinidad HSF, Timor-Leste, Namibia, Ghana and Kazakhstan all confirm external managers and custodians without naming one firm. Botswana's IFSWF self-assessment says international managers run about half the Pula Fund, plus a global custodian and an investment consultant — not one is named. The BIS Banking Department says it manages mandates for central banks and names no client.


### 3a. Gold custodians — 14%, and slowing
**The method is the note to the accounts, not the gold page.** Four countries in round 23 disclosed a location table only in the notes to their financial statements and advertised it nowhere else: Portugal (note 2, a table headed "Gold was held in the following institutions"), Belgium (note 1), Türkiye (a gram-level table by location), Mauritius (note 7). Search for the statements PDF and read the gold note directly, with offset re-reads at 100,000-character steps.

**What is deliberately not filed**: gold *lending* (the Czech National Bank lending gold to other central banks; Bulgaria's deposits with unnamed commercial banks), and country-level answers that name no institution — Czechia's London share, Italy's three foreign shares ("primarie banche centrali"), Austria's roughly 140 tonnes given only as "the U.K." and "Switzerland", Kazakhstan's "specialised foreign repositories". Sri Lanka, Nepal and Serbia have a gold note that names only the LBMA valuation source.

**Two strong open leads**: the Bank of Greece's 2024 full-notes statements historically carry the location table, reached through an athens.euronext.com redirect that was never completed; and Romania, where the "Rezerva de aur" page sits behind a menu link search will not return, with Romanian press carrying a BNR statement that about 60 tonnes sit in a Bank of England account. **Not reached at all for budget**: South Korea, Thailand, Malaysia, Egypt, Jordan, Nigeria, Kenya, Tanzania, Zambia, Ukraine, Georgia, Mongolia, Cambodia, Brazil, Argentina, Venezuela, Ecuador, Bolivia, Singapore, Japan, Taiwan.

**Central banks disclose their gold custodians freely and their portfolio managers almost never.** Latvijas Banka's 2024 annual report names the Bank of England as the store of its gold in the same chapter where it refuses to name its seven external fixed-income managers. That asymmetry gave 27 records at 11 countries in one round, all from official sources: an RBA question-and-answer page, a Bundesbank release with four locations and tonnages, a Bank of Finland release with five custodians and their shares, a Riksbank notice, De Nederlandsche Bank's gold page, the SNB's balance-sheet questions, the Reserve Bank of India's half-yearly reserves report, and an Irish parliamentary answer.

This is a relation of its own — `holds its gold reserves in custody` — with its own sentence in `SAY` and its own entry in `build_net.py`'s `REL` map. It is not the same thing as the gold dataset in `events_gold.json`, which gives tonnage per country and names no custodian. **Keep storage and management apart in the wording**: a bank holding gold "as bailee" leaves ownership with the depositor.

**Still unworked and likely to disclose**: Poland, Portugal, Belgium, Italy, Spain, Denmark, the Philippines, Sri Lanka, Nepal, Thailand, Malaysia, and the Bank of England's own statistics on who holds gold accounts with it.

**Why the manager row stays stuck.** Brazil's standalone reserves report says the reserves are managed internally; Turkey's 2024 reserves chapter says the same. The UAE selects external managers from "the top ten globally" and names none; the HKMA runs 30% externally, including all its listed equity portfolios, and names none. Every asset-manager and Central Banking hit this round was anonymised.

### 4. Revolving door — now the shallowest it has been
**The method:** go to the central bank's own governor or board page, or the private firm's own board page, and read the career list. Do not search for scandal.
**Closed as blanks:** BCEAO and BEAC publish no board biographies at all — this killed the best remaining lead. Solomon Islands has the most detailed Pacific board page found and still yields nothing, because no employer is characterised. Taiwan's three senior officials are wholly public careers; China looks like a genuine blank, its senior PBoC careers running between state bodies.
**Still worth trying:** Cambodia, Laos, Myanmar, Brunei (BDCB annual report PDFs under cms.bdcb.gov.bn; Baiduri Bank's own governance disclosure prints director biographies), Tonga.
**Named candidate:** Taiwan's CBC board also seats Dong Jui-pin, who chairs Mega Financial Holding — not filed because Mega is likely Ministry of Finance-controlled and the CBC states no ownership. Settling document: Mega's major-shareholders table.
**The denominator moves.** The inside-influence score divides each country's count by the highest anywhere, which the United States holds. Any round adding US records re-checks the whole map.

### 5. Governor dismissals
Thirteen of the seventeen leads left from round 4 are closed, each recorded with what it turned out to be. Prefer the bank's own release, the government gazette or a wire agency — several Central Banking pages are paywalled after the first paragraph.

### 6. Corruption cases — treat as near-exhausted by ordinary search
Round 5 retried Bahrain, Saudi Arabia, Oman, Taiwan and Singapore in Arabic, Chinese and English and found nothing. **Don't spend another round on local-language retries.** Taking this further needs a different source type: court bulletins, supreme audit institution reports, parliamentary questions, central bank annual reports' own disciplinary notes. Still with no case and not retried: UAE, Qatar, Jordan, Brunei, Macao, Samoa, Fiji. San Marino's Confuorti and Buriani rulings still need a court or news source.

## How long to finish

**The union floor was dealt with in round 21.** A tie held by a currency union now shows in every member country, the way corruption cases already did. In `app.js`, `linksOfCountry` reads `BYCB` for the country's union as well as for the country, and `cbOfLink` expands any union code. **Union-wide records are keyed to the union code** (`ECB`, `BCEAO`, `BEAC`, `ECCB`), not to the head-office country: the old head-office rule is reversed, and merge scripts must no longer map `BCEAO`→`SEN`, `BEAC`→`CMR`, `ECCB`→`KNA`. `coverage.py` expands union codes too, which revealed it had been understating corruption cases, revolving door and swap lines for several rounds.

**What remains is a smaller floor: ten places have no central bank at all**, so no auditor, printer or manager record can ever exist for them — Panama, Kiribati, Tuvalu, Nauru, Micronesia, the Marshall Islands, Palau, Andorra, Monaco and Liechtenstein. They are listed in `gaps.json` under `no_central_bank` and left in the 206-place denominator, so every service row is understated by about five points. The reachable ceiling for those rows is 196 of 206, or 95%.

**Three of the categories can reach 100% and three cannot**, and conflating them is what makes the question unanswerable.

**Can finish:** external auditors (every bank has a law naming its auditor); the Federal Reserve seam (a countable 246 profiles, now thinning — round 16 got 12 records from ~30 names against round 15's 19 from 24); and the five patterns already complete because a source publishes the whole list.

**Cannot finish:** corruption cases, governor removals, and revolving door outside closed sets. No complete count exists anywhere, so the "35–45%" in `about.html` is a judgement made while compiling and will stay one. These approach completeness asymptotically.

**Estimate: 4 to 6 more rounds** for everything finishable. Yield by round: 35, 34, 33, 56, 50, 24, 34, 42, 40, 21, 14, 13.

**The bottleneck is now access, not search, and the fix is the browser.** Four scanned auditor reports have been settled by opening the page and reading it — Botswana, Serbia, the Maldives, Brunei — after every text extraction returned them empty. Still waiting on that method: Bahrain, Barbados, Fiji's annual report, Eswatini, the Bahamas, Rwanda's document list, Taiwan's untitled publication links, Iceland's gold explainer, Greece's gold note, Cambodia's 2023 report. **That list is most of what is left on the two finishable rows.** A round spent entirely in the browser would likely settle more than a round spent searching.

**Two rules have now been applied consistently enough to be settled policy.** A source saying a firm is a *supplier* is not a printing statement: Denmark was rejected on that ground in round 24 and Trinidad in round 25, and Denmark was then filed properly in round 25 when the bank's own page named De La Rue as the printer of the 2028 series. And gold placed in accounts for yield is not custody: Bolivia's own report names six institutions holding 19.91 tonnes in gold accounts and none of them was filed.

**Round 24 is the first round where every row slowed at once**, and the reason is the same in each: the cheap sources are spent. Auditors now cost about three fetches per settled country and three full reads ended in nothing because those banks print no auditor's name at all. Gold fell from 22 records to 3 — the notes-to-the-accounts method produced one of them, and the rest of the easy disclosers are done. Printers held up best, at 12 new places, but the archive's hit rate is a third rather than a half.

**What is left is mostly not search, it is access.** Greece's gold note needs a host that refused the fetch twice; Cambodia's 2023 annual report is one approval away; Barbados, Brunei, Fiji, Eswatini and the Bahamas need a browser rather than a fetcher. The remaining work is less about finding documents than about opening the ones already found.

**External auditors has hit the scan wall.** The offset re-read is now exhausted on the Bahamas, Serbia, Botswana, Barbados, the Maldives, Uzbekistan and Eswatini — their auditor pages carry no machine-readable text in any year or file form, and Uzbekistan's annual report series contains no financial statements at all. **The method that breaks this is opening the scanned page in a browser and reading it**: that settled Botswana (EY, Plot 22 Khama Crescent, Gaborone, unmodified opinion for 2025, statements approved by the Board on 27 March 2026) off a page every extraction returns empty. The same should settle Serbia, Barbados, the Maldives, Eswatini, Brunei, Fiji's annual report and the Bahamas. One caveat learned the hard way: **get the PDF URL from a fresh search each time** — two URLs recorded in earlier notes are now 404.

**Three banks are fetcher-blocked rather than sourceless, and a browser settles them.** Peru fell this way: the Memoria 2024 chapter 7 PDF sits behind Incapsula to the fetcher and opens normally in Chrome. Romania fell to an offset read of a mirror. **North Macedonia did not**: nbrm.mk sits behind a Cloudflare bot check, which is not something to work around — it needs the file fetched by hand or a different mirror.

## Questions the user has settled (don't reopen)
- **Unproven allegations** (10 November 2026). Show both and let the reader switch. A tick box, "Count cases that are allegations alone", sits under the legend on the three case layers, ticked by default. Cleared, a bank whose only cases are allegations stays on the inside layer scored at nothing rather than dropping off, and its box says any score in the paragraph was written with allegations counted.
- **Which statuses count** (10 November 2026). The one rule is above. Romania is the edge case: Olteanu was convicted with a final five-year sentence in October 2020, the conviction was annulled as time-barred on 31 March 2023, and the court still confiscated the €1 million. It is left out because no conviction stands, and its writeup gives all three facts. **If reversed, it is one string to move between `CC_OUT` in `app.js` and `CC_COUNTED`/`CC_NOT_COUNTED` in `build_final.py`.**

## UI behaviour to preserve
- **Hover:** only diamonds light their ties; lines take no hover or click. Small sources of their own (`hot-lines`, `hot-nodes`); never re-filter the country layer on hover. `setP`/`setF` skip repeated paint and filter calls.
- **Markers:** each party has one fixed spot computed in `build_net.py` — the city point, or a spot 1–8 km around it, over land. Never screen-pixel offsets; markers must not move with zoom. Clicking a stack opens a list (`stackBox`).
- **Ghosts:** parties whose kind of tie is switched off stay as faint grey diamonds that can still be clicked (`net-ghost`).
- **Index:** the box under Find a place (`indexItems`, `drawIndex`). `selectEntity` turns ties on if the party is hidden and draws a ring (`drawSel`).
- **Details box:** positioned in pixels by `openDet`, drags by its top edge. `#det` does not scroll; `#detBody` does. `makeResizable(el, onStart)` adds 8 handles to `#det` and `.win`.
- **Anchors:** `anchorsOf` reads multi-currency anchors, so Belarus (0.2 EUR + 0.5 RUB + 0.3 USD) draws to Moscow. Ilzetzki–Reinhart–Rogoff give "n.a." for Russia and 19 others, which is why they have no outgoing line.
- **Small places:** `build_final.py` adds real outlines from `ne10` (`D.XSHAPE`) for Monaco, Tuvalu and Nauru.
- **Recenter:** `#centerBtn` runs `recenter()`; `homePadding()` removes the padding a box adds.

## Keep these two in step
`about.html`'s "How much of the subject is here" table and the figures in this handoff describe the same thing for different readers. **Change both together**, and take the numbers from `coverage.py` and the build output rather than estimating.
