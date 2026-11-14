# Round 22 — audit of `lenders[].role` across 46 Case Map cards

Scope: 46 cases from rounds 20 and 21, 56 lender entries, ~63,000 characters of role prose.
Every rating, date, amount, loan number, sanction term and implementing agency was read out of the
completion report, the Evaluation Group review, the appraisal document, the Project Performance
Assessment Report, the additional-financing project paper or the Inspection Panel investigation
report itself, from `/home/claude/r20/cache` and `/home/claude/r21/cache`. No document had to be
fetched; the cache covered all 46 P-numbers cited.

## 1. Counts

- Entries checked: **56** (46 cards)
- Clean: **37**
- Corrected: **19 entries / 22 edits**, all in `/home/claude/r22/r26f_role_audit_textfix.json`

Dry-run: `base.html` and `merge_textfix.py` copied to `/home/claude/r22/dryrun`, run there —
**records applied 19 ; problems 0**. The real `/home/claude/maps/case-map-src/base.html` was not touched.

## 2. The corrections

1. **sichuan-small-towns-unfinished-resettlement** — card: total project cost at appraisal
   US$169.95m. Documents: the completion report's Annex 1 gives Total Project Costs 169.70 at
   appraisal (141.81 actual), and the review's own text says "the total appraisal estimate for this
   project was US$169.7 million" (ICRR0020788, §2e). US$169.95m is only the review data sheet's
   Total Project Cost field (= 100 Bank + 69.95 borrower). Column now named.
2. **qufu-gupan-pond-demolition** — card: "against US$86,560,000 at appraisal". The report disowns
   that figure in its own note under the data sheet (ICR00004242, p.5): "the original Total Project
   Cost should be US$130.78 million, as reported in the Project Appraisal Document (PAD). The amount
   could not be fixed in the portal by the team."
3. **liaoning-coastal-zone-resettlement** — card: "Environmental category A." Documents: ICR data
   sheet, Original and Revised EA Category both "Partial Assessment (B)"; PAD Basic Information,
   "B - Partial Assessment".
4. **liaoning-coastal-zone-resettlement** — card: the project office was "the same provincial office
   that ran the Bank's earlier Liaoning Medium Cities loans". No cited document says so. ICR para 70
   says only that the project "followed four World Bank-financed urban environmental projects in
   Liaoning" and used their lessons. Replaced with what the records do say, including that the PAD
   names the Liaoning Provincial Development and Reform Commission as responsible agency.
5. **second-shandong-environment-resettlement** — card: the review "lowered Bank performance to
   Moderately Satisfactory". The review's ratings table (ICRR14669, §12) lowers borrower performance
   to Moderately Satisfactory as well, with its own reason (shortcomings in the implementing agency's
   performance). One of two downgrades was reported.
6. **luan-huaibei-urban-transport-resettlement** — card: "The report records that one reason the
   closing date was extended was delay in land acquisition and resettlement." That sentence is the
   review's ("because of the delays in land acquisition and resettlement, the loan closing date was
   extended to July 31, 2016", ICRR0021546 §2e). The completion report attributes the 23-month
   extension to the Wuhu changes (ICR00004265 para 47) and records the land-acquisition delays
   separately (paras 49–50).
7. **sichuan-wudu-canal-resettlement** — card named two triggered policies (OP 4.12, OP 4.37). ICR
   para 63 lists five: OP 4.01, OP 4.04, OP 4.09, OP 4.12, OP 4.37.
8. **yining-urban-roads-demolition** — card named three triggered policies and omitted Indigenous
   Peoples OP 4.10, which the PAD's safeguards table and para 34 record — material on a card about
   demolition in the seat of the Yili Kazakh prefecture.
9. **rogun-stage1-resettlement** — card: additional grant H757-TJ "approved 14 February 2012". No
   cited document carries that date. ICR00003310 says "In February 2012, the Bank's Board of
   Directors approved an Additional Financing" with no day; its data sheet lists the restructuring as
   02/10/2012; the project paper is dated 19 January 2012.
