# Round 32 — batch `southasia_mena` (7 rows)

Output: `/home/claude/work/out32/southasia_mena.json`

## Outcome of every row

| PID | ICIJ row | Outcome | Reason in one line |
|---|---|---|---|
| P084461 | GZ- Electric Utility Management (Palestine, est. 38) | **case** `west-bank-substation-land-taking-eump` | Land taken from 38 owners at four substation sites; works began at three of them before the Bank cleared the resettlement instruments, with compensation unfinished. |
| P041396 | Integrated Solar Combined Cycle (Morocco, est. 35) | **dropped** | 203 ha acquired, 48 persons and bodies affected, no displacement, compensation paid, no loss recorded in any outcome document. |
| P071191 | Ahwaz & Shiraz Water Supply and Sanitation (Iran, est. 8) | **case** `ahwaz-jomhori-pumping-station-house-expropriation` | Completion report records a house expropriated for pumping station AS23-1 and resettlement of at least eight individuals. |
| P103189 / P075776 | Africa Stockpiles Programme (Tunisia, est. 8) | **dropped** | Temporary resettlement of a shop occupant and seven workers, implemented and compensated; completion report calls it highly satisfactory. |
| P122735 | Metro Colombo Urban Development (Sri Lanka, est. 2) | **extend** to `colombo-st-sebastian-canal-mcudp` | Already on the map on CPA's account; the 2022 completion report and a 10 November 2026 committee hearing add the Norris Canal eviction, the project-wide total and the current state. |
| P118028 | ARTF-2nd Judicial Reform (Afghanistan, no estimate) | **dropped** | Completion report: "land acquisition or relocation did not occur as all construction work was carried out on available government land." |
| P120843 | BD Private Sector Development (Bangladesh, no estimate) | **dropped** | Two plans counted 24 households to displace; the completion report says the resettlement budget was not needed and spent US$0.0m, and the Mirsharai approach road was built by the Roads and Highways Department. |

Two cases, one extend, four drops. The extend was found by the dedupe script, not by name: `P122735`
is already on the map as `colombo-st-sebastian-canal-mcudp`, carried there on a Centre for Policy
Alternatives report, with no Bank completion report because the report did not exist until
December 2022.

## My own two weakest entries

**1. `west-bank-substation-land-taking-eump` — the harm is land taken with money assessed, and the
substations were not paid for by the Bank.** Two things to test hardest:

- The limb (b) harm is "land taken" plus "compensation unfinished", not compensation refused. The
  strongest single line is in the resettlement plan's annexed compensation table for Jenin:
  23 owners, JD 66,315.2, no expropriation decree number, no date, comments column
  "Assessed amount not yet awarded" — while the plan's own summary table two pages earlier marks
  the Jenin status "Resettlement process finish". Both are in the card. If a checker reads
  "assessed but not awarded" as an administrative stage rather than a loss, the card thins to
  the completion report's sentence that the compensation process "had started but it had not yet
  been completed" when civil works began, plus the review's harder reading of the same page.
- The four substations were financed by the European Investment Bank, not by the Bank's trust fund
  grants, which paid for the central distribution system, distribution rehabilitation, capacity
  building and the start-up of the new transmission company and regulator. This is the Burkina
  Faso test. The reasons it is not the Burkina situation are on the card: the substations were
  Component 1 of the project the Bank appraised, the Bank required the resettlement policy
  framework they were prepared under, and it was a Bank supervision mission that found the
  borrower non-compliant at three of them. EIB is listed as the second lender rather than being
  hidden behind the Bank. If the checker disagrees, the honest fix is to keep the card with EIB as
  `lenders[0]`, not to delete it.

**2. `ahwaz-jomhori-pumping-station-house-expropriation` — `displaced: 8` is the same number ICIJ
gives, and that will look wrong at first glance.** It is not ICIJ's figure. It is the completion
report's own sentence: "Since the deal involved resettlement of at least eight individuals, an
abbreviated Resettlement Action Plan (RAP) was prepared", in the safeguards section, about a house
that the same sentence-pair says "was expropriated". Both the label and the note say it is a floor
("at least eight"), say where it comes from, and say that ICIJ's identical 8 is a count of affected
people. If the rule is read strictly — ICIJ's number must never sit in `displaced`, whatever its
provenance — strip the field and the card still stands on limb (b): a home of two owners taken, a
down payment paid and nothing in any document about the balance. The whole case is two sentences of
the lender's own prose; there is no independent source at all.

## Unreconciled figures, with both sides

1. **Palestine, where the compensation ended up.** Completion report, 24 March 2017, paragraph 30:
   "Project affected people were identified prior to construction and the compensation process had
   started but it had not yet been completed", followed by "The issue was solved thanks to the
   proactivity of the Bank team". ICR Review, 2017, section 11a, reading that same page: "Although
   project affected people were identified prior to the commencement of construction activities,
   the compensation process had not been completed by project closure (ICR, page 12)". The review
   then says the task team leader "subsequently informed IEG that the process was subsequently
   completed" — a staff statement, flagged as such on the card and not used as a fact.
