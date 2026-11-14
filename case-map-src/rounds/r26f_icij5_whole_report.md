# Round 21 whole-picture text — writer's report

20 cases in, 20 paragraphs written, 0 blanks. `self_reported` is true on all 20: every
delivery figure comes from the World Bank's own completion report, from the Independent
Evaluation Group's review of that report, or from the appraisal document. The Evaluation
Group sits inside the Bank Group, so its reviews are not treated as independent checks and
each paragraph ends saying no independent check was found. **No web search or fetch was used.
Every document was read from `/home/claude/r21/cache/` with grep, by P-number.** Search
budget used: zero, as in rounds 19 and 20.

`sources_add` is empty for all 20: each card already carries the completion report, the
Evaluation Group review and the appraisal document in `sources`, and those are the only
documents the paragraphs rest on (plus, for three cases, a resettlement document already on
the card).

## What each paragraph rests on

| case | documents read | the delivery spine |
|---|---|---|
| `xian-weiyang-xinjiamiao-resettlement` | P092631 ICR, ICRR | 19-row results framework, Annex 2 outputs-by-component, para 15 component changes, §3.3 efficiency, Annex 1 costs |
| `wuhan-nanhu-village-resettlement-delay` | P112838 ICR, ICRR | Annex 1 framework and key outputs, Table 3 component changes, §§47–52 efficiency, Annex 4 para 4 |
| `qingyang-xifeng-ring-road-relocation` | P123133 ICR, ICRR | Annex 1 framework, Table 2 environmental targets, paras 9–11 restructurings, §C efficiency Table 3 |
| `xining-wusixi-road-demolition` | P127867 ICR, ICRR, RAP2018 | Annex 1 framework and key outputs, para 12 component changes, §§56–60 efficiency |
| `shangrao-sanqingshan-airport-land-take` | P123729 ICR, ICRR | Annex 1 framework and key outputs, Table 2 traffic statistics, Table 3 economic analysis, §§35–38, ICRR §5 |
| `corridor-x-dimitrovgrad-bypass-serbia` | P108005 ICR, ICRR | Annex 1 framework, Tables 5–9 (cost, time, traffic, EIRR, FIRR), ICRR §5 |
| `milot-rreshen-road-compensation-albania` | P078949 ICR, ICRR | Datasheet indicators, Annex 1 costs, Annex 2 outputs, Annex 3 Tables 3–4, §3.3 |
| `amman-development-corridor-land` | P081505 ICR, ICRR | Datasheet indicators, Annex 2 outputs, Annex 3 Tables 3.1 and 3.6, borrower's Annex 7 para 20, ICRR §5 |
| `lagos-brt-ikorodu-market-traders` | P112956 ICR, ICRR | Datasheet indicators, §§18–25 restructurings, Table 2 mobility framework, §§47, 57–59 |
| `baoro-bouar-road-house-damage-car` | P079736 ICR, ICRR | §§32–36 efficacy, Table 3 economic evaluation, §§41–44 efficiency, §(ii) implementation (CAR), ICRR §5 |
| `fenjiang-river-foshan-resettlement` | P081776 ICR, ICRR | Datasheet indicators 1–9, pp.16–21 delivery by city, §3.3 financial and economic analysis, p.5 scope changes |
| `qiantang-small-town-house-demolition` | P116656 ICR, ICRR | Datasheet indicators, §§31–32 restructuring, §§76–79 efficiency, Annex 3 Table 3.1 |
| `laibin-water-environment-displacement` | P126817 ICR, ICRR | Annex 1 framework and key outputs, §§20–27 changes and cancellation, §C efficiency, §72 procurement |
| `corumana-dam-resettlement-mozambique` | P107350 ICR, ICRR | Annex 1 framework, §§36–39 efficacy, §C efficiency Tables 4–5, ICRR efficiency |
| `ethiopia-sudan-interconnector-line-deaths` | P074011 ICR, ICRR | Datasheet indicators 1–6, §3.3 efficiency, Annex 2 paras 5–8, ICRR §5 |
| `gameleira-agrovila-ceara` | P006449 ICR, ICRR | Datasheet PDO and intermediate indicators, §§37–40 and 47 implementation, §78 and Annex 3 economic analysis |
| `patna-ganga-riverfront-resettlement` | P119085 ICR, ICRR | Annex 1 framework, §§59–61 efficiency, Annex 4 EFA table, §67, ICRR efficiency |
| `newmap-nigeria-erosion-displacement` | P124905 ICR, ICRR | Annex 1 framework, Table 5 interventions, §§45–50 and 64 efficacy, §C efficiency Table 6 |
| `nepal-raidp-land-donation` | P083923 ICR, ICRR | Datasheet indicators 1–11, §§62–65 efficiency, ICRR §5 |
| `ouagadougou-onea-works-before-compensation` | P106909 ICR, ICRR | §§31–33 and 46 efficacy, §§59–68 efficiency, §20 (self-installed connections), ICRR §5 and rate box |

