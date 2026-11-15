# Check log — round 31, batch `west_central_africa`

Checked: `/home/claude/work/out/west_central_africa.json` (8 cases, 6 drops, 1 already-on-map)
against the documents in `/home/claude/work/cache/<PID>/` and the briefs in `/home/claude/work/briefs/`.
Output: `/home/claude/work/out/west_central_africa_checked.json`.

**Outcome of the check: 1 case cut, 7 kept with corrections on all 7. Every one of the 6 drops
confirmed; 2 of them had a clause added. `killed` went from 5 to 0.**

No document was re-fetched. Web use: HTTP HEAD on all 24 source URLs (all 200). No new web research
was needed to decide anything, because nothing in the batch turned on a non-lender source; all 8
entries were already `contested` and stay so.

---

## 1. The case that was cut

### `kimbanseke-inga-kinshasa-line-pending-compensation-claims` (P097201) → **dropped**

Deciding sentence, Independent Evaluation Group review ICRR0021847, section 10a:

> "The ICR provides little detail on the status of compliance with individual safeguard policies.
> However, it indicates that at project closing, all triggered safeguards were rated Moderately
> Satisfactory, but there were several pending social and safeguard issues relating to dam safety,
> the arrangements to get rid of hazardous materials linked to the control of the black fly nuisance,
> and claims from Kimbanseke project-affected persons (PAPs). SNEL did confirm that the rehabilitation
> of the people affected by the construction of the second Inga-Kinshasa T-Line was completed, and
> there was agreement with stakeholders on how to close the process (the line would not be put into
> operation until the payment process was concluded)."

Limb (b) is not met. The harm is a pending claim of unstated content: no count, no sum, no date, no
statement of what any claimant lost, and the same sentence records the rehabilitation of the people
affected by that line as complete. Kimbanseke is a commune of Kinshasa of over a million people, not
a site. BRIEF31 fixes the floor at `bukoba-airport-resettlement-arrears` — compensation unpaid in
five identified cases at a named site — and says anything thinner is not limb (b). This is thinner on
both counts: no count of cases, and no site.

**What was checked in the outcome material before cutting, and what it holds.** The project's own
completion report is not reachable on any route tried, so the review is the only account of it. Beyond
the review:

- The appraisal document's 270 households for the transmission line and 129 for the distribution works
  are what the project *expected* to affect; the writer had already kept them out of every numeric
  field, correctly.
- The April 2011 resettlement plan filed under this project (RP1135 v2) is a **late plan and worth
  reading in full**, on the `xining-wusixi-road-demolition` precedent. It records in the past tense
  that 229 families were censused at the affected sites, 211 in Kinshasa with the largest number in
  Kimbanseke commune, split 43 resident owners / 137 non-resident owners / 49 tenants or rent-free
  occupants, and that the compensation amounts were negotiated and the agreements on them formalised.
  Every loss in it carries a future verb: 141 houses and 1,537 fruit trees "will" be destroyed,
  US$2,315,477 is the total "provided for", and the plan's execution is a nine-month programme still
  to run. Its cover reads "Projet de Plan" — a draft.
- **A rescue is available and was not taken, because it would be the checker's claim.** Reading the
  2011 census of 229 families with agreed compensation amounts together with the 2018 pending claims
  would put this at or above the Bukoba edge. Neither document refers to the other, and nothing in
  either says the pending claims are those families'. That join is an inference, and a tidy join of
  two documents needs a source that makes it. The owner may want to look at this one again if the
  project's completion report ever becomes reachable, because that report is where the join would be
  made or refused.

The writer named this entry the batch's weakest and wrote that a checker who cut it would not be wrong
to. The dropped card is preserved under `dropped_card` in the drop record, so nothing is lost; it must
not be merged from there.

**Citation error found in it:** the source was titled "Plan de réinstallation du MEADE". The document's
own cover reads **PMEDE** — Projet de développement du Marché d'Électricité pour la consommation
Domestique et à l'Exportation. It is this project's plan, not another project's, so the fact is right
and the citation was unusable as written.

---

## 2. `killed` — the figure this round turned on

### `abidjan-lagos-corridor-road-works-deaths-and-late-compensation` (P116323): `killed: 5` → **`killed: 0`**

Both tests in the brief fail, and they fail separately.

**Test 1, a document cause tying the death to the works.** The five deaths appear twice in the
completion report and nowhere else.

- Paragraph 62: "Component B of the project was suspended between December 2016 and June 2017 because
  of serious occupational safety and road safety issues on the road works that resulted in 22
  accidents, including five fatalities in 6 months".
- Paragraph 71 (the safeguards section, read in full): "There were **at least** 22 accidents, including
  five fatalities, that had not been properly reported to the World Bank, and some of which had led to
  protests from local communities."

The report gives a collective cause — safety failures on the works — and no cause for any individual
death. It does not say which of the dead were workers and which were road users; "road safety issues"
and "occupational safety" are run together in one clause. It names nobody. And paragraph 71's "at
least" makes the figure a floor, which under CHECK20's inexact-figure rule puts it in `killed_note`
by itself. There is no health-and-safety annex with a different number: the two sentences above are
every mention of an accident or a death in the 51-page report, and the Evaluation Group's review only
repeats them, citing the report's paragraph 72 for what is in fact paragraph 71.

