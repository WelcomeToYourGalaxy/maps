# Check log — conds_2 (26 cases), round 33 lender-condition batch

Independent check against CONDR.md, CHECK31.md and CHECK20.md. Every agreement relied on was
opened and its cover read. Documents already on disk were read from `cache/`; five documents the
writer relied on are not in the cache and were fetched once each, after reproducing their URL
through the Bank's documents API.

- 26 ids in, 26 out, same set.
- **1 term cut** (kamuzu-barrage-liwonde-businesses).
- **15 entries corrected**, 5 of them on substance and 10 on figures, names, numbers or notes.
- **10 entries confirmed unchanged**: riohacha, djibouti, canal-neyba, igoeti, nagapattinam,
  jordan, tabanovce, beira-maputo, senegal-river, chobhar.

---

## 1. The cut

### kamuzu-barrage-liwonde-businesses (P117617, Malawi) — `safeguard` cut, now `exhaust`

The whole term rested on one amendment letter of 11 August 2017. Read in full. Its only
substantive covenant is:

> "The Recipient shall furnish to the Association for review, no later than September 1, 2018 or
> the date on which at least 95% of the Financing has been disbursed, whichever occurs earlier,
> operational procedures with respect to the dams constructed or upgraded under the Project..."

Three faults, each sufficient on its own.

1. **Date.** The harm — businesses and fishermen displaced at the barrage — runs 2012–2019, and
   the barrage upgrade was the project's largest investment. A reporting duty falling due on
   1 September 2018 did not govern it.
2. **Subject.** The covenant is dam safety. It says nothing about land, resettlement, compensation
   or displaced people, and it never names the Kamuzu Barrage — the writer's "among them the Kamuzu
   Barrage" is the writer's own addition to "the dams constructed or upgraded under the Project".
3. **Inference about an unpublished provision.** The writer's first sentence asserted that the
   22 August 2012 financing agreement "carried a dated obligation about the dams built or upgraded
   under the project". The letter deletes Section I.E.6 and replaces it; it does not print or
   describe what it deletes. The content of the deleted provision is not in evidence.

`exhaust` is the right answer and is now evidenced. Searches of the documents API for
`Financing Agreement Credit 5125-MW`, `5125-MW`, `H775-MW` and the project by name return exactly
two papers, both dated 11 August 2017: this amendment letter and a supplemental letter on
performance indicators. The 22 August 2012 agreement is unpublished.

---

## 2. Substantive corrections

### honduras-road-rehabilitation-ii-land-taken (P109058) — term from the wrong roads

The writer's lead `safeguard` quote was the bar in the 2010 additional credit:

> "The Recipient shall not carry out any works under Parts A.7, A.8 and A.9 of the Project until
> the Association has received the updated: (i) IPP; (ii) ESMF; and (iii) Resettlement Plan, all
> of which shall be satisfactory to the Association." (Credit 4583-HN, Schedule 2, Section I.E.2)

Reading Schedule 1 of the same agreement settles what A.7–A.9 are:

> "7. Reconstruction of sections of the following primary roads damaged as a result of Tropical
> Depression No. 16: (a) Tegucigalpa-Danli; (b) La Entrada-Copan Ruinas; (c) La Entrada-Santa
> Rosa-Ocotepeque; and (d) Santa Rita-Yoro. 8. Reconstruction or replacement of bridges... 9.
> Rehabilitation of sections of secondary roads damaged as a result of Tropical Depression No. 16."

The harm is elsewhere. The completion report of 25 November 2015 gives the 201 cases by corridor:
"San Lorenzo – Olanchito 8 cases; El Porvenir – Marale 25 cases (plus 59 cases related to the
acquisition of land for the construction of the El Porvenir by-pass); La Esperanza - Camasca 109
cases". Those are Parts A.4, A.5 and A.3, all present in the 2008 agreement and untouched by the
A.7–A.9 bar. Part A.9 was dropped altogether in the September 2011 restructuring and A.7 was
modified.

So the bar is a term of a different phase applied to roads it did not cover — CONDR failure 8.

