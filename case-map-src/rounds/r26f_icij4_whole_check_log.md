# Check log — round 20 whole-picture text, 26 ICIJ cases

Checker's input: `r20/r26f_icij4_whole.json` and `r20/r26f_icij4_whole_report.md`.
Output: `r20/r26f_icij4_whole_checked.json` (same keys, same object shape).

**No web calls were used.** Every figure was re-read from the paired `.txt` files in
`/home/claude/r20/cache/`, the same documents the writer used, with the P-number taken from each
case's `lenders[0].role` in `base.html`. `CHECKW.md` asks for WebFetch; the sources here are
Bank documents already on disk, so they were read on disk, which is what the task directed.

**23 of 26 paragraphs corrected.** Unchanged: `zhegan-line-railway-resettlement`,
`yining-urban-roads-demolition` (text unchanged, `searched` line corrected),
`dar-brt-kariakoo-clearance`.

**`self_reported` stays `true` on all 26** and every paragraph still carries the
"no independent check was found" sentence. Reasoning for the two judgement calls is below.

## The three worst faults

1. **`nanchang-line-2-demolition` — an inverted indicator, and a shortfall that does not exist.**
   The travel-time indicator counts **minutes saved**, baseline 0 (ICR Annex 1: "Reduced travel
   time on public transport modes along Line 2 corridor", target 22, actual 23). Its three
   sub-indicators are 25 against a target of 25, **27 against 25** and **17 against 15** — the
   last two **exceeded** their targets. The paragraph said "Two of those three segments therefore
   fell short while the average met its mark", which reverses the direction of the measure. Every
   indicator in Nanchang's framework was met or exceeded; the paragraph now says so, says what the
   indicator counts, and drops the invented shortfall. This is the same class of fault as round
   19's manufactured disagreement.

2. **`liuzhou-environment-management-resettlement` — an economic rate of return that is a financial
   one, and that was recalculated.** The paragraph said "The economic rate of return was 9.5 per
   cent at appraisal, covering 81 per cent of project cost, and was not recalculated at closing".
   ICRR section 5 states: "No economic rate of return was calculated at appraisal or closure. The
   financial rate of return (FRR) of the wastewater component was calculated at appraisal and
   recalculated in the ICR. The ex-post FRR is estimated at 5.8%, which is lower than the rate of
   9.5% estimated at appraisal" (coverage 81 per cent at appraisal, 59 per cent at ICR). Rewritten:
   no ERR at either point, FRR 9.5 to 5.8 per cent, slower tariff rises, and the review's two
   stated reasons for Modest. Added the cost figures the review gives (US$199.6m actual, 3 per cent
   below the US$203.6m appraisal estimate, loan fully disbursed).

3. **`shaying-river-sanba-village-resettlement` — units read as counts.** "206 navigation
   structures and 206 navigation aids installed" is wrong: the two intermediate indicators are
   "Navigation infrastructure — Length of Class IV channel upgraded (km) 206" and "Navigation aids
   — Installation of modern comprehensive navigation aids system (km) 206". Both are kilometres.
   "585 training programmes run against a target of 550" is also wrong: the indicator is "Number of
   trainees who attend the training and study tours (Person-Month)". Corrected to 206 km of channel,
   aids along the same 206 km, and 585 person-months against 550.

## The shortfall test — three paragraphs failed it

The writer claimed every paragraph giving a results-framework figure also gives the rows in the
same table that went the other way. Each named framework was opened.

- **`guangxi-poor-rural-land-acquisition` — four 100-per-cent targets, not three, and a fifth row
  missed.** The Guangxi KPI table shows four rows short of 100-per-cent targets: assistance 78.6,
  training 70.7, applied technology training 76.8 and **poor households covered 91.7**, the last
  left out of the paragraph. The ICR's own comment names five (KPIs 6, 7, 10, 11 and 14) as
  100-per-cent targets "probably set too high at the time of appraisal", though the table prints a
  60-per-cent target for KPI 11, which was exceeded at 70.2. Also missing: **PDO indicator 4
  (environment), recorded "Relatively improved" against a target of "Significantly improved"**,
  with the ICR's comment that it "was not an agreed upon project objective and the values reported
  are difficult to understand". Both are now in the paragraph. Separately, 76.8 per cent was
  described as "basic education support"; the row is "% of households receiving applied technology
  training" (it sits under the Basic Education heading). Corrected.
- **`second-shandong-environment-resettlement` — three adverse rows in the same tables.** Municipal
  solid waste to landfill 351,660 t/y against a target of 450,775 (78 per cent, "due to an
  overestimation of waste generation at appraisal"); total water production 70.72 against 104.03
  million m3/y, missed on the original project because the Huantai water investments were deleted;
  non-revenue water 10 against a 20 per cent target, where the ICR says "the indicator is not
  relevant to project activities" and the achievement "cannot be verified". All three added. The
  GEF septic-tank row also needed the ICR's qualification that BOD reduction "was in line with
  original target if the number of septic tanks and sizes are corrected".
- **`nanning-urban-environment-resettlement` — the per-plant rows.** The paragraph gave only the
  ICRR's summary. The ICR's own framework has plants short of their *revised* targets: Shanglin
  service coverage 48 per cent of target and its pollution rows 30 to 66 per cent, Binyang coverage
  88 per cent, Mashan coverage 94 per cent and its TP and TN rows 53 and 44 per cent. Added.
- **`sutp-brts-corridor-displacement` — one more adverse row.** "Pimpri-Chinchwad — At least 2 BRT
  corridors operational": target 2, actual 1. Added. (Two resettlement-completion rows, 96.40 and
  97.50 per cent against 100, were left out: they are the harm the card already carries.)
- Tested and sound: Sichuan Small Towns indicator 13; Luan-Huaibei's Huaibei rows and the Anqing
  and Lu'an travel times (Anqing's annual ridership row, 48.91 against 49.79 million, was missing
  and has been added); Liaoning's industries connected; Bukoba's Kigoma and Tabora.
