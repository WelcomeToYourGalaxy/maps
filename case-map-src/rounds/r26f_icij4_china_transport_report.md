# Round 20, batch B — China transport, rail, water and rural (ICIJ tranche 4)

Output file: `/home/claude/r20/r26f_icij4_china_transport.json` — 11 cases, 1 drop, 0 extends, 0 already-on-map.
All 11 are `contested`.

## P-numbers established for all 12 leads

| ICIJ lead | P-number | Board approval | Outcome |
|---|---|---|---|
| ZhangHu Railway | P122319 | 15 Mar 2012 | case `zhanghu-railway-resettlement` |
| Anhui Medium Cities Urban Transport | P111421 | 20 May 2010 | case `luan-huaibei-urban-transport-resettlement` |
| Second National Railways (Zhe-Gan Line) | P075602 | 24 Jun 2004 | case `zhegan-line-railway-resettlement` |
| Inner Mongolia Highway and Trade Corridor | P068752 | 15 Feb 2005 | **dropped** |
| Nanchang Urban Rail | P132154 | 20 Jun 2013 | case `nanchang-line-2-demolition` |
| Henan Towns Water Supply and Sanitation | P081348 | 27 Jun 2006 | case `henan-towns-water-land-acquisition` |
| Sichuan Wudu Irrigated Agriculture | P121414 | 28 Feb 2012 | case `sichuan-wudu-canal-resettlement` |
| Xining Flood and Watershed Management | P101829 | 2 Jun 2009 | case `xining-riverway-house-demolition` |
| Xinjiang Yining Urban Transport Improvement | P126454 | 29 May 2012 | case `yining-urban-roads-demolition` |
| Anhui Shaying River Channel Improvement | P118647 | 12 Apr 2011 | case `shaying-river-sanba-village-resettlement` |
| Chongqing Urban-Rural Integration | P086446 | 3 Jun 2010 | case `tongliang-road-land-lease-compensation` |
| Poor Rural Communities Development | P071094 | 21 Jun 2005 | case `guangxi-poor-rural-land-acquisition` |

`dedupe_leads.py` on all 12 plus P081161: all 12 new, P081161 on the map as
`chongqing-small-cities-qianjiang-resettlement`.

## The three specific warnings

1. **Chongqing.** The two projects are distinct. The existing case
   `chongqing-small-cities-qianjiang-resettlement` is **P081161**, Chongqing Small Cities
   Infrastructure Improvement Project, approved 21 June 2005, closed 30 June 2012 — confirmed by the
   dedupe script, which returned that case id for P081161. The lead is **P086446**, Chongqing
   Urban-Rural Integration Project, approved 3 June 2010, closed 30 June 2017, a different loan
   (IBRD-79200 against 4794-CHA), different districts and a different sector unit. A third Chongqing
   project, P126210, Chongqing Urban Rural Integration Project II-Health, approved 14 June 2012, also
   exists and is not this lead. On the PPAR point: P086446's ICR Review (ICRR0021166) contains no
   recommendation for further assessment and no PPAR is filed under P086446 in the `wds` list for that
   project id. The 48-households-by-the-road finding from round 18 belongs to P081161's Project
   Performance Assessment Report and is already in the existing case; it is not repeated here.
2. **Anhui / Shaying vs the Huai River case.** The Shaying lead is **not** the same works as
   `huai-river-flood-drainage-resettlement`, which is **P098078**, the Huai River Basin Flood
   Management and Drainage Improvement Project (loan IBRD-79380, approved 6 July 2010, dikes,
   dredging and drainage for flood control across Anhui, Jiangsu, Henan and Shandong). The Shaying
   lead is **P118647** (loan IBRD-80360, approved 12 April 2011), navigation works on 205.6 km of the
   Shaying channel in Anhui only: dredging to Class IV navigation standard, 43.87 km of bank
   protection, four bridges rebuilt for clearance, ship locks, navigation signals. Different loan,
   different purpose, different implementing agency (Anhui Provincial Transport Department and
   APPSCIG against the Huai River Basin Commission under the Ministry of Water Resources). A separate
   pin is justified. The other Anhui lead, P111421, is urban road works in four municipalities and is
   unrelated to both.
