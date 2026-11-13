# Round 17, batch R: check log

Input: `/home/claude/r17/out_R.json` (10 cases, leads 1, 2, 10, 12, 17, 18, 20, 21, 23, 33).
Output: `/home/claude/r17/checked_R.json` — 10 cases kept, 0 extends, 0 drops. All 10 corrected.

## How the figures were verified

Every PDF cited on every card was downloaded again with `curl` from `documents1.worldbank.org`
into a fresh directory (`/home/claude/r17/vfy/`), converted with `pdftotext -layout`, and read
from disk. 23 documents in all, plus one adjacent document (see lead 1). No figure was taken
from the on-disk copies left by earlier passes, and no large PDF was read through a fetch tool.
Document lists came from `https://search.worldbank.org/api/v3/wds?format=json&projectid=<P>`.
ICIJ's two method pages and all ten ICIJ project pages were fetched and read.

Every figure on every card was checked against the document. Everything not listed below as a
correction was confirmed as printed.

## The rule applied to `displaced`

`displaced` holds **the Bank document's own count of people physically relocated by the
project** — persons where the document counts persons, households where the document counts only
households. `displaced_label` names the unit and the source in its first words; `displaced_note`
carries the plan figure, the wider "affected" figure and ICIJ's estimate.

Three consequences, applied to all ten:

1. **No conversion in either direction.** Where a document gives households and no persons
   (leads 12, 17, 20), the card says so in the label and no person figure is produced. An
   earlier draft in this round multiplied households by an average household size to account
   for ICIJ's figure and was refuted from the project's own resettlement plans; deriving a
   person count the same way would be the same fault.
2. **A wider category is not a relocation count.** `displaced` may not hold
   "project-affected people", "families losing more than 10 per cent of their land", or
   "households affected". Those are kept in the label and the note with the category named.
3. **Where no Bank document counts anyone relocated, the field is omitted** rather than filled
   with the nearest available number. That applies to two cards, leads 1 and 23.

This matches the convention already used in `checked_D.json`, which holds persons for one
railway case and households for two others, with the unit named in the label.

Resulting values: lead 2 — 2,998 persons; lead 10 — 4,884 people; lead 18 — 6,080 people;
lead 20 — 2,463 households; lead 21 — 223 people; lead 33 — 559 persons; lead 12 — 65
households; lead 17 — 5 households; leads 1 and 23 — field removed.

## Checks run across the whole batch

- **The refuted explanation.** No card states or implies that ICIJ's figure is households times
  an average household size. The method paragraph on each card is attributed to ICIJ's own
  method page throughout and was verified word for word against it: ICIJ looked for what the
  Bank's documents call "Project-Affected People (PAP)" or "displaced people", searched for
  "affected", "PAP" or "displaced", says that where a document counted only households "it is
  necessary to look for the average number of family members by household", "decided to include
  all impacts" because the temporary/permanent distinction is not made in all documents, and
  counts impacts "as modest as losing less than 1 percent of their land or income". The footnote
  claim (more than 20,000 people affected but most expected to have only minor impacts) was
  verified on ICIJ's about page, and the footnote itself was verified present on the ICIJ pages
  for leads 1, 12 and 17 and absent on the other seven. Each card now ends the comparison with
  the statement that the documents do not explain the gap, and stops there.
- **Verbs.** Every figure was checked against the verb in its sentence. No "affected by" is
  rendered as "displaced" or "relocated" anywhere in the batch. Leads 1 and 23 were the two
  cards that failed this test and both were changed (below).
- **Rating attribution.** Every rating was read off the completion report's own rating summary
  and off the Evaluation Group's own ratings table, separately, and each is now printed with the
  body that gave it. Four cards printed a rating label the source does not print; one card's
  ratings record held a genuine disagreement between two Bank documents that was not shown.
