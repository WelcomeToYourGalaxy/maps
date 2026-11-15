# Independent check — whole-picture paragraphs, batch whole_1 (19 cases)

Checker did not write these paragraphs. Every figure was traced to the cached
World Bank document (ICR, ICRR, PPAR) under `cache/<PID>/`, or, for the two web
sources and the São Paulo recovery, to a page opened in this pass. Table figures
were read from the printed block, not from a grep hit.

## Ruling applied to `self_reported`

The brief's ruling governs: `self_reported` stays **true** where every figure
comes from the lender, the borrower, the implementing agency, the operator, or
the lender's own evaluation office (IEG: ICRR and PPAR all count as the lender's
own). It turns **false** only where a figure comes from someone outside the
project.

Re-tested on all 19:

| id | writer | checked | reason |
|---|---|---|---|
| morupule-b-family-moved-fatal-accidents | false | **false** (kept) | Statistics Botswana is the national statistics office — outside the project. Figures verified on the Q3 2017 brief (see below). |
| ceara-sanear-ii-resettlement | true | **false** (changed) | The writer's restraint was **over-cautious**. The paragraph carries a figure from Instituto Trata Brasil drawn from the federal SNIS 2020 data. Under the ruling what matters is who the figure comes from, not whether it checks the project's own counts. Trata Brasil and SNIS are outside the project, so the flag turns false. The paragraph still says in terms that the project's delivery figures are the Bank's and the state's own and that no independent check of them was found. |
| pinheiros-station-collapse-sao-paulo | true | **true** (kept, but basis changed) | The writer's basis — the Bank's 2024 feature page plus the operator ViaQuatro's ridership figures in the Brazilian press — was all lender-or-operator material, so true was right. The paragraph is now rewritten from the recovered completion report and IEG review; still all lender and implementing agency, so true. |
| other 16 | true | **true** | Every figure is from the ICR, the ICRR or the PPAR, i.e. the lender and its evaluation office. No change. |

Net: one record changed — `ceara-sanear-ii-resettlement` from true to false.
Final tally: **17 true, 2 false** (ceará and morupule). The writer had 18 true,
1 false.

## São Paulo Metro Line 4 — recovery of the completion report: SUCCEEDED

The writer reported SITE_BLOCKED on pdf and client_error on txt from
documents.worldbank.org, nothing cached, and rested the paragraph on the Bank's
2024 feature page plus operator figures in the press.

Route that worked, exactly as the brief suggested:

1. `GET https://search.worldbank.org/api/v3/wds?format=json&projectid=P051696&rows=50&fl=docna,docty,pdfurl,txturl,docdt,projn,repnb,guid` — 25 records, repeatable.
2. Took the `txturl` for ICR1735 (2012-06-01) and ICRR14009 (2013-04-23) and rewrote the host to `documents1.worldbank.org`:
   - `https://documents1.worldbank.org/curated/en/547441468228275910/text/ICR17350P051690C0disclosed070200120.txt` — HTTP 200, 162,199 bytes.
   - `https://documents1.worldbank.org/curated/en/692971474577575098/text/000020051-20140625200029.txt` — HTTP 200, 46,960 bytes.

The sibling checker's report is confirmed: the API holds two records for this
conformed agreement under P051696 and documents1 served both files. Saved to
`/home/claude/work/sp33/`.

The paragraph was rewritten from those two documents. The URLs stored in
`sources_add` are the API's own `txturl` values path-for-path (documents host,
not the documents1 rewrite used only to fetch). Both web sources the writer had
used were dropped: the 2024 feature page's "US$434 million" is Phases 1 and 2
combined (the ICR shows US$304.0 million for Phase 1 and a separate US$130
million loan approved in 2010 for Phase 2), and its "11.3 km with 11 stations"
does not match the ICR, which gives 12.8 km with 11 stations for the full line
and six stations for Phase 1. The press ridership figure is gone because the
completion report carries a dated one.

Figures now in the card, with their source lines:
- Cost and financing: Annex 1 (a) "Total Project Cost 933,90 ... 1.776,26" and (b) "IBRD 209,00 / Aditivos 95,00; JBIC 209,00 / 95,13; State of São Paulo 308,40 / 922,03; Private Sector – PPP Concession 207,50 / 246,10".
- "The Phase 1 portion of Line 4 was moving over 600,000 passengers per day after 6 months in operation" (ICR); "According to the TTL, the daily ridership is currently approaching 700,000 (as of October 2012)" (ICRR) — attributed to the Bank's own task team, as the ICRR does.
- "six of 11 stations planned for Phase 1 began operations gradually between May 25, 2010 and September 15, 2011"; "The integration of municipal and inter-municipal bus lines was achieved in all six stations of Phase 1."
- Results framework achieved column: metro share 16% → 19.3% (revised target 17.5%); generalised cost Vila Sonia–Luz 104 → 73 minutes (revised target 82).
- "the revised Net Present Value (NPV) of benefits is US$364million and an Economic Internal Rate of Return (EIRR) is estimated to be13.8% as compared with an NPV of US$554million and EIRR of 17.7 percent at appraisal" (ICRR).

