# Check log — batch A (India, Pakistan, Bangladesh, Nepal, Sri Lanka)

Writer's file: `out_A.json` (10 cases, 2 dropped rows).
Corrected file: `checked_A.json` — **9 cases, 3 dropped.**

Every document was opened and grepped directly from the PDFs in `/home/claude/r19/dl`
(text extracted with `pdftotext -layout`), and the identity of all 26 batch-A PDFs was
confirmed from each file's own cover page (report number, project name, document type).
All 27 source URLs were re-fetched: all return HTTP 200 and the right PDF. Document
availability for the two missing completion reports was re-tested with three separate
queries against the Bank's archive.

---

## 1. Confidence values — all re-set to the map's two values

**Every one of the nine kept cases is `contested`.** Not one case in this batch has a
source outside the lender. The whole batch rests on the Bank's own completion reports,
the Independent Evaluation Group's reviews of those reports, the Bank's appraisal
documents and borrower-prepared resettlement plans disclosed by the Bank. Under the rule,
the Independent Evaluation Group reviews the report rather than going into the field, so
that is the lender reporting on its own project.

| case | writer had | set to | why |
|---|---|---|---|
| `ceip-polder-land-payments-bangladesh` | high | contested | ICR + IEG review of it + PAD. The 94 per cent figure is not in a document at all — the review attributes it to the Bank task team. |
| `lahore-walled-city-shop-removals` | high | contested | ICR + IEG review of it + the borrower's own Resettlement Action Plan, disclosed by the Bank. |
| `nepal-road-sector-unpaid-compensation` | medium | contested | The 24 unpaid households exist only in the Bank's completion report. |
| `swat-s3b-road-land-acquisition` | medium | contested | All figures are the implementing agency's, reported through the Bank's completion report; the review adds no resettlement detail. |
| `siddhirganj-pipeline-transmission-land` | high | contested | ICR + PAD only. No IEG review was opened and none was found. |
| `gujarat-highway-ii-delayed-compensation` | medium | contested | IEG review of an undisclosed completion report, plus the PAD. |
| `dehlon-bypass-uncompensated-landowner` | medium | contested | Same, and on the state of compensation it is the Bank's task team leader speaking to the evaluators, not a document. |
| `salem-tnudp-squatter-resettlement` | high | contested | ICR + IEG review of it. The impact evaluation survives only as the ICR's summary of it. |
| `assam-roads-uncompensated-acquisition` | medium | contested | ICR + IEG review of it; the closing statement that all compensation was paid is a project-team email to the evaluators. |

Each `confidence_note` was rewritten to say plainly who is reporting on whom.

---

## 2. The two entries the writer flagged

### `tudella-jaela-a3-culvert-complaint` — **CUT**

Resolved on the documents. It fails test 2 and both limbs of the forward rule.

**The sentence that decided it on test 2** — Inspection Panel, *Notice of Non-Registration*,
10 November 2014, under the heading "Panel's Determination":

> "The likelihood of harm from possible flooding potentially exacerbated by the Project, as
> alleged in the Request, is not occurring at this time."

Everything the requesters allege is forward-looking in the Panel's own rendering of it:
"may flood their properties", "the approximate number of properties likely to be impacted
is eight", "possibly lead to displacement". The one actual increase in flooding in the
record is attributed by Bank management to the requesters' own closure of the private
trench on 26 January 2014. The Court of Appeal injunction halts construction on the
property — harm prevented, not suffered.

**The sentence that decided limb (a)** — ICR3433, para 47:

> "no physical or economic displacement of persons or resettlement impacts were experienced
> by the Project"

**On limb (b) — the 4,000-plus complaints.** The brief told me to read that passage before
deciding, so here it is in full. It is **not** in the Bank's own text. It is Annex 7 Part 1,
"Borrower's ICR" — the Road Development Authority's own account, at its para 12:

> "RSAP received over 4000 complaints; all but two were resolved on site. More than 60
> percent of the public complaints **or requests** were related to house access, 25 percent
> to road access, and 10 percent to retaining and parapet walls."

