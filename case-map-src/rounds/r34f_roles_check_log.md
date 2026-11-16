# Independent check of the round-34 `lenders[].role` audit

Checker: separate agent; did not write the audit. Standards read in full before starting:
`docs/ROLES.md` (ten error classes, the data-sheet/review-table mechanism, the ISR leg of the date
rule) and `docs/CHECK31.md`.

**Result: 26 corrections tested, 23 upheld, 3 rejected. 3 further errors found that the audit did
not correct (2 on cards marked clean). One new error class ruled in and applied.**

Mechanical pre-check: all 26 `was` strings are exact substrings of the live `role` in `r34in/`.
Re-asserted in python over the 23 survivors and the 3 checker-found corrections before finishing;
0 failures.

---

## 1. The five `wrong_column` corrections — all five upheld

ROLES.md's warning about extracted tables arriving unaligned is real, so for each I printed the
block from the header row to the footnote and read the columns.

**jituhun-railway-resettlement (P122321) — upheld.** `P122321_ICR.txt` Annex 1(a), header
`Appraisal Estimate / Actual-Latest Estimate / Percentage of Appraisal`, prints
`Total Project Cost 5,960.50 / 5,010.15 / 87` and `Total Financing Required 6,303.00 / 5,272.45 / 86`.
The card's "about US$6.3 billion" total cost is the appraisal column of *financing required*. Its only
other home is the report's own paragraph 71 ("financing only 3 percent of an almost US$6.3 billion
project") — prose against the table, and ROLES.md gives the table. The `now` prints all four figures
with where each appears.

**kisip-informal-settlements-fatalities (P113542) — upheld.** `P113542_ICR.txt` FINANCING table,
header `Original Amount (US$) / Revised Amount (US$) / Actual Disbursed (US$)`, row
`IDA-48730  100,000,000 / 99,998,818 / 93,287,879`. The card's "US$99.99 million disbursed by the
revised figures" is the Revised *Amount* column, a commitment, not any disbursement. Corroborating:
the same card's AFD and Sida entries already use the right pattern ("revised to ... with ... disbursed"),
so lender 0 was the outlier.

