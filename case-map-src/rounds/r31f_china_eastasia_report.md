# Round 31, batch china_eastasia — writer's report

15 rows from ICIJ's confirmed-displacement table (China 8, Viet Nam 3, Indonesia 1, Laos 1,
Philippines 1, plus one sibling number). Documents were read from
`/home/claude/work/cache/<PID>/`; no Bank document was re-fetched.

**Outcome counts: 6 cases, 8 drops, 1 already on the map.**

## Row by row

| PID | ICIJ project | Outcome | Reason in one line |
|---|---|---|---|
| P123323 | Ningbo Municipal Solid Waste Minimization and Recycling | dropped | The only relocation count (167 households, 395 persons) exists solely as "The project team provided following information" in the evaluation review; the completion report gives 1,249 people *affected* and says compensation was completed in full. |
| P091949 | Gansu Cultural and Natural Heritage | **case** `lutusi-liancheng-heritage-resettlement` | Completion report's actual column: 14 households relocated, 870.71 m² demolished, 19.54 mu taken; water and electricity slow to reach the resettlement houses, site rejected by seven households. |
| P101988 | Jiangxi Shihutang Navigation and Hydropower | **case** `shihutang-dam-ganjiang-relocation` | Completion report: 141 households / 515 people relocated, 654.9 ha permanently acquired against a 615 ha estimate. |
| P067828 | Renewable Energy Scale-up (CRESP) | dropped | Completion report and field-based assessment report both record compensation fully paid, replacement houses completed, incomes restored or increased, no significant issues; no count relocated. |
| P096158 | Follow Up to CRESP Phase I | dropped | Same operation, same two outcome documents, same finding. |
| P111163 | Xinjiang Turfan Water Conservation | **case** `ertanggou-reservoir-tuyamar-village-inundation` | Completion report: a Uyghur herders' hamlet of 26 households and 103 people wholly inundated, houses demolished, moved 15 km; 4,774.36 m² of housing and 924 mu of land in the inventory table. |
| P098654 | Thermal Power Efficiency | dropped | ICIJ's 702 is a heat-pipeline resettlement plan's affected-population survey; all three outcome documents discuss worker redundancy only, and the assessment report says most workers did not need to relocate. |
| P090990 | Western Indonesia National Roads (WINRIP) | **case** `lubuk-alung-kuraitaji-road-works-death` | Completion report: a supervision site engineer killed on package 21A on 27 July 2019, which the report says adequate traffic management provisions would have prevented. |
| P090374 | VN-GEF-Coastal Cities | already on map | `quy-nhon-coastal-cities-sanitation-resettlement`; same joint 2015 completion report, nothing new. One numeric correction reported below. |
| P102398 | Road Sector Project (Laos) | dropped | Completion report: resettlement paid before works started, compensation and support provided to all affected households, the only grievances about traffic signs on NR6A; no count relocated. |
| P117470 | Laguna de Bay Institutional Strengthening — Additional Financing | **case** `rodriguez-ecotourism-site-397-families-relocated` | Parent project P070899's completion report: the Rodriguez local government "had to relocate and resettle 397 families of illegal settlers from their ecotourism sub-project site", with a few still waiting at closure because the Sitio Sapo site was held up over permits. |
| P095275 | Central North Region Health Support (Viet Nam) | dropped | Completion report and review: resettlement activities "fully implemented", 30 centres built with no complaints on compensation or resettlement. |
| P073763 | Viet Nam Water Supply Development | dropped | Delays in site clearance and compensation are recorded, and the consequence named in the same paragraph is "considerable adverse impact on the progress of civil works". No household counted, no payment said to be missing. |
| P090336 | GEF-Ningbo Water and Environment | dropped | The mudflat restoration never happened, so "those engaged in aquaculture were not displaced and their livelihoods were not affected by the project" and the resettlement plan was never carried out. |
| P106956 | Ningbo New Countryside Development | **case** `chunhu-fenghua-access-road-demolition` | Completion report's social safeguards table, actual column: 7,647.6 m² of housing demolished against 3,479 planned, 325.63 mu acquired against 265.06 planned. |

Dedupe: `dedupe_leads.py` run on all 16 numbers; only P090374 came back on the map. The five
other new cases were also checked by place and years against the 1,093 cases — no Gansu heritage,
Gan River, Turpan, West Sumatra roads, Rizal or Fenghua case matches them.

