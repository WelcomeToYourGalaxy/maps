# Round 17 fact-check log — file F (leads 4, 7, 8, 9, 19, 23, 27, 29, 30, 31, 35)

Input: `/home/claude/r17/out_F.json` (8 cases, 1 extend, 2 drops).
Output: `/home/claude/r17/checked_F.json` — 7 cases, 1 extend, 3 drops.

Every document named below was downloaded with `curl` to `/home/claude/r17/chk/` and read from
disk with `pdftotext -layout`. Line counts of the extracted text are given where an absence
claim depends on having read the whole file.

---

## 1. Lead 29 — `biftu-quarry-mizan-dima-road`: the death figure. **`killed` corrected 19 → 7.**

Opened: Ethiopia Transport Sector Project in Support of RSDP4, ICR00004796, 23 September 2019
(2,091 lines).

The footnote is real and the draft quoted it correctly. It is footnote 3 to paragraph 55, which
reads in full: *"In total 19 fatal accidents occurred in the project - 2 fatalities under
Kombolcha-Mille, 4 fatalities under Konso-Yabello, 7 fatalities under Mizan-Dima, 6 fatalities
under Ambo-wolliso during the construction periods."* The four figures sum to 19. Paragraph 55
places them under *"a number of issues in other contracts related to occupational health and
safety, some of which resulted in fatal accidents"*. The 19 therefore covers four separate road
contracts under the one credit, and `killed: 19` on a card about one of those four corridors
attributed to one corridor the deaths recorded on four. That was an outright error.

**Resolved figure: 7, the Mizan-Dima contract.** Reasoning, since the task asked for it:

- The document does attribute a cause. These are not unexplained deaths: the report files them
  as construction-site fatal accidents on the project's own works contracts, says at paragraph
  59 that the Bank identified "the high level of fatalities in construction sites" at appraisal,
  and lists "compensation to the family of victims of fatal accidents" among the safeguards
  actions the Bank still required of the borrower after the credit closed. A death in a work
  accident on a contract the credit paid for is a death caused by the project and its
  contractors, which is what `killed` counts.
- What the document will not attribute is the victims — who they were, and how each died. That
  is a reason to say so plainly in `killed_note`, which the card now does, not a reason to
  uncount deaths the report ties to the project's own contracts.
- 7 and not 19, because the card's unit is the Mizan-Dima contract. The other 12 belong to the
  Kombolcha-Mille, Konso-Yabello and Ambo-Woliso contracts, and `killed` counts only deaths for
  this case. `killed_note` prints all four figures, the total, and the fact that the other 12 sit
  on three other contracts under the same credit and are not counted here.
- 7 and not 0, with a scope fix to match. The card's `place` and `title` previously centred the
  Biftu quarry, and the report does not place any of the 7 deaths at the quarry. Rather than
  carry a contract-level figure on a quarry-level card, the card's unit is now stated as the
  Mizan-Dima road contract and the quarry that supplied it — which is what the card's lender,
  suspension and completion facts were always about — and `killed_note` says the report does not
  say whether any of the 7 died at the quarry.

Other checks on this case, all confirmed from the data sheet and paragraphs 42-45, 52-55:
credit IDA-51550 (Credit 5155-ET), US$415,000,000 original, US$290,905,981 revised,
US$262,666,331 disbursed; approval 25 September 2012, effectiveness 25 January 2013, original
closing 30 April 2019, actual closing 26 October 2018; category A (full assessment); outcome
Moderately Unsatisfactory, Bank performance Unsatisfactory, and paragraph 52 "the project's
environmental and social management was Unsatisfactory". The quarry narrative, the
November 2015-April 2016 complaints, "but it was not fully managed at site", the contractor's
failure to implement the supervising consultant's measures, the February 2017 action plan, the
January 2018 partial suspension running to closing, and "more than 95% of the complainants have
obtained appropriate compensation" are all paragraph 42. The Ethiopian Roads Authority's
rebuttal is Annex 5, and the independent experts' 150-metre area of influence, "there is no any
damage that occur on the initial complaint", the 4,000-plus payments, the 15 million Birr for
crop loss, the 372 households and the Jimma Agricultural Institute assessment are all in it.

Corrections made besides the death figure:
- "monthly payments to 25 people in vulnerable groups, and 20 business groups set up" → the
  borrower's letter says "25 vulnerable groups getting monthly payments and 20 corporate groups
  established to have own business". Corrected.
