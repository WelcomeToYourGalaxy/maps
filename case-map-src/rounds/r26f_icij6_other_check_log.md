# Check log: round 22, batch C (`rounds/r26f_icij6_other.json`)

Checker's output: `rounds/r26f_icij6_other_checked.json`. Nothing merged, nothing built, nothing committed.

**No writer report exists for this batch.** The handoff records that it was never written. Everything below
was worked out from the batch file, `docs/leads_c_other_2.json`, `docs/HANDOFF.md`, `docs/BRIEF22.md` and
`docs/CHECK20.md`, and from documents found and read for this check. A missing justification is not taken
here as the absence of one: where a claim checked out, it is recorded as confirmed, not as a lucky guess.

**The document cache died with the previous session and was rebuilt.** 37 files were downloaded for this
check into `/home/claude/r22/cache`, paired `.pdf` and `.txt`, named by P-number: `P088994_{ICR,ICRR,PAD}`,
`P130413_{ICR,ICRR,RAP,RAP2,PAD}`, `P124720_{ICR,ICRR,RAP,RAP_RPF,PAD,ISR_20160410,ISR_20161225,ISR_20170518}`,
`P126180_{ICR,ICRR,RAP,RAP2012,PAD}`, `P125032_{ICR,ICRR,RAP,RAP2013,PAD}`,
`P090135_{ICR,ICRR,RAP_akure,RAP_gombe,RAP_mokwa,RAP_enugu}`, `P064438_{ICR,ICRR,RAP,PAD}`, plus
`JACSES_letter_20061026`, `JACSES_factsheet_20061128`, `JACSES_index.html`, `connor_repec.html`,
`wds_P124720.json`. The folder is shared with two other checkers; nothing in it was deleted and no file
not listed above is claimed as this job's download.

**Result: 1 of 7 cut as a duplicate, 6 kept, every one of the 6 corrected.**

---

## 1. `taunsa-barrage-basti-shaikhan-relocation` (P088994, Pakistan) - CUT, duplicate

**The project is already on the map, as `taunsa-barrage-relocation` (Taunsa Barrage, Indus River, Punjab,
2005-2009).** Same loan (US$123 million, approved 15 March 2005, closed 31 December 2009), same completion
report, same Evaluation Group review, same two villages moved in June 2005 at the ICB-01 contractor's
request, same 160 families and about 900 people, same breach of OP 4.12, same canal closures, same JACSES
report of 38 people indicted, same Descon protest, same Dawn and JACSES sources.

`dedupe_leads.py` reported P088994 as new because the existing case carries no P-number - the exact failure
the handoff warns about, and the lead row's own `_local_match` flagged `taunsa-barrage-relocation` at
strength 3. Confirmed by place and years as the handoff instructs, by reading the live case out of
`window.CASES`.

Set to `"status": "dropped"`, `"r22_outcome": "already_on_map"`, with the new material carried in
`_extend_recommendation` so the lead can decide whether to write an extend. **The material genuinely new to
the map is substantial and was checked against the documents**, and it includes one correction to the
existing case: the live case dates the Descon protest to August 2007 and cites Dawn news/262073; the protest
at which a case was filed against some 15 people and two were arrested is Dawn news/205738 of **12 August
2006** (dateline Multan, 11 August), fetched and read. The existing case also carries `displaced: 900` where
the report's unit is 160 families; that is the lead's call, not a new finding.

**Corrections found in the draft, recorded so they are not carried into an extend:**

- **Unsupported figure.** `displaced_note` attributed "157 households and 799 people" to the Japan Center's
  reading of the resettlement action plan of 29 November 2005. That figure is in neither the 26 October 2006
  letter (read in full, 7 kB of text) nor the English project page (read in full). The 28 November 2006
  factsheet is in Japanese with an Adobe-Japan1 CID font: `pdftotext` returns 239 bytes, and `pdftoppm` at
  130 dpi renders page 1 with every Japanese glyph dropped. **Nothing can be read out of that file by any
  route tried**, so the claim is unsupported as cited. 799 is also exactly ICIJ's own number for this project.
- **Date error.** The draft says "In January 2026, Dawn reported" the police and bulldozer operation. The
  Dawn article is dated **24 April 2026** and reports an operation that took place in January. Report date
  and event date are different dates.
- **Place error.** The draft says the August 2006 protest was held "in Multan". Multan is the dateline; the
  protest was at the barrage.
