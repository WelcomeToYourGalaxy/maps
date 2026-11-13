# Round 20 — whole-picture text for the 26 new ICIJ cases

Written: 12 November 2026. Output: `r20/r26f_icij4_whole.json` (the form `merge_whole.py`
and `docs/WHOLE.md` expect: `{id: {whole, self_reported, searched, sources_add}}`) and
`r20/r26f_icij4_whole_strings.json` (the plain `{id: paragraph}` form the task asked for).
Both files hold the same 26 paragraphs; the merge script reads the first.

**26 of 26 written. No blanks.** `self_reported` is **true** on all 26: every delivery figure in
every paragraph comes from a World Bank completion report, the Independent Evaluation Group's
review of it, or an IEG Project Performance Assessment Report. No outside figure on what any of
these projects delivered was found in the cached documents, and nothing was fetched from the web.

**Web searches used: zero.** The whole job ran off `/home/claude/r20/cache/` with `grep` and the
`pdftotext -layout` text files, as round 19's handoff advised. `sources_add` is empty for all 26
because every document used is already in each case's `sources` list.

## What each paragraph rests on

Unless noted, "ICR" is the project's Implementation Completion and Results Report and "ICRR" the
IEG ICR Review, both read from the cached `.txt` on disk.

| Case | Documents read | Core of the paragraph |
|---|---|---|
| sichuan-small-towns-unfinished-resettlement | P110632 ICR, ICRR | 13 PDO indicators (12 met, Liujiang water plant 80% at closing, operational 30 May 2017); Annex 2 outputs; Annex 3 EIRR/NPV table for 8 sub-components; US$17m savings and 30–45% contract savings; ICRR's note that the ICR does not discuss quality effects |
| qufu-gupan-pond-demolition | P120234 ICR, ICRR | 40 of 41 sites (22/23 Qufu, 18/18 Zoucheng), mansion No. 10 cancelled over military-land title; beneficiaries 2,349,000 v 2,155,000; satisfaction 96% v 75% from project-run surveys; ICR NPV US$50m, EIRR 16% v PAD 27.50/12.89/8.16%; ICR Table 10 split rating |
| xiangyang-panggong-resettlement-housing-delay | P119071 ICR, ICRR | 20.04 km roads, 17 intersections, 100 stops, 40 buses, 364 staff; bus speed 19.2 km/h against a target cut 24→19; casualties 7 v 25 target from 37; satisfaction 95.1% (project survey, sample ≥200); accessibility indicator the ICR calls difficult to assess; EIRR 14.17 v 17.1%; ICR para 50 rates efficiency Modest |
| nanning-urban-environment-resettlement | P108627 ICR, ICRR | Jiangnan plant 240,000→480,000 m³/d, five plants 102,000 m³/d; 56.5 km sewers v 84.9 original, 5 of 8 pump stations, 10.363 km river v 14.245; coverage 89.19% v 75.5 revised/77.1 original; ICRR: restructuring 3 months before closing at 92% disbursed, revised targets 24–80% lower, original plant targets 30–78% achieved; FIRR >6%→>10% |
| liaoning-coastal-zone-resettlement | P126611 ICR, ICRR | 50.70 km street v 52 original/31.68 revised; 6 industries connected v 20/5; beneficiaries 350,340 v 340,000/213,200; all data from the Provincial PMO, with the ICR calling one passenger figure's reliability questionable; four EIRRs appraisal v completion, overall 14.2%; ICR Satisfactory/Substantial against ICRR Moderately Satisfactory/Modest |
| han-river-urban-environment-resettlement | P087224 ICR, ICRR | 85 km sewers, 3 plants 130,000 m³/d, 3,600 connections ≈25,000 people, 5 landfills 8.29m m³, 5 leachate plants 660 m³/d; sewer shortfalls at Hanchuan, Xiangyang, Shayang; Dawu solid waste 75% v 90/95; fee collection 90–96% v ~40; ICR section 3.4: no EIRR/FIRR, benefits not quantified, outcome Moderately Unsatisfactory |
| second-shandong-environment-resettlement | P077752 ICR, ICRR | 100,000 m³/d wastewater + 370 km sewers, 105,000 m³/d water + 432 km mains, 780 t/d landfill; connected 90.7% v 85; compliance 98.2% v 90; water-quality 129.5 of 148 km with the ICR calling the indicator problematic; reuse 18.2% v 21 with the ICR calling the data unverifiable; GEF 1,056 of 1,700 septic tanks, BOD 806.4 v 1,700 t/y; appraisal EIRRs >15% |
| shanghai-urban-environment-apl2-resettlement | P075732 ICR, ICRR | Western Trunk Sewer 377,000 m³/d = 94% of design v 80% target; Xujing 205,000 people; Bailonggang 178 t/d = 92%; Zhuyuan plant untested, 0%; solid waste component dropped, dumps left to the borrower; 10 of 11 revised (15 original) studies; ICRR: 29% cost rise 434.24→559.84, counterpart +53%, tariffs +86/+89% without covenant compliance |
| liuzhou-environment-management-resettlement | P081346 ICR, ICRR | 475,000 m³/d treated (capacity 500,000) from 60,000; 42 of 62 toilets, 20 cancelled after public objection; all 42 waste collection stations cancelled, 450 t/d transfer station built; COD −9,668 v −10,428 t/y, 2 of 11 polluters bankrupt, heavy metals unmeasured; satisfaction 78→84%, none at closing; appraisal ERR 9.5% over 81% of cost, not redone |
| zhanghu-railway-resettlement | P122319 ICR, ICRR | 286 km line; transit 411→86 min v 100; 21 of 25 train pairs; 4m annualised v 9m target, 6.4m full-year 2020; RMB31.2bn v 34.65bn feasibility, RMB83m/km v 93 and 85; ex-post EIRR 8.4% (text) / 8% (Annex 4 and ICRR) v 15% appraisal; NPV −RMB18.4bn v +6.0bn |
| luan-huaibei-urban-transport-resettlement | P111421 ICR, ICRR | Corridor ridership 634,838 v 571,316 but Huaibei 122,500 v 132,000 and 69.55m v 79.02m annual; travel time 188 v 185 min, Anqing 23 v 19 (baseline 20); Huaihai Road and Tuohe depot cancelled, 146 of 248 parking spaces; US$22.36m cancelled; EIRR 17.2→23.5% while NPV US$203.1m→143.7m |
| zhegan-line-railway-resettlement | P075602 ICR, ICRR | Annex 2 plan-v-actual (1,164 km track v 900; 2,826 of 3,045 track km electrified; 23 of 28 machines; 4 TA studies → none); transit times and traffic volumes; downtime 180→90 min; ERR 19% appraisal → 26% ex-post, with the ICRR table printing 23% at appraisal |
| nanchang-line-2-demolition | P132154 ICR, ICRR | 23.8 km, 21 stations, stage II a year late; 206,800 weekday trips v 200,000, 189,500 at full opening; travel-time average 23 v 22 with two of three segments short; car-access 40% v 15; satisfaction 91% v 70; cost ~15% below appraisal; EIRR 9.6→11.93%, NPV RMB8.00bn, BCR 1.6 v 1.2 |
| henan-towns-water-land-acquisition | P081348 ICR, ICRR | Water 2.17m v 4.20m original/2.36m revised; wastewater 697,000 v 811,000/563,000; utilities' net profit −RMB5.58m v +110.4m/+69.34m; 17 counties dropped (11 on ineligible retroactive procurement ≈ a third of the loan); EIRRs 21.9/12.5/31.1 v 25.8/25.0/33.6%; FIRRs 0–12.4 v 9.6–16.4%; ICR outcome Unsatisfactory |
| sichuan-wudu-canal-resettlement | P121414 ICR, ICRR | Xizi canal 108 km, branches 305.24 km, laterals 38.91 km, 22 O&M plans, all at targets set at the December 2017 restructuring (originals nil); command area 929,600 mu; 137.5m m³/y supply; on-farm works not Bank-financed, 11 of 52 laterals and 3 of 9 plants under way Sept 2020; ERR 11% v 13%, 6% in the delay case |
| yining-urban-roads-demolition | P126454 ICR, ICRR | 30.4 km improved, 33.54 km new after 8.5 km cut; 2 terminals and 2 fuel stations cancelled, 4 upgraded; maintenance study dropped; 33 signals, 88 cameras; 250 buses, 216 retired, fleet 329→497, 300 m access 33→60%; ridership 77→105.5m v 96m; zero deaths v 2.6 per 10,000 vehicles; EIRR 9% (roads only, 28% of cost) → 14.2% (88% of cost) |
| shaying-river-sanba-village-resettlement | P118647 ICR, ICRR | All framework targets met (206 structures, 206 aids, 4 bridges, 2 locks, 585 of 550 trainings); 500 dwt share 97–99% v 25–34%; cargo 13m v 3.6m and 11.9m v 3.0m t/y; EIRR 14.6→31.5%, 21.6% sensitivity; misprocurement on two contracts, June 2014 |
| tongliang-road-land-lease-compensation | P086446 ICR, ICRR | 77.6 km roads v 100 original/77.6 revised; Tongliang 3 roads/31.5 km v 5 roads/25.6 km; road access 341,000 v 306,000/230,000; 24,340 trainees v 13,000; 822 health facilities v 727; beneficiaries 6,672,860 v 8,582,570 (Yubei hospital unfinished); water component dropped, built without Bank money at 17,500 m³/d v 12,800; Table A4-1 EIRR/NPV falls; Shizhu training ERR 1.3%; clinic fees below costs |
| guangxi-poor-rural-land-acquisition | P071094 ICR, ICRR | Guangxi KPI table (poverty 80.8→31.2%, participation 86.9% v 80, infrastructure 92.2% v 80, assistance 78.6% and training 70.7% v 100%); NSB Module 1 income tables (RMB1,983→3,217, +38.7%, "similar to the provincial averages"), running water 23→47%; project ERR 30% at both appraisal and completion with component splits |
| rogun-stage1-resettlement | P089244 ICR, ICRR, IEG PPAR 2020 | 215,835 meters delivered v 215,000, 171,904 installed; 143,790 gas meters v 160,000 cut to 144,000; two Rogun studies August 2014 v December 2013; unaccounted-for electricity 17.5% v 14.5% target; collections 84.7% v 89; tariff 2.04 v 2.40 c/kWh; sales 2,236 v 1,940 GWh; PPAR's post-closure figures (15.3% in 2019, tariff 1.89 c, Barqi Tojik losses SM1.72→3.31bn, equity −2.75→−9.09bn, two of six turbines by Sept 2019) |
| kwabenya-landfill-expropriation | P082373 ICR, ICRR, IEG PPAR 2016, Inspection Panel investigation report | Landfill (US$9.5m base cost) dropped at the October 2010 MTR with ≈US$4m for private operators and the Tema septage road; 16.8 km drains at US$863,000/km v US$1m; latrines 189,463 v 230,000 and 49,420 v 70,000 pupils, US$25 a head v ~50% less at appraisal; 5 of 5 towns on waste collection; 14 communities/100,000 v 13/80,800; the PDO indicator inferred, not measured; PPAR field findings and the 47% health figure |
| santa-fe-road-19-expropriation | P099051 ICR, ICRR, Inspection Panel investigation report | Travel times −8 to −23% v ≥5% target; NR19 deaths −73.3% v province +13.6% (Provincial Road Safety Agency, created 2010, baseline from OCCOVI); ERR 19.3→12.4% with the ICRR's three stated reasons; appraisal NPV US$67.1m; counts taken after closing by the University of Cordoba under the PMU; safety pilots unanalysed |
| sutp-brts-corridor-displacement | P110371 ICR, ICRR | Pimpri-Chinchwad 48.3 km/4 corridors with per-corridor ridership at launch and later; Hubli-Dharwad 22.25 km in trial running, ≈55,000/day; mode shares 8.82% v 8 and 42.4% v 40 revised/50 original; Hubli-Dharwad mode-share indicator recorded 0/not measured; 16 practices v 6; CO₂ 312,000 v 128,000 t; EIRR 11.2% and NPV US$276m v appraisal 24%/US$185m and design-stage 29.5%/US$448m |
| dar-brt-kariakoo-clearance | P103633 ICR, ICRR | BRT works 100% by December 2015, interim service from 10 May 2016; travel time 62→28 min v 25; 140 buses v 248 revised/305 original; 162,000 v 360,000 passengers/day (baseline 250,000) plus ≈200,000 on daladalas; satisfaction Moderately Satisfactory v Satisfactory; Zanzibar runway August 2010; roadworks US$110m→177m; ex-post EIRR 1.8% at 125,809 riders v 14.5% appraisal and 12.4% restructuring, 8.4% at 250,000 and 18% at 524,000 |
| nutrip-road-compensation-arrears | P126321 ICR, ICRR | 20 km rehabilitated v 118 km target; US$61.87m of US$300m; travel time and vehicle operating costs unchanged because works unfinished; crashes −22% v −15% credited to NTSA enforcement; PPP indicator not achieved; ICR Table 4 cost rises including RAP US$1.3m→120m; Meru ex-post 30.7% v 17.2%, NPV US$91.19m v 11.6m; no return for James Gichuru–Rironi at 18% complete; both documents rate the outcome Unsatisfactory, efficacy Negligible |
| bukoba-airport-resettlement-arrears | P055120 ICR, ICRR | 909 km of road (268 + 641 km with 212 culverts and 2 bridges), ≈14% of the paved network; VOC 0.34→0.22 v 0.23 and 0.45→0.27 v 0.25; road condition 86% v 70% with the ICR calling the measurement inconsistent; Bukoba 33,138 v 34,000 passengers, 8.6→18.6 passengers per aircraft, new terminal, code 2C; Kigoma 29,781 v 40,000, Tabora 16,505 v 30,000 (baseline 22,912), Zanzibar 946,905 v 660,000; ERRs 18.3 v 15, 8.5 v 23, −9.6, 17.1 v 19/19.9, 16.3 v 15.2; ICR rates efficiency Modest |