**salem-tnudp-squatter-resettlement (P083780) — upheld, the best-evidenced of the five.**
`cache/P083780/ICR_2014-09-30_20263592.txt`, Table 9. The extraction splits the row ("Rehabilitation &
Resettlement and" / "191.21" / "137.22  191.20 ... 0" / "Shifting of Utilities"), which is exactly the
trap. Columns are `Revised allocation: Project Cost (INR in mn) | Amount committed | Expenditure up to
March 2014 | Works completed up to March payment made subsequently`. I settled the reading by summing
each column against its printed Total:

| column | sum of six rows | printed Total |
|---|---|---|
| revised allocation | 1748.00 | 1748.00 |
| amount committed | 1734.44 | 1734.44 |
| expenditure to March 2014 | 1588.99 | 1588.99 |

So 137.22 is the revised allocation (not appraisal), 191.20 is committed and 191.21 is expenditure to
March 2014. The card had read the revised-allocation column as appraisal and the committed column as
spend. The `now` is right on both.
*Unfixed and noted:* Table 9 sits inside Annex 7, "Summary of Borrower's ICR and/or Comments on Draft
ICR", whose header is the borrower's own "Evaluation Report ... July 2014". It is the borrower's table
reproduced, not the Bank's cost table. The card calls it "the completion report's cost table" and the
correction leaves that phrase untouched (it is outside `was`). Batch 3 flagged this itself in
`could_not_settle` item 41. Left as a pre-existing attribution point for a later round.

**shizheng-railway-resettlement (P099062) — upheld.** The brief asked whether US$6.544 billion is a
restructuring paper's financing-plan total rather than a cost. It is: Restructuring Paper
Report No. 71424-CN, heading "2. Revised Financing Plan (US$m)", `BORR 6,200.00 / 6,244.00`,
`IBRD 300.00 / 300.00`, `Total 6,500.00 / 6,544.00`. 6,544 is the Revised column of a financing plan.
The ICR's Annex 1 gives `Total Project Costs 5,017.25 / 5,051.81` and `Total Financing Required
6,224.10 / 5,197.29` under a column headed "Appraisal Estimate" (footnotes 6, 7 and 9 say the CMV
component added at restructuring is included in that column for comparison), so the `now`'s phrase
"in its appraisal-estimate column" is the document's own label and properly hedged.
*Recommended amendment, not applied:* the `now` replaces a **cost** claim with a financing-required
figure only, and omits the ICR's own `Total Project Costs` row (5,017.25 appraisal / 5,051.81 actual)
sitting eight lines above it in the same table. Jituhun's `now`, for the identical fault, prints both
rows. I upheld the correction as written rather than edit another agent's text, but the next round
should add the cost row for consistency.

**vietnam-water-resources-assistance-resettlement (P065898) — upheld.** The brief asked me to confirm
the remedy prints two figures with where each appears rather than picking one. It does, and both sides
check out. The 2019 performance assessment's preface reads "Total project cost at completion was
special drawing rights 102.83 million ($159.44 million equivalent)"; the 2013 ICR review's data table
puts `Loan /Credit (US$M) 157.8 / 159.44` and `Project Costs (US$M) 176.2 / 177.84`. So 159.44 is the
credit, not the cost — independently corroborated by the performance assessment's own Table A.2, whose
actual cumulative disbursement reaches 159.4 at FY13, and by its Table A.1, which gives total project
costs 176.2. The card printed one of two conflicting IEG figures as settled, which ROLES.md makes a
correction. *Noted:* the `now` does not mention that the performance assessment contradicts itself
(preface 159.44 as cost, Table A.1 176.2 as cost). Not required — adding material is barred — but it is
the sharper fact.

## 2. The five `date_unsupported` corrections — 3 upheld, 2 rejected

The ISR test was applied to each. It is worth its place: on all three substantive dates it either
confirmed the correction or supplied the date the cited documents lacked.

**bumbuna-hydro-reservoir-resettlement (P086801) — upheld; ISR confirms.** ICR2972 paragraph 43:
"restructuring of the project only took place in September 2010 ... The PRG component was canceled and
funds reallocated (US$9.5 million which is equivalent to a guarantee of US$38.0 million) ... The
restructured project, renamed the Bumbuna Hydroelectric Environmental and Social Management Project,
became effective in March 2011." ISR13813's loan table: `IDA-H6250 approved 28-Sep-2010, signed
29-Sep-2010, effective 14-Mar-2011`. The card tied the cancellation and the US$9.5 million
reallocation to 2011; both are 2010, and 2011 is effectiveness. The `now` gives each date its own
event. (The same ISR prints Board Approval Date 16-Jun-2005, which confirms that batch 1 was right to
drop its Bumbuna approval-date correction.)

**kamwenge-fort-portal-road (P092837) — upheld; ISR confirms.** ICR00002228 paragraph 20: "On June 16,
2011, less than a year after the effectiveness of the original Credit and with an appropriate waiver
from Bank management dated November 19, 2010, the Board approved a further IDA Credit (4949-UG) in the
equivalent amount of US$75 million." Its Table 1.4 AF-Credit row gives Approval Date June 16, 2011 and
Financing Agreement Signing June 5, 2012. ISR of 5 February 2012: `IDA-49490 Not Effective, Approval
Date 16-Jun-2011`, signing column still blank — consistent with a June 2012 signature. The card's 2010
is the waiver date. The same card's lender 0 already says "approved in 2011", so the card contradicted
itself.

**kandadji-dam (P130174) — upheld; ISR confirms.** Project Paper 87654 paragraph 2: "The original
financing amount of US$203 million was approved by the Board on October 2, 2012 and became effective on
March 13, 2013"; paragraph 43: "The existing IDA credit and grant of US$203 million would be increased
to US$258.3 million." Restructuring Paper RES48057's financing table: `IDA-54590` and `IDA-H9520`
approved 29-May-2014; `IDA-67000 (100.00)` and `IDA-D6700 (50.00)` approved 24-Jun-2020. The ISR of
30 May 2013 gives `Board Approval Date 02-Oct-2012, Effectiveness Date 13-Mar-2013`. I also confirmed
that the string `258.31` occurs in none of the five cached Kandadji documents (only `258.3`, once).
So the card's approval date, its "by 2020", and its figure 258.31 are all unsupported.

**REJECTED — caldwell-bridge-liberia-compensation (P113099).** The brief asked me to say that a
completion report's cover date is a kind ISRs do not carry, rather than treat the test as passed. That
is right, and batch 1 said so itself. But the correction fails on a prior ground. ICR00004329's cover
prints "December 19, 2017"; the card's "22 December 2017" is the Bank catalogue's own `docdt` for that
document (`r34docs/wds/P113099.json`: docdt `2017-12-22`, docty "Implementation Completion and Resul").
ROLES.md: "Citation style is not a fact ... cited with one from the Bank's catalogue — unattributed, not
wrong. Leave it." The class `date_unsupported` means "a date no cited document gives", and the
correction's own `why` concedes the date is the catalogue's. Nothing about the project changes.

**REJECTED — siddhirganj-pipeline-transmission-land (P095965).** Identical shape. Cover prints
"September 28, 2020" (Report No. ICR00005299); the card's 26 September 2020 is the catalogue `docdt`
(`r34api/P095965.json`). Rejected on the same rule.

Two things decided these two rather than the cover-beats-catalogue instinct. First, ROLES.md's
cover rule is written for *loan and credit numbers* — facts about the operation — not for the date in a
citation, which is a locator. Second, Bumbuna shows that "the date on the cover" is not uniquely the
document's own date: ICR2972's cover prints "July 30, 2014" while its data sheet prints
`ICR Date: 07/31/2014`, and the card's 31 July 2014 is therefore in the document. I had provisionally
logged the Bumbuna citation as a missed error on the strength of the cover and the catalogue alone, and
withdrew it on reading the data sheet — the same mistake the brief warned about, made and caught.
**This is the rule the next brief should settle explicitly**, because it decided 2 of 26 corrections.
Neither Caldwell's nor Siddhirganj's ICR carries an `ICR Date` field, so in both the cover date is the
only one in the document; the question is purely whether a citation follows the cover or the catalogue.

## 3. The three `partial_list` corrections — all three upheld

Test applied: did the card present its list as the whole set, and is each added policy marked
triggered in the appraisal document's **own safeguards table**, not merely in prose.

**gujarat-highway-ii-delayed-compensation (P114827) — upheld**, after treating it as the closest call
of the three. The card mirrors its cited review's own construction: ICRR0022895 reads "The project was
classified as Category A under Environmental Assessment (OP/BP 4.01) and triggered the Physical
Cultural Resources (OP/BP 4.11), the Involuntary Settlement (OP/BP 4.12), Indigenous Peoples (OP/BP
4.10) and the Forests (OP/BP 4.36) safeguard policies" — 4.01 sits outside the list, exactly as on the
card. But the card compresses "classified as Category A under Environmental Assessment (OP/BP 4.01)"
to "Classified Category A", after which 4.01 is named nowhere and the four read as the triggered set.
PAD758's safeguards table marks exactly five Yes: 4.01, 4.36, 4.11, 4.10, 4.12. The card cites that PAD
as one of its two sources. ROLES.md settles it: an omission is an error where the card claims
completeness, and it names "a policy list" as such a claim.

**rurrenabaque-airport-land-compensation (P122007) — upheld.** PAD (6 April 2011) safeguards table
marks Yes for 4.01, 4.04, 4.36, 4.11, 4.10, 4.12 — all three added policies pass the table test. The
mechanism is visible: ICR paragraph 67 names the three *social* policies, paragraph 69 reads "The
Project was classified as category B and triggered the following policies: Environmental Assessment
(OP 4.01), Natural Habitats (OP 4.04), and Forest Management (OP 4.36)". The card attached
paragraph 67's three to the words "Environmental category B", i.e. to the sentence that in the report
introduces the other three.

**south-west-roads-turkestan-sairam-compensation (P099270) — upheld.** ICR00317 paragraph 75: Category
A, triggered OP/BP 4.01, and "During the 2017 restructuring, two additional safeguard policies were
triggered" — OP 4.11 and OP 4.04; paragraph 77 adds OP/BP 4.12. The data-sheet restructuring table
lists "Safeguard Policies Triggered" against 16-Jun-2017. The card named one of four. Note on the
table test: 4.11 and 4.04 are *not* in the appraisal table and could not be, since they were triggered
in 2017; the `now` says so explicitly ("added at the 2017 restructuring"), which is the right handling
and the reason the appraisal table is not the test for a restructuring-added policy.

## 4. The two `review_prose_over_table` corrections — both upheld

**ribb-megech-irrigation (P092353) — upheld.** Second test first: the card *does* attribute the figure
correctly in form — "Disbursed: US$105.8 million per the completion report (the IEG review gives
US$129.9 million)". It is still right to delete. ICRR0021528's own project data table prints
`Revised Commitment 121,314,499.56` and `Actual 105,794,445.60`, the same actual as the ICR's data
sheet (`Total ... 105,794,445`). The 129.9 is in the review's prose alone ("The total disbursement was
US$129.9 million"), and the real 129.93 is a Bank allocation figure in the ICR ("required for the
Project, to US$129,933,487"). So there is no disagreement *between* documents to preserve under
CHECK31 — the ICR and the review's table agree, and the card's parenthesis manufactures a conflict out
of a slip in one review's prose. Deleting it leaves the card agreeing with both documents.

**rsdp-apl3-road-deaths (P091077) — upheld.** ICR00003504 Table 4, "Original and Revised Components":
row 2 `Construction of regional rural road -> Excluded from IDA financing`, reason "government decided
to drop this component"; row 3 `Institutional Strengthening of ERA -> No change`, reason "Only change
in numbering, is now component 2". Paragraph 18: "The major change ... was the exclusion of the
regional roads component." The review agrees with the table: "The second component construction of
regional roads, specifically the Yalo-Nehile road estimated to costs US$18.2 million, was dropped in
2013", and the ICR's own annex carries "*Dropped - Yalo-Nehile 18.19". The card said institutional
strengthening was dropped, which the table says was unchanged; it had followed the ICR's paragraph 17
("the exception of Component 3 which was excluded"), the report's own numbering slip.
*Class note:* this is the **report's** prose against the **report's** table, with the review on the
table's side — not the review's prose. The class `review_prose_over_table` is the nearest fit and the
principle (table wins) is the same, but the taxonomy has no label for a report contradicting its own
table, which is what happened here and in jituhun.

## 5. The five `wrong_document` corrections — 4 upheld, 1 rejected

Tested on the extended standard: not only which document gives the figure but **whose finding the
sentence is** — the heading of the section it sits in, and the next sentence.

**philippines-nrimp2-unpaid-land-claims (P079935) — upheld; the exemplar.** ICR00003186 page 34 carries
"Inadequate handover between successive TTLs was also considered a factor in the resettlement issues
which emerged, as better safeguards oversight would have prevented linked works from proceeding without
compensation being paid." ICRR0020824's section 13 reproduces it verbatim under the heading
"Adapted from ICR (paras 119- 123) with some modification of language :". So the review did not agree
independently; it reprinted the report's lesson under a heading saying so. The `now` says the review
repeats the lesson, which keeps the fact that the review carries it without claiming agreement.

**mekenajo-dembidolo-road-coffee (P106872) — upheld, and it is a speaker error too.** ICRR0021231's
quality-of-ICR bullet: "The cost tables are incorrect/confusing. On page 2, total project is reported
as US$206.3 million while in Annex 3 the total project cost is reported as US$276.4 million." Its
section e instead *relies* on the third figure: "The actual total project cost is reported to be
US$275.2 million (ICR, Tale 7.6, page 53)", without criticism. The ICR's Annex 3 total reads 276.44.
The card paired 206.3 with 275.2 and credited the evaluators with calling that pair incorrect — a
criticism they did not make about a figure they adopted. The `now` names all three figures and
attaches the criticism to the two the review actually names.

**burkina-donsin-airport-roads-resettlement (P120960) — upheld.** ICRR0021994's data sheet gives
`Original Commitment 85,000,000 / Revised 85,000,000 / Actual 80,887,030.24`, with Total Project Cost
the same and Closing Date (Actual) 30-Apr-2019. The card's US$79.65 million is the disbursed column of
ISR36770 (`P120960 IDA-52510 ... 79.65 ... 98%`), archived eleven days before closing, whose text says
"As of April 19, 2019, cumulative disbursements had reached about 98.27 percent". A mid-stream figure
printed as the disbursed total.

**kandadji-dam lender 2 (P130174) — upheld.** The `was` asserts the Bank's record "gives the larger
current commitments without explaining the relationship between them". Project Paper 87654 paragraphs
2 and 43 and RES48057's financing table do explain it, as set out in section 2 above, so the claim of
no explanation is false. The `was` is also researcher voice ("The existing card's figure..."), which
ROLES.md bars in a corrected substring; the `now` removes it. *Noted:* after both Kandadji corrections
apply, lender 0 still carries "International Rivers reports a $203 million loan approved in 2012",
which becomes redundant beside the corrected first sentence, and lender 2 still carries the
US$408.31 million and US$1,095.11 million figures that batch 2 could not open a source for
(`could_not_settle` item 23). Neither is a correction; both are for a later round.

**REJECTED — ningxia-highway-compensation-delays (P096920).** The correction moves "land acquisition
and compensation for land loss were, the Bank's evaluators say, almost completed" from the evaluators
to the completion report, on the ground that the claim is the report's and the review doubted it. The
review's safeguards section does exactly that: "The ICR (page 6, paragraph 21) asserts that land
acquisition and compensation for land loss was almost completed by the end of June 2010 ... The ICR
however provides no evidence on the actual number of people who were compensated." But the card did
not take it from there. ICRR0020123's section **"a. Quality-at-Entry"** states in the review's own
voice: "by the project launch mission in August 2010, the project investment works were well underway
(with about 20-55% of the nine CQE subgrade contracts launched and land acquisition and compensation
for land loss were almost completed by June 2010)." The card's sentence tracks that parenthesis clause
for clause — launch mission, 20 to 55 per cent of nine subgrade contracts, compensation almost
completed — and not the ICR's separate sentences. A review that adopts a claim in one section and
doubts it in another does not make "the evaluators say" wrong, and the correction would swap one
accurate attribution for another while asserting the first was false. *What both the card and the
correction miss, and the real finding here:* the review says the report gives no evidence for the
claim, which for a card about delayed compensation is the material point. Recorded for a later round;
not written in, since adding material is barred.

## 6. The four `wrong_number` and two `wrong_agency` corrections — all upheld

**chebei (P075728), shiyan (P081749), guiyang (P093963) — upheld; covers read.**
`cache/P075728/AGR_2004-07-05_5129828.txt` cover: "CONFORMED COPY / LOAN NUMBER 4742 - CHA / Dated
July 5, 2004", and the project agreement the same. `cache/P081749/AGR_2004-10-11_5371719.txt`:
"CONFORMED COPY / LOAN NUMBER 4745-CHA / Dated October 11, 2004", project agreement the same.
`r34docs/txt/P093963/LA_4881.txt` (36.9 KB, not a redirect stub): "CONFORMED COPY / LOAN NUMBER
4881-CHA / Dated March 18, 2008", and ICR2512's own cover prints "(IBRD 48810-CHA)" with its data
sheet "L/C/TF Number(s): IBRD48810-CHA". ROLES.md's warning about a file the archive titles
"Conformed" being an unsigned draft with the number and date left blank does not bite: all three carry
both the number and the date.

**lower-nzoia-irrigation-unpaid-compensation (P117635) — upheld.** ICR00185's restructuring table marks
"Loan Closing Date Extension" at exactly three dates — 17-Dec-2020, 14-Dec-2022, 22-Sep-2023 — and
paragraph 17 reads "three extensions of the closing date (concurrent with Restructurings 5, 6, and 7)".
The card said four. *Class note:* `wrong_number` is defined as "a wrong report number"; a wrong count
of extensions is not one. Mislabelled, correction sound.

**haiphong-bac-son-nam-hai-road (P111548) — upheld, with a caveat on the reasoning.** ICR00005180
paragraph 13 is the sentence that carries the figure: "The GoV would provide counterpart funding of
US$101.61 million", and the financing table's row is labelled `Borrower/Recipient 101,610,000`. The
card attached the figure to the Haiphong city government, which no sentence or cell does.
*But the correction's `why` is wrong where it says "Haiphong People's Committee appears in the report
only in the acronym list."* It does not: the report has "both of which were approved by the Haiphong
City People's Committee", and, more to the point, "the slow land clearance and resettlement were due to
the Haiphong Government's financial constraints in providing counterpart funding". So the card's
original was not baseless — the Haiphong Government did provide counterpart funding. The correction
holds because the **named figure** belongs to GoV, not because Haiphong is absent from the report.

**orissa-state-roads-compensation (P096023) — upheld.** ICR00003903 Table 3, "Project Funding
Allocation", labels the row carrying 54.94 `Borrower`, and the data sheet gives "Borrower: Republic of
India". The review calls the same figure counterpart financing. The only sentence naming the state
reads "The GOO would pay the cost of land acquisition (LA) and shifting of utilities" — a scope of
costs, not the US$54.94 million. The `now` uses the table's own word, "the borrower", which asserts
nothing the document does not.

## 7. The opposite error: 12+ clean cards sampled, 3 errors found

Sampled 14 cards deeply and screened all 60 mechanically. Two screens were run over every clean card:
one flagging any figure on a card absent from that project's own documents in any format, one
normalising and checking every date on a card against the documents in nine written forms. Flags were
then read by hand. Deep sample: drc-selembao (P057296), da-nang-sustainable-city (P123384),
kibera-mukuru (P079734), swat-s3b (P125584), olkaria-maasai (P103037), nepal-road-sector (P095977),
hanoi-ring-road-2 (P083581), rwanda-rssp2 (P105176), dehlon-bypass (P090585), eastern-dedicated-freight
(P114338), upper-cisokan (P112158), lom-pangar (P114077), qmm-fort-dauphin (P083351), vietnam-medium-
cities-phu-ly (P116398). Screened additionally: assam-roads, ceip-polder, uganda-ert2, karnataka-
state-highways-ii, rusumo-falls, kawanda-masaka, vietnam-road-asset-management and the rest of the 60.

### Errors found (written up as `checker_found` in roles_checked.json, not merged into the audit's own)

**1. hanoi-ring-road-2-relocation (P083581), marked clean by batch 1 — `partial_list`.** The card says
"The credit triggered Involuntary Resettlement policy OP/BP 4.12". The appraisal table
(`PAD_2007-05-17`) marks Yes for exactly two: Environmental Assessment (OP/BP/GP 4.01) and Involuntary
Resettlement (OP/BP 4.12). The cited ICR's paragraph 71 reads "The project was classified as a
Category A project under OP 4.01 - Environmental Assessment"; paragraph 75 gives 4.12. The card took
paragraph 75 and left 71 out — structurally the same error batch 3 corrected on rurrenabaque, where the
card took the social-policy paragraph and dropped the environmental one. Batch 1 left it on the reason
"The card does not claim a full list" (`could_not_settle` item 19), which is the reasoning ROLES.md
overrides by naming "a policy list" as a completeness claim. **Inconsistent application of
`partial_list` between batch 1 and batch 3 is the single clearest process fault in the three audits.**

**2. rwanda-rssp2-marshland-resettlement (P105176), marked clean by batch 3 — `partial_list`.** The
card names two triggered policies, 4.12 and 7.50. The appraisal table (`PAD_2008-06-02`) marks five
Yes: 4.01, 4.04, 4.09, 4.12, 7.50. The cited ICR names the same five: "four safeguards policies
triggered by RSSP 2 (OP/BP 4.01, OP/BP 4.04, OP/BP 4.09, OP 4.12)" plus "OP 7.50 (Projects in
International Waterways) was also" triggered. Two of five.

**3. eastern-dedicated-freight-corridor (P114338) — `wrong_scope`, the new class.** Batch 1 found this
error and filed it unsettled for want of a class; I verified it independently and have applied it. See
section 8.

### Checked and confirmed clean (the ones worth recording)

- **kibera-mukuru (P079734):** I suspected the card's split of the relocation line item — US$92.80
  million actual "of which IDA paid US$39.10 million and the government of Kenya US$53.70 million" —
  because the review calls 39.10 "a revised estimate at the Level 1 restructuring". Printing the block
  settled it for the card: ICR Annex 1 Table 1-1 header is `Appraisal Document 2005 | Revised Estimate
  2011 | Actual December 2015: Total | IDA | Gov't | TMEA` and the row is
  `d. Implement Relocation Action Plan  11.00 | 39.10 | 92.80 | 39.10 | 53.70 | 0.00`. 39.10 appears
  twice, as the 2011 revised estimate and as IDA's actual share, and the card read the IDA column.
  39.10 + 53.70 = 92.80. A coincidence of equal figures in two columns, which is the same hazard as
  the five `wrong_column` cases and this time the card got it right.
- **salem, swat, da-nang, drc-selembao, dehlon, nepal, upper-cisokan:** every figure, date, rating,
  loan number and agency I tested matched. Da Nang's financing table, dates, borrower and implementing
  agency were verified line by line. Swat's two-document ratings clash is handled correctly: the ICR
  data sheet says risk to development outcome "Significant" and the IEG ratings table prints
  "Substantial / Substantial", and the card attributes each rating to the document that gives it.
  Kibera's and Swat's outcome ratings were read from both documents (ICR "Moderately Satisfactory";
  ICRR section "a. Outcome Rating: Moderately Unsatisfactory").
- **upper-cisokan (P112158)** validates the ISR leg of the date rule from the other side: the card's
  "P172256, approved 10 September 2021" is in no completion report, and `r34docs/P172256/ISR_2022-01-27`
  prints `Bank Approval Date: 10-Sep-2021` and `P172256 IBRD-92780 10-Sep-2021`. On the cited documents
  alone this would have been scored `date_unsupported` and made wrong.
- **rwanda "ICR2741"** is not in the document, which prints no report number at all. Batch 3 flagged
  this (item 40) and left it on the citation-style rule. I settled it: re-running the documented API
  call with the report-number field, `search.worldbank.org/api/v3/wds?format=json&projectid=P105176&fl=docdt,display_title,docty,repnb`,
  returns `repnb = ICR2741`. It is the Bank's own report number for the file, so not an error — and
  this is the same ground on which I rejected the two cover-date corrections.
- **dehlon-bypass (P090585):** the card's four triggered policies are exactly the four its PAD table
  marks Yes (4.01, 4.11, 4.12, 4.36). A policy list that is complete.
- **lom-pangar (P114077):** the card names four of seven policies but writes "among others", which
  disclaims completeness. Batch 2's reasoning (item 29) is right, and consistent with the rule I
  applied to Hanoi: the test is whether completeness is claimed.
- Screen flags resolved as artefacts: `172.6` (= `172,600,000` in the ICR total row), `76.04`
  (= `76,040,785`), `339.9`/`308.3` (= `339,900,000`/`308,334,882`), `229.77`/`205.43`
  (= `229,771,673`/`205,430,693`), da-nang's lender-1 figures (they belong to P086508, a different
  project folder), drc's `P096305` (a project number, attributed on the card to the projects API).