**Test 2, which credit paid for the works.** Footnote 6 to the project description: "Of which IDA will
finance only the Aboisso-Noé section (about 59.2 km)." The rest of the Component B road corridor,
including the Grand-Bassam–Aboisso section, was financed by the government's counterpart funds, which
were 41 per cent of Component B at appraisal and 31 per cent at closing; paragraph 74 records that
"the procurement of works financed by the counterpart funds suffered even greater challenges and
delays", and names the Grand Bassam–Aboisso contract among them. The report never says which section
the accidents were on. So the document cannot place the deaths on works this credit paid for.

**The title was also corrected.** It read "Five deaths on the Aboisso-Noé road works" — the document
places the deaths on "the road works", not on a named section, and naming the IDA-financed section was
the one attribution the document does not support. New title: "Late compensation for 2,411 people and
a safety suspension on the Grand-Bassam–Aboisso–Noé road works".

**Verified as instructed: the review's platform explanation was not used.** The review says "According
to the information provided by the team, a platform refers to land that was built into a market for
the relocated traders", and separately attributes its physical-cultural-resources finding to the same
source. Neither is on the card. The card's platform sentence — 8,800 m², the Noé Traders Management
Committee created by Ministerial Order in June 2019 — comes from the completion report's own
paragraph 70. The writer's `confidence_note` already said so, and it is true.

---

## 3. Figures left UNRECONCILED

### (a) P116323, the length of the suspension — **five figures, four of them inside one document**

The writer reported this as completion report "seven months" against review "eight months". It is
worse than that, and all of it stays on the card:

| Figure | Where |
|---|---|
| "suspended for seven months in 2017" | completion report, efficiency section (twice, paragraphs cited as the seven-month figure) |
| "suspended between December 2016 and June 2017" | completion report, paragraph 62 |
| "the team worked closely with the client for almost 8 months in view of..." | completion report, paragraph 77 — this is the period of work to lift it, not the suspension |
| "the long suspension of disbursements (8 months)" | the **borrower's own report printed in the same completion report** |
| "The suspension was lifted after eight months"; "partial suspension of disbursements for eight months in 2016" | review ICRR0021995, sections 10a and on efficiency |

No source reconciles them. The card now gives all of them and reconciles nothing. Note that the
review's second form dates the suspension to 2016 while the completion report dates the seven months
to 2017.

### (b) P110020, how many of 639 were paid — **inside one document.** Confirmed exactly as the writer
reported it, and this is the batch's sharpest finding. Main text paragraph 34: the plans "provided
compensation to all 639 persons affected by temporary closures causing loss of income due to works at
these sites. No other safeguard actions were required and the rating of safeguards had been
satisfactory throughout the project." Borrower's annex paragraph 50: "A total of 629 PAPs have been
compensated to the amount of FCFA 857,568,478 for a total of 639 PAPs identified. It remains to
reimburse the salaries of 10 store employees affected by the Riviera 2 constructions due to technical
unemployment, for whom salaries were pre-financed by employers, who have however failed to produce
documentary evidence of this pre-financing to justify their refund." Neither passage mentions the
other. The review repeats the main text.

### (c) P084002, how much was paid. Completion report: 88 per cent of 585 as of 31 January 2016, CFAF
401 million, "88 percent of the total amount due". Review: "The Task Team Leader clarified that 95%
compensation has been made to date." Confirmed, and correctly handled on the card as a staff statement
to the evaluators rather than a document.

### (d) Ratings, each read from the document that gave it. All confirmed:
P116323 Moderately Satisfactory / Moderately Satisfactory (completion report paragraph 47 — the
paragraph number on the card is right, and the review's own cross-reference to "paragraph 48" is the
one that is wrong). P110177 Satisfactory (paragraph 46), no review. P084002 Moderately Satisfactory /
Moderately Satisfactory, risk High both. P110020 Highly Satisfactory (calculated at 7.76) against
Satisfactory. P104497 Satisfactory / Satisfactory. P082725 Satisfactory / Moderately Satisfactory.
P129713 Moderately Unsatisfactory (paragraph 47) / Moderately Unsatisfactory.

### (e) A rating disagreement **inside a completion report**, reported only by the review (P097201).
ICRR0021847: "there is a disconnect between the ratings for Outcome and Bank Performance in the Data
Sheets of the ICR (page 3) and those in the main text. The Data Sheets indicate Moderately
Satisfactory for both criteria, whereas the main text assign ratings of Moderately Unsatisfactory for
Outcome (paragraph 75) and Bank Performance (ICR, paragraph 124)." The card is dropped, so this is
recorded here only. The same review also says the completion report names four triggered safeguard
policies and that "a comparison with the PAD reveals that these were the only four that were actually
not triggered."

### (f) An invented conflict I looked for and did **not** find.
The P110177 approval date: the completion report's data sheet and its body both give 11 November 2011;
ICIJ's lead row gives 10 November. Document against ICIJ lead row is not two documents disagreeing,
and the card uses the document. Correct as written.

---

## 4. The plan-reprint call, card by card

The briefs returned `reprint_flags: 0` for every row in this batch, so the mechanical check did no
work here and could not be relied on. It was run by hand on every figure in `displaced`,
`displaced_label` and the `community` prose.

