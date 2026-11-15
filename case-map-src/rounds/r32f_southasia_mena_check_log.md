# Round 32 check log — batch `southasia_mena`

Checked: `/home/claude/work/out32/southasia_mena.json` (2 cases, 1 extend, 4 drops) and
`southasia_mena_report.md`. Corrected file: `/home/claude/work/out32/southasia_mena_checked.json`.
Every document was read from `/home/claude/work/cache/<PID>/`; nothing was re-fetched from the Bank.
Outcome: **both cases kept with corrections, the extend kept with corrections, all four drops kept
with two of the four drop reasons rewritten.** No case was cut. The two figures that most needed
cutting were cut: `displaced: 8` on the Iran card, and the lender order on the Palestine card.

---

## 1. `west-bank-substation-land-taking-eump` (P084461) — KEPT, lender order corrected

### The lender link holds, but not in the order the writer put it

What the Bank credit financed, from the completion report's own component list and donor table:
**Component 1, the four 161/33/22 kV substations, is headed "Component 1 (financed by EIB)"**
(ICR para 13), and the donor contributions table gives Component 1 an actual cost of US$56.5
million against "EIB", footnoted "Majoritarily EIB with funding from Norway for some auxiliary
equipment". The World Bank's grants (TF-92336, TF-94587, US$14.5 million disbursed) paid for
Component 2(i)(c) the central distribution system (US$3.0m), distribution rehabilitation, capacity
building, consultancies, and the start-up costs of PETL and PERC. **The land was taken for the
substations.** So the works that caused the harm were EIB's.

Two further clauses the writer did not have on the card, both of which cut against the Bank link
and are now on it:

- ICR para 17: the September 2013 level-one restructuring was "to: (i) Adjust components to reflect
  Bank-financed activities only; (ii) Revise the PDO and the project outcomes/performance indicators
  to reflect the results of the Bank-financed activities only".
- ICR Review, section 8b: the Bank "continued to monitor safeguard compliance related to the
  high-voltage substations **even after restructuring when these activities no longer formed part of
  the project**", and "Bank-managed financing accounted for less than 10% of the cost of the original
  project".

### Why this is not the Burkina Faso airport platform

Burkina was cut because **Bank management had determined the platform was not an associated
facility** — the Bank disclaimed it. Here the Bank did the opposite, and the documents say so three
times over:

- ICR para 30: the planning of the four substations "included the preparation of Environment and
  Social Management Plans (ESMP) and Abbreviated Resettlement Action Plans (ARAP) **in accordance
  with the Resettlement Policy Framework prepared by PENRA in 2008 and the World Bank guidelines**
  for each of the substations".
- ICR para 30: "In September 2013, a Bank supervision mission found that PENRA was noncompliant
  with the Bank's safeguards policies for three of the four substations financed by EIB (Jenin,
  Nablus and Hebron)."
- PAD data sheet: "The Project would finance: (i) Supply and install four new bulk 161/33/22kV
  supply substations" — the substations are inside the project the Bank appraised, and OP/BP 4.12
  was triggered for them.

The land taking also sits entirely **before** the restructuring that removed the substations from
the project: the resettlement plan is March 2011, the non-compliance finding September 2013, the
safeguards upgrade May 2014.

**Correction made:** European Investment Bank moved to `lenders[0]`, World Bank to `lenders[1]`,
`lk` reordered to `["eib","wb"]`. The EIB role now also carries the ICR's statement that the EUR 45
million loan effective in 2005 was "originally to finance two of the four substations", EUR 10
million of meters and part of the distribution system. The World Bank role now carries the
restructuring clause and the Evaluation Group's "no longer formed part of the project" sentence, so
a reader is told what the Bank's own money did and did not pay for without having to infer it.

### Figures, all verified against the documents

