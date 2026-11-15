# Round 32 — east_southern_africa — check log

Checker's file: `/home/claude/work/out32/east_southern_africa_checked.json`.
Writer's file: `east_southern_africa.json` (11 cases, 1 drop, 1 already on the map, from 13 rows).

**Result: 6 cases, 6 drops, 1 already on the map.** Five of the writer's eleven keeps are cut. Every
one of the six surviving cases is corrected; three carried a figure, a quotation or an attribution
that no document supports.

---

## The 85 per cent case rate was not sound

The batch file settles the frame before any document is opened. Every one of the thirteen rows
carries `"relocation_counts_in_outcome_doc": null`, so **limb (a) of the forward rule was
unavailable on all thirteen** and the writer knew it. Eleven keeps therefore had to rest on limb (b),
and the writer's own report says so. What the reading shows is that five of them rested on something
thinner than `bukoba-airport-resettlement-arrears`, which the task names as the standing edge:

| row | what the whole case rested on | verdict |
|---|---|---|
| P083325 Mozambique | one clause: people "were displaced ... and were consequently relocated to a new settlement". No count, no site, no loss | drop |
| P050440 Uganda | seven households named in a plan; outcome documents say people "had to be relocated", no count, no loss | drop |
| P060005 Rwanda | "866 persons were compensated" — compensation paid, no loss on top | drop |
| P069208 Uganda | "one lady" in a future-tense plan; the outcome sentence is a list of mitigation measures | drop |
| P071407 Zambia | "resettlement took place prior effectiveness. It included adequate compensation" — no count, no loss | drop |

Three of those five (Rwanda, Uganda P069208, Zambia P071407) are the shape the forward rule names
explicitly as a drop: *land taken and fully compensated with no loss recorded on top of it*, and
*a completed, compensated acquisition with no count in an outcome document*. Mozambique and Uganda
P050440 are the shape it names as the other drop: *a card whose entire content is a count of people
affected*, or in these two cases not even a count.

The remaining six are real and two of them are strong — Zanzibar's five deaths with a cause each and
Malawi's economic displacement of 22 people, four institutions and 32 fishermen are both recorded
in a completion report in its own words.

So the 50 per cent rate this check lands on is in line with the rest of the round and with rounds 16
to 22. **The batch was written to a looser line than the rest of the round**, in one specific way: the
writer treated "a relocation verb somewhere in an outcome document" as satisfying the forward rule,
where the rule requires either a count attached to that verb or a loss recorded on top of the move.
That single reading produced four of the five cuts. It is not carelessness — the writer named
Mozambique and Uganda P069208 as its own two weakest entries, and both are cut — but it was applied
across the batch and nothing else in the batch corrected for it.

---

## Cuts, each with the document and the sentence that decided it

### 1. `jardim-benfica-road-resettlement` (P083325) — CUT
Deciding document: completion report ICR00004791, 28 November 2019, paragraph 82.
Deciding sentence: *"Project implementation was generally carried out in line with the social
safeguards frameworks and plans, and there was effective engagement with project affected persons
throughout the period, especially where the PAPs along the Jardim-Benfica Road who were displaced by
the road works and were consequently relocated to a new settlement."*
The relocation clause is a subordinate example inside a favourable finding. Nothing is counted; the
settlement is not named; no document records a loss. The rest of the paragraph, which the card did
carry, runs the other way (strong performance by the road administration's social unit; external
audit of the resettlement rated satisfactory). The Evaluation Group's review goes further than the
report and says "for the rehabilitation work, no land acquisition was required and there was no loss
of other assets or crops" — the report confines that to the emergency works. Only figure in the
harvest: "resettlement for 25 structures at US$5,592.94 each", a budget line in the November 2006
policy framework, for structures. Reopenable if the Jardim-Benfica resettlement action plan is found.