- **Over-specification.** The draft says the May 2006 protest was "at the resettlement site". The article
  does not say so; it says the rally was taken out during a World Bank delegation's visit and that police
  first blocked the protesters, who then pushed through to the delegation. The police blocking is adverse
  and the draft omitted it.
- **Attribution dropped.** The draft gives the Rs 40,000 and Rs 16,000 payments as the Japan Center's own
  statement. The letter's own words are "According to villagers of Basti Sheikhan ... and Basti Allah Wali".
- **Quotation summarised.** The draft has the review saying the Bank "could have" done more "on
  environmental and social issues at entry". ICRR13423 says: "The Bank could have done more to ensure that
  the Project Management Office developed a thorough communications strategy and was adequately staffed to
  manage the environmental and social aspects of the project."

**Confirmed in the documents:** 160 families, 137 left bank and 23 right, "comprising of some 900 people"
(ICR0000998, section 1 and Annex 9); the Annex 9 narrative in full; initial RAP cost Rs 12.42 million,
Rs 14.704 million spent of a revised PC-1 provision of Rs 19.883 million, plus Rs 17.150 million of community
works, total Rs 31.855 million; 2.8 hectares of new sites; 136 local people employed by the contractor
including 66 affected persons; ICRR13423 `Date Posted : 03/24/2011`; the WWF baseline survey passage
including "some 25 Indus Dolphins within 2.5 km of the Barrage ... appeared to have been displaced by the
disturbance arising from project activities" and "Not all recommendations of the report were implemented";
the dolphin incident passage; and the health and safety section, read in full - it records protective
equipment in use and HIV/Aids and Hepatitis training and no deaths, so `killed: 0` with its absence note
stands. The section also records a coffer dam breach causing extensive damage because there was no adequate
emergency response system at the site, which the draft did not use.

---

## 2. `agara-zemo-osiauri-e60-agarebi` (P130413, Georgia) - KEPT, corrected

**Not a duplicate.** The map's `east-west-highway-khevi` covers the Rikoti Pass and Khevi sections from 2020
under ADB, EIB and World Bank finance; this is the Agara to Zemo Osiauri section, km 114 to 126, under credit
IDA-52450 and loan IBRD-82630, 2013 to 2019. Separate loans, separate works, separate section.

**Confirmed against ICR00005191:** approval 9 May 2013, effectiveness 5 August 2013, mid-term review
20 April 2016, original closing 28 February 2018, actual 31 December 2019, restructurings 7 December 2017 and
27 February 2019 both for the closing date; IBRD reduced to US$35,023,065; disbursements US$35,738,583 and
US$35,023,065, US$70,761,648 of US$75,000,000; Georgia US$21,549,436 against US$18,750,000 - every figure
read out of the data sheet's own columns, which is where round 22's audit found three errors elsewhere.
Ratings read out of each document separately: the report rates outcome Satisfactory, Bank performance
Moderately Satisfactory, M&E Substantial (paragraph 62 and the KEY RATINGS block); ICRR0022356 rates outcome
Moderately Satisfactory on "Modest Efficacy of PDO 2" and Bank performance Moderately Satisfactory, and
agrees on M&E Substantial. Paragraph 67's quoted clause "required land acquisition causing both physical and
economic displacement" is verbatim. Paragraph 68's figures - 110 ha, 571 parcels, 40 per cent private,
1,162 persons in 272 households, five households resettled, four businesses stopped, one plant and 20
reservoirs relocated within the company's own grounds, 20 ancillary and 45 minor structures, GEL 8.2 million,
resettlement complete February 2018 - all verbatim. Paragraph 69's complaint narrative and the June 2020
livelihood restoration plan for 44 households, verbatim. Contractors COPRI and Blacksea Group confirmed at
paragraph 46, including the report's own framing of the sub-contract as an unintended benefit.
The March 2017 plan's paragraph 25 confirmed word for word, including both quoted sentences about the two
households at interchange two. The addendum of **11 January 2018** confirmed: 2 affected households, 7
persons, one of them (4 persons) to be resettled, bringing the section to "a combined total of 5 households"
physically displaced.

**Corrected:**

