# Round 17 check log — batch E (Vietnam, 11 ICIJ leads)

Kept 6 cases, corrected all 6, cut none. Kept all 5 drops, corrected 5 drop reasons.

Every document below was fetched independently with `curl` from `documents1.worldbank.org`
and read from disk with `pdftotext -layout`. Document lists came from
`https://search.worldbank.org/api/v3/wds?format=json&projectid=<P-number>`.

---

## The round's central finding: ICIJ's 773,838 for P074688

Documents opened and read in full as text: Project Appraisal Document 21 Oct 2004
(`29860.pdf`, 5,988 lines), Integrated Safeguards Data Sheet 24 May 2004 (`30303.pdf`, 366
lines), 2009 additional-financing project paper (`480390PJPR...`, 1,088 lines), ICR 13 Dec
2014 (`ICR31940P074680...`, 2,877 lines), IEG ICR Review 12 May 2015 (`ICRR14722-P074688...`,
535 lines). Also the resettlement-plan volume headed "Project Affected Persons"
(`RP2420v250...`, 1,231 lines) and three further provincial resettlement plans
(`RP2420vol01`, `RP2420vol02`, `rp242`).

**Confirmed.**

- The string `773,838` and the digits `773` appear in none of the six documents. Confirmed by
  grep over all converted text.
- ISDS, all three quotations exact and in one paragraph (lines 186–204): "The Project will not
  involve any major resettlement but will entail land acquisition and resettlement impacts due
  to construction of new lines and substations"; "In the first phase of project 131,955
  households will be affected by the Project. The number of DPs is high because of the DPs are
  scattered along the lines"; "Impacts on houses will be mostly partial and generally will not
  require the relocation of families outside their residential plots". Also "Most of impacts on
  land will be temporary."
- PAD Annex 13, Table 1, "Number of DPs to be affected in six project provinces - Phase l(a)":
  column headed "Number of Families Losing >10% of Productive Land Holding", total **178**;
  permanent land acquisition **299,746 m²**; temporary **14,256,140 m²**. All three confirmed.
- Distribution Efficiency Project ICR 14 June 2019, line 1469: "The PCs were able to minimize
  physical relocation (only five households were relocated out of 12,880 Project Affected
  Households) by the construction/execution of 169 subprojects". Exact.
- ICIJ method page (icij.org, "Data dive", Cecile S. Gallego, 22 April 2015): search terms
  "affected", "PAP" or "displaced" confirmed; "it is necessary to look for the average number
  of family members by household, which can be found in the socio-economic survey" confirmed;
  "this distinction is not made in all documents, we decided to include all impacts" confirmed.

**Corrected — two parts of the writer's version did not hold.**

1. **The absence claim was too wide.** The project's document file holds **91 items**, more than
   20 of them provincial resettlement action plans — exactly where phase-by-phase
   affected-person counts live. Five core documents plus four resettlement plans were read; the
   rest were not. The drop reason now states the scope of the absence claim explicitly.

2. **The arithmetic explanation is wrong, and had to be removed.** 773,838 ÷ 131,955 = 5.8644,
   so "5.86" is correct arithmetic. But the inference that this is households × average
   household size is **contradicted by the project's own documents**: the four provincial
   resettlement plans read report average family sizes of **4.4, 4.93, 4.3 and 4.59 persons**.
   Applied to 131,955 households those give 567,000–651,000, not 773,838. No document read
   anywhere states 5.86, or any household size near it. The 131,955 is also first-phase only
   while the project ran in about 25 provinces, so the figure may be a sum across phases.
   The drop reason now prints the ratio and the documented household sizes side by side and
   states that the documents do not say how ICIJ arrived at the figure. A tidy explanation of
   the gap would have been a claim without a source.

**Also corrected:** the 178 now carries what it counts — families losing more than 10 percent
of productive land holding, in the six Phase 1(a) provinces only, all 178 of them in Vinh Phuc
and none in the other five — and the table's own note that the numbers could differ from the
detailed measurement survey carried out later.

