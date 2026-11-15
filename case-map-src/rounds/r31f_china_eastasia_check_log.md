# Check log, round 31, batch china_eastasia

Checked: `/home/claude/work/out/china_eastasia.json` (6 cases, 8 drops, 1 already on map) and the
writer's report. Corrected file: `/home/claude/work/out/china_eastasia_checked.json`.

Every figure, quotation, rating, date and policy list on the six cards was opened in the cached
document and read in its own paragraph. No Bank document was re-fetched.

**Outcome of the check: 0 cases cut, 6 kept, 11 corrections made, 4 of them to the same field.**
Eight of the writer's drops were tested against the outcome document and all eight hold. The reason
this check cuts nothing is in section 6; it is a property of this batch's documents, not a
concession.

---

## 1. Cases: what was confirmed, what was corrected

### `lutusi-liancheng-heritage-resettlement` (Gansu, P091949) — KEPT

Confirmed in `ICR_2016-02-27_26010945.txt`: 14 households permanently relocated, 19.54 mu acquired,
870.71 m² demolished, 26 households and 123 persons affected permanently or temporarily, planned
17 households and 1,241.49 m² (Table A6-1, actual column, titled "Actual Versus Planned Involuntary
Resettlement"); all relocation and all demolition at Lutusi (Qingcheng's rows are 0 and 0); the two
named reasons for the moderately satisfactory resettlement rating; the car park dropped after seven
households refused the site; "Compensation standards for land use and house demolition were at least
on par with those stipulated in the RAPs"; "No complaint was received throughout the project";
RMB 2.76 million estimate against RMB 5.80 million in the body and RMB 5.79 million in the table.
Cover date February 27, 2016. Datasheet: IBRD-75420, US$38.40M, disbursed US$35.02M, approved
20 March 2008, effective 11 August 2008, two restructurings (9 August 2013, 17 December 2015),
closed 30 June 2015, Category A, outcome Satisfactory, Bank and borrower Moderately Satisfactory,
risk Moderate. Review `ICRR0021406`: agrees on all four, prints the report's risk as **Modest**.
The card's handling of that substitution is correct.

The 14 households, 19.54 mu and 870.71 m² appear in no plan. Plan-reprint call: clean.

**Correction 1 — `lenders[0].role`, safeguard list.** Card: "The involuntary resettlement policy
OP 4.12 and the indigenous peoples policy OP 4.10 were both triggered." The report, twice, says
five: "It triggered five Bank safeguard policies including Environmental Assessment; Involuntary
Resettlement; Physical Cultural Resources; Indigenous Peoples; and Safety of Dams" (p. 7, repeated
in the safeguards section). A separate paragraph works OP 4.11 through seven named sites. Corrected
to the five.

**Correction 2 — `outcome`, a one-document disagreement the card did not carry.** The body says the
appraisal "estimated 34 households"; the planned column of Table A6-1 in the same report gives 17.
Added, unreconciled.

### `shihutang-dam-ganjiang-relocation` (Jiangxi, P101988) — KEPT

Confirmed in `ICR_2014-12-18_23090298.txt` paragraph 36, read whole: 654.9 ha permanently acquired
against an appraisal estimate of 615 ha, 70.6 ha temporarily against 330 ha, "141 households
comprising 515 people were relocated (appraisal estimate 169 households comprising 597 people)",
the Huangkeng site and Dongmen canal delays, the Donggang canal design change, special assistance
to vulnerable households, farmland elevated, six-monthly external monitoring confirming compliance,
RAP implementation Moderately Satisfactory "because difficulties in land acquisition impacted
progress". The 53 villages and one state farm are in the appraisal document at p. 912 in the future
tense, as the card says. Annex 1 cost table confirmed line by line: 2.13/2.17 and 28.65/28.87,
counterpart column, no IBRD figure against either. Datasheet and `ICRR14711` ratings confirmed,
including the review printing the report's "Low or Negligible" as "Negligible to Low". Date Posted
04/20/2015 confirmed on the review's own line.

The card correctly refuses the review's extra fact — that the Donggang difficulty came from
households refusing the plan — because the review attributes it to "the project team". Verified at
review line 364.

