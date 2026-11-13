# Round 17 fact-check log — batch D (China, ICIJ displacement leads)

7 cases kept, 6 of the 7 corrected, 0 cut. 7 drops, 2 drop reasons corrected or extended.
Nothing was promoted from drop to case. `extend` stays empty.

## Method

Every document was downloaded with `curl` to `/home/claude/r17/dlD/` and read from disk with
`pdftotext -layout`. 25 PDFs in all: the Implementation Completion and Results Report and the
Independent Evaluation Group validation for each of the 7 kept projects and each of the 7 dropped
projects, plus the Independent Evaluation Group's 2018 Project Performance Assessment Report for
P112359, which the writer had not opened. `documents.worldbank.org` URLs were rewritten to
`documents1.worldbank.org`; all served. The World Bank documents API
(`search.worldbank.org/api/v3/wds?projectid=`) supplied the URLs for the seven dropped projects,
for which the draft gave none.

## The writer's central finding: tested, and it holds

The writer reported that for all 14 leads the World Bank's own documents are the only source.
Four independent searches were run against the three most serious cases, two of them in Chinese:

- `车陂村 拆迁 回迁房 猎德 污水 征地 世界银行` and an English search on Chebei village
  resettlement: results were World Bank documents, an unrelated 2012 Guangzhou urban-village
  redevelopment compensation story, and a 2026 Chinadaily piece on industrial growth in Chebei.
  Nothing on the project resettlement.
- `贵阳 油小路 世界银行 贷款 拆迁 补偿 征地`: World Bank press releases only.
- `贵广铁路 征地 补偿 失地农民 社保 上访 阳朔 贺州`: nothing on the Guiyang–Guangzhou line.

One near-miss was followed up and rejected: a Reuters report of 19 December 2008, carried by China
Digital Times, of residents in Liwan district, Guangzhou refusing to leave their homes for "a
railway", a scuffle with demolition workers over compensation and five arrests. It names no line,
and the Guangdong counties the Bank's own report lists for this project are in Zhaoqing and Foshan,
not Liwan. It cannot be tied to the GuiGuang project and was not used anywhere.

So `contested` stays on all 7 cases, and every `confidence_note` says plainly that the lender is
reporting on its own project. On the three cases where searches were run, the note now records that
searches in English and Chinese returned only World Bank documents, which is a fact about the
record rather than about the search.

## Bucket verdicts after checking

- **(a) Documented failure: leads 13, 25, 5, 22.**
  - 13 Chebei: households moved before their replacement housing existed, the Bank's own "Pending
    Issue", and the borrower demanding the passage be deleted. The strongest case in the batch.
  - 25 Youxiao Road: compensation below the plan rates found by the Bank's own launch mission;
    contracts signed three years after the road opened.
  - 5 GuiGuang: livelihood payments tied to land acquisition unfinished a year past the extended
    closing date.
  - 22 Liupanshui–Zhanyi: Yunnan compensation at times below the plan rates; six- and sixteen-month
    construction delays caused by the funding dispute.
- **(b) Large resettlement, no documented failure: leads 3 and 26.** Both confirmed as (b). Each
  records a completed move larger than the appraisal estimate with compensation at or above plan
  rates and an external monitor calling it satisfactory.
- **Lead 24 Shiyan is a borderline (a).** The failure is real, is the Bank's own finding and is a
  breach of the Project Agreement, but it is a procurement-and-procedure failure with no person,
  house or field attached to it anywhere in the record. See below.

## The three same-shape railway records: my verdict for the owner

Leads 3 (ShiZheng, 4,752 households against 3,029), 26 (JiTuHun, 5,508 against 4,221) and 20
(NanGuang, 2,463 against 2,029) are the same record in three sizes. All three: land acquisition
completed, more households moved than the appraisal estimate, compensation recorded as at or above
the resettlement plan's rates, an external monitor hired for the project concluding the plan was
implemented satisfactorily, no named community, no complaint, no failure.

Keeping two and dropping the third draws the line at household count, which is not a principle.
I did not cut 3 and 26, because CHECK17 forbids dropping a case merely for being bucket (b), and I
did not promote 20, because writing a new case is not the checker's job. But the owner should take
all three or none, and my own view is **none**: what these three cards actually carry is the gap
between ICIJ's figure and the Bank's own outcome figure, and that is one finding about ICIJ's
numbers, not three map pins. The point is sharpened by what I found for lead 20 and the writer did
not: the Independent Evaluation Group published a full Project Performance Assessment Report on
NanGuang in 2018, whose mission interviewed the project's resettlement specialist. It is the most
closely examined of the three and it records no failure — affected households relocated within
their own villages, each with a signed agreement with the local government. Of the three records,
the one with the most scrutiny is the one with the least to show. Lead 20's drop reason now carries
that report, and says in terms that if the owner wants the set, this one belongs with it.