| Card | Figure | Result |
|---|---|---|
| P116323 | 2,411 / 2,256 / 155 | **Not a reprint.** Grepped the appraisal document and both resettlement plans: zero hits for 2411 or 2256 in any of them. The figures are in the completion report (paragraph 70) and the review only. The verb is "affected"/"were compensated", which is why nothing went in `displaced`. |
| P116323 | ICIJ's 692 | **Traced to the plan.** It is the exact total of the October 2011 plan's census table (Tableau 2: 692 persons recorded, of whom 13 households and 677 managers of economic activities), and the same plan says the census "identified a total of 695 people who will have to vacate the works right of way" — future tense. The card carried **no `displaced_note` at all**, the only card in the batch without one. One has been added, giving ICIJ's figure, its origin in the plan's table, and the fact that no outcome document counts anyone relocated. |
| P110177 | 23 families | **Not a reprint.** "23 families" appears in no document in the cache but the completion report (paragraph 70 of the M&E section). Verb: "the 2012 AMR highlighted the **physical resettlement** of 23 families". Outcome document, people-bearing unit, relocation verb. `displaced: 23` stands. |
| P104497 | 72 households, 245 people, 30/23/19 | **Reprint, and the writer's own prose had already half-caught it.** All of these are the June 2010 resettlement plan's summary table — including "Nombre de ménages ayant perdu leur logement: 23", a past participle in a plan written seven months before the works started in January 2011. The completion report **does carry 72 and 245**, one paragraph from the outcome, but attached to something else: "A total of 72 heads of households received training on how to use their compensation for income-generation activities, benefiting 245 people in the affected households." That is training, not relocation. The card correctly had no `displaced`; its **title** read "Seventy-two households lose land, houses and crops", which presents a plan count as an outcome, and has been changed. The `displaced_note` now states the reprint and what verb the report attaches. |
| P082725 | none | No count of households or people in either document. Nothing to check. |
| P129713 | 15 | **Not a reprint, and it is the real thing.** The June 2021 implementation report for the Kananga MONUSCO erosion works records payment on 16 June 2021 to one household head counted as 15 affected persons, US$5,650 in all (US$4,000 house, US$1,600 trees and family crops, US$50 to one person assessed as vulnerable), "100 % du total prévu au PSR"; the commission then asked him to vacate the old house and occupy the new one, "ce qui fut fait"; and the conclusion says "cette réinstallation s'est faite avant que l'ancienne maison de la PAP ne soit detruite". `displaced: 15` stands. Only the label was wrong — it said resettled *at* Avenue Lithanie, which is where they were moved *from*. |
| P129713 | 1,078 / 1,041 | Completion report paragraph 74, confirmed verbatim. Not in `displaced`; "identified through RAPs" and "compensated". Correct. |

---

## 5. Corrections, by card, with both readings

### `abidjan-lagos-corridor-...` (P116323)
1. `killed` 5 → 0 (above).
2. Title (above).
3. `displaced_note` added (above).
4. **The Ghana plan's 38 was a future-tense count given as a count.** Card read "counted 38 affected
   household heads". The plan's Table 1 reads "Total Affected Household **Heads/PAPs who will be
   losing** Structures and Crops — 38". Corrected to the document's wording, with the plan's total
   valuation added (GH¢389,513.95 / US$88,525.90) and the fact that payment is the Government of
   Ghana's responsibility, the Ministry of Finance having already released the funds to the Ghana
   Highway Authority pending the Bank's approval of the plan.
5. **"nothing had changed on the ground as of December 2017" was ambiguous to the point of reversing.**
   On the card it sat after the sentence about payment delays and read as "no payment, no progress".
   What the plan says is that site visits on 27–29 November and 5 December 2017 found no new cocoa
   trees or other crops planted and nothing changed on the ground since the cut-off date — the
   right-of-way is frozen — "however, the planting of crops around the houses have been going on with
   agreement of PAPs until they receive the compensation." Both halves are now on the card.
6. `outcome`: "Moderately Unsatisfactory for a long stretch of implementation" → the report's own
   "during a significant period of implementation"; added paragraph 71's clause that some of the
   accidents "had led to protests from local communities", which the card had dropped.
7. The real limb (b) on the Ghanaian side is intact and now stated plainly: cut-off 19 October 2015,
   "the PAPs have already stopped farming after the notification of the cut-off date", plan still
   awaiting Bank approval in December 2017, consultations "to update the PAPs on the delay".
8. Confirmed and unchanged: IDA H7870, SDR 57.9m / US$90m, approval 31 May 2012, actual closing
   29 March 2019 (data sheet); 2,411 / 2,256 / 94 per cent / 155; FCFA 3.6bn, 3.5bn, 98 per cent,
   FCFA 56m escrow; Port-Bouët, Samo, Assouba, Aboisso, Noé; 8,800 m² platform; Ministerial Order
   June 2019; 113.59 km against 130.3 km; nine-point action plan; the implementing-unit history,
   including the transfer to the PRICI unit on 30 November 2016 (paragraph 60); the borrower annex's
   "preserves the activities of the people affected by the project" and the defective Noé parking lot.

### `kribi-gas-plant-land-and-crops-taken-mpolongwe` (P110177)
1. **Wartsila's role overstated.** Card said it "supplied the gas engines for the 216 MW plant". The
   report says Wartsila "was the only bidder to propose a detailed binding offer for a larger plant
   size" and offered the lowest cost, and that "the choice of gas engines was made on the basis that
   the bidder (Wartsila) made an optional binding offer". Who supplied the engines is not in the
   report. Corrected to the document.