### 2. `kampala-records-centre-households-moved` (P050440) — CUT
Deciding documents: completion report ICR00003266, 26 February 2015, paragraphs 42-43; abbreviated
plan of October 2006.
The report says only *"since there were people currently living at the site identified for the NCRA
who had to be relocated, an abbreviated Resettlement and Compensation Action Plan (RAP) was also
developed"* and that the ministry *"held meetings with the people residing at the site to implement
the recommendations of the RAP"*. Neither says the move happened. The plan is wholly future tense —
*"the compensation will be paid for the 7 households before effectiveness of the project"*,
*"physical relocation will take place as soon as the PAPs find reasonable accommodations"* — sets the
entitlement at six months' rent plus crops plus transport, and says *"the compensation rate is in
line with the established rates in Uganda"* and *"the households do not have fixed structures or
assets that could be lost as a result of relocation"*.
Selective quotation found: the one outcome statement on safeguards is favourable **and** is a staff
statement — *"it was noted by the project environmental and social specialists that no major
safeguards issues arose during the implementation of the project"* — and the card omitted it.
**Two facts on this card are in no document for this project.** "The two grandchildren in one
household had never been to school" and "one man had no identity card, had tried once to get one and
lacked witnesses" do not appear anywhere in `cache/P050440/` (five documents, all greppable). They
are in the Morupule B abbreviated resettlement plan of May 2009, `cache/P112516/RP_2009-05-21`,
lines 123-132, another row of this same batch, where they are true of the Botswana family. Verified
by grepping the whole 1,000-plus-project cache for both strings: `never been to school` returns
P090157 and P112516 only.

### 3. `kigali-huye-musanze-urban-works-compensation` (P060005) — CUT
Deciding document: completion report ICR00001375, 24 June 2010.
*"The Resettlement Action Plans have been completed and recommendations to finalize compensation
taken into account. A total of 866 persons were compensated in accordance with the Resettlement
Action Plans."* The next sentence, dropped by the card: *"The June 2009 and March 2010 implementation
support missions by Bank safeguards specialists confirmed that Bank safeguards policies have been
respected."* The 2018 field assessment repeats the 866 inside an equally favourable paragraph
(*"consistently rated safeguards compliance as satisfactory"*). People compensated is not people
moved, and no loss is recorded on top. The 29 households and the 17 who were to move their own hedges
uncompensated are from the October 2006 plan and are what was planned. The idle 33 hectares at
Akumunigo is an efficiency finding about project resources, which is what the Group uses it for.
Ratings on the card were correct and are recorded in the drop reason.

### 4. `mutundwe-thermal-plant-land-and-homes` (P069208) — CUT
Deciding documents: resettlement plan RP442, November 2006; completion report ICR2159, 31 March 2012,
paragraph 36.
Plan: *"The construction of the thermal-power plant ... will affect one lady in a negative manner.
This will be in form of loss of land and crops."* Future tense, one person, to be compensated.
Report, read whole: the paragraph opens *"The project complied with the identified safeguard policies
(OP 4.01 and 4.12) at both preparation and implementation phases"* and the sentence the card leaned
on is a list of measures — *"Other mitigation measures included compensation and resettlement for
residents near the plant in other areas for the duration of the PPA; construction of a 5m noise
barrier ...; and monitoring of households that were resettled out of the plant site."* The relocation
word is inside the description of a monitoring measure. No count, no place, no amount, no loss.

### 5. `imusho-village-moved-from-national-park` (P071407) — CUT
Deciding document: completion report ICR00002238, 29 June 2012, paragraph 50.
*"Guided by the RAP, resettlement took place prior effectiveness. It included adequate compensation
as determined by a Bank social specialist."* That is the whole of it. No count — the 35 adult men, 12
adult women and 13 children are the September 2003 plan's census of November 2001, before the move.
The plan records the move as agreed after meetings, with title to 233.53 hectares at the new site,
compensation at replacement cost without depreciation paid before anyone moved, transport provided,
and leave to stay for anyone who chose. Nothing is recorded as lost on top. The Namwala Game
Management Area displacement, which the card carried as a second harm, is uncounted and the same
paragraph attributes it to *"an instruction issued by the land chiefs"* and records the Bank's
conclusion of no non-compliance. The timing test is met despite the pre-effectiveness move — the plan
was prepared for this project and cleared by the lender, and the report's own output table lists
"Resettlement of Imusho village prior effectiveness" as a project output — so the row dies on the
forward rule and not on timing. That is recorded in the drop reason.

