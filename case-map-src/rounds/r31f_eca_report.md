# Batch `eca` — 15 rows from ICIJ's confirmed-displacement table

Output: `/home/claude/work/out/eca.json` — 8 new cases, 7 drops, 0 extends, 0 already-on-map.
All 15 P-numbers were run through `dedupe_leads.py` before any research: all 15 came back "not on the
map", and each case was then checked by place and years against the local-match hints. None of the
eight matched an existing case under a different name. Every case carries its P-number in
`lenders[0].role`.

## Row by row

| P-number | Project, country | Outcome | Why |
|---|---|---|---|
| P086768 | Odra River Basin Flood Protection, Poland | **case** `raciborz-polder-nieboczowy-village-removal` | Limb (a). About 700 people in about 250 households resettled from Nieboczowy and Ligota Tworkowska; houses, church and cemetery removed; 30 houses taken by administrative decision in 2013. |
| P096181 | Energy Sector Cleanup and Land Reclamation, Kosovo | **case** `hade-shala-neighbourhood-mine-resettlement` | Limbs (a) and (b). 63 households, 320 residents, physically displaced from the Shala neighbourhood; years in temporary housing; rent allowance stopped April 2014 with the site unready; legal-covenant breach; Inspection Panel investigation. |
| P091723 | Second Trade and Transport Facilitation, North Macedonia | **case** `tabanovce-kumanovo-motorway-compensation-arrears` | Limb (b). Land from about 102 owners, 294 parcels; compensation not paid to all owners before works started; Bank Warning of Suspension, March 2009; "a serious safeguard violation". |
| P094044 | Second East-West Highway Improvement, Georgia | **case** `igoeti-sveneti-highway-worker-death-and-land-damage` | Limb (b). A contractor's employee killed on site; contractor refused compensation to the family for about 1.5 years; works begun on an Igoeti resident's land before acquisition was complete, damaging her house. |
| P110538 | Ferghana Valley Water Resources Management Phase I, Uzbekistan | **case** `ferghana-valley-drainage-land-taken-without-plan` | Limb (b). 338 farmers' land taken 2012–14 without the resettlement plan being updated (OP 4.12 non-compliance); payments late, after works began; most farmers received no cash because compensation went against tax arrears. |
| P077328 | Railways Restructuring, Turkey | **case** `yenice-logistic-village-urgent-expropriation` | Limb (b). Urgent expropriation under Article 27 at Yenice; courts granted land entry on 30 June 2010; 43 parcels left to valuation lawsuits. |
| P126033 | Regional Development, Georgia | **case** `dartlo-telavi-rehabilitation-compensation-delays` | Limb (b). At Dartlo no owner was paid in 2012; money due to 21 people was paid in 2014 to 19, two still unpaid in 2016. At Telavi 37 grievances from 2014 went unanswered until 2016. |
| P114766 | Moinak Electricity Transmission, Kazakhstan | **case** `moinak-transmission-line-land-taken-before-plan` | Limb (b), narrowly. 14 ha permanent and 555 ha temporary taken from 316 land users; the line was built before the Bank approved the land acquisition plan; agreements still being concluded in May 2012. |
| P107608 | National Road Rehabilitation (Osh-Batken-Isfana), Kyrgyzstan | **dropped** | Completion report: no land acquisition and no project-affected people under the parent project or the first additional financing; seven road-side businesses at the Nookat pass paid KGS 350,000 for lost profit. |
| P104994 | Bishkek and Osh Urban Infrastructure, Kyrgyzstan | **dropped** | Nine project-affected people in total, each itemised and paid, one complaint resolved at first instance. |
| P116748 | Electricity Supply Reliability, Armenia | **dropped** | No outcome count of land, households or unpaid compensation; the delays' stated consequence is that the transmission works finished in 2020, four years late; 80–95 per cent of affected households recorded as satisfied. |
| P117152 | Kakheti Regional Roads Improvement, Georgia | **dropped** | 31 land plots acquired against 174 expected; all owners fully compensated and no complaints, in both the 2016 review and the 2020 assessment report. |
| P110267 | Second Rural Water Supply and Sanitation, Kyrgyzstan | **dropped** | 118 affected people in ten villages, mostly temporary access restrictions and trees, all fully paid before closing, KGS 1,979,254. |
| P102733 | Water Sector Investment, Albania | **dropped** | "The project avoided resettlement by changing the routes"; the only specific complaint is a contractor's delay in restoring a local road, with no people identified. |
| P119939 | Talimarjan Transmission, Uzbekistan | **dropped** | 12.03 ha permanent and 159.42 ha temporary from leasehold farms; 141 farmers and district administrations compensated by April 2013; no complaints recorded. |

