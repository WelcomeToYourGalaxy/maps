# Round 18 check log — batch G2 (ICIJ displacement leads, China and Vietnam)

Input: `/home/claude/r18/out_G2.json` (6 cases, 0 extends, 4 drops).
Output: `/home/claude/r18/checked_G2.json`.
Result: **6 kept, all 6 corrected, 0 cut; 4 drops upheld.** All ten lead numbers appear once.

## Documents opened from disk

Downloaded with `curl` from `documents1.worldbank.org` into `/home/claude/r18/ck2/` and read with
`pdftotext -layout`. Line counts are of the extracted text, and each was read in full where an
absence claim rests on it.

| Document | Lines |
| --- | --- |
| Jiangxi ICR00001853 (29 June 2011) | 2,925 |
| Jiangxi ICRR13739 (posted 10 September 2012) | 468 |
| Trung Son ICR00004999 (24 June 2020) | 3,422 |
| Trung Son ICRR (30 September 2020) | 800 |
| Trung Son PAD 57910-VN (30 March 2011) | 9,359 |
| Trung Son, Managing Social Risks and Impacts (September 2020) | 3,787 |
| Trung Son INT redacted report (November 2018) | 159 |
| Ningxia ICR00003484 (8 December 2015) | 2,087 |
| Ningxia ICRR (29 July 2016) | 636 |
| Zhejiang ICR00001917 (26 December 2011) | 3,253 |
| Zhejiang ICRR (posted 1 May 2014) | 657 |
| Yiba ICR00003722 (21 June 2016) | 2,684 |
| Yiba ICRR (9 February 2017) | 649 |
| Vietnam RAMP ICR (30 September 2023) | 2,703 |
| Vietnam RAMP ICRR0023795 (12 March 2024) | 707 |
| Meizhou Bay ICR (20 December 2019) | 1,948 |
| Yunnan Urban Environment ICR (23 April 2018) | 3,549 |
| Poyang Lake ICR (27 June 2020) + ICRR (16 February 2021) | 3,656 + 1,141 |
| Taiyuan Note on Cancelled Operation (4 December 2014) | 760 |

Also opened: the Bao Thanh tra article of 18 November 2025 on Government Inspectorate conclusion
375/KL-TTCP (fetched and read as text), and the Bank's documents API records for P084773, P124848,
P096812, P126856 and P081615.

## Ruling under the refined forward rule, case by case

Limb (a) = a document counting people or households actually relocated. Limb (b) = a specific
documented harm to identifiable people.

| Lead | Case | Limb | Bucket after check |
| --- | --- | --- | --- |
| 17 | jiangxi-third-highway-resettlement | (a) — 747 households "who had to relocate their houses" | (b) |
| 18 | trung-son-hydropower-resettlement | (a) and (b) — 695 households relocated; two deaths during construction | **(a)** |
| 19 | ningxia-highway-compensation-delays | (b) — compensation payment delayed; land taken from 261 counted households | **(a)** |
| 21 | zhejiang-urban-environment-resettlement | (a) — 4,628 people affected by house demolition, all resettled per the plans | (b) |
| 31 | hubei-yiba-expressway-resettlement | (a) — 1,038 families relocated | (b) |
| 35 | vietnam-road-asset-management-resettlement | (a) and (b) — 105 households relocated; land clearance not carried out, resettlement pending at closing | **(a)** |

Bucket (b) after checking: leads 17, 21 and 31. Three compliant resettlements at documented scale,
with no failure recorded in any document opened. They are for the owner to decide on.

### Lead 19 Ningxia — ruled KEEP (the writer's own weakest, and it said it would not argue if cut)

Both quoted findings verified in the Evaluation Group's review:

- "Non-agreement a priori on compensation rates for the project-affected people at appraisal
  contributed to delays in payment of compensation during implementation." The draft wrote "before
  approval"; the document says "at appraisal". Corrected.
- "The ICR however provides no evidence on the actual number of people who were compensated as
  compared to the number identified at appraisal and provides no evidence whether the funding
  provided was adequate."

Also verified: the completion report's "land acquisition and house demolition for the project was
completed in 2013 and water and sewer services to relocated households were restored in 2014"; a
footnote saying compensation was paid to all relocated households while the housing, paved roads,
water and sewerage were still in progress; the quality-of-ICR rating Modest; the three further
quoted criticisms.