What does hold, read out of Credit 4466-HN of 13 October 2008, which financed those corridors:
its Schedule 2 Section I.B.1(a)(iv) requires the Operational Manual, acceptable to the
Association and amendable only with its prior written approval, to set forth "the ESMF, the IPP,
the GAP, the GAP Priority Measures and the Resettlement Plan for the Project", the Resettlement
Plan being "the Recipient's plan dated April 2008... which consists, inter alia, of the actions to
be undertaken by the Recipient in connection with resettlement activities under Part A of the
Project" (Appendix, definition 23). Its own Safeguards section (I.D) covers only critical natural
habitats, natural forests and protected areas. There is no covenant in the 2008 agreement
requiring the resettlement plan to be *carried out*: the phrase "in accordance with the
Operational Manual" appears nowhere in it, and the only party bound to the manual is the Road
Fund, for Parts B, C.2 and D.2 — the maintenance components, not the road works.

Entry rewritten to say that, with the A.7–A.9 point kept and correctly scoped. `ct` unchanged at
`safeguard`, `admin`; the `safeguard` anchor moved to the natural-habitats covenant, which the
2008 agreement does impose.

### manta-properties-taken-without-agreement (P143996) — wrong borrower

Cover, and Article VI:

> "LOAN NUMBER 8289-EC Loan Agreement (Manta Public Services Improvement Project) between
> INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT and THE MUNICIPALITY OF MANTA"
> "6.01. The Borrower's Representative is its Alcalde del Gobierno Autónomo Descentralizado
> Municipal del Cantón Manta."

Every obligation in Schedule 2 runs to "the Borrower". The writer had them running to Ecuador
three times. Ecuador is the guarantor under a separate guarantee agreement of the same date.
Corrected throughout.

### dennery-embankment-land-used-without-compensation (P111708) — a draft cited as an agreement

One of the three cited instruments is not an agreement. The document the Bank's archive titles
"Credit Agreement C3936-LC - Conformed" opens:

> "845-SLU.doc\JCA Legal Department CONFIDENTIAL DRAFT (Subject to Change) Juan Carlos Alvarez
> May 3, 2004 ... CREDIT NUMBER ___________-SLU Development Credit Agreement ... Dated
> ____________, ____ ... AGREEMENT, dated __________, _____"

Unsigned, undated, credit number blank. The writer's sentence "The credit agreement for Credit
3936-LC incorporates that article and applies it to the credit (Article III, Section 3.01)" is cut
and the document removed from `sources_add`. The catalogue title is wrong about its own file; this
is worth a line in the next brief.

The `safeguard` term itself holds on the executed instruments and both were read in full:
Loan Agreement Section 3.08 and Credit 4498-LC Schedule 2 Section I.C, verbatim as quoted.

The absence claim is confirmed and tightened: in the loan agreement of 29 July 2004 and the
financing agreement of 6 November 2008, the strings `esettl`, `and acquisition`, `ompensat`,
`xpropriat` and `isplaced` each occur **zero** times. Read whole, not grepped alone.

### kumasi-lands-office-farmers-displaced (P120636, Ghana) — the date cannot be settled

Verified, against the grant agreement itself:
- CIDA Trust Fund TF014256 is on this case: the lender role lists "Trust Fund TF-14256,
  US$2,879,706, of which US$2,500,919 was disbursed" among the project's money.
- The Kumasi plan is in the grant's own definition: "'Abbreviated Resettlement Action Plan' or
  'ARAP' means the plan dated November 27, 2010 and published on January 6, 2011, that includes
  the set of mitigation, enhancement, monitoring, and institutional measures to be taken during
  implementation of **Part D.2** of the Project..." and Part D.2 is "Construction of a regional
  office for the land sector agencies in Kumasi". "Safeguard Instruments" means the ESIA and ARAP.
- The quoted clause is at Annex, Section 2.03.D.2, exactly as cited, and Section 2.02 requires the
  project to be carried out in accordance with the Safeguard Instruments.
- One framing correction, in the log rather than the card: the instrument is an agreement between
  Ghana and IBRD/IDA administering Canadian funds, not a third-party co-financier's own agreement
  with Ghana. The writer called it "a co-financier's agreement"; `searched` now says it is one of
  the project's financiers without implying CIDA is the counterparty.