Each drop record quotes the sentence that decided it, names what was checked in the outcome
document, and gives the URL of that document.

## (a) The two weakest entries

**1. `moinak-transmission-line-land-taken-before-plan` (P114766, Kazakhstan) — the weakest.**
Nobody was relocated; the completion report says all 316 land users "received reasonable cash
compensation" and that all compensation was completed before the loan closed. The whole case is
limb (b) in its narrowest form: land taken, 14 ha permanently, plus the order of events — the line
was built before the Bank approved the plan that set each land user's entitlement, and the plan
itself records compensation agreements still being concluded in May 2012. Not one land user is
identified, no amount paid to any of them appears in the text (the plan refers to an appendix with
the per-user amounts that the text does not reproduce), and no complaint exists anywhere. This row
sits on the line between a thin case and a drop; its nearest neighbour in this batch, P119939
Talimarjan, was dropped, and the only thing separating them is that at Moinak the works started
before the plan was approved. If the checker cuts one entry from this batch, this is the one.

**2. `dartlo-telavi-rehabilitation-compensation-delays` (P126033, Georgia).**
The moves were temporary, the numbers are small, and the lender's own conclusion runs the other
way on every point: the completion report says the project complied with OP 4.12, that all
complaints were addressed and that the Dartlo plan was "completed without grievances or
complaints" — the last of which sits oddly beside the plan update's own record that no owner was
paid in 2012 and two were still waiting in 2016. The Telavi strand is the 37 unanswered grievances
and the footnote that they were claims that compensation did not cover losses; the lender's
independent consultant then "confirmed compliance", so the compensation claim itself is
unresolved and only the two-year delay is solid. Georgian-language searching found nothing
outside the lender.

Honourable mention for a different reason: `yenice-logistic-village-urgent-expropriation` (P077328)
rests entirely on one document, the borrower's March 2011 resettlement plan, and on a facility the
lender's own review calls "not financed by the project but adjacent to the project". That is the
Burkina Faso airport-platform trap in a new shape. It is kept, and flagged on the card, because the
lender did the opposite of what it did at Burkina: it pulled Yenice inside the project's
resettlement plan and restructured the loan to create obligations to implement that plan. A
checker who reads that differently should cut it.

## (b) Did the pre-extracted briefs help?

They helped, substantially, in one way and were actively misleading in another.

**What helped.** The document inventory with paths was worth more than everything else in the brief
put together. Zero searches were spent re-finding Bank documents, and having the appraisal document,
the completion report, the evaluation review, every resettlement plan and, where it existed, the
assessment report all on disk as greppable text made it possible to read whole paragraphs around
every hit instead of sampling. The plan-reprint check earned its place on P086768: it surfaced the
700/250 figures in both the evaluation review and a 2005 resettlement plan, which forced a check of
the verb — and the verb settles it, because the 2005 plan says "will entail… the resettlement of
almost 700 people" while the completion report of 2021 says the process "included around 700
individuals belonging to about 250 households". Same number, plan and outcome, and only the verb
tells them apart. BRIEF31's instruction to look for a late-project plan update also paid off twice:
the Dartlo abbreviated plan update of July 2016 is the only document in the P126033 set that records
the 2012 compensation going unpaid, and the Fergana land-acquisition report of November 2015 is the
only document with the per-resolution payment table.

