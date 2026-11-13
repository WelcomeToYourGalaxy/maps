# Fact-check log: whole_out_2.json -> whole_checked_2.json

12 paragraphs checked. **0 kept unchanged, 12 corrected, 0 blanked.**
Every document was read from the `pdftotext -layout` text already on disk under
`/home/claude/r17/chk/`, `/dlD/`, `/vfy/` and `/dl/`. No fetch tool was used.
Each file's project id and report number were confirmed from the text before use:

| case | completion report | Evaluation Group | file |
|---|---|---|---|
| Lucknow-Muzaffarpur | ICR2475, P077856 | ICRR14100 | chk/lucknow_* |
| Ethiopia RSDP IV | ICR00004205, P106872 | ICRR0021231 | chk/eth_apl4_* |
| Naji / 4th Inland Waterways | ICR1376, P077137 | ICRR13857 | dlD/iw4_*, vfy/iw4_* |
| NanGuang Railway | ICR00003432, P112359 | ICRR0020097 + PPAR 127580 | dlD/ng_*, vfy/ng_* |
| NHIIP | ICR00005937, P121185 | ICRR0023078 | chk/nhiip_*, vfy/nhiip_* |
| Orissa State Roads | ICR00003903, P096023 | ICRR0020654 | chk/orissa_* |
| Shaanxi Ankang | ICR2142, P075613 | ICRR14449 | dlD/ank_*, vfy/ank_* |
| Shiyan / Hubei Shiman | ICR00001409, P081749 | ICRR13442 | dlD/shiyan_* |
| ShiZheng Railway | ICR00003435, P099062 | ICRR0020495 | dlD/sz_* |
| Vietnam Distribution Efficiency | ICR00004664, P125996 | ICRR0021771 | vfy/vn_dep_* |
| Vietnam Rural Energy 2 | ICR00003194, P074688 | ICRR14722 | vfy/vn_re2_* |
| Vietnam Water Resources | ICR00002604 (not on disk) | ICRR14273 + PPAR 138389 | vfy/vn_wrap_*, dl/000020051-20140626114618 |

## 1. Rating disagreements

Verified from the two columns printed side by side in each Evaluation Group review.

**Survive as reported:**

- **Lucknow-Muzaffarpur (P077856).** Group's table: Outcome - report Moderately
  Unsatisfactory, Group Unsatisfactory. Bank Performance - report Moderately
  Unsatisfactory, Group Unsatisfactory. "M&E Quality Rating: Negligible". The report's own
  rating sheet gives Outcomes, Bank Performance and Borrower Performance all Moderately
  Unsatisfactory, so the Group's table is an accurate copy here. Risk to Development
  Outcome is Significant in both columns. All three claims correct.
