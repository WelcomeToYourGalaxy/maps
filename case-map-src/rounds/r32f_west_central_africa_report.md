# Round 32, west and central Africa — writer's report

22 rows. **9 cases, 13 drops, 0 extends, 0 already on the map.**
Output: `/home/claude/work/out32/west_central_africa.json`.

Dedupe: `python3 /home/claude/maps/case-map-src/dedupe_leads.py` on all 22 P-numbers returned
22 of 22 new (1,136 cases, 217 entity records on the map). Confirmed by place and years as well:
`window.CASES` was searched for Maradi, Niamey, Bijilo, Gambia, Lalara, Gabon, Kumasi, São Tomé,
Bombri, Rosso, Mauritania, Senegal River, Sakoinsé, Ouagadougou, RN5, RN6, Gemena, Kasenga, Kaédi,
Hérémakono and Bougouni. No overlap with any of the nine. Two existing cases are the same *shape*
and are worth the lead's eye for consistency, not for a merge:
`ouagadougou-onea-works-before-compensation` (works begun before compensation, Burkina Faso) and
`kwabenya-landfill-expropriation` (Ghana, but Greater Accra, not the Kumasi land office).

## Outcome by row

| P-number | Row | Outcome |
|---|---|---|
| P095949 | Niger, Local Urban Infrastructure Development | **case** `maradi-central-market-works-before-compensation` |
| P112131 | Mauritania Road Corridor ACGF | **case** `nouakchott-rosso-corridor-temporary-moves` |
| P117652 | Central African Backbone APL2, São Tomé | **case** `sao-gabriel-cable-station-urban-farmers` |
| P120636 | Ghana, Land Administration 2 | **case** `kumasi-lands-office-farmers-displaced` |
| P093826 | Senegal River Basin Multi-purpose Water Resources | **case** `senegal-river-perimeter-crops-destroyed` |
| P122402 | WARCIP APL 1B, Gambia/Guinea/Burkina Faso | **case** `bijilo-cable-route-compensation-unpaid` |
| P122776 | Central African Backbone APL4, Gabon | **case** `lalara-fibre-assets-destroyed` |
| P079749 | West Africa Regional Transport and Transit Facilitation | **case** `tema-ouagadougou-bamako-corridor-compensation` |
| P088619 | DR Congo, Emergency Living Conditions Improvement | **case** `drc-rn5-rn6-rn2-compensation-arrears` |
| P103189 | Africa Stockpiles, Mali | dropped — Nanguila relocation reported as implemented in full compliance, no count, no loss; the 170 is the plan's "huit familles totalisant environ 170 personnes" |
| P104716 | Liberia Agriculture and Infrastructure | dropped — Vai Town squatters resettled, funds "released in a timely manner"; the 147 lives in the 2008 plan |
| P115664 | Emergency Monrovia Urban Sanitation | dropped — "Compensation was paid with no outstanding issues"; the harm on record is odour, litter and mosquitoes, uncounted |
| P122065 | WAAPP 1C, Togo | dropped — "no negative social impacts occurred"; the labour findings name no country and no worker |
| P108941 | West Africa Regional Fisheries | dropped — works scaled down or dropped, "no complaints or consequences"; the arrests are of fishing vessels, the project's own output |
| P104456 | Cameroon Energy Sector Development | dropped — 92 to 100 per cent of affected persons paid, shortfall uncounted and attributed to people not being found |
| P071391 | Nigeria Second National Urban Water | dropped — two-month works suspension over payment delays in Lagos, resolved; no count |
| P083751 | West and Central Africa Air Transport Safety | dropped — gardens and plant sellers moved at three airports, all "satisfactorily", no count anywhere |
| P087004 | Cape Verde Road Sector Support | dropped — "satisfactorily implemented"; the named landowners are in the 2012 plan only |
| P130184 | WARCIP 1C, Benin | dropped — "compensation of all individuals and businesses along the cable route"; the 6 is the plan's |
| P095210 | Niger Agro-Pastoral Export (PRODEX) | dropped — "brief resettlement action plans" with no count and no shortfall |
| P073629 | Cameroon Community Development (PNDP) | dropped — two *cases* of involuntary displacement, people resettled back to their initial site |
| P111338 | Lomé Infrastructure Rehabilitation | dropped — no outcome document on either route tried |

Every drop reason quotes the outcome document and says what was checked there. No row was dropped
on a null sentence from a plan or a framework.