**Which candidate-sentence kinds were noise.** In order of how much time they cost:

- **"replacement cost"** — noise in all 12 appearances: it fires in 12 of the 15 briefs, once each. Every one was the definitional glossary
  entry or the entitlement-matrix recital in a resettlement framework. Not one indicated a payment
  below replacement cost.
- **"death, with any cause given"** — noise in every appearance but one. On P107608, P094044 and
  P117152 these were road fatality rate indicators ("number of fatalities per 10,000 cars"), and on
  P086768 it was the project's own development objective ("protect the population… against loss of
  life"). The one real death in this batch, the contractor's employee on P094044, did also come up,
  so the pattern is not useless — but one of the nine hits in this batch was a real death and eight were not.
- **"arrests, police or force"** — noise in all four appearances. On P107608 it was a jurisdictional
  dispute between two ministries over who owned the road safety strategy; on P096181 it was the word
  "lateral dam structures… raised against the existing pit walls"; on P110538 it was a groundwater
  table that needed to "be arrested and reversed".
- **"compensation unpaid or late"** — the best of the patterns: about half of its 12 hits were signal. The real finds on P091723, P110538 and
  P126033 all came through this pattern. The false ones were monitoring-indicator headings in
  resettlement plans that list "number of people not receiving compensation in time" as a thing to
  be measured (P119939, both hits), and the standard clause allowing possession before payment where
  the money is pledged in court (P116748).
- **"count with a relocation verb"** — 7 hits, and the worst false positives of all, because they look like
  findings. On P107608 and P104994 the hit was the June 2010 Osh civil unrest, in which "about
  400,000 people were displaced and several hundred people lost their lives" — a real catastrophe,
  nothing to do with the project, which the completion report gives as a reason for implementation
  delay. A writer skimming would have put 400,000 displaced on a Kyrgyz road card. On P110267 and
  P126033 the hit was OP 4.12's own threshold sentence, "fewer than 200 people are displaced".

**What the extraction should have surfaced and did not.**

1. **The decisive sentence on four of the seven drops is a sentence that says nothing happened**, and
   no pattern looks for it. "There was no land acquisition under either the parent project or AFs,
   and there were no project affected people" (P107608) and "there were nine project affected people"
   (P104994) are the whole answer for those rows, and neither appeared in either brief — not even
   under the "CAUTION — null sentence" heading, which carried framework boilerplate instead. A
   pattern for *outcome-document* sentences of the form "there were N project affected people" /
   "no land acquisition was required under the project", confined to the ICR and the review, would
   have been the single most useful addition.
2. **Settlement, payment and court-order sentences in resettlement plans written in the past tense.**
   The whole P077328 case is in one such passage — expropriation value set by the Tarsus courts,
   money remitted to owners' accounts on 30 June 2010, land-entry permits granted, 43 parcels sent
   to lawsuits. None of it appeared in that brief, whose seven hits were all glossary and policy
   recital. A pattern on "was carried out", "has been carried out", "were paid", "lawsuits were
   filed", "title transfer was carried out" inside RP documents would catch it.
3. **The "where did the money actually go" sentence.** "In most cases, the PAPs did not receive any
   cash as compensation was used to settle outstanding tax arrears" (P110538) is one of the sharpest
   facts in the batch and it reached the brief only as the tail of a hit whose head was about bank
   requisites.
4. **Project-boundary sentences.** "Not financed by the project but adjacent to the project"
   (P077328) and "the project did not cause nor finance the resettlement; it only supervised"
   (P096181) decide how a case may be written at all. Both had to be found by hand.

