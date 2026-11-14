# Round 21, batch A — Chinese urban and airport rows

Output: `/home/claude/r21/r26f_icij5_china_urban.json` — 6 cases, 1 drop, 0 extends, 0 already_on_map.
Cache: `/home/claude/r21/cache/` (see the last section).

All seven P-numbers came back clean from `dedupe_leads.py` (1,052 cases, 217 entity records):
P123729, P127867, P098915, P092631, P070519, P123133, P112838 — none on the map, no URL-only
hits. The P-number is in the lender role of every case written.

## Row by row

| ICIJ project | P-number | `r21_outcome` | Case id / reason |
|---|---|---|---|
| Xi'an Sustainable Urban Transport | P092631 | case | `xian-weiyang-xinjiamiao-resettlement` — 2,371 households (11,433 people) resettled against 527 households (4,770 people) at appraisal; payments to 39 + 37 households late, forcing a nine-month loan extension; 37 households still in transitional housing when the loan closed |
| China Wuhan Second Urban Transport | P112838 | case | `wuhan-nanhu-village-resettlement-delay` — Jiefang Avenue resettlement took over six years; Nanhu Village resettlement site delayed over three years and could not be connected to electricity, drinking water or gas; resettlement still unfinished 10 months after closing |
| Gansu Qingyang Urban Infrastructure Improvement | P123133 | case | `qingyang-xifeng-ring-road-relocation` — completion report Table 4 counts 226 households relocated and 2,149 affected; 640 households paid for house demolition; land acquisition and resettlement cost 229 per cent over the plan |
| Qinghai Xining Urban Transport | P127867 | case | `xining-wusixi-road-demolition` — demolition finished 31 Dec 2016, replacement housing about three years late, one of three resettlement complexes not started by Jan 2018 |
| Fuzhou Nantai Island Peri-Urban Development | P070519 | case | `nanjiangbin-road-slum-resettlement-fuzhou` — 3,000 households resettled off the road alignment (480 directly affected); social safeguards cut to Moderately Satisfactory for considerable delays and additional costs; access ramps left unbuilt at closing for want of resettlement |
| Jiangxi Shangrao Sanqingshan Airport | P123729 | case | `shangrao-sanqingshan-airport-land-take` — 2,913 mu (194 ha) of village land acquired and 7,708 m² of houses of 21 households demolished, both above plan; no shortfall of any kind recorded |
| GEF Sino-Singapore Tianjin Eco-City | P098915 | dropped | The money was a GEF grant of US$6,163,636 (TF-97018) financing green-building pilots **on existing public land** plus technical assistance. The 16 km² land acquisition from three villages, two state-owned enterprises and a military enterprise began in 2007, all land was acquired in 2008 and resettlement was complete by late 2008 or early 2009, carried out by the Tianjin Municipal Government **before Bank project identification**. Both the appraisal document and the completion report state that no additional land acquisition or resettlement occurred during implementation and that no social risks or negative impacts emerged. Fails the time test and the "harm on the thing the money financed" test. |

## What the works actually were (the sector test this round is for)

ICIJ's sector tags held for six of seven, but the works are more varied than "urban" suggests.

- **P123729, tagged `airport` — really an airport.** A new 4C feeder airfield: runway, taxiway,
  terminal building and apron, on farmland. Plus a 4.65 km access road built by the municipality
  outside the project — and, unlike the Burkina Faso road that cost round 20 a card, the Bank
  **did** bring that linked road inside the resettlement action plan for safeguards purposes.
- **P127867, tagged `urban` — new-build urban roads, not a retrofit.** Xicheng Avenue (3.64 km,
  three bridges, one underpass), Wusixi Road (3.43 km), No. 5 Road (1.02 km), bus lanes and an
  interchange, area traffic control; later Qiyi, Delingha, Bayi and Wuyi roads and a relocated
  long-distance passenger station.
- **P098915, tagged `urban` — neither urban works nor a loan.** A GEF grant for green-building
  pilots, an enabling framework and transport technical assistance inside an eco-city someone else
  had already cleared. The tag is the most wrong of the seven.
