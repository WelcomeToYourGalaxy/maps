# Globalization Case Map — handoff for adding more cases

Live page: `globalization.html` in WelcomeToYourGalaxy/maps (published straight from `main`).
This folder (`case-map-src/`) is everything needed to keep adding cases and rebuild the page.
State at handoff (4 Nov 2026, after round 17): **855 cases** in 116 countries, 3,001 complaint records, 579 lender offices.

## The owner's standards (non-negotiable)

- **No fabrication.** Every figure, date, name and quote must come from a page the researcher actually opened. If a source won't open, the fact is removed or the case dropped. Disputed figures give who says what.
- **Three tests for a case:**
  1. **Link:** documented outside lender, development financier, public fund or foreign investor/owner tied to what happened. The tie can come from the lender's own records, a contract, a court, a complaint office or an independent source. A foreign company that was only a contractor, supplier or buyer does **not** pass.
  2. **Actual harm:** people displaced, land or income lost, poisoned, jailed or killed, or land and water damaged. Feared or "at risk" harm does not count.
  3. **Timing:** the outside money or company was involved when the harm happened.
- **Contested:** if the lender or other sources dispute the link, set `confidence: "contested"` and give both sides. If the core harm rests on EJAtlas alone, drop the case.
- **Deaths:** count in `killed` only deaths caused by the project, the company, or forces acting for them. Put everything else in `killed_note`, uncounted, with who reported it. Settlements without admission of liability leave deaths uncounted.
- **Workplace pay or dismissal disputes alone are not cases.**
- **Writing:** plain, novice-friendly wording, no purple prose, show figures. No orange, yellow or neon colours anywhere.
- **Every batch is fact-checked by a separate agent before merging.**

## Workflow that has worked (rounds 9–17)

1. **Research agent** (general-purpose, background). Give it a brief modelled on `docs/BRIEF17.md`; the brief points to `docs/BRIEF13.md`, `BRIEF.md` and `BRIEF2.md` for rules and case shape. Have it dedupe against the current case list: extract it with `python3 -c "import json;s=open('case-map-src/base.html').read();i=s.index('window.CASES = ')+15;json.dump(json.JSONDecoder().raw_decode(s[i:])[0],open('cases.json','w'))"`. Output `{"cases": [...], "extend": [...], "dropped": [...]}`.
2. **Before checking, dedupe again yourself.** Search the existing cases by iso3, nearby coordinates and key words. Earlier rounds often re-found Rempang, Okomu, Sino-Metals and similar.
3. **Fact-check agent** (separate, background), following `docs/CHECK13.md`. It writes `rXXf.json` and `rXXf_log.json`. Tell it the specific weak points to check: timing, owner at the time of harm, single-source facts, Wikipedia-only facts, and coordinates.
4. **Merge:** copy the checked file into `case-map-src/rounds/`, back up `base.html`, then run `python3 case-map-src/merge.py rounds/rXXf.json`. The merge appends cases, applies `extend` (lenders_add, lk_add/lk_remove, cp_add, sources_add, fields_add appended), `complaint_links`, `complaint_fixes`, and back-links complaints onto cases.
5. **Build:** `python3 case-map-src/build.py`. This writes `../globalization.html` (about 19 MB) and prints "loan-condition cases matched 173 of 173".
6. **Test** in headless Chromium with Playwright: serve the repo with `python3 -m http.server 8766`, load the page, and wait about 16 seconds. Look for page errors and check the case count in the left panel.
7. **Push:** `git add globalization.html case-map-src && git commit -m "..." && git pull --rebase && git push`. Two bots commit daily (live data, other maps), so always pull with rebase first. If the rebase conflicts on `case_map_live.json`, keep the newer data.

## Case shape (keys in every case)

`id, title, place, iso3, lat, lng, point, start, end, mechanism, lenders[{name, role}], conditions, companies[{name, role, hq, hq_lat, hq_lng}], community, suppression, killed, killed_note, outcome, sources[{title, publisher, year, url}], confidence (documented|contested), confidence_note, lk[], cp[], rg, cx[], ecosystem`. Optional keys: `ap` (point approximate), `displaced`, `displaced_note`, `displaced_label`, `iso3_more`.

The research file also carries `levers` and `lvwhy` per case; merge.py moves them into the separate lever store.