One structural caution about the briefs, offered as a user's report and not a complaint: by handing
over a clause with its document and date already attached, the brief makes a quotable-looking
fragment the path of least resistance. On P117152 the brief's null-sentence block quoted a paragraph
beginning "At appraisal, no land acquisition or resettlements were envisioned… Minor land
acquisitions had to take place during project implementation", labelled **[PPAR 2020-06-17]**. That
paragraph is real and that is the right document — but it sits under the heading for the *other*
project the assessment report covers, Georgia Secondary and Local Roads, P086277. Kakheti's own
paragraphs, four pages later, say something different: 31 land plots instead of 174, all owners
fully compensated, no complaints. The brief is accurate and the inference from it would have been
wrong. Any brief drawn from a joint-project assessment report needs the section heading carried
along with the hit.

## (c) Figures where documents disagree, left unreconciled

1. **P110538, Ferghana Valley — safeguards compliance.** The completion report of 16 May 2017 says
   land acquisition took place without the resettlement plan being updated, "which constituted a
   noncompliance with the World Bank OP 4.12, causing overall downgrade in the safeguards compliance
   rating", and the evaluation review of 16 October 2017 repeats it. The Independent Evaluation
   Group's field-based Project Performance Assessment Report of 29 March 2019 says, of the same
   project: "Overall, the project complied with the implementation of safeguards. Previous reviews
   of the safeguards confirmed full compliance." Neither document mentions the other's position.
   Both are on the card.

2. **P096181, Kosovo — what the Inspection Panel found.** The evaluation review of 29 June 2017 says
   the Panel found the Bank's approach to the resettlement policy framework and the Shala plan, and
   its monitoring and supervision, "were in compliance with OP/BP 4.12", with "two minor instances
   of non-compliance" over asset valuation, infrastructure delays and malfunctioning sewage.
   Prishtina Insight of 14 November 2016, reporting from the leaked investigation report, says the
   Panel found that the Bank's management "did not comply with its operational procedures on
   involuntary resettlement", that the policy framework lacked methods for valuing the assets of
   people inside the restricted mining zone, and that the Bank's failings contributed to "real and
   often severe harm" over a "prolonged period"; CEE Bankwatch's account of 19 December 2016 adds
   that the planned livelihood restoration programme was never developed. Both versions are on the
   card, each named to its source.

3. **P096181, Kosovo — houses built and occupied at the resettlement site.** The resettlement
   completion report of July 2016 counts, as of June 2015, 22 plots with construction started or
   finished, 15 houses ready for occupation, 12 occupied and 53 people living there. The Inspection
   Panel's report of 2 September 2015 records the community's own count: 23 houses built and 11
   families moved in. Management's figures to the Panel, as of July 2015, were 21 homes under
   construction and 12 families moved in. The documents do not explain the differences. All three
   are small and none changes the shape of the case; the completion report's figures are used on the
   card and the Panel's are given beside them.

4. **P119939, Talimarjan — how many farmers.** 114 in the resettlement plan, 147 in a supervision
   aide-memoire, 141 on the final list of compensated farmers. This one **is** reconciled in the
   source: the completion report explains it by a government farm-consolidation programme and an
   audit that found six farmers paid in error. Recorded here because the three-way mismatch would
   otherwise look like the Xining problem, and it is not.

5. **P086768, Odra — ICIJ against the documents.** ICIJ gives 689; the documents give "about 700"
   residents in "about 250" households. No document states 689 and nothing explains the gap. It is
   not reconstructed, and ICIJ's figure is in `displaced_note` labelled as its count of affected
   people.

Two near-misses worth naming so the checker does not read them as disagreements. On P091723 ICIJ's
estimate, 294, is identical to the completion report's "about 294 parcels of land" in a sentence
whose other figure is "about 102 affected owners". The card states both figures and that 294 is a
parcel count; it does not claim ICIJ counted parcels as people. On P114766 ICIJ's 316 is to the
person the completion report's "316 persons (land users) have been affected", in a sentence that
continues "None had to be resettled" — which is the clearest single illustration in this batch of
what ICIJ's column actually counts.

## (d) What could not be checked — the route that failed

