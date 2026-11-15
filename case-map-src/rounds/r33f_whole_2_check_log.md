# Independent check: whole-picture paragraphs, batch whole_2 (19 cases)

Checked against the cached Bank documents in /home/claude/work/cache/<PID>/ and, for the three non-Bank sources, against the pages themselves. Every Bank URL in `sources_add` was matched path-for-path against `harvest_manifest.json`: all 20 match, none constructed.

## Headline counts

- Paragraphs with a figure or clause cut: 3 (Kribi ARSEL output, DRC urban 'markets', Kakheti hotel beds)
- Paragraphs corrected in some way: 13 of 19; 6 left unchanged
- `self_reported` changed under the ruling: 1 (Kribi, false -> true). The other two false records (Gabon, The Gambia) were tested and upheld.
- Dated figures failing the date rule: 4 (Manta, Gabon, Ghana, Indonesia) - all four were a closing date that the document's own KEY DATES table contradicts.
- Voice: grep for 'I ', 'we ', 'our ', 'my ', 'this pass', 'read here', 'searches', 'this card' on word boundaries across all 19 `whole` values returns nothing, before and after.
- Every paragraph is 3 or 4 sentences.

## The ruling on `self_reported`, re-tested on all 19

Under the ruling, a figure from the lender, the borrower, the implementing agency, the operator or the lender's own evaluation office is self-reporting. Applying that:

- 17 records: `self_reported` **true**, unchanged and correct. Every figure is from an ICR, a project unit, or in Colombia's case the Independent Evaluation Group, which is the Bank's own office - the Colombia paragraph says so on the card, as required.
- Kribi (P110177): **false -> true**. See the entry below; the one outside figure was dropped on the unit question, which left only Bank figures.
- Gabon (P122776) and The Gambia (P122402): **false upheld**. Both rest on the UN Statistical Yearbook's table 30, whose source note reads 'International Telecommunication Union (ITU), Geneva, the ITU database, last accessed March 2023'. The ITU ran no part of either project, so it is an outside source.
- Two near-misses worth recording. Cameroon PDUE quotes CDE data and Georgia Kakheti quotes GeoStat data, which look outside the project at first glance. CDE is the water operator, so self-reporting; and the ICR labels the GeoStat-based tourism figures 'Calculations of project team, using data from GeoStat', so they are the project's arithmetic, not a published statistic. Both stay true.

## ARSEL, settled

ARSEL **does** qualify as independent: its 2021 activity report describes it as an Etablissement Public Administratif whose role is to 'assure la regulation, le controle et le suivi des activites des exploitants', and it names ENEO, KPDC, DPDC and EDC as the operators. It ran no part of the works. The figure fails on the unit instead, exactly as suspected. In the table under the heading 'Suivi de la consommation specifique des centrales thermiques', KPDC is a column and the rows are 'Energie Produite 2020' and 'Energie Produite 2021', holding 1 153 000 and 1 116 955. No column header in that table states a unit. The only unit nearby is the axis label of the chart beside it, which reads 'Energie en MW'. So the unit was taken from a neighbouring chart, and the chart's own label does not even say MWh. The sentence is cut: a figure with an invented unit cannot be published, and without a unit it says nothing.

## The two baseline disagreements

Both verified and both left as who-says-what. Neither paragraph interpolates a year.

**The Gambia.** Completion report para 32: 'In The Gambia, the share of the population with access to internet services surpassed its target by 93 percent, growing from 0.75 percent of the population in the 2010 baseline to 28 percent by closure in 2016, while the end-of-the-project target was 3 percent', footnote 31 'Government completion report. December 2016'. UN yearbook table 30, Gambia row under the printed year columns 2000 / 2005 / 2010 / 2015 / 2019 / 2020 / 2021: 0.9 / 3.8 / 9.2 / 17.6 / 28.8 / 31.6 / 33.0. The card gives 9.2 (2010), 17.6 (2015) and 33.0 (2021) - all printed values for printed years.

**Gabon.** Completion report: 'the ITU's percentage of individuals using the Internet indicator jumped from 24% in 2012 to 62% in 2019', footnote 46 citing the ITU World Telecommunication/ICT Indicators Database 2020. UN yearbook, Gabon row: 1.2 / 4.9 / 13.0 / 45.8 / 68.7 / 70.8 / 71.7. The card gives 13.0 (2010), 45.8 (2015) and 71.7 (2021) - again printed values for printed years.

One caution on the yearbook: the fetched text aligned each row's seven values to the seven printed year columns by position, and some figures carry an unexplained asterisk. The alignment is corroborated for Gabon by the completion report's own ITU series, and each row holds exactly seven values for seven columns, but it rests on positional reading rather than a cell-by-cell render.

## The Gambia case flag: whose figures are they?

**Every figure on the Gambia record is The Gambia's.** ICR00005569 covers Burkina Faso, The Gambia and Guinea under WARCIP APL 1B, and its results framework carries a programme-level row and a separate per-country row for the same indicators - a real trap, and the writer did not fall into it. The price figure is from the Gambia row (baseline 5,000.00, actual 500.00, unit USD/month/2Mbit/s); the programme row for the same indicator runs 7,300.00 to 739.66 and was correctly not used. The internet, business-price and rate-of-return figures all sit in sentences that begin 'In The Gambia' and end where the next sentence begins 'In Guinea'. The word 'Bijilo' does indeed appear nowhere in the ICR, which is a matter for the parent card rather than this paragraph.

## Achieved-against-target ratios, each read from its own table

Each was printed header row to footnote and read, not grepped. All seven hold:

| Figure | Where it sits | Verdict |
| --- | --- | --- |
| Riohacha lagoon 9% complete | Contract table 'CONTRACT 239-2015 - LAGUNAS', row Lagoons, 'Achieved (%)' column | holds |
| Riohacha treated wastewater 20% -> 14% | ICR para 35, past tense ('actually decreased from') | holds, but the favourable half of the same sentence was missing and has been added |
| Honduras 127 km against 200 / 300 / 143 | Indicator 3, achieved column 'At least 127 km' plus the comment naming all three target revisions | holds, unusually well told |
| Indonesia 578 km against 715 | Indicator row: baseline 0.00, original target 715.00, revised 578.00, actual 578.00 | holds |
| DRC urban US$108.2m of US$190m; grant sub-component US$6.4m of US$70m | FINANCING table, 'Actual Disbursed' column 108,159,215 against 'Original Amount' 190,000,000; para 16a | holds |
| Dominican Republic Maguaca 16% and in litigation | Indicator 2, achieved column 3 of 4, comment quoting the 16% | holds |
| Abidjan 21,500 sewer connections against 350,000 | Intermediate indicator 4: baseline 0, target 350,000, actual 21,500, comment 'Not achieved' | holds |

## Figures left unreconciled

Two, both internal contradictions inside a single Bank document. Neither is a fabrication by the writer; both values are printed.

1. **Kakheti hotel beds (P126033).** The outcome-indicator summary says 'achieved: 3016'; Table 15 in the annex gives the same indicator an Actual of 3,588. One document, two outcomes, no basis for preferring either. The figure is **cut** rather than reconciled, and the paragraph stands on the other three indicators.

2. **Gambia internet access (P122402).** The narrative says 28 percent at closure in 2016, twice. The results table gives the same indicator ('Gambia: Access to Internet Services (number of subscribers per 100 people)') an actual of 35.90 at 23-Dec-2016. The 28 percent is **kept**: it is the narrative finding, it is sourced in a footnote to the government's completion report, and the card already sets it against the ITU series as who-says-what. Recorded here as unreconciled.

## Routes that failed

None failed in a way that cost a fact. The ARSEL report had to be fetched twice, the table falling past the first 100,000 characters; the second fetch reached it and settled the question. No Bank document needed the web: all 19 completion reports, both evaluation reviews used, and the Colombia Project Performance Assessment Report were on disk as text.

## Case by case

### abidjan-riviera-2-shop-workers-unpaid-wages

**Change:** none - **self_reported:** true

Every figure sits in the Actual-Value-Achieved column of the ICR00003208 results framework (pp. x-xi), date achieved 03/31/2014: 5,750,000 people with improved water (revised target 4,500,000, 'Target exceeded (180%)'), 35,586 new piped household connections (target 32,000), 3,230,000 within 500 m of an all-season road (revised target 3,115,000), 21,500 new sewer connections against 350,000 ('Not achieved'), and reduction of waste water discharged into the Abidjan lagoon actual 0 against a target of 14,000 m3/day ('Target not achieved'). Favourable and damaging figures both present. self_reported true is correct under the ruling: every figure is the lender's.

### kribi-gas-plant-land-and-crops-taken-mpolongwe

**Change:** text changed - **self_reported:** true

ARSEL sentence CUT and self_reported flipped false->true. ARSEL does qualify as independent (the 2021 activity report describes ARSEL as an Etablissement Public Administratif that 'assure la regulation, le controle et le suivi des activites des exploitants'; it ran no part of the works). But the figure fails the table-reading rule: the KPDC column figures 1 153 000 (row 'Energie Produite 2020') and 1 116 955 (row 'Energie Produite 2021') sit in a table whose column headers state no unit at all, and the only unit nearby is a garbled axis label on the adjacent chart reading 'Energie en MW'. The unit 'megawatt hours' was inferred from a neighbouring chart, so it is not publishable, and the bare number says nothing without it. With ARSEL gone every remaining figure is the lender's. Bank figures all verified: ICR paras 34 and 46 and Figure 3 give 216 MW nameplate (196 MW contractual firm) added to a system 'of about 933MW', commercial operations May 2013, the Figure 3 Actual row 0/532/1,197/1,261/1,116 under year headers 2012-2016 with prose confirming 1,197 'by 2014' and 1,127 GWh/yr as the long-term target, and CFA 40 billion (US$82 million) raised, actual equal to target.

Before:

> The Kribi plant started selling power in May 2013, adding 216 megawatts to a national system of about 933 megawatts. The World Bank's completion report records generation of 532 gigawatt hours in 2013, 1,197 in 2014, 1,261 in 2015 and 1,116 in 2016, against a long-term target of 1,127 a year. Cameroon's electricity regulator, ARSEL, separately records the plant's operator KPDC producing 1,153,000 megawatt hours in 2020 and 1,116,955 in 2021. The completion report also records the CFA 40 billion local bank loan, about US$82 million, that the IDA guarantee was designed to make possible as raised in full.

After:

> The Kribi plant started selling power in May 2013, adding 216 megawatts of nameplate capacity to a national system of about 933 megawatts. The World Bank's completion report records generation of 532 gigawatt hours in 2013, 1,197 in 2014, 1,261 in 2015 and 1,116 in 2016, against a long-term target of 1,127 a year. The same report records the CFA 40 billion local bank loan, about US$82 million, that the IDA guarantee was designed to make possible as raised in full. These are the lender's own figures; no independent check was found.

### pdue-cameroon-unpaid-compensation-yaounde