1. **An absence claim, refuted.** `confidence_note` said "The completion report carries no printed date;
   30 September 2020 is the date the Bank's document system records for it." The report's cover page prints
   **30 September 2020** (line 44 of the extracted text, immediately under the report number). Rewritten to
   state the cover date. The claim about the review is correct and kept: ICRR0022356 prints no date anywhere
   on its 22 pages, checked by grepping the whole file for "2021", "June" and "posted" - no match.
2. **Selective quotation.** The card took the 50 Agarebi complaints out of paragraph 68 and left behind the
   sentence immediately before them: "No complaints related to land acquisition and resettlement were
   reported." It also left the clause saying the second interchange's design "saw several modifications aimed
   at minimizing resettlement impact". Both added to `community`, and the first added to `confidence_note`.
3. **A plan figure that could be read as an outcome.** The five resettled households, the 272 households and
   the 1,162 persons all appear in the January 2018 addendum's own table under "Final updated 2018", a month
   before the report records resettlement as complete. The report's verb is past tense and this is a
   late-project plan update of the kind BRIEF22 says can carry an outcome, so `displaced: 5` stands - but
   `displaced_label` and `displaced_note` now say where else the figure sits, so a later reader is not left
   to discover it.

---

## 3. `maluku-sez-maes-inkiene-demolition` (P124720, DR Congo) - KEPT, corrected; one of the two weakest

**What earns the card had to be found, and it is not what the draft led with.** The draft's harm was a
resettlement plan (58 households, a plan) plus a safeguards breach. The completion report counts nobody
relocated, so limb (a) fails. Limb (b) is met by one thing, which the draft had only in a company's role
field: the **Implementation Status and Results Report of 10 April 2016**, found through `wds?projectid=`
and downloaded for this check, records that the wholesale market was built "on a plot of 14ha allocated by
the Government within the Maluku SEZ **while the owner of the land has not yet been compensated**", and that
compensating that owner was one of the two conditions for lifting the suspension. The completion report puts
the ground for the suspension as non-adherence to safeguards "with regard to resettlements and compensation
of owners being displaced because of the establishment of the SEZ". Land taken and compensation unpaid, the
lender's own record, with the Bank's own formal sanction attached. Both are now in `community`.

**Corrected:**

1. **A factual error.** The draft said the report "describes two cases in which compensation was paid to
   people who turned out not to own the land". Only one is that. In the second (November 2019, family Y) the
   report records that the claimants' "fraud attempt ... was revealed" and they withdrew at the Court of
   Tshela - no wrong payment. The first case (October 2018, family X) is also **recorded as closed on
   12 December 2018 after negotiations between the parties**, which the draft omitted. Rewritten to one case,
   with its resolution.
2. **A derived figure presented as a count.** The plan's "about 545 persons" is its own extrapolation: it
   surveyed 46 of the 58 households, found 431 people, took the average of 9.4 and applied it to all 58.
   Said so in `community` and `displaced_note`. This map does not reconstruct arithmetic and should not
   reprint someone else's without saying what it is.
3. **The plan contradicts itself on the villages.** Its summary table and body text say 22 households at
   Inkiene and 37 at Maes; its own numbered list runs Inkiene at rows 1-21 and Maes from row 22. The draft
   silently followed the list. Both now given.
4. **Writer's arithmetic.** "Leaving 12 of the 49 with nothing recorded" became "the report says that 37
   were declared eligible and received compensation, and says nothing about the other 12".
5. **A figure given a unit the source does not give.** The review prints the actual spend on component 2 as
   "US$6", with no unit, where it writes "million" for every other component. Stated as the review prints it,
   in the role field and the outcome.
6. **Favourable material omitted.** The report rates environmental and social safeguards overall moderately
   satisfactory and records that supervision missions found the instruments were being adhered to. Added.

**Confirmed:** report number ICR00005497, cover date 30 June 2021, ratings Moderately Satisfactory /
Moderately Satisfactory / Modest, and ICRR0022662 agreeing on outcome and Bank performance and on M&E Modest;
the suspension notified 13 January 2016 and lifted 29 March 2017, 14.5 months, under category 2.3; the MIK
quotation, verbatim and in full; the 622 people and US$4,422,055.68, with US$3,906,544.01 for the Maluku
plan; the 49 growers' complaints of September 2018 and the 37 found eligible; "around ten" occupational
incidents, mostly minor finger and foot injuries, and no deaths reported by the project unit; the seven
safeguard policies and the riparian exception of 1 May 2013; the resettlement plan's 58 households, 37
further rightsholders, 2,800 m2, 39 ha and about 20 ha, the football pitch, the preserved cemetery, the
233 ha footprint and 11.3 ha inhabited, and the Artelia census with its 25 July 2012 cut-off; annex 8's
"Success story", its 244 ha, and its silence on the resettlement, the suspension and the complaints.