## My two weakest paragraphs

1. **`guangxi-poor-rural-land-acquisition`.** The project covered 18 counties in three provinces and
   the case is about Guangxi, so the paragraph uses the Guangxi column throughout — but the two
   strongest statements in the ICR about what the money changed are project-wide (per capita incomes
   rising 12% a year against 9% in non-project villages) and the ICR itself says Guangxi's own income
   growth was "similar to the provincial averages". I kept the Guangxi figures and that qualifier and
   left the project-wide comparison out, which is the honest reading but makes the paragraph less
   definite than the others. A checker should also test my treatment of the National Statistics Bureau
   and ITAD surveys: they were carried out by bodies outside the project office but **paid for by the
   project and by DFID grants**, which is why `self_reported` is true. If the map's convention is that
   a national statistics office is an outside source, this flag should be false and the sentence
   rewritten. I read the ICR's footnote describing the three monitoring modules (ICR p.iii footnote 1
   and section 2.3) before deciding.
2. **`sichuan-wudu-canal-resettlement`.** Every target in the results framework was met exactly, and
   every one of them was set at the December 2017 restructuring against original targets of 0.00 — so
   "all targets met" carries almost no information, and the real content is that the water reaching
   farmland depends on on-farm works the Bank did not finance and that had barely started. I said
   both, but the paragraph has no indicator that went the other way because the framework contains
   none, and a checker should confirm that by reading Annex 1 rather than taking my word for it.
   The ICRR's own efficiency text gives the opportunity cost of capital as 5% in one sentence and 6%
   in the next; I used neither figure.

