# Round 32, west and central Africa — checker's log

Checked: `/home/claude/work/out32/west_central_africa.json` (9 cases, 13 drops) and
`west_central_africa_report.md`. Output: `west_central_africa_checked.json`.

**Result: 7 cases, 15 drops.** Two of the writer's nine cases cut. Substantive corrections on five of
the remaining seven. All thirteen of the writer's drops upheld, including the three re-opened on
instruction. Every document was read from `/home/claude/work/cache/<PID>/`; nothing was re-fetched.

---

## 1. Cuts

### `maradi-central-market-works-before-compensation` (P095949) — CUT

**Deciding document and sentence.** Completion report ICR2680 of 1 July 2013, paragraph 35:

> The project was generally implemented in compliance with safeguards policies, but in several cases
> did works start with sites still occupied by affected persons, or compensation of affected persons
> was not assured before commencement of works.

Read whole, that sentence is the entire harm and it fails limb (b) three ways at once. It gives no
count ("several"). It names no site. And it is disjunctive about what happened in any of the cases:
either works began on an occupied site, **or** compensation was not assured. The same paragraph, nine
lines on, closes it:

> At the time of finalizing this ICR, all issues raised during project implementation support
> missions and in technical audit reports have been fully resolved and proof of adequate compensation
> of all project affected persons has been provided to the World Bank.

The writer quoted both halves and did not hide the resolution clause — this is not selective
quotation. It is a limb (b) failure. I read the whole report for anything else: a grep of every
compensation, resettlement, displacement and relocation word in the file returns six hits, and the
other five are the 2,712 persons affected and 2,586 traders "affected by the temporary and voluntary
relocation" of the Marché Central (a count of people *affected*, and a relocation the document calls
voluntary); paragraph 59, where people in Niamey Commune V "had already voluntarily relocated
temporarily" for road works the project then dropped; and paragraph 3.3.3 of the borrower's annex,
which says only that compensation was the cities' responsibility.

**The one version with a count and a site is a staff statement.** The Evaluation Group's review of
14 October 2014 says that with the exception of three persons all affected people in the market were
satisfactorily relocated, that "The Municipality had received only tacit agreement from the three
persons before rehabilitation and reconstruction work commenced on two public latrines and one water
kiosk." Section 8 of the same review gives its provenance: "The project team has since provided
further clarification. According to the TTL..." A number Bank staff gave the Bank's evaluators during
a review is not a document. The writer labelled it correctly and declined to count it; I agree, and
that is what leaves the card with nothing.

**Against the Bukoba edge** — compensation unpaid in five identified resettlement cases at a named
site — this has no count, no site, and nothing outstanding. The writer named it as their second
weakest and said the reason to cut it would be that it is thinner than Bukoba. It is.

Also corrected in passing: the card's `place` read "Marché Central, Maradi, and sites in Niamey and
Dosso" and the `point` note conceded that the report does not say which sites the finding covers. A
card cannot attach a harm to sites the document does not attach it to.

### `nouakchott-rosso-corridor-temporary-moves` (P112131) — CUT, on two independent grounds

The writer named this their weakest entry and set out the test. Both halves of it fail.

**The figure.** The completion report of 8 October 2015 states its 250 twice, in different terms.

- Annex 2, Outputs by Component, line 1252: the consultant "worked with the Government to compensate
  the 250 persons who had to temporarily move their homes or businesses due to the construction works
  as part of the ARAP". People-bearing, relocation verb, definite article.
- Paragraph 27, the safeguards narrative — the document's own account of what happened: the consultant
  and the hired non-governmental organisation "interviewed some 250 persons who were temporarily
  displaced **or affected** by the road works, and subsequently compensated these persons".
- Evaluation Group's review: "250 people satisfactorily relocated **and/or** compensated", and
  elsewhere "250 people (para 27 ICR), who were displaced **or affected** by the road works and
  subsequently resettled".

Two of the three statements are disjunctive, and the only clean one is a single cell in a table of
consultant deliverables. `displaced` holds a count of people relocated and never "affected". Where a
document's own narrative cannot say whether its 250 were moved or only affected, the deliverables
table cannot certify the count. Round 19 cut a figure on exactly this shape. The figure therefore
cannot sit in `displaced` — and the writer stated the consequence themselves: without it the card
rests on a relocation with no count, so limb (a) is gone, and limb (b) needs a loss on top of the
move. There is none on record. The grantee's annex (paragraph 14): "persons affected by the project
were consulted and compensated at the rate of 32,431,905 MRO and claims were handled without
reservation as confirmed by the absence of complaints". Paragraph 19: "All persons affected by the
project were properly consulted and compensated and all claims settled without reservation." No work
accidents.

**The lender link.** The grant and the government co-financed Lot 2 only, the 47 km Bombri–Rosso
section; the European Union financed Lot 1, the 145 km Nouakchott–Bombri section, still under
construction at closing. No document allocates the 250 between them. Paragraph 27 adds that the
environmental and social assessment and management plan were "financed from the TSIDTAP" — a
different operation — and paragraph 44 that "the Government was efficient in implementing and funding
the ESMP and ARAP". The compensation was paid by the government, not from the grant.

**Not a plan reprint.** The 250 appears in no plan or appraisal document for this project; the
appraisal document's only "250" is a US$250,000 technical-audit line. The pre-extraction's own
`relocation_counts_in_outcome_doc` field is null for this row, so the brief did not see it either.

---

## 2. The writer's line, tested

