# Globalization Case Map: handoff for a new chat

Last updated: 7 Nov 2026. Replaces the 6 Nov handoff.

Live page: `globalization.html` in WelcomeToYourGalaxy/maps (published from `main`). Source folder: `case-map-src/`. Rebuild with `python3 case-map-src/build.py`.

## Current state (7 Nov 2026)

- **946 cases** in the page data.
- **478 cases have rounded "what happened to people" text** (`whole`), fact-checked and merged. The owner chose order 3: **largest harms first**. Rounds r26f_whole_h1 and h2 covered every case with recorded deaths or displacement (159 cases): 146 got text, 13 are blank (listed in `docs/r26_whole_order.json` via the case data; most failed because search ran out or EJAtlas pages would not render; retry them).
- **Batch h3 (7 Nov)** retried the 13 harm-ranked blanks (12 filled; Malawi still blank) and did the first 62 of `rest`. **Next:** `rest` from item 63 on (453 cases) in `docs/r26_whole_order.json` (no death or displacement count, so no harm ranking). Briefs: `docs/WHOLE.md` (researcher) and `docs/CHECKW.md` (checker). Merge with `merge_whole.py`.
- **7 older blanks** (no credible information): Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher.
- **Company descriptions:** cards now show a one-line "what this company is" (`desc` on each case company), then "In this case:" and its role. 93 names checked and merged (`rounds/r26f_companies_1.json`, merged with `merge_codesc.py`). About 899 names still lack one. Batch 1 inputs came from the 250 most-used names; 78 of its entries were blanked only because company sites refused to load and can be re-checked. Brief: `docs/COMP.md`.
- **Condition types:** every case has `ct` (types of condition attached to the money), read from its own sourced text and independently checked (`rounds/r26_cond_types.json`, log `_log.json`; brief `docs/COND.md`). 344 cases are tagged `research`: a lender is named but the write-up does not say what it required. These need real research next; the filter shows them under "Lender named, but its conditions are not yet found".
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

## Pending case-text fixes (flagged by checkers, not yet applied)

- Peru 1977 inflation measure; Theun-Hinboun 7,500 vs 4,800; Peru / Elliott $11.3M vs $11.4M and $58.45M vs $58M; Jirau, Lake Turkana, Vedanta still credit Wikipedia; Gezhouba dates; Upper Atbara Abu Dhabi fund $90M missing from lenders; Buchanan $77m vs $62m; Barishal dates; Caculo Cabaça MW; Celukan Bawang MW; Green Resources dates; Kompas 2013 Batam figure; ICC Njeem press release.
- Nathpa Jhakri whole text: the income study was paid for by the operating company; self_reported could be set true.
- Vishnugad Pipalkoti: case says a $648M loan; the World Bank's 2022 paper gives a $448M net commitment.
- Tractebel: card may mean the 1990s Suez-owned energy group, not today's engineering firm; description left blank.

## Open decisions for the owner

- Keep al-Serraj (weakest Libya person)? Keep Arab Bank and UNICEF wells as contested? Payment services vs loans: how to present? Keep the nine `documents1.worldbank.org` links? Drop Kaziranga and Virunga-type cases if death counts are questionable?
- Decided: `loan-conditions.html` stays online. Decided 7 Nov: whole text runs largest harms first.

## Where coverage is thin

- People: project totals per person not yet added; more people wanted.
- Lender offices: IDB, AfDB and BII directories blocked; IMF per-country pages not read; IFC and China Development Bank lists not reachable.
- Buyers of case output: 49 cases.
- Lender-financed projects; IMF and World Bank policy-loan conditions since 2015; Chinese state finance (AidData); Middle East and North Africa, Europe and Central Asia. Leads: `docs/backlog.json`; Payra, Mattala and Kyaukphyu not researched.
- Waiting on events: Bishoftu airport; Kerio Valley; Thar Block-1, Nam Ngiep 1, Kaliwa dam.

## Tool limits

- WebSearch is capped at about 200 calls per turn, shared by every agent in that turn. Run at most two or three research agents per turn, or they run out partway (this happened on 7 Nov).
- WebFetch has an hourly limit shared across agents, and some company sites refuse fetches; checkers then blank the facts, which can be re-checked later.