## My own two weakest paragraphs

1. **`ethiopia-sudan-interconnector-line-deaths`.** The economic return is the shakiest thing
   I wrote anywhere. The completion report's Table 2 is badly mangled in the cached text: the
   row labels and the three scenario columns do not line up, so the only internally consistent
   figures are the ones in Annex 2 paragraph 7 (Ethiopia 22 per cent, Sudan 35, both together
   28, with NPVs of US$77.16m, US$100.94m and US$178.09m). The Evaluation Group prints a
   *different* set for the scenario at the actual US$0.05 price (Ethiopia 26, Sudan 17,
   combined 23), and its own rate box gives 28 per cent as the ICR estimate. I used the
   Annex 2 figures and the 28 per cent, and said they rest on an assumption that the price
   rises to US$0.07 from 2017 — which is what the report says of that scenario. A checker
   should re-read the PDF's Table 2, not the text dump, before trusting the 22 and the 35.
   Also: the appraisal's 48.6 per cent is printed without saying whose return it is, so I
   attributed it to the appraisal document and to no country.
2. **`gameleira-agrovila-ceara`.** The hardest case to keep straight, because the loan closed
   in December 2011 and the report then describes works as they stood in mid-December 2012,
   so almost every delivery sentence has two dates behind it. Gameleira at 75 per cent is a
   December 2012 observation, not a closing figure, and I said so, but the "six reservoirs plus
   two" count is a closing figure. The water figures (17.45 m³/s, 13.21 m³/s increase to
   Fortaleza, 300,000 and 2.6 million people out of rationing) are the state water company's
   own counts reprinted by the Bank, a second remove I flagged only by the standing
   lender's-figures sentence. The report's own 695 per cent and 156 per cent achievement
   percentages are arithmetic against targets that it says covered a different set of
   reservoirs, so I gave the raw figures and left its percentages out.

Runners-up, for the record: `fenjiang-river-foshan-resettlement`, where the Foshan
ammoniacal-nitrogen row beats a target cut from 1,095 to 150 while the report calls the whole
indicator partially achieved, and the report contradicts itself on the final project cost; and
`nepal-raidp-land-donation`, whose headline trip and travel-time gains are measured against a
2011 study substituted for the 2005 baseline.

## Figures where two documents, or two parts of one document, disagree

Both figures and both sources in each case.

1. **Albania construction cost, within one report (P078949 ICR).** Annex 3 Table 3 gives the
   26 km road at US$41.0 million at appraisal and US$38.7 million actual, and the text calls
   that 6 per cent lower. Annex 1's cost table gives the three construction lots at
   US$36.2 million at appraisal (12.30 + 10.70 + 13.20) and US$38.44 million actual
   (14.48 + 10.32 + 13.64), about 6 per cent **higher**. The ex-post 24.6 per cent return
   rests on the lower-cost reading. Both are in the paragraph.
2. **Jordan appraisal economic return (P081505).** ICR Annex 3 para 2 and borrower Annex 7
   para 19: 17.5 per cent. Evaluation Group review §5: "the ERR for the road component was
   calculated at 17.3%". Both in the paragraph.
3. **Jordan closing economic return, Bank against borrower (P081505 ICR).** Bank's Annex 3
   Table 3.6: 12.71 per cent, ENPV JD 11.76 million. Borrower's own Annex 7 para 20:
   13.07 per cent, ENPV JD 17.47 million. Both in the paragraph.
4. **Serbia 2018 traffic shortfall (P108005).** ICR Table 7: actual 2018 traffic was 46 per
   cent of the appraisal forecast **on the E-80 Dimitrovgrad bypass** and 70 per cent across
   the four sections (75, 74 and 71 per cent on the three E-75 sections). Evaluation Group
   review §5 states the lower return was "due to a lower than expected actual traffic volume
   (46 % of the appraisal estimate in 2018)" with no section named, which reads as project-wide.
   Both in the paragraph, with the discrepancy named.
5. **Central African Republic, Baoro–Bouar complete or not (P079736 ICR).** Table 3 of the
   economic evaluation labels the 56 km section "(achieved)". §(ii) under implementation says
   works "were not completed at the time of project closure after 34 months of work instead of
   the 20 months initially planned", and the safeguards section, discussing quarry and borrow-pit
   rehabilitation left undone, calls it "the abrupt halt to the construction of the
   Baoro-Bouar road". Both in the paragraph.
6. **Foshan final project cost (P081776 ICR).** Main text p.5: US$142.2 million, with
   US$70.92 million of loan disbursed. Economic analysis section: "The final project cost
   incurred was US$147.1 million." Both in the paragraph.