- Added, from paragraph 45 and Annex 5: security problems described as social unrest at the
  Mizan-Dima sites through the works period, and the borrower's account that the Biftu quarry at
  kilometre 39 was used because a security problem near the only other suitable source at
  kilometre 80.5 made that site hard to reach. Both bear on the episode.
- Not printed: the borrower's letter dates the suspension letter "8th January 2017" while the
  Bank's text and the letter's own three-month timeline put it in January 2018. That is an
  internal date slip in one letter, not two documents disagreeing about a fact, and printing it
  as a conflict would require explaining it. Flagged here instead.

## 2. Lead 9 — `orissa-state-roads-compensation`. Kept. Every load-bearing figure holds.

Opened: ICR00003903, 17 February 2017 (3,315 lines); IEG ICR Review, 21 June 2017 (733 lines).

Verified in the ICR: 7,948 project-affected people enumerated, 6,050 eligible and 1,890
ineligible (Annex 9 para 16), 6,058 eligible in the very next paragraph (para 17) — **the
self-contradiction is real and both figures are printed**; 5,730 relocated, 328 not; 828 / 730 /
632 on homes, 3,130 / 2,915 / 2,700 on commercial structures, 2,100 / 2,070 / 2,085 on kiosks;
7,698 awards, 6,312 paid INR 604,582,870, INR 110,740,687 unpaid on 1,376 awards, 253 in court,
84 at the Endowment Commissioner; INR 4,080,642 in civil deposits; 4,258 of 4,995 and 1,235 of
2,288 on resettlement assistance. Data sheet: IBRD-75770, US$250.00m original, US$163.00m
revised, US$87.00m cancelled, US$79.28m disbursed; approval 30 September 2008, effectiveness
15 April 2009, closing 31 December 2014 revised to 30 June 2016; Outcome Moderately
Unsatisfactory, Bank Performance Moderately Unsatisfactory, **Borrower Performance
Unsatisfactory**. Paragraph 55: the PPP enabling support "was removed from the project because of
noncompliance by the GOO to World Bank safeguards policies". Paragraph 30: complaints reported to
the Integrity Vice Presidency, "and INT has been investigating the complaints". Paragraph 31:
"For over nine months in the first year of the project, road contractors could not take
possession of the sites". 461 km / 303 km / 150 km confirmed. The IEG review gives the same
1,376 unpaid awards and the same 5,730 relocated.

Corrections and additions:
- `confidence` **`documented` → `contested`**. The core harm rests on the Bank's completion
  report and on the Bank's own evaluators reading that same report; no independent record exists.
  The brief sets `contested` wherever the core harm rests on a single source, and CHECK17 item 5
  asks for that flag on every such case. The note now says plainly that the lender is reporting
  on its own project. This is a rule-driven downgrade, not a doubt about the figures.
- The resettlement figures are now attributed to Annex 9, "Summary of Social Safeguards
  Activities", rather than to the report at large, because that annex is built from the project
  unit's own monitoring data and its tone shows it ("the project has completed the process of
  R&R of PAPs very satisfactorily").
- **Added a material omission**: the Bank suspended loan disbursements on this project and set
  eight actions for the state before lifting it; paragraph 29 says it took 17 months, May 2011 to
  October 2012, for the state to substantially comply. A card about this project that omits the
  suspension understates the record.
- Added the complaint handling system: 626 complaints between 9 October 2009 and 15 August 2016,
  495 resolved, 66 at hearing, 65 pending, plus 15 right-to-information petitions (Annex 9
  para 23).
- 176,000 saplings re-attributed: that figure is in Annex 6, the report of a workshop the state
  works department organised, not a Bank finding. The environment sentence now uses the ICR's own
  words at paragraph 32, "substantial deficiencies in implementation of environmental management
  safeguards", with the four areas it names.
- `conditions` now names the three social safeguard policies and the fact that the indigenous
  peoples policy was not triggered during implementation, because the roads finally chosen left
  out the tribal-area roads.

## 3. Lead 35 — `karnataka-state-highways-ii-compensation`. Kept. All checks hold.

Opened: ICR, 23 October 2019 (3,896 lines); IEG ICR Review, 30 December 2019 (808 lines).