### 6. `p075997-cape-biodiversity-coleske` (P075997) — the writer's drop, CONFIRMED
Checked as instructed, against the outcome document and not a plan. The completion report of 25
April 2011, paragraphs 37-39, is quoted accurately: the farm purchase *"completed well before the
start of the BCSD project, was between willing buyer and willing seller"*, the project *"did not
include funding for any such resettlement"*, and the Coleske residents *"have thus been able to
maintain or improve their livelihoods"*. The drop is sound, and the two Macgregor documents are
recorded on the right side of it.
**One correction inside the drop reason.** The phrase *"was not completed by project close"* is in the
Evaluation Group's review (line 443), not in the completion report, which the drop reason attributed
it to. Fixed in the checked file.

---

## Corrections on the six cases kept, with both readings

### `kasumbalesa-market-traders-moved` (P071985) — KEEP, three corrections
The strongest case in the batch, and the writer's reading of why is right: the abbreviated plan of
May 2006 is an outcome document for the move, because the move had already happened —
*"The EMU was informed late 2005 (December) that some marketeers had been resettled from the
north-eastern side of the road to the western side of the road"*, and *"The EMU was informed after
the marketeers had been resettled."* Limb (b) is satisfied well above Bukoba: 67 numbered traders
with names and national registration numbers, trade by trade, with sums set and no document saying
they were paid. The table checks out line by line — restaurants 1-23, groceries 24-43, marketeers
44-64, carpentry 65, pay phones 66-67; K2,590,000 / K1,390,000 / K400,000 / K250,000 / K8,000,000;
total K113,410,000 as printed.