- **Orissa (P096023).** Group: "Efficacy is rated as negligible", "Outcome Rating:
  Unsatisfactory". The report's rating sheet and its section 3.4 give Moderately
  Unsatisfactory. The substantive disagreement is real.
  **The writer's finding about the table is confirmed:** the Group's ratings table prints
  the ICR column as "Outcome: Unsatisfactory" with "---" in the disagreement column, while
  the report itself says Moderately Unsatisfactory. The table therefore records agreement
  where there is a disagreement. The Group's narrative rating is Unsatisfactory on its own
  reasoning, not borrowed from the report. The paragraph as written (Group Unsatisfactory
  against the report's Moderately Unsatisfactory) is right, and is more accurate than the
  Group's own table. Two corrections made: Bank Performance is Moderately Unsatisfactory in
  **both** columns, so there is no disagreement there; and a real disagreement the writer
  missed was added - Risk to Development Outcome, report Modest against the Group's
  Substantial.
- **ShiZheng (P099062).** Table: Outcome Satisfactory/Satisfactory; Risk to Development
  Outcome - report Negligible, Group **Modest**, the stated reason being that the Group
  rated social risk modest rather than negligible because "attitude surveys may not have
  captured the real price elasticity of demand". Bank and Borrower Performance
  Satisfactory/Satisfactory. Correct as reported.
- **Ethiopia RSDP IV (P106872).** Table: Outcome Moderately Satisfactory both; Bank
  Performance Moderately Satisfactory both; Quality of M&E - report Substantial, Group
  **Modest**, "Due to shortcomings in design and utilization of the M&E indicators".
  Correct. A second disagreement was added: the Group rates **efficiency Modest** where the
  report rates it Substantial, citing the dropped 89 km road and the cost overruns.
- **Shaanxi Ankang (P075613).** Confirmed: outcome Moderately Satisfactory in both, with
  Bank and Borrower Performance cut from Satisfactory to Moderately Satisfactory and risk
  raised to Moderate. Left out of the paragraph, correctly, because the case's own outcome
  field carries the full set with the Group's reasons.

**Mislabelled or reversed:**

- **Naji (P077137).** The description "Bank and borrower performance cut from Satisfactory
  to Moderately Satisfactory ... expressly for insufficient assessment of needs and process
  requirements for land acquisition" describes the Group's table, and that table misreports
  the report. The completion report's rating summary gives Bank and Borrower Performance
  **Moderately Satisfactory**; the Group's table enters the report's figures as Satisfactory
  and its own as Moderately Satisfactory, so it shows a cut that did not happen. Both bodies
  in fact reached the same rating. This is already set out in the case's outcome field, and
  the paragraph correctly carries no rating set.
- **Shiyan (P081749).** Every row agrees and the label sets match - Outcome
  Satisfactory/Satisfactory, Risk Moderate/Moderate, Bank Satisfactory/Satisfactory,
  Borrower Satisfactory/Satisfactory.
- **NanGuang (P112359), Vietnam Distribution Efficiency (P125996), Vietnam Rural Energy 2
  (P074688), Vietnam Water Resources (P065898).** All verified as genuine agreement on
  matching labels. Distribution Efficiency: Outcome Highly Satisfactory/Highly
  Satisfactory, Bank Highly Satisfactory/Highly Satisfactory, Quality of M&E High/High.
  Rural Energy 2: Outcome, Risk (Moderate), Bank and Borrower all identical. Water
  Resources: the 2019 assessment's three-column table gives Moderately satisfactory for
  Outcome, Bank and Borrower and Moderate for Risk across report, review and assessment.
- **NHIIP (P121185).** Agreement confirmed; the Group additionally rates the quality of the
  report itself Modest, as the case's outcome field already says.

## 2. The two numeric conflicts

- **Ankang expressway length.** The writer's reasoning holds, and is better supported than
  the writer said. The completion report says "the construction of an 87 km expressway
  connecting Ankang and Maoba". The Group's review says "about 87km" in its own component
  description and "A new 78 km expressway connecting Ankang and Maobao was constructed" in
  an output bullet. The 78 km is contradicted inside the Group's own document, which makes
  it a slip in one bullet rather than a dispute between the two bodies. 87 km kept; the
  discrepancy is recorded in "searched", not presented as a finding.
- **Orissa economic rate of return.** The garbled sentence exists verbatim: "The overall
  ex-post ERR was 25.1 percent compared to the ex-ante ERR of 18.6 percent." The Group's
  own rate table on the same page reads Appraisal 25.10 (95 per cent of cost), ICR Estimate
  18.60 (93 per cent) - the reverse. The figures used in the paragraph are the per-road ones
  both documents agree on: 19.4 against 22.3 per cent for Khariar-Bhawanipatna, 18.6 against
  15.4 per cent for the Berhampur-Taptapani section. Verified.

## 3. The sharpest claims

All six stand, with wording tightened to the documents.

- **Vietnam Rural Energy 2.** Group, outputs and outcomes list: "No study was carried out at
  project closure to assess the project's impact on the socio-economic development of rural
  communities within the selected provinces." The objective it bears on is quoted from the
  appraisal document: "to improve access to good quality, affordable electricity services to
  rural communities, in an efficient and sustainable manner to support Vietnam's efforts
  towards socio-economic development." The same bullet notes the report cites instead a 2011
  study of rural electrification in Vietnam as a whole; that qualification was added.
- **NHIIP road safety pilot.** Group: cost "increased from US$17.50 million to US$72.50
  million to pilot safety enforcement mechanism in the roads upgraded under the project ...
  Given that the actual cost of this component was only US$3.20 million, this review
  concludes that safety enforcement mechanism in the project roads was not piloted."
  Correct. Noted in "searched" that the Group's ICR-quality section gives the allocation as
  US$55 million, inconsistent with its own US$72.50 million.
- **NHIIP road condition.** Group: baseline 65 per cent of 37,501 km; "The achievement is
  reported as 72.80 percent, but the size of the total classified road network increased to
  87,995 km. Therefore the achievement cannot be **fully** attributed to the project's
  intervention." Corrected from "cannot be attributed" to "cannot be fully attributed".
- **NanGuang agglomeration - misattributed, corrected.** The assessment says "About half of
  the project benefits were estimated **at the ICR stage** to be from agglomeration
  effects", and "The Project Appraisal Document and the ICR estimated the benefits from
  agglomeration effects using an approach developed by the United Kingdom Department for
  Transport." The 2018 field mission did not discover this; it tested it, found the
  assumptions consistent with its interviews, recalculated with the effects cut 30 per cent
  and still got 14.1 per cent. The paragraph now credits the half-of-benefits estimate and
  the UK method to the completion report, and adds the report's own figures without
  agglomeration benefits: 11 per cent after the event against 9 per cent at appraisal.
- **Vietnam Distribution Efficiency tariffs.** Group: "the ICR did not discuss the situation
  for household consumers as a result of the increases in retail electricity tariffs since
  the project was approved" - correct. The 53 and 56 per cent figures were **wrongly dated**:
  the Group quotes a forthcoming Bank study (Lee and Gerner) saying "Nominal average
  electricity tariffs increased by 53 percent from January 2019 to January 2015, whereas
  cumulative inflation for the same period was around 56 percent." That is a four-year span,
  not 2005-2019; 2005-2019 is the period over which the tariff was revised 13 times.
  Corrected to January 2015 to January 2019, and the reversed printing of the dates is
  recorded.
- **Vietnam Water Resources.** Group: "much of the increase was due to the increase in
  effectively irrigated area (rehabilitation) rather than to the impact from
  modernization"; 2019 assessment: "a one-third reduction in actually completed
  infrastructure improvements versus what was originally planned", and achievement "relied
  heavily on the government extension programme". All correct.

## 4. sources_add

The writer's reason checks out, and sources_add stays empty for all 12. Every document drawn
on is already in the case's sources with the same documents1.worldbank.org URL: report plus
review for ten cases, review plus 2018 assessment plus report for NanGuang, review plus 2019
assessment for Water Resources. No paragraph rests on a document the case does not already
cite. Water Resources does not cite the project's own completion report, ICR00002604, which
is not on disk; its ratings are reported inside the 2019 assessment's three-column table,
which is cited, and "searched" now says so.

## 5. The claimed card defect - not a defect

The URL ending 000020051-20140626114618.pdf serves, on its first page: "Report Number :
ICRR14273", "IEG ICR Review / Independent Evaluation Group", Country Vietnam, Project ID
P065898, Date Posted 12/09/2013. The on-disk copy is identical in its first 40 lines to
vfy/vn_wrap_ieg.txt. So it is indeed the Evaluation Group's ICR Review.

**The card already labels it correctly.** The source entry reads "Vietnam - Water Resources
Assistance Project: Implementation Completion **Report Review** (ICRR14273)", publisher
"World Bank Independent Evaluation Group". The writer read the opening words "Implementation
Completion ..." as the start of "Implementation Completion and Results Report"; the title is
complete and accurate as it stands. **No relabelling is needed.** If the owner wants the
Bank's own wording instead, the document's title block is: *ICR Review: Vietnam - Water
Resources Assistance Project (P065898)*, Report No. ICRR14273, World Bank Independent
Evaluation Group, posted 9 December 2013.

Spot-check of the claimed metadata pattern: the same 000020051-2014... URL form appears on
the Naji, Shiyan and Ankang cards, and on all three the title already reads "Implementation
Completion Report Review" with the Evaluation Group as publisher. Lucknow's review URL takes
the same form and is titled "ICR Review". The pattern holds and none of these cards is
mislabelled.

## 6. self_reported

True for all 12, correctly - every figure in every paragraph comes from a World Bank or
Independent Evaluation Group document, and no non-Bank source with output figures was found
for any of these projects. **But the required sentence was present in only 1 of the 12
paragraphs** (Lucknow, "No figures from outside the Bank were found"). The other 11 carried
the statement only in "searched", where the card does not show it. A closing sentence was
added to all 12: "All of these figures come from the World Bank's own documents; no
independent check of them was found."

## 7. Duplication of the case's own outcome field

- Naji and Ankang: the writer's decision to leave the rating sets out is right; both outcome
  fields carry them in full, including the Naji table mislabel. Kept out.
- Lucknow: the paragraph restated "The completion report rated the outcome Moderately
  Unsatisfactory", which the outcome field already gives. Removed; only the Group's
  departures are kept.
- NanGuang, Shiyan, ShiZheng, Vietnam Water Resources: paragraphs restated rating agreements
  the outcome fields already give. Removed; the space went to delivery figures and to the
  substantive findings.
- Orissa: the paragraph uses the roads-finished count and the per-road returns, which the
  outcome field does not carry, rather than the 150 km figure, which it does.
- No paragraph repeats the harm set out in the community field.

## 8. Economic rates of return

Scope and what each return measures are now stated in every paragraph.

- **Lucknow - corrected.** The paragraph gave a bare "26 per cent". The report's Annex 3 says
  the combined return for the full 483 km at processing stage was 26 per cent and the
  end-of-project return for the restructured 327 km is 26.2 per cent. Both scopes now given.
  What it counts: vehicle operating cost savings and travel time for passengers and goods;
  accident savings are explicitly excluded from the discounting.
- **Ethiopia.** 14.8 to 21.5 per cent is right for the Mekenajo-Dembidolo road, named in the
  paragraph. Counts savings in vehicle operating costs and travel time; "maintenance" was
  removed - the appraisal treats net incremental road maintenance as a **cost**, not a
  benefit. Whole-project figures, which the paragraph does not use: 14.4 to 22.8 per cent in
  the report's table, 13.5 to 22.8 per cent in the Group's.
- **NHIIP.** 25.74 per cent at appraisal for 1,200 km in eleven sections against 20.3 per
  cent for the eight sections built, 617.3 km. Scopes correct; "617" refined to 617.3 km and
  the eleven-section appraisal scope added.
- **ShiZheng.** 20 to 15 per cent correct. What it counts was wrong: the writer gave
  "capacity freed on the old line", which is not in the list. The report lists passenger and
  freight traffic cost-benefit (travel-time savings) and externalities (carbon emissions,
  reduced accidents), with agglomeration benefits deliberately excluded to match the
  appraisal method. Corrected.
- **Naji.** 18 to 15.8 per cent for the Guangxi component, counting savings in travel cost
  per tonne and the economic benefit of the electricity generated. Added.
- **Ankang.** 15.3 per cent at completion for the whole project; the 17.9 per cent appraisal
  figure and the "savings in vehicle operation cost / savings in passenger travel time"
  definition come from the **Group's** review, not the report, and are now credited to it.
- **Orissa, Shiyan, Vietnam DEP, Vietnam RE2, Vietnam WRAP.** Scopes added: corridor
  appraisal estimates against per-road ex-post returns (Orissa); whole project and local
  roads programme separately, over 24 years (Shiyan); whole project at completion against
  first-phase subprojects at appraisal (DEP); the same 355 communes in six provinces at both
  dates (RE2); 88 per cent of project costs on agricultural benefits versus all schemes with
  municipal and industrial use added, against 14.7 per cent at appraisal (WRAP).

## 9. Other factual corrections made

- **Ankang:** local roads 1,391.**57** km, not 1,391.75 - a digit transposition by the
  writer. The expressway traffic target in the results sheet is 5,870 to 6,360 vehicles a
  day; the 6,585 is the report's forecast of when the target would be reached, 2018. "Two
  deaths against a target of 13" is **2 fatal accidents against a target of 13 fatal
  accidents**; the report says fatality accidents "were much lower than the targeted value",
  that is, better than target, while total accidents were worse. The US$1,096 million cost is
  95 per cent above the US$561 million **base** cost for that component, not above the
  appraisal estimate as such.
- **Shiyan - a reversed finding.** The paragraph said the fatal accident rate "fell from 3.4
  to 3.1 per million vehicle-kilometres against a target of 2.9", which reads as a
  shortfall. The results sheet gives the unit as per 100,000 vehicle-km, baseline 3.4
  (2004), target 2.9, **actual 2.1** at 31 December 2009, with the comment "Target achieved
  ... surpassed the target in 2009". The 3.1 is an interim 2008 figure from the narrative.
  Corrected. Also: 262 km of local roads is **three** roads, not four - the fourth item in
  the component is the Jiangjunhe bridge. All three roads were earth roads of the lowest
  class; the 45 and 90 day closures apply to the two roads selected for monitoring.
- **Ethiopia:** travel time on Mekenajo-Dembidolo fell from **2.5** minutes a kilometre in
  2009 to 1 minute in 2017, per the report's text and its results framework (baseline 2.50
  at 1 May 2009). The Group's review prints 3 minutes for this road and 2.5 for
  Welkite-Hosaina, the reverse of the report; the report's figures are used. The clause
  saying the Group noted that the wider road-condition and rural-access figures reflect the
  whole government programme was **removed as unsupported** - no such note appears in the
  review; the programme-wide figures (asphalt 17 to 35 per cent and so on) are RSDP history
  in an annex of the report.
