# Fact-check log: whole-picture paragraphs, batch 1 (12 cases)

Checker: independent. Method: every figure, date and rating re-read from the project PDFs on disk
(`pdftotext -layout` run fresh into a separate directory, not the writer's own .txt files), plus the
World Bank WDS API for document dates and a curl HTTP check on all 24 URLs in `sources_add` (all 200).
Three web spot-checks for non-Bank accounts of delivery (GuiGuang ridership, Cuijiaying generation,
CAG audit of Himachal Pradesh roads) returned nothing usable, so `self_reported: true` stands on all 12.

Counts: **0 kept unchanged, 12 corrected, 0 blanked.**

## 1. biftu-quarry-mizan-dima-road
- change: text changed
- self_reported: true (sentence present)
- Rating claim VERIFIED. IEG ICR Review (ICRR0021923) ratings table: Outcome Moderately Unsatisfactory =
  Moderately Unsatisfactory, Bank Performance Unsatisfactory = Unsatisfactory, Quality of M&E Modest =
  Modest. This is a genuine agreement, and the two label sets match. Paragraph now names all three rows
  rather than only the outcome.
- CORRECTED: the beneficiary count was given as "1,983,354 people were counted as beneficiaries against a
  target of 2,325,900", omitting that the baseline was already 1,943,400. The ICR calls the indicator
  "marginally achieved (10%)" and the IEG calls 1,983,357 "slightly above the baseline of 1,943,400". The
  baseline is now shown; without it the figure reads as 2 million people reached by the project.
- CORRECTED: "the deterioration of the stretch inside Djibouti" overstated the ICR, which says the rest of
  the route had deteriorated "mostly in the territory of Djibouti". Now "mostly inside Djibouti".
- 32.4% VERIFIED as the ex-post EIRR for Mizan-Dima against a PAD EIRR of 15.1% (ICR Table 6). The
  statement that it counts no payment to anyone moved is supportable: ICR para 25 says the HDM-4
  calculation covers road agency costs and road users' vehicle operating and travel time costs over 20
  years at a 10.23% discount rate, and compensation is not among those inputs. Reworded to "counts no
  payment to anyone moved or compensated" so it describes the calculation's inputs rather than judging it.
- Source added by the writer VERIFIED: the WDS API for P117731 returns "Ethiopia - Ethiopia-Transport
  Sector Project", docdt 2020-01-28, at .../251441580240225684/pdf/Ethiopia-Ethiopia-Transport-Sector-Project.pdf.
  Right project, right date, URL returns 200.
- Rounding pair (25 vs 23 km/h baseline; 36.9 vs 37 per cent) correctly kept out of `whole` and left in
  `searched` as transcription/rounding, not as a finding. A third such pair found and added: the
  beneficiary count is 1,983,354 in the ICR and 1,983,357 in the review.
- Figures re-verified: 305 of 434.5 km, 320 km after April 2019, 133 km / 77 of 92 / 95 of 105, two
  contracts terminated, 17.8 to 36.9 against 40 per cent, 70 against 80 km/h, six days unchanged.

## 2. caldwell-bridge-liberia-compensation
- change: text changed
- self_reported: true (sentence present)
- Rating claim VERIFIED. IEG table: Outcome Satisfactory = Satisfactory; Bank Performance Highly
  Satisfactory cut to Satisfactory, reason "Minor shortcomings with M&E"; Quality of M&E Substantial =
  Substantial. Outcome agreed, Bank's own performance cut, as reported.
- CORRECTED: the 94 per cent rural-access figure was given bare. The same IEG passage gives the revised
  target (90 per cent) and immediately qualifies the figure with a separate Bank spatial analysis putting
  Liberia's rural accessibility index at 48 per cent, up from 40. Both now shown; the 94 per cent figure
  on its own invites the reader to think nearly all rural Liberians gained all-season access.
- CORRECTED: 45.5 km of maintenance was set only against "an original target of 641 km". The revised
  target was 131.6 km; both now given.
- Figures re-verified: 24 km city streets, 148.5 km rural road, Vai Town intersection, two misprocured
  lots, fuel unloading facility not in service at closing, 163 to 55 and 160 to 45 minutes, 5 to 35 per
  cent of streets, 1,194,729 against 744,980, 10 km buffer and the whole-of-Monrovia assumption, ERR 18
  per cent over 86 per cent of cost with none at appraisal.
- No duplication: the case's `outcome` carries the bridge itself and the US$8.0 million of IDA money put
  into resettlement payments; the paragraph does not restate either.

## 3. chebei-village-guangzhou-resettlement
- change: text changed
- self_reported: true (sentence present)
- Rating claim VERIFIED. IEG ICRR13992 table: Outcome Moderately Satisfactory vs Moderately
  Unsatisfactory; Bank Performance Moderately Satisfactory vs Moderately Unsatisfactory; Risk Significant
  = Significant; Borrower Performance Moderately Satisfactory = Moderately Satisfactory.
- CORRECTED for duplication: the paragraph restated the Moderately Satisfactory / Moderately
  Unsatisfactory outcome pair, which the case's `outcome` field already carries verbatim along with the
  Significant risk rating. The restatement is cut; the grounds for the downgrade, which are new, are kept,
  and the Bank-performance cut (not on the card) is added.
- Grounds re-verified word by word: project investments "accounted for only 6% of the US$8.5 billion that
  the Government was concurrently spending on the Pearl River Clean up Campaign"; two of three
  inter-municipal pilots completed, third not undertaken, implementation of the regional master plan not
  begun; about 70 per cent of samples meeting Class III against a 58 per cent baseline and an 80 per cent
  target, and "not evident that the improvement in surface water samples is a result of the project".
- Other figures re-verified: 475,000 m3/day across three plants; 50 to 97 per cent against 90; about 20
  per cent of Guangzhou's capacity; hazardous waste plant 150,000 to 290,000 m3, three-year operator
  contract let late 2012, operating from August 2013, about 9,000 tonnes treated against a 45,000
  tonnes/year target; tariff Y0.70 baseline, Y1.50 target, Y1.07 actual, Y2.94 needed for depreciation;
  US$520.8m against US$431.9m, increase "financed entirely by the Government"; no ERR at either stage.
- REMOVED: "rose about 50 per cent" before the tariff figures. The figures carry it.

## 4. cuijiaying-han-river-resettlement
- change: text changed
- self_reported: true (sentence present)
- Rating claim VERIFIED. IEG table: Outcome Satisfactory vs Moderately Satisfactory, reason the causal
  link from project activities to standard of living "was weak, and was not backed by sufficient
  evidence"; Bank Performance Satisfactory vs Moderately Satisfactory; Risk Negligible to Low = Negligible
  to Low; Borrower Performance Satisfactory = Satisfactory.
- CORRECTED for duplication, the largest cut in the batch. The paragraph's closing sentence reproduced the
  income claim (just over 3,000 to over 5,000 yuan), the borrower's-own-survey criticism, the absence of a
  counterfactual, the silence on inflation, and the Satisfactory-to-Moderately-Satisfactory downgrade. All
  five are already in the case's `outcome` field, in more detail. Cut entirely; the paragraph now ends on
  whose figures these are. The point is not lost to the reader, it is one field away on the same card.
- ADDED (verified, and not on the card): cost per kilowatt installed US$2,132 against a target of US$2,150.
- Figures re-verified: six turbines, 90 MW, 431 GWh in 2010, 446 GWh expected, about 322,800 tonnes of CO2,
  about 40 million tonnes of live storage, 118,000 ha in Tangdong, 33 km of waterway, 1,000-tonne vessels
  and tows of two to four barges, lock availability 95 against 85 per cent, 5.61 against 3.66 million
  tonnes attributed to the project team, US$254.2m against US$211.1m, ERR 21.3 against 22.2 per cent over
  99 per cent of cost.
- Appraisal-versus-completion returns correctly treated as before-and-after, not as a disagreement.

## 5. guiguang-railway-land-acquisition
- change: text changed
- self_reported: true (sentence present)
- Rating claim VERIFIED. IEG table: Outcome Highly Satisfactory vs Satisfactory; Risk to Development
  Outcome Negligible vs Modest, reason "There is modest financial risk associated with the financial
  viability of the newly created line"; Bank and Borrower Performance Satisfactory = Satisfactory. The
  writer's handling of the Negligible/Modest pair is right and does not pretend the two labels are from
  one scale.
- CORRECTED for duplication: the case's `outcome` already carries the Highly Satisfactory / Satisfactory
  outcome pair. That restatement is cut; the risk-rating rise, which is not on the card, is kept with its
  reason, now naming the newly created line company as the document does.
- CORRECTED: "a unit cost of about US$14 million per kilometre that the report calls among the lowest in
  the world" now credits the Bank study the report relies on ("High-speed Railways in China: A look at
  Construction costs", China transport topics No 9), so the characterisation is not left as the report's
  unsupported word.
- ADDED: the 25 pairs a day beat targets of 15 and later 20.
- Figures re-verified: 847 km, 342 bridges and viaducts, 233 tunnels, 21 of 30 stations, 1,500 to 251
  minutes and 83 per cent against an original 330-minute target, three to 25 pairs a day, no freight,
  survey of 467 passengers on 12 trains with 61 per cent tourists, 36 per cent business, over 40 per cent
  on 4,000 yuan a month or less and 36 per cent generated trips, US$12,526.56m appraisal and US$13,054.98m
  actual, US$299.49m disbursed of a US$300m loan, ERR 16 to 18 per cent over 74 per cent of cost.

## 6. guiyang-youxiao-road-resettlement
- change: text changed
- self_reported: true (sentence present)
- Rating claim VERIFIED. IEG table: Outcome Moderately Satisfactory = Moderately Satisfactory; Risk
  Moderate vs Significant; Bank and Borrower Performance Moderately Satisfactory = Moderately
  Satisfactory; Quality of ICR Unsatisfactory. So the completion report on this project is the one
  document in the batch that the evaluators rated Unsatisfactory as a report.
- CORRECTED for duplication: the case's `outcome` already carries the agreed Moderately Satisfactory
  outcome and the rise in risk from Moderate to Significant. Both restatements cut; the Unsatisfactory
  rating of the report itself, which is not on the card, is kept.
- ADDED (verified, and it bears directly on the terminals the paragraph credits): the completion report
  reports that most of the bus terminals and freight depots are not well operated and maintained.
- CORRECTED: "which a mountain had separated from the city centre" to mountains separating Longdongbao
  from the core urban area, as the review puts it.
- Figures re-verified: 7.04 km at a 60 km/h design speed, 11 rural road segments, 15 bus terminals and one
  freight depot, 21-minute saving attributed to the project team, 67 additional administrative villages,
  118 administrative villages served by the terminals, 39.8 to 25.8 minutes on a 25 per cent sample,
  Rmb 528 million and 192 per cent against 2009, 129.2 per cent revenue rise, US$360.7m against
  US$314.42m, ERR 16.9 at appraisal and 16 per cent at completion over 99.2 and 99.4 per cent of cost.

## 7. himachal-pradesh-state-roads-debris
- change: text changed
- self_reported: true (sentence present)
- Rating claim VERIFIED. IEG table: Outcome Moderately Satisfactory = Moderately Satisfactory; Bank
  Performance Moderately Satisfactory = Moderately Satisfactory; Quality of M&E Substantial vs Modest,
  reason a missing outcome indicator for the transport-cost objective and missing indicators for Component
  2 and the institutional work. Efficiency rated Modest in the body despite an ex-post EIRR of 26 per
  cent, on the project's cost and time overruns, with road-upgrading contracts 31 per cent over estimate
  and four extra years of implementation. All as reported.
- CORRECTED: "26 per cent at completion against 27 per cent at appraisal, covering 88 per cent of project
  cost" attached one coverage figure to both returns. The IEG table gives 88 per cent for the completion
  estimate and 78 per cent for the appraisal estimate; both now shown.
- CORRECTED: "the share of in-house labour in maintenance spending" to the indicator's actual subject, the
  share of permanent gang labour costs in spending on routine and emergency works (75 to 62 per cent
  against a 50 per cent target).
- CORRECTED: 1,831 km is the length of periodic maintenance work *awarded*, against a target framed in the
  report as "approximately" 2,000 km. Both qualifications restored.
- ADDED: the agreement on Bank performance, which the paragraph had not mentioned.
- Figures re-verified: 25 blackspots against 20, accident database in every district by July 2015, 29 to
  40 km/h and +38 per cent against a +25 per cent target (36 km/h), core network in poor condition 40 to
  10.4 per cent, deaths per 1,000 vehicles 0.28 in 2014 to 0.21 in 2017, VOC 14.39 to 9.78 rupees/km
  (32 per cent), no road fund created.
- No duplication: the case's 355 km, the debris sites and the 432,692 trees are not repeated.

## 8. huai-river-flood-drainage-resettlement
- change: text changed
- self_reported: true (sentence present)
- **MISLABELLED AGREEMENT, CORRECTED.** The paragraph said the Independent Evaluation Group "agreed with
  every rating in the report". The IEG table does print matching labels in both columns, but the label it
  puts in the report's column for risk is Modest, and the completion report's own rating is **Moderate**
  (ICR data sheet p.i, and ICR para "Rating: Moderate"). The case's `outcome` field flags exactly this. The
  paragraph now says the review gave the same outcome, Bank performance and borrower performance ratings,
  and prints the risk as Modest where the report used Moderate.
- **FIGURE ERROR, CORRECTED.** People protected: target given as 6.54 million. The report's results
  framework and its efficacy text both give 6.64 million. Changed.
- CORRECTED: "a project costed at US$597.41 million" is the appraisal estimate. Actual total financing was
  US$613.77 million (102.74 per cent). Both now given.
- CORRECTED for duplication: "Incomes were recorded as improved for 81,311 affected people against a
  target of 57,173" reproduces the case's `outcome` field, which carries both numbers and adds the
  warning that they count people the project was meant to help, not people moved. Cut.
- CHECKED and kept: the dredging target of 980.54 km. It is the annex table 2.2 total; the results
  framework row gives 980.2 km. Both are in the document, so the figure is sourced, and the discrepancy is
  now noted in `searched` rather than left silent.
- Figures re-verified against annex tables 2.1-2.7: 444.62 against 417.45 km of dike, 1,023.51 km dredged,
  252 pumping stations against 182, 487 sluice gates and culverts against 427, 250 bridges against 197,
  140.88 km of ditches, 36 associations (4 pilot plus 32), 9,682.4 against 9,576.2 km2, RMB 260 against
  233, RMB 263.33m against 118.41m, RMB 797.99m against 699.45m, ERR 25 against 20 per cent over 61 per
  cent of cost.
- VERIFIED: the aquaculture claim. The review's efficacy text marks the diversification into aquaculture
  "(not documented)".
- CORRECTED: "dikes built" to dikes strengthened, the annex table's own word.

## 9. jituhun-railway-resettlement
- change: text changed
- self_reported: true (sentence present)
- Rating claim VERIFIED. IEG table: Outcome Highly Satisfactory vs Satisfactory; Borrower Performance
  Highly Satisfactory vs Satisfactory; Risk Negligible = Negligible; Bank Performance Satisfactory =
  Satisfactory. The grounds the paragraph gave are the review's own: efficacy Substantial "albeit that
  there were minor shortcomings such as underestimation of passenger traffic flows on the corridor and
  non-completion of two stations at project closure".
- **FIGURE ERROR, CORRECTED.** Transit time Tumen to Jilin given as falling "from 420 minutes to 113". The
  report's indicator table gives the baseline as **460** minutes (and a 75 per cent fall). Changed.
- **FIGURE ERROR, CORRECTED.** "155.7 km inside 66 tunnels". The report gives **85** tunnels: design
  changes converted long tunnels into shorter ones, raising the count from 77 to 85 and cutting cumulative
  length from 159.4 to 155.7 km. The bridge and viaduct count, 115, was also missing and is added.
- CORRECTED: "a project costed at US$6.30 billion" is the appraisal estimate only. Actual cost was
  US$5,272.45 million, 86 per cent of the estimate, after the switch to ballasted track and the dropping
  of the Jilin hub loop. The paragraph presented the larger figure as the project's cost; both are now
  given, with the reason.
- CORRECTED for duplication: the case's `outcome` carries the Highly Satisfactory / Satisfactory outcome
  pair. Cut; the borrower-performance cut, which is not on the card, is kept.
- ADDED: eight stations were built (seven new plus one rehabilitated) and the two unopened ones are named
  in the report (DashitouNan and Weihuling); trains run at a maximum of 200 km/h to save energy against a
  250 km/h design speed, which bears on the traffic shortfall the paragraph reports.
- Figures re-verified: 360 km, 250 km/h design, 90.96 km on bridges and viaducts, 3.3 km four-track bridge
  over a highway and the Songhua River, 26 pairs against a target of 13, 8.2 million passengers against 8
  million, traffic density 24 per cent below appraisal in 2016, survey of 500 with 17 and 83 per cent,
  US$200m loan with US$198.67m disbursed, ERR 8.4 against 6.2 per cent on travel time savings only.

## 10. karnataka-state-highways-ii-compensation
- change: text changed (most corrections in the batch)
- self_reported: true (sentence present)
- Rating claim VERIFIED. IEG table: Outcome Satisfactory = Satisfactory; Bank Performance Satisfactory =
  Satisfactory; Quality of M&E Substantial = Substantial. ERR 30 per cent at appraisal and 32 at
  completion, each over 97 per cent of project cost. A real agreement, same labels on both sides.
- **UNSUPPORTED FIGURE REMOVED.** "831 km ... against a revised target of 845 km". No target of 845 km
  appears anywhere in either document. The results framework gives revised targets of 534 km for item-rate
  contracts and 301 km for the concessions, 835 km together. The paragraph's own split (503 + 300) sums to
  803, not 831, and sat beside the unsourced 845. Replaced with what the document actually records: the
  narrative total of 831 km, and the two results-table rows, 503 of a revised 534 km and 300 of 301 km.
- **UNSUPPORTED FIGURE REMOVED.** Fatalities on the safety corridor "down 41 per cent against a target of
  21 per cent". The report's narrative gives the target as **30 per cent** ("fatalities by 41 percent
  against the original target of 30 percent", and the key-outputs annex repeats a 30 per cent target). The
  21 is a bare number in the results-framework row, which also prints a baseline of 31 and an actual of
  41, and cannot be read as a percentage target without contradicting the row's own baseline. Changed to
  30 per cent, with the table's 21 noted in `searched` as a third internal inconsistency.
- **UNSUPPORTED DETAIL REMOVED.** "ten-year design-build-finance-operate-maintain-transfer concessions".
  The report says these roads are in an operation and maintenance phase of eight years. No ten-year term
  is stated. Term dropped.
- CORRECTED: the 19 km unfinished was attributed to land acquisition alone. The report splits it: 13 km
  held up by land acquisition and utility shifting, 6 km by works in progress.
- VERIFIED, and now shown in the paragraph: the road-condition target inconsistency the writer reported is
  real. The narrative and the key-outputs annex both give "from 50% to 65% by EoP"; the PDO results row
  gives baseline 50.00, original target 50.00, revised target 50.00, actual 70.00. The paragraph gave
  "up from 50 to 70 per cent" with no target at all, which hid the conflict; both target values are now
  printed.
- VERIFIED: the accident inconsistency is real. 66 per cent in the safe-corridor passage, 60 per cent in
  the outcome summary and the key-outputs annex. Kept visible, as the writer had it.
- CORRECTED: US$416.5 million to US$416.56 million, and the US$97 million sentence now gives what the
  report gives about the other 40 per cent of concession construction cost, paid up front in equal parts
  from the Bank loan and a commercial bank, rather than the paragraph's vaguer "the rest coming from".
- CORRECTED: "a further 1,078 km of non-rural roads were rehabilitated as planned" to built, the
  indicator's own word ("Roads constructed, non-rural", target 1,078, actual 1,078).
- Figures re-verified: travel time down 30-40 against a 25 per cent target, VOC down 19 against 15 per
  cent, 62 km corridor, 143 blackspots in FY18-19, 0.834 million person-days with 69 per cent local and
  about 17 per cent women.
- No duplication: the case's land-acquisition and resettlement shortfalls are not repeated.

## 11. liaoning-medium-cities-resettlement
- change: text changed
- self_reported: true (sentence present)
- Rating claim VERIFIED as far as it goes. IEG table: Outcome Satisfactory = Satisfactory; Risk Negligible
  to Low in both columns; Bank and Borrower Performance Moderately Satisfactory = Moderately
  Satisfactory. The paragraph claimed agreement only on the outcome, which is right. Note for the record:
  the completion report's own risk label is Low, and the review prints Negligible to Low in the report's
  column, the same substitution as in the Huai River card; the paragraph never claimed otherwise, so
  nothing had to be unwound here.
- **CAVEAT VERIFIED.** The review's ERR table gives 15.2 per cent at appraisal over 70 per cent of project
  cost and 22.7 per cent at the ICR over 41 per cent, and its text says the re-estimate used actual
  traffic counts on roads in the six cities "that accounted for 41 percent of the actual costs". The
  caveat is accurate and necessary: without it the rise from 15.2 to 22.7 reads as the same measure
  improving. Wording tightened to say the two are not measured over the same thing.
- CORRECTED: "the Independent Evaluation Group rated that objective Modest, finding no evidence that
  maintenance costs or coverage improved". The review says lower unit cost and wider coverage would have
  been the evidence, and concludes "the project made few improvements to road maintenance". Changed to the
  document's own finding; "no evidence" was stronger than what is written.
- CORRECTED: "20 bus priority routes" to bus priority lines, "112 buses in Panjin" to 112 buses bought in
  Panjin, and "travel times on 12 monitored routes" to travel times on monitored routes, as the review's
  text does not tie the 13-to-68 per cent range to a count of twelve.
- Figures re-verified: 107 km of road and six bridges, less than planned because local governments
  completed sections with their own funds; about 4,478,000 m2 of surface and footway; traffic lights on
  156 km; drainage on 107 km; 824 monitoring and control installations; 141 sets of equipment; 11 depots,
  196 stops and shelters; roads in good condition from 41-60 to 70-89 per cent; bus passengers up 21 per
  cent in Fushun to 281 per cent in Panjin; deaths per 10,000 vehicles 3.3 to 2.8 in Liaoyang (15 per
  cent) and 4.3 to 1.3 in Jinzhou (70 per cent); US$397.44m against US$525.43m.
- No duplication: the 2007 external audit findings on Panjin and Fushun are on the card and are not
  repeated.

## 12. liuzhan-railway-resettlement
- change: text changed
- self_reported: true (sentence present)
- Rating claim VERIFIED. IEG table: Outcome Satisfactory = Satisfactory; Risk Negligible to Low in both
  columns; Bank and Borrower Performance Satisfactory = Satisfactory. Genuine agreement.
- CORRECTED for duplication: the case's `outcome` already carries the Satisfactory outcome rating. Cut.
- CORRECTED: "across three mountain ranges" to three mountains over 6,000 feet high, which is what the
  review says.
- CORRECTED: "the renovation of 14 stations that had not been costed" to 14 *existing* stations, the
  review's word, so the figure is not read as 14 further stations built.
- CORRECTED: ERR coverage. The review's table gives 100 per cent coverage for both the appraisal and the
  completion estimate, so "covering the whole project" now applies to each rather than to the completion
  figure alone.
- Figures re-verified: 97 km in Guizhou with 62.3 km of tunnel and 15.7 km of bridge and viaduct, two new
  and seven renovated stations, 99.7 km in Yunnan with 10.7 km of tunnel and 9.2 km of bridge, freight
  speeds 23 to 70 km/h against a target of 41, express passenger 55 to 100 against 90, trains 31 to 45
  pairs a day by October 2014 four months after closing against a target of 50 after the first year,
  US$1,541.6m against US$1,120.2m (40 per cent more), ERR 13 at completion against 17 per cent at
  appraisal.
- No duplication: the resettlement monitor's RMB 3,200 and 7 per cent income figures are on the card and
  are not repeated.

## Cross-cutting

**Rating disagreements that survived checking, all seven as reported.** Chebei/Guangzhou (P075728)
Moderately Satisfactory against Moderately Unsatisfactory with Bank performance also cut, on the 6 per
cent of US$8.5 billion and the unattributable water samples. Cuijiaying (P085333) Satisfactory against
Moderately Satisfactory, with Bank performance cut, on the living-standards evidence. GuiGuang (P107559)
Highly Satisfactory against Satisfactory, risk Negligible to Modest over the new line company's financial
viability. JiTuHun (P122321) Highly Satisfactory against Satisfactory for both outcome and borrower
performance, on traffic flows underestimated and two stations unopened. Caldwell Bridge (P113099) outcome
agreed, Bank performance Highly Satisfactory to Satisfactory on monitoring. Himachal Pradesh (P096019)
outcome agreed, efficiency Modest against a 26 per cent ex-post return, monitoring Substantial to Modest.
Guiyang (P093963) outcome agreed, the completion report itself rated Unsatisfactory, risk Moderate to
Significant.

**Mislabelled agreements.** One of the five: **Huai River**, where "agreed with every rating" papered over
the review printing Modest in the report's risk column while the report itself says Moderate. The other
four (Ethiopia, Karnataka, Liaoning, Liuzhan) survive, but two of them only because the paragraph happened
to claim agreement on a single row: Liaoning's report says Low where the review prints Negligible to Low,
and Liuzhan's rows all read Negligible to Low on both sides. Ethiopia and Karnataka are agreements on
every row with matching labels.

**Manufactured conflicts.** None found. The writer's decision to treat appraisal-versus-completion rates
of return as before-and-after estimates is correct for all nine: in every case the IEG's own table has one
"Appraisal" row and one "ICR Estimate" row for the same quantity. The framing is applied consistently.
The one place where the two numbers genuinely are not comparable, Liaoning's 41 per cent against 70 per
cent coverage, is the one place the writer added a caveat, and that caveat checks out.

**Real conflicts left visible.** Karnataka's two internal inconsistencies are real, and a third was found
(fatalities target 30 per cent in the narrative, 21 in the results table). Ethiopia's 25-against-23 km/h
and 36.9-against-37 per cent are correctly handled as rounding and transcription in `searched`, not
dressed up as findings; a third pair (1,983,354 against 1,983,357) was added there.

**Patterns worth carrying forward.**
1. *Appraisal estimates presented as what a project cost.* Three times (JiTuHun US$6.30bn against an
   actual US$5.27bn, Huai River US$597.41m against US$613.77m, Karnataka's phantom 845 km target). On
   World Bank cards, always take both columns of the cost table.
2. *Baselines dropped from indicator rows.* Ethiopia's 1,983,354 beneficiaries against a baseline of
   1,943,400 is the clearest case: with the baseline the indicator is a 10 per cent achievement, without
   it the project looks like it reached two million people. Any "X people benefited" figure needs its
   baseline row read.
3. *Coverage percentages attached to the wrong rate of return.* Himachal (88 against 78) and Liaoning (41
   against 70). The IEG tables give a separate coverage figure per row; one coverage figure quoted for
   both rows is a silent error.
4. *"They agree" is a claim about labels, not about judgement.* The Modest/Moderate and
   Negligible/Negligible-to-Low substitutions are systematic in IEG reviews. A paragraph should say which
   rows match and name the label each body used, which is also the only way the reader can see that the
   evaluators re-scored the report rather than endorsing it.
5. *Duplication clusters on the rating sentence.* Six paragraphs restated a rating pair already in the
   case's `outcome` field. The grounds for a downgrade are almost always new; the labels almost never are.