A counted loss-of-access harm with no description is not enough for limb (b), and this is
not even that. Four things kill it:
1. It counts **complaints and requests**, not losses. The card had silently dropped "or
   requests" and written the count as complaints "concerned access to houses" — selective
   quotation of the kind the brief warns about.
2. "Over 4000" is a floor, not a count.
3. "All but two were resolved on site" — the document's own statement is that the access
   problems were fixed. The two unresolved ones are neither identified nor described.
4. Not one person's loss is described anywhere in the document.

So the remainder of the card is feared harm plus a grievance log. Cut, with the reason
recorded in the `reason` field.

### `swat-s3b-road-land-acquisition` — **KEPT**, limb (b) met

Every figure checked out to the word against ICR00003859 paras 27–31: 498 / 3.75 acres /
1.75 acres / 1,000 trees / 158 structures at the project-paper stage; 114 people, 1.6 acres,
74 trees, 24 structures in Phase I; 88 people, 4.5 acres, 731 trees, 23 structures in
Phase II; 12 people with "very small losses" in Phase III; 98 per cent compensated, the
remainder "absent and have not responded"; the five-month withdrawal of the Deputy Director
(E&R); "GoKP appears reluctant to devote staff and resources".

Limb (b) is met on land and assets actually taken: 1.6 acres acquired or reclaimed,
47 structures and 805 trees lost across two phases, from 214 counted people. "Land taken"
is an enumerated limb-(b) harm and this is a documented, counted taking, not a plan.
Corrections made:
- **214 is the writer's sum, not the report's.** The report gives 114 + 88 + 12 and no
  total. Now stated as a sum of the report's three figures.
- Added the counterweight the card omitted, from the report's own summary table: "Virtually
  all persons who lost property were compensated."
- Added the auditors' finding of "a high degree of compliance" across all three phases.

---

## 3. Specific checks the task set

### `killed: 2` on `dehlon-bypass-uncompensated-landowner` — **moved to `killed_note`, `killed` now 0**

The whole of the record is one sentence, in the Independent Evaluation Group's review
(ICRR0021189, p. 13):

> "The ICR reports (para 66) that there were two fatal workplace accidents in 2016 which
> were not reported to the Bank. The Bank's team learned about these accidents after a
> specific request was made to PRDB on February 2017."

