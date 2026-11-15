# Check log: round 22, batch B (`r26f_icij6_energy.json`) — energy, transmission and urban roads

Checked against `docs/CHECK20.md` plus `docs/BRIEF22.md` and the handoff's round 20, 21 and
lender-role-audit sections. Nothing merged, `build.py` not run, git not touched.

**Result: 7 of 8 kept, all 7 corrected, 1 cut.** The cut is `vietnam-redp-small-hydro-land`.
Corrections: 23 across the seven keeps. Two refuted absence claims, two unsourced passages removed,
one passage moved from the card it did not belong to, one new document found that the writer never
used, and one new ICIJ-figure match.

## The document cache

Rebuilt at `/home/claude/r22/cache` from the `wds` API plus `documents1.worldbank.org`, read with
`pdftotext -layout`. **40 documents downloaded by this job**, as paired `.pdf` and `.txt`:
`P101645_{ICR,ICRR,RAP,PAD}`, `P075994_{ICR,ICRR,RAP,RAP2,PAD}`,
`P094919_{ICR,ICRR,RAP,RAP2,PAD,PPAR}`, `P110075_{ICR,ICRR,PAD}`,
`P095982_{ICR,ICRR,RAP,RAP2,PAD}`, `P078382_{ICRR,RAP,PAD}`,
`P111153_{ICR,ICRR,RAP,RAP2,RAP3,PAD,RAP_2016v3}`, `P103238_{ICR,ICRR,RAP,RAP2,RAP3,RAP4,RAP5,PAD}`.
`P075994_RAP_dec.txt` is a working decode of a shifted-glyph font, not a download.
`P094919_PPAR` and `P111153_RAP_2016v3` are not in the writer's list — the first matters (below).
Nothing in the folder written by another agent was touched.

---

## 1. `tedap-ukonga-mzinga-wayleaves` (P101645 / P092154) — KEPT

The strongest card in the batch, and the writer's document route is the reason: TANESCO's
**Amendment of Resettlement Action Plan, January 2014** (RP539 V7) was read in full, all 17,000
characters of it, and every quotation on the card is in it verbatim.

Confirmed from the amendment: the 43 named affected people at Ukonga and the losses recorded against
each name, including "75% of house affected, Borehole, Trees" and "Kiosk (3)"; the Tshs
300,639,109.92 paid, which the budget table heads "Actual cost paid for valuation of properties and
compensation"; the Managing Director's approval to value and compensate for exhausted improvements
on the land only because the land belonged to RAHCO, "in order to meet the World Bank requirement and
allow the contractor to continue with works smoothly"; the meeting of 18 September 2011 at Ukonga
Magereza and the two requests made there; TANESCO's own sentence, quoted exactly on the card,
"Experience shows that after compensation payment even if you give them a year PAPs are normally
slow to vacate freely; a close follow up will be needed"; the Kurasini sequence, three families in
two houses earmarked and then Tshs 1,638,111,700 paid to Kurasini Oil Storage Company Limited,
formerly MPS Oil (T) Limited; and the Mbagala sequence of 13 June 2012, the Chief Government
Valuer's signed valuation and the payment schedule taken to the District Commissioner at Temeke.
**The card's absence claim about Mbagala holds**: the amendment's budget table carries valuation and
an NDC refund for Mbagala and no compensation line, so it does not say whether those three were paid.

Confirmed from the completion report (ICR00004395, cover 27 June 2018): the 11,070 project-affected
people the September 2017 resettlement audit set for Component A; the audit's three conclusions,
quoted accurately including the favourable first one; the 16 households at Mzinga Creek with
compensation made for 13 and not for 3; the top-up approved after completion; the environmental unit
growing from four people with no social scientist to 18 including social scientists; the four
cancelled distribution packages and the debarment of two private companies after an Integrity Vice
Presidency inquiry, in the report's own words "submitted false financial documents"; the 13 km
Ubungo-Kurasini section dropped for a TANROADS road expansion and financed by TANESCO after closing;
six safeguard policies and category B partial assessment; the July 2007 RAP and the June 2012
rewritten frameworks. Every financing figure in the role field matches the data sheet to the dollar.
Confirmed from the Evaluation Group's review: the split rating arithmetic and the sentence that the
report could usefully have given an update on the three remaining households.

**Corrected — 3.**
1. **M&E rating, the data-sheet-against-body fault the lender audit named.** The card gave
   "monitoring and evaluation quality Modest", which is the data sheet's KEY RATINGS field. The
   report's own section IV.A heading and its paragraph 114 both rate quality of M&E **Moderately
   Satisfactory**. Both now printed, with the note that the report does not reconcile them.
2. **Environmental category.** "Category B" alone; paragraph 115 says Category B "requiring a
   partial assessment", which is the house form. Added.
