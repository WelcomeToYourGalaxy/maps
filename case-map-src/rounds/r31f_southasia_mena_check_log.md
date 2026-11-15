# Check log — round 31, batch southasia_mena

Checked: `/home/claude/work/out/southasia_mena.json` (10 cases, 6 drops) and the writer's report.
Output: `/home/claude/work/out/southasia_mena_checked.json` — **9 cases, 7 drops.**

One case cut. Twenty-three source URLs were unusable as cited and all were replaced. Corrections
were made on eight of the ten cases, including two in `lenders[0].role` that were wrong on the
documents and one outcome sentence that no document supports.

Every figure on every kept card was looked up in the file on disk and read in its own paragraph.
Both cards the task named for particular attention were checked line by line and both survive, one
with its death count unchanged and one with its `documented` rating upheld after the independent
source was opened.

---

## The cut

### `dhaka-khal-rehabilitation-eviction` (P093988) — DROPPED

Deciding document: Implementation Completion and Results Report, 21 December 2016, footnote 23
(page 27), which is the whole of the card's harm:

> "In one of the khals eviction took place of an unknown number of people. A tracer study was
> expedited by DWASA. However due to the risk that these studies are incomplete, this khal was
> dropped. A total of seven khals were dropped due to complex resettlement issues."

Two clauses in that footnote decide it, and the second is the one the writer did not weigh.

1. **The people are not identifiable in any sense limb (b) allows.** No count, no canal, no date,
   no account of what became of them. The standing edge on this map is compensation unpaid in five
   identified resettlement cases at a named site, with the people neither named nor counted. An
   unknown number of people on an unnamed canal at an unknown date is thinner than that.
2. **The footnote's own next sentence is that the khal was dropped from the project.** So no
   document ties the eviction to works the credit paid for, and the footnote never says who evicted
   anyone or on what authority. Which credit paid for the works is the first of the two tests, and
   it fails here on the same sentence that supplies the harm.

The surrounding record cuts the same way. Paragraph 32 says no private land was acquired, that the
two pumping stations affected 221 households and the canal works 216 households, and that these
were adequately compensated; the review of 8 March 2017 does not mention the eviction at all. The
borrower's section calls the impacts on the 67 encroachers "negligible".

The card's coordinate compounded it: the point was Khilgaon, which is where a *different* incident
happened — a partial building demolition on the Khilgaon-Bashabo canal right of way, recorded in the
same paragraph as adequately resolved. The card would have plotted the wrong canal. The writer named
this its own weakest entry and said so plainly; that was the right call.

---

## Corrections, with both readings

### `iraq-expressway-worker-deaths-vendor-relocation` (P131550) — `killed: 3` UPHELD

The three deaths were tested one at a time, as instructed. Paragraph 74 of the completion report,
read whole:

> "On the contractor's side, regrettably, three worker fatalities were registered due to operational
> safety. The first was the driver of a pick-up van that collided with a parked vehicle. The second
> case was a supervising engineer who was run over by a project vehicle during site supervision
> works. The third case was a daily worker hit by a pick-up car while he was standing on the road.
> These tragic incidents were completely avoidable had higher levels of worker awareness, training,
> safety provisions, and close supervision been in place."

- **Which credit paid for the works**: all three are on the contractor's side of works the loan
  financed, and the report's own remedy sentence is about the project's worker training and site
  supervision. Test met for all three.
- **Whether a cause is stated**: collision with a parked vehicle; run over by a project vehicle
  during site supervision; hit by a pick-up car while standing on the road. A cause is stated for
  each. The first is the thinnest of the three — it gives the mechanism without placing it on a
  worksite — but it sits inside the report's own count of worker fatalities "due to operational
  safety". Test met for all three.

`killed` stays 3. **No death was moved to `killed_note` on this test**, and the two deaths that were
already in `killed_note` stay there: paragraph 73's "two unfortunate accidental deaths of two
members, the resident engineer and the contractor, between July 2017 and August 2018" gives no cause
at all, only that their reporting to the Bank was improper. Corrected: the card said those two were
"on the same two segments", which paragraph 73 does not say — in the report the two segments attach
to the measures to be adopted, not to where the deaths occurred. The review of 2 May 2024 does place
them "along these segments of the project", so the claim is now attributed to the review.

Other corrections on this card:
- **`lenders[0].role`, a date no cited document gives.** The card said "loan agreement signed 2
  March 2014". The agreement's own signature line in the text on disk reads "Dated 2 , 1 2014" —
  the month is lost in the extraction. 2 March 2014 is the Bank's filename. Date removed.