**Verdict: the finding holds in its core and must be stated without the arithmetic.** ICIJ's
773,838 is not a count of people moved: the Bank's appraisal, safeguards sheet, completion
report and IEG review record minor, mostly temporary right-of-way impacts, no count of anyone
physically relocated, and 178 families losing more than a tenth of their productive land in the
six first-phase provinces. The corroborating case is stronger than the headline one, because
the Distribution Efficiency ICR states the relocation count directly: five households of
12,880, against ICIJ's 31,581.

---

## Lead 12 — Water Resources Assistance (P065898), drop confirmed

Read in full: IEG Project Performance Assessment Report 20 Aug 2019 (field-mission based) and
IEG ICR Review 9 Dec 2013. PPAR §3.7 exact: "In all, 5,974 households were negatively affected;
of these 167 households were classified as 'severely affected' with loses of more than 20
percent of their land. Sixty-five households required resettlement." The 69 Tay and Nung
households at Cau Son-Cam Son confirmed. Safeguards compliance "adequate" confirmed.

**Corrected:** the writer called 11,000 "the appraisal estimate". The ICR Review's own words are
"reduce the number of affected households from the initial 11,000 to about 6,000, although the
ICR does not evaluate the adequacy of the compensation". The drop reason now uses that wording
and says ICIJ's 53,600 is "of the same order as" the initial estimate rather than matching it.

---

## Cases

### 1. `vinh-loc-b-resettlement-hcmc` (lead 11) — kept, `documented`, bucket (a)

Opened: ICR P070197 (3,352 lines) and IEG ICR Review 2016 (675 lines), both in full;
VietNamNet 26 June 2024; VnExpress 6 June 2024.

Bank figures all confirmed. ICR Table 3 and Table A9.3: partially affected 16,569 expected /
18,959 actual; relocation 4,859 expected / 2,917 actual. Compensation and resettlement cost
US$188.5m against US$111.3m. ICR Table A9.1: Vinh Loc B, Binh Chanh district, 30.6 ha, 529
plots, 1,939 apartments. 571 complaints, 568 resolved, three in Nam Dinh outstanding. Credit
IDA-38870 SDR 148.8m / US$222.5m, effectiveness 06/10/2004, AF Cr. 4604 US$160m September 2009,
closing 31 Dec 2012 moved to 31 Dec 2014. AFD US$37.5m withdrawal in 2005 confirmed. COD 811
mg/l in 2009 to 80–130 mg/l in 2015, and over 90,000 m³ of dredged material, confirmed.
IEG: "resettlement and compensation to households suffered severe delays" and "Delays in
counterpart funds for land acquisition and compensation payments led to resettlement taking
more time than anticipated" — both exact.

**Corrections.**

- **Tran Thi Hong was displaced by a different project.** VietNamNet says her family gave up
  land for the **Tham Luong–Ben Cat–Nuoc Len canal improvement project**. The card said only
  "a canal project" while sitting inside an account of the Bank-financed Tan Hoa–Lo Gom canal,
  which reads as though the loan moved her. Now named, and flagged as a different scheme. Tran
  Huu Son, by contrast, is confirmed as a Tan Hoa–Lo Gom household (VnExpress: handed over land
  in 2012 for "the Tan Hoa - Lo Gom canal sanitation project"), and his detail is what makes
  this case independently documented.
- **"Her apartment was roomier" is not in the page** and was cut. VietNamNet says she received
  a 50 m² apartment; that is now what the card says.
- **The vacancy "disagreement" is not one.** 1,500 of 2,000 (VietNamNet) and 80 percent of 1,900
  (VnExpress) are the same magnitude, one thing at two precisions. The writer's note presented
  it as a conflict. Rewritten: the genuine difference is the apartment count, where three
  sources give three numbers (ICR 1,939, VietNamNet 2,000, VnExpress 1,900), all now printed
  with who says what and none reconciled. The vacancy figures are printed and explicitly not
  called a disagreement.
- **The two distance figures measure different things** and the `point` field was blending them
  into "about 12 to 20 km". Rewritten: 20 km is VietNamNet's distance from the city's central
  area, 12 km is VnExpress's distance between one resident's former home and the apartment he
  was offered. Neither is now given as the project's distance.