3. **The 16 at Mzinga Creek.** The report writes "16 households will be affected" at paragraph 117
   and "compensation of 16 PAPs … 13 PAPs … 3 PAPs" at paragraph 118 for the same group. The card
   now says so, because the unit is the Bank's own confusion and not the card's.

**Absence claim turned into a task and discharged.** The card said the resettlement audit "was not
found". It is not in the Bank's archive: `wds?projectid=P101645` returns 67 documents, whose only
audits are TANESCO and REA financial audit reports, and two `qterm` searches for a resettlement audit
returned none. The card now says that, rather than that it was not found.

Also recorded on the card: the amendment contradicts itself on the line it covers, its introduction
describing Factory Zone III (Gongo la Mboto) to Factory Zone II (Kiwalani) and its Ukonga section
Factory Zone II (Gongo la Mboto) to Factory Zone III (Kipawa).

## 2. `ctb-kwabenya-stone-crackers` (P075994) — KEPT

Confirmed from the completion report (ICR00004338, 28 February 2018), paragraphs 39 to 41, read whole:
"The Ghana component complied partially with social constraints"; "About 1,700 persons were
affected"; "The MTR noted that the project was not in compliance with World Bank policies because
construction started before compensation"; and, in the same paragraph, "By 2011, the VRA had fully
settled outstanding compensation to all affected parties, including landowners and stone crackers".
**No selective quotation**: the card carries the favourable clause, the "minor failings … subsequently
corrected" sentence and the full settlement by 2011. Ratings read out of the ICR itself — outcome
Unsatisfactory, risk High, Bank performance Moderately Unsatisfactory, borrower split Ghana
Moderately Satisfactory and Benin Unsatisfactory — which matters, because the review's ratings table
prints the ICR's borrower performance as a single Moderately Satisfactory and loses the split.

Confirmed from the addendum: 1,454 affected farms (1,051 original, 403 diversion; Greater Accra 142,
Central 1,106, Western 206), under a column the table heads "Total no. of payments"; 410 buildings
and structures "actually condemned" (271, 136, 3); the 22 stone crackers excluded from the property
owners "since their loss basically is a loss of right to engage in an economic activity but not loss
of proprietary right"; GHc 18,968 "(to be paid by end of 2010)"; cut-off dates 30 August 2008 and 21
April 2010; the realignments at the nine named places "to avoid huge compensation cost"; 215 km to
219.2 km, 860 to 876 hectares, eleven new towers; the uncompleted bulk of the Greater Accra
properties, the owner-occupation by relatives and dependants, no claim from any tenant, and the
minimum three years from consultation to relocation. **The arithmetic flaw the card flags is real**:
the affected-houses table gives 226, 16 and 1 in its "Original no. of PAPs" column and 43 in that
column's total row, while 292 and 118 do sum to 410. Confirmed from the 2004 plan: 215 km corridor,
8.6 km² (860 ha), and 307 of the affected people giving household sizes from two to thirty-one, a
district mean of 5.1 to 8.6.

**Corrected — 5.**
1. **Two signing dates no document gives.** The card had the phase 2 credits "signed 4 December 2007"
   and "signed 2 March 2007" and the first phase "under the Development Credit Agreement of 31 August
   2005". Those three dates are the dates of the agreements as the report's footnote **cites** them;
   neither Bank document says anything was signed on any of them. Reworded, with the data sheet's
   phase 2 approval and effectiveness dates added.
2. **The addendum does print a date.** The card said it prints none and that July 2010 was the
   catalogue field. Its cover prints "JULY, 2010" in a font whose glyphs are shifted 29 code points,
   which `pdftotext` renders as `-8/<\x0f\x03\x03\x15\x13\x14\x13`; decoded, that is JULY, 2010, and
   "PREPARED BY REAL ESTATE DEPARTMENT" sits above it. Claim removed.
3. **The 2004 plan's date.** Its running header says December 2004 and its cover says FEBRUARY, 2005.
   Both now on the card and in the source title.
4. **`iso3_more` BEN and TGO removed, and the CEB cash-flow sentence taken off the card.** The only
   Benin or Togo content was the report's bullet on recurrent cash flow difficulties at the
   Communauté Électrique du Bénin delaying the money set aside to compensate people affected by the
   Ghana-Togo-Benin 330 kV line. That line is the second phase under a separate project number, its
   construction was financed by other lenders, and the same report's paragraph 44 says the Benin
   component financed by this credit raised no social safeguard issue because it required no land
   acquisition or resettlement. That is CHECK20's test on whether the harm is on the thing the credit
   financed, and it fails. The finding is kept in `confidence_note`, stated as the second phase's.