- **`place`.** "the Girsheen-Suheila section of the North-South corridor in Dohuk governorate".
  No document on disk puts Girsheen-Suheila in Dohuk; the only Dohuk reference is to Yazidi
  internally displaced people the project tried to employ. Changed to "in the north of the country".
- **Title.** "72 roadside shops" → "72 roadside shop owners". The document's unit is shop owners.
  A card once carried 147 shops in `displaced`; the distinction is the reason.
- **Suspension scope.** The card had the partial suspension without the document's own limit on it.
  Now reads as the report does: disbursement for the activities under the Roads and Bridges
  Directorate.

`displaced: 72` kept. The verb in paragraph 72 is "the resettlement of 72 shop owners ... to
dedicated serviced lay-bys", the unit bears people, the status column says Completed, and the review
repeats it. The plan-reprint call was made and is clear: the only other occurrences of 72 in this
project's resettlement plans are a table row number in a Babil column, not a count of vendors. The
paragraph is favourable throughout — a new idea for Iraq, the poorest segment benefited, increased
business — and the writer put all of that on the card, which is the right handling.

### `chobhar-dry-port-arrests-kathmandu` (P144335) — `documented` UPHELD

The independent source exists, is independent of the Bank, and says what the card says. The
Kathmandu Post of 18 January 2019 was fetched and reproduces: "Police arrested at least 54
protesters from the area where around 150 locals had gathered since Thursday morning"; the figure
attributed to Panchha Lal Maharjan, coordinator of the Chobhar Conservation Committee, exactly as
the card has it; the government's claim of 1,054 ropanis acquired, 228 for the dry port and 826 for
an exhibition centre; the 416 cement factory employees unpaid for 19 months; and the board's Rabi
Shankar Sainju saying the corporation's audit shows no employee liabilities but that the matter
would be taken to the Finance Ministry if genuine. A Nepali national daily reporting a police
action it attributes to a named local source is not the Bank reporting on itself. `documented`
stands.

Verified separately: "fifty-two locals were arbitrarily detained from the streets and their houses"
at paragraph 9 of the Request for Inspection of 25 April 2020; the withheld disbursements to
February 2020 at paragraph 18 of the Notice of Registration of 27 May 2020, where they are a
statement by Bank Management to the Panel and are attributed to the Bank on the card; the Panel's
site visit and its decision not to investigate at paragraph 55 of the completion report; approval
28 June 2013, effectiveness 10 September 2013, closing 30 November 2021 and the 23-month extension
at the restructuring of 23 December 2019, all from the report's own data sheet and paragraph 16.

**One correction.** The card attributed to "the project's environmental assessment" a statement that
all the dry port land is government-owned and no further acquisition, resettlement or compensation
was needed. That document is not on disk and is not among the card's sources; the sentence exists
here only as a quotation inside the Request for Inspection, at its paragraph 18, footnoted to "EIA
report, Pp xv". A real fact in the wrong document is still a sourcing failure. Now attributed to the
requesters' quotation of the draft assessment.

### `kabeli-transmission-line-compensation-arrears` (P112893)

- **`lenders[0].role`: wrong count of financed works.** The card said Component 1 paid for the line
  "and four substations". Paragraph 8 of the completion report: the component "consisted of the
  supply and construction of a 90 km 132 kV double circuit transmission line ... along with three
  new 132/33 kV substations in Godak, Phidim, and Amarpur areas". The fourth substation on the
  project, Damak, is recorded in the report's own output table as financed by the utility from its
  own resources. Corrected to three, with Damak named and its financing stated.
- **An outcome sentence no document supports.** The card said "The line's third section was put
  into service in August 2019." It is in neither Bank document — the report predates it — and the
  press source cited elsewhere on the card says only that the Kabeli corridor "finally assumed full
  shape in August", after twelve years, with no mention of a third section. Replaced with what the
  source says, attributed to it.
- **Arithmetic.** "Eighteen months after the project closed" for a report dated September 2018 on a
  project that closed 31 December 2016 → about twenty months.
- **A clause cutting the other way, restored.** The sentence immediately before Table 1 reads
  "There is good progress in compensation payment since the closing", and paragraph 30 ends
  "Overall, the Bank observed good progress in implementation of the safeguard activities". Both are
  now on the card beside the arrears.