**Change:** none - **self_reported:** true

All verified in the ICR results framework (pp. iv-vii), date achieved 08/31/2015: roads non-rural 63.2 km against revised target 41, drainage 108.5 km against 49, 435,263 people within 500 m, social connections 35,411 against target 70,000 ('Achievement rate is 51%', described at p. 1837 as subsidised), community water points 82 against revised target 1,200 with the comment 'The target value was an additional 1,200 standposts constructed. The activity was cancelled under the water component', and indicator 10 'Progress towards financial equilibrium of the urban water supply sector' actual 'Financial equilibrium not achieved'. Cities Douala, Yaounde, Bamenda, Maroua, Mbalmayo confirmed at para 9. self_reported true: all figures are the Bank's, the project unit's or the operator CDE's.

### drc-rn5-rn6-rn2-compensation-arrears

**Change:** none - **self_reported:** true

All verified in the ICR results framework (pp. vii-ix): roads rehabilitated 360 km actual against 522 at approval and 360 revised ('69% achieved for the original target, 100% achieved for the restructured project'); indicator comment 'Before, the Lubumbashi-Kasenga (RN5) drive took 60 hours, now 3 hours are enough. Access by truck to Gemena from both sides ... reduced from about one week before to 1-2 days'; 1,891,932 additional rural people with all-season road access; person days in labour-intensive public works actual 3,500,000. Closing 06/30/2012 is the date-achieved cell. self_reported true.

### drc-urban-project-injury-threats-and-works-before-resettlement

**Change:** text changed - **self_reported:** true

'markets' CUT from the first sentence: a target read as an output. 'market' appears three times in the whole ICR and never as a delivered output - para 15 says only that 'The investments were expected to cover roads and transport, drainage, markets, water, solid waste', while the Key Outputs list records roads, drainage, erosion works and person-days. Replaced with 'erosion works', which the outputs list does record ('Two heads of erosion stabilized in Kananga'). Everything else holds: FINANCING table gives Original Amount 190,000,000 and Actual Disbursed 108,159,215; KEY DATES gives Actual Closing 30-Jul-2021; the roads indicator reads baseline 0.00, original target 11.90, revised 31.80, actual 31.81; beneficiaries 406,911 against revised 391,000; para 16a gives 'Performance-based investments (appraisal: US$ 30.0 million, AF: US$ 70 million, final cost: US$ 6.4 million)'; and 'For the final performance evaluation carried out in 2020, all four cities (Bukavu, Goma, Kikwit and Matadi) met the minimum conditions and passed the performance criteria.' Nine cities is the achieved value of the 'Cities with improved livability' indicator, which names all nine.

Before:

> The project funded roads, drainage and markets in nine Congolese cities and a performance grant scheme for city governments. By the Bank's own count at closing in July 2021, 406,911 people had improved urban living conditions against a revised target of 391,000, and 31.81 kilometres of city road had been rehabilitated against a revised target of 31.8 kilometres, raised from 11.9 kilometres at appraisal. Of US$190 million originally committed, US$108.2 million was disbursed; the performance-based investment sub-component spent US$6.4 million of the US$70 million planned after the additional financing, and four cities met the performance conditions. The figures are the lender's own; no independent check was found.

After:

> The project funded roads, drainage and erosion works in nine Congolese cities and a performance grant scheme for city governments. By the Bank's own count at closing in July 2021, 406,911 people had improved urban living conditions against a revised target of 391,000, and 31.81 kilometres of city road had been rehabilitated against a revised target of 31.8 kilometres, raised from 11.9 kilometres at appraisal. Of US$190 million originally committed, US$108.2 million was disbursed; the performance-based investment sub-component spent US$6.4 million of the US$70 million planned after the additional financing, and four cities met the performance conditions. The figures are the lender's own; no independent check was found.

### kinshasa-water-works-land-and-houses-taken

**Change:** none - **self_reported:** true

All verified in the ICR results framework (pp. vii-ix), date achieved 05/31/2013: 216,000 people with improved water sources against target 239,000; standposts constructed or rehabilitated 86 against target 80; primary, secondary and tertiary network 85.3 km against 140 km ('61% achieved'); roads rehabilitated non-rural 40.2 km against 40.0; people within 500 m of an all-season road 1,300,000 against target 800,000. School grants and Bandundu both confirmed. self_reported true.

### colombia-water-easements-unsettled-at-closing

**Change:** text changed - **self_reported:** true

Two corrections. (1) 44,205 and 25,773 were published as 'new water connections' and 'new sewer connections'; they are people, not connections. The ICR indicators read '40,000 new consumers connected to urban water supply networks' and '60,000 new consumers connected to urban sewerage networks', Table 1 labels them 'New Access: Number of People Reached', and the Annex 2 summary table columns are 'Pop. New Access Water Supply' and 'Pop. New Access Sanit. (Sew. Conn.)'. Rewritten as people newly connected. (2) The damaging sewerage figures now carry the favourable clause from the same PPAR paragraph: 'Current data show that sewerage connections increased 30 percent from project start-up'. Everything else verified: 1,520,554 against target 1,200,000 with the ICR's own comment 'The extent to which infrastructure improvements enhance access to reliable and safe WSS is unclear since a M&E system wasn't defined at the subproject level'; PPAR p. 517-528 'The average coverage in all the project areas increased to 85 percent by 2014, which is 10 percent lower than the national average of 95 percent', 'coverage ranges between not having been implemented (in 10 subprojects)', 'The average coverage in the participating municipalities was 60 percent, compared with the average target of 87 percent'. The 2016 date and the field basis check out: the PPAR rests on an 'IEG mission that visited Colombia during March 6-19, 2016' with 'field visits to a stratified sample of 24 projects'. self_reported stays TRUE under the ruling and the paragraph says the Evaluation Group is the lender's own office, as required.