5. **`end` 2016 to 2013.** 2016 was the Benin credit's closing date. The Ghana first-phase credit,
   which paid for the Aboadze-Volta line this card is about, closed 30 June 2013.

## 3. `wapp-apl3-zagtouli-bolgatanga-deaths` (P094919) — KEPT, `killed: 2` upheld

**The cause test, applied to each death.** Both counted; none left out, because the documents record
no other death on this project.
- The worker declared dead at the scene when the transmission tower gave way during assembly works,
  carrying two workers down. Counted. The completion report's paragraph 77 ties the accidents to a
  stated supervision failure — one health and safety supervisor for all sites, hundreds of kilometres
  apart — and its lessons say that had the later measures been in place earlier "the accidents might
  have been avoided".
- The minor who drowned in a pool formed in the excavated tower foundations after they filled with
  rain water. Counted. The hazard is the works' own excavation, the same paragraph carries it, and the
  twenty-point remedy includes securing all work sites with wooden barricades before starting work.
- **And a document the writer did not have makes the cause explicit.** `wds?projectid=P094919`
  returns an **Evaluation Group Project Performance Assessment Report, Report 187586, 30 October
  2024**, written after a mission with site visits at Zagtouli. Its paragraph 2.16 states that
  "contractor implementation and enforcement of on-campsite safety measures were insufficient,
  resulting in two fatalities and the serious injury of a third worker". Added as a source, with its
  finding that the compensation delays cost two months on the civil works and that workers had a
  grievance mechanism but no redress mechanism. It is still the lender's own evaluation arm, so
  `confidence` stays `contested`.

Confirmed otherwise: every financing figure, date and restructuring in the role field against the
data sheet; outcome Satisfactory, Bank performance Moderately Satisfactory, M&E Substantial, read out
of the report, where data sheet and body agree; the review's outcome Satisfactory, quality of
supervision Moderately Satisfactory and overall Bank performance Moderately Satisfactory, read out of
the review's own rating lines; four safeguard policies and category B partial assessment, against
both the report and the appraisal document's table; the twenty-point plan including the sacrificial
rituals the customary authorities demanded; the compensation-delay causes; the absence of a formal
grievance mechanism until 2018. The card's attribution of "All compensations were completed before
project closing, according to the ICR team" as a staff statement and not a document is correct, and
the review's criticism of the status reports' candidness is the review's own. Eiffage's page returns
200 and says what the card says it says.

**Corrected — 4.**
1. **"15 communities" to 16.** The plan's sentence that gives the 1,166 says the 87 households lie
   "in all the 16 communities"; elsewhere the same plan says "fifteen settlements" and "all the 15
   communities have access to potable water". Both now on the card.
2. **The Ghana plan does print a date.** "April 2011" is on its cover page above the acronym list.
   The unverified-date claim for it is removed; the claim stands for the review, which prints none.
3. **A source title and publisher that do not match the document.** RP1139 V2 was cited as "Land
   Acquisition and Resettlement Policy Framework, Inter-Zonal Transmission Hub Project of the WAPP",
   publisher "West African Power Pool". Its cover reads "LAND ACQUISITION AND RESETTLEMENT POLICY
   FRAMEWORK, GHANA ENERGY DEVELOPMENT AND ACCESS PROJECT, FEBRUARY, 2007", prepared by the Volta
   River Authority, and it says it applies to all the Authority's land-based projects whatever the
   funding. The Ghana-section plan annexes it as Annex 2 and builds on it. Title, publisher and the
   `conditions` sentence corrected; the framework's replacement-cost-or-market-value standard added.
4. **The plan's survey covers a route mostly dropped.** The report records the line cut from 210 km
   (171 in Burkina Faso, 39 in Ghana) to 188 km (171 and 17). The 87 households and 1,166 people were
   counted along the original 39.3 km in Ghana, more than twice what was built there. Added, because
   without it the planning figure reads as if it described the works.

`killed_note` was empty and now states both causes, the report's supervision finding, the 2024
report's stronger statement of cause, and that no other death appears in any of the three documents.

## 4. `benin-iame-transmission-compensation` (P110075) — KEPT

