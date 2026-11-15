# Round 32, Latin America and the Caribbean — checker's log

Checked: `/home/claude/work/out32/latam.json` (10 cases, 1 already on the map, 10 drops) against the
documents in `/home/claude/work/cache/<PID>/`, the decoded copies in `/home/claude/work/fixed/<PID>/`,
and `/home/claude/work/harvest_manifest.json`. Corrected file: `latam_checked.json`.

**Outcome: 8 cases, 12 drops, 1 already on the map.** Two of the writer's ten cases were cut. Six of
the eight kept were corrected. All ten of the writer's drops stand.

| id | P-number | checker's outcome |
|---|---|---|
| `canal-neyba-arroyo-rico-expropriations` | P109932 | kept, four corrections |
| `ceara-sanear-ii-resettlement` | P106765 | kept, one invented conflict removed |
| `skeldon-cattle-farmers-grazing-loss` | P090044 | **CUT** — lender link and timing |
| `rn34-colonia-santa-rosa-canteen-eviction` | P095569 | kept, three corrections |
| `honduras-road-rehabilitation-ii-land-taken` | P109058 | kept, plan reprint found, five corrections |
| `peru-rural-electrification-right-of-way-arrears` | P090116 | kept, absence claim refuted, title corrected |
| `colombia-water-easements-unsettled-at-closing` | P082973 | kept, nothing corrected |
| `pelotas-street-vendors-shopping-popular` | P094199 | **CUT** — figure is a plan reprint, no loss recorded |
| `dennery-embankment-land-used-without-compensation` | P111708 | kept, one correction |
| `dangriga-market-vendors-income-loss` | P111928 | kept, four corrections |

## Encoding: which files were read in which form

The writer's account is substantially right and the decoded copies are usable. Counting mojibake
markers (`Ã`, `Â`, `â€`) against real accented characters across the batch's cache directories, the
files with heavy double-encoding are: P109932 ICR (221 markers), P106765 ICR (352), P095569 IPP
(1,166) and the two RPs (1,869 and 80), P082973 ICR (339), P112074 PAD, P105288 RP, and the four
P127203 documents (314, 6,840, 3,340, 6,961). Eleven of those have decoded copies in `fixed/`. The
three the writer decoded and then deleted are consistent with what is on disk: `fixed/P094199/` and
`fixed/P109932/` are empty directories, and both P109932's ICR (221 markers against 293 real
accents) and P094199's `RP_2008-08-26_9837993.txt` (72 against 8,763) are files where decoding would
have destroyed more than it fixed. `cache/P105959/RP_2007-12-01_8985394.txt` has 14 markers against
544 real accents and was also correctly left alone.

Read in **decoded** form, via `/home/claude/scripts/g.py`, which prefers the `fixed/` copy:
P106765 ICR, P082973 ICR, P095569 IPP and both RPs, P127203 PAD and RP. The Argentine remedial action
plan `fixed/P095569/RP_2011-12-07_15569946.txt` was read whole, in decoded form, and is where the
correction to the Argentine card came from.

Read in **raw cache** form, with `sed`/`grep` directly, because they are genuine UTF-8 or plain ASCII:
all four P109932 corrective resettlement plans (0 markers, 232–460 real accents each), P109932
ICR and `RP_2010-07-01_12592077.txt`, P109058 ICR and both resettlement plans, P094199 ICR and PAD,
P111928 plan and ICR and ICRR, P111708 plan, P090044 PAD and plan, P090116 ICR and PPAR and ICRR,
P082973 PPAR and ICRR, P085539 ICR and ICRR, P089011 ICR, P112074 ICR, P127203 ICR and ICRR.

Every quotation the writer took from a Spanish or Portuguese document was checked against the correct
encoding of that file. All of them are verbatim. One attribution is loose and is now fixed — see the
Dominican entry.

## Cuts

### `skeldon-cattle-farmers-grazing-loss` (P090044) — CUT

Not on the harm, which is real and documented. On the lender link and on timing, and the deciding
sentences are all in the Bank's own appraisal document of 25 January 2008, the only outcome-side
document that exists for this number.

- **What the Bank brought.** Para 23: *"Apart from the CFU's support, the project does not include any
  World Bank or IFC financing."* The CFU support is a proposed purchase of emissions reductions by the
  Community Development Carbon Fund from the cogeneration plant. The same paragraph says the payment
  schedule would be prepared *"At the time of the signing of the Emission Reductions Purchase
  Agreement"* — so no instrument was in force when the document was written, and the cover sheet gives
  "Expected closing date: ERPA purchase concluded December 31 2014".
- **What caused the harm.** Para 49: *"Most of the adverse environmental impacts associated with this
  project are not the result of the bagasse cogeneration facility per se, but from the expansion of
  sugar cane cultivation under the SSMP."* The safeguards table the writer cites is for the SSMP, as
  the sentence above it says: *"The responses shown in the table below pertain to the SSMP."* Nothing
  in either document names a financier for the SSMP.
- **When.** Para 71: *"Block 2 has now been cleared for sugar cultivation"*; para 2257: *"Block 2 has
  recently been planted with sugar cane as part of the SSMP expansion"*; and the impoundment, *"After
  many warnings, GuySuCo finally took the step of impounding 150 heads of cattle"*, is reported in the
  past in the same document. The clearance and the impoundment were complete before the appraisal.

This is CHECK20's airport-platform test with the sign reversed: there the Bank had determined the
harm was not on an associated facility; here the Bank's own document says the harm was not on the
thing it was paying for and that it was paying for nothing else. The appraisal document also frames
the OP 4.12 case as moving cattle rather than people: *"While there is no involuntary resettlement of
people in this project, there is a need to relocate the cattle that previously had grazed on Block 2."*
The drop reason in the corrected file says what to do if a financier for the SSMP is ever found.