- **No implied failure.** Where more households moved or more land was taken than the appraisal
  estimated (leads 20 and 33), the card now says the figures and that no document records anyone
  harmed by the difference, without the word overrun doing any work. Where compensation is
  recorded as paid at or above plan rates (leads 21, 33, 20), the card says so.
- **Duplicates.** All ten ids are new against `cases.json` (957 records) and against
  `checked_D.json`, `checked_E.json` and `checked_F.json`. The ten lead numbers are exactly the
  ten dropped in those three files. Coordinates were compared with every existing case of the
  same iso3 within 60 km: three near-matches, all different projects — lead 1 and lead 17 sit
  near `cat-linh-ha-dong-accidents` (Hanoi metro) because Hanoi and Vinh Yen are the provincial
  anchors for country-wide line projects, and lead 12 sits 24 km from
  `da-nang-quang-ngai-expressway`. No episode overlap.
- **First person and process narration.** None found on the drafts; none introduced. Seven
  framing or opinion sentences were removed (listed per card below). The phrase "Searches
  found..." in five `confidence_note` fields was rewritten as a fact about the record, matching
  the wording used in the three sibling files.
- **Coordinates.** All ten carry `ap: true` and a `point` that says what the coordinates are.
  One `point` claimed the coordinates sat on a dam they do not sit on and was corrected.

## Per card

### Lead 2 — `shaanxi-ankang-road-resettlement`
Opened: ICR2142 (13 June 2013, 451 KB of text) and the Evaluation Group's ICR Review (22
September 2014), both in full.
Confirmed: 5,713 mu permanent including 3,040 mu farmland, 2,459 mu temporary, 698 households
with 2,998 persons relocated, 11 enterprises, RMB 262 million; the Evaluation Group's metric
restatement (3.8 million m² permanent, 1.63 million m² temporary); about 120 meetings; the
external monitor's conclusion on income and housing; 87 km expressway, Maoba close to the
Sichuan border; loan IBRD-48530, US$300 million, approved 13 March 2007, effective 10 August
2007, closing 30 June 2012 to 31 December 2012, fully disbursed, Category A; both rating sets
and all three of the Evaluation Group's reasons for disagreement.
Corrected:
- Added the report's own wider count, which the card omitted and which is the figure ICIJ's
  category corresponds to: 7,266 households with 29,096 persons affected in total, against
  7,361 households and 30,257 persons in the resettlement plan; and 698 households relocated
  against 496 in the plan. The ICIJ comparison in the note now runs against both the 2,998 and
  the 29,096.
- Added the Evaluation Group's reason for raising the risk rating (regional economic
  development, possible toll level adjustments, limits on budget and capacity).
- Added to `killed_note`, uncounted and attributed: the Evaluation Group records 126 accidents
  on the finished expressway in 2012 against a target of 35 a year, and 2 fatal accidents
  against a target of 13. These are traffic accidents on the completed road reported as a
  safety indicator, not deaths caused by the project, so `killed` stays 0.
- `point` rewritten: the local roads component covered county and village roads in the rural
  areas around the corridor; the three roads the card named (Dongda in Ziyang County, Gaoping
  in Hanbin District, Shiguan in Langao County) are the three the report names as delayed.
- The completion report's own cover sheet dates it 17 June 2013 and the Bank's catalogue dates
  it 13 June 2013. The card prints the catalogue date, as the other nine do.

### Lead 10 — `huai-river-flood-drainage-resettlement`
Opened: ICR00004036 (20 June 2017) and the Evaluation Group's review (7 September 2017), both in
full.
Confirmed: 7,044 to 4,884; the indicator reading "Resettled people whose incomes and lives
maintained or improved", target 7,044, achievement 4,884; the separate benefit indicator 57,173
to 81,311; 10 cultural sites in Jiangsu; 11 natural habitats of which seven near or
hydrologically linked to project sites; basin 270,000 km² in four provinces; loan IBRD-79380,
US$200 million, approved 6 July 2010, effective 26 January 2011, restructured 15 June 2016,
closed 31 December 2016, fully disbursed.
Corrected:
- Implementing agency is **Huai River Basin Commission**, with Anhui, Henan, Jiangsu and
  Shandong listed beside it. The card had "Huai River Water Resources Commission", which is not
  the name in the document.