## (a) My own two weakest entries

**1. `lubuk-alung-kuraitaji-road-works-death` (WINRIP).** The whole case is one death, and whether
it belongs to the project turns on which half of a single sentence is read as the cause. The
completion report gives both in that one sentence: "The cause of the accident was a human error (a
car at speed of around 60 km/h hit him from behind when he was taking pictures at the center of the
carriageway) that could have been prevented if adequate traffic management provisions would had
been deployed." I set `killed: 1` because the works' missing traffic management is named as what
would have prevented it, the victim was the project's own supervision engineer, and it happened on
a live works site rather than a finished road — but a checker reading "human error" by a
third-party driver as the cause will cut it to 0, and the family's payment came through Indonesia's
work-accident insurance scheme, which `CHECK31` rightly says is not an admission of causation.
Both readings are set out on the card. The engineer is not named. Nothing else on the card is harm:
the report says every affected person was paid at replacement cost.

**2. `chunhu-fenghua-access-road-demolition` (Ningbo New Countryside).** No person or household is
counted anywhere. The case is floor area and land area in the actual column of one table —
7,647.6 m² demolished against 3,479 planned, 325.63 mu against 265.06 — in a project whose
completion report says no complaint was received over its whole life, that all property losses
were adequately compensated, and whose external monitor reports affected households' per capita
net income rising from about RMB 40,000 to RMB 58,600. It qualifies under limb (b) as housing
actually demolished and land actually taken, and nothing more. It also carries the figure conflict
in (c) below.

## (b) Did the pre-extracted briefs help or mislead

**They helped, on balance, and saved what would have been the whole search budget.** Having every
document on disk with its path made it possible to read six outcome documents end to end, grep for
the clause that cuts the other way, and check every quotation in its own paragraph. Three findings
on this batch came from reading past the candidate sentences and would not have survived a brief-only
read: the Ningbo solid waste relocation count being a staff statement, the Laos ICR-author
contradiction, and the Dominican Republic file sitting in a China cache.

**Where the briefs misled.**

- **The brief's single most dangerous item was the one it labelled correctly.** On P123323 the
  "count with a relocation verb" section — the only bucket that looks like a finding — held
  167 households / 395 persons, and the `STAFF STATEMENT` section held the same sentence. A writer
  taking the buckets at face value writes that card. The brief put the same text in two buckets
  without saying that the second cancels the first.
- **A wrong document in the cache.** `cache/P106956/ICR_2016-10-20_26901073.txt` is not this
  project's completion report. It is the Implementation Completion and Results Report for the
  **Dominican Republic Social Protection Investment Project**, Report No. ICR00003930, and its
  URL in `harvest_manifest.json` carries `P090010`. The brief drew a `PLAN VERB` candidate sentence
  from it (the "second SIUBEN's socio-economic study" line), presenting a Dominican Republic
  sentence as evidence about Ningbo. The correct file is `ICR_2016-10-20_26901074.txt`,
  Report No. ICR00003806. Worth sweeping the other 300-odd cache folders for the same fault.
- **An empty harvested file reported as a document.** `cache/P117470/RP_2012-12-18_17282165.txt`
  is 243 bytes: the "Public Disclosure Authorized" watermark layer and nothing else. It is the
  only document the brief lists for that row, and the brief presents the row as having one
  document. The row was workable only because the parent project's documents had been harvested
  under P070899, which that brief's candidate-parent list named but did not say were already on disk.

**Which candidate-sentence kinds were noise.**

- `replacement cost` — noise on 6 of 6 rows where it fired. Every hit was the policy recital in a
  resettlement framework or, on P123323, an economic-analysis line about the avoided replacement
  cost of landfill capacity. Not one hit was a finding about compensation paid below replacement cost.
- `arrests, police or force` — noise on 3 of 3. On P091949 it fired on a procurement list of
  "monitoring and security systems"; on P101988 and P111163 on compensation-procedure text and a
  bulldozer unit-cost calculation. No hit concerned force used against anyone.
- `death, with any cause given` — noise on 2 of 3. On P102398 it fired on road-safety campaign
  indicators and a plan's list of future hazards; on P090374 it fired on "there was no recorded
  fatality at construction sites", the opposite of a death. It was a true positive once, on P090990.