### `pelotas-street-vendors-shopping-popular` (P094199) — CUT

Both of the things the card rested on fail.

**`displaced: 500` is an appraisal target reprinted, and it is not a count of people removed.** The
appraisal document of 10 December 2007, in the intermediate-outcome table for Component 2, sets the
target "500 cluster firms and street vendors, 200 rural producers" for the indicator *Number of
beneficiaries of training and/or technical assistance*, with the year-five cumulative column reading
500. The completion report of 30 June 2014 reports the actual against that same row as "500 (street
vendors); 60 (rural producers); 0; 0" and marks it TARGET SUBSTANTIALLY MET. The only sentence in
the report that attaches 500 to the facility calls them beneficiaries: *"Results refer to the 500
beneficiaries of the Street vendors' facility (Shopping Popular)."* No document found attaches a
relocation verb to 500. This is the plan-reprint check returning a hit the writer did not run on this
row — their report says the check "earned its place on exactly one row, P057481".

The numbers that do carry a removal verb are in the results annex and sum differently:
*"383 peddlers and 217 walking vendors benefited. 100 of the 600 persons targeted were not removed to
the Shopping Popular since they had several stalls or changed their routes."* 383 + 217 = 600, which
is the figure the same sentence calls the target. 600 − 100 = 500 is arithmetic the report does not do.
**Left UNRECONCILED**, and not with a tidy number in `displaced`.

**No loss is recorded anywhere in the Bank record.** The completion report, the evaluation review of
22 June 2016, the loan agreement and the programme's four resettlement framework documents were
grepped for grievance, complaint, protest, resistance, coercion, eviction and informal commerce. The
only hit in the completion report is the "urban control" sentence. Everything else runs the other
way, and the writer's own card carries it: formality 50 to 70 per cent; the rent *"calculated to be
sufficient to assure the maintenance of the equipment and at the same time the viability of the
businesses of the beneficiaries"*; *"the municipality has satisfactorily relocated street vendors to
appropriate commercial facilities, not only improving their businesses"*; and the borrower's section,
the building *"allowed all walking and street vendors to move off of the streets"*. The four
resettlement documents (RP697, RP698, RP576, RP707, RP708) are a state-level Marco Conceitual and an
environmental and social management plan; none carries a Pelotas vendor count.

So limb (a) has a relocation verb with no count, and limb (b) has no documented loss. What is left is
the UFPel conference paper. I read it — the writer's characterisation is accurate: public
demonstrations, large protests around 2010, the vendors accusing the authorities of
*"intransigência e coercitividade"*, no vendor count, no income figure, no identified person. Accusations
in a paper its own authors call preliminary, against a lender record that is uniformly positive, is
thinner than the standing edge of limb (b) that BRIEF31 sets at Bukoba.

Kept in the drop reason, for whoever revisits it: the urban-control sentence is the one line in the
Bank record describing a restriction, and a Brazilian municipal source on that policy would make this
a case.

## Corrections, with both readings

### `honduras-road-rehabilitation-ii-land-taken` (P109058) — the plan reprint the writer missed

The card's whole limb (a) figure is `displaced: 3`, from the completion report of 25 November 2015:
*"In 3 cases, households were resettled in all other cases compensation was paid in an aggregate total
amount of US$0.45 million."*

**The same figure 3 is in the project's own resettlement plan of April 2008** (RP746 V.1 and the
framework V.2), as a forecast for one road: *"En el tramo de San Lorenzo – Olanchito, se prevé el
reasentamiento de 3 familias"* and *"solamente se trata de tres familias"*. The writer's
`displaced_note` says of the figure 3 only that it equals ICIJ's 3 and that "no document found
explains that". The plan does, seven years earlier.

The verb test keeps the figure alive: the completion report's verb is past and the document is the
outcome document. But the plan then cuts the other way in a detail the writer never read: of the
three families, two accepted a move to the hamlet of Santa Bárbara a kilometre and a half from La
Tejera, and the third — *"una anciana de 88 años"*, Sra. Florencia Rodríguez, represented by her
daughter Celina Rodríguez — *"prefieren recibir el efectivo por concepto de compensación y no
construir una nueva casa (reasentarlo en otro sitio)"*, preferred the cash to being resettled. So the
plan foresees three affected households and two resettlements, and the completion report reports
three resettled. **Left UNRECONCILED** in `displaced_note`, with both sides given. `displaced` stays
at 3 because the completion report is the outcome document and its verb is a past-tense relocation
verb; this is now the weakest figure in the batch and the log says so rather than tidying it.

**Limb (b), the question put to me.** Read whole, the completion report's paragraph 66 and paragraph
37 give: 201 land-acquisition cases *"identified and resolved with compensation effected in full"*;
3 households resettled; US$0.45 million paid; and *"During implementation, only minor issues were
encountered such as administrative delays in the payment of compensation to affected parties"*, with
no count of who was delayed and no duration. **Limb (b) is not met.** Land taken is on the forward
rule's list, but with compensation effected in full in every case and the delays called minor by the
only document that mentions them, there is no documented shortfall to anybody. The row survives on
**limb (a) alone** — three households resettled — and the card has been retitled to lead with that
instead of with the 201 compensated acquisitions.

Four more corrections on this card:
- **Project name.** The card said "Road Reconstruction and Improvement Project II". The report's cover
  page says SECOND ROAD REHABILITATION AND IMPROVEMENT PROJECT and its basic-information block says
  HONDURAS ROAD REHABILITATION AND IMPROVEMENT II. Corrected.
- **A missing lender.** The report's basic information lists BCIE as cofinancier, and para 15 gives
  *"co-financing of US$15 million from the Central American Bank for Economic Integration (BCIE)"*, of
  which US$14 million in Component 1 — the road works on which the land was taken — and a footnote
  says BCIE *"increased credit amount to US$22 mn based on revised estimated costs of La Esperanza –
  Camasca construction"*. La Esperanza–Camasca carries 109 of the 201 cases and is where the card's
  coordinate sits. BCIE added to `lenders` with that documented role. The report does not say which
  credit paid for any one corridor, and the card now says so.