### One sourcing problem on a clean card, short of an error

**olkaria-maasai (P103037), lender 1.** The card's EIB figures — a loan of up to EUR 119 million,
EUR 71.3 million disbursed at the time of the complaints review, AFD as lead among the European
lenders — are not verifiable from anything on disk. Batch 2's `checked` line cites "EIB Complaints
Mechanism conclusions report SG/E/2014/07 and 08". The only EIB file in the harvest,
`r34docs/other/eib.txt`, is the Conclusions Report for the **Bujagali Hydroelectric Project, Jinja,
Uganda, Complaint SG/E/2009/09, 30 August 2012** — a different case, and the one the `bujagali` card
rests on. It contains no "71.3", no "SG/E/2014", and its money is in Ugandan shillings. Either the
report was fetched without being cached or the two EIB cases were conflated. I cannot show the figures
are wrong, so this is not a correction; it is an unverifiable `checked` claim, and the EIB complaints
case page is a route the next round should try.

## 8. Ruling on the missing error class

**Ruled: a new class, `wrong_scope`, and applied to the EDFC card.**

Definition: *a mis-stated statement of what a loan built or where — the sections, route, components or
works a card says the money paid for — measured against the completion report's own component or
section description.*

Why not an existing class. `partial_list` is the closest, and the structure of the EDFC error is
indeed a subset read as the whole. But `partial_list` is defined for safeguard-policy lists and its
operative test is whether the appraisal document's safeguards table marks a policy triggered, which
has no meaning for a railway route; the classes exist to route a correction to its test. The other
nine all turn on which document, which column or which speaker a figure came from, and this error is
none of those: every figure on the EDFC card is right. A scope claim has its own test — does the
completion report's description of the components or sections match what the card says the money
financed — so it warrants its own class. Batch 1 was right to file it rather than force a bad label;
ROLES.md tells an auditor to do exactly that when no class fits.

