# Check log — Case Map ICIJ tranche 7 (round 31), ECA batch

Checked file: `/home/claude/work/out/eca.json` (8 written cases, 7 drops).
Corrected file: `/home/claude/work/out/eca_checked.json` (6 cases, 9 drops).

**No writer's report exists.** `/home/claude/work/out/eca_report.md` was not written, so BRIEF31's two
closing requirements — name your own two weakest entries, and say whether the pre-extraction helped —
were not delivered for this batch. The other four batches in `/home/claude/work/out/` have reports.
The two weakest entries are named below by the checker instead.

Also missing: `/home/claude/work/batch/eca.json`, named in the check task. That directory holds only
`china_eastasia.json` and `east_southern_africa.json`. The batch's composition was recovered from
`/home/claude/work/batch_manifest.json`, which lists the 15 ECA P-numbers, and all 15 match the rows in
the written file. Documents were read from `/home/claude/work/cache/<PID>/` as instructed; nothing was
re-fetched from the Bank.

---

## Cuts

### 1. `yenice-logistic-village-urgent-expropriation` (Turkey, P077328) — CUT

Deciding document and sentence: completion report of 3 December 2015, paragraph 33 — *"During the course
of project implementation, the need for land acquisition arose at passing loops and near Yenice Logistic
Village (which was not financed by the Bank but adjacent to the project)."* The appraisal document of
12 May 2005 did not trigger OP 4.12 and says *"No resettlement or land acquisition is involved."*

The card's entire factual content about what happened at Yenice is the urgent expropriation of 2008 to
2010 for the logistics village: a TCDD board decision of 25 January 2008, a Council of Ministers decree
of 31 March 2008, court valuations, money remitted into owners' accounts on 30 June 2010, 43 valuation
suits filed on 14 July 2010. Every element of that predates the Bank's 2011 restructuring, by which the
Bank first required a resettlement plan covering Yenice, and none of it is on works the loan financed.
This is the shape of the precedent cut CHECK20 records — the 942 households on an airport platform the
Bank had determined was not an associated facility of the road credit. The project's own land take (74
parcels, 41 households, three houses) exists only as a plan figure with no outcome document behind it.

Limb (b) is not the reason for the cut: land was taken from identifiable owners at a named site. The cut
is on the lender-link test, and the drop reason says so, so the row can be reopened if a document is
found tying the loan to the Yenice land take or recording how the 43 suits ended.

**Correction found while checking it, recorded for the pattern even though the card is now a drop:** the
card attributed the "not financed by the project but adjacent to the project" clause to the Independent
Evaluation Group's review as something it "adds". The review's own text cites it to page 9 of the
completion report. It is the report's statement, repeated, not an added finding.

### 2. `moinak-transmission-line-land-taken-before-plan` (Kazakhstan, P114766) — CUT

Deciding document and sentences: completion report of 30 October 2013, involuntary resettlement section —
*"In total, 316 persons (land users) have been affected. None had to be resettled, and all received
reasonable cash compensation"*, and *"All compensation has been completed prior to loan closure."* The
only finding in the document is procedural: *"construction of the line started prior to the Bank's formal
approval of a Land Acquisition Plan"*, after which a plan was approved with *"relevant retroactive
measures"*.

The card's whole quantitative content is a count of people **affected** — which CHECK20 makes a cut on
its own — plus a sequencing failure with no recorded loss to any identified person. It is the same shape
as four rows the writer itself dropped in this batch (Talimarjan, Kakheti roads, Kyrgyz second rural
water, Bishkek–Osh), where land was taken, everyone was paid and no complaint was recorded. Keeping
Moinak while dropping those four is not a position the documents support.

**Refuted absence claim in the cut card:** it said *"The amount paid to any land user is in an appendix
the text refers to but does not reproduce."* Appendix 2 of that same Land Acquisition Plan is reproduced
in the document and lists each land user by name with the area taken and the compensation amount. The
drop reason names this appendix as the route back: its date columns may show land taken months before
agreement for named people, which would be limb (b). In the harvested text those columns are mangled, so
no claim was built on them.

---

## Corrections, card by card

### `raciborz-polder-nieboczowy-village-removal` (Poland, P086768) — kept, `documented` holds

**`documented` verified.** The independent corroboration exists, resolves, and says what the card says.
RMF24, 25 April 2007: residents told the Silesian voivode *"We will leave this area if you move the whole
village, including the church"*, and *"its construction was blocked by 200 residents of the village."*
Gosc Niedzielny, 30 June 2020: *"In the place that the embankments now enclose lay the villages of
Nieboczowy and Ligota Tworkowska. The residents of Nieboczowy jointly demanded the relocation of their
village to another place and obtained the decision-makers' agreement. The 'new' Nieboczowy was built from
scratch 7 kilometres away, in the same commune of Lubomia, next to the village of Syrynia."* Both are
press independent of the lender and both corroborate the core harm, so `documented` stands.

**Invented conflict, corrected.** The card said ICIJ's 689 was *"its count of project-affected people and
not a count of people moved"* and that *"The documents do not explain the difference between the two
figures."* The appraisal document explains it on its own pages. Its Annex 10.2 table gives the inhabitants
of the two villages as 564 in Nieboczowy plus 125 in Ligota Tworkowska, total 689, alongside 260 families
and 161 inhabited properties; paragraph 31 calls 689 *"the population to be resettled"*; the body text
rounds the same population to *"about 700 people"*. The 689 and the roughly 700 are one population counted
once and rounded once. `displaced_note` rewritten accordingly.

