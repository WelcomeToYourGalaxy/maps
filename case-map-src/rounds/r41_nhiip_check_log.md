# Round 41, single-case pass — check log

One case, `nhiip-india-corridor-land-acquisition`. The writer promoted it from `contested` to
`documented`. **The promotion stands, with corrections.** I opened every document the entry relies on
and sixteen it does not, marked all six Patna High Court orders line by line for voice, and
re-verified every figure in the rewritten `community` field against the page it came from. Sixteen
corrections went in. Two of the writer's own fourteen corrections were wrong and are replaced; one was
wrong in a number and is fixed. Nothing was cut outright, but the entry's central claim about
financing after 2020 was reversed.

**A procedural defect first.** BRIEF40 requires `rounds/r41_nhiip_report.md`. There is no such file in
the repository. The task brief told me to read it. Round 40's batch A checker handed back without a
log and that is recorded as a defect; this is the writer's side of the same failure, and it cost me
the thing the brief says a checker most needs — the writer's own named weakest call. I had to find the
weak points myself, which is the whole reason the report is mandatory.

## 1. The financing link — every element confirmed, with three qualifications

The sentence under test was that the Bank's procurement plan of 9 June 2020 puts Birpur–Bihpur km 0 to
106 of NH-106 against loan IBRD-83010, prior review, US$101,671,942.50 actually contracted, under
implementation three months before the loan closed.

I downloaded the plan and read it with `pdftotext -layout`, then located every value by character
offset against the table headers rather than by eye. The row reads: `WBR 25 - Pkg NHIIP-BR-106-7 /
Rehabilitation and Upgrading to 2- lanes/2 - lane with Paved Shoulders Configuration and Strengthening
of Birpur - Bihpur Section (km0 to km 106.0) of NH-106 in the State of Bihar under Phase-I of National
Highways Inter-connectivity Improvement Projects`; Loan / Credit No. `IBRD / 83010`; Component `Road
Improvement and Maintenance`; Review Type `Prior`; Estimated Amount `0.00`; Actual Amount (US$)
`101,671,942.50`; Process Status `Under Implementation`. The documents API gives `docdt` 2020-06-09 and
the pdfurl the writer cited. The loan number is the one on the card. An Authority Engineer consultancy
for the same section, `NHIIP-BR-106-AE-07 2ND CALL`, sits on the same plan against the same loan,
prior review, with a contract completion date of 7 February 2025.

Three qualifications, all now on the card:

- **The row sits under the plan's `GOODS` heading, not `WORKS`.** `WORKS` begins at one point in the
  document and `GOODS` later; the NH-106 row is after `GOODS`. It describes road rehabilitation, so
  this is the Bank misfiling its own civil-works package, not a doubt about what the package is. But a
  writer who calls it "a works package" is describing the 2013 plan, not this one.
- **There is no signed-contract date.** The only date on the row, 9 November 2015, falls in the
  *Actual* cell of the *Bid Evaluation Report and Recommendation for Award* pair — the seventh of nine
  date pairs — and the *Signed Contract* pair is empty. The NH-30A row on the same page carries both a
  planned (2015-11-09) and an actual (2016-07-19) signing date and the status `Signed`. So "actually
  contracted" is a reading of the Actual Amount column plus the `Under Implementation` status, not of a
  recorded signature. It is a fair reading — a package cannot be under implementation without a
  contract, and the Patna High Court independently records the IL&FS agreement — but the card has to
  say which field it is standing on.
- **"Three months" is three months and three weeks.** Harmonised to "three and a half months", which
  is what the writer's own `community` field says.

I also tested the obvious attack on the document: its General section is stale, giving a Bank approval
date of 1 June 2017 and a period covered of June 2016 to December 2017. That does not sink the reading,
because the table carries contract completion dates of 16 August 2024 and 7 February 2025, so it is
regenerated from the procurement system at disclosure and the status fields are current at June 2020.

**Are the 2020 and the 2013 plans consistent accounts of the same package?** Yes, and the difference is
informative rather than troubling. The 2013 plan lists works package 12, "Rehabilitation and Upgarding
of Birpur - Bihpur Section of NH 106", Rs 435.89 crore, ICB, prequalification Yes, Prior, bid opening
07.03.2014, with a supervision consultancy at item 11 and a RAP implementation support agency at item
10 (that one Post review) for the same section. Rs 435.89 crore is a pre-bid *estimate*; US$101,671,942.50
is a post-award *actual*. The Rs 675 crore contract value the Patna High Court records is about 55 per
cent above the estimate, which the card did not say and now does. The writer's note that the
rupee–dollar correspondence is at the rate of the year of award and is not stated by any document is
correct and properly hedged (Rs 675 crore ÷ US$101,671,942.50 = 66.4 to the dollar).

