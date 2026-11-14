# Check log — round 21, batch B (non-China road and urban rows)

Checked file: `/home/claude/r21/r26f_icij5_road_other.json` (6 cases, 1 extend)
Output: `/home/claude/r21/r26f_icij5_road_other_checked.json`
Documents read from `/home/claude/r21/cache/` (`.txt` renderings, with `pdftotext -layout` re-runs on
three freshly re-fetched PDFs to confirm the cache matched the cited URLs).

Result: **5 cases kept, 1 case cut, 1 extend kept, 4 drops confirmed.** Nine corrections across three
cards, one of them a wrong document number in both a source title and a lender role.

---

## 1. `corridor-x-dimitrovgrad-bypass-serbia` — kept, `documented`, four corrections

Verified hardest, as instructed. Everything the task listed is in the end-of-term impact evaluation of
12 July 2016, at the pages given below, and the wording is close to the document's own.

Confirmed:
- **Three physically displaced households.** "There were only 13 case where the expropriated structures
  included houses, and out of those only 3 included physical relocation" (p. 23); six of seven residential
  structures at CM Dimitrovgrad are weekend houses, one was derelict with nobody living there, three of six
  houses at CM Gradinje are weekend homes. `displaced: 3` is the document's count of households
  relocated, not an "affected" figure. Correct field, correct label.
- **No allowances.** For the first household: "there is no evidence that the compensation included moving
  allowance as prescribed by the law. They also didn't receive any transitional allowance as required by
  RPF." For the second: "There is no evidence in this case either." For Kolev: "He did not receive any
  additional compensation in terms of moving allowance for his household or the business, or transitional
  allowance." Serbian law prescribes a moving allowance in cases of physical relocation "but it doesn't
  prescribe transitional allowance"; the RPF required the transitional allowance. Card correct.
- **Vasil Kolev**, named in the document: 140 m² structure fully expropriated, registered auto repair
  workshop on the ground floor and the residence above, replacement value assessed at about EUR 27,000 or
  EUR 160/m², notice in 2008, authorities "irresponsive to his appeal to re-assess", no compensation for
  loss of business or income, valuation "evaluated for construction value only" so equipment was not
  valued and he removed it at his own cost, loss of the workshop meant the household "lost the only source
  of income", age 60, part-time handyman, wife disabled from birth, daughter a trained hairdresser not in
  full-time work, property prices risen, now lives in his late father's house. All confirmed verbatim.
- **The evaluation's own finding**: "In the case of affected business it appears that that basic
  requirements of the Resettlement Policy Framework were not met. The compensation offered to the PAP to
  date is not compliant with the provisions of the RPF." The card drops the document's hedge "it appears
  that"; left as is, because the consultant separately confirmed from the valuation report that only
  construction value was assessed, but the hedge is noted here.
- **`killed: 3` — countable.** The ICR (p. 21) records three separate fatal accidents at the sites,
  September 2013 at Grabovnica-Grdelica and November 2014 and February 2017 at the Dimitrovgrad bypass,
  and attributes them to "unsatisfactory management of site safety"; the IEG review downrates Bank
  supervision for that same reason and states "there were three fatalities during highway construction".
  Both documents therefore attribute three construction deaths to unsatisfactory site-safety management.
  These are deaths on the works the loan financed, so they count; the card's note that neither document
  names the dead or says whether there was negligence is the review's own statement and is accurate.
- **Over 100 households affected by blasting** — in the document, but see correction (b).
- **Land figures.** ICR: 322.7 ha / 2,092 cases on the original three sections, 371.8 ha / 2,491 with Lot
  6. PAD, paras 59 and 220-221: 50 + 130 + 50 = 230 ha expected. Both confirmed; rule 2 passes (the
  outcome figures are nowhere in the appraisal).
- **Loan arithmetic.** 388,000,000 committed / 335,213,259 disbursed, AF 38,900,000 / 40,340,629,
  borrower 60,000,000 planned against 7,240,000 actual, total 486.9m against 382,793,888 — all on the ICR
  data sheet. Ratings: ICR outcome Satisfactory, Bank performance Satisfactory, M&E Substantial; IEG
  Satisfactory / Moderately Satisfactory / Substantial, downrated for site safety. Confirmed in each
  document itself, not out of the other's column.
