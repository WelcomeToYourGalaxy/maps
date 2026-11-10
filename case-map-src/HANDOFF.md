# Globalization Case Map: handoff for a new chat

Last updated: 10 Nov 2026. Replaces the 7 Nov handoff.

Live page: `globalization.html` in WelcomeToYourGalaxy/maps (published from `main`). Source folder: `case-map-src/`. Rebuild with `python3 case-map-src/build.py`.

## Current state (10 Nov 2026)

- **946 cases** in the page data.
- **925 of 946 cases have rounded "what happened to people" text** (`whole`), fact-checked and merged. **The first pass is complete.** Order used: largest harms first. Batches r26f_whole_h1 through h10 are in `rounds/`, each with its checker log. Briefs: `docs/WHOLE.md` (researcher) and `docs/CHECKW.md` (checker). Merge with `merge_whole.py`.
- **21 cases still blank** after the first pass (searches ran out, or the sources would not open): Mali Office du Niger, Zambia Camdex, Morelos/Samir Flores, Peñarroya Santo Amaro, Batang, Cilacap, Java 7, Multan WWTP, Shell Vila Carioca, Pacitan, Tanjung Kasam, Equatorial Palm Oil/Jogbahn, Heinda tin, Shell Ogbodo, Tayan Nuur, IPP4 Al-Manakher, BNP Rwanda, Yakjin, Vedan Thi Vai, DRC bank channels, Arab Bank. Seven of these were already judged to have no credible information (Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher); the rest can be retried.
- **7 older blanks** (no credible information): Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher.
- **Company descriptions:** cards now show a one-line "what this company is" (`desc` on each case company), then "In this case:" and its role. 93 + 67 names checked and merged (`rounds/r26f_companies_1.json`, `_2.json`, merged with `merge_codesc.py`). About 830 names still lack one. Batch 1 inputs came from the 250 most-used names; 78 of its entries were blanked only because company sites refused to load and can be re-checked. Brief: `docs/COMP.md`.
- **Condition types:** every case has `ct` (types of condition attached to the money), read from its own sourced text and independently checked (`rounds/r26_cond_types.json`, log `_log.json`; brief `docs/COND.md`). Originally 344 cases were tagged `research`. **208 still tagged `research` after round 4.** Rounds so far: 1 (`rounds/r26f_conds_research_1.json`), 2 (`_2a`, `_2b`), 3 (`_3a`, `_3b`), 4 (`_4a`, `_4b`), inputs in `docs/r26_condr2_*.json` through `r26_condr4_*.json`, checker logs alongside, merged with `merge_conds.py`, brief `docs/CONDR.md`. **Rounds 5 and 6 are merged (10 Nov). Cases tagged `research` fell from 208 to 158.** Inputs `docs/r26_condr5_*.json` and `r26_condr6_*.json` (25 cases each); raw outputs and `_checked.json` files with logs in `rounds/`.