Verified independently before applying. ICR00004930 (27 February 2024, the combined report for EDFC 1,
2 and 3) gives EDFC-1 as "the 343 km Khurja and Kanpur section", EDFC-2 as "the 393 km Kanpur- Mughal
Sarai section", EDFC-3 as "the 401 km Ludhiana- Khurja section", and sets out the phasing as "APL1 for
the Khurja - Kanpur section; APL2 for the Kanpur - Deen Dayal Upadhyaya Station (DDU, formerly
Mughalsarai Station) section; and APL3 for the Ludhiana - Khurja section". With EDFC-3 in, the three
loans run Ludhiana to Mughal Sarai. The card's amounts and approval date check out, as batch 1 said.

Batch 1 also filed three other wording faults under the same gap — burkina-donsin item 7 (advice *on*
an airport resettlement plan turned into advice *to make* one) and dakar items 17 and 18 (an IDA credit
said to be "for the whole project" where the appraisal document says IDA did not finance Component A,
the road itself). Items 7 and 18 are `wrong_scope` on the definition above and should be corrected in
the next round; item 17 could not be settled because the AfDB document would not open.

## 9. The China loan-number question

Covers read for all three `-CN` -> `-CHA` corrections (section 6); all three are right. No card has
been corrected in the wrong direction. I scanned all twelve China loan references across the 87 cards:

| card | number on card | status |
|---|---|---|
| chebei P075728 | L4742-CN | corrected to 4742-CHA; agreement cover confirms |
| shiyan P081749 | L4745-CN | corrected to 4745-CHA; agreement cover confirms |
| guiyang P093963 | L4881-CN | corrected to 4881-CHA; agreement cover and ICR cover confirm |
| chongqing P081161 | 4794-CHA | already CHA, untouched |
| sichuan P083322 | 4838-CHA | already CHA, untouched |
| shaanxi P075613 | 4853-CHA | already CHA, untouched |
| liuzhan P086515 | L4847-CN | left alone — correctly, see below |
| shizheng P099062 | L7557-CN | left alone; loan agreement cover prints "LOAN NUMBER 7557-CN" |
| guiguang P107559 | L7678-CN | left alone |
| huai river P098078 | 7938-CN | left alone |
| ningxia P096920 | 7880-CN | left alone |
| jituhun P122321 | L8052-CN | left alone |

**Batch 1's generalisation — that pre-2005 China operations print `-CHA` while 2009-2010 ones are
`-CN` — does not hold, and should not be carried forward.** Guiyang's Loan 4881 is dated 18 March 2008
and prints `-CHA`; Liuzhan's Loan 4847 is dated 6 April 2007 and prints `-CN`. I tested Liuzhan
specifically on a 4xxx-series hypothesis and it fails: ICR00002178's cover carries only "(IBRD-48470)"
with no suffix, but its bibliography cites "Loan Agreement (Loan IBRD 4847-CN)" twice, and the
catalogue carries both "Loan Agreement L4847-CN - Conformed" (2007) and "Official Documents- Amendment
to the Loan Agreement for Loan 4847-CN" (2012). So the card agrees with its own cited report and there
is nothing to correct. The rule to carry forward is that **the suffix must be read off each document
and never inferred from the year or the number series.**