## 2. The post-2020 transfer — settled, against the writer

**The writer's answer is wrong and it is the most consequential thing in this check.** The entry says
flatly: "The works were not paid for by a different operation", and reasons from (a) the Green
Corridors restructuring being July 2022 rather than 2020 and (b) no Green Corridors procurement plan
naming NH-106.

Four documents say otherwise, three of them the Bank's own and one Indian:

1. **NHIIP's completion report, paragraph 15:** in mid-2020 four large contracts in Bihar and Odisha
   were in trouble over contractors' cash flow, and "[g]iven the impending loan closing date of
   September 30, 2020, GoI and the Bank agreed to transfer the balance of NHIIP works" to the Green
   Corridors project. Paragraph 74: "at the time of loan closure the remaining activities of NHIIP were
   agreed to be transferred". Paragraph 22: of the 155 km of balance works, 102 km "had been completed
   under GNHCP" by 31 March 2022 — before that project's own restructuring was approved.
2. **The Independent Evaluation Group:** "The supervision of this safeguard policy related to the civil
   works transferred to and implemented under the Green National Highway Corridor Project continues
   under that project." The resettlement supervision for these works moved.
3. **The Comptroller and Auditor General's certificate on loan 8301-IN for 2020-21**, which the writer
   did not find: the year's gross expenditure of Rs 600.41 crore "includes expenditure incurred under
   NHIIP and balance activities of NHIIP transferred to GNHCP after restructuring approved by World
   Bank on July 06, 2022 **with retroactive effect**". Bihar is Rs 531.59 crore of that Rs 600.41
   crore, with Rs 28.66 crore disallowed.
4. **Arithmetic the writer had and did not use:** the completion report's own state table leaves Bihar
   151 km short at closing and West Bengal nothing, out of 155 km of balance works. NH-106 is a Bihar
   EPC contract, held by a contractor whose liquidity collapse is the stated reason for the transfer,
   and the Patna High Court has it at 95.31 per cent in April 2025. On the Bank's own account this road
   is among the transferred contracts.

The procurement-plan absence argument is also weaker than the writer makes it. I listed 22 Green
Corridors procurement plans from the API — the writer read six — and downloaded four, including all
three post-restructuring ones the writer skipped (7, 17 and 20 March 2025) plus 21 November 2023. Zero
hits for Birpur, Bihpur or NH-106 in any of them. But that absence is close to meaningless, because
transferred works are the continuation of contracts already procured under NHIIP and would not be
re-tendered; and the one NHIIP trace in those plans, a technical audit consultancy for "stretches
under GNHCP & NHIIP", points the other way.

**So does the card fail the Burkina test?** No, and the reason matters. In the Burkina airport platform
error and the São Paulo Line 5 drop the lender financed none of the thing that caused the harm. Here
the Bank's own procurement plan carries this exact package, by chainage, against this exact loan, under
its own prior review, with US$101,671,942.50 in the actual-amount column — and the acquisition, the
construction, the possession and the arbitral award of 16 July 2021 all fall inside the period that
loan financed. What changed in 2022 is who paid for the unfinished remainder. The card now says that,
and says that no document apportions NH-106 spending between the two loans by date. The writer replaced
round 40's open question with a wrong answer; I have replaced the wrong answer with the original
question, narrowed.

## 3. Findings versus pleadings — every record marked, and two more cut

Round 40 cut two claims on this card for quoting relief sought as though it were decided. The writer's
own correction 2 catches a third instance that round 40's checker got wrong, and I confirm it. But the
writer then made the same mistake twice more.

**CWJC 320 of 2019, order of 24 January 2023.** The court's own narration: the MoRTH–IL&FS agreement of
29 July 2016, commencement 3 October 2016, "the stipulated date for completion of the work as 2nd
October, 2019", the contract value of Rs 675 crore, the three sections over km 0 to 106, and the
revision of the completion date to July 2023. **The writer's first claim — that the court records in its
own voice that the works were due to finish on 2 October 2019 — is verified**, and independently again
in the order of 18 April 2025.