3. **Zhe-Gan.** Handled by querying the projects API with `&os=0&rows=100` from the start rather than
   the default page, which returned it directly: `P075602 | Second National Railways Project
   (Zhe-Gan Line) | 2004-06-24`. It is the sixth of seven results for that query term, so the default
   page size would have been enough here, but the wide query cost nothing. Note two near-neighbours that are not this project: P086515 Third
   National Railway Project (2007) and P058846 CN-Natl Railway Project (2002).

## The drop

**P068752, Inner Mongolia Highway and Trade Corridor — dropped.** Neither limb is met. The ICR of
29 June 2011 gives no outcome count of people or households relocated; it says only that
"Project resettlement was fully implemented", that all affected households restored their housing
"with better quality than before relocation", that all land was fully compensated and livelihoods
restored. The ICR Review of 28 August 2012 says so explicitly: the appraisal document's figures were
16,984 mu of land affecting 2,129 people in 590 households in 39 villages, and "Comparative figures
at completion are not stated in the ICR". The review repeats the point in its comments on ICR
quality: "Comparative figures for environmental and social activities at appraisal and completion
were not given." So the only count is an appraisal plan figure, which the brief rules out, and no
specific harm to identifiable people is recorded. The review's "Assessment Recommended?" box gives
as its reason the worsening terms of trade and doubtful traffic forecasts, not the resettlement, and
no PPAR is filed under P068752.

## My two weakest entries

1. **`nanchang-line-2-demolition` (P132154).** The verb problem the brief warns about sits at the
   centre of it. The ICR's sentence is "Altogether 1344 urban families, 130 enterprises and 41 rural
   families were affected" — *affected*, not relocated — and the next sentence calls them "the
   displaced families". No document separates families whose houses were demolished from families who
   lost only land, although the ICR does say the demolition of private houses was fully completed by
   August 2014. The `displaced: 1344` therefore rests on the report's own slide from "affected" to
   "displaced families", and the label says so. The only other harm figure is an absence: 27 per cent
   of affected families gained an improvement in their living environment and nothing is recorded
   about the other 73 per cent. Everything else in both documents is favourable. If the checker wants
   to cut one, cut this one.
2. **`yining-urban-roads-demolition` (P126454).** 93 households is a real outcome figure from the
   ICR's own planned-against-actual table, and it is small. Every other fact about those households in
   both documents is favourable: compensation above the planned rates, transition payments, incomes up
   RMB 1,412 per person, 94 per cent satisfied, no substantive complaints. The case stands on the bare
   relocation count under limb (a) plus the Bank evaluators' finding that the land acquisition and
   compensation spending cannot be traced in the appraisal document, the loan agreement or the ICR.
   It is in Xinjiang and the ICR says most affected people are Uygur, which is why it is worth a pin
   at all, but nothing outside the Bank corroborates anything in it.

Runner-up weak point: `sichuan-wudu-canal-resettlement` and `xining-riverway-house-demolition` both
carry a clean relocation count with no recorded loss on top of the move. Wudu's count (3,449 people in
992 households) is a genuine outcome figure; Xining's (132 households, 538 people) is identical in the
appraisal document and the ICR, so it is a plan figure the ICR repeats rather than a measured outcome.

## Figures where two documents disagree

1. **P086446 Chongqing, ICR body text against the ICR's own Annex 7.** Body text: 412.526 mu
   permanently acquired, affecting 593 households or **2,837** people, and **70 m2** of residential
   housing demolished affecting **seven houses** and 25 people. Annex 7 table: 309.194 mu case-by-case
   plus 322.526 mu permanent plus 90 mu government-allocated; house demolition **2,474.96 m2** with 593
   affected households and **2,387** project-affected people; and, in a separate column, **seven
   individual enterprises** covering 70 m2 with 25 project-affected people. So the body text attributes
   to seven *houses* what the annex attributes to seven *enterprises*, and 2,837 against 2,387 is a
   transposed digit pair. Same document, no reconciliation. The cost is also given twice: body text
   US$50 million estimated against US$15 million actual, Annex 7 "around USD20 million at the loan
   closing".
2. **P081348 Henan, ICR Table 5.1 against ICR Table 5.2.** Table 5.1 and the body text: 713 households
   or **2,834** people affected by acquisition of 659.73 mu. Table 5.2, the planned-against-actual
   comparison in the same annex: affected people, actual, **1,041**. The ICR itself says "there are
   inconsistencies in the data, which the PPMO has not been able to clarify". Cost also differs: body
   text RMB 34.67 million, Annex 5 RMB 36.47 million.