- **The Inspection Panel's 2016 Investigation Report on the Kosovo case (case 103).** The Panel's
  September 2015 Report and Recommendation downloaded and converted cleanly from
  `thedocs.worldbank.org` by `curl` plus `pdftotext -layout`, and it is a source on the card. The
  investigation report and the management report that followed it did not. The failed route: guessing
  sibling filenames under the same `thedocs.worldbank.org/en/doc/<hash>-0490012022/related/` prefix
  — `103-Investigation-Report.pdf` and `103-Management-Report-and-Recommendation.pdf` both return
  **HTTP 404 with a 100,826-byte HTML error page**, i.e. a body that looks like a document to a
  size check. The second failed route: the canonical Panel case page at
  `inspectionpanel.org/panel-cases/kosovo-power-project-proposed-p118287-and-second-additional-financing-energy-sector`,
  which returned a client error through the fetch tool. The host serves documents fine — the
  guessed path and that one page did not. A search result points at a live case page under a
  different slug (`.../proposed-kosovo-power-project-and-second-additional-financing-energy-sector-clean-and`)
  which was not tried. **That is the first thing to try next round**, and it would likely convert the
  two conflicting second-hand accounts of the Panel's findings into one primary document.
- **Independent corroboration for six of the eight cases.** Searches outside the lender found
  nothing usable for North Macedonia (Macedonian, on Kumanovo–Tabanovce expropriation), Turkey
  (Turkish, on the Yenice urgent expropriation and the 43 Tarsus lawsuits), Georgia twice (Georgian,
  on the Telavi business compensation and on the Igoeti worker's death), Uzbekistan (Russian, on the
  Fergana compensation) and Kazakhstan (Russian, on the Moinak land users). These are genuine
  absences in what search returns, not blocked hosts: every search completed and returned results,
  and the results were resettlement frameworks for other projects, unrelated recent news, and
  aggregator copies of the same Bank documents already on disk. The six cases are marked
  `contested` for exactly this reason.
- **Two figures that exist only as references to appendices.** The per-land-user compensation
  amounts on P114766 (the plan's Appendix 2) and the per-farm payment detail on P110538 (Annexes 2
  to 4 of the November 2015 report) are referred to in the body text of documents that are on disk,
  but the text extraction of those appendices is tabular fragments that cannot be read reliably.
  Neither card states any individual amount from them.
- **Nominatim** answered for every place in this batch in Latin script, including "Hade e Re",
  "Bog'dod" and "Dartlo". One query failed mid-transfer and succeeded on retry. One caution for the
  checker: on P086768 Nominatim returns two Nieboczowy — a locality node at 50.0440/18.2593 and a
  village boundary relation at 50.0090/18.3415. The card uses the locality node and the `point`
  field says what it is and where the new village stands relative to it; the choice is consistent
  with the press report that the new village is about 7 km away near Syrynia, which Nominatim puts
  at 50.0236/18.3352.

## Document cache

Nothing was re-fetched from the Bank: all 15 rows were worked from the text already on disk under
`/home/claude/work/cache/<PID>/`, 135 files across the 15 projects (completion reports, evaluation
reviews, appraisal documents, resettlement plans and frameworks in English and in local languages,
conformed loan and financing agreements, and the two Project Performance Assessment Reports for
P110538 and P117152).

One directory was added: **`/home/claude/work/cache/P096181_panel/`**, holding `panel103.pdf` and
`panel103.txt`, the Inspection Panel's Report and Recommendation of 2 September 2015 on the Kosovo
case (Report No. 99247-XK), downloaded from `thedocs.worldbank.org` and converted with
`pdftotext -layout`. That document also supplies the second P-number the Kosovo operation is filed
under, **P131539** for the Second Additional Financing, and the proposed Kosovo Power Project's
number, **P118287**, neither of which appeared in the batch file or the brief.

Source URLs on every card and in every drop record are the real `pdfurl` values from
`/home/claude/work/harvest_manifest.json`, rewritten to `https://documents1.worldbank.org`. Three
were spot-checked with a ranged `curl` and all three returned HTTP 200.