Nothing about the collapse or the deaths is in the paragraph; the card's
`community` and `outcome` already carry them.

## Paragraphs cut

None. No paragraph was blanked.

## Corrections, with the sentence that decided each

### bajkaj-landfill-land-taken-before-payment
1. **US$15.8 million → US$14.7 million disbursed.** 15.8 appears nowhere in either document. ICRR: "At closure, the IDA contribution was US$14.7 million". ICR financing table: "International Development Association (IDA) 17.50 14.7 84".
2. **"25,000 tonnes of waste a year" → "25,000 cubic metres of waste a year".** The ICR's own economic annex: "The total design capacity of the landfill is 365,000 m3 and with an annual receiving capacity of 25,000 m3", and its assumptions table "Landfill capacity (m3/year) 25,000 / Lifetime capacity (m3) 365,000". The ICRR says "25000 tons waste annually" — an unreconciled units conflict between the two documents, resolved in favour of the completion report, which also prints a conversion ("Weight of solid waste per cubic meter (kg/m3) 712") that makes tonnes and cubic metres plainly different.
3. Wording: "nine road or square rehabilitations" → "nine village road or square schemes", per the ICR's "Nine subprojects for rehabilitation of village roads/squares and five subprojects for small water supply systems"; "Board" → "Executive Directors", the document's own term, with the date 1 November 2007.