Confirmed verbatim from the completion report: paragraph 127 on the payments, including the
favourable opening "Most payments under the RAP received compensation on time", the first 50 km paid
by October 2012, the next phase planned for December 2014, the 60 km unaccounted for, the assurance
that all payments would be made by 31 December 2014, "They had encountered some resistance from those
who had not received their payments", the commercial short-term loan, payments made in early 2015,
and the March 2018 supervision finding of irregularities including "the existence of 70
project-affected persons who were identified but did not showed up" with the action plan setting the
money aside; and paragraph 108's "the to-be relocated people blocking progress on the line" with
"Construction of the transmission line financed by IDA only began in 2016". Confirmed from the
review: the same sequence as "protests from people who could not receive their compensations", the 70
who "did not receive their payments, because they did not contact the CEB", and the project team's
confirmation of compliance at closing, which the card attributes to the team and not to a document.
**All four versions of the 1,322 are right**: appraisal paragraph 62 "need to be physically
resettled", its annex "will need to be resettled and/or compensated", report paragraph 125
"resettled and/or compensated", review "were to be resettled". 123 + 61 = 184 and 640 + 682 = 1,322,
so the review's 184 families is the sum and not a new figure. Disclosure 21 January 2009 at the Bank;
28 January in the appraisal document and 29 January in the report, both given. Ten safeguard policies
confirmed against paragraph 122, which is itself the full list and not a partial one. Every financing
figure matches the data sheet. The contractor sequence SAE to GAMMON in 2015 to TELL in 2017, the
six-month payment-detail updates and the field workers' strike are verbatim.

**Corrected — 3.**
1. **M&E rating, the same fault as card 1 and in the opposite direction.** The card gave
   "Substantial", which is the data sheet's field. The report's section IV.A and its paragraph 121
   both say **Modest**, and the review's M&E rating is Modest too. Corrected to Modest with the data
   sheet's Substantial noted.
2. **"Three extensions totalling 38 months".** 38 is the review's own total; the parts it lists are
   one year, two years and six months, which come to 42, and the report says the project overran its
   original closing date "by three-and-a-half years". The card now gives the parts, the review's 38
   and the report's three and a half years.
3. **Effectiveness.** The data sheet says 13 July 2009; the review says "became effective ten months
   later on April 30, 2010". Both now printed.

What earns the card is limb (b) at a named place: unpaid compensation on the Onigbolo-Parakou line,
people awaiting payment blocking the works, a utility borrowing commercially to pay them, and 70
people found uncompensated in 2018. The card says plainly that nobody is counted as relocated.

## 5. `pakistan-edtip-crop-compensation` (P095982) — KEPT

Confirmed verbatim: the social safeguards paragraph, including "the common practice across all
DISCOs is to undertake assessment after the damages", "The result was that compensation payments were
severely and consistently delayed in the Project", "IESCO, LESCO and MEPCO reported
pending/outstanding payments even at the end of the Project", the one-year delay at IESCO, "MEPCO had
only paid 19% of the compensation owed for crop losses by the end of the project", the 15 affected
people whose land LESCO acquired, and the grievance mechanism's limited scope. The favourable
clauses are on the card. 66 per cent of subprojects completed and 51 per cent of cost spent are both
in the report. The three safeguard policies and the Azad Kashmir trigger are right. The review's
"Date Posted: 01/07/2016" is printed on the document, so that date needs no caveat; the risk rating
Substantial in the report against Significant in the review is handled correctly, with the report's
rating read out of the report. **The `killed_note` is right and the exclusion is right**: the FY13
zero / FY12 18 / FY11 11 figures are a footnote to a sentence about aerial bundled conductor reducing
public fatalities on HESCO's network, not deaths caused by the works.

**Corrected — 5.**
1. **Report number.** "ICR3137" on the card; the cover prints **ICR00003137**.
2. **Report date.** Cover 23 September 2014, data sheet 22 September 2014. Both now given.
3. **A cause and a subject swapped.** The card said "in one company the sub-divisional officer
   concerned acted as the assessor … and that this affected public grievances in that regard." The
   report says the **Project** kept its existing system of using the land revenue officers and the
   sub-divisional officer as assessors, that the social and environment cell "was not part of this
   process and could not play a role in prompt assessment, public consultations and outreach on the
   assessment process and replying effectively to public grievances in this regard", and that this
   hit the cell's efficacy. Rewritten to that.
4. **A sentence attributed to the wrong document, and reworded in the move.** The card had the
   Evaluation Group saying "improving performance on safeguards, particularly on compensation
   payments, remains critical to the distribution companies." The sentence is the **completion
   report's** own lesson and reads "Institutional reform on social safeguards, particularly on
   compensation payments, remains critical to the DISCOs functioning as modern, efficient entities
   embodying good practices on social issues." The phrase does not appear in the review at all.
   Reattributed and quoted properly.
5. **Implementing agencies and the cost column.** The report's safeguards section names five
   agencies; its data sheet lists six, adding the Pakistan Electric Power Company. And 309.37 /
   159.03 / 51 per cent is the cost table, where the financing table on the facing page gives
   309.86 / 159.59 / 52 per cent for the same quantity. Both noted.