**The date test does not pass and does not fail.** The covenant is dated 30 April 2013. The ARAP it
names is dated 27 November 2010. The project's own IDA financing agreement of 15 June 2011 is
unpublished. Neither completion report gives a date for the six farmers' economic displacement —
the 2020 report says only "Although the Project did not involve physical displacement of
population or communities, it involved economic displacement of six farmers. Therefore, an
Abbreviated Resettlement Action Plan was prepared." A sentence saying the covenant cannot be
placed before or after the loss has been added to the entry.

### tripoli-tyre-heritage-market-relocation (P116197, Lebanon) — loan number, and the date test passes

Corrected: the cover of the project agreement reads "LOAN NUMBER 7166-LE" and both amendment
letters head themselves "Lebanese Republic - Cultural Heritage and Urban Development Project
(LE-7166)". The writer wrote 7166-LB, which is the Bank's catalogue metadata, three times.

The date test passes, and the writer had already handled it correctly. The 9 August 2012
amendment is the instrument carrying the quoted covenant, but the **original project agreement of
24 July 2003** already carried the operative bar, verbatim:

> "4. Part A of the Project — It is hereby agreed that no Sub-Project involving involuntary
> resettlement of local population and/or land acquisition shall be carried out under Part A of
> the Project, unless CDR shall have first furnished to the Bank a Resettlement Action Plan, in
> form and substance satisfactory to the Bank, relating to the carrying out of the Sub-project in
> question."

The amended Schedule 2 paragraphs 3 and 4 and the Section 1.02(p) definition list of RAPs are all
verbatim as quoted. The writer's quotation of the RAP list omits the Salameh building (Saida) RAP
but says "among them", so it is not presented as exhaustive.

---

## 3. Figure, name and note corrections

| case | was | document says |
|---|---|---|
| ahwaz | "a ratio of operating expenses to operating revenues of no more than 0.75" | "a ratio of total operating expenses, **excluding depreciation and financial charges**, to total operating revenues not higher than 0.75" (Ahwaz Project Agreement, Section 4.04(a)) |
| cap-labadie | "escrow account opened at the Bank of the Republic of Haiti for eleven people" | "the Central Bank of Haiti (BRH)"; nineteen project-affected people were owed compensation, "eight cases were compensated as required", eleven remained (ICR ¶83). Both added. |
| sena | "the port company CFM" | "CFM" means Portos e Caminhos de Ferro de Moçambique, E.P. — the state ports **and railways** company |
| lubuk-alung | "six later amendment letters" | five are published: Nos. 1, 2, 4, 5 and 6. No. 3 is not in the archive. |
| dartlo | "forty-four documents the Bank publishes" (in public `ct_note`) | the API returns 43 under P126033. Count removed from the public note and stated in `searched` with the date qualifier. |
| bijilo | "all ninety-three documents" | 92. Corrected. |
| lesotho | Credit 4237-LS, Grant H255-LS | cover reads 4237-LSO and H255-LSO. Noted in `searched`; catalogue uses -LS. |

## 4. Favourable clauses the writer dropped, now restored

CHECK20's first-named fault. Three found, all in the same paragraph as the quoted material.

- **east-tsankhi** — the completion report's covenant passage ends "The documents were disclosed
  and this covenant is considered 'complied with'." Added.
- **lalara** — the withdrawal condition for Category (3) has a fourth limb the writer stopped
  before: money could not be drawn until Gabon "shall have adopted the ESIA, ESMP, RAP and/or the
  IPP, as the case may be, and the same documents have been consulted upon and disclosed as
  approved by the Bank". This cuts *for* the card, which is the point: dropped clauses are dropped
  in both directions. Added.
- **sena** — the completion report: "13,600 staff (all CFM) were retrenched. This was a
  precondition for the Concession." Added, attributed to the report; it is what connects the
  credit's concession-effectiveness condition to the retrenchment, which the writer had left
  implicit.

One addition that strengthens a `required` claim:

- **iraq** — the completion report ¶73: "The project was subject to partial suspension for
  disbursement related to activities under RBD primarily due to delays in fully complying with the
  social safeguards policies. This was specifically related to updating and implementing the RAP
  satisfactory to the World Bank for the vendors along segments R7 and R8 of Expressway No. 1."
  This is a document saying the money depended on the term. Added.

---

## 5. The date test, case by case