**One ambiguity left standing, because both documents are in the file:** the completion report calls MIK a
"joint venture between the Government of DRC and the South-African operator Africom"; the 2016 status report
expands MIK as "Marché International de Kinshasa", the wholesale market itself. The card follows the
completion report, which is the cited source, and the status report's sentence is quoted separately.

---

## 4. `freetown-wellington-33kv-demolitions` (P126180, Sierra Leone) - KEPT, corrected

**Confirmed against ICR00004215:** data-sheet approval 23 January 2013, effectiveness 18 September 2013
against an original 20 September 2013 (printed "09/20/2103"), closing 31 October 2015 to 31 July 2017,
US$15.67 million disbursed of US$16 million, category B, two policies triggered; relevance of objectives
High, outcome Moderately Satisfactory, Bank performance Moderately Satisfactory, M&E Moderately Satisfactory,
efficiency Modest ("Overall efficiency is also rated Modest"), all read out of the report itself;
ICRR0021153 rates outcome and Bank performance Moderately Satisfactory. Paragraphs 68 to 71 verbatim,
including "additional damage to properties", the contractor's "lack of speedy responsiveness ... in adhering
to very basic safety precautions", the escalation and "disbursement was subsequently suspended for a while to
force compliance", the two outstanding payments totalling about US$1,000 and their two reasons, the 65 to 70
people in the livelihood programme and the 68 hand washing basins. The 2016 plan's 107 affected persons, 81
partial and 26 complete demolitions, 54 towers, the 2010 round in which only 22 of 23 were paid, the
self-demolition condition and "However, not all the PAPs complied and have continued to occupy the RoW", the
2012 plan never implemented, the 31 January 2015 cut-off, the over-75-per-cent clause, the four-tier
grievance process and CARL as external monitor - all verbatim. The review's 164 households compensated during
preparation under the earlier Power and Water Project's plan, confirmed. The DFID claim is right, and it is
the report's own: paragraph 62, "A change in the priorities and the support nature of a key donor (DFID) led
to a level 1 restructuring", with the cancellation of the rural electrification component and DFID's wish to
exclude the photovoltaic pilot. The no-mid-term-review claim is right and is the report's own cause, not the
writer's: "The midterm review (MTR) exercise could not take place, because it coincided with the outbreak of
the Ebola crisis." The two internal conflicts the draft flagged are real: the monitoring section dates the
level one restructuring to October 2013 where the rest of the report dates it to October 2015.

**Corrected:**

1. **Selective quotation, and the sharpest instance in the batch.** The card quoted the plan's
   "In anticipation of any potential resistance by the current occupants to prevent the project from taking
   place" and stopped. The same paragraph goes on: the inter-ministerial committee was formed so that "the
   Government and in particular the President achieves its agenda of providing electricity in the capital
   city", and it ends "As a result the chances that resistance to relocate might arise is minimal if not
   none." Both added. The quoted clause reads as preparation for force; the paragraph it sits in says the
   opposite about the expected outcome, and the card must carry both.
2. **A clause trimmed at the favourable end.** "the plan was implemented with two cash compensations
   outstanding" is the report's "was implemented satisfactorily with only two outstanding cash compensation
   (totaling about 1000 USD) largely attributed to procedural bottlenecks". Quoted in full now.
3. **Omitted rating.** The report's overall safeguards rating of Moderately Satisfactory, and its statement
   that the project was in compliance at the time of finalising the report, added to `outcome`.
4. **A restructuring date printed from one place only.** The data sheet gives 29 October 2015; the
   restructuring table in section H gives 28 October 2015. Both printed, house style.
5. The review prints no date anywhere; 4 June 2018 is the Bank document date. Said so in `confidence_note`.

---

## 5. `laulara-solerema-road-structures` (P125032, Timor-Leste) - KEPT, heavily corrected; the weakest keep

