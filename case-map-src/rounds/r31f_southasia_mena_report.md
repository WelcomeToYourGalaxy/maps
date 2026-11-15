# Round 31, batch southasia_mena — report

15 rows from ICIJ's confirmed-displacement table, South Asia and the Middle East and North
Africa. Every row was read. Nothing was screened out on a sentence.

Output: `/home/claude/work/out/southasia_mena.json` — 16 records keyed by case id: **10 cases,
6 drops, 0 extends, 0 already-on-map.** Two of the cases come from one row (P144335), which
has two harms in two places more than 100 km apart.

Dedupe: `dedupe_leads.py` run on all 15 P-numbers, then on the two parent numbers found during
the work (P010556, P050529). All 17 came back not on the map, and the place-and-years check
found no case carrying any of these projects under a name without a number.

## Row by row

| Row | Project | Outcome | Reason in one line |
|---|---|---|---|
| P086414 | India, Power System Development III | **dropped** | No physical displacement; the one substation with a plan sat on state industrial-corporation land, no land compensation was due to anyone, plan completed March 2008 |
| P113416 | Egypt, Wind Power Development | **dropped** | Desert route; tower-footing land bought willing-seller/willing-buyer, crops paid at market rates, no significant disputes |
| P099040 | Pakistan, Highways Rehabilitation (1st Additional Financing) | **case** `pakistan-earthquake-roads-compensation-arrears` | 1,007 kanals taken for the earthquake roads, 72% of compensation paid, Rs 31m sitting in revenue-department escrow at close |
| P107847 | Sri Lanka, Provincial Roads | **dropped** | Land by voluntary donation, no acquisition, harm is uncounted construction damage handled by the grievance mechanism |
| P144335 | Nepal-India Regional Trade and Transport | **case** `narayanghat-mugling-road-structures` | 131 private structures of 103 households hit by the road upgrade and by landslides, above the appraisal estimate of 80 and 74 |
| P144335 | same project, second place | **case** `chobhar-dry-port-arrests-kathmandu` | 52 or at least 54 arrests at the January 2019 groundbreaking, unsettled land claims, works stopped Aug 2018–Jan 2019, disbursements withheld to Feb 2020 |
| P116197 | Lebanon, Cultural Heritage AF | **case** `tripoli-tyre-heritage-market-relocation` | 38 + 33 households physically relocated from Khan el Askar, 280 vendors moved in Tripoli; the Bank's own field report found the Tyre market failing |
| P094513 | India, Emergency Tsunami Reconstruction | **case** `nagapattinam-canal-demolition-tsunami-rebuild` | Local authorities demolished structures on the North Buckingham canal without offering compensation; 5 of 6 families paid at close |
| P093988 | Bangladesh, Dhaka Water Supply and Sanitation | **case** `dhaka-khal-rehabilitation-eviction` | A footnote records an eviction of an unknown number of people on one canal; seven canals dropped over resettlement |
| P090157 | Bhutan, Urban Development II | **case** `thimphu-land-pooling-compensation-arrears` | Structures, fruit trees, businesses and rental access lost to land pooling; three owners never traced, money held by the Thromde |
| P131550 | Iraq, Transport Corridors | **case** `iraq-expressway-worker-deaths-vendor-relocation` | Three worker deaths with causes, called completely avoidable; 72 shop owners resettled; part of the loan suspended over the vendors' resettlement plan |
| P081823 | Jordan, Cultural Heritage, Tourism and Urban Development | **case** `jordan-heritage-cities-house-shop-demolition` | Actual-column table: 2,905 m² of housing and 1,750 m² of shops demolished, 46 households affected, 12,408 m² taken |
| P128938 | Kiribati, Pacific Aviation Investment | **dropped** | One dwelling obstructing a survey and a pre-existing terminal land claim, both recorded only as "resolved"; no count, no arrears |
| P082510 | India, Karnataka Urban Water Sector Improvement | **dropped** | 8.41 ha affecting 215 families — land area plus an "affected" count; plans satisfactorily implemented, no complaints. ICIJ's 215 is this figure |
| P112893 | Nepal, Kabeli Transmission | **case** `kabeli-transmission-line-compensation-arrears` | 55% of compensation paid overall: 188/228 tower pads, 41/82 structures, 673/1,339 easement; R&R to residential owners and non-titleholders unpaid |
| P105404 | Palestine, Southern West Bank Solid Waste Management | **dropped** | All former Yatta waste pickers given jobs or training, 100% of affected households integrated against an 80% target |