Verified: paragraph 56, "the safeguards management for OP 4.12 remained Unsatisfactory or
Moderately Unsatisfactory for over three years"; paragraph 57, among the issues "depositing over
40% of the compensation amounts with the courts", non-functional grievance committees and
non-functional database; Annex para 9, income tax deducted from "7 land owners by KSHIP unit and
67 land owners by KRDCL, which will be required to be reimbursed as per the policy provisions
applied for the project"; Annex para 8, "the KSHIP received 1,235 complaints and the KRDCL
received 543 complaints" (1,778 together); Annex para 9, "issue of ownership titles to 27
families in one of the resettlement site at Hungsagi Village in Yadgiri district" and
"resettlement of 31 displaced Thangadagi village in Bijapur district"; paragraph 54, 602 acres of
private land, about 6,800 landowners, about 2,200 informal settlers, about 200 households
physically displaced of whom about 140 informal; Annex para 2, midterm 2014, "a large number of
PAP (more than 90 percent) are not satisfied with the compensation amounts, and about 20 percent
have approached the courts"; Annex para 7, compensation "deposited in the courts for want of
ownership documents and these people faced several hardships in realizing the compensation
amounts from the courts with high legal fees, long delays, multiple court hearings"; Annex paras
3 and 6, the 700-family and 110-household surveys and the 15 / 52 / one-third income split.
Data sheet: IBRD-80220 US$350,000,000 → US$295,213,354 disbursed, TF-92428 US$440,000 →
US$182,630, approval 24 March 2011, closing 31 December 2016 → 28 December 2018; outcome
Satisfactory, Bank performance Satisfactory. The odd effectiveness date of 17 July 2008, earlier
than approval, is what the data sheet prints and the card says so.

**The US$416m co-financier, checked as asked.** The ICR's financing table does list
"Foreign Private Commercial Sources (unidentified)": US$500,000,000 original, US$400,000,000
revised, US$416,000,000 actual, with no lender named anywhere in the report. It is a real finding
and it stays unnamed. But the same report, at paragraph 27 and in the results framework, records
US$416.56 million as the private sector capital the Government of Karnataka generated for the
core road network — one of the project's own PDO targets. The `lenders` entry now carries both
descriptions, so the money is not presented as straightforward co-financing of the Bank's works.

Other corrections: village spellings to the document's ("Hungsagi Village in Yadgiri district");
the 31 at Thangadagi now carry the report's own ambiguity, since it does not say whether 31 is
people or families; "93 per cent" attributed to the IEG review, which words it as "93% of the
land acquisition activities had been completed at closure"; compensatory planting now gives the
figures (153,000 saplings against a plan of over 223,000, remaining 73,500 due by December 2019)
rather than characterising it; `confidence` `documented` → `contested`, same single-source reason
as Orissa, with the two impact evaluations identified as consultants commissioned by the project.

## 4. Lead 8 — Padma Bridge drop. **Confirmed. The zero disbursement is in the document.**

Opened: Note on Cancelled Operation, cover-dated 15 August 2013, NCO date 16 August 2013 (517
lines), read in full; IEG ICR Review, 24 March 2014 (351 lines).

The data sheet gives credit IDA-48650, Original Total Commitment **XDR 779.30M**, Revised Amount
**XDR 0.00M**, Disbursed Amount **XDR 0.00M**. The disbursement profile shows FY12 actual 0.00
against 144.20 planned. Key dates: approval 24 February 2011, effectiveness 31 July 2012,
original closing 31 August 2016, actual closing 29 June 2012 — terminated about a month before
effectiveness, as the draft said. The narrative confirms the April 2012 conditions, the 29 June
2012 termination of the legal agreements "with immediate effect", and the government's withdrawal
of its request for Bank financing on 31 January 2013. IEG: "The project was not implemented",
rated non-evaluable on that ground, with 76,211 people in 13,526 households potentially affected
and relocation of 20,972 people in 3,886 households at an estimated US$273.2 million — appraisal
figures.

On the July 2011 compensation payments: the IEG review does record that the social programmes
were "making progress in the payment of compensation funds" and that resettlement sites were
being developed. Neither document records any disbursement, advance, project preparation facility
or retroactive financing against that work, and the credit's disbursed amount is zero in both the
commitment line and the year-by-year profile. **No Bank money paid for any of it.** The drop
stands on tests 1 and 3.

The drop reason has been rewritten to rest only on the two Bank documents. The draft's bdnews24
paragraph (2,452 acres acquired, Tk 10 billion, 12,532 landowners paid) was removed: it was not
verified here, and nothing in the drop needs it.

