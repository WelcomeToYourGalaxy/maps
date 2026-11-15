# Round 31, batch `west_central_africa` — writer's report

Fifteen rows worked. Outcome counts: **8 new cases, 6 drops, 1 already on the map, 0 extends.**

Output: `/home/claude/work/out/west_central_africa.json`.
Document cache used, not re-fetched: `/home/claude/work/cache/<PID>/` (plain-text completion
reports, evaluation reviews, appraisal documents, resettlement plans and conformed agreements for
all 15 projects). Web searches spent: 6 searches and 3 page fetches, all on sources outside the
lender. None of them produced a usable corroboration, so **all 8 cases are `contested`**.

## Row by row

| P-number | Project, country | Outcome | Reason in one line |
|---|---|---|---|
| P112573 | Urgent Electricity Rehabilitation, Côte d'Ivoire | dropped | 22 resettlement plans "covering about 200 persons", street vendors and artisans, plans "successfully completed"; no relocation count, no recorded loss |
| P116323 | Abidjan-Lagos Trade and Transport Facilitation APL-2, Côte d'Ivoire | **case** `abidjan-lagos-corridor-road-works-deaths-and-late-compensation` | Five deaths and 22 accidents on the road works in six months; 2,411 affected, 155 never reached, works ran ahead of the resettlement plan |
| P110177 | Kribi Gas Power, Cameroon | **case** `kribi-gas-plant-land-and-crops-taken-mpolongwe` | 23 families physically resettled (2012 monitoring report via the completion report); land and crops actually paid for at Bipaga, with amounts and dates |
| P084002 | Urban and Water Development Support (PDUE), Cameroon | **case** `pdue-cameroon-unpaid-compensation-yaounde` | 51 per cent of 585 affected people paid at closing, 88 per cent five months later, two Yaoundé payments still unpaid; resettlement policy rated Moderately Unsatisfactory |
| P110020 | Emergency Urban Infrastructure, Côte d'Ivoire | **case** `abidjan-riviera-2-shop-workers-unpaid-wages` | Borrower annex: 629 of 639 paid, ten shop employees at Riviera 2 still unreimbursed for lost wages |
| P100160 | Emergency Infrastructure, Liberia | dropped | One case of OP 4.12 non-compliance on the Mesurado River; works stopped before anyone was moved; the 99 households are a draft plan figure |
| P095003 | Rural Access and Mobility Phase 2, Nigeria | dropped | 2,423 affected and all compensated, late; the review states the consequence as project delay and closing-date extension |
| P105654 | Additional Financing for Southern Africa Power Market APL1, DR Congo | dropped | No outcome document on any route; every figure in the 2008 plans carries a future-tense verb |
| P084022 | Local Authorities Development Program, Senegal | dropped | Both documents report compliance and count nobody — not one person affected, relocated or paid |
| P095091 | Fostering Agricultural Productivity, Mali | already on map | `mali-office-du-niger-hamlets`; the evaluation review adds nothing the existing case lacks |
| P097201 | Regional and Domestic Power Markets Development (APL-1b), DR Congo | **case** `kimbanseke-inga-kinshasa-line-pending-compensation-claims` | Claims from Kimbanseke affected persons still open at closing; the second Inga–Kinshasa line held out of service until payment concluded |
| P104497 | Emergency Urban and Social Rehabilitation (PURUS), DR Congo | **case** `kinshasa-water-works-land-and-houses-taken` | 72 households, 245 people, lost land, houses or crops at four Kinshasa water sites; US$1,215,322 paid after the Bank waived its cash-compensation rule |
| P082725 | Second Decentralized City Management (PGUD2), Benin | **case** `takon-landfill-land-taken-porto-novo` | Land taken for the Takon landfill, paid for in CFA 830 million of buildings and services; landfill not operating at closing |
| P129713 | Urban Development Project, DR Congo | **case** `drc-urban-project-injury-threats-and-works-before-resettlement` | Works started before resettlement twice, one severe fall-from-height injury, a complainant in Mbandaka allegedly threatened by provincial authorities; one household of 15 resettled at Kananga |
| P072644 | Rural Access and Mobility (RAMP I), Nigeria | dropped | Only the evaluation review is reachable and its compliance findings are "the Bank team informed IEG"; the people left out of the plan were paid and the works were not delayed |

## (a) My own two weakest entries

**1. `kimbanseke-inga-kinshasa-line-pending-compensation-claims` (P097201) — the weakest.**
The project's own completion report is not reachable; the Independent Evaluation Group's review is
the only route, and that review itself says the completion report "provides little detail on the
status of compliance with individual safeguard policies". The entire harm is one clause in a list of
pending issues: "claims from Kimbanseke project-affected persons (PAPs)". There is no count, no
names, no sum, no date for the claims, and no statement of what any claimant lost. The same
sentence carries two clauses that cut the other way, both of which the entry gives: SNEL confirmed
the rehabilitation of people affected by the second Inga–Kinshasa line was complete, and there was
agreement with stakeholders on how to close the process. It is at or just past the Bukoba edge, and
a checker who cuts it will not be wrong to. The appraisal's 270 and 129 households are kept out of
every numeric field because they are what the project *expected* to affect.