Harm dates from `start`/`end` and from the completion report; covenant dates from the agreement's
own cover or the amendment that introduced the clause.

**Covenant postdates the harm — 1 case:** kamuzu (cut, above).

**Covenant date cannot be placed against the harm — 1 case:** kumasi (stated in the entry).

**Covenant predates the harm, confirmed — 24 cases.** Agreement cover dates read in every case:
riohacha 16 Apr 2007 (harm 2007–18); djibouti 2 Oct 2004 (2004–09); canal-neyba 27 May 2008
(2013–16); manta Nov 2013, RAP of 9 Jun 2013 named in it (2013–20); lalara 21 May 2012 (2012–21);
igoeti 20 Dec 2007 (2008–12); cap-labadie — the Labadie road was financed under the first
additional financing, Grant H812-HT of 11 Nov 2012, and the compensation fell due April 2017, so
both the 2012 and the 2016 covenants predate the harm; nagapattinam 12 May 2005 (2005–11); ahwaz
17 Jul 2004 (2004–09); honduras 13 Oct 2008 (2008–15); iraq 2 Mar 2014, works began 2016, the two
deaths "between July 2017 and August 2018"; jordan 11 Feb 2007 (2007–14); lesotho 21 Nov 2006,
ESMF Plan of 8 Dec 2005 (2006–15); tabanovce 18 Sep 2007 (2007–12); east-tsankhi — see below;
beira-maputo 4 May 2012 (2012–21); sena 16 Dec 2004 (2004–11); senegal-river 13 Sep 2006 (2006–13);
chobhar 11 Jul 2013 (2013–21); tripoli — 2003 agreement carries the bar; dennery 29 Jul 2004
(2005–07). The three `exhaust` cases carry no covenant to date.

**east-tsankhi, the case the writer caught, verified in full.** The 2008 financing agreement was
read end to end: its Schedule 2 Section I has three headings only — A Institutional Arrangements,
B Anti-Corruption, C Implementation Documents — and there is no safeguards section anywhere in the
agreement. The strings `esettl`, `and acquisition`, `ompensat`, `xpropriat`, `isplaced` and
`afeguard` each occur **zero** times in the whole text. The writer's citation of Section I.C.3 to
I.C.5 for the model investment contracts and the mining assessment study is exact. The completion
report reproduces the revised covenant and gives "No later than May 31, 2014", amended "to December
15, 2015 by formal notice of the Bank to the Borrower dated October 8, 2014" — both as the writer
has them — and sources it to the "Revised and Restated Financing Agreement, 2014", dated elsewhere
in the report as 18 February 2014. The relocation date is given twice: "The relocation of two
winter shelters had taken place in 2010 in connection with development of this mine" and
"relocations of two winter shelters took place in 2010". The writer's finding stands.

---

## 6. Figures and statements where two documents disagree, left unreconciled

1. **east-tsankhi, whether the 2008 agreement had a safeguards covenant at all.** The completion
   report says "The legal covenant on safeguards **in the original Financing Agreement** was
   modified by adding the portions italicized below." The original financing agreement, read whole,
   has no safeguards covenant and no safeguards section. Both readings are in the file; neither is
   reconciled. The writer's narrower claim — no requirement about land, resettlement or
   compensation before 2014 — holds on either reading, since the resettlement wording is in the
   added portions. The same report adds in a footnote: "Although it was intended that the entire
   covenant would be dropped, the Restated Financing Agreement of February 18, 2014 contains a
   single section of the original covenant (at page 14), namely sub-clause (a). Whether this was
   intentional or not is unclear."
2. **kumasi, whether the Kumasi office was in the original design.** The 2020 completion report:
   "More funds were expended than was envisaged during project preparation because of the addition
   of the new office for land sector agencies in Kumasi". But the ARAP for that office is dated
   27 November 2010, before Board approval on 31 March 2011, and Part D.2 of the 2013 grant
   agreement's project description is the office itself. Nothing in the entry rests on this.
3. **Credit-number suffixes: the catalogue and the cover disagree in four of twenty-six cases.**
   Iran L4738-IR / cover 4738-IRN; Lebanon 7166-LB / cover 7166-LE; St Lucia L7238-LC / cover
   7238-SLU; Lesotho 4237-LS, H255-LS / cover 4237-LSO, H255-LSO. In each case the cover is now
   what the prose gives, with `sources_add` keeping the catalogue title so it matches the URL.

