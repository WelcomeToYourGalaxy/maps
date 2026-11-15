# Round 31, batch `latam` — report

Batch: `/home/claude/work/batch/latam.json`, 15 rows from ICIJ's confirmed-displacement table.
Output: `/home/claude/work/out/latam.json`.

Dedupe: `python3 /home/claude/maps/case-map-src/dedupe_leads.py` on all 15 P-numbers returned
"not on the map" for every one, with the hits all lead data. Confirmed by place and years as well:
`window.CASES` was searched for Santos, Recife, Bogotá, São Paulo, Metro Line, Guajira, Vilcanota,
Cusco, Manta, Pernambuco, Córdoba, Rio de Janeiro, Nicaragua, Haiti, St Vincent and Bolivia. The
nearest existing cases are `bogota-metro-line1-predios` (a different project and corridor),
`cerrejon-resettlements-coal-dust` and `carbocol-sale-tabaco` in La Guajira (both mining, not water),
`itaparica-resettlement` and `suape-van-oord-atradius-tatuoca` in Pernambuco (different projects),
and `santa-fe-road-19-expropriation` in Argentina (Santa Fe, not Córdoba). None overlaps.

## Outcome counts

9 cases, 6 drops, 0 extends, 0 already on the map.

| row | P-number | outcome | key |
|---|---|---|---|
| 1 | P104995 | **case** | `santos-vila-gilda-stilt-house-resettlement` |
| 2 | P124939 | **case** | `hopewell-road-land-taken-st-vincent` |
| 3 | P089013 | dropped | `recife-capibaribe-resettlement-still-pending` |
| 4 | P127088 | dropped | `corn-island-wetland-resettlement` |
| 5 | P120895 | **case** | `cap-labadie-road-compensation-escrow` |
| 6 | P096965 | **case** | `riohacha-wayuu-lagoon-resettlement` |
| 7 | P116170 | dropped | `sao-paulo-metro-line-5-expropriations` |
| 8 | P082625 | dropped | `machu-picchu-pueblo-resettlement-dropped` |
| 9 | P111479 | dropped | `rio-bogota-el-porvenir-resettlement` |
| 10 | P125630 | **case** | `rio-janeiro-rail-right-of-way-removals` |
| 11 | P108654 | **case** | `pernambuco-easement-payments-undocumented` |
| 12 | P099585 | dropped | `cordoba-road-right-of-way-land-donations` |
| 13 | P143996 | **case** | `manta-properties-taken-without-agreement` |
| 14 | P083979 | **case** | `el-alto-avenue-land-paid-for-afterwards` |
| 15 | P105959 | **case** | `pinheiros-station-collapse-sao-paulo` |

Three cases rest on limb (a) with a count of people actually moved (Santos 712 families, Haiti 12
households, Rio de Janeiro 83 families). Six rest on limb (b): land taken, compensation unpaid or
undocumented, agreed benefits not delivered, or deaths. One is `documented`; the other eight are
`contested`, every one of them because the harm rests on the lender's own reporting.

Row 15 is the only `documented` case in the batch and the only one with deaths: the Pinheiros
station collapse of 12 January 2007 on São Paulo Metro Line 4, 7 killed, 99 properties affected,
12 condemned and 6 demolished, with a São Paulo state court improbity judgment published on
16 February 2024 holding six people and seven companies liable.

Row 10 (P125630) was reported in the brief as having no reachable completion report. It does have
one: the outcome document is filed under the parent operation **P111996**, whose ICR of 27 June 2023
and evaluation review ICRR0023561 were already in the cache at `cache/P111996/`. Both P-numbers are
in the lender role.

Row 15 (P105959) genuinely has no outcome document. Its only Bank document is the resettlement
plan, and the card says so.

## (a) My own two weakest entries

**1. `rio-janeiro-rail-right-of-way-removals`.** It passes limb (a) and nothing more. The completion
report gives the resettlement a single paragraph — 83 families resettled, 70 rehoused, 13 taking
cash — calls the handling satisfactory and records no complaint, no delay and no unpaid amount. The
only documented facts about the people are from the plan written twelve years earlier. The plan
counts 80 households and the report 83 families resettled, and nothing explains the gap. A checker
could reasonably say this is removal from a rail right of way handled to the lender's own
satisfaction, with no loss on top of the move, and cut it. What keeps it in: the families were
living inside the strip the project needed, on state land with no title to it, and were moved
because of the works, not for their own benefit, which is what separates it from the Bogotá hazard
relocations the map has dropped.