1. **`displaced` 65 → removed.** Two reasons, either sufficient. The figure is explicitly inexact —
   *"The total number of people involved is roughly sixty-five (65)"* — and an inexact figure is a
   floor that belongs in the note uncounted. And the verb attached to it is not a relocation verb:
   65 counts the people being compensated, while the relocation sentence counts nobody ("some
   marketeers"). `displaced_label` removed with it; `displaced_note` now carries both figures and
   says why neither is counted.
2. **A quotation that is not in the document, attributed to the wrong document.** Card: *"The
   completion report says the government's share of the money was not paid on schedule, which caused
   'major delays in implementing the Resettlement Action Plan'".* The sentence is in the **Evaluation
   Group's review**, line 448, and reads *"causing delays in implementing the Resettlement Action
   Plan (RAP)"* — the word "major" is not there. It appears in the completion report, but attached to
   something else: *"major delays in the release of funds by the Government to support ROADSIP II"*.
   This is the two-copies mechanism the round 22 audit named.
3. **Selective quotation in the same sentence.** The review's next clause, dropped by the card:
   *"However it was fully realized (US$64.3 million) at project closure as per commitment"*, and the
   review rates government performance Moderately Satisfactory. Both now on the card.
4. **Off-site content cut.** The card carried *"Elsewhere on the same project, a resettlement plan
   costing US$3.5 million was prepared and carried out for 333 people in 57 households affected by
   the construction of Mufuchani Bridge"*. The quotation is accurate to P071985's safeguards
   paragraph, but the Mufuchani bridge and its resettlement belong to **P106596** and are already a
   case on the map — `kitwe-mufuchani-bridge-relocation`, merged in round 31, which attributes them
   to Credit IDA-46540 under the Second Phase project. Mufuchani appears in P071985's completion
   report only in its safeguards section and safeguards table, and nowhere in its list of works.
   Printing it as "the same project" both duplicates an existing case and attributes the harm to the
   wrong credit. Cut, and left unreconciled below.
5. Road length corrected to give all three readings the documents give (see unreconciled figures).
Confirmed unchanged: ICR ratings Moderately Satisfactory outcome and Moderately Unsatisfactory
implementing agencies, read out of the ICR itself; Evaluation Group Moderately Unsatisfactory on
outcome, Bank and borrower; credit numbers as on the cover (IDA-38660, IDA-38661, IDPA-48210 — the
data sheet gives IDA-48210, and the card correctly says "the cover"); XDR 59.98 million disbursed;
closing 30 June 2014 against 30 June 2007; the three road agencies established in 2005; the
Chililabombwe council's Engineering Section as the body that relocated and valued.

### `kamuzu-barrage-liwonde-businesses` (P117617) — KEEP, three corrections
The ICR records the harm in its own words, in Annex 8: *"The operation's subprojects did not entail
physical relocation. However, there was economic displacement of 22 individual PAPs, 4 institutions
(ESCOM, Maritime Police Office, Liwonde Town Council and Liwonde National Park) and 32 Fishermen at
both the barrage and SRBA building."* Plus a grievance mechanism *"gauged as partially non-inclusive
to all PAPs because larger business owners did not use it"* and one grievance unresolved and in the
courts at closure. Table 39 of the February 2014 plan (RP1254 V3 REV, Volume 1 Main Report) checks
out item by item: Billy Mphande's complete closure with boat safari, bar, restaurants, 5 guest rooms
and 20 campsites; Steven Njovuyalema Moyo's reception building, bar, house, gate house, old
restaurant and loss of income; Felix Mwawa's 6 shops and dwelling house; Liwonde Town Assembly's
*"temporary loss of income from six business shelters for three years"*; the consultation sentence and
the valuation team's non-answer, verbatim.

1. **"Eight men" → eight people.** The plan lists them as tenants of the council's shelter and counts
   them elsewhere as *"eight households ... operating as shop owners selling meat"*. The card
   inferred gender from the names.
2. **Counter-clause added.** The completion report elsewhere says *"all grievances were amicably
   resolved except one grievance by a lodge owner which is currently in court"*. That both softens the
   grievance finding and identifies the one unresolved grievance, which is what links it to the 2026
   court claim in the outcome.
3. Financing: the card gave disbursement against the appraisal cost only; the revised cost of
   US$131.58 million added.
Confirmed unchanged: SDR 60.6m/US$93.75m credit and SDR 20.2m/US$31.25m grant, approval 14 June 2012,
effectiveness 7 September 2012, closing 31 January 2019, US$121.88m disbursed; GEF TF-12920 at
US$5.078m and LDCF TF-12921 at US$1.5m, both fully disbursed, filed under P127866; ICR ratings
Satisfactory, Satisfactory, Substantial off the ICR's own key-ratings block; the writer's
safeguard-count finding (ICR Annex 8: "six environment and social safeguard policies ... and two
legal safeguard policies"; Evaluation Group: "eight safeguard policies" — the same eight, counted
differently, and the card does not use either count). The 2015 and 2019 national flood death tolls
are correctly kept out of `killed`. Both non-Bank URLs on this card resolve (see routes).

### `mafinga-igawa-road-deaths-displacement` (P120370) — KEEP, `lenders[0].role` rewritten
The best-balanced card in the batch: the quotations are exact and the card volunteers every clause
that cuts the other way — the 0.06 against 0.11 fatalities per km per year, the slower speeds, the
road safety audit, and the borrower's dissent printed in the same report. `killed: 2` stands: *"Of
these, two were attributed to the contractors' employees or involved contractors' employees and/or
equipment, with the rest due to road crashes"* is a cause tying two deaths to the works, and the
credit paid for the road — *"accounting for the majority of project funds (78%), the rehabilitation
of the Mafinga – Igawa road segment (137.9 km)"*.

1. **What the credit financed was wrong.** Card: *"The project financed the rehabilitation of the
   corridor from Igawa to the Zambian border at Tunduma."* The report says the opposite of that: the
   project rehabilitated **Mafinga-Igawa**, and for the remaining portion to the border it financed
   only *"feasibility studies, detailed designs and environmental safeguards instruments"*. DANIDA
   paid for the sections above Mafinga. Corrected.
2. **A rating read out of the wrong document.** Card: *"The completion report ... records a safeguards
   rating of Moderately Unsatisfactory at closing."* The completion report's key ratings are Outcome
   Moderately Unsatisfactory, **Bank Performance Moderately Satisfactory**, M&E Modest, and it gives
   no safeguards rating anywhere. The safeguards rating is the Evaluation Group's: *"the project
   closed with moderately unsatisfactory rating for safeguards"*. Both ratings and both documents now
   named, including the disagreement on Bank performance.
3. Source title confirmed against the cover, not the archive: the document at the cited URL is the
   **Southern** Africa Trade and Transport Facilitation Program report, as the card says, even though
   the archive metadata and the Bank's own filename both call it "Eastern Africa". The writer got
   this right where the manifest would have misled.
Confirmed unchanged: approval 21 May 2013, effectiveness 26 Nov 2013, closing 31 Dec 2020,
US$175.4m disbursed, eight black spots with none fully addressed, 24-to-72-hour border crossing time,
the two safeguard failures at the border post and the black spot quoted verbatim, and the writer's
observation that the Evaluation Group's policy list prints OP/BP 4.12 twice (lines 796-797).

### `zanzibar-drainage-deaths-compensation` (P111155) — KEEP, one `lenders[0].role` cut
`killed: 5` stands and is the firmest death count in the batch: three accidents, each with a cause
tying it to the works, in the completion report's own words, and the report attributes all three to
*"weaknesses on the implementation of health and safety issues"*. The compensation findings are
exact, footnote 18 included — 605 compensated *"albeit with some delays"*, 167 more delayed and
incomplete, all but three paid by 1 April 2021 after the Bank released US$550,000, and the three
unreachable *"through radio, newspaper, village leaders, and so on"*. The plan figures are correctly
labelled as plan figures, and the plan-reprint check comes back clean: neither 605 nor 167 appears in
either resettlement plan in a resettlement sense (the only `167` in the plans is a banana count in a
crop table and a page number).

1. **One clause in the role is supported by nothing.** Card: *"the Evaluation Group records that the
   overall safeguards compliance rating went to unsatisfactory in March 2013 and stayed in the
   negative range."* The word "unsatisfactory" does not occur anywhere in the Evaluation Group's
   review. The nearest fact is in the **completion report's** own table of supervision reports: the
   development objective and implementation progress were both rated Moderately Unsatisfactory in the
   report archived **9 July 2013**, were back to Moderately Satisfactory by March 2014 and Satisfactory
   at closing. Four errors in one clause — wrong document, wrong noun, wrong date, wrong duration.
   Replaced with the ratings each document actually gives, including the ICR's Satisfactory against
   the review's Moderately Satisfactory on Bank performance.
Confirmed unchanged: SDR63.9 million on the cover, US$38m and US$55m credits, US$87.57m disbursed,
approval 24 February 2011, closing 31 May 2021 against an original 30 June 2016, the credit paying
compensation costs because the government could not and no land was available for swaps, and the
Evaluation Group's open-dumping finding verbatim.

### `morupule-b-family-moved-fatal-accidents` (P112516) — KEEP, five corrections
1. **`killed` 5 → 0.** The writer put the question itself and answered it correctly in the note: the
   completion report's footnote 4 counts five fatal **accidents**, not five people, and gives no
   number of people killed. A fatal-accident count is not a people count — Zanzibar's own three
   accidents produced five deaths. The causes and dates stay in `killed_note`, with the Global Energy
   Monitor "at least two" as a floor, uncounted.
2. **`displaced` 4 stands, but on a different document.** The card sourced it to the plan; the
   completion report carries it directly, and with a relocation verb: *"The resettlement of the single
   family of four began during project preparation and had been completed satisfactorily prior to the
   start of construction activities."* That passes the plan-reprint check — the figure appears in the
   plan, the appraisal document, the report and the review, and the report's verb is "resettlement ...
   completed", not "affected". `displaced_label` and `displaced_note` rewritten to cite the report and
   to print the plan-versus-report conflict on the date (below).
3. **A quotation that is not in the document.** Card: the October 2011 mission *"confirmed a serious
   lack of safety enforcement by the EPC contractor"*. The report says: *"The Bank mission in October
   2011 concluded that there was a serious lack of safety observance and enforcement at the site for
   which the main EPC contractor should take prime responsibility."* Replaced with the document's
   words.
4. **Which credit paid — the biggest correction on this card.** The role said only "IBRD loan 78010
   of US$136.4 million and an IBRD partial credit guarantee of US$242.7 million", which leaves a
   reader to assume the Bank's loan paid for the plant where the deaths happened. The report says
   otherwise: the loan was for *"the facilities associated with the power plant - water supply and
   transmission lines - and some technical assistance and capacity building activities"*, while the
   plant was built under an **US$825 million ICBC loan** that the guarantee supported by extending its
   repayment from 15 to 20 years. The report also records that the technology and the contractor
   *"were taken prior to the involvement of the World Bank"*, that the contract was signed in November
   2008 and construction began 29 April 2009, and that appraisal was completed in August 2009. The
   plant is still inside the Bank-appraised operation — the report calls it *"the central component of
   the project"* and the ICR is a joint report on the loan and the guarantee — so the case stands, but
   the card has to say which money built what. Note that the house demolished on the **transmission
   corridor**, the one harm here with an identifiable person attached, is on exactly the part the IBRD
   loan did pay for.
5. **`confidence` documented → contested.** The two harms in the title rest on the lender reporting on
   its own project: the family's move on the completion report and its own Group's review, and the
   Group adds that *"the project team confirmed a resettlement action plan was prepared and
   successfully implemented"* — a staff statement to the evaluators, which is not a document. The five
   accidents are the report's own count. Both outside sources were opened and both check out, but
   neither corroborates the title harms: the Mmegi article of 8 January 2016 is about the dismissal of
   thirty NEPEC 11 workers (card's `suppression`, accurate including Jia Zhu's denial and the never-
   conducted medical examinations), and Global Energy Monitor reports the deaths only as "reports",
   citing a Mmegi article of 30 July 2015 that nobody in this chain has read. The other reading, for
   the record: Mmegi is independent press corroborating a harm the card carries, which would support
   `documented`. The core-harm test decides it the other way.
Confirmed unchanged: the family's census detail (two huts of scrap, store, fence, about 2,000 m²,
three donkeys and a cart, firewood, mopane worms, the unplanted crops, the two plots 5-6 km from
Palapye, houses 3.4 m by 10 m, tents while building, the move set for 25 May 2009, no school, no
identity card); about 130 households impacted; the five accident dates and causes; the temporary
suspension of work at height, police deployment, safety firm and scaffolding contractor after the
third accident; "safety remained a serious concern throughout the project"; the fines and the noise
finding.