Before:

> The loan paid for water and sewer sub-projects in municipalities across Colombia. The Bank's completion report counts 1,520,554 people living where the infrastructure was upgraded, against a target of 1.2 million, with 44,205 new water connections against a target of 40,000, but 25,773 new sewer connections against a target of 60,000. It adds that no monitoring system was set up at sub-project level, so how far the works improved service is unclear. A later field review by the Bank's Independent Evaluation Group, still the lender's own office, found water coverage in the project areas up to 85 percent by 2014 against a national average of 95 percent, sewerage coverage averaging 60 percent against a target of 87 percent, and sewerage works not carried out at all in ten sub-projects.

After:

> The loan paid for water and sewer sub-projects in municipalities across Colombia. The Bank's completion report counts 1,520,554 people living where the infrastructure was upgraded, against a target of 1.2 million, with 44,205 people newly connected to urban water networks against a target of 40,000 and 25,773 newly connected to urban sewer networks against a target of 60,000. It adds that no monitoring system was set up at sub-project level, so how far the works improved service is unclear. A later field review by the Bank's Independent Evaluation Group, still the lender's own office, found water coverage in the project areas up to 85 percent by 2014 against a national average of 95 percent, sewerage connections up 30 percent from the project's start, and sewerage coverage averaging 60 percent against a target of 87 percent, with no sewerage works carried out at all in ten sub-projects.

### riohacha-wayuu-lagoon-resettlement

**Change:** text changed - **self_reported:** true

Favourable clause added from the same ICR sentence (para 35): 'Wastewater treatment targets were achieved in Barrancas and Fonseca and exceeded in San Juan del Cesar and Villanueva, but the average wastewater treatment rate in Project areas actually decreased from 20 percent to 14 percent'. The published paragraph had only the second half. Figures verified: 409,160 against 357,285; service continuity indicator baseline 8.00, original target 22.00, revised 14.00, actual 11.40; micro-metering baseline 16.00, revised target 81.00, actual 51.00; contract table 'CONTRACT 239-2015 - LAGUNAS', row Lagoons, Achieved (%) column 9%. KEY DATES gives Actual Closing 16-Apr-2018, so 'closing in 2018' holds. self_reported true.

Before:

> The loan paid for water and sewer works across La Guajira. By the Bank's own count at closing in 2018, 409,160 urban residents had access to improved water sources against a target of 357,285, water ran for an average of 11.4 hours a day against 8 hours before the project and a revised target of 14, and metering reached 51 percent of households against a target of 81 percent. The wastewater lagoons the works were meant to feed were not finished: the completion report puts the Riohacha lagoon contract at 9 percent complete at closing, and records the average share of wastewater treated in the project areas falling from 20 percent to 14 percent. These are the lender's own figures; no independent check was found.

After:

> The loan paid for water and sewer works across La Guajira. By the Bank's own count at closing in 2018, 409,160 urban residents had access to improved water sources against a target of 357,285, water ran for an average of 11.4 hours a day against 8 hours before the project and a revised target of 14, and metering reached 51 percent of households against a target of 81 percent. The wastewater lagoons the works were meant to feed were not finished: the completion report puts the Riohacha lagoon contract at 9 percent complete at closing, and records wastewater treatment targets met in Barrancas and Fonseca and exceeded in San Juan del Cesar and Villanueva while the average share of wastewater treated across the project areas fell from 20 percent to 14 percent. These are the lender's own figures; no independent check was found.

### djibouti-ambouli-dike-resettlement

**Change:** none - **self_reported:** true

All verified in the ICR results framework (pp. iii-v). PDO indicator 3 achieved value 'Dike reconstructed and provided with erosion control', date achieved 03/31/2009, with the comment in the same cell 'The dike is expected to protect the city up to a 1500m3/s flood intensity provided it is well maintained' - so the conditional 'if it is maintained' is the document's own, not added. Intermediate indicator 1 achieved 'Successful reconstruction of Km. 2.5 of flood protection dike', comment 'Dike was completed in March 2009'. Intermediate indicator 2 achieved column: '14 paved roads, 2 bridges, 5 Km. of storm-water channels, 500 manholes'. April 2004 floods confirmed at para 225. self_reported true.

### canal-neyba-arroyo-rico-expropriations

**Change:** text changed - **self_reported:** true

One correction: the stations clause dropped the favourable half of its own sentence. The ICR comment reads '14 of the 64 hydro-meteorological stations have been partially vandalized, but stored safely, repaired, and will be re-installed in the short term once sites are secured', and Annex 2 adds 'then disassembled and stored in safe place for future re-installation'. 'Vandalised' is now 'partly vandalised, then stored and repaired for re-installation', and 'weather and river-gauging' becomes the document's own 'hydro-meteorological' in plain words. Other figures verified in the results framework (pp. ix-x), date achieved 10/31/2016: irrigation 37,218 ha against original target 12,000 (revised 11,577); dams actual 3 of 4 with the comment 'The works of the Maguaca dam were under litigation with only 16% of the works achieved by the contractor at closing'; transmission 152 km actual equal to revised target; hydro capacity actual 252 MW against revised target 254 MW.

Before:

> The loan paid to repair irrigation, dams and power works after storms. By the Bank's own count at closing in October 2016, irrigation service had been restored on 37,218 hectares against a target of 12,000, 152 kilometres of transmission line had been rebuilt, and 252 megawatts of hydro capacity had been restored against a revised target of 254. Of four dams to be rehabilitated three were done, while works on the Maguaca dam were in litigation with 16 percent complete at closing, and 14 of 64 new weather and river-gauging stations are recorded as vandalised. These are the lender's own figures; no independent check was found.

After:

> The loan paid to repair irrigation, dams and power works after storms. By the Bank's own count at closing in October 2016, irrigation service had been restored on 37,218 hectares against a target of 12,000, 152 kilometres of transmission line had been rebuilt, and 252 megawatts of hydro capacity had been restored against a revised target of 254. Of four dams to be rehabilitated three were done, while works on the Maguaca dam were in litigation with 16 percent complete at closing, and 14 of 64 new hydrological and weather monitoring stations are recorded as partly vandalised, then stored and repaired for re-installation. These are the lender's own figures; no independent check was found.

### manta-properties-taken-without-agreement

**Change:** text changed - **self_reported:** true

DATE RULE FAILURE corrected. The paragraph said 'at closing in 2021'; the ICR KEY DATES table gives Actual Closing 31-Dec-2020. The 2021 almost certainly came from the ICR's own cover date (30-Nov-2021) and from the data notes ('Updated based on the data provided by the PIU in May, 2021'; 'According to data from August of 2021'), neither of which dates the figures to a closing. The figures are now undated and the closing is stated separately and correctly. Also removed the opinion word 'only' from 'fell only from 88 percent', and 'eaten by' from the working-ratio gloss (the ICR defines it at para 1098 as EPAM's ability to recover its operating costs from revenue). Figures verified: continuity baseline 14.00, target 24.00, actual 19.30; paved access actual 23,024 against target 22,100; household sewerage connections benefiting from rehabilitation works actual 15,740 against target 15,500; working ratio baseline 88.00, original 60.00, revised 70.00, actual 85.00, with 'Decreased from 88% to 85%, missing the restructured target of 70%'; travel time baseline 15.00, target 10.00, actual 13.00.

Before:

> The loan paid for water, sewer and street works in Manta. By the Bank's own count at closing in 2021, water ran for an average of 19.3 hours a day against 14 hours before the project and a target of 24, 23,024 people were given paved access to their houses in lower-income neighbourhoods, and 15,740 household sewer connections were covered by rehabilitation works. The utility's working ratio, the share of revenue eaten by running costs, fell only from 88 percent to 85 percent against a revised target of 70 percent, and travel time along the Par Vial corridor fell from 15 to 13 minutes against a target of 10. These are the lender's own figures, taken from the project unit; no independent check was found.

After:

> The loan paid for water, sewer and street works in Manta. By the Bank's own count, water ran for an average of 19.3 hours a day against 14 hours before the project and a target of 24, 23,024 people were given paved access to their houses in lower-income neighbourhoods, and 15,740 household sewer connections were covered by rehabilitation works. The utility's working ratio, the share of revenue taken up by running costs, fell from 88 percent to 85 percent against a revised target of 70 percent, and travel time along the Par Vial corridor fell from 15 to 13 minutes against a target of 10. The project closed in December 2020; these are the lender's own figures, taken from the project unit, and no independent check was found.

### lalara-fibre-assets-destroyed

**Change:** text changed - **self_reported:** false

DATE RULE FAILURE corrected: 'at closing in 2021' replaced with the ICR's own Actual Closing of 31-Oct-2020 (KEY DATES table; para 1009 also writes 'at project closing (2020)'). The 2021 came from the ICR's cover date, 09-Apr-2021. self_reported FALSE is upheld: the UN Statistical Yearbook was opened directly and its table '30 Internet usage' carries the source note 'International Telecommunication Union (ITU), Geneva, the ITU database, last accessed March 2023', with year columns 2000, 2005, 2010, 2015, 2019, 2020, 2021 and the Gabon row 1.2 / 4.9 / 13.0 / 45.8 / 68.7 / 70.8 / 71.7 - the ITU is outside the project, so it qualifies. No year is interpolated: 2010, 2015 and 2021 are all printed columns. The two baseline accounts are left as who-says-what, not reconciled. Bank figures verified: 'The full 1,760-km fiber-optic terrestrial backbone ... connects 26 cities to the capital Libreville, and reaches the borders of Congo, Cameroon, and Equatorial Guinea'; 'The first 1,140 km ... has been in commercial operation since February 2019'; 'The 620-km extension ... was fully completed in March 2020 but was not commercialized as of the project's closing date'; price 'from a baseline of $10,500 to $273' with the unit stated in the indicator name as 'US$/month/2 Mbps', and retail 'to $6/Mbps/month from a baseline of $218'; and 'the ITU's percentage of individuals using the Internet indicator jumped from 24% in 2012 to 62% in 2019' (footnote 46, ITU database).

Before:

> By the Bank's own count at closing in 2021, 1,760 kilometres of fibre optic cable had been laid, linking 26 towns to Libreville and reaching the borders of Congo, Cameroon and Equatorial Guinea. The first 1,140 kilometres has been sold commercially since February 2019; the 620-kilometre extension was finished in March 2020 but was not yet being sold when the project closed. The same report puts the wholesale price of an international 2 megabit link to Europe down from US$10,500 to US$273 a month, and retail internet down from US$218 to US$6 per megabit a month. The United Nations Statistical Yearbook, using International Telecommunication Union figures, puts the share of people in Gabon using the internet at 13.0 percent in 2010, 45.8 percent in 2015 and 71.7 percent in 2021, while the completion report quotes ITU figures of 24 percent for 2012 and 62 percent for 2019.

