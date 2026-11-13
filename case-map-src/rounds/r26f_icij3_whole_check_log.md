# Round 19 — independent check of the 18 whole-picture paragraphs

Output: `/home/claude/r19/whole_checked.json` (18 keys, every value non-empty).
Method: every figure read from the paired `.txt` of the on-disk source PDFs under `/home/claude/r19/dl`
(`pdftotext -layout`). No network calls were made; every document cited on the 18 cards was present.
Completion-report ratings were read from each report's own `C.1 Performance Rating by ICR` block or its
"Justification of Overall Outcome Rating" heading. Evaluation Group ratings were read from each review's own
`a. Outcome Rating` line and `Efficiency Rating` line. No rating in the output was taken from the Group's
reproduction of a report's rating.

---

## Per case

### 1. ceip-polder-land-payments-bangladesh — confirmed, no change
Checked every figure against `ceip_icr.txt` and `ceip_icrr.txt`. 405.67 km against revised 408 and original
623 (ICR results framework, "Length of upgraded embankment"); 305.85 km drainage channel against revised 305;
89 drainage and 85 flushing structures; 700 ha afforested; 65,657 ha against revised 66,012 and original
100,800; 720,573 people against revised 724,202; EIRR 25.7 per cent whole project. Ratings read out of each
document: report, "The overall outcome is rated Moderately Satisfactory ... Modest efficiency"; review,
`a. Outcome Rating / Moderately Satisfactory`, `Efficiency / Modest`. Report date 28 June 2024 and review date
30 November 2024 both match. Self-reported flag true and correct.

### 2. lahore-walled-city-shop-removals — corrected, substantially rewritten
**Error cut.** "The loan paid for 14 infrastructure investments" is wrong. 14 is the number of sub-projects
covered by the beneficiary survey (`pmsip_icrr` l.287, `pmsip_icr` l.1482). The loan financed 39 completed
sub-projects in 29 urban centres (`pmsip_icr` l.2201, l.3430). Corrected.

**Absence claim tested and found wrong, and this is the main correction.** The writer's report says "No
document found gives a rate of return, a visitor count or a trade figure for the Shahi Guzargah itself". No
rate of return and no visitor count exist — confirmed, having read the whole cultural-heritage annex (Annex 10)
and the whole economic annex (Annex 3). But the completion report does carry physical delivery figures for the
street where the shops stood, in Annex 10 paragraphs 26–27: planned scope of 57 streets to be paved and 773
facades to be improved; at closing 72 per cent of the facade work and 52 per cent of street surfacing done, and
75/70/70/80/60 per cent of the general, water-supply, sewerage, storm-drainage and electrical works; the works
contract unfinished at closing; about US$1.2 million of loan funds unused (l.979–982); remaining works
completed afterwards with provincial funds. These are now the core of the paragraph. On the item-5 question
(do the loan-wide figures belong?): they do, because the paragraph is about what the loan delivered, but they
are now subordinated to the Shahi Guzargah figures and the four recalculated rates of return are explicitly
marked as not being Walled City sub-projects.

**Added:** the landfill target (70 per cent, `pmsip_icrr` l.278), and the completion report's own count of
people served by the 39 sub-projects, more than 1.66 million (`pmsip_icr` l.2201–2203). The review rounds the
same figure to "about 1.7 million"; the report's own number is used.

Ratings confirmed from each document: report l.197 `Outcomes: Satisfactory` and l.1442 "Rating:
Satisfactory"; review l.366 `a. Outcome Rating: Moderately Satisfactory`, efficiency modest at l.342.

Note, not used: the beneficiary survey was run by "an independent contractor" (review l.287) but was
commissioned under the project, so the self-reported flag stands.

### 3. nepal-road-sector-unpaid-compensation — corrected
**Error fixed.** "9,000 m of minor bridge maintenance" — the figure is 9,500 m (`nprsdp_icrr` l.361,
`nprsdp_icr` l.512, l.1533, l.1773).
**Error fixed.** "the completion report of 30 September 2020". The report's cover carries only "September
2020" (`nprsdp_icr` l.52); 31 July 2020 is its exchange-rate date. No day is stated in the document. Changed to
"September 2020".
**Rating disagreement the writer missed and did not list.** The report rates efficiency **Substantial**
(`nprsdp_icr` l.652–653, "C. EFFICIENCY / Rating: Substantial"); the review rates efficiency **modest**
(`nprsdp_icrr` l.469, l.492). The paragraph gave only the review's rating. Now both, each named with its
document.
**Added:** the original 297 km target for roads rehabilitated (revised to 705), and the resilience works
shortfall the review records — six bridges of a 31-bridge target complete at closing, 0.73 km of a 16 km road
target (`nprsdp_icrr` l.366–375). The paragraph previously gave only the met and nearly-met indicators.
Confirmed unchanged: 680/705 km, 8→15 per cent against target 14, four hours to 1.9 hours, 752,000 against
800,000, EIRR 41.1 and 29.4 at completion against 29.4 and 23.4 at appraisal (`nprsdp_icr` Table 2, l.661–663),
report outcome Moderately Satisfactory (l.713–719), review outcome Moderately Satisfactory (l.499).

