# Check log — round 20, batch B (China transport, rail, water and rural), ICIJ tranche 4

Writer's file: `r26f_icij4_china_transport.json`, 11 cases, all `contested`.
Checked file: `r26f_icij4_china_transport_checked.json`, 11 cases, 0 dropped, 2 stripped of their
`displaced` field, 9 otherwise corrected or confirmed.

Documents read from `/home/claude/r20/cache/` as `pdftotext -layout` text: the ICR, the ICR Review
and the PAD of all twelve projects (36 documents, including the dropped P068752). Nothing was
re-fetched except the 33 World Bank PDFs named in `sources`, which were downloaded once to confirm
that each URL serves the document the citation claims.

---

## The four points the task named

### 1. `nanchang-line-2-demolition` — `displaced: 1344` removed, case kept on limb (b)

The ICR sentence is as the writer quoted it, verbatim (P132154 ICR, para 74): "Altogether 1344
urban families, 130 enterprises and 41 rural families were affected and 170,468.13m2 of land was
acquired." The next sentence is "Multiple mitigation measures such as cash compensation and
resettlement relocation housing were provided to the displaced families."

The ICR Review uses the same verb (P132154 ICRR, social safeguards section): "the project affected
1,344 urban families, 130 enterprises, and 41 rural families, and required the acquisition of
170,468.13m2 of land." So **no document attaches a relocation verb to the 1,344**, and the
"displaced families" of the following sentence is an unquantified set. Under the brief's rule the
field cannot hold it. `displaced` and `displaced_label` are removed and `displaced_note` now says
plainly that no document gives a relocation count and why.

**The case survives on limb (b).** The ICR records as completed facts, not plans: "the demolition
of private houses and concerned resettlement work was fully completed by August 2014 and the
enterprise structures by the end of 2017", and 170,468.13 m2 of land acquired. Houses demolished
and land taken are limb (b) harms, and they are outcome statements in a completion report. The
title has been rewritten to the demolition and the land acquisition rather than to families
"cleared from the corridor", and the `outcome` field no longer carries the writer's second
statement about the 73 per cent of families not recorded as gaining an improvement — the 27 per
cent figure stays once, in `community`, where the report puts it. Read for this: ICR paras 72–77
and the ICRR environmental and social safeguards section in full; nothing in either says anything
about the other families.

### 2. `yining-urban-roads-demolition` — kept, title corrected

Table 3 of the P126454 ICR is exactly as the card gives it: land acquisition planned 213 households
/ 980.75 mu, actual 166 / 525.52 mu; house demolition planned 648 households / 94,964.74 m2, actual
93 / 14,585.63 m2, both reductions marked "Reduction achieved from 'design optimization'". 93
households whose houses were demolished is an outcome figure in the lender's own planned-against-
actual table, so limb (a) is met.

The favourable material has **not** been dropped. ICR para 42 is reproduced on the card almost
clause by clause: compensation "timely at higher rates than indicated in the RAP", transition
payments for the temporary stay, incomes up RMB 1,412 per person 2010–2016, "94% of the PAPs were
satisfied ... and no substantive complaints were filed", EMDP implemented as planned, support and
training for women and poor families. The adverse clauses on the card (resettlement rated
moderately satisfactory around the mid-term review for slow site construction, delays to road
works) are in the same paragraph and in ICR paras 41 and 50. This is not selective quotation.

The evaluators' finding is real and is quoted accurately in `lenders[0].role` (P126454 ICRR, p.3):
"expenses for land acquisition are not mentioned in any of the three key documents (PAD, Loan
Agreement and ICR). The PAD (p.23) mentions that the equivalent of US$19.5 million had been
budgeted for compensation and resettlement, but this amount is not shown in any of the project cost
tables."

Two corrections:
- **Title.** "in a mostly Uygur city" is not supported. The ICR gives Yining as "Uygur 50 %, Han
  35%, Hui 7.5%, and Kazakh 4.5%"; the PAD gives "Uygurs account for 49.7 percent". The title now
  tracks the ICR's own sentence, "Most project beneficiaries and affected people belong to the
  Uygur ethnic minority".
- **"almost two thirds of Yining's population"** corrected to the PAD's own figures: ethnic
  minorities "about 65%", Uygurs 49.7 per cent. Note that the PAD's other "two thirds" on p.377 is
  about per capita GDP, which is the nearby-text hazard the brief warns about.

### 3. Wudu and Xining relocation counts — one stands, one does not

**Wudu stands.** P121414 ICR para 67: "Resettlement under the project included land acquisition and
population relocation caused by the construction of Jinfeng reservoir, the Xizi main canal, and the
branch and lateral canals in 14,408.04 mu (about 9.6 square km) of land acquisition and 3,449
relocated people in 992 households." The verb is "relocated", the figure is not in the PAD (whose
plan was 990 people in 264 households losing houses), so it is an outcome. The limb (a) limit on
hazard relocations does not bite: this is reservoir and canal construction with 14,408.04 mu of land
acquisition, so there is a loss on top of the move.