**Plan-reprint call, run and recorded.** The 700 is the appraisal's figure, not a measured outcome: PAD
paragraph 69, *"primarily about 700 people, about 260 families"*; PAD Annex, *"resettlement of about 240
families (about 700 people)"*; PAD safeguards annex, *"Two villages will be resettled affecting some 240
families (about 700 people)."* The completion report of 28 January 2021 carries it forward at paragraph 71
and in Box 2. What makes `displaced: 700` survive the call is the verb in the outcome document's own
results annex — *"All PAP have been resettled (250 families) and the RAP was implemented as agreed"* —
together with the press confirmation that the villages are gone and a replacement village is occupied.
`displaced_label` now states plainly that the 700 comes from the appraisal and what the outcome document
records. The household count moved from the appraisal's 240–260 families to the report's 250.

**Dropped counter-clauses in the survey paragraph, restored.** The card gave *"91.9 per cent of residents
formally accepted displacement"*. The plan update says *"as much as 91.9% of surveyed inhabitants"* and,
in the same paragraph, that the 1998 survey *"encountered hostility from the residents"* and that ten
households, 6 per cent, in Nieboczowy refused to answer it. For 2002 the card gave 42.2 and 29.4 per cent
without the same paragraph's two qualifiers: data were collected from 70 per cent of households, and the
survey followed a campaign by the defence committee urging residents not to co-operate. The following
sentences, which the card omitted, record 74 owners declaring a will to move in 2007 and 72 families
willing to resettle as of April 2010. All added.

**Statement attributed to the wrong document, corrected.** The card said DZMiUW *"carried out land
acquisition for the Wroclaw floodway works, supervised alongside the new village construction (completion
report, 28 January 2021)."* The completion report's only mention of the board, in its outputs annex, says
the coordination unit monitored the construction of the new village and *"the process of land acquisition
by the Lower Silesian Board for Amelioration and Hydraulic Structures (DZMiUW)"*. It does not say which
works that acquisition was for. The company role now says only what the report says.

**Confirmed without change:** loan IBRD-74360; approval 21 March 2007; original closing 30 November 2014,
actual 30 June 2020; US$184,000,000 original and US$166,561,150 disbursed; total project cost
US$1,018,571,150; €131.94 million of an original €140.1 million, about 91 per cent, at paragraph 51;
Table 3 cost-overrun figures for the European Commission (130.0 appraisal, 340.56 disbursed) and the CEB
(204.9, 204.66); joint review missions with the CEB; outcome Satisfactory in the report's own KEY RATINGS
and paragraph 56, and Satisfactory in the review's ratings table; appraisal figures of about 2,600 ha, 20
businesses and 22 community assets with the full itemisation; the 13 wayside shrines and conciliation
crosses, which is the completion report's figure (the plan budgeted nine units); the acquisition-by-year
counts 68 / 1 / 14 / 11 / 8 / 16 / 55 and the 30 houses taken in 2013 under the Silesian Voivode's
decision No. 1/2012 of 26 November 2012; the committee formally constituted in March 2002 as an
association for the defence of Nieboczowy against displacement; 150 appeals at the Ministry of
Infrastructure and 18 at the Administrative Court in Warsaw; the Supreme Administrative Court ruling of
27 April 2007. Cover dates read off the covers: completion report *January 28, 2021*; plan update *Most
Recent Update on March 2015*.

### `hade-shala-neighbourhood-mine-resettlement` (Kosovo, P096181) — kept, `documented` holds

**`documented` verified, and the independence of each source stated.** The Inspection Panel visited the
site in 2015 and published its own observations; CHECK20 names an Inspection Panel finding as independent
corroboration. Prishtina Insight of 14 November 2016, which saw the leaked investigation report, is
independent press and says what the card says: *"the panel found failings on the part of the bank
contributed to 'real and often severe harm' over a 'prolonged period'"*, and *"The Panel found that the
bank management was not in compliance with operational procedures on involuntary resettlement, as 'the
resettlement policy framework did not include principles and methods for the valuation of assets of
affected people living under the restrictions of the Zone in the New Mining Field.'"* Both verified at
the URLs cited. So `documented` stands on the Panel plus the press.

**One source is not independent and now says so.** The CEE Bankwatch post of 19 December 2016 is a guest
post by Dajana Berisha of the Forum for Civic Initiatives — the person the Requesters designated as their
representative to the Panel. It is a party's account. It also gives a third reading of the Panel's
finding, that the Bank did not make the resettlement decisions and could not be held directly responsible
but could have advised on mitigating the impacts and did not. Added to `confidence_note`.

**What was actually read, stated.** The card's source is the Panel's *Report and Recommendation* of
2 September 2015, written at the eligibility stage, not the 2016 investigation report; the card's
confidence note admitted the investigation report could not be opened but the body prose read as though
the Panel had found what residents alleged. Attribution tightened throughout: the temporary housing since
2011 or 2012, the plots in late 2014, the April 2014 stoppage of rent and food assistance, the 2004
valuation, the 12,500 euro difference, the smaller plots, the 20 KEK jobs, the absent school and
dispensary and the unknown grievance mechanism are all at paragraphs 48 to 55 of that report and all are
residents' statements to the Panel. The Panel's own observations — the incomplete sewerage, the condition
of the secondary roads, the confusion of institutional responsibility — are separated out as such.