### 4. swat-s3b-road-land-acquisition — confirmed, no change
50.3 km against revised target 40.9 (123 per cent of revised target, `kp_icr` l.349–354); extra length from
exchange-rate and other savings (`kp_icrr` l.223–225); VOC down 34, 26 and 5 per cent (`kp_icr` l.268, l.454);
29.9 per cent appraisal for phase I and 28 per cent for phases II and III together (`kp_icrr` l.216, l.219);
"there was no estimate of the ex-post ERR" (`kp_icrr` l.228); efficiency modest (l.231); both outcomes
Moderately Satisfactory (`kp_icr` l.195 and l.1175; `kp_icrr` l.270–271). The paragraph correctly declines to
present the appraisal figures as results, even though the report argues they "would be valid at project
completion".

### 5. siddhirganj-pipeline-transmission-land — corrected
**Unsupported inference removed.** "31 per cent when estimated at the 2014 restructuring". The report says
only "the appraisal stage NPV (at the time of Project restructuring) of US$643 million and an EIRR of 31
percent" (`sidd_icr` l.1851–1852); it names no restructuring, and there were six. Changed to "estimated at the
time of a restructuring".
**Reworded, not a figure change.** "sixth to ninth cheapest of 45 baseload plants on the dispatch list" — the
report says the plant was "listed between sixth and ninth place on BPDB's merit order dispatch list (out of 45
total baseload power plants)" (l.1201–1203). Changed to "sixth to ninth on the national dispatch merit order of
45 baseload plants", which is what the document says.
Confirmed: 335 MW plant, 345 MW net tested output, 60 km pipeline, 11 km 230 kV double-circuit line with two
substations, 935 GWh over ten months at about 38 per cent utilisation against a 2,490 GWh a year target,
BDT 1.03–1.06 per kWh, EIRR 26.33 per cent, overall outcome Moderately Satisfactory (l.1943–1963), report dated
28 September 2020 (cover, l.41).

### 6. gujarat-highway-ii-delayed-compensation — corrected
**Error cut: a merged explanation.** The paragraph said "the review cites the completion report's explanation
that costs came in lower and that the road length measured was 25 km shorter" for the fall in net present
value. The review says the opposite division (`gshp2_icrr` l.605–612): the 25 km shorter segment is a
methodological note on the recalculation; lower construction contract costs and early completion explain the
**rise** in the rate of return; the net present value fell because of "lower than estimated traffic volumes
because the economic slow-down caused by COVID-19 pandemic". Both explanations now sit with the figure each
belongs to.
**Added, answering item 5 directly.** The paragraph had no outcome figure attributable to the project. One
exists: the share of all classified state roads in good or fair condition rose from 43 per cent to 81 per cent
against a revised target of 75, and the review itself states the indicator counted non-project roads and puts
the project-financed roads' own contribution at 11.1 percentage points against a revised target of 12
(`gshp2_icrr` l.472–477). That is the strongest project-attributed figure in the document and is now in the
paragraph with the review's own caveat.
**Added:** the review rates efficiency Substantial (l.687–688). Decision on the figures that were there: the
journey times (75→57 and 85→67 minutes per 50 km) and the 1,758 mm/km roughness reading are the review's own
outcome indicators for this project's roads and belong; the beneficiary count genuinely does not exist — I
grepped the whole review for "beneficiar", "people" and "population" and found only safeguards references.
Outcome Moderately Satisfactory confirmed at l.695–696.

### 7. dehlon-bypass-uncompensated-landowner — corrected; the writer's own worry was half wrong
The writer called this its weakest paragraph on the ground that "the fatal-accident rise from 2,655 to 5,077 is
a network count with no established relation to the project's works". The relation is established, by the
review itself: the fatal-accident count is the project's own road-safety outcome indicator, and the review's
heading over it is "Road safety on the Plan Road network was not improved" (`punjrd_icrr` l.291–292). Kept, but
reframed as the project's indicator and the review's finding of no improvement, rather than as a free-floating
death toll. The same holds for the 711 km, the 347 black spots and the network speed: all are the project's
indicators as the review presents them.
**Added, and this is the substance that was missing.** The review's two other outcome series: project roads in
poor condition 67 per cent (2006) → 1.4 per cent (2012) → 31.6 per cent (2017) as backlogs built (l.268–271);
and vehicle operating costs, measured only on the roads worked on — up 10 per cent on rehabilitated roads and
11 per cent on periodic-maintenance roads, down nearly 24 per cent on the output and performance-based
contract roads against a 20 per cent target (l.281–287). Also added: the review rates efficiency substantial
(l.450).
Confirmed: 711 km against original target 700 (l.244–245); 347 black spots (l.257); bypass completed (l.251);
speed 34.2 → 47.6 km/h against revised target 48 (l.273–274); 2,655 / 5,077 / about 4,278 (l.291–292); ERRs
31.8 / 28.5 / 50.4 against 36.5 / 44.2 / 58.4 and the report's explanation (l.396–400); outcome Moderately
Unsatisfactory (l.454). The completion report is not disclosed, so nothing here can be read out of it.