- `displaced_label` now reads "people resettled", which is what the indicator counts, instead of
  "people for whom resettlement was required".
- Rating attribution: the completion report rates risk to the development outcome **Moderate**;
  the Evaluation Group's table prints that rating, for both columns, as **Modest**. The card
  said the Evaluation Group "agrees on every one of those ratings". It now prints each label
  with the document that prints it.
- Added the report's example of how the number fell (redesigning the shape of river channels
  reduced land acquisition and houses to be demolished).
- Framing sentence removed from `community`.

### Lead 18 — `liaoning-medium-cities-resettlement`
Opened: ICR2930 (29 April 2014) and the Evaluation Group's ICR Review ICRR14508 (5 December
2014), both in full. This is the card the owner flagged as the round's cleanest finding, so
every element was read in its own sentence.
Confirmed, verbatim from paragraph 26 of the completion report: "The original resettlement plan
involved 4,994 households, 677 enterprises and shops, and 31,547 people. Actual resettlement was
scaled down because of cancellations and adjustments of the project components. The final
resettlement involved 2467 households, 119 enterprises and shops, and 6080 people." Also
confirmed: the six places (Panjin, Jinzhou, Fushun, Benxi and Liaoyang municipalities and the
county town of Dengta in Liaoyang municipality); most resettlement completed before loan closing;
first external monitoring report March 2007; post-evaluations in 2010 and 2011; resettlement
consistently rated satisfactory; road component US$330.93 million including US$105.1 million of
resettlement costs; the 2007 audit, the Panjin RMB 19.89 million, the Fushun RMB 7.7 million, the
21 and 13 per cent shares, the Unsatisfactory financial management rating in the April 2009
report; loan IBRD-48310, US$218 million, approved 27 June 2006, signed 18 October 2006, effective
5 January 2007, restructured 18 September 2011, closing 31 December 2011 to 31 October 2013,
US$212.82 million disbursed. ICIJ's figure for the project is 31,547, which is the plan figure to
the person.
Corrected:
- Implementing agency is **Liaoning Urban Construction and Renewal Project Office (LUCRPO)**.
  The card had "Liaoning Urban Construction Project Office (LUCPRO)"; LUCPRO appears once in the
  report as a typographical variant and the abbreviation list gives LUCRPO.
- Rating attribution: the Evaluation Group's table prints the risk rating, in both columns, as
  Negligible to Low, where the completion report's summary says Low. Both are now printed with
  their source.
- The slow-implementation sentence was incomplete: the report gives substantial revisions in
  project scope and procurement plans first, then counterpart fund shortages, slow resettlement
  and policy changes. All four are now listed.
- Added that independent investigations confirmed the bulk of the audited work conformed to
  specifications, so the audit paragraph is not left implying unremedied loss, and the card
  keeps its existing sentence that the finding concerned loan funds, not the resettlement.
- Removed from `displaced_note`: "This is the clearest case in this group of the distance
  between a resettlement plan and what the lender recorded as done." It is an opinion and a
  cross-batch comparison. The figures now stand on their own.