## Figures where two documents disagree

Both figures and both documents in each case. Nothing here is presented in the paragraphs as a
dispute unless the two numbers measure the same quantity at the same date.

1. **Zhanghu ex-post rate of return: 8.4% v 8%.** The ICR's main text, para 28, gives 8.4 per cent;
   the ICR's own Annex 4, para 30, gives 8 per cent, as does the ICRR (p.9). Same quantity, same
   evaluation. The paragraph names both and says which document carries which.
2. **Zhanghu appraisal rate of return without the extra benefits: 8.2% v 9%.** The ICR para 28 says
   that stripping freight and wider benefits out of the appraisal case would have given 8.2 per cent;
   the ICRR, quoting PAD para 42, says the appraisal analysis without the wider benefits "still showed
   an EIRR of 9 percent". The two strip out different things (the ICR removes freight as well), so I
   used neither in the paragraph.
3. **Zhe-Gan appraisal rate of return: 19% v 23%.** The ICR (Annex 3) and the ICRR's own text both
   say 19 per cent at appraisal; the ICRR's rate table prints 23 per cent at appraisal with 85 per cent
   coverage. Named in the paragraph.
4. **Han River industrial polluters, original target: 36 v 28.** The ICR's results framework prints an
   original target of 36 with a revised 28; the ICR's own text (para 51) says 28 polluters installed
   facilities "against the original target of 28", with a footnote that the revised targets of 28 and 50
   "were fully met". Same document, two places. Named in the paragraph.