- **N1, 24 November 2016, independent.** N1 is a Serbian commercial news broadcaster, not the Bank and
  not the borrower, and the piece is by its own reporter (Gordana Bjeletić). The content the card draws
  is there: Gradina near Dimitrovgrad, works a few metres from houses for five years, cracks inside and
  out, most residents want to move, at least five firms worked the section and were all asked for
  compensation while the damage grew, letters to several authorities asking to be relocated and another
  the week before, a threat to block the blasting, Koridori Srbije gave no official response, unofficially
  no expropriation at this stage and compensation only after all work finishes, and Corridor
  representatives promised compensation once blasting ended. Both residents' quotes are in the article.

Corrected:
- (a) **`ICRR0022470` is the wrong report number.** The review of this project is **ICRR0022096** — on the
  cover of the cached file and of the file freshly re-fetched from the cited URL. Fixed in the source
  title and in `lenders[0].role`.
- (b) **"the evaluation records as having affected over 100 households"** overstated the attribution. The
  document says "According to the Municipality representatives, over 100 households were impacted to
  various extent during blasting activities", and adds "About 20 households were severely affected by
  blasting in Gradinje". Both now on the card, with the attribution.
- (c) **An absence claim refuted by the cited document.** The card said no document records whether the
  households affected by blasting were compensated. The same evaluation (p. 32) says compensation for
  blasting damage was being paid by the insurer Wiener Städtische but "only five cases have been
  compensated to date" and the claim process is long, and that damage to houses in and around Sutjeska
  Street in Dimitrovgrad "was reimbursed for five households from the Contractor bank guarantee, based on
  court decisions", with cases still pending in court. Rewritten; the surviving absence is now that no
  document gives a final total.
- (d) **"court-appointed experts had said the buildings were not safe to live in"** is not in N1. The
  article has a resident, Nebojša Ivanov, saying "Bili su veštaci. Kažu da objekat nije bezbedan za
  stanovanje" — experts came and said the building is not safe to live in — and that he will sue if he
  cannot agree with Koridori Srbije. The article does not say who engaged them and does not say *sudski
  veštaci*. Rewritten on the card and in `confidence_note`. Slavka Gligorijev's "daily disruption" was
  also a characterisation and is now what she said: she is waiting for the works to end and does not know
  what will be done about the damaged houses.
- (e) **`lenders[0].role` claimed both documents rated social management and environmental management
  Moderately Satisfactory.** The ICR does (paras 65 and 66). The IEG review gives **no** separate rating
  for either: its "Moderately Satisfactory" lines are quality of supervision and overall Bank performance,
  and its safeguards section reproduces the ICR's text and reports the ICR's statement that "overall
  compliance with the environmental safeguards policies was adequate". Corrected and that favourable
  clause added.
- (f) The review prints no date anywhere on its pages (report number only). The BRIEF21 finding-3 caveat
  was on four of the six review-sourced cards but not this one; added.

`confidence: documented` **kept.** One of the two harms in the title — cracked houses from blasting — is
corroborated by independent press. The other — the uncompensated workshop and the unpaid allowances —
rests on a single source, a field evaluation commissioned by the state company that ran the works, and
`confidence_note` says that plainly, naming who is reporting on whom.

Timing: the three displacements and the Kolev expropriation were completed in Phase 1, 2008-2009, "prior
to IFIs involvement" (evaluation p. 24), and the PAD said in advance that the first 5.9 km from Prosek
would not be subject to the RPF. What sits inside the loan is the Bank-endorsed framework under which the
allowances were owed on the Bank-financed 8.67 km section, the evaluation's finding that they were not
paid, and the construction impacts. The card states this; the test passes, but it is the one point on
this card a reader will press.

## 2. `baoro-bouar-road-house-damage-car` — kept, `killed: 1` upheld, premise verified