- Press attribution tightened: the Kathmandu Post of 25 April 2016 says a stakeholder committee
  formed by 67 houses "in the area" dissented, and separately that the line was to pass through
  wards 4, 5, 7 and 9; the card had merged the two.

Confirmed unchanged: 188 of 228 for tower pads, 41 of 82 for structures, 673 of 1,339 for the
easement fee, with each stated reason for each gap, from Table 1, sourced in the report to "Kabeli
TL Project, August, 2018"; the 55 per cent and "social safeguards were partially implemented" from
the review; the unpaid resettlement assistance to residential owners and to non-titleholders with
the reasons given; the 3.8 km re-routing at Jorsal, Phidim and the sentence that there is no
community resistance there now; the 34.5 km of 90 km operational at closing. Plan-reprint call
made: none of 228, 82 or 1,339 appears in the project's resettlement plans or appraisal document.
Both press reports were fetched and match the card.

### `jordan-heritage-cities-house-shop-demolition` (P081823)

- **`lenders[0].role`: a figure read as a cost that is a budget line.** The card said land
  acquisition, expropriation and resettlement "cost US$7.60 million against US$5.86 million
  estimated at appraisal". Table 5 of the report shows 5.86 and 7.60 as the original and revised
  allocations for that line at the first restructuring; Annex 1(a) carries 7.60 as the actual or
  latest estimate against the 5.86 appraisal estimate, at 130 per cent. Table 10, separately, gives
  the resettlement cost as 4.18 million Jordanian dinars planned against 4.96 million actual, about
  US$5.9 million against US$7 million. The card now says which figure is which and where each
  comes from, and does not reconcile them, because no document does.
- **A clause the card omitted that cuts the other way.** The sentence introducing Table 9 is "The
  actual resettlement impacts were slightly smaller than the impacts documented in Resettlement
  Action Plans at appraisal stage." The card gave the plan-and-actual pairs but not the report's own
  summary of them. Added.
- Stray `displaced_label` removed (see the pattern section).

Table 9 was read line by line and every figure matches, including the town splits the card gives:
residential 2,505 Karak and 400 Jerash to a total of 2,905; commercial 1,555 Jerash and 195 Ajloun
to 1,750; land 2,681 Karak and 9,727 Ajloun to 12,408; households 6, 11, 17 and 12 to 46, Madaba
none. The counterweight the card carries is all real and was read in its own paragraph (paragraph
102): all affected people satisfied with the compensation and resettlement package, rates set on
market value reflecting replacement cost, renters eventually went back to improved and renovated
shops. The card is kept on the standing rule that housing actually demolished, in a table with a
separate commercial column, meets limb (b) without a count of people moved.

### `tripoli-tyre-heritage-market-relocation` (P116197 / P050529)

- **A possible plan reprint the writer cleared too quickly.** The card stated "280 vendors
  physically relocated into the new marketplace in Tripoli". Table 8 does mark that row Completed —
  but the figure 280 already appears in an August 2011 project document as "the revised RAP for the
  280 vendors at the Tripoli market". The card now records both and leaves it unreconciled. This
  does not touch `displaced: 71`, which comes from the two Khan el Askar rows.
- **`lenders[0].role`: allocations presented as spending.** The 17.9, 6.7 and 2.2 million are the
  additional financing's Bank-financing column in the appraisal-stage component table, not actual
  outlays. Rewritten as allocations, with the table named and the five cities named from the
  report's own list (Baalbeck, Byblos, Saida, Tripoli, Tyre).

`displaced: 71` kept. Table 8 gives "Khan el Askar block A and B in Tripoli / Physical relocation of
residents / 38 households with 209 persons / Completed" and "Khan el Askar block C in Tripoli /
Physical relocation of residents / 33 households with 124 persons / Completed". Two rows of one
table, same unit, same quarter, same verb, both Completed; summing them is arithmetic and the card
says so in `confidence_note`. The household unit is kept rather than converting to the 333 persons.

Verified in the Project Performance Assessment Report, each in its own paragraph: the market "looked
deserted" on a day that should have been busy and the vegetable and fruit sellers "were playing
cards because they had no customers" (3.9); "fewer permanent vendors than what had been arranged
through the resettlement action plan worked in the marketplace" (3.9); the compromise for 180 cars
against an actual 36 (3.14); the signatures of hundreds of vendors and two sit-ins (3.14);
"Residents of the historic souk houses denied being contacted before or during the work" and went to
engineers on site themselves (3.13). The favourable half of 3.13 — Tripoli souk vendors were
contacted before the works and adequately informed — is on the card. Also confirmed: 760
project-affected people, six plans, four implemented by closing, the Tripoli plan finished three
months after closure, the four-year halt from 2012 due to active shooting, the cancelled component
that left the 31-person shops plan unimplemented, and the 2017 Sustainable Development
Vice-Presidency award.