### Lead 20 — `nanguang-railway-resettlement`
Opened: ICR3432 (3 December 2015), the Evaluation Group's ICR Review (9 June 2016) and the
Evaluation Group's Project Performance Assessment Report No. 127580 (26 June 2018), all three in
full.
Confirmed from paragraph 30 of the completion report: land acquisition of 16 km² against an
appraisal estimate of 17 km²; "A total of 2,463 households were relocated compared to the 2,029
households estimated at appraisal"; total compensation equivalent to the appraisal estimate.
Confirmed from paragraphs 3.5 and 3.6 of the 2018 assessment: the mission interview with the
project's resettlement specialist; the right of way affecting farmers to a varying extent; the
overall impact in a typical village small; compensation as a combination of cash and
re-allocation of land among farmers in a village; "Affected households were relocated within
their villages with compensation. Each affected household signed a formal agreement with the
local government for its relocation."; the external monitoring team recruited by the Ministry of
Railways' Foreign Capital and Technical Import Center from a list the Bank recommended;
supervision once or twice a year; the conclusion on implementation capacity. Also confirmed: the
line about 400 km from Litang West to New Zhaoqing; NGRC incorporated July 2009; loan IBRD-77220,
US$300 million, approved 24 June 2009, effective 21 December 2009, restructured 25 August 2011 and
14 October 2014, closing 31 December 2014 to 30 June 2015, US$297.54 million disbursed, Category
A; all three rating sets identical.
Corrected:
- Company role: the card said the railway company "carried out the land acquisition and
  relocation". No document says that. The completion report names China Railway Corporation as
  implementing agency, and the 2018 assessment records each affected household signing an
  agreement with the **local government**. The company entry now stops at building and running
  the line, China Railway Corporation is listed as the implementing agency the report names, and
  the local governments' role is in `community` where the document puts it.
- Rating attribution: the completion report's summary says risk to the development outcome is
  **Low or Negligible**; the 2018 assessment's table prints it, for all three documents, as
  **Negligible**. Both are now printed.
- Removed "This is the most closely examined of the Bank's Chinese railway resettlements."
- The overrun sentence was reworded so it carries no implication of harm: the two figures, then
  the statement that none of the three documents records anyone harmed by the difference.
- `displaced_label` now says that no Bank document gives a number of people.
Duplicate check against the two near-identical cases in `checked_D.json`: different project
(P112359 against P099062 and P122321), different loan (IBRD-77220 against IBRD-75570 and
IBRD-80520), different line and provinces (Litang West–New Zhaoqing in Guangxi and Guangdong,
against Shijiazhuang–Zhengzhou in Hebei and Henan, and Jilin–Tumen–Hunchun in Jilin), different
figures (2,463 households against 4,752 and 5,508) and coordinates 1,400 km and 2,200 km apart.
A reader meets three different lines, three different loan numbers and three different household
counts. No duplication.

### Lead 21 — `cuijiaying-han-river-resettlement` (renamed from "China: Fifth Inland Waterways")
Opened: ICR1913 (19 December 2011) and the Evaluation Group's ICR Review (14 January 2013), both
in full.
Place verified from the document, not inferred: the completion report's component A is
"Construction of the Cuijiaying Navigation Complex on the Han River downstream from the city of
Xiangfan, including construction of a dam of about 18 meter high, a shiplock", the implementing
department is the Hubei Provincial Transport Department, and the special purpose unit it created
is the Cuijiaying Complex Management Office. The resettlement figures sit in the same paragraph
as the complex, so the project-to-place link is the document's.
Confirmed: resettlement plan completed September 2009 "without rancor or dispute"; 37,541 mu
(2,503 ha); 57 households with 223 people relocated; 23 business enterprises compensated; all 57
moved within the same village into new cement-brick houses; dam-site farmers who lost the most
land compensated above the plan; 34 vulnerable people on RMB 100–300 a month; 24 family
businesses employing 55 farmers moved to National Road 207; reservoir-area villages losing less
than five per cent of their land; 77.5 per cent of interviewed households; loan IBRD-48040,
US$100 million, approved 11 October 2005, effective 13 December 2005, closed 30 June 2011, fully
disbursed. Both rating sets and the Evaluation Group's two reasons for disagreement confirmed,
including its note that the 3,000-to-5,000-yuan income claim comes from the borrower's completion
report with no counterfactual and no indication of inflation adjustment.
Corrected:
- `point` said the coordinates sit on the Cuijiaying complex downstream of Xiangyang. They sit on
  Xiangyang itself, about where the second company's headquarters is placed. Rewritten to say
  they sit on the city, that the report places the complex downstream of it, and that the Bank's
  documents give no coordinates for the dam. No coordinates were invented.