**The ruling's premise holds.** The September 2019 fatal accident was on works this credit financed. The
footnote (ICR footnote 29) hangs off paragraph 77, "In Cameroon, the project has reported six OHS
incidents since the start of works" — occupational incidents on the project. The Cameroon road works were
the project's own: "the Mora – Dabanga (131.5 km) and Dabanga - Kousseri (72 km) major ongoing road works
contracts **funded under the project** were suspended" after the May 2014 Boko Haram attack (para on
factors affecting implementation), the 2017 Level 1 restructuring approved their resumption, and from the
June 2018 restructuring they were carried out by the Army Corps of Engineers under an output-based
disbursement force account. No other financier's works and no other country's credit is in play. So the
death is this project's: `killed: 1` stands and `iso3_more` already carries `CMR` (and `TCD`, which the
Chad safeguards failures on the card support). `killed_note` rewritten to say why it is countable and to
drop the speculation that the person might have been a road user — the report classes it as occupational.

Confirmed verbatim from ICR paragraph 84: 1,350 complaints registered over one year on the Baoro-Bouar
works, 1,289 reviewed, 61 not yet reviewed because of the conflict of December 2020 and left to the
coordination unit with payment if needed through the rural connectivity project, about 518 validated and
notified for compensation in cash or kind, of which 429 for house cracking from vibration and 89 for other
damage (trees, animals), and of the 89, 51 paid FCFA 2,168,000 and 48 outstanding for FCFA 2,425,500.
Cameroon: all complaints about land lost to machinery, all processed and closed. Chad: no complaint
received. Paragraph 82's safeguards failures (reforestation, Army Corps labour-law non-compliance with
social-insurance affiliation, hiring medicals and non-payment of wages, Chad's missing audit and the
customs-site waste, CAR's unrehabilitated quarries) are all as the card has them.

Corrected:
- (a) The card omitted the favourable clause opening the same paragraph: "Grievance Redress Mechanism
  (GRM) implementation at project closing was Satisfactory." Added.
- (b) **"The works on the Baoro-Bouar road were not completed at closure"** is one of two things the same
  report says. Paragraph 40 lists "Baoro-Bouar (56 km, in CAR)" among five road sections "completed at
  project closing"; the factors-affecting-implementation section says the works "were not completed at the
  time of project closure after 34 months of work instead of the 20 months initially planned". Both now on
  the card, labelled.
- (c) `confidence_note` called the review's "all the complaints" sentence a contradiction of the report's
  numbers. It is not quite that: in the ICR the sentence is about **Cameroon alone**, where every complaint
  was about land lost to machinery and all were closed. The review reprints it with the country stripped,
  so it reads as covering the project, while the report's CAR figures sit two bullets below. Rewritten to
  say exactly that. This was one of the three reported disagreements I was told to test; it is a scope
  error in the review, not a conflict between two counts.

`confidence: contested` correct — the Bank reporting on its own project, nothing independent found.

## 3. `agona-elubo-corridor-compensation-ghana` — **cut** (`status: dropped`, reason on the card)

Read both documents. The writer's expectation is right, and all three of the stacked problems check out.

- The review's PAP counts are the appraisal's, word for word. PAD paragraph 97: "(i) Benin: 101 households
  (404 persons); (ii) Togo 379 households, (1,920 persons); and (iii) Ghana 744 households (2,094 persons)
  (about US$7.8 million)", repeated in Annex 10. The review prints the identical string with no
  attribution. BRIEF21 rule 2 at one remove, confirmed.
- **And the appraisal figure is itself mislabelled.** The Ghana resettlement action plan of November 2009
  gives 744 as the number of "Fully and Partially Affected Building Structures (Total)" — 231 permanent and
  513 temporary — and "it was estimated that seven hundred and forty-four (744) structures along the
  project road will be affected". The appraisal turned 744 structures into 744 households. The plan's own
  person counts (1,441 males, 576 females, 50 unknown) sum to 2,067, not 2,094. So the number the review
  prints as a project-affected-person count is a plan count of buildings.
- The later figures are prefaced "The project team provided following additional information to IEG",
  with "(This information is available and fully detailed in the last ISR)". A staff statement, not a
  document. BRIEF20 trap 4.