### `nagapattinam-canal-demolition-tsunami-rebuild` (P094513)

- **Half a review's finding.** The card said the Evaluation Group "rates the outcome Unsatisfactory
  against the revised objective". The review rates it Unsatisfactory against **both** the original
  and the revised objectives (its paragraphs on each). Corrected.
- **Coordinate did not match the card's own point text.** The point text says "Nagapattinam, the
  district headquarters"; the coordinate 10.6026 / 79.7619 is Nominatim's first hit for
  "Nagapattinam, Tamil Nadu", which is a district-level point about 20 km from the town. Moved to
  10.7648 / 79.8431, the town, which is what the text describes.

Paragraph 53 confirmed word for word, including the clauses after the demolition: retrofit measures
prepared and implemented once the Bank team learned of it, all six displaced families offered cash
grants, five paid at credit closing, the sixth in process. `displaced: 6` is right — an outcome
document, a people-bearing unit, and the document's own phrase is "All six displaced families".
Paragraph 52 confirmed for the 560 and 330 hectares, the 200 per cent government order, the 40
hectares donated and the statement that only state funds, not Bank funds, paid for that land.
The 100 host families exist as a displacement figure only in the review's sentence beginning
"According to the project team", and the card already keeps them out of `displaced` and labels them
a staff statement. That is the correct handling and it was verified in the review.

### `pakistan-earthquake-roads-compensation-arrears` (P099040 / P010556)

- **Arithmetic in `lenders[0].role`.** "seven weeks after the 8 October 2005 earthquake" for an
  approval on 1 December 2005 is 54 days. The week count is removed rather than corrected; the two
  dates are both on the card.
- **An inference beyond the document.** The card said "the delay in acquiring land ran far enough
  that the Bank considered suspending disbursement". The borrower's section says the acquisition
  "was delayed beyond proportion to the extent of risking the suspension of disbursement" — that the
  delay risked suspension, not that the Bank considered it. Rewritten in the document's own terms.
- **Two stray round keys removed.** The card carried `r20_outcome: case` and `r22_outcome: case` for
  a row the writer's own report lists as first worked in round 31, and the dedupe run found nothing
  for either P-number on the map. They assert prior-round outcomes that cannot be true and are
  dropped.

The candidate-parent link was re-verified independently, as the brief requires. The completion
report for P010556 records the first Additional Financing as a US$100.0 million loan, Ln. 7341-PK,
"approved on December 1, 2005", "for reconstruction and rehabilitation of three strategic roads of
national importance that were damaged by the earthquake of October 8, 2005", and the borrower's
section repeats the US$100 million. ICIJ's row for P099040 gives Pakistan, 1 December 2005, $100M.
Amount, date, country and component list all agree; the cover lists IBRD-73410. The link holds.

Paragraph 2.4.2(c) confirmed word for word: 1,007 kanals, Rs 108 million (US$1.1 million), Rs 76.5
million (US$0.78 million) at 72 per cent, Rs 31 million (US$0.32 million) outstanding, the four
reasons including the shamlat joint owners under US$100 unwilling to open a bank account, and
"the compensation amounts are already deposited and held in escrow accounts with the LRDs".
**Deposited and uncollected, not merely awarded** — the test the task set for this harm is met on
the document's own words. The 36 per cent of the unpaid balance is the review's own figure and the
review itself attributes it to the project team; the card attributes it the same way. The four
borrower findings are all on page 49 as cited, including "Utilization of funds by AJ&K government
for other purposes rather than disbursement to affected persons". Ratings read from each document
separately: report Satisfactory and social safeguards Moderately Satisfactory at its section 2.4.2;
review Moderately Satisfactory on modest efficiency due to significant cost overruns.

### `thimphu-land-pooling-compensation-arrears` (P090157)

- **A plan figure reported as an outcome.** The card said the Evaluation Group "records that title
  owners who agreed to the approach contributed 25 per cent of their land and were to receive
  compensation". The review's sentence cites page 66 of the **appraisal document**: it is the plan.
  Now attributed as the plan.
- `confidence_note` phrasing: "three named-as-three owners" → "three owners, counted but not named".