## Corrections, case by case

### 13 `chebei-village-guangzhou-resettlement` (P075728) — three corrections, one serious

Opened: ICR00002281 (22 June 2012, 3,411 lines of extracted text, read in full around every
occurrence of "Chebei", plus the resettlement annex, the borrower's annex and the ratings pages)
and the Independent Evaluation Group's validation (10 pages, read in full).

Verified and left as drafted:
- "Resettlement was almost entirely completed by the end of 2011, except for replacement housing
  construction for Chebei Village (under the wastewater component). By 2009, a total of 154
  households (550 people) at the village had been relocated, but replacement housing had not been
  completed at Loan closing" — ICR p.11.
- The "E. Pending Issue" heading in Annex 7, naming GZPMO as responsible for completing the housing
  and saying the Bank will supervise the work through satisfactory completion. Annex 7 is the ICR's
  own annex; Annex 5 is the borrower's. The draft's attribution was right.
- "given the seriousness of the land compensation and resettlement related challenges in this
  project, the Bank could have devoted more supervision resources to work closer with the client in
  solving these issues."
- GSTC held responsible for the improper fiduciary practices and the pending resettlement issues,
  and the passage on requesting municipal mediation and realigning the collection pipelines.
- The wastewater component table: 643 households and 6,780 people against 6,030 and 24,342 planned;
  1,207 mu against 1,640; 238,868 m² of housing affected against 958,564.
- The borrower's comments, word for word. The draft's rendering of them is accurate, including the
  request to delete. The exact sentence is now quoted on the card: "There is still serious dispute
  between two parties, and the assessment made by the Bank solely from the Bank's perspective in the
  ICR is not fair and Guangdong PMO requested to delete all the related Chebei Village resettlement
  issue from the ICR."
- Loan facts: IBRD-47420 US$128m and GEF TF-53359 US$10m, disbursed US$126.89m and US$9.99m,
  effective 30 November 2004, closing 31 December 2009 moved to 31 December 2011, restructuring
  5 February 2010, project IDs P075728 and P084003.

**Correction 1, serious.** The draft gave the Independent Evaluation Group's outcome rating as
Moderately Satisfactory. That is the completion report's rating. The Independent Evaluation Group
rated the outcome **Moderately Unsatisfactory** and the risk to the development outcome Significant.
Both ratings are now printed with who gave which.

**Correction 2, serious.** The draft wrote that the validation "does not mention Chebei Village" and
"records instead" that the plan was successful. The village is not named, but the validation does
cover the issue, and what it says is stronger than anything the draft used:

> "The ICR notes that resettlement had been completed by project closing with the exception of the
> completion of replacement housing for one village affected by the wastewater component. 154
> households had been relocated, but replacement housing had not been completed. The Bank team
> reported to IEG that there had been a published announcement that Guangzhou had started the
> construction of replacement housing for the affected households in 2013. No information has been
> provided with respect to the location of the relocated households in the absence of uncompleted
> replacement housing. Note that the Borrower disputes that any further action is required."

Nobody told the Bank's evaluators where 154 households were living. That is now on the card and in
the confidence note. The absence claim as drafted was literally true of the name and false of the
substance; it is removed.

**Correction 3.** "The Bank left the passages in and published them alongside the request" was a
characterisation of a decision. Replaced with the observable fact: the passages remain in the report
as published and the request to delete them is printed beside them.

Also: `lk` was `["wb","gef"]`. `gef` is not in the map's existing link vocabulary (18 codes across
957 cases, no `gef`), so it is now `["wb"]`; the Global Environment Facility grant stays named in
`lenders`. `displaced_label` reworded, because the 6,780 figure is the project total as well as the
wastewater component total — the Independent Evaluation Group gives the same number for the project.

### 25 `guiyang-youxiao-road-resettlement` (P093963) — two corrections

Opened: ICR00002512 (10 May 2014, 2,444 lines) and the validation (read in full).