2. **Palestine, Jenin's status.** Summary table: "Resettlement process finish". Annexed
   compensation table for the same parcels: "Assessed amount not yet awarded", with the
   expropriation decree number and date blank. Same document, March 2011.
3. **Iran, risk rating label.** Completion report data sheet: Risk to Development Outcome
   **Substantial**. ICR Review's own ratings table, in the column for the completion report's
   rating: **Significant**. The review's own rating is also Significant. This is the label
   substitution BRIEF20 warns about, and it is in the review's table, not its text.
4. **Iran, whether residences were affected.** Appraisal document, 29 April 2004, OP 4.12 section:
   "In no case are residences or current economic activities or livelihoods affected." Completion
   report, 31 March 2010: the land for pumping station AS23-1 "was a residential house that
   belonged to two individual owners". Neither document explains it; both are on the card.
5. **Iran, the date of its own completion report.** Cover page: March 31, 2010. Data sheet two
   pages later: ICR Date 04/06/2010. The card and sources use the cover date.
6. **Iran, the tense of the harm to poor neighbourhoods.** Completion report: lack of completion
   "will disproportionately affect the poorer segments of the society". ICR Review: it "has
   disproportionately affected the poorer segments of society". The review turns a forecast into an
   outcome. Not used as harm on the card; the completion report's own counter-clause, that the
   proportion of completed works is also higher in poor neighbourhoods, is quoted beside it.
7. **Colombo, Norris Canal owners.** Completion report, paragraph 59: the 24 households
   "comprised 16 tenants and 8 legal owners", then, four lines later, acquisition "of the
   properties belonging to the four legal owners". 8 against 4, same paragraph, no explanation.
8. **Colombo, grievances.** Bank text: 407 grievances, 377 resolved. Borrower's own section of the
   same report: 423 grievances. Both figures are in the extend.
9. **Colombo, the unfinished stretch.** Completion report: 126 metres of 675 not built. The
   Morning, 11 November 2026: the route "stalled 100 to 150 metres short of completion". Both given.
10. **Bangladesh, 14 households against an unspent budget.** Mirsharai EZ2 abbreviated resettlement
    plan, August 2016: road widening "will displace a total of 14 non-titled households ... and
    5 mosques". Completion report, 22 December 2021: resettlement compensation "was ultimately not
    needed", resettlement line US$0.9m allocated, US$0.0m actual. No document found says what
    became of the 14. This is the sharpest open question in the batch and the drop reason says so.

## Did the pre-extracted briefs help or mislead?

They helped, in two ways that mattered and one that was decisive.

- **Decisive:** the brief's own warning that the extraction is thin on footnotes and annex tables
  is what sent me to the Palestine completion report's footnote 17 (the emailed complaint from the
  Nablus substation's nearest neighbour, who met the task team with four other neighbours and the
  mayor) and to the Jenin compensation annex ("Assessed amount not yet awarded"). Neither appears
  in any candidate sentence. The same instruction found the Colombo borrower section's 423
  grievances against the Bank text's 407. Three of the four things the brief predicted would be
  missed were in fact missed by the patterns and present in the documents.
- **The plan-reprint check worked as described** on Morocco. It returned 203, 160 and 88, and the
  verbs settled it: "will be acquired" in the appraisal document, "were acquired" in the completion
  report's own annex 2. Those figures are outcomes, not a reprint — which is why the Morocco drop
  rests on the absence of harm and not on the figures being plan figures.
- **What it should have surfaced and did not.** Three kinds:
  1. **The sentence that kills a row.** The Afghanistan brief carried two candidate sentences, one
     of them the replacement-cost recital, and neither was the completion report's
     "land acquisition or relocation did not occur as all construction work was carried out on
     available government land" — the single sentence the row turns on. Likewise Bangladesh's
     "this was ultimately not needed" and its US$0.0 million resettlement line. A pattern for
     "did not occur / was not needed / not required" in an **outcome** document, reported as a
     finding rather than filtered out, would save a reader a full pass.
  2. **A plan's count where the outcome document is silent.** The Mirsharai "will displace a total
     of 14 non-titled households" sentence is the whole of that row's open question and it is not
     in the brief, even though the brief has a "count with a relocation verb" bucket — which on
     that row returned a quotation of OP 4.12's own 200-person threshold instead.
  3. **Figures inside a table's own rows.** The Palestine summary table's "Number of person
     affected" column — 23, 10, 4, 1, totalling exactly ICIJ's 38 — is the origin of ICIJ's
     estimate for that row and it appears nowhere in the brief.