- "substantial delays" → the ICR's own word, "significant".
- VnExpress's date is 6 June 2024, not 26 June (that is VietNamNet's). Both dates now on the card.
- 2,547 clarified: the ICR says 2,641 plots and 2,383 apartments were built and "only 2,547
  plots and apartments were utilized for resettlement within the Project".
- Vinh Loc B's area is given as 30.6 ha in ICR Table A9.1 and 30.0 ha in Table A2.2. The card
  now attributes the 30.6 to the resettlement-areas table rather than stating it flat.
- `displaced: 2917` added (the Bank's own outcome figure), per the rule that ICIJ's number never
  occupies that field.

`documented` is correct: the harm rests on the Bank's documents **and** on two Vietnamese
outlets with named residents, one of them displaced by the financed work.

### 2. `vietnam-urban-water-wastewater-below-replacement` (lead 28) — kept, `contested`, bucket (a)

Opened: ICR P119077 (3,540 lines) in full. The quotation is exact, §114:
"local authorities often applied government policies where gaps were identified in compensation
plans, including assistance to households that lost 30 percent of agricultural land, and
**compensation for structures on agricultural land from 50 percent to 80 percent of its
replacement value**" ... "such issues were addressed in most subprojects, **except in Thai Hoa
and Ninh Binh subprojects where the status has not been affirmed officially to the World Bank**."
Both named subprojects confirmed and both are in the project's town list (Thai Hoa, Nghe An;
Ninh Binh, Ninh Binh). §113 figures confirmed: 3,081 affected, 45 relocated, 455 losing more
than 20 percent of agricultural land, 2,581 marginally affected. Appraisal 870,583 m², 556
households, 9 relocated — confirmed. Loan: IDA-49480 US$200m, approval 24 May 2011,
effectiveness 7 Oct 2011, closing 31 Dec 2019, AF 26 May 2016 (IBRD-86210 US$69m, IDA-58170
US$50m), disbursed US$266,452,160 of a US$299,552,160 project.