- **P092631, tagged `urban` — six components, only two of them roads.** Ring road and interchange
  works plus four roads in Huxian; two passenger terminals and a bus depot; an area traffic control
  system; an **air-quality monitoring centre and laboratory**; a **Han Dynasty road network inside
  the Weiyang Palace archaeological site** and tourist bicycle routes; institutional development.
  The resettlement that went wrong was at the cultural-heritage component, not the roads.
- **P070519, tagged `urban` — three big road works plus a bus depot.** Nanjiangbin Road (4.1 km
  riverside), the 11.6 km southern section of the Third Ring Road, the cable-stayed Kuiqi Bridge
  over the Min River, the Jinshan Bus Depot, a pilot bus priority lane, and a Regional Wetlands
  Protection Plan the Bank got in exchange for dropping a road through the wetlands island.
- **P123133, tagged `urban` — half roads, half wastewater.** Ring road sections (Anding, Qinghua
  middle and south, Beijing north, Guxiang Lu) **and the Dongqu wastewater treatment plant**, which
  is one of the six sub-projects in the resettlement table. A row this round's batch C would have
  called "water" sits inside an "urban" row.
- **P112838, tagged `urban` — roads and bus terminals.** The Jiefang Avenue Extension, the elevated
  and ground Shuidong section of the Second Ring Road, the Tianshunyuan and Sanjintan bus terminals.