## 10. The 47 `could_not_settle` items

All 47 read. They are the strongest part of the three audits: they name the route that failed rather
than the host, and several record conflicts with both sides given, as CHECK31 asks.

**Real absences verified (two of the four, as asked).** Re-ran
`search.worldbank.org/api/v3/wds?format=json&projectid=<P>&rows=200&fl=docdt,display_title,docty,repnb`:

- **P120960** — API `total` = 37, matching batch 1's count. The only document whose `docty` begins
  "Implementation Completion" is the IEG review `ICRR0021994` (2020-06-17). No completion report.
- **P114827** — API `total` = 118, matching batch 1's count. Only `ICRR0022895` (2022-06-13). No
  completion report.

ROLES.md's warning that a blank `docty` can hide a project's only completion report was checked rather
than assumed: in both responses the single entry with no `docty` is the API's own `facets` key, not a
document. Both absences are real. The other two claims (P081161 with 23 documents, P090585 with 62)
were not re-run.

**Items a route I can reach would settle.** Outbound HTTPS works from here and the WDS API answers, so:
- **rwanda item 40 (ICR2741)** — settled above by adding `repnb` to the documented API call. Worth
  adding `repnb` to the standard harvest query: it would settle every cited report number cheaply.
- **kandadji item 23** — the figures come from the projects *web page*, which returned an unanswered
  permission prompt. The projects API, re-run, gives different numbers (idacommamt 405,000,000;
  lendprojectcost 1,044,550,020) than the card's US$408.31 million and US$1,095.11 million. A
  `projects` API route, not the web page, would settle it; the card's three commitment figures remain
  unsourced and should be revisited before the web-page numbers are trusted.