- **NanGuang:** the closing clause - "the Group records income and land-value rises along the
  line but says there was no counterfactual, so the project's share in them cannot be
  separated from inflation and other causes" - is **in neither Group document** and was
  removed. The assessment's actual statement, now used, is that the project "benefitted from
  becoming part of a broader railway system" and "the benefits of this intersystem connection
  are impossible to disentangle from the benefits of the NanGuang project on its own". Also:
  the freight reason is the railway's network-wide strategy of running dedicated passenger
  high-speed lines, not keeping freight on the conventional line; the 94 million man-days
  figure now carries the report's qualifier that about 15 per cent went to local labour; the
  7-to-31 train pairs and 620-to-156 minutes are the report's closing figures, the 2018
  assessment giving 56 pairs and about 182 minutes from its own estimate.
- **ShiZheng:** "eight stations against a target of six" was misleading. Six new stations
  were planned and built, at Gaoyi, Xingtai, Handan, Anyang, Hebi and Xinxiang; the Group
  counts eight along the line and calls that exceeding the target, but the report says the
  Shijiazhuang and Zhengzhou stations "are not part of this project". Both statements now
  given. The reason for 60 rather than 100 high-speed pairs is corrected to the report's: the
  railway kept about 65 conventional trains running in response to public feedback on fares
  and on access to intermediate stations.