Verified exactly as drafted: "During the Project Launch mission in July 2008, the Bank mission found
that compensation rates for the Youxiao Road resettlement were lower than those specified in the
RAP"; remedied, and in October 2008 rates higher than the RAP required; "All 142 households
displaced due to construction of Youxiao Road signed contracts for resettlement and/or compensation
only by September 2013, just 3 months prior to project close"; "Full resettlement will not be
completed until December 2014"; the road opened to traffic 5 February 2010; land acquisition and
resettlement on the Youxiao Road US$22.07m at appraisal against US$72.95m actual and on rural
transport US$27.62m against US$33.03m (Annex 1, "At Appraisal" and "At Actual", US$ million); the
September 2009 mission finding about half the Batch-I rural roads and bus terminals behind schedule
"mainly due to unresolved resettlement issues"; Xiaohegou–Shuikou and Weicheng–Liuji finished one
month before closing; six external social monitoring reports, the last in April 2014; total project
cost US$314.42m estimated against US$360.70m actual; loan IBRD 48810-CHA, approved 8 January 2008,
signed 18 March 2008, effective 9 June 2008, closing 31 December 2012 moved to 31 December 2013,
disbursed US$100.00m in full; the legal covenant added by the December 2012 restructuring.

**Correction 1.** The draft said the Independent Evaluation Group rated the outcome Satisfactory.
It rated it **Moderately Satisfactory**, as did the completion report. Both are now given. The draft
also attributed the completion report's quality-at-entry rating to the Independent Evaluation Group;
the two differ (Moderately Unsatisfactory in the report, Moderately Satisfactory in the validation)
and both are now printed.

**Correction 2.** OP 4.12 and OP 4.20, and the Miao and Buyi communities, appear in the validation,
not in the completion report. `conditions` now says so.

Added: the Independent Evaluation Group rated the quality of the completion report **Unsatisfactory**,
because it made statements about the project's achievements without substantiating them. On a case
that rests on that report alone, that belongs in the confidence note.

Tightened: the completion report gives the scope as 11 rural roads and 16 bus terminals and the
output as 11 segments of rural road, 15 bus terminals and one freight depot. `point` now says which
is which instead of mixing them.

### 5 `guiguang-railway-land-acquisition` (P107559) — two corrections

Opened: ICR03434 (15 June 2017, 2,923 lines, including Annex 9 in full) and the validation.

The two quantities the task warned about are distinct in the record and are now distinct on the
card in all three places they appear. The completion report, p.8–9: permanently acquired land
"affected 26,696 families, including 64,030 people"; temporary acquisition "affected 21,643
households, including 81,324 people"; and separately, in the risk section, "More than 60,000 farmers
were affected and around 8,000 people were relocated." `displaced_label` now carries both the
64,030 and the 8,000 so the headline number cannot be read as a count of people moved out of their
homes.

Verified as drafted: the programmes "account for about three percent of total support to the project
affected people and about half of it had not disbursed at loan closing"; the closing date extended
by one year to 31 December 2016 because the three programmes were not complete; the agreement of
23 September 2016 and the transfer of CNY 337 million; and every detail of Annex 9 — the nine
Guangxi counties and districts by name, RMB 90.46 million, funds to municipal level on 12 December
2016 and to county finance bureau social security accounts between 20 January and 29 March 2017,
accounts for affected farmers still being established, funds to reach county accounts by the end of
2017; the six Guangdong counties and districts in Zhaoqing and Foshan paid to bureaux and expected
to reach villages by the end of May 2017; Guizhou bureaux paid in November 2016 and the programme
expected to finish March 2018. Also verified: 857 km, 226 villages in 87 townships of 26 counties,
restructuring 2 August 2013, line operating from December 2014, 40 of 48 sensitive areas avoided,
IBRD-76780 US$300m approved 16 April 2009, effective 26 August 2009, disbursed US$299.49m, borrower
financing US$12,226.56m estimated against US$12,755.49m actual. The appraisal figures the draft
attributes to the validation are all there, including 23,983 households and 100,190 persons, of whom
63,164 through land acquisition and 3,259 households with 11,041 people through urban house
demolition.

**Correction 1.** The draft used Annex 9 and omitted the main text. The same report, paragraph 43(a),
says "Guangxi Province. The SIP was completed in March 2017", and paragraph 28 says only the Guangxi
programme was complete when the report was prepared. Annex 9, current to the same month, says the
government was still establishing the farmers' accounts and the funds would reach county accounts by
the end of 2017. Both are now printed, with the note that the report does not reconcile them. Not
reconciled here either.

**Correction 2.** The validation rated the outcome **Satisfactory** against the completion report's
Highly Satisfactory. Both now given.