The line: *keep where an outcome document gives a people-bearing relocation count, or records
something still owed or lost; drop where the only record is a completed, compensated acquisition with
no count in an outcome document.* Tested against the forward rule and against Bukoba, it holds, and I
applied it harder than the writer did — it is the line that cuts Maradi and Nouakchott, not just the
six drops the writer applied it to. Where limb (b) is in play, "something still owed or lost" is
doing the work that CHECK20's limb (b) list intends; the list's "land taken" cannot mean every
compensated acquisition, or it would swallow the separate item "compensation unpaid or below
replacement cost" that sits four words from it.

All three re-opened drops stay dropped.

### P083751, West and Central Africa Air Transport Safety — stays dropped

Completion report of 12 December 2014, paragraph 65(a) and (c), read whole: "Plant sellers along
'Patte d'Oie' roundabout in the airport security perimeter were satisfactorily relocated, and
supported by a compensation process executed in compliance with The World Bank safeguards"; "All
farming activities have been satisfactorily relocated. This was supported by a compensation process
executed in a transparent manner, and in compliance with the RAP." Paragraph 64: "all three RAPs and
other environmental mitigation measures were fully and successfully implemented." Paragraph 65 opens
"no sensitive environmental and social issues have been raised during the project implementation".
The Yaoundé shrine relocation flagged in the plan did not happen — the government built a road round
it. The review of 1 June 2015 adds nothing.