### 8. salem-tnudp-squatter-resettlement — corrected
**Internal conflict now stated, not hidden by choice.** The report's own results table gives 290,000 new
household sewer connections against a target of 150,000 (`tnudp_icr` l.442–446); its narrative and annexes give
"over 299,000" (l.1094) and 298,688 (l.2962, l.3573) for the same item. The paragraph gave only 290,000. Both
now given.
**Added:** report date 30 September 2014 (cover, l.41) and review date 12 May 2015 (`tnudp_icrr` l.15,
`Date Posted: 05/12/2015`). The paragraph had no dates on either rating.
Confirmed: more than 2.3 million people and 440,000 in low-income neighbourhoods (l.300–303); US$52 million
against US$40 million (l.309, l.1188–1189); weighted average ERR 19 per cent, water 24, roads 15
(l.1224–1235); report `Outcomes: Satisfactory` (l.166) and "overall achievement of outcomes is rated as
Satisfactory" (l.1262); review `a. Outcome Rating: Moderately Satisfactory` (l.301) and efficiency modest
(l.299).
Noted, not used: the report says "440,000 in low-income neighborhoods" in the indicator comment and "440,000
households in low income neighborhoods" in the body (l.1272) — people in one place, households in the other.
The paragraph follows the indicator table.

### 9. assam-roads-uncompensated-acquisition — corrected (addition only)
**Added:** the headline road-condition outcome, which was missing. The report records all 978 km in good or
fair condition at completion (`assam_icr` l.641); the review puts the share of Assam's whole secondary network
in good or fair condition at 55 per cent against a target of 40 (`assam_icrr` l.416–418).
Confirmed: 978 km against revised 1,000, made of 248 and 730 km (`assam_icr` l.637–641); travel time down 23
and 27 per cent against a 20 per cent target (l.651, l.1546–1547); ERRs 41.14 and 25.79 against 45 and 37.4
(l.852–858). Ratings read from each document and the disagreement holds: report, efficiency Modest (l.885,
l.911) and overall Moderately Satisfactory (l.912, l.920); review, "Overall, project efficiency is rated
substantial" (`assam_icrr` l.512) and `a. Outcome Rating / Satisfactory` (l.547–548).

### 10. drc-selembao-loange-compensation — corrected
**Imprecision fixed.** "water production in the project areas" — the figure is the N'Djili plant serving
Kinshasa (`cd_icr` l.1228–1229, `cd_ieg` l.211).
**Internal conflict now stated.** The report's results table gives the starting production as 160,000 cubic
metres a day (`cd_icr` l.335–337) and its own paragraph 48 gives 150,000 (l.1228–1229). The review carries
160,000. Both now given, each attributed to where it appears.
**Wording fixed.** "the project maintained 1,047 km" came from the indicator label. The report's text says the
1,047 km of the main national highway EN1 was "rehabilitated or reconstructed" (l.1230–1234) and the review
says "rehabilitated" (`cd_ieg` l.202). Changed.
**Figure cut.** I did not carry the feeder-road access series forward. The review states access "increased from
343,200 to 540,000" (`cd_ieg` l.194–195), but the report's results table shows 0 as the baseline, 343,200 as
the **target** and 540,000 as achieved, at 157 per cent (`cd_icr` l.286–293). The review has read a target as a
baseline. Rather than propagate either reading in a short paragraph, the item is dropped and reported here.
Confirmed: 1.6 million to 4.0 million with access to safe water, target 4.0 million (`cd_icr` l.335–342);
electricity three hours to 24 hours in target areas (l.325–331); 2,123 km of feeder roads against 2,500
(l.484); "Neither ex-ante nor ex-post economic and financial analysis was carried out" and "Efficiency is rated
modest" (`cd_ieg` l.260, l.266); review `a. Outcome Rating : Moderately Satisfactory` (l.289); report
`Outcomes: Satisfactory` (l.191) and l.1205–1206 "Rating: Satisfactory". Review date 6 June 2012 from the
document's own `Date Posted : 06/06/2012` (l.15); report date 29 October 2010 from its cover (l.54).

### 11. ghana-urban-water-unpaid-compensation — corrected
**Conflict the writer missed, and it is a real one.** On the appraisal rate of return the two documents
contradict each other. The report gives "EIRR of 26.18% (21% in the PAD)" (`gh_w_icr` l.1421–1422). The review
states that appraisal "included a financial model ... However, there was no economic analysis of the costs and
benefits for the physical investments (Component 1)" and that "Due to the lack of similar analysis in the PAD,
comparison to a baseline is not possible" (`gh_w_ieg` l.465–477). Same quantity, same measurement point. Both
now stated, each with its document, and no reconciliation offered.
**Overreach trimmed.** The paragraph attached "a different timeframe and exchange rate" to the 21 per cent
rate of return. In the report that parenthesis attaches to the net present value comparison ($454 million
against $22 million), with "(21% in the PAD)" standing alone in the next clause. Reworded so the clause sits
where the document puts it.
**Selectivity fixed.** The paragraph gave only the original beneficiary target of 500,000. The report also
records a revised target of 550,000, exceeded by 155 per cent (l.1313). Both now given.
Confirmed: 850,300 people (l.1273); 45,000 connections, 90 per cent of 50,000 (l.1276–1277); 449 water points,
90 per cent of 500 (l.1280–1281); 25 systems across 10 regions (l.1951, l.968) with 21 complete or about 95 per
cent complete at closing (l.1326); 3.6 against 13.88 and 11.10 cedis (l.1289–1290). Report `Outcomes:
Moderately Unsatisfactory` (l.192) and l.1482; review `a. Outcome Rating / Moderately Unsatisfactory` (l.553)
and `Efficiency Rating / Modest` (l.498, l.502). Dates 21 December 2016 and 15 June 2017 confirmed.