The case keeps on limb (b). Late payment of compensation is one of the harms the refined rule names
by name, and it is stated as having happened by the Bank's own evaluators, not predicted. The
infrastructure for relocated households came a year after their houses went. **The draft's absence
claim was too strong and is corrected:** the completion report's Annex 2 does carry one actual
household figure — "Land Acquisition of GQE affected 261 households (49 households fewer than
expected)". The report does not say whether those households were relocated, and does not say which
appraisal figure the 49 is measured against (appraisal expected 2,395 households affected by
permanent land acquisition and 310 households relocated). The 261 is printed in `community` and
`displaced_note` with the document's own label, and no derivation is asserted. `displaced` is left
absent, because no figure in the record is labelled as people or households relocated.

### Does the Ningxia-equals-appraisal finding hold? Yes, and there is a second one

The Evaluation Group's review states: "A total of 2,395 households and 10,436 people from 32
villages were expected to be affected by permanent land acquisition, and 59,695 square meters of
houses were to be demolished and 1,429 people in 310 households were to be relocated." ICIJ's
10,436 is that appraisal estimate to the person. **Confirmed.**

**A third exact match, found in this check, is stronger still.** Trung Son's appraisal document of
March 2011, paragraph 89, says: "About 2,327 households or 10,591 people will be resettled from
reservoir area, access road, dam construction sites, borrow pits and workers' camps." ICIJ's figure
for the project is 10,591, to the person — and here the appraisal's verb is "resettled". The outcome
was 695 households relocated against 2,327 planned. The draft had guessed instead that ICIJ's 10,591
tracked the completion report's "approximately 10,600 people (3,413 households) directly or
indirectly"; that guess is replaced with the verified appraisal figure. Both Ningxia and Trung Son
belong in the project's permanent notes beside Liaoning.

### Lead 17 Jiangxi — ruled KEEP

747 is verified in Annex 7, "Summary of Borrower's ICR", and the card says so. It is the only count
of households moved in the file. Added: the report's own statement that resettlement on the local
roads component was "small, and was effectively carried out", which is as close as the Bank comes to
a project-wide figure; that the Bank's Annex 5 figures are taken from the Resettlement
Implementation Report of August 2009 by the Center for Involuntary Resettlement Research at Wuhan
University, the project's independent monitoring organisation (the draft credited that body only
with satisfaction surveys); the borrower's own arithmetic, where 606 rebuilt plus 142 rebuilding
plus 1 not rebuilt makes 749, not 747, and the same passage then refers to three unrelocated houses
where it had said one; a second named place, Dongtian village, Maodian town, Gan county, with the
RMB 3,600 self-relocation allowance and the lottery used to settle site disputes; and the annex's
table of relocated households' own ratings at 14 named sites, where 9.1 per cent said they were
dissatisfied and 3.4 per cent very dissatisfied overall, 40 per cent dissatisfied at Tianxin and
23.1 per cent very dissatisfied at Shuiduan. Loan figures corrected: the report gives US$189.7
million disbursed against a commitment revised to US$195 million, while the Evaluation Group's table
gives the loan's actual amount as US$187.8 million and US$12.2 million cancelled, of which the
US$5 million misprocurement cancellation was part. Both are printed.

## The two label substitutions, and two more

Verified side by side in the ratings tables:

- **Zhejiang.** Completion report summary: risk to the development outcome **Modest**. The Group's
  table prints **Moderate** in the report's own column. Held.
- **Yiba.** Completion report summary: **Moderate**. The Group's table prints **Modest** in the
  report's column. Held.
- **Ningxia.** Completion report summary: **Negligible to Low**. The Group's table prints
  **Negligible** in the report's column. Held.
- **A fourth, found here.** Jiangxi's report summary says **Low or Negligible**; the Group's table
  prints **Negligible to Low** in the report's column. Added to that card.

## The two in-document conflicts

- **Yiba.** Main text: "By project completion 4,325 persons (1,038 families) were relocated". Annex
  10: "Some 1,038 families were relocated, involving 3,736 persons." Same households, same date, no
  explanation. Genuine; kept, both printed.
- **Trung Son.** Text: "total compensation of VND 541.3 billion ($24.98 million) had been paid (see
  table 5)". Table 5 totals VND 581,250 million for the same US$24,977,438. Genuine; kept, both
  printed, and the card now notes that the text itself points the reader to the table.

## Most serious corrections

1. **Two deaths the draft did not carry (lead 18).** The Trung Son completion report, paragraph 88:
   "The TSHPP recorded two fatalities during the construction period. The first fatality was because
   of a fall by a construction worker, while the second fatality was due to a vehicular accident on
   January 17, 2014, at the project site. The families of both victims were appropriately
   compensated." `killed` set to 2, with the report's own wording in `killed_note`. The storm death
   of 2018 stays uncounted, as the draft had it. This also moves the case to bucket (a).