A named site (the Patte d'Oie roundabout) and an identified group (plant sellers there) put this at
Bukoba's level on identifiability, but nothing is owed and nothing is recorded as lost: that is the
axis on which Bukoba is a keep. No people-bearing count anywhere, so limb (a) is out. "All farming
activities" is not a people-bearing unit.

One internal inconsistency worth recording, not load-bearing: paragraph 63 places the resettlement
impacts "at Conakry, Douala and Yaoundé international airports in Guinea and Cameroon", and paragraph
65(a) then reports the plant-seller relocation at Ouagadougou in Burkina Faso.

### P087004, Cape Verde Road Sector Support — stays dropped, with the drop reason corrected

Completion report of 28 May 2014, paragraph 38, in full: the original project required no land
acquisition; the Alcatraz–Figueira alignment on Maio "required minor land acquisition of uncultivated
agricultural land"; the Ponta de Talho–Igreja works "required partial acquisition of agricultural
plots"; an abbreviated resettlement plan "was prepared, disclosed and satisfactorily implemented". No
count, no shortfall. The review of 27 October 2014 adds only that the Vila das Pombas and Eito works,
where the appraisal expected minor land taking of stonewalls, were to be funded from the borrower's
own funds and that the completion report does not report compliance there — an absence, not a harm,
and on works the credit did not finance.

**Correction to the drop reason.** The writer wrote that the named landowners "are in the 2012 plan
only". They are not. Georgina Melo and Antonio dos Santos, with 200 m² of sugar-cane land and the
compensation calculated for it, are in the abbreviated resettlement plan of 7 May 2008 and in the
appraisal document of 22 April 2005 (page 17 table), for the Santo Antão works; the June 2012 plan is
a separate document covering the Santiago roads. The substance of the drop is unchanged — every
named landowner is in an appraisal-stage document — but the drop reason as written is wrong about
which document, and a fact sourced to the wrong document is a sourcing failure even when the fact is
right.

### P104456, Cameroon Energy Sector Development — stays dropped

Completion report of 27 December 2017, paragraph 64, read whole: compensation decrees signed in 2015
"with a delay of more than two years"; campaigns for the 20 departments completed between April and
December 2015; "The compensation campaigns were well managed and allowed the payment of compensation
of between 92 and 100 percent of the PAPs depending on the department or region (a small percentage
of PAPs could not be compensated because they could not be found)." The same paragraph: "Implementation
of safeguards was satisfactory throughout Project implementation" and "The Project complied with all
the mitigation measures mandated under the ESMP and RAPs."

The shortfall is real and uncounted, but it has no count of people, no count of cases, no site
narrower than a region, and the stated reason is that the people could not be located. Three regions
are named; the 20 departments are not. The only other candidate, a borrower recommendation to run
communications campaigns "to avoid recurrent complaints by the PAPs", is forward-looking and attaches
to nobody. Against Bukoba's five identified cases at a named site this is thinner on the two axes
that matter. The writer's additional point is confirmed: paragraph 65 says the credit financed only
preparatory activities for Lom Pangar and that "These activities did not trigger any safeguard
policies", so nothing at the dam attaches to this row.

---

## 3. Corrections to the seven kept cases

### `sao-gabriel-cable-station-urban-farmers` (P117652) — an invented conflict, removed

The writer listed "how many people lost the São Gabriel land" as an unreconciled conflict: the
assessment report says the abbreviated plan "identified six individuals who would lose access to the
land and thereby to their source of income" (paragraph 3.29) and that "seven project-affected persons
were compensated" (paragraph 3.30), with no document reconciling them. **There is no conflict.** The
abbreviated plan of 4 July 2011 is on disk and says seven:

> The area to be developed will require approximately 1,922m² of land that is currently being used
> for agriculture. There are seven farmers that will be impacted upon and will loose a portion of the
> land they cultivate.

and its Appendix 1 opens "The following seven PAPs will be affected" and prints seven data sheets,
one per farmer, with age, schooling, household and crops. The six is the assessment report's own
error about the document it cites. An invented conflict is the same fault as a tidy reconciliation,
and this one was avoidable: the plan the conflict turns on was in the brief's document list.

Corrected: title now "Seven farmers…"; the `community` prose gives the plan's seven, its own words,
and the detail from the data sheets (fifteen years' cultivation, market sale, cabbage, onions, green
peppers, sweet potatoes, one farmer losing about 70 per cent and another about half, the medical
specialist losing all of his), then notes that the assessment report says six; `displaced_note` and
`confidence_note` rewritten. The case is stronger after the correction, not weaker: seven identified
people, each with a data sheet, a named site, a stated loss of land and income, and US$13,005 paid in
three components. All figures confirmed against paragraphs 3.29 and 3.30. The completion report's own
statement is confirmed at line 1057 and in the Annex 2 row at line 1890 ("All compensations that were
due were calculated and successfully paid to the affected people") — no numbers in either, as the
card says.

Ratings confirmed from the document that gave each: completion report Highly Satisfactory / risk "Low
or Negligible" (data sheet, page i); review Highly Satisfactory / "Negligible to Low"; assessment
report Satisfactory (Principal Ratings table). The review prints "Negligible to Low" in **both**
columns of its summary table, including the column for the completion report's own rating, which the
report gives as "Low or Negligible" — trap 1, and the card reads each from its own document.
Financing confirmed: SDR 9.8 million, US$14.9 million equivalent, IDA-H6420, XDR 9.80M disbursed,
approval 20 January 2011, closing 31 December 2014, cover date 17 June 2015, report ICR00003141.

### `kumasi-lands-office-farmers-displaced` (P120636) — the batch's one real plan reprint, undisclosed

**The six farmers are the resettlement plan's own count, and the card did not say so.** The figure is
in the abbreviated plan of October 2010 — "The section on the Socio-Economic Profile of Affected
People presents data gathered on the six PAPs on the 11th and 12th October 2010. There are six (6)
farmers on the Kumasi site; one female and five males aged between 28 years and 65 years" — and in
the appraisal document of March 2011 ("in view of the six farmers undertaking their farming
activities on the site"; "affected people are six farmers on the … The plan will be implemented").
The writer's card said only that the appraisal "had noted that people occupying the land earmarked
for the office could lose their livelihood", which conceals that the appraisal carried the number.

**The verb check saves the card.** The plan is present tense and prospective ("There are six
farmers"; "they will have to relocate their activities prior to the commencement of civil works").
The revised completion report of 18 June 2020, paragraph 98, attaches a completed causal verb: the
site "caused economic displacement of six (6) farmers", and "Although the Project did not involve
physical displacement of population or communities, it involved economic displacement of six
farmers." That is an outcome, not a reprinted plan, so the row is a keep — but the provenance belongs
on the card and is now on it, with the plan's detail (one woman, five men, 28 to 65, two in piggery,
cassava, plantain and maize, GH¢10 to GH¢400 a month, cash compensation their stated preference).

**The pre-extraction missed this entirely.** `reprint_flags` is 0 for P120636 and the brief lists no
reprint candidates. It is the only genuine reprint in the batch and the mechanical check did not see
it. See section 7.

**Absence claim turned into a figure.** "No document says what the six farmers were paid" was an
untested absence claim. The plan's section 9.0 gives a total estimated resettlement budget of
GH¢9,432.70. The card now gives that and says no *outcome* document says what was paid, which is what
the record supports.

**`lenders[0].role` error, corrected.** The card said the revised completion report "says the rating
was lowered from the earlier report to reflect the financing gap". It says no such thing. Paragraph 68
gives the reason: relevance high, efficiency substantial, but "due to the failure of the Project and
the Lands Commission to address the key bottlenecks in registration of both deeds and title and
achieve and outcome indicators, the efficacy is Modest. Therefore, the overall outcome rating is
Moderately Unsatisfactory." The earlier report of 19 October 2018 rated the outcome Moderately
Satisfactory on efficacy and efficiency both substantial (paragraph 67, and its KEY RATINGS block).
The financing gap is discussed at paragraph 86 and is not given as the reason for the rating. Also
added: the Evaluation Group reviewed **both** reports, and its first review of 22 March 2019 already
rated the outcome Moderately Unsatisfactory — the card cited only the 2020 review.

Everything else in that field is exact and I checked it line by line against the FINANCING block:
IDA-48700 50,000,000 / 46,795,104; TF-14256 2,879,706 / 2,500,919 / 2,500,919; IDA-63450 35,000,000 /
0; key dates 31-Mar-2011, 08-Aug-2011, 02-Jun-2014, 31-Mar-2016, 20-Jan-2020; and paragraph 86's
"less than US$1 million out of US$5million disbursed by the GOG". The 2018 report's safeguards
paragraph 93 is confirmed as containing nothing about the six farmers: "OP4.01 … and OP4.12 … were
triggered, and no issues arose during project implementation."

### `senegal-river-perimeter-crops-destroyed` (P093826) — site claim corrected, policy conflict added

The quotation is exact and the whole of paragraph 28 is on the card, including the three clauses that
cut the other way ("The compliance of the small scale construction activities with the safeguards
requirements was consistently rated satisfactory during Bank supervision missions"; "The executing
agencies fulfilled their responsibilities in the majority of cases"; the positive feedback on
walkways). No selective quotation.

**Correction 1.** The writer's report says the basin organisation's annex "repeats the destroyed-crops
finding word for word". It does not: Annex 7.1 says "it was noted that the **winter** crops were
destroyed by the implementation of the project and no compensation had been paid", where the main text
says "crops had been destroyed" and attributes the observation to the OMVS completion assessors. The
annex adds a detail rather than repeating; the card now says so. Annex 7.1 is confirmed as the
IDA-financed-activities annex, not the Dutch Trust Fund annex 7.2.

**Correction 2, `place`.** The card placed the harm in "Irrigation perimeters in the Gorgol and Trarza
wilayas". No document does. A grep of the completion report for "perimeter" returns five hits and not
one names a Mauritanian perimeter; the Gorgol/Trarza attribution comes from the appraisal document's
account of where the Mauritanian works were. `place` now reads "An unnamed irrigation perimeter in the
Senegal River valley, Mauritania", and the `point` note already said the report does not name it.

**The safeguard-policy list — both readings kept, and a third added.** Confirmed: the completion
report's paragraph 26 lists ten policies as triggered; the review's section 11a says "The PAD
identified the project as a Category 'A' project, and the OP/BP 4.01 was triggered" and names no
other. The writer was right to carry the report's ten and to report what the review says. **What
neither of them checked is the appraisal document itself.** Its own table of policies triggered marks
eight in the Yes column and marks two of the report's ten in the **No** column: Indigenous Peoples
(then OD 4.20, being revised as OP 4.10) and Projects in Disputed Areas (OP/BP/GP 7.60). That is now
in `lenders[0].role`, unreconciled. The review's single-policy sentence is wrong against the appraisal
document it cites as well as against the completion report.

One further finding added to `confidence_note`: the review paraphrases the sentence immediately
preceding the destroyed-crops finding — safeguards work in the field going to physical issues at the
expense of social ones — and stops before the example that follows it. The writer's statement that the
review "does not mention the destroyed crops" is confirmed, and is sharper than it looked.

Ratings confirmed from each document: report Satisfactory / risk Moderate / Bank and borrower
Satisfactory; review (Date Posted 06/30/2015) Moderately Satisfactory, Bank Moderately Unsatisfactory,
borrower Moderately Satisfactory, quality of ICR Unsatisfactory. Cover date 25 September 2013
confirmed. Financing confirmed line by line from the cover and the data sheet (SDR 21.0 / 22.2 / 21.0 /
12.60 / 8.5 million; XDR 76.80M committed, 68.01M disbursed). Outputs confirmed: "well more than
4 400 ha were rehabilitated or developed for irrigation, 88 kilometers of irrigation canals were built
or rehabilitated (instead of the targeted 50) … therefore 47 pumping stations".

**This is now the batch's weakest keep, and both sides belong on the record.** For: a completed loss
(crops destroyed), compensation explicitly not paid, stated in an outcome document and independently
restated in the borrower's own annex with an added detail; plus a second documented loss in Mali
(crops over two seasons, with the executing agency distributing food directly). Against: no count of
people, no count of cases, and no named perimeter — on the identifiability axis it is thinner than
Bukoba, which at least counts five cases at a named site. I keep it because the harm is definite and
doubly recorded where Bukoba's is singly recorded, but a lead who reads the "anything thinner than
Bukoba is not limb (b)" line strictly will cut it, and should know that is the choice.

### `bijilo-cable-route-compensation-unpaid` (P122402) — the 15 is a plan figure with its unit changed

The plan-reprint check in this row's brief flagged 15, and the writer did not address it. It is real
and it matters. The resettlement plan of May 2011, section 8.0: "This Resettlement Plan has covered
**15 shops and 4 residential houses** which will be impacted by the project." Its Annex 1 is a table
of 15 numbered entitlement entries with a disturbance allowance and supplementary assistance for
each, totalling 37,923.49 dalasi — and the entries are a mix of individuals given by initials (A.S.,
M.J., S.K., N.J., O.T., E.J., A.J.) and premises or trades (SPEED Petrol Station, Bijilo Inn, Lumber
Seller, Charcoal/Firewood, Concrete Products Manufacturing Site, Pavement Blocks Seller). The
completion report of 25 February 2022 then says "The total number of people **affected** was then
listed as 15, entitled to an estimated total compensation close to US$1,500.00", and the review says
"The total number of people who were affected was listed as fifteen during implementation." The unit
shifts from shops and entitlement rows to people, and no document explains it. The plan's
compensation total of D37,923.49 is also, at 2011 rates, roughly the US$1,500 the completion report
gives — a second plan figure carried into the outcome document.

The card now says all of this: `community`, `displaced_note`, `outcome` and `confidence_note` are
rewritten, and the title changed from "Nine of fifteen people affected … were never paid" to
"Compensation paid to six of the fifteen on the Bijilo cable route in The Gambia". The nine was a
subtraction no document prints.

**The case survives it, and is the strongest in the batch.** The harm does not depend on what the 15
counts: compensation under an approved plan reached six of the fifteen entitled parties and not the
rest, by the closing date, nine years after the plan. The completion report cites its sources by date
in footnote 49 — a Monitoring Report on the Resettlement Payment from MOICI dated 7 October 2014, and
"The Supervision Mission Aide-Mémoire January 19–23, 2015, acknowledges the payment of compensation
to just six of the 15 people affected" — and the review states independently that "Six people had
received compensation when the project closed." The individuals are identified in the plan's annex.
That is above the Bukoba edge on every axis.

The writer's handling of the 27 is confirmed correct and unusually careful: the plan does give 27
twice over, as a census ("no more than 27 persons may be affected") and as a table of "27 structures/
plots of land" that includes two empty plots, three uncompleted structures, an uninhabited structure
and a security zone. The card's prose on that was right; only the ICIJ sentence needed softening,
since identifying ICIJ's 27 *as* the plan's figure is a claim about ICIJ's sourcing that nothing
supports.

Burkina Faso figures confirmed exactly from paragraph 79(a) and (b): 277 identified, 274 compensated,
FCFA 23 million / about US$40,000, with "The RAP completion report informed that all compensation
measures were accomplished" in the same sentence pair; 198 affected and all 198 paid, FCFA 19 million
/ about US$33,000. The three households are unaccounted for and no document addresses them — left
unreconciled, as the card has it. **Not a reprint**: the Burkina document in this row is a framework
and says in terms that "l'estimation précise du nombre de personnes affectées … n'est pas réalisable
à ce stade", so 277, 274 and 198 appear in no plan.

Financing and dates confirmed line by line (112,000,000 / 109,513,830 / 100,919,477; H7130
35,000,000 / 32,563,720; H7120 23,000,000 / 19,948,274; H7140 34,000,000 / 31,755,664; 62220
20,000,000 / 16,651,819; 21-Jun-2011, 31-Oct-2011, 02-Jun-2014, 31-Dec-2016, 30-Jul-2021; ICR00005569,
cover date 25 February 2022). Four policies confirmed, named as the documents name them, including
the misnomer the writer flagged ("Natural Habitats (OP/BP 4.36)" in both documents; OP 4.36 is
Forests) — the card names them as the documents do and does not correct them, which is right.

### `lalara-fibre-assets-destroyed` (P122776) — invented figure removed, financing conflict added

Paragraph 72 and footnotes 75 to 77 confirmed word for word, including the "generally compliant"
clause that opens the passage and which the card carries. Footnote 75: "Construction operators were
requested to compensate these destructions, but this had not been done by the closing date, raising
the prospects of complaints from people whose assets were destroyed."

**Correction 1.** `outcome` said the project closed "with 39 of the 168 complaints unresolved". No
document gives 39; it is 168 minus 129, and the 129 is itself dated "so far" to a project unit report
of 11 March 2021, after closing, with "the pending ones … being processed". Replaced with what the
document says.

**Correction 2, `lenders[0].role`.** The card said the US$51 million of counterpart financing "was
revised to nil", which is what the completion report's financing table shows (original 51,000,000,
revised 0, disbursed 0). The review says the opposite: "The borrower contribution was estimated at
US51.0 million at appraisal. According to the information provided by the team, their actual
contribution was US$53.1 million (including US$51 million for the original project and US$2.1 million
for the AF project)." Both now on the card, unreconciled, with the review's figure marked as a staff
statement.

The complaints disagreement the writer reported is confirmed: the report says 168 complaints, "41% of
which were related to loss of revenue and stalls"; the review says "Of the 168 complaints received
relating to loss of revenue, 129 complaints were resolved". The review turns a subset into the whole.

**Reprint flags on this row are all artifacts.** See section 7. The lender link is confirmed: Lalara
is in Part 2 of the loan agreement's schedule of the links the loan financed ("Boué – Koumameyong –
Lalara – Mitzic – Oyem – Bitam – Eboro / Border with Cameroon"). The Nominatim/Bank disagreement on
Lalara's province is correctly carried on the card both ways.

### `tema-ouagadougou-bamako-corridor-compensation` (P079749) — confirmed, one attribution tightened

Paragraph 67 confirmed in full, including the Ghana clause between the two the card uses: "the
compensations were fully carried out, albeit with delays. Particularly in Burkina Faso, the works
contract was signed while the compensations were still ongoing. In Ghana, the increase in the
financing parameters helped expedite the resettlement and compensation … In the case of Mali,
involuntary resettlements were made for seven households."

`displaced: 7` stands. People-bearing unit, relocation verb, two outcome documents — the completion
report of 31 December 2015 and the field-based assessment report of 19 April 2018, paragraph 4.6 ("In
Mali, seven households were resettled and compensation was timely"). **Not a reprint**: no plan or
framework in this row's cache contains a seven-household figure; the brief's flagged 200 and 21 are
the OP 4.12 abbreviated-plan threshold and a footnote number.

The October 2007 abbreviated compensation plan is confirmed as the card describes it: Table 6 names
four owners — Kaboré Koudyamba, Roamba Tenga, Kiendrebéogo Issaka, Zongo Issouf — each losing 1 ha
and 800 kg/year of harvest at borrow pit 4, in Sakoinsé and Douré, with trees at two other pits. The
card presents it as a plan, which it is.

Tightened: the clause "the second only for minor land acquisition or loss of income" is the assessment
report's, not the completion report's, and is now attributed. The completion report's own Table 3
marks exactly two policies triggered, as the card says. Cover date and report number confirmed
(ICR00003592, December 31, 2015); assessment report cover APRIL 19, 2018, Report No. 124817, borrower
performance moderately satisfactory.

One structural weakness the lead should see: the card's point and `place` are the Ouagadougou–Sakoinsé
section in Burkina Faso, while the counted harm in `displaced` is the seven households in Mali, whose
location no document gives. The card discloses this in `confidence_note` ("counted but not placed"),
which is the right disclosure, but the geometry of the card puts a Mali count on a Burkina point.

### `drc-rn5-rn6-rn2-compensation-arrears` (P088619) — title corrected

Paragraphs 39 and 40 confirmed word for word, and the review's resettlement section confirmed. The
title said "39 per cent of the RN2 payments never made". The documents say 61 per cent paid
"currently" and that "the government is implementing the RAP as funds become available" — outstanding
at the report date, not never made, and the 39 is a subtraction. Retitled "…with 61 per cent of the
National Road 2 payments made at closing". The `outcome` field already said it correctly.

The unreconciled US$262,090 / US$202,090 is confirmed on both sides and from both documents, with
neither explaining the difference. Everything else on the card checks out, including the borrower
annex's "inadequate monitoring of environmental and social aspects during construction" (quoted in the
review at ICR p. 40) and the review's refusal to conclude environmental compliance. The card's own
qualification — that the reduced RN2 shoulders are the earlier project's work and only the unpaid
balance belongs to this grant — is correct and necessary.

---

## 4. Drops upheld without change

Each of the remaining ten was checked against the outcome document named, and every quotation was
found and read in its paragraph.

| P-number | Outcome-document sentence that decides it | Verdict |
|---|---|---|
| P103189 | ICR 28 Jun 2013 ¶27: resettlement plan for Nanguila "subsequently implemented in full compliance with safeguard requirements"; the 170 is the plan's "huit familles totalisant environ 170 personnes" | drop upheld |
| P104716 | ICR 26 Jan 2016 ¶107: "the government expeditiously implemented the safeguards policy and funds for compensation were released in a timely manner" — read whole; the surrounding sentences contain no shortfall clause | drop upheld |
| P115664 | ICR 20 Jun 2017 ¶40: "Compensation was paid with no outstanding issues" | drop upheld |
| P122065 | ICR 19 Jun 2020 ¶88: "The World Bank's involuntary resettlement policy was triggered, but no negative social impacts occurred"; ¶87's labour findings name no country, no subproject and no worker | drop upheld |
| P108941 | ICR 12 May 2017 ¶45: "since the works were very small, there were no complaints or consequences"; the arrests are of vessels | drop upheld |
| P071391 | ICR 21 May 2018 ¶52, read whole: "Delays in payments to Project Affected People in Lagos led to a brief suspension of works in February 2017, but this was quickly resolved by April 2017"; ¶50 "no major violations are on record". No count, no site beyond the city | drop upheld |
| P130184 | ICR 12 Jan 2018 ¶106: the government "had executed all social and environmental plans satisfactorily, including adequate information sharing and compensation of all individuals and businesses along the cable route"; the 6 is the April 2012 plan's "dix (10) biens … appartenant à six (6) PAP" | drop upheld |
| P095210 | ICR 24 Apr 2018 ¶54: road subprojects "required the preparation and implementation of brief resettlement action plans", no count, no site, no shortfall | drop upheld |
| P073629 | ICR 25 May 2010 ¶49, read whole: "Only two cases (out of more than 300 subprojects) of involuntary displacements were recorded during Project implementation. Adequate measures were taken to resettle the concerned parties back to their initial site." A count of cases is not a people-bearing count, and nothing is left standing | drop upheld, and it is the closest call, as the writer said |
| P111338 | No outcome document on either route tried; the one disclosed document is the April 2008 resettlement policy framework, which records no works and no affected person | drop upheld, with the route failure named in section 6 |

Two of the writer's quotations in this group did not return from a first grep — P130184's
"compensation of all individuals and businesses" and P122065's "no negative social impacts occurred".
Both are in the documents; the greps failed on soft hyphens and non-breaking spaces in the extracted
text. Noted because the same failure mode could produce a false absence claim.

---

## 5. Figures left UNRECONCILED, both sides given

1. **P088619, the RN2 plan total.** Completion report, 21 December 2012, ¶40: "an ex-post RAP (final
   amount US$262,090)" and "has currently paid 61 percent of the adjusted amount of US$ 262,090 due to
   35 project affected persons". Evaluation Group's review, 23 September 2013: the plan "identified the
   need for compensation payments of US$ 202,090". Neither explains the difference. Both on the card.
2. **P122402, Burkina Faso.** 277 households identified as affected, 274 compensated, and in the same
   sentence pair "The RAP completion report informed that all compensation measures were accomplished".
   Three households unaccounted for; no document addresses them.
3. **P122402, the unit of the 15.** Plan: "15 shops and 4 residential houses", and an annex of 15
   entitlement entries. Completion report and review: 15 people affected. No document explains the
   shift.
4. **P122402, two reviews five days apart.** Archive dates 18 and 23 August 2022. The earlier says
   the project "closed on July 30, 2022" and that the closing date "was extended from June 30, 2021 to
   July 30, 2022"; the later says "closed on July 30, 2021", adds "The project closing date was
   extended by a month from June 30, 2021 to July 30, 2021", and drops the other sentence. Both print
   30-Jul-2021 in their own data tables, and the completion report's data sheet gives actual closing
   30-Jul-2021. The card cites the later review and the report's date.
5. **P122776, the complaints.** Report: 168 received, "41% of which were related to loss of revenue
   and stalls", 129 resolved. Review: "Of the 168 complaints received relating to loss of revenue, 129
   complaints were resolved". The review makes a subset the whole.
6. **P122776, the borrower's contribution.** Report's financing table: US$51 million at appraisal
   revised to nil, nil disbursed. Review, from the project team: actual contribution US$53.1 million.
   Both now on the card.
7. **P093826, the triggered policies — three documents, three answers.** Completion report ¶26: ten
   policies. Review §11a: "the OP/BP 4.01 was triggered", no other named. Appraisal document's own
   table: eight in the Yes column, with Indigenous Peoples and Projects in Disputed Areas in the No
   column. All three now on the card.
8. **P117652, outcome rating — three documents, three answers.** Completion report Highly
   Satisfactory; review Highly Satisfactory; assessment report (2018) Satisfactory. All three named on
   the card. Confirmed from the assessment report's Principal Ratings table.
9. **P112131, the 250, stated three ways.** Set out in full in the drop reason; this is now a drop
   rather than an unreconciled figure on a live card.

**Conflicts the writer reported that are not conflicts.** P117652's six against seven is the
assessment report misreporting the plan it cites; the plan says seven. Removed, with the plan quoted.

**Review-column rating substitutions, all three confirmed** and all three handled correctly by the
writer, each rating read out of the document that gave it: P095949 review column "Significant" against
the report's "Substantial"; P104456 "Modest" against "Moderate"; P117652 "Negligible to Low" against
"Low or Negligible".

---

## 6. A quotation that is not in the document — confirmed, and a second instance

The writer's finding holds and is worth recording about the template. The Evaluation Group's review of
P095949, 14 October 2014, section 11a, puts the following inside quotation marks and attributes it to
the completion report:

> The ICR states, "The project was generally in compliance with safeguards policies, and only in
> limited cases did physical works begin before all affected persons had been compensated or
> resettled.

The completion report's sentence is "The project was generally implemented in compliance with
safeguards policies, but in several cases did works start with sites still occupied by affected
persons, or compensation of affected persons was not assured before commencement of works." The
string "limited cases" does not appear anywhere in the completion report — a grep returns twelve hits
for "limited", none of them this. The rewrite runs one way: "but in several cases" becomes "and only
in limited cases", and the clause about works starting on sites still occupied by affected persons
disappears. The opening quotation mark is never closed.

**A second instance in the same review**, section 8, which the writer did not report: "The ICR (page
10) had reported some 2700 persons temporarily relocated as a result of the rehabilitation of the
Central Market in Maradi." The completion report says 2,712 persons were **affected**, of whom 2,586
traders were affected by the temporary and voluntary relocation. The review converts "affected" to
"temporarily relocated", drops "voluntary", and rounds a figure it attributes to a page.