**Plan-reprint call, run.** The resettlement completion report's indicator table marks 93 affected and 63
physically displaced households *"As of November, 2011 (Shala RAP)"* — they are the plan's figures. What
carries `displaced: 63` through the call is the outcome line in the same table, *"Households still
residing in Shala neighbourhood in Hade Village — 0 / 63 — As of June, 2015"*, together with the body
text at the report's section 2 that by September 2013 the remaining 42 households to be physically
displaced *"had moved out of the area"*. `displaced_label` now states both.

**Selective quotation, corrected twice.**
- The card gave 43.8 per cent worse off against 23.1 per cent in 2011. The same table (Table 14) shows
  "better" rising from 7.7 to 25 per cent and "same" falling from 67.3 to 31.2 per cent, and the paragraph
  opens *"Overall, in 2015 the majority of households (56.2%) perceived that their economic conditions are
  better or the same than in the previous year."* Added, with the physically-displaced/economically-
  displaced split of 37.5 against 62.5 per cent.
- The card said *"Rebuilding was slow"* and gave 22 plots built of 52. The same passage gives the
  report's own explanation, which the card dropped: households growing accustomed to living near the city
  where they had temporarily relocated and buying or building there, households investing elsewhere, and
  the perception that New Shkabaj was incomplete — *"many have later opted to stay in their temporary
  housing accommodations in Pristina while others have opted to buy or build in other places."* Added.

**Sample size corrected.** The card said *"the 2015 survey of 32 households"*. The report says 32
interviews were completed, covering 38 of the 93 affected households, a 40.8 per cent sample with a
margin of error of 10 points.

**Confirmed without change:** P096181 with grants IDA-H2340 and IDA-H3190, credit IDA-52400, trust funds
TF-13509 and TF-90160; approval 13 June 2006 and actual closing 31 August 2016 from the report's Key
Dates; second additional financing of US$4.2 million with a second Netherlands grant of US$1.2 million at
paragraph 63, Board approval 10 May 2013 — the data sheet's footnote says the system date of 28 March 2013
*"could not be changed, but the actual date of Board approval is May 10, 2013"*, and the Panel report
independently gives 10 May 2013; P131539 as the second additional financing's own number, confirmed on
the Panel report's cover; Component F added at the March 2013 restructuring; *"the project did not cause
nor finance the resettlement; it only supervised MESP's responsibility to implement the RAP"* at paragraph
41; the December 2006 Netherlands grant of US$4.33 million; the breach of the RAP and the legal covenants
by December 2013, the threat to suspend disbursements and the resolution through additional rent payments
for 21 families at paragraph 65; KEK's untimely rent payments putting the project in bad standing with its
covenants at paragraph 182; the three follow-up actions, the sewage repaired by December 2016 and the
workshop of 14 February 2017 at paragraph 69, with only the sewage repair directly linked to the project;
50 metres of blocked pipe reported in October 2015 and about 200 metres the ministry estimated needed
replacing; three economically displaced households still unclaimed in February 2016; 21 of 93 in a risk
zone required to evacuate in January 2012 with a monthly rent and living allowance; the conclusion that
*"livelihoods and living conditions have been at least restored and in some instances improved"*; outcome
Satisfactory in both the report and the review; the Shala RAP as an output of the Lignite Power Technical
Assistance Project, confirmed at paragraph 28 of the Panel report. Cover date read off the cover:
*February 28, 2017*.

### `tabanovce-kumanovo-motorway-compensation-arrears` (North Macedonia, P091723) — kept, `contested`

**Selective quotation, corrected.** This is the clearest instance in the batch. The card quoted the
report's words *"a serious safeguard violation"* and stopped there. The sentence reads: *"The delays in
payment of compensation were a serious safeguard violation which were corrected in time and detracted
slightly from the very positive outcome."* The rest of the sentence is restored.

**Figure disagreement, left unreconciled.** The card asserted flatly that *"The completion report's figure
of about 294 is a count of land parcels, not of people."* Two of the three documents support that: the
appraisal document of 16 April 2007 says *"There are 294 agricultural plots that will need to be acquired
affecting 102 owners"*, and the completion report says *"about 102 affected owners involving about 294
parcels of land."* The resettlement plan of 5 April 2007 says the opposite: *"There are 294 owners
affected by the Project, and the most of them will lose part of their agricultural land."* `displaced_note`
now gives both readings and reconciles neither. ICIJ's 294 traces to one of them and the documents do not
say which.

**`lenders[0].role` corrected.** The card said *"In March 2009 the Bank sent a Warning of Suspension of
Disbursement."* The report dates the Bank team's discovery to March 2009 and does not date the warning;
the role now says what the report says. Added: the original closing date of 30 September 2011 that makes
the nine-month extension checkable, environmental category B, and the figure conflict below.

**Figure disagreement between documents, left unreconciled.** Disbursement: the completion report's data
sheet gives *Disbursed Amount: USD 20.52M*; the Independent Evaluation Group's review gives 20.27 in its
Loan/Credit actual column (against 20.0 appraisal), and 22.39 for actual project costs against 25.0 at
appraisal. Both now stated in the role.

