# Globalization Case Map: handoff for a new chat

Last updated: 10 Nov 2026. Replaces the 7 Nov handoff.

Live page: `globalization.html` in WelcomeToYourGalaxy/maps (published from `main`). Source folder: `case-map-src/`. Rebuild with `python3 case-map-src/build.py`.

## Current state (10 Nov 2026)

- **946 cases** in the page data.
- **925 of 946 cases have rounded "what happened to people" text** (`whole`), fact-checked and merged. **The first pass is complete.** Order used: largest harms first. Batches r26f_whole_h1 through h10 are in `rounds/`, each with its checker log. Briefs: `docs/WHOLE.md` (researcher) and `docs/CHECKW.md` (checker). Merge with `merge_whole.py`.
- **21 cases still blank** after the first pass (searches ran out, or the sources would not open): Mali Office du Niger, Zambia Camdex, Morelos/Samir Flores, Peñarroya Santo Amaro, Batang, Cilacap, Java 7, Multan WWTP, Shell Vila Carioca, Pacitan, Tanjung Kasam, Equatorial Palm Oil/Jogbahn, Heinda tin, Shell Ogbodo, Tayan Nuur, IPP4 Al-Manakher, BNP Rwanda, Yakjin, Vedan Thi Vai, DRC bank channels, Arab Bank. Seven of these were already judged to have no credible information (Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher); the rest can be retried.
- **7 older blanks** (no credible information): Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher.
- **Company descriptions:** cards now show a one-line "what this company is" (`desc` on each case company), then "In this case:" and its role. 93 + 67 names checked and merged (`rounds/r26f_companies_1.json`, `_2.json`, merged with `merge_codesc.py`). About 830 names still lack one. Batch 1 inputs came from the 250 most-used names; 78 of its entries were blanked only because company sites refused to load and can be re-checked. Brief: `docs/COMP.md`.
- **Condition types:** every case has `ct` (types of condition attached to the money), read from its own sourced text and independently checked (`rounds/r26_cond_types.json`, log `_log.json`; brief `docs/COND.md`). Originally 344 cases were tagged `research`. **208 still tagged `research` after round 4.** Rounds so far: 1 (`rounds/r26f_conds_research_1.json`), 2 (`_2a`, `_2b`), 3 (`_3a`, `_3b`), 4 (`_4a`, `_4b`), inputs in `docs/r26_condr2_*.json` through `r26_condr4_*.json`, checker logs alongside, merged with `merge_conds.py`, brief `docs/CONDR.md`. **Rounds 5, 6 and 7 are merged (10 Nov). Cases tagged `research` fell from 208 to 146, and every case on the map has now been tried at least once.** Inputs `docs/r26_condr5_*.json` through `r26_condr7_a.json`; raw outputs and `_checked.json` files with logs in `rounds/`.

