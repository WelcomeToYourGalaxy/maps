# Fact-check log: whole-picture paragraphs, r18 batch of 8

Method: all eight writer PDFs re-extracted from disk with `pdftotext -layout` into a separate
directory and read there (ratings tables, efficiency sections, rate-of-return tables with their
coverage columns, results frameworks). Document lists and Project Performance Assessment Report
searches run against `search.worldbank.org/api/v3/wds`. All 17 source URLs fetched and returned
HTTP 200. No web page was used for a fact that is not in a document read from disk.

Result: 8 of 8 paragraphs corrected. 0 kept unchanged, 0 blanked. `self_reported` stays true on
all eight, and every paragraph now carries the sentence saying no independent check was found.

## Ratings: what the two columns actually say

Read side by side from each review's ratings table plus each document's own efficiency and
relevance ratings (the newer review template has no efficiency or relevance row, so those were
read from the body text of both documents).

| Project | Completion report | Independent Evaluation Group |
|---|---|---|
| P086801 Bumbuna | outcome MU, Bank perf. MU, efficiency **low** | outcome **U**, Bank perf. **U**, efficiency **Negligible** |
| P079734 East Africa | outcome MS, risk **Modest** | outcome **MU**, risk **Substantial** |
| P112334 Uganda ERT2 | outcome MS, efficiency **Substantial** | outcome **MU**, efficiency **Modest** |
| P091077 Ethiopia APL3 | outcome MS, Bank perf. MS, borrower **MS** | outcome MS, Bank perf. MS, borrower **MU** |
| P119737 Kawanda-Masaka | outcome MS, efficiency Modest, relevance **High** | outcome MS, efficiency Modest, relevance **Substantial** |
| P113542 KISIP | outcome S; efficiency **Substantial** in its efficiency section, **High** in its summary | outcome S, efficiency Substantial |
| P117635 Lower Nzoia | outcome MS, efficiency Modest | outcome MS, efficiency Modest |
| P112158 Upper Cisokan | outcome MU, efficiency Modest | outcome MU, efficiency Modest |

Disagreements the writer reported: all five verified (Bumbuna outcome and Bank performance;
East Africa outcome and risk; ERT2 outcome; Ethiopia borrower performance; Kawanda relevance).

New disagreement the writer missed and reported as agreement: **P112334 efficiency**. The
completion report rates efficiency Substantial (section 3.3, "Rating: Substantial", repeated in
its overall-outcome justification); the review rates it Modest. The writer wrote "both rating
efficiency Modest". Corrected.

Label substitutions: none found in this batch. The three "agreements" hold on the labels
themselves: KISIP Satisfactory/Satisfactory, Lower Nzoia Moderately Satisfactory and Modest on
both sides, Upper Cisokan Moderately Unsatisfactory and Modest on both sides. The one soft spot
is KISIP's completion report, which gives its own efficiency as Substantial in one place and High
in another; the paragraph now credits Substantial to the Evaluation Group only and makes no claim
about agreement on efficiency.

Also corrected: Bumbuna. The writer credited Negligible efficiency to the Evaluation Group
correctly, but gave no completion-report column. The completion report rates efficiency "low".
Both columns are now shown.

## Rulings on the writer's four flagged uncertainties

1. **Bumbuna internal inconsistencies.** Board approval: real but one-sided. The review's text
   says "approved by the Board on July 16, 2005"; the review's own data table says 06/16/2005 and
   the completion report's data sheet says Approval 06/16/2005. Two data tables against one line
   of prose. Does not belong on the card. Restructuring count: **the claimed conflict is not
   real.** The review says "6 restructurings" and the completion report's restructuring table
   lists exactly six dates (26 Jun 2008, 24 Jul 2009, 30 Dec 2009, 25 Jun 2010, 28 Sep 2010,
   20 Sep 2012). Nothing in either document says seven. Kept off the card — but see the note to
   the owner below, because the case card itself says "restructured seven times".
2. **East Africa coverage.** The paragraph cannot stand without it, so it is now in. The
   inconsistency is real on its face and resolvable: the analysis covered US$118.36 million, which
   is 60 per cent of the US$197.62 million appraisal cost total used in the review's efficiency
   section and 42 per cent of the US$281.67 million appraisal cost total the same review quotes
   from the appraisal document. Two denominators, one numerator. The paragraph gives the dollar
   figure and both percentages and says which document part each comes from, rather than picking
   one.