- The only outcome finding is the review quoting ICR paragraph 82: at closing OP 4.12 "was not complied
  with as approximately 11% of PAPs still needed to be paid". No number of people, and no denominator in
  any document — 2,094 is the plan, 5,416 is the staff statement.

**Neither limb of the forward rule is met.** Limb (a): no document counts anyone relocated; the 2,094 paid
in December 2012 is a payment count equal to the plan figure, before works began. Limb (b): the only
recorded shortfall is a percentage — no count of people, no named person, no sum outstanding, no date by
which anyone was still unpaid. The review's list of social impacts ("loss of residential houses,
businesses, temporary structures") is a generic safeguards-section list, not a demolition table, so
BRIEF21 rule 1 does not rescue it. Against that sit the review's statements that compensation was
completed within a month of closing and full plan implementation achieved in August 2017.

The Ghanaian Times near-miss was correctly kept off the card and should stay off: Lot 1 of a later
corridor project, nine years after this credit closed.

## 4. The extend to `webuye-interchange-traders` — kept

Shape: five keys at top level (`extend`, `lenders_add`, `sources_add`, `fields_add`, `cp_add`) ✓.
`fields_add` has one key, `community`, and its value is a string ✓. (It opens with a single leading space,
which is presumably deliberate for appending; flagging it so the merge does not double-space.)

The death is in the document and the cause makes it countable. ICR annex, paragraph 41, Kakamega–Webuye
road section: a complainant to the Bank's Grievance Redress Service alleged "A fatal accident involving a
worker on site"; the task team's mission "confirmed … (a) That there was a fatal accident on site
involving an operator of an excavator. The accident had been reported to the Police when it happened, and
the Police took over the case. The Task team followed up with KeNHA and ensured that the family of the
deceased was compensated as per the Kenyan law." A worker killed on site by project works, one person
("the family of the deceased", singular), an exact count, not a floor. Under the `killed` rule this is a
death the project caused and it counts. The 13 small business tenants omitted from the plan and paid KES
20,000 each in April 2020, the market for the 52 mobile traders omitted from the 2011 plan, the five
security dogs and the bitten worker treated at a local hospital, the unsubstantiated sexual-exploitation
allegation, the unconfirmed summary dismissals, the Gimu interchange delay, the Bachuma Gate escrow case
and the 13 April 2022 notice of non-registration are all confirmed in the ICR and the Panel notice.

**Values for the lead to set by hand on `webuye-interchange-traders`:**

```
"killed": 1,
"killed_note": "The Bank's completion report of 29 January 2021 records that a complaint to the Bank's
Grievance Redress Service about the Kakamega to Webuye road section alleged a fatal accident involving a
worker on site, and that a Bank mission confirmed that there had been a fatal accident on site involving
the operator of an excavator. The accident was reported to the police when it happened and the police took
over the case, and the Bank team followed up with the Kenya National Highways Authority to ensure the
family of the deceased was compensated under Kenyan law. The report does not name the person, give the
date of the accident or say what caused it. The death was on the Kakamega to Webuye section of the
project's road works, not at the Webuye interchange where the card's point sits."
```

One other thing for the lead: the existing card's `end` is 2020 and the project closed 31 December 2020,
but the extend's last fact is the Panel's notice of 13 April 2022. Either leave `end` at the closing year
and let the 2022 notice sit in the text, or move it; it should be a decision, not an oversight.

## 5. The four drops — all confirmed on the documents

Round 17's lesson was applied: I looked for a documented resettlement in each, not for a recorded failure.
None of the four has one.

- **Kiribati P122151.** ICR paras 81-82: residential land permanently acquired for about 200 bus stopping
  places, 17 drainage easements and 56 minor realignments; "the affected strips of private land amounted
  to 8,256m2 and 131 trees belonging to 348 households, but these represented a minor portion of affected
  households' yards with no serious impacts on incomes or livelihoods"; 317 PAPs compensated, 22 held in
  escrow; 111 complaints, with an independent NGO review confirming all grievances at the time of its
  assessment had been appropriately addressed. The 2013 resettlement plan: "(iii) No loss of primary and
  secondary structures and no relocation of households", "(iv) No loss of agricultural land", "(vi) No
  Project cases of economic resettlement and vulnerable people". Land area plus an affected count. Drop
  correct.