**Correction 3 — `lenders[0].role`, safeguard list.** Card: "Four safeguard policies were
triggered", listing OP 4.12, 4.37, 4.04, 4.11. The report, paragraph 28: "Involuntary Resettlement,
OP4.12; Environmental Assessment, OP4.01; Natural Habitats, OP4.04; Physical Cultural Resources,
OP4.11; and Safety of Dams, OP 4.37" — five. Paragraph 38 is where the four comes from: "the Project
was classified as Category A (Full Assessment) and triggered four environmental safeguards
policies", i.e. four *environmental* ones beside OP 4.12. Corrected to five.

### `ertanggou-reservoir-tuyamar-village-inundation` (Xinjiang, P111163) — KEPT, materially rewritten

Confirmed in `ICR_2017-10-13_28092983.txt` paragraphs 143 to 149: 103 people in 26 households, all
Uyghur herders, Tuyamar village / Ertanggou villager group of Qialekan administrative village;
"The whole village was inundated and the houses demolished"; four outside households counted inside
the 103; nobody affected at Alagou or Meiyaogou; "the 26 Uygur households in the resettled Tuyamar
village"; a new site 15 km away, 29 house yards of 1,300 m², clinic, grocery, mosque, school
expansion, RMB 5,000 of furniture; 14 ha of desert reclaimed, 818 m of canals, initial high
salinity; Table 5-4 sample of 10 households / 58 people, RMB 28,175 against RMB 41,646; costs
22,156.8 planned against 20,229.7 spent plus Y27.63 million of county money to a Y47.86 million
total; the pasturing pause attributed to a Turpan Prefecture hill-closure campaign. Datasheet:
IBRD-79340, US$100M disbursed in full, approved 17 June 2010, effective 28 October 2010, closed
31 March 2017, Category A, Highly Satisfactory outcome. `ICRR0020960` agrees on four and prints the
report's "Moderate" risk as "Modest". The dam coordinates, 89°53'E 43°18'N, are in the 2009 plan and
convert correctly to the card's point.

**Correction 4 — the plan-reprint call was made on one figure and missed the table it sits in.**
The writer flagged 103 as possibly carried forward from the plan. It did not check the rest of the
report's Table 5-2, "Inundation Impact of Ertanggou Reservoir". That table is the 2009 plan's
Table 1-2, "Physical Inundation Indexes of Ertanggou Reservoir", reprinted whole: arable 14.11,
orchard 21.37, man-made pasture 35.05, natural pasture 700, forestry 167.86, houses 4,774.36 m²,
plus the plan's Table 1-3 hydrological station. The plan's own sentence is "The area of houses which
will be resettled is 4774.36 m2" — future tense, forecast. The card presented the whole inventory,
including the 4,774.36 m² of housing, as the completion report's count of what was lost. Rewritten
on the card (`community`, `ecosystem`, `confidence_note`) to say what each document is and that
nothing says the quantities were measured again at the end.

The case survives the correction because what carries it is not the table. The report states in its
own words, and the plan does not, that the village was inundated, the houses were demolished, the
26 households were resettled 15 km away and 29 house yards were built. The plan forecast 20
households rising to 21; the report's 26 is not a plan figure. `displaced: 26` holds: a people-bearing
unit, outcome document, relocation verb ("the 26 Uygur households in the resettled Tuyamar village",
"For their relocation, Shanshan County constructed a new site"). The `displaced_label` correctly
keeps 103 as "affected" rather than promoting it.

**Correction 5 — `lenders[0].role`, safeguard list.** Card: three policies. Report paragraph 39:
"This project triggered seven safeguards: Environmental Assessment (OP4.01), Natural Habitats
(OP4.04), Pest Management (OP4.09), Physical Cultural Resources (OP4.11), Involuntary Resettlement
(OP4.12), Indigenous Peoples (OP4.10), and Safety of Dams (OP4.37)." Corrected to seven.

### `lubuk-alung-kuraitaji-road-works-death` (WINRIP, P090990) — KEPT, `killed: 1` upheld

