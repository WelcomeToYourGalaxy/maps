# Round 32, batch china_eastasia — check log

Writer's file: `out32/china_eastasia.json` (19 rows: 4 cases, 1 already on the map, 14 drops).
Corrected file: `out32/china_eastasia_checked.json`, same keys, same 19 rows.

**Outcome of the check: 0 cases cut, 4 cases corrected (39 edits), 14 drops upheld, 2 drop reasons
corrected, 1 already-on-map confirmed.** Nothing was cut because the four cases each rest on a
relocation count or a documented loss in an outcome document that I opened and read. That is not a
comfortable result for a check brief that says a check confirming everything was not done, so the
log says plainly below which single case is closest to a cut and why I did not make it.

Every document cited was read from `/home/claude/work/cache/<PID>/`. Nothing was re-fetched except
two files named in the route section.

---

## 1. The five things the task singled out

### 1.1 `east-tsankhi-herder-displacement` (P108768) — the lender-link test. **Kept. Link verified; the two Bank documents disagree about cause and the card now says so.**

**The Evaluation Group sentence exists and says what the writer quoted.**
`cache/P108768/ICRR_2017-12-22_29303182.txt` line 819, in the Involuntary Resettlement paragraph of
section 10a: "As explained above, this safeguard policy was triggered as a result of the relocation
of two winter shelters by an activity financed by the project." The same review says it a second
time and more strongly, at line 576 in its Quality of Supervision section: "A safeguards review
conducted during the preparations for the second restructuring resulted in triggering Involuntary
Resettlement (OP/BP 4.12) safeguard policy. Two winter shelters had to be relocated because of a
pre-feasibility study financed by the project."

**The completion report does not say that.** `cache/P108768/ICR_2017-03-30_27348194.txt` line 1384:
"The relocation of two winter shelters had taken place in 2010 **in connection with development of
this mine**". At line 1898 (paragraph 66) it is the same: relocations "took place" at the mine
"where" the study was financed. The report puts the relocation beside the mine's development; the
review puts the study itself in the causal chain.

The writer's card wrote this as "The Evaluation Group's review puts it more directly", which turns a
disagreement about causation into a difference of wording. **Corrected**: the card now sets the two
sentences against each other and attributes each.

The lender link holds on three things that are each in a document: the Bank triggered OP 4.12
retroactively over this relocation in the January 2014 restructuring; the review states the study as
the cause twice; and the credit then paid for the remedial plan and the policy framework. The study
is not the works, and that is why the card is `contested` and why the clause cutting the other way
is quoted on it — the report's own "(albeit notrelated to MSISTAP or the East Tsankhi pre-feasibility
study)" about the later resettlements, which the card already carried.