Six drops of fifteen rows. That is lower than BRIEF31 warned to expect, and it is because nine
of these rows turn on limb (b), not on a count: unpaid or uncollected compensation on five of
them, demolition without compensation on one, worker deaths on one, an uncounted eviction on
one. Only three cases carry a `displaced` number at all (71 households in Tripoli, 6 families
in Nagapattinam, 72 shop owners in Iraq). The forward rule's second limb is doing nearly all
the work, exactly as BRIEF31 predicted.

The recurring regional harm the task names is the dominant shape in this batch: **money paid
into a deposit or escrow account that the owner never collects.** It appears on four separate
cases, in four countries, with four different causes — Pakistan (owners died in the
earthquake, owners untraceable, court disputes, shamlat joint owners whose shares fall under
US$100 and who will not open a bank account), Nepal/Kabeli (no district land-survey record of
the owner, sums too small to be worth collecting, absentees), Bhutan (three owners not
trackable despite repeated efforts) and the Jhelum Valley case within Pakistan (state funds
spent on other things). In none of the four does a Bank document treat the uncollected money
as a loss; all four call it available for payment.

## (a) My two weakest entries

**1. `dhaka-khal-rehabilitation-eviction` (P093988) — weakest.** The entire harm is one
footnote, number 23, of the completion report: "In one of the khals eviction took place of an
unknown number of people." No count, no canal named, no date, no indication of what became of
the people. The Independent Evaluation Group's review of the same report does not mention it.
The report's own main text says there are no outstanding environmental or social safeguards
issues and that the 221 and 216 affected households were adequately compensated. The point
coordinate is Khilgaon, which is where the *other* canal incident happened (a partial building
demolition, recorded as resolved), not necessarily the eviction canal — the eviction canal is
unidentifiable. If the checker cuts one entry from this batch it should probably be this one;
it is kept because the withdrawn screen was built to kill exactly this shape and because an
eviction recorded in an outcome document is an eviction.