**Xining does not.** The writer's suspicion is right and stronger than stated. The P101829 ICR's
para 37 figures are the P101829 PAD's figures word for word, including the units:
- PAD (2009), three separate passages: "A total of 1,635.1 mu of collective land is to be acquired
  from 39 rural villages that will affect 3,549 farmers in 888 households. In addition, 538 people
  in 132 households will be relocated for their house demolition (among them, 313 people in 89
  households are affected by loss of both land and houses)."
- ICR (2016), para 37: "the acquisition of 1,635.1 mu (108.7 ha) of rural collective land in 39
  villages affecting 888 households comprising 3,549 people. Urban riverway management activities
  involved house demolition and affected 132 households (538 people)."

So the completion report repeats the plan and its own verb for the 132 households is "affected".
`displaced` and `displaced_label` are removed. The ICRR carries no count at all — grep for 132,
538, 888 and 3,549 in the ICRR returns nothing; the review only says a RAP was developed for
"resettlement needs in downtown Xining and Hangyuan County (land acquisition and house demolition)".

**The case is kept, narrowly, on limb (b)**, and I flag it as the one decision in this batch the
lead may want to overturn. What holds it up is that the completion report states in the past tense,
at closing, that the acquisition and the house demolition were carried out, and that the fifth
project component spent US$31.06 million of US$35.00 million on resettlement and environmental
management; land taken and houses demolished are limb (b) harms. What is weak is that every
magnitude on the card is an appraisal figure, and the ICR and ICRR record compensation satisfaction,
restored livelihoods and no grievance. If the lead applies the same line as the writer's own drop of
P068752 — only plan figures, nothing measured at completion, nothing adverse recorded — Xining goes
too. I kept it because, unlike P068752, the completion report does assert the acquisition and
demolition as things that happened, and the card now says on its face that the counts are the
appraisal document's repeated unchanged. Title, `outcome`, `displaced_note` and `confidence_note`
all rewritten to that effect, and `end` moved from 2016 to 2015, the closing year, since no harm is
documented after closing.

### 4. Tongliang — dates and the correction

Both halves check out, and the "only at loan closing" dating comes from the right place rather than
from the neighbouring sentence:
- Borrower's Annex 7, note 3 (P086446 ICR): "In Tongliang, due to the complicated procedures and
  land quota by the state government, land for the roads construction were initially compensated as
  per land lease. This was finally corrected per the Bank requirements and all villages/villagers
  were properly compensated for the land acquired according to Bank policies." The correction is
  recorded as made, and the card says so.
- The Bank's own supervision assessment, same ICR: "Some issues remained for a protracted period
  without properly being solved (such as the construction of Yubei Hospital which was delayed by
  more than four years, and resettlement issue in Tongliang, solved just at the loan closing
  although the works had been completed three years earlier)."
- Echoed in the ICRR: "Resettlement issue in Tongliang was solved at loan closing (ICR, p. 29)."

Loan closed 30 June 2017 (ICR data sheet: approval 03-Jun-2010, effectiveness 18-Oct-2010, MTR
22-Mar-2013, original closing 30-Jun-2016, actual closing 30-Jun-2017) — all as the card gives
them. `end` corrected from 2018 to 2017: the ICR's date is February 2018 but no harm is documented
after closing, and the rest of the batch uses the closing year unless harm runs on.

---

## The ten reported figure disagreements, each tested for quantity and date

**Real, same quantity, same date:**

1. **P086446 ICR body text against its own Annex 7 — real, and the sharpest thing in the batch.**
   I read both passages. Body text: "Actual resettlement impacts included 412.526 mu of permanently
   acquired land, which affected 593 households or 2,837 people, and 70 m2 of residential housing
   were demolished which affected seven houses and 25 people." Annex 7's table, which I reconciled
   row by row (Yongchun Roads, Tongliang Roads, Qijiang New Countryside, Chengkou water supply,
   Chengkou roads), is internally consistent and adds to: case-by-case acquisition 309.194 mu,
   permanent acquisition 322.526 mu, allocated by government 90 mu; house demolition 2,474.96 m2
   with 593 affected households and 2,387 project-affected people; and, in a separate column headed
   "Impacted Individual Enterprises", 7 enterprises covering 70 m2 with 25 project-affected people —
   all of them in the Yongchun Roads row. So the body text (a) takes the enterprise column's 7 / 70
   m2 / 25 people and reports it as seven *houses*, (b) drops the 2,474.96 m2 of house demolition
   entirely, understating it by a factor of 35, (c) prints 2,837 where the annex totals 2,387, and
   (d) gives 412.526 mu, which is the annex's permanent 322.526 plus the 90 allocated by government,
   omitting the 309.194 mu acquired case by case. The card's account of all four is accurate.
   The cost is given twice as the writer says: body "The original cost estimates (USD50 million) for
   land acquisition and resettlement were much lower than the actual (USD15 Million)" against Annex
   7 note 4, "the final costs for compensation was around USD20 million at the loan closing".