**2. `el-alto-avenue-land-paid-for-afterwards`.** Small, and the counts do not line up. The
completion report gives six owners on Avenida Santa Vera Cruz Tramo 1, five settled and one not;
the July 2013 plan for the same avenue gives nine properties required to pull back to the municipal
line and eight eligible after one waiver; the November 2010 plan for Avenida Litoral gives eleven.
No document reconciles them, and the Avenida Litoral plan says no valuation was ever done because
the land was treated as a return of municipal property, so there is no figure for what was taken.
The statement that the 44 shops and 54 hauliers would get no material compensation is from the plan,
not from an outcome document, so whether they lost trade is unrecorded. The one real limb (b) fact
with an outcome behind it is the single owner still uncompensated when the credits closed.

Close third: `hopewell-road-land-taken-st-vincent`. Four people, two families, and the plan leaves
every valuation as "value tbd", so the card cannot say what was offered or paid.

## (b) Did the pre-extracted briefs help or mislead?

**Helped.** The plan-reprint block did its job on Santos: it put 90,000, 2,400 and 1,100 in front of
me as figures appearing in both the appraisal document and an outcome document, which is exactly
what they are, and the outcome figure (712) is nowhere near any of them. On Haiti it surfaced the
12 households and the 11 unpaid landowners in one block. The **staff-statement bucket was the most
valuable thing in the briefs**: it caught the Haiti "the project team informed IEG that 11 out of the
19 PAPs have been compensated" and the Line 5 "the project team confirmed (email dated August 17,
2021)" before I had read either document, and both are figures that would otherwise have gone onto
a card as documentary.

**Noise.** Two buckets over-matched almost totally.

- **"death, with any cause given"** was noise on every row it fired on in this batch. Córdoba:
  national road-fatality rates in the appraisal document and a claimed *fall* in deaths in the
  completion report. Manta: a sentence about clogging and leaks "which could lead to fatal
  accidents". Bolivia: mudslides in La Paz before the project. Recife: city homicide and
  traffic-accident percentages in the appraisal document's context section. Río Bogotá: an
  occupational-health table whose own figure is **0 fatalities**, and the 2010–11 "Winter Wave". The
  one real death figure in the batch — 7 at Pinheiros — was in a row whose candidate-sentence
  section was empty.