2. **Which credit paid for the Bipaga works, and when.** The access road was built for SNH's own
   Sanaga-Sud pipeline project and paid for out of SNH's budget under Prime Ministerial Decree
   2010/2341/PM; the payments were made on 23 September and 3 December 2010, a year before the Bank's
   Board approved the guarantee on 11 November 2011. The link holds, because paragraph 73 brings the
   onshore gas pipeline inside the project: "The scope of the update ESIA included the power plant,
   associated facilities such as the transmission line, substation, marine and onshore gas pipelines
   as well as the Sanaga South gas field." All of that is now on the card instead of implied.
3. Confirmed unchanged: guarantee G-2090, up to CFA 40 billion / US$82 million, approval 11 November
   2011, effective 23 August 2012, closed 2013 against an original 2016 ("Actual closing date was
   modified to fit completion of the underlying investment"), outcome Satisfactory at paragraph 46;
   Category A and the five policies as the report lists them (the report itself misnumbers Physical
   Cultural Resources as OP/BP 4.12 — the card names the policies without numbers, so nothing carried
   over); Siemens France with KEC India as preferred bidder for the 225 kV line and 11/225 kV
   substation EPC; the Bipaga figures (24 people paid for crops; 5,543 m² / FCFA 27,715,000, 846 m² /
   FCFA 8,460,000, 1,360 m² / FCFA 6,800,000 under titles 2089/0, 3768/0, 1671/0; houses at market
   economic value, mostly temporary materials; payments by cheque and in cash; "le processus a été
   participatif et pacifique" and "ces compensations se sont déroulées de manière pacifique et à
   temps, aucune contestation y ayant trait n'a été enregistrée"); the noise paragraph with **both**
   halves, including that the baseline levels were also above the recommended levels. The absence
   claims were tested: the whole 41-page report contains no instance of accident, injury, death,
   Bakola or Bagyeli, so "records no deaths" and "gives no outcome for those communities" hold.
   `displaced: 23` stands.

### `pdue-cameroon-unpaid-compensation-yaounde` (P084002)
1. **A clause in the same paragraph that cuts the other way was dropped.** Paragraph 37 continues:
   "In practice though, as noted in supervision reports, the PCU had complied with the policy's
   requirements through consultations on the project' benefits." Added.
2. "Two payments for Yaoundé" → the report's own "two for Yaoundé were still awaiting the presidential
   clearance at the time of this report". The antecedent in that sentence is "Payments", so the
   writer's reading is the natural one, but the document does not say "payments" in the clause and the
   project also had decrees awaiting legal clearance; the card now tracks the sentence.
3. `killed_note` was empty; filled with the absence, checked.
4. Confirmed unchanged: credits IDA-43130 and IDA-48200, which the conformed agreements in the cache
   title C4313-CM and Credit 4820-CM as the card gives them; SDR 53.3m / US$80m and SDR 18.9m /
   US$28.7m from Pilot Crisis Response Window resources; approval 29 May 2007, actual closing
   31 August 2015; 585 affected, 88 per cent at 31 January 2016 against 51 per cent at closing,
   CFAF 401m, "88 percent of the total amount due"; MU on OP 4.12 in early 2014 and at closing; the
   Presidential Decree step; Phase 2 plans approved end-2014; "remains of utmost importance"; the
   Inclusive Cities Board condition; the TTL's 95 per cent handled as a staff statement.

### `abidjan-riviera-2-shop-workers-unpaid-wages` (P110020)
1. **The title and `outcome` said the workers went unpaid. The document says the opposite.** The annex
   says the ten employees' "salaries were pre-financed by employers"; what remains outstanding is the
   project's reimbursement, and the annex's reason is that the employers "failed to produce documentary
   evidence of this pre-financing to justify **their** refund". So the party out of pocket is the
   employers. This is the same fault class as round 22's Nigerian `displaced: 675`, which counted
   people who moved a business rather than a home. Title changed to "Ten of 639 affected people at the
   Riviera 2 underpass left out of the compensation, Abidjan"; `outcome` and `confidence_note`
   rewritten to say who was owed what. The case is **kept**: ten of 639 identified affected persons at
   a named site were not compensated under a Bank-required resettlement plan, which is limb (b) in the
   Bukoba form, and the body of the card already had the mechanism right.
2. **Two counter-clauses from the same annex were dropped.** Paragraph 50: "For these cases the
   coordination unit has ensured that Project-Affected Persons (PAPs) were duly compensated."
   Paragraph 49: "An environmental and social review mission recruited in 2012 confirmed compliance
   with project safeguard instruments." Both added.
3. The review's rating: the card said the Evaluation Group rated it Satisfactory "finding minor
   shortcomings". The review's "minor shortcomings" attaches to efficacy against the original and
   revised objectives, not to the outcome rating. Left as a rating of Satisfactory; this is the kind
   of noun-slippage CHECK20 names, and it is small enough here to note rather than rewrite.
4. `killed_note` filled.
5. Confirmed unchanged: grants IDA-H3970 and IDA-H5910, which the conformed agreements title H397-CI
   and H591-CI as the card gives them; SDR 57.10m / US$94m and SDR 33.10m / US$50m including SDR 9.93m
   / US$15m Pilot Crisis Response Window; approval 12 June 2008, closing 31 March 2014 against
   15 September 2012; review Date Posted 04/20/2015; the four plan sites; MACOM's role and the
   January 2009 recruitments; FCFA 857,568,478.

### `kinshasa-water-works-land-and-houses-taken` (P104497)
1. Title (above): plan counts were presented as an outcome.
2. `community` now says in terms that every count of people is the June 2010 plan's, written before
   the works began.
3. **A counter-clause in the same paragraph was dropped.** Paragraph 42: "The Bank Task Team and
   management actively monitored the issue and ensured that no construction works took place prior to
   the completion and disclosure of the safeguards instruments." Added beside the 13-months point.
4. "9,306 square metres of surface area" → the plan's "perte définitive d'espaces cultivables",
   permanent loss of cultivable land, 517 market-garden beds.
5. `displaced_note` extended with the reprint finding (above). `killed_note` filled.
6. Confirmed unchanged: grants IDA-H2820 and IDA-H5960, titled H282-ZR and H596-ZR in the conformed
   agreements as the card gives them; SDR 120m / US$180m and SDR 26.5m / US$40m from the Crisis
   Response Window; approval 29 March 2007, closing 31 May 2013 against 31 May 2011; review Date
   Posted 07/29/2014; both Satisfactory; the four sites; the plan's 41/7/5/19 split and 30/23/19
   breakdown; 72 fruit trees and 3 cassava gardens; works awarded November 2009 and started January
   2011 "due to time taken to agree on who should pay compensation to project affected persons...
   and clear the sites"; US$1,215,322 in cash indemnities and the Bank's waiver of its own bar on
   cash compensation because "the government did not have funds to pay the compensations"; the NGO
   and the 72 heads of household trained; "fully complied with".

### `takon-landfill-land-taken-porto-novo` (P082725)
1. **The title asserted a shortfall neither document states.** "paid for in buildings not money"
   carries an implication of compensation below entitlement; both documents say the project complied
   and that resettlement plans were prepared and carried out before civil works began. New title:
   "Land acquired from the Takon community for the Porto-Novo landfill, compensated in buildings and
   services".
2. **`outcome` moved a finding to the wrong time.** Card: the landfill "was not fully functional when
   the evaluation review was written". The review says "some infrastructure (notably the Takon solid
   waste landfill) still not fully functional **by project closure**". Corrected.
3. `killed_note` filled.
4. Confirmed unchanged: credits IDA-41170 and IDA-44900, titled C4117-BJ and C4490-BJ in the conformed
   agreements as the card gives them; SDR 24.00m original and SDR 48.30m revised; approval
   12 September 2005, closing 29 June 2012 against 30 June 2010; review Date Posted 09/16/2013;
   Satisfactory against Moderately Satisfactory; the CFA 830 million and the list of measures
   (paragraphs quoted verbatim); the 10 per cent and 15 per cent counterpart shares and the
   8 July 2011 reallocation; the results-framework comment "For the Takon community whose land was
   officially acquired for the construction of the landfill", which is what carries limb (b) here;
   the operator's contract signed six months after closing and the procurement-board delay; the
   footnote "Resettlement was not planned during Phase 1. However, some resettlement activity took
   place without a resettlement framework being in place", correctly attributed to the programme's
   first phase.
5. **This is now the batch's weakest keep** and the owner should see it as such. The harm is land
   acquired from a community that no document counts, compensated in kind in full, on a project both
   documents rate compliant. It stands only because the forward rule lists "land taken" flatly.

### `drc-urban-project-injury-threats-and-works-before-resettlement` (P129713)
1. **`lenders[0].role` carried two garbled financing numbers.** Card: "IDA grant H842-0" and "credit
   6034-0". The completion report's cover reads IDA-H8420 and IDA-60340; the project's own works
   contract for the Kananga site heads itself "ACCORD DE DON N° H8420-ZR ET ACCORD DE FINANCEMENT
   N° 6034-ZR", and the additional-financing agreement in the cache is titled "Credit 6034-ZR".
   Corrected to H8420-ZR / 6034-ZR with the report's cover forms given.
2. **The role gave half the scope history.** It said the scope was cut from nine cities to four. The
   report records six at appraisal (Bukavu, Kalemie, Kikwit, Kindu, Matadi, Mbandaka), nine with the
   additional financing (adding Goma, Kisangani, Kolwezi), then four in the 2020 restructuring
   (Bukavu, Goma, Kikwit, Matadi), with Kananga added afterwards. Corrected, and the four cities named.
3. **`place` omitted a project city.** Kalemie was missing from a list of nine. Added.
4. **"The remaining 37" is a figure the report does not print.** 1,078 − 1,041 is the checker's and
   the writer's arithmetic. The report says the rest "did not present themselves to receive
   compensation" and gives the reserved sum of US$18,984. The card and `outcome` now say that and no
   longer state a count.
5. Footnote 6 to paragraph 75 names the city: "Which is the reason that no infrastructure was financed
   by the PDU in Goma." Added.
6. Kolwezi: the card gave "sums of US$50 and US$100" as examples. The mission report's table totals
   US$1,195 for the 13, of which US$150 is assistance to people counted as vulnerable, and it carries
   a GPS point for each of the 13. Added.
7. Kananga: the financial table is headed "Synthèse des données financières relatives à la gestion des
   fonds pour paiement des PAP omises" — funds for paying affected people who had been **left out**.
   Added; it puts Kananga and Kolwezi in the same class of finding.
8. `displaced_label`: "resettled at Avenue Lithanie" → "resettled from Avenue Lithanie".
9. `suppression` said the review "gives the same account". It does not, quite: the completion report
   says the complainant "was allegedly subsequently threatened by provincial authorities"; the review
   says "a complainant reported being threatened by the provincial authorities", without the
   qualifier, and it divides the three non-compliance cases differently — counting works started
   before contract signature and works started before the resettlement plan as two separate cases,
   where the report counts two cases of works before the plan, one of them also before signature.
   Both differences are now on the card.
10. Confirmed unchanged: SDR 66.1m / US$100m and SDR 66.5m / US$90m; approval 9 May 2013, actual
    closing 30 July 2021; US$190,000,000 → US$108,159,215; Moderately Unsatisfactory both; Category B
    and the three policies; 1,078 / 1,041 / US$155,918 / US$18,984; 41 complaints all closed; 79
    occupational health and safety incidents, 75 indicative, three serious, one severe fall from
    height reported through ESIRT with documentation of treatment and full recovery; the three
    non-compliance cases; the Mbandaka episode and everything the Bank did about it; the 13 named
    people on Avenue Gazumbu, the 2016 consultant's finding of no affected people, the absent cut-off
    date and absent signage, and the mayor's office's readiness to pay; the Kananga payment in full
    (US$5,650 = 4,000 + 1,600 + 50 on 16 June 2021, 100 per cent of the plan), the city hall / project
    split, the household vacating before demolition, "s'est globalement bien déroulée et sans
    incident", and the grievance registers at the town hall and in Mulombodi quarter with the
    mechanism running from 19 June 2021.

---

## 6. Every drop, checked

All six confirmed. None of the six rests on a null sentence from a plan; every one names an outcome
document, a paragraph and what was found there, which is what BRIEF31 asks for. Two had a clause added.

| Row | Verified against | Verdict |
|---|---|---|
| **P112573** Urgent Electricity Rehabilitation, Côte d'Ivoire | Completion report ICR3428 paragraph 68, read whole. Confirmed verbatim: 22 of 89 subprojects needed plans "covering about 200 persons"; "the resettlement aspect was related mainly to the impact on street vendors and artisans along the routes where the underground lines were replaced, as well as acquisition of land for small substations"; plans "successfully completed". The 2012 plan's falling counts confirmed (39 against 82 at the Azito resettlement site; Yopougon gare attributed to "l'opération ville propre" of the Ministry of Urban Sanitation). | **Drop confirmed.** The one thing worth recording: the paragraph does mention "acquisition of land for small substations", with no site, no count and no person, which is below the limb (b) floor. The Azito subproject serves a site where people evicted earlier had been resettled — those evictions are not this credit's. |
| **P100160** Emergency Infrastructure, Liberia | Completion report ICR2630 paragraphs 37, 43, 84. Paragraph 37 confirmed verbatim, including "In spite of this, it is considered that overall safeguard compliance was satisfactory". Paragraph 84: "Funding for resettlement was made available in a timely manner." The July 2008 plan's 99 households confirmed as "those individuals living within the area to be cleared of refuse **who will be displaced**" — future tense in a plan. | **Drop confirmed, with a clause added.** Paragraph 43 of the same report: "the solid waste activities were curtailed after they exceeded the intermediate outcome and have been continued under the Bank funded EMUS Project". That is the documentary reason the Whein Town landfill harm does not attach to this credit, and it corroborates the press attribution the writer declined to use. **Lead for the main session, not a change here:** the Emergency Monrovia Urban Sanitation project (P115664) is in the cache and is where that harm would be tested. |
| **P095003** RAMP 2, Nigeria | Completion report paragraphs 57–60, read whole, and the review's safeguards section. Paragraph 57 confirmed verbatim, including "with 2,423 affected persons compensated for a total amount of Naira123,528,553" — all paid. The shrine finding does exist in the review only as what "the project team subsequently informed IEG". | **Drop confirmed.** I agree with the writer's treatment of the two kidnappings of contractor staff in Osun and Niger states between February and April 2019: harm to identifiable people by third parties, not harm caused by the lending, and not in the forward rule's list. The owner may want to look again, because it is a specific documented harm on project sites; it is a judgement, not an error. Also recorded by the report itself and not used: Annex 8 marks a long list of this project's resettlement plans "Not found on WB external website". |
| **P105654** Southern Africa Power Market additional financing, DRC | The June 2008 updated compensation and resettlement plan (RP770) and the January 2008 study. Every figure the writer quoted confirmed in place and in verb: "SNEL promises to compensate", USD 1,042,482 overall, USD 463,345.00 for crops, "approximately USD 230 per square meter", "individuals (or households) would be affected over a total cultivated area of 172 ha", "the number of farmers that could be affected", "since they know they will be relocated within the village, none of them feel dispossessed", "in 2008, the people met with as part of the updated study are still confident about the compensation process". | **Drop confirmed.** The route failure is stated correctly and as a route: no completion report and no assessment report under this number by either the projectid query or a title search; the sibling P097201's review reviews that project's own report. Nothing was written from the sibling. |
| **P084022** Local Authorities Development, Senegal | Completion report ICR2982 paragraphs 34–36, read whole, and the review (Date Posted 03/24/2015). Confirmed verbatim, including "a few simplified resettlement plans were also produced" and, for the inter-communal investments, that the recommendations were "approved by the Bank, implemented and monitored as appropriate". | **Drop confirmed.** Neither document counts one person affected, relocated or paid, names a site, or records an injury, arrest, death or unpaid sum. |
| **P072644** RAMP 1, Nigeria | Review ICRR0020754, whole safeguards section. Confirmed verbatim, including "The process did not affect the progress of the works. The PAPs were compensated." | **Drop confirmed, with a clause added.** The writer's reason leaned on the staff statements; the sentence immediately after the environmental one reads "An independent audit did not reveal issues or concerns on compliance with safeguard policies", so the review does not rest on staff statements alone. Added, because it makes the drop stronger and the reason as written slightly overstated. |

### The already-on-map row
**P095091 Mali** → `mali-office-du-niger-hamlets`. Confirmed, and I went looking for the opposite. The
review's safeguards section carries four findings beyond what the writer's note lists — infrastructure
built to the plan that "did not comply with national standards", the grievance mechanism not following
Bank standards with no report of its implementation available, the Bank's recommendation to the client,
and "it remains unclear whether the Client took the necessary actions recommended by the Bank or not" —
and the existing case on the map already carries every one of them, plus the 3 hectares against 5, and
already cites this review as a source. The writer's "adds nothing" is right. No extend.

---

## 7. Patterns — faults appearing on more than one card

1. **A clause in the same paragraph cutting the other way, dropped: four cards** (P084002 paragraph 37,
   P110020 annex paragraphs 49 and 50, P104497 paragraph 42, P116323 paragraph 71's protests). In
   every case the dropped clause was favourable to the lender, which is the direction CHECK20 says it
   always runs. None of the four changed an outcome; all four are now on the cards.
2. **A plan figure presented in an outcome voice: three cards** (P104497's title, P116323's Ghana 38,
   and P116323's missing `displaced_note`). The mechanical reprint check returned zero for every row
   in this batch and would have caught none of them, because none of these is a figure reprinted in an
   outcome document — two are figures taken straight from a plan with the plan's verb stripped, and one
   is an absent note. **The check as built looks for the wrong shape.** The shape that bit here is a
   plan figure quoted *as a plan figure* and then titled as a result.
3. **A figure derived by arithmetic the document does not do: one card** (P129713's 37). Small, but it
   is the same class as a reconciliation.
4. **`lenders[0].role`: one real error in eight cards, not the 19-in-46 rate.** Only P129713's
   financing numbers were wrong. I started to report a pattern of truncated credit numbers across six
   cards — H397-CI, 4313-CM, H282-ZR, 4117-BJ, H296-ZR — and then checked the conformed financing
   agreements in each cache: those are the Bank's own forms, from the agreements' own titles. **The
   pattern was mine, not the writer's**, and an invented pattern is the same fault as an invented
   conflict. Worth recording because the next checker will see the same shape. The one thing that is
   genuinely loose: the credit-number forms come from conformed agreements that are not in any card's
   `sources`, though the IDA-xxxxx forms are in the completion reports that are.
5. **Report-number cross-references inside the Bank's own documents are unreliable.** The P116323
   review cites the completion report's paragraph 72 for what is paragraph 71, and cites paragraph 48
   for the outcome rating that is in paragraph 47. The P097201 review says the completion report names
   four triggered policies that were "the only four that were actually not triggered". Every rating and
   paragraph number on these cards was read from the document that gave it, which is why none of this
   got onto a card.

---

## 8. Anything I could not check, named as a route

1. **The writer's working notes.** My task names `/home/claude/work/out/_notes.md`. That file does not
   exist, and no file anywhere under `/home/claude/work` mentions this batch other than the batch input,
   the output and the report. The writer's working notes for this batch are inside
   `west_central_africa_report.md`. Everything my task quoted from "the notes" was found there and has
   been checked. Failed route: the named path, not a missing step by the writer.
2. **No completion report for P097201, P105654 or P072644, and no evaluation review for P100160 or
   P110177, in the harvest.** Each is recorded on the drop or the card. I did not re-run the Bank
   queries, as instructed; so I am confirming the writer's route findings, not independently
   reproducing them. The one I can corroborate from the cache: P097201's review is present under the
   title-search route and no completion report is, which matches what the writer reported.
3. **The dates of five Evaluation Group reviews are not on the documents.** The newer IEG template
   (2016 onward) carries no date and no "Date Posted" line anywhere in its text: verified for
   ICRR0021995 (P116323), ICRR0021847 (P097201), ICRR0022973 (P129713), ICRR0020199 (P084002),
   ICRR0020754 (P072644) and P112573's and P095003's reviews. Their dates on the cards come from the
   Bank document library's own `docdt` field, recorded in `harvest_manifest.json` at harvest — **not**
   from a filename or a URL, which is why I have not "corrected" them: they are the publisher's date
   for the document, which is what a `sources` date is for. They are the publisher's date and not
   something the document says, so they are left as they stand on every card, in `sources` and in the
   prose that cites a review by number and date, and nothing was changed on that account. Recorded here
   so the next checker does not take a day-precision review date for something read off a cover. The
   older template does carry the line, and those four were read off it: 09/16/2013, 07/29/2014,
   04/20/2015, 03/24/2015.
4. **No independent corroboration exists for any of the seven cases**, so all seven remain `contested`
   and each `confidence_note` says who is reporting on whom. I did not re-run the writer's six searches;
   the two near-misses they describe (the ACP report on Kinshasa ring-road expropriations, the Oyono
   open letter on gas prices) are plainly off-subject as described, and spending searches to re-find
   nothing was not worth the budget against reading the documents.
5. **No host refused a request.** The 24 source URLs all returned 200 on a HEAD request through the
   proxy. The one dead page the writer reported — the suspended `newspublictrust.com` article — bears
   on a dropped row and on a landfill the completion report assigns to a different credit, so nothing
   on any card depends on it.

---

## 9. Did the pre-extracted briefs help or mislead?

I used them only to find the documents, and for that they were right every time: paths, document-type
tags and the second project numbers all matched what was on disk, and the one route note I could test
(P097201's review reachable only by title search) matched the cache.

**As an aid to reading they are worse than useless on this batch, and the writer's account of why is
accurate and I can add to it.** The single most serious fact in the batch — "22 accidents, including
five fatalities in 6 months" — *was* surfaced, as the sole hit in the brief's "death, with any cause
given" bucket. But the brief's truncated snippet stops mid-sentence, and the sentence it stops in is
the one that says "the accidents were reported to the World Bank" where the report means the opposite
(paragraph 71: "had not been properly reported"). A writer working from the snippet rather than the
file would have taken the Bank's own framing backwards. The snippet also carries the paragraph-62 form
of the figure and not the paragraph-71 form, and the difference between them — "22 accidents" against
"at least 22 accidents" — is what decides whether the figure can be counted at all. **A brief that
quotes one of a document's two statements of the same figure makes the inexact-figure rule
unenforceable from the brief.**

The other buckets, confirmed as noise exactly as the writer describes: "compensation unpaid or late"
fired three times on P116323 and all three are useless — twice on the same delay table's phrase "long
administrative procedures for the compensation of PAPs" (the same text, extracted twice from two
printings of one table), and once on the Ghana plan's statement that funds had already been released.
"replacement cost" fired on the Ghana plan's policy recital. "PLAN VERB" fired on the project's theory
of change ("the project envisaged to capitalize on"). On P112573, both of the two hits are irrelevant.

**What the extraction missed, each of which decided something here:**

1. **Borrower-written annexes.** The ten at Riviera 2 exist only in the borrower's annex to the
   completion report; so does P116323's third figure for the suspension length, "(8 months)", which
   changes a two-document disagreement into a four-way one inside and across documents. No candidate
   sentence in any of the fifteen briefs came from an annex.
2. **Reports of *carrying out* a plan, filed under the plan tag.** P129713's brief tagged 22 documents
   `RP`; two of them are outcome documents (the June 2021 Kananga implementation report, which carries
   the batch's only valid `displaced`, and the February 2019 Kolwezi mission report). The brief's
   `relocation_counts_in_outcome_doc: 0` was wrong for that row as a result. A title pattern on "mise
   en œuvre", "rapport de mission" or "rapport de mise en oeuvre" would catch them.
3. **Counts in table row labels.** P104497's whole 72/245/30/23/19 structure is in a summary table
   ("Nombre de ménages ayant perdu leur logement: 23"), and so is P116323's 692 — which is ICIJ's own
   figure, sitting in a plan's census table. **If the extraction read plan summary tables, the ICIJ
   figure could be traced to its source document automatically on a large fraction of rows**, which is
   worth more than any of the harm buckets: it is the check the `displaced_note` rule exists to make,
   and it was done by hand on two rows here.
4. **The financing footnote.** Footnote 6 of P116323 — "Of which IDA will finance only the Aboisso-Noé
   section" — is half of the test that moved `killed` from 5 to 0, and no bucket would ever surface it.
   A bucket for sentences that limit what the credit financed ("only", "financed by the counterpart",
   "not an associated facility") would be worth more than the police and replacement-cost buckets put
   together.

**On the plan-reprint check:** zero flags on all fifteen rows, so it did no work and could not be
tested — and section 6 above explains why it would not have caught the three plan-voice faults that
were actually here. The check looks for a figure in two documents. The fault is a figure in one
document and a verb from nowhere.

---

## 10. For the owner

- **Weakest keep:** `takon-landfill-land-taken-porto-novo`. Land acquired from a community that no
  document counts, compensated in kind in full, on a project both documents call compliant. It stands
  only because the forward rule lists "land taken" without qualification.
- **Second weakest:** `abidjan-riviera-2-shop-workers-unpaid-wages`, now that the ten are correctly
  described. Ten of 639 affected people at one named site were not reimbursed, the party out of pocket
  is their employers, and the two halves of the one document that says so contradict each other.
- The dropped Kimbanseke card is preserved under `dropped_card` in its drop record. It must not be
  merged from there; it is kept only so the April 2011 plan finding is not lost if the project's
  completion report ever becomes reachable.