2. **The draft's "most serious thing in the batch" does not hold as framed (lead 35).** The Group's
   safeguards section says: "Overall, according to the ICR, the project complied with the
   environmental safeguard policies, and safeguards compliance during project implementation was
   rated Satisfactory or Moderately Satisfactory (ICR p.24)." Page 24 of the completion report does
   say, in paragraph 68, that "the project complied well with the environmental safeguard policies"
   and that "safeguards compliance during project implementation was rated as between 'Satisfactory'
   and 'Moderately Satisfactory'". So the page citation is accurate and the Group is not
   misreporting the page. What is true, and now on the card, is that page 24 also carries the
   report's rating of environmental safeguards as **Moderately Unsatisfactory** at closing, that the
   matching **Moderately Unsatisfactory** rating for social safeguards is on page 25, and that the
   Group's safeguards section carries neither. The draft placed both ratings on page 24 and
   presented the Group as contradicting the page it cites.
3. **An invented conflict removed (lead 31).** The draft said the Yiba report gives the 35 and 65
   per cent split of resettlement choices "the other way round" elsewhere in the annex. It does not.
   Annex 10 says "35 % of the displaced families preferred to be relocated into resettlement
   centralized sites and 65% preferred to be back-up relocations in their original villages", and
   later "over 35% of displaced families were relocated into the new sites and 65% were relocated in
   their original villages". Same direction, one in intention and one in outcome. Removed.
4. **A figure that said the opposite of the indicator (lead 35).** The draft wrote that "of 6,661
   affected households that were direct beneficiaries for compensation, 87.09 per cent were
   female-headed". The report's results framework shows 87.09 per cent is the share of affected
   households with a woman attending consultation on compensation and resettlement, against a target
   of 80 per cent, worked out in the report itself from 6,671 of 7,660 affected households. The
   report's narrative text does garble it as female-headed households; the card now gives the
   indicator and notes the text's wording. The 7,660 is also printed beside the safeguards section's
   4,672 affected households, without reconciling them.
5. **Wrong attribution and wrong count of environmental ratings (lead 18).** The draft said the
   Evaluation Group rated seven of ten environmental triggers Satisfactory and three Moderately
   Satisfactory. The completion report, paragraph 43, says that at project closing three of seven
   were Moderately Satisfactory and the remaining four Satisfactory. Corrected and reattributed.
6. **Yiba road length (lead 31).** The connecting roads are 35.4 km in the completion report's main
   text and in the Group's review; 44.1 km appears only in Annex 10. The draft used 44.1 km twice.
   Main figure used, annex variant noted once.
7. Unverifiable "loan agreement conformed on …" clauses removed from four cards. Jiangxi, Ningxia,
   Zhejiang and Yiba now carry only approval, effectiveness, restructuring and closing dates taken
   from the reports' own key-dates tables.
8. Smaller additions from the documents: the Yiba misprocurement described concretely (eight
   subgrade contracts, about US$120 million, 80 per cent of the loan, declared without cancellation,
   financed by the borrower, proceeds reallocated to pavement, traffic facilities and electrical and
   mechanical works); the three named environmental non-compliance incidents on Yiba (asphalt-plant
   waste dumped in a river in February 2012, tunnel spoil in a flood channel in March 2012, an
   unapproved spoil deposit at Liangshuijing in October 2013); the Zhejiang comparison table's
   second, different per-sub-project breakdown; the Trung Son integrity report's third finding, on
   the environmental specialist's availability; and on lead 35 the Inspectorate's finding of a risk
   of loss and waste, the percentage sizes of the two capital cuts, where it places responsibility,
   and the Government Office's November 2024 notice to Quang Tri province.

## Independent source on lead 35 — verified

Government Inspectorate conclusion 375/KL-TTCP of 14 October 2025 exists and is reported by Bao
Thanh tra on 18 November 2025 under the headline given. Verified in the article: the project is the
upgrading and widening of National Highway 9 from Cua Viet port to National Highway 1 in Quang Tri;
compensation, support, resettlement and land clearance were split into a separate sub-project and
left out of the approved investment totals, which the inspectorate holds to breach the Construction
Law 2014, the Public Investment Law 2019 and two decrees; "some land clearance sites were late, some
could not be cleared for handover to the construction unit", so the project fell behind, did not meet
its investment objective, was not granted a loan extension by the World Bank and "has been stopped
since 31 December 2022"; "one of the causes of the above was that the Quang Tri provincial people's
committee did not carry out land clearance as committed"; capital cut by VND 50,000 million in 2022
(23.25 per cent) and VND 48,909 million in 2023 (85.80 per cent); and the recommendation that
leaders at the construction ministry, the finance ministry and Quang Tri province be reviewed and
held to account. One correction of attribution: Bao Thanh tra is the Government Inspectorate's own
newspaper, not a general state newspaper, and the card now says so. The text of the conclusion
itself is not public, so the findings are given as the newspaper reports them. `confidence` stays
`documented`: the land clearance failure is recorded both by the Bank's completion report (National
Highway 9 cancelled for delayed land acquisition and resettlement, social safeguards Moderately
Unsatisfactory for pending resettlement) and by a body outside the lender. 105 relocated of 4,672
affected households verified in the report's paragraph 71.