**2. `takon-landfill-land-taken-porto-novo` (P082725).**
It rests on limb (b) through "land taken", with no count of households or people anywhere in either
document — the affected are described only as "communities whose land was acquired". The harm is
inferred from an accounting fact: the government spent CFA 830 million of its counterpart money on
compensation it had not budgeted for, and so could not fund its share of the credit. Both documents
also say in terms that the project complied with all safeguard requirements and that resettlement
plans were prepared and carried out *before* civil works began, which the entry gives. The footnote
about resettlement in Phase 1 happening "without a resettlement framework being in place" belongs
to the programme's first phase, a different credit, and is reported as such.

Two others worth the checker's attention. On `abidjan-lagos-...-deaths-and-late-compensation` the
`killed: 5` is the one judgement call in the batch: the completion report says the five deaths
"resulted" from occupational safety and road safety issues *on the road works*, which states a
cause, but it does not say which of the dead were workers and which were road users, and names
nobody. If the checker reads that as unseparable from road-user deaths, the figure belongs in
`killed_note` and `killed` goes to 0. On `kinshasa-water-works-land-and-houses-taken` the
compensation was in the end paid in full and the completion report concludes the policies were
"fully complied with"; the entry stands on land and houses taken, which the forward rule lists, not
on a payment failure.

## (b) Did the pre-extracted briefs help or mislead?

**They helped on routing and hurt on reading.** The paths, the document type tags and the dates were
right every time, and the time that would have gone on finding documents went on reading them
instead. Two specific gains: the briefs flagged P105654 and P072644 as having no completion report
before any time was spent looking, and the route note on P097201 — that `wds?projectid=` missed its
own evaluation review and a title search found it — matched what the cache contained.

**The candidate sentences were close to useless and in one place actively misleading.** Of the
fifteen briefs, the sentence sets were dominated by two kinds of noise:

- **"PLAN VERB — the reprint trap" fired on the word "envisaged" or "will be" anywhere in any
  document.** On P112573 both of its two candidate sentences are in this bucket, and neither has
  anything to do with resettlement: one is the completion report on the Bank's 2008 Interim Strategy
  Note "which envisaged interventions to assist civil war-affected populations", the other is the
  appraisal's note that "10 pickup type vehicles will be acquired to ensure mobility for project
  supervision staff". A writer skimming the brief rather than the document would have found nothing
  in that project and concluded, correctly but for the wrong reason, that there is nothing in it.
- **"compensation unpaid or late" fired on tariff pricing and on unit-cost recitals.** On P105654
  the single hit in that bucket is the plan's price schedule — "approximately USD 230 per square
  meter, including outdoor latrines" — which is a rate, not a payment, and certainly not a late one.
  The same pattern would fire on Kribi's "tariff compensation" from the government to the
  distributor, which is a subsidy payment between two companies and not compensation to anyone
  affected.

**The kinds of sentence the extraction should have surfaced and did not**, each of which decided a
case in this batch:

1. **Borrower-written annexes.** The ten unpaid shop workers at Riviera 2 (P110020) exist only in
   the borrower's own report printed as an annex to the completion report, and they contradict the
   Bank's main text on the same page. No candidate sentence came from any annex in any of the
   fifteen briefs. This is where the batch's sharpest single finding was.
2. **Reports of *carrying out* a resettlement plan, as against the plan itself.** P129713's brief
   listed 22 documents all tagged `RP`. Two of them are not plans: a June 2021 implementation report
   for Kananga, which records one household actually paid and moved on 16 June 2021, and a February
   2019 mission report that found 13 people losing income on Avenue Gazumbu in Kolwezi whom the 2016
   study had missed. Those are outcome documents filed under a plan tag, and the brief's
   "relocation_counts_in_outcome_doc: 0" was wrong for that row because of it. A tag or a pattern on
   titles containing "mise en œuvre", "rapport de mission" or "implementation report" would catch
   them.
3. **Sentences where a *count of households* sits in a row label rather than in prose.** The 72/30/23/19
   breakdown on P104497 is in a summary table — "Nombre de ménages ayant perdu leur logement: 23" —
   and no candidate sentence reached it.
4. **Accident and fatality language.** "22 accidents, including five fatalities" is the most serious
   finding in the batch and no candidate sentence in the P116323 brief carried it.