## 7. Card data outside the fields checked

Noticed while reading the documents. Not changed by me; for the main session.

- **honduras.** The completion report says the 201 cases were "resolved with compensation effected
  in full", with "only minor issues... such as administrative delays in the payment of
  compensation to affected parties", and "In 3 cases, households were resettled in all other cases
  compensation was paid in an aggregate total amount of US$0.45 million." A card whose harm is
  land taken in 201 cases has to reckon with "effected in full" in the same sentence.
- **kumasi.** The 2020 completion report: resettlement activities "were implemented with the proper
  disclosure of information and the involvement of stakeholders and **no issues arose**", safeguards
  rated Satisfactory. The 2018 report says the same.
- **sena.** "All individuals and businesses were compensated", and "Compliance with requirements for
  involuntary resettlements and social safeguards implemented by CFM was reported as satisfactory
  or highly satisfactory throughout the Project."
- **bijilo.** The string "Bijilo" does not appear anywhere in the completion report.
- **chobhar.** Neither "Chobhar" nor "arrest" nor "protest" appears anywhere in the completion
  report. A card titled for arrests at Chobhar is not resting on this document.
- **beira-maputo.** The completion report records "recurrent issues of non-compliance with OHS and
  community health and safety plans, including the fatality of one worker and three community
  members", and "retroactive RAPs for two cases where gaps in past implementation had been
  identified" — useful for `killed` and `killed_note`, which need a stated cause.
- **iraq.** Road-safety fatality figures in this report are the CHECK31 over-match: "an estimated
  fatality rate of 31.5 deaths per 100,000 people in 2013" and a traffic-fatality outcome indicator.
  The writer did not touch them. "No fatalities from the public were recorded" appears in ¶74.
- **cap-labadie.** The lender role already flags that the report gives two different Bank-performance
  ratings; confirmed on the file (key ratings page Satisfactory, ¶92 Moderately Satisfactory).

## 8. URL set

**Holds.** 37 source URLs across the writer's file. 29 match a `pdfurl` in `harvest_manifest.json`
path-for-path. The other 8 are not in the manifest and were each reproduced from a documents API
query before use, with the API returning the identical path:

| case | query that reproduced it | API docdt |
|---|---|---|
| lesotho (2006 FA) | `Financing Agreement Credit 4237-LS` | 2006-11-21 |
| tripoli (PA amendment) | `Amendment to the Project Agreement for Loan 7166-LB` | 2012-08-09 |
| tripoli (LA amendment) | same query, second hit | 2012-08-09 |
| kumasi (CIDA grant) | `TF014256` | 2013-04-30 |
| kamuzu (amendment letter) | `Credit 5125-MW Grant H775-MW Amendments` | 2017-08-11 |
| dartlo (restructuring paper) | `Georgia Regional Development Project restructuring P126033` | 2017-11-28 |
| lubuk-alung (amendments 1 and 4) | `8043-ID` | 2012-08-08, 2017-11-23 |

No URL was constructed. Fetches used the documented `documents1` host rewrite only. One source
was removed from the file (the St Lucia draft); no URL was added.

## 9. The P122402 trap, and what the archive actually holds

Confirmed from the cached file's own cover:

> "OFFICIAL DOCUMENTS **CREDIT NUMBER 6222-BF** Financing Agreement (Additional Financing for First
> Phase of the West Africa Regional Communications Infrastructure Program - **Burkina Faso**
> Project) between **BURKINA FASO** and INTERNATIONAL DEVELOPMENT ASSOCIATION"

Path: `/home/claude/work/cache/P122402/AGR_2018-05-11_29939619.txt`.

**Not a harvester fault and not for quarantine.** P122402 is the three-country WARCIP APL-1B
programme, so a Burkina Faso instrument is correctly filed under The Gambia's case project number.
This is the multi-country-programme trap: a document correctly filed under the case's project
number can still be another country's instrument, and only the cover settles it.

The writer built nothing from it: `conditions_add` is empty, `ct` is `["exhaust"]`, and the only
source is the completion report.