| On the card | Document | Verdict |
|---|---|---|
| TF-92336, TF-94587; US$12.0m original, US$14.5m disbursed; Category B | ICR data sheet | confirmed |
| Approval 15 May 2008; closing 30 Sep 2016 against original 30 Sep 2013 | ICR data sheet (05/15/2008; 09/30/2013 → 09/30/2016) | confirmed |
| Grant agreement TF092336 dated 30 June 2008 | ICR Annex 10: "Agreement, TF092336 GZ, June 30, 2008" | confirmed |
| Report numbers ICR00002455, ICRR0020707, PAD 43298-62 | cover pages and ICR Annex 10 | confirmed |
| Safeguard table: EA and Involuntary Resettlement yes, the other eight no | PAD section F table, all ten rows read | confirmed — the fuller of the PAD's two copies was used, which is the right one |
| Jenin 15,028 m², 23 owners, JD 66,315.20 at JD 4.41 | RAP §2.3.1 and Table D | confirmed, verbatim |
| Sarra 15,174 m², 10 owners, JD 349,000 at JD 23 | RAP §2.3.2 | confirmed |
| Beit Oula about 17,524 m², 4 owners, JD 89,898 at JD 5.13 | RAP §2.3.3 | confirmed |
| Qalandia 11,000 m², bought directly, one person, no price | RAP §2.3.4 and Table D | confirmed |
| 23 + 10 + 4 + 1 = 38 in a column headed "Number of person affected" | RAP Table D | confirmed; this is ICIJ's 38 and the card says so |
| 23 owners named in the Jenin annex across parcels 8/1, 10/1, 11/1 | RAP Annex 1, names counted: 8 + 11 + 4 = 23 | confirmed |
| IEG outcome Moderately Unsatisfactory, weighted by 81% disbursed at restructuring; risk High | ICRR sections 6, 7 | confirmed |
| ICR outcome Moderately Satisfactory | ICR data sheet | confirmed |
| Three substations complete at closing, Ramallah 15%, Area C permits, July 2018 | ICR para 26 and milestone table | confirmed |
| Contract terms May 2008 to October 2010; IEC's disincentive; Feb 2012 signature | ICR paras 25–26 and milestone table | confirmed, verbatim |
| Footnote 17: emailed complaint from the Nablus substation's nearest neighbour, task team met the complainant, four other neighbours and the mayor, written response | ICR footnote 17 | confirmed; the footnote does indeed not say what the complaint was about |
| Point 32.2095, 35.1902 | Nominatim `q=Sarra&countrycodes=ps` returns صره at 32.2095467, 35.1901938 | confirmed to four decimals |

**No plan-reprint problem.** The brief flagged no reprints for this row and none exists: the areas,
owner counts and assessed sums appear in the March 2011 plan and in no outcome document. The card
now says that in terms, so a reader cannot take them for outcome figures.

### Three corrections inside the prose

1. **The consultation dates were not consultations about the land.** The writer wrote "The plan also
   sets out when people were to be consulted". The plan's §3.1 says the Citizen Consultancy Meetings
   "aim at gathering data and community feedbacks concerning the system configuration of JDECO for
   development of the distribution system in the central area of the West Bank". That is a clause in
   the same section that cuts the other way and it was dropped. Corrected on the card.
2. **The Jenin annex column.** "JD 66,315.2 awarded" reads as a payment. The table's column head is
   the amount awarded to owners and the comments column on the same row reads "Assessed amount not
   yet awarded", with the decree number and date blank. Reworded so the contradiction is in the
   table's own terms.
3. **A favourable clause in the review's same paragraph.** The ICR Review says "The ICR reports,
   however, that these issues had been rectified by closure, although it does not state whether or
   not there was compliance with OP 4.01" — immediately before the compensation sentence the card
   quotes. Added.

### Title corrected

"38 owners" → "38 people". Jenin's 23, Sarra's 10 and Beit Oula's 4 are called owners; Qalandia's
one is listed only as a person affected, on land "bought directly".

`confidence: contested` is right and the note says plainly who reports on whom. The
`informed IEG` grep returns one hit, the Task Team Leader's statement that the compensation process
was later completed, and the card attributes it to the staff statement rather than to a document.

---

## 2. `ahwaz-jomhori-pumping-station-house-expropriation` (P071191) — KEPT, `displaced: 8` CUT

### The figure is the report's own, and it still may not sit in `displaced`

The writer is right that it is not ICIJ's number. The sentence is in the completion report's
safeguards section, and the whole passage reads:

> "Land Acquisition Plans (LAPs) were prepared wherever land expropriations were involved. In
> addition, wherever resettlement of people, including displacement of livelihoods, was involved, a
> Resettlement Action Plan (RAP) was prepared. For example, in Ahwaz, the land for pumping station
> (AS23-1) located on Jomhori Boulevard (with surface area 800 sq. m) was a residential house that
> belonged to two individual owners and agreement with them was reached, a down payment was paid,
> and the property was expropriated. Since the deal involved resettlement of at least eight
> individuals, an abbreviated Resettlement Action Plan (RAP) was prepared."

**Two independent reasons the field must go, and either alone decides it:**

1. **"At least eight" is a floor.** Round 18 moved an Ethiopian "over 30" out of `killed` on exactly
   this ground, and CHECK20 states the rule without an exception: an inexact figure goes in the note
   uncounted. There is no reading of "at least eight" that is a count.
2. **The verb does not say anyone was moved.** The sentence's subject is the preparation of a plan:
   a RAP was prepared *because* the deal involved resettlement of at least eight individuals. The
   document records the property expropriated and a down payment paid; it does not record eight
   people relocated. `displaced` holds a document's count of people actually relocated.