Both are in the review's own prose about a named page of a named document. Where a card quotes the
review's account of a completion report, the completion report has to be opened.

---

## 7. Did the briefs help or mislead?

**The plan-reprint check, as delivered, was close to useless on this batch, and in one row actively
wrong.**

- **It missed the batch's only real reprint.** P120636 carries `reprint_flags: 0` and its brief lists
  no reprint candidates, yet the six farmers on which that card rests are the October 2010 plan's own
  census count and are in the appraisal document as well. The check is the thing that should have
  caught it and did not.
- **It treats resettlement plans as outcome documents.** On P122776 and P079749, every flagged figure
  has an `RP` document on the "outcome" side of the pair — on P122776 the same 2011 resettlement plan
  appears on both sides of one flag, once decoded and once mojibaked, so the tool matched a document
  against itself. All six flags on those two rows are artifacts.
- **It matches policy recitals and footnote numbers.** P079749's two flags are the OP 4.12
  abbreviated-plan threshold ("fewer than 200 people are displaced") and footnote 21 of OP 4.12,
  identical in two frameworks because both quote the policy. P122776's flags include "10" from a
  numbered heading and "100 ha / 80 ha" of land requirements for a railway and a road.
- **Where it did fire usefully, nobody used it.** P122402's flagged 15 is a real and sharp find — the
  plan's shops reprinted as the outcome document's people — and the writer did not address it. That
  flag alone justifies the mechanism; it needs a reader.
