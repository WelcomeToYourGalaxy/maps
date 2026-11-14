# Round 22, batch A — 16 Chinese rows

Output: `/home/claude/r22/r26f_icij6_china.json` — 16 keyed objects, 8 cases and 8 drops.
Cache: `/home/claude/r22/cache/` (shared folder; my 57 documents, 114 paired `.pdf`/`.txt` files, listed at the end).

All 16 P-numbers were established and all 16 came back new from `dedupe_leads.py`. None was an extend.

## Did the screen hold?

Yes, partly, and the brief's two cautions both bit.

- **Four rows screened out cheaply on a quoted no-relocation sentence**: P087291 Jincheng CBM ("no house demolition"), P100968 Shanxi CBM ("No house demolition and relocation would be required" / "No demolition and relocation will be involved"), P129563 Anhui Yellow Mountain ("there was no physical relocation of affected persons", stated as an outcome), P093882 Shandong FGD ("with no new land acquisition and resettlement", plus the only subproject built being inside an existing power plant). Those four cost under an hour between them.
- **Four more were dropped but needed full research**, because no such sentence existed: P121263 (GEF grant, dropped on what the money financed), P099224 Liaoning Third (its resettlement plan *does* plan 562 persons in 179 households of house demolition, so the screen pointed the wrong way; the drop came from the completion report giving no outcome count at all), P111325 Dashiqiao (a carbon ERPA that turned out to be a subproject of P099224), P112626 Liuzhou II (whose *updated* 2015 plan carries real outcome figures, exactly where BRIEF22 said an outcome can hide — and they turned out to be non-residential structures and business premises, not dwellings).
- **Eight rows needed the full pass** and became cases.

The caution that mattered most: a no-relocation sentence in the plan is not the end, and the reverse — a plan that *does* plan relocation is not a case either. P099224 is the clean example of the second direction.

## Row by row

| Row | P-number | Outcome |
|---|---|---|
| Wuhan Urban Transport | P069852 | **case** `wuhan-middle-ring-resettlement-overrun` — 7,312 households relocated against an appraisal plan of 2,478; resettlement cost US$514m, nearly twice the appraisal estimate |
| Wenchuan Earthquake Recovery | P114107 | **case** `moba-gorge-forest-land-compensation` — 213,373.62 m² demolished, 1,081 households; Moba Gorge forest land paid at RMB650/mu against the plan's RMB1,744–3,160/mu |
| CN-Guizhou Cultural and Natural Heritage | P091950 | **case** `guizhou-heritage-sites-demolition` — 12 houses and 1 unit demolished, 12 households resettled; 65 traditional houses at Huangping Jiuzhou renovated and occupants moved out without the procedures the project's own framework required |
| Kunming Urban Rail | P117656 | **case** `kunming-line-3-jinmasi-relocation` — about 600 households relocated, buildings dismantled for cut-and-cover, relocation took over two years, resettlement 28 months late |
| CN Integrated Economic Development of Small Towns | P118597 | **case** `hunan-gansu-small-towns-demolition` — 16,681.1 m² / 82 households in Hunan, 22,085 m² / 243 households in Gansu (230 of them moved before the project began) |
| Chongqing Urban Rural Integration II-Health | P126210 | **case** `wushan-hospital-landslide-resettlement` — 31 households physically affected, 29 resettled; one resettled into a building inside a landslide zone the Evaluation Group says is not stabilised |
| Anhui Xuancheng Infrastructure for Industry Relocation | P129431 | **case** `xuancheng-industry-zone-house-demolition` — 23,747 m² / 86 households' houses demolished; one crane operator killed |
| China-PCF-CDCF Hubei Guangrun Hydropower | P094795 | **case** `zhamushui-guangrun-resettlement-postponed` — 2,185 m² demolished, 28 families relocated at Zhamushui, 15 of them left waiting until mid-June 2012 |
| CN-PCF Jincheng Coal Bed Methane | P087291 | dropped — plan says no demolition, no resettlement; ICIJ's 2,443 is the combined population of three villages, from the plan's own Table 2.2 |
| Shanxi Coal Bed Methane | P100968 | dropped — plan says no house demolition and no relocation, twice; completion report's annex records land acquisition only, compensation at or above plan rates |
| China GEF City Cluster Eco-Transport | P121263 | dropped — the grant "paid for consultant services and IT goods"; the terminals were paid for with US$27.27m of counterpart funds |
| CN-Guizhou… / Anhui Yellow Mountain | P129563 | dropped — "only 22 ha of farmland were acquired at closing and there was no physical relocation of affected persons" |
| Liaoning Third Medium Cities Infrastructure | P099224 | dropped — plan figures only; completion report gives no demolition or relocation outcome, and later plans carry none either |
| Dashiqiao Central Heating Supply | P111325 | dropped — a carbon offset ERPA, and "a subproject under Liaoning Third Medium Cities Infrastructure Project (P099224)"; no completion report exists |
| Shandong Flue Gas Desulfurization | P093882 | dropped — the two plants with resettlement plans were never built; the one built was inside an existing power plant and was then cancelled for fraud |
| Liuzhou Environment Management Phase II | P112626 | dropped — 8,134.9 m² demolished but all of it non-residential field attendance houses and five business premises; the completion report reports livelihoods fully recovered. **Figures recorded in the drop reason so the lead can reverse this if the five demolished business premises count as trading places taken.** |