A note on the plan-reprint check: every row in this batch came back `reprint_flags: 0`, so the check
did no work here and could not be tested. It was verified by hand where it mattered — the 2,411 and
2,256 on P116323 appear in the completion report and the evaluation review and in neither the
appraisal document nor either resettlement plan, and "23 families" on P110177 appears in no document
but the completion report.

## (c) Figures where two documents, or one document, disagree — left unreconciled

1. **P110020, how many of 639 were paid, inside one document.** The completion report's main text,
   paragraph 34: the resettlement plans "provided compensation to all 639 persons affected by
   temporary closures causing loss of income due to works at these sites". The borrower's report in
   the same document's annex, paragraph 50: "A total of 629 PAPs have been compensated to the amount
   of FCFA 857,568,478 for a total of 639 PAPs identified. It remains to reimburse the salaries of 10
   store employees affected by the Riviera 2 constructions due to technical unemployment." Neither
   passage mentions the other. The Independent Evaluation Group's review of 20 April 2015 repeats
   the main text's "all 639" and does not carry the annex's 629 or the ten.
2. **P116323, how long the suspension lasted.** Completion report paragraph 36: "disbursements had
   been suspended for seven months in 2017". Completion report paragraph 62: Component B "was
   suspended between December 2016 and June 2017". Evaluation review ICRR0021995: "The suspension
   was lifted after eight months following the establishment of a new PIU."
3. **P084002, how much compensation had been paid.** Completion report, 29 February 2016: 88 per
   cent of the 585 affected people compensated as of 31 January 2016, for CFAF 401 million, "88
   percent of the total amount due", with two Yaoundé payments awaiting presidential clearance.
   Evaluation review, 28 June 2016: "The Task Team Leader clarified that 95% compensation has been
   made to date." The second figure is a Bank staff statement to the evaluators, not a document, and
   is reported as such on the entry.
4. **P082725, the overall outcome rating.** Completion report ICR2504: "The overall project outcome
   is rated satisfactory". Evaluation review ICRR14151: "overall outcome is assessed as moderately
   satisfactory".
5. **P110020, the overall outcome rating.** Completion report ICR00003208 calculates and states
   Highly Satisfactory. Evaluation review ICRR14735 gives Satisfactory, "there were minor
   shortcomings".
6. **P110177, the approval date.** The completion report's data sheet gives Approval 11 November
   2011 and the body says the project "was approved by the Board in November 2011". ICIJ's lead row
   gives 10 November 2011. The entry uses the document.

## (d) What could not be checked, and the route that failed

- **No completion report for P105654 (Southern Africa Power Market additional financing).** Failed
  route: `wds?projectid=P105654` returns resettlement plans only, and a `qterm` title search on the
  project name returns nothing filed under that number. The sibling P097201 has an evaluation review
  but it reviews that project's own report. Nothing was written from the sibling's documents.
- **No completion report for P097201 in the harvest**, only the evaluation review ICRR0021847.
  The review cites the report by paragraph and is the only route; the entry says so.
- **No completion report for P072644 (RAMP I) in the harvest**, only the evaluation review of
  1 September 2017; that review's safeguards findings rest on "the Bank team informed IEG", which is
  the stated reason for the drop rather than something unchecked.
- **No evaluation review for P100160 (Liberia) and P110177 (Kribi) in the harvest.** Neither entry
  nor drop relies on one.
- **One route failed on the open web, not a host.** `newspublictrust.com`, which a search returned
  as carrying a water-contamination investigation at the Whein Town landfill, serves a Bluehost
  "Account Suspended" page on the article URL. That is the one page that might have carried test
  results for Whein Town. `frontpageafricaonline.com` served its Whein Town article normally over
  the fetch tool; what it carries is residents' accounts with no figures, and it attributes the
  landfill to a different project. No host in this batch refused a request.
- **Searches that returned nothing usable, so the fact was left out rather than softened:** Ivorian
  press on the five deaths on the Grand-Bassam–Aboisso–Noé works (searched in French); Ivorian press
  on the Noé traders' move to the new market platform (French); Congolese press on the Kimbanseke
  compensation claims (French — the one near match, an ACP report of 4 July 2025, concerns
  expropriation for the Kinshasa ring roads and names neither SNEL nor the Bank); Beninese sources on
  the Takon landfill land acquisition (French); Cameroonian press on PDUE's unpaid compensation and on
  noise and compensation around the Kribi plant (French — the one near match, an open letter by the
  Océan deputy Martin Oyono published 7 May 2015, concerns the gas price and the plant's engines and
  says nothing about land, compensation or resettlement).
- **The exact sites behind three entries are not published and are not pinned:** the four water sites
  under P104497 are named but have no coordinates in any document; the Kimbanseke claims have no
  address; the two outstanding Yaoundé payments under P084002 are not identified. All three entries
  carry `ap: true` and say in `point` what the coordinate is.