**Omission corrected.** Added the report's *"A total of 102 households were expected to lose part of their
land holdings due to the road expansion. No residence was affected"*, and the plan's *"No residences are
adversely affected; so there will be no physical displacement of persons"*, in place of the card's
unsourced assertion that no resettlement or demolition took place.

**Staff-told-evaluators material, checked and not used by the card.** The review contains two: *"In the
Decision Meeting minutes, the Lead Environmental Specialist confirmed that all safeguard requirements
including resettlement and land acquisition issues had been satisfactorily addressed for appraisal"*, and
*"Based on the IEG discussions with the Task Team Leader, the Project was in compliance."* Neither is on
the card. Correct.

**Confirmed without change:** loan IBRD-48590; approval 29 May 2007; actual closing 30 June 2012; the
March 2009 discovery and the Warning of Suspension for the road part of the loan; the amendment of the
plan and loan agreement, the special account, the change in national law; four to five court cases pending
at closure and payment from the state budget automatic once a court awards; 27 parcels at Blace after the
government's assurance that none were needed, delaying civil works more than two years; the review's
*"quickly resolved"*; outcome Satisfactory in both. Review date read off its own line: *Date Posted :
09/12/2013*. Cover date of the report read off the cover: *December 12, 2012* (its data sheet separately
carries *ICR Date: 12/17/2012*; the card's date follows the cover, which is right).

**Forward rule, re-tested:** limb (b) holds. Compensation was not paid to all landowners before the
contractor started work, at a named 7.3 km section, to about 102 owners of about 294 parcels, with four or
five of them still in court at closing. That is the Bukoba standard — unpaid compensation at a named site,
people neither named nor counted — and not thinner.

### `igoeti-sveneti-highway-worker-death-and-land-damage` (Georgia, P094044) — kept, `contested`

**`killed` corrected from 0 to 1.** The writer set it to 0 on the ground that the stated cause was a
speeding driver. CHECK31's test is whether a document gives a cause tying the death to the works, and this
one does: the man was a local employee of the first road contractor, he was *"performing a pavement test"*
on the project section, the driver *"ignored a road construction warning sign"*, the report calls it *"the
fatal accident on the Project section"*, and its lesson 6.6 is that *"traffic safety during construction
works on roads remains a problem"* and that *"when it has been determined that the contractor has not been
compliant with safety requirements, payment should be refused."* This is not a road accident on a finished
road; it is a construction-site death the report treats as a contractor safety failure. `killed_note`
rewritten to keep the stated cause, the unnamed worker and the missing accident date on the card.

**Omitted plan figure, added.** The card gave the outcome, *"the number of plots in the right of way
reached 192, covering 146,914 square metres, against the resettlement plan's own figure"*, without giving
that figure. The report gives it: *"The original RAP envisioned 167 land plots (91,968 m²)."* Added, with
the report's stated reason for the difference (inconsistent right-of-way data and poor coordination
between the plan's cadastral data and the preliminary design data).

**Confirmed without change:** credits IDA-43730 and IDA-45120; approval 18 December 2007; original closing
29 February 2012, actual 30 June 2012; XDR 34.72M disbursed; environmental category A; outcome Moderately
Satisfactory in the report's own ratings and Moderately Satisfactory in the review (review date read off
*Date Posted : 10/28/2013*); both quotations about the death and about the contractor's refusal to pay for
about 1.5 years; the Igoeti resident's agreement of 25 June 2012 for GEL 11,139, about US$6,700, for 954 m²
and 62 fruit trees, effective 9 July 2012, and the earlier February 2011 payment of GEL 45,000, about
US$27,270, for damage to her summer house; total compensation GEL 1,343,773, about US$0.81 million; about
4 ha more for connecting roads; the contractor taking advantage of known design errors and failing on the
environmental management plan, especially storage and disposal of materials; the Resettlement Unit of four
staff plus a hired consultant; the Roads Department moved from the Ministry of Economic Development to the
new Ministry of Regional Development and Infrastructure in the 2009 ministerial reforms, which is
footnote 7. The counter-clause *"all outstanding cases were resolved to satisfaction of the Project-
affected people"* was already on the card.

### `ferghana-valley-drainage-land-taken-without-plan` (Uzbekistan, P110538) — kept, `contested`

**The heaviest corrections in the batch. Two faults, both in the direction CHECK20 predicts.**

**(a) Invented conflict, removed.** The card's `outcome` said *"The two evaluation documents do not agree
about compliance"*, setting the completion report's non-compliance finding against the Project Performance
Assessment Report's *"overall, the project complied with the implementation of safeguards"* and *"previous
reviews of the safeguards confirmed full compliance"* (paragraph 2.26). The same assessment report says, at
paragraph 2.71, that the project unit *"was understaffed to carry out environmental and social safeguards,
which partly led to noncompliance with both"*, and that *"issues related to approval of the resettlement
action plan and delays in compensation payments to the project-affected people persisted for some time,
causing the downgrade in safeguards performance ratings."* There is no disagreement between the two
documents about whether non-compliance occurred; the assessment report records both. `outcome` now gives
both paragraphs of the one document and asserts no conflict.