### `burundi-fibre-backbone-unpaid-compensation` (P094103) — KEEP, one date correction
The case stands on limb (b): compensation unpaid, counted, in an outcome document.
*"In the case of Burundi, compensations were paid in full for 8,265 people for a total amount of
Burundian Franc (BIF) 105,311,800 (equivalent of approximately US$67,000 in April 2015). 115 people
were yet to be paid compensation at project closure."* 115 counted people left unpaid is at least as
identifiable as Bukoba's five uncounted cases. The card is right not to divide the sum, right that no
document says what the 8,265 lost or why the 115 were unpaid, and right that the figures reach us
only through the Evaluation Group's review, which cites the completion report by page — the report is
not in the harvest for this project number.

1. **Wrong closing date for the component where the harm is.** The card said the project *"closed 31
   December 2016"* and set `end: 2016`. The review says: *"The project for Burundi closed 27 months
   behind schedule on October 31, 2014."* 31 December 2016 is Kenya's closing and the operation's. So
   "at project closure" in the 115 sentence means 31 October 2014. `end` → 2014 and the role now gives
   both dates.
Confirmed unchanged: grant IDA-H2830 estimated US$20.10m and US$20.60m disbursed; the three-country
grant estimate rising from US$164.50m to US$249.60m; borrower contribution US$37.40m estimated and
US$0.00 million delivered; nine level two restructurings; 1,254 km of cable, 34 communes, 58
government institutions and 14 universities; the January 2017 nationalisation *"without consultation
or compensation"*; Kenya needing no resettlement; Madagascar's US$56,941 and US$9,241.