- **Not reported to the Bank until it asked in February 2017: confirmed**, word for word
  (the document's "PRDB" is a typo for PRBDB).
- **On the financed works: not stated.** The document says "workplace accidents". It does
  not say the works were project-financed, which contractor's site they were on, where they
  were, when in 2016, or who died. The surrounding paragraphs are about this project's
  work-site safety management and the Bank's response was meetings with this project's
  contractors and board — but that is an inference, not the document's statement. The task's
  instruction was explicit: if the document does not place them on the financed works, they
  move. Moved, with the full reasoning in `killed_note`.
- The card title asserted "Two Deaths on the Punjab Road Works". Retitled to
  "Dehlon Bypass Built Over a Disputed Plot, Punjab".

The case still stands on limb (b) twice over: a co-owner's land built over and unpaid, and
drains sitting above plinth level "blocking numerous commercial and residential entrances"
(2009) — loss of access.

### The P090585 appraisal document's self-contradiction — **real, confirmed, and the card is right to use the main text**

Both readings are in report 37561-IN, *Project Appraisal Document, India Punjab State Road
Sector Project*, 10 November 2006:

- **Main text, para 72:** "On roads identified for upgrading during Phase I, 4,731 people
  from **1,233 households** will be affected, at least temporarily. However, only people
  from 197 households are expected to be displaced by the project."
- **Safeguards annex, para 10.9:** "On upgradation roads, 4,731 persons would be affected
  from **831 households** of which **1,233 would be displaced** from 197 households."

So the same document gives 1,233 as both a count of affected households and a count of
people displaced, and gives both 1,233 and 831 as the number of affected households. The
Independent Evaluation Group's review reads it the main-text way ("4,731 people from 1,233
households were expected be affected... only 197 households were expected to be displaced").
Confirmed that the card used only the main-text reading and labelled it as the appraisal
expectation. I have **added the annex's differing figures to the card and to
`displaced_note`**, named as the same document's own second reading, because the owner's
rule is to give both where documents disagree and not to pick for them.

### The two allegedly missing completion reports — **genuinely not disclosed**

The task asked for a `qterm` title search before accepting the absence. Three routes, all
negative:

1. `wds?projectid=P090585&rows=200` → 62 documents, no ICR. `projectid=P114827` → 118
   documents, no ICR. Both lists contain an "Implementation Completion Report Review" and
   nothing else of that family.
2. `qterm=Punjab+State+Road+Sector+Project&docty_exact=Implementation+Completion+and+Results+Report`
   → 2 results, both other projects (Tamil Nadu P050649, Pakistan PAF P049791). Same query
   for "Second Gujarat State Highway Project" → 1 result, the *first* Gujarat project
   (P010566, 2008).
3. Exact-phrase `qterm="Punjab State Road Sector"` across 62 hits and
   `qterm="Second Gujarat State Highway"` across 120 hits, filtered to any document type
   containing "Completion" → one hit each, the IEG review (ICRR0021189 and ICRR0022895).

Both `confidence_note`s now say so without researcher voice, and name how many documents
were searched. The Gujarat `outcome` field was also rewritten: "No Implementation Completion
and Results Report for this project is disclosed in the Bank's document archive."

---

## 4. Figures corrected, card by card

Confirmed-as-written items are not all relisted; everything below is a change.

**`ceip-polder-land-payments-bangladesh`** — 92.4% (ICR para 76), 94% (ICRR, task team,
June 2024), "no further update since June 2024", 269 complaints by 31 Dec 2023, 36 GRCs,
291 and 478 female-headed households, PAD's 6,203 households and persons from the
February 2012 census, US$12.69m forfeited (6.24 + 6.45), 311.84 + 25.00 = 336.84, scope cut
17→10 polders January 2020, US$24.26m cancelled 17 days before closing: **all confirmed to
the digit.** Corrected: SDR 18.2m → **18.223m** (the document's figure); "operation and
maintenance engineers" → **"executive engineers of the … O&M divisions"**; the
interim-government sentence re-attributed to **the Bank task team**, which is whom the review
attributes it to; the split rating re-attributed to **the Independent Evaluation Group** (the
ICR contains no split rating — the word appears only in the review); **added the counterweight
sentence** that opens the same paragraph as the 92.4 per cent: "By project close, the project
had made significant progress on land acquisition and compensation payments and no
construction was carried out until the process was complete."

**`lahore-walled-city-shop-removals`** — all RAP detail confirmed verbatim (147 including
sub-units, 84/22/18/10 ownership, 28/76/8/11/22 status, 50 and 61 income bands, 79 day
sellers / 10 khokhas / 2 tharas / 19 others, 53 employees, Rs 15,000 and Rs 6,000,
the 879→6,153 sentence, 371 people, 173 replacement shops), and the ICR's 147 / 264 / 732 and
"more than a thousand meetings".
- **Ratings error, the exact trap in the brief.** The card stated outcome and overall Bank
  performance "both rated Moderately Satisfactory, and risk to development outcome
  Significant" and cited **both** documents. Those are the review's ratings only. ICR3023's
  own data sheet: **Outcomes Satisfactory, Risk to Development Outcome Substantial, Bank
  Performance Satisfactory, Borrower Performance Satisfactory.** ICRR14661: **Outcome
  Moderately Satisfactory, Risk Significant, Overall Bank Performance Moderately
  Satisfactory, Borrower Performance Moderately Satisfactory, Quality of ICR
  Unsatisfactory.** Both now named with the document that gave each.
- **US$59.00 million at appraisal is unsupported.** The ICR financing table gives IBRD 50.00
  + borrower 8.90 = 58.90 appraisal, and 48.85 + 5.74 = 54.59 actual. Both of the card's
  totals were the writer's own sums. Replaced with the components as the table gives them.
- The same document gives disbursement as **48.85** (financing table) and **48.86** (data
  sheet). Both now stated.
- `displaced: 147` with `displaced_label` "shops removed completely" — **removed the numeric
  field.** 147 shops is not a count of people or households relocated, and the RAP states
  flatly: "No population/ person is going to be impacted due to impact on houses/residences."
  The 147 is kept in full in `community` and in `displaced_note`. **Lead's call to restore it
  if `displaced_label` is meant to carry non-person units** — flagging it rather than deciding
  for the owner, but an aggregate of `displaced` would otherwise count shops as people.
- Added that RAP sentence as the counterweight it is.
- Source title "ICR00003023" → **ICR3023**, the number on the document.

**`nepal-road-sector-unpaid-compensation`** — 91 households / 76 parcels / 48 structures,
24 households / 19 parcels / 11 structures, 22 deposited at district administration offices,
2 awaiting the Compensation Determining Committee and an escrow account, the FY2018-19
downgrade over the 5 per cent mobilisation advance, "Compliance with both social and
environmental safeguards policies were rated Moderately Satisfactory during the last
implementation support mission in November - December 2019", and the RAP's 73 households /
7 severely affected / 5 Dalit: **all confirmed verbatim.**
- **"Total project cost US$126,444,070" is wrong.** That is the Independent Evaluation
  Group's data-sheet label for what is in fact the Bank disbursement. The completion report's
  own table gives **Total Project Cost US$174,004,274**, including US$47,560,204 from the
  borrower. Both now stated, each with its document.
- Disbursement is **126,444,071** in the ICR table and **126,444,070.00** in the review's data
  sheet. ICR figure used.
- "US$42.6 million approved" now identified as **grant IDA-H3390**, with the five
  instruments' original total of US$172.6 million, which the card had omitted.
- "accounts for 115 project-affected households in total" — the report gives 91 and 24 and no
  total. Arithmetic now visible.
- `confidence_note`'s claim that the 73 "does not add to the 115" asserts a relationship no
  document states. Softened to: the 73 covers one road only and no document found explains
  how it relates to the 115.

**`swat-s3b-road-land-acquisition`** —
- **`killed_note` was sourced to the wrong project.** The card read: "Two suicide attacks
  occurred while the project was being implemented, according to the completion report."
  That sentence is **not in ICR00003859 or ICRR0020397**. It is in the **FATA** project's
  completion report (P128966, the dropped row): "incidents still occurred such as two suicide
  attacks while the project was being implemented". `killed_note` emptied, and the sentence
  moved to the FATA drop reason where it belongs. The writer's report repeats the error
  ("the two suicide attacks during the Swat road works").
- **Grant number.** Card had TF-10122. The ICR's data-sheet header and the review both say
  **TF-10112**; only the ICR's own key-dates table says TF-10122. Corrected, with the
  document's internal inconsistency recorded.
- **Ratings** split by document (see §6).
- **Place and point.** The card put the road as "Chakdara to Madyan". The financed 40.9 km is
  **Chakdara to Kanju**; Kanju–Madyan was USAID-funded, which the ICR states at para 600
  ("USAID funded the remaining section of S3-B (Madyan to Kanju)"). Place, point and
  `community` corrected, and the USAID section named so the reader is not misled.

**`siddhirganj-pipeline-transmission-land`** — 46.05 ha permanent and 85.00 ha temporary,
1,501 entitled persons, 93 structures, one poultry farm, one pond, 201 female-headed
households, mid-May 2012 handover, 72 families on the old route and 19 on the chosen one,
the non-compensation of private landowners, "over 20,000 Project-affected households",
the school and students' health, outcome Moderately Satisfactory and Bank performance
Satisfactory, and every credit figure (332,621,020 / 309,875,467 / 176,710,000 / 115,501,477 /
112,652,157 / 526,710,000 / 422,527,624 / 312,890,000 nil): **all confirmed to the digit.**
- "losing roughly 20 per cent **or more**" — the document says "losing approximately 20
  percent". "or more" removed.
- **The 30 October 2008 approval date is in neither cited document.** The ICR gives only the
  signing of the financing agreement on 13 November 2008 and effectiveness on 31 March 2009.
  The date is right — the Bank's projects API gives `boardapprovaldate 2008-10-30` — so the
  project record has been added as a source and the date labelled to it.
- 1,501 now quoted as the document has it, "entitled persons … affected by the Project", in
  the paragraph on gas pipeline resettlement; the card had narrowed it to "affected by the gas
  pipeline".
- The outcome rating is a split rating; now said so.

**`gujarat-highway-ii-delayed-compensation`** — 14.4 ha / 11.51 ha private, January 2017 and
February 2019 notifications, "two years", 730 households / 23 ha private / 7 ha government /
304 structures, three Scheduled Tribe households, the 23-month extension at the 13 September
2018 restructuring, US$158.50m and US$37.40m: **all confirmed.**
- **Wrong component.** The card said "Component B financed land acquisition and resettlement".
  Component B is **Sector Policy and Institutional Development**. The land acquisition and
  resettlement support sits in **Component A**, Highway Improvement, in both of its
  sub-components. Corrected.
- **Added, because it bears on the lender link:** the appraisal document states "All costs
  towards LA and R&R paid in cash would be met out of GoG funds", with Bank money covering the
  consultancies, goods and works for carrying out the resettlement plans.
- **Wrong corridors on the place and the point.** The card's place named "Eight road widening
  corridors … including Mehsana to Palanpur with the Mehsana bypass, Radhanpur to Chanasma and
  Vallabhipur to Ranghola", and the coordinate sat on Mahesana. Those three are the **three
  rehabilitation corridors added at the September 2018 restructuring**, not the eight widening
  corridors, and the land acquisition harm is on the eight. The documents opened do not name the
  eight. Place rewritten to say so, the three named in `community` as what they are, and the
  point moved to **Gandhinagar** (23.2232877, 72.6492267, OpenStreetMap city point, verified),
  the seat of the implementing department, with the point text saying the corridor is not named.
- **"a gap of about two years between the land being taken and the award of compensation being
  notified"** equates the statutory notification of acquisition with the land being taken. No
  document makes that step. Rewritten as the two notices and their dates.
- The appraisal figures are now labelled as appraisal expectations throughout.

**`salem-tnudp-squatter-resettlement`** — 65 squatter families into multi-storied apartments,
5 displaced families, 212 title and 337 non-title holders, INR 132.32m / US$2.20m / 8.5 per
cent, 110 sub-projects with 7 involving private land and 1 resettlement, 21 ha from 31
landowners, 45 ha government land including 23 acres of temple land, INR 30m at 0.73 per cent,
titles due December 2014 after a five-year stay, the impact evaluation's erratic water, top
floors without water, elderly and sick on higher floors, thefts and security, children still
at the old schools, 75 per cent satisfied with the compensation rate, 40 per cent of
compensation spent on houses, 16 of over 40 sites changed, closing 30 March 2011 → 31 March
2014: **all confirmed verbatim.** `displaced: 70` is sound — these are families actually
moved, which is a household count.
- **"The project was restructured in June 2009" is in no document.** The ICR's text says
  "First restructuring: August 2009" and "Second restructuring (Loan Extension): January
  2012"; its data sheet says 07/01/2009 and 02/07/2012. Both pairs now given, each attributed,
  and the second restructuring added.
- INR 191.21m: the extracted cost table carries both 191.20 and 191.21 in adjacent columns, so
  the card now gives INR 191.2 million against the appraisal estimate of 137.22.
- Loan "L4798" → **IBRD-47980**, as the document numbers it; effectiveness 19 October 2005
  added.

**`assam-roads-uncompensated-acquisition`** — the central sentence is confirmed exactly, ICR
para 66: "in one of the packages the project witnessed deviation from the agreements reached
under the RAP. The land and properties were acquired without paying compensation to the
owners. As a corrective measure, the work on the affected package was suspended till the
required processes were completed and the compensation funds were transferred." Also
confirmed: "Compensation, barring for one package, was largely paid on time" (para 48); the
utilisation certificates; the financial management downgrade to unsatisfactory for a year
after a two-year delay answering the Auditor General; OP 4.10 never applied; 978 km.
- **The card's absence claim is false.** It said "The Independent Evaluation Group's review of
  26 June 2020 does not mention the uncompensated acquisition at all." It does, on p. 15:
  "The ICR indicates (para 66) that most of the compensation, wherever applicable, was
  disbursed. However, there was one package where land and properties were acquired without
  compensation. The work on the affected package was suspended till the required processes
  were completed and the compensation funds were transferred." Corrected in `community`,
  `outcome` and `confidence_note`.
- **Added**, as the counterweight it is, what the review reports the project team said by
  email on 10 June 2020: that no designated staff was involved in land acquisition for the
  first three years, and that after the department strengthened its environment and social
  cell "all the compensation was fully paid, and all the land acquisition issues were
  amicably settled". That is staff telling the evaluators, and it is now labelled as such.
- **Three financing figures were wrong or mis-assigned.** The card gave loan IBRD-81360 a
  "revised commitment US$321,748,396.16" and "US$284,447,922.45 disbursed", with total project
  cost US$284,447,922.45. The ICR's own financing table gives the **loan** as 320,000,000
  original, 320,000,000 revised, **280,777,402 disbursed**; the loan and grant **together** as
  321,750,000 / 321,748,396 / **282,525,798**; and **Total Project Cost** as 401,750,000 at
  appraisal and **282,525,798** actual. 321,748,396.16 and 284,447,922.45 are the Independent
  Evaluation Group's data-sheet figures. All corrected, with both documents' figures named.

**Dropped rows (both drops upheld).** Haryana P110051: confirmed "Haryana State Industrial
and Infrastructure Development Corporation Ltd. acquired all the land (government land)",
INR 1,654,749,000, the three sub-projects dropped or moved after community agitation, and
that the ICR's "two accidents under the project due to negligence" states no death or injury.
Reason tightened to quote that phrase and to record the packages disagreement. FATA P128966:
confirmed agricultural-only land, no residential land, general satisfaction with a few
landowners wanting higher rates for inflation; the suicide-attacks sentence added here, where
the document puts it.

---

## 5. Voice and writing

No "I", "we", "my", "our", "card", "entry", "draft" or "writer" in any field of the corrected
file (the only "I" matches are "Phase I"). Three research-process phrases were in the writer's
`confidence_note`s and are gone: "so it could not be read directly" (Dehlon), "the completion
report itself was not found in the Bank's document list … so the account here rests on"
(Gujarat), "the one road-level resettlement plan opened here" survives only where it names
what the document is. Absence claims are now stated as facts about the archive, with the
number of documents searched, rather than as failures to find.

---

## 6. Where two documents disagree

1. **P083929 Lahore — the ratings.** ICR3023 (19 May 2014): Outcome **Satisfactory**, Risk to
   Development Outcome **Substantial**, Bank Performance **Satisfactory**, Borrower
   Performance **Satisfactory**. ICRR14661 (2 June 2015): Outcome **Moderately Satisfactory**,
   Risk **Significant**, Overall Bank Performance **Moderately Satisfactory**, Borrower
   Performance **Moderately Satisfactory**, Quality of ICR **Unsatisfactory**. The review's
   own "ICR" column also contradicts its own comment text: the column says the ICR rated Bank
   performance Moderately Satisfactory, while the comment beside it says "The ICR rates
   overall Bank performance as fully satisfactory in both the Data Sheet and on page 22".
2. **P096018 Assam — the loan and the project cost.** ICR00005164 financing table: loan
   revised **320,000,000**, disbursed **280,777,402**; loan + grant disbursed
   **282,525,798**; Total Project Cost actual **282,525,798** against 401,750,000 at
   appraisal. ICRR0022128 data sheet: revised IBRD commitment **321,748,396.16**, Total
   Project Cost **284,447,922.45**.
3. **P095977 Nepal — the total project cost.** ICR00005285: **US$174,004,274** (Bank
   126,444,071 + borrower 47,560,204). ICRR0022396 data sheet: **US$126,444,070.00** labelled
   "Total Project Cost". The same pair also differ by one dollar on Bank disbursement
   (126,444,071 against 126,444,070.00).
4. **P125584 Swat — approval and closing dates.** ICR00003859 data sheet: Phase I approval
   **23 August 2011**, last closing **31 October 2015**. ICRR0020397 data sheet: Bank approval
   **16 July 2011**, actual closing **12 December 2015**. The same pair differ on risk to
   development outcome: ICR **Significant**, review's table **Substantial** in both of its
   columns.
5. **P125584 Swat — the grant number.** ICR data-sheet header and the review: **TF-10112**.
   The ICR's own key-dates table: **TF-10122**.
6. **P090585 Punjab — one document against itself.** PAD 37561-IN main text para 72:
   4,731 people from **1,233 households** affected, people from 197 households displaced. Its
   safeguards annex para 10.9: 4,731 persons from **831 households**, of which **1,233 would
   be displaced** from 197 households.
7. **P083780 Salem — restructuring dates, one document against itself.** ICR00003125 text:
   "First restructuring: August 2009", "Second restructuring … January 2012". Its data sheet:
   **07/01/2009** and **02/07/2012**.
8. **P083929 Lahore — disbursement, one document against itself.** ICR3023 financing table
   **US$48.85 million**; its data sheet **USD 48.86M**.
9. **P083929 Lahore — the ICR's own date.** The document's data sheet gives ICR Date
   **05/15/2014**; the Bank's archive gives the document date as **2014-05-19**, which is what
   the card cites. Noted, not changed — every other card in the batch cites archive dates too.
10. **P110051 Haryana (dropped)** — packages needing resettlement plans: ICR "nearly 11",
    review "ten". Recorded in the drop reason.
11. **P086411 Sri Lanka (cut)** — second additional financing approval: the Panel notice's
    text "April 29, 2011", the Panel case page "04/12/2011", the projects API 2011-04-12.

---

## 7. Faults that appear in more than one card

1. **A rating or a figure attributed to two documents at once, or to the wrong one of the
   two.** Lahore (ratings), Swat (ratings), CEIP (the split rating, which is the review's
   alone). In each case the writer took the review's figure and cited both documents.
2. **The Independent Evaluation Group's data sheet mistaken for the completion report's
   financing table.** Nepal and Assam both carried the review's mislabelled "Total Project
   Cost" — which is in fact the Bank disbursement, not the project cost — as the project cost,
   and Assam also took the review's loan-plus-grant total as the loan's own revised commitment.
   The review's data sheets in this batch are unreliable on the financing rows and on dates;
   the completion report's own table should be preferred wherever it exists.
3. **The writer's own arithmetic presented as the document's count.** Swat's 214 (114+88+12),
   Nepal's 115 (91+24), Lahore's 54.59 and 59.00 (48.85+5.74 and 50.00+8.90, the latter
   wrong by 0.10). None of these totals is in any document. Three of the four are harmless
   sums; one was an error. All are now shown as sums of the document's own figures.
4. **Numbers reported to the evaluators rather than published in a document.** Four cases:
   CEIP's 94 per cent ("According to the World Bank Task team"), CEIP's interim-government
   change ("According to the World Bank Task Team"), Dehlon's "half of the co-owners have
   received compensation" ("The TTL informed IEG"), and Assam's "all the compensation was
   fully paid" (project team email, 10 June 2020). The writer attributed one of these four and
   presented the other three as the review's own findings. All four are now attributed.
5. **Selective quotation — the counterweight clause left out.** CEIP (the same paragraph opens
   "no construction was carried out until the process was complete"), Swat ("Virtually all
   persons who lost property were compensated"), Lahore (the RAP: "No population/ person is
   going to be impacted due to impact on houses/residences"), Dehlon (the plaintiff's no-show
   at the 31 January 2018 hearing), Sri Lanka (the dropped "or requests"). Five of ten cards.
6. **Absence claims not tested.** Assam's "the Independent Evaluation Group's review … does
   not mention the uncompensated acquisition at all" was false; the Gujarat and Punjab
   "no completion report exists" claims held up on three query routes each. The lesson is that
   the archive-level absences were checked and the within-document absence was not.

---

## 8. Things outside the fields I was asked to check

1. **`lenders[0].role`, Gujarat — the wrong component.** "Component B financed land
   acquisition and resettlement" — Component B is Sector Policy and Institutional Development.
   The support sits in Component A. Corrected.
2. **`lenders[0].role`, Swat — the wrong grant number** (TF-10122 for TF-10112), from the one
   place in the ICR that disagrees with itself. Corrected.
3. **`lenders[0].role`, Assam — three wrong financing figures** (see §4). Corrected.
4. **`lenders[0].role`, Nepal — "total project cost US$126,444,070"**, which is a Bank
   disbursement with the review's wrong label on it. Corrected.
5. **`lenders[0].role`, Salem — "restructured in June 2009"**, a date in no document.
   Corrected.
6. **`lenders[0].role`, Siddhirganj — an approval date in neither cited document.** Right
   date, no source. A source has been added for it.
7. **`place` and `point`, Gujarat — the coordinate was on the wrong road.** The three
   corridors named in `place` are the 2018 rehabilitation additions; the documented land
   acquisition is on the eight widening corridors, which the documents do not name. Point
   moved to Gandhinagar and the uncertainty stated in the point text.
8. **`place` and `point`, Swat — the road's extent was overstated** (Chakdara to Madyan is the
   whole 88 km road, of which USAID funded Kanju–Madyan). Corrected to Chakdara–Kanju.
9. **`companies` is empty on eight of nine cases.** Siddhirganj and Nepal name firms;
   everywhere else the contractors are in the documents but unnamed on the card. Not an error,
   but Assam, Punjab and Gujarat all turn on what a contractor did (a contractor went back
   onto the Dehlon plot after closing; a contractor's works took Assam land unpaid) and name
   nobody. Worth a pass if the owner wants `companies` populated.
10. **The writer's dedupe note is worth acting on.** It reports that the brief's grep gives a
    false positive on all 12 P-numbers because each sits inside an ICIJ `"dl"` / `"dpy"`
    reference array in `base.html` rather than in a case object. I did not re-run the dedupe —
    `base.html` was not in scope here — so this is relayed, not verified. If it is right, the
    dedupe step in the brief needs fixing before the next round.

---

## 9. What I could not check, and what stopped me

1. **The two completion reports for P090585 and P114827 do not exist publicly.** Three query
   routes confirm it. Everything on those two cards is the Independent Evaluation Group's
   paraphrase of a document the public cannot read, including the two fatal accidents and the
   Dehlon sequence. That is a hard limit, not a fetch failure.
2. **Whether the two 2016 fatal accidents were on project-financed works.** Only the
   undisclosed completion report's para 66 could settle it. Deaths left uncounted for that
   reason.
3. **Whether any of these harms was ever remedied.** Six of the nine cards end with the
   Bank's last document. No later Bank document, no national audit, no court record and no
   press report was found for any of them. Specifically unresolved: whether the Nepal 24 were
   paid; whether the Salem 65 got their titles in December 2014; whether the final 6 per cent
   of CEIP land payments was made; whether the Dehlon co-owner was ever paid; how many Assam
   owners there were.
4. **What the 92.4 and 94 per cent at CEIP are percentages of.** Neither document defines the
   denominator — value, parcels or households.
5. **No independent source exists for any case in this batch.** Not an archive problem: the
   search was the Bank's own document system, which by construction holds only the Bank's
   documents. If the owner wants any of these nine at `documented` rather than `contested`,
   someone has to go outside the Bank — Indian and Bangladeshi press, the Comptroller and
   Auditor General of India's state audit reports, Punjab and Gujarat High Court records. Three
   of these cards name a live court case or a specific district, which is where that search
   would start.