**(b) Dropped counter-clauses, restored — the pattern ran through the whole borrower report.** The card
said *"513 farm enterprises were due compensation and 373 were paid, UZS 937,803,509 in total, leaving UZS
980,473,630 to be paid by the end of 2015"*, and used exactly one of the report's explanations for an
unpaid group. The report explains nearly all of them, and the explanations cut the other way:
- *"36 farmers will receive compensation after submission of correct banking details and 104 farmers were
  not harmed, as the work was carried out before planting and after harvest of crop."* That is the whole
  513 minus 373 difference, and 104 of the 140 suffered no damage at all. The card did not carry it.
- Under the first of the four decisions, of 10 October 2011, all 37 enterprises listed were paid in full.
  The card omitted that decision and opened with the December 2013 one.
- Under the 15 April 2014 decision: *"Of remaining 38 land users, there was no damage to 28 land users
  during construction, and money to 10 land users came back due to incorrectly furnished bank accounts."*
  Not on the card.
- Under the 15 February 2014 decision: *"Damage to the rest 2 farm enterprises was covered but due to
  incorrectly furnished bank accounts money came back."* Not on the card.
- What UZS 980,473,630 is: *"Total damage under the Project was UZS 1 918 million including UZS 937 803 509
  were paid in 2011-2014, UZS 980 473 630 are due to be paid for till the end of 2015"*, and the same
  paragraph estimates UZS 436.35 million of damage for 2015. The balance is assessed and expected damage
  together, not arrears owed to the 513. The card read it as arrears.
All restored.

**Four disagreements inside the one document, left unreconciled and now stated on the card:**
1. 15 February 2014 decision — the text says *"damage size to 62 farm enterprises equaled to UZS 127 215
   230 and UZS 126 246 030 were paid to 60 land users"*; Table 6 lists 128 enterprises under the same
   resolution with 60 paid. The card carried only the table's 128, which makes 68 farmers look unpaid when
   the text says 2 were.
2. 15 April 2014 decision — the text says UZS 235,988,691 was paid to 121 land users; Table 6 says 123.
3. 2013 land take — the text says *"land acquisition equaled to 358 ha"*; the table for the same year
   totals 334.51 ha. The card carried 334.51 only.
4. Table 6's own arithmetic — its paid column reads 37 + 155 + 60 + 123, which sums to 375, against its
   stated total of 373. The card used 373, the document's stated total; both are now on the card.

**Confirmed without change:** credit IDA-46480; approval 24 September 2009; original closing 31 July 2016,
actual 31 December 2016; XDR 33.76M disbursed; outcome Moderately Satisfactory in both the report and the
review of 16 October 2017; the three quotations from paragraphs 37 and 38, each checked against the whole
paragraph, including the counter-clauses *"this did not seem to cause any unhappiness in the farmers'
community"* and the farmers paid who turned out not to be affected with no mechanism to recover payments,
both of which the card already carried; the RAP updated in 2011 covering 37 farmers; the downgrade and
later upgrade of the safeguards rating; the UZS 494,989,548 assessed on 25 December 2014 with no payment
made because funds had to be reallocated; the 2012 explanation of 10 of 34 with no damage after part of
the collector works was dropped at detailed design and 24 whose money came back on bank details; 515.25
ha in 2012 and 197.49 ha in 2015; compensation set by decisions of the Fergana regional governor.
Assessment report cover date read off the cover: *MARCH 29, 2019*; borrower report cover: *November 2015*.

### `dartlo-telavi-rehabilitation-compensation-delays` (Georgia, P126033) — kept, `contested`

**Corrected.** The card said works started on 33 buildings in 2012, *"all of them in the category whose
residents were required to relocate temporarily."* The plan update says all 33 fell in the third category
but that seven were ruins and seven more had only small-scale works which, *"according to the Building and
Supervisory Company, did not need temporal resettlement of people"*, leaving the owners of 19 buildings
entitled to compensation under the 2012 plan. As written the card put 14 households into temporary
relocation that the document excludes.

**Disagreement inside the one document, now stated:** the same update says 19 affected persons were
entitled under the 2012 plan and, two pages later, that *"the compensation due to 21 APs in 2012, was
given to 19 AP's. 2 APs are still to receive the compensation."* Both on the card, unreconciled.

**Dropped counter-clause, restored:** the paragraph the card quotes for the Telavi and Kvareli coverage
also says *"Both Kvareli and Telavi aRAPs were fully implemented prior to the start of physical works."*
That bears directly on the Telavi business-compensation complaint and was omitted.

**Confirmed without change:** loan IBRD-81480; approval 20 March 2012; original closing 31 December 2016,
actual 31 December 2017; US$60,000,000 committed and US$57,266,743 disbursed of a total project cost of
US$72,184,676; outcome Moderately Satisfactory and Bank performance Satisfactory in the report's own KEY
RATINGS, Moderately Satisfactory in the review; 33 people at Kvareli, 91 households and 84 businesses at
Telavi, 44 residential buildings at Dartlo; *"In 2012, no one owner of the buildings has received the
compensations"* verbatim; 37 Telavi grievances submitted in 2014 not addressed until 2016 and the footnote
that they *"involved claims by affected business owners that the provided compensation did not fully cover
losses incurred as a result of the Project"*; the independent consultant appointed in summer 2014 and the
assessment that *"helped address outstanding complaints and confirmed compliance"*; the environmental
supervision passage, *"creating substantial risks for the livelihood of affected communities, health of
workers"*, the construction companies without adequate waste disposal arrangements and the *"obvious
deficiencies in protecting workers' health and safety"*; buildings unregistered in 2012 with owners
identified from villagers' verbal statements, and building #24 recorded as one owner and later registered
by three; the safeguards staff growing from 5 to 12. Plan update cover date read off the cover: *July
2016* — the card's date is right although the archive filed it under 2012.