`displaced` and `displaced_label` deleted. `displaced_note` rewritten to open with "No count of
people relocated is entered for this case", then give the report's floor, where it sits and why it
is uncounted, and ICIJ's identical 8 separately.

**The card still stands without the field**, on limb (b): a residential house belonging to two
identified owners, 800 square metres, at a named site, expropriated after a down payment, with no
document recording the balance. That is the Bukoba standard — identifiable rather than named — and
the forward rule lists "land taken" as limb (b) harm in its own right.

### Corrections

1. **A favourable clause in the same paragraph, dropped.** The sentence two lines above the quoted
   passage reads: "The environmental impact of the investments was generally positive and there were
   no compliance issues in both Ahwaz and Shiraz." The card quoted the Evaluation Group's weaker
   restatement of this instead of the report's own. Added.
2. **Loan number wrong.** The card said "Loan 4738-IR" twice. The conformed agreement's cover reads
   **LOAN NUMBER 4738-IRN**. The Bank's catalogue title for the same file reads "Loan Agreement,
   L4738-IR" — that is metadata, so the cover wins, per the dates-and-metadata rule. Corrected in
   the lender role and in the source title, with the catalogue form noted there.
3. **Two passages conflated.** The card ran "will disproportionately affect the poorer segments of
   the society" together with "in the same list adds that the proportion of completed works is also
   higher in poorer neighbourhoods". Those are different places: the future-tense sentence is in the
   body (page on outcomes); the counter-clause is in the risk list, where the report itself writes
   "**The poor are disproportionately affected** due to lack of completion", present tense.
   Corrected, and the writer's reported conflict 6 is downgraded — see Conflicts below.
4. **Appraisal against outcome framed as a contradiction.** "had said the opposite" is a
   before-and-after unless the quantity and the date are named. The appraisal's "In no case are
   residences or current economic activities or livelihoods affected" governs the expropriations its
   own table lists: 67 ha from 13 local farmers, and eight pumping-station plots of which two were
   private, all "undeveloped urban land", with the Ahwaz annex adding "There are no holders of other
   rights, no relocation or loss of shelter, income, or livelihoods". The Jomhori Boulevard house
   matches none of those entries and appears only in the 2010 report. Both documents stay on the
   card, now with what each covers and when, and no reconciliation.
5. **The cultural-property policy is named twice, differently, inside one report.** The ICR's
   background section says "OPN 11.03 'Cultural Property' was also triggered for Shiraz"; its
   safeguards compliance section says "Safeguard Policy (OP 4.11) for cultural heritage sites was
   triggered". Left unreconciled, with both on the card.