**`killed` moved from 1 to 0.** The draft counted the loader operator who died on 14 August 2022 on the
strength of the report's lesson that stone masonry guard rails "should be improved upon or replaced ... as to
avoid fatal incidents, such as the one involving a loader operator of the TLRCRP Lot 2 contractor - on
August 14, 2022". That is a recommendation about the project's guard rails, not a statement of what caused
the death. Paragraph 68, the only other place either death appears, says the two fatal traffic incidents
"were not reported immediately", that root cause analysis reports were submitted on 23 November 2022, and
what corrective actions the Bank then required - it does not give the contents of either analysis. Under
BRIEF22's rule the deaths belong to this project, because the Lot 2 contractor's works are what the credit
paid for, but neither is counted, because no document states a cause. Both now sit in `killed_note` with the
documents named.

**The plan contradicts itself, and the draft used one side of it.** The updated Lot 2 plan of August 2018
says twice that "26 APs with 146 households will be displaced since their residential structures need to be
demolished", and in a later section that the number is "12 APs with 84 households". It gives the household
total as 1,454 in its summary and 1,545 in its socio-economic chapter, and 164 structures owned by "123 APs
with 771 AHs" in one place and "122 APs with 871 AHs" in another. It also uses "households" and "family
members" as the same word throughout. All of this is now on the card, and `displaced` stays unfilled.

**Also corrected:** "11 toilets" was the writer's sum of a table that prints 7 permanent, 2 semi-permanent
and 2 temporary; printed as the table prints it. The report's own favourable findings - social safeguards
compliance rated **overall Satisfactory**, "with World Bank safeguard requirements being observed", and
compensation paid to all affected people on every lot - were absent from `community` and `outcome` and are
now in both. The title was changed from "Houses and Roadside Stalls Taken" to "Roadside Stalls and Houses
Listed for Demolition", because no outcome document records a demolition; what the completion report records
is that the plan listing them was carried out in full and paid in full.

**Confirmed:** ICR00006223 dated 29 November 2023, ICRR0023845; the four tranches and their amounts,
US$80,596,762 disbursed of US$95,201,256, Timor-Leste's US$50.9 million against nothing planned, total
US$131,496,761; mid-term review 12 December 2014, closings 31 December 2015 to 31 December 2022, the two
additional financings and four restructurings; category B with environmental assessment, indigenous peoples
and involuntary resettlement; the report's outcome Satisfactory, Bank performance Moderately Satisfactory,
M&E Modest, social safeguards Satisfactory and environmental safeguards Moderately Satisfactory, against the
review's Moderately Satisfactory on outcome and Bank performance. From the plan: 242 affected persons, 11 on
the re-alignments with 105 members, 164 units with 102 barakas owned by 82 households, 13 permanent and 8
semi-permanent commercial structures, 8 permanent, 4 semi-permanent and 8 temporary residential structures,
13 temporary kitchens, 78.9 m of concrete fence, 245 m of temporary fence, 203 m of cyclone wire,
1,190.63 m2 belonging to 34 affected persons, 7,432 trees with 5,364 fruit or fruit-timber and 796 timber,
2,847 already removed on the re-alignments, "All the surveyed assets encroached on the land owned by the
government", and the relocation-is-not-a-preference sentence. From the report: the 1,184 affected people and
their split across five lots, the 53 grievances split 43 / 6 / 4, the one gender-based violence incident, the
tree that fell on a house in April 2022, and the road safety audit lesson. The Marino Enterprise quotation in
the companies array is complete, including the half that says the contractor paid and the man rebuilt
outside the right of way - the one place in this batch where the writer quoted a passage whole.

---

## 6. `nigeria-federal-roads-trader-relocations` (P090135, Nigeria) - KEPT, corrected

**Confirmed against ICR00004170:** cover date 29 December 2017; SDR 207.5 million, US$330 million, grant
TF-56896 of US$3 million; approval 3 April 2008, effectiveness 23 January 2009, closings 31 December 2016 to
30 June 2017; disbursements US$301,133,499 and US$2,488,183; Nigeria US$31,344,000 of US$32,000,000;
restructurings 2 February 2011 (results framework, components and cost, legal covenants) and 21 December
2016; outcome Moderately Unsatisfactory, Bank performance Moderately Unsatisfactory, M&E Modest, with
ICRR0021110 agreeing on both; "6TTLs over its 9 years of implementation, in addition to 4 Social Safeguards
Specialists and 4 Environmental Specialists"; the fatality rate indicator 161 baseline, 120 target, 143
achieved. Paragraphs 73 and 74 verbatim, including the 675, "Largely the owners of these businesses have been
compensated and all have confirmed their satisfaction, though payments were later than expected", the April
2016 mission finding that people on the Akure to Ilesha road "had not been paid compensation as late as March
2016, even though the works had been completed", the single treasury account reason, and "Subsequently the
counterpart funds have been released and payment made to all PAPs." **The draft carried the favourable
clauses as well as the damaging one, which is the first batch in several rounds where that was true of the
central passage.** The three plan counts check out: Akure to Ilesha 130 with N7,294,407.13 and the 10 m
setback, Gombe to Biu 190 at 3.65 m, Mokwa to Bida 366. The Enugu plan does name Patricia Anyanwu, and its
compensation schedule carries N21,000 to her for "RELOCATION OF KIOSK", which the draft did not use.