`ICR_2021-12-14_33682829.txt` paragraph 54 read whole and the paragraphs either side of it. The
quoted sentence is exact. Both halves of it are on the card and in `killed_note`, which is the right
treatment: the report gives the driver's error and the missing traffic management provisions in one
breath and settles neither as the cause.

`killed: 1` upheld on the two tests separately. Which credit paid for the works: package 21A is in
the report's own cost annex (US$58,087 thousand) and in its table of packages supported by the
project, so the works are the loan's. Whether a cause is stated: the report states one that is a
feature of the works — "could have been prevented if adequate traffic management provisions would
had been deployed" — and the Bank treated the death as the project's own safeguards incident, under
ESIRT, with a Safeguards Corrective Action Plan and an After-Action Memo. The BPJS JKK payment is
correctly described on the card as not a statement of fault. The victim was the project's own
supervision engineer on a live works site. The counter-reading is on the card.

Also confirmed: all affected people compensated at replacement cost on an external valuation, social
safeguards upgraded to Satisfactory in December 2018, 24 complaints received and resolved, last in
October 2018 — all of which cut against the card and are all on it.

**Correction 6 — `lenders[0].role`, safeguard list, two policies asserted that the appraisal marks
as not triggered.** Card: OP 4.12, 4.01, 4.04, 4.36 and 4.11 triggered. The appraisal document's
safeguard table (p. 283 of the text file) marks Yes against Environmental Assessment 4.01, Physical
Cultural Resources 4.11 and Involuntary Resettlement 4.12, and No against Natural Habitats 4.04,
Forests 4.36, Indigenous Peoples 4.10 and Safety of Dams 4.37; paragraph 28 says of 4.10 outright
that "the results show that OP 4.10 will not be triggered". Corrected to the three, with the
not-triggered four named so the next reader does not have to redo the checkbox reading. Environmental
category B added; the card gave none.

**Correction 7 — `community`, the package 21A sequence.** Card: "a new contract let in January 2019
after the earlier contract for the same section, package 21, was terminated in June 2019". January
2019 is the date the *restructuring* that added 21A was initiated — the report's footnote 11 says
so explicitly — and the sequence as written reads as a contract let before the event it followed.
Rewritten to the report's own dates from Annex 6 Table 1: commencement of work 3 January 2019,
taking over 1 July 2019. That taking-over date is 26 days before the accident the report places on
package 21A. Left on the card unreconciled; see section 4.

**Correction 8 — the project-cost discrepancy moved out of `confidence_note` into
`lenders[0].role`.** It is a financing fact and it was crowding the field whose job is to say who is
reporting on whom. Not a factual change; both figures still on the card, still unreconciled.

### `rodriguez-ecotourism-site-397-families-relocated` (Laguna de Bay, P070899/P117470) — KEPT

Confirmed in `ICR_2014-11-25_23010868.txt`, involuntary resettlement paragraph read whole: "There
was only one sub-project with a relocation and resettlement compliance requirement. The Rodriquez
LGU had to relocate and resettle 397 families of illegal settlers from their ecotourism sub-project
site"; most accommodated at Phase 1-D Kasiglahan Village, Barangay San Jose; "Relocation of a few
families is pending as the development of the Sitio Sapo resettlement site was delayed due to issues
relating to the Development Permit and Environmental Compliance Certificate"; the NHA and NGO roles;
the Pangil expropriation case; land acquisition elsewhere by consent through purchase, lease,
donation, usufruct or exchange; compliance with OP 4.12 rated satisfactory. The indigenous-peoples
paragraph, including the NCIP clearance and the 3 per cent revenue-sharing agreement, is reported
accurately and is the clause that cuts the other way. 397 appears in no plan — only in the report
and in the review repeating it, which is why `contested` is right and the card says so.

The credit link was verified rather than assumed. The brief listed P070899 as an unverified name
match. The report covers IBRD-72050, IBRD-80350 and TF-52826; its paragraph on the additional
financing gives approval 12 April 2011, US$10 million, effective 27 July 2011, which is the ICIJ
row; Rodriguez sub-projects 38 to 40 sit under "II. ADDITIONAL FINANCING" in the report's
sub-project list, and the results table's category is "Eco-tourism/Environmental Improvement
facilities". The sub-project is the loan's.