2. **P081348 Table 5.1 against Table 5.2 — real.** Same quantity, same date, same annex: Table 5.1
   and the body give 713 households and 2,834 affected people over 659.73 mu; Table 5.2's "Actual"
   column gives affected people 1,041 and permanent land acquisition 644.95 mu. The ICR's own
   admission is verbatim: "A final report on resettlement implementation was prepared, but there are
   inconsistencies in the data, which the PPMO has not been able to clarify." **I added the 644.95 /
   659.73 pair to the card — the writer had the people and the cost but missed the land.** Cost:
   body "RMB 97.67 million, but the final cost was much lower at about RMB 34.67 million" against
   Annex 5's "The updated cost is RMB36.47 million" — a second transposed pair in the same report.
3. **P122319 ICR against ICRR on ratings — real, and correctly attributed on the card.** ICR data
   sheet: Outcome Satisfactory, Bank Performance Satisfactory, M&E Modest. ICRR ratings table:
   Outcome Moderately Unsatisfactory, Bank Performance Moderately Satisfactory, M&E Modest, with the
   reasons printed. The ICRR's ICR column is right about the ICR in every row, so no rating is read
   out of the wrong document.
4. **P122319 PAD main text against PAD safeguards annex — real but small.** Main text "approximately
   7,500 persons ... approximately 3,600 people from 1,078 households will be relocated"; annex
   "approximately 7,511 persons ... approximately 3,631 people from 1,078 households will be
   relocated. In addition, the project will affect 1,763 people from 34 enterprises." Both are
   appraisal estimates of the same thing, both hedged "approximately".
9. **P071094 cover against data sheet on trust funds — real.** Cover: "(IBRD-73100 TF-54747
   TF-55699)". Data sheet: "54949, TF-70354". The body text names TF54949 and TF70354 as the DFID
   grants, so the data sheet's pair is the one the report uses. Both are in the lender role; fine.
10. **Cover dates against data-sheet dates — real.** P081348: cover 24 December 2013, data sheet
    "ICR Date: 11/14/2013". P075602: cover 15 August 2008, data sheet 08/17/2008. Cards use the
    cover date, as the brief requires. The same mismatch exists on **P101829, which the writer did
    not record**: cover 9 June 2016, data sheet "ICR Date: 05/25/2016". The card uses 9 June 2016,
    so the citation is right; only the completeness of the note differs.

**Not disagreements — appraisal against outcome, i.e. before-and-after:**

5. **P121414 PAD against ICR.** PAD: 990 people in 264 households "will lose their houses" (plan,
   January 2012). ICR: 3,449 relocated people in 992 households (outcome, November 2020). Different
   dates and, strictly, different quantities (houses lost at appraisal against people relocated at
   completion). The card's wording "Neither Bank document explains why the number relocated came out
   at 3,449 ... against an appraisal figure of 990" put an unexplained-gap claim on a before-and-
   after; **corrected to state both figures and that neither document compares them.** Same
   correction made to `confidence_note`.
6. **P132154 PAD against ICR.** Same shape: 1,043 families / 4,001 people / 83,817 m2 at appraisal
   against 1,344 urban families / 41 rural families / 130 enterprises / 170,468.13 m2 at completion.
   PAD figures confirmed verbatim. **The "documents do not explain the gap" sentence corrected the
   same way.** The RAP cost US$193 million at appraisal against US$514 million actual is the ICR's
   own comparison, in one sentence of one document, and stands.
8. **P075602 "internal tension" — not a conflict at all.** The ICRR's shortcoming is that the ICR
   "does not discuss the number of **people** resettled"; Annex 2 of the ICR gives **families**
   (7,573 against 2,666 planned). Both statements are true and compatible. The card already draws
   that distinction correctly ("although Annex 2 of the report gives the number of families"), so
   nothing needed changing on the card; the report's list is what overstates it.

**One of the three label substitutions is the same rating reworded:**

7. Verified each against the ICR itself, not against the ICRR's ICR column:
   - **P081348 — real.** ICR data sheet: "Risk to Development Outcome: Substantial". ICRR table
     prints "Significant" in both the ICR column and the IEG column. Card correct.
   - **P101829 — real.** ICR data sheet "Risk to Development Outcome: Moderate" and body section 4
     "the overall risk to development outcome is rated Moderate". ICRR table and rating line print
     "Modest" in both columns. Card correct.
   - **P075602 — not a substitution of substance.** ICR: "Low or Negligible". ICRR: "Negligible to
     Low" in both columns. That is the same rating with its two words reversed, not a different
     rating. **Removed from the Zhe-Gan lender role**, which was presenting it as a discrepancy; the
     ICRR number ICRR13032 is given there instead. The P081348 sub-point about borrower performance
     is also not a contradiction: the ICRR downgrades borrower performance to Unsatisfactory and its
     "Government Performance Rating" line says Unsatisfactory, which agrees rather than conflicts.
     Nothing of it is on the card.