## 5. Lead 31 — Badia East extend. **Same credit, same episode. Confirmed.**

Opened: ICR2968, 15 October 2013 (2,980 lines); IEG ICR Review (814 lines). The existing case
`badia-east-lagos` names "IDA Credit 4219 UNI for the Lagos Metropolitan Development and
Governance Project (LMDGP), approved 6 July 2006, closed 30 September 2013". The ICR data sheet
gives P071340, IDA-42190, approval 06/07/2006, effectiveness 02/16/2007, restructuring
07/05/2011, closing 09/30/2013 original and actual, XDR 138.10M committed and XDR 90.11M
disbursed, environmental category B, all three ratings Moderately Unsatisfactory. Same credit,
same project, same two Badia demolitions, so the extend is correct and a new case would have
duplicated.

Each added fact verified at paragraph 41: the social safeguards audit and its four findings,
including decisions on community livelihoods "taken on an informal and ad hoc basis without
consultation, restoration or compensation" and works that "have proceeded and triggered
demolition in several cases without prior RAPs"; "Due to lack of compliance, in June 2012, the
Bank suspended all activities related to new sub-projects until an action plan to redress the
situation was put in place"; five retroactive RAPs including Badia's and six retroactive ESMPs;
"The total number of PAPs was 2605 tenants and 319 landlords"; all retroactive RAPs implemented
successfully by the end of the project. Paragraph 42 and the Inspection Panel box confirm the
2012 canal-and-road demolition with people in the right of way, the February 2013 Badia East
demolition as not an LMDGP-financed activity with the Bank asking the state to apply the
resettlement policy framework, and the 28 March 2014 update that the Lagos government began
distributing compensation payments in mid-February 2014. The nine slums and the 1.6 million
beneficiaries are paragraph 13. The barge alternative and the 15-metre right of way are footnote
12 and the text at page 11-12, including that a 5-metre access road on one side only would have
been easier than the access roads on both sides "which is what Lagos State asked for".

**One correction, and it matters.** The results figures — flooding ended in eight named
communities, water from 50 Naira to about 5 Naira per 25 litres — are in Box 2, headed
"Selected Impacts under LMDGP (Extracted from the document Lagos is Working, Project Coordination
Unit, LMDGP, 2013)". They are the project's own coordination unit's claims reproduced in the ICR,
not a Bank finding, and the extend now says so. The flooding sentence also reads "some
communities in" those eight places, not the whole of them, and has been corrected to match.

## 6. Lead 23 — `nhiip-bihar-bengal-compensation`. **Cut.**

Opened: ICR, 29 June 2022 (2,646 lines); IEG ICR Review, 2023 (1,185 lines).

Both quoted sentences are accurate. ICR paragraph 57: "At closure, compensation and eligible
assistance were duly paid to all PAPs in six of the 11 road corridors. The remaining five roads
in the state of Bihar and West Bengal have been transferred to the Bank-funded GNHCP, and will be
closely monitored for the completion of pending RAP actions." IEG: "disbursement of compensation
to project-affected people (PAPs) were substantially delayed in several sections but by project
closing, all 11,138 PAPs were compensated for land acquisition **for the subprojects completed
under the project**." The figures 775 acres, 558 private, 6,390 structures, 451 common property
resources, 11,138 people and 347 grievances with all but one resolved are all confirmed.

My verdict on the question asked: **a recorded contradiction is not enough for a card, and here
there is not even a contradiction.** The IEG sentence is expressly limited to the subprojects
completed under the project, which is the same set as the ICR's six corridors; the five
transferred corridors are outside both statements. Printing the two as a disagreement would be
the fault CHECK17 item 9 warns about. Strip the supposed conflict and what is left is: a delay
with no number of people, no date, no place and no named community, on a five-state corridor
project, with no court record, press report or NGO field research. Below the bar. Cut, with the
reason recorded in `dropped`.

## 7. Lead 30 — `himachal-pradesh-state-roads-debris`. Kept, re-centred.

Opened: ICR, 20 December 2017 (2,744 lines), read in full; IEG ICR Review, 27 February 2018
(682 lines).

**Does the card claim a compensation failure it cannot support?** The draft came close. Its title
said "payments short at closing" and its first substantive sentences were the 96.2 per cent and
93.5 per cent residuals — which the ICR attributes at paragraph 57 to owners dying with heirs not
yet on record, court cases and stays, co-owner disputes, owners not collecting despite notices,
and untraceable beneficiaries. On that record the residuals are not a failure of the project and
cannot carry a card. The title has been changed and the confidence note now says in terms that
the residuals are not presented as a compensation failure.