6. **A company role that described a body wrongly.** The card called the National Water and
   Wastewater Engineering Company "the holding company for Iran's urban water and wastewater
   utilities". No document says that. The completion report says "The government had established a
   strong NWWEC **within the Ministry of Energy, reporting directly to the Vice Minister for Water
   Supply and Sanitation**". Corrected to the report's own description. The rest of that role holds:
   the technical support units did carry out procurement (ICR: "Establishing the TSU to support the
   project technically and implement all procurements") and the project's environment and safety
   officer sat in a TSU (PAD).

### Figures verified

Loan US$279,000,000 at Section 2.01 dated 17 July 2004; Board 25 May 2004; effective 17 November
2004; closed 30 September 2009 with no restructuring; US$200.6 million disbursed; Category A; OP
4.01 triggered; exemption for OP 7.50; ICR ratings Unsatisfactory / Substantial / Moderately
Unsatisfactory / Moderately Satisfactory; ICRR13381 Date Posted 09/22/2010, outcome Unsatisfactory.
All confirmed from the ICR data sheet, the conformed Loan Agreement and the review's own first page.
Point 31.3231, 48.6793 matches Nominatim's result for Ahvaz to four decimals. The `informed IEG` /
`the project team` greps return nothing in this project's review.

---

## 3. `colombo-st-sebastian-canal-mcudp` (P122735) — extend KEPT, shape fixed, three corrections

### Shape

`merge.py` reads an extend's content from the top level of the object and indexes it by `x['id']`.
The writer's object had the content at the top level correctly — `extend`, `lenders_add`, `lk_add`,
`cp_add`, `sources_add`, `fields_add`, nothing nested under an `add` key, so the round 18 silent
no-op is not present. **One gap: there was no `id` key.** The dict key carries the id, but the
converter that turns this file into merge.py's `{"extend": [...]}` list has to supply it, and the
round 31 checker added `id` to its own extend for that reason. `id` added. `fields_add` holds three
strings and nothing else; leading spaces stripped, since merge.py inserts the separator itself.

I merged the extend against `window.CASES` out of `base.html` in a dry run: all three fields append
and read as continuous prose, and `sources_add` adds three sources to the live seven with no URL
collision.

### Duplication against the live card

The live card already says "in 2014, 91 families living along St. Sebastian's Canal in Maligawatte
were forced to move", on CPA's account, and its `displaced_note` repeats the 91. The writer's added
text re-introduced 91 as a plan figure, which on the merged card reads as a new count and then
appears to undercut the live one. Reworded to "The same figure of 91 appears as a target in the
project's own Resettlement Action Plan", which is the useful fact: CPA's 91 and the plan's 91 are
the same number, and no Bank document counts how many of them moved.

### Corrections

1. **A reconciliation neither source makes.** The writer's note said The Morning "independently
   records the same eight households still in place". The completion report counts 24 households in
   the building — 16 tenants and 8 legal owners — and says "eight tenants are in the process of
   relocating"; the newspaper counts "eight structures occupied the stretch" and "eight houses".
   Whether the newspaper's eight are the report's eight owners, its eight relocating tenants, or
   neither, is stated by nobody. Corrected to say exactly that.
2. **The newspaper names the canal, which makes the card stronger, not weaker.** The writer's
   confidence note said the tie to the loan rests on the completion report naming the same canal and
   stretch. The article's first paragraph reads: "Flooding at the National Hospital in Colombo during
   recent heavy rains has been **linked to an unfinished drainage project on the Norris Canal**,
   which remains blocked by eight houses". The identification is the article's own. Added, and the
   hedge narrowed to what is actually missing — the article does not mention the World Bank.
3. **Who is paying for the works now.** The completion report's paragraph 59 ends: "At project
   closure, this sub-project was incomplete and **GoSL agreed to finance the completion of the
   balance work of 126 meters**. The project had diligently followed the resettlement process
   indicated in the RAP and there was no safeguards non-compliance. The Bank will continue to
   monitor the progress of the remaining resettlement." The writer had the second sentence but not
   the first or the third. It matters: the removal now being threatened is on works the government
   agreed to pay for after the loan closed, while the Bank undertook to keep monitoring the
   resettlement. Both added.
4. "The Norris Canal eviction" → "the Norris Canal resettlement". Nobody has been removed; the
   article says the residents refuse to vacate and the government will proceed under the Act.
5. Added two of the plan's own favourable clauses beside its 91: the flats are 400 square feet
   "worth LKR 7 million each", and "around eighty out of 91 households (87.9%) will not experience
   any adverse impacts on their livelihood activities".

### Figures verified

652 households (ICR para 57, verbatim, including "largely the non-titleholder squatter families
living along canal banks"); 24 households, 16 tenants, 8 legal owners, four legal owners, Supreme
Court, early stages (para 59, verbatim); 126 of 675 metres (para 60); LKR 12.3 million to 56
female-headed households, four of five and four of six management positions (para about social
safeguards); 407 grievances and 377 resolved (para 58) against 423 in the borrower's section;
closed 31-Dec-2021, US$199,059,117 of US$213,000,000, Outcome / Bank Performance Moderately
Satisfactory, M&E Modest (data sheet); 91 households, "regulatory requirement that these 91
households are relocated", 66 Watte, September 2014, LKR 5,000 transport allowance, "expressed
willingness to relocate" (RAP SFG1314, §§1.2.7, 1.5.3, 1.5.4 and the entitlement budget).
The Morning's figures and both quotations confirmed against the cached page.

### What the lead must do by hand — confirmed, and neither is fixable through `fields_add`

1. **`end: 2016` on the live card.** The added facts run to November 2026 and the project closed
   31 December 2021. `fields_add` only concatenates strings, so a number cannot be set from here.
   `end` should become 2021 if it means the loan's closing date, 2026 if it means the last event on
   the card. The map's other cards use the harm's own span, which argues for 2026.
2. **`lenders[0].role` carries no P-number.** Confirmed: the live role gives the loan amount, the
   approval date and the ministry, and no project number. P122735 is in the appended prose so the
   dedupe will see it, but the role should carry it.

A third, which the writer did not raise: the live card's `displaced_note` says "91 families moved
along St. Sebastian's Canal in 2014, per CPA" while the project's own plan gives 91 as a target. The
note is correctly attributed to CPA and stays, but the lead should know the two 91s are the same
number before anyone treats that note as a Bank-documented relocation count.

---

## 4. `morocco-ain-beni-mathar-solar-land` (P041396) — DROP STANDS, reason rewritten

The outcome document settles it: ICR, 25 June 2013, "Regarding social issues, all measures put
forward by ONEE to be in compliance with Bank's policies, e.g. compensation to landowners for loss
of agricultural productivity, were considered satisfactory and no particular issues arose",
repeated by the evaluation review of 27 June 2014 and attributed there to the ICR. No outcome
document records a loss to anyone. Neither limb is met.

The plan-reprint call was made correctly: PAD "203 hectares of land **will be acquired** by O.N.E."
against ICR Annex "203 hectares of land **were acquired** by ONEE", so the 203 / 160 / 88 figures
are outcomes.

**But the drop reason as written rested on one of three documents and on half of one sentence.**
Rewritten with all sides:

- **Counts, three ways, unreconciled.** RP443 v2 (June 2006): "Le nombre de ces personnes et
  organismes est de 48 (6 propriétaires pour le site de la centrale et 42 personnes et organismes
  pour la bretelle de gaz)" — the writer's figures. The social evaluation of the **same month**:
  "Les personnes touchées par l'acquisition des terrains pour le site sont au nombre de **7**" and
  "pour la bretelle de gaz sont au nombre de **21**", plus 3 public bodies and the ethnic
  collectivity. The PAD of February 2007: consultations with "**8** persons whose land and/or assets
  will be affected by the power plant construction and **21** persons affected by the gas pipelines".
- **"Already compensated" has a counter-clause in the other document.** The writer quoted RP443 v2:
  the farmers on the plant site "ont été indemnisés par l'ONE selon les prix fixés par la commission
  administrative d'expertise". The social evaluation of the same month says of the same people:
  "Ces personnes ont déjà été indemnisées par l'ONE pour privation d'exploitation, mais **elles sont
  en attente de l'indemnisation pour la vente qui doit leur être versée par le Ministère de
  l'Intérieur**", and for the gas spur "L'ONE attend l'envoi par la Province du PV d'expertise qui
  fixe les prix pour entamer la procédure d'indemnisation des propriétaires."
- **Four people refused.** Same document: "4 personnes ne veulent pas céder leurs terrains qu'ils
  considèrent comme source principale de revenus et qu'ils veulent les laisser à leurs enfants",
  while saying they did not oppose the project. That sits directly against the null sentence the
  drop leaned on, "ces terrains ... ne constituent pas la seule source de revenu de leurs
  propriétaires", in the same document.

None of that becomes limb (b), because the 2006 positions are interim stages of an acquisition and
the only outcome document says the compensation was satisfactory and nothing arose. But a drop
reason that quotes the favourable half of a June 2006 sentence and not the unpaid half is the fault
this round was told to look for, and it is now stated both ways on the record.

The collective-land thread is kept as the writer had it, with one addition: the social evaluation
says the community projects were "identifiés par la commune et les représentants de la Collectivité
Ethnique sur la base des besoins de la population", which is the clause that stops the 7,998,750
dirhams going to the state from being a documented loss to the rights-holders.

---

## 5. `tunisia-fathallah-pesticide-store-occupants` (P103189 / P075776) — DROP STANDS

Verified in full. The plan of 12 May 2011: "Sept ouvriers en plus de l'occupant lui même seront
directement affectés par le projet", budget 7,925 dinars of which 2,125 for the compensation of the
occupant and his workers, all future tense, loss identified as a shortfall in earnings while the
business is suspended. The outcome document, ICR 28 June 2013 paragraph 36: the policy was triggered
for the Fathallah store "that was being used for business purposes by occupants" and "Despite
smaller incidents and a difficult political environment resulting from the aftermath of the Tunisian
revolution, the comprehensive resettlement action plan was implemented and completed to a highly
satisfactory extent in June 2012." The lessons section: the project "compensated affected
individuals financially for their loss in income during their temporary resettlement". Temporary
throughout, carried out, paid. Neither limb is met.

**The cross-batch collision is real and harmless.** ICIJ files a Tunisia row (estimate 8) and a Mali
row (estimate 170) under the one number P103189. The completion report says which number is whose:
"The second and third set of country-level projects (ASP-P1 Mali, Morocco, Tanzania (P103189); and
ASP-P1 Ethiopia (P105711)) could not be processed under the project number which was used for ASP-P1
South Africa and Tunisia (P075776)." So the writer is right that the Tunisia documents sit under
P075776; that sentence is now the citation in the drop reason. Checked for an id collision across
the two batches: `west_central_africa.json` carries `p103189-africa-stockpiles-mali`, this batch
carries `tunisia-fathallah-pesticide-store-occupants`. **Different ids, both `status: dropped`, so
nothing merges and nothing collides.** The `ICR_2013-06-28_18645044.txt` file in the two cache
folders is byte-identical (same md5), which is why one report covers both rows.

---

## 6. `afghanistan-justice-service-delivery-land` (P118028) — DROP STANDS

The outcome document was read and the sentence is verbatim, ICR 28 June 2018 paragraph 87: "However,
land acquisition or relocation did not occur as all construction work was carried out on available
government land. Overall, no complaint and non-compliance cases were recorded during implementation
of the safeguards' instruments under the parent Project." Paragraph 85 gives the four provinces,
Kabul, Herat, Logar and Bamyan, and the Resettlement Policy Framework of April 2012.

I checked the one thing that could have undone it — whether an additional financing with its own
works sits outside that sentence's "parent Project". The ICR says the project "has been extended for
six months to November 30, 2017, **with no additional financing**". There is no AF.

**The parent-document link, which BRIEF31 says to verify rather than assume, holds:** the evaluation
review is headed "AF: ARTF-2nd Judicial Reform Project (P118028)" — ICIJ's own row name — and gives
L/C/TF number TF-12533, which is the grant number on the cover of the completion report for the
Justice Service Delivery Project. Same grant, same project, two names. Added to the drop reason.

The abbreviated resettlement plan is as described: principles and process, no site, no census, no
figures, and its one candidate sentence is the replacement-cost recital. The review's "The project
team later confirmed that there was full compliance, to the best of its knowledge, with safeguard
policies" is a staff statement; the writer flagged it and did not rely on it, which is right.

---

## 7. `bangladesh-psdsp-economic-zone-roads` (P120843) — DROP STANDS, reason rewritten

### The works the plans covered were built, and the credit paid for access roads at that zone

The drop reason's deciding claim was that "the road widening was not paid for by this credit, which
is the first of the three tests". **That claim is contradicted by the completion report itself.** The
writer searched for "Mirsharai", the plan's spelling. The report spells it **Mirsarai**, and in
Annex 8 says:

> "The project also supported sizable construction of a 7.7Km of embankment and site development of
> 938.5 acres at Mirsarai 2A and 572.6 acres at Mirsarai 2B. Site development included landfilling
> through dredging material from the sea, **access roads**, bridges, power and gas sub-stations, a
> sluice gate, and a water supply system."

The August 2016 plan is for the same zone phase and says so in terms: it was prepared for impacts
"due to establishment of the Mirsharai Economic Zone Phase 2 (MEZ2), which is a subproject of the
Private Sector Development Support Project (PSDSP)", a project "being jointly financed by the
Government of Bangladesh (GOB) and the World Bank". So the lender link is not disposed of.

The Financial Express report is real and accurate as the writer described it — I fetched it to check,
since the writer cached no copy: 1 March 2019, "Construction of MEZ approach road to fall behind
schedule", the 10-km road from Abu Torab built by the Roads and Highways Department at Tk 1.41
billion at BEZA's request, 46 acres handed over for the new section, no households and no World Bank
financing mentioned. It is evidence that the approach road was built on a government budget line
outside the credit. It is not proof, because the report names neither the 6.5-km widening nor the
credit. **Both readings are now in the drop reason, unreconciled.**

### The drop still holds, on the forward rule rather than on the lender test

No outcome document records anyone displaced, any compensation paid or any loss. ICR paragraph 10:
Component 2 "also provided resettlement compensation for households affected during the development,
but this was ultimately not needed"; paragraph 12 and Table 1: resettlement US$0.9 million allocated,
US$0.0 million actual, reallocated "because the resettlement budget was not needed". A plan saying
people will be moved is not harm. Two facts added that strengthen the drop:

- The evaluation review records the resettlement line being cancelled once already: in July 2013 the
  component's IDA allocation was cut "from an amount of US$111.9 million down to US$24.6 million, due
  to the cancelation of the costs for the rail connections, carriages and landings, and most
  importantly, and the compensation for Eligible Resettlement Costs as well", before the February
  2016 additional financing restored it.
- The ICR says some zones "deemed non-feasible due to social, environmental, or economic factors were
  removed" and that "the social safeguards regarding resettlement and dispute resolution mechanisms
  that were no longer applicable to the project were scaled down significantly". Mongla EZ, to be
  built by a private developer on a design-build-finance-own-operate-transfer basis, appears nowhere
  in the report and is not among the operational zones listed at closing. That is consistent with
  Mongla having left the project, though no document says so, and it is not stated as a finding.

Also added: the August 2016 plan's impact table gives the 14 non-titled households as **82 persons**,
a figure the drop reason did not carry, and records that the widening was put on the west side
because the east "would have required private land acquisition and displacement of some 90 private
households". The 14 households remain the sharpest open question in the batch, now stated as
unreconciled rather than as answered.

---

## Figures where documents disagree, left unreconciled

1. **Palestine, where the compensation ended up.** ICR para 30: "the compensation process had started
   but it had not yet been completed", then "The issue was solved thanks to the proactivity of the
   Bank team". ICR Review §11a on the same page: "Although project affected people were identified
   prior to the commencement of construction activities, the compensation process had not been
   completed by project closure", with "The Task Team Leader subsequently informed IEG that the
   process was subsequently completed". Both on the card; the staff statement labelled as one.
2. **Palestine, Jenin's status, inside one document.** RAP Table D: "Resettlement process finish".
   RAP Annex 1 Table B for the same three parcels: 23 owners, JD 66,315.2, no decree number, no date,
   "Assessed amount not yet awarded".
3. **Palestine, the ICR's risk rating as the review prints it.** ICR data sheet: Risk to Development
   Outcome **Moderate**. ICR Review §12 ratings table, in the column for the ICR's own rating:
   **Modest**. Not on the card. This is the fault CHECK20 names — the Group's column for the report's
   own ratings is sometimes wrong — and it occurs here as well as on the Iran row.
4. **Iran, the ICR's risk rating as the review prints it.** ICR data sheet: **Substantial**. ICR
   Review ratings table, ICR column: **Significant**. The writer found this one. Not on the card.
5. **Iran, whether residences were affected.** PAD 29 April 2004: "In no case are residences or
   current economic activities or livelihoods affected", governing an expropriation table of
   agricultural and undeveloped urban land. ICR 31 March 2010: the land for AS23-1 "was a residential
   house that belonged to two individual owners". Both on the card, each with what it covers and when.
6. **Iran, the appraisal's own hectares.** PAD body: "an unused agricultural plot of 67 ha from 13
   owners". PAD Annex 12b expropriation table, same plot: **67.5 ha**. Both now on the card.
7. **Iran, the date of its own completion report.** Cover: March 31, 2010. Data sheet: ICR Date
   04/06/2010. Card and source use the cover date, which is right.
8. **Iran, the name of the cultural-property policy inside one report.** OPN 11.03 in the background
   section, OP 4.11 in the safeguards compliance section. Both now on the card.
9. **Iran, the loan number.** Agreement cover: LOAN NUMBER 4738-IRN. Bank catalogue title for the same
   file: "Loan Agreement, L4738-IR". ICR: "Loan No.: IBRD47380". Cover used, catalogue form noted.
10. **Morocco, how many people.** 48 (6 + 42) in RP443 v2 of June 2006; 7 and 21 plus 3 bodies in the
    social evaluation of June 2006; 8 and 21 in the PAD of February 2007. Three documents, three
    answers, no reconciliation offered.
11. **Morocco, whether the plant-site farmers had been paid.** "ont été indemnisés ... selon les prix
    fixés par la commission administrative d'expertise" (RP443 v2) against "en attente de
    l'indemnisation pour la vente qui doit leur être versée par le Ministère de l'Intérieur" (social
    evaluation, same month).