---

## ICIJ figures: two claimed matches and nine claimed absences

Both matches confirmed in the document named, not in a quotation of it:
- **P111421, 5,480.** PAD: "The project will affect 5,480 people"; "The 5,480 persons to be
  displaced belong to 1,463 families (average size 3.5 persons)"; and 5,480 as the 100 per cent row
  of the resettlement annex's table. The card's description of it as ICIJ's project-affected count
  is right.
- **P121414, 3,848.** PAD: "About 3,848 farmers in 1,063 households will be affected", repeated in
  the safeguards annex as "A total of 3848 farmers in 1,063 households".

The nine absence claims are a task, so I did the task rather than spot-checking three. I grepped
every one of the nine figures, in both comma and plain forms, across all three cached documents of
its project (27 documents): P122319 5,748; P132154 5,058; P081348 3,995; P101829 3,840; P126454
3,552; P075602 5,277; P118647 3,140; P086446 2,912; P071094 2,791. **Zero hits anywhere.** The
claim is sound, and the cards state it in the limited form the evidence supports — "no figure
matching X appears in the documents opened" — which matters, because no resettlement action plan
was downloaded and ICIJ drew mainly on those. All eleven ICIJ figures on the cards match
`leads_b_china_transport.json` exactly.

---

## The Guangxi written-agreement finding

Whose sentence and which document: it is the **Bank's own safeguards specialist**, recorded in the
**P071094 ICR, section 2.4.4** — not in the PAD and not an IEG finding. The sentence is quoted
accurately: "the Bank's safeguards specialist noted that agreement in writing was not always
reached in advance with the PAPs when it was necessary to take their land in order to complete
project civil works, and that compensation standards should be (a) adequately discussed with and
supported by the PAPs, and (b) in line with the local government regulations." The ICRR restates it
at p.598–601 in the words the card attributes to it.

The sentences that cut the other way are in the same section and the one before it, and all of them
are already on the card: "Project land acquisition activities in Guangxi were carried out to the
satisfaction of the affected people through participatory approaches"; "Most of the land needed for
the village-level infrastructure works was voluntarily provided"; "their income levels increased by
at least 50% during 2004-10 on average"; "All land acquisition was generally done in accordance
with Chinese regulations and Bank policies". Nothing favourable was withheld.

Three corrections:
- **A factual error in `companies[0].role`.** The card said the provincial and county offices took
  corrective action "after procurement problems were found in Luocheng County". The ICR says the
  April 2007 fourth supervision mission "found extreme deficiencies in institutional capacity in
  Luocheng County in Guangxi"; the procurement problems in this ICR are in **Yunnan** (no approved
  procurement plans in the Yunnan county PMOs, contract administration in Menglian County).
  Corrected to institutional capacity, with the mission and date.
- **A characterisation the document does not make.** "The report also records the pressure that
  made the land easier to obtain" — the ICR's sentence is about the participatory approach, early
  advance notice and community mobilisation making land requisition "much easier, lower cost, and
  more efficient", and villagers volunteering land. "Pressure" is the writer's word for the Bank's
  favourable finding. Rewritten to what the report says.
- **An absence claim tightened.** "No document found records what compensation those households
  finally received" → "Neither Bank document states what compensation those households received."
  I read every occurrence of "compensat" in the ICR (two: the safeguards specialist's sentence and
  an unrelated travel-cost line) and in the ICRR (four, all in the land-acquisition paragraph).
  There is no compensation figure for Guangxi in either.

The case passes limb (b): over 8,000 households in Guangxi lost about 3,000 mu of land, stated as
an outcome in the completion report, and land taken is a limb (b) harm.

---

## Everything else, case by case

- **zhanghu-railway-resettlement — confirmed, one figure added.** ICR paras 58–61 confirm every
  number on the card verbatim: 14,867 mu, 57 per cent farmland, 7,416 households, 116 villages, 10
  counties/districts, 29 townships, 396,969 m2 demolished and "relocation of 1,446 HHs" (relocation
  verb, so `displaced: 1446` stands), 168 enterprises with 1,879 employees, 6,717 mu temporary and
  restored, RMB 2,156 million / US$317 million paid in Inner Mongolia, 96 per cent of RMB 1,664
  million / US$245 million in Hebei, 97 per cent overall, RMB 67 million outstanding, the
  Zhangjiakou Bank borrowing of RMB 30 million each by Wanquan District and Huai'an County, the
  letter of commitment from Zhangjiakou Transport Investment Company, the three households with
  ~100 m2 apartments retained and houses elsewhere, the three enterprises and two lawsuits, the
  escrow. The staff statement is attributed as a statement, and it is the only one used in the
  batch: ICRR, "discussion with the Bank task team showed that they are still following up with the
  Borrower on the outstanding resettlement compensation payments". **Added:** the ICR gives the
  funding shortage as RMB 57 million in the sentence that introduces the two reasons and RMB 56
  million in the bullet below it; the card had only the 56.