3. **P122319 ZhangHu, ICR against ICRR on the outcome rating.** ICR: Satisfactory. ICRR0022658:
   Moderately Unsatisfactory, with the reason printed. Bank performance: Satisfactory against
   Moderately Satisfactory. Both named to their document in the card.
4. **P122319 ZhangHu, PAD main text against PAD annex.** Main text: approximately 7,500 persons
   affected, approximately 3,600 people from 1,078 households relocated. Safeguards annex:
   approximately 7,511 persons, approximately 3,631 people from 1,078 households relocated, plus 1,763
   people from 34 enterprises. The ICR's enterprise figure is different again: 168 enterprises with
   1,879 employees.
5. **P121414 Wudu, PAD against ICR on relocation.** PAD: 990 people in 264 households would lose their
   houses under the Bank-financed works (and the wider Wudu Phase II programme would relocate 3,525
   people). ICR: 3,449 relocated people in 992 households. Unexplained in both documents.
6. **P132154 Nanchang, PAD against ICR.** PAD: 83,817 m2 demolished, owned by 1,043 families,
   affecting 4,001 people, plus 201 shops and 22 enterprises/organisations, plus 142 people from 31
   families for land. ICR: 1,344 urban families, 41 rural families, 130 enterprises, 170,468.13 m2 of
   land acquired. Resettlement plan cost US$193 million at appraisal against US$514 million actual.