### 12. burkina-donsin-airport-roads-resettlement — corrected
**Added:** the only people-facing outcome in the review, which was missing — the share of the rural population
with access to an all-season road rose from 22.3 per cent to 34.3 per cent against a target of 33.3 per cent
(`bf_ieg` l.296–297).
**Attribution sharpened, and a scope difference exposed.** "the airport project body" is now "the Donsin
airport project authority", and the two rates of return are no longer presented as a like-for-like pair without
qualification: the 14.3 per cent was estimated for the **NR3 improvement** in the project authority's own
feasibility studies, the 15.3 per cent is the ex-post figure for **the project** (`bf_ieg` l.344–350). The
review itself makes the comparison, so the comparison is attributed to the review rather than asserted.
**Date removed.** The paragraph carried no date and none has been added: the review carries no `Date Posted`
line in the extracted text, so 17 June 2020 could be confirmed only from the card and the archive filename.
Confirmed: 24.3 km link road as planned, 17.2 km of NR3 against 17.5, 42.5 km of rural roads against 40
(l.252–259); Donsin 50→25 minutes meeting the target and Loumbila 23→15 against 14 (l.281–285); no
concessionaire agreement signed at completion, attributed in the review to the completion report paragraph 31,
not to the task leader's email that follows it (l.300–303); `Efficiency Rating / Modest` (l.374) and
`a. Outcome Rating / Moderately Unsatisfactory` (l.400).

### 13. rwanda-rssp2-marshland-resettlement — corrected
**Unsupported attribution cut.** The paragraph said the figures "come from the World Bank and the project's own
staff reporting on their own work", implying a figure from the implementer's resettlement report. No figure in
the paragraph comes from `rw2_rap16`; all come from the completion report. Changed to the lender alone.
**Added:** 3,324 hectares of new marshland brought into operation (`rw2_icr` l.346–347), and the report's own
date, 30 April 2013 (cover, l.35).
Confirmed: rice 5,597 → 18,675 tonnes against a target of 11,194 (l.288, l.1188–1189); rice yield 3 → 6.7
t/ha, "6.7 t/ha for direct beneficiaries" (l.545, l.983); nine sites, eight dams at five sites (l.346–350);
10,096 additional hectares to a total of 24,581 (l.373–374); ERR 47 per cent against 34 at appraisal (l.1377–
1379); `Outcomes: Highly Satisfactory` (l.215) and l.1442–1443.
Could not check: that no Evaluation Group review exists. See the limits section.

### 14. south-west-roads-turkestan-sairam-compensation — corrected
**Characterisation cut and replaced with the figure behind it.** "most of it widened to four-lane dual
carriageway" is not supported: the report's component outputs give 788 km upgraded to Category II **or**
Category I, 354 km to Category I and 181 km of dual carriageway (`kz_icr` l.1833, l.1837, l.1881), which does
not add to "most". The report does give a clean figure for the same idea in footnote 32 (l.1185): "2,050
carriageway-kilometers at completion compared with 1,265 carriageway-kilometers at entry". Used instead.
**Garbled sentence fixed.** "speed limits ... rose from 60 to 110 km an hour up to 140 km an hour" misreads
the report, which says the limit was raised "on many sections up to 140 kph from 60-110 kph" (l.911–912).
**Scopes now named.** The rate of return comparison is 15.6 per cent covering 96 per cent of project cost
against 13 per cent at appraisal covering the 1,062 km then planned (l.1059–1068).
**Added:** the vehicle operating cost baseline of US$0.26 per vehicle-kilometre (l.542, l.1710), without which
"down 35 per cent to US$0.17" cannot be read.
Confirmed: 1,281 km, over 200 km more than planned (l.1098); KazAvtoZhol's own figure with the report's
separate modelling supporting it (l.915–918); the 2017 road user study commissioned by the World Bank, 7 → 85
per cent satisfied, 123 → 79 minutes (l.919–926); report "The overall project outcome is rated Satisfactory
... Substantial efficiency" (l.1178–1180); review `a. Outcome Rating / Satisfactory` (l.555–556) and
`Efficiency Rating / Substantial` (l.533–534); report dated 19 June 2025 (cover, l.29). The self-reported flag
is right: the survey was commissioned by the lender, which the paragraph now says.

### 15. hanoi-ring-road-2-relocation — corrected
**Date error fixed.** "the completion report of 31 January 2018". The report's cover is dated **18 January
2018** (`vn_hanoi_icr` l.45); 31 January is the date in the archive filename only. Changed, and the review's
date (29 April 2018) added.
**Internal conflict now stated.** The journey-time targets differ inside the report. Its text and the review's
text both give 20 minutes for the bus and 18 for the motorcycle (`vn_hanoi_icr` l.891–895; `vn_hanoi_ieg`
l.389–398), while the report's results framework gives 22 and 15 against baselines of 28 and 21
(`vn_hanoi_icr` l.1831, l.1843). The paragraph gave only 20 and 18. Both now given, each located.
**Added:** the motorcycle baseline of 21 minutes, which was missing, and the shared efficiency rating Modest.
Confirmed: 6.1 km, Buoi / Dao Tan / Cau Giay interchanges, open since 18 January 2016 (l.885–887); traffic
count 77,000–93,000 vehicles, 50–75 per cent motorcycles (l.897); five more bus routes (l.890); ring road ERR
14.5 at appraisal and 18.5 at completion, bus rapid transit 21.0 and 6.0 (l.1043–1045, reproduced at
`vn_hanoi_ieg` l.560–564); report outcome Moderately Satisfactory (l.1058–1064); review `a. Outcome Rating /
Moderately Satisfactory` (l.594) and `Efficiency Rating / Modest` (l.569–570).