---

## The seven drops: all seven stand

Each gives what the writer found in the outcome document, not a null sentence from a plan. Every quotation
was checked in the file.

| row | outcome document and deciding sentence | verdict |
|---|---|---|
| `osh-batken-isfana-road-no-land-taken` (P107608) | Completion report 27 June 2015, para 2.4.7: *"There was no land acquisition under either the parent project or AFs, and there were no project affected people (PAPs) under the parent project and AF1. The total compensation of about KGS 350,000 (US$7,000) was paid to seven project affected businesses under AF2."* Verified; paragraph numbering verified. | stands |
| `bishkek-osh-urban-infrastructure-nine-affected-paid` (P104994) | Completion report 26 May 2016, para 38: four plans for Bash-Karasuu, Naryn, Isfana and Tash-Kumyr, *"There were nine project affected people. Only one complaint was received and was addressed at the first grievance redress instance."* Borrower annex verified item by item: five farmers in Orok ayil aymak KGS 240,000 between them; a Naryn resident KGS 25,000 plus a land plot from the mayor's office; an Isfana farmer KGS 28,820 plus a plot; two Tash-Kumyr residents KGS 6,000 each for removed trees. | stands |
| `armenia-electricity-supply-reliability-no-outcome-count` (P116748) | Completion report 30 July 2024: the financial constraints *"contributed to the documented delays, including those related to land acquisition and RAP compensations"*, and the next sentences give the consequence — the transmission rehabilitation concluded in 2020, four years after the original closing. Social safeguards section: Satisfactory at closing, all compliance reports found the abbreviated plans complied, *"most of the affected households (on average from 80 to 95 percent) were satisfied"*. Garbled grievance count confirmed garbled in the document: *"A GRM, which received and addressed 157 was established."* | stands, with a note |
| `kakheti-regional-roads-31-plots-paid` (P117152) | Assessment report 17 June 2020: *"the land acquisition involved 31 land plots instead of the 174 expected at appraisal"*, and the road department *"fully compensated all landowners in accordance with the provisions of the resettlement action plan and received no complaints."* The writer's trap note is correct and worth keeping: the paragraph beginning *"At appraisal, no land acquisition or resettlements were envisioned"* sits above the heading *"Kakheti Regional Roads Improvement Project (P117152)"* and belongs to the Secondary and Local Roads Project. Verified by reading across the heading. No completion report exists for this project; the review of 10 June 2016 gives the same 31 against 174. | stands |
| `kyrgyz-second-rural-water-118-paid` (P110267) | Completion report 27 April 2015, para 46: *"118 Project Affected Persons (PAPs) in ten villages were identified"*, *"mainly affected by temporary restrictions to access or loss of trees and crops"*, *"All PAPs were fully paid by the project closing date"*, compensation KGS 1,979,254, about US$50,000, financed by IDA on an exceptional basis. | stands |
| `albania-water-sector-resettlement-avoided` (P102733) | Completion report 25 September 2020, para 56: the late social safeguards appointment *"caused delays in implementing the social safeguard instruments (for example, the RAP), which resulted in changing the locations of one of the wells as the implementation of the RAP was stalled"*, and *"The project avoided resettlement by changing the routes of some of the water and wastewater lines in some areas."* The one complaint, about a contractor delaying restoration of a local road, verified, with no people identified. | stands |
| `talimarjan-transmission-land-compensation-completed` (P119939) | Completion report 22 December 2016, paras 32 and 50 to 52: 12.03 ha permanent and 159.42 ha temporary from 114 leasehold farms, 90 in Kashkadarya and 24 in Samarkand; *"In total 141 farmers and Hokimiyats in eight districts... received compensation"*; the 26.7 ha substation take and the 1.1 ha average; *"To date, no complaints have been recorded"*; and the document's own explanation of 114 / 147 / 141 by the farm-consolidation programme and the audit that found six farmers paid in error and asked for the money back, with the entitlement matrix never modified. Note: the completion report dates the compensation to *"completed by April 2013"* in paragraph 51 as the writer says; the borrower section separately says *"land compensations have been paid during 2010-2013"*. | stands |

**One note on the Armenia drop.** Its reason says the harm hits were *"all recitals in the framework"* and
cites only the resettlement policy framework of July 2015. That understates what is on disk. There are
four abbreviated resettlement action plans of November 2014 with real counts — the Vorotan 1 section plan
alone covers 88 affected households and 119 owners of 43 plots, and records that of 43 protocols for
privately owned properties, 39 were signed. They are plan documents and no outcome document counts
anything, so the drop stands under the forward rule. But with ICIJ's largest estimate in this batch at
440 and a completion report that records *"delays... related to land acquisition and RAP compensations"*,
this is the row in the batch most worth reopening if an Armenian independent source is ever found. The
drop reason should have said what is in those four plans.