- `demolished housing` — the highest-volume bucket and almost entirely plan text. Of 8 hits on
  P123323 and 7 on P102398, every one was in a resettlement plan or an indigenous peoples plan in
  the future tense. The two true outcome figures on this batch, Gansu's Table A6-1 and Ningbo's
  Table 7.1, were reached by reading the annex, not from this bucket.
- `affected, NOT a relocation count` — correctly labelled and genuinely useful: on five rows it is
  the whole of what exists, and that is itself the drop.

**What the briefs should have surfaced and did not.**

1. **A bucket for the outcome document's own planned-versus-actual table.** The two strongest
   figures in this batch, Gansu's "Planned 17 / Actual 14" and Ningbo's "Planned 3,479 / Actual
   7,647.6", sit in annex tables and appear in no candidate-sentence bucket. The reprint check
   lists figures found in both a plan and an outcome document, which is the inverse: it surfaces
   figures to be suspicious of, never the figure that settles the row. A bucket keyed on
   "Planned", "Actual", "Actual Versus Planned" and "Comparison of Planned and Actual" would
   have put both in front of the reader.
2. **A cross-check that the harvested file is the named project's document.** One line comparing
   the report number or the project name on the cover page against the PID would have caught
   `26901073`.
3. **A flag on a zero-content harvest.** A file of a few hundred bytes should not be listed as a
   document without saying so.
4. **A note that a sibling or parent folder already holds documents.** P117470's brief listed
   P070899 as an unverified name match while its completion report and evaluation review were
   already sitting in `cache/P070899/`.
5. **The negative statement as its own bucket.** The sentences that decided three of the eight
   drops are of the form "were not displaced and their livelihoods were not affected", "most
   workers did not need to relocate", "no persons affected". These are findings, and strong ones.
   The `CAUTION — null sentence` bucket collected only plan-stage boilerplate, never an outcome
   document's negative finding.

## (c) Figures where two documents, or one document, disagree — left unreconciled

1. **Ningbo New Countryside, land permanently acquired.** The Bank's own body text (paragraph 54)
   and its Table 7.1 give **325.63 mu**, a 24 per cent rise over the 265.06 mu planned. The
   Summary of Borrower's ICR in Annex 5 of the **same document** gives **270.67 mu**, "5.61mu more
   than planned". Both agree on 7,647.62 m² of housing. Nothing in the document reconciles them.
   Both are on the card.
2. **Gansu, final resettlement cost.** The completion report's body text and Annex 6 text give
   **RMB 5.80 million**; the actual column of its own Table A6-1 gives **RMB 5.79 million**. One
   document, two figures. Both on the card.
3. **Turfan, which county the village was in.** Paragraph 143 of the completion report places
   Tuyamar village in "Jinsheng township of Turpan city"; paragraphs 144 to 147 of the same
   document have **Shanshan County** government commissioning and building the resettlement, and
   the 2009 resettlement plan is issued by the People's Government of Shanshan County and cites
   Shengjin Township's statistical yearbook. Not reconciled on the card.
4. **Turfan, households resettled.** The 2009 resettlement plan: "resettlers in the planning year
   of the project construction will reach **103 in 21 households**". The 2017 completion report:
   "**103 people in 26 households**", and "**29** spacious and tidy house yards were built". The
   person count is identical across plan and outcome, the household count is not, and no document
   explains it. Flagged on the card as a possible plan figure carried forward.
5. **WINRIP, total project cost.** The completion report's financing table gives
   **US$224,160,404**, as both the amount disbursed under IBRD-80430 and the total project cost.
   The Evaluation Group's review's data sheet gives the total project cost as
   **US$223,780,891.76**. On the card.
6. **Laos Road Sector, whether anyone was affected at all.** The evaluation review states "The ICR
   author advised there were no persons affected by the project." The completion report itself
   says "The RAP implementation has been completed with compensation and required support provided
   to all Project Affected Households (PAH)" and that "All resettlements on NR1B and NR6A were
   fully paid by GoL". Both sides are in the drop reason; the row is a drop either way.
7. **Laguna de Bay, amount disbursed.** The completion report's data sheet: disbursed
   **US$6.80 million**. Its Annex 1 financing table: IBRD actual **US$6.83 million**. On the card.