- **Rajasthan P130164.** ICR para 70 verbatim as quoted in the writer's report: "There were no major
  resettlement issues. Most roads were built or upgraded in the right-of-way. Land acquisition was mainly
  handled through voluntary donations". No count of donors, no hectares, no relocation. The one
  non-compliance is works completed on 26 roads before forest clearance (para 71), which harms no
  identified person. Drop correct. *Report-level correction:* the cached project resettlement plan
  (`P130164_RAP_SIA`) is for **SH-2, Dausa–Chaksu–Phagi–Dudu including the Dausa bypass, 140 km**, not the
  Deeg–Alwar–Behror SH-14 corridor the writer's report names.
- **Indonesia P079906.** ICR para 36: "All land acquisitions which took place in SRIP's subprojects were
  carried out in a satisfactory manner… All cash compensation was paid at or above market price by using
  local bank land market price information as a basis for compensation negotiation"; 5 subprojects had
  tracer studies, 15 had resettlement plans. The IEG review adds nothing. No count of anyone relocated and
  no recorded shortfall. Drop correct. One item worth recording, because it is the only thing in the four
  drops that touches displacement: borrower lesson 34 in the ICR annex says that on a few packages land
  "previously been acquired" had new squatters because of "the long time between the removal of the
  original tenants and the start of construction", and advises local government to secure acquired land
  "in order to avoid paying compensation". No count, no date, no identified people, and the acquisitions
  concerned pre-date Bank financing. Not enough to recover; a lead if anyone ever gets the tracer studies.
- **Georgia P112523.** The sentence is there, twice. The 2009 resettlement plan: "No physical relocation
  of households is required. Land will be acquired and buildings will be demolished for the three existing
  businesses (all petrol stations)", and later "six (6) households will lose part of the residential plots.
  No physical relocation will be necessary." ICR para 45: "the latest updated figures show that 2393
  people (617 households) have been affected and in total, 736 land plots (land area of 1.318.448m²) have
  been acquired", and "Though the Project was closed on June 30, 2016, resettlement activities are still
  not completed" — and the next sentence is the two parallel access roads, paved completed November 2016,
  gravel expected April 2017, confirming the writer's reading. Para 46 rates OP 4.12 compliance "mainly …
  satisfactory", downgraded to Moderately Satisfactory at the end for delays in updating the plan,
  reporting gaps and understaffing. Hectares plus an affected count, and the only demolitions (three
  petrol stations, nine workers made redundant) are plan figures the ICR never returns to. Drop correct.

## 6. The eleven reported document disagreements — three of eleven are real

Checked each for the quantity measured and the date measured at, as instructed.

**Genuine conflicts of fact (2):**
1. **P081505 Board approval date.** ICR data sheet: "Approval: 06/03/2004". IEG review data sheet: "Board
   Approval Date : 06/15/2004". Same quantity, same event, two values. The ICR's narrative says only
   "Board approval in June". Real, and one of the two is wrong.
2. **P079736, where the halted road is.** IEG review: "issues pertaining to the abrupt halt on the
   construction of the Baoro-Bour road **in Chad**". ICR para 82: "In CAR, (iv) the abrupt halt to the
   construction of the Baoro-Bouar road…". Baoro and Bouar are both in the Central African Republic. Real,
   and the review is wrong.

**A conflict inside one document (1), which the writer did not report:**
3. **P079736, whether Baoro-Bouar was finished.** ICR para 40 lists it among five sections "completed at
   project closing"; the factors-affecting-implementation section says the works "were not completed at the
   time of project closure". Same report, same date, two answers. Now on the card.

**Not conflicts (4):**
- P108005 230 ha expected against 322.7/371.8 ha taken — appraisal against outcome, a before-and-after.
  This is the rule-2 evidence, not a disagreement.
- P108005 33 structures in the plan against 30 cases in the road enterprise's records — the evaluation
  states the difference itself and explains it (cases bundling a house with wells, fences and storage).
  A sourced reconciliation, not two documents at odds.