- **luan-huaibei-urban-transport-resettlement — confirmed, nothing changed.** ICR para 58 carries
  473 (68 Huaibei, 405 Lu'an) at closing, 68 and 284 resettled by December 2018, 121 outstanding in
  Lu'an, 65 expected August 2019 and 56 in 2020, the cause (delay in Lu'an's large-scale
  resettlement housing, shared with other domestic projects), and every favourable clause the card
  carries, in the same paragraph: transition subsidy in conformity with local policy, compensation
  timely, "transitional supports were doubly paid due to extensions of the transitional period",
  subsidy "well sufficient to pay rental for the similar housing to their original property",
  quarterly monitoring, continued Bank monitoring under P153173. PAD confirms 2,060 mu / 137 ha /
  15 villages / 11 townships / rice two-fifths. Cancelled Tuohe depot and 146 of 248 bus bays
  confirmed. The 473 were out of their homes and in transitional housing, so limb (a) is met and
  the prolonged wait is the loss on top of the move.
- **zhegan-line-railway-resettlement — confirmed.** Annex 2 of the ICR prints the planned and actual
  columns side by side: land acquisition 26,668 mu planned / 31,800 mu actual; resettlement 2,666
  families planned / 7,573 families actual. The gap is therefore the report's own comparison, not a
  constructed one. PAD confirms 560 villages, 133 townships, 943 km, 49,102 people, 45,853 by land
  requisition, 2,666 households with 9,401 inhabitants, 6,152 affected by both. Three provinces are
  Zhejiang, Jiangxi and Hunan, as the card says. The lesson quotation on the ministry-pays/
  local-government-administers disconnect is in the ICR. Only the risk-rating clause was removed.
- **henan-towns-water-land-acquisition — confirmed, `displaced: 4` kept.** Body and Annex 5 confirm
  659.73 mu, 713 households, 2,834 people, 300 m2 demolished affecting 4 households / 15 people,
  Lushan 130 households / 520 people, Dengzhou 87 / 348, the 57.4 mu exception, the cost figures,
  and the Hohai University monitoring (four reports March 2007 to March 2012, fifth in 2013). The
  ICRR paragraph does drop the 57.4 mu exception and the 713/2,834 figures, and states the
  higher-than-RAP compensation without qualification — confirmed by reading the whole ICRR
  paragraph. I kept `displaced: 4` even though the ICR's verb is "affected", because the quantity
  is households whose dwellings were demolished, which is a count of households that lost their
  homes rather than a project-affected count; the label now says what the figure is and what it is
  out of. Ratings read out of the ICR itself: Unsatisfactory / Substantial / Moderately
  Unsatisfactory / Moderately Unsatisfactory.
- **sichuan-wudu-canal-resettlement — confirmed.** Figures as above. The two companies check out:
  the ICR data sheet names the Sichuan Wudu Water Diversion Management Bureau as implementing
  agency, and para 67 names "River Development Corporation from General Planning and Design
  Institute under the Ministry of Water Resources" as the external monitor employed by the PMO. No
  oversight body is listed beside the agency that caused the harm — the monitor is the borrower's
  own contractor, which the role says.
- **shaying-river-sanba-village-resettlement — confirmed, nothing changed. The strongest case in
  the batch.** ICR paras 57–58 carry the whole account in the card's order: 23 rural households
  resettled at Sanba, the January 2018 notice that the resettlement site itself had been identified
  for economic development, 10 taking cash and departing, 13 opting for Xiayuan Resident Compound
  with construction "expected to be completed only by June 2019", the 18-month transition fee
  "sufficient to rent houses in nearby towns", the grievance mechanism being established, the
  six-monthly county reports, the Anhui Rural Road Program, and the two Bank monitoring missions in
  early 2019 and June 2019. PAD confirms 1,658 mu / 111 ha, 9,874 mu / 658 ha, 364 households /
  1,489 people relocated, 2,891 households / 10,316 people at 34 disposal sites, and the PAD's own
  stated total of 3,679 households / 13,456 people — which does not equal 364 + 2,891, and the card
  is right to present it as "a stated total".
- **tongliang-road-land-lease-compensation — confirmed; `end` 2018 → 2017.** Ratings read out of the
  ICR data sheet: Outcome Moderately Unsatisfactory, Bank Performance Moderately Unsatisfactory, M&E
  Modest; the ICRR table matches in all three rows. The card's statement that the two agree is
  right. No `displaced` field, correctly — the body text and the annex cannot both be right about
  how many households lost housing.