- **`relocation_counts_in_outcome_doc` is null for all 22 rows**, including P112131, whose outcome
  document contains "the 250 persons who had to temporarily move their homes or businesses", and
  P079749, whose outcome documents both contain "seven households were resettled". The field found
  nothing that was there.

**One brief gives a flatly wrong instruction.** P087004's document list annotates the 2005 appraisal
document: "**<- filed as a plan but reads as an outcome document; treat its figures as outcomes**".
It is a Project Appraisal Document. Its named-landowner table with Georgina Melo's 200 m² is an
appraisal-stage estimate. A writer who followed that instruction would have written a case from an
appraisal table. This writer did not, but the annotation should be removed before any further round
uses these briefs.

**What helped.** The document paths and the complete per-row document lists. Four of the nine cases
turn on passages no candidate sentence surfaced, which the writer reported accurately — and I would add
the sharper version: the two documents that decided the most in this batch, P117652's abbreviated
resettlement plan and P120636's abbreviated plan, were both in the brief's document list with nothing
quoted from either, and both overturn something a card said. The briefs are useful as an index of what
is on disk and should not be read as an index of what matters.

**Noise confirmed.** The "household-loss table label (incl. French)" bucket and the "PLAN VERB" bucket
were as the writer describes. The writer's proposed addition — concessive phrases inside the
safeguards section ("albeit", "but in several cases", "had not been done by", "were not adequately") —
is sound and I can confirm it reaches the deciding sentence on six of the seven surviving cases. It
would not have reached P117652's or P120636's, whose deciding sentences are in a plan.