3. **Ethiopia 498 / 509 / 499.36 km.** The writer is right. 498 km is the results-framework figure
   for road upgraded against a 509 km target, and the review itself breaks it down as 99 + 268 +
   131 km. The 499.36 km on the card is the sum of the six contract lengths. One quantity,
   1.36 km apart in two accountings; not a conflict, and the target comparison is the one that
   belongs in a delivery paragraph.
4. **Lower Nzoia rates of return.** The writer's before-and-after was misleading and is fixed. The
   paragraph now states the appraisal rate with its 20-year horizon and 12 per cent discount rate
   and the closing rate with its 30-year horizon and 6 per cent discount rate, and says plainly
   that the two rest on different assumptions. There are not three rates but five: 14.6 per cent
   at appraisal, 13.8 per cent at the 2015 additional financing (10 per cent discount rate),
   8.9 per cent when US$70 million was cancelled in 2019, 24.61 per cent at the 2023 additional
   financing (8 per cent discount rate), 13.81 per cent at closing. All five are now listed, so no
   selection is being made on the owner's behalf.

## PPAR absence: holds

No Project Performance Assessment Report exists for any of the eight. Full `projectid` document
lists pulled for all eight (P079734 127 docs, P113542 175, P117635 129, P119737 55, P112158 52,
P112334 50, P086801 32, P091077 31): the only Evaluation Group document in any of them is the one
Implementation Completion Report Review already used. Separate searches of the "Project
Performance Assessment Report" document type for East Africa trade and transport facilitation,
Kenya informal settlements, Bumbuna, Uganda energy for rural transformation, Upper Cisokan
pumped storage, Kenya water security, Uganda electricity transmission and Ethiopia road sector
returned nothing covering these projects. The two projects whose reviews recommend an assessment
(P079734 and P113542, both "Assessment Recommended? Yes") have none. The nearest hit is the
2008 "Ethiopia - Road Sector Development Program" assessment, seven years before APL3 closed; not
used, as the writer said.

## Per-entry changes

- **bumbuna-hydro-reservoir-resettlement** — text changed. "The dam was commissioned" to "The
  plant was commissioned" (the completion report's sentence is about the hydroelectric plant).
  Completion-report efficiency rating ("low") added beside the Evaluation Group's Negligible, so
  both columns appear. Design figures (50 MW installed power, 315 GWh average annual energy) were
  checked in the appraisal document, which is cited. Long sentences split.
- **kawanda-masaka-line-galatiya** — text changed. **606 GWh corrected to 605 GWh**: the
  completion report's results table gives 605.01 and its annex 605.00 against the 617.4 target;
  606.0 is the review's rounding, which the writer used without saying so. Added that the rate of
  return covers the transmission line component alone, 83 per cent of project cost at appraisal
  and 79 per cent at completion. Added the verified relevance disagreement (High against
  Substantial). "Fortuitous" replaced with the plain fact: a large part of the saving was
  unplanned, from falls in world steel and aluminium prices.
- **kibera-mukuru-railway-relocation** — text changed. Coverage of the 26 per cent appraisal rate
  added, with both the review's figures and where each comes from. "Twelve planned" softened to
  what the review says ("appear to have been planned"). Self-reported sentence completed.
  Sentences split. Figures checked: dwell times 13 to 3 days at Mombasa and 18 to 7 at
  Dar es Salaam, Malaba 45 hours to 2.1 hours, five posts 50 per cent complete and two not
  started, transit and market-share targets not met, US$139 million invested, losses above
  10 per cent of revenue since 2011, 26 per cent and 49 per cent.
- **kisip-informal-settlements-fatalities** — text changed. The tenure-security figure (125,525)
  and the beneficiary figure (1,389,980) are both from the beneficiary survey the project
  commissioned, not from the Bank's own results count; attribution fixed. 26,148 "construction
  jobs" changed to "jobs on construction sites", the review's own wording (it describes the same
  26,148 elsewhere as jobs under the government's hygiene programme, so the characterisation was
  not safe). What the analysis measures added. The 38 per cent is identified as the review's data
  table figure for the same analysis. Efficiency now credited to the Evaluation Group only.