### shkodra-lezha-school-sites-land-cleared
No corrections. All checked and held: US$15 million each from IDA, CEB and EIB with US$30 million from the government ("The project utilized a pooled funding mechanism with each of the partners financing US$ 15.0 million and the government financing US$ 30.0 million"); US$65.9 million spent, "88 percent of the appraisal estimate of US$75.0 million" (the ICR's own table says 89% — a one-point conflict inside the Bank's own papers, left as the ICRR's 88 because that is who the figure is credited to); "22 basic and secondary schools (comprising 518 classrooms ... ) were built or rehabilitated (target was 30 schools)"; "6 new basic schools were constructed", "4 new secondary schools were constructed"; Components 3 and 4 at "159 percent" and Component 2 at "14 percent"; "the project's schools were substantially more expensive and (based on CEB comments and field visits with beneficiary schools) of poor quality"; "Teachers who participate in continuous professional development (%) ... None / 70% / 12%".

### rn34-colonia-santa-rosa-canteen-eviction
1. **"a programme costing about US$1,353 million" cut.** No document gives that total. It is US$400m + US$952.7m added up by the writer — arithmetic the documents do not do. Replaced with the two figures the documents give: the loan fully disbursed at US$400 million and the ICR's financing table "Borrower 935.10 952.70 101.88".
2. **"6 of 15 accident black spots had reached bidding without any works being built" → "of 15 accident black spots 6 had reached bidding and 3 were built".** The "no works built" clause is contradicted by the ICR: "of the 31 black spots initially identified (but later reduced to 15 interventions), only 3 were executed", and its output table "• Restore 15 black spots; • 3 Black spots restored".
3. **"one of two planned road safety corridors" → "one of the planned road safety corridors".** The ICRR says two originally planned, the ICR says four reduced to one at restructuring; the number is not settled, the one-ready-but-untendered fact is.
4. Roughness target stated as "below 3.5" rather than "3.5", following the ICR text ("keep the average IRI below 3.5"). The results-framework row gives a different pairing (target "less than 3.8", actual 3.08) — noted, not used, because the writer's pairing is the one the narrative states.

### balakhani-landfill-families-and-waste-pickers
1. **"132 informal dumps covering 199 hectares were closed" wrongly credited to the project.** PPAR: "40 dump sites were closed under the World Bank project (143 hectares), and 92 were closed by the government (56 hectares)". The paragraph now says 132 closed over the project period, of which the project closed 40 covering 143 hectares.
2. **US$54.3 million → US$54.28 million.** ICRR: "Balakhani landfill rehabilitation and management. Appraisal estimate US$12.64 million. AF US$48.14 million. Actual cost US$54.28 million."
3. **Added the damaging clause that sits beside the favourable ones**, as the standing test requires: PPAR, "An estimated 50 percent of the collected waste is dumped informally and fails to reach the authorized treatment and disposal facilities."
4. "A rate of return of 20 per cent was calculated only at closing, none having been done at appraisal" tightened to "no economic analysis having been done at appraisal", the PPAR's own wording: "There was no economic analysis at appraisal or for the additional financing project." (The PPAR separately says "No financial analysis was conducted at appraisal or closure" — a different thing; the paragraph does not conflate them.)
5. Dropped the bins/landfill clause "132 informal dumps ... against a revised target of 50" from the Bank-count sentence and moved the dump count into the IEG sentence where the 40/92 split is.

Unreconciled, left out of the card and recorded here:
- **Capacity units.** ICR body: "a sanitary landfill designed for 20 years with 9.7 million cubic meters of additional capacity"; ICR indicator table: "Industrial and municipal waste disposal capacity created under the project (tons) ... 9,700,000"; ICRR and PPAR: "9.7 million tons". Tonnes kept, as three of four statements say tonnes.
- **The government disputes the dump count.** PPAR appendix, comments of the Ministry of Economy: "Different parts of the Report mention the closure of 132 informal dump sites under the Project. However, in reality, 41 informal dump sites were closed". Not used; it is a borrower comment on an evaluation, and the 40/92 split in the PPAR's own text already corrects the attribution.
- Satisfaction: 68 per cent against a revised 70 per cent target confirmed ("Sixty-eight percent of the population expressed satisfaction ... slightly short of the revised target of 70 percent").

### burundi-fibre-backbone-unpaid-compensation
No corrections. All held against the ICRR: "Revised Commitment 226,587,108.68 ... Actual 222,396,166.92"; "Eight operators had access to the landing station at closure. This exceeded the revised target of six"; "34 localities (communes) had access to broadband at project closure. This exceeded the revised target of 20"; "Price of a whole international E1 capacity link reduced to US$300 a month"; "Mobile phone charges dropped from 320 fbu/mn at the baseline to 60 at closure"; "Resale price for Internet Access (monthly price for 256 kb connection) fell from US$2,500 at the baseline to US$300"; "3,061,706 people representing 50% of the population benefited ... This exceeded the revised target of 3,003,000."

**Contradiction confirmed as the writer reported it:** the same review gives the fibre as "1,245 kilometers (km) Fiber Optic Network were built as per the revised target" in the Burundi outputs list and "contributed to the construction of 1,254 kilometers (Km) of fiber optic cable" in the other outputs list. Both figures are on the card, which is the right handling.

### takon-landfill-land-taken-porto-novo
1. **"all of it IDA credit" is wrong.** ICRR: "Total actual cost was US$76.17 million consisting of US$36.86 million from the original credit and US$37.40 million from the Additional Financing and US$ 1.9 million in counterpart financing." The paragraph now gives the three parts. (The ICRR's own data sheet row "Loan/Credit (US$M): 35.00 76.17" contradicts its narrative; the narrative is used.)
2. **"double the US$37.6 million estimated at appraisal" → the two figures side by side.** "Double" is a characterisation the documents do not make, and 76.17/37.60 is not exactly double.
3. **"11 classrooms" cut.** Three incompatible accounts in the Bank's own papers: ICRR "11 new classrooms"; ICR main text "nine three-class and two two-class modules" (eleven modules, thirty-one rooms); ICR annex "23 classrooms (12 promised in PP)". Nothing is safe to state, so the classroom figure is out. Latrines restated as "21 latrine blocks" per the ICR's "21 four-block latrines".
4. "56 per cent for the project as a whole excluding roads" **verified, not cut** — ICRR: "The ERR and MERR for the project as a whole (minus the roads component) are estimated to be 56% and 40% respectively (ICR, p. 42)". Marked here because it looked at first like a figure read out of a neighbouring table (an unrelated "56 percent" sits in the municipal-revenue indicator row); printing the block settled it.
5. The perceptions point broadened to match the source: the ICRR says the benefits of components B, C **and** D came from a perceptions survey and "it is unclear how these perceptions were quantified", not that the completion report is silent on method for the waste component alone.
6. Added the ICR's target for roads ("against a target of 32.18 km promised in the PAD") so the output figure is not read as unqualified.

### tema-ouagadougou-bamako-corridor-compensation
1. **Country split reversed: 103 km is Ghana and 154 km is Mali, not the other way round.** The writer followed the ICRR's outputs bullet ("including 54 km in Burkina Faso, 103 km in Mali and 154 in Ghana"), but the same review's component description says "Rehabilitation of 54 kilometers (Km) of roads in Burkina Faso, 103 km in Ghana and 154 km in Mali", and the PPAR names the roads: "103 km of the Buipe-Tamale road in Ghana; 54 km of the Ouagadougou–Sakoinsé road in Burkina Faso; and two roads in Mali: 154 km of the Bamako-Bougouni road and 45 km of the Sikasso-Heremakono road." The review's bullet is the outlier.
2. **Added the later deterioration beside the travel-time gain**, as the standing test requires: PPAR, "The IEG mission found that transit time from Tema to Ouagadougou has increased to more than seven days ... because two bridges in the Ghana part of the corridor are being rehabilitated".
3. **Rest stops corrected to the PPAR's later finding**: "the IEG mission found that these rest stops have not been completed. In Mali, the one rest stop constructed was also not operational." The writer's "rest stops in Burkina Faso and Ghana were not operating at closing" came from the ICRR and was attributed to the PPAR's December 2017 visit; the attribution is now right and the Mali finding is included.
4. Attribution fixed: the PPAR visited Burkina Faso and Ghana only — "IEG visited Burkina Faso and Ghana in December 2017. No mission was conducted in Mali owing to security concerns."
5. Checkpoints verified: "In Mali, the number of fixed customs checkpoints increased from four at project start-up to six at project closure (compared to the target of just one)."

Unreconciled, recorded: the ICRR says 311 km rehabilitated "as targeted"; the PPAR says "about 356 km of road, which is about 19 percent of the Tema-Ouagadougou-Bamako Corridor" and lists 356 km of roads (103+54+154+45). The 311 km is kept because it is the figure credited to the completion report; the 45 km Sikasso-Heremakono road accounts for the gap.

### dangriga-market-vendors-income-loss
1. **"a project costing US$15.73 million" was the appraisal estimate.** ICRR: "At appraisal, the total project cost was US$15.73 million; actual cost was also US$15.62 million." Both figures now given, actual first.
2. **Revenue dating corrected.** The writer had "from about US$11.4 million in 2012 to about US$16.9 million a year in 2013-15"; the ICR says "from approximately US$ 11.4 million (average for fiscal years 2009/2010, 2010/2011, and 2011/2012) to US$ 16.9 million (average for fiscal years 2012/2013, 2013/2014, and 2014/2015)". The ICRR's loose "in FY12" is the source of the error.
3. **Rate of return scoped.** The 51.3 per cent is for the capacity-building component over five years, not the project: "the ICR estimated that the net present value (NPV) for the next five years would be US$4.79 million, the benefit/cost ration would be 1.51, and the internal rate of return (IRR) would be 51.3%".
4. "circumstantial" verified and re-rendered closer to the source: ICRR, "Despite only circumstantial evidence to support claims regarding the achievements of sub-objective 2 as a consequence of the project-financed training".
5. Dangriga outputs read from the printed output block, not grep: "Dangriga Streets and Drains rehabilitated 865 meters 1165 meters ... Market Rehabilitated and Extension constructed 7,900 sq. ft. 7,900 sq. ft."

### el-alto-avenue-land-paid-for-afterwards
1. **"5,010 households were connected to new sewers" is the baseline, not the achievement.** The ICR's results row reads "Number of houses with new sanitary Number of houses 5,010 6,045 5,548", i.e. baseline 5,010, target 6,045, actual 5,548. The ICRR converted the baseline into the output ("5,010 households connected to new sanitary networks, not reaching the target of 6,045") and the writer followed. Corrected to 5,548 against a target of 6,045 from a baseline of 5,010. This is the baseline-read-as-achieved trap in its plainest form.
2. "more than 13 km" → 13.44 km, the value in the achieved column ("Roads constructed, non-rural Kilometers 6.70 10.11 11.16 13.44 - El Alto").
3. Verified unchanged: "the cancellation of US$4,040,000 of Component 2 of the project and the contract of US$3,400,000 that was declared as misprocurement in the same component"; "two different methodologies for estimation of property value were used at appraisal and at closure"; 197,073 direct beneficiaries, which the ICR places in the El Alto component (the ICRR mislabels them as La Paz); travel time 60 → 43 minutes against a target of 42; 110,409 people against a target of 151,078; 18,937 metres of sidewalk border against 12,978.

### ceara-sanear-ii-resettlement
1. `self_reported` **true → false** (see ruling above).
2. "water losses held below the 27 per cent target" → "water losses at 26.03 per cent against a 27 per cent target", the achieved value in the ICR's indicator row ("Water losses ... 29.7% 28.2% 27% 26.03%").
3. Instituto Trata Brasil fact sheet opened and verified: "60,1% tinham acesso ao sistema de rede de água", "29,4% habitavam em residências com sistema de rede de coleta de esgoto", "com base nos dados de 2020". The paragraph states the publisher and the data year.
4. Verified unchanged: US$238.75 million disbursed of US$240 million; "Urban water connections grew from 51,300 in 2007 to 315,800 in 2011. Sewer connections rose from 22,400 to 139,800 over the same period"; "The state's current fiscal balance increased from R$1,296 million in 2007 to R$1,882 million in 2011"; "second-grade literacy rate, increased from 56.0 to 81.4 percent of students tested from 2009 to 2011"; "the ONA indicator was not met. The amount of the loan linked to this performance metric ($1,077,620) was cancelled."

### santos-vila-gilda-stilt-house-resettlement
**The writer's self-report was wrong on the point it flagged.** It said it had used the review's text figures over its data sheet "and that the two disagree" — but the paragraph as delivered gave US$22.77m and US$21.23m with no mention of any disagreement. All three figures exist and are now set out in the card:
- ICRR text: "Actual IBRD loan disbursement was US$22.77 million and the undisbursed balance at closing of US$21.23 million was cancelled with the notification date on August 5, 2016 according to the World Bank Client Connection website."
- ICRR data sheet: "Original Commitment 44,000,000.00 ... Actual 24,123,717.34".
- ICR Annex 1 (b): "International Bank for 44.00 23.42 53% Reconstruction and Development".
A third figure the writer did not report. The paragraph now names all three and says they disagree, rather than picking a side.

Other corrections:
1. **"two of 28 planned landslide works" kept but the review's own warning about it is recorded here**, since there is no room for it on a four-sentence card: ICRR, "Two landslide prevention works were completed, among the 28 originally planned interventions. There is some discrepancy in the ICR regarding the number of works completed. The ICR on page 21 refers to two, but on page 33 to only one." **Contradiction confirmed.**
2. Attribution fixed: the engineering-design cause is the review's, not the completion report's — ICRR, "By project closing, less than 10 percent of the planned drainage system construction works were completed. This was mainly due to poor engineering designs, procurement issues and implementation problems."
3. "2,950 families were moved out of flood-prone areas" softened to "recorded as moved", because the ICR's own indicator row gives a different number and a different unit: "50% reduction in percent of Santos families living in flood-prone areas ... 90,000 45,000 2,960 ... 2,960 inhabitants were relocated from flood prone areas equivalent to around 3%." The ICRR's 2,950 families is kept as the credited figure. Unreconciled.
4. Verified unchanged: appraisal US$88 million, actual US$62.37 million; 800 of 2,400 households, 712 resettled and 88 improved; survey 95% Caneleira IV, 94% Pelé Village II, 64% Quadras 1 and 35; "An ex-post economic analysis used the same methodology at project appraisal ... showed losses of BRL 92.7 million with a negative ERR and benefit cost ratio of 0.16", against 20.8 per cent at appraisal.

### thimphu-land-pooling-compensation-arrears
1. **The connection figures were given only in their favourable framing.** The ICRR says "732 households were provided with new piped water connections, exceeding the target of 600" and "510 households were provided with new sewerage connections. This represented 85% of the target of 600." The completion report's own annex tables say otherwise: "Table 2: Water Connection Targets and Results ... Total 0 850 732 86.1" and "Table 3: Sewerage Connection Targets and Results ... Total 0 950 510 53.6", with the body text "there were a combined 510 completed sewerage connections (54 percent of the target)". The card now gives 732 and 510 with the annex percentages (86 and 54 per cent). **Unreconciled inside the Bank's own papers; the shortfall framing is used because the annex sets out the per-plan arithmetic and the results-framework row does not.**
2. US$24.8 million → US$24.7 million disbursed, the ICRR's figure ("The amount disbursed US$24.7 million"); the ICR says "very close to $24.77 million". Unreconciled to the last decimal; the review's figure used.
3. "20.40 km of internal roads, 10.39 km of roadside drains" marked "as targeted", which is what the review says, so they are not read as overachievements.
4. Verified unchanged: 624 plots against a target of 300; 14.58 km footpaths against 10.98 km; 20.30 km water pipeline against a revised 20.70 km; 13.75 km sewer against 13.05 km; 364 permits at 85 per cent of 430; "Property taxes collected in Thimphu municipality increased to over 250 million Bhutanese Ngultrum (BTM), as compared to the target of 200 million BTM between 2011 and 2017"; November 2019 survey, 87 per cent and 92 per cent.

**Taba contradiction confirmed, and nothing from it reached the card.** ICRR: "The estimated ex post EIRR for Taba LAP, was 25% as compared to the ex ante EIRR of 12%, The ex post EIRR for Taba was considerably lower than the ex ante EIRR, due to the slower than forecast uptake of water and sewer connections." 25 is higher than 12, so the sentence contradicts itself; the ICR's own text gives "an ERR of 25 percent" for Taba with no comparison. Correctly left out.

### morupule-b-family-moved-fatal-accidents
1. **"a project costing US$1,662 million" was the appraisal estimate.** ICRR: "Appraisal estimates of the total project cost was US$ 1,662.3 million including contingencies, taxes, duties and IDC. Actual/latest estimates of the total project cost was US$ 1,298.98 million". The card now gives the actual against the estimate. This is the commonest trap on this map and it was live here.
2. **"a Bank commitment of US$136.4 million cut to US$66.1 million" restated as a loan of US$136.4 million of which US$66.1 million was used.** The ICR financing table gives "International Bank for 136.40 66.1 48 Reconstruction and Development" and the ICR text "The IBRD loan closed with substantial, undisbursed savings of USD 70.3 million out of an original financing amount of USD 136.4 million". The ICR data sheet separately reports "Disbursed Amount: USD 68.88M (IBRD)" — unreconciled, so the paragraph no longer asserts a revised commitment.
3. "US$30 a tonne" → "US$30 a ton", the document's unit: "When the cost of carbon (US$ 30 per ton of carbon) was included, the EIRR declined to 5.1 percent."
4. Statistics Botswana Q3 2017 brief opened and verified exactly: locally generated 87.8 per cent, 893,831 MWh of 1,018,442 MWh distributed, imports 124,612 MWh; Q3 2016, 66.5 per cent, 661,245 MWh, imports 333,355 MWh. All four figures and both percentages hold.
5. Verified unchanged: 600 MW ("construction of a 600 MW (4x150 MW) coal-fired power station"); "fully taken over by BPC on May 4, 2014, albeit with significant defects"; capacity factor about 80 per cent expected and about 4,200 GWh, running "closer to 50 percent ... due to forced outages"; revenue grant 455 → 1,488 million pula, US$40m → US$132m; "In FY2014, the subsidies reached 66 percent of BPC revenues"; "the average tariff was covering only about 63 percent of the costs"; "from Pula119 million in FY2009 to Pula 6,331 million in FY2014".

Unreconciled, recorded: the appraisal rate of return. ICRR: "The ex-ante EIRR was 14.1 percent in the PAD", data sheet "Appraisal 14.10 ... ICR Estimate 10.50". ICR: "the EIRR is nearly halved relative to the appraisal case (10.5 percent versus 19.6 percent)". The card keeps the review's 14.1 per cent, credited to the review; the completion report's 19.6 per cent is not used.

### chunhu-fenghua-access-road-demolition
1. **Wrong document cited.** The writer's completion-report URL is in the manifest under P106956 but the Bank's own record titles it "Dominican Republic - Social Protection Investment Project", and the file at it opens "IMPLEMENTATION COMPLETION AND RESULTS REPORT ... TO THE DOMINICAN REPUBLIC FOR A SOCIAL PROTECTION INVESTMENT PROJECT". The Ningbo completion report is the other ICR under the same P-number (id 26901074), at `.../773421477925988125/pdf/ICR-Main-Document-10272016.pdf`. The source has been replaced. The URL is not constructed — it is the manifest's `pdfurl` path-for-path. The figures themselves all came from the right file, so no figure moved because of this.
2. **"a project costing US$157.09 million" was the appraisal estimate.** ICR: "Total Financing Required 157.09 170.33 108%" and "The actual project investments (US$170.33m) exceeded the planned investment (US$157.09m) by 8.4%". Corrected.
3. **"14.5 km of distribution network" does not exist.** The only "14.5" in the completion report is a date in a training-session table: "14.5 Sub-PMOs NRWTPMO Responsible person ... Lectures 10000". The output table's actual column reads "15km of water supply transmission mains ... together with a booster pump station and a 13km-long water distribution network". Corrected to 13 km. (The ICR's narrative elsewhere gives 15.8 km and 12.9 km — unreconciled; the output table is used because the writer's 15 km came from it too.) **This is the grep-a-table error the brief warns about, found again.**
4. **The wastewater plant was presented at design capacity as though achieved, with the damaging clause missing.** ICR: "The WWTP was built with a capacity of 10,000 m³/day, but was treating a volume of 6,000 m³/day at project close due to the lower-than-anticipated capacity from the Hongsheng Haitang ne[w zone]", and "as secondary and tertiary collection networks had not been constructed at the time that the WWTP was completed, the plant lay idle for over a year". Both are now in the same sentence as the design figure. The favourable counterpart — "84% of Chunhu wastewater being treated at closing" against a 70 per cent target — is added beside them.
5. Verified unchanged: Chunhu component US$103.36m against US$78.49m; "a 6.2km-long, four-lane road"; "the distance from Chunhu Town to the center of Fenghua City has been shortened from 24km to 14.2km ... Travel time was shortened from 40 minutes to 15 minutes"; 13,933 car equivalents against 13,000; "a wastewater collection network 19km in length"; 76,500 residents in 25,500 households; 144 villages against 150 and 45,500 households against 41,000. "13,933" restated as car-equivalent vehicles a day, the document's unit.

### ertanggou-reservoir-tuyamar-village-inundation
1. **"a project costing US$204.08 million" was the appraisal estimate.** ICRR: "The project was estimated to cost US$204.8 million. Actual cost was US$207.85 million", and the ICR table "Total Financing Required 204.07 207.85 102%". Corrected to US$207.85 million actual against US$204.07 million at appraisal. (The data-sheet "Total Project Cost (USD) 204,080,000.00" is the appraisal number; the writer took it as the cost.)
2. **"groundwater overdraft in the project irrigation areas fell from 874 million cubic metres to 17.38 million" is wrong.** 17.38 is the *reduction*, not a remaining level. ICR results row: "Groundwater overdraft reduced in project irrigation areas and the basin as a whole ... Project Area: 0 3.75 million m3 / Basin: 0 37.4 million m3 ... 17.38 million m3 ... 169 million m3", and the ICR text "the total actual reduction in overdraft was 17.38 million cubic meters, as compared to the target reduction value of 3.75 million cubic meters". The 874 figure appears only in the ICRR's garbled sentence ("reduced in project irrigation areas from 874 million cubic meters in 2009 to 17.38 million cubic meters") and nowhere in the completion report. Rewritten as reductions against targets, and 874 dropped.
3. "Meiyaogou" left without a capacity, as the writer had it. **The Meiyaogou contradiction is confirmed:** the same completion report gives "Meiyaogou with a capacity of 8 million cubic meters" in the component description and "Meiyaogou (with storage capacity of 9.8 millionm3)" in its resettlement summary. Nothing from it reached the card. Alagou's figure is also given twice (46 and 45.7 million m³), so "46 million cubic metres" was dropped from the card as well.
4. Verified unchanged: 260,000 people with flood protection, target achieved; "Economic losses from flooding decreased from RMB15.48 million in 2009 to zero in 2017" (the ICR's Table 3-1 gives the baseline as 15.96 million RMB and the text "some 16 million RMB" — unreconciled, the results-framework value kept); 43 water user associations; 21,021 members trained against 2,650; "the project has increased farmers' income by 16-20%".

Unreconciled, recorded: the appraisal rate of return. ICRR data sheet "Appraisal 21.00 ... ICR Estimate 29.00"; ICR text "higher than the estimate at project appraisal of 20 percent". The card keeps 29 against 21.

### lutusi-liancheng-heritage-resettlement
1. **"eight sites" → "nine sites", twice.** ICR: "The project was comprised of two components covering nine project sites"; "Table 4. Project Direct Economic and Financial Impacts at the Nine Project Sites".
2. **Lutusi revenue start year wrong: 1.4 million → 0.8 million yuan.** The ICR's per-site revenue table reads "Lutusi 0.8 1.0 1.2 1.4 1.8 2.1 2.5" for 2008–2014 in million RMB. 1.4 is the 2011 value. The 1.4-million figure the writer used belongs to a different site: "revenue from direct visitor expenditure increased from RMB 1.4 million in 2008 to RMB 15.8 million in 2014" is Qingcheng Ancient Town.
3. **"a car park built with government counterpart funds" dropped.** The same completion report says both things: output table, "the car park was completed with counterpart funds"; safeguards section, "The location selection for seven households in Lutusi was not accepted by all the households and eventually resulted in the project abandoning the planned land acquisition and the site's car park." **Contradiction confirmed**; neither version is stated.
4. Disbursement given precisely: ICR data sheet "Original Total US$ 38.40M ... Disbursed Amount: US$ 35.02M"; the ICRR notes the completion report elsewhere said US$37.79 million — unreconciled, so the data-sheet pair is used.
5. Nine-site totals restated in the document's own units: "revenue directly generated from the visitors more than quadrupled from RMB 1.22 billion to RMB 4.79 billion" (the per-site table's "Total 1,220.3 ... 4,792.6" million RMB agrees). The writer's "1,220 million to 4,793 million yuan" was supportable but mixed units with the billions the text uses.
6. Verified unchanged: Lutusi visitors 10 → 29 (thousands) per the per-site table, so 10,000 in 2008 to 29,000 in 2014, and Lutusi is the smallest of the nine by visitors; "a 418 m² tourist service center and web-based tourism information system"; "Completed stabilization of 4,596 m² of ground surface"; "442 m fencing around Lutusi"; "(b) 85 m² public toilet, a garbage transfer station, and wastewater treatment plant ... was dropped due to shortage of funds"; sanitation table "LTSC4 Lutusi WWTP 300m3/day 300m3/day Yes". **The dropped-versus-operating contradiction the writer reported is confirmed and both are on the card, which is the right handling.**

### shihutang-dam-ganjiang-relocation
No corrections. Every figure held, including the ones that looked like appraisal-column reads:
- Cost: "The total project cost was US$344.05 million at closure, about 8% higher than the the appraisal estimate of US$319 million".
- "a powerhouse with the capacity of 120 MW and average annual power generation of 527 million KWH" — kept as a design figure, which is how the card words it.
- Flood protection actual column: "43 kilometers of dikes, (ii) 45 kilometers of diversion canals, (iii) 8 sets of pumping stations with total capacity of 5,980kW" (the appraisal design was 56 km of canals and about six pumping stations, so these are achieved values, not targets).
- "4,389ha of crop fields were protected against 10-year flood, as planned"; "The navigable time per year or 1,000-ton vessels on the 38km upgraded channel increased from 27% to 95%, as targeted".
- "284 GWh of hydropower was generated at project closure, which was 60% of the target of 472GWh in 2013"; cause: "delays in generator installation and operation caused by unexpected floods".
- "The volume of cargo passing the Shihutang ship lock during low water season between October and December was 9,000 tons, less than 1% of the target of 1.03 million tons ... due to the development of Xiajiang ship lock 90 km downstream".
- "EIRR ... 12.9% at project closure as compared with 14.9% at appraisal"; "it shortened travel distance between Wanhe Town and Taihe County by about 12 kilometers, directly benefiting about 50,000 pedestrians and vehicle users". (The appraisal document had expected 150,000 people for the same road; the card uses the reported 50,000.)

### abidjan-lagos-corridor-road-works-deaths-and-late-compensation
1. **The border-time gain was given without the reversal that both documents attach to it.** ICR: "the border crossing time from Elubo to Noé was reduced by 48.6 percent (14 hours) from a baseline value of 37 hours ... In contrast, it is worth to note the low performance of 47 hours for Noé-Elubo crossing direction one year after the proj[ect]". ICRR: "this outcome was significantly undermined and the border crossing time reverted to 47 hours one year after ... Rating Modest". The 47-hour figure is now in the same sentence.
2. **"20 per cent against 17 per cent at appraisal" mislabelled.** The 17 per cent is a recalculated appraisal baseline, not the appraisal figure: "The revised appraisal baseline resulted in an NPV of US$32.43 million at 12 percent discount rate and an internal rate of return (EIRR) of 17 percent, which is slightly higher when compared to the results from the economic analysis at appraisal", against the closure case (a) "EIRR of 20.06 percent". Reworded.
3. Verified unchanged: "The actual amount disbursed was US$80.4 million" of a US$90.0 million IDA grant; "113.59 km of non-rural roads on the corridor were rehabilitated at project closure, slightly short of the target of 130.3 km" (87 per cent); "The market at Elubo was rehabilitated but was not yet functional when the project closed"; "92% of the roads of the corridor in Cote d'Ivoire were reported to be in good or fair condition at project closure in March 2019, as compared to 71% at the baseline in September 2012"; "the journey time from Abidjan to Noé has dropped to two hours compared to up to 5 hours in 2012"; "four checkpoints along the 170 km from Noe to Abidjan in 2018"; "53 million people ... exceeded the target of 50 million. 33% of the beneficiaries were women (This was short of the target of 55%)".

Unreconciled, recorded: the ICR's borrower annex gives "a total length of 118.75 km was rehabilitated on the Côte d'Ivoire side against 130 km expected" against the results framework's 113.59 km. The results-framework value is kept.

## Routes that failed

- **Ceará state comptroller's audit of the water company's 2012 accounts.** The writer reported it as blocked by robots. Not retried in this pass; it would be the one genuinely independent check of the project's own water and sewer connection counts, and its absence is why the card still says no independent check of those counts was found.
- **No other route failed.** All 18 non-São Paulo records were checked entirely against documents already on disk; the two web sources opened on the first attempt; the São Paulo documents were recovered on the first attempt by the API-plus-documents1 route.

## Figures left unreconciled (summary)

| case | the two accounts |
|---|---|
| bajkaj | landfill intake 25,000 m³/yr (ICR) vs 25,000 tons/yr (ICRR) |
| shkodra | project cost 88 per cent of appraisal (ICRR) vs 89 per cent (ICR table) |
| balakhani | capacity 9.7 million m³ (ICR body) vs 9.7 million tons (ICR table, ICRR, PPAR); dumps closed 132 (all Bank docs) vs 41 (government's comment in the PPAR) |
| burundi | fibre 1,245 km vs 1,254 km, same review |
| takon | classrooms 11 (ICRR) vs 11 modules of 31 rooms (ICR text) vs 23 (ICR annex); credit total US$76.17m all-credit (ICRR data sheet) vs 36.86+37.40+1.9 (ICRR narrative) |
| tema | 311 km (ICRR) vs 356 km (PPAR); 103/154 km country split reversed between the ICRR's two sections; Mali rest stops two built as targeted (ICRR) vs one built and not operating (PPAR) |
| santos | IBRD used US$22.77m vs US$24.12m vs US$23.42m; landslide works two vs one in the same ICR; flood-area relocations 2,950 families vs 2,960 inhabitants |
| thimphu | water target 600 (ICRR, results row) vs 850 (ICR annex); sewer target 600 (ICRR) vs 950 (ICR annex and text); disbursed US$24.7m vs US$24.77m; Taba EIRR 25 per cent called "considerably lower" than 12 per cent |
| morupule | appraisal EIRR 14.1 per cent (ICRR) vs 19.6 per cent (ICR); IBRD used US$66.1m (ICR table) vs US$68.88m (ICR data sheet) |
| chunhu | distribution network 13 km (output table) vs 12.9 km (narrative); transmission main 15 km vs 15.8 km |
| ertanggou | Meiyaogou 8 vs 9.8 million m³; Alagou 46 vs 45.7 million m³; flood-loss baseline 15.48 vs 15.96 million RMB; appraisal ERR 21 vs 20 per cent |
| lutusi | Lutusi car park built with counterpart funds vs abandoned, same ICR; disbursed US$35.02m vs US$37.79m |
| abidjan | 113.59 km (results framework) vs 118.75 km (borrower annex) |

## Mechanical checks

- Output has the same 19 ids and the same four keys per id as the input.
- Every Bank URL in `sources_add` matches a `pdfurl` or `txturl` in `harvest_manifest.json` path-for-path, except the two São Paulo URLs, which are the `txturl` values returned by the wds API query recorded above and reproducible from it.
- Voice grep on every `whole` for "I ", "we ", "our ", "my ", "this pass", "read here", "searches", "this card", on word boundaries: no hits.
- Every paragraph is four sentences.
- Each paragraph checked against the input's `community` and `outcome`: no paragraph repeats the harm already on its card.
- No Wikipedia source anywhere in the batch; no fact rests on a search snippet.