- P081505 "about US$ 160 million equivalent" in the ICR text against US$158.43 million in the ICR cost
  table — rounding inside one document.
- P096407 PAP counts — the review reprinting the appraisal. Rule 2, not a disagreement.

**The ordinary ICR-against-IEG rating gap (4):** P108005 Bank performance (S / MS), P081505 outcome and
Bank performance (MU/MU / U/U), P112956 outcome (S / MS), P079736 Bank performance (MS / MU). Each was
read out of its own document and each is confirmed; the review's own ratings table prints the gap and its
reason. These are what the two documents are for, not findings. Worth saying because listing them as
"disagreements" inflates the count from three to eleven.

## 7. Rule 2 — four spot-checks, all four pass except Ghana

- **Serbia**: ICR 322.7 ha / 2,092 cases and 371.8 / 2,491 appear nowhere in the PAD, which expects 230 ha
  and says "The number of project affected households is not known at this stage". Passes.
- **Jordan**: ICR 3,028 affected, 440 ha / 850 plots / 2,250 PAPs and 500 ha / 240 plots / 778 PAPs — none
  in the PAD or the February 2004 plan. The PAD does carry **500 ha** as the planned minimum area for the
  depot site ("at least 500 ha"), so that one number is both plan and outcome; the plot and person counts
  are outcome only. Passes, with that noted.
- **Albania**: 23 / 12 / 338 households and the two compensation totals are in the ICR only; the PAD has
  no household counts at all. Passes.
- **Nigeria**: ICR 2,231 with its eight-site footnote is not in the PAD or the June 2012 plan, whose
  figures are 1,171 PAPs "to be relocated" and 112 structures to be demolished — the card uses neither.
  Passes.
- **Ghana**: fails, as above, and the card is cut.

## 8. The finding to test — the documents bear it out

Sector does not separate the cases from the drops in this batch. Eight of the eleven rows are tagged
`road`; four of those eight are cases and four are drops. Georgia and Kiribati carry the same tag as
Serbia and Albania.

What separates them is what the works took. The five surviving cases each record a dwelling, a shop, a
market pitch or a house damaged beyond use: 3 households relocated and a workshop taken with no
compensation for the business (Serbia); 23 households relocated and 12 commercial structures lost
(Albania); about 300 owners and occupants who had to find new places to live (Jordan); market and street
traders moved and moved again (Nigeria); 429 complaints of houses cracking from blasting (CEMAC). The four
drops each record strips of land, yards, trees or donated right-of-way, compensated at or above market
price, with nobody losing a dwelling or a trading place.

**The proposed pre-screen is available in three of the four drops, and it says the same thing each time.**
Georgia's 2009 plan: "No physical relocation of households is required." Kiribati's 2013 plan: "No loss of
primary and secondary structures and no relocation of households." Rajasthan's published plan: "No
displacement / Resettlement is required." Indonesia is the exception and shows the limit: there is no
single project plan to grep — fifteen subproject plans and five tracer studies, none of them a disclosed
document in the cache. So the screen would have sorted three of these four rows out before any document
work, and would have left the fourth untouched. On the other side it does not produce false drops here:
Nigeria's plan says 1,171 people will be relocated, and Serbia's framework and section plans provide for
physical relocation and allowances. Recommend it for round 22 as a first pass, with the caveat that a
project whose resettlement instrument is a framework plus many subproject plans is not screenable this way
and still needs the completion report read.

---

## Required closing items

**1. What I could not check, and what stopped me.**
- The Jordanian, Albanian and French-language absence claims. I did not re-run those searches; the cards
  now state them as "no independent account was found" rather than as a record of searching, which is what
  that form of claim can carry.
- Whether the Serbia evaluation's recommendations were ever acted on, and the fate of Kolev's
  re-expropriation claim. Nothing after 12 July 2016 was found; the ICR of 24 March 2020 does not return
  to either.
- The Ghana completion report. It is not in the cache and the review quotes it by paragraph; I confirmed
  only that the review's quoted strings are internally consistent and that its PAP counts come from the
  appraisal. I did not retry the document routes for it.