### 22 `liuzhan-railway-resettlement` (P086515) — no corrections

Opened: ICR00002178 (2,239 lines) and the validation. Every figure checked against the page.
"Cash compensation for land acquisition in Yunnan Province was paid to affected persons at the rates
established by local government before July, 2009, which were at times below the RAP rates" — exact,
and it is in the ICR's own Annex 4 on environmental and social safeguards, not in the borrower's
annex, so the draft's attribution to the completion report is right. Also verified: RMB 49.7 million
of additional in-kind spending and the external monitoring's conclusion that each village's in-kind
expenditure offset its land compensation shortfall; total land acquisition cost RMB 1.02 billion,
"104% more than the estimates in the RAP"; 16 per cent less land, 16 per cent more houses demolished;
eight concentrated resettlement sites; six months' delay in Yunnan and sixteen in Guizhou; income
per head rising to RMB 3,200, up 7 per cent; the borrower's annex figures (431,886 m² of housing,
5,587.4 mu, RMB 24,000/mu and RMB 500/m² average with the railway paying RMB 13,000 and RMB 240,
3,702 mu temporary, RMB 17.24m rent, RMB 9.67m for 671 mu unreclaimable, RMB 7.31m for crops and
fruit trees, no petitioning and no violent confrontation, everyone resettled in place); loan
IBRD-48470 US$200m, effective 16 May 2007, disbursed US$199.76m, closing 30 June 2012 moved to
30 June 2013, total financing required RMB 13,285m against RMB 9,433m. Validation outcome
Satisfactory, the resettlement risk "identified but not adequately mitigated", construction held up
"by more than six months", and the OP 4.04 point about the nature reserve with no reporting on
compliance issues. This card carries no `displaced` number, which is the honest choice: no document
gives one.

### 24 `shiyan-connecting-road-safeguards` (P081749) — four corrections, and the trap

Opened: ICR00001409 (2,947 lines) and the validation.

**Correction 1, a fabricated figure.** "Total project cost at appraisal was US$529 million" is in
neither document; "529" does not occur in the completion report. Annex 1 gives total project cost
US$533.90m at appraisal against US$725.361m actual, and borrower financing US$329.00m estimated
against US$527.00m actual, 160 per cent. The card now carries those.

**Correction 2, the trap.** `displaced_label` read "persons in 1,480 households relocated for the
expressway and local roads". The completion report makes no such split: it gives 5,007 persons in
1,480 households for the resettlement carried out under the Resettlement Action Plan, project-wide,
and the connecting road was inside the project until the Bank dropped it. The label now says
"relocated under the project's Resettlement Action Plan", and both `community` and `displaced_note`
state in terms that the figure is not for the widened connecting road, for which no figure exists.
On the task's question: no, the card cannot now be read as attributing 5,007 people to the connecting
road, and it does not assert any human harm from the widening. What it asserts is the Bank's own
finding of a procedure breached. That is all the record carries.

**Correction 3.** Added from the completion report's output table: the connecting road was completed
under the project as a two-lane road, and the widening to four and six lanes was financed by Shiyan
city. That sequence makes the misreading harder still.

**Correction 4.** "Wuhan University" is "the University of Wuhan" as the validation prints it. Added:
the validation sets the Shiyan road out under fiduciary compliance and calls it the only issue in
the project's procurement.

Verified as drafted: the city of Shiyan arranging with the contractor to widen the road, "This was
not in accordance with the Project Agreement, and safeguards procedures were not followed"; the
April 2006 post-review mission finding that "Bank policies on procurement and safeguard were not
strictly followed"; the road dropped from Bank financing and paid for by the city; US$0.47 million
of savings reallocated in May 2007; built together with Gansu Road, not Bank-financed; the Bank not
informed in advance; 75/16/4 per cent post-resettlement survey, with the remaining share unaccounted
for in the report; brick-and-concrete houses larger than those previously occupied; the heavy rains
of 2007 collapsing slopes and retaining walls and the policy changes on resettlement compensation;
loan IBRD-47450 US$200m, effective 30 December 2004, disbursed US$199.0m, closing moved to
31 December 2009; outcome Satisfactory in both documents.

**My view for the owner: this is the weakest of the four (a) cases and I would not argue if it were
cut.** A breach of the Project Agreement with no recorded consequence for any person is a
governance finding, not an episode of harm, and this map's cases are episodes. It survives because
the breach is the lender's own finding about its own loan and is stated without a harm figure
attached. If the owner wants only cases with people in them, this is the one to drop.