- **`sichuan-wudu-canal-resettlement`: the writer's claim that the framework holds no adverse row is
  correct.** All four PDO and six intermediate indicators were read: originals 0.00 throughout,
  targets set 28 December 2017, every one met and two exceeded (farmers 120.00 against 115.15,
  female study-tour participants 80 against 50).

## Other corrections, case by case

- **`sichuan-small-towns`**: "Puxing Town" is **Puxin Town** in the ICR. The US$17 million of
  savings was presented as a procurement result alone; ICR para 10 says it came from "Competitive
  bidding **and the dropping of the wastewater treatment facility in Xinjin and a sewage pump
  station in Pengshan**". Both cancellations (January 2016 restructuring) added, with the reuse of
  the savings in Hongya and Daying.
- **`xiangyang-panggong`**: added the July 2018 restructuring's cancellation of the eastern railway
  station bus terminal and the dropping of the Panggong branch roads — the second matters to this
  case directly. Ratings spot-check passed (see below).
- **`han-river`**: Shayang was listed as a sewer shortfall, "10 at Shayang against an original 45".
  Its target was cut to 10 and 10 km were built; the ICR's comment names only Hanchuan and
  Xiangyang as short. Rewritten so the cut target is visible and Shayang is not presented as a
  failure. (The framework shows all five cities' dumpsites closed; the paragraph's "four old dump
  sites" is the ICR's own Annex figure and was left.)
- **`shanghai-urban-environment-apl2`**: Bailonggang was listed under "Two things were not
  delivered". It treated 178 t/d **against a target of 163 t/d** — it exceeded its target; the 92
  per cent is of design capacity. Only Zhuyuan, at zero, was undelivered. Rewritten.
- **`zhanghu-railway`**: "reaching 25 by the end of 2020" is not what the ICR says — para 20 gives
  an average of 25 pairs a day "From September 2020 to February 2021". Corrected.
- **`henan-towns-water`**: the beneficiary counts cover the **20 towns** still in the project, not
  20 counties (ICR para 11: "4.202 million people in 37 towns... reduced to 2.360 million in 20
  towns"). The 17 dropped are counties in the ICR's own words and were left as such.
- **`sichuan-wudu-canal`**: "on-farm works... that the Bank did not finance" was too broad — the
  project financed the on-farm works in the three demonstration areas (38.91 km of laterals, "On-farm
  works have been fully completed under the project"). Narrowed to the scheme-wide works outside
  the demonstration areas, which the PAD puts on county governments and beneficiaries. The
  sensitivity case is a delay "beyond the next FYP (2021-2025)", not simply beyond 2025.
- **`tongliang`**: **seven** roads of 31.5 km in Tongliang, not three (ICR: "seven roads totaling
  31.5 km in Tongliang County to improve the connectivity of six townships/villages"); the plan was
  "five rural roads and seven urban roads", not five rural roads of 25.6 km.
- **`guangxi`**: the income sentence read "RMB1,983 in 2006 and RMB3,217 in 2010, a rise of 38.7 per
  cent". Those two table values differ by 62 per cent; 38.7 per cent is the report's own figure in
  para B.5 and the ICR does not say what it is adjusted for. Now attributed to the report rather
  than presented as the difference between the two. The Sichuan comparison was also misleading: the
  ICR says the annual rates "are similar to the provincial averages **in Guangxi and Sichuan**", so
  setting Guangxi's qualifier against Sichuan's 58.5 per cent implied a contrast the source denies.
  Yunnan's figure is "11.2% higher than the provincial average", not 11.2 points.
- **`rogun`**: the turbines were launched "by the end of 2019" in the PPAR, not by September 2019.
  The studies' target date is 31 December 2013 (now dated in full).
- **`kwabenya`**: the PPAR's sentence names **two** cancelled subcomponents — Kwabenya (US$9.5m)
  **and the Achimota septage facility (US$8m)**; the second was missing. The US$0.5m Tema road cost
  added. The 50-per-cent target belongs to a separate intermediate indicator (people near the new
  drains reporting less flooding); the objective indicator's own target is 15 per cent, which the
  paragraph did not give. Both fixed. The October 2010 mid-term review attribution was dropped in
  favour of the ICR's own reason, strong public opposition to the site.
- **`santa-fe`**: the ICR's consolidated ex-post rate is **12.35 per cent** across the five
  segments; 12.4 per cent is segment 1, and is what the ICRR's table prints as the ICR estimate.
  Both now given. Added the completion net present value — AR$8.82 million, about US$2.93 million,
  against US$67.1 million at appraisal — and the two segments that returned 11.8 and 10.8 per cent
  with negative net present values, which the paragraph omitted while giving the appraisal NPV.
- **`sutp`**: "the Hubli-Dharwad mode share indicator is recorded as 0 and not yet measured" is
  wrong twice. ICR Table 4: baseline **30 per cent**, revised target 33, actual **"n.a."**. Corrected.
- **`nutrip`**: added the 2016 figure (crashes down 30 per cent) beside 2017's 22 per cent, both
  against the 15 per cent target.
- **`bukoba`**: added the roads component's own small shortfall, 268.4 km against a 270 km target,
  and Bukoba airport's baseline of 26,628 passengers.
- **`liaoning`**: the two withdrawing parties are the city of Suizhong and the **Longcheng district
  of Chaoyang** (ICRR), not Chaoyang; added the cost revision from US$339.5m to US$216.3m that the
  ICRR ties to the withdrawals. "the completion report states that all of these figures... come
  from the Provincial Project Management Office" was softened to the indicator data, which is what
  the framework comments say row by row.
- **`qufu`**: the 96 per cent satisfaction figure was sourced to "satisfaction surveys run at the
  Confucius and Mencius complexes"; the ICR says an end-of-project tourist survey. Corrected.
- **`yining`**: text unaffected, but the `searched` line claimed "Annex 1 results framework". **The
  cached Yining ICR stops at page 20 of 38 and contains no Annex 1** (re-extracted from the PDF to
  confirm). Every figure in the paragraph is in the main text (paras 15 to 22 and Table 2), so
  nothing had to be removed; the `searched` line now says the annex was not available.

## `self_reported` — the two judgement calls, both resolved as `true`

- **Guangxi.** The ICR calls the monitoring system "external" and "independent", but footnote 1 and
  the Annex head say it is "the external monitoring system **funding by the project and with the
  assistance of DFID grants**", and Component 6 paid for "the design and operation of the
  independent impact assessment system". The National Statistics Bureau and ITAD did the surveys,
  but the project commissioned and paid for them. Under the rule given — a figure commissioned under
  the project is the lender's — `self_reported` is **true**. The paragraph says who ran the surveys
  and who paid, so the reader can see the shape of it.
- **Santa Fe.** "The University of Cordoba, under the supervision of the PMU, was in charge of
  collecting the data" (ICR para 35), and the counts were taken after closing at the PMU's
  direction. Commissioned under the project: **true**.
- The IEG reviews and Project Performance Assessment Reports used in Rogun, Kwabenya and Santa Fe
  sit inside the World Bank Group, so they do not make any of these paragraphs independently
  checked. No non-Bank figure on what any of these 26 projects delivered appears in the cache.

## The reported contradictions — all four real, and the non-conflict correctly presented

1. **Zhanghu 8.4 v 8 per cent.** Real. ICR para 28 (main text): "The ex-post Economic Internal Rate
   of Return (EIRR) is 8.4 percent." ICR Annex 4 para 30: "an EIRR of 8%". ICRR: "The ex-post
   analysis showed an EIRR of 8 percent". Same quantity, same evaluation. Correctly attributed.
2. **Zhe-Gan 19 v 23 per cent at appraisal.** Real. ICR section 3.3 and Annex 3: 26 per cent
   ex-post "compared to the economic return of 19 percent reported in the PAD"; ICRR text repeats
   19 per cent, its own rate table prints "Appraisal ... 23% ... 85%". Correctly attributed.
3. **Han River 36 v 28 polluters.** Real, and inside one document. Framework indicator 4: original
   target 36, revised 28, actual 28. ICR text: 28 installed "against the original target of 28".
   Correctly attributed.
4. **Second Shandong 97 v 93 per cent satisfaction.** Real, and inside one document. Framework
   indicator 1: 97 per cent against a 92 per cent target, with 99/94/98 for the three services in
   the comment; ICR section 3.2: satisfaction "reached on average 93%". Correctly attributed.
5. **Dar es Salaam 162,000 v 125,809 — not a disagreement, and the paragraph says so correctly.**
   162,000 is intermediate indicator 3, "Average number of public transport passengers per day
   through the Morogoro corridor at Jangwani" (baseline 250,000, target 360,000). 125,809 is the
   BRT's own average daily ridership in the ex-post economic model (ICR para 48 and Annex 3 table
   3.2, against 406,000 at appraisal and 524,000 at reassessment). Two different quantities, named
   as such. No manufactured disagreement anywhere in this batch.

## Completion-report ratings — all seven spot-checks passed

Each was read out of the completion report itself, not the review's column:

| Case | Where | What the completion report says |
| --- | --- | --- |
| Qufu | ICR Table 10 | Moderately Unsatisfactory before, Highly Satisfactory after, overall Satisfactory; efficiency Substantial |
| Xiangyang | ICR para 50 | "the efficiency of the project is rated as Modest" (ICRR: Substantial) |
| Liaoning | ICR para 63 and Table 4 | relevance, efficacy and efficiency substantial, outcome Satisfactory; split MU/S by disbursement |
| Han River | ICR 3.4 | "Rating: Moderately Unsatisfactory" |
| Henan | ICR 3.4 | "Rating: Unsatisfactory" (and DO rated Unsatisfactory in every ISR from 29 June 2010) |
| NUTRIP | ICR para 31 | relevance High, efficacy Negligible, efficiency Modest, outcome Unsatisfactory |
| Bukoba | ICR para 43 | "The Efficiency Rating is Modest" (outcome Moderately Satisfactory, para 44) |

## Correction to case data, not whole text — `liaoning-coastal-zone-resettlement`

Both ratings verified in both documents:
- Completion report of 28 March 2020, para 63 and Table 4: relevance substantial, efficacy
  substantial, **efficiency Substantial**, **overall outcome Satisfactory**.
- ICRR0022097, section 5 "Efficiency Rating: **Modest**" and section 11 ratings table "Outcome —
  ICR Satisfactory — IEG **Moderately Satisfactory**", with IEG's stated reason: "There were
  moderate shortcomings in the project's intended progress towards its' outcomes." Its efficacy
  table gives Modest original / Substantial revised and outcome MU/MS.

`lenders[0].role` currently gives only the completion report's ratings while citing the review
without its verdict. The sentence to add to that field, after the existing ratings sentence:

> ICRR0022097, the Independent Evaluation Group's review of that report, disagreed: it rated the
> outcome Moderately Satisfactory and efficiency Modest, citing four years of implementation in
> which only a third of the loan was disbursed for want of counterpart financing and the withdrawal
> of Suizhong and the Longcheng district of Chaoyang, which cut the estimated project cost from
> US$339.5 million to US$216.3 million.

This is case data; it has not been written to any file.

## Figures where two documents disagree

Beyond the four above:

1. **Nanning river course cleaned: 10.366 v 10.363 km.** ICR results framework indicator 5 prints
   10.366 (target and actual); the ICRR's output list prints "10.363 km (original target was 14.245
   km)". The paragraph had the ICRR's figure; it now uses the completion report's 10.366.
2. **Santa Fe ex-post rate: 12.35 v 12.4 per cent.** ICR Annex 3 consolidated 12.35 per cent over
   five segments; ICRR rate table "ICR estimate 12.4%". Both now in the paragraph.
3. **Henan appraisal financial rate of return, upper bound: 16.4 v 17.8 per cent.** ICR para 49:
   "mostly above 10%, ranging between 9.6% and 16.4%"; ICR Annex 3 para 7: "ranging from
   9.6%-17.8%". Same document, two places; the paragraph uses the main text's 16.4, as the writer
   did. Not flagged in the writer's report.
4. **Tongliang revised road-access target: 230,000 v 227,000.** ICR para at section 1.7: "reduced
   from 306,000 to 227,000"; ICR efficacy section: "the revised target of 230,000". Same document.
   The paragraph uses 230,000. Not flagged in the writer's report.
5. **Yining completion rate: 14.2 v 14.3 per cent** (ICR para 22 text v its Table 2) — as the
   writer reported; the text figure is used.
6. **Henan efficiency rating inside the ICR:** section 3.3 heading "Rating: Moderately
   satisfactory" against its own para 48, "Efficiency is rated satisfactory". Not used in the
   paragraph.
7. Rogun's 14.5 per cent (a 2014 target in the ICR, a 2011 actual in the PPAR) and its two
   electricity-sales target vintages (1,940 GWh for 2014, 2,569 GWh in the PPAR), NUTRIP's ICRR
   civil-works figure (US$29.4m to US$42.2m, matching neither ICR row), and Liaoning's two
   disbursement splits (ICR US$5.48m/US$135.06m; ICRR US$5.86m/US$134.69m) were all reported by the
   writer and are all real; none is used in the paragraphs, which is right.

## Faults appearing in more than one paragraph

- **A target that was lowered, or a measure whose direction was not checked, presented as a
  shortfall.** Nanchang (minutes saved read as minutes taken), Han River (Shayang), Shanghai
  (Bailonggang), Luan-Huaibei (the safety ceiling of 261 read as an ordinary target). Four cards.
- **Adverse rows left out of a table the paragraph otherwise quotes.** Guangxi, Second Shandong,
  Nanning, SUTP, Luan-Huaibei, Bukoba. Six cards.
- **Cancelled or dropped works omitted.** Sichuan Small Towns (Xinjin plant, Pengshan pump
  station), Xiangyang (eastern station bus terminal, Panggong branch roads), Kwabenya (Achimota
  septage facility). Three cards, and in each case the cancellation is in the same paragraph of the
  source as a figure the writer did use.
- **A figure's unit or kind misread:** Shaying (km read as counts, person-months read as
  programmes), Liuzhou (financial rate read as economic), Tongliang (seven roads read as three),
  SUTP (a 30 per cent baseline read as 0).

## Absence claims

The writer reports no case lacking delivery figures and no blanks. That holds: all 26 have real
delivered quantities — plant capacity, kilometres, passenger counts, meters installed — from a
completion report. The thinnest were checked against the "inputs and plans dressed as outputs"
test:

- **Sichuan Wudu** is the one where the test bites, and the writer was right to flag it: the only
  delivered things are canals, and the irrigation benefit depends on works that had barely begun.
  The corrected paragraph keeps the delivered lengths and says plainly that the 1.2 million farmers
  are a count of people who "would obtain access to water once the on-farm works are completed" —
  the ICR's own wording.
- **Rogun** delivers meters and two studies; the paragraph says so and does not credit the project
  with anything about the dam. The 215,835 delivered against 171,904 installed distinction is kept,
  which is the input-versus-output line in this case.
- **NUTRIP** delivers 20 km against 118 and US$61.87m of US$300m; nothing is dressed up.
- **Kwabenya**'s objective indicator is inferred rather than measured, and the paragraph now says
  what the target was as well.
- **SUTP** carries one genuinely unmeasured outcome (Hubli-Dharwad mode share) and one forecast
  presented as a forecast (carbon dioxide savings "forecast... over ten years"), correctly labelled.

## Voice

Scanned all 26 for first person, "this card", and any record of searching. Nothing found; the only
hits were "US$". No change needed on this head.

## What could not be checked, and why

- **The Yining results framework.** The cached `P126454_ICR.pdf`/`.txt` stops before Annex 1, so the
  indicator table, its baselines and its revised targets could not be read. The paragraph's figures
  all appear in the main text, so none rests on the missing annex, but no shortfall test could be
  run on that framework.
- **Dates on the IEG reviews.** Nine of the cached ICRR texts print no date, as the task noted. No
  paragraph dates an ICRR except Liaoning's 26 June 2020, which comes from the card's own lender
  entry rather than from the document; that date is not verifiable in the cache.
- **Nothing outside the cache was opened**, so no outside check on any of these projects was looked
  for beyond confirming that the cached documents contain none. If an independent evaluation of any
  of these 26 exists in the press or the literature, this check would not have found it, and
  `self_reported: true` rests on the cache alone.
- **Other card data was not reviewed** beyond the `lenders[0].role` item above and the P-numbers,
  which match the writer's basis table for all 26 cases (Rogun, Dar es Salaam and Bukoba each cite a
  second P-number in the same role field; the delivery figures used come from the first).