- The exact Serbian wording of the N1 quotes was verified through a fetch of the article, not from a
  stored copy; nothing in the batch is cached for N1.

**2. Figures where two documents disagree.** The three in §6 above: P081505 Board approval date (ICR
06/03/2004 against IEG review 06/15/2004); P079736 the halted road's country (ICR, Central African
Republic, against IEG review, Chad); and inside the P079736 ICR itself, Baoro-Bouar listed as completed at
closing in paragraph 40 and as not completed at closure in the factors-affecting section. Also, outside
the writer's list: the Ghana resettlement plan's 744 is a count of **structures** (231 permanent, 513
temporary) where the appraisal and the review print 744 **households**, and the plan's own person counts
sum to 2,067 against the appraisal's 2,094.

**3. Faults in more than one card.**
- **Attribution slipping up a level.** Serbia: a municipality's statement presented as the evaluation's
  finding, and a resident's statement about experts presented as N1's. CEMAC: a Cameroon-only sentence
  presented as a project-wide claim — though there the slip is the review's and the card inherited it.
  Three instances, all in the same direction: the weaker speaker is replaced by the stronger one.
- **The favourable clause in the same paragraph left out.** Serbia: the review's "overall safeguards
  compliance was deemed adequate". CEMAC: "GRM implementation at project closing was Satisfactory". Two
  instances; both were in the paragraph the card quoted from.
- **Absence claims that the cited document refutes.** One, on Serbia, and it was the largest single
  correction in the batch. Worth noting that the refutation sat ten pages from the quoted passage in the
  same file.

**4. Wrong in the card data outside the fields I was asked to check.**
- **`ICRR0022470` for Serbia is wrong in two places** — `lenders[0].role` and a source title. The document
  is ICRR0022096. This is the fault CHECK20 §5 warns about: substantively right, uncitable as cited. Fixed.
- **`lenders[0].role` for Serbia attributed two safeguard ratings to a document that gives neither.**
  Fixed. (Second round running that a checker has found a factual error inside `lenders[0].role`.)
- **Three source `date` fields assert a day the document does not give**: Nigeria's resettlement plan
  (`2012-06-01`, cover says "June 2012"), Ghana's (`2009-11-01`, cover "NOVEMBER, 2009"), Jordan's
  (`2004-02-01`, cover "February 2004"). Left as they are because the field looks schema-bound, but
  BRIEF20 says a month-only document gives a month only; the lead should decide whether the schema can
  hold `2012-06`.
- **The Jordan plan's source title says "land acquisition and resettlement plan update"** where the
  document's own cover says "LAND ACQUISITION & RESETTLEMENT PLAN", Rev C, February 2004. Probably the
  archive's catalogue title; noted rather than changed.
- **Nigeria's `point` text carries a derived figure** — "1,045 of the project's 2,231 affected people" is
  473 + 572 from the ICR footnote, added by the writer. Transparent, both numbers labelled in the
  document, but it is arithmetic the document does not do.
- Loan arithmetic checked on three cards (Serbia, Albania, Nigeria) against the data sheets, including the
  cancellations of EUR 220,630.46 and SDR 368,625.00 and the US$14,890,705 exchange loss: all correct.
- All 25 source URLs resolve: 24 PDFs with `200 application/pdf` and the N1 page with `200 text/html`. The
  Serbia evaluation, the Jordan review and the Ghana review were re-fetched and their covers match their
  cited titles, dates and report numbers.

**5. Routes that failed.** None of mine failed. The 25 cited URLs all answered on first request through
`curl -L`, and `pdftotext -layout` rendered every PDF re-fetched. Of the writer's reported failures, one
is worth restating as a route and not a host: `curl -L` to `irep.ntu.ac.uk` returning HTML for a PDF path
is one URL on one route, and the host was never tried through a fetch tool — it is not a blocked host. The
Ghana completion report's absence is an absence under `wds?projectid=`, under the sibling number and under
a `qterm` title search, which is three routes and not a verdict on the document; I did not retry them.

Nothing merged, `build.py` not run, git untouched.