- **Vietnam Distribution Efficiency:** the 8,587 km and 4,742 MVA totals are arithmetic the
  writer did, not figures in any document. Replaced with the report's own component lines
  (4,001 km of new low-voltage line against 2,446 planned, and so on). The 448.5 GWh against
  414.5 GWh is the **Northern Power Corporation alone**, not a combined figure; the combined
  figure in that table is 365,707 against 269,148 tonnes of avoided emissions. Corrected.
- **Vietnam Water Resources:** the return is 15.3 per cent, not "about 15"; the appraisal
  figure of 14.7 per cent was missing; the 50-to-81 per cent figure is the **average** share
  across schemes, not each scheme's. The 2019 assessment's report number is **138389**, not
  13838 as the writer's "searched" line had it.
- **Naji:** the paragraph gave only the 273 GWh expectation and omitted what the plant
  actually generated - 227 GWh in 2009, 10.2 per cent below that year's 253 GWh target. The
  actual figure now comes first and the expectation second. The reason for the lower
  financial return is given as the documents give it: the provincial government decided to
  charge no shiplock fee along the Xijiang in Guangxi, and the grid sale price was fixed at
  RMB 0.29 per kWh against RMB 0.35 assumed.
- **Orissa:** traffic growth came out **1.73 and 2.93 times** the appraisal estimate, not
  "two to three times"; "no road fund was set up" added, since the study was completed but
  the fund was not established.