7. **Qingyang suspended-solids result (P123133 ICR).** Annex 1 and Table 2 both give 1,166
   tonnes a year against a revised target of 693 — exceeded. Paragraph 24 of the main text
   says "the target for SS was partially almost reached". I used the two tables, which agree
   with each other, and did not use paragraph 24.
8. **Qingyang appraisal sub-component returns (P123133 ICR).** Paragraph 33 lists appraisal
   EIRRs of 11.4, 11.1 and 24.7 per cent for sub-components 1.1 Urban Bypass, 1.2 Integrated
   Road Corridor and 1.3 Drainage and Sewage, in that order. Table 3 immediately below
   assigns 11.10 to Urban Bypass, 24.70 to Integrated Road Corridor and 11.40 to Existing
   Road Upgrading, with no drainage row. The labels do not match. I used only Table 3's rows
   and totals.
9. **NEWMAP land area (P124905 ICR).** Paragraph 48: area under sustainable landscape
   management "estimated to be 27,593 hectares". Annex 1 results framework: 30,627.96 hectares
   for that indicator — and the same 30,627.96 for a different indicator, land treated for
   erosion. Both in the paragraph.
10. **Nepal trail bridges (P083923 ICR).** Datasheet indicator 8: 745 bridges, of which 164
    built in full and 581 fabricated. Paragraph 64: "the construction of 750 bridges was
    supported". I used 745 and did not mention the 750.
11. **Lagos travel time (P112956 ICR).** Datasheet indicator 1: 87 minutes. Table 2 text:
    "reduction of travel time from Ikorodu to TBS by 28%, from 120 minutes to 86 minutes".
    I used 87, the indicator value.
12. **Albania traffic growth (P078949).** §3.3.2 and the ICRR both say actual 2011 traffic was
    32 per cent above the appraisal estimate; Annex 3 says 33 per cent. I used 32.
13. **CAR / Cameroon economic return, report against review (P079736).** The report gives
    7.1 per cent for Mbéré–Ngaoundéré and 7.5 per cent for the Mbé cliff section of
    Ngaoundéré–Garoua, against ex-ante 16.3 and 13.9/14.9 per cent. The Evaluation Group's
    rate box gives a single pair, 15.50 per cent at appraisal and 7.30 at ICR estimate,
    covering 100 and 84 per cent of cost. The paragraph uses the report's two section figures.

Nothing here is an appraisal-against-outcome pairing presented as a disagreement. Every
before-and-after pair in the 20 paragraphs names the quantity, the date and, where the review
prints it, the share of project cost the rate covers.

## Direction-of-measure checks made before calling anything a shortfall

- **Qingyang "Journey time saved for through traffic (freight)", minutes: baseline 28.40,
  target 18.20, actual 15.80.** The indicator's name says "saved" but its baseline is non-zero
  and its target is below its baseline, so it counts journey time, not minutes saved, and 15.80
  beats the target. The report prints no achievement comment on that row. I wrote it as the
  three values with no verdict attached, and called it neither a success nor a shortfall.
- **Wuhan travel-time rows (minutes), Xining travel time (minutes), Albania journey time
  (minutes), Lagos travel time (minutes), CAR transit days and transit-time variance, Serbia
  road user costs and crash rates, Qingyang and Wuhan and Xining casualty counts, Foshan unit
  operating cost:** all count downwards, so lower is better. Checked each against its own
  comment row before writing. The Wuhan Heping Avenue bus row (33 against 30) and the Foshan
  operating-cost rows are genuine shortfalls on that reading, and both are labelled as not
  achieved by the report itself.
- **Xi'an "Number of days for maintenance", 135 against a target of 163 from a baseline of
  93**, counts upwards and the report marks it "partially achieved (-17%)". Taken as a
  shortfall on the report's own label rather than on my reading of the unit.
- **NEWMAP "Net Greenhouse Emissions (tCO2-eq annually)", 149,554 against a target of 2,411**,
  is a net *reduction*: the restructuring table prints the target as -2,411 and the comment
  decomposes the actual into -198,908 from afforestation and -93,284 from solar against
  +142,618 from construction. Written as a reduction, with the decomposition.
- **Jordan cost per container, US$425 against a target of 300 from a baseline of 385**, counts
  downwards, so this is a measure that moved the wrong way, not merely short of target. Written
  as such, with the report's own oil-price remark attached.

## Units read as units, not counts

- Serbia: **36,161 person-months** of employment created under the contractors against a target
  of 20,000 person-months — not 36,161 jobs.
- Wuhan: **1,200 person-days** of training against 1,000; the indicator name ends
  "(Person*day)".
- Patna: **404 million litres a day** of wastewater kept out of the river; INR **crore** in the
  economic analysis table, against INR **billion** for the project net present value, both as
  printed.
- Qingyang, Xi'an: **mu** converted nowhere by me; the land figures stay in the units the card
  already uses.