**Two new condition types were added** to `CTN` in `base.html`: `fincov` (financial covenants and use-of-proceeds terms: required rate of return, self-financing or debt-to-equity ratio, offtake undertaking, restriction on what the money may be spent on, required escrow or minimum balance) and `admin` (institutional or planning covenants: create an agency, adopt an action plan or manual, set up a unit or committee, submit plans for the lender's review). These released 12 cases whose checked text had fitted no type (`rounds/r26f_conds_retype_1.json`, proposal and desk check in `docs/r26_ct_retype_proposed.json` and `_checked.json`).

**`merge_conds.py` now carries checked text through even when `ct` is empty**, instead of discarding it, and leaves the case tagged `research` so it stays on the to-do list. It also skips text already present, so re-running is safe.

**What the checkers keep rejecting, in order of frequency:**
1. A lender's general policy presented as a term of this loan (ADB's Safeguard Policy Statement, JICA's Guidelines, the Equator Principles, IFC Performance Standards applied to all financial-sector clients, a bank's own sector policy, an IFC Environmental and Social Review Summary's standard framing). This is the single biggest source of false positives.
2. `none` claimed where the source is merely silent. "General in nature" means unrestricted use of proceeds, not an absence of conditions. All seven `none` tags in round 6a failed on this.
3. Facts about a loan (pricing, fees, maturity, collateral the database does not record) read as conditions.
4. An appraisal forecast, a readiness timeline, or a description of what happened read as a covenant.
5. Terms set after the harm.

Untagged-but-confirmed texts (Saguling, Mangla, Giza, Cambodia resin, Ibadan, Wilmar) do not merge because no type fits; a "financial or administrative terms only" type could be added if wanted. No separate checker brief exists for this job; the checker prompt: open every source, say "required" only where the source says the money depended on it, and terms set after the harm or bank-wide policy do not count.
- **People totals:** 18 people have a checked `total` ("In context" line on their card; `rounds/r26f_people_totals.json`, `merge_people_total.py`, brief `docs/PEOPLE.md`). Not yet researched: about 16 company heads (Vale, Union Carbide, Trafigura, Renco, Lundin, Shell Nigeria, Unocal, Elliott's Paul Singer); missing years for Lagarde, Lipton, Wolfensohn, Zoellick, McNamara, Woods could be filled. The World Bank projects API was refused to agents.
- **Still to do:** add more people and lender offices (gaps below); extend the buyers list (only 49 cases have documented buyers).

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
5. **Build:** `python3 case-map-src/build.py` (should print "loan-condition cases matched 173 of 173").
6. **Test** headless Chromium via Playwright (`NODE_PATH=$(npm root -g)`), served with `python3 -m http.server 8766` in the repo. Re-rendering menus can make Playwright's own clicks hang; clicking through `page.evaluate(() => el.click())` is reliable. Check for page errors and the case count.
7. **Push:** `git add globalization.html case-map-src && git commit` (attribution trailers from the session reminder), then `git pull --rebase -q && git push -q`. If the push is refused by the git proxy, attach the repo to the session first (add_repo, push access).

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

- Everything through condition round 6 is merged, built, tested and pushed (10 Nov).
- Note: pushing needs the repo attached to the session first (`add_repo`, push access), or the git proxy refuses with a 403.

## Pending case-text fixes

- Applied 7 Nov evening (`rounds/r26f_textfix_1.json`, checked; log alongside; script `merge_textfix.py`, which handles "people:<id>" keys, paths like `lenders[0].role`, and `lenders_append`): Peru 1977 inflation, Theun-Hinboun, Elliott, Jirau, Lake Turkana, Vedanta, Gezhouba, Upper Atbara (Abu Dhabi fund added), Buchanan, Barishal, Caculo Cabaça, Celukan Bawang, Green Resources, Kompas/Tanjung Kasam, ICC Njeem post label, Vishnugad ($648M less two $100M cancellations = $448M), Tractebel on the Arequipazo card. Nathpa Jhakri already said the operator paid for the study.
- Still open: Cochabamba (Aguas del Tunari) still credits Wikipedia for shareholdings and lists it as a source. Barishal "first loan in May 2021" (Global Energy Monitor, blocked) sits before AidData's September 2021 signing date; unchecked. Tanjung Kasam capacity: Jakarta Post 2×55 MW vs AidData 130 MW. Several map-point labels say "Wikipedia coordinates" (location only, not facts).

## Open decisions for the owner

- Decided 7 Nov (owner left it to Claude): Agrokasa blanked (investment never made); GMR kept; Planafloro and ProRoutes accepted on Panel quotes of agreement sections; Suralaya kept with CAO doubt; Bataan and Escondida blanked (guarantees to banks and plain owner-debt terms are not lender conditions); Bastar, Kihansi and Bolivia keep tags with "agreed" wording; Bertin kept (agreed IFC action plan). Komodo keeps "fees"; Metolong kept (MCC is a listed co-funder); CBG kept (IFC loan active during the harm, plan dates given); Teresina and Dakar kept, credited to their planning documents.
- Keep al-Serraj (weakest Libya person)? Keep Arab Bank and UNICEF wells as contested? Payment services vs loans: how to present? Keep the nine `documents1.worldbank.org` links? Drop Kaziranga and Virunga-type cases if death counts are questionable?
- Decided: `loan-conditions.html` stays online. Decided 7 Nov: whole text runs largest harms first.

## Where coverage is thin

- People: 18 have totals; more people and more totals wanted.
- Lender offices: IDB, AfDB and BII directories blocked; IMF per-country pages not read; IFC and China Development Bank lists not reachable.
- Buyers of case output: 49 cases.
- Lender-financed projects; IMF and World Bank policy-loan conditions since 2015; Chinese state finance (AidData); Middle East and North Africa, Europe and Central Asia. Leads: `docs/backlog.json`; Payra, Mattala and Kyaukphyu not researched.
- Waiting on events: Bishoftu airport; Kerio Valley; Thar Block-1, Nam Ngiep 1, Kaliwa dam.

## Tool limits

- WebSearch is capped at about 200 calls per turn, shared by every agent in that turn. Run at most two or three research agents per turn, or they run out partway (this happened on 7 Nov).
- WebFetch now refuses URLs that have not appeared in a WebSearch result in the session ("provenance"), so case source links often can't be opened directly; each new source costs a search. SEC EDGAR full-text hits work well for listed firms.
- WebFetch has an hourly limit shared across agents, and some company sites refuse fetches; checkers then blank the facts, which can be re-checked later.