Footnote 22 confirmed word for word: "Only three AHPs are left to be paid, as they could not be
tracked despite repeated efforts; the compensation amounts have been retained in the Thromde
accounts section and are available for payment." Money retained and uncollected is what keeps this
card, and the stated reason is on it. Paragraph 68's list of losses, paragraph 67's Satisfactory
rating for social safeguard compliance, the grievance committee, the review's sentence that
compensation payments were made, and the 60 / 60 / 54 per cent beneficiary survey all confirmed.
Financing confirmed from the data sheet: IDA-47440 at 12,007,500, IDA-54310 at 17,400,000, 24.8
million of 29.4 million disbursed, approval 29 April 2010, effectiveness 24 August 2010, closing
31 December 2015 to 30 June 2019. This stays one of the two thinnest entries in the batch and would
be the next to go if the owner wants the batch smaller.

### `narayanghat-mugling-road-structures` (P144335)

- Verb tightened: "hit 131 private structures" → "affected", which is the completion report's word,
  in the title as well as the prose.
- Stray `displaced_label` removed.
- `displaced_note` extended with the plan figure the card should set against its silence: the 2013
  resettlement action plan says "Altogether 74 households come within the COI thus their houses will
  be dismantled as there is no space to shift their houses within the ROW. Hence all 74 households
  will be displaced." That is a plan in the future tense, the outcome document carries no
  displacement count at all, and the card now says both.

131 structures and 103 households confirmed at paragraph 53 of the report and in the review, which
prints the appraisal estimates of 80 and 74 beside them — so the outcome figure is not the
appraisal's reprinted. Paragraph 54 confirmed for the allowances paid, the one absentee household,
the 20 community structures reinstated and the 91 households under the vulnerable community plan.
Worth recording: the appraisal document's own count of 414 project-affected persons is the same
number as ICIJ's estimate for this project, and neither is used anywhere on either card.

---

## Every drop, re-opened

The brief's rule is that a drop whose whole reason is a null sentence from a plan is not a finished
drop. **None of the six is of that shape.** Each names an outcome document, quotes or closely
paraphrases it, and says what was found there. All six were re-read against the documents and all
six stand.

| Row | Outcome document checked | Verdict |
|---|---|---|
| P086414 India, Power System Development III | ICR 30 Jan 2012, Annex 2 substation table and the safeguards passage at pp. 9–11; ICRR 12 Nov 2012 | **Drop stands** |
| P113416 Egypt, Wind Power Development | ICR 30 May 2020 paragraphs 56–58 and 61; ICRR 4 Feb 2021 | **Drop stands** |
| P107847 Sri Lanka, Provincial Roads | ICR 28 Dec 2015 paragraphs 36–38 and the borrower's annex; ICRR 10 Jun 2016 | **Drop stands** |
| P128938 Kiribati, Pacific Aviation | ICR 19 Dec 2019 paragraph 58; ICRR 6 May 2020; social safeguards report 5 Dec 2013 §3.7 and its footnote 23 | **Drop stands** |
| P082510 India, Karnataka Urban Water | ICRR 12 Sep 2012 safeguards section (the report itself is not in the harvest) | **Drop stands** |
| P105404 Palestine, Southern West Bank Solid Waste | ICRR 22 May 2017 (the report itself is not in the harvest) | **Drop stands** |

Notes on the four where there was something to argue about:

- **P086414.** The Wardha row of the scheme table says what the drop reason says: 89.20 acres of
  Maharashtra Industrial Development Corporation land, "No land compensation was required to be paid
  to any Project Affected Families (PAFs) as land belonged to MIDC", plan completed March 2008, INR
  3.62 lakh of rehabilitation assistance distributed to all PAFs and vocational training at Krishi
  Kendra, Wardha. The three other substations are extensions with no plan, and the line schemes
  record "RAP was not required as this scheme involved only transmission lines". There were
  project-affected families at Wardha and no count of them anywhere, but also no recorded loss: the
  report's one evaluative sentence is that an external agency's impact assessment "has revealed an
  improvement of the socioeconomic status of a majority of the affected people". The writer's catch
  that the only people-bearing figures in the project's resettlement papers belong to the Solapur
  substation under a different operation was checked and is right.