### 16. bahia-viver-melhor-ii-resettlement — corrected
**Fabricated attribution cut.** "which the completion report attributes to unfinished works in four areas" for
the 1,093 of 6,332 households. No such explanation is in the completion report; the report gives the figure
with no reason (`br_bahia_icr` l.1841–1842), and the explanation comes from the review: "not meeting the target
of 6,332 due to delays of construction work" (`br_bahia_ieg` l.247). The nearest "four" in that list is "4
local technical offices were installed meeting the target of 4" on the next line. Corrected and re-attributed.
**Date error fixed.** "the Independent Evaluation Group's review of 26 June 2014". The review's own
`Date Posted : 06/11/2014` (l.16) makes it **11 June 2014**; 26 June is the archive date in the URL. Changed,
and the report's own date, 30 April 2014, added.
**Attribution fixed.** The 16 per cent ex-post rate of return is the completion report's own calculation
(`br_bahia_icr` l.1337, l.1971, l.2143, l.2244, and its tables at l.1351–1356), which the review reports
(`br_bahia_ieg` l.277–279). The paragraph credited it to the review.
**Blanket flag corrected — item 6.** This is the one case of the 18 where "all the figures are the lender's
own" is not true. The US$3,000-per-household benchmark is from the UN Millennium Task Force on Improving the
Lives of Slum Dwellers, 2005 (`br_bahia_ieg` l.283–285), an outside source. The flag is now scoped to exclude
it. It is a benchmark, not an independent measurement of this project, so "no independent check was found"
still stands for the project's own figures.
Ratings confirmed from each document, which is where round 19 previously went wrong: report `Outcomes:
Moderately Unsatisfactory` (l.169) and l.1359–1363; review `a. Outcome Rating : Moderately Unsatisfactory`
(l.324). Both correct as the writer had them.
Confirmed: 92.5 → 100 per cent within 250 m of a paved road (l.267–273); 74.78 → 89.7 per cent sanitation
(l.281–288); 0 → 33 per cent within 1 km of social facilities (l.293–300); 14,080 against 12,812 and 904
against 600 (l.1867, l.1870); appraisal ERRs 35.8, 37.6 and 33.9 per cent, so the 33.9–37.6 range is right
(`br_bahia_ieg` l.264–265); US$11,482 per housing unit (l.283).