- Laibin: the staff-training row is "328" against a target the report elsewhere states as
  "300-person training days", so I left that row out entirely rather than report 328 of
  anything.
- Shangrao: the ICR's "total number of tourists in Shangrao in 2017 reached 1.6 billion" and
  "RMB148 billion" of tourism revenue, and its tourism-jobs figures sourced to sohu.com and a
  provincial TV site, are all left out. The 1.6 billion is not a number of tourists on any
  reading and the conversion cannot be recovered from the text.
- Xining: the "percentage of jobs accessible" row prints 189,400 in its original-target column,
  a leftover from the pre-2019 indicator that counted jobs; that row is left out.
- Wuhan: sub-indicator 3.3 prints an actual of **500.00** minutes against a target of 5 for the
  Jiefang Avenue Extension, which is a data error in the report. Left out.

## Cancelled and unfinished works, by case

Every paragraph that uses a results-framework figure also carries the works that were dropped,
where the report records any:

Xi'an — Dongcheng Road, 26.7 km Ming City bicycle route, intersection channelling, accident
remedial measures, road-user education, strategic urban transport studies; bus priority lanes
13 to 1; heritage component cut 58 per cent. Wuhan — 15 appraisal activities, two PT corridors,
three road safety corridors, two terminals, one study. Qingyang — last km of the Western Ring
Road, vehicle equipment. Xining — Guihua 1 and 2 access roads, portable enforcement recorders,
three studies. Serbia — none recorded; the E-80 came in 0.7 km short of target by design.
Albania — 20 pieces of road safety equipment, six traffic counters, vehicles and training at
zero spend. Jordan — the customs depot and superstructure never built, the inland-port
component practically dropped, Section 1 at 65 per cent. Lagos — the Oshodi–Mile 2–Obalende
corridor, the air-quality monitoring subcomponent. CAR — Dabanga–Kousseri, Kousseri bypass and
Nguelendeng–Bongor–Éré–Kélo not achieved, Magada–Maroua dropped, Baoro–Bouar, the rest stops
and the Beloko platform unfinished, US$107.9m cancelled. Foshan — 1.1 km of sewers and 0.9 km
of embankment moved to local funding, 7 km less dredging, environmental management system and a
pumping station unfinished at closing. Qiantang — 4.3 km of Panji Road, Pan'an Yunshan sewers,
US$14.3m of loan cancelled. Laibin — Longdong river flood works, the low-impact drainage pilot,
an asset-management study, one sewerage contract, US$14m cancelled. Corumana — the saddle dam
fuse plug replaced by an auxiliary spillway not yet built, US$5m cancelled. Ethiopia–Sudan —
training left incomplete. Ceará — three dams and six pipelines unfinished at closing, the
Itapipoca contract cancelled. Patna — US$60.7m cancelled, the Tolly Nala contract retendered
into the successor project. NEWMAP — 11 sites left part-finished. Nepal — none recorded.
Ouagadougou — none recorded; connections moved from contractors to the utility.

## Causes

Where a shortfall has a cause, the cause is the document's own: Wuhan's Heping Avenue
(metro line 5 construction), Foshan's pollution rows (influent loads overestimated at
appraisal), Lagos's bus utilisation (lower demand, longer trips), Serbia's traffic (motorways
not fully open until 2019 and the neighbouring downturn), Xining's return (longer
implementation and pandemic traffic), Qingyang's revised pollution targets (the plant's
capacity miscalculated), Laibin's cuts (the municipality's land use plan change), CAR's
Baoro–Bouar (contractor performance, explosives imports, Covid-19, political turmoil),
Ethiopia–Sudan (force majeure in the report, customs, compensation arrears and Iran sanctions
in the review), Ceará (higher investment and operating costs). **Where no cause is given I say
so:** Albania's road-condition indicator, 4.5 against a target of 10, is marked "Partially
achieved" with no reason, and the paragraph states that the report gives none.

## Blanks

None. No case in this batch lacked a credible record of what the project delivered: all 20 are
World Bank operations with a completion report and an Evaluation Group review in the cache, and
every one of those reports carries a results framework with actuals. The nearest thing to a
blank is the Central African Republic, where **no ex-post economic return exists for the CAR
roads at all** — insecurity prevented traffic data collection, which the report states plainly
— so that paragraph says so and uses the April 2021 user survey the report offers instead,
labelled as a survey.

## Two things a checker should test first

- The Ethiopia–Sudan economic-return figures, against the PDF rather than the text dump
  (Table 2 is garbled in the cache).
- Whether the Wuhan, Xining, Laibin and Patna "revised target met / appraisal target missed"
  pairs are stated the right way round in each paragraph. Four of the 20 cases turn on a target
  that was cut before it was met, and that is the shape most likely to come out backwards.