**On the hypothesis:** six of seven productive. But the yield did not come from the sector. It came
from three document features: a completion report that prints an **outcome table** (Qingyang's
Table 4, Xi'an's resettlement paragraph), a **separate resettlement plan filed late in the project**
(Xining's January 2018 update, which is the only place the delay is recorded), or an **unfinished
resettlement at closing** (Wuhan, Fuzhou). The one drop failed on what the money bought, not on
sector. A round that sorted on "does the project have a post-2015 outcome document naming a
resettlement site" would predict better than sector does.

## Answers to the three specific warnings

1. **Xining did not repeat the Flood and Watershed pattern — but only just, and not in the
   completion report.** The completion report and the Evaluation Group's review *do* reprint the
   appraisal's figures with the appraisal's verb: both give "121 households (527 individuals)" and
   the review writes that the investments "involved displacing" them. On those two documents alone
   this row would be a drop, exactly as P101829 was. What saves it is a third document the earlier
   round did not have: the **updated Resettlement Action Plan of January 2018**, which gives real
   outcome figures from the external monitor (233,600 m² demolished, 724.88 mu acquired, all
   complete by 31 December 2016 — against 150,661 m² and 788.09 mu planned) and then records that
   the resettlement complexes were about three years behind, with Taobei started October 2017,
   Wangjiazhai November 2017 and Huangzhong County not started at all. **Lesson for the next round:
   when a completion report reprints the appraisal, check for a late-project RAP update before
   dropping the row.** Also: Xining's 760 households resettled in 2010-2012, with 520,487 m² of
   houses demolished, are real and counted in the appraisal, but they happened before the project
   was identified and the project did not finance land acquisition; they are named on the card and
   explicitly not counted as the project's doing.
2. **No Guangdong overlap.** None of the seven projects has works in Guangdong, and none of the
   six cases shares a site, an implementing agency or a resettlement site with
   `chebei-village-guangzhou-resettlement`. Nothing for batch C to reconcile from this batch.
3. **Tianjin Eco-City was GEF money, and it bought nothing where the harm was.** Grant TF-97018,
   US$6,163,636 (total project cost US$64.06 million), approved 22 July 2010, closed 30 June 2016.
   Pilot investments were all on existing public land; no land acquisition or resettlement occurred
   under the grant. Dropped. **And it produced the cleanest ICIJ-figure match of the batch:** ICIJ's
   2,157 is the exact sum of the "Total Project Affected Person (PAP)" column of Table A10-1 in the
   appraisal document — Wuqi Village 1,057, Dongfeng Village 600, Qingtuozi village 500 — a table
   describing a pre-project due-diligence review of land taken in 2007-2008. 1,057 + 600 + 500 =
   2,157.
4. **`contested` on all six, as expected.** Two searches spent looking for a non-Bank source: one
   in English on the Weiyang Palace / Han Chang'an relocation and the Bank road, one in Chinese on
   南湖村 / 黄陂 / 解放大道延长线 / 拆迁. Neither returned anything about these works. Stopped there
   per the brief. Every case rests on the Bank reporting on its own project.

## My two weakest entries

1. **`shangrao-sanqingshan-airport-land-take` is the weakest, and by a distance.** The only
   documented harm is the land take itself: 2,913 mu (194 ha) of village land acquired and 7,708 m²
   of houses of 21 households demolished, both above the appraisal plan. Everything else in the
   documents runs the other way — monitoring says affected people have better housing with better
   water, drainage and community services; the Evaluation Group says there were **no delays in the
   payment of appropriate compensation**; a consultant survey of 30 households in Zunqiao found
   incomes up 26 per cent; the Evaluation Group rates the whole project **Highly Satisfactory**. It
   is in on BRIEF21 rule 1 (housing actually demolished, with a household count) and on limb (b)'s
   "land taken", and on nothing else. If the lead wants a floor on recorded adverse outcome rather
   than on scale, this is the row to cut.
2. **`xining-wusixi-road-demolition` rests its whole finding on one document.** The three-year
   delay and the unstarted Huangzhong County complex appear **only** in the January 2018 RAP update,
   prepared by the borrower's own project office and its hired consultant and disclosed by the Bank.
   Its figures are attributed to an external monitoring report that is not in the Bank's archive.
   The completion report and the Evaluation Group's review are silent on the delay and favourable
   throughout. No document says how many households were waiting at any complex or for how long.
   `displaced` is deliberately absent: the only household figure, 121, is the appraisal's.

   Third, for completeness: **`nanjiangbin-road-slum-resettlement-fuzhou`** is strong on the count
   (3,000 households, 4,642 apartments) and weak on the loss. The move was at the community's
   request, out of housing with no kitchens or toilets, and ex-post interviews report high
   satisfaction — close to the Bogotá hazard-relocation pattern that round 19 dropped. It is in
   because 480 households stood in the Bank-financed road's path and were moved involuntarily, and
   because the Bank cut its own social safeguards rating to Moderately Satisfactory for
   "considerable delays and additional costs in resettlement". Both halves are on the card.

## Figures and ratings where two documents disagree

| Project | Item | Completion report | Other document |
|---|---|---|---|
| P092631 Xi'an | Risk to development outcome | **Moderate** | **Modest** (IEG review) — a label substitution of the kind BRIEF20 trap 3 names |
| P123729 Shangrao | Outcome rating | **Satisfactory** | **Highly Satisfactory** (IEG review) |
| P123729 Shangrao | Bank performance | **Satisfactory** | **Highly Satisfactory** (IEG review) |
| P070519 Fuzhou | Risk to development outcome | **Low** | **Moderate** (IEG review) |
| P070519 Fuzhou | Date of the completion report | **11 November 2013** (cover page) | **7 November 2013** (its own data sheet); the `wds` archive field gives 11 November |
| P127867 Xining | Date of the completion report | **22 February 2022** (cover page) | **22 February 2021** (`wds` archive `docdt` field) — the cover is a year later than the API |
| P127867 Xining | Land acquired | 788.09 mu planned (appraisal, reprinted) | **724.88 mu actually acquired** (RAP update, Jan 2018) |
| P127867 Xining | Structures demolished | 150,661 m² planned (appraisal, reprinted) | **233,600 m² actually demolished** (RAP update, Jan 2018) |
| P112838 Wuhan | Land required | 48.2 ha at appraisal | **31 ha** at completion |
| P123133 Qingyang | People in the 143 house-demolition families | **528** (appraisal, p. 26) | **529** (appraisal, p. 11) — the same document, two figures |

Ratings on which the two documents agree, each read out of the document that gave it: P127867
Satisfactory / Satisfactory / Substantial in both; P123133 Moderately Satisfactory / Satisfactory /
Modest in both; P092631 Moderately Satisfactory on outcome in both (the review on a split rating,
weighted 3.6).

## Routes that failed, and what the failure was

- **`pdftotext -layout` on the Xining Project Agreement (L8319-CN) returns 129 bytes** — only the
  "Public Disclosure Authorized" stamp layer. `pdfinfo` shows the file was made by "Image2PDF
  Command Line Software": it is a scanned image with no text layer. Not a host or route refusal;
  the file downloaded fine from `documents1.worldbank.org`. Consequence: **no claim about Xining's
  loan covenants is made on any card**, and BRIEF21's rule 2 warning about absence claims on this
  vintage is respected by writing nothing either way. The five other project agreements
  (L8256-CN, L7558-CN, L4812-CN, L8170-CN, L7864-CN) extracted cleanly and are quoted.
- **`wds?projectid=P098915` does not return the Tianjin completion report.** Its `docty` field is
  **empty**, exactly the failure BRIEF21 finding 1 describes. It was found by a `qterm` title
  search on "Sino-Singapore Tianjin Eco-City Implementation Completion", which returned it as
  document D27144327 with a date of 24 January 2017 and a `pdfurl` of
  `.../389021485801750546/pdf/ICR-ICR00002116-with-MAPS-003-01262017.pdf`. It is now cached as
  `P098915_ICR.pdf`. Note the URL says `01262017` and the cover page says **January 24, 2017**.
- **Nominatim returns nothing usable for Nanhu Village, Huangpi District, Wuhan.** The Latin query
  returns nothing; the Chinese query `南湖村 黄陂区` returns three hamlets whose `display_name` says
  黄陂区 but whose coordinates (30.68 N) are south of the Yangtze, nowhere near Huangpi (31.06 N),
  and whose postal code 420112 belongs to a different district. The Wuhan card therefore uses the
  **Huangpi District administrative point with `ap: true`** and says in `point` that the village
  could not be confirmed at a point. Someone with the Chinese cadastral layer should fix this.
- **The 16 external resettlement monitoring reports by Wuhan University's Center for Involuntary
  Resettlement Research (Jan 2011 – Jul 2018), the 10 monitoring reports behind Qingyang's Table 4,
  and the external monitoring report behind Xining's outcome figures are all cited by Bank
  documents and none is in the Bank's public archive.** Searched by project id and by `qterm`.
- **One "informed IEG" item found and excluded.** The Shangrao review states: "The Project Team
  provided a detailed table of land acquisition comparing planned and actual figures as the units
  were different in PAD and ICR." That table is in no document. Nothing from it is on the card, and
  the card says so in `displaced_note`. Grepped all six reviews for `informed IEG`, `the project
  team` and `the World Bank team stated`; this was the only hit that carried a figure.
- **Five of the six IEG ICR Reviews print no date anywhere on the page.** Only the Fuzhou review
  carries a `Date Posted` line (06/20/2014). For P123729, P092631, P123133, P112838 and P098915 the
  source date is the Bank's `wds` `docdt` field, unverified at document level, and each card's
  `confidence_note` says so. (The Xining review also prints no date; its 29 June 2022 is the
  archive field, consistent with the ICR's own February 2022 cover date.)

## Document cache

`/home/claude/r21/cache/` — 31 documents from this batch, each as paired `.pdf` and `.txt`
(`pdftotext -layout`), named `P<number>_<type>`. Other batches are writing to the same folder
concurrently; the files from this batch are:

- **P123729** (Shangrao airport): `_ICR`, `_ICRR`, `_PAD`, `_PA`
- **P127867** (Xining): `_ICR`, `_ICRR`, `_PAD`, `_PA` (image-only, 129-byte text), `_RAP2018`
  (the January 2018 updated Resettlement Action Plan — the key document for this row),
  `_RESTR2019` (restructuring paper, 26 September 2019)
- **P098915** (Tianjin Eco-City): `_ICR` (the one with the empty `docty`, found by title search),
  `_ICRR`, `_PAD`, `_RAP` (land acquisition review report, November 2009), `_RPF` (resettlement
  policy framework, 24 December 2009)
- **P092631** (Xi'an): `_ICR`, `_ICRR`, `_PAD`, `_PA`
- **P070519** (Fuzhou): `_ICR`, `_ICRR`, `_PAD`, `_PA`
- **P123133** (Qingyang): `_ICR`, `_ICRR`, `_PAD`, `_PA`
- **P112838** (Wuhan): `_ICR`, `_ICRR`, `_PAD`, `_PA`

Nothing in `/home/claude/r20/cache/` covered any of these seven projects, so nothing was reused;
it was checked first (the nearest neighbour there is P101829, round 20's dropped Xining Flood and
Watershed project, which is a different project in the same city).

Nothing was merged, `build.py` was not run, git was not touched.