- **The point.** The coordinate is on La Esperanza, chosen for the 109 cases. The only resettlement any
  document locates is on San Lorenzo–Olanchito. The coordinate is left where it is, since moving it
  would be my geocoding rather than a document's, and the `point` text now records the plan's location.
- **Date check.** The card dates the completion report 25 November 2015. The report's internal field
  says "ICR Date: 11/23/2015" but its **cover page** says November 25, 2015. The card is right under
  CHECK20's rule.

### `peru-rural-electrification-right-of-way-arrears` (P090116) — absence claim refuted inside a cited document

The card's `confidence_note` said the assessment report of 30 June 2017 "is the only one of the three
that visited the project **and the only one that gives the 86 and 84 per cent figures**." The second
half is false, and the refutation is in the card's own second source. Completion report of 26 December
2013, in the safeguards paragraph: *"DFC-DGER reported that 86 percent of the amount of the right of
way payments corresponding to 84 percent of the affected people had been made by July 31, 2013."*
Assessment report: *"By July 31, 2013 (one month after the closing date), DFC-DGER reported that 86
percent of the amount of right-or-way payments, which corresponded to 84 percent of the concerned
residents, had been made."* Both carry it, in almost the same words, five years apart. Corrected in
`confidence_note`, in `community` and in `outcome`. Note the unit changes between the two: "affected
people" in the report, "concerned residents" in the assessment report.

Also corrected: the title said "A Sixth of the Residents". The documents give 84 per cent paid. "A
sixth" is 16.67 and the complement of 84 is 16; neither document does the subtraction and neither
says "a sixth". Title now reads sixteen per cent, which is the subtraction and nothing more.

### `canal-neyba-arroyo-rico-expropriations` (P109932)

The strongest card in the batch. Every Spanish quotation was found and read in its paragraph; the
thirteen-plot table, the two payment tables, the 15 October 2014 second group, the 0.15 to 24.31
tareas range, the 2 February 2014 expropriation date on all seven of the first group, the five La
Gina cases with four expropriated 10 September 2013 and paid 28 October 2013 and the fifth paid 10
February 2015, the six Bonao plots with payment preceding expropriation on both groups, the pending
plot held by two brothers settled 28 December 2014, Isidro Peralta Amparo's 63 cocoa trees, the
second 63 on the Río Jayán front paid 16 March 2015, and the 75-against-150 dispute — all verbatim,
all in context. The writer's refusal to treat the two 63s as one event is right: the plan does not
say they are.

Four corrections:
1. **The quote's home.** *"Dichas expropiaciones ocurrieron, antes de otorgarles las indemnizaciones
   correspondientes a todos los propietarios de predios"* is in the **km 5.00–8.50** plan (SFG2600 V2,
   `RP_2016-03-11_26902319.txt`), where it describes what happened on **km 0.00–5.00**; the sentence
   continues *"localizados dentro del tramo del Canal Neyba Km 0.00 hasta Km 5.00"* and the next
   sentence turns to km 5.00–8.50. The card cited it to "the plan" with both plans in `sources`, which
   leaves a reader unable to find it. Now attributed and the clause restored.
2. **An absence claim that was wrong.** The `point` note said "the Neyba and La Gina plans give none"
   of coordinates. The La Gina plan gives grid coordinates for both dikes: Dique Arroyo Rico
   480995.00E / 2099931.00N, Dique Rio Jayán 481274.81E / 2100095.81N. Corrected.
3. **Half a finding.** The card said the additional financing "was approved on 17 November 2011" —
   which the evaluation review does say — and stopped there. The completion report para 1.7.3 adds
   that the loan agreement was signed 18 November 2011, that *"the loan was then terminated as a
   result of not meeting this deadline"* of 17 August 2012, and that it was reinstated with the
   effectiveness deadline extended to 16 November 2012. The instrument's own history is now on the card.
4. **Selective quotation, in the favourable direction.** The card's `displaced_note` carried only the
   plans' *"en ningún caso hubo necesidad de expropiaciones del total de predios, de desplazamiento del
   lugar"*. The completion report's Bank-performance section says the Bank team *"took rapid action
   when INDRHI was found to be in non-compliance regarding the displacement of people, an element not
   covered at that time by a Bank pre-approved Resettlement Plan"*. The lender's own two documents
   disagree on whether people were displaced. **Left UNRECONCILED** on the card, both sides given.
   `displaced` stays empty: "displacement of people" with no count is not a count.

### `rn34-colonia-santa-rosa-canteen-eviction` (P095569)

The four-page remedial action plan was read whole in decoded form. The footnote the case rests on is
exact: *"El operador del comedor fue notificado judicialmente que estaba en el DDV en 2002. Un juez
ordena el desalojo del operador del comedor en 2009. El operador del comedor se muda a Saucelito con
apoyo del Municipio."* The affected parties are named in the table: José Villarreal, the comedor
operator, and Blanca M. Chávez, owner of the depot, whom footnote 1 identifies as the widow of
Gustavo Salinas, the person originally sued. Limb (b) is met twice over — a court-ordered eviction of
a named person at a named site, and compensation to a second named person that the plan lists as an
outstanding action rather than as done.

Three corrections:
1. **A count read off the wrong rows.** The card said "In five of the eight the plan states that the
   works had already been carried out." The plan says *"La obra ya se realizó"* in **four** rows —
   cases 1, 2, 4 and 5. Case 3 reads *"Se solicitó la no ejecución de la obra por reformulación del
   proyecto"*, cases 6 and 7 read *"Reubicación futura"*, case 8 has no entry. Corrected to four, with
   the other four accounted for.