**Absence claim refuted.** The card said the IESCO and MEPCO resettlement plans "give no total of
affected households or structures". Both give one, in the section headed "Affected Persons and
Assets": IESCO's Exhibit 5.1 counts **453 affectees** along 286 km of temporary right of way, about
2,145 acres, plus three grid-station landowners for four new stations; MEPCO's Exhibits 5.1 and 5.2
count **669 affectees** on 1,339 acres of cultivated land across six transmission line components
with crop compensation estimated at **Rs 9,626,145**, plus four landowners for five new stations. The
verbs are future ("will be damaged", "to be affected"), so they stay out of `displaced` and go in
`displaced_note` as planning figures — but they give the scale of the crop compensation that ended up
19 per cent paid, which is the card's subject.

## 6. `kiidp-kampala-roads-compensation` (P078382) — KEPT, and this one lost the most

Confirmed from the review (ICRR14588, Date Posted 25 February 2015, printed on the document): 494
project-affected persons compensated and 239 yet to receive compensation at the closing date of 31
December 2013; the attribution of most of the outstanding payments to unsubstantiated claims at ICR
paragraph 48; all eligible claims paid off by the time the ICR was concluded; the landfill
deficiencies at ICR paragraph 43, quoted accurately and completely, including their resolution within
a month of closure; the lack of capacity and of a safeguards specialist; the two restructurings and
the new category of eligible expenditure for involuntary resettlement created because the government
could no longer fully finance the resettlement cost. Board approval 6 November 2007, credit C4367 of
US$33.6 million, appraisal cost US$37.10 million, closing 31 December 2010 to 31 December 2013, all
from the review's data block. Three safeguard policies confirmed against the appraisal document's own
table. Confirmed from the October 2006 plan: 415 entities, 141 to relocate, the extra 15 per cent on
property value, the eligibility ladder down to licensees and squatters, the cut-off date of 15 April
2006, the three-stage grievance procedure.

**The ICR being undisclosed is confirmed, not assumed.** `wds?projectid=P078382` returns no
completion report of any kind, and the project's catalogue list has an appraisal document and the
review and no ICR.

**Corrected — 3, two of them cuts.**
1. **Three clauses cut as being in another project's document.** The card said the Kampala plan
   recorded "a 16-metre corridor would be used where houses were concentrated", that "a number of
   houses would have to be partially demolished", and that owners of partly affected houses feared
   being treated as encroachers in the road reserve. That passage is in the **Arusha** plan of the
   Tanzania Strategic Cities Project (RP913 v1, card 7 in this batch), at its section 3.6: "A corridor
   of 16 metres is proposed where there is concentrated number of housed being affected. However with
   a corridor of 16 m a number of houses will have to be partially demolished. On the other hand
   owners of partially affected houses are concerned with their fate and feel that in future they are
   likely to be considered encroachers in the road reserve land if not resettled." The Kampala plan
   contains no "16 m" anywhere — it recommends a 15 m reserve on two roads and a junction — no
   instance of "demolis", no instance of "encroacher", and no instance of "worri" or "fear". Cut.
2. **Relocated utilities read as people moved twice.** The card said "on one road it noted that
   people would have to move for the second time, having already been moved under an earlier road
   project." The plan's sentence is about "existing utility installations (water mains, sewer lines,
   electrical cables and telephone cables) … For some it will be the second time because they were
   moved during the NCRP." Cut.
3. **Second restructuring dated** 27 December 2012, from the review.

**ICIJ's figure explained, and it is a new entry for the handoff's table.** ICIJ gives **1,118** for
this project. The plan's census, in the section on the delineated corridor, counts **623 (55%)
renting and 495 (45%) claiming to own** — **1,118 people, to the person**. Added to `displaced_note`.
Also added, from the plan's scenario table: **91 of the 141 relocations fall on the Lubigi primary
channel**, which runs through Kawaala — the same channel and place as the Inspection Panel case
registered under the successor project, which the card's `outcome` already mentions.

## 7. `tanzania-tscp-compensation-delays` (P111153) — KEPT, and rewritten in three places

Confirmed verbatim from the completion report (ICR00005449, 13 May 2021): paragraph 63 entire, with
the card's quotation exact — "RAP implementation was often delayed sometimes to over nine months when
LGAs lacked funds for compensation of PAPs thus delaying construction activities and raising
complaints by PAPs" — and its favourable opening, "Subprojects complied with Resettlement Action Plans
(RAPs)", on the card; paragraph 64 on the grievance committees, the logbooks, the absence of any
contractor-level procedure for workers' complaints, the unbudgeted mechanism and the uncertainty after
closing; paragraph 48 on counterpart funding, naming the landfill buffer zones at Mwanza, Kigoma-Ujiji
and Mbeya and the road corridor wayleaves at Ilemela and Arusha, the engagement with the Treasury, the
delayed payments to contractors and "Delay in utility removal and compensation was also revealed to be
a source of grievances". Credits, SDR 236.2 million, dates, the single restructuring of 4 May 2020,
Denmark's US$12.5 million recorded as nil, US$340,372,832 disbursed of US$342,997,608: all match the
data sheet. Outcome Satisfactory, Bank performance Satisfactory, M&E Substantial, and here data sheet
and body agree (paragraph 60). The review agrees on all three and prints no date, so the catalogue
caveat is right.