**Corrected:**

1. The 21 December 2016 restructuring changed the results framework as well as the closing date.
2. **A manufactured gap.** `displaced_note` said the plans' 130, 190 and 366 "come to 686, eleven more than
   the report's 675, and no document found explains the difference". These are not the same quantity: the
   plans are pre-works estimates for three of the five roads that had plans, and 675 is the report's
   project-wide outcome. Rewritten to say what each measures and to drop the invented discrepancy.

**Left standing for the lead, not corrected:** `displaced: 675` holds people who "had to relocate their
businesses", a trading place and not a dwelling. The unit is people, the document is the completion report
and the verb is "relocate", so it meets the field's test as written, and `displaced_label` says in its first
words that these are trading places. But it is the first time this map has put business relocations in that
field, as far as this check could tell, and it is a precedent the lead may want to set deliberately.

**One oddity in the document, not an error on the card:** paragraph 73 says "OP 4.10 was triggered and a
Resettlement Policy Framework (RPF) was prepared". OP 4.10 is Indigenous Peoples; the resettlement policy is
OP 4.12. The card cites no OP number, so nothing had to change.

---

## 7. `addo-park-farm-worker-rehousing` (P064438, South Africa) - KEPT, corrected

**`displaced: 21` removed.** 21 is 11 plus 10 and appears in no document. The handoff's ruling on
`hunan-gansu-small-towns-demolition` is explicit - "this map does not compute a figure no document prints" -
and the figures the report does print (29, 11, 10, 8) are now in `displaced_label` and `displaced_note` with
the report named, and the field is left off.

**A manufactured conflict removed.** The draft said in two places that the report and the Evaluation Group's
review "disagree on the outcome", the review stating "flatly that '29 households were resettled'". The
review's very next sentence gives the same three groups the report gives and says the 8 "are scheduled to
move to housing projects but are waiting for relocation". The two documents record the same outcome in
different words. Rewritten in `displaced_note` and `confidence_note`.

**Selective quotation, twice, and both cut the same way.**

1. The card ended the report's passage at the 8 households not moved and the person off the housing list. The
   same paragraph says the Bank's social safeguards specialist "visited the new houses and was satisfied with
   these arrangements as all the affected households were in better housing conditions than before the move".
   Added to `community` and `outcome`.
2. The card quoted the plan's "Once displaced from the farn, such benefits would fall away" and stopped at
   the typo. The next sentence is the plan's undertaking that South African National Parks "will ensure that
   incomes are replaced via the income restoration strategy outlined in this document". Added.

**`confidence` changed from `documented` to `contested`.** The core harm - 29 households, 11 and 10 moved,
8 not, one person off the list - rests on the Bank's completion report alone, with the Evaluation Group's
review of that report repeating it. Teresa Connor's field study corroborates the **mechanism**, that a
willing-seller purchase required a farm to be cleared of all previous inhabitants, but gives no count and
does not report on these households. Under CHECK20 that is a single source for the core harm.

**A citation that did not resolve to its claim.** The Connor quotation was cited to
`ideas.repec.org/a/taf/deveza/v22y2005i3p365-382.html`. That page was fetched and read: it carries the
title, authorship, abstract and DOI and **not the quoted sentence** - "willing seller" does not appear on it
at all. The sentence was found and verified in the full text at
`informahealthcare.com/doi/full/10.1080/03768350500253179`, and the source URL and title were changed to
that. The fact was right; the citation was not usable as given.