**What the draft missed, and what now carries the card.** Footnote 42 of the ICR: "During two
consecutive supervision missions in 2008 and 2009, social safeguards performance was rated MU
because the post of social development officer in RIDC remained vacant, no NGO was in place for
R&R assistance, and RIDC failed to take action on allegations that contractors had occupied
private land in excess of what had been acquired. The problems were eventually remedied." That is
a documented social failure with a cause the Bank attributes to the implementing corporation, and
it is now in the card. With it sit the verified environmental findings: the Moderately
Unsatisfactory environmental rating from late 2014 over, in the IEG's words, "serious problems in
contracts 5-I, 5-II, 6-I and 6-II with poor debris management, protection of forest lands, dust
pollution, road safety, and workplace safety"; footnote 40, "in September 2011, lack of proper
planning and sequencing of works in contract 9 led to several large landslides affecting access
for vehicles and pedestrians"; the unprecedented landslide later on the same contract; about 80
debris disposal sites rehabilitated; 432,692 trees planted at a 69.75 per cent survival rate;
154 ha of forest land diverted and a land acquisition output of 132 ha.

The absence claim is sound and is now stated with its basis: the full 56-page report yields no
count of project-affected people — searched across the whole extracted text for project-affected
people, PAPs, families, households, hectares and acres, with the only land figures being the two
output targets. So ICIJ's 16,896 has nothing in the Bank's record to be set against, which the
card says. Loan figures confirmed: IBRD-48600 US$220m approved 5 June 2007 with US$219,998,008
disbursed, IBRD-81990 additional US$61.7m cut to US$46.7m, effectiveness 5 October 2007, closing
30 June 2013 → 30 June 2017, outcome Moderately Satisfactory, 355 km of 447 km upgraded.

## 8. Lead 19 — `mekenajo-dembidolo-road-coffee`. **The completion report was found. Rewritten.**

The draft said the APL4 completion report "is not returned by the World Bank's document search".
It is. `https://search.worldbank.org/api/v3/wds?format=json&projectid=P106872` returns 41
documents, including "Implementation Completion and Results Report, 2018-05-31, Ethiopia - Road
Sector Development Program Project", ICR00004205 (4,396 lines of extracted text). It is filed
under a title that does not carry "APL4", which is presumably why the draft missed it. **The
card no longer rests on a quotation of a quotation.**

The passage is at pages 76-77, paragraph 7(c): "The problem of flooding has been widely observed
in the Mekenajo-Dembidolo road corridor, where several coffee-growing farmers reported losing
coffee trees and other perennial crops." Word for word what the IEG review quoted.

But reading it in place changes how it must be presented: it sits in **Annex 10, "Summary of
Findings of the Transport and Poverty Observatory Study"** — a five-year panel study, 2012 to
2016, on four of the programme's corridors, 667 km and 25 woredas, using household surveys, focus
group discussions and key informant interviews. It is a study summary inside the ICR, not a Bank
inspection finding, and the losses are what farmers reported to that study. The card says so.

Two further findings from the same annex, both new to the card: paragraph 7(b), "Complaints
regarding compensation were raised in all road corridors. The details for size of land lost for
the road construction and the number of PAP who have been compensated for the loss of their
produce and the amount of compensation payment made to PAP is currently being worked out by ERA"
— that is, at completion the roads authority had not yet established how much land was taken or
how many people were paid; and paragraph 7(a), dust strong enough in some localities to affect
traffic movement and cause vehicle accidents during construction. These stand directly against
the ICR's own main text at paragraph 41, "ERA ensured that all PAPs were compensated following
ESIA recommendations". **That is a genuine disagreement inside one document and both halves are
now printed, unreconciled.**