- **P107847.** The harm the row does carry is paragraph 38's "access to residential properties and
  shops, damages to houses and boundary walls, basic amenities such as side drains and toilet
  structures", with no count against any of it and grievance mechanisms in every province. This is
  the same shape as a case this map keeps — cracked houses on a road — so it was calibrated against
  it: that case rests on 1,350 registered complaints, 429 of them for houses cracking from
  vibration, 518 validated for compensation, and 48 money claims unpaid with the amounts given.
  Sri Lanka has none of that, and the borrower's section says all project-affected people
  identified were provided mitigation measures. Drop stands.
- **P128938.** The land claim was the thing to test, because unpaid lease arrears at an airport is
  the shape of the map's weakest keep. The social safeguards report of 5 December 2013 says the
  dispute over the strip under the terminal and car park "moved through different levels of court
  to the High Court and is now resolved", and its footnote 23 says "the outcome to date is that the
  Government will be paying the lease including arrears to landowners" — arrears being paid, not
  withheld, on land taken during the Second World War, long before the project. The report of 19
  December 2019 lists the dwelling obstructing the obstacle limitation survey among the safeguards
  issues and says "All of these were resolved at the completion of the project", with no count and
  no date. Drop stands.
- **P082510.** The review's figure is "The total land acquisition for the project involved 8.41
  hectares affecting 215 families primarily in the Hubli-Dharwar and Gulbarga areas", with the plans
  "satisfactorily implemented and there were no complaints". Land area plus a count of "affected"
  people is the established rule's excluded case, and a road row was dropped on exactly that shape
  in an earlier round. ICIJ's 215 is this number to the person, which is itself the tell. Drop
  stands. The writer's identification of the only compliance statement on the environmental policy
  as a staff statement ("The project team subsequently informed IEG that the project was in
  compliance with OP 4.01") was checked and is correct.

---

## Figures left unreconciled

Given with both sides and no tidy resolution, because no document offers one.

1. **Iraq, traffic fatalities at closing, inside one document.** The completion report of 18
   December 2023 gives **23** in its text at paragraph 31 ("the three-year average of traffic
   fatalities for 2020–2023 along all segments totaled 23 per year") and **23.00** in its results
   annex, but **21** in the PDO indicator table in its own body (page 14: baseline 113, final target
   87, actual value at closing 21). One document, one indicator, two actual values. The card carries
   23, which two of the three places give, and now says the third gives 21.
2. **Iraq, number of deaths.** Paragraph 73 records two accidental deaths of "the resident engineer
   and the contractor" between July 2017 and August 2018; paragraph 74 records three worker
   fatalities with causes, one of them "a supervising engineer who was run over by a project
   vehicle". Whether the engineer of 73 is the engineer of 74 is stated nowhere, and the review
   repeats both passages without reconciling them. Not resolvable on these documents: `killed` is 3,
   the three with stated causes, and the two of paragraph 73 stay uncounted with who reported them.
   **The writer asked whether this could be resolved to 5. It cannot, on anything available here.**
3. **Chobhar, people detained on 17 January 2019.** Request for Inspection, 25 April 2020: "fifty-
   two locals were arbitrarily detained from the streets and their houses". The Kathmandu Post, 18
   January 2019: police arrested "at least 54", attributed to the Chobhar Conservation Committee's
   coordinator. Both on the card with who says which. The second is a floor, not a count, and is
   written as one.
4. **Tripoli, the 280 vendors.** Completion report Table 8: 280 vendors, physical relocation,
   "Completed at the time of the ICR". A project document of August 2011: "The revised RAP for the
   280 vendors at the Tripoli market". Whether the outcome figure is the plan's own is not
   determinable from either. Left unreconciled on the card.
5. **Dhaka, households affected by the canal works.** Main text and Annex 2: 216 households
   compensated along the khals (and 225 households receiving compensation, for a results-table total
   of 441 against a target of 500). Borrower's section, page 43: the improvements on the nine canals
   "as a whole, affected 187 persons/households, of which 67 were encroachers", whose impacts it
   calls negligible. One document, two counts, no explanation. Recorded here rather than on a card,
   because the card is cut.
6. **Jordan, the appraised land take.** Report Table 9: 20,332 m² planned. Review: "in comparison
   to the appraised 20,333m2". One square metre; recorded for completeness, not used.
7. **Jordan, the resettlement cost.** Annex 1(a): US$7.60 million actual or latest estimate against
   a US$5.86 million appraisal estimate for the land acquisition, expropriation and resettlement
   line. Table 10: 4.96 million Jordanian dinars actual against 4.18 million planned, which the
   report itself converts to about US$7 million against US$5.9 million. The two quantities are
   probably not the same scope, and no document says so, so they are left side by side rather than
   merged.
8. **Pakistan, the project's own approval date.** The completion report says "The project was
   approved on December 23, 2003" at its paragraph 1.7.1 and "approved on December 13, 2003" in
   footnote 19 to Annex 2. Neither is used on the card, which turns on the Additional Financing of
   1 December 2005, given consistently in three places.
9. **India tsunami, how many families were still unpaid.** The report says one family at credit
   closing; the review says "the Government of Tamil Nadu was still in the process of paying the
   grant to the displaced families", plural. The card follows the report, which is the document that
   counts them.

---

## Faults appearing on more than one card

1. **Every Bank source URL in the batch was a 404.** All 23 Bank entries used the form
   `https://documents1.worldbank.org/curated/en/docsearch/projects/<PID>`, which is not a document
   path and returns HTTP 404 with an HTML error page. The map's own convention, on 976 existing
   source entries, is `documents1.worldbank.org/curated/en/<id>/pdf/<name>.pdf`. The real URL for
   every cached document is in `harvest/manifest.json`, which the writer did not use. **All 23 were
   replaced from the manifest and all 18 distinct URLs were fetched and returned HTTP 200 with
   `application/pdf`.** Titles were taken from the manifest too, so each now matches what is at the
   URL. This is the single largest defect in the batch and it would have shipped a batch of
   unusable citations.
2. **`displaced_label` present with no `displaced` value**, on `narayanghat-mugling-road-structures`
   and `jordan-heritage-cities-house-shop-demolition`. Both labels said, in effect, "no count of
   people relocated appears" — which is `displaced_note`'s job. Both removed; the content is already
   in `displaced_note` on each card.
3. **A plan or appraisal statement carried as an outcome, through the review's paraphrase.** Bhutan
   (the 25 per cent land contribution, cited by the review to the appraisal document) and Tripoli
   (the 17.9 / 6.7 / 2.2 million component allocations, from the appraisal-stage table). Different
   cards, same mechanism: the review or the annex drops the tense and the figure reads as a result.
4. **`lenders[0].role` wrong on the documents, twice in ten cards** — Kabeli's four substations for
   three, and Jordan's budget line read as a cost — plus a date no cited document gives (Iraq's
   agreement signature), a half-reported review finding (India's Unsatisfactory against one
   objective instead of both), and one arithmetic slip (Pakistan's seven weeks for 54 days). Five
   defects across ten cards in the field the round-22 audit found errors in 19 of 46 cases. The
   pattern that audit named holds here: the field is written last, from a data sheet and a review
   table at once, and the nearer copy of a figure goes in.
5. **A specific claim with no document behind it, twice.** Kabeli's "third section was put into
   service in August 2019" and Iraq's "in Dohuk governorate". Both are the kind of detail that is
   probably true in the world and is in none of the cited files.

## Anything wrong in the card data outside the fields asked about

- The two stray round keys on the Pakistan card (`r20_outcome`, `r22_outcome`) asserting outcomes
  from rounds that never saw the row. Removed.
- The Nagapattinam coordinate, which was Nominatim's district-level hit while the card's `point`
  text described the town, about 20 km away. Moved to the town.
- The Dhaka coordinate, which pointed at the canal where a different and resolved incident
  happened. Moot now that the card is cut, but it is worth naming as a failure mode: a card whose
  site is unidentifiable will tend to acquire the nearest named site in the same document.
- Each kept card now carries a `check_note` recording what was verified and on which paragraph.

## What could not be checked, by route

- **Iraq, the two deaths of paragraph 73 against the three of paragraph 74.** No route exists. Both
  Bank documents print both passages; neither names a person, a date, a contractor or a section, so
  there is nothing to search on. **Route that failed: there is no document on either side that
  joins or separates them.** Left unreconciled, as above.
- **Iraq, independent corroboration of the three worker deaths.** Nothing to search on, for the same
  reason. **Route that failed: search, for want of a search term** — not a host refusal.
- **Lebanon, Bhutan, Jordan, Bangladesh, independent sources.** Not re-attempted beyond the
  writer's own searches; the kept cards are `contested` on that basis and say who is reporting on
  whom. **Route not attempted rather than failed.**
- **The Inspection Panel's Report and Recommendation on case 147.** Not fetched, by the writer or
  here. The Panel's decision not to investigate and its recommendation on consultation are taken
  from paragraph 55 of the completion report and from the review, both of which state them, so the
  card does not depend on it. **Route not attempted rather than failed.**
- **Indian audit route (`saiindia.gov.in/uploads/`).** Not opened. The one Indian case kept turns on
  a single district-level demolition that the report does not locate beyond the district and the
  canal's name; there is no searchable identifier to take to a state audit report. **Route not
  attempted, and named as such.**
- No host refused anything during this check. The three fetches that mattered — The Kathmandu Post
  twice and The Himalayan Times once — all returned the articles, as did all 18 replacement Bank
  URLs and both Inspection Panel PDFs over `curl`.

## Did the pre-extracted briefs help the writer or mislead them?

**They helped, and on this batch they did not mislead once.** The checkable claim — that every path
in every brief resolves to a readable file — holds: all documents named in the briefs for these 15
rows were on disk and readable, and nothing had to be re-fetched to check anything. Zero searches
were spent re-finding Bank documents at either stage.

What the briefs got right, verified:
- **The candidate-parent warning worked exactly as intended on the two rows that needed it.** Both
  candidates turned out to be correct, and in both cases the writer verified the link against the
  documents rather than the name — Pakistan by amount, approval date and loan number, Lebanon by a
  cover page printing both P-numbers. Neither card rests on a name match. This is the brief's own
  rule being followed rather than tested.
- **The staff-statement flag caught two real traps**, both confirmed here: Karnataka's only
  environmental-compliance statement, and the India tsunami row's 100 physically displaced families,
  which exist as a displacement figure only in "According to the project team". Both were handled
  correctly on the cards.
- **The plan-reprint check was cheap and all three flags cleared correctly**, which I re-verified
  independently for Iraq (72 occurs in the plans only as a table row number) and Kabeli (228, 82 and
  1,339 occur in no plan). But see the next section: the check as specified found nothing, while two
  real reprint risks in this batch were not flagged at all.

Candidate-sentence kinds that were noise, confirmed by reading them:
- **"replacement cost"** — fired on the entitlement-matrix recital in every resettlement framework,
  as the brief predicted. Not one hit was usable. On P099040's brief it returned the three-part
  compensation recital of a 2007 social assessment, which is boilerplate.
- **"police"** — never usable. The one real police action in the batch, the 54 arrests at Chobhar,
  is in no Bank document and no grep of the cache could have surfaced it.
- **"PLAN VERB — the reprint trap"** — the weakest category. On P099040 it returned the definition
  of a corridor-of-impact limit; on P113416, a sentence about procurement risk.
- **"affected, NOT a relocation count"** — correctly labelled, but on P086414 both hits came from a
  resettlement plan for the Solapur substation under a *different* operation. The brief had no way
  to know that, and it is the one place where a brief could have produced a wrong card. The writer
  caught it.

What the briefs should have surfaced and did not. The writer named footnotes and
post-closing compensation tables, and that is right and is confirmed: footnote 23 of the Dhaka
report, footnote 22 of the Bhutan report, footnote 23 of the Kiribati safeguards report, and
Kabeli's Table 1 sourced to August 2018, twenty months after closing, carry the whole harm on four
of the sixteen rows between them and not one of them appeared as a candidate sentence. Two more to
add from the checking side:

- **Plan-and-actual tables in the outcome document.** The brief's plan-reprint check looks for the
  same figure in two *different* documents. The sharpest material in this batch is the opposite
  shape: Jordan's Table 9 and the Narayanghat passage both print the appraisal estimate beside the
  outcome *inside one document*, which is what proves a figure is not a reprint. A pattern for
  table rows carrying two numbers under headers containing "planned"/"actual" or "appraisal
  estimate" would have surfaced the best-evidenced figures in the batch and would also catch the
  round-22 fault of a plan column sitting one column from the outcome.
- **The borrower's own section.** The writer named this too and it is worth seconding with a second
  instance: the Pakistan case's sharpest finding is on page 49 in the borrower's annex, and the
  Dhaka 187-against-216 conflict is on page 43 of the same. Both are outside every pattern the
  briefs ran.

## Named for the owner

Weakest kept entry: **`thimphu-land-pooling-compensation-arrears`** — three owners, counted but not
named, whose money is held and available, on a scheme the owners agreed to and which the report
rates Satisfactory. It is kept because money retained and uncollected is the harm the region's
pattern is about and the document says retained, not awarded. Second weakest:
**`jordan-heritage-cities-house-shop-demolition`**, where homes and shops were demolished and
nothing else went wrong; it is kept on an established rule rather than on a judgement.

Not merged. `build.py` not run. Nothing pushed.