- Removed "This is a small resettlement and the documents record it as a small one."
- `community` tightened to the document's own words on the few affected in the reservoir area
  being fully compensated.

### Lead 33 — `naji-youjiang-waterways-resettlement` (renamed from "Fourth Inland Waterways")
Opened: ICR1376 (28 December 2011) and the Evaluation Group's ICR Review (14 January 2013), both
in full.
Place verified from the document: component A is "Construction of the Naji Navigation Complex on
the Youjiang River between the cities of Baise and Nanning, including: construction of a 20 meter
high dam", and the completion report's poverty section says "In Tianyang County, which was
directly impacted by the Naji development". Tianyang in Baise prefecture is therefore the
document's own location for the complex, not the writer's inference, and the coordinates sit on
the You River in Tianyang. The Guangdong half of the loan (Xiniu complex on the Lian River) is
named separately in `place` and `point`.
Confirmed: 864 ha, 4.2 per cent above plan; 131 households relocated, 82 more than the plan; the
annex line "49 households, 151 persons for relocation and rehabilitation" against "131 households
and 559 persons were relocated and rehabilitated"; 15,622 m² rebuilt against 16,532 m² planned;
RMB 236.7 million paid against RMB 66.0 million budgeted (the completion report rounds this to
RMB 237 million and the Evaluation Group gives 236.7); income per head up 112 per cent at the dam
site and 32 per cent in the reservoir area; the Guangdong figures 82.4 ha against 56.6 ha and
77.8 ha "an increase of 50%"; Zhangwu and Hetou; 36 per cent at Xiniu and about 45 per cent at
Longma and Lianyao; 31 per cent cost overrun; 23.7 and 28.5 per cent; 7.2 to 22.5 per cent; the
Evaluation Group's sentence "No households were reallocated in the Guangdong portion."; the dam
safety panels; the cultural relics; loan IBRD-47280, US$91 million, approved 25 March 2004,
effective 9 January 2005, closing 31 January 2010 to 30 June 2011, US$90.55 million disbursed.
Corrected:
- The card attributed the 77.8 ha figure to the completion report's list of changes in scope and
  the 82.4 ha figure to the Evaluation Group. Both figures are in the completion report (82.4 in
  the safeguards section, 77.8 in the changes-in-scope list) and the Evaluation Group reproduces
  both. The card now says so, and still does not reconcile them.
- The Evaluation Group's sentence on Guangdong is now quoted rather than paraphrased, because its
  verb is "reallocated".
- **Ratings record.** The completion report's own summary rates Bank performance and borrower
  performance Moderately Satisfactory; the Evaluation Group's table enters the completion
  report's ratings for both as Satisfactory and its own as Moderately Satisfactory, that is, it
  records a disagreement the completion report's summary does not support. Both are now printed
  with who says what, and the end point — both documents' own final ratings are Moderately
  Satisfactory — is stated without reconciling the tables.
- Added that the Guangdong Provincial Waterway Bureau dropped the Qingyuan terminal and
  maintenance station from the project because of difficulties in acquiring land.
- The overrun sentence reworded as a difference from the estimates, with no implication of harm.