### `p126579-eastern-electricity-highway` — already on the map, CONFIRMED, with a process note
The case exists and already carries this material. Round 31's own checked batch for this region
(`case-map-src/rounds/r31f_east_southern_africa_checked.json`) holds an `extend` record for
`ethiopia-kenya-power-line-kenya` adding the two fatal accidents, the livestock feed plant and the
mini-grid settlements from these same documents. **So this row was worked and closed in round 31 and
should not have been in the round 32 batch**; the batch builder handed it out twice. The writer spent
a row's worth of reading on it and reached the right answer. Nothing to merge.

---

## Figures left unreconciled, both sides given

1. **P071985, length of the Chingola-Kasumbalesa road rehabilitated.** 39 km in the completion
   report's results annex ("132.5 km ... includes 40.5 km of Luanshya-Kafulafuta; 39 km of Chingola –
   Kasumbalesa, and 53 of Lusaka-Chirundu"); **40.5 km** in the same report's outputs annex ("the
   rehabilitation works covered a total length of 40.5km"); **40 km** in the Evaluation Group's table.
   The card said 39 km alone. All three now on the card, attributed. No document reconciles them and
   neither does this log.
2. **P071985, number of traders.** 67 numbered rows in the plan's table, three names repeating; the
   plan's own text "roughly sixty-five (65)"; ICIJ's 67, which is the row count. Both on the card,
   neither counted.