---

## 8. Anything I could not check, by route

- **P111338, Lomé Infrastructure Rehabilitation and Maintenance (Togo): no outcome document.** I did
  not re-run the queries; I checked the writer's account against what is on disk, which is one
  document, the April 2008 resettlement policy framework, and read it. The two routes the writer names
  as having failed — `wds?format=json&projectid=P111338` returning one document, and
  `projects?countrycode_exact=TG&rows=100` returning 159 Togo projects with no parent or sibling — are
  list-query routes, and both returned data rather than being refused. **The route BRIEF31 names as
  the one it has not tried is the `qterm` title search**, which that brief says found evaluation
  reviews for five of this round's projects that the `projectid` query returned nothing for. The
  writer's account does not say whether a title search on "Lomé Infrastructure Rehabilitation" was
  run. Until it is, "no outcome document exists" is not established; what is established is that the
  `projectid` route and the country-list route do not reach one. The drop stands either way, because a
  framework records no harm.
- **Underlying documents cited by date and not disclosed.** P122402's footnote 49 cites a MOICI
  Monitoring Report on the Resettlement Payment of 7 October 2014 and a Supervision Mission
  Aide-Mémoire of 19–23 January 2015; P122776's footnote 77 cites a project unit report of 11 March
  2021. None is public and none is on disk. The six-of-15 and the 129-of-168 therefore rest on the
  completion report's report of them, which is what the cards say.