Other corrections: the credit number IDA-45610 (Credit 4561-ET) was missing from the card and is
added; the data sheet's figures confirm US$245,000,000 original, US$204,920,973 revised,
US$206,283,547 disbursed, approval 2 June 2009, effectiveness 14 September 2009, closing 30 June
2016 → 30 June 2017, borrower contribution zero against US$63.23m at appraisal. The draft's
"actual total project cost US$275.2 million" is one of two figures the ICR gives; the IEG review
notes the report's cost tables as "incorrect/confusing", page 2 giving US$206.3 million and Table
7.6 on page 53 giving US$275.2 million. Both are now printed with the IEG's observation.
"Implementation of safeguards was not effective because of the inability of the bodies involved"
was loose: the source says it was ineffective "due to inability of contractors to implement the
ESMP". Corrected. The ICR is added as the card's first source and the card now carries paragraph
41's own account of the division of duties between the roads authority and the woredas, the
10-months-against-28-days delay on site-specific plans, and the slope planting that had not
rooted (ICR page 22). The IEG's two absence statements — the report does not give the number
relocated, and contains no safeguards compliance statement — are confirmed at IEG pages 11-12 and
independently against the full ICR text.

## 9. Lead 19 against lead 29 — overlap check. **No duplicate.**

Different credits, different corridors, different harms. Lead 19 is P106872, credit IDA-45610
(4561-ET), approved 2 June 2009; its corridors are Wolkite-Hossaina, Mekenajo-Dembidolo and the
dropped Ankober-Dulecha-Awash Arba, and its harm is flooding and lost coffee trees on
Mekenajo-Dembidolo plus slope planting that did not root. Lead 29 is P117731, credit IDA-51550
(5155-ET), approved 25 September 2012; its contracts are Kombolcha-Burka-Mille, Konso-Yabello,
Mizan-Dima, Ambo-Woliso and Debre Birhan-Ankober, and its harm is quarry dust and blasting damage
at Biftu on the Mizan-Dima contract, the partial suspension, and the contract fatalities. No road
section and no episode appears on both cards. The name Ankober appears in both programmes, but in
lead 19 that road was dropped in 2015 and in lead 29 the Debre Birhan-Ankober contract never
started work. Coordinates are about 300 km apart and neither sits within 50 km of the other.

## 10. Lead 7 — `lucknow-muzaffarpur-highway-land`. Kept. **One error corrected.**

Opened: ICR, 13 December 2012 (3,753 lines); IEG ICR Review, 25 June 2014 (441 lines).

Both halves of the draft's account check out. ICR page 11-12: impacts "high in magnitude as well
as intensity", 442 ha of private land from about 14,976 titleholders and 8,418 non-titleholders,
259 religious properties, ratings moving satisfactory to unsatisfactory and back, and "By the
project closing date, the land acquisition and resettlement implementation was fully completed
and all affected families received their compensation and main entitlements, except a few whose
cases were in court on ownership disputes." Footnote 14 gives the 1,800 metres taken out of scope
and the four religious properties not moved. IEG: "the ICR does not state that all safeguards
were met and were in compliance with Bank requirements."

**The error.** Both documents say the evaluation consultants "were not hired until the closing
date" — late, but hired — and the IEG adds "As such, the evaluation and survey is on-going and
will continue to be monitored by the Bank until the final report is submitted". The draft turned
this into "were not hired by the closing date" and, in `outcome`, "The end-of-project study of
what happened to resettled people was not carried out." That is a claim the documents do not
make. Corrected in both fields, and the confidence note now states in terms that an unmeasured
outcome is not a measured harm and that none is claimed. `displaced_label` also corrected:
"landholders who lost land" was wrong for the 8,418 without title.

## 11. Lead 27 — `caldwell-bridge-liberia-compensation`. Kept. All three facts verified.

Opened: ICR00004329, 22 December 2017 (2,496 lines); IEG ICR Review, 2018 (678 lines).

Paragraph 91: "In 2016, five compensation checks totaling US$11,348 were stolen from the PFMU
office and illegally cashed. The GOL refunded the stolen funds to the Bank and PFMU implemented
strict measures to lower the risk of reoccurrence, including installing cameras to monitor the
movements of staff and clients." The PFMU is the Project Financial Management Unit under the
Ministry of Finance (paragraph 90). Paragraph 86: "For works of Caldwell bridge, late payments of
PAPs led to delayed site handover and a compensation of **US$315,000** by the GOL to the
contractor." Paragraph 87: "the Bank agreed to allocate **US$ 8.0 million of IDA funds** under
the URIRP AF2 to cover RAP payments under both URIRP and LIBRAMP" — LIBRAMP being the Road Asset
Management Project — followed by the hindsight passage and "the Bank's RAP funding may have
pre-empted significant local tension and conflict risks in the project area". Paragraph 88
confirms the frequent payment delays, the poor coordination between government bodies, and the
Monrovia-Buchanan road's inadequate information, missing community grievance mechanism and
disagreements over assessment. Financing confirmed: IDA-H4780 US$44m, IDA-H6040 US$20m,
IDA-53510 US$19.6m, TF-94353 US$9.2m, TF-98040 US$27m → US$25.2m, TF-16065 US$9.4m → US$8.4m,
total disbursed US$126,861,560, no borrower contribution; approval 21 April 2009, effectiveness
21 July 2009, closing 30 June 2014 → 30 June 2017; category B. The Liberia Reconstruction Trust
Fund's founding in 2007 by the European Union and partners, and the partner list — Germany,
Ireland, Sweden, Norway, Britain and the Bank's LICUS trust fund — are paragraph 5 and footnote 3.
Only wording tightened, plus the single-source note.