## The `_local_match` work the brief flagged

- **Liuzhou II against Phase I (P081346)**: separate loans, separate P-numbers, separate instruments. Phase II is a drop, so no overlap arises.
- **Liaoning Third (P099224) against P099992 and P126611**: three separate loans run partly by the same provincial office. P099224 is a drop. The Dashiqiao row (P111325) turned out to be a *subproject of P099224*, not a separate operation — its own resettlement "plans" are both volumes of RP590, the P099224 framework. That is two of my 16 rows collapsing into one dropped project.
- **Wuhan Urban Transport (P069852) against `wuhan-nanhu-village-resettlement-delay` (P112838)**: genuinely two projects, two loans (L4727 and the 2010 second project), two periods (2004–2010 and 2010–2020). This is the round-18 shape the brief warned about — one continuing municipal road-building episode in one city under two credits — and I wrote the first as a separate case because the appraisal and outcome figures are its own. **Flagging it for the lead: if the map's convention is one point per continuing episode, this may belong as an extend to the existing Nanhu case rather than as a second Wuhan card.**
- **Chongqing II-Health (P126210) against `tongliang-road-land-lease-compensation` (P086446) and `chongqing-small-cities-qianjiang-resettlement` (P081161)**: P126210 is the project the lead's note called "a third Chongqing project" and it is my row. Different county (Wushan), different sector (health), different loan.
- **Anhui rows against `shaying-river-sanba-village-resettlement` (P118647) and `luan-huaibei-urban-transport-resettlement` (P111421)**: unrelated beyond the province. Xuancheng is a case; Yellow Mountain is a drop.
- **Guizhou (P091950) against `qufu-gupan-pond-demolition` (P120234)**: the lead was right that this is the most valuable row. It has the Qufu shape — demolition inside protected heritage sites — plus something Qufu may not have: a Bank finding at mid-term review that the occupants of 65 traditional houses at Huangping Jiuzhou were moved out during renovation without the resettlement procedures the project's own framework required to be prepared, Bank-reviewed and disclosed *before* the work began.

## What the carbon and GEF money actually was

- **P121263 (GEF, US$4.8m)**: a grant for consultancy and IT goods. The relocation of 65 urban and 54 rural households was for the Western Changsha Hub, built with counterpart funds by the Hunan Department of Transport. Dropped on the round-20/21 rule.
- **P087291 (PCF, US$10m)** and **P111325 (ERPA, US$5.6m)**: purchases of emission reductions, no works financed, no completion report in either case. Dropped.
- **P094795 (PCF/CDCF, US$4.6m)**: the exception. The carbon purchase is a 157,745-CER ERPA that bought nothing, **but the works were a fifth component of the parent IBRD loan (P068049, Loan 4666-CHA), added in July 2006 out of about US$16m of loan savings, and the amended Loan Agreement's own list of financed activities includes "Compensation, resettlement, and rehabilitation of project-affected persons (PAPs)."** The 2020 carbon completion report is the only document found that reports the Guangrun resettlement outcome; neither the parent's 2012 completion report nor the Evaluation Group's 2018 PPAR gives those figures. Written as a case against the parent loan, with the ERPA named separately as what it was.