- **lower-nzoia-irrigation-unpaid-compensation** — text changed. The derived "60 per cent of the
  original 4,043 hectares" removed (the review gives only the raw "2,457 out of 4,043 ha"; the
  arithmetic is 60.8 per cent). Horizons and discount rates added for both rates, with the three
  intermediate re-estimates. The monitoring-station finding is credited to the review, which
  sources it to an ICR interview of 25 February 2026, not to the completion report's text. Target
  for produce marketed given as the document states it (2,683 million Kenyan shillings, about
  US$30 million). Self-reported sentence completed.
- **rsdp-apl3-road-deaths** — text changed. Coverage of the rate of return added (93 per cent at
  appraisal, 94 per cent afterwards). Bank performance added, so the borrower-performance
  disagreement is read against a full column rather than outcome alone. The Evaluation Group's
  reason for the downgrade (no evidence of compliance with the involuntary safeguard requirements)
  was deliberately left out: it is already on the card's outcome field. Self-reported sentence
  completed. All output figures verified: 498 against 509 km, 5,764 jobs with about 13 per cent
  women, 70 to 91 per cent against 82, traffic 174 / 123 / 299 per cent, road fund 258.2 to 1,200
  million birr against 1,075 million, 16.5 to 27.1 per cent, 151 per cent time and 12.4 per cent
  cost overrun.
- **uganda-ert2-grid-compensation** — text changed, most substantially. The efficiency ratings
  disagree (Substantial against Modest) and were reported as agreement; fixed. The Uganda Bureau
  of Statistics point was garbled: the survey is the basis on which the **target** was raised from
  6 to 7 per cent, and it is the rise in rural electrification, not the 7 per cent figure, that
  the review says cannot be fully attributed to the project. The 12 per cent rate is now said to
  cover two of the three components, and the third benefit stream (avoided peak load demand) is
  included. The ratings sentence now leads with the Evaluation Group, because the card's outcome
  field already carries the Bank's own Moderately Satisfactory. Self-reported sentence completed.
- **upper-cisokan-pumped-storage-land** — text changed. Removed the restatement of the loan
  cancellation and of the plant not being built, both already on the card's outcome field; what
  stays is the zero reading on the peaking-capacity indicator and what was delivered. Chronology
  corrected: the dispute took from 2016 to 2021 to resolve, and the writer's wording put the
  cancellation after it (the loan allocation for that component was cancelled in May 2017 and the
  component was dropped at the 30 December 2018 restructuring); the paragraph now does not imply
  an order. Added that the three procured contracts came in up to 25 per cent below estimate and
  were carried to a later loan, which is part of what the money produced. Coverage of the 19 per
  cent rate added (84 per cent of project cost). The documents do not state the benefit streams
  behind that rate beyond its sensitivity to investment costs and fuel prices, so no description
  of what it measures was invented; the paragraph calls it a cost-benefit analysis of the plant.
  Self-reported sentence completed.

## Checks that found nothing to change

- No harm duplication left. Nothing about deaths, unpaid compensation, armed police, evictions or
  the energization and de-energization of the Kawanda-Masaka line appears in any paragraph; the
  only overlaps found were the Upper Cisokan loan cancellation and "the dam was not built",
  which were cut.
- No harm source was turned into a delivery source. `sources_add` across all eight contains only
  World Bank and Independent Evaluation Group documents plus the Bumbuna appraisal document. The
  thesis, the Amnesty International urgent action, the Daily Nation, Daily Monitor, The Star,
  Republika and iNews stay where they are, on the harm.
- Every `sources_add` entry is used for a fact in its paragraph, and all 17 URLs return HTTP 200.
  The Bumbuna appraisal document is cited for the 50 MW and 315 GWh design figures.
- No rate of return is described as a benefit to anyone displaced. Each paragraph now says what
  the documents say its rate counts, except Upper Cisokan, where they do not say.
- No first person, no process narration, no sentence addressed to an editor, and no opinion words
  in any paragraph.

## Two notes for the owner, outside these paragraphs

- The Bumbuna case's `lenders` field says the project "was restructured seven times". The
  completion report's restructuring table lists six restructurings and the review says six.
- The Kibera/Mukuru case's `lenders` field says "Outcome was rated Moderately Unsatisfactory
  (World Bank Implementation Completion and Results Report, 27 September 2016; Independent
  Evaluation Group ICR Review, 9 May 2017)". The completion report rated the outcome Moderately
  Satisfactory; Moderately Unsatisfactory is the Evaluation Group's rating alone.