10. **santa-fe-road-19-expropriation** — card: "the loan and guarantee agreements signed 12 June
    2007". Not in the ICR, the review, the PAD or either Inspection Panel investigation report. The
    documents give approval 13 February 2007 and effectiveness 17 August 2007 (ICR data sheet and
    p.722). Date now attributed to the Bank's catalogue.
11. **bukoba-airport-resettlement-arrears** — card: "The implementing agencies were the Tanzania
    National Roads Agency and the Tanzania Airports Authority." The data sheet names TANROADS alone;
    ICR00004352 para 57: TANROADS was "the principal implementing agency" and handled overall
    coordination, "TAA for Component B-regional airports, GoZ for Component B-Zanzibar airport, two
    separate Divisions within the MoWTC for Components C and D".
12. **xian-weiyang-xinjiamiao-resettlement** — card: report number ICR00004130. The cover prints
    **ICR00004124**; ICR00004130 appears nowhere in the document.
13. **wuhan-nanhu-village-resettlement-delay** — card: field assessment recommended "alongside two
    other Chinese urban transport projects". The review's assessment note is about the same city:
    the first Wuhan project (approved March 2004) and the third (2012), "to provide important
    lessons on city-wide engagement in the urban transport sector".
14. **xining-wusixi-road-demolition** — card: the 2019 restructuring added "73 electric bus charging
    points and a relocated passenger station". ICR00005538 para 12b: 73 electric bus charging
    stations and 1,648 on-board bus units (passenger flow analysis systems); the only relocation is
    the interchange move from Yanxiaocun to Wangjiazhai, which the card already states. No cited
    document has a relocated passenger station added.
15. **amman-development-corridor-land** — card: US$455.97m actual, "132 per cent over". 132 is the
    cost table's "Percentage of 2008 Appraisal" against the revised estimate of US$343.18m; against
    the 2004 appraisal estimate of US$160.60m the actual cost was about 284 per cent.
16. **amman-development-corridor-land** — card: "both rated risk to development outcome High". The
    completion report rates that risk **Substantial** (ICR00002661 section 4, "Rating:
    Substantial"); High in the ICR column of the review's table is the review's entry. This is the
    round-20 fault again: a completion-report rating read out of the review's column.
17. **amman-development-corridor-land** — card: additional financing "approved 4 December 2008". Not
    in any cited document; the ICR's footnote cites "World Bank Project Paper on Additional Financing
    for US$ 33 million, November 6, 2008".
18. **nutrip-road-compensation-arrears** — card: the category B-to-A reclassification followed
    putting BRT into "the James Gichuru junction to Rironi section". ICR00004798 para 53 names the
    **JKIA–Rironi** road section; James Gichuru–Rironi is the 26 km funded part of that 53 km corridor.
19. **qiantang-small-town-house-demolition** — card: "Total project cost was US$215 million", with no
    column. The cost annex gives US$215.99m at appraisal and US$193.01m actual.
20. **corumana-dam-resettlement-mozambique** — card: "Credits IDA-50110 of US$70 million and
    IDA-53070 of US$32 million … approved 15 September 2011." IDA-53070 was the additional financing
    approved at the first restructuring on 27 September 2013 (ICR00005264 para 10).
21. **patna-ganga-riverfront-resettlement** — card: "The project financing agreement was revised to
    include the provisions of" the 2013 land acquisition Act. ICR00006028 para 21: it was the
    **Environment and Social Management Framework** that was revised. The financing agreement is
    mentioned in the report only as the source of the PDO.
22. **ouagadougou-onea-works-before-compensation** — card: the review "rated it Satisfactory, citing
    weak evidence of sanitation sustainability and the project's efficiency, and noted moderate
    shortcomings in procurement and in the implementation of safeguard policies that delayed the
    project." The review rates efficacy substantial because the sanitation-sustainability evidence is
    weak and rates efficiency substantial; and those shortcomings are its stated grounds for
    **lowering Bank performance from Satisfactory to Moderately Satisfactory**, a downgrade the card
    did not report.

## 3. Faults appearing on more than one card

- **A completion-report rating taken from the review's column (round 20's fault): 2 cards.**
  amman-development-corridor-land (risk High where the report says Substantial) and — in the other
  direction, handled correctly — the many cards that flag the Modest/Moderate and
  Negligible-to-Low/Low-or-Negligible label differences. Only Amman actually asserted the review's
  column as the report's rating. Against that, nine cards (sichuan-small-towns, nanning, han-river,
  shanghai-apl2, liuzhou, second-shandong, henan-towns, kwabenya, gameleira) state the label
  mismatch explicitly and correctly, and liuzhou catches the review misreporting the report's own
  Bank performance. The habit is established; Amman is where it lapsed.