### 17. rurrenabaque-airport-land-compensation — corrected
**Attribution added.** The bus fare fall from 50 to 30 bolivianos was stated as a measurement. The report says
"Beneficiaries mentioned bus fares for a trip from San Buenaventura to Ixiamas have changed from BOB50 before
the Project to BOB30 after the Project" (`bo_icr` l.836–838) — an interview statement. Now attributed.
**Explanation completed.** The report gives three reasons for the lower return, not two: traffic volumes, the
shift from larger vehicles to motorcycles, and the change in the project's scope from paving the whole road to
paving 7 km (l.924–927). The third was missing.
**Wording tightened.** "the gains cannot be attributed to the project alone" is the writer's gloss; the report
says the earlier Beni prefecture and AASANA works "also largely contributed to operations reliability"
(l.874–877). Changed to the report's own claim.
**Added:** the review's date, 4 September 2024.
Confirmed: 22 bridges, 21 of them new (l.797–798); 7 km of about 114 km paved, rest kept up by maintenance
(l.801–803); impassable 75 days a year, 0 days of interruption since April 2023 (l.795, l.818–819); 3 hours to
under 2 dry season, over 5 hours to about 2 wet season (l.826–831); flights operated 65 → 95 per cent against
an original target of 90 (l.860–861, l.1762); 4,912 and 10,120 passengers (l.880); NPV US$0.5 million and IRR
13.0 per cent against US$25.7 million and 15.5 per cent, Table 6 (l.947–949). Report "overall outcome rating
is considered Moderately Satisfactory", final weighted 3.5 (l.1000, l.1028); review `a. Outcome Rating /
Moderately Unsatisfactory`, final weighted 3.36 (`bo_ieg` l.603–609). Report dated 31 May 2024 (cover, l.39).

### 18. philippines-nrimp2-unpaid-land-claims — confirmed on the conflict; one addition
**The reported conflict is real, exactly as described.** Both halves verified.
- 55 per cent: the report's PDO indicator table, Indicator 2, "Improved asset management of National Road
  Network - percentage of roads in good and fair condition as a share of total classified national roads",
  baseline 55, revised target 60, achieved at completion 55, comment "No change from baseline" (`ph_icr`
  l.316–323). Repeated in the narrative at l.1476–1477.
- 77 per cent: `ph_ieg` l.398–400, "As clarified by the project team, the revised PDO indicator - the
  percentage of roads in 'good and fair condition' improved from baseline of 55 percent to 77 percent,
  exceeding the project target of 60 percent", and the same sentence at l.361–363.
- The attribution is to the project team, not to a document: "As clarified by the project team", and the
  following sentences are "The project team further explained ..." (l.402).
- Same indicator, same measurement point (completion), against the same revised target of 60.
- The paragraph gives both figures, attributes the second to the project team, and offers no reconciliation.
  Confirmed and left that way. No tidy explanation has been added.
**Added:** both documents state why this indicator could not be attributed to the project — the works came to
about two per cent of the roads department's maintenance budget (`ph_icr` l.1478–1484; `ph_ieg` l.1027–1030,
"was not attributable to project"). That is the documents' own account of the gap's context, and it is not an
explanation of the 55-versus-77 difference.
Confirmed: 295 km against revised 280 and original 450, 680 km under long-term contracts meeting target, 1,200
km of 1,500 km rehabilitated (`ph_ieg` l.377–390); administrative efficiency 6 → 50 per cent against 70
(`ph_icr` l.305–314); 74 per cent stakeholder satisfaction against above 60 (l.326–333). Both outcomes
Moderately Satisfactory: report l.1787–1790; review `a. Outcome Rating / Moderately Satisfactory` (l.784–785).

---

## 1. What could not be checked, and what stopped it

- **That no Evaluation Group review exists for Siddhirganj (P095965) or Rwanda RSSP2 (P105176).** Both
  paragraphs assert it. Neither `/home/claude/r19/dl` nor any on-disk document can settle it; confirming an
  absence in the Bank's archive needs a catalogue query, and no network call was made. The writer used the
  projects API for Siddhirganj. The assertions are plausible and consistent with what is on disk, but they are
  unverified here. I left both as the writer had them rather than drop a claim I cannot disprove.
- **That the completion reports for Gujarat (P114827), Punjab (P090585) and Burkina Donsin (P120960) are not
  disclosed.** Same reason: no such file is on disk and no archive search was made. All three paragraphs say
  so, and all three correctly attribute their figures to the review rather than to the report.
- **The Burkina review's date.** The extracted text carries no `Date Posted` line, so 17 June 2020 could only
  be taken from the card and the archive filename. The date is therefore absent from that paragraph.
- **The Kazakhstan review's date.** Same: the paragraph names the review without a date.
- Nothing else was blocked. Every figure in all 18 paragraphs was located in an on-disk document, and no
  WebFetch quota was touched.

## 2. Every figure where two documents disagree

1. **Philippines NRIMP-2, share of national roads in good or fair condition at completion.**
   55 per cent, "No change from baseline", against a revised target of 60 — World Bank, Implementation
   Completion and Results Report (P079935), 21 June 2017, PDO indicator table, Indicator 2.
   77 per cent, "exceeding the project target of 60 percent" — Independent Evaluation Group, ICR Review
   (P079935), 20 November 2017, attributed in that document to what the project team told the evaluators.
   Same indicator, same point of measurement. Both in the paragraph; no explanation offered.
2. **Ghana Urban Water, rate of return at appraisal.**
   21 per cent — World Bank, Implementation Completion and Results Report (P056256), 21 December 2016,
   "EIRR of 26.18% (21% in the PAD)".
   None, and no comparison possible — Independent Evaluation Group, ICR Review (P056256), 15 June 2017:
   appraisal "included a financial model ... However, there was no economic analysis of the costs and benefits
   for the physical investments", so "Due to the lack of similar analysis in the PAD, comparison to a baseline
   is not possible." Both now in the paragraph. **This conflict was not in the writer's report.**
3. **DRC Emergency Multisector, people within reach of a feeder road.**
   Baseline 0, target 343,200, achieved 540,000 at 157 per cent — completion report, 29 October 2010, results
   table, Indicator 2.
   "increased from 343,200 to 540,000 at project closing" — Evaluation Group review, 6 June 2012. The review
   has turned a target into a baseline. The item was dropped from the paragraph rather than reported either way.
4. **DRC Emergency Multisector, N'Djili water production before the project.** 160,000 cubic metres a day in
   the completion report's results table; 150,000 in the same report's paragraph 48. The review carries
   160,000. Both figures now in the paragraph, each located. (Within one document, but it is a figure conflict.)
5. **Hanoi Ring Road 2, journey-time targets.** Bus 20 minutes and motorcycle 18 minutes in the completion
   report's text and in the review's text; 22 and 15 minutes in the completion report's own results framework.
   Both now in the paragraph.
6. **Hanoi Ring Road 2, project-level rate of return.** The review's own summary data sheet gives Appraisal
   16.50 per cent and ICR Estimate 14.00 per cent (covering 96.5 and 98.5 per cent of cost) — figures that
   appear in neither document's economic-analysis table, which give the component figures 21.0/6.0 for bus
   rapid transit and 14.5/18.5 for the ring road. Not used in the paragraph; the component figures are, as both
   tables give them.
7. **Tamil Nadu III, new household sewer connections.** 290,000 in the completion report's results table and
   narrative at l.1737; "over 299,000" at l.1094 and 298,688 in its annexes. Both now in the paragraph.
8. **Nepal Road Sector, efficiency rating.** Substantial — completion report, September 2020, section C.
   Modest — Evaluation Group review, 22 February 2021. A rating disagreement the writer's report did not list.
9. The five rating disagreements the writer did list are all confirmed against each document's own ratings
   block, with no reliance on the Group's reproduction of a report's rating: Lahore (Satisfactory / Moderately
   Satisfactory), Salem (Satisfactory / Moderately Satisfactory), Assam (Moderately Satisfactory with Modest
   efficiency / Satisfactory with substantial efficiency), DRC (Satisfactory / Moderately Satisfactory),
   Bolivia (Moderately Satisfactory / Moderately Unsatisfactory). Both Bahia ratings are Moderately
   Unsatisfactory in each document's own block, which is what the paragraph says.

## 3. Faults appearing in more than one paragraph

- **Dates taken from archive filenames rather than from the document's cover or its `Date Posted` line.** Three
  cases. Hanoi's report became "31 January 2018" from the filename `...01312018` when its cover says 18 January
  2018; Bahia's review became "26 June 2014" from `...20140626130834` when its own `Date Posted` is 11 June
  2014; Nepal's report became "30 September 2020" when its cover carries only "September 2020". Every date now
  in the file comes from the document itself, and where the document gives no date, none is given.
- **The explanation of one figure attached to a different figure.** Twice, and both times it made a project look
  tidier than its documents do. Gujarat: the reason for the rise in the rate of return (lower contract costs)
  was given as the reason for the fall in net present value, which the review attributes to traffic below
  forecast in the COVID-19 slowdown. Bahia: an explanation for 1,093 of 6,332 households was attributed to the
  completion report, which gives none, and worded as "unfinished works in four areas", which appears nowhere;
  the review says "delays of construction work". The habit to watch is supplying a cause for a shortfall from
  nearby text.
- **The lender's own count of sub-projects or scope swapped for a sample size.** Lahore's "14 infrastructure
  investments" is the beneficiary-survey sample against 39 completed sub-projects; Kazakhstan's "most of it
  widened to four-lane dual carriageway" is a characterisation the component figures do not support. In both
  cases a hard figure existed in the same document.
- **Shortfalls omitted while met targets were kept.** Nepal (the resilience bridges: six of 31, 0.73 km of 16
  km), Dehlon (roads in poor condition back to 31.6 per cent; vehicle operating costs up 10 and 11 per cent),
  Gujarat (the road-condition indicator and its 11.1-point project share). Each paragraph listed the indicators
  that were met or nearly met and left out the ones in the same list that were not. All now included.
- **The grep for staff statements was run but under-reported.** The writer's report names hits in six reviews.
  Running the same patterns, plus "the TTL", "team explained", "team stated" and "team provided", there are hits
  in ten: `ceip_icrr` 11, `pmsip_icrr` 7, `gshp2_icrr` 6, `punjrd_icrr` 6, `assam_icrr` 9, `cd_ieg` 14,
  `bf_ieg` 8, `kz_ieg` 6, `vn_hanoi_ieg` 2, `ph_ieg` 11; none in `nprsdp_icrr`, `kp_icrr`, `tnudp_icrr`,
  `gh_w_ieg`, `br_bahia_ieg`, `bo_ieg`. I read every hit in the four the writer missed. **Its substantive claim
  holds**: none of them supplies a delivery figure used in any paragraph. They concern a cancelled undisbursed
  balance and audit opinions (`pmsip_icrr` l.111, l.611), maintenance task forces, the existence of a
  resettlement plan and fiduciary compliance (`cd_ieg` l.295, l.427–438), safeguards and a post-closing status
  update (`bf_ieg` l.305, l.540, l.574), and supervision (`vn_hanoi_ieg` l.651). The Philippines 77 per cent
  remains the only delivery figure in any of the 18 that rests on a staff statement, and it is attributed. Note
  for Burkina in particular: the "no private operator selected" statement rests on the completion report
  (review, "ICR para 31"), not on the task leader's email that follows it.

**Manufactured conflicts — item 3.** None found. Every appraisal-versus-completion pair the writer listed as a
before-and-after is one: in each case the two figures measure the same indicator at two different dates, and
each is written as such. Two pairs needed the scopes naming and now have them: Burkina's 14.3 per cent is for
the NR3 works in the project authority's feasibility studies while the 15.3 per cent is for the whole project;
Kazakhstan's 13 per cent covers the 1,062 km planned at appraisal while the 15.6 per cent covers 96 per cent of
actual project cost. Both reviews make these comparisons themselves, so both are attributed to the review
rather than asserted. Swat's 29.9 and 28.0 per cent are correctly presented as appraisal estimates with the
review's statement that no completion estimate was made.

## 4. Wrong in the card data itself (reported, not changed)

- **`lahore-walled-city-shop-removals`, `lenders[0].role`:** "the restructuring of 2 August 2010". The
  completion report's key-dates table gives the restructurings as 08/31/2010 and 11/13/2012 (`pmsip_icr`
  l.195–196), and its narrative says "In August 2010, following the Mid-Term Review" (l.724). Nothing in the
  report supports 2 August; 31 August 2010 is what it gives.
- **`siddhirganj-pipeline-transmission-land`, `sources[0].date`:** given as 2020-09-26. The report's cover is
  dated **September 28, 2020** (`sidd_icr` l.41). The writer's paragraph uses 28 September, which is right, so
  the source date and the prose disagree within the same card.
- **`nepal-road-sector-unpaid-compensation`, `sources[0].date`:** given as 2020-09-30. The report's cover
  carries only "September 2020" with no day (`nprsdp_icr` l.52); 31 July 2020 is its exchange-rate date. The
  precise day is not in the document.
- **`hanoi-ring-road-2-relocation`, `sources[0]`:** the date 2018-01-18 is right (cover, l.45), but the URL it
  sits on is `...ICR-Document-01312018`, which is where the writer's "31 January" came from. Worth a note on
  the card so the filename is not read as the date again.
- **`bahia-viver-melhor-ii-resettlement`, `sources[1].date`:** 2014-06-11 is right and matches the review's own
  `Date Posted : 06/11/2014`. Flagged only because the URL carries 20140626 and the writer followed the URL.
- Not an error, but worth recording: three cards already flag internal document conflicts in their own prose
  (DRC's US$533,000 against US$553,000; Nepal's two disbursement labels; Salem's two restructuring dates). The
  same treatment is warranted for the figure conflicts listed in section 2 above, which are of the same kind.
- `lenders[0].role` was read in full for all 18. Apart from the Lahore restructuring date, every checkable
  numeric claim I tested held: CEIP approval 26 June 2013 and closing 31 December 2023 (`ceip_icr` l.217);
  Assam approval 13 March 2012 and actual closing 30 September 2019 (`assam_icr` l.217); Bolivia approval
  5 May 2011, original closing 31 December 2016, actual closing 2 August 2023 (`bo_icr` l.227); Philippines
  original closing 31 December 2012 and actual 31 December 2016 (`ph_icr` l.214); Bahia report and review dates;
  the DRC credit and grant amounts (`cd_icr` l.20–26).

## JSON log, as CHECKW.md asks

```json
{"entries":[
 {"id":"ceip-polder-land-payments-bangladesh","change":"none","why":"every figure, both ratings and both dates confirmed in the report's results framework and the review's own rating lines","self_reported":true},
 {"id":"lahore-walled-city-shop-removals","change":"text changed","why":"'14 infrastructure investments' was the beneficiary-survey sample, not the loan's scope (39 sub-projects in 29 urban centres); the Shahi Guzargah's own delivery figures exist in the report's Annex 10 and are now the core of the paragraph","self_reported":true},
 {"id":"nepal-road-sector-unpaid-compensation","change":"text changed","why":"minor bridge maintenance is 9,500 m not 9,000 m; the report's cover gives no day in September 2020; report rates efficiency Substantial against the review's modest; the resilience-works shortfall was omitted","self_reported":true},
 {"id":"swat-s3b-road-land-acquisition","change":"none","why":"all figures and both Moderately Satisfactory ratings confirmed; the appraisal rates of return are correctly not presented as results","self_reported":true},
 {"id":"siddhirganj-pipeline-transmission-land","change":"text changed","why":"the report names no restructuring for the 31 per cent figure, so '2014' was removed; dispatch-merit wording brought back to the document's","self_reported":true},
 {"id":"gujarat-highway-ii-delayed-compensation","change":"text changed","why":"the explanations for the rate-of-return rise and the net-present-value fall were merged and swapped; the project-attributed road-condition figure (11.1 percentage points of the rise from 43 to 81 per cent) was missing","self_reported":true},
 {"id":"dehlon-bypass-uncompensated-landowner","change":"text changed","why":"the fatal-accident series is the project's own road-safety indicator and is now framed as the review frames it; the road-condition and vehicle-operating-cost results were omitted","self_reported":true},
 {"id":"salem-tnudp-squatter-resettlement","change":"text changed","why":"the report gives 290,000 and 298,688 for the same sewer-connection item, so both are stated; dates added for both ratings","self_reported":true},
 {"id":"assam-roads-uncompensated-acquisition","change":"text changed","why":"the headline road-condition outcome was missing; the rating disagreement confirmed from each document's own block","self_reported":true},
 {"id":"drc-selembao-loange-compensation","change":"text changed","why":"the water figure is the N'Djili plant serving Kinshasa, not 'the project areas'; the report's own text and table disagree, 150,000 against 160,000; the review reads the feeder-road target as a baseline, so that item was cut","self_reported":true},
 {"id":"ghana-urban-water-unpaid-compensation","change":"text changed","why":"the two documents contradict each other on whether an appraisal rate of return exists, which the paragraph did not report; the revised beneficiary target of 550,000 was omitted","self_reported":true},
 {"id":"burkina-donsin-airport-roads-resettlement","change":"text changed","why":"the all-season road access outcome was missing; the two rates of return cover different scopes and the comparison is now attributed to the review","self_reported":true},
 {"id":"rwanda-rssp2-marshland-resettlement","change":"text changed","why":"no figure came from the implementer's resettlement report, so that attribution was dropped; marshland hectares and the report's date added","self_reported":true},
 {"id":"south-west-roads-turkestan-sairam-compensation","change":"text changed","why":"'most of it widened to four-lane dual carriageway' is unsupported and was replaced by the report's carriageway-kilometre figures; the speed-limit sentence misread the report; scopes of the two rates of return named","self_reported":true},
 {"id":"hanoi-ring-road-2-relocation","change":"text changed","why":"the report is dated 18 January 2018, not 31 January; the journey-time targets differ between the documents' text and the report's results framework, so both are stated","self_reported":true},
 {"id":"bahia-viver-melhor-ii-resettlement","change":"text changed","why":"'unfinished works in four areas' appears in no document and the explanation is the review's, not the report's; the review is dated 11 June 2014; the US$3,000 benchmark is from a 2005 UN study, so the blanket self-reported flag was scoped","self_reported":true},
 {"id":"rurrenabaque-airport-land-compensation","change":"text changed","why":"the bus fares are what interviewed beneficiaries said, not a measurement; the report gives three reasons for the lower return, not two","self_reported":true},
 {"id":"philippines-nrimp2-unpaid-land-claims","change":"text changed","why":"the reported conflict is real and correctly attributed and is left unreconciled; added both documents' statement that the indicator was not attributable to the project, the works being about two per cent of the maintenance budget","self_reported":true}
]}
```