**Corrected — 6, two of them cuts of unsourced figures.**
1. **The Mbeya paragraph was not in the Mbeya plan.** The card gave "75 buildings, 34 fences, 43
   stands of permanent crops, 26 kiosks, 4 walls, 2 hedges, 15 stalls and one well", "55 people …
   mostly totally", all 55 squatters in the right of way, "14 claiming for crops, 4 for a building
   only and 37 for both", and relocation "to land the council provided in the Mdenga Namadi area".
   The cited plan (RP913 v5, Mbeya City Council, March 2010) says, in its census section: "Census
   survey for affected property on Mbeya city roads project revealed that mostly affected assets are
   35 buildings including fences and 6 areas with crops. A total of 41 people will be affected." The
   file contains no "55", no "Namadi", no "kiosk", no "hedge" and no "stall" count; nor do the ICR,
   the review, the appraisal document or the other two plans. Replaced with what the plan says, plus
   its entitlement-matrix line that people without formal legal rights get full replacement cost for
   assets but nothing for land "because they are encroachers along the road reserve".
2. **"Another plan counts 161 households to be affected by a proposed road" — cut.** No "161"
   appears in any of the three cited plans.
3. **The 16-metre passage given its document.** It is the Arusha plan's, quoted above under card 6,
   and is now attributed to the Arusha plan on this card, where it belongs.
4. **The Arusha entitlement list completed.** The plan gives four categories and the card gave two:
   added the 20 households owning land only and the 13 administrators acting for 23 deceased and a
   shrine. That last matters, because of correction 6.
5. **Dodoma, three errors in one sentence.** The plan says "A total of **3 buildings** and 20
   farmlands will be compensated at Chidaya landfill site", not three households; it says the city
   development authority "**has agreed to pay** each household a total of Tshs. 400,000 by way of
   accommodation (Tshs. 300,000) and transport allowance (Tshs. 100,000)", not that it had already
   paid, and says nothing about six months; and the reason it gives for there being no resettlement
   issue on the Kisasa roads is that the people living along them "have been required to relocate from
   RoW for many years ago (since 2002) before the commencement of this project". All three corrected,
   and the plan's own figures added: about 29 households at Kikuyu and 21 at Chidaya village, which it
   converts at 4.3 people a household to about 100 people affected, with dwelling houses and several
   graveyards among the affected structures.
6. **A partial list of safeguard policies.** The card said the project triggered environmental
   assessment and involuntary resettlement. The appraisal document's table and the report's paragraph
   65 both give three, the third being **Physical Cultural Resources OP/BP 4.11** — material on a card
   whose plans count 23 graves, a shrine and several graveyards. Added, with category B partial
   assessment and the appraisal document's disclosure dates (draft 2 and 5 February 2010, final 5 May
   2010 at the Bank and in Tanzania).
Also: "portfolio-wide issue affecting other Bank-financed urban projects **in Tanzania**" — the report
says "other Bank-financed urban projects as well", without the country. Corrected. And the three
March 2010 plans were prepared by the **Prime Minister's** Office - Regional Administration and Local
Government, renamed the President's Office later; source publishers and the role field now say so.

## 8. `vietnam-redp-small-hydro-land` (P103238) — CUT

Confirmed first, because the quotations are accurate: paragraph 44, "The implementation of REDP
financed SHPs did not involve significant resettlement and/or create any adverse socioeconomic
impacts. In total, the project required reallocation of less than 50 households and affected more than
2,000 households in term of losses of agricultural/tree crop land and sources of incomes"; and
paragraph 82, the same with "no adverse socioeconomic impacts have been recorded" and "approximately
2,500 households". The card quotes both and both of their favourable halves.

**Cut on the forward rule.** Limb (a) fails: no document counts anyone relocated, and "less than 50
households" is a ceiling attached to no plant, province or community. Limb (b) fails at outcome: the
report says land acquisition, compensation, livelihood restoration and ethnic minority development
complied with the plans, that the only social issues were minor, "such as slightly late
compensations", and both it and the review rate the project Highly Satisfactory. What is left is a
count of households affected by land loss with no named site, no named people, no arrears and no
recorded failure to restore a livelihood — the shape CHECK20 drops. The specific, sited material on
this project is all planning material, and a plan saying people will be moved is not harm.