**2. `thimphu-land-pooling-compensation-arrears` (P090157).** The harm is a list of kinds of
loss with no number against any of them ("loss of physical structures, fruit trees, businesses
and access to rental houses due to land pooling") plus three owners never traced and never
paid, again in a footnote. Social safeguard compliance is rated Satisfactory by the completion
report, and the Evaluation Group's review says compensation payments were made to the affected
people. Land pooling is also a scheme owners agreed to, contributing 25 per cent of their land
and keeping a serviced plot — not a taking. Three unpaid owners is a real limb (b) harm and
the shape of the map's weakest existing keep, but it is three people and no count of anything
else.

Third weakest, named because it may be the one to argue about rather than the one to cut:
**`jordan-heritage-cities-house-shop-demolition`**. The figures are solid — an actual column
beside a planned column, repeated by the Evaluation Group, with the actual below the plan on
every line — and it qualifies under round 20's housing-demolished rule without a household
count. But nothing went wrong: compensation was higher than planned, set on market value at
replacement cost, affected people are recorded as satisfied and renters went back to renovated
shops. The case is "homes and shops were demolished", nothing more, and the card says so.

## (b) Did the pre-extracted briefs help or mislead?

**Net: they helped, and mostly by what they saved rather than by what they found.** Having 13
documents per project already on disk as greppable UTF-8 is worth more than every candidate
sentence in the briefs put together. Zero searches were spent on Bank documents. Seven of the
ten cases turn on a passage that no candidate sentence in any brief surfaced.

What the briefs got right:
- **The document inventory and the paths.** Flawless. Every path resolved.
- **The parent/sibling candidates on the two rows with no outcome document.** Both candidates
  were right, and both were verifiable against the documents rather than on the name. P010556
  was confirmed for P099040 by approval date: the parent's completion report says "Additional
  Financing – October 8, 2005 Earthquake – approved on December 1, 2005", which matches ICIJ's
  approval date to the day, and the component list matches the loan number Ln. 7341-PK.
  P050529 was confirmed for P116197 by the cover page, which prints both P-numbers.
- **Flagging staff statements.** The "informed IEG" / "the project team" grep caught real
  traps. Two mattered: the Karnataka row (the only compliance statement on the environmental
  policy is a staff statement) and the India tsunami row, where the only figure for people
  physically displaced in Tamil Nadu — 100 families — exists solely as something the project
  team told the evaluators, which is why that figure is attributed to the staff statement on
  the card and is not in `displaced`.
- **The plan-reprint check.** Three rows were flagged. All three flags were false in the sense
  that mattered, but cheap to clear: P086414's 363 is a line length in kilometres, P131550's
  was likewise not a people figure, and P112893's resolved on the verb. The check cost about
  five minutes total and is worth keeping.

Kinds of candidate sentence that were pure noise:
- **"replacement cost"** — fired on the entitlement-matrix recital in every single resettlement
  framework, exactly as BRIEF31 warned. Not one hit of this kind was usable on any row.
- **"police"** — did not fire usefully once. The one real police action in the batch (54
  arrests at Chobhar) is not in a Bank document at all and no grep of the cache could have
  found it.
- **"PLAN VERB — the reprint trap"** — the lowest-value category. On P113416 it returned "no
  technical issues are envisaged during appraisal", a sentence about procurement risk with no
  people in it; on P099040 it returned a definition of a corridor-of-impact limit.
- **"affected, NOT a relocation count"** — correctly labelled, but on P086414 the two hits came
  from a plan for a *different substation under a different operation* (Solapur, Western Region
  System Strengthening II), which the brief had no way to flag and which would have been an
  easy card to write wrongly.

**What the briefs should have surfaced and did not.** One pattern, and it decided four of the
ten cases:

> **Footnotes, and compensation-status tables printed after the closing date.**

The single most load-bearing sentence on this batch's weakest case is footnote 23 of the Dhaka
completion report. The Bhutan case is footnote 22 of its completion report. The Iraq worker
deaths are in running text but the two extra deaths are footnoted to an Implementation Status
Report. And the Kabeli case is a table headed "Compensation payment progress" sourced to
"Kabeli TL Project, August, 2018" — compensation figures *dated twenty months after the project
closed*, printed in the completion report. None of these appeared as a candidate sentence.
A pattern for `^\s*\d+\s` footnote bodies containing `compensat|evict|relocat|unpaid|traced`,
and one for tables whose source line carries a date later than the closing date, would have
caught all four.

Second, smaller gap: **nothing flagged the borrower's own annex.** The Pakistan case's sharpest
finding — "Utilization of funds by AJ&K government for other purposes rather than disbursement
to affected persons" — is on page 49 of the completion report, in the borrower's section, and
reaches the Evaluation Group's review only as a half-sentence. Annex 7 of that report also
records the delay in releasing funds by the implementing agency "despite the fact that the land
acquisition was financed by the Bank". A grep restricted to the borrower's-ICR annex would be a
high-yield pattern.

## (c) Figures where documents disagree, left unreconciled

1. **Dhaka, households affected by canal works.** The completion report's main text and its
   Annex 2 give **216 households compensated along the khals** (and 225 households receiving
   compensation, for a results-table total of 441 against a target of 500). The **borrower's
   own section of the same report** says the improvements on the nine canals "as a whole,
   affected **187 persons/households**, of which 67 were encroachers" who the framework made
   ineligible for resettlement assistance. 216 against 187, inside one document, with no
   explanation of the gap. Both are on the card.
2. **Chobhar, people detained on 17 January 2019.** The **Request for Inspection** of 25 April
   2020 says "**fifty-two** locals were arbitrarily detained from the streets and their houses".
   **The Kathmandu Post** of 18 January 2019 says police arrested "**at least 54**", attributing
   the figure to Panchha Lal Maharjan of the Chobhar Conservation Committee. Both are on the
   card, with who says which.
3. **Iraq, deaths.** The completion report's paragraph 73 records "two unfortunate accidental
   deaths of two members, the resident engineer and the contractor, between July 2017 and
   August 2018". Paragraph 74 records "three worker fatalities" and describes them, one of
   which is "a supervising engineer who was run over by a project vehicle". Whether the
   engineer in paragraph 73 is the engineer in paragraph 74 is not stated anywhere, and the
   Evaluation Group's review repeats both passages without reconciling them. `killed` is 3, the
   three with stated causes; the two of paragraph 73 are in `killed_note` saying the documents
   do not establish whether they are the same deaths. **If the checker can resolve this, the
   count may need to go to 5.**
4. **Iraq, outcome rating.** Completion report: Highly Satisfactory. Independent Evaluation
   Group: Satisfactory, on minor shortcomings in efficacy. Quality of monitoring runs the other
   way — the report says Modest, the Group says Substantial. Both named with their document.
5. **Pakistan, outcome rating.** Completion report: Satisfactory. Evaluation Group: Moderately
   Satisfactory, efficiency modest on significant cost overruns. Risk to development outcome:
   report Moderate, Group Significant.
6. **Lebanon, outcome rating.** Completion report: Satisfactory, safeguards Satisfactory.
   Evaluation Group: Moderately Satisfactory, efficiency modest on high cost overruns. And the
   Group's own field report of 2019 contradicts the completion report on the Tyre market: the
   report calls the marketplace resettlement satisfactorily implemented and award-winning, the
   field report found fewer permanent vendors working there than the resettlement plan had
   arranged for and the market deserted on a day that should have been busy. Both accounts are
   on the card.
7. **India tsunami, families physically displaced in Tamil Nadu.** The completion report counts
   6 displaced families in Nagapattinam and about 100 host families affected at two resettlement
   sites. The Evaluation Group's review says, **"According to the project team"**, that the 100
   families subject to physical displacement were either given alternative housing or expected
   to be shortly. The 100 as a displacement figure exists only in the staff statement; it is on
   the card as a staff statement and not in `displaced`.

## (d) What could not be checked, by route

- **Pakistan, the Babusar Top overlap.** A Senate Standing Committee on Communication hearing
  reported by The Express Tribune on 22 February 2019 concerns unpaid land acquisition on the
  Naran–Kaghan–Babusar Top road — which is N-15, one of this project's three roads — covering
  1,698 kanals at Rs 0.274 million per kanal, unpaid for 17 years. Seventeen years back from
  2019 is about 2002, three years before this loan, and 1,698 kanals is not 1,007. **Route that
  failed: there is no document on either side that ties the two acquisitions together or
  separates them.** The fact is left off the card rather than guessed at, and is recorded in
  `confidence_note` as unmatchable.
- **Pakistan, the Auditor General route.** `agp.gov.pk` served the Special Audit Report on
  Acquisition of Land for National Highway and Motorway Projects (audit year 2016-17) over
  `curl` with a browser user agent, 828 KB, and `pdftotext -layout` read it. **The route
  worked; the document does not cover the three earthquake-damaged roads.** Its two near-misses
  are a Muzaffarabad Dual Carriageway (a different project) and a Baleli Bridge Road reference
  carrying the string N-35. `saiindia.gov.in/uploads/` was not needed, because no Indian audit
  route was opened: the two Indian rows that survived reading are a drop and a case whose harm
  is a single district-level demolition that a state audit report would be unlikely to carry
  under a searchable name.
- **Nepal, Inspection Panel case 147 final report.** The Panel's Report and Recommendation not
  to investigate was not fetched; the Notice of Registration (27 May 2020) and the Request for
  Inspection (25 April 2020) were, both from `inspectionpanel.org` over `curl` with a browser
  user agent. The outcome — Panel visited, found no sufficient grounds, recommended stronger
  consultation — is taken from the completion report and its review, both of which state it.
  **Route not attempted rather than failed.**
- **Lebanon, local press.** No Lebanese press, court record or audit on the Khan el Askar or
  Tyre market relocations was found. **Route that failed: search.** The Bank's own field-based
  Project Performance Assessment Report is doing the work an independent source would do, and
  the card says so, but it is still the lender's document and the case stays `contested`.
- **Bhutan.** No Bhutanese press, court or audit source on the Thimphu land pooling
  compensation was found. **Route that failed: search.** Bhutan has a small searchable press
  and the three unpaid owners are, on the documents, unidentified.
- **Egypt, Bangladesh, Jordan, Iraq.** No independent source was found for any of them; for
  Egypt and Palestine that does not matter because both are drops. **Route that failed:
  search.** For Iraq specifically, the three worker deaths carry no names, no dates and no
  contractor in either document, which leaves nothing to search on.
- Two WebSearch calls were interrupted mid-batch by a session restart and were re-run; nothing
  was lost. **That is a route interruption, not a host refusal.**

Searches used: 6 WebSearch, 5 WebFetch, 3 direct `curl` fetches, 10 Nominatim lookups — well
under the 40 budgeted, because nine of the fifteen rows had no outside source to find.

## Cache and files

- Bank documents: `/home/claude/work/cache/<PID>/`, already there at the start of the batch and
  not re-fetched. Used from this batch: the 15 rows' own folders plus **two parents that were
  already in the cache and are not in the batch file** — `P010556/` (Pakistan Highways
  Rehabilitation: completion report 21 Nov 2013, ICR Review 11 Jun 2014, appraisal document,
  five loan agreements, one resettlement plan) and `P050529/` (Lebanon Cultural Heritage:
  completion report 15 Jun 2017, ICR Review 22 Nov 2017, **Project Performance Assessment
  Report 13 Aug 2019**, appraisal document, two agreements, twelve resettlement plans). Anyone
  working either of those cases should go to the parent folder, not the batch row's folder,
  which has no outcome document in it.
- Non-Bank documents downloaded in this batch: `/home/claude/work/ext/`, as paired `.pdf` and
  `.txt`:
  - `147-Request_for_Inspection-25Apr2020-Redacted_0.pdf` / `.txt` — Inspection Panel case 147,
    Chobhar dry port
  - `147-Notice_of_Registration-27_May_2020.pdf` / `.txt` — same case
  - `agp_special_ar_land_nha.pdf` / `.txt` — Auditor General of Pakistan, Special Audit Report
    on Acquisition of Land for National Highway and Motorway Projects, audit year 2016-17 (does
    not cover the earthquake roads; kept so the next round does not fetch it again)
- Nothing was merged into the map, `build.py` was not run, nothing was pushed.

## Coordinates

All ten case points were resolved through OpenStreetMap's Nominatim and the resolved name is
recorded in each `point` field. Six carry `ap: true` because the coordinate is a town or
district rather than the exact works: Pakistan (Muzaffarabad, for a harm spread over three
highways in two jurisdictions), Narayanghat–Mugling (Mugling, for a 33 km road), Nagapattinam
(district headquarters; the canal stretch is unnamed), Dhaka (Khilgaon; the eviction canal is
unnamed), Thimphu (Dechencholing, first of three neighbourhoods), Iraq (Nasiriya, for two
expressway segments plus a northern section), Lebanon (Khan el Askar, for works in five
cities), Jordan (Jerash, for works in five towns) and Kabeli (Phidim, for a 90 km line).
`chobhar-dry-port-arrests-kathmandu` is the only case whose point is the site itself.