**Confirmed:** ICR00001883, cover date 27 April 2011 with the data sheet's own "ICR Date: 04/28/2011" (both
now printed); grant TF-53110, US$5.5 million original, US$5.3 million revised and disbursed; approval
24 February 2004, effectiveness 28 June 2004 against an original 30 April 2004, mid-term review 21 May 2007
against a planned 30 April 2007, closing 30 April 2010 to 30 October 2010; "Environmental Category: B" and
"Global Focal Area: B"; outcome Satisfactory, risk to global environment outcome Low or Negligible, Bank
performance Satisfactory, borrower performance Highly Satisfactory; ICRR13655 `Date Posted : 11/07/2013`,
outcome Moderately Satisfactory, risk Moderate. From the plan: 165 workers and 544 dependants over 13 farms
in phase 1, 35 workers and 34 dependants and 69 inhabitants on the 6 priority farms, 3.3 people and 1.7
workers a household, the 84 per cent, 73 per cent, 24 per cent and 13 per cent profile, the in-kind income
list, the vulnerability paragraph quoted whole, and the median - which is a **median household cash income**
of R588 with an average of R698, not simply "median income". From the report: 236,000 ha cut to 205,000 and
46,000 cut to 30,000 at mid-term, 170,115 ha and 17,608 ha achieved, land prices from R1,080-R1,315 a hectare
in 2003-2004 to R7,000-R8,817 in 2010, and the Enon Bersheba agreement blocked because title had not been
transferred to the community.

---

## The two weakest keeps

1. **`laulara-solerema-road-structures` (Timor-Leste).** Everything it counts is in a plan, and that plan
   contradicts itself on the central figure - 26 affected persons with 146 households in its summary, 12 with
   84 in its body. The completion report counts nobody relocated, records no demolition, rates social
   safeguards compliance overall Satisfactory and says compensation was paid to all affected people. What is
   left is the plan's inventory of structures, the report's statement that the plan was carried out and paid
   in full, delays on every lot, work stoppages, and two worker deaths with no cause given for either. If the
   lead wants a line drawn, this is the card on the line: it survives on BRIEF22's rule that a documented
   list of housing to be demolished plus a report confirming the plan was executed in full is a loss of
   homes, and it would fall if that rule is read to require the demolition itself to be recorded in an
   outcome document.
2. **`maluku-sez-maes-inkiene-demolition` (DR Congo).** No count of anyone relocated exists anywhere. The
   card now rests on a single identifiable harm - a 14-hectare plot built on while its owner was
   uncompensated, with the Bank's partial suspension and the condition for lifting it as corroboration -
   plus the report's own ground for the suspension, "compensation of owners being displaced". The 58
   households are a plan, and its 545 people are an extrapolation. Keep or cut turns on whether one
   uncompensated landowner, unnamed, carries a card about two villages.

## Anything the lead must decide

1. **Taunsa: extend or leave alone.** The new material is real and is listed in `_extend_recommendation`.
   An extend would also need to decide what to do with the existing case's `displaced: 900` and its dating of
   the Descon protest to August 2007.
2. **`displaced: 675` on the Nigeria card** holds relocated businesses, not dwellings. A precedent.
3. **The batch's own counts do not match the handoff.** `_r22_dropped_and_mapped_rows` holds **9** rows:
   7 dropped (Ghana, Indonesia, Peru, Philippines, Betim, Madagascar, India) and **2** already on the map
   (Brasilia, Nepal). The handoff says 8 drops and 1 already on the map. 7 cases plus 9 rows is 16, so no row
   is missing; the split is recorded differently. The drop reasons were read and each quotes a document;
   they were not re-checked against the documents, which was not this job.
4. **The task brief described this batch as Pakistan, Georgia, Indonesia, Sierra Leone, Timor-Leste, Nigeria
   and Ghana.** It is Pakistan, Georgia, **the Democratic Republic of the Congo** (Maluku commune, Kinshasa,
   not the Indonesian province), Sierra Leone, Timor-Leste, Nigeria and **South Africa**. Indonesia and Ghana
   are among the dropped rows.

## Anything I could not check

- **The JACSES factsheet of 28 November 2006.** Japanese, Adobe-Japan1 CID font with no usable mapping.
  `pdftotext -layout` returns 239 bytes; `pdftoppm -r 130 -png` renders the page with every Japanese glyph
  dropped, leaving only the Latin letterhead. Both routes tried; nothing readable by either.