- **olkaria lender 1** — see section 7; the EIB complaints case page for SG/E/2014/07-08 is untried.
- **dakar item 16 (AfDB behind a Cloudflare challenge)** — I did not retry it. Both routes batch 1
  names failed for different reasons (a 5.9 KB "Just a moment" interstitial; an unanswered permission
  prompt), and the honest record is that the host is reachable but the file is not served to a plain
  client. Worth one attempt from a browser tool next round rather than curl, which is the distinction
  CHECK31 asks to be drawn.
- **trung-son item 43 ("the loan agreement signed in June 2011")** — the ISR route is the obvious one
  and is not mentioned in the item; ISRs print signing dates in their loan tables, as ISR13813 and the
  Kamwenge ISR both do above. Try it before scoring the date.

**Items correctly left alone**, and worth keeping as the pattern for later rounds: items 1, 21, 22, 25,
26, 27, 28, 34, 35, 42, 46, 47 all record a figure or label given two ways and leave the card following
the document it cites. Item 5 is the Bumbuna approval date dropped after the ISR test; item 9 says
plainly that ISRs were not a route to a report's cover date. Item 29 (lom-pangar) and item 19 (hanoi)
apply the same completeness test to opposite conclusions — item 29 is right and item 19 is the missed
correction in section 7.

## 11. Outputs

- `out34/roles_checked.json` — 22 cases carrying the 23 surviving corrections, in the audits' own
  shape, with each case's `checked` and `could_not_settle` carried over. Top-level `rejected` holds the
  3 thrown out, each with the `was`, the proposed `now` and the sentence that saved the card.
  Top-level `checker_found` holds the 3 errors I found, marked `"source": "checker"` and kept **out**
  of the case objects so that applying the audit's surviving corrections mechanically does not
  silently apply mine; `new_class_ruling` records the `wrong_scope` definition.
- Every surviving `was`, and every checker-found `was`, asserted in python to be an exact substring of
  the live `role` in `r34in/`. 0 failures.
- `base.html` untouched. Nothing merged, built or pushed.