- **No independent corroboration sought.** I spent no search budget. All seven cases are `contested`
  and each `confidence_note` says who is reporting on whom. On P117652 the core harm rests on the
  Evaluation Group's own field-based assessment report, which is closer to a field study than a desk
  review but is still the lender's own evaluation arm and is the only document carrying the numbers:
  `contested` either way, and the note says so.
- **Dates on the newer review template.** Verified independently: `grep` for "Date Posted" and for any
  ISO or numeric date in the body returns zero on all five of the reviews concerned (P079749 2016,
  P112131, P120636 2020, P122402, P122776). The template carries no date. The archive `docdt` stands
  and four of the five cards say so in `lenders[0].role`. The fifth, P079749, cites its 2016 review
  only in `sources`, with the archive date and no annotation; the card's dated statements all come
  from the assessment report's cover (APRIL 19, 2018) and the completion report's cover (December 31,
  2015), so nothing rests on it. Worth a convention: a source entry whose date is the archive's rather
  than the document's should say so wherever it appears.
- **Source URLs.** Checked mechanically, not by fetching: every one of the 32 URLs on the nine
  submitted cases matches a URL in `harvest_manifest.json` after the prescribed
  `documents.worldbank.org` → `documents1.worldbank.org` rewrite and the http→https upgrade, and every
  source `date` matches that record's `docdt` to the day. No URL was constructed and no date was taken
  off a filename. I did not re-request them; the writer reports all 32 returned 200 or 206.