## Pattern worth carrying forward

Three recurring failure modes in this batch, all worth a standing check.

1. **The Evaluation Group's own documents carry transposition errors in exactly the places a
   writer is most likely to quote** - the ICR column of the ratings table (Orissa, Naji), a
   single output bullet (Ankang 78 km), and paired baselines for two roads (Ethiopia
   2.5/3.0). Any figure or rating taken from a Group review should be read against the
   completion report's own text before use, and never the other way round.
2. **A target met is as easy to misreport as a target missed.** Shiyan's accident rate and
   Ankang's fatal accidents were both presented as shortfalls when the documents record them
   as met or exceeded. Results sheets should be read to the "actual at completion" column
   and the "Comments (incl. % achievement)" cell, not to an interim figure in the narrative.
3. **The self-reported sentence must be in "whole", not "searched".** It was missing from the
   paragraph in 11 of 12 cases while the flag was set correctly in all 12. Check the
   sentence, not the flag, on every future round.

A fourth, smaller point: arithmetic the writer performs on document figures - the
Distribution Efficiency km and MVA totals - reads on the card as a document figure but is not
one. Prefer the document's own component lines.

## Per-entry summary

```json
{
 "entries": [
  {
   "id": "lucknow-muzaffarpur-highway-land",
   "change": "text changed",
   "why": "economic return given without scope (26.2 per cent for the 327 km built against 26 per cent at appraisal for the full 483 km); what the return measures added; restatement of the completion report's outcome rating removed as already in the case's outcome field; self-reported sentence standardised",
   "self_reported": true
  },
  {
   "id": "mekenajo-dembidolo-road-coffee",
   "change": "text changed",
   "why": "travel time corrected from 3 to 2.5 minutes a kilometre per the completion report and its results framework; 'maintenance' removed from the benefits counted; unsupported clause about the Group noting programme-wide road-condition figures removed; the Group's efficiency disagreement (Modest against Substantial) added; self-reported sentence added",
   "self_reported": true
  },
  {
   "id": "naji-youjiang-waterways-resettlement",
   "change": "text changed",
   "why": "actual 2009 generation of 227 GWh, 10.2 per cent below target, was missing while only the 273 GWh expectation was given; what the return measures added; reasons for the fall in financial return given as the documents give them; self-reported sentence added",
   "self_reported": true
  },
  {
   "id": "nanguang-railway-resettlement",
   "change": "text changed",
   "why": "the half-of-benefits agglomeration estimate and the UK Department for Transport method were misattributed to the Group's 2018 field mission; both come from the completion report and the appraisal document, and the mission tested them; the closing claim about income and land-value rises and a missing counterfactual is in neither Group document and was replaced with the assessment's actual statement; freight reason corrected; self-reported sentence added",
   "self_reported": true
  },
  {
   "id": "nhiip-india-corridor-land-acquisition",
   "change": "text changed",
   "why": "'cannot be attributed' corrected to the Group's 'cannot be fully attributed'; appraisal scope (eleven sections, 1,200 km) and completed scope (617.3 km) stated; road safety budget history added; self-reported sentence added",
   "self_reported": true
  },
  {
   "id": "orissa-state-roads-compensation",
   "change": "text changed",
   "why": "traffic growth corrected to 1.73 and 2.93 times the appraisal estimate from 'two to three times'; the Group's Risk to Development Outcome disagreement (Substantial against the report's Modest) added and the false Bank-performance disagreement avoided; scope of the appraisal returns clarified; road fund not established added; self-reported sentence added",
   "self_reported": true
  },
  {
   "id": "shaanxi-ankang-road-resettlement",
   "change": "text changed",
   "why": "local roads 1,391.57 km not 1,391.75; expressway traffic target is 5,870 to 6,360, the 6,585 being a 2018 forecast; '2 deaths against a target of 13' corrected to 2 fatal accidents against a target of 13; cost comparison is against the US$561 million base cost; the 17.9 per cent appraisal return and the benefit definition credited to the Evaluation Group; self-reported sentence added",
   "self_reported": true
  },
  {
   "id": "shiyan-connecting-road-safeguards",
   "change": "text changed",
   "why": "accident finding reversed: the completion value is 2.1 per 100,000 vehicle-km against a 2.9 target, target achieved, not 3.1 falling short; 262 km is three local roads not four, the fourth component item being the bridge; all three roads were earth roads and the 45 and 90 day closures apply to the two monitored; GDP figure credited to the completion report as well as the Group; return scope and benefits added; self-reported sentence added",
   "self_reported": true
  },
  {
   "id": "shizheng-railway-resettlement",
   "change": "text changed",
   "why": "'eight stations against a target of six' corrected: six new stations planned and built, the Group counting eight including two the report says are not part of the project; 'capacity freed on the old line' removed from what the return measures; reason for 60 rather than 100 high-speed pairs corrected to the report's; self-reported sentence added",
   "self_reported": true
  },
  {
   "id": "vietnam-distribution-efficiency-five-households",
   "change": "text changed",
   "why": "8,587 km and 4,742 MVA were the writer's own sums, replaced with the report's component lines; 448.5 GWh against 414.5 GWh is the Northern Power Corporation alone, not a combined figure; tariff figures redated to January 2015 to January 2019 and credited to the Bank study the Group quotes; self-reported sentence added",
   "self_reported": true
  },
  {
   "id": "vietnam-rural-energy-2-land-loss",
   "change": "text changed",
   "why": "return scope added (the same first-phase investments in 355 communes in six provinces at both dates); the objective quoted more closely and the Group's missing-study finding stated as the Group states it, with the report's 2011 national study qualification; revised targets labelled; self-reported sentence added",
   "self_reported": true
  },
  {
   "id": "vietnam-water-resources-assistance-resettlement",
   "change": "text changed",
   "why": "return is 15.3 per cent and the appraisal figure of 14.7 per cent was missing; 50 to 81 per cent is the average share across schemes; restatement of the three-way rating agreement removed as already in the case's outcome field; assessment report number is 138389; self-reported sentence added",
   "self_reported": true
  }
 ]
}
```