**Correction 9 — `lenders[0].role`, half a finding, twice over, and one number no document gives.**
(a) Card: "closed on 30 April 2014 after four extensions totalling 27 months". The report gives the
four extensions totalling 27 months and then, in the next paragraph, a fifth: "the closing date was
extended (for the fifth time) by three years, to April 30, 2014"; a later page says "extension of 5
times". Corrected. (b) Card: "of which US$4.5 million was cancelled on 11 July 2013". The same
paragraph ends "Additional US$3 million was cancelled at the project closing." Added. (c) Card:
"Project P070899, with the additional financing filed as P117470." No cited document contains the
string P117470; the number is ICIJ's. Reattributed to ICIJ on the card.

Confirmed as written: Category B, disbursed US$6.80M on the datasheet and US$6.83M in the Annex 1
financing table, both on the card; Netherlands line 5.00 appraisal / 4.24 actual, parallel
co-financing; loan agreements dated January 26, 2004 and May 12, 2011 off their own cover pages;
ratings including Government Moderately Unsatisfactory; review Date Posted 10/08/2015 and the
report's "Substantial" risk printed as "Significant".

### `chunhu-fenghua-access-road-demolition` (Ningbo New Countryside, P106956) — KEPT, weakest keep

Confirmed in `ICR_2016-10-20_26901074.txt` (Report No. ICR00003806, the right file — see section 7):
Table 7.1 "Comparison of Planned and Actual Resettlement Impact", actual column, total 325.63 mu
against 265.06 planned and 7,647.6 m² against 3,479 planned, with all 7,647.6 m² on the
Fenghua-Chunhu Access Road line against 3,027 planned and the Chunhu wastewater line at 0 against
452 planned; paragraph 54's "a 24% increase over the planned amount, and housing demolition doubled
due to unforeseen requirements for the Chunhu-Fenghua Access Road", and the temporary-land sentence.
Every counter-clause the writer put on the card is there in paragraph 53: all property losses
adequately compensated, resettlement proceeded smoothly, per capita net income from about CNY 40,000
to CNY 58,600, 44 / 50 / just under 6 per cent satisfaction, no appeals on the grievance system. The
National Research Center for Resettlement post-evaluation confirmed. The plan's 95 households and
287 persons, and the planned 265.06 mu and 3,479 m², are in the June 2009 Chunhu RAP as the card
says, so the actuals genuinely exceed what any plan carried; the card correctly enters no `displaced`.

Limb (b) is met on housing actually demolished and land actually taken, both from an outcome
document's actual column, which is the `liuzhou-environment-management-resettlement` rule. It is
thin — no person is counted and the lender says every loss was paid — and it stays a keep because
the demolition is more than double what the disclosed plan told anyone to expect. This is the card
on this batch most open to a different judgement, and the writer named it as such.

**Correction 10 — `lenders[0].role`, half of the review's finding, and a disagreement the card
omits.** Card: the review "rates the outcome Moderately Satisfactory, one notch lower, giving as its
reason that the relevance of the design was Substantial rather than High." The review's reason
column has five parts, and the one it treats as the shortfall is not the design clause: relevance of
objective High, relevance of design Substantial, rural wastewater Substantial, infrastructure
Substantial, **township management in small towns Modest**, efficiency Substantial. The card also
omitted that the same review rates Bank performance Moderately Satisfactory where the report says
Satisfactory, and risk to the development outcome **Substantial** where the report says Moderate and
the review's own column for the report prints Modest. All corrected. The writer's report listed the
rating substitutions for four projects and the genuine disagreements for two, and this risk
disagreement appears in neither list.

**Correction 11 — `companies[1]`, a role taken off a plan's cover page.** Card: Fenghua Investment
Co., Ltd. "Prepared the resettlement action plan ... which it is named on as author, dated June 2009."
True but it understates what the documents put it on. The completion report names FCIC as "the
designated PIU for all infrastructure" and the review as "responsible for the implementation of the
Chunhu Town infrastructure development component including the design and construction of the
infrastructure and servicing the debt", rated Moderately Satisfactory. Rewritten to that. This is
the body that built the road the houses came down for, not a document's author.