### Lead 1 — `vietnam-rural-energy-2-land-loss`
Opened: the appraisal document (Report 29860-VN, 21 October 2004, 403 KB of text), the updated
Integrated Safeguards Data Sheet (Report 30303, 24 May 2004), the completion report (ICR00003194,
13 December 2014) and the Evaluation Group's review (ICRR14722, 12 May 2015), all four in full.
Also opened, to test whether a field-based Evaluation Group assessment covers this project: the
2014 Project Performance Assessment Report tagged to P074688 in the Bank's file. It assesses
three other Vietnamese power projects (IDA-30340, IDA-33580, IDA-36800) and not this credit, so
nothing from it is used.
Confirmed: the seven impact categories, five of them temporary; the table total of 178 families
losing more than 10 per cent of their productive land holding, all in Vinh Phuc, with 299,746 m²
permanent and 14,256,140 m² temporary, under the note that the numbers could differ from the
later detailed measurement survey; all four quoted passages of the safeguards data sheet; the
completion report's four difficulties and its provincial-unit-versus-power-company comparison;
the Bank's file holding 91 items; credits IDA-40000 (SDR 151.1 million) and IDA-45760 (SDR 133.8
million), SDR 284.9 million together, TF-54464, the GEF grant, restructurings 21 May 2009 and 16
December 2013, closing 31 December 2011 to 30 June 2014, Category B; both rating sets identical.
Corrected — this card had the most serious fault in the batch:
- **`displaced` removed.** It held 178, which is families losing more than a tenth of their
  productive land holding in an appraisal estimate: not people, not households relocated, and
  not an outcome. The completion report was read in full and gives no count of land acquired and
  no count of households, only that "a small volume of land acquisition was required" and that
  compliance was Satisfactory. No Bank document for this project counts anyone relocated, so no
  number is given.
- **Title changed.** It read "178 families lose more than a tenth of their land", which presents
  an appraisal estimate as something that happened. It now says land was taken along power lines
  in 25 provinces with no count of anyone moved.
- `community` and `displaced_note` rewritten so that every figure carries the word estimate or
  the document that estimated it, and so that the safeguards data sheet's statement that the
  project "will not involve any major resettlement" sits beside the 131,955 households it says
  would be affected.
- Removed the sentence narrating which documents were and were not read. The note now states as
  a fact about the record that the Bank's file holds 91 items including more than twenty
  provincial resettlement action plans which are not among the documents cited, so the absence
  claim is bounded without describing anyone's reading.
- Added from the safeguards data sheet that people who did have to rebuild houses were to receive
  a subsidy covering livelihood losses during rebuilding.

### Lead 12 — `vietnam-water-resources-assistance-resettlement`
Opened: the Evaluation Group's Project Performance Assessment Report No. 138389 (20 August 2019)
and its earlier ICR Review ICRR14273 (9 December 2013), both in full.
Confirmed verbatim: "In all, 5,974 households were negatively affected; of these 167 households
were classified as 'severely affected' with loses of more than 20 percent of their land.
Sixty-five households required resettlement." Also confirmed: 69 Tay and Nung households at Cau
Son-Cam Son and the ethnic minority development plan; the gender and poverty monitoring gap; the
2019 mission (consultants Richard Pollard and Hoàn Pham, March 2019, three of the six schemes,
interviews with central government, provincial officials, non-governmental organisations and
beneficiaries); the 2013 review's sentence on reducing affected households from 11,000 to about
6,000 and its note that the completion report does not evaluate the adequacy of the compensation
package; the three-year delay in appointing the environmental monitoring consultant; seven
safeguard policies; credit IDA-38800 / C3880, SDR 105.7 million (US$157.8 million equivalent),
TF-54751, approved 30 March 2004, effective 21 December 2004, closing 31 December 2011 to 31
December 2012, completion cost SDR 102.83 million (US$159.44 million equivalent); the PPAR's
principal ratings table, in which the completion report, the ICR Review and the PPAR all give
Moderately satisfactory, Moderate, Moderately satisfactory, Moderately satisfactory.
Corrected:
- `displaced_label` now states that the documents count households and give no number of people.
- `community` and `displaced_note` reordered so that the 11,000-to-6,000 reduction is attributed
  to the 2013 review as a separate record and is not offered as an account of ICIJ's 53,600; the
  card previously said ICIJ's figure "is of the same order as" the initial estimate, which is a
  reconciliation the documents do not make. It is gone.
- Framing sentence removed from `community`.
- `confidence_note` rewritten to the sibling files' wording, keeping the point that the 2019
  assessment carries the most detail while the Evaluation Group is part of the World Bank Group.