12. **Colombo, Norris Canal owners.** ICR para 59: "The 24 households comprised 16 tenants and 8 legal
    owners", then "the properties belonging to the four legal owners". 8 against 4, same paragraph, no
    explanation.
13. **Colombo, grievances.** 407 in the Bank's text (para 58); 423 in the borrower's own section of
    the same report. Both on the card.
14. **Colombo, the unfinished stretch.** 126 metres of 675 (ICR para 60) against "100 to 150 metres"
    (The Morning, 11 November 2026). Both on the card.
15. **Bangladesh, 14 households against an unspent budget.** "will displace a total of 14 non-titled
    households ... and 5 mosques" (Mirsharai EZ2 plan, August 2016, 82 persons in its table) against
    "this was ultimately not needed" and US$0.0 million actual (ICR, 22 December 2021). No document
    says what became of them.

### One conflict the writer reported that I am downgrading

The writer's conflict 6 — "the review turns a forecast into an outcome" on Iran's poor
neighbourhoods — is only half there. The ICR says it in the future tense once ("will
disproportionately affect") and in the present tense twice ("The poor are disproportionately
affected", and "the poor are disproportionately affected if the project is left incomplete"). The
Evaluation Group's past tense is not a change of the report's meaning. The card's claim that the
review restated it in a different tense has been removed. Nothing else turned on it.

---

## Faults appearing in more than one card

1. **The favourable clause in the same paragraph, dropped.** Three times: Palestine's consultation
   purpose and the review's "rectified by closure"; Iran's "there were no compliance issues in both
   Ahwaz and Shiraz"; Colombo's "GoSL agreed to finance the completion of the balance work". Plus the
   Morocco drop reason's half-sentence on compensation. The writer's report claims the favourable
   clause was quoted beside every damaging one. **That claim does not hold: it was quoted beside most
   of them, and the four misses all run the same way, towards the harm.**
2. **A tidy identification nobody makes.** Colombo's "the same eight households" is the only instance,
   but it is the same mechanism as a tidy reconciliation of two figures.
3. **A body described in words no document uses.** Iran's NWWEC as "the holding company". One
   instance, caught only because the role was read against the ICR.

---

## Anything outside the fields I was asked to check

- **`lenders[0].role`, both cards.** Palestine: the financing, dates, report numbers, environmental
  category and the full safeguard-policy table all check out — this is the one field in the batch that
  was written from the documents rather than from a data sheet, and the only correction needed was the
  missing restructuring clause. Iran: one real error, the loan number, plus the single-naming of a
  policy the report names two ways.
- **The live Colombo card, two fields the extend cannot reach**, confirmed as the writer reported and
  set out above, plus the `displaced_note` point about the two 91s.
- **`ct: ["safeguard"]`** on both new cards matches the live card's tag and the harm type.
- **`mechanism: "project"`** on both. The live Colombo card uses `"land"` for a canal-bank relocation.
  Both are in the allowed set and both readings are defensible for a land taking under a project
  credit; worth the owner's eye rather than a correction from me.

---

## Anything I could not check, by the route that failed

1. **Whether any of the 38 Palestinian owners was ever paid.** The harvest holds no document later
   than the March 2017 completion report, and the only statement that the process finished is the
   Task Team Leader's to the Bank's evaluators. Route that failed: there is no later document in the
   cache and no Bank route was tried, under this round's instruction not to re-fetch. Not a host
   problem.
2. **What became of the 14 households and 82 persons on the Mirsarai approach road.** Route: the
   completion report and the evaluation review were both read end to end for "Mirsarai", "Mirsharai",
   "resettl", "displace" and "access road"; the only outside report found on that road, the Financial
   Express of 1 March 2019, was fetched and names no households.
3. **Whether the eight structures in The Morning of 11 November 2026 are the completion report's eight
   legal owners or its eight relocating tenants.** Neither source says, and no later Bank document
   exists; the project closed in 2021 and the works passed to the government.
4. **What the "smaller incidents" at the Fathallah pesticide store were.** The completion report
   mentions them in paragraph 36 and describes none; the Project Performance Assessment Report of 29
   September 2016 and the resettlement plan were both searched and add nothing.
5. **The Jenin village point.** Not plotted. Nominatim returned nothing for "المقيبلة جنين" or
   "Al-Mqeible, Jenin" — a single geocoder route on one name, not a host refusal, and the card names
   the village without plotting it.

**No route was blocked.** All eleven source URLs in the file answer HTTP 200, the ten Bank URLs as
`application/pdf`; Nominatim answered on two of three queries; the two outside pages fetched fine.

## Source URLs

Every Bank URL in the file matches a `pdfurl` in `/home/claude/work/harvest_manifest.json` exactly,
path for path, with the host rewritten to `documents1.worldbank.org` and the scheme upgraded. I
checked all ten against the manifest programmatically and then with a HEAD request: **ten of ten
answer 200 `application/pdf`**, and each document id in the URL matches the cached text file the card
quotes — including the Palestine resettlement plan, where the manifest holds two files under
`RP655 v2` and the URL on the card is the English one (id 14561327) that the card actually quotes,
not the Arabic (id 14561328). The eleventh, The Morning, answers 200 `text/html`. **Nothing was
constructed.** The round 31 failure for this region — 23 of 23 URLs 404 — is not repeated.

## Did the briefs help or mislead?

Helped, with one real cost.

- **The warning about thin extraction did the work.** It is what sent the writer to the Palestine
  completion report's footnote 17 and to the Jenin compensation annex, neither of which appears in any
  candidate sentence, and to the Colombo borrower section's 423 grievances. I confirmed all three in
  the documents. That instruction is worth keeping at the top of the brief.
- **The plan-reprint check worked exactly as described on Morocco**, and the verb test settled it.
  The brief's three flagged figures were the three that mattered.
- **It misled once, by omission, in a way that cost a drop reason its deciding fact.** The Bangladesh
  brief surfaced nothing from the completion report's Annex 8 — not the Mirsarai 2A/2B site
  development, not the words "access roads". A brief that lists an outcome document's annexes by name
  and flags the project's own site names, including spelling variants of them, would have put the
  writer on it. **The variant spelling is the generalisable finding: the plan says Mirsharai, the
  report says Mirsarai, and a grep on the plan's spelling returns nothing.** Worth a brief section
  listing every spelling of each site name that occurs across a row's documents.
- **The writer's three complaints about the briefs are all correct**, and I would add a fourth: the
  brief surfaced no sentence from a *second* plan contradicting the first, which is what decided the
  Morocco counts. Morocco's folder holds two June 2006 resettlement documents that disagree on how
  many people were affected and on whether they had been paid, and nothing in the brief pointed at
  the disagreement.
- **Noise, confirmed.** "Replacement cost" fired on the policy recital in the Afghanistan framework,
  as predicted. The Morocco "affected, NOT a relocation count" bucket returned the PAD's 8-and-21
  consultation sentence, which turned out to be one of the three disagreeing counts — so that bucket
  was more useful than its label suggests.