**Corrections.** Ninh Binh to Thai Hoa is about **120 km**, not 170 (great-circle from the
card's own coordinates). The key sentences are now quoted in the report's words rather than
paraphrased, since the wording is the finding. Added the additional-financing land take the
card omitted: 69,732 m², permanently affecting 57 households, three firms and five
organisations. Added that Di An joined with the 2016 additional financing. `displaced: 3081`
added.

This is the strongest documented failure in the batch after lead 11: compensation below
replacement cost, in the lender's own words, with two subprojects named as unresolved.

### 3. `haiphong-bac-son-nam-hai-road` (lead 32) — kept, `contested`, bucket (a)

Opened: ICR P111548 (2,923 lines) in full. §55 and §70 confirm 3,037 project-affected
households in 13 communes/wards, 909 to be relocated, and "the relocation process into
resettlement sites would **affect** an additional 871 households (4,223 persons)". §56 confirms
"the Haiphong Government's financial constraints in providing counterpart funding and delayed
hand-over of the accessible sites to the contractors"; the nearly eight-month delay; the
2016–2020 Medium-Term Investment Plan shortfall; "By November 2018 ... there were 69 outstanding
cases of resettlement activities (or nearly 6% of the 3,037 total resettlement cases)"; and
"the completion of Component 1 accumulated nearly 3.5 years in delays, of which more than 80% is
attributable to delays in resolving the aforemention 6% of the remaining resettlement cases."
§71 confirms 109 cases resolved by October 2019 (3.5 percent), three outstanding then, one at
closure, resolved as of 1 October 2020. Road opening 3 May 2020. Loan details confirmed:
IDA-49000 US$175m, approval 29 Mar 2011, effectiveness 28 Jul 2011, original closing 31 Dec
2016, actual 29 Feb 2020, disbursed US$152,529,765, borrower US$101.61m, total US$254.1m.

**Corrections.**

- **"nine of the project's 20 progress reports" is wrong.** The ICR lists **19** ISRs and rates
  implementation progress moderately unsatisfactory in **six** of them (nos. 08, 09, 10, 11, 14,
  15). Corrected.
- **The ICR's own person-count was missing.** §70 gives the 3,037 households as **12,605
  persons**. Added, and used for `displaced`, since it is the Bank's own figure for this project
  and keeps ICIJ's 16,828 out of that field.
- The 871 households are recorded as **affected by** the acquisition for the resettlement sites.
  The report does not say how many were moved. The card now says so, because "871 households
  displaced to make room for other people's resettlement" would be more than the document
  supports — and that is the one sentence on this card most likely to be quoted.
- "about 6 percent" → "nearly 6 percent" as printed.

### 4. `mekong-delta-transport-unpaid-compensation` (lead 15) — kept, `contested`, bucket (a)

Opened: ICR P083588 (3,621 lines) in full. §40 confirms the two first-phase plans (7,245 and
2,840 displaced persons) and "an increase from 15,000 to 22,663 in the number of affected
households (an increase of over 30 percent) on 518.43ha land, although the majority of those
affected were only marginally affected (loss of trees, garden fences and similar)". §41 exact:
"In the initial years, there were a small number of instances identified where affected persons
were not compensated in accordance with the approved safeguards measures"; about 110 households
under component B at the closing date "due to compensation rate issue"; "Up to date 30 HHs still
remain for whom compensation is planned to complete by end March 2017". §32 confirms "The need
for an unforeseen increase of US$52M in counterpart funds was flagged in late 2015 to cover
additional resettlement costs", the contractors' blocked site access, and the provinces
advancing their own budgets. Annex component subtotals confirmed: A 3,638, B 7,620, C 11,405,
grand total 22,663 on 5,184,270 m². Loan details confirmed (IDA-4306 SDR 137.20m / US$207.7m;
raised to SDR 238.5m / US$363.7m; US$7.42m cancelled; AusAID TF-91332 and TF-13700, AU$47.4m).

**Corrections.**

- **The province list was short by three.** The annex names Ben Tre, Vinh Long and Hau Giang as
  well, so it is **13 provinces and Ho Chi Minh City**, not 11. Corrected in `place`, `point`,
  `community` and `lvwhy`. Dropping three provinces from a list the source publishes is an
  editorial choice the owner did not make.
- The implementing agency, the **Ministry of Transport**, is now named, because lead 36's case
  sits in overlapping provinces and years.

### 5. `quy-nhon-coastal-cities-sanitation-resettlement` (lead 34) — kept, `contested`, **bucket (b)**

Opened: ICR P082295/P122940/P090374 (2,747 lines) in full. §49 confirms "around 189.4 ha of land
in all three cities, with 1,247 affected HHs, of which 223 HHs had to be resettled", VND 233bn
(US$11.1m) paid, VND 3bn (US$0.14m) "transferred to the state treasury accounts for 11 HHs in
Quy Nhon City". §50 confirms 223 against 245 in the approved RAPs and 259 land plots on five
sites, one built by the project in Quy Nhon, and the Nha Trang site that the city replaced with
existing sites. §41 confirms the 2014 complaints from the 11 households and the March 2015 last
report, with the plan endorsed by the Binh Dinh PPC. Ten RAPs confirmed (§48). Loan details
confirmed: IDA-42530 and IDA-48850 US$190,245,588, disbursed US$185,533,996; PHRD TF056325
US$4,616,400, disbursed US$4,270,780; GEF TF094335, approval 23 Jun 2009, closing 31 Dec 2014;
approval 19 Dec 2006, effectiveness 15 Jun 2007, closing 30 Nov 2014.

**Verdict on the writer's bucket (b) call: agreed, this is bucket (b), and it is the weaker of
its two weakest entries.** The resettlement is documented as having happened (223 households,
189.4 ha, 1,247 affected). The only candidate failure is 11 households out of 223 whose
compensation was still being settled, and the report records the plan as endorsed and the money
as transferred. There is no documented shortfall, no length of delay, no outcome, and the record
stops in March 2015. It claims no failure the documents do not support, and it says plainly what
is missing, so it meets the standard for a (b) card — but if the owner decides this map does not
want (b) cases, this is the first one to go.

**Corrections.**

- **Distances were both wrong.** From the card's own Quy Nhon coordinates: Nha Trang is about
  **170 km** south, not 300; Dong Hoi about **500 km** north, not 700.
- **"rather than paid to them directly" was an inference and is cut.** The ICR says the approved
  budget "has been transferred to the state treasury accounts for the mentioned HHs" and says
  nothing about whether the households took the money. The card now states the report's words
  and that it does not say.
- The confidence note said the report "does not say what the 11 households complained about".
  It does say the complaints were "related to their compensation and resettlement"; what it does
  not say is what they asked for. Corrected.

**On the overlap with `nha-trang-ngoc-hiep`: geographic only, not the same episode.** Checked
against `cases.json`. The existing case is the **Coastal Cities Sustainable Environment
Project**, an IBRD US$46m plus IDA US$190.2m loan approved 5 May 2017, Ngoc Hiep ward in Nha
Trang, with an Inspection Panel case running to 2026. Lead 34 is the **Coastal Cities
Environmental Sanitation Project**, approved 19 December 2006 and closed 30 November 2014, and
its harm is in Quy Nhon. Different loan, different P-numbers, different decade, different city;
the two points are 166 km apart, outside the 50 km test. Both cards now carry an explicit
sentence distinguishing them, because the project names are nearly identical and a reader would
otherwise take them for one thing.

### 6. `mekong-delta-water-management-compensation-delays` (lead 36) — kept, `contested`, **bucket (a), the thinnest in the batch**

Opened: ICR P113949 (2,658 lines) and IEG ICR Review 2018, both in full; plus the appraisal
document for the province list. §76 confirms 5,435 households affected, 215 relocated, 304
losing part of their agricultural land, 70 rebuilding on remaining land; the four listed causes
including "the delay of the payment of resettlement compensations due to lack of counterpart
funding"; 260 grievances with 250 solved by the provincial units; and that at completion all
grievances and outstanding issues were solved. Replacement-cost and monitoring statements
confirmed. 14 bridges in Bac Lieu confirmed (48 in Soc Trang). Loan details confirmed:
IDA-49510 US$160m, approval 7 Jun 2011, effectiveness 7 Oct 2011, original closing 31 Mar 2017,
actual 15 Sep 2017, disbursed US$134,289,842, borrower US$45,091,000 of US$46.6m.

**Verdict: this is bucket (a), not (b), but only just.** Late payment of compensation is on the
brief's own list of documented failures, and the Bank states it as fact and as a cause of delay.
What is missing is everything that would make it specific: no length of delay, no count of the
households affected by it, no account of what the 260 grievances asked for, and everything
recorded as settled. The writer named it as one of its two weakest entries and that is right.

**Corrections.**

- **All seven provinces are now named.** The completion report says "seven provinces" and names
  only six. The appraisal document names the target area: An Giang, Ca Mau, Hau Giang, Soc
  Trang, Bac Lieu and Kien Giang, plus the municipality of Can Tho, "hereafter the term 'seven
  provinces'". **Kien Giang** was the missing one. The card now names all seven and says which
  document names them.
- The implementing ministry, **Agriculture and Rural Development**, is now named.

**On whether leads 15 and 36 are one episode: genuinely separate.** Different loans (IDA-4306
and IDA-5200, approved 22 May 2007, versus IDA-49510, approved 7 June 2011), different
P-numbers (P083588 versus P113949), different implementing ministries (Transport versus
Agriculture and Rural Development), different works (roads, highways and inland waterways
versus irrigation, salinity control, rural water supply and bridges). They do overlap in
provinces — An Giang, Bac Lieu, Soc Trang, Kien Giang, Can Tho appear in both — and in years,
and their points are 86 km apart, inside the 50 km test's spirit. So each card now names its
loan, its loan number, its ministry and the other case, so the two cannot be read as one.

---

## Lead 6 — Rural Distribution (P099211): drop upheld, with a view

Opened: ICR 24 Dec 2013 (3,428 lines) in full. Both quotations are exact, in **Annex 7, the
summary of the borrower's own completion report**, written by **Central Power Corporation
(formerly Power Company No. 3)**: "The conduct of compensation and resettlement was difficult,
complicated and long-lasted. Compensation unit price in provinces was low as compared with
average price of the market, interfering significantly in compensation declaration to local
residents. Simultaneously, some problems arose such as people did not accept compensation,
obstructed construction and made long solving time." The Bank's own §: "caused modest land
acquisition for the individual project affected household"; "The land acquisition and
compensation activities by Implementation Agencies satisfactorily complied with OP 4.12";
"disagreements by affected households with proposed compensation rates".

**Corrected:** the writer called this "a 13-province distribution network". It is not. The ICR
describes about **15 provinces in the north (PC1), 19 in the south (PC2), 11 in the central
region (PC3)** plus Hai Phong and Hai Duong — about 45 provinces. The CPC passage is the
account of the company that ran the central-region component, so it covers about 11 provinces
and no narrower place than that.

**View on whether it carries a card: no, and the reason is not timidity.** A borrower admitting
below-market compensation and obstruction of construction is real evidence, and it is better
evidence than a Bank self-assessment because the implementing company had no reason to say it.
But a card on this map fixes a point on the earth and makes a claim about identified people. The
passage gives no province, no commune, no household count, no date, and no outcome for anyone.
Placing a point anywhere in those 11 provinces would be the checker's choice, not the document's,
and the figure field would be empty. It is a drop whose quotation belongs in the round's notes
on what these documents do and do not record — which is where it now sits, in full and with its
author named — and not on the map.

---

## Buckets after checking

- **(a) documented failure:** 11 (Vinh Loc B), 28 (urban water, below replacement cost),
  32 (Haiphong), 15 (Mekong Delta transport), 36 (Mekong Delta water — thinnest (a) in the batch).
- **(b) large resettlement, no documented failure:** 34 (Quy Nhon).

## Dedupe

All six checked against `cases.json` by iso3, coordinates, project name and years. Seven existing
VNM cases. Nearest existing case to each new point, by great-circle distance:

- lead 11 → `vedan-thi-vai-river`, 56 km (a 1994–2011 Taiwanese factory discharge case in Dong Nai;
  different mechanism, different decade, no lender)
- lead 28 → `cat-linh-ha-dong-accidents`, 84 km (Hanoi metro line, Chinese lending)
- lead 32 → `cat-linh-ha-dong-accidents`, 90 km
- lead 36 → `con-son-tiger-cages-us-aid`, 117 km (1970–71, unrelated; this is the "weak overlap"
  the lead file flagged on lead 32 on the shared word "vietnam")
- lead 15 → `vedan-thi-vai-river`, 155 km
- lead 34 → `nha-trang-ngoc-hiep`, 166 km (different loan and decade, treated above)

Two points fall inside 100 km of an existing case but none is the same episode: no shared loan,
project, year range or community. No duplicates, no extends.

## Pattern worth carrying forward

Three faults recurred and all three are the same fault — a tidy sentence put where the document
has a ragged one.

1. **Reconstructed arithmetic presented as explanation.** The 773,838 ÷ 131,955 = 5.86 step is
   the round's signature finding and it does not survive contact with the project's own
   resettlement plans, which give 4.3 to 4.93 persons per household. Checkers on the remaining
   leads should test any "ICIJ multiplied households by household size" claim against the
   household size the project's own socio-economic survey reports, which is usually in the
   resettlement action plans rather than the ICR.
2. **Manufactured conflicts.** One of two reported source disagreements on lead 11 was one
   quantity at two precisions. Name the quantity and the date before calling two numbers a
   conflict.
3. **Silent narrowing of published lists.** Lead 15 lost three provinces, lead 36 lost its
   seventh, lead 32 lost the Bank's own person-count, lead 28 lost the additional financing's
   land take. None changed a conclusion; all four removed something the source published.

And one that will recur on every remaining lead: the Bank's documents say "affected by" far more
often than they say "relocated", and the difference between those two verbs is the whole finding.
Lead 32's 871 households were "affected by" the acquisition of resettlement land; the writer's
summary turned that into people displaced to make room for other people's resettlement. The
document does not say that.