## The line I drew, since it decided six of the thirteen drops

Six rows record a land acquisition or a relocation that happened and was paid for, with no count in
an outcome document and nothing left owing (P103189, P104716, P083751, P087004, P130184, and
P095210). Six others record a shortfall. The rule applied: **keep where an outcome document gives a
people-bearing relocation count, or records something still owed or lost** — compensation unpaid,
late, works begun before payment, assets destroyed and not paid for, crops destroyed, land or income
lost by counted people. **Drop where the only record is a completed, compensated acquisition with no
count in an outcome document.** That is why Cape Verde is a drop while Ghana and São Tomé are cases:
Cape Verde's named landowners exist only in its 2012 plan, while Ghana's six farmers and São Tomé's
six-then-seven individuals are counted in the completion report and the assessment report. If the
lead wants the other line, P083751 and P087004 are the two that would come back first.

## My own two weakest entries

**1. `nouakchott-rosso-corridor-temporary-moves` (P112131) — the only card in this batch with a
number in `displaced`, and the number is stated two ways in one report.** The outputs annex says
"the 250 persons who had to temporarily move their homes or businesses due to the construction
works", which is exact and carries a relocation verb. Paragraph 27 of the same report says "some 250
persons who were temporarily displaced **or affected** by the road works" — approximate and
disjunctive, which under the round-31 rule is a floor and not a count. The Evaluation Group's review
makes it "250 people satisfactorily relocated **and/or** compensated". I put 250 in `displaced` on
the annex wording and set out all three forms in `displaced_note`; a checker who holds the
disjunction against it should move the figure to the note, and the card then rests on a relocation
with no count. Two further weaknesses on the same card: the grant financed Lot 2 only, the 47 km
Bombri to Rosso section of a 192 km corridor whose other 145 km the European Union paid for and which
was still being built at closing, and no document says how many of the 250 were on the section the
grant paid for; and the resettlement payments themselves were funded by the government, not the
grant. Both documents record the compensation as paid in full, 32,431,905 ouguiya, with no complaints.

**2. `maradi-central-market-works-before-compensation` (P095949) — the harm has no count of cases and
no named site.** It is one sentence: "in several cases did works start with sites still occupied by
affected persons, or compensation of affected persons was not assured before commencement of works."
"Several" is not a count, the sentence names no site, and the same paragraph says every issue had been
resolved and that proof of adequate compensation of all affected persons was given to the Bank. The
2,586 traders at the Maradi market are "affected by the temporary and voluntary relocation", and a
card whose whole content is a count of people affected is a drop — so the card leans on the
works-before-compensation sentence and uses the 2,586 only to show the scale of the market work. The
site is attached by inference about which works the project did, not by the report. If the checker
cuts this one, the reason to cut it is that it is thinner than Bukoba.

## Did the pre-extracted briefs help or mislead?

**They helped on three rows and were beside the point on the rest.** Two concrete findings:

- **Four of the nine cases turn on a passage no candidate sentence surfaced.** The São Tomé case is
  entirely in paragraphs 3.29 and 3.30 of a 2018 field assessment report that the brief listed as a
  harvested document but quoted nothing from. The Gabon case is in a footnote ("Construction
  operators were requested to compensate these destructions, but this had not been done by the
  closing date"). The Gambia case is in a paragraph whose key numbers sit in footnotes 47 to 49. The
  Senegal River case is in a subordinate clause of a paragraph that is otherwise about compliance.
- **The two sentence kinds that were pure noise**: the "household-loss table label (incl. French)"
  bucket, which on P095949 returned four hits and every one of them was a line from the resettlement
  framework's own table of contents or its glossary of terms, and the "PLAN VERB" bucket, which on
  the same row returned a sentence about fiscal transfer mechanisms containing the word "envisaged".
- **One kind the extraction should surface and does not: the single sentence in a safeguards
  paragraph that reports a shortfall inside an otherwise compliant account.** Every case in this
  batch has that shape. The pattern is not "compensation" plus a number; it is a concessive —
  "albeit", "but in several cases", "although", "with the exception of", "had not been done by",
  "had not been initiated", "were not adequately", "no compensation had been paid". Tested against
  these nine documents, a grep for those phrases *inside the safeguards section* reaches the harm
  sentence on seven of the nine: P095949 ("but in several cases"), P120636 ("Although the Project did
  not involve physical displacement"), P093826 ("Some issues were not tracked effectively" and "no
  compensation had been paid"), P122402 ("the implementation had not been initiated"), P122776 ("had
  not been done by the closing date"), P079749 ("albeit with delays") and P088619 ("were not
  adequately compensated"). It misses P112131, whose finding is a plain count, and P117652, whose
  finding is a plain sentence in a document the extraction listed but did not quote from. The same
  phrases fire 10 to 56 times per document across the whole file, so the section restriction is the
  part that makes it usable.
- **The borrower's annex paid off twice.** In the Senegal River report the basin organisation's own
  annex repeats the destroyed-crops finding word for word, which puts it beyond a drafting slip in
  the Bank's main text. In the DR Congo report the borrower's own account adds "inadequate monitoring
  of environmental and social aspects during construction" from a technical audit, which is nowhere
  in the Bank's main text. It paid off negatively on Niger: the borrower's report does not contradict
  the works-before-compensation finding, and it adds that the shops enclosing the Maradi market were
  still unbuilt when the project ended.
- **The "Resettlement Plan" docty warning was right once.** P117652 is filed with four documents
  tagged as resettlement plans; none of them carries the outcome. The outcome is in the PPAR.

## Figures left unreconciled, with both sides

1. **P088619, the RN2 after-the-fact resettlement plan.** The completion report (21 December 2012,
   paragraph 40) gives "final amount US$262,090" and says the government "has currently paid 61
   percent of the adjusted amount of US$ 262,090 due to 35 project affected persons". The Evaluation
   Group's review (23 September 2013) says the plan "identified the need for compensation payments of
   US$ 202,090". Neither explains the difference. Both figures are on the card.
2. **P117652, how many people lost the São Gabriel land.** The assessment report (4 June 2018) says
   the abbreviated plan "identified six individuals who would lose access to the land and thereby to
   their source of income" and, in the next paragraph, that "seven project-affected persons were
   compensated". Both are on the card; no document reconciles them.
3. **P122402, Burkina Faso.** 277 households identified as affected, 274 compensated — and the same
   sentence adds that "The RAP completion report informed that all compensation measures were
   accomplished". Three households are unaccounted for and no document addresses them.
4. **P112131, the 250.** Three wordings, given above.
5. **P122776, the complaints.** The completion report says 168 complaints were received, "41% of which
   were related to loss of revenue and stalls". The Evaluation Group's review says "Of the 168
   complaints received relating to loss of revenue, 129 complaints were resolved". The review turns a
   subset into the whole.
6. **P095949, a quotation that does not exist.** The Evaluation Group's review puts in quotation
   marks: "The project was generally in compliance with safeguards policies, and only in limited
   cases did physical works begin before all affected persons had been compensated or resettled."
   The completion report's sentence is "in several cases did works start with sites still occupied by
   affected persons, or compensation of affected persons was not assured before commencement of
   works". The string "limited cases" does not appear in the completion report. Noted on the card.
7. **Three rating-label substitutions, of the kind trap 1 describes.** P095949: the review's column
   for the completion report's risk to development outcome says **Significant**; the report itself
   says **Substantial**. P104456: the review's column says **Modest**; the report says **Moderate**.
   P117652: the review's column says **Negligible to Low**; the report says **Low or Negligible**.
   Every rating on every card is read out of the document that gave it.
8. **P093826, the safeguard-policy list.** The completion report lists **ten** policies as triggered
   (4.01, 4.04, 4.09, 4.11, 4.12, 4.10, 4.36, 4.37, 7.60, 7.50). The Evaluation Group's review says
   "The PAD identified the project as a Category 'A' project, and the OP/BP 4.01 was triggered" and
   names no other. The card carries the completion report's list of ten and says what the review says.
9. **P122402 has two evaluation reviews five days apart** (archive dates 18 and 23 August 2022) whose
   text differs on the facts: one says the project closed on 30 July **2022**, the other 30 July
   **2021**, and the second adds a sentence about a one-month extension the first does not have. The
   data sheet of the completion report gives actual closing 30 July 2021. The card cites the later
   review and the completion report's date.
10. **P117652 outcome rating, three documents, three answers**: completion report **Highly
    Satisfactory**, Evaluation Group review **Highly Satisfactory**, Group assessment report (2018)
    **Satisfactory**. All three are on the card, each named.
11. **P122402, a policy misnamed in both documents.** Completion report and review both give
    "Natural Habitats (OP/BP 4.36)". OP 4.36 is Forests; Natural Habitats is OP 4.04. The card names
    the four policies as the documents name them and does not correct them.

## What could not be checked, and the route that failed

- **P111338, Lomé Infrastructure Rehabilitation and Maintenance (Togo): no outcome document.** Two
  routes were tried and both came back empty, not refused. `wds?format=json&projectid=P111338`
  returns `total: 1` and that one document is the April 2008 resettlement policy framework.
  `projects?countrycode_exact=TG&rows=100` returns 159 Togo projects and no parent or sibling under
  which a completion report for this grant is filed; the nearest by name and date is P113415,
  Emergency Infrastructure Rehabilitation and Energy Project, approved a year later in June 2009 with
  US$25 million, which is a different operation. The project record for P111338 itself returns a
  grant of US$1,575,000 approved 23 May 2008, closing 30 June 2010, with `status`, `totalamt` and
  `lendinginstr` all null. No evaluation review exists either, so the route of last resort in
  BRIEF31 — the review that cites the report by paragraph — is not available.
- **Dates on five evaluation reviews.** The newer review template prints no date anywhere in the
  document body: P112131, P120636 (2020), P122402, P122776 and P079749 (2016) all carry only a
  project data table. The date on those five sources is the archive's own `docdt` metadata field, not
  a filename and not a URL, and that is the best available. Every other date on every card was read
  off the document's cover or its "Date Posted" line; the one that needed watching, P093826, has a
  cover date of 25 September 2013 and an internal "ICR Date: 01/08/2013", and the card uses the cover.
- **Source URLs.** Taken from `harvest_manifest.json`, with the host rewritten from
  `documents.worldbank.org` (which refuses) to `documents1.worldbank.org` and `http` upgraded to
  `https`, exactly as BRIEF20 prescribes. No path segment was altered and no URL was built by hand.
  All 32 cited URLs were range-requested and returned HTTP 200 or 206.
- **Independent corroboration: none found, so all nine cases are `contested`.** Three searches were
  spent, in French, on the Maradi market relocation, the Gabon fibre route at Lalara and the Cameroon
  rural electrification compensation. Nothing came back that named a site, a person or a payment.
  Searching was stopped after that: these are small projects whose harms are recorded in a sentence
  or a footnote, and the remaining search budget was not worth spending at that rate. Every card says
  in `confidence_note` that no independent account was found.
- **Staff statements kept off the cards as facts.** Four were found by grepping the reviews for
  "informed IEG", "the project team" and "the team clarified": P095949 (with the exception of three
  people all affected people in the Maradi market were satisfactorily relocated), P122402 (only six
  of the fifteen could be identified and the actions taken were appropriate and sufficient), P122776
  (there was no land acquisition; and the Lalara and indigenous peoples issues are still unresolved),
  P120636 (a customary land intervention assessment was prepared in June 2017). The first three are
  on their cards, each labelled as a statement by staff rather than a document. The fourth is not
  used.
- **Which credit paid, checked on all nine.** The one that moved an outcome: P104456, where the
  credit financed only preparatory activities for the Lom Pangar hydropower dam and the completion
  report says those triggered no safeguard policies — so nothing at the dam could belong to that row,
  which is a drop on other grounds anyway. The one that qualifies a card: P088619, where the reduced
  road shoulders on National Road 2 are the earlier project's work and only the unpaid balance of the
  after-the-fact plan belongs to this grant; the card says so. On P122776, Lalara is named in the loan
  agreement's list of the links the loan financed. On P093826, the destroyed-crops finding sits in
  Annex 7.1, the annex covering the IDA-financed activities, and not in Annex 7.2, the Dutch Trust
  Fund one. On P087004, the Vila das Pombas works where the appraisal expected land taking were to be
  paid for from the borrower's own funds.

## Document cache

All documents were read from disk at `/home/claude/work/cache/<P-number>/` as the briefs listed them.
Nothing was re-fetched. Three API calls were made, all list queries and no documents: two to
`search.worldbank.org/api/v3` for P111338's documents and Togo's projects, and one for P111338's own
project record. Nine Nominatim lookups supplied the coordinates; the one that disagrees with the Bank
is Lalara, which Nominatim places in Woleu-Ntem and both Bank documents place in Ogooué-Ivindo, and
the card says both.