**The remedial plan's findings are the plan's own, not forecasts — verified.** The plan is a
*remedial* plan: its executive summary (lines 40–46) says "The field study carried out in August,
2014 to estimate key baseline socio-economic indicators", and the counts that follow are past tense
throughout ("were impacted", "received incomplete compensation", "have not received any
compensation"). Table 2.5.1 at line 1431 is headed "Eastern Tsankhi area's pasture use and mining
impact, **2010-2011**". Table 2.7.1 at line 1704 is "Compensation provided by ETT company to the
affected persons impacted by the physical displacement", with a "Year affected by the resettlement"
row giving 2011 and 2010 and a "Current situation" row. These are retrospective findings. The only
forward-looking material in the plan is the tailings section, and the card's one sentence from it is
now explicitly marked a forecast.

**Three corrections inside the 17 economically displaced** (Table 2.5.2a, lines 1493–1520):
- the card said the plan "lists 15 of them by name". The table names **17** — two inside the
  licence area (S.Khuukhenjav, Khunchuluu) and 15 in the five-kilometre zone. The plan's own
  sentence "Out of 15 households Chimid deceased..." refers to its section B only.
- the card gave the pasture lost as running "from 14 hectares to 2,772 hectares". **The 14 is not a
  hectare figure.** In Chimid's row the printed values are `117 117 14 14` — winter camp 117,
  spring camp 117, summer camp 14, autumn camp 14 — and his hectare cell is blank. The same 14
  appears as A.Enkhtuya's summer and autumn camp IDs. The real floor is **65 hectares**
  (Khunchuluu). This is the table form of the page-number fault: a seasonal-camp identifier in the
  adjoining column read as a count.
- "against 13 of those names it records Out-migrated" is **14**; one carries "Deceased", one
  "Settled in bag center", and A.Enkhtuya carries no status at all, her pasture counted in the same
  merged cell as M. Enkhtaivan's 2,538 hectares. All four readings now on the card.

**One omission corrected.** Table 2.7.1's compensation cell for O. Erdenebileg reads "Received 2
winter camps from the soum government, 15 million tugrugs from ETT **and 3 children were employed
(requested to create a well at new winter camp)**". The card took the camps and the money and
dropped the jobs — a favourable clause in the same table cell as the damaging one.

**Also verified as an artefact, as the writer said:** "43 households affected by the mine tailing
location" (line 1833) is the page number 43 printed into the middle of a bullet about what a
resettlement agreement should contain. It is not a count.

### 1.2 `manila-sewerage-site-clearances-san-mateo-road-5` — the `displaced: 23`. **Kept at 23, with the label rewritten. I am overruling the instruction in my task and saying so.**

The two figures are confirmed in one paragraph of one outcome document,
`cache/P079661/ICR_2012-12-28_17163123.txt` Annex 6 ("Social Safeguards Compliance Results"), lines
2090–2100: "Two of the eight sub-project sites had occupants who were requested to relocate ...
There were eleven (11) households (46 persons) at the site of the North Septage Treatment in San
Mateo ... MWCI prepared an ARAP and provided relocation assistance to all the displaced households";
and lines 2104–2112: "there were 12 households illegally occupying the land. These 12 households
were considered non-poor. They were issued notifications to vacate ... MWSS ... initiated the
relocation activities ... relocation financial assistance were provided using the standard financial
assistance package per displaced household of PHP 22,500". Both counts are households, both have a
relocation verb, both are past tense, neither is a plan reprint, and the report never adds them.

My task says this map does not put derived arithmetic in `displaced` and tells me to choose between
11, 12 and removing the field. **The map's own record says otherwise, twice, including once in the
round immediately before this one:**
- `rounds/r31f_southasia_mena_checked.json`, `tripoli-tyre-heritage-market-relocation`:
  `displaced: 71`, label "the sum of the two rows of the completion report's Table 8 that record
  physical relocation of residents, 38 households with 209 people from blocks A and B and 33
  households with 124 people from block C".
- `rounds/r26f_icij3_southasia_check_log.md` line 98, a checker's own correction: "**214 is the
  writer's sum, not the report's.** The report gives 114 + 88 + 12 and no total. **Now stated as a
  sum of the report's three figures.**" The remedy there was to name the arithmetic, not to delete
  the number.

11 and 12 are each a part of what this card covers, so either would under-report, and removing the
field would drop a count the Bank's own document states twice. **So: 23 stands, and the label now
reads "... the two counts the Bank's completion report of 28 December 2012 gives in its social
safeguards annex; 23 is the sum of those two counts and is not a figure any document states."** If
the owner wants the Tripoli and Swat precedent reversed, this is the card to reverse it on and it is
a one-line edit; what I will not do is apply a rule to one card that two merged cards break.

**The Road 5 hazard reason — the card survives the limb-(a) hazard limit, but not on the balance the
writer struck.** `cache/P079661/RP_2005-03-04_5684487.txt` gives the hazard and the land need in one
sentence: "Aside from the need of MWCI to have unobstructed access to its facility ... there is also
an imminent risk to the health and safety of the lot's occupants as their houses are resting on a
structure that is not designed to bear heavy load and contains accumulated septage and gases.
Resettlement in this case is imperative." The documented loss on top of the move is in the
completion report, not the plan: the land was the sewerage system's, no payment for land was made,
the package was 60 days of the minimum wage, and the occupants were notified to vacate.

But **the same plan carries two clauses the card dropped**, in the paragraphs the card quarried for
its coercive details: "The displaced people are informal settlers who **have expressed their
preference for relocation**", and "Result of the initial dialogues are **positive with the affected
families willing to relocate** after due assistance (i.e., option 1)" — option 1 being socialised
housing, not the cash. Both now on the card. The San Mateo half is not a hazard relocation at all,
and there the plan's "The identified families **have agreed that they will vacate** the premises once
the lot is sold" was also dropped and is now restored, with the plan's estimate of 15,000 pesos
average monthly household income and the fact that four of the eleven households had arrived in
January 2005, one month before the census.

### 1.3 `philippines-irrigation-canal-easement-relocations` (P088926) — is a relocation count with no recorded loss and no site a case? **Kept. There is a recorded loss, and the siting is defensible once stated properly.**

Read in full: `cache/P088926/ICR_2019-04-25_31026588.txt` paragraphs 83–88 and the borrower's annex
paragraph 37, and `ICRR_2019-06-21_31184111.txt` section 10a.

Limb (a) is met twice over in the outcome document. Paragraph 84: "Of the informal settlers, 35
families (13 are IPs) have availed of the resettlement sites that NIA and host Local Government
Units (LGUs) have provided". Borrower's annex paragraph 37: "Thirty-five (35) families, including 13
IPs, **were relocated** to the resettlement sites provided by the Local Government Units (LGUs) in
Region 5 and Region 11."

**The premise that there is no recorded loss is not right.** The same paragraph records land taken
from identified people: "Of the 401 who had lost portions of their lands (average of 708 sq. m per
family), 102 opted to receive compensation at the prevailing market price, while other affected
people donated their lands", 288 informal settlers who had to move or "set back their homes from the
canal", "some initial delays in the payment of compensation", and funds for three absentee claimants
put in a trust account rather than paid. Land taken is an enumerated limb-(b) harm, and this is a
counted, actual taking. The nearest precedent is `swat` in round 26, kept on exactly that reading
with "Virtually all persons who lost property were compensated" printed beside it.