**Two new condition types were added** to `CTN` in `base.html`: `fincov` (financial covenants and use-of-proceeds terms: required rate of return, self-financing or debt-to-equity ratio, offtake undertaking, restriction on what the money may be spent on, required escrow or minimum balance) and `admin` (institutional or planning covenants: create an agency, adopt an action plan or manual, set up a unit or committee, submit plans for the lender's review). These released 12 cases whose checked text had fitted no type (`rounds/r26f_conds_retype_1.json`, proposal and desk check in `docs/r26_ct_retype_proposed.json` and `_checked.json`).

**`merge_conds.py` now carries checked text through even when `ct` is empty**, instead of discarding it, and leaves the case tagged `research` so it stays on the to-do list. It also skips text already present, so re-running is safe.

**What the checkers keep rejecting, in order of frequency. Put this in every researcher brief:**
1. A lender's general policy presented as a term of this loan (ADB's Safeguard Policy Statement, JICA's Guidelines, the Equator Principles, IFC Performance Standards applied to all financial-sector clients, an IFC Environmental and Social Review Summary's standard framing, a bank's own sector or credit policy). This is by far the biggest source of false positives.
2. `none` claimed where the source is merely silent. "General in nature" means unrestricted use of proceeds, not an absence of conditions. All seven `none` tags in round 6a failed on this.
3. Facts about a loan (pricing, fees, maturity, collateral a database does not record) read as conditions. Write them as facts with no type.
4. An appraisal forecast, a readiness timeline, subproject selection criteria, or a description of what happened read as a covenant.
5. Terms set after the harm. Where the terms are the only ones documented and the case is worth keeping, say the dates on the face of the text so the gap is visible (Noor Ouarzazate, Mahenge).
6. A procurement label read as its opposite: "Partially Untied" and "General Untied" are not `tied`; a credit covering the value of one country's exports says what the money buys, not that buying there was required.

Untagged-but-confirmed texts (Saguling, Mangla, Giza, Cambodia resin, Ibadan, Wilmar) do not merge because no type fits; a "financial or administrative terms only" type could be added if wanted. No separate checker brief exists for this job; the checker prompt: open every source, say "required" only where the source says the money depended on it, and terms set after the harm or bank-wide policy do not count.
- **People totals:** 18 people have a checked `total` ("In context" line on their card; `rounds/r26f_people_totals.json`, `merge_people_total.py`, brief `docs/PEOPLE.md`). Not yet researched: about 16 company heads (Vale, Union Carbide, Trafigura, Renco, Lundin, Shell Nigeria, Unocal, Elliott's Paul Singer); missing years for Lagarde, Lipton, Wolfensohn, Zoellick, McNamara, Woods could be filled. The World Bank projects API was refused to agents.
- **Company descriptions:** 274 of 992 names have a one-line "what this company is" (`desc`). Batches 1 and 2 (`rounds/r26f_companies_1.json`, `_2.json`), then 3a and 3b (10 Nov, `_3a_checked.json`, `_3b_checked.json`, logs alongside). Merge with `merge_codesc.py`. Brief `docs/COMP.md`. 718 names remain; batches 4a and 4b were out at the end of 10 Nov.
- **People:** 18 of 173 have a checked `total` ("In context" line on their card; `rounds/r26f_people_totals.json`, `merge_people_total.py`, brief `docs/PEOPLE.md`). The World Bank projects API refuses agents.
- **Buyers:** 34 of 946 cases have a documented buyer of what the project produced (`window.PROD.chains`, 49 chains).

## Page changes made 7 Nov 2026

- **Lawsuits** is a new top-level section, placed below Complaints (`suitsHTML()`, switch `SECT.suits`, `isSuitLayer`): investor-treaty layers and creditor lawsuits moved here from Conditionalities, plus a button for the "company sued the state" pattern.
- **Investor-claims data is complete:** rebuilt from UNCTAD's full Excel release (1,332 cases, 1987–2023; `rounds/r26_isds_unctad.json`): cases, decided for investor, for state, settled, pending, US-dollar claims, US-dollar awards/settlements (other currencies not converted, so floors), and investors' home countries.
- **Conditionalities:** new "The cases, by type of condition" chips (FG group `ct`, `CTN` labels); private-lender block is now debt deals only; China (`lc:cn`) and Saudi/Qatar (`lc:tuff`) money layers moved to their lender rows (`LENDER_LC`).
- **"Other money, for comparison"** removed: FDI → Foreign companies row, foundations → Private foundations row, private debt → Banks row, bilateral debt → Other governments row; new rows for aid, money sent home, and debt payments (`FLOWROW`) under "Not lenders, but part of the same money".
- Chinese infrastructure count layer moved to the Chinese lender row; the exact-spot toggle now says which layers it applies to.
- **Contracts and Earnings** (was "Companies in roads, ports, power and water"): contracts, earnings by lender, Chinese firms' earnings, and company-funded deal layers (`ppi_*`).
- Coverage text for each kind of money compares case counts with sourced totals (`MK_COVER`; figures in `docs/r26_denoms.json`).
- Share-of-money text explains share buying vs foreign company investment (World Bank's 10% line) and why each is left out.
- Deaths/displacement notes moved to the end of "What happened to people". Timeline window has search and ordering. Year bar no longer runs off the edge (`S.y0` starts at `YMIN`). People marks follow case filters. Flat map repeats the world (`setRenderWorldCopies`) so Pacific cases such as Banaba sit on land.

## The owner's standards (non-negotiable)

- **No fabrication.** Every figure, date, name and quote must come from a page the researcher actually opened. If a source won't open, the fact is removed or the case is dropped. Disputed figures give who says what.
- **Don't make editorial choices for the owner in data work.** Include everything the source publishes.
- **Three tests for a case:**
  1. **Link:** a documented outside lender, development financier, public fund or foreign investor/owner tied to what happened. A foreign company that was only a contractor, supplier or buyer does **not** pass.
  2. **Actual harm:** people displaced, land or income lost, poisoned, jailed or killed, or land and water damaged. Feared or "at risk" harm does not count.
  3. **Timing:** the outside money or company was involved when the harm happened.
- **Contested:** if the lender or other sources dispute the link, set `confidence: "contested"` and give both sides. If the core harm rests on EJAtlas alone, drop the case.
- **Deaths:** count in `killed` only deaths caused by the project, the company, or forces acting for them. Everything else goes in `killed_note`, uncounted, with who reported it. Settlements without admission of liability leave deaths uncounted.
- **Workplace pay or dismissal disputes alone are not cases.**
- **Whole-picture text rules:** what the programme achieved where documented; lender-, company- or government-produced figures flagged as such ("no independent check was found"); plain figures; each kind of money gets its own full set of categories.
- **Writing:** plain, novice-friendly wording, short sentences, no purple prose, show figures rather than characterising them. No orange, yellow or neon colours; earthy and muted palettes.
- **Every batch is fact-checked by a separate agent before merging.**
- **Repo updates** are committed and pushed directly from chat.

## Workflow

1. **Research agent** (general-purpose, background) with a brief from `docs/` (`BRIEF17.md` for new cases; `WHOLE.md`, `COMP.md`, `COND.md` for the add-on texts). Extract current cases first: `python3 -c "import json;s=open('case-map-src/base.html').read();i=s.index('window.CASES = ')+15;json.dump(json.JSONDecoder().raw_decode(s[i:])[0],open('cases.json','w'))"`.
2. **Dedupe yourself before checking** (iso3, nearby coordinates, keywords).
3. **Fact-check agent** (separate, background): `docs/CHECK13.md` for cases, `docs/CHECKW.md` for whole text. Name the weak points.
4. **Merge:** back up `base.html`, copy the checked file into `rounds/`, then `merge.py` (cases), `merge_whole.py` (whole text) or `merge_codesc.py` (company descriptions). merge.py does not handle people; add those directly to `window.ENT`.
5. **Build inputs for the next batch** straight from `base.html` rather than from an old list. Conditions: cases with `research` in `ct`, minus ids already in any `rounds/r26f_conds_research_*.json`, ranked by `killed * 100 + displaced`. Companies: names in `companies[]` with no `desc`, ranked by how many cases use the name, passing up to four `uses` each for context.
6. **Build:** `python3 case-map-src/build.py` (should print "loan-condition cases matched 173 of 173").
7. **Test** headless Chromium via Playwright (`NODE_PATH=$(npm root -g)`), served with `python3 -m http.server 8766` in the repo. Re-rendering menus can make Playwright's own clicks hang; clicking through `page.evaluate(() => el.click())` is reliable. Check for page errors and the case count.
8. **Push:** `git add globalization.html case-map-src && git commit` (attribution trailers from the session reminder), then `git pull --rebase -q && git push -q`. If the push is refused by the git proxy, attach the repo to the session first (add_repo, push access).

## Case shape

Keys in every case: `id, title, place, iso3, lat, lng, point, start, end, mechanism, lenders[{name, role}], conditions, companies[{name, role, hq, hq_lat, hq_lng, desc?}], community, suppression, killed, killed_note, outcome, sources[{title, publisher, year, url}], confidence, confidence_note, lk[], cp[], rg, cx[], ecosystem, whole, ct[]`, and `kind` for newer cases. Optional: `ap`, `displaced`, `displaced_note`, `displaced_label`, `iso3_more`.

- `mechanism`: project, austerity, land, privatization, debt, trade
- `lk`: wb, ifc, miga, imf, icsid, idb, adb, afdb, ebrd, eib, aiib, reg, cn, bil, eu, priv, fdn, fdi
- `kind`: off, fdi, gra, prv, pay, gov
- `ct`: priv, prices, tax, cuts, deval, trade, labour, land, fees, invest, law, repay, tied, safeguard, none, research
- `rg`, `levers`, `cp`: as before (see BRIEF17.md).

## Money data

- **Share of money:** `window.MK_SHARE` from World Bank WDI net flows 2014–2023. Share buying and remittances excluded; the brief now explains why.
- **Investor claims:** complete, from UNCTAD's 31 Dec 2023 Excel file (`rounds/r26_isds_unctad.json`). The owner's copy of the file was attached in chat on 7 Nov 2026.
- **Private-loan layers:** `rounds/r24f_conds.json` (`prv_*`); lawsuits now show under Lawsuits, debt deals under Conditionalities.
- **Contracts, tied aid, company-funded deals, offices, live projects, loan-conditions layers:** unchanged (see `infra_*.py`, `docs/offices_notes.md`, `case-map-live-src/`, `loan-conditions-src/`).

## Push status

- Everything through condition round 7 and company batches 3a and 3b is merged, built, tested and pushed (10 Nov).
- Pushing needs the repo attached to the session first (`add_repo`, push access), or the git proxy refuses with a 403. A plain `git clone` works for reading without it.

## Pending case-text fixes

- Applied 7 Nov evening (`rounds/r26f_textfix_1.json`, checked; log alongside; script `merge_textfix.py`, which handles "people:<id>" keys, paths like `lenders[0].role`, and `lenders_append`): Peru 1977 inflation, Theun-Hinboun, Elliott, Jirau, Lake Turkana, Vedanta, Gezhouba, Upper Atbara (Abu Dhabi fund added), Buchanan, Barishal, Caculo Cabaça, Celukan Bawang, Green Resources, Kompas/Tanjung Kasam, ICC Njeem post label, Vishnugad ($648M less two $100M cancellations = $448M), Tractebel on the Arequipazo card. Nathpa Jhakri already said the operator paid for the study.
- Applied 10 Nov (`rounds/r26f_textfix_2.json`): Freeport-McMoRan's headquarters corrected to Phoenix (New Orleans was the old Freeport-McMoRan Inc. base); CIFI's to Panama City; Ecoener stated as holding 85% of Hidro Santa Cruz with Hidralia 15%; Thames Water's RWE ownership dated (2001 to October 2006, then Macquarie-led funds); Terminal Investment Limited corrected from "joint venture partner" to co-sponsor and sister company of Global Terminal Limited, which indirectly wholly owns the Lome terminal company. Both corrected headquarters markers were moved. Note `merge_textfix.py` writes strings, so numeric fields such as `hq_lat`/`hq_lng` must be set by a separate short script or they become strings.
- Still open: Cochabamba (Aguas del Tunari) still credits Wikipedia for shareholdings and lists it as a source. Barishal "first loan in May 2021" (Global Energy Monitor, blocked) sits before AidData's September 2021 signing date; unchecked. Tanjung Kasam capacity: Jakarta Post 2×55 MW vs AidData 130 MW. Several map-point labels say "Wikipedia coordinates" (location only, not facts).

## Open decisions for the owner

- Decided 7 Nov (owner left it to Claude): Agrokasa blanked (investment never made); GMR kept; Planafloro and ProRoutes accepted on Panel quotes of agreement sections; Suralaya kept with CAO doubt; Bataan and Escondida blanked (guarantees to banks and plain owner-debt terms are not lender conditions); Bastar, Kihansi and Bolivia keep tags with "agreed" wording; Bertin kept (agreed IFC action plan). Komodo keeps "fees"; Metolong kept (MCC is a listed co-funder); CBG kept (IFC loan active during the harm, plan dates given); Teresina and Dakar kept, credited to their planning documents.
- Keep al-Serraj (weakest Libya person)? Keep Arab Bank and UNICEF wells as contested? Payment services vs loans: how to present? Keep the nine `documents1.worldbank.org` links? Drop Kaziranga and Virunga-type cases if death counts are questionable?
- Decided: `loan-conditions.html` stays online. Decided 7 Nov: whole text runs largest harms first.

## What is left, and how to finish it

Counted from the page data on 10 Nov 2026. The About panel now carries these same shares, computed at build time, under "How complete this map is".

### 1. Company descriptions — 718 of 992 names left (biggest gap)
Run two agents per turn on 60 names each, then a fact-checker per batch. Build inputs by ranking names with no `desc` by how many cases use them (see the snippet in "Workflow" below). About 115 names clear per turn at the current rate, so roughly six more turns.
Expect most entries to come back corrected, almost always for the same fault: claiming slightly more than the cited page says. Tell each writer so up front. Honest blanks are the right outcome for small local firms, dissolved companies and subsidiaries with no published record.
This work keeps finding errors in case data that nobody had re-checked since the cases were written. Collect them and apply them through `merge_textfix.py` (see "Pending case-text fixes").

### 2. Condition types — 146 cases still tagged `research`
Every case has now been tried at least once, so these are all retries. 108 of the 146 already carry some conditions text; what is missing is a documented term the money depended on.
By lender: bilateral 47, private 34, IFC 29, foreign company 20, World Bank 17, Chinese state 17, other regional 15, foundations 9, MIGA 8, AfDB 8, ADB 5, IDB 5, EBRD 4, EU 4, IMF 3, EIB 2, AIIB 1.
The blanks cluster by lender, not by case, because of what can be fetched:
- **ADB is the most productive route.** Its document paths fetch directly: `https://www.adb.org/sites/default/files/project-documents/<proj>/<proj>-rrp-en.pdf`. The Recommendation of the President reports carry full covenant summaries.
- **EBRD** blocks automated fetching. Accountability-mechanism mirrors describe the complaints but not the financing terms. A mirror for EBRD project summaries would unlock Vares, Shah Deniz, IPP4 and TAP, which all went blank for this reason alone.
- **AfDB** returns client errors on project pages and appraisal paths; the Early Warning System mirror often records no project information. Thwake is blank for this reason.
- **IDB**: `iadb.org/document.cfm` and `mici.iadb.org` refuse direct fetches; the Accountability Console mirrors the MICI reports and works.
- **IFC**: `disclosures.ifc.org` project pages refuse direct fetches.
Before accepting any new entry, check it against the five recurring failures listed above. A lender's general policy read as a term of this loan is the most common by far.

### 3. Whole-picture text — 21 blanks
Seven were judged to have no credible information (Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher). The other 14 can be retried: Mali Office du Niger, Zambia Camdex, Penarroya Santo Amaro, Multan sewage plant, Shell Vila Carioca, Equatorial Palm Oil/Jogbahn, Heinda tin, Shell Ogbodo, Tayan Nuur, BNP Rwanda, Yakjin, Vedan Thi Vai, DRC bank channels, Arab Bank.

### 4. People — 155 of 173 lack a checked `total`
Not yet researched: about 16 company heads (Vale, Union Carbide, Trafigura, Renco, Lundin, Shell Nigeria, Unocal, Elliott's Paul Singer). Missing years for Lagarde, Lipton, Wolfensohn, Zoellick, McNamara and Woods could be filled.

### 5. Buyers — 34 of 946 cases
Only where a source documents who bought the output. This is a long tail and will never reach 100%.

### 6. Lender offices
IDB, AfDB and BII directories blocked; IMF per-country pages not read; IFC and China Development Bank lists not reachable.

### 7. New cases
Leads in `docs/backlog.json`. Thin regions: Middle East and North Africa, Europe and Central Asia. Not researched: Payra, Mattala, Kyaukphyu. Waiting on events: Bishoftu airport, Kerio Valley, Thar Block-1, Nam Ngiep 1, Kaliwa dam.

### Two figures to settle, not to guess
- **Mundra**: the card says the plant is 4,150 MW; the source opened in the company work gives 4,000 MW. Likely nameplate against the UMPP's nominal size. Check against the plant's unit configuration before changing either.
- **Shuakhevi**: the card says 185 MW; IFC gives 178 MW for Shuakhevi and 184 MW for the financed project including the 6 MW Skhalta. Decide which the card should state.

## Tool limits

- WebSearch is capped at about 200 calls per turn, shared by every agent in that turn. Run at most two or three research agents per turn, or they run out partway (this happened on 7 Nov).
- WebFetch now refuses URLs that have not appeared in a WebSearch result in the session ("provenance"), so case source links often can't be opened directly; each new source costs a search. SEC EDGAR full-text hits work well for listed firms.
- WebFetch has an hourly limit shared across agents, and some company sites refuse fetches; checkers then blank the facts, which can be re-checked later.
- Hosts that refuse automated fetches, found the hard way: ebrd.com, afdb.org project pages, iadb.org/document.cfm, mici.iadb.org, disclosures.ifc.org, Reuters, The Guardian, and sec.gov's cgi-bin EDGAR search. These work: adb.org document paths, sec.gov/Archives, Companies House, the Early Warning System and Accountability Console mirrors, and most PDF annual reports.
- A blocked lender site is not evidence that no condition existed. Record it as blocked so a later round knows to try a mirror.

## The completeness panel

`completeHTML()` in `base.html` computes the "How complete this map is" section of the About panel from the page data at build time: cases and countries, and the share of cases with whole-picture text, with a statement of what the money came with, with settled lender terms, plus company descriptions, people records and documented buyers. It is injected into `window.ABOUT_HTML` at the `<!--COMPLETENESS-->` marker. Add a row there when a new kind of information starts being filled in; never write these figures in by hand.
