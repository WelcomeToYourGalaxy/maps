# Round 19 — `whole` field for the 18 ICIJ-3 land/compensation cases

All 18 ids written to `/home/claude/r19/whole_out.json`, every value non-empty. No merge, no build, no push.

## Method
Every figure was read from a document on disk under `/home/claude/r19/dl`, extracted with `pdftotext -layout`
(the files were already downloaded in an earlier step of this round). No PDF was read through a fetch tool and
no web search was needed: all documents cited on the 18 cards were present locally. Documents used, by case
prefix: `ceip_*`, `pmsip_*`, `nprsdp_*`, `kp_*`, `sidd_*`, `gshp2_*`, `punjrd_*`, `tnudp_*`, `assam_*`, `cd_*`,
`gh_w_*`, `bf_*`, `rw2_*`, `kz_*`, `vn_hanoi_*`, `br_bahia_*`, `bo_*`, `ph_*`.

Completion-report ratings were read out of each completion report's own ratings summary or its
"Justification of Overall Outcome Rating" table, never out of the Independent Evaluation Group's data sheet.
Group ratings were read out of each review's own `a. Outcome Rating` line. No rating is stated citing both
documents.

Every one of the 18 rests on the Bank reporting on its own project, so each paragraph says the figures are the
lender's own and that no independent check was found. Three cases have no disclosed completion report
(Gujarat, Dehlon/Punjab, Burkina Faso); those paragraphs say so and attribute the figures to the review.
Two cases have no Group review at all (Siddhirganj, Rwanda RSSP2); Rwanda's figures come additionally from the
project's own resettlement report, which the paragraph flags as the implementer's own work.

Each review was grepped for "informed IEG", "the project team", "the World Bank team stated", "team
confirmed" and "clarified that" before any figure was taken from it. Hits that bear on these paragraphs:
`ph_ieg` (the 77 per cent road-condition figure — attributed in the text to the project team, not to a
document), `punjrd_icrr` (compensation state — not used as a delivery figure), `gshp2_icrr` (safeguard
compliance — not used), `kz_ieg` (M&E, safeguards, procurement and a disbursement-variance explanation dated
29 August and 19 September 2025 — none used), `ceip_icrr` and `assam_icrr` (task-team clarifications — none
used as delivery figures). No delivery figure in any paragraph comes from a staff statement.

## Figures where two documents disagree
Only one true conflict of quantity was found.

1. **Philippines NRIMP-2 — share of national roads in good or fair condition at completion.**
   - 55 per cent, "No change from baseline", against a revised target of 60 per cent — World Bank,
     Implementation Completion and Results Report (P079935), June 2017, PDO indicator table, Indicator 2.
   - 77 per cent, "exceeding the project target of 60 percent" — Independent Evaluation Group, ICR Review
     (P079935), 20 November 2017, which attributes the figure to what the project team told the evaluators.
   Same indicator, same measurement point (completion). Both figures are given in the paragraph, with the
   attribution of the second. The documents do not explain the gap and no explanation is offered here.

Ratings on which the two documents differ (each named with its own document in the paragraph, never merged):
- Lahore / Punjab Municipal Services: completion report 19 May 2014 Satisfactory; Group review 2 June 2015
  Moderately Satisfactory.
- Salem / Third Tamil Nadu Urban Development: completion report Satisfactory; Group review Moderately
  Satisfactory.
- Assam State Roads: completion report 25 March 2020 Moderately Satisfactory with efficiency Modest; Group
  review 26 June 2020 Satisfactory with efficiency substantial.
- DRC Emergency Multisector Rehabilitation: completion report 29 October 2010 Satisfactory; Group review
  Moderately Satisfactory.
- Bolivia National Roads and Airport: completion report 31 May 2024 Moderately Satisfactory; Group review
  Moderately Unsatisfactory.

## Comparisons deliberately NOT written up as conflicts
These are before-and-after pairs or recalculations with a method change, not contradictions, and are written
that way:
- Appraisal versus completion rates of return: CEIP, Nepal (41.1 and 29.4 per cent at completion against 29.4
  and 23.4 at appraisal), Assam, Gujarat (51.9 against 35.1), Punjab (31.8/28.5/50.4 against 36.5/44.2/58.4),
  Burkina (15.3 against 14.3), Kazakhstan (15.6 against 13), Hanoi (ring road 18.5 against 14.5; bus rapid
  transit 6.0 against 21.0), Bolivia (13.0 against 15.5), Siddhirganj (26.33 against 31), Philippines (23.4
  against 27), Bahia (16 against 33.9–37.6).
- Gujarat's net present value, Rs 20.2 billion after closing against Rs 21.3 billion at appraisal: the review
  cites the completion report's own explanation (lower costs, and 25 km less road measured), so that
  explanation is attributed, not invented.
- Ghana's rate of return, 26.18 per cent at completion against 21 per cent in the appraisal document: the
  completion report itself states the appraisal figure used a different timeframe and exchange rate.
- Bahia's rate of return: the Group review states the completion report could not use the appraisal's hedonic
  price method because price data were missing. The method difference is reported; no reconciliation of the
  numbers is attempted.
- Swat's 29.9 and 28.0 per cent are appraisal estimates only; the Group review records that no rate of return
  was estimated at completion, and the paragraph says so rather than treating the appraisal figures as results.

## My own two weakest paragraphs
1. **`dehlon-bypass-uncompensated-landowner`** — the weakest. There is no disclosed completion report, so
   every figure is the Group review's summary of a document the public cannot read. Worse, nothing in the
   paragraph is about the Dehlon bypass itself: the 711 km, the 347 black spots, the network speed and the
   fatal-accident series are all state-network figures, and the fatal-accident rise from 2,655 to 5,077 is a
   network count with no established relation to the project's works. The paragraph gives context for the
   loan, not for the plot the bypass crossed.
2. **`gujarat-highway-ii-delayed-compensation`** — also rests entirely on a review of an undisclosed
   completion report, and is thin on what the roads did for people: the only user-facing figures are journey
   times per 50 km and a surface-roughness reading. There is no beneficiary count, no traffic figure and no
   independent measurement of anything.

Third weakest, for the record: **`lahore-walled-city-shop-removals`**. The delivery figures that exist are for
the loan's municipal-services side (water connections, landfill share, four sub-project rates of return) and
not for the Walled City street works where the shops were removed. No document found gives a rate of return,
a visitor count or a trade figure for the Shahi Guzargah itself.