### 26 `jituhun-railway-resettlement` (P122321) — two corrections

Opened: ICR00003943 (2,667 lines) and the validation.

Verified: 18,495 mu acquired against about 17,000 estimated; 1,233 hectares against 1,133.3 in the
validation; 5,508 households relocated against 4,221 estimated; resettlement cost at completion
RMB 5.24 billion, 22 per cent above the approved budget; the line fully opened September 2015; the
appraisal split of buildings (39 per cent rural housing, 49 per cent urban); 98 per cent rural
collective land; no illegal structures expected; loan IBRD-80520 US$200m approved 24 May 2011,
effective 30 August 2011, closed 31 December 2016, disbursed US$198.67m, project about US$6.3bn.

**Correction 1, the minority-village point.** The screening finding is accurate: the validation says
"Korean minority villages in Jiaohe Country and some villages in Man minorities in Yanji City were
within the project intervened areas", and an Ethnic Minority Development Plan was prepared and
integrated with the resettlement plan. Nothing in either document says what happened to those
villages, how many of those households were moved, or what they were paid. The card stated the
screening finding without saying that, which left a reader free to supply a harm. `conditions` now
says in terms that no figure or outcome for those villages is on the record. Unlike GuiGuang, this
project has no count of ethnic minority households relocated anywhere in the record.

**Correction 2.** "31 per cent more households than the plan allowed for": 5,508 against 4,221 is
30.5 per cent, and an appraisal estimate is not an allowance. Now "about 30 per cent more households
than the appraisal estimate". Added both outcome ratings (Highly Satisfactory in the report,
Satisfactory in the validation).

Noted, not printed: the validation gives the resettlement cost as "RMB 5.24 million" where the
completion report says RMB 5.24 billion. At 5,508 households the million figure is impossible. This
is a unit slip in the validation, not a disagreement between two documents, so printing it as a
conflict would have been inventing one. The card uses the completion report's figure.

### 3 `shizheng-railway-resettlement` (P099062) — one correction

Opened: ICR00003435 (2,477 lines) and the validation.

Verified: 10 km² acquired, 5.5 in Hebei and 4.5 in Henan, against 11.5 km² at appraisal; 4,752
households relocated, 3,195 in Hebei and 1,557 in Henan, against 3,029 at appraisal; house
compensation averaging RMB 450/m² in Henan and RMB 600–800/m² in Hebei, "higher than that of the
RAP"; the appraisal socio-economic assessment figures from the validation (1,171.2 hectares, 3,029
households with 15,087 persons, 46 enterprises and nine schools with 4,134 persons, 886 hectares
temporary); loan IBRD-75570 US$300m approved 24 June 2008, effective 18 November 2008, disbursed
US$297.06m, closing 31 December 2013 moved to 30 November 2015, restructuring 21 August 2012.

**Correction.** "57 per cent more households than the plan allowed for" is arithmetically right
(4,752 against 3,029) but an appraisal estimate is not an allowance; reworded. Added both outcome
ratings, Satisfactory in each document.

Noted, not corrected: the validation prints "collective land on which 9.815 persons lived" in a list
of person counts. The card gives 9,815. The decimal point is a typo in the source; the figure is
left as a count because that is what the sentence counts.

## Drops — all seven checked, all seven stand

The five numbers going into the handoff were each read on the page:

| Project | Bank's own outcome figure | ICIJ |
|---|---|---|
| Shaanxi Ankang P075613 | 698 households, 2,998 persons relocated (ICR; repeated in the validation) | 171,568 |
| Huai River P098078 | 4,884 people to be resettled after design changes cut it from 7,044 | 58,659 |
| Liaoning P099992 | 2,467 households, 119 enterprises and shops, 6,080 people | 31,547 |
| Fifth Inland Waterways P085333 | 57 households, 223 people relocated | 25,655 |
| Fourth Inland Waterways P077137 | 131 households, 559 persons, against 49 households and 151 persons planned | 16,805 |