- **The independent resettlement audit behind the Addo card**, by South African National Parks in 2010. The
  completion report lists it among unpublished supporting documents. Not searched for outside the Bank.
- **The Bank's project record for Sierra Leone**, which the draft says gives approval as 31 January 2013
  against the report's 23 January. Not checked; the card attributes each date to its source.
- **The drop reasons in `_r22_dropped_and_mapped_rows`.** Read, not re-verified.

## Figures where two documents, or one document, disagree

| Quantity | One figure | The other |
| --- | --- | --- |
| Households displaced, Timor Lot 2 | 26 affected persons / 146 households (plan, summary, twice) | 12 affected persons / 84 households (same plan, later section) |
| Household members, Timor Lot 2 | 1,454 (plan, summary) | 1,545 (same plan, socio-economic chapter) |
| Owners of the 164 structures, Timor | 123 affected persons / 771 members (plan, summary) | 122 affected persons / 871 members (same plan) |
| Households at Inkiene, Maluku | 22 (plan text, twice) | 21 (same plan's numbered list) |
| Maluku zone area | 233 ha (resettlement plan) | 244 ha (completion report, annex 8) |
| Sierra Leone level one restructuring | 29 October 2015 (data sheet) | 28 October 2015 (section H table) |
| Sierra Leone level one restructuring, year | October 2015 (most of the report) | October 2013 (monitoring section, paragraph 65) |
| Addo completion report date | 27 April 2011 (cover) | 28 April 2011 (data sheet, "ICR Date") |
| Sierra Leone approval | 23 January 2013 (data sheet) | 31 January 2013 (Bank project record, per the draft; unverified) |
| Nigeria, people who moved a business | 675 project-wide (completion report) | 686 across three of five road plans (pre-works estimates) |

## Faults that appear in more than one card

- **Selective quotation, in five of the seven cards**, and running the same way every time: the damaging
  clause quoted, the favourable clause in the same paragraph dropped. Georgia ("No complaints related to
  land acquisition and resettlement were reported"); Sierra Leone ("the chances that resistance to relocate
  might arise is minimal if not none", and "implemented satisfactorily with only two outstanding"); DR Congo
  (the family X complaint closed after negotiations, and the overall moderately satisfactory rating);
  Timor-Leste (social safeguards rated overall Satisfactory, compensation paid to all); South Africa (the
  Bank specialist's finding that all were better housed, and the plan's undertaking to replace incomes). The
  two cards where it does not appear are Nigeria, which quoted its central passage whole, and Pakistan, whose
  source documents are candid enough that there was little to drop.
- **Arithmetic the documents do not print, presented as a document's figure**: `displaced: 21` at Addo,
  "11 toilets" in Timor-Leste, "leaving 12 of the 49" in DR Congo, "686" in Nigeria. Four cards.
- **A conflict asserted where there is none**: Addo (report against review), Nigeria (686 against 675). Two
  cards, both now rewritten.
- **An absence claim that a document refutes**: Georgia's "the completion report carries no printed date".
  One card, and the cover page carries it.

## Routes that failed, named as routes

- `curl` to `https://www.dawn.com/news/191411`, `.../205738` and `.../1994681` - **HTTP 403 on all three,
  from the plain `curl` route with no browser headers.** The same three articles were then read without
  difficulty through WebSearch followed by WebFetch, which is the route BRIEF22 describes. dawn.com is not
  blocked; plain `curl` against it is.
- `pdftotext -layout` on `JACSES_factsheet_20061128.pdf` - returns 239 bytes with "Missing language pack for
  'Adobe-Japan1' mapping". `pdftoppm -r 130 -png` on the same file - renders, but with all Japanese glyphs
  dropped. Two routes, one file, neither usable; the host served the file at HTTP 200 both times.
- `https://ideas.repec.org/a/taf/deveza/v22y2005i3p365-382.html` - resolves at HTTP 200 and is a real page
  for the article, but is an abstract page and does not carry the sentence cited to it. Not a route failure;
  a citation failure, recorded here so it is not mistaken for one.
- No route to `documents1.worldbank.org` failed. 37 of 37 documents downloaded at HTTP 200 by rewriting
  `documents.worldbank.org` to `documents1.worldbank.org`, as the handoff describes. The
  `wds?projectid=P124720` query returned all 60 documents for that project, including the three
  implementation status reports that settled the DR Congo card. No permission prompt was raised and no fetch
  gate closed during this run.