## Lead 18 — ICIJ correspondence and duplication

The draft's suggested correspondence between ICIJ's 10,591 and the report's "approximately 10,600
people (3,413 households) directly or indirectly" was a coincidence of rounding; the real match is
the appraisal's 10,591 people to be resettled, set out above. No derivation is asserted on the card
beyond quoting both documents.

Duplication: no hydropower case on the map is within 120 km of the dam. The nearest existing cases
are cat-linh-ha-dong-accidents (109 km), vietnam-rural-energy-2-land-loss (111 km) and
vietnam-distribution-efficiency-five-households (114 km), all different projects; and in this round's
other batches vietnam-medium-cities-phu-ly-noncompliance (112 km). None is the same episode.

## Coordinate neighbour — verified

three-gorges-eca sits at 30.8346, 111.0666, which is 33.0 km from the Yiba corridor point at 30.95,
110.75. Different project (the Three Gorges dam and European and Canadian export credit, 1996-2008)
and different years from the 2009-2016 expressway. The Yiba `point` field said so and now names the
existing case and its years. No other case in `cases.json`, `out_G1.json` or `out_J.json` is within
120 km of any of the six points except as listed above.

## Drops — all four upheld

- **Lead 23, Meizhou Bay.** The report states that the Bank-financed project caused no physical
  resettlement and that no household relocation was required. The 987 households / 5,016 persons are
  livelihoods affected, and the borrower's section shows the bulk of that is 2,040 mu of sea area
  reclaimed by the government under linked activities, affecting 5,006 persons in 986 households,
  with the Bank-financed works themselves affecting one household of 10 persons. Compensation and
  livelihood restoration are recorded as completed by the end of August 2018 and consistent with the
  plan. Neither limb: nobody counted as moved, and no harm recorded as unremedied. The reason now
  states the linked-activities point, which also weakens the link to the loan.
- **Lead 28, Yunnan Urban Environment.** The only household figure is the appraisal's 376 households
  / 1,570 people, and the report says that resettlement was carried out under the client-financed
  Component 3. Demolition came in 41,724 square metres below plan, so the appraisal estimate cannot
  stand as an outcome. No petition or appeal recorded. Neither limb.
- **Lead 30, Poyang Lake.** 10,873 counts people affected including land acquisition and relocation;
  relocated households are described in percentages but never counted. Compensation fully disbursed,
  house compensation above plan standards in three counties, no failure recorded. The integrity
  report concerns a debarred bidder, as the draft said — verified. Neither limb.
- **Lead 36, Taiyuan.** The interesting one, and still a drop. The monitor's finding of
  31 December 2013 is real and is quoted in the reason: Taiyuan Municipality "did not adequately
  compensate for land belonging to state-own enterprises and institutes, and thus was not in
  compliance with the project Resettlement Action Plan". But limb (b) requires harm to identifiable
  people, and the land in that finding is held by state-owned enterprises and institutes; the word
  "household" does not appear once in the note's 760 lines, so no person or household is identified
  or counted. Nothing was disbursed from the loan but the US$375,000 front-end fee, and the borrower
  went on to finance Taihang Road with domestic funds. A non-compliance finding over institutional
  landholdings, with nobody counted and no loan money spent on the works, is not a case. If the
  owner later decides that a documented safeguards non-compliance is itself mappable regardless of
  who held the land, this is the lead to revisit, and the quoted finding is preserved in the drop
  reason for that purpose.

## Pattern worth carrying forward

Three of this round's ICIJ figures are now verified as exact appraisal estimates: Liaoning 31,547,
Ningxia 10,436 and Trung Son 10,591. In each case the outcome recorded later is a fraction of it
(Liaoning 2,467 households, Ningxia 261 households counted at all, Trung Son 695 of 2,327 planned).
The check that pays is to search the project's appraisal document for ICIJ's exact digits before
anything else — in two of these three the match was in the appraisal document, not in the completion
report or the validation, so a writer who reads only the completion documents cannot find it.

Second pattern: the Evaluation Group's ratings table does not always print the completion report's
own words in the report's column. Four of the six projects in this batch show it. It is worth
checking the report's own ratings summary against the Group's table every time, and printing both.