Also confirmed: IBRD-78490, US$50M disbursed in full, approved 25 February 2010, closed 31 March
2016, no restructuring, Category B, report ratings all Satisfactory with risk Moderate. The card's
"effective 16 July 2010" is the datasheet's original effectiveness date; its actual column reads NA.

---

## 2. Drops: all eight tested in the outcome document, all eight hold

BRIEF22's withdrawn screen is not in use here. Every drop reason in this batch names what the writer
read in the outcome document, and the two that quote a null sentence say outright that the null
sentence is not what decided them. Checked individually:

| Row | What the outcome document says | Verdict |
|---|---|---|
| P123323 Ningbo solid waste | Review line 740: "The project team provided following information on land acquisition: ... relocation of 167 households with 395 persons"; line 737, immediately above: "The ICR does not discuss the magnitude of land acquisition." Completion report paragraph 80 gives 1,249 **project affected persons** and compensation "completed in full"; a sweep of the report for relocat/demolit/resettl returns nothing else. The Dongqiao Town demolition is likewise "The project team clarified". | Sound. The only count is a staff statement to the evaluators. |
| P067828 CRESP | Completion report: "all relocated households have completed the construction of replacement houses ... Income and livelihood of the affected people have been restored and even increased", no count beside it; the two named problems are the Rudong site change and the Inner Mongolia road estimate. Field-based assessment report paragraph 3.21: "The project encountered no significant issues with land acquisition and resettlement for the pilot-investment subprojects." | Sound. |
| P096158 CRESP follow-up | Shares the 2012 completion report (which covers IBRD-47920 and IBRD-48160 and the GEF grant) and the 2017 assessment report. ICIJ's 131 traces to the Huitengxile wind farm RAP, where it is the number of staff on a state-owned farm whose land, the plan says, "belongs to Huitengliang farm, not the individual staff", with "very small impact". | Sound. Reason corrected: this is the programme's **second IBRD loan**, not a GEF follow-up — the assessment report calls it "a second IBRD loan (P096158)". |
| P098654 Thermal Power | ICIJ's 702 confirmed in the October 2007 Shandong Huangtai heat pipeline RAP, in the future tense. Completion report paragraph 46 is about workers only; assessment report paragraph 2.14: "This ensured that most workers did not need to relocate as there were similar opportunities nearby." | Sound. Citation corrected: the underestimation finding is in the report's summary of what did not work, not paragraph 3.1. |
| P102398 Laos Road Sector | Completion report paragraph 64 and borrower item A.1.c confirmed verbatim. A sweep of the report for relocat/demolish/fatal/injur returns one hit, a proposed road-safety indicator. | Sound. |
| P095275 Viet Nam health | Paragraph 49 confirmed verbatim, including "no complaints on compensation/resettlement"; no relocation or demolition anywhere in the report. The framework's null sentence is quoted and expressly not the reason. | Sound. |
| P073763 Viet Nam water supply | Section 2.4 confirmed verbatim: the consequence named in the same paragraph is "considerable adverse impact on the progress of civil works". Section 2.1's three causes confirmed, including "(b) disagreement between District Committees and affected persons on the amount of compensation". | Sound, and the closest to the line in the batch. That disagreement clause is the only limb (b) candidate: it has no site, no count, and no finding that anything went unpaid or below replacement cost, which is thinner than Bukoba. Tested and agreed. |
| P090336 GEF-Ningbo | Section 2.4 confirmed verbatim: "Since the restoration of the mudflats in Plots A3 and A5 did not take place, those engaged in aquaculture were not displaced and their livelihoods were not affected by the project." Section 2.2 confirms the mudflats were not restored and the RAP "was not carried out". | Sound, and the model of a finished drop. |

`quy-nhon-coastal-cities-sanitation-resettlement` is correctly identified as already on the map.

---

## 3. The correction to the existing case, with a caveat added