3. **P071985, who financed the Mufuchani resettlement.** P071985's completion report lists the
   US$3.5 million Mufuchani RAP for 333 people in 57 households in its own safeguards section and
   safeguards table, while naming no Mufuchani works anywhere in its list of works; the map's
   existing case `kitwe-mufuchani-bridge-relocation` attributes the bridge and the resettlement to
   P106596, Credit IDA-46540, approved 16 October 2009. Left unreconciled; the sentence is off this
   card either way.
4. **P120370, deaths.** 24 in the Bank's text ("104 accidents ... 13 of which were fatal, accounting
   for 24 total fatalities"); **23** in the borrower's comments printed in the same report. Both on
   the card. Neither side explains the gap.
5. **P120370, Bank performance.** Moderately Satisfactory in the completion report's key ratings;
   Moderately Unsatisfactory in the Evaluation Group's review. Both now on the card.
6. **P111155, Bank performance.** Satisfactory in the completion report; Moderately Satisfactory in
   the review. Both now on the card.
7. **P112516, when the family moved.** The abbreviated plan of May 2009 says they were to be moved on
   25 May 2009; the completion report says the resettlement *"had been completed satisfactorily prior
   to the start of construction activities"*, and the same report dates the start of construction to
   29 April 2009. Both on the card, unreconciled.
8. **P112516, size of the family.** "one family of four is resident" in the plan's headline and in the
   report; five members in the plan's census table, the fifth living in Palapye and visiting. Both on
   the card; 4 counted, from the report.
9. **P069208, commissioning date** (July 2008 in the implementation section, August 2008 in the
   outputs annex of the same report). Noted by the writer, correct, and now irrelevant: the row is
   dropped.
10. **Invented conflict, none found.** Every conflict the writer reported was real on inspection. The
    writer's own list also declined to reconcile the Burundi per-person figure, which is the right
    call.

---

## Faults appearing on more than one card

1. **A relocation verb without a count or a loss read as satisfying the forward rule.** Four of the
   five cuts (P083325, P050440, P069208, P071407). The common shape: an outcome document that says
   people had to be, or were, relocated, inside a paragraph whose subject is compliance, with the
   numbers coming from a plan written beforehand.