- **A date asserted that no cited document contains (round 19's fault): 3 cards.**
  santa-fe (signing 12 June 2007), rogun (additional grant 14 February 2012), amman (additional
  financing 4 December 2008). All three are signing or board dates for a second instrument — the
  exact field the Bank's project portal carries and the documents often do not.
- **A single figure given without naming its column: 4 cards.** sichuan-small-towns (appraisal cost
  from the review's catalogue field), qufu (a data-sheet figure the report disowns), amman (132 per
  cent against the wrong base), qiantang (appraisal cost presented as the cost). Round 21 found the
  same class (a revised commitment given as a disbursement).
- **An incomplete list of triggered safeguard policies: 2 cards.** sichuan-wudu (2 of 5),
  yining (3 of 4).
- **A review's downgrade dropped while its reasoning is quoted: 2 cards.** second-shandong (borrower
  performance), ouagadougou (Bank performance).
- **Implementing agency not as the Bank's records have it: 2 cards.** liaoning-coastal (an
  unsupported claim about earlier loans, plus a different responsible agency in the PAD), bukoba
  (two agencies named where the data sheet names one and the report distributes the rest).
- **Pattern B, not corrected, present on 10 cards:** the completion report's cover date and the date
  in its own data sheet differ, and the card gives the cover date only. sichuan-small-towns (cover 31
  May 2017 / sheet 04/14/2017), nanning (11 Apr 2017 / 12/19/2016), shanghai-apl2 (30 Nov 2015 /
  09/02/2015), santa-fe (24 Jun 2013 / 06/28/2013), milot-rreshen (28 Dec 2011 / 12/29/2011),
  qiantang (7 Jun 2017 / 06/05/2017), nepal-raidp (24 Jun 2014 / 06/23/2014), gameleira (28 Dec 2012
  / 12/31/2012), kwabenya (27 Jun 2013 on both, no divergence) and two others; where the two dates
  agree — xi'an, liuzhou, han-river, dar-brt, second-shandong — there is nothing to add. Two cards
  do it the way the brief asks —
  zhegan-line and henan-towns both print both dates — so the fix is already in the house style.
- **Pattern C, not corrected, present on 39 of 46 reviews:** the Evaluation Group's review prints no
  date anywhere in the document, and 39 cards cite one anyway. I checked every ICRR in the cache:
  39 have no date on their opening pages; the 7 that show dates (P120234, P055120, P092631, P112956,
  P079736, P119085, P106909) show dates of other events, not of the review. In every case the date
  on the card matches the card's own `sources` entry, i.e. the Bank's catalogue field, so the dates
  are not wrong — they are unattributed. Round 21's cards already solved this ("dated 30 September
  2019 in the Bank's archive record", "Bank document date 17 December 2020"); round 20's cards do not.
  Applying that phrasing to the round-20 cards would be a 29-card citation-style change, which is a
  rewrite rather than a correction, so it is reported here and left out of the textfix file.

## 4. Not checked, and why

- **Nothing was blocked for want of a document.** All 46 P-numbers cited in role prose had the
  needed report in cache, including the Rogun PPAR and additional-financing project paper, the
  Kwabenya PPAR and three Inspection Panel reports, and the two Santa Fe investigation reports.
- **P071094 (Guangxi) PAD is a poor scan**: its safeguards table is unreadable in the text layer, so
  the triggered policies (OP 4.01, OD 4.20, OP 4.12) were verified from the review's safeguards
  section instead, which states them in those terms.