2. **A figure read off the wrong row.** The card's `confidence_note` said "the eviction came four
   months before construction of the access began". "4 meses antes del inicio de la construcción del
   acceso" is the **deadline** in the Fecha límite column for cases 6 and 7, Embarcación and Aguaray,
   for sending the Bank a final abbreviated resettlement plan. Case 5's deadline is Junio 30, 2012.
   The plan gives no date at all for the construction of the Colonia Santa Rosa access. Clause removed.
3. **Selective quotation.** The completion report's paragraph on why the six policies were activated
   says the impacts came from roundabouts requiring taking of land and *"temporary dislocation of
   settlement within the right-away"*, and then — in the same sentence, before the clause the card
   quotes — *"The impacts were minor, however"*. The card quoted the damaging half of that sentence
   and dropped the qualifier. Added to `lenders[0].role` and to `confidence_note`.

The province: the plan says *"Provincia de Jujuy, RN-34, empalme RN-50, cerca del límite con Bolivia"*
while the town of Colonia Santa Rosa is in the Orán department of Salta. The writer flagged this in
`point` but asserted Salta in `place`. `place` now carries both readings and names the plan as the
source of Jujuy. Not resolved — no document resolves it.

**`lenders[0].role` — the safeguard numbering, reported and not corrected.** Confirmed in both
documents, verbatim. Completion report, 28 March 2014: *"prompted the Bank to activate six safeguards
policies, namely: The Natural Habitats (O.P 4.04), Forest (OP 4.36), Pest Management (OP 4.09)
Physical Cultural Resources (OP 4.11), Indigenous People (OP 4.20) and Involuntary Resettlement (OP
4.10)."* Evaluation review, 5 November 2014, safeguards section: the same six with the same two
numbers. The Bank's own numbering is 4.10 Indigenous Peoples and 4.12 Involuntary Resettlement, and
4.20 was the old Indigenous Peoples number withdrawn in 2005. The card reports the documents' numbers
and names the error; left that way.

### `dangriga-market-vendors-income-loss` (P111928)

**The question put to me: does Channel 5 Belize say it, and is it independent?** It says it. Channel
5 Belize, 30 January 2014: *"The vendors continue to lose twenty-five percent of their income"* —
Mayor Gilbert Swaso. But the independence does not hold the way the card claimed it. Swaso heads the
Dangriga Town Council, which put up BZ$44,253.33 of the sub-project cost, paid the relocated vendors'
utilities and stall-fee arrears, and was one of the two parties to the evaluation the plan reports
(*"an exercise executed jointly between the PIU and the DTC"*). So the 25 per cent is one figure from
one side, published twice. `confidence_note` rewritten to say that plainly.

**`documented` is kept**, but on different ground: what the Belizean press corroborates independently
is the harm around the figure — the works stopping in September 2013, the market staying shut, the
change of contractor, the overrun to BZ$1,843,419.67, and a government minister apologising to
Dangriga residents for the delays. And limb (b) is met from the plan alone, well above the Bukoba
edge: twenty vendors named in a table, each with 26 months in the Length of Relocation column and
Moderate in the Valuation of Loss column, stall-fee arrears of BZ$24,530.00 and utilities of
BZ$14,990.68 needing to be covered, and BZ$6,955.00 reimbursed to four of them.

**Item 4 of my instructions, confirmed.** Completion report, 5 June 2017, para 39: *"Four sites
required development of Resettlement Plans. All vendors were resettled and moved to more lucrative
locations, or compensated."* Evaluation review, 5 September 2017, citing ICR para 39: *"Resettlement
plans were developed for four sites, and all vendors were resettled and moved to more lucrative
locations (ICR, para 39)."* The review drops ", or compensated" while citing the paragraph by number.
That is a finding about the review template and it holds. The review also carries a staff statement
the writer correctly labelled: *"The Bank project team confirmed to IEG that compliance with all
safeguards was achieved for all subprojects by the end of the project."*

Also confirmed: the completion report's para 39 gives Indigenous Peoples as **OP/BP 4.11**, the
physical cultural resources number, which the same report gives correctly at para 38; the appraisal
document and the review both give 4.10. Reported, not silently corrected.

Three corrections:
1. **Title.** It said "Dangriga's Market Vendors Lost a Quarter of Their Income While the Market Was
   Closed for Two and a Half Years". Two things wrong. The loss is recorded for the twenty
   **temporarily relocated** vendors; the plan's table marks the twenty parking-lot vendors "No Loss".
   And no document says two and a half years: the plan says 26 months since commencement, the works
   ran June 2012 to the opening on 23 October 2014. Retitled to the twenty vendors and 26 months.
2. **Selective quotation.** The card said "five families each lose one or more stalls to that policy".
   The same paragraph, clause (d), says temporary stalls *"will be erected in the area adjacent to the
   Cubanos to accommodate those vendors in the parking-lot who will be compensated with one or more
   stalls lost as a result of the Town Council's 'one stall per family policy'"*. The compensation
   clause was dropped. Added, in `community` and in the town council's role.
3. **A press figure rounded past its source.** "about 1.84 million Belize dollars" and "a new fish
   section". Channel 5 Belize, 23 October 2014, gives BZ$1,843,419.67 and 44 stalls for food,
   vegetable and fruit vendors plus clothing stalls; the fish section is in the plan, not in that
   article. Exact figure substituted, fish section removed from the sentence attributed to Channel 5.

The writer's "26 months" reading survives a trap worth recording. The plan's narrative gives 26
months as the **project's** duration since commencement (*"the project completion date was adjusted to
September 2014 (a total of 26 months since its commencement)"*), and the same number appears in the
table's **Length of Relocation** column against each of the twenty temporarily relocated vendors. The
table attaches it to the relocation, so the card may; but the two uses are one number and a reader of
the narrative alone would mis-attribute it.