## My two weakest entries

1. **`wuhan-middle-ring-resettlement-overrun` (P069852)** — the weakest, and it is weak in a specific way. **The Bank's completion report for this project is not disclosed.** It is absent from `wds?projectid=P069852`, absent from a quoted-phrase title search, and absent from a `docty_exact` search for ICRs mentioning Wuhan (which returns only P112838, P148294, P044829 and P003580). Every outcome figure on the card — 7,312 households, 375 ha, 1.45 million m², US$514m, US$321m — comes from ICRR13574's summary of a document that cannot be read. The appraisal plan figures (1,164 urban + 1,064 suburban households; 9,072 people in 2,478 households) *were* read in the appraisal document, so the plan-versus-outcome gap that makes the case interesting is documented at one end only. The review's favourable clauses are on the card.
2. **`wushan-hospital-landslide-resettlement` (P126210)** — the harm is one household. 29 households were resettled and the documents record all of them compensated; what makes it a case is that one of them was settled at the Heiliangzi Residential Site *inside* the landslide-affected area, in a building the June 2018 landslide had affected, and moved in in July 2020. No document records injury or loss to that household. The completion report says the building is "well within safety limits in terms of movement"; the review, three months later, says the landslide "has not been effectively stabilized and the risk of deterioration remains." If the lead judges a single household living in a monitored building to be too thin, this is the card to cut.

A third worth naming: **`hunan-gansu-small-towns-demolition`** carries no `displaced` value. The completion report gives two province figures for households affected by house demolition (82 Hunan, 243 Gansu) and prints no total, and 230 of the Gansu 243 were moved before the project began. Rather than sum figures the report does not sum, or pick one province, I left the field out and put all of it in `displaced_note`. **If the lead wants a number there, 82 (Hunan only) or 95 (Hunan plus the 13 Gansu households the project itself moved) are the two defensible values; the second is my arithmetic, not the report's.**

## Figures where two documents, or one document, disagree

