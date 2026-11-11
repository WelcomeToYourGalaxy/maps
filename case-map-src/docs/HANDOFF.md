# Globalization Case Map: handoff for a new chat

Last updated: 11 Nov 2026 (late afternoon). Replaces the earlier 11 Nov handoffs.

Live page: `globalization.html` in WelcomeToYourGalaxy/maps (published from `main`). Source folder: `case-map-src/`. Rebuild with `python3 case-map-src/build.py`.

## Start here

1. `git clone https://github.com/WelcomeToYourGalaxy/maps` — reading works without anything else. **To push, attach the repo to the session first** (`add_repo`, push access), or the git proxy refuses with a 403.
2. Read this file and `docs/COMP.md` or `docs/CONDR.md`, depending on which job you are doing.
3. Build the batch inputs from `base.html` itself, never from a list in this file — the counts here go stale. The snippets are under "Workflow" below.
4. Run two research agents, then a separate fact-checker per batch. Merge only checked files.
5. Build, test headless, commit, push, and update this file with the new counts.

The two jobs worth doing next: **condition retries** (102 cases, all third or fourth attempts; round 10b inputs are already built) and **people totals** (127 of 173). Company descriptions and whole-picture text are both finished as first passes. Everything else is listed under "What is left, and how to finish it".

## Current state (11 Nov 2026, late afternoon)

**946 cases**, in 126 countries and territories. The page builds clean and loads headless with no errors; `build.py` prints "loan-condition cases matched 173 of 173".

These are the figures the About panel shows under "How complete this map is", computed from the page data at build time:

| What | Filled | Share |
| --- | --- | --- |
| Rounded "what happened to people" paragraph (`whole`) | 939 of 946 | 99% |
| Cases that say what the money came with (`conditions`) | 937 of 946 | 99% |
| Lender's terms looked for and settled (not tagged `research`) | 844 of 946 | 89% |
| Company names with a line saying what the firm is (`desc`) | 912 of 992 | 92% |
| People with a checked `total` | 46 of 173 | 27% |
| Cases with a documented buyer | 34 of 946 | 4% |

### Whole-picture text — complete
Batches `rounds/r26f_whole_h1` through `h11_checked.json`, each with a checker log. Briefs `docs/WHOLE.md` (researcher) and `docs/CHECKW.md` (checker). Merge with `merge_whole.py`.
939 of 946 cases have text. Round h11 cleared all 14 retryable blanks, so the only 7 left are the ones judged to have no credible information: Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher. **Nothing is queued on this job.**

### Condition types — 102 cases still tagged `research`
Nine rounds are merged (`rounds/r26f_conds_research_1.json` through `_9a_checked.json`, inputs in `docs/r26_condr*.json`, checker logs alongside). Merge with `merge_conds.py`, brief `docs/CONDR.md`.
**Every case has been tried at least twice**, so what remains are third and fourth attempts. Round 8 settled 19 of 146 (16 of 86 development-bank cases, 3 of 60 financed by bilateral, Chinese state, private, foreign-company or foundation money). Round 9a settled 22 of 70 after its checker blanked 11 of the 33 it submitted; round 10a settled 3 of 43, a thin round by design because 11 of its blanks were the intermediary cases 9a's checker had already rejected and the writer left them alone rather than resubmitting them. Splitting batches by lender rather than by harm is what makes this work — the groups need completely different routes.

Two types were added to `CTN` in `base.html` on 10 Nov, which released 12 stranded cases (`rounds/r26f_conds_retype_1.json`; proposal and desk check in `docs/r26_ct_retype_proposed.json` and `_checked.json`):
- `fincov` — financial covenants and use-of-proceeds terms: a required rate of return, a self-financing or debt-to-equity ratio, an offtake undertaking, a restriction on what the money may be spent on, a required escrow or minimum balance.
- `admin` — institutional or planning covenants: create an agency, adopt an action plan or manual, set up a unit or committee, submit plans for the lender's review.

`merge_conds.py` now carries checked text through even when `ct` is empty, instead of discarding it, and leaves the case tagged `research` so it stays on the to-do list. It skips text already present, so re-running is safe. Six cases carry text with no type on purpose: four record loan terms rather than conditions (Kotopanjang, Ramu, Hambantota, Santo António) and two record a condition's absence (Sendou, where the AfDB found environmental and social covenants were left out of the agreement; Wilmar, where a Category C rating meant the Performance Standards were never triggered).