All five verified. Supporting detail verified too: Ankang's 5,713 mu permanent (3,040 mu farmland),
2,459 mu temporary, 11 enterprises, RMB 262 million, and the external monitor's conclusion that
affected households restored their income and housing; Liaoning's original plan of 4,994 households,
677 enterprises and shops and **31,547 people** — ICIJ's figure is the plan figure to the person, the
single clearest example in this batch of what ICIJ's number is; Liaoning's 2007 external audit
finding of "serious issues of non-compliance in the use of Bank's funds in the Panjin and Fushun
jurisdictions", RMB 19.89 million claimed in Panjin for work not conforming to specifications and
RMB 7.7 million in Fushun drawn for unapproved work and returned, which is a fiduciary finding and
not a resettlement one, as the draft said; the Fifth Inland Waterways details (37,541 mu / 2,503 ha,
all 57 households moved within the same village, 23 business enterprises, 34 vulnerable people on
RMB 100–300 a month, reservoir villages losing under five per cent of their land); the Fourth Inland
Waterways details (864 ha, 4.2 per cent above plan, RMB 236.7 million paid against a budgeted
RMB 66.0 million, income per head up 112 per cent at the dam site and 32 per cent in the reservoir
area, Guangdong acquisition up from 56.6 to 77.8 hectares).

Two drop reasons corrected:
- **Lead 33** now gives 131 households *with 559 persons* against 49 households *and 151 persons*
  planned, from the ICR's comparison table. The draft gave households only.
- **Lead 20** rewritten to add the Independent Evaluation Group's 2018 Project Performance
  Assessment Report and to state the consistency point openly. See the verdict section above.

**Lead 14 Fujian Highway (P091020) is confirmed as the batch's one true bucket (c).** The validation
says: "The ICR does not explicitly state the compliance for each safeguard. No information about
mitigation activities, impacts, and affected households is provided in order to validate compliance.
The information had to be sought from the project team." The completion report's whole statement on
the subject is that "the safeguard issues and compliance were well managed". There is no outcome
figure for land or households anywhere in either document, so ICIJ's 45,578 cannot be tested against
anything. Correct drop, and the reason as drafted is accurate.

## Checks that found nothing wrong

- **ICIJ's figure is nowhere in a `displaced` field.** Every `displaced` holds a Bank document's own
  outcome figure, every `displaced_note` names ICIJ, says the figure comes from the Bank's own
  documents and dates it to 31 December 2014. On leads 3 and 22 the note says plainly that no figure
  in the record matches ICIJ's.
- **No card implies displacement larger than the documents support.** The one place where that risk
  was live, lead 24's 5,007 persons, is fixed above. Lead 5's two quantities are now labelled.
- **Deaths.** `killed` is 0 on all seven and no document attributes a death to any of these projects.
  No construction fatality figures appear in any of the 25 documents.
- **Duplicates.** Nine China cases exist on the map. None is within 50 km of any of these points
  except `gold-peak-huizhou-cadmium`, 106 km from Chebei, which is a battery-plant cadmium case of
  2004–2006 and unrelated. No id collides with the 957 existing ids.
- **Coordinates.** All seven sit on the place named in `place`: Chebei in Tianhe District (23.126,
  113.384), Yangshuo County on the GuiGuang corridor (24.78, 110.49), Guiyang (26.55, 106.75),
  Shiyan (32.63, 110.80), the Liupanshui–Zhanyi line (26.09, 104.28), the Jilin–Hunchun line (43.37,
  128.23), the Shijiazhuang–Zhengzhou line (36.40, 114.07). All carry `ap: true` and a `point` that
  says what the coordinates are.
- **Writing.** No first person, no process narration, no "the draft" anywhere in the seven cards,
  before or after correction. Nothing was rewritten on that ground.
- **Schema.** Validated with python: required keys present on all seven, `mechanism`, `rg`, `kind`,
  `levers`, `lvwhy` keys, `confidence` and `lk` all from the allowed vocabularies, ids unique and
  absent from `cases.json`, all source URLs http(s), and each of the 14 lead numbers appearing
  exactly once across `cases`, `extend` and `dropped`.

## Pattern worth carrying forward

Three of the six corrections to kept cases were the same mistake: **a rating from the completion
report attributed to the Independent Evaluation Group.** On lead 13 it reversed the finding, because
the evaluators downgraded the project to Moderately Unsatisfactory and the card said Moderately
Satisfactory. The two documents carry two columns of ratings and the validation prints them side by
side; whoever writes the card must read the column heading. Worth a standing instruction: give both
ratings, with who gave which.

Second pattern: **the validations are shorter and were read less carefully than the completion
reports, and they are where the sharpest sentences are.** The best line in this whole batch — nobody
told the Bank's evaluators where the 154 Chebei households were living — sits in a ten-page document
the draft had described as silent on the subject. An absence claim about a short document is as much
work as an absence claim about a long one, and it failed here on the short one.