2. **Quoted words that are not in the quoted document.** Three cards. P071985 ("major delays in
   implementing the Resettlement Action Plan" — the review says "delays", and "major" belongs to a
   different sentence in a different document); P112516 (the October 2011 mission "confirmed a serious
   lack of safety enforcement by the EPC contractor" — the report says "concluded that there was a
   serious lack of safety observance and enforcement at the site for which the main EPC contractor
   should take prime responsibility"); P075997 inside a drop reason ("was not completed by project
   close" is the review's phrase, attributed to the report).
3. **`lenders[0].role` carrying a statement from the wrong document.** Three of the six keeps —
   P120370 (safeguards rating), P111155 (an entire clause with no support anywhere), P112516 (what
   the loan paid for, by omission). The round 22 audit's mechanism — two copies of a fact, the nearer
   one goes in — is visible in all three. No kept card's role carries a safeguard-policy list, so
   that particular class did not arise in this batch; the writer checked the count sentences and
   reported them in the report rather than putting them on the cards, which is why.
4. **Research-process voice on the public card.** "No document opened records ...", "no document
   opened says ...", on six cards. It appears once in the whole current built map and not at all in
   round 31's checked batch, so it is a round 32 regression. Rewritten on the keeps as "No document
   records ...". "No independent report was found" is left: that is established house style in
   `confidence_note`, where it names who reported on whom.
5. **Content from one row appearing on another.** Once, but twice over: the Botswana family's
   never-schooled grandchildren and the man without an identity card were printed on the Uganda
   records-centre card as well. Both rows are in this batch, and the Botswana plan is where both facts
   are true. Worth a merge-time check across a batch's cards for shared sentences.

---

## Anything I could not check, by route

1. **P071407 `RP192 v3`, the aide memoire that might record what happened to Imusho after the move.**
   The writer's three findings are reproduced exactly here: `cache/P071407/RP_2007-07-03_8028352.txt`
   is 261 bytes and holds only "Public Disclosure Authorized" repeated with the document number, so
   the **Bank `/txt/` route** returns a stamp page for this document; the manifest records it as
   `route: cached, bytes: 261`, indistinguishable from a small success. I did not test the two routes
   the writer reports as failing — **`curl` to `documents1.worldbank.org`**, refused by this session's
   command classifier, and **the fetch tool on the same PDF**, which returned `PROVENANCE_REQUIRED`
   because the permission prompt went unanswered — because the task forbids re-fetching Bank
   documents. Neither is a host refusal and neither should be recorded as one. The row is dropped on
   the completion report, which is an outcome document, so the unread volume could only reopen it, not
   decide it. **A minimum-bytes check at harvest would have flagged this file**, and that is the one
   harvest change this check would ask for.
2. **P094103's completion report.** Not in the harvest for this project number; every figure on the
   Burundi card reaches us through the Evaluation Group's review, which cites the report by page.
   BRIEF31's route finding 2 says a `qterm` title search finds reports that `wds?projectid=` misses,
   so the writer's absence claim is correctly scoped to the route ("under this project number") but is
   not settled. Not tested here, for the same reason as above.
3. **Mmegi, 30 July 2015, "Morupule B environmental disaster".** The only outside report of deaths at
   Morupule B. Not read by the writer and not read here — Global Energy Monitor cites it without a
   URL. The GEM page itself was opened and does say what the card attributes to it, as "reports".
4. **The already-on-map claim for P126579** could not be checked against the live map: the build file
   in `case-map-src/D.json.gz` carries 173 cases, not the map's full set, and does not contain
   `ethiopia-kenya-power-line-kenya`. It was confirmed instead against round 31's checked batch, which
   extends that case with facts from these same documents.
5. **Routes that worked.** `gem.wiki` and `mmegi.bw` both answered on the first try through the
   ordinary fetch route. `ground.news` was not re-fetched; the card's handling of it is cautious and
   self-limiting, and the completion report independently identifies the one unresolved grievance as a
   lodge owner's, which is what the claim concerns.

---

## Did the briefs help the writer or mislead them?

Mostly help, and the writer's account of it holds up on inspection. The two decisive finds — Zanzibar's
five fatalities and Botswana's accident sentences — are quoted exactly as the documents have them, and
the writer verified them in context rather than taking the clause. The writer's report also names the
brief's real gap correctly: **a plan written after the move is an outcome document, and no pattern in
the brief looks for past-tense harm inside a plan.** Kasumbalesa, the strongest case here, turns on
*"had been resettled"* on page one of a resettlement plan, and the brief surfaced nothing from that
document but a table-of-contents line. Two further gaps worth the same note: the extraction reaches
sentences but not tables, and both Zambia's 67-name table and Malawi's Table 39 — the named-person
content that carries limb (b) on those two cards — had to be found by hand; and on a multi-country row
the brief does not say which country a candidate sentence belongs to, which on P094103 surfaced
Madagascar boilerplate and one Burundi sentence while the load-bearing fact sat in a bucket labelled
"CAUTION — null sentence".

Where it misled, the writer caught it: the P060005 brief flags the appraisal document as "filed as a
plan but reads as an outcome document; treat its figures as outcomes". It is dated five weeks before
approval and its figures are forecasts. Following that instruction would have produced a card out of
background prose — and it is worth saying that **the row dies anyway**, on its real outcome documents,
so the flag cost nothing here but should be removed before it costs something elsewhere.

One thing the brief got exactly right and the batch did not use hard enough: `relocation_counts_in_outcome_doc`
was `null` on all thirteen rows. That field, read before writing, is a warning that every case in the
batch has to be argued on limb (b) — and it is the fastest check a merge gate could run.