## 12. Lead 4 — Kerala drop. Confirmed, reason corrected.

Opened: ICR, 21 June 2022 (2,515 lines). Paragraph 54 confirmed word for word: "The project paid
appropriate compensation to all PAPs/project affected families (PAFs), except PAFs that opted for
a Court ruling to enhance compensation." No count of affected people anywhere in the report,
searched across the full text. The 41 km stretch dropped over land acquisition time after the
2013 act is confirmed at the output table footnote. One correction to the drop reason: the report
does quantify the work-site accidents — paragraph 47, "The project witnessed two accidents in
2017, each of which resulted in a fatality: the toppling of the mast of a church flagpole due to
the excavation of a nearby retaining wall; and a water tanker accident", with compensation paid
to the families. So there are two recorded deaths on this project, not an unnumbered mention. The
drop still stands — two deaths with compensation paid, no displacement finding, no community and
no other harm will not carry a card — but the owner should see that the figure exists.

---

## Bucket verdicts after checking

- **(a) Documented failure**: lead 9 Orissa; lead 35 Karnataka; lead 29 Mizan-Dima/Biftu; lead 27
  Caldwell Bridge; lead 19 Mekenajo-Dembidolo; lead 30 Himachal Pradesh. Lead 30 is (a) on the
  environmental record and the 2008-2009 excess-land-occupation finding, not on compensation.
  Lead 19 is (a) on crop losses reported to a study inside the ICR, which is the weakest (a) here.
- **(b) Large resettlement, no documented failure**: lead 7 Lucknow-Muzaffarpur. The land taking
  is documented as completed with compensation paid; the card claims no failure.
- **(c) Nothing usable**: lead 23 NHIIP (cut here), lead 4 Kerala, lead 8 Padma (fails the link
  and timing tests rather than being unusable).

## Counts

Kept 7 of 8 cases, 1 extend, 3 drops (2 inherited, 1 added). Every kept entry was corrected;
none was passed through unchanged. All 11 lead numbers appear exactly once. Both output files
validated with python: required keys present on every case, enumerated values from the brief's
lists, ids unique and absent from `cases.json`, the extend id present in `cases.json`, no
first-person or process narration in any card field.

## Patterns worth carrying forward

1. **A project-wide footnote is not a corridor figure.** The 19 deaths were a four-contract total
   on a single-corridor card. Any aggregate in a footnote needs its unit checked before it goes
   in a counting field.
2. **"Not returned by the documents API" needs the `projectid` filter before it is written
   down.** The APL4 completion report was there all along, filed under a title without "APL4".
   `projectid=<P-number>` lists everything; a `qterm` search on the ICIJ project name does not.
3. **Find the annex before quoting the number.** Four figures in this batch changed hands on
   inspection: the Orissa saplings (a state-organised workshop report), the Orissa resettlement
   counts (the project unit's own monitoring, in Annex 9), the Lagos results box (the project
   coordination unit's own promotional document), and the APL4 flooding passage (a study summary
   in Annex 10). All were in Bank reports; none was a Bank finding.
4. **Check the qualifier before printing a conflict.** The NHIIP "contradiction" dissolved on the
   seven words "for the subprojects completed under the project".
5. **"Not hired until X" is not "not hired".** One preposition turned a late evaluation into an
   absent one on the Lucknow card.
6. **Single-sourcing is the condition of this whole round, not an exception in it.** Every kept
   case here now carries `contested`, because in all seven the harm rests on the Bank reporting
   on its own project — including the two strongest, where the Bank's own evaluators reading the
   Bank's own report is still one source.