After:

> By the Bank's own count, 1,760 kilometres of fibre optic cable had been laid by the project's close in October 2020, linking 26 towns to Libreville and reaching the borders of Congo, Cameroon and Equatorial Guinea. The first 1,140 kilometres has been sold commercially since February 2019; the 620-kilometre extension was finished in March 2020 but was not yet being sold when the project closed. The same report puts the wholesale price of an international 2 megabit link to Europe down from US$10,500 to US$273 a month, and retail internet down from US$218 to US$6 per megabit a month. The United Nations Statistical Yearbook, using International Telecommunication Union figures, puts the share of people in Gabon using the internet at 13.0 percent in 2010, 45.8 percent in 2015 and 71.7 percent in 2021, while the completion report quotes ITU figures of 24 percent for 2012 and 62 percent for 2019.

### dartlo-telavi-rehabilitation-compensation-delays

**Change:** text changed - **self_reported:** true

Hotel-beds figure CUT: the ICR contradicts itself on it. The outcome-indicator summary says 'Increase number of hotel beds in circuit route areas (baseline: 1610, target: 1932, achieved: 3016)', while Table 15 in the annex gives the same indicator as Baseline 1,610, Target 1,932, Actual 3,588. The published 3,016 is in the document, so not invented, but one source cannot be quoted for two different outcomes, and neither value can be preferred, so the figure is dropped rather than reconciled. Also dropped 'revised' from the private-investment target: Table 15 shows Baseline 0, Target 50,000,000, Actual 61,000,000 with no revision recorded. Remaining figures verified: 'Roads constructed and rehabilitated (target: 20 km, achieved: 26.3 km)'; 'rehabilitation works undertaken by the project (target: 500, achieved: 907)'; points of sale 'baseline:248, target:323, achieved: 337'; Actual Closing 31-Dec-2017. self_reported true - the region-wide tourism growth figures in Annex 7 draw on GeoStat but the ICR labels them 'Calculations of project team, using data from GeoStat', so they are not an outside check.

Before:

> The project paid for roads, water and heritage works in Kakheti to draw tourists. By the Bank's own count at closing in December 2017, 26.3 kilometres of road had been built or rehabilitated against a target of 20, and 907 households had piped water connections from the works against a target of 500. The same report counts hotel beds in the tourist circuit rising from 1,610 to 3,016, points of sale from 248 to 337, and US$61 million of private investment against a revised target of US$50 million. These are the lender's own figures; no independent check was found.

After:

> The project paid for roads, water and heritage works in Kakheti to draw tourists. By the Bank's own count at closing in December 2017, 26.3 kilometres of road had been built or rehabilitated against a target of 20, and 907 households had piped water connections from the works against a target of 500. The same report counts points of sale in the renovated heritage sites and towns rising from 248 to 337 against a target of 323, and US$61 million of private investment against a target of US$50 million. These are the lender's own figures; no independent check was found.

### igoeti-sveneti-highway-worker-death-and-land-damage

**Change:** text changed - **self_reported:** true

'in Georgia' removed from the road-deaths clause: the indicator is simply 'Number of fatalities per 10,000 cars' and neither the indicator nor its comment states the area it covers, so the national scope was an inference. The figures themselves hold, with the date in the same cell: baseline 14.5, target 12, actual 6.8, date achieved 12/29/2011, comment 'Exceeded by 43% for target year of 2011. Data for 2012 is not available yet.' Also verified: km upgraded 48 actual against 48 target, 'Fully met'; transit time baseline 19, target 12, actual 11.8; car VOC 0.20 to 0.18; truck VOC 0.76 to 0.71; Closing 06/30/2012.

Before:

> The credit paid to upgrade 48 kilometres of the east-west highway between Igoeti and Sveneti. By the Bank's own count at closing in June 2012 the full 48 kilometres were built, and the drive between the two points fell from 19 minutes to 11.8. The same report puts operating costs for a car at US$0.18 a kilometre against US$0.20 before the works, and for a truck at US$0.71 against US$0.76, and records road deaths per 10,000 cars in Georgia falling from 14.5 to 6.8 by the end of 2011. These are the lender's own figures; no independent check was found.

After:

> The credit paid to upgrade 48 kilometres of the east-west highway between Igoeti and Sveneti. By the Bank's own count at closing in June 2012 the full 48 kilometres were built, and the drive between the two points fell from 19 minutes to 11.8. The same report puts operating costs for a car at US$0.18 a kilometre against US$0.20 before the works, and for a truck at US$0.71 against US$0.76, and records road deaths per 10,000 cars falling from 14.5 to 6.8 by the end of 2011. These are the lender's own figures; no independent check was found.

### kumasi-lands-office-farmers-displaced

**Change:** text changed - **self_reported:** true

DATE RULE FAILURE corrected: 'at closing in December 2019' is two claims and one of them is wrong. The ICR KEY DATES table gives Actual Closing 20-Jan-2020. 31-Dec-2019 is the date cell of the two indicators themselves, so the date is kept and attached only to the figure it belongs to ('by the end of 2019'), and the false closing claim is dropped. Also 'inaccurately recorded' corrected to the document's word: 'During preparation for the ICR, both the baseline data and the target data were found to be unclear and inaccurately reported.' Verified: registered land transactions baseline 0, target 30,000, actual 82,438, date 31-Dec-2019; deeds turn-around baseline 3 months, target 1 month, actual 2.11 months, date 31-Dec-2019; the title turn-around indicator actual is 'n/a'; para 18 'Component 4 (US$10.78 million in PAD, US$17.16 million disbursed). Human Resource Development and Project Management ... More funds were expended than was envisaged during project preparation because of the addition of the new office for land sector agencies in Kumasi and the extended length of the project'.