5. **Second Shandong citizen satisfaction: 97% v 93%.** The results framework gives 97 per cent
   (99/94/98 for water, wastewater and solid waste); the ICR's text, section 3.2, says satisfaction
   "reached on average 93%". Both against the same 92 per cent target. Named in the paragraph.
6. **Liaoning disbursement split and project cost.** ICR Table 4: US$5.48m before and US$135.06m
   after restructuring; ICRR: US$5.86m and US$134.69m. ICRR also says the appraisal cost of
   US$339.5m "was revised to US$216.3 million" and counterpart commitment cut from US$189.5m to
   US$75.7m, where the card's own lender entry records total cost of US$193.14m actual and the
   borrower's actual share at US$52.59m. Not used in the paragraph.
7. **NUTRIP civil works cost increase.** ICR Table 4 gives Meru US$25.0m→34.4m and James
   Gichuru–Rironi US$54.08m→163.8m; the ICRR says the cost of civil works for those same two
   sections was 44 per cent higher, "from US$29.4 million at appraisal to US$42.2 million", which
   matches neither row nor their sum. The paragraph uses the ICR's table only.
8. **Yining completion rate of return: 14.2% v 14.3%.** ICR para 22 text says "about 14.2%"; its own
   Table 2 totals 14.3 per cent. The paragraph uses 14.2 per cent, the figure in the text.