### Lead 17 — `vietnam-distribution-efficiency-five-households`
Opened: the completion report (ICR00004664, 14 June 2019) and the Evaluation Group's review (21
January 2020), both in full.
Confirmed verbatim: "The PCs were able to minimize physical relocation (only five households were
relocated out of 12,880 Project Affected Households) by the construction/execution of 169
subprojects"; the "low and/manageable" sentence; VND 287 billion (US$12.4 million); 167 of 169
subprojects, 98.8 per cent, as of 31 May 2019, with one Hanoi Power Corporation and one Southern
Power Corporation subproject outstanding and targeted for 30 June 2019; the hindsight sentence on
advance consultation; the two lessons; credit IDA-51560, SDR 297.7 million (US$448.9 million
equivalent), TF-13456 and TF-13468, approved 11 September 2012, effective 7 February 2013,
restructured 22 June 2016, closed 31 December 2018 on its original closing date; the AusAID grant
reduced from US$8 million to US$6.2 million at effectiveness; ratings Highly Satisfactory, Highly
Satisfactory, High in both documents.
Corrected:
- Attribution: the card credited the Evaluation Group with the statement that delayed approvals
  meant the works portion of five subprojects could not be finished. That sentence is the
  completion report's lesson 101; the Evaluation Group reproduces it. Now attributed to the
  completion report.
- Added the completion report's named instances, which give the card two places instead of none:
  the Phu Xuyen subproject in Ha Noi, where the land for a substation could not be acquired
  within the project's life, and the Giang Dien transmission line in Dong Nai, where land
  acquisition was affected by rapid urbanisation, industrialisation and rising land prices; in
  both, equipment was bought with project funds and the works continued on counterpart
  financing.
- Removed from `displaced_note`: "The gap between five households relocated and 31,581 people is
  the point of this record." Replaced by a flat statement that the two figures count different
  things.
- Framing sentence removed from `community`; `displaced_label` and note now say the report counts
  households.

### Lead 23 — `nhiip-india-corridor-land-acquisition`
Opened: the completion report (29 June 2022, 2,647 lines) and the Evaluation Group's review
(ICRR0023078, 21 February 2023), both in full.
Confirmed verbatim: "The project impacted 775 acres of land, including 558 acres of private land,
6390 structures (including 451 CPRs) and 11,138 PAPs"; "compensation and eligible assistance were
duly paid to all PAPs in six of the 11 road corridors"; the transfer of five roads in Bihar and
West Bengal to the Green National Highway Corridors Project; and the Evaluation Group's
"disbursement of compensation to project-affected people (PAPs) were substantially delayed in
several sections but by project closing, all 11,138 PAPs were compensated for land acquisition
for the subprojects completed under the project". The two statements cover the same set and the
card does not present them as disagreeing. Also confirmed: four Bihar roads mis-sized by
inadequate design; 347 grievances, all but one resolved; 856 km planned and 704 km built in the
low-income states (82 per cent), 215 km and 212 km in the middle-income states (99 per cent),
Bihar 499 km planned and 348 km built; 155 km transferred, 102 km of it done by 31 March 2022;
loan IBRD-83010, US$500 million, approved 29 October 2013, effective 5 August 2014, mid-term
review 12 May 2017, closing 30 June 2019 to 30 September 2020; road component US$1,106.4 million
including US$468.05 million of Bank money, completed at US$704.0 million including US$293.6
million; identical ratings with no disagreement, and the Evaluation Group rating the completion
report itself Modest.
Corrected:
- **`displaced` removed.** It held 11,138, which is project-affected people. The completion
  report was read in full: the words "displaced" and "relocated" do not appear in it at all, and
  "resettlement" appears only in the names of the plans and the policy framework. There is no
  count of anyone relocated in either document, so no number is given. The 11,138 stays in the
  note with its category named and with the statement that neither document separates people who
  lost a house from people who lost only land or a roadside pitch.