**The 60 structures — verified with a qualification, and one word cut.** The sentence is the court's
own: "Also, there are at least 60 structures (house, building, shops and religious structures), which
need to be removed and the site made available for construction of the project." No attributive tag. It
is separated from the attribution by the court's own aside, "Why such fact was not made known to the
authorities is not evident from the record", which shows the court treating it as a fact on the record.
But the paragraph above it opens "Today, we are informed by the principal contractor", so the source of
the figure is the contractor's statement adopted by the court, and the card now says so. More
seriously: the writer's `community` field read "recording sixty households, shops and places of
worship". The order counts *structures*, one of which category is "house". **Sixty structures is not
sixty households**, and the order gives no number of people or families. Cut.

**The order of 18 April 2025 — one finding kept, one cut.** Paragraphs 1 and 2 are the court's own:
respondent 7 "has undertaken the work of construction of NH-106 Birpur-Bihpur Section for 106
kilometers under Phase-I of the National Highways Interconnectivity Improvement Project", the work "was
to commence from 03.10.2016 and had to be completed by 02.10.2019", and "only 95.31% of the work has
been completed". Those stay. But the writer wrote that the Acting Chief Justice "described" the 103
kilometres as unusable for want of link roads, "creating protest among people living nearby and regular
commuters". Paragraph 5 reads: "Mr. Anjani Kumar, the learned AAG-4, on instructions, has pointed out
that in the absence of any link road or a makeshift diversion, even 103 kilometres road constructed by
respondent No. 7 is not being put to use, creating a groundswell of protest". **That is the State's
counsel on instructions, not the judge.** Re-attributed on the card and in `what_the_outside_source_settles`.

**CWJC 1694 of 2023, order of 28 March 2023 — one more cut.** Everything about the Commissioner's order
of 16.7.2021, memo 785 of 17.7.2021, the Rs 3,66,61,312 in the letter of 4.4.2022 and the authorities
"proceeding with the construction in question" without paying sits inside "It is submitted by the
learned Senior counsel appearing for the petitioner that". The court's own voice carries only the
status quo direction. The writer correctly attributed the figure and the non-payment to the petitioner's
case, but stated flatly, as the court's, that the Commissioner "directed that the Collector of
Madhepura take possession of her land only after the compensation had been calculated". **No court says
that.** Re-attributed.

**CWJC 13438 of 2024 — the writer's correction 2 is right and round 40's checker was wrong.**
Paragraphs 3 and 4 are "Learned Senior Advocate for the petitioner contended" and carry the award, the
execution order, the Rs 3,66,61,312 and "till date, the petitioner has not been accorded the award
amount". Paragraphs 6 and 7 are the court's own and carry the "hope and expectation" of compliance in
eight weeks and the direction to MoRTH and NHAI counsel to co-operate, "if the award holds the field
till date". Round 40's recommended ground for promotion — that these were recorded "as fact, not as
pleading" — does not exist. Respondent 5 is "The Nodal Officer, NHIIP, R.C.D., Bihar, Patna" and
respondent 10 the "Land Acquisition Officer cum Competent Authority N.H.- 106, Madhepura".

**C.Misc. 919 of 2024, order of 17 November 2025 — the keystone, and it holds.** Paragraph 1 is the
court's own recital of the orders under challenge: the execution order of 08.02.2024 of the Additional
District Judge III, Madhepura, in Execution Case No. 06 of 2023, "by which in execution of the award
dated 16.07.2021, passed by the learned Commissioner, Koshi Division cum Arbitrator in Arbitration Case
No. 31 of 2020, the petitioners herein have been directed to pay an amount of Rs. 3,66,61,312.00 … to
the respondent no. 1/awardee." Paragraph 4 is the court setting that order aside for want of
jurisdiction and sending the parties to the District Judge of Madhepura as Commercial Court. **The
award, its date, its case number, the amount and the execution order are the court's own words.** The
writer is right that this is where those facts stop being a party's account.

Three errors in the writer's handling of it, all corrected:

- **It was not "the state".** The applicant is the Executive Engineer, National Highway Division,
  Ministry of Road Transport and Highways, Madhepura Division, part-represented by Central Government
  counsel; the State of Bihar is respondent no. 2. The card said "the state" four times. The project
  authority litigating against the award is a different and stronger fact than the state doing so.
- **Miscellaneous Appeal No. 1 of 2022 is counsel's submission, and its subject is unstated.**
  Paragraph 3: "He further submits that he has also filed Miscellaneous Appeal No. 1 of 2022, which is
  also pending before the same Court". The order never says what it challenges. "The state's own
  Miscellaneous Appeal … against the award" is two inferences wearing a finding's clothes.