Confirmed in the joint completion report of 30 May 2015, paragraphs 49 and 50: "The project acquired
around 189.4 ha of land in all three cities, with 1,247 affected HHs, of which 223 HHs had to be
resettled", and "The actual number of resettled HHs (223) was decreased by about 10 percent compared
with the original 245". So the existing case's `displaced: 1247` is a count of households affected,
not moved, and the writer is right to report it.

**What the writer's report did not say, and the lead needs:** both numbers are three-city totals
across Quy Nhon, Nha Trang and Dong Hoi, and the report gives no Quy Nhon-only breakdown of either.
223 cannot simply replace 1,247 on a card named for Quy Nhon without the label saying it is the
three-city figure. Added to the note in the checked file.

---

## 4. Figures where two documents, or one document, disagree — left unreconciled

Each is named by the quantity it measures and the date it is measured at, as the brief requires.
Items 1 to 4 are the writer's, verified. Items 5 to 8 are added by this check.

1. **Ningbo New Countryside, land permanently acquired at project end.** Body text and Table 7.1:
   **325.63 mu**. Summary of the Borrower's ICR in Annex 5 of the same report: **270.67 mu**, "5.61mu
   more than planned". Same quantity, same date, one document. Unreconciled. Both agree on
   7,647.62 m² of housing.
2. **Gansu, final resettlement cost.** Body text and Annex 6 text: **RMB 5.80 million**. Actual
   column of Table A6-1 in the same report: **RMB 5.79 million**. Unreconciled.
3. **Turfan, which county.** Completion report paragraph 143 places Tuyamar village in "Jinsheng
   township of Turpan city"; paragraphs 144 to 147 of the same report have Shanshan County
   commissioning and building the resettlement; the 2009 plan is issued by the People's Government of
   Shanshan County, places the impact in "Chalekan Village of Liangmuxing Township in Turpan" and
   cites Shengjin Township's statistical yearbook. Unreconciled.
4. **Turfan, households.** 2009 plan: 20 households and 97 people in the base year, "103 in 21
   households" in the planning year. 2017 completion report: 103 people in 26 households, and 29
   house yards built. Three household counts, one person count. Unreconciled. Note this is not a
   before-and-after of the same quantity: the plan's is a forecast and the report's is presented as
   impact, and the 103 is identical across both.
5. **WINRIP, total project cost at completion.** Completion report data sheet: Total Project Cost
   actual **US$224,160,404**, equal to the Bank disbursement because the borrower's revised
   contribution is 0. Evaluation Group review data sheet: Total Project Cost **US$223,780,891.76**,
   with Actual IBRD/IDA **US$224,160,404.03** on the same page. Same quantity, same date, two
   documents, and internally inconsistent in the second. Unreconciled.
6. **WINRIP, package 21A's dates against the accident date (added).** The report places the fatal
   accident "in package 21A on July 27, 2019". Its own Annex 6 Table 1 gives package 21A a taking-over
   date of 1 July 2019. Unreconciled; both are on the card now.
7. **Gansu, households planned (added).** Body text: the appraisal "estimated 34 households".
   Table A6-1 planned column, same report: 17. Unreconciled.
8. **Ningbo New Countryside, land planned (added).** Annex 7 text: "as compared to the 262 mu
   planned". Table 7.1 planned column, same annex: 265.06. The report's "24% increase" is computed
   off 262, not off 265.06. Unreconciled; noted on the card.

**Not a disagreement, checked and discarded.** Turfan paragraph 143's "1 ha of village farmland,
1.5 ha of orchards, 49 ha of grassland" against Table 5-2's 14.11 mu, 21.37 mu and 735.05 mu of
pasture: the same quantities in mu and hectares. The writer did not call it a conflict and was right
not to. Likewise every rating pair where the review's column for the report substitutes a word —
Modest for Moderate at Gansu and Turfan, Negligible to Low for Low or Negligible at Shihutang,
Significant for Substantial at Laguna de Bay. Those are label substitutions in the review's column,
not disagreements, and the writer labelled them correctly. The one the writer filed as a
substitution and is not is Ningbo New Countryside's risk rating: there the review's own rating is
Substantial against the report's Moderate, which is a real disagreement (correction 10).