### `ceara-sanear-ii-resettlement` (P106765) — an invented conflict removed

The case is sound. Completion report of 18 December 2012, para 38, read whole in decoded form:
*"These investments were not expected to cause physical displacement of people. However, OP/BP for
Involuntary Resettlement was triggered as a precaution. As it happened, however, the works required
for the SANEAR II program led to the resettlement of 114 families in Fortaleza and the interior of the
state."* Outcome document, people-bearing unit, past-tense relocation verb. The writer's absence
claim checks out: the resettlement framework of 14 March 2008 does not contain the string 114, so the
figure is not an appraisal estimate reprinted. The appraisal document's *"Only very limited involuntary
resettlement is expected to occur under the water and sanitation component"* is at para 73, verbatim.
The safeguard list of three policies is complete — para 32 names those three and nothing more.

Removed: the card said the review "gives the risk as Negligible to Low where the report says Low or
Negligible". Those are the same rating with the words in a different order. The review's ratings table
prints Negligible to Low in **both** columns and records no disagreement. That is CHECK20's invented
conflict and it is out.

One quote the card normalises silently and I have left alone: *"The SWAP II loan will continue
supporting the 'Projeto Sanear II'"*. The cached text of the appraisal document reads *"The SWAP 11
loan will continue supporting the 'Projeto Sanear I.'"* — OCR damage to the roman numerals, which the
writer repaired. Substantively right; worth knowing the quotation is not byte-exact.

### `dennery-embankment-land-used-without-compensation` (P111708)

Every quotation exact and every favourable clause already on the card, including the owners' agreement
that the project will benefit them and their eagerness *"to see the works extended and completed as
far in advance as possible before this year's June storms"*. The named family, the named site, the
land built on *"without consent or compensation"* with only coconut trees paid for, and the
contractor's statement that the government *"would expropriate the necessary land with or without
their consent"* — all verbatim. Strongest limb (b) in the batch. 6,039 m² of 19,895.77, 30 per cent,
180 metres, the Mirai contract at EC$6,683,042.53: all confirmed.

One correction: the card said the second contract went "to a contractor it identifies only as HES".
The report names it in full — *"awarded to Hippolyte Equipment Services (HES)"* — and gives its
completion as 30 July 2007. Corrected. The Government of Saint Lucia press release resolves (200) and
says what is claimed: US$7.5 million, IBRD loan of US$3.7 million and IDA credit of US$3.8 million,
Second St. Lucia Disaster Mitigation Project, 7 February 2005.

### `colombia-water-easements-unsettled-at-closing` (P082973) — nothing corrected

Checked hardest of the eight because the writer named it near-thinnest, and it held. The completion
report's sentence is exact and its surrounding paragraph is on the card both ways: the final report
concluding that the ministry's own activities were complete and *"a high percentage of cases were
resolved"*, footnote 6's 80 of 103 parcels and 1,093 of 1,177 easements, and then *"The SRAP, however,
is not complete as the resettlement of two families in the Municipality of Neiva and the legalization
of 23 parcels and 84 easements are currently in progress."* The review's restatement is exact. The
POAD spelling in the review's safeguards sentence is the review's own, not the writer's.

The writer's absence claim about the Project Performance Assessment Report is correct and I verified
it by grep across the whole document: para 4.21 repeats 80/103 and 1,093/1,177 and the words "a high
percentage of cases were resolved", and the strings "23 parcels", "84 easements" and "Neiva" appear
nowhere in it. The rating divergence is also exactly as reported — the PPAR's own table for this
project gives Moderately satisfactory / Moderately satisfactory / **Moderately unsatisfactory** across
ICR, ICR Review and PPAR, with risk Moderate / Moderate / Substantial.

Limb (b) is met, just: compensation unresolved in 107 counted cases at closing, documented by the
lender's own review, plus two families at a named municipality. The counted cases have no named site
and the named site has no completed harm, so this sits on the Bukoba edge from the other direction.
Kept.

## The already-on-map call (P105959) — the key cannot collide

Confirmed, and the mechanism is stronger than the writer's note claims.

`normalise.py` lines 89–101 read each row's `status` first. `already_on_map` and `already-on-map` are
routed into a `mapped` list carrying `key`, `file`, `pid`, `case_id` and `note`, and then `continue` —
the row never reaches the case path, the extend path or `merge.py`. The dict key is only ever used as
a label in that list. The `if is_extend and 'id' not in rec: rec['id'] = key` line that would promote
a key to an id is below the `continue` and is unreachable for this row.

Two further locks. The row carries no `id` field at all, so nothing could be written under the live
id even if it reached `merge.py`. And `merge.py` line 22 is `if c['id'] in ids: print('skip dup',
c['id']); continue` — a row carrying an id already on the map is skipped, not merged, so a live card
cannot be overwritten by a stub by this route in any case. `pinheiros-station-collapse-sao-paulo`
appears twice in `base.html`; `p105959-already-on-map` appears nowhere in it. No collision is possible.

## P127203 Haiti — the drop tested on both of its legs, and it stands

**The cause.** Completion report of 29 July 2021, paragraph 99, read whole with paragraphs 96 to 100:
the Bank was informed of *"a fatality of a member of the contractor's team installing solar lighting on
the Champ de Mars which had occurred in August 2019 during the 'Peyi Lock' period when civil
disturbances led to many casualties"*, and *"The team's assessment was that the incident was not
project-related, but rather a direct consequence of civil unrest, and that the contractor had
undertaken mitigation measures to the extent possible under the circumstances."* The evaluation review
of 7 February 2022 repeats it: *"The team concluded that the incident was a direct consequence of civil
unrest."* No document gives any other cause. Under BRIEF31's rule the death is uncounted.