- **Noise.** The worst buckets were "borrower's own account, not the Bank's", which on three of the
  four rows that had it returned nothing but the table of contents line for Annex 8, and "eviction, or people
  never traced", which on Morocco returned two paragraphs about the global solar thermal industry
  and on Iran returned Iranian expropriation law on owners who cannot be found. "Replacement cost"
  fired on the policy recital every time, as predicted.

## Routes, and what failed on them

- **Source URLs.** Taken from `harvest_manifest.json` `pdfurl`, with the host rewritten to
  `documents1.worldbank.org` and `http` upgraded to `https`, which is what BRIEF20 says to do with
  that field. The manifest serves them on `documents.worldbank.org`, which answers **302 to HTML**
  for the same path. All ten URLs shipped in this file were checked with a HEAD request and return
  **200 `application/pdf`**. No URL was constructed.
- **Nominatim** returned nothing for "Sarra, Nablus, Palestine", for "Beit Oula, Hebron, Palestine"
  or for "Al-Mqeible, Jenin, Palestine" in those forms. Dropping the country words worked for two
  of them: bare "Sarra" with `countrycodes=ps` returns the village صره at 32.2095, 35.1902, and
  "بيت أولا" in Arabic returns Beit Oula. "المقيبلة جنين" returns nothing in either script, so the
  Jenin village is named on the card but not plotted. "بلوار جمهوری اهواز" and
  "Jomhouri Street, Ahvaz" both return nothing, so the Iran point is the city, with `ap: true`.
- **What could not be checked.** Whether any of the 38 Palestinian owners was ever paid: there is
  no later document in the harvest, and the only statement that the process finished is attributed
  to a Bank staff member by the Bank's own evaluators. Whether the 14 households on the Mirsharai
  access road lost their homes: no outcome document mentions them, and the one outside report found
  on that road, the Financial Express of 1 March 2019, discusses 46 acres handed over and names no
  households. What the "smaller incidents" at the Tunisian pesticide store were: the completion
  report mentions them and describes none.
- **Searches spent: 9 of about 40, plus four page fetches.** Eight searches returned nothing
  usable; one returned the piece that carries the Colombo extend. The nil results, so the next round does not repeat them: Arabic and
  English searches on the Nablus, Beit Oula and Jenin substation land and compensation (nothing on
  the land takings; `poica.org` indexes Israeli confiscations, not Palestinian Authority
  expropriations); a Persian search on the Ahwaz pumping station and Jomhori Boulevard (nothing);
  a French search on the Ain Beni Mathar collective land and its rights-holders (nothing but the
  Bank's and EIB's own documents and Masen's unrelated Noor prospectuses); two searches on Colombo
  canal relocations that returned the 1990s JICA-funded Greater Colombo Flood Control project and
  the government's Urban Regeneration Project, neither of which is this loan — Nishara Fernando's
  2018 study of three Colombo relocations covers 1990s projects and never mentions the World Bank,
  and groundviews' "Evicted under the World Bank's watch" (29 May 2015) names no project, no canal
  and no Bank operation, so neither was used.
- **The one find.** `themorning.lk`, 11 November 2026, "NHSL flooding: Officials blame 8 houses
  blocking new drain", fetched with `curl` and a browser user agent after a fetch tool returned
  only a summary. It reports the same eight households still in the building on the Norris Canal
  route, the Rs 5 million and then about Rs 11 million housing offers they refused, an official
  saying the government will proceed under the Land Acquisition Act, the Prime Minister agreeing,
  and a proposed task force including the police and the armed forces. It does not mention the
  World Bank; the tie to the loan comes from the Bank's completion report, which names the same
  canal and the same unfinished stretch. That limitation is written into the extend's
  `confidence_note`.

## Two things the lead has to do by hand

1. **`colombo-st-sebastian-canal-mcudp` has `end: 2016`.** The facts added run to November 2026.
   `fields_add` cannot set a number, so the field is untouched in the file. It should become 2026,
   or 2021 if the map's `end` means the project's closing date.
2. **That case's `lenders[0].role` carries no P-number.** It cannot be edited through
   `fields_add` either. P122735 is written into the appended prose so the next round's dedupe can
   see it, but the lender role should get it properly.

## Document cache

Nothing new was downloaded from the Bank. Everything read is where the briefs said it was:
`/home/claude/work/cache/P084461/`, `/P041396/`, `/P071191/`, `/P103189/` and `/P075776/`
(the Tunisia resettlement plans are under P075776, not P103189), `/P122735/`, `/P118028/` and
`/P120843/`. Two files fetched from outside the lender are in `/tmp/ext_lk/`:
`morning.html` (The Morning, 11 November 2026) and `fernando.pdf` with its `.txt` (the 2018
Colombo relocation study, read and not used).