## killed

Zero on all eleven cards, `killed_note` empty, and that is right. I grepped every one of the twelve
ICRs for `fatalit`, `death`, `died`, `killed`, `fatal`. The only hits are in P111421 and P126454 and
they are traffic-safety indicators measuring fatalities and injuries on project corridors as a
benefit, plus P086446's unrelated word "remedied". P132154's ICR states "there were no reports on
human worksite accidents". No project-caused death anywhere in the batch.

## Sources

All 46 unique URLs fetched: **46 of 46 returned HTTP 200**, no 403, no 404, no redirect failure.
All 33 World Bank PDFs were downloaded and their first pages read: every one is the document its
citation claims, matched on report number and title — ICR00005333, ICRR0022658, 66008-CN (ZhangHu);
ICR00004265, ICRR0021546, 45059-CN (Anhui Medium Cities); ICR0000918, ICRR13032, 29067 (Zhe-Gan);
ICR00005224, ICRR0022446, 74279-CN (Nanchang); ICR00002898, ICRR14478, 33668-CN (Henan);
ICR00005031, ICRR0022453, 57661-CN (Wudu); ICR00003778, ICRR0020299, 46291-CN (Xining);
ICR00004354, ICRR0021326, 66467-CN (Yining); ICR00004372, ICRR0021305, 55660-CN (Shaying);
ICR00004173, ICRR0021166, 47995-CN (Chongqing); ICR1835, ICRR13840, 31447-CHA (Poor Rural
Communities). The writer's warning about near-miss P-numbers inside URL paths is correct and
harmless to the citations themselves.

Dates: the four older reviews print their own "Date Posted" and the cards use it — 09/30/2008
(P075602), 10/17/2014 (P081348), 01/27/2014 (P071094), 08/28/2012 (P068752). I could not verify the
seven newer reviews' dates, which carry no date inside the document (see "could not check").

## Coordinates

Every `lat`/`lng` was re-resolved against Nominatim and all eleven match to the fourth decimal the
place each `point` field names: Nanchang 28.6472/116.0348, Xining 36.8245/101.4408, Zitong County
31.6551/105.1912, Yining 43.9052/81.2748, Yingshang County 32.6531/116.2515, Tongliang District
29.8474/106.0525, Luocheng County 24.8760/108.7905, Lu'an 31.7383/116.5142, Lushan County
33.7417/112.7269, Wanquan District 40.8474/114.5977, Yingtan 28.2378/117.1143. `ap: true` on all
eleven, correctly. The Xining spelling note is right: the ICR writes "Hangyuan County" in para 37
and "Huangyuan Water Affairs Bureau" in its implementing-agency list, and Nominatim resolves
Huangyuan County (36.6129/101.1748) and not Hangyuan.

## Voice

Scanned every prose field, company role and lender role of all eleven cards for `I`, `we`, `my`,
`our`, `us`, `this card`, `this entry`, `the draft`, `the writer`, `researcher`. **No hits** — the
only matches were "US$" catching "us". No record of the research process is on any card. The one
process-shaped sentence I removed was Nanchang's second absence statement in `outcome`.

## Confidence

All eleven are correctly `contested`: every case rests on a World Bank completion report and the
Independent Evaluation Group's review of that report, which is the Bank reporting on its own
project, and no independent press, court record, Inspection Panel finding, field study, audit or
NGO report was found for any of them. Ten of the eleven `confidence_note` fields already said so in
the required plain terms. **`guangxi-poor-rural-land-acquisition` did not**, and the sentence naming
who is reporting on whom has been added.

## The drop

**P068752, Inner Mongolia Highway and Trade Corridor — I agree with the drop.** The ICR's social
paragraph is entirely favourable and gives no count: "Project resettlement was fully implemented
... All the affected households have restored their housing, with better quality than before
relocation ... All the land was fully compensated and the livelihood of the affected is restored."
The ICRR's statement is as quoted: the appraisal figures were 16,984 mu affecting "2,129 people in
590 households in 39 villages", and "Comparative figures at completion are not stated in the ICR
which simply says that the project resettlement was fully implemented", repeated in its comments on
ICR quality. Appraisal plan only, no recorded loss — neither limb.

---

# Required closing items

## 1. What I could not check, and what stopped it

- **The dates of the seven newer ICR Reviews** (P122319, P111421, P132154, P121414, P101829,
  P126454, P118647, P086446 — eight in fact). These documents carry no date in their text, only a
  report number. The writer says the dates in `sources` are the Bank's `wds` `docdt` field. I
  confirmed by reading each cover that no date is printed, so I could neither confirm nor refute the
  dates; I did not re-query the API. They are not filename dates — the URL paths carry no parseable
  date — and each is plausibly after its ICR. **The lead should treat these eight `sources` dates
  and the review dates quoted in `lenders[0].role` and `outcome` as unverified at document level.**