---

## 9. Faults appearing in more than one card

1. **Arithmetic presented as a document's figure.** Three cards: "Nine of fifteen … were never paid"
   (P122402), "39 of the 168 complaints unresolved" (P122776), "39 per cent of the RN2 payments never
   made" (P088619). In each the document gives one side and the card prints the complement. Two of the
   three also shift tense: "unresolved" and "never made" where the documents say the rest was still
   being processed or still being paid as funds allowed. This is the one fault that runs right through
   the batch and all three were in titles or outcome fields, the most-read prose on a card.
2. **A figure's provenance in a plan left off the card.** P120636 (six farmers), P122402 (the 15),
   P117652 (the seven, though there the plan is what corrects the card). In none of the three does the
   reprint sink the case, because the outcome document attaches a completed verb in each — but in none
   of the three did the card tell the reader the number started in a plan.
3. **A harm attached to a site the document does not attach it to.** P095949 (`place` naming the
   Maradi market and sites in Niamey and Dosso; now cut) and P093826 (`place` naming the Gorgol and
   Trarza wilayas). Both cards' `point` notes admitted the inference while `place` asserted it. The
   `point` note is doing honest work that `place` then undoes.
4. **The Evaluation Group's reviews rewriting the completion report they quote.** P095949 twice (the
   phantom quotation; "affected" to "temporarily relocated"), P122776 (a 41 per cent subset made the
   whole), P093826 (ten triggered policies reduced to one, and a paraphrase that stops one sentence
   short of the harm), P117652 (seven made six, and the report's own risk rating misprinted in the
   review's column for it), P104456 and P095949 again (rating-column substitutions). Six of the eight
   projects with a review show the review altering something it cites. The standing instruction to read
   every rating out of the document that gave it should be extended: read every *figure* and every
   *quotation* out of the document that gave it, because the review's quotation marks are not
   reliable.

## 10. Outside the fields I was asked to check

- **`lenders[0].role`, one substantive error found**, on P120636: a reason for a rating change that no
  document gives, in a field written last and checked by nobody. Round 22's finding holds. Everything
  else in that field across the nine cases — five multi-credit financing tables, every approval,
  effectiveness, mid-term, original-closing and actual-closing date, every report number, every
  environmental category, every policy list — checked out against the data sheets line by line, which
  is a better result than round 22's 19 of 46.
- **`companies`, two judgement calls I left standing and am flagging rather than editing.** P112131
  lists Assistance Sans Frontière, a non-governmental organisation, beside the two ministry
  directorates; P122402 lists SAL Consult Limited, the consultancy that wrote the plan, beside the
  ministry and the telecommunications company whose dispute the report names as the cause of the
  delay. Neither is an oversight body and the documents put both on the project — the completion report
  puts ASF in the compensation sentence itself — so neither breaches the rule as written, but both
  read as implicating a party the documents do not blame. P112131 is now a drop, so only SAL Consult
  survives. The lead may want to decide whether a plan-writing consultant belongs in `companies` on a
  card about the plan not being carried out.
- **Geometry.** P079749 carries `displaced: 7` for seven households in Mali on a point in Sakoinsé,
  Burkina Faso, because no document places the Malian households. The card says so in
  `confidence_note`. It is honest and it is still a card whose number and whose dot are in different
  countries.