### Company descriptions — first pass complete, 912 of 992
Cards show a one-line "what this company is" (`desc`), then "In this case:" and the role. Merged: batches 1, 2, 3a/3b, 4a/4b, 5a/5b, 6a/6b, 7a/7b, 8a/8b, 9a/9b (`rounds/r26f_companies_*_checked.json`, logs alongside). Merge with `merge_codesc.py`, brief `docs/COMP.md`, which now carries the three recurring faults and the discrepancy-reporting step in the writer's own instructions.
**Every one of the 992 names has now been attempted at least once.** The 80 without a description came back blank with a sound note and are finished, not pending. Do not re-queue them; a later round could retry only the ones whose note records a blocked host rather than an absent source.

### People — 155 of 173 lack a checked `total`
`rounds/r26f_people_totals.json`, `merge_people_total.py`, brief `docs/PEOPLE.md`. Not yet researched: about 16 company heads (Vale, Union Carbide, Trafigura, Renco, Lundin, Shell Nigeria, Unocal, Elliott's Paul Singer). Missing years for Lagarde, Lipton, Wolfensohn, Zoellick, McNamara and Woods could be filled. The World Bank projects API refuses agents.

### Buyers — 34 of 946 cases
`window.PROD.chains`, 49 chains. Only where a source documents who bought the output; this will never reach 100%.

## Page changes made 11 Nov 2026

- No page-code changes. All of 11 Nov went to data: whole-picture text round h11, condition retry rounds 8 and 9a, and company batches 8 and 9.

## Page changes made 10 Nov 2026

- **The kind-of-money list opens closed.** `S.kindOpen` starts `false`, so "Every kind together" is still the selected kind (all 946 cases) but its panel — brief, key and layers — no longer unfolds on load, and all seven kinds are visible at once. One click opens it. `resetLayers()` returns to the same closed state, so Reset matches how the page opens.

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
5. **Build inputs for the next batch** straight from `base.html` rather than from an old list. Conditions: cases with `research` in `ct`, minus ids already in any `rounds/r26f_conds_research_*.json`, ranked by `killed * 100 + displaced`. Companies: names in `companies[]` with no `desc`, **minus every name already present as a key in any `rounds/r26f_companies_*.json`**, ranked by how many cases use the name, passing up to four `uses` each for context. Skipping the already-attempted names matters: batch 5a wasted 10 of its 60 slots re-researching names that earlier batches had already looked for and deliberately blanked. A name that came back blank with a sound note is finished, not pending.
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

- Everything through condition retry round 9a, whole-text round h11 and company batch 9 is merged, built, tested and pushed (11 Nov afternoon). Company descriptions and whole-picture text are both complete as first passes.
- Out at the time of writing and not yet merged: condition retry round 10a (43 institutional cases, `docs/r26_condr10a.json`) and people totals round 2 (155 people, `docs/r26_people_in2.json`). Round 10b inputs are built but unassigned (`docs/r26_condr10b.json`, 62 cases with bilateral, Chinese state, private, foreign-company or foundation money). Each needs its own fact-checker before merging.
- Pushing needs the repo attached to the session first (`add_repo`, push access), or the git proxy refuses with a 403. A plain `git clone` works for reading without it.

## Pending case-text fixes

- Applied 7 Nov evening (`rounds/r26f_textfix_1.json`, checked; log alongside; script `merge_textfix.py`, which handles "people:<id>" keys, paths like `lenders[0].role`, and `lenders_append`): Peru 1977 inflation, Theun-Hinboun, Elliott, Jirau, Lake Turkana, Vedanta, Gezhouba, Upper Atbara (Abu Dhabi fund added), Buchanan, Barishal, Caculo Cabaça, Celukan Bawang, Green Resources, Kompas/Tanjung Kasam, ICC Njeem post label, Vishnugad ($648M less two $100M cancellations = $448M), Tractebel on the Arequipazo card. Nathpa Jhakri already said the operator paid for the study.
- Applied 10 Nov (`rounds/r26f_textfix_2.json`): Freeport-McMoRan's headquarters corrected to Phoenix (New Orleans was the old Freeport-McMoRan Inc. base); CIFI's to Panama City; Ecoener stated as holding 85% of Hidro Santa Cruz with Hidralia 15%; Thames Water's RWE ownership dated (2001 to October 2006, then Macquarie-led funds); Terminal Investment Limited corrected from "joint venture partner" to co-sponsor and sister company of Global Terminal Limited, which indirectly wholly owns the Lome terminal company. Both corrected headquarters markers were moved. Note `merge_textfix.py` writes strings, so numeric fields such as `hq_lat`/`hq_lng` must be set by a separate short script or they become strings.
- Applied 10 Nov evening (`rounds/r26f_textfix_3.json`), all dated rather than overwritten: Ambatovy (none of the three named owners still holds a stake — Sherritt exited 2020, Korea Resources merged into KOMIR 2021, Sumitomo transferred its interest 2026); Aracruz (merged into Fibria 2009, later Suzano); Anglo American Platinum (demerged 31 May 2025, renamed Valterra Platinum, Anglo keeping about 19.9%); Adriatic Metals (acquired by Dundee Precious Metals 3 September 2025, renamed DPM BH Holdings); Base Resources (acquired by Energy Fuels 2 October 2024); Bougainville Copper (about 72.9% held by the Autonomous Bougainville Government and the people of Bougainville after the January 2026 transfer); Prodeco (starting to return its Colombian mining contracts, February 2021); and Caracol, which no longer states Harvard Management Company ownership flatly but gives both sides.
- Applied 10 Nov late evening (`rounds/r26f_textfix_5.json` and `_6.json`): San Carlos-Panantza, whose card said the Chinese owners were not named in its sources and put the marker in Beijing (they are named: the CRCC-Tongguan consortium, ExplorCobres as Tongguan Nonferrous Metals Group's project subsidiary, EcuaCorriente a joint venture of Tongling Nonferrous Metals 70% and China Railway Construction Corporation 30%; marker removed, no source gives a Beijing address); Frontier Energy, called a Danish private equity fund that majority-owns and manages both plants, where Proparco says only that Frontier Energy II Alpha K/S is a fund headquartered in Denmark managed by Frontier Investment Management; Golden Star's unsupported Denver marker, removed; Sadiola, where IAMGOLD's 2024 Annual Information Form does not mention the mine and records the December 2022 sale of its Senegal, Mali and Guinea interests to Managem; Kamoa Copper, replacing "majority owner of operator" with the filing's structure (DRC state 20%, holding company 49.5% Ivanhoe, 49.5% Zijin, 1% Crystal River); Johnson Controls, incorporated in Ireland and headquartered in Cork by its own 10-K, marker moved from Milwaukee; Interagua and Irish Water, where the cards' dates conflict with the CAO closure report and Uisce Eireann's own annual report and both sides are now given; Jamuna Multipurpose Bridge Authority, renamed the Bangladesh Bridge Authority with effect from 18 December 2007; Sega Mining corrected to Seguenega Mining SA; and Indorama, where the IFC says Singapore against the Bretton Woods Project's "Indonesian".
- Applied 10 Nov late night (`rounds/r26f_textfix_7.json`, 25 records from the batch 8 checkers): Rio Tinto's Simandou interest restated as indirect and partial (SimFer is 15% the Guinean State and 85% SimFer Jersey, itself 53% Rio Tinto and 47% CIOH); Theun-Hinboun's September 2014 share transfers; SPDC's US$2.4bn sale to Renaissance reported March 2025; ZCCM's formation in 1982 and the August 2015 transfer of the government's 60.3% to the IDC; Kaltim Prima Coal's 61,543-hectare licence from 1 January 2022 against the card's 90,000 hectares; Toll becoming a Japan Post division on 28 May 2015; Westinghouse becoming CBS Corporation in 1997; Union Fenosa into Gas Natural Fenosa in April 2009; SONACOS privatised 2005 and renamed SUNEOR in 2007; Proactiva's 2013 passage to full Veolia ownership; Rio Algom into BHP Billiton in 2000; SN Power's sale by Norfund to Scatec; Feronia's concession figures; Seli's 2015 split; and the Luanshya card, which no longer credits Wikipedia. Not applied: Santo Antonio Energia, whose verified name does not match any company key, and SK E&C's identity as SK Ecoplant, which rests on a filing name alone.
- Applied 10 Nov late night (`rounds/r26f_textfix_8.json`, 25 records from the batch 9 checkers): TAP's own November 2025 page lists five shareholders at 20% each with no Axpo; Umeme's concession ended 31 March 2025 with the network passing to UEDCL; Gazprom's Sakhalin purchase reported done in April 2007, both sides given on the December 2006 date; SKS Microfinance into IndusInd Bank from 4 July 2019; Rossing's majority to China National Uranium in 2019; PT Vale Indonesia's June 2024 divestment leaving MIND ID largest on about 34%; South32's binding agreement of 7 July 2025 to divest Cerro Matoso; Philex's own 2023 filing giving Mandaluyong rather than Pasig (noted on the card, marker not moved for want of sourced coordinates); Thor SA named as the Cato Ridge operator with Tato Holdings as the restructured former parent; and renamings for SOCO/Pharos, Sime Darby Plantation/SD Guthrie, Tiomin/Vaaldiam, Salini Impregilo/Webuild, Red Back/Kinross and Ratchaburi/RATCH.
- Still open: Cochabamba (Aguas del Tunari) still credits Wikipedia for shareholdings and lists it as a source. Barishal "first loan in May 2021" (Global Energy Monitor, blocked) sits before AidData's September 2021 signing date; unchecked. Tanjung Kasam capacity: Jakarta Post 2×55 MW vs AidData 130 MW. Several map-point labels say "Wikipedia coordinates" (location only, not facts).

## Questions the owner has not settled

These came out of the company work and are deliberately not changed, because changing them could make a card worse:
- **Biopalm Energy's headquarters** is given as Singapore; the only source describes the Siva Group as Chennai-based and says nothing about Biopalm's own base. Remove the unsourced HQ (which removes a map marker) or find a source?
- **COBRAC's headquarters** (Rieux, France) rests on Portuguese Wikipedia alone. The peer-reviewed paper that confirms the 1989 rename to Plumbum Mineração gives only the plant site.
- **Alcoa's headquarters**: the card says Pittsburgh, the 2016 S-1 says 390 Park Avenue, New York. Alcoa has used both; the S-1 is evidence about 2016, not about now.
- **Mundra capacity**: card 4,150 MW, source 4,000 MW. Likely nameplate against the UMPP's nominal size; check the unit configuration.
- **Shuakhevi capacity**: card 185 MW; IFC gives 178 MW for Shuakhevi and 184 MW for the financed project including the 6 MW Skhalta.
- **Antea Cement capacity**: Titan says 1.5 Mt/yr, IFC's 2008 appraisal says 1.4 Mt/yr. A genuine disagreement between two credible sources, not an error.
- **Three shareholding splits on cards rest on nothing retrievable**: Huaneng Shandong Ruyi (Pakistan) Energy at 51/49, KEPCO SPC Power at 60/40, and Iso Tech at 4%. The NEPRA licence states no percentages at all, the Power Engineering piece calls KSPC a joint venture with no split, and Iso Tech's 4% is on no page that opens. Unconfirmed rather than contradicted.
- **Johnson Controls' "Glendale corporate campus"**: Cork is confirmed from the 10-K, but the checker could read only the first 100,000 characters, where neither Glendale nor Milwaukee appears at all.
- **BWDB's embankment figure** rests on Banglapedia, a published national encyclopedia rather than a crowd wiki. At the edge of what `docs/COMP.md` allows.

## Open decisions for the owner

- Decided 7 Nov (owner left it to Claude): Agrokasa blanked (investment never made); GMR kept; Planafloro and ProRoutes accepted on Panel quotes of agreement sections; Suralaya kept with CAO doubt; Bataan and Escondida blanked (guarantees to banks and plain owner-debt terms are not lender conditions); Bastar, Kihansi and Bolivia keep tags with "agreed" wording; Bertin kept (agreed IFC action plan). Komodo keeps "fees"; Metolong kept (MCC is a listed co-funder); CBG kept (IFC loan active during the harm, plan dates given); Teresina and Dakar kept, credited to their planning documents.
- **`kalangala-oil-palm` carries a `wb` lender key that looks wrong.** The World Bank projects API returns zero for Uganda plus Kalangala, oil palm or vegetable oil, and IFAD's own evaluation gives the financing as a US$20m IFAD loan of April 1997 with private and government cofinancing, names no World Bank or IDA money, and records the Bank as the project's *cooperating institution* only until August 2004, when UNOPS took over and the Bank withdrew over its forestry safeguards policy. Case data untouched. Dropping `wb` would move the case out of the World Bank layers; the question is whether it still passes the link test on another lender or should come off the map.
- Keep al-Serraj (weakest Libya person)? Keep Arab Bank and UNICEF wells as contested? Payment services vs loans: how to present? Keep the nine `documents1.worldbank.org` links? Drop Kaziranga and Virunga-type cases if death counts are questionable?
- Decided: `loan-conditions.html` stays online. Decided 7 Nov: whole text runs largest harms first.

## What is left, and how to finish it

Counted from the page data on 10 Nov 2026. The About panel now carries these same shares, computed at build time, under "How complete this map is".

### 1. Company descriptions — first pass complete (912 of 992)
Nothing is queued. The 80 blanks each carry a note; only those blocked by a refusing host are worth a retry. If new cases add names, run the same shape: two writers on 50-60 names each per turn, then a fact-checker per batch, building inputs by ranking undescribed, never-attempted names by how many cases use them.

**Three faults dominate every batch. Put all three in the WRITER's brief, not just the checker's** — doing so cut the blank rate and raised the restraint, though the correction rate stayed near two thirds:
1. **Claiming more than the cited page says.** Nationality is the commonest invention by far: a page saying a firm is "deeply rooted in France" does not say it is French, and a foreign-sounding name is not a source. Same for a headquarters city, a stock exchange, a founder, a product range, a country count. A ticker in logo alt text is not a stated listing. Never take a figure's year from the article's date.
2. **Describing a parent and presenting it as the subsidiary.** If no source names the company in the key, it cannot be described. A source describing what a firm did at a project site is not a description of the firm. Where a key names two entities and the sources cover one, describe that one and say nothing about the other — that rule saved four entries in round 6b. The exception is a documented identity link: CMS Nomeco survived only because an SEC filing shows CMS Oil and Gas was formerly named CMS NOMECO.
3. **Attaching a figure or shareholding to the wrong entity.** Round 6 found three: a provincial state body controlling the listed company rather than the group, a 10% stake held by a three-member consortium rather than two named firms, and a debt belonging to a subsidiary in another country. Round 5 found a report listing stakes without saying which company they sat in, one of which belonged to a different company entirely.

Honest blanks run 5-20% and are the right outcome. Do not re-queue a name that came back blank with a sound note.

**A batch with no blanks is a warning, not a win.** Batch 9b returned 49 descriptions from 49 of the map's least-used names; its checker then had to correct 31 of them, almost all for claiming more than the cited page said. Tell the checker when a batch's blank rate is below the usual range and ask it to blank what the sources do not carry. The checkers' own correction rate held near two thirds all the way through (8a 24 of 53, 8b 43 of 54, 9a 37 of 48, 9b 31 of 49), so the separate check is doing the work, not the writer's restraint.

**Market-data aggregators are the single commonest bad source** — StockAnalysis, Screener.in and similar profiles. They do not qualify under `docs/COMP.md`, and a figure from one should be replaced with a filing or removed. Sponsored "featured company" pages (mining-technology.com and the like) are the same problem with a different look.

**This job doubles as an audit of the case data**, and that is most of its value — about 40 discrepancies in five rounds. Ownership decays fastest: a card naming owners from when the case was written reads as a current claim. Collect them, have the checker verify each against a source it opens itself, then apply through `merge_textfix.py`. Phrase history with dates rather than overwriting ("X held 38% at the time; the 2024 filing does not mention the mine"), and give both sides where sources disagree.

**Unsupported headquarters are common**, and several map markers sat at addresses no source gives. Remove the coordinates rather than guess a replacement, and say so on the card. Done so far: Compañía de Tierras Sud Argentino, ExplorCobres (marker was in Beijing), Golden Star (Denver). Moved on evidence: De Beers to London, Johnson Controls to Cork, Freeport to Phoenix, CIFI to Panama City.

### 2. Condition types — 102 cases still tagged `research`
All retries. By lender after round 9a: bilateral 38, private 29, foreign company 19, IFC 16, Chinese state 16, other regional 12, foundations 9, MIGA 7, AfDB 7, IDB 3, EBRD 3, EU 3, World Bank 2, IMF 1, ADB 1.

**Retire the MIGA cases rather than re-searching them.** Round 9a tested this properly: miga.org project pages serve normally but publish only cover type, amount, fiscal year, sector and status. MIGA's Policy on Environmental and Social Sustainability speaks only in general terms about its *standard* contract of guarantee, says nothing about any particular guarantee, and postdates most of these. No guarantee contract or term sheet is published anywhere.

**AfDB is the one institution where a mirror was tested and does not substitute.** The Early Warning System serves AfDB project records but carries only amount, sector, borrower and board date, often with "No project information available at the time of disclosure", and links back to afdb.org rather than mirroring any appraisal. afdb.org itself could not be fetched at all in round 9a — the fetch needed a permission that was not granted, which is different from a server refusal and worth re-testing in a session where it can be granted. That is the only thing standing between the map and 7 AfDB cases.

Which routes work, as established by rounds 8 and 9a:
- **The World Bank documents API is the highest-yield route found so far.** `https://search.worldbank.org/api/v3/wds?format=json&qterm=...&fl=docdt,display_title,pdfurl,docty` returns conformed loan agreements and appraisal reports; then fetch the PDF on **documents1**.worldbank.org, because documents.worldbank.org itself refuses. Put the document type in `qterm` — `docty` as a filter parameter returns nothing. This opened appraisals back to 1964.
- **ADB is the next most productive.** Its document paths fetch directly: `https://www.adb.org/sites/default/files/project-documents/<proj>/<proj>-rrp-en.pdf`. The Recommendation of the President reports carry full covenant summaries; some older ones (Samut Prakarn 1995) are un-OCR'd scans.
- **AidData's Chinese official finance records** often carry the collateral, escrow and repayment terms of Chinese state loans. For Serbian loans the Ministry of Finance publishes ratifying laws with the whole agreement attached (mfin.gov.rs), where the parliamentary site refuses.
- **Loan and facility agreements filed as exhibits on sec.gov/Archives**, bond prospectuses, and arbitration awards and court filings, which quote the agreement, are the routes that work for private lenders.
- **IFC serves normally — this was wrong in three earlier handoffs and cost three rounds.** `disclosures.ifc.org/project-detail/SPI/<id>/<slug>`, and the `/ESRS/` and `/ERS/` paths, all fetch in full once a WebSearch has surfaced the URL. SPI pages carry amounts, dates, use of proceeds and category, and for financial-intermediary investments an explicit list beginning "the bank will be required to"; ESRS and ERS pages carry the action-plan items. Records go back to about 1994 as stubs; 1988 investments such as Escondida have no page. `disclosuresservice.ifc.org/api/File/downloadfile` does refuse, which is the path EWS links IFC annex files from.
- **`ewsdata.rightsindevelopment.org`** — note `ewsdata`, not `ews` — mirrors ADB, AIIB, World Bank, AfDB and IDB files as PDFs at `/files/documents/<nn>/<BANK>-<id>.pdf`. This is how round 9a got the ADB Report and Recommendation of the President for Amaravati.
- **`idbinvest.org` is fully open**, project pages and `environmental-and-social-review-*.pdf` files alike. Use it for IDB Invest private-sector cases instead of `iadb.org`, which returns client errors, and `mici.iadb.org`, which refuses.
- **IFAD is the best remaining multilateral route.** `members.ifad.org` (and `webapps.ifad.org`, which it redirects to) serves Executive Board President's Reports in full, with complete conditions-precedent and covenant schedules, plus its evaluation reports.
- **`eib.org`** project summary sheets and public-register PDFs both fetch. `cao-ombudsman.org`, `fmo.nl`, `imf.org`, `accountabilitycounsel.org`, `info.undp.org`, `arabfund.org/blog/projects/…` and `banktrack.org` all serve. `statewatch.org/media` and `data.privacyinternational.org` serve released EU action documents, which do carry conditionality.
- **afdb.org is not uniformly refusing**, and the blanket block recorded against seven AfDB cases is too strong: `afdb.org/en/documents/document/<slug>` paths fetch and read normally. A later round should search AfDB appraisal reports under that path by project title — EWS records for other AfDB projects list "Project Appraisal Report (EN)" among their bank documents. The Accountability Console also links AfDB Independent Review Mechanism case PDFs on `aconsole-static.s3.amazonaws.com`, which is untested: both attempts failed on a lapsed permission, not on the host.
- **EBRD** blocks automated fetching, as with afdb.org a fetch-permission block rather than a server error. A mirror for EBRD project summaries would unlock Vares, Shah Deniz and IPP4.
- **The Accountability Console** serves complaint records without login but carries **no financing terms**. It is good for confirming project ids and disbursement dates, and for establishing whether a lender's own mechanism treats an operator as a sub-client — which is how two intermediary cases survived round 9a's check.
Before accepting any new entry, check it against the five failures now written into `docs/CONDR.md`.

**Failure #4 — a term from a different loan — is now the one that costs most.** It took out 11 of round 9a's 33 entries. All 11 put the condition on a bank or fund the lender financed rather than on the project that caused the harm, and seven rested on a single IFC facility to ICICI Bank (project 25492). The requirement there is real but hedged ("commit to formalize, **if required**, the SEMS"), the use of proceeds was the bank's own capital "especially in key areas such as rural banking and microfinance", and the only basis for tying it to Mundra, Mahan or NTPC was that the IFC does not disclose end use. A facility size matching across two cases is not evidence of a link — the ZAR 1 billion in both Nedbank cases is just the one facility quoted twice.
Only four intermediary entries survived, and each had a documented step from the intermediary to the project: Siguiri, where the CAO registered the complaint under IFC project 26014 and calls the mine operator a sub-client; Rio Salá, where the fund bought 51% of the dam owner's majority holder; and the two HAGL cases, once re-anchored from project 10740 onto 20926, the fund the CAO complaint is actually against. Agua Zarca went out because the CAO states the fund stopped considering it and "can find no other link between the DESA project and the IFC".
Round 8's checkers also caught an invented effectiveness condition at Chixoy and, at Plan Colombia, spraying tests quoted from the FY2003 appropriations act under the FY2002 act the card cites. Round 9a found Amaravati resting on a World Bank loan that was never approved — India withdrew in July 2019 — so its requirements bound no one.

**Entries that record what a loan did NOT require are worth having and need the strictest check.** Kainji's covenant list (para. 92 a-h) carries an 8% return on net fixed assets and a 1.5x debt-service test but nothing on resettling the roughly 140,000 displaced; the 1990 Jakarta water appraisal has no privatisation condition; Transmigration III has no covenant on existing residents' land claims. Each was let through only after the checker could see the whole covenant schedule. Taunsa's was softened for the opposite reason: its section 2.03(a) binds Punjab to General Conditions on land acquisition that the agreement does not reproduce, so "no resettlement covenant" could not be said.

**Ordinary commercial terms are not conditions.** Round 8 deliberately left untyped the pricing, fees, tenor and debt-to-equity ratios at Hambantota and Hongsa, the share pledges and completion guarantee at Obi, a bank's own lending policy, and an issuer's green-bond rule.

**Nor is a financing plan.** Round 10a's Upper Atbara entry rested on "The Government of Sudan will cover the remaining cost of the project and any additional cost that may arise" from Arab Fund loan 557. It was blanked: the sentence sits in the financing plan and says who pays the rest, with no covenant language, no condition precedent and no remedy. A counterpart-funding line is not a term the money depended on.

**Which phase or loan paid for the harm decides everything.** Round 10a's Kalangala entry had to be rewritten once the checker established that the Bugala Island estate was built under phase one — a US$20m IFAD loan of April 1997 whose evaluation names no covenant — while the documented covenants belong to the April 2010 second phase and restrain new planting on Buvuma and the outlying islands, not on Bugala. The same trap caught Interagua, where the only document with terms is a 2016/2018 IDB Invest loan against harm in 2001-2011. Check the phase before writing the entry.

### 3. Whole-picture text — complete, 7 blanks left on purpose
Round h11 cleared all 14 retryable blanks. The 7 remaining were judged to have no credible information (Morelos, Batang, Java 7, Pacitan, Tanjung Kasam, Cilacap, IPP4 Al-Manakher). Nothing is queued.

The round worked because it went to primary documents instead of news: the World Bank documents API gave the Mali Office du Niger completion report (6,209 ha developed, 247,720 beneficiaries, 11.7% economic return against 34% at appraisal, rated Moderately Unsatisfactory), and ADB's evaluation path gave the Multan validation PVR-293. **A documents.worldbank.org URL opens if you swap the host to documents1 and the `/pdf/` segment to `/text/`**; the text versions are easier to query than the PDFs.

Its checker corrected 13 of the 14 and is worth reading for the shape of the faults (`rounds/r26f_whole_h11_check_log.md`). The worst was a **manufactured disagreement**: the figure of 216 for Cobrac at Santo Amaro is a 1983 lead-poisoning study's sample, not a headcount, so setting it against a 2024 research project's 2,500 compared a sample with a workforce. Also removed: an Arab Bank settlement claim absent from both cited sources, two unreconciled 33% figures at Tayan Nuur where the sourced export share is about 15% in 2013, and a Vila Carioca date the council minutes do not carry. Several facts were quoted in prose with the source never listed — the checker had to find and open them to keep them.

### 4. People — 127 of 173 lack a checked `total`
Round 2 (`rounds/r26f_people_totals_2_checked.json`, input `docs/r26_people_in2.json`, checker log alongside) researched 155 and wrote 28, taking the page from 18 to 46. Brief `docs/PEOPLE.md`; merge with `merge_people_total.py`. Note `merge.py` does not handle people — these live in `window.ENT.people`.
**125 of the 155 are deliberately empty and should not be re-queued.** A minister who signed one deal, a site manager, a guard commander or a named victim has no countable output; each note records what was opened and what it lacked. Private groups that publish nothing (Renco, Privinvest, BSGR) are in that group.
**The World Bank projects API answers agents** — the old note that it refuses was wrong, the second such error found in one day. `https://search.worldbank.org/api/v2/projects?format=json&rows=0&strdate=…&enddate=…` returns `{"total":"N"}` and the dates filter on board approval date. But **the count is not IBRD/IDA approvals**: it also includes recipient-executed trust-fund activities, guarantees, GEF, carbon offset, Montreal Protocol, special financing and debt-reduction operations — 13% of Kim's 1,848 and 6% of Georgieva's, near zero for Black, Clausen and Conable — so any sentence using it must break the figure down. IFC and MIGA are absent, and additional financings count as separate rows.
**Six people listed in earlier handoffs as needing a year filled — Lagarde, Lipton, Wolfensohn, Zoellick, McNamara, Woods — already carry finished totals** in `rounds/r26f_people_totals.json` and were never in round 2's input. If a year is still missing in one of those sentences, fix it in that earlier file.
Two entries were blanked on judgement and are worth revisiting only if the owner disagrees: Summers and Stiglitz. Both approval counts reproduce, but a bank-wide figure hung on a chief economist's post states a scale neither had lending authority over, and the map's criticism of Summers is a memo rather than a project.
One left empty with the figure sitting in its note, for the owner to decide: Riah Phiyega. The SAPS Annual Report 2012/13 gives 197,946 personnel and 1,132 police stations as at 31 March 2013 — Marikana's year and her first as National Commissioner. Filling it is a one-line change; it was left out because she commanded a police service rather than overseeing projects.

### 5. Buyers — 34 of 946 cases
Only where a source documents who bought the output. This is a long tail and will never reach 100%.

### 6. Lender offices
IDB, AfDB and BII directories blocked; IMF per-country pages not read; IFC and China Development Bank lists not reachable.

### 7. New cases
Leads in `docs/backlog.json`. Thin regions: Middle East and North Africa, Europe and Central Asia. Not researched: Payra, Mattala, Kyaukphyu. Waiting on events: Bishoftu airport, Kerio Valley, Thar Block-1, Nam Ngiep 1, Kaliwa dam.

## Tool limits

- WebSearch is capped at about 200 calls per turn, shared by every agent in that turn. Run at most two or three research agents per turn, or they run out partway (this happened on 7 Nov).
- WebFetch now refuses URLs that have not appeared in a WebSearch result in the session ("provenance"), so case source links often can't be opened directly; each new source costs a search. SEC EDGAR full-text hits work well for listed firms.
- WebFetch has an hourly limit shared across agents, and some company sites refuse fetches; checkers then blank the facts, which can be re-checked later.
- Hosts that refuse automated fetches, found the hard way: ebrd.com, afdb.org, iadb.org, mici.iadb.org, documents.worldbank.org (but documents1 works), disclosuresservice.ifc.org download paths, otvoreniparlament.rs, jica.go.jp project pages (its evaluation PDFs do open), peoplepower21.org, mneguidelines.oecd.org, miningnews.net, theedgemalaysia.com, businesslive.co.za, athexgroup.gr, Reuters, The Guardian, and sec.gov's cgi-bin EDGAR search. These work: disclosures.ifc.org (SPI, ESRS and ERS paths), idbinvest.org, ewsdata.rightsindevelopment.org, eib.org, miga.org, cao-ombudsman.org, fmo.nl, imf.org, banktrack.org, the World Bank WDS API and documents1.worldbank.org, adb.org document paths, sec.gov/Archives, Companies House, HKEXnews, cninfo, govinfo, the Accountability Console, and most PDF annual reports.
- **Check a "blocked host" claim before trusting it; two of this list's entries were wrong for weeks.** `disclosures.ifc.org` and `idbinvest.org` were both recorded here as refusing and both serve normally — that error alone kept 29 IFC cases blank across three rounds. A spot-check of ten blanks separately found four naming a host-wide refusal where none exists: recommon.org, buzzfeednews.com and kathmandupost.com all serve, and kfw.de and banktrack.org refuse only particular files. Record the exact failure, not a general one, and re-test an inherited block before building a round around it.
- A fetch that fails because a permission was not granted is **not** a server refusal, and the two should not be recorded the same way. afdb.org and ebrd.com failed that way in round 9a; afdb.org has since been read successfully under its `/en/documents/document/` paths.
- **The operative provenance rule:** a URL surfaced by WebSearch fetches without a prompt, but a URL surfaced only inside an earlier WebFetch result needs a permission grant — and once one grant lapses in a session, every later one is refused without being sent. An agent that hits that should say so rather than record the host as blocked, and the work should move to URLs a search can surface.
- Direct `curl` from the shell is blocked by the agent proxy, and WebFetch needs a URL it has already seen in a search result or an earlier fetch; guessing a path on an already-seen host fails.
- A blocked lender site is not evidence that no condition existed. Record it as blocked so a later round knows to try a mirror.

## The completeness panel

`completeHTML()` in `base.html` computes the "How complete this map is" section of the About panel from the page data at build time: cases and countries, and the share of cases with whole-picture text, with a statement of what the money came with, with settled lender terms, plus company descriptions, people records and documented buyers. It is injected into `window.ABOUT_HTML` at the `<!--COMPLETENESS-->` marker. Add a row there when a new kind of information starts being filled in; never write these figures in by hand.