**Which credit paid.** This is the leg the writer did not test and it comes out the other way from the
cause. The works were this credit's. Completion report: *"the project funded the construction of a
solar power plant (110kW photovoltaic coupled with a lithium-ion battery to pilot the power storage
from the PV plant) to secure the lighting of the Champ de Mars"*; the outputs annex lists
*"Construction of a 100 kW Photovoltaic Power Plant at the Champ de Mars"* and *"Acquisition,
Installation and Maintenance of Champ de Mars Lighting equipment, including 210 plaza lights, 120
streetlights, and 20 projector lights"* under Component 1; and annex 9 is headed SOLAR
ELECTRIFICATION OF THE CHAMP DE MARS IN PAP WITH THE SUPPORT OF THE PRELEN PROJECT. The only
co-financier named anywhere in the report is the French Development Agency, on a different operation.

So the first test — did the credit pay for the works the person died on — is **met**, and only the
second, whether a cause ties the death to the works, fails. That is the right outcome for the row and
the wrong reason was nearly given for it: the writer's drop reason says the cause "leaves nothing else
attached to it", which is true, but the drop rests on the cause alone and not on the works being
somebody else's. The corrected file keeps the writer's drop and this log records the distinction so a
future round does not re-litigate the wrong leg. If a Haitian source ever gives a cause tied to the
installation work, the row is a case against this credit.

The gender-based violence item is correctly dropped: *"the Bank's management decided not to take
action because the alleged incident could not be confirmed"*. The three occupational health and safety
events at Drouet were *"all classified as indicative"* — improper lubricant storage, improper use of
removed sediment, and a third — with no injury to anyone.

## The other nine drops — spot-checked, all stand

- **P085539 Limón.** The nearest of the nine to a keep, and the only one I hesitated on. The completion
  report of 24 December 2014, paragraph 32, read whole: *"For the planned sewerage and drainage
  component, there were a total of 19 resettlement cases, 11 for sewerage and 8 for drainage, 18 of
  which were concluded by Project closure, and the remaining one in August 2014."* Nineteen is a real
  resettlement count in an outcome document, so what decides the drop is the unit and the absence of a
  loss: "cases" is not people, households or families, the verb is "concluded", and nothing in the
  report, the review or the draft plan records compensation withheld, a livelihood not restored or a
  destination. If a Costa Rican source ever puts a loss against those cases, revisit it. The safeguard
  divergence the writer reports is real: report *"Cultural and Physical Property (OP 11.03)"*, review
  *"Physical Cultural Resources (OP 4.11)"*.
- **P089011 Uberaba.** Confirmed at paragraph 32: *"Apart from the administrative time and effort in
  preparing and processing the necessary paperwork, there was no real impact of this retrofitting
  process on Project implementation."* The one contested expropriation in the retroactive plan is of
  part of a university campus — a legal entity, not people.
- **P112074 Sergipe.** Confirmed at paragraph 67, read whole: *"It did not cause any involuntary
  resettlement of beneficiaries"*, the areas were *"partial portions of empty land, without
  houses/residences or other improvements, productive /commercial use or other livelihoods"*, and
  *"All areas were acquired and compensated before the beginning of the works and in compliance with
  OP 4.12."* The framework's 366, 96 and 28 families are pre-existing irregular settlements, which is
  the correct reading.
- **P086775 Camalotales, P091299 Knollis, P105288 Buenos Aires, P057481 Uruguay, P078220 Amoyá,
  P080093 Sibimbe** — drop reasons read against the documents they name; each says what was found in
  the outcome document, or says that no outcome document exists and what was searched instead. That
  satisfies CHECK31's requirement, which is the one BRIEF22 had let writers skip. The two carbon-finance
  rows (P078220, P080093) would have failed on the lender link in any case, for the same reason
  P090044 now does.

## 1. What I could not check, named as a route

- **The UFPel conference paper, `cti.ufpel.edu.br`.** A plain `curl` with and without a browser
  User-Agent returns **403 with a 15,604-byte HTML interstitial from a "safeline" web application
  firewall** — not a 404, not a host refusal, and the PDF is really there. The WebFetch route returned
  the document's contents and confirmed the writer's reading of it. So: the curl route fails, the
  WebFetch route works, and the citation is sound but not machine-fetchable. Moot now, since the
  Pelotas row is dropped, but the route finding is worth inheriting.
- **The P090044 completion report.** None exists in the cache or the manifest for the Guyana carbon
  project, so nothing records what happened at the Manarabisi pasture, whether the move to Sookram's
  Pasture happened, or whether the impoundment fines were refunded. Under the instruction not to
  re-fetch Bank documents I did not go looking, and the row is dropped on other grounds.