**The two road-safety rows, checked in both directions, as the task required.** P107608 (Osh–Batken–Isfana)
and P117152 (Kakheti roads) are the rows whose documents score high on harm language. Both directions
checked. The harm language is noise in both: in P107608 the *"police"* hit is a dispute between the
Ministry of Transport and the Ministry of Internal Affairs over ownership of the road safety strategy, the
death sentences are road fatality rate indicators, and the one count carrying a relocation verb is the
June 2010 civil unrest in Osh and Jalal-Abad in which about 400,000 people were displaced, which the
report gives as a cause of implementation delay. In P117152 the hits are fatality-rate indicators and the
entitlement matrix's recital of replacement cost. Neither contains project-caused harm. In the other
direction, P107608's safeguards section does record seven road-side businesses at the Nookat pass
compensated for lost profit, and P117152's assessment report does record 31 plots acquired and fully
compensated, and both were read rather than screened. Neither reaches either limb.

---

## Unreconciled figure disagreements (full list)

1. **Poland, one document against itself.** The completion report's FINANCING data sheet gives the European
   Commission 130,000,000 original and 382,650,000 actual, under a *US$* column header. Its Table 3, in €
   millions, gives the same source 130.0 at appraisal and 340.56 disbursed. The review flags the report's
   currency confusion itself and says the data sheet reports the Cohesion Fund as €101.29 million or
   US$130 million equivalent. The card cites Table 3 explicitly and quotes it correctly; no reconciliation
   is attempted.
2. **Poland, the review against itself.** *"Relocation was also carried out, involving 250 residents from
   the old villages of Nieboczowy and Ligota Tworkowska"* in its outputs list, against *"250 families were
   resettled, representing about 700 residents"* six paragraphs later. The card uses the second. Both
   recorded here.
3. **North Macedonia, plan against appraisal and completion report.** 294 owners, against 294 parcels
   affecting 102 owners. On the card as two readings.
4. **North Macedonia, completion report against review.** Disbursement US$20.52 million against 20.27;
   project costs 22.39 actual against 25.0 appraisal in the review. On the card.
5. **Uzbekistan Ferghana, four inside the one borrower report.** 62 against 128 enterprises under the
   February 2014 decision; 121 against 123 paid under the April 2014 decision; 358 ha against 334.51 ha for
   2013; and a paid column summing to 375 against a stated total of 373. All four on the card.
6. **Georgia Regional Development, one document against itself.** 19 affected persons entitled against 21
   due payment, in the same plan update. On the card.
7. **Kosovo, three sources on how many families had moved in.** 12 of 22 houses occupied as of June 2015
   (resettlement completion report); 23 houses built and 11 families moved in, as the community told the
   Panel in 2015; 22 families at the site in November 2016 (Prishtina Insight). The dates differ, so this
   may be a sequence rather than a contradiction — which is exactly why it is not reconciled here. On the
   card.
8. **Poland, plan against outcome, minor.** The plan update budgets nine units of historical crosses and
   shrines for relocation; the completion report records 13 relocated. Not on the card; the card uses the
   completion report's 13, which is right. Recorded for completeness.

## Things that could not be checked, named by route

- **The Inspection Panel's 2016 investigation report for Kosovo.** Not read. The route that was tried and
  worked is the Panel's September 2015 Report and Recommendation at the `thedocs.worldbank.org` path the
  card cites, which returns HTTP 200 and 186 KB of PDF. The 2016 investigation report was not found on
  that path and no other path for it was tried, because the card does not cite one and the search budget
  was spent on the press sources that decide `documented`. The two published accounts of what it found —
  the review's and Prishtina Insight's — disagree and both are now on the card with their sources named.
  This is a missing document, not a blocked host: `thedocs.worldbank.org`, `documents1.worldbank.org`,
  `prishtinainsight.com`, `bankwatch.org`, `rmf24.pl` and `katowice.gosc.pl` all answered 200 on first
  request, and all 27 source URLs on the kept cards resolve.
- **Review dates for the newer template.** The Independent Evaluation Group's reviews in the old template
  (North Macedonia, Georgia East–West) carry a *Date Posted* line on their face, and those two card dates
  were read off it. The newer-template reviews (Poland, Kosovo, Uzbekistan Ferghana, Georgia Regional
  Development, Albania, Armenia) carry no date anywhere in the document — cover, header or footer. Their
  dates on the cards come from the archive's own document-date metadata, captured at harvest. That is the
  Bank's *Date Posted* field rather than a filename inference, so the dates were left standing, but no
  cover-page confirmation exists for any of them and the rule in CHECK20 cannot be satisfied for that
  template from the file alone.
- **Independent sources for four of the six kept cards.** No Georgian, Uzbek, Kazakh or Macedonian press,
  court or audit source was looked for by this check beyond what the writer reports having searched; the
  search budget went to the two `documented` cards, which is where it decides an outcome. All four remain
  `contested`, which is the right value whether or not such a source exists, so nothing turns on it.
- **The Kazakhstan Land Acquisition Plan's Appendix 2 date columns.** The columns are mangled in the
  harvested text, as described in that row's drop reason. A `pdftotext -layout` pass on the original PDF
  might resolve them; that was not done, because the row is a drop on other grounds.

## Faults appearing on more than one card