- `mechanism`: project, austerity, land, privatization, debt, trade
- `lk` (lender keys): wb, ifc, miga, imf, icsid, idb, adb, afdb, ebrd, eib, aiib, reg, cn, bil, eu, priv, fdn, fdi
- `rg`: Africa south of the Sahara / East Asia and the Pacific / Europe and Central Asia / Latin America and the Caribbean / Middle East and North Africa / South Asia
- `levers`: deval, prices, cuts, tax, priv, trade, land, fees, labour, project, finance
- `cp` (complaint offices): ip, cao, mici, am, irm, ipam, eibcm, ppm, icm, aiddata, ncp, jica, dfc, afd

## Where coverage is thin (best targets next)

- **IMF and World Bank policy-loan conditions since 2015** (price, tax, pay and job cuts; privatizations; required law changes) with the condition shown in the lender's own documents. Round 15 found none because imf.org blocked the researcher. Round 17 kept 6 of 15 (3 more became extends): most well-known episodes are already mapped, and IMF letter-of-intent PDFs still fail to open, though press releases do. Try WebFetch on imf.org country-report pages, the IMF's Monitoring of Fund Arrangements (MONA) data, or copies on eurodad.org and brettonwoodsproject.org.
- **Lender-financed projects rather than foreign-company cases.** Round 15 found 14 of its 20 new cases were foreign investment only, because almost every complaint-office case with documented harm is already mapped. Sources that worked:
  - Accountability Counsel's case list
  - Inclusive Development International (IFC lending through banks and funds)
  - Bank Information Center
  - Human Rights Watch and Amnesty reports since 2015
  - Global Witness, Forest Peoples Programme, Urgewald, Recourse
  - Coalition for Human Rights in Development ("Uncalculated Risks")
- **Chinese state finance.** Use AidData's Global Chinese Development Finance records, court rulings and the reporting AidData cites. The certificate bundle for AidData pages from an earlier session may be needed.
- **Regions with few cases:** Middle East and North Africa (37), Europe and Central Asia (84).
- **Leads that earlier rounds left open:** see `docs/backlog.json`, and the `dropped` lists in past rounds marked "not yet researched". From round 17: Accountability Counsel's list was never read (page refused); Human Rights Watch, Amnesty, Global Witness, Forest Peoples Programme, Both ENDS and "Uncalculated Risks" were not gone through one by one; Payra, Mattala and Kyaukphyu not researched; Aché Finca 470 report would not open; Bangladesh 2023–25 power and VAT could return with a measure of household loss.
- **Leads waiting on events:**
  - Bishoftu airport, Ethiopia: revisit if the African Development Bank board approves its US$500m loan.
  - Kerio Valley (CAO complaint): harm only preliminary so far.
  - Thar Block-1, Nam Ngiep 1, Kaliwa dam: harm only expected so far.

## Other data on the page and how it updates

- **Projects under way and planned (World Bank):**
  - `case-map-live-src/update_live.py` runs daily via `.github/workflows/case-map-live.yml` and writes `case_map_live.json`.
  - It covers active and pipeline projects, risk ratings, documents, borrower, team leaders, listed places, and contract awards (individual consultants left out).
  - It flags concern from `case-map-live-src/ip_projects.json`, and from P-codes named in cases.
- **Lender offices:**
  - These are embedded in `base.html` as `window.LOFF`; `docs/offices_notes.md` has sources and gaps.
  - **Gaps:** the IDB, AfDB and BII directories were blocked. The IMF's 86 resident offices need its per-country pages (`imf.org/en/countries/resrep/<iso3>`). The IFC and China Development Bank office lists were not reachable.
- **Loan-conditions layers:** they come from `D.json.gz`, built by `loan-conditions-src/`; `lc.js` and `adapter.js` draw them. The "loan condition led to harm" rings match the loan-conditions map's 173 records to cases, using the `_DUP` table in `build.py`.
- **The Atlas cartouche** is in `base.html` as `window.PLATE_IMG` (webp). It was repainted with "CASE MAP" in Cinzel.

## UI pieces most often edited (all in `base.html`)

| What | Where |
|---|---|
| Brief | `briefHTML()` |
| Cases section | `buildKey()`, `lchHTML()`, `pastHTML()` |
| Layer menu | `buildLayers()`, `wireLayers()`, `liveHTML()`, `officesHTML()`, `infraSec()` (infrastructure layers, under The Companies) |
| Category switches | `SECT` |
| Cards | `detailCase()`, `detailLiveWB()`, `detailOffice()` |
| Card shrink, move-aside and resize | `dragDet()` |
| Hiding markers at the globe's edge | `limbHide()` |
| About page | `window.ABOUT_HTML` |

Patch with exact-string replacements (Python `str.replace`, asserting each match is unique), then rebuild.

## Web fetch limit

WebFetch has an hourly limit shared across agents. Running several agents at once hits it; they should wait for the next UTC hour and use no other route.