7. **Label substitutions in ICRR rating tables** (brief trap 1 and 3), all three verified against the
   ICR itself:
   - **P081348**: ICR data sheet says risk to development outcome **Substantial**; the ICRR table prints
     **Significant** in *both* the ICR column and the IEG column. The ICRR also *downgrades* borrower
     performance (ICR Moderately Unsatisfactory → IEG Unsatisfactory) while its own "Government
     Performance Rating" line says Unsatisfactory.
   - **P075602**: ICR says **"Low or Negligible"**; the ICRR table prints **"Negligible to Low"** in both
     columns.
   - **P101829**: ICR says risk **Moderate** (data sheet and body text, "the overall risk to development
     outcome is rated Moderate"); the ICRR table prints **Modest** in both columns.
8. **P075602 internal tension.** The ICR Review's comment on ICR quality says the report "does not
   discuss the number of people resettled" — while Annex 2 of that report gives 7,573 families against
   2,666 planned. Both statements are in the card.
9. **P071094 cover against data sheet.** The ICR cover names trust funds TF-54747 and TF-55699; the data
   sheet names TF-54949 and TF-70354. Both are recorded in the lender role.
10. **ICR date, P081348.** Cover page: 24 December 2013. Own data sheet: "ICR Date: 11/14/2013". The
    card uses the cover date and names the other. Same pattern on P075602: cover 15 August 2008, data
    sheet 17 August 2008; both given.

## Selective-quotation checks made

Every damaging clause used was read in its whole paragraph and the favourable clause from the same
paragraph is in the card:
- P111421: the 121 unmoved households sit in the same paragraph as the transition subsidy paid in
  conformity with local policy, paid twice over for the extension, and "well sufficient" to rent
  comparable housing. Both are in.
- P122319: the RMB 67 million unpaid sits beside funds in escrow, replacement apartments of ~100 m2
  retained for the three households, and the report's statement that they have houses elsewhere to live
  in. All in.
- P081348: "compensation rates ... ended up higher than the rates agreed in the RAP" is in, together
  with its exception, "except for about 57.4 mu of land for which an annual rental fee is being paid".
  The ICRR drops that exception; the card records that it does.
- P086446: the Tongliang lease-compensation failure sits beside compensation exceeding agreed rates,
  funds paid without deduction, and the monitor's finding that no affected person was pushed into
  poverty. All in.
- P118647: the second move of the 23 Sanba households sits beside the 18-month transition fee called
  sufficient to rent in nearby towns, the grievance mechanism being set up and the two planned Bank
  monitoring visits. All in.
- P071094: the safeguards specialist's finding on missing written agreement sits beside land
  voluntarily provided, satisfaction with the arrangements and incomes up at least 50 per cent
  2004–10. All in.

## Staff statements, not documents

Grepped every ICRR for `informed IEG`, `the project team`, `the World Bank team stated` and `TTL`.
Hit counts: P126454 20, P122319 15, P075602 15, P068752 13, P118647 12, P132154 12, P086446 10,
P111421 8, P101829 5, P081348 5, P121414 3, P071094 3. One such statement is used, and it is
attributed as a statement: P122319's ICRR records that "IEG's discussion with the Bank task team showed
that they are still following up with the Borrower on the outstanding resettlement compensation
payments even though the project closed more than a year ago." No figure in any card comes from a staff
statement.

## killed

Zero across all 12 projects, `killed_note` empty. Checked each ICR for `fatalit`, `death`, `died`,
`injur`. The only hits are road-traffic safety indicators (P111421, P126454) counting traffic
fatalities and injuries on project corridors as a *benefit* measure, plus a RMB 500,000 per-death
valuation used in P111421's economic analysis. No worker death, no death caused by any project, in any
of the 24 ICR/ICRR documents.

## Independent sources

None found, as three earlier tranches predicted. Two searches were spent and then stopped, as the
brief directs: one in Chinese on the named village and county (`颍上县 三坝村 移民安置 沙颍河 世界银行`) and
one in English on the Zhangjiakou/Hohhot compensation disputes. The Chinese search returned Three
Gorges coverage and a Bank feature story; the English search returned Laos–China railway compensation
reporting and an unrelated RFA piece on Xinjiang land compensation. Nothing on any of these 12
projects. Every card says so in `confidence_note` and every card is `contested`.

## Routes that worked and the one that didn't

- Projects API with `countrycode_exact=CN&qterm=...&os=0&rows=100` resolved all 12 P-numbers in two
  calls. Matching on approval date was necessary for Chongqing (three candidate projects) and Inner
  Mongolia (two).
- `wds?format=json&projectid=P...&rows=200` listed every project's documents; all 12 have both a
  disclosed ICR and a disclosed ICR Review filed under their own number. No parent or sibling lookup
  was needed and no report was undisclosed.
- `pdfurl` came back on the refusing host `documents.worldbank.org` for every document; rewriting the
  host to `documents1.worldbank.org` and fetching with `curl`, then reading with `pdftotext -layout`,
  worked for all 36 PDFs with no failures.
- Nominatim resolved 15 of 16 place queries in Latin script. The one failure: **金凤水库 四川**
  (Jinfeng reservoir, Sichuan) returned no result in Chinese or in Latin script, and no Bank document
  places the Jinfeng reservoir in a named county, so the Wudu point sits on Zitong County with
  `ap: true` and the point text says the documents do not place the reservoir.
- Note on a spelling, not a failure: P101829's ICR writes "Hangyuan County" while the same report's
  implementing-agency list writes "Huangyuan Water Affairs Bureau". Nominatim resolves Huangyuan County
  and not Hangyuan. The card's `place` uses Huangyuan and the `point` text records both spellings.
- Note on the newer ICRR template: the 2016-onward reviews carry **no date inside the document** —
  only a report number (e.g. ICRR0021305) and the project's approval and closing dates. Their dates in
  the `sources` arrays are the Bank's own `docdt` field from the `wds` API, not a filename. The older
  reviews (P075602, P068752, P081348, P071094) print "Date Posted" in their text and those dates are
  taken from the document.

## Document cache

`/home/claude/r20/cache/` — 72 files from this batch, paired `.pdf` and `.txt` (`pdftotext -layout`),
named `P<number>_<TYPE>`:

- `_ICR` — Implementation Completion and Results Report, all 12 projects.
- `_ICRR` — Independent Evaluation Group ICR Review, all 12 projects.
- `_PAD` — Project Appraisal Document, all 12 projects.

P-numbers in the cache from this batch: P122319, P111421, P075602, P068752, P132154, P081348, P121414,
P101829, P126454, P118647, P086446, P071094. No resettlement action plans were downloaded; where an
appraisal resettlement figure was needed it was read out of the PAD, which carries it. The ICIJ figure
comparison in each `displaced_note` rests on the PAD, read directly, not on the ICRR's quotation of it.

## One thing for the lead to know

Each card's `sources` array contains real `documents1.worldbank.org` URLs whose path segments embed
near-miss P-numbers (e.g. the P081348 ICR sits at a path containing `P081340`, the P086446 PAD at one
containing `P086101`). `dedupe_leads.py` searches all strings inside a case object, so a future round
checking one of those near-miss numbers would get a false "ON THE MAP" hit. The true P-number is in the
lender role of every card as the brief requires.