---

## 5. Anything that could not be checked, named as a route

- **The Philippine government's impact evaluation of LISCOP.** Not attempted again this round; the
  writer's two failures are recorded as route failures and read as such. The route that failed was a
  `curl -sL` through the agent proxy to a `nep.depdev.gov.ph` path, cut off mid-exchange twice, and a
  fetch of the same URL refused by the site's robots rule. Neither is a blocked host: the URL came
  from a search result on that host. A browser route remains untried. This is the one source that
  could move `rodriguez-ecotourism-site-397-families-relocated` to `documented`.
- **Independent corroboration for the four China cases and WINRIP.** Not re-attempted. The writer
  spent two Chinese-language searches and one Indonesian-language search and reported them as
  returning nothing on these projects. That is consistent with three prior rounds. All five cards
  stay `contested` and all five `confidence_note` fields say plainly that the lender is reporting on
  its own project, which is the correct reading of the confidence rule: a completion report plus the
  Evaluation Group's review of that report is one party.
- **Whether the Chunhu demolition fell on dwellings or included non-residential floor area.** Table
  7.1's column is headed "Demolition of Houses (m2)" and the plan's 3,479 m² is residential, so the
  column is residential on its face. Neither document breaks the 7,647.6 m² down by building type,
  and no document counts the households behind it. The card says so.
- **All 15 source URLs were fetched and return HTTP 200.** Each was also matched against
  `harvest_manifest.json` to confirm the URL serves the document the card titles — including the
  Turfan plan URL, which resolves to the September 2009 Ertanggou RAP and not to one of the five
  other resettlement plans in that folder, and the Ningbo plan URL, which resolves to the June 2009
  Chunhu RAP whose cover reads "Resettlement Action Plan (Evaluation version)".

---

## 6. Patterns across more than one card

**One fault ran on four of six cards: `lenders[0].role` reports a partial list of triggered
safeguard policies as the full list.** Gansu two of five, Shihutang four of five, Turfan three of
seven, Ningbo New Countryside two of three. WINRIP is the same fault inverted and worse: two policies
the appraisal's table marks as not triggered are asserted as triggered. Five of the six cards carried
it; only Laguna de Bay did not. Round 22's audit named this class and it is still running at four
fifths of the batch. The mechanism is visible in the documents: every one of these reports states the
list twice, once as a count ("five Bank safeguard policies", "seven safeguards") and once as the
policies relevant to the section being read, and the nearer copy goes in. The count sentence is the
one to read.

**The second repeated fault is half of a finding.** Laguna de Bay twice (four extensions of five, one
cancellation of two) and Ningbo New Countryside twice (one of five clauses in the review's reason,
and two of three rating disagreements omitted). In each case the missing half is in the next sentence
or the next row of the same table.

**Selective quotation: not found.** This is worth stating because it is the fault that usually decides
the drops. On every card the clause that cuts the other way is present and in the writer's own words
— Gansu's "no complaint was received" and compensation at or above plan, Shihutang's external
monitoring confirming compliance, Turfan's satisfaction and income rise and Highly Satisfactory
rating, WINRIP's replacement-cost compensation and upgraded safeguards rating, Laguna's satisfactory
OP 4.12 compliance and NCIP clearance, Chunhu's no-complaints and income figures. The paragraph
around every quotation was read and no suppressed counter-clause was found.

**Why nothing was cut.** Four of the six cases rest on limb (a) with a count of households actually
relocated sitting in an actual-versus-planned column of an outcome document: Gansu 14, Shihutang 141
households and 515 people, Turfan 26, Laguna de Bay 397 families. That is a property of Chinese and
Philippine completion reports in this tranche, which print resettlement outcome tables that most of
the map's material does not, and it is also why the writer's drop rate of 8 in 15 is where the brief
expects it. The two limb (b) cards are the two the writer named as weakest and both were tested
hard: WINRIP's death survives both of CHECK31's tests taken separately, and Chunhu survives on the
housing-demolished rule with the plan beaten by more than double. A cut made to hit a rate would have
been a worse log entry than this one.