8. **Risk-to-development-outcome label substitutions, three of four reviews in this batch.**
   Gansu: report says **Moderate**, review's column says **Modest**. Turfan: report says
   **Moderate**, review says **Modest**. Shihutang: report says **Low or Negligible**, review says
   **Negligible to Low**. Laguna de Bay: report says **Substantial**, review says **Significant** —
   the exact pair `BRIEF20` names. Every rating on every card was read out of the document that
   gave it, and each is attributed by name.
9. **Genuine rating disagreements, not substitutions, on two rows.** WINRIP: quality of monitoring
   and evaluation, report **Substantial**, Evaluation Group **Modest**, reason given as
   shortcomings in M&E design. Ningbo New Countryside: outcome, report **Satisfactory**,
   Evaluation Group **Moderately Satisfactory**, reason given as relevance of design being
   Substantial rather than High. Both on the cards.

## (d) What could not be checked — naming the route, not the host

- **The Philippine government's own impact evaluation of LISCOP**, an outside-the-lender source
  that could have moved `rodriguez-ecotourism-site-397-families-relocated` from `contested` to
  `documented`. Two routes failed and the file was never read. Route 1: `curl -sL` to
  `nep.depdev.gov.ph/storage/document/1634053877_IES Final Report - LISCOP.pdf` — the agent proxy
  reported `ws_closed_mid_exchange`, the tunnel to the egress proxy closing before the exchange
  completed, on two attempts with a 90 and a 120 second timeout. Route 2: the fetch tool on the
  same URL — refused by the site's robots rule (`robots_disallowed`), nothing of the file
  retrieved. The host is not blocked; a search result from it is what pointed at the file. A
  browser-based route was not tried.
- **Indonesian press on the 27 July 2019 fatality.** One Indonesian-language search on the
  accident, the package and the road section returned nothing about it — the hits were unrelated
  2019 construction and traffic accidents elsewhere. So WINRIP rests on the lender's own documents.
- **Chinese-language sources for all four China cases.** Two searches, on 石虎塘航电枢纽 with the
  township and compensation terms, and on 二塘沟水库 with the county and herder terms, returned
  nothing about either project. Consistent with `BRIEF20`'s note that three rounds have found
  nothing outside the Bank for Chinese cases; I did not spend more than the two.
- **Kasiglahan Village reporting was found and deliberately not used.** Philippine outlets
  (Bulatlat, Davao Today, a UP Philippine Journal of Social Development paper) document flooding
  and conditions at Kasiglahan Village, which is where the completion report says most of the 397
  families went. None of them names these families or this project; the relocatees they describe
  came from Metro Manila. Citing them would be conflation, so the case stays `contested` on the
  Bank's documents alone.
- **No contractor is named for WINRIP package 21A.** The completion report names the design and
  supervision consultants only as "DSC" and names three firms (PT. Perent Jana Djaja, Yongma
  Engineering Co. Ltd., PT. Epadascon Permata) solely as the authors of the core team consultant's
  final report, not as the employer of the engineer who died. The `companies` array therefore
  carries the implementing agency only.

## One correction to an existing case, for the lead to make by hand

`quy-nhon-coastal-cities-sanitation-resettlement` carries **`displaced: 1247`**. That is the
completion report's count of affected households (189.4 ha acquired "with 1,247 affected HHs"); the
report's count of households actually resettled is **223**, "decreased by about 10 percent compared
with the original 245". `fields_add` cannot set a number, so this is reported rather than filed.
The case's own `displaced_label` and `displaced_note` already state both figures correctly.

## Where the cache is and what is in it

`/home/claude/work/cache/<PID>/`, one folder per project, plain UTF-8 `.txt` (with `.pdf` alongside
for a few agreement documents). The 16 folders this batch used hold 166 files: completion reports,
evaluation reviews, appraisal documents, resettlement plans, indigenous peoples plans, loan and
project agreements, and project performance assessment reports for CRESP and Thermal Power
Efficiency. `/home/claude/work/harvest_manifest.json` maps every file to its document id, its
`docdt`, its title and its `pdfurl`; the `pdfurl` values are on the refusing `documents.worldbank.org`
host and need the host rewritten to `documents1.worldbank.org` and `http` upgraded to `https`, which
is how every URL on the six cards was built. All 15 source URLs on the cards were checked and
return HTTP 200. Two cache defects are recorded in section (b): a Dominican Republic report filed
under P106956, and a zero-content file under P117470.