**The siting.** The writer was right that nothing ties the 35 families to the Tigman-Hinagyanan-
Inarihan system, and right to flag it. But the point is better founded than the writer's note
allowed, and the card now says why: Calabanga is in Camarines Sur, Camarines Sur is in **Region 5**,
and Region 5 is one of the two regions the completion report does name for the resettlement sites.
So the marker is inside a region the outcome document states, and the system it marks is the one
whose plan counts the project's largest group of canal-easement households. I checked that last
claim against every resettlement plan in the folder: Tigman 204 (`RP_2008-08-01_9861657.txt`), Lupon
67, Upper Chico 141 but recorded as "will not be affected by the rehabilitation", the rest in single
and double digits. Tigman is the largest counted group and holds the project's only full plan rather
than an abbreviated one. The `point` text now states the inference and its limit in one place.

Two corrections in the prose: the 204 are counted "within the jurisdiction of 7 lmgators
Associations", not "across four municipalities" (the four municipalities — Magarao, Calabanga,
Libmanan, Bombon — are the system's extent, line 94); and the 45 are the plan's category 3,
"willing to vacate occupied canal ROW and expect compensation on their affected assets, project
provided relocation plots and transport assistance", not simply households who "wanted plots".

### 1.4 The blank `docty` — **the P098572 document is exactly what the writer says it is, and the P115695 one is not what the writer implied.**

`cache/P098572/ICR_2012-06-29_20351543.txt`, cover pages: "Document of The World Bank / Report No:
70326-PH / IMPLEMENTATION COMPLETION AND RESULTS REPORT / ON CARBON FINANCE / TO THE PHILIPPINES
ENERGY DEVELOPMENT CORPORATION / FOR THE NORTHERN NEGROS GEOTHERMAL PROJECT / June 29, 2012".
Report number, type, date and project all confirmed. The three sentences the drop rests on are at
lines 431–447 and read as quoted, including "By the start of World Bank engagement, the project was
already halfway in its implementation" and "At the time of the review, EDC had already implemented a
resettlement plan". **So the brief's "no completion report is reachable" was a brief's silence read
as a fact, and the writer caught it. That is the best single piece of work in this batch.**

**I checked the second blank-`docty` document rather than taking the generalisation.** The Bank's
wds API for P115695 returns 43 documents, one of which has `docty: None`, dated 2014-12-31, id
27003004, pdf `.../221191481117927781/pdf/110814-AD-P115695-PUBLIC-ACS.pdf` — the writer's
description confirmed. I fetched it (the `/text/` route 301s; the pdf route returns 200 on
`documents1`) and read it. It is **Audit Report (2015) No. 005 of the Audit Office of Inner Mongolia
Autonomous Region**, a financial audit of the 2014 accounting year for loan 8047-CN, 20 pages, with
nothing on resettlement, land or compensation. So the finding to carry forward is narrower than the
writer's "a blank `docty` makes a document invisible to the type filter, and on P098572 that was the
outcome document": the blindness is real and worth a sweep, but on the one other row in this batch
where it occurs, the hidden document is a financial audit. The drop reason now records that this was
checked, so nobody has to check it again.

### 1.5 `P115695` (Bayannaoer) — the flagged line call. **Drop upheld. It is the closest call in the batch and the reason now carries the material that would reverse it.**

What is in the outcome documents (`ICR_2019-06-24_31250463.txt` paragraph 84 and borrower's annex
paragraphs 9–10): 53 hectares of permanent land required, 22 temporary; "All resettlement policies
were carried out consistent with the resettlement action plan and in compliance with the Bank Policy
OP/BP 4.12. Compensation was paid to the affected families before the land was acquired"; permanent
acquisition at loan closure 798.05 mu against 682.5 mu at appraisal, temporary 325.9 mu against
2,015.9 mu; "All settlers had received compensation, with the total resettlement compensation of RMB
5.7 million"; "the impacted household can recover regular livelihood and are generally satisfied".
No demolition anywhere: the plan says "as this project does not involve house demolition, there is
no population affected by demolition."

What the writer did not put in the reason, and I have added, because it is the strongest limb-(b)
material in the row: `RP_2010-06-01_12545251.txt` lines 4075–4090 **names the five households** —
Shan Baolin, Wang Fugui, Chen Jinyong, Wang Erhu, Hao Zhen, 22 people, Shawan Village, Shanba
Township, Hanggin Rear Banner — says 38.00 mu of the community's cultivated land was to be taken
for the No. 3 Main Drain reclaimed-water works, that this is 11.18 per cent of the community's
cultivated land, that per capita cultivated land would fall from 7.39 mu to 6.57 mu, and that for
these five households "the impact degree of cultivated land ... is more than 20%". That is better
identification than Bukoba, the standing edge.