- **Whether any resettlement action plan contains the ICIJ figures.** None was downloaded, by the
  writer or by me. The cards' absence claims are correctly limited to "the documents opened", so
  nothing on a card overstates this, but the possibility that ICIJ's nine unmatched figures come
  from RAPs is untested.
- **Whether a PPAR exists for P086446.** I did not re-query the `wds` list; I confirmed only that
  the ICRR contains no recommendation for further assessment.
- **Independent corroboration.** I did not spend searches re-running the writer's two. Every card is
  `contested` and says no outside source was found, which is the honest position either way.

## 2. Figures where two documents disagree

The full list, with both figures and both documents, is in the section above. The ones that are real
and matter:

| Quantity | Figure A | Figure B |
|---|---|---|
| Residential housing demolished, P086446 | 70 m2, "seven houses", 25 people (ICR body text) | 2,474.96 m2, 593 households, 2,387 people, with 70 m2 / 7 / 25 belonging to **enterprises** (ICR Annex 7) |
| People affected, P086446 | 2,837 (ICR body text) | 2,387 (ICR Annex 7 totals, which add up) |
| Land acquired, P086446 | 412.526 mu (ICR body text) | 309.194 + 322.526 + 90 = 721.72 mu (ICR Annex 7) |
| Land acquisition and resettlement cost, P086446 | US$50m estimated / US$15m actual (ICR body) | "around USD20 million at the loan closing" (ICR Annex 7) |
| Affected people, P081348 | 2,834 (ICR body and Annex 5 Table 5.1) | 1,041 (ICR Annex 5 Table 5.2, actual column) |
| Permanent land acquired, P081348 | 659.73 mu (Table 5.1) | 644.95 mu (Table 5.2, actual) — **not previously reported** |
| Land acquisition cost, P081348 | RMB 34.67m (ICR body) | RMB 36.47m (ICR Annex 5) |
| Outcome rating, P122319 | Satisfactory (ICR) | Moderately Unsatisfactory (ICRR0022658) |
| Bank performance, P122319 | Satisfactory (ICR) | Moderately Satisfactory (ICRR0022658) |
| Funding shortage behind the unpaid RMB 67m, P122319 | RMB 57 million (ICR para 59 sentence) | RMB 56 million (ICR para 59 bullet) — **not previously reported** |
| Risk to development outcome, P081348 | Substantial (ICR) | Significant (ICRR, printed in **both** columns) |
| Risk to development outcome, P101829 | Moderate (ICR) | Modest (ICRR, printed in **both** columns) |
| Persons affected at appraisal, P122319 | ~7,500, ~3,600 relocated (PAD main text) | ~7,511, ~3,631 relocated, plus 1,763 from 34 enterprises (PAD annex) |
| Enterprises, P122319 | 34 with 1,763 people (PAD annex) | 168 with 1,879 employees (ICR, outcome) — before-and-after, not a conflict |
| Trust funds, P071094 | TF-54747, TF-55699 (ICR cover) | TF-54949, TF-70354 (ICR data sheet and body) |
| ICR date, P101829 | 9 June 2016 (cover) | 25 May 2016 (data sheet) — **not previously reported** |
| People relocated, P121414 | 990 in 264 households (PAD) | 3,449 in 992 households (ICR) — **before-and-after, not a conflict** |
| Families resettled, P075602 | 2,666 planned (PAD and ICR Annex 2) | 7,573 actual (ICR Annex 2) — **the report's own comparison** |
| Families, P132154 | 1,043 (PAD) | 1,344 urban + 41 rural (ICR) — **before-and-after, not a conflict** |
| Programme-wide relocation, P121414 | 3,525 people (PAD main text) | 3,523 people (PAD annex) — trivial, not on any card |
| Farmland in the Bank-financed area, P121414 | 2,318 mu (PAD main text) | 2,138 mu (PAD annex) — trivial, not on any card |

## 3. Faults appearing in more than one card

1. **A plan-versus-outcome gap written as something the documents fail to explain.** Three cards:
   Nanchang ("The documents do not explain the gap between 1,043 families at appraisal and 1,344 ...
   at completion"), Wudu ("Neither Bank document explains why the number relocated came out at
   3,449 ... against an appraisal figure of 990"), and the same sentence again in Wudu's
   `confidence_note`. An appraisal estimate and a completion figure are different measurements at
   different dates; no document owes a reconciliation. All three corrected to state both figures and
   that neither document compares them. The writer's own report lists two of these among its "ten
   figure disagreements", which is where the habit shows.
2. **A count whose verb in the document is "affected" sitting in `displaced`.** Two cards, Nanchang
   (1,344) and Xining (132), both now stripped. In Xining's case the figure is also the appraisal
   plan repeated. This is the single most consequential pattern in the batch, and it is the one the
   brief names first.
3. **A favourable Bank finding re-described in adverse words.** Guangxi's "the pressure that made
   the land easier to obtain" for the ICR's participatory approach and voluntary offers of land;
   Nanchang's framing of the unreported 73 per cent as "the clearest harm figure" (in the writer's
   report) and its duplication across `community` and `outcome`. Both corrected. This is the mild
   form of the selective-quotation fault: the quotations themselves were honest everywhere I
   checked, but the connective prose leaned.