- **Title changed** from "11,138 people affected" to the land taken and the people affected, so
  the headline figure is not read as displacement.
- **A false absence claim was removed.** The card said neither Bank document names the eleven
  corridors by highway number, and used that to explain why Bihar land disputes cannot be matched
  to the loan. The completion report does name the completed road sections, repeatedly: Lasot–
  Karanli on NH11B and Pratapgarh–Padi on NH113 in Rajasthan, Anishabad–Aurangabad on NH98 in
  Bihar in two contract lots, Madhugiri–Chikaballapura–Mulgabal on NH234 in Karnataka, Purlia–
  Bankura on NH60A in West Bengal, Bhojpur–Chattabar on NH200 and Nabarangpur–Koksara on NH201
  in Odisha. They are now on the card, and the reason the Bihar disputes cannot be matched is
  stated accurately: the records found name other roads, and the five transferred sections are
  not named in either document.
- Added the completion report's own record of how the land acquisition went: most of it for the
  15 packages completed on schedule, but short and challenging sections on all corridors causing
  delays, and the entire land not handed over in practice despite each state public works
  department guaranteeing availability. Added that it rates social safeguards performance
  Moderately Satisfactory, and that variable work by non-governmental organisation consultants
  with weak contract management by the ministry led to serious implementation delays.
- `lenders` now carries the loan's revision from US$500 million to US$307.74 million, which is
  what was disbursed.
- Independence tested rather than assumed, as instructed: a search for independent records of
  land acquisition on this project returned Land Conflict Watch entries and Indian press reports
  on highway land disputes in Bihar, including NH77 and the Patna–Buxar road, a Patna High Court
  listing, and parliamentary questions. None names a section financed by this loan. `contested`
  therefore stands, and the `confidence_note` says what exists and why it cannot be attached.

## Bucket after checking

All ten are **bucket (b)**: a resettlement or land acquisition the Bank's own documents record as
carried out and compliant, with no documented failure. Nothing in the batch moves to (a).

The nearest things to a documented failure, none of which supports an (a) label on its own:
- Lead 23: compensation "substantially delayed in several sections", with no length, date, place
  or number of people in either document; plus the land acquisition mis-sized on four Bihar roads
  and social safeguards performance rated Moderately Satisfactory.
- Lead 18: the 2007 audit findings in Panjin and Fushun, which concern the use of loan funds and
  not the resettlement.
- Lead 1: four named difficulties in land acquisition, including long negotiations with affected
  households over compensation and lack of cooperation from local authorities, none quantified.
- Lead 17: land acquisition unfinished at two named subprojects at closing, with works carried on
  under counterpart financing.

## Confidence

All ten are `contested`. For the nine China and Vietnam cases the Bank's own documents are the
only source and each `confidence_note` says so in those words, including that the completion
report is written by Bank staff with a borrower section and that the Evaluation Group is the
Bank's own evaluator. For lead 23 the independent record was tested, not assumed, and the result
is on the card.

## Thinnest entries

**Lead 1** is the one I judge too thin to carry a card even under the decision to include
compliant resettlements. The owner's test for these ten is that a loan moved a documented number
of people. Here no Bank document counts anyone moved; the safeguards data sheet says the project
"will not involve any major resettlement" and that impacts on houses "generally will not require
the relocation of families outside their residential plots"; the only quantified figures are
appraisal estimates carrying the appraisal's own warning that they could change; and the
completion report records land acquisition without a number. What is left is a documented land
acquisition of unstated size and the gap to ICIJ's 773,838. It is kept because the owner
recovered it deliberately and because the card now says all of that plainly, but it is the one
to cut if the map wants only resettlements that are counted.

**Lead 23** is the second thinnest, for the same reason in a milder form: 11,138 project-affected
people and 775 acres are documented, the delay in paying them is documented without any
quantity, and no document says anyone moved house.