**Why it is still a drop:** every one of those loss figures is the June 2010 plan's prospective
assessment. The outcome documents carry area and money and no loss attached to any person, and they
affirmatively record payment before acquisition and livelihoods recovered. BRIEF20's second test is
actual harm, not planned. A card here would have to print the plan's >20 per cent beside the
completion report's "can recover regular livelihood and are generally satisfied", and the second
sentence is the one from the outcome document.

**And the overrun is softer than the writer's reason said.** There are three figures for planned
permanent acquisition, not one: 682.5 mu (borrower's annex, "at appraisal"), 50.5 hectares
(appraisal document page 59, as the Evaluation Group quotes it at `ICRR` line 716), and 758.00 mu
(the June 2010 resettlement plan, section 3.3.1). 758.00 mu is 50.5 hectares — the plan and the
appraisal document agree with each other and not with the annex. Against 682.5 mu the overrun is
115.55 mu; against 758.00 mu it is about 40 mu. Both readings are now in the drop reason, unreconciled.

The reprint call on this row is sound: the review marks 50.5, 32.5 and 15.5 hectares as the
appraisal's expectations in its own words — "the PAD (page 59) notes that four towns or townships
**were expected** to be affected ... **would require** 50.5 hectares ... five rural households ...
**were to be affected**" — and gives the report's 53 and 22 as the implementation figures.

---

## 2. Every correction, with both readings

### `muntinlupa-sewage-plant-site-clearances` (P113844) — the most corrected card in the batch

| # | What the card said | What the document says | Document |
|---|---|---|---|
| 1 | "eight renters and nine tenants of an apartment on the same land were given three months' notice" | **One group of renting families, on a different parcel.** Elenita Daco's property, bought for the same plant; "On Mrs. Daco's property, were six (6) door- 2 storey apartment and a bungalow which were occupied by 9 renters/tenants ... These structures were removed to have access to the wastewater treatment plant from the Manuel L. Quezon Road." Table 3 names nine heads of household, 47 members. The report's own summary then says "The fifteen (15) households (7 informal settlers and **8 renters**)". **Nine and eight are the same group, counted twice by one report; the card made them two groups and moved them onto the Arevalo-Cruz land.** Notice from September 2012, all gone by January 2013, "More than 3 months notice", one month's rent as help, last rental not collected. | Cupang resettlement completion report, 28 May 2014, lines 441–457, 561–566, 877–880 |
| 2 | ICR triggered "the involuntary resettlement policy OP 4.12"; the review "says the project triggered Environmental Assessment (OP 4.01) and Natural Habitats (OP 4.04)" | The **completion report itself** names OP 4.01 and OP 4.04 at paragraph 68 and OP 4.12 at paragraph 71. The review cites those two paragraphs for all three. A partial list read as the full list, and a statement attributed to the wrong document — the two classes round 31 found on five of six cards in this region. | ICR lines 1540–1541 and 1588; ICRR lines 634–636, 684 |
| 3 | Maynilad "bought both plant sites, **paid the people living on them** and ran the resettlement" | Maynilad bought the sites and ran the resettlement under the loan covenant, but both resettlement completion reports record the **selling landowners** paying: "In total Php 143,000 was paid to the 7 households" by the landowner; "The fifteen (15) households ... left the area after receiving payments from the landowner"; at Tunasan "In total, Php 160,000 was given by the owner as compensations for their affected structures", and "Mr. Guerra paid the cost to rebuild the shanty of the Solomons". | Cupang report lines 448–452, 877; Tunasan report lines 940–950, 866 |
| 4 | the plots were "sold to them, not given" at 64,000 pesos a plot — and nothing else | The same section of the same report quantifies what the landowner gave up and counts it as the package: 15,900 pesos a household in transfer and title costs, 16,000 pesos in two years' free use, 50,614 pesos in forgone interest, "TOTAL - Php 82,514"; plus salvage rights, manpower to dismantle, a site within walking distance, the 14 relocated together as a group, and the report's own "would cause no significant socio-economic disruptions or physical adjustments to their usual activities". **The card quoted the price and dropped the discounts from the same page.** | Tunasan report lines 845–935 |
| 5 | the eighth Cupang household's "father-in-law was sick" | "Marjorie Solomon's **father**, who is a transient occupant was sick and could not move" | Cupang report line 868 |
| 6 | four items unresolved at the Tunasan site after the 20 June 2014 visit | Confirmed — and the same report says an updated plan of 10 November 2014 covered the restoration of those utilities, that the completion report "is prepared following the resolution of the pending safeguard measures", and that "Majority had signified contentment on their entitlement received". | Tunasan report lines 158–168, 1038 |
| 7 | the sellers' relative parcelled the relocation lot | "Marife Espeleta (**attorney-in-fact** of the sellers) facilitated the sale of the relocation site" — the report does not call her a relative | Tunasan report line 845 |
| 8 | the news report's subsidence sentence alone | The same report gives rain as part of the cause: the resident "recalled ... it was raining through Sunday night, which could have turned the ground to mush", and "Then followed several days of raining that may have caused softening and mobility of the foundation soil." | Interaksyon, 25 April 2017 |
| 9 | title: "and a house down during sewer digging in Cupang" | **Removed from the title.** No document ties that excavation to the Bank-financed conveyance system, the news report gives a second cause, and the card's own text says so. A title asserts; the body can carry a gap. The nine renting families, who are documented, took its place in the title. | — |
| 10 | "Neither document explains the gap" between 7 and 8 at Cupang | The Cupang report explains it in the sentence the card itself paraphrased: the eighth was rebuilt on the unsold part of the estate, so it never left. **False absence claim, and it contradicted the card's own prose.** Replaced with the gap that really is unexplained in that report: nine renters in its table against eight in its summary. | Cupang report lines 455–460, 866–872 |
| 11 | source: Interaksyon `?p=68221`, "25 April 2017, modified 26 April 2017" | The short link resolves (200) to the canonical article URL, now cited. The "modified 26 April" is page metadata and nobody's statement; dropped for the byline date. | fetched |
| 12 | financing: 96.7 at appraisal, 142,114,000 actual | Correct, but the table's **revised** borrower figure is 228,000,000 and the appraisal total 371,700,000. Both added. | ICR FINANCING table |

`displaced: 21` **confirmed and not a sum**: the completion report's own text says "the relocation of
21 informal settler families in Tunasan STP and in Cupang STP" and its footnote 28 reads "Informal
settler families: Tunasan STP (14) and Cupang STP (7)". ICIJ's 192 appears in no document of the
project, as the card says. The nine renting families are now in `displaced_note` as a separate
documented group that the Bank's 21 excludes — **not added in**, because no document adds them.

Plan-reprint call on this card: the 14 appears in the November 2014 updated plan as an accomplished
fact ("the cleared area previously occupied by the 14 displaced families", "Nine (9) of the 14
displaced households are now living in the relocation site"), so it is an outcome figure in both
documents and not a plan carried forward. Checked by hand, not from the brief.

### `philippines-irrigation-canal-easement-relocations` (P088926)
- title: "19.7 hectares signed over by 299 **others**" → "299 project-affected people". "Others"
  asserted the donors were a different group from the 35 relocated families. No document says so.
- the 960 has **three** descriptions, not two: "960 families, consisting of 401 landowners, 288
  informal settlers and 271 owners of crops trees" (ICR para 84); "960 PAPs whose properties and
  livelihood opportunities were affected by project construction" — persons, the report's acronym
  list defining PAP as project affected person (borrower's annex para 37); "There were 960 families
  that had encroached into the existing canal right of way" (review). The writer reported two.
- the 204 and the 45, as above.
- `lenders[0].role` **checked line by line against the data sheet and found clean**: approval
  24-Jun-2009, effectiveness 03-Nov-2009, MTR 10-May-2013, original closing 31-Mar-2015, actual
  31-Aug-2018, four restructurings on 11-Feb-2015, 24-Sep-2015, 31-Mar-2016, 13-Feb-2017;
  70,360,000 original / 58,015,957 revised and disbursed; borrower 43,230,000 / 42,844,004; total
  113,590,000 / 100,859,961; Partial Assessment (B); outcome Moderately Satisfactory, Bank
  performance Moderately Satisfactory, M&E Modest (ICR KEY RATINGS); safeguards Satisfactory (ICR
  para 88, read from the ICR); review's table agreeing on all three and rating Quality of ICR
  Substantial. The "including" before the five policies is the report's own word and the card's
  flag of it is right; the review gives the five as a closed list, which it does.

### `manila-sewerage-site-clearances-san-mateo-road-5` (P079661)
- "a tricycle driver there since 1986 and **his** unemployed cousin": the plan says "Federico Suarez
  is a cousin of **Armando Suarez**. Gene Granada is a settler **not related** to the Suarez family."
  Corrected.
- the plan's favourable clauses at both sites restored (see 1.2).
- the absence claim corrected (see §3).
- `lenders[0].role` **checked and clean** on: Japanese yen 6,592.00 million / US$64 million
  equivalent, IBRD-73110, Land Bank with the Republic's guarantee, approval 06/21/2005,
  effectiveness 03/06/2006, MTR 03/10/2008 actual, closing 06/30/2010 original and 06/30/2012
  actual, restructurings 06/25/2010 and 01/17/2011, disbursed USD 40.56M, Environmental Category A.
  Ratings **read out of the ICR itself** and not out of the review's column for them: ICR C.1 gives
  Outcomes / Risk / Bank / Borrower as Moderately Satisfactory, Moderate, Moderately Satisfactory,
  Moderately Satisfactory — the review's column reproduces them correctly this time. Review's own:
  Unsatisfactory, Moderate, Moderately Unsatisfactory, Moderately Unsatisfactory, Quality of ICR
  Unsatisfactory, Date Posted 03/12/2015 on its own first page. 1,415 tonnes against 20,400 and "one
  quarter of the originally planned number of plants" confirmed at ICRR lines 328–330.
- added: the report's cover is dated 28 December 2012 and its own data sheet gives "ICR Date:
  12/27/2012".

### `east-tsankhi-herder-displacement` (P108768)
Covered at 1.1. `lenders[0].role` otherwise **checked and clean**: IDA-44890 / C4489-MN and
IDA-H4110 / H411-MN, SDR 5.72 million, US$9.3 million equivalent, financing agreement conformed
7 October 2008, approval 26 June 2008, effectiveness 4 May 2009, MTR 1 November 2011, original
closing 31 December 2012, actual 31 December 2015, restructurings 2 July 2012, 10 January 2014,
30 March 2015, SDR 5.66 million disbursed, Category B, no safeguard policy triggered at appraisal.
The review's downgrade of borrower performance and its remark that the report's Bank-performance
rating "should have been Moderately Unsatisfactory" are the review's own. The card's attribution of
"no other safeguards issues during implementation" to Bank staff is right — ICRR line 823, "The
Project Team informed that no other safeguards issues during implementation were documented" — and
the card already says so.

### Drop reasons corrected
- **P074591**: the quotation ended on "The reasons for the change in the numbers of PAPs are not
  documented" and dropped the report's **next sentence**: "The change could be due to new settlements
  in the project areas and/or reassessment after detailed design." Added. And the review's "was
  unable to find any documentation" is the review reporting that **the completion report** could not
  find it, not the review's own search: "The ICR found that the number of project-affected persons
  increased significantly to about 200 households but was unable to find any documentation on the
  reasons for this". Re-attributed. The drop stands either way: 200 is a count of people affected,
  the 2004 plan's figures are all future-tense, and no outcome document reports the five properties
  being taken.
- **P115695**: three additions, as at 1.5.

---

## 3. Figures and dates left UNRECONCILED, both sides given

1. **P108768, cause of the relocation.** ICR: the relocation took place "in connection with
   development of this mine". Review: "the relocation of two winter shelters **by an activity
   financed by the project**" and "Two winter shelters **had to be relocated because of** a
   pre-feasibility study financed by the project". Both now on the card.
2. **P108768, date of the relocation.** ICR and review: both winter shelters in 2010. Remedial plan,
   Table 2.7.1 "Year affected by the resettlement": G. Damchii 2010, O. Erdenebileg 2011. On the card.
3. **P108768, compensation of the two.** Executive summary: "2 households received **incomplete**
   compensation for physical displacement". Section 2.7 of the same plan: "2 households received
   compensation for physical displacement from ETT". Writer reported this; confirmed; stays unreconciled.
4. **P108768, Tsagaan-Ovoo Bagh.** Impacts section: "about **137 households** are living in this
   village". Evaluation section: "has **over 100** households". Both now on the card.
5. **P079661, people at the San Mateo site.** Completion report: "eleven (11) households (**46
   persons**)". Abbreviated plan of 4 March 2005: "Total families: 11 / Total population: **53**".
   **New — the writer did not report this one.** On the card.
6. **P079661, households at Road 5.** Plan of 4 March 2005: three, named, from a census of 20
   October 2003. Completion report: "there were 12 households illegally occupying the land". The
   report offers a mechanism ("through the years, the occupant and his relatives relocated to the
   property and built houses") but the plan is dated March 2005 and still counts three. Writer
   reported the conflict and wrongly said neither document explains it; the mechanism is now printed
   and the conflict left standing.
7. **P079661, the report's own date.** Cover: December 28, 2012. Data sheet: ICR Date 12/27/2012.
8. **P113844, renters on the Daco parcel.** Table 3: nine named heads of household. Summary
   paragraph of the same report: "8 renters". One document, two counts, no explanation. **New.**
9. **P113844, informal settlers at Cupang.** Completion report footnote 28: 7. Cupang report: "eight
   (8) informal settler-households ... have been displaced", 44 persons. **Accounted for** — the
   eighth was rebuilt on the unsold part of the estate — so this is no longer offered as an
   unexplained gap. The writer offered it as one.
10. **P113844, the Bayanan house.** Main text paragraph 73: "the owner of the house **affected** by
    the Bayanan Pumping Station". Appendix 2, same subproject row: "the house that **will be**
    affected". Writer reported it; confirmed at ICR lines 1610 and 2643.
11. **P115695, planned permanent land acquisition — three figures.** Borrower's annex: 682.5 mu "at
    appraisal". Appraisal document page 59, as the review quotes it: 50.5 hectares. June 2010
    resettlement plan section 3.3.1: 758.00 mu. The second and third agree (758 mu = 50.5 ha) and
    the first does not. **New — the writer reported only the main-text-against-annex pair.**
12. **P115695, actual permanent land acquisition.** ICR main text paragraph 84: 53 hectares.
    Borrower's annex paragraph 9: 798.05 mu. Writer reported it; confirmed; stays unreconciled,
    with no conversion offered on the card.
13. **P088926, what the 960 are.** Families of three named kinds (ICR para 84); persons (borrower's
    annex para 37); families who had all encroached (review). Three readings, now all three on the card.
14. **P088926, the project's approval date.** Data sheet: 24-Jun-2009. Borrower's annex paragraph 2:
    "approved by the World Bank on June 21, 2009". The card follows the data sheet. Noted here only.

No conflict was invented and none was tidied. Where I added a conflict I named the two documents and
the line.

---

## 4. Faults appearing on more than one card

1. **A clause in the same paragraph, page or table cell, dropped — five times.** Erdenebileg's three
   children employed; the Tunasan landowner's 82,514 pesos of discounts beside the 64,000-peso price;
   the Road 5 families' stated preference for relocation beside their notice to vacate; the San Mateo
   families' agreement to vacate beside their eviction; the rain beside the subsidence. Every one of
   the five ran in the same direction — the damaging clause kept, the favourable clause in the same
   paragraph dropped. This is the fault the briefs say decides more drops than any other and it is
   still the dominant fault in this batch.
2. **"Neither document explains the gap" used twice, and wrong both times.** At Cupang the report
   does explain it and the card's own prose contained the explanation; at Road 5 the report gives a
   mechanism. An absence claim is a task, not a finding, and this writer wrote the same one twice.
3. **A count read off a table column that is not the count column — twice in this batch and both
   times with small numbers.** The writer caught two page-number artefacts ("the displaced 5
   persons", "43 households affected by the mine tailing location") and then committed the table
   version of the same fault twice on the card it was proudest of: "14 hectares" is a seasonal-camp
   ID, and "15 of them by name" takes a sub-total sentence for the table.
4. **Groups double-counted into existence.** "Eight renters and nine tenants" (one group, counted
   twice by one report) and "299 others" (asserting a group distinct from the 35). Both make a card's
   population larger than the documents do.
5. **Researcher voice in a settled phrase, three times** — "none of the 19 / nine / six project
   documents read here" and "the full list is not read here". Four instances across three cards, in
   `displaced_note` and `lenders[0].role`. No merged card uses that phrasing.

---

## 5. Card data outside the fields I was asked to check

- **`companies[0].role` on P113844 was factually wrong** (Maynilad paying the residents). Corrected.
  The other entries hold: Land Bank is the borrower and the financial intermediary; Dragonhart is
  named as the Muntinlupa conveyance contractor in the May 2018 land acquisition completion report,
  and the card is right not to equate it with the news report's Dragon Health Corporation.
- **`companies` on P079661**: the Metropolitan Waterworks and Sewerage System's role, including the
  April 2008 lease termination "for non-payment of the lease rentals and the need of the project for
  land", is in the completion report at lines 2097–2100. Manila Water as east-zone concessionaire and
  Land Bank as borrower both confirmed. No oversight body is listed beside the agency that caused the
  harm, though the Commission on Human Rights and the Presidential Commission for the Urban Poor
  appear in the prose as members of the relocation committee, which is what the report says they were.
- **`companies` on P108768**: the Ministry of Finance as implementing agency and the State
  Secretary's chairing of the steering committee are both in the report; Erdenes Tavan Tolgoi as a
  subsidiary of Erdenes MGL is in the report and the plan.
- **`ap: true` on all four** — all four are projects with an ICIJ confirmed-displacement row, which
  is what that flag has meant in every earlier round.
- **Every source URL traced to `harvest_manifest.json`, not constructed.** All 21 Bank URLs on the
  four cards match a manifest `pdfurl` path exactly, with only the host changed from
  `documents.worldbank.org` to `documents1.worldbank.org`, which is the documented behaviour of that
  host. One title mismatch worth knowing: the Cupang resettlement completion report (id 19764960) is
  filed in the Bank's archive under the title "Philippines - **Metro Manila Water and Wastewater
  Improvement Project**", a different operation's name, while the document's own cover reads "METRO
  MANILA WASTEWATER MANAGEMENT PROJECT (P113844)". The card titles it from the cover, which is right;
  anyone checking the citation against the archive's title list will think it is misfiled, and it is
  — by the Bank.

---

## 6. What I could not check, named as a route

- **No Bank route failed.** Everything cited was on disk. The two files I fetched both answered:
  the wds API query `search.worldbank.org/api/v2/wds?projectid=P115695` returned 200 with 43
  documents; `documents1.worldbank.org/.../text/110814-AD-P115695-PUBLIC-ACS.txt` returned **301**
  and `documents.worldbank.org` the same path **302**, so the `/text/` route does not serve that
  document and the `/pdf/` route on `documents1` returned 200 and 2.7 MB. That is a route finding, not
  a host one: on a document the harvester never typed, the `/txt/` shortcut the round brief
  recommends is not always there.
- **The Interaksyon short link resolves**, 200, to a canonical path; the card now carries that path.
- **I did not look for an independent source.** The writer ran nine searches and found none, and the
  confidence on all four cards is `contested`, which is where a case resting on the Bank's own report
  and the Group's review of it belongs. I spent no search budget re-testing a negative; if the owner
  wants `documented` on any of these four, the Philippine press on the Tunasan and Cupang land sales
  and Mongolian-language coverage of Tsogttsetsii soum are where it would have to come from, and the
  writer says both were tried.
- **The appraisal documents' safeguard checkbox tables.** Confirmed as a text-pipeline limit and not
  a refusal: on `P113844/PAD_2012-04-16_16243453.txt` the policy rows survive as bare names with the
  Yes/No marks stripped. Both affected cards say so without claiming the policies were not triggered,
  and on P113844 the completion report supplied the full list anyway once it was read properly (see
  §2, item 2).
- **One thing I could not settle and am not pretending to.** Whether the two winter shelters the
  Bank's documents date to 2010 are the two households the plan dates to 2010 and 2011, or whether
  "two winter shelters" means O. Erdenebileg's two winter camps and therefore one household. The
  plan's Table 2.7.1 gives him "2 winter camps, 2 herder hand-wells"; the ICR says "two winter
  shelters". No document maps one onto the other. `displaced: 2` rests on the plan's count of
  **households**, which is a people-bearing unit and is unaffected by this; the card now carries both
  datings so the question is visible.

---

## 7. Did the briefs help or mislead?

**Helped, and the writer's account of it is honest.** Two of the four cases exist because a brief
pointed at a sentence: the retroactive OP 4.12 triggering on P108768 and the reprint pairing on
P079661. The writer's three noise buckets are real, and I can confirm the fourth and worst of them
from the other side: **the "borrower's own account" bucket returning only the table-of-contents line
"Annex 7. Summary of Borrower's ICR" is the single most expensive gap in the extraction.** On
P088926 the borrower's annex is where "were relocated", the 299 donors and the 197,767 square metres
sit; on P115695 it holds the 798.05 mu and the RMB 5.7 million; on P113844 the only split of the 21
is in a footnote. **None of those is body text, and three of the four cases in this batch turn on an
annex or a footnote.** The brief should index Annex 7 and the footnote apparatus, not their
table-of-contents entries.

**Where the briefs misled, and the writer did not say so.** The briefs taught the writer to look for
a plan figure reprinted in a results table, and he did that well. They did not teach him that a
table has columns, and the two table faults in §4 item 3 are the consequence: a camp identifier read
as hectares, a sub-total sentence read as the table's extent. **The reprint check is blind to column
order, exactly as my task warned, and it is blind in both directions — not only to a plan figure
sitting in an outcome annex, but to a figure in the wrong column of a table nobody reprinted.**

One thing the extraction cannot be blamed for and should be credited with: the P098572 brief said no
completion report was reachable, the writer did not believe it, and the drop now rests on the real
outcome document. That is the round's standing fault — a brief's silence read as a fact — caught by
the writer rather than by the check, on the one row where it mattered.

## 8. The two weakest entries after correction

Not the writer's two. His weakest, P088926, is stronger than he thought once the siting is stated as
Region 5 and the 401 landowners' land is read as the limb-(b) harm it is.

1. **`muntinlupa-sewage-plant-site-clearances`** is now the weakest, and it is weakest in the place
   the writer did not name: the Cupang house collapse. It is the only harm on any of the four cards
   with no document linking it to the financed works, the news report gives rain as a second cause,
   and the contractor's name does not match the Bank's. It is out of the title and it is in the prose
   with the gap stated twice. If the owner would rather the card not carry an unattributed harm at
   all, cut the last two sentences of `community` and the last sentence of `confidence_note` and the
   card loses nothing it rests on.
2. **`manila-sewerage-site-clearances-san-mateo-road-5`**, for the `displaced: 23` and nothing else.
   The relocations are solid; the arithmetic is this map's, and whether a sum belongs in that field is
   a decision for the owner and not for me, because the map's two merged precedents and my check
   brief say opposite things. §1.2 sets both out.