- **"replacement cost"** fired on the policy recital, as BRIEF31 said it would, in St Vincent and
  La Guajira. The useful discriminator, from the one row where the hit was real: a replacement-cost
  sentence sitting in a completion report's **lessons or safeguards** section is worth reading
  (Manta, "the Ecuadorian national regulation does not reach the full replacement cost required by
  OP 4.12"); one sitting in a framework's legal chapter is boilerplate.
- "affected, NOT a relocation count" fired twice (Recife, Pernambuco) and was right both times.
- "PLAN VERB — the reprint trap" fired mostly on the word "envisaged" in sentences about
  restructuring, cost estimates and training, nothing to do with people.

**What the extraction should have surfaced and did not.** Five kinds of sentence, and four of the
nine cases in this batch turn on one of them:

1. **Land taken without consent or without permits.** Manta's whole case is one sentence — "Several
   properties were taken without having all the required permits or without having reached
   agreements with the owners" — and no bucket fired on it. There is no pattern for taken/occupied
   *without agreement/permit/authorisation*.
2. **Easement and right-of-way payments.** Pernambuco's case is "pending issues related to the
   documentation of the payment of easement fees for 20 landholders". "Easement fee", and
   *servidão* in the Portuguese originals, is how right-of-way compensation is described across
   Brazilian water projects and is not in the pattern set.
3. **Agreed benefits and consultation commitments not delivered.** La Guajira's case rests on "the
   municipalities/departments were not complying with the agreements established in the
   consultations" and "the communities started stalling the works because they had not received any
   of the benefits agreed on through 'Consulta Previa'". Nothing fired. Unmet *consulta previa* and
   indigenous-plan commitments have no bucket at all, and this is the limb (b) shape that recurs
   across Latin America.
4. **Retroactive compensation and "voluntary cession".** El Alto's case is "documentation of a
   'voluntary cession of land' had been planned before the PP's identification phase, but had been
   carried out after the Bank's involvement". Nothing fired; the words are *cession*, *retroactive*
   and *donation*, not *resettled* or *compensated*.
5. **Post-closing safeguards action plans.** Three of this batch's rows (Pernambuco, Santos, Haiti)
   carry their unfinished obligations into a plan that runs after the loan closes. That phrase is a
   reliable marker for unfinished compensation and should be its own bucket.

**The largest gap is language.** Row 15's brief had an empty candidate-sentence section and one
harvested document, and that document is the richest in the batch: 7 fatal victims, 8 death
indemnity agreements, 99 properties, 271 people, 12 condemned, 6 demolished. It found nothing
because the document is in Portuguese and the patterns are English. The same is true of the Rio de
Janeiro rail plan (Portuguese, where the 80-household census lives), the Riohacha indigenous
resettlement plan (Spanish, where the 110 families and 518 people live) and both El Alto plans
(Spanish). In a Latin American batch the pre-extraction is close to blind on the plans, which is
where the baseline counts are. Patterns worth adding: *reasentad*, *reubicad*, *desplazad*,
*indemniz*, *expropiac*, *afectad*, *predios*, *familias*, *viviendas*, *servidão*, *benfeitoria*,
*remoção*, *desapropriação*, *vítimas fatais*, *réinstallation*, *indemnisation*, *expropri*.

One structural point: the reprint check returned 4 flags on Santos and **0** on row 10, where the
plan/outcome pair (80 households against 83 families resettled) is precisely what the check exists
to find. It missed it because the plan is filed under P125630 and the outcome document under
P111996, so the two never met inside one row's document set. The check should run across sibling
and parent numbers.

## (c) Figures where two documents, or one document, disagree — both sides given, unreconciled

1. **Haiti, who had been paid.** The completion report (27 December 2018, §83) says eight of the 19
   landowners on the Cap Labadie road "were compensated as required" before closing and that an
   escrow account was opened for "the remaining 11". The evaluation review ICRR0021536 says "the
   project team informed IEG that since the writing of the ICR, 11 out of the 19 PAPs have been
   compensated. The Bank team is working with the authorities to compensate the remaining 8." The
   split is reversed. The review's figure is attributed to staff, not to a document, and neither
   document explains the difference. Both are on the card.
2. **Haiti, Bank performance rating.** The completion report's own KEY RATINGS page gives Bank
   performance **Satisfactory**. The evaluation review's ratings table reports the completion
   report's rating as **Moderately Satisfactory** and its own as Moderately Satisfactory, and the
   comment column says "There is no discrepancy between IEG and ICR rating." This is trap 1 from
   BRIEF20, in the same shape as the earlier Significant/Substantial case. The card states the
   report's rating from the report.
3. **Santos, how many of the 65 families were finally moved.** Footnote 13 to §61 of the completion
   report: "By the ICR submission, 62 families have been resettled to Caneleira IV Housing Complex,
   and the Bank continued to follow-up the situation of the 3 remaining households." Annex 4 §5:
   "Late 2015, around 40 families from that group were resettled to Caneleira IV (Phase 1), and in
   May 2016, the Municipality confirmed that 23 additional families had been finally resettled."
   One document, two accounts, not reconciled.
4. **Rio de Janeiro rail, how many households were in the strip.** The resettlement plan of
   September 2011 censuses 80 (59 + 7 + 14) and says the number of solutions required equals the
   number of registrations. The completion report of 27 June 2023 says 83 families were resettled.
   Unexplained.
5. **El Alto, how many owners on Avenida Santa Vera Cruz.** Completion report: retroactive in-kind
   compensation to **6** property owners on Tramo 1, five settled, one pending. Abbreviated
   resettlement plan, July 2013: **9** properties required to pull back to the municipal line, one
   owner waiving the entitlement, "los beneficiarios afectados han sido reducidos a **8**". A third
   figure, **11**, is in the November 2010 plan for Avenida Litoral. No document reconciles any pair.
6. **Río Bogotá, how many households (a drop, but the figures are on record).** The completion
   report's component description, page 12, lists "land acquisition, resettlement, and compensation
   of **188** households". Its outcome narrative gives **105** families resettled collectively and
   **19** individually, against 124 buildings in El Porvenir. The report does not reconcile 188 with
   105 + 19.
7. **La Guajira, outcome rating.** Completion report: outcome **Moderately Satisfactory**.
   Evaluation review ICRR0021445: **Moderately Unsatisfactory**, with the stated reason that
   "achievement against the project's objectives had significant shortcomings". This one is an
   explicit, reasoned disagreement rather than an unreconciled gap; both are named on the card.
8. **St Vincent, how much the loss mattered.** Remedial plan, 14 March 2013: the 3,064 square feet
   taken was "40 per cent … of the landowners assets". Completion report, 30 June 2014: the
   encroachment "did not have a substantial impact on the two affected land owners, nor on the
   community". Both on the card. Also on this row: the completion report rates risk to development
   outcome **Moderate** and the evaluation review **Significant**.
9. **Manta, which safeguards were triggered.** The completion report says the project "triggered the
   resettlement safeguard policy (OP 4.12)". The evaluation review's safeguards section lists
   OP 4.01, OP 4.09, OP 4.11 and OP 4.37 and omits OP 4.12 — then goes on to describe the
   resettlement policy framework and the properties taken.
10. **Santos, the completion report's own date.** Cover: 7 June 2016. Data sheet "ICR Date":
    23 September 2015. The card gives both.

Worth recording separately, not a disagreement: **ICIJ's 57 for Nicaragua (P127088) is to the
person the completion report's outcome figure** — "a total of 10 families (57 people) were
resettled" — and **ICIJ's 518 for La Guajira (P096965) is to the person the June 2011 plan's count**
of the population of the nine Wayuu communities in the direct area of influence. Two more worked
examples of what the ICIJ column actually contains, one an outcome and one a plan.

## (d) What could not be checked — the route that failed

- **Whether the two St Vincent land payments were ever made.** The route that failed is the
  completion report itself: it says the Bank "assisted the GoSVG" in addressing the compensation but
  never states that payment was made, gives no amount, and the remedial plan it rests on leaves
  every valuation as "value tbd" with the two land payments marked "Awaiting payment" against a June
  2013 target. The project closed in December 2013, so there is no later supervision report in the
  archive to carry the answer. Not a host failure; the record stops.
- **The amounts owed to the 19 Haitian landowners, and whether the escrow has been drawn.** No Bank
  document later than the June 2018 plan and the June 2019 review exists for P120895. The June 2018
  plan's tables give budget lines, not payments.
- **Whether the Pernambuco easement fees were paid.** The completion report's body says the
  post-closing safeguards action plan includes "the provision of the evidence of payment of these
  easement fees and the preparation of the completion reports of the 4 Abbreviated Resettlement
  Action Plans". The report's own Annex 6, "Post-Closing Safeguard Compliance Action Plan and Status
  of Implementation", lists only environmental items — dam corrective works, erosion prevention,
  slope stabilisation, greenbelt planting, effluent reuse — and no social item at all. The route
  that failed is the report's own status annex, which does not carry what its body says the plan
  contains.
- **The names of the six people and seven companies held liable for the Pinheiros collapse.** The
  São Paulo state court's public notice withholds them, and so does the press coverage found. The
  case number is on the card (0009559-70.2010.8.26.0053); the case file on the court's own e-SAJ
  portal was not opened.
- **The loan number and amount of the P105959 operation.** No appraisal document, loan agreement,
  completion report or evaluation review for it is in the cache, and the brief records that both the
  `wds?projectid=` query and the `qterm` title search returned nothing under that number. The card
  says this in `confidence_note` and gives no loan number.
- **Independent corroboration, 7 of 9 cases.** Searches outside the lender found nothing usable on
  Santos, La Guajira, Haiti, Manta, Rio de Janeiro rail, Pernambuco or El Alto. Two routes are worth
  naming rather than the hosts:
  - **IPEA's article landing page** (`ipea.gov.br/ppp/.../view/173`) serves abstract and metadata
    only for the one field study on Dique Vila Gilda, "Dique Vila Gilda: caminhos para a
    regularização", Fabiano and Muniz, *Planejamento e Políticas Públicas* 34, 2010. The abstract
    carries a 2007 COHAB-ST estimate of about 6,000 families on at most one minimum wage; the
    resettlement content, if any, is in a PDF behind a separate link that was not followed. That is
    the most promising unexhausted route in this batch.
  - **Searching the La Guajira works by name in Spanish returns the wrong project.** "Procuraduría
    pide al alcalde de Riohacha terminar obra de microacueducto", El Heraldo, 22 August 2015, is
    about a micro-aqueduct in the Wayuu Mañature resguardo under interadministrative contract
    No. 011 funded from royalties, with no Bank link, and is not the project's Maicao
    micro-aqueduct. It was checked and discarded.
  - French and Creole searches for the Cap-Haïtien–Labadie compensation returned only lender
    documents, several of them mirror copies of Bank PDFs on `ewsdata.rightsindevelopment.org`.
- Searching for the El Porvenir resettlement in Mosquera, which would have been the one thing that
  could have turned that drop into a case, returned only World Bank blog posts. The drop stands on
  the lender's own account, and the drop record says so.

## Where the document cache is

`/home/claude/work/cache/<PID>/`, as harvested before this round — nothing was re-fetched and
nothing was added. Files are plain UTF-8 text named `<TYPE>_<date>_<docid>.txt`. The P-numbers read
for this batch: P083979, P089013, P096965, P099585, P104995, P105959, P108654, P111479, P111996,
P116170, P120895, P124939, P125630, P127088, P143996. The two web pages opened — the São Paulo
state court notice and the TNH1 report on the same judgment — are cited by URL in the Pinheiros
card's `sources` and were not written to disk.