**One correction recorded so the drop is honest, and it cuts the other way.** The card's claim that
"the five subproject resettlement plans examined all record nil relocated displaced persons" is wrong.
Three of them do say "there is no HH have to relocate" and print nil relocated. The **Ha Tay** plan
(RP755 v6, Chu Pah district, Gia Lai province) states that of 1,394,649 m² acquired, the reservoir bed
takes 211 m² of residential land of 7 households, "(04 households shall have to relocate)" in place,
together with one-crop rice land of 47 households and burnt-over land of 61 households. That is a
named site where the works needed ground people lived on. It is still a plan, and no outcome document
for Ha Tay was found, so the drop stands — but the lead can reinstate the card on that basis, and if a
later round finds an outcome document for Ha Tay it is a case.

---

## The two weakest keeps

**1. `tanzania-tscp-compensation-delays`.** The writer named it as the weakest and the check did not
improve it; it got worse before it got better. Its whole outcome harm is one sentence — compensation
delayed, sometimes over nine months, with complaints raised — attached to no count of people, no city,
no number of complaints and no statement that anyone was unpaid at closing, in a report that rates the
project Satisfactory and says the subprojects complied with their plans. Everything concrete on the
card is a March 2010 planning figure, and two of the figures the card carried were not in the documents
it cited. It now rests on what the three plans actually say plus that one sentence. If the lead wants
one card out of this batch, this is it.

**2. `kiidp-kampala-roads-compensation`.** It rests on a single document, because the completion report
is undisclosed; the 494 compensated and 239 unpaid exist only as the review's report of ICR paragraph
48, and the underlying document cannot be read. The check also removed two passages from it that were
not in its own plan. What survives is strong in kind — 239 people unpaid on the day a credit closed —
but it is one sentence of one review, and the review adds that all eligible claims were paid in the
end.

## For the lead to decide

1. **`vietnam-redp-small-hydro-land`**: cut on the forward rule, reversible. The Ha Tay plan's named
   site and 4 households is the argument for reinstating; the absence of any outcome document and the
   lender's compliance findings are the argument against.
2. **`ctb-kwabenya-stone-crackers` lost Benin and Togo** from `iso3_more`, and the CEB cash-flow
   finding came off the card's harm narrative. That finding is real and belongs on a P094917 card if
   one is ever written. If the lead wants the countries kept for the lending flow rather than the harm,
   that is a mapping convention question, not a facts question.
3. **The 2024 Project Performance Assessment Report for P094919** is the first field-visit evaluation
   document in these ICIJ tranches. `wds?projectid=` was not queried for PPARs in this round's
   research; of the seven surviving projects only P094919 has one. **Worth a sweep across rounds 17 to
   21's 95 ICIJ cases**: a PPAR carries stronger cause statements than an ICR, as this one does.
4. **The M&E data-sheet fault is systematic, not incidental.** Two of eight cards took the M&E rating
   from the data sheet where the report's own body says something else, once higher and once lower.
   Add to BRIEF: read every rating from the body section that justifies it, and print the data sheet's
   value only as a second figure.

## Faults that appear on more than one card

1. **The data-sheet-against-body rating**, on P101645 (Modest against Moderately Satisfactory) and
   P110075 (Substantial against Modest). Same mechanism the lender-role audit named: the nearer copy
   of a figure goes in.
2. **A passage from one project's document on another project's card.** The Arusha plan's 16-metre
   corridor and encroacher sentences appear on both the Kampala card and the TSCP card. The TSCP card
   is where they belong. This is the first cross-card contamination of this kind in the rounds this
   file records, and it is worth a line in the next check brief: when the same unusual sentence appears
   on two cards in a batch, one of them is wrong.
3. **Absence claims that a grep refutes**, twice: the Pakistan plans' totals and the Vietnam plans' nil
   relocations. Both were claims about documents already on disk.
4. **Dates asserted as signings.** Three on the CTB card, all of them agreement dates cited in a
   footnote.
5. **A partial list of triggered safeguard policies**, on the TSCP card — the same class the audit
   found at Wudu and Yining, and again the omitted policy was the one that mattered.

## Figures where two documents disagree

1. **P101645 M&E quality**: data sheet Modest; section IV.A and paragraph 114 Moderately Satisfactory.
2. **P110075 M&E quality**: data sheet Substantial; section IV.A and paragraph 121 Modest; review Modest.
3. **P110075 effectiveness**: data sheet 13 July 2009; review 30 April 2010.
4. **P110075 extension**: review 38 months; its own components 12 + 24 + 6; report "three-and-a-half
   years". The review also says the actual project cost was not reported in the ICR, where the ICR's
   data sheet prints US$107,960,374.