The Gambia's instrument is confirmed from the completion report's source list, verbatim:

> "Financing Agreement between Republic of The Gambia and International Development Association,
> Grant Number H713-GM, dated June 29, 2011 • Financing Agreement between Republic of Guinea and
> International Development Association, Grant Number H714-GN, dated June 29, 2011 • Financing
> Agreement between Burkina Faso and International Development Association, Grant Number H712-BF,
> dated July 4, 2011"

API searches for `H713-GM` and `Financing Agreement Grant H713-GM Gambia` return **0** results.

**The absence is the programme's, not The Gambia's** — the sentence the coordinator asked for.
Listing all 92 documents under P122402, the only agreements published are: Burkina Faso's Credit
6222-BF financing agreement (2018-05-11) and two amendments to it (2019-06-28, 2022-05-11), an
amendment to Burkina Faso's Grant H712-BF (2018-05-11), and two project-preparation advance
agreements, Q762-GN and Q761-BF. None of the three countries' original grant agreements is
published; Guinea's H714-GN is as absent as The Gambia's H713-GM. `ct_note` now says so.

## 10. The other two `exhaust` claims, tested

- **lubuk-alung (P090990, Indonesia).** Accepted. API queries `8043-ID`,
  `Loan Agreement 8043-ID Conformed` and `Western Indonesia National Roads Improvement Loan
  Agreement` return five documents between them, all amendment letters to Loan 8043-ID (Nos. 1, 2,
  4, 5, 6). No original loan agreement at any query. `ct_note` corrected from six letters to five.
- **dartlo-telavi (P126033, Georgia).** Accepted. API query `8148-GE` returns one document, an
  audited financial statement. `Loan Agreement 8148-GE` returns zero.
  `Georgia Regional Development Project Loan Agreement Conformed` returns twelve agreements, all
  for other Georgian projects (7962-GE, 7741-GE, 4824-GE, 4062-GE, 8775-GE, C3156, C3266, C3473).
  Listing all 43 documents under P126033 returns **no document of any agreement type**: status
  reports, audits, resettlement plans, procurement plans, briefs, project papers, project
  information documents, environmental assessments, a safeguards data sheet, the appraisal
  document, the completion report and its review.

## 11. Routes that failed, named as routes

None. Every route attempted returned. For the record, what worked:

- `https://search.worldbank.org/api/v3/wds?format=json&qterm=...&fl=...&rows=N` — served every
  query, including by bare credit number.
- **`projectid=<P-number>` works as an API filter** and returns the same total as putting the
  P-number in `qterm`. This is how the two absence claims were proved by enumeration rather than
  by guessing. CONDR.md says `docty` as a filter returns nothing; `projectid` is not the same and
  does work. Worth adding to the brief.
- `documents1.worldbank.org` with the host swap — served all five off-cache PDFs.
- `pdftotext -layout` emits "Missing language pack for 'Adobe-GB1'" warnings on these files. They
  are cosmetic; the text extracts fully.

## 12. One finding for the next round's brief

**Read the credit number off the cover, not off the catalogue title — it differed in four of
twenty-six cases this round, and in one case the catalogue title misdescribed the document type
outright.** The St Lucia file the archive titles "Credit Agreement C3936-LC - Conformed" is an
unsigned "CONFIDENTIAL DRAFT (Subject to Change)" with the credit number and date left blank, and
the writer built a sentence on it. The suffix mismatches (4738-IR/IRN, 7166-LB/LE, 7238-LC/SLU,
4237-LS/LSO) are harmless on their own but they are the same mechanism, and they are the warning
sign: when the catalogue and the cover disagree about the number, the catalogue may also be wrong
about the country, the parties or whether the thing was ever signed. The instruction should be the
two-line one: open the cover; confirm country, borrower, number **and that it is executed** —
a date, a signature block, and no blanks.

Runner-up, because it decided this round's one cut and one of its two substantive corrections:
**a covenant that names project Parts must be checked against that agreement's own Schedule 1.**
At Honduras, Parts A.7–A.9 read as the project's safeguard parts in the 2008 agreement and as
storm-damage roads in the 2010 one; the part numbers moved between the two agreements, and the
writer carried the covenant across. Never cite a part-numbered covenant without reading the
project description in the same document.