1. **P091950 Guizhou, disbursement**: data sheet gives US$59,167,978 disbursed of US$60m; the financial management paragraph of the *same report* says "the loan amount of US$ 60 million was fully disbursed at loan closing." (ICR00004154, 18 Dec 2017.)
2. **P117656 Kunming, loan utilisation**: data sheet gives the commitment revised from US$300m to US$276,926,592, a US$23.07m reduction; the economic analysis of the same report says "Only US$2 million of the initial loan was not utilized during project implementation."
3. **P117656 Kunming, closing extension**: the review says 19 months (which matches the data sheet's 30 Nov 2016 → 30 Jun 2018); the report's economic analysis says 18 months.
4. **P091950 Guizhou, cause of the Huangping Jiuzhou breach**: the completion report says the renovation went ahead "without the appropriate procedures set forth in the RPF" — non-compliance with the framework. The review says "A shortcoming of the Resettlement Policy Framework was that it did not include appropriate procedures for the temporary resettlement of small scale farmers and shopkeepers" — a defect in the framework. Opposite attributions of fault. Both are on the card.
5. **P126210 Wushan, landslide stability**: completion report (29 Oct 2021) says the resettlement building is well within safety limits; review (13 Jan 2022) says the landslide has not been effectively stabilised and the risk of deterioration remains. Both on the card.
6. **P114107 Wenchuan, report date**: data sheet "ICR Date: 02/21/2017"; cover page "February 27, 2017". Card uses the cover page and names the discrepancy.
7. **P094795 Guangrun, report date**: data sheet "ICR Date: September 30, 2020"; cover page "October 14, 2020". Card uses the cover page and names the discrepancy.
8. **P091950 Guizhou, outcome rating**: the report rates the overall outcome Satisfactory on a split rating (original objective Moderately Unsatisfactory, revised Highly Satisfactory); the review rates it Moderately Satisfactory (original Moderately Unsatisfactory, revised Satisfactory). Each named with its document.
9. **P069852 Wuhan, outcome rating**: the review rates the outcome Moderately Satisfactory and prints Satisfactory in its column for the completion report's rating. Since the report is undisclosed, that Satisfactory is reported on the card as what the review says the report said, not as a rating read out of the report.

## Routes

**Worked.** The projects API with `countrycode_exact=CN&qterm=` found all 16 P-numbers on the first pass, matched on approval date. `wds?projectid=` plus host rewrite to `documents1.worldbank.org`, `curl` and `pdftotext -layout` served everything except two documents. Nominatim with Chinese-script queries (旧州镇, 沧水铺镇, 金马寺, 三金潭, 巫山县, 宣州区, 建始县, 成县) returned every point I needed; Latin-script equivalents were not tried.

**Failures, with what failed.**
1. **The P114107 Wenchuan completion report has an empty `docty` field** and is therefore invisible to `wds?projectid=P114107`, which returns 40 documents without it. A quoted-phrase `qterm` search — `qterm="Wenchuan Earthquake Recovery"` — returns it as ICR3783 with a blank document-type column. This is exactly the failure mode BRIEF21 recorded, and it worked exactly as BRIEF21 said it would. Not a host problem.
2. **The P069852 Wuhan completion report could not be found by any route tried**: `wds?projectid=P069852` (19 documents, no ICR), `qterm="Wuhan Urban Transport"` (18 documents, no ICR), `qterm=Wuhan&docty_exact=Implementation Completion and Results Report` (4 documents, all other projects), and a WebSearch. It appears genuinely undisclosed, not hidden behind a field. Said so on the card.
3. **One download failure was my own shell**, not a host: the P129563 ICR URL was truncated of its `.pdf` extension when I extracted it through `grep`. Re-fetched with the full URL and it served normally. Worth recording because it looks like a 404 from a refusing host and is not one.
4. **No host refused anything.** `documents1.worldbank.org` served 57 documents over `curl` without a single failure.

**Independent sourcing.** Two searches, per the brief: one English (Wuhan 7,312 households / Middle Ring resettlement) and one Chinese (黄平旧州 世界银行 文化自然遗产 拆迁). Neither returned anything about these projects — the English search returned only Bank documents and the ICIJ project page, the Chinese search returned unrelated heritage and resettlement coverage. **All eight cases are therefore `contested`,** and each `confidence_note` says so. That is now six tranches of Chinese cases with no source outside the Bank.

## Cache contents — 57 documents of mine, 114 files

Keyed by P-number and document type in `/home/claude/r22/cache/`:

- **P068049** ICR, ICRR, PPAR (parent of the Guangrun component — the PPAR is field-based and does *not* carry the Guangrun resettlement counts)
- **P069852** ICRR, PAD, RP2007 (no ICR — undisclosed)
- **P087291** RP
- **P091950** ICR, ICRR, PAD, RP
- **P093882** ICR, ICRR, PAD, RP_Laiwu
- **P094795** ICR, RP
- **P099224** ICR, ICRR, PAD, RP2007, RP2013, RP2014
- **P100968** ICR, ICRR, RP2008
- **P111325** ISR2014, PID2009, RP1, RP2 (the two RPs are both volumes of RP590, the P099224 framework)
- **P112626** ICR, ICRR, PAD, RP2010, **RP2015** (the updated plan with outcome figures)
- **P114107** ICR (found by title search), ICRR, PP
- **P117656** ICR, ICRR, PAD
- **P118597** ICR, ICRR, PAD
- **P121263** ICR, ICRR, PAD
- **P126210** ICR, ICRR, PAD
- **P129431** ICR, ICRR, PAD, RP2013
- **P129563** ICR, ICRR, PAD

Nothing was merged, `build.py` was not run, git was not touched.