---

## 7. Did the pre-extracted briefs help or mislead

**They helped.** Every document on disk with its path is what made it possible to read six outcome
documents end to end, grep each for the clause that cuts the other way, and check every quotation in
its own paragraph. That is visible in the output: no selective quotation, and eight drops each
naming what the outcome document says.

**Where they misled, verified independently of the writer's account.**

1. **The reprint check missed a reprinted table, which is the thing it exists to catch.** On P111163
   the check returned two figures, 103 and 58. The completion report's Table 5-2 is the 2009 plan's
   Table 1-2 reprinted whole — six physical quantities and a hydrological station, 4,774.36 m² of
   housing among them — and not one of those figures was flagged. The check appears to look for a
   figure in a sentence with resettlement words around it, and a table row is not a sentence. Round
   22's lesson was that the reprint hides in an annex table; the check as built cannot see annex
   tables. **Fix: match figures in table rows, not only in sentences, and flag a figure that appears
   in the same column order in both documents.**
2. **The P123323 brief put the same staff statement in two buckets and let the second cancel the
   first silently.** "167 households with 395 persons" is the only entry in the one bucket that looks
   like a finding — "count with a relocation verb" — and the identical sentence is in the STAFF
   STATEMENT bucket. The writer caught it. A writer reading the buckets in order would have written
   that card. **Fix: suppress a sentence from the finding buckets when it also lands in the staff
   statement bucket, or print the cancellation beside it.**
3. **A wrong document in the cache, confirmed.** `cache/P106956/ICR_2016-10-20_26901073.txt` is the
   completion report for the **Dominican Republic Social Protection Investment Project**, Report No.
   ICR00003930, and the manifest's own title line for that file says so, with a `pdfurl` carrying
   `P090010`. The brief drew a candidate sentence from it and presented a Dominican Republic sentence
   as evidence about Ningbo. The correct file, `..._26901074.txt`, is Report No. ICR00003806. The two
   differ only in the last digit of the document id. Worth a sweep of the other cache folders for
   adjacent-id collisions.
4. **An empty harvest listed as a document, confirmed.** `cache/P117470/RP_2012-12-18_17282165.txt`
   is 243 bytes and contains four repetitions of "Public Disclosure Authorized" and the string
   RP1392. It is the only document the P117470 brief lists, and the brief presents the row as having
   one document.
5. **The candidate-parent list did not say the parent's documents were already on disk.** P117470's
   brief lists P070899 as an unverified name match while `cache/P070899/` already held its completion
   report, review, appraisal document and agreements. The row was workable only because the writer
   looked.

**Which candidate-sentence kinds were noise, checked against the documents.** `replacement cost`:
noise on every row it fired on, always the policy recital in a framework. `arrests, police or force`:
noise on all three — a procurement list of "monitoring and security systems" on P091949, compensation
procedure text and a bulldozer unit cost on P101988 and P111163. `death, with any cause given`: noise
on two of three; on P102398 it fired on proposed road-safety indicators, which a sweep of that report
confirms are the only hits in it, and on P090374 it fired on "there was no recorded fatality at
construction sites". `demolished housing`: almost all plan text in the future tense; the two outcome
figures that carried cases on this batch, Gansu's Table A6-1 and Ningbo's Table 7.1, are in annexes
and in no bucket at all. `affected, NOT a relocation count`: correctly labelled and genuinely useful,
because on five rows it is the whole of what exists and that is the drop.

**What the briefs should surface and do not, confirmed against this batch.** A bucket keyed on
"Planned", "Actual", "Actual Versus Planned" and "Comparison of Planned and Actual" would have put
both of this batch's decisive tables in front of the reader; the reprint check is the inverse of that
and surfaces only figures to distrust. And a bucket for the outcome document's own negative finding —
"were not displaced and their livelihoods were not affected", "most workers did not need to relocate",
"there were no reports of major social safeguards issues" — would collect the sentences that decided
four of the eight drops. Those are findings, and the CAUTION bucket collects only plan boilerplate.

---

## 8. Not merged, not built, not pushed.