1. **A counter-clause in the same paragraph, dropped.** Five of the eight written cards:
   North Macedonia (*"which were corrected in time and detracted slightly from the very positive
   outcome"*), Uzbekistan Ferghana (four separate explanations of unpaid groups, including 104 farmers who
   suffered no damage), Kosovo (the "better off" column of the same table, and the report's own explanation
   for the unbuilt plots), Poland (the response rates and hostility qualifying the 91.9 and 42.2 per cent),
   Georgia Regional Development (*"fully implemented prior to the start of physical works"*). This is the
   fault CHECK31 predicted, and it ran in one direction on every card: the damaging clause kept, the
   favourable clause in the same paragraph dropped. The pre-extracted briefs did not cause it but they made
   it easy, because a brief hands over a clause already separated from its paragraph.
2. **A conflict asserted where the document explains itself.** Twice, both in the direction of making the
   lender look more evasive than the file supports: Poland's 689 against 700, which the appraisal document's
   own annex table resolves; and Uzbekistan's ICR against the assessment report, where the assessment report
   records the non-compliance itself at paragraph 2.71.
3. **A figure read from the table when the text of the same document says something else.** Twice in the
   Ferghana borrower report (62 against 128; 121 against 123) and once in the direction of a larger apparent
   arrears figure each time.
4. **A statement attributed to the wrong document.** Twice: Poland's DZMiUW role cited to the completion
   report for a fact the report does not state, and Turkey's "not financed by the project" clause credited
   to the review as an addition when the review cites it to the report.

## Anything wrong in card data outside the fields asked about

- `lenders[0].role` was read against the documents on all eight written cards. Two carried errors —
  North Macedonia (the warning dated to March 2009, which the report does not do) and the Turkey card now
  dropped (the attribution of the adjacency clause). The other six are accurate as to report numbers,
  credit and loan numbers, approval and closing dates, committed and disbursed amounts, environmental
  categories where given, and ratings read from the document that gave each one. Round 22's error rate for
  this field was 19 of 46; this batch's is 2 of 8, which is lower but on the same order.
- Co-financier roles were checked too. Poland's European Commission and CEB roles are accurate to Table 3
  and the joint-mission sentence; Kosovo's Netherlands role is accurate to paragraphs 42 and 63.
- `start` and `end` on the kept cards are consistent with the documents' dates.
- No researcher voice in any kept card: a scan of `community`, `outcome`, `point`, `displaced_label`,
  `displaced_note`, `killed_note` and `confidence_note` across the six kept cases returns no instance of
  "I", "we", "my", "our", "this card", "this entry", "the draft" or "the writer".
- `companies` arrays: no oversight or civil-society body is listed beside the agency that caused the harm
  on any card. Kosovo lists rePlan Inc., the consultancy that wrote and monitored the plan, which is a
  party the documents put on the project and whose role the card describes accurately. Poland's second
  entry was the only problem and is corrected above. The Kosovo entry for KEK keeps the completion report's
  own mis-expansion of the acronym, flagged as such on the card, which is right.

## Did the pre-extracted briefs help or mislead?

They did both, in the way BRIEF31 warned. On the helping side: every document the eight cards rest on was
on disk and correctly matched to its project; nothing in this batch rested on a candidate parent or sibling
project, so that trap did not fire here; and the one project with no completion report (P117152, Kakheti
roads) was handled through the assessment report and the review, which is the right route and which the
writer said so on the drop.

On the misleading side, the three noise kinds named in the brief all fired, and the drop reasons show the
writer recognising them: "police" on road-safety indicators and on an inter-ministerial turf dispute;
"replacement cost" on entitlement-matrix recitals in every framework; and fatality-rate indicators read by
the pattern as deaths. Two further noise kinds that the drop reasons record and that are worth naming for
the next round: a count with a relocation verb that belongs to an unrelated event (the 400,000 displaced by
the June 2010 Osh unrest, which the report gives as a cause of delay), and a monitoring-indicator heading
that names a harm as a thing to be measured ("number of people not receiving compensation in time" in the
Talimarjan plan), which reads to a pattern exactly like a finding.

The kind of sentence the briefs should have surfaced and did not, on the evidence of what this check had to
restore by hand: **the sentence that explains an unpaid or uncompleted count.** Every one of the four
explanations missing from the Ferghana card is of that shape — *"104 farmers were not harmed"*, *"there was
no damage to 28 land users"*, *"the rest 2 farm enterprises... money came back"*, *"10 farm enterprises due
to cancellation of part of collectors"*. A pattern that catches a count next to a compensation word and
does not also catch "no damage", "not harmed", "not affected", "came back", "returned" and "erroneously
received" hands the writer one half of a ledger. The same gap explains the Kosovo omission (*"many have
later opted to stay in their temporary housing accommodations in Pristina"*) and the North Macedonia one
(*"corrected in time"*). On a batch where limb (b) turns on whether a loss is left standing after payment,
that is the single most consequential gap in the extraction.

The second kind not surfaced: **the appraisal document's own census table.** The Poland invented conflict
existed only because the 689 was not shown next to the "about 700" it is the precise form of. The
plan-reprint check lists figures that appear in both a plan and an outcome document; it would have caught
this if it also listed figures that appear in two forms, rounded and exact, inside the appraisal document
itself.