- **"More than four years after the award, the money has not been paid" has to go.** Nothing records
  non-payment after September 2024, and that record is counsel's. What survives: non-payment as at 8
  February 2024 follows from the execution order itself, which the High Court recites — an execution
  court does not order payment of an award that has been satisfied. Beyond that date the card now says
  the entitlement is back before a Commercial Court and the amount is in dispute, and no more.

## 4. Smt. Nutan's plot — the promotion survives the gap, and the card now says so

I read the resettlement plan in full. The village chainage table has the village at km 75+400 to 76+000
in Madhepura district and tehsil, spelled **"Mankipur"**; the common-property table has "Manikpur" at km
75.610, inside that range; the land schedule has Manikpur at 39,083 square metres, Rs 500 a square
metre, Rs 1,95,41,500. The chainage is corroborated twice and the variant spelling is a typing error,
which the card now notes so a later reader does not think the figure was invented. Kamalpur is at km
43+000 to 44+400 and Tola Kamalpur plots are in the owner schedule. **Neither "Nutan" nor "Arun" as her
husband's name occurs anywhere in the plan**; the only Nutan is the residential squatter at km 9+450,
Bhagwanpur, Supaul, so the writer's near-miss note is right. The Manikpur (Thana No. 62) schedule names
some fifty khesra numbers and other owners.

**The promotion survives.** The reason is that the gap is narrower than the failure CHECK40 item 2
guards against. That item forbids promoting a card whose link to the lender's money "runs through
geography alone", and asks whether a document names the loan and the parcels together. Here no single
document does — but the loan number is in the Bank's record against this package by chainage, the
project is in the court record in the court's own voice, the acquiring authority in the cause title is
the "Land Acquisition Officer cum Competent Authority, N.H.-106", and the "Nodal Officer, NHIIP" is a
respondent in her own writ. What is missing is one link in a four-link chain, and it is the link
between a plot and a chainage — not the link between the harm and the lender's operation. Round 40's
batch A let `documented` stand on the Assam card where the loan number appeared nowhere at all and the
project link rested on a respondent's name; holding this one to a stricter rule would be inconsistent.

**But the card had to say it, and it did not.** The writer conceded the gap in
`what_it_does_not_settle` and nowhere in the `community` field a reader of the map will see. I wrote
four sentences into that field: that no document places her plot on the financed kilometres; that what
is placed is her village at km 75+400 to 76+000, the acquiring authority and the project; that she is
absent from the plan's 2014 Manikpur owner schedule; and that a Madhepura address alone would place
nothing, because Madhepura also carries Package II land — the Lok Sabha speech asks for compensation
funds to be sent to the District Officer, Madhepura, for the km 124 to 136 stretch this loan did not
finance. **That is checker-written card text, and nobody checks it.** Flagged here as the brief
requires.

## 5. The fourteen corrections, spot-checked

Eleven hold. One is wrong in a number. Two are wrong.

| # | subject | result |
|---|---|---|
| 1 | km 0–136 split into Package I (0–106) and Package II (106–136) | **holds**, verbatim in the resettlement plan |
| 2 | CWJC 13438 of 2024 is counsel's narrative; 17 Nov 2025 is the court's recital | **holds**, both read line by line |
| 3 | execution order set aside 17 Nov 2025 for want of jurisdiction | **holds**; "the state" and "against the award" corrected |
| 4 | 9 June 2020 plan, IBRD-83010, prior review, US$101,671,942.50 | **holds**; GOODS table, empty signing field and the pre-bid-estimate point added |
| 5 | transfer approved 6 July 2022, not at closing in 2020 | **wrong as a conclusion** — replaced (see §2) |
| 6 | no Green Corridors plan names NH-106 | **holds on fact, overstated as evidence** — rewritten; six of 22 plans read, ten now |
| 7 | Green Corridors report says NHIIP "closed in September 2022"; the card says 30 September 2020 | **holds**; NHIIP's own Key Dates give Actual Closing 30-Sep-2020 |
| 8 | Inspection Panel, one request plus 28 more | **wrong in number** — the notice says "two Requests for Inspection, followed by 28 additional ones", thirty in all; fixed |
| 9 | claimants' villages in the loan's resettlement plan with chainages | **holds**; spelling variant noted |
| 10 | Nutan Devi the squatter at km 9+450 is a different person | **holds** |
| 11 | the Lok Sabha speech is about km 124–136, Package II | **holds**; read in the Hindi original |
| 12 | OP 4.10 not triggered on this road | **holds**, verbatim |
| 13 | "[P121885]" heading typo; the API returns one Birpur hit, projectid P121185 | **holds**, re-run |
| 14 | "All eight World Bank URLs in the round 40 entry point at documents.worldbank.org, which does not serve" | **wrong on both limbs** — replaced |