9. **Rogun unaccounted-for electricity in Dushanbe.** The ICR reports 17.5 per cent at completion
   (31 December 2014) against a revised target of 14.5 per cent for that date and a 2004 baseline of
   13 per cent. The 2020 PPAR instead presents 14.5 per cent as the **2011** value and reports 15.3
   per cent for 2019. The two are not strictly in conflict — different dates — but the same number,
   14.5, appears as a 2014 target in one document and a 2011 actual in the other. The paragraph gives
   each with its date and its document.
10. **Rogun electricity sales target: 1,940 GWh v 2,569 GWh.** The ICR gives a target of 1,940 GWh
    for 31 December 2014 and 2,236 GWh achieved at 30 November 2014; the PPAR reports 2,495 GWh in
    2018 "close to the target of 2,569 gigawatt-hours". Different target vintages; the paragraph uses
    the ICR pair only.
11. **Dar es Salaam ridership: 162,000 v 125,809 a day.** These are different quantities — the first
    is all public transport passengers through Jangwani on the corridor (PDO indicator 3), the second
    the BRT's own average daily ridership used in the ex-post economic model (ICR para 48). Not a
    disagreement; the paragraph names what each counts, because the two are easy to confuse.
12. **Liuzhou and Han River IEG ratings tables** misreport the completion reports' own words, as the
    cards already record (Modest for Modest/Moderate, Negligible to Low for Low or Negligible, and in
    Liuzhou's case Moderately Satisfactory for the report's Satisfactory Bank performance). Every
    completion-report rating used in these paragraphs was read out of the completion report itself:
    Qufu ICR Table 10, Xiangyang ICR para 50, Liaoning ICR paras 63 and Table 4, Han River ICR
    section 3.4, Henan ICR section 3.4, NUTRIP ICR para 31, Bukoba ICR para 43.
13. **Liaoning outcome rating** is a substantive disagreement the card does not yet carry: the
    completion report of 28 March 2020 rates the outcome **Satisfactory** with efficiency Substantial;
    ICRR0022097 rates the outcome **Moderately Satisfactory** with efficiency Modest. The card's lender
    entry gives only the completion report's ratings. The paragraph states both. **This is worth
    adding to that case's `lenders[0].role` in a later pass.**

## Cases with no delivery figures

None. All 26 have documented delivery figures and all 26 have a paragraph. Every project in the
batch had at least an ICR and an ICRR in the cache, and for three (Rogun, Kwabenya, Santa Fe) there
were also IEG Project Performance Assessment Reports or Inspection Panel investigation reports.

## Notes for whoever checks this

- **Where a target was lowered, the paragraph gives both the original and the revised figure.** That
  pattern decides six of these cases (Nanning, Liaoning, Han River, Henan, Tongliang, Rogun) and in
  Nanning's case the Evaluation Group's own view is that measuring against the revised targets tells
  you little.
- **Where a results framework contains a row that went the other way, that row is in the paragraph.**
  The ones to test against the documents: Sichuan Small Towns indicator 13; Nanchang's two short
  travel-time segments; Luan–Huaibei's Huaibei rows and the Anqing travel time; Liaoning's industries
  connected; Guangxi's three 100-per-cent targets; Bukoba's Kigoma and Tabora passenger counts;
  SUTP's unmeasured Hubli-Dharwad mode share.
- **Nine of twelve ICRRs in one sub-batch carry no date on the page**, as the task noted. No paragraph
  dates an ICRR; where an IEG review's date matters (Liaoning, 26 June 2020) it is the date already
  carried in the card's lender entry, which came from the Bank's document-system record.