- **P081505 (Amman) ICR is a scan with heavy OCR damage** in the ratings summary; the ratings were
  verified from the report's narrative sections (section 4 for risk, section 5 for performance) and
  the review's table. The risk correction rests on section 4's "Rating: Substantial", which is clean
  text.
- **Two claims could not be traced to a cited document and were corrected rather than verified**: the
  Santa Fe signing date and the Amman additional-financing approval date (see §2). I did not fetch
  the loan agreements or the Bank portal to confirm them, so the cards now attribute them to the
  catalogue rather than asserting them.
- **Not in scope, not checked**: `killed` and `displaced` values, the body text of the cards, and any
  field other than `lenders[].role`.

## 5. Errors found outside the role field

- **P055120 (Bukoba) completion report is misdated by the Bank.** Its cover reads "January 16, 2017",
  but the project closed 20 June 2017, its exchange-rate note is "Effective {Dec 27, 2017}", and its
  passenger data run "through the end of September, 2017". The cover date cannot be right. The card
  gives no ICR date, which is the safe handling; any future card that wants one should say the cover
  is dated 16 January 2017 and that the report's own contents postdate it.
- **P079736 (CEMAC) data sheet contradicts the report's text.** The sheet prints "Partial Assessment
  (B)" as both original and revised EA category, while para 76 states "In 2017, as part of the
  restructuring to include force account using the Army Corps of Engineers, the project category was
  changed from B to A." The card follows the text, correctly.
- **P120234 (Qufu) data sheet carries a figure its own note retracts** (see correction 2) — the
  report says the portal could not be fixed.
- **P082373 (Kwabenya): the PPAR's ratings table also prints "Significant" as the completion report's
  risk rating** where the report says Substantial, so the review's column error is reproduced
  downstream in a second Evaluation Group document. The card handles both correctly.
- Two documents contain typographic errors the cards reproduce deliberately and correctly:
  P127867's "The project did not finance land acquisision" (quoted with the misspelling) and
  P126611's review writing "Longchang" for Longcheng district.

## 6. Verdict: pattern, not coincidence — but a narrowing one

**Pattern.** Three rounds found one or two errors each in this field by accident; a deliberate pass
over 56 entries found 22 in 19 of them, and they fall into the same six recurring classes rather than
scattering. Specifically, each of the three earlier findings reappears here:

- round 19's class (a date cited to a document that does not contain it) recurs on 3 cards, and all
  three are the signing or board-approval date of a second instrument;
- round 20's class (a rating or report number taken from the wrong place) recurs twice — Amman's risk
  rating from the review's column, Xi'an's report number ICR00004130 for ICR00004124;
- round 21's class (a column or clause inverted or unlabelled) recurs on 4 cards as unlabelled or
  wrong-base figures.

The mechanism is consistent and mundane: the field is written from a data sheet and a review table at
the same time, and when a figure or label exists in two places the role takes whichever is nearer to
hand. That is why the errors cluster on second instruments, on revised-versus-actual columns and on
the review's ICR column.

Two things argue against treating the field as generally unreliable. First, the bulk of it is right:
37 of 56 entries survived a line-by-line check with nothing to change, including the most
figure-dense entries in the batch (kwabenya, baoro-bouar, nutrip, zhanghu, corridor-x), and the card
round 21 corrected (laibin) now matches the report clause by clause, including "procurement
noncompliance", the five contracts and the works being substantially complete. Second, the field
already contains the habits that prevent these errors — zhegan-line and henan-towns print both report
dates; liuzhou, nanning and seven others flag the review's label substitutions; xiangyang says
"named in the data sheet" of its agency; ouagadougou flags an unreconciled approval date; amman
itself catches the two data sheets disagreeing on approval. The round-21 cards use "Bank document
date" for undated reviews throughout.

So the three earlier errors were not bad luck, and they are not evidence of a field written
carelessly. They are the predictable residue of one practice that is not yet applied everywhere:
naming the source column, and the source document, for every figure that exists in more than one
place. Two cheap standing rules would close most of it — never give a rating, amount or date without
the column or document it came from, and never read a completion-report rating out of the review's
table — and the single highest-yield remaining job is pattern C: 29 round-20 cards cite a review date
the review does not print.