4. **Trivial or non-existent discrepancies carried on cards as though they bore weight.** The
   Zhe-Gan "Low or Negligible" / "Negligible to Low" clause (removed) and the cover-versus-data-
   sheet dates, which are recorded on two cards and silently omitted on a third where the same
   mismatch exists.

## 4. Things wrong in the card data outside the fields I was asked to check

- **`guangxi-poor-rural-land-acquisition`, `companies[0].role`:** the Luocheng County finding was
  about institutional capacity, not procurement; the procurement findings in that ICR are in Yunnan.
  Corrected. This is the fault the brief predicts for `role` fields, and it was real.
- **`xining-riverway-house-demolition`, `end`: 2016 → 2015.** The loan closed 31 December 2015 and
  nothing adverse is documented after closing; 2016 is the ICR's date, not the harm's.
- **`tongliang-road-land-lease-compensation`, `end`: 2018 → 2017.** Same reason; the Tongliang
  correction was made at closing, 30 June 2017, and 2018 is the ICR's date.
- **`zhanghu-railway-resettlement`, `end`: 2021** — left as it is. Unlike the two above, it is
  supported: compensation was still unpaid and the task team still following up when the ICRR was
  written.
- Checked and **found correct**, for the record: every implementing agency named is a body the
  documents put on that project (Nanchang Urban Rail Group Co., Yining Project Management Office,
  Sichuan Wudu Water Diversion Management Bureau, Henan Provincial Financial Department / PPMO,
  Anhui Construction Management Offices and Wuhu Transport Bureau, Anhui Provincial Transport
  Department, APPSCIG, Huzhang Railway Passenger Dedicated Line Co. Ltd registered 10 October 2013,
  China Railway Corporation with RMB 13.151 billion of capital, MOR's FCTIC, LGOP with MOF and the
  three provincial FPMOs, Xining Water Affairs Bureau named first among four). No civil-society or
  oversight body is listed beside an agency that caused harm; the two external monitors listed
  (Hohai University's Resettlement Research Center, River Development Corporation) are the
  borrower's own contractors and their roles say so. DFID's US$37 million co-financing is on the ICR
  cover page as stated.
- The writer's note that `sources` URL paths embed near-miss P-numbers (P081340 in the P081348 ICR
  path, P086101 in the P086446 PAD path) is accurate and is a genuine hazard for a future
  `dedupe_leads.py` run on those numbers. Worth the lead's attention, since the fix is in the
  dedupe script and not in these cards.

## 5. Routes

No route failed. Named as routes:

- `https://documents1.worldbank.org/curated/...` over the agent proxy with `curl`: 46 of 46 URLs
  returned HTTP 200, including all 33 PDFs re-downloaded for identity checks. The writer's note that
  `documents.worldbank.org` (without the `1`) refuses `pdfurl` requests and that rewriting the host
  works is consistent with what I saw; I used the rewritten host throughout and it never failed.
- `https://nominatim.openstreetmap.org/search`: 13 of 13 queries resolved, all in Latin script. I
  did not retry the writer's one reported failure, the Chinese-script query for 金凤水库 四川
  (Jinfeng reservoir), so that remains the writer's finding rather than mine.
- `https://projects.icij.org/...` and `https://www.icij.org/...`: 200 on all 13.
- No permission prompt was raised and no host refused anything.

## Lead's overrule, 12 Nov 2026

`xining-riverway-house-demolition` is **dropped**. The checker kept it narrowly on limb (b) and
flagged it as the one call to overrule, which is the right flag.

Paragraph 37 of the completion report (P101829) reproduces the appraisal's figures word for word —
1,635.1 mu of collective land in 39 villages affecting 888 households comprising 3,549 people, and
house demolition affecting 132 households and 538 people — and where the appraisal writes "538
people in 132 households will be relocated", the completion report's own verb is "affected". There
is therefore no outcome count of anyone moved and no outcome count of land actually taken. The
same paragraph records the plan implemented satisfactorily, resettlement effective, livelihoods
restored and farmers highly satisfied with compensation, so nothing adverse sits on top of the
move either.

That is the same position as this batch's own P068752 drop, where the only count was the appraisal
plan. Keeping one and dropping the other would have been inconsistent, and the inconsistency would
have been invisible on the map.