Before:

> The project paid to modernise Ghana's land registries, including a new office for the land sector agencies in Kumasi. By the Bank's own count at closing in December 2019, 82,438 land transactions had been registered against a target of 30,000, and the time to register a deed in the reformed offices fell from three months to 2.11 months against a target of one month. The same report says the time to register a land title could not be reported because the baseline and target were found to be unclear and inaccurately recorded, and that spending on the component paying for the Kumasi building and project management reached US$17.16 million against US$10.78 million planned. These are the lender's own figures; no independent check was found.

After:

> The project paid to modernise Ghana's land registries, including a new office for the land sector agencies in Kumasi. By the Bank's own count, 82,438 land transactions had been registered by the end of 2019 against a target of 30,000, and the time to register a deed in the reformed offices fell from three months to 2.11 months against a target of one month. The same report says the time to register a land title could not be reported because the baseline and target were found to be unclear and inaccurately reported, and that spending on the component paying for the Kumasi building and project management reached US$17.16 million against US$10.78 million planned. These are the lender's own figures; no independent check was found.

### bijilo-cable-route-compensation-unpaid

**Change:** text changed - **self_reported:** false

EVERY FIGURE ON THIS RECORD IS THE GAMBIA'S, not the programme's and not another member country's. ICR00005569 covers Burkina Faso, The Gambia and Guinea (WARCIP APL 1B) and its results framework carries a programme-level row and a per-country row for the same indicators; the writer took the Gambia rows throughout and avoided the programme rows. Checked one by one: internet access - para 32 'In The Gambia, the share of the population with access to internet services surpassed its target by 93 percent, growing from 0.75 percent of the population in the 2010 baseline to 28 percent by closure in 2016, while the end-of-the-project target was 3 percent', footnote 31 'Government completion report. December 2016'; price - the Gambia row reads baseline 5,000.00 (31-Dec-2010), target 1,000.00, actual 500.00 (23-Dec-2016), unit 'USD/month/2Mbit/s', while the PROGRAMME row is 7,300.00 to 739.66 and was correctly not used; business price - para 35 runs 'In The Gambia, the price of international E1 capacity decreased ... During implementation, the price of 1 Mbit/s per month for enterprises decreased by 73 percent, from US$1,500 to around US$400', the next sentence beginning 'In Guinea', and the Gambia key-outputs list confirms 'The Gambia 1. Retail price of internet services. Target US$500 per month; Results US$400 per month'; return - para 42 'In The Gambia, the IRR of 38 percent shows that investment in ACE was highly profitable with a net present value (NPV) of US$17 million'. Two changes made. (1) 'and the cable route inland' CUT: the Gambia key-outputs list records no terrestrial backbone for The Gambia. It records the ACE membership fees 'made as scheduled in 2011/2012', a landing station 'built and reached a capacity of 10 Gbit/s', 'new internet capacity to 36 ministries, departments and agencies', and 'the connectivity of six secondary schools'. Those replace it. (2) 'the return' is now 'the internal rate of return', the document's own term, and the US$400 endpoint added. UNRECONCILED, and flagged here rather than published: the ICR's own results table gives this indicator ('Gambia: Access to Internet Services (number of subscribers per 100 people)') a baseline of 0.75 and an actual of 35.90 at 23-Dec-2016, not the 28 percent its narrative states twice (paras 32 and 3655). The 28 percent is kept because it is the narrative finding and is sourced to the government report, and because the card sets it against the ITU figures as who-says-what. Also noted for the parent card: the word 'Bijilo' appears nowhere in this ICR. self_reported FALSE upheld - the UN Statistical Yearbook table 30 was opened directly, credits the ITU database, and its Gambia row under the printed year columns is 0.9 / 3.8 / 9.2 / 17.6 / 28.8 / 31.6 / 33.0 for 2000 / 2005 / 2010 / 2015 / 2019 / 2020 / 2021, so 9.2, 17.6 and 33.0 are printed values for printed years and no year is interpolated.

Before:

> The grant paid The Gambia's membership of the Africa Coast to Europe submarine cable and the cable route inland. By the Bank's count, drawing on the government's own completion report, the share of Gambians with access to internet service rose from 0.75 percent in 2010 to 28 percent by the country's part of the project closing in 2016, against a target of 3 percent; the United Nations Statistical Yearbook, using International Telecommunication Union figures, puts internet use in The Gambia at 9.2 percent in 2010, 17.6 percent in 2015 and 33.0 percent in 2021. The same report puts the wholesale price of an international 2 megabit link to Europe down from US$5,000 to US$500 a month, and the business price of a megabit a month down 73 percent from US$1,500. Its own calculation puts the return on the cable investment at 38 percent, with a net present value of US$17 million.

After:

> The grant paid The Gambia's membership fees for the Africa Coast to Europe submarine cable, a landing station that reached 10 gigabits a second, and internet links for 36 government bodies and six secondary schools. By the Bank's count, drawing on the government's own completion report, the share of Gambians with access to internet service rose from 0.75 percent in 2010 to 28 percent by the country's part of the project closing in 2016, against a target of 3 percent; the United Nations Statistical Yearbook, using International Telecommunication Union figures, puts internet use in The Gambia at 9.2 percent in 2010, 17.6 percent in 2015 and 33.0 percent in 2021. The same report puts the wholesale price of an international 2 megabit link to Europe down from US$5,000 to US$500 a month, and the business price of a megabit a month down 73 percent, from US$1,500 to about US$400. Its own calculation puts the internal rate of return on the cable investment at 38 percent, with a net present value of US$17 million.