- **The two scanned plans the writer names** (P080093 RP338, P057481's March 2005 plan). I did not
  re-test them; the writer's account — the Bank `/txt/` route returning 357 and 1,030 bytes because the
  archive copies are scans — matches what those files hold on disk. OCR over the PDFs is the route that
  would settle them and neither drop turns on it.
- **The French volume of the Haiti completion report** (`ICR_2021-07-29_33407968.txt`, 5,701 real
  accents, genuine UTF-8). I read the English volume. I did not read the French end to end; I checked
  it for "Champ de Mars" and "fatality" equivalents and found the same material. If it carries anything
  the English does not, it is unread.
- **`cache/P127203/AGR_2017-12-22_29500994.txt`** is 146 bytes against a 894 KB PDF. The text route
  produced nothing for that agreement. It bears on nothing kept or dropped.
- **Which road corridor the three Honduran households were on.** The completion report does not say.
  The April 2008 plan locates its forecast three on San Lorenzo–Olanchito. No route closes the gap.
- **Where in Peru the unpaid residents are.** Confirmed as the writer reports: the completion report,
  the review, the assessment report and the framework are all national in scope. The coordinate sits on
  the ministry directorate's seat in Lima with `point` saying it is not a site of the harm. That is
  honest but it does put a harm pin on a ministry; whether the map should carry a case it cannot place
  is the owner's call, not mine, and I have left it.
- **The Argentine court order.** No case number in any document, so there is nothing to search a
  provincial court index for. Confirmed by reading the plan whole: the footnote gives the year and
  nothing else.

## 2. Figures where documents disagree, left unreconciled

Carried forward from the writer's list, each verified in both documents:

1. **P109058 Honduras, how many households were resettled.** Completion report, 25 November 2015: *"In
   3 cases, households were resettled."* Resettlement plan, April 2008: *"se prevé el reasentamiento de
   3 familias"* on San Lorenzo–Olanchito, of whom two agreed to move and the third asked for cash
   instead. **New this round, and the most consequential figure in the batch.** On the card.
2. **P109932 Dominican Republic, whether anyone was displaced.** Completion report: the Bank acted on
   INDRHI's *"non-compliance regarding the displacement of people"*. Corrective plans: *"en ningún caso
   hubo … desplazamiento del lugar"*. **New this round.** On the card.
3. **P090116 Peru, how many were late paying.** Completion report: *"two distribution companies were
   late"*. Assessment report: *"Two of the nine companies, however, fell behind … (Electrocentro and
   Hidrandina)"*. Review: resolved *"except for right-of-way payments for three sub-projects"*. Two
   companies against three sub-projects — different quantities, so possibly both true; neither document
   says so. Verified.
4. **P090116 Peru, the outcome rating, three ways.** ICR Moderately Satisfactory; review Satisfactory,
   its table giving the reason *"The ICR used the cumulative rating categories incorrectly"*; assessment
   report satisfactory with risk negligible. Verified in all three.
5. **P082973 Colombia, the outcome rating.** ICR and review Moderately Satisfactory, no disagreement
   recorded; PPAR Moderately unsatisfactory with risk Substantial. Verified in the PPAR's own table.
6. **P109932, the restructuring date.** ICR body *"restructured in November 2010"*; ICR key-dates table
   10/01/2010; ICR Table 1 October 1, 2010; review October 1, 2010. Verified — the ICR disagrees with
   itself, which is sharper than the writer's framing of report against review.
7. **P109932, the social commission's visit to La Gina.** The same plan, the same paragraph:
   *"en visita realizada en fecha jueves 11 de diciembre del 2014"* and *"días 9, 10 y 11 de diciembre
   del año 2015"*. Verified verbatim.
8. **P111928 Belize, the cost of the market.** Plan BZ$1,519,364.33 for the sub-project of which
   BZ$1,475,111.00 from the loan; Amandala the second contract alone at BZ$1,228,310.95 against an
   original BZ$1.4 million; Channel 5 Belize BZ$1,843,419.67 final with about BZ$800,000 to the first
   contractor. Verified in all three.
9. **P111928, the first contractor.** Plan *"Mr. Smart"*; Amandala Kenard Smart of K & G Construction;
   Channel 5 Belize Kenard Smart of Corozal. Verified.
10. **P094199 Pelotas, the vendor counts.** 383 + 217 "benefited" = 600; "100 of the 600 persons
    targeted were not removed"; "the 500 beneficiaries". Verified. Row dropped; the conflict is in the
    drop reason, unreconciled.
11. **P085539 Costa Rica, one safeguard policy.** Report OP 11.03 Cultural and Physical Property;
    review OP 4.11 Physical Cultural Resources. Verified.
12. **P095569 Argentina, two policy numbers wrong in both documents.** Verified verbatim in both, and
    reported on the card rather than corrected, as instructed.
13. **P111928, one policy number.** Report para 39 Indigenous Peoples as OP/BP 4.11, against its own
    para 38 and the appraisal document and the review at 4.10. Verified.
14. **ICIJ's number equalling a document's number against a different unit, three rows.** P106765 ICIJ
    114 against 114 families; P109058 ICIJ 3 against 3 households; P090116 ICIJ 2 against 2 families.
    All three checked. No document explains any of them, no conversion was made on any card, and in all
    three the card's figure comes from the Bank document and not from ICIJ. For P109058 the coincidence
    is now three-way, because the April 2008 plan carries 3 as well.

**One conflict removed as invented:** P106765's review "Negligible to Low" against the report's "Low
or Negligible" is one rating written two ways.

## 3. Faults appearing in more than one card

1. **The favourable clause in the same sentence, dropped.** Three cards: P095569 (*"The impacts were
   minor, however"*), P111928 (the parking-lot families *"will be compensated with one or more stalls"*),
   P109932 (the plans' no-displacement sentence carried without the report's "displacement of people").
   In every instance the clause sits in the sentence or paragraph the card already quotes. This is the
   fault both briefs name first and it is still the batch's most common.
2. **The plan-reprint check run on one row and not on the rest.** The writer's report says the check
   "earned its place on exactly one row, P057481". It also fires on P094199 (500, a target in the
   appraisal table and an actual in the same row of the completion report — fatal to that card) and on
   P109058 (3 families, forecast in the April 2008 plan and reported in the 2015 completion report —
   the batch's weakest surviving figure). Both were there to be found: both figures sit in the project's
   own documents, not in a sibling's.
3. **An absence claim that the cited document refutes.** Two: P090116 ("the only one that gives the 86
   and 84 per cent figures" — the completion report gives them too) and P109932 ("the Neyba and La Gina
   plans give none" of coordinates — the La Gina plan gives two sets). Both were one grep away in a file
   already open.
4. **A figure or a date read off the neighbouring row of a table.** P095569's "four months before
   construction" came from the deadline column of two other cases; P095569's "five of the eight" came
   from counting rows loosely. Tables in these plans put each case's data on several physical lines and
   the columns do not align in the text extraction, which is where this fault comes from — it is a
   mechanical risk and not carelessness, and it argues for reading a table by printing the whole block
   rather than grepping a value out of it.

## 4. Wrong in the card data, outside what I was asked to check

- **`lenders` was short a lender on P109058.** BCIE co-financed US$15 million rising to US$22 million,
  US$14 million of it in the component that did the road works, and the report names it as cofinancier
  on its basic-information page. Added. Three other kept cards name a second lender correctly
  (P106765's Inter-American Development Bank, P111708's IBRD-and-IDA split).
- **The project name was wrong on P109058.** "Road Reconstruction and Improvement" for "Road
  Rehabilitation and Improvement" / "Second Road Rehabilitation and Improvement Project".
- **A company named less fully than the document names it**, on P111708: HES is Hippolyte Equipment
  Services and the report says so twice.
- **`companies` on P109058 names one of two implementing agencies.** The report's basic information
  gives *"Implementing Agencies: INSEP and Fondo Vial"*; the card has INSEP only. Not an error — the
  land acquisition is INSEP's and the card says so — but worth knowing.
- **A harm pin on an administrative seat**, P090116, flagged in `point`. Noted above; left for the owner.
- **Naming practice is inconsistent across the batch.** The Dominican card names Isidro Peralta Amparo
  and the Belize card names twenty vendors and five families, all from public Bank documents; the
  Argentine card declines to name José Villarreal and Blanca Magdalena Chávez, who are named in the
  same kind of document. Either practice is defensible; both in one batch is not a rule. Left as the
  writer had it, since narrowing is the safer direction.
- **`ecosystem` on P109058** (the Refugio de Vida Silvestre Colibrí Esmeralda, US$1.8 million of Spanish
  debt-swap grant, the disbursement condition lifted in March 2012) was spot-checked against the report
  and is sound.
- **Voice.** Clean. A regex for I, we, our, my, us, "this card", "this entry", "the draft", "the writer"
  across every prose field and every lender and company role on all ten submitted cards returned zero
  hits. Against the 24 instances in one earlier round's ten merged cases, this is the regression closed.
- **URLs.** All 42 source URLs were HTTP-checked. Forty-one answer 200: 38 Bank PDFs with
  `content-type: application/pdf`, the Government of Saint Lucia page, both Channel 5 Belize archive
  pages and the Amandala page. Every Bank URL matches a `pdfurl` in `harvest_manifest.json` by its
  `/curated/en/...` path, and every `date` on a Bank source matches that document's `docdt` in the
  manifest — no constructed URLs and no dates off a filename. The one non-200 is the UFPel paper
  described above. The writer rewrote the manifest's `documents.worldbank.org` host to
  `documents1.worldbank.org`; that is the resolvable form and all 38 prove it, but it is a
  transformation of the manifest value and worth stating.
- **Press content verified, not assumed.** All three Belizean articles were opened and their load-bearing
  sentences checked: the 25 per cent quotation and the road-works money in the 30 January 2014 piece;
  CB Construction, BZ$1,228,310.95, 24 March 2014, Kenard Smart of K & G Construction, the original
  BZ$1.4 million, the September 2013 extortion allegation, the four dismissals and the denials in
  Amandala; and the opening date, 44 stalls, BZ$1,843,419.67, the BZ$800,000 and Minister Santiago
  Castillo Jr.'s apology in the 23 October 2014 piece.

## 5. Routes that failed, named as routes

One, and it is not a host refusal: **`curl` to `cti.ufpel.edu.br` over HTTPS returns 403 with a
"safeline" web application firewall interstitial**, with and without a browser User-Agent, while the
WebFetch route to the same URL returns the document. The host serves the file; one client route is
blocked. Nothing else failed. Every Bank document this check needed was on disk, every URL resolved,
and no permission prompt was raised.

## Whether the briefs helped or misled — the checker's view

**CHECK31's central instruction was the one that paid.** "The fault to expect this round is not a
missed document. It is a grep hit used without being read in context." Every correction in this log
came from printing the whole paragraph or the whole table block around a sentence the writer had
already quoted correctly. Not one came from finding a document the writer had not opened.

**The plan-reprint section earned more than the writer credited it with.** The writer's report says it
fired on one row; it fires on three, and one of the three (P094199's 500) kills a card. The brief told
the writer to check the verb; what it did not say, and should, is that the figure may be a target
rather than a forecast — "500 cluster firms and street vendors" in a results-framework target column is
not the kind of sentence either brief's examples prepare you for, because the examples are all
resettlement plans with household counts. The sharper instruction is: for every figure on a card, open
the appraisal document's results framework and look for it in the target column, not only in the prose.

**BRIEF31's withdrawal of the screening instruction was right and it shows in this batch.** The ten
drops are all argued from outcome documents, and the two rows a mechanical screen would have thrown
away — P109932, whose completion report says the project did not expect to trigger either social
policy, and P111708, whose harm is in one meeting record and nowhere in a results table — are two of
the three strongest cases here.

**Where the briefs under-prepared the writer: tables.** Four of my corrections come from the same place
— a value read out of a table without the whole block printed. These documents' tables survive text
extraction as columns that do not align, with one case's data spread over four or five physical lines
and the neighbouring case's deadline sitting directly above the value you want. The writer's own report
asks for a pattern over paired date columns; the instruction a checker actually needs is simpler:
**never take a number out of a table by grep — print the block from the header row to the footnote.**
Both of the batch's keeps that turn on a table (Belize's twenty vendors, the Dominican payment dates)
are right, and both of the table-reading errors are in the one card where the writer worked from grep
hits.

**And one thing in the briefs that could have caused a wrong drop, which the writer is right about.**
The "What to decide" paragraph's only worked example of limb (b) is housing demolished with an
enterprise column. On this batch nothing is demolished, and a writer following that example alone
would have dropped Belize, Saint Lucia, Peru and Colombia. The worked examples this material needs are
a payment dated after a taking, land occupied and not paid for, and a court-ordered eviction in a plan
footnote — all four of which this batch supplies.