**Correction 14 in detail**, because CHECK40 says a correction that is itself wrong is worse than the
error it replaces. Round 40's entry has eight added sources, of which **six are Indian Kanoon and two
are World Bank**. And documents.worldbank.org **serves**: both of those two URLs return a 302 to the
https host and then to documents1, delivering the file with a 200 and the full byte count under `curl
-L`. The defensible point is narrower — the host redirects rather than serving directly, so a fetch
that does not follow redirects sees only a 302, and documents1 is the host to cite. The sources in this
round do use documents1, which is right; the stated reason was not.

## Four corrections of my own, added

- The 2020 plan's empty Signed Contract field, GOODS-table placement, zero estimate, and the 9 November
  2015 date falling in the bid-evaluation column.
- **Three Comptroller and Auditor General audits exist on this loan, not one.** The entry says "the only
  Indian state audit found" is the 2018-19 report. The Bank's P121185 list carries eight auditing
  documents; besides the one the writer read there are certificates for 2019-20 (disclosed 8 October
  2021) and 2020-21 (disclosed 9 November 2022), and the latter is the document that settles §2. All
  three give a clean opinion expressly "read with" observations set out in a Management Letter that the
  disclosed copies do not contain, and the covering letters say the observations not in the report are
  in that letter — so "unqualified" flatters them, which is the correction round 40's checker made to
  the Kenyan audit on this same map. The 2018-19 copy is a five-page scan extracting to about 810
  words, so the writer's word search of it for Birpur, land acquisition, Madhepura and Supaul is a
  poor-OCR negative, not an absence.
- The Mankipur/Manikpur spelling.
- **Two courts give different contract dates.** The Patna High Court puts the MoRTH–IL&FS agreement at
  29 July 2016; the Central Administrative Tribunal judgment of 10 September 2026, which round 40
  relied on, puts it at 27 September 2016, with the work order on 3 October 2016. Both give 3 October
  2016 and 2 October 2019 for commencement and completion. Round 41 switched silently from the
  tribunal's date to the High Court's.

Also added to `sources_add`: **CWJC 13438 of 2024**, which the card leans on in three places and the
writer listed in `documents_opened` but left out of the sources; and the **2020-21 audit certificate**.

## Writer-work I declined to do, named

Three facts are available, bear directly on this card, and are not written into it, because writing
them is the writer's call:

- The completion report says the five transferred roads "will be closely monitored for the completion
  of **pending RAP actions**" — the lender recording that resettlement actions were still outstanding on
  this corridor at closing, which is the card's harm in the lender's own words and better than the
  "substantially delayed" line the card already carries.
- The IEG says safeguard supervision for the transferred works moved to the Green Corridors project.
- **Madanpur, Madhepura** — the village in the Vijay Kumar pleading — is in the resettlement plan's own
  schedule of affected holdings as Thana No. 64. The writer placed Nutan's and Mishra's villages on the
  financed package and missed the third.

## One error of my own, recorded

I first concluded that the IEG quotation "were substantially delayed in several sections" and the
11,138 figure were absent from the IEG review, because I searched with a context-window regular
expression that required 80 characters on each side and the phrase sits near a line break. A plain
`grep -n` found both, in one sentence, exactly as the writer has them. The method was wrong and nearly
produced a false cut of a correct claim. Both uses of that document are accurate.

## What I did not do

Did not touch base.html, did not build, did not commit. **Zero WebSearch calls of the fifteen allowed**
— everything here came from the documents API, documents1.worldbank.org, cag.gov.in's documents as
disclosed by the Bank, and Indian Kanoon over plain curl. No route failed; `routes_that_failed` is
empty and that is a real empty, not an unattempted one. Twelve of the twenty-two Green Corridors
procurement plans and the five P121185 audits from 2016-17 to 2017-18 were not opened. **The most
valuable unread documents are the three Management Letters**, which are referred to in the audit
certificates, are not in the disclosed copies, and are the only Indian state-audit text that could
speak to compensation on this corridor. A disbursement record naming the package is still the one
document that would close the financing question outright; round 40's checker named that gap and it is
still open.