### honduras-road-rehabilitation-ii-land-taken

**Change:** none - **self_reported:** true

The achieved-to-target chain verifies exactly. ICR indicator 3 'Up to 200 km of primary and secondary roads returned to good condition': achieved column 'At least 127 km', date 05/31/2015, with the comment 'On approval of the AF on May 5, 2009, the target value was increased to 300 km ... At the June 13, 2013 restructuring the target was adjusted again to 143 km to reflect only those works which were going to be financed under the credits. At Project closing, 127 km had been completed.' Indicator 4 achieved column: 'Average reduction in VOCs as follows: San Lorenzo - Olanchito 36-42% and El Porvenir - Marale 37-44%'. self_reported true.

### cap-labadie-road-compensation-escrow

**Change:** text changed - **self_reported:** true

One correction: the 27-against-14 comparison now carries the caution the document attaches to it in the same paragraph - 'The Investment Economic Internal Rate Return (EIRR) was estimated to be 14 percent. An ex-post consumers' surplus analysis was performed for the ICR and showed a 27 percent Economic Internal Return Rate (EIRR). Despite a different methodology (producers' surplus vs consumers' surplus) the ex-post rate is higher than the ex-ante EIRR.' Comparing the two straight, as the paragraph did, is the thing the report itself warns about. Other figures verified: 'This resulted in the construction of an 8.5 km road ... Out of the 95,000 days of work for the local labor force man-days generated by the Project, the road works also generated job opportunities of 45,000 man-days'; Annex cost table 'Labadie works ... 8,198,995 ... 8.5 km' and para 21 'The Cap-Haitien - Labadie road rehabilitation final cost is US$8,198,995 for 8.5km'; indicator 'Roads rehabilitated, Rural' baseline 0.00, original target 0.00, revised target 100.00, actual 100.00; para 40 'More than 1,100,000 people benefited directly from repaired infrastructure'; Actual Closing 29-Jun-2018.

Before:

> The grant paid for earthquake recovery works, among them the road from Cap-Haïtien to Labadie. By the Bank's own count at closing in June 2018, 8.5 kilometres of that road were built for US$8.2 million of works, and the road accounted for 45,000 of the 95,000 days of local paid labour the project generated. Across the project, 100 kilometres of road were stabilised or rehabilitated, matching the revised target, and 1.1 million people were counted as benefiting from repaired infrastructure. The completion report's own after-the-fact calculation puts the road's economic rate of return at 27 percent, against 14 percent estimated when the financing was approved; both figures are the lender's, and no independent check was found.

After:

> The grant paid for earthquake recovery works, among them the road from Cap-Haitien to Labadie. By the Bank's own count at closing in June 2018, 8.5 kilometres of that road were built for US$8.2 million of works, and the road accounted for 45,000 of the 95,000 days of local paid labour the project generated. Across the project, 100 kilometres of road were stabilised or rehabilitated, matching the revised target, and 1.1 million people were counted as benefiting from repaired infrastructure. The completion report's own after-the-fact calculation puts the road's economic rate of return at 27 percent, against the 14 percent estimated when the financing was approved, and notes the two rest on different methods; both figures are the lender's, and no independent check was found.

### lubuk-alung-kuraitaji-road-works-death

**Change:** text changed - **self_reported:** true

DATE RULE FAILURE corrected: 'closing in May 2021' replaced with the ICR KEY DATES value, Actual Closing 30-Jun-2021. Also added the traffic target the paragraph had left out, which is the damaging half of its own sentence: the indicator reads baseline 7,505.00, revised target 14,544.00, actual 14,490.00, and the ICR says 'Although the AADT target (14,544) was not fully achieved (14,490 was [reached])'. Other figures verified: km of improved national roads baseline 0.00, original target 715.00, revised 578.00, actual 578.00, with cancellation of road packages recorded in the restructuring table; para 21c 'typical car (-8.00 percent achieved vs. the target of -5.00 percent); (ii) typical bus (-18.00 percent achieved vs. the target of -8.00 percent); and (iii) typical heavy trucks (-14.00 percent achieved vs. the target of -10.00 percent)'; para 21b 'light vehicles (-21.11 percent)'.

Before:

> The loan paid to widen and strengthen national roads in western Sumatra. By the Bank's own count at closing in May 2021, 578 kilometres of national road had been improved, which matched the revised target after cancelled road packages but was below the 715 kilometres targeted at the start. The same report puts daily traffic on the project roads at 14,490 vehicles against 7,505 before the works, operating costs down 8 percent for a car, 18 percent for a bus and 14 percent for a heavy truck, and travel time for light vehicles down 21 percent. These are the lender's own figures; no independent check was found.

After:

> The loan paid to widen and strengthen national roads in western Sumatra. By the Bank's own count at closing in June 2021, 578 kilometres of national road had been improved, which matched the revised target after cancelled road packages but was below the 715 kilometres targeted at the start. The same report puts daily traffic on the project roads at 14,490 vehicles against 7,505 before the works and a target of 14,544, operating costs down 8 percent for a car, 18 percent for a bus and 14 percent for a heavy truck, and travel time for light vehicles down 21 percent. These are the lender's own figures; no independent check was found.