5. **P095982 report date**: cover 23 September 2014; data sheet 22 September 2014.
6. **P095982 total project cost**: cost table 309.37 / 159.03; financing table 309.86 / 159.59.
7. **P095982 risk to development outcome**: report Substantial; review Significant, in both columns of
   its own ratings table. And the agency's name: MEPCO in the report, MESCO in the review.
8. **P094919 the second death's date**: report, both accidents in July 2017 less than a month apart;
   review, tower collapse "On July 2017" and the drowning "A month later". Both on the card.
9. **P094919 who the casualties were**: report, two workers on the tower, one killed and one seriously
   injured, plus a minor drowned; 2024 performance assessment, "two fatalities and the serious injury
   of a third worker".
10. **P094919 Ghana line length**: 39.3 km in the resettlement plan; 39 km then 17 km in the report,
    after the first restructuring.
11. **P094919 affected communities**: "all the 16 communities" and "fifteen settlements" / "all the 15
    communities", in one plan.
12. **P075994 addendum table**: "Original no. of PAPs" rows 226, 16, 1 against a printed total of 43.
13. **P075994 the 2004 plan's date**: running header December 2004; cover February 2005.
14. **P103238 households that lost farmland and income**: more than 2,000 at paragraph 44; about 2,500
    at paragraph 82, in one report.
15. **P075994 ICR borrower performance**: split Ghana Moderately Satisfactory / Benin Unsatisfactory in
    the report; a single Moderately Satisfactory in the review's ICR column.
16. **P095982 implementing agencies**: five in the safeguards section, six in the data sheet.
17. **P111153 implementing agency's name**: Prime Minister's Office in the 2010 documents, President's
    Office in the 2021 report.

## Errors in the Bank's own documents, found while reading

- The P110075 completion report lists Safety of Dams as "OP/BP 7.60", which is Projects in Disputed
  Areas; the policy is OP/BP 4.37. The card does not reproduce the slip.
- The P094919 completion report's financing table gives the World Bank total actual as US$36,347,292
  and the total project cost actual as US$36,347,293.
- The P078382 resettlement plan's own census total, 1,118, is not printed anywhere in the plan as a
  total; it is 623 + 495 from the same sentence, which is also ICIJ's figure.

## Routes

**Worked.** `search.worldbank.org/api/v3/wds?format=json&projectid=<P>&fl=docdt,display_title,pdfurl,docty`
for all seven surviving projects, then the `pdfurl` host rewritten from `documents.worldbank.org` to
`documents1.worldbank.org` and fetched with `curl` and read with `pdftotext -layout`. All 33 source
URLs on the kept cards return HTTP 200, re-checked one by one after the corrections, the Eiffage page
included. `qterm` searches worked for the absence checks on the P101645 resettlement audit.

**A font that defeats `pdftotext`, and the fix.** The P075994 addendum's cover and several of its
bullet lists use a font whose glyphs are offset by 29 code points, so extraction yields
`35(3$5('%<` for "PREPARED BY" and `-8/<` for "JULY". Subtracting the offset recovers the text and
with it the document's date. Worth knowing before anyone records another document of this vintage as
undated: **check for a shifted-glyph cover before writing that a document prints no date.** Two of the
three date claims corrected in this batch were of that kind.

**Failed, named as routes.**
- `https://search.worldbank.org/api/v3/wds?format=json&qterm=TEDAP%20resettlement%20audit&fl=docdt,display_title,pdfurl,docty`
  — returns `total: 0`. The longer form
  `qterm=Tanzania%20Energy%20Development%20Access%20Expansion%20resettlement%20audit` returns 14
  documents and no resettlement audit. Not a refusal; the document is not in the archive.
- `https://search.worldbank.org/api/v3/wds?format=json&qterm=Mbeya%20city%20council%20resettlement%20action%20plan%20Strategic%20Cities&fl=docdt,display_title,pdfurl&rows=10`
  — returns one document, for an unrelated Tanzania-Zambia interconnector. The RP913 volumes are found
  by `qterm=RP913%20Tanzania%20Strategic%20Cities%20resettlement`, which returns all eight city volumes
  plus a 2012 valuation volume.
- No other route was attempted and no host refused anything. No permission prompt was raised, so the
  fetch gate stayed open for the whole run.

**Not attempted, and a gap worth naming.** No search outside the Bank was run in this check. The
writer reports real searches for each of the eight and nothing independent found, and every surviving
card is `contested` on that basis, which is the right setting whatever an outside search would have
returned, because each rests on the lender's own documents. If the lead wants any of these moved to
`documented`, the places to start are the two named in the cards: the Burkina Faso labour inspectorate
or SONABEL on the two 2017 deaths, and Beninese press or court records on the Onigbolo-Parakou
compensation.
