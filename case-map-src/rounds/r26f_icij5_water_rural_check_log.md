# Check log — round 21, batch C (water, irrigation and rural rows)

File checked: `/home/claude/r21/r26f_icij5_water_rural.json` — 10 cases, 1 extend.
Corrected file: `/home/claude/r21/r26f_icij5_water_rural_checked.json`.
Every document was read from `/home/claude/r21/cache/` by P-number. All 32 URLs in `sources` and
`sources_add` were fetched and returned 200.

**Outcome: 10 cases kept, 1 extend kept, 0 dropped. Two counts came off the cards — `displaced`
5,721 on Nigeria and `killed` 3 on Nigeria — and one reported disagreement was manufactured.**

---

## The ruling on deaths, applied

| card | writer | checked | the document's cause |
|---|---|---|---|
| `ethiopia-sudan-interconnector-line-deaths` | 3 | **3 confirmed** | ICR para 56(i): one death June 2010 "due to the negligence of the personnel, who did not use scaffolding or care when crossing the road for the purposes of stringing a line"; "The other two deaths occurred in 2011 as a result of an accident during a tower erection, as the personnel did not wear safety belts"; the subcontractor "neglected to mandate the use safety of equipment such as safety belts and helmets". Cause tied to the works. |
| `patna-ganga-riverfront-resettlement` | 3 | **3 confirmed** | ICR para 89: "three workers died under circumstances that appear to have been preventable", root-cause analysis "pointed at gaps in site management and OHS practices". The project-history annex adds a second, firmer cause: "The root-cause analysis indicated the accidents occurred due to negligence on OHS training of workers and supervisors." |
| `corumana-dam-resettlement-mozambique` | 1 | **1 confirmed** | ICR Annex 7 para 3: "One fatality occurred during construction, caused by a preventable vehicle accident, the root cause of which was determined to be mainly a lack of senior management commitment in the Contractor's organization and to some extent to the inadequate borrower capacity to manage safeguards measures." |
| `newmap-nigeria-erosion-displacement` | 3 | **0 — corrected** | ICR para 96 is the only passage: "OHS issues were reported during project implementation, three fatalities were recorded and ESIRT were triggered. For all these incidents, root cause analysis was carried out, whose findings showed that they were not systemic issues but one-off cases." No cause, no date, no place, no identity. The review repeats it without adding anything. The three are now in `killed_note`, naming the completion report of 19 July 2023. |
| `metolong-dam` extend | 0, text only | **0, now in `killed_note`** | ICR para 35, verified verbatim: "There were 10 fatalities that happened during the implementation of the MDWSP. All of them were properly reported and settled following the requirements of the Labor Code of Lesotho, well before GRMs were the norm in projects." The sentence sits in the paragraph on the grievance redress mechanism, with no cause, date, place or identity. |

**On the Metolong `fields_add`.** The existing `metolong-dam` card carries **no `killed` key and no
`killed_note` key at all** — not `killed: 0` as the writer's report says. 217 of the 1,052 cards on
the map have no `killed`, and three carry a `killed_note` with no `killed`, so the precedent is
clean. `merge.py` builds `c[k] = str(c.get(k) or '') + ' ' + v`, so a `fields_add.killed_note`
string **creates** the field rather than appending to anything. The writer put the ten fatalities
only into `fields_add.community` and `fields_add.confidence_note`, which would have left the card
with no `killed_note` of its own. I added `fields_add.killed_note` as a string. All six top-level
extend keys are present (`extend`, `lenders_add`, `lk_add`, `cp_add`, `sources_add`, `fields_add`),
`fields_add` is string-only, and the shape matches the two extends in
`rounds/r26f_icij4_nonchina_checked.json`.

---

## 1. Nigeria's 5,721 — read and rejected

The figure appears once in the completion report, at the fourth bullet of the closing benefit-cost
analysis. The bullet's own heading is **"Benefit 4: Avoided involuntary displacement of people
'with project'"**. Its text:

> "The current estimate, based on the RAP Implementation Reports from 84 project sites shows that
> the project spent an average of USD 3,453 on resettling each of the 5,721 project-affected
> persons (PAPs) actually displaced by the project. Extrapolated to 81 sites, the total figure is
> 7,015 PAPs while, using an economic conversion factor of 0.84 to correct for domestic price
> distortions (as in the BCA of the 2012 PAD), yields a cost of USD 2900 per person, and a total
> benefit of USD 20.347 million per year."

The number's work in that sentence is to supply a divisor — spending ÷ people = US$3,453 a head —
which is then applied to the 254,000 people the 2019 analysis said the works would spare from
displacement, to price the benefit. The review confirms the frame: it lists "Avoided displacement of
people" as one of the three benefit sources added in 2019 and kept at closing. The review never
prints 5,721 or 7,015. The report's own **social safeguards section (paras 101-106) gives no
displacement count at all**; its counts are 9,696 affected people compensated by 31 October 2022
under 94 resettlement plans, 9,471 under 83 plans, and 32 people Abia and Imo could not locate.
And the arithmetic in the bullet does not work: going from 84 sites to 81 yields a *higher* total.

**Decision: 5,721 cannot sit in `displaced`.** It is a modelling input, in a passage whose internal
figures are incoherent, in a report whose quality the review rates Modest. `displaced` and
`displaced_label` are removed; the figure, the 7,015, the 84-to-81 switch and the review's silence
are all set out in `displaced_note`.

**The case survives, on limb (b), on the safeguards section instead of the economic analysis:**
9,696 people compensated for lost productive assets and activities under 94 plans; 32 people in Abia
and Imo never located, with counterpart money placed in escrow; **Imo State still implementing its
resettlement plan at project closing with the compensation fund lodged in escrow**, and the one
state that provided no letter of comfort for its unfinished sites. Those are counted people with
documented losses, which is what the Egypt row dropped for want of (see the drops below). Title,
`place`, `community` and `confidence_note` rewritten so the card leads on what the document records
rather than on the modelling input. **The lead should know this is now a much smaller card than the
one submitted**; if the Egypt standard is applied to it strictly it is arguable, but unlike Egypt the
counts exist.

## 2. The writer's two self-named weakest

**`ouagadougou-onea-works-before-compensation` — kept, with the "disagreement" reframed.** Both
documents verified. The review's safeguards section does place the breach: "ONEA started the
Ouagadougou water transmission civil works funded under additional financing without preparing a RAP
and without compensating four project-affected people, which resulted in the suspension of works in
December 2016." The location does rest on that one sentence, but the sentence is explicit and the
completion report's footnote 50 independently confirms the same incident, the same four people and
the suspension of 15 December 2016. The two residues are **not an unreconciled conflict in the shape
the writer gave them**: the review's 49 of 817 is measured **at May 2017**, the report's 30 of 835
(26 of 756 on lot 2.2, 4 of 79 on lot 6.1) is the position **at closing in December 2019**, after
three reminders. A fall from 49 to 30 is what finding people later looks like. What does not
reconcile is the 18-person gap between the two totals of affected people, 817 against 835. Card and
note corrected to say that. **This remains the thinnest card in the batch** — the harm is a
sequencing breach fixed inside six months plus 30 people who could not be found, with the money
escrowed, nobody named and no amount given.

**`fenjiang-river-foshan-resettlement` — kept.** Every figure confirmed against the report's Annex 6
tables: 85.22 mu state land and 1.68 mu collective, 15 households and 46 people relocated including
two vulnerable people against 10 and 38 planned, 59,790.56 m² demolished of which 2,676.39 m²
belonged to the 15 households, 53 enterprises and shops partly affected, the Zhen'an plant's 86.89
mu against 45 planned with 41.89 mu for a future phase IV, 43,324.17 m² of enterprise buildings,
302 affected people against 1,974 planned, total demolition 105,442.04 m² planned against
112,084.73 m² actual, the private-house rate up "about 140%", full replacement cost on the sampled
cases, and "All the affected households and enterprises/shops received 100% of the compensation upon
contract signed." The report's own words are that 15 households "were re-located", so limb (a) is
met on an outcome figure, and round 17's ruling keeps a documented resettlement even where the
lender recorded no failure. **Hohai University's dual role is on the card and is verbatim in the
report: "Resettlement implementation of the Foshan Component was closely monitored by Hohai
University which also prepared the Resettlement Planning of the project."** Two corrections: the
card had the report "attribute the increase to households splitting after parents died", where the
report's annex note actually reads "Number of relocated HHs **reduced** mainly due to family
spliting after parents passed away" — a note that says reduced where the table shows a rise from 10
to 15, now stated as such; and the one adverse clause the card had left out is added — "Apart from
some delays in the implementation of some resettlement actions, there were no other issues related
to land acquisition or resettlement of project affected people."

## 3. `gameleira-agrovila-ceara` — the one `documented` card, verified hardest

Bank documents, all confirmed: 11 dams across the two phases; 1,394 families under the first phase's
six and 780 under the additional financing's five; the Gameleira population "resettled into homes in
the Gameleira agrovila in January 2011 only had access to water and electric power supply in
December 2012", with plot handover, land titles and fencing unresolved at December 2012; "The
titling of lots had not been done in any of the agrovilas financed by the Project under its two
phases"; Jenipapeiro "filled before any relocation of the power grid that passed through the
reservoir basin", leaving families "without power, and thus without water, since their water supply
relies on electric pumps", solved in early 2012; the 35 Umari houses "presenting structural problems
and the solution was to demolish and reconstruct all of them", by the original contractor at no
extra cost in groups of five with families in government-rented houses; 14 open compensation cases
at December 2012, most with 80 per cent deposited as a court bond; safeguard compliance downgraded
to Moderately Unsatisfactory.

**One correction, and it is the batch's second count.** `displaced: 2174` was the number of families
**affected**, not resettled. The report's table 1 columns show what each family got: 261 into
agrovilas, 377 onto unaffected parts of their own farms, 491 self-resettled with a grant, 12 into
homes in towns — **1,141 families moved** — and **1,033 landowners who took cash compensation and
whose movement the report does not record**. `displaced` is now 1,141 (412 of them under the
additional financing), with the label naming the four columns and the arithmetic, and the note
carrying the 2,174 and the 1,033.

**Independence of Agência Pública confirmed, and every claim the card draws from it is there.**
Fetched and read in full. It is a Brazilian non-profit investigative newsroom; the piece is a signed
field report by Ciro Barros and Giulia Afiune dated 16 April 2015, reported on site with named
residents and photographs, and it is adverse to the Bank — it prints the Bank's reply and then
contradicts it. Confirmed in the text: R$40 million for the dam, R$18 million of it Bank money, on
the state government's figures; "Das 180 famílias atingidas pela obra, de acordo com dados da
Secretaria de Recursos Hídricos (SRH), 91 moravam no local"; the contractor EIT, which "entrou em
recuperação judicial e não pode concluir os serviços", payments suspended by court order in August
2011 and works halted in December 2011, "mas as famílias já estavam sendo reassentadas desde janeiro
daquele ano"; "cada família tem direito a 36 litros de água para seu consumo diário", with the
desalinator treating about 25 per cent of daily use; R$7,000 to Antenor David de Araújo and R$5,000
a house to Maria Socorro, against the R$12,000 ceiling; "Indenizada não, a gente foi agradado pra
poder sair de lá"; Paulo Sérgio de Moraes Alves, president of the residents' association ISCA, on
the salty water and on waiting days for a tanker; the health post "não passa de uma carcaça de
concreto"; refuse collection and leisure areas never delivered; Coelce cutting the illegal
connection in January 2012 and power arriving late 2012; **the prosecutor Glaydson Alexandre of the
Ministério Público de Contas filing a representation in March 2012 against SRH and EIT, "as famílias
assentadas vivem em condições sub-humanas"**; the Bank's reply that its missions "concluíram que o
suprimento de água para a comunidade era adequado"; Aracoiaba finished December 2002 at about R$14
million, 608 families affected and 333 living on the site; and 4,625 families affected by
Bank-financed works in Ceará on SRH's own resettlement-plan data. The article independently
corroborates the Bank's own dates. `documented` stands.

Three small additions made so the card cannot be misread: EIT's judicial recovery; that the
R$250,000 pipeline contract went to a **different** firm, I. C. Projetos e Construções, not EIT; and
that the 36 litres are for drinking and cooking with the salty well water used for everything else.

## 4. The three Evaluation Group omissions — all three hold

**Lesotho (P108143).** The report, para 35: *"There were 10 fatalities that happened during the
implementation of the MDWSP."* Para 70: *"In 2012, the dam contractor began dam construction and
blasting activities without an approved environmental protection plan, a blasting plan, a blasting
method statement, a mining permit, an approved evacuation plan, or a satisfactory dilapidation
survey. This resulted in the suspension of some activities, and complaints were made following an
uncontrolled blast in August 2012. … disputes arose and delayed compensation and necessitated the
involvement of the ombudsman to reach a settlement."*
The review's entire safeguards section instead: *"Specific ESMPs were prepared for the various
project components, and specified mitigation measures were implemented satisfactorily. Compliance
with environmental and social safeguards aspects of the operation was monitored by an independent
panel of experts reporting to the MA. Progress reports on ESMP implementation were submitted to the
World Bank on a quarterly basis, confirming compliance of the agreed ESMPs and other mitigation
measures."* No fatalities, no blasting, no ombudsman. **A fourth omission the writer did not catch:
the 183 outstanding compensation cases appear nowhere in the review either** — it carries only
"2,615 households received compensation, out of a total of 2,798 households affected (93 percent of
target met)", which states the shortfall without naming it.

**Mozambique (P107350).** The report, Annex 7 para 3: *"…initially poor OHS performance, which was
corrected in later months through penalties, training, stringent monitoring and ongoing corrective
action. One fatality occurred during construction, caused by a preventable vehicle accident, the
root cause of which was determined to be mainly a lack of senior management commitment in the
Contractor's organization…"*
The review: *"According to the ICR paragraph 76) 'the construction works caused limited and largely
temporary adverse environmental impacts, with deviations from the ESMP, mainly concerning
housekeeping and waste management, and initially poor OHS performance, which was corrected in later
months through penalties, training, stringent monitoring and ongoing corrective action.' Major
construction ended and all rehabilitation around the works was completed by the time of the ICR."*
The quotation closes on the last word before the sentence recording the death. Confirmed exactly as
the writer described.

**India (P119085).** The report, para 87: *"The only investment that required full land acquisition
was the Patna RFD investment – 249 Project Affected Families (PAFs). Patna RFD RAP implementation
was complex and cumbersome."* Its footnote 58: *"…land allotment was stalled for 2 years and
eventually, extra cash compensation was provided instead of land. Another complication was the
handing over of sites to the contractor before PAPs were resettled and compensation was paid."*
The review's social paragraph, citing that same para 87: *"Land acquisition was utilized where
unavoidable for which RAPs and Abbreviated RAPs (ARAPs) prepared and disclosed. At closing, all RAPs
had been fully implemented and only one ARAP was pending to compensate three Project-affected
people. All Project Affected Families (PAFs) were eventually compensated and provided training for
restoration of income. (ICR para. 87)."* The 249, the two-year stall and the sites handed over early
are all gone; the summary is the sentence the writer quoted.

**This is the batch's most useful finding and it is a pattern, not three incidents: in each case the
review cites the paragraph it is summarising, and in each case what it drops is the fatality, the
permit breach or the count of people left waiting.** On this evidence the review cannot be used as a
check on the completion report's safeguards reporting, only as a second copy of its favourable half.

## 5. The Metolong extend's premise — confirmed

P108143 is the same project as the existing `metolong-dam` card: the report's cover is the Second
Phase of the Water Sector Improvement Project, Metolong Dam and Water Supply, report ICR00004565,
cover date **June 26, 2019**; approval 26 May 2009 and closing 31 December 2018 match the card's
2009-2018 span and its place. The card's "$49.5 million" is the **disbursed** figure: the financing
table gives 53,435,000 committed, 52,799,797 revised, **49,579,223 disbursed**. The lender role the
extend adds says so. The extend's five `*_add` keys sit at the top level with string-only
`fields_add`, as above. The GroundUp source was fetched: dated 19 February 2026, by Sechaba
Mokhethi, R7-billion, "Financed by a consortium of international lenders including the World Bank",
and the spokesperson is Masheane Nkhetše of the Machache Water Supply Movement — "We host this
project. It is on our land. … But we do not benefit." **The title on the card carried an extra word:
the page is "A R7-billion dam but no tap water for villagers in Lesotho", not "for local
villagers".** Corrected.

## 6. The thirteen reported disagreements, each tested for quantity and date

| # | reported | verdict |
|---|---|---|
| 1 | Burkina, 49 of 817 vs 30 of 835 | **Part timing, part real.** Review measures at May 2017, report at closing; 49→30 is consistent with people found later. The 817 vs 835 gap of 18 affected people is real and unexplained. Card reframed. |
| 2 | Ethiopia, whether compensation was timely | **Manufactured — removed from the card.** The review's sentence is in its **Government Performance** section, not Bank performance, and it is a counterfactual: *"a higher level of government input could have expedited customs clearance issues at the Port of Djibouti, … and ensured that compensation payments to PAPs was timely."* That says compensation was **not** timely. The same review's efficiency section says *"Outstanding compensation due to Project Affected People by the district administration (woredas) also caused delays and rescheduling of work … the overall delay was 8 months."* The two documents agree. |
| 3 | Nepal, social safeguards rating twice inside one report | **Real.** Para 33 heading: "Social Safeguards (Satisfactory)" and "the project closed with a satisfactory rating on social safeguards". Para 35 ends: "This improvement resulted in a final rating of 'moderately satisfactory'." Same quantity, same moment. The review names it as the fourth of four faults. |
| 4 | Nepal outcome, MS vs S | **Real.** ICR rating page MS; review "a. Outcome Rating: Satisfactory". |
| 5 | Brazil AF approval date inside one report | **Real.** Data sheet "12/18/2008 (AF)"; text three times "approved by the Board on December 17, 2008". |
| 6 | Brazil risk and Bank performance | **Real.** ICR Moderate / Moderately Satisfactory; review High / Moderately Unsatisfactory. |
| 7 | Nigeria outcome | **Real.** ICR Satisfactory; review Moderately Satisfactory, ICR quality Modest. |
| 8 | Nigeria livelihood beneficiaries inside one report | **Real.** Para 107: "35,977 out of which 15,977 are male and 20,509 are female" = 36,486. |
| 9 | Nigeria people displaced inside one report | **Real**, and now the reason the figure is off the card. |
| 10 | Burkina outcome | **Real.** ICR Highly Satisfactory; review Satisfactory. |
| 11 | Zhejiang resettlement cost | **Not a disagreement — a unit error in the review.** The report's Table 9.2 header is "Total Cost (RMB 000)" and the total row reads 167,009.9 planned against 141,998.7 actual; the report's text gives "US$20.88 million (RMB142 million) which was about 15.5% lower". The review writes "the total resettlement cost was 141,998.7 RMB as compared to the original estimate of 167,009.9 RMB (ICR, page 66)", dropping the thousands. The card already said so correctly; reclassified here, not on the card. |
| 12 | Lesotho affected households and unpaid cases | **A before-and-after, not a conflict.** 2,798 affected and 183 outstanding at 31 December 2018, against 2,786 affected and 247 unpaid reported for August 2018 — four months apart, with the unpaid falling as payments continued. The extend's note reworded to say so. |
| 13 | Burkina AF approval date | **Real, and verified on both sides.** The ICR's restructuring table and its para 23 both give 21 October 2014. The Bank's project record for P149556, queried live, returns `boardapprovaldate 2015-01-12`. |

Three of thirteen were not what they were called: one manufactured, one a unit error, one a
before-and-after. That is the same ratio the brief warns about.

## 7. The seven drops — all confirmed, two with the Georgia-style sentence

- **P095315, Western Provinces Rural Water Supply (China).** Annex 4, verbatim: *"The involuntary
  resettlement activities did not have any house demolition or people replaced according to the
  resettlement action plans (RAPs) and actual land acquisition in the two project provinces."*
  12.61 ha permanent and 132.06 ha temporary across 25 counties, 622 households and 2,422 people
  affected, land compensation US$0.515 million, land-for-land in five Sichuan counties. **Drop
  correct** — land area plus an affected count. ICIJ's 2,422 is this report's own actual
  affected-persons total, as the writer said.
- **P114138, Water Conservation II (China).** *"The project did not entail household relocation."*
  3.58 mu acquired in one province, none in the other two, "hardly any land acquisition or
  compensation was necessary". **Drop correct.**
- **P126813, Ma'anshan Cihu River Basin.** 56.25 ha collective and 1.31 ha state land, "affecting
  534 families and a population of 1,309", no demolition or relocation count, no grievance ever
  filed. **The Georgia-style sentence is in the appraisal document: "especially land acquisition;
  there will be no relocation of people."** The completion report reuses the same clause with the
  no-relocation half removed — *"to minimize negative impacts arising from resettlement, especially
  land acquisition and relocation of people"* — which is a mild instance of BRIEF21's rule 2 running
  in reverse. ICIJ's 1,714 is the appraisal's planned affected population, confirmed. **Drop
  correct.**
- **P091092, DRC Urban Water Supply.** Para 74 confirmed: involuntary resettlement the only
  safeguard not satisfactory at closure, Moderately Satisfactory, for late plans in three cities and
  a Kinshasa plan implemented without waiting for Bank approval, reconciled by a government
  assessment of economic loss the Bank accepted. 187 complaints, 162 founded, all processed; seven
  OHS incidents, six serious, one indicative, none severe, all closed. No relocation count, no
  description of what the 162 founded complaints concerned, no loss figure. **Drop correct**, and the
  staff-severance avenue really does go nowhere: no count of staff separated appears in either
  document.
- **P087154, Tanzania Water Sector Support.** 968 of 1,075 subprojects screened, "The vast majority
  of subprojects were Category C, with negligible impacts"; the borrower annex's only resettlement
  sentence is *"project-affected people fully participated in the process of valuation and
  compensation was done accordingly."* No count of anything. **Drop correct.**
- **P073977, Egypt Integrated Irrigation Improvement.** Para 33 and para 72 confirmed word for word,
  including the April-May 2016 field visits in Kafr El Sheikh, the Behira non-payment "because of
  lack of funds", and compliance on the electrical contracts "only resolved during the final stages
  of the project". **No count of farmers in either governorate and no amount, in either document.
  Drop correct** — and this is the standard against which the Nigeria card was re-tested.
- **P077287, VN-Red River Delta Rural Water Supply.** No completion report in the archive; the
  review's safeguards section records a resettlement plan prepared and disclosed, participatory
  planning and equitable choices for ethnic minorities, and **no land acquisition outcome, no count
  and no loss**. **The Georgia-style sentence is in the appraisal document: "In the sub-projects to
  be implemented in the first year, which are considered to be typical of all sub-projects, none of
  the project affected people will be severely affected or require relocation."** That is an
  appraisal expectation, not an outcome, so it supports the drop without being evidence for it.
  **Drop correct.**

I looked for a recoverable round-17-style compliant resettlement in all seven and found none: no
document in the seven gives a count of anyone relocated, and two state in terms that nobody was.

---

## Required endings

**1. What I could not check, and what stopped me.**
- **Nepal's 11,460 of 11,866.** In the published completion report the parenthesis that should hold
  these figures is **empty in the document's text layer**, under `pdftotext -layout` and `-raw`
  alike, across the whole file: "resolution of 97% of the land ownership issues by the EOP ( ) The
  remaining land owners could not be compensated…". The pair can be read only in the Evaluation
  Group's review, which cites ICR page 8. The card said "The report elsewhere reports that…"; that
  was a fact sourced to a document in which it cannot be read, and both the card and the confidence
  note now attribute it to the review and say why. Whether the parenthesis is a redaction or a
  failed figure I could not establish without rendering the page as an image, which I did not do.
- **The Metolong extend's GroundUp figures beyond the article** — the article gives no compensation
  or resettlement numbers, as the extend says; nothing further to check.
- Everything else named in the task was checked on the documents.

**2. Figures where two documents disagree.** The table in section 6 is the full list, with both
figures in each row. The ones that survived testing as genuine disagreements between two documents
are: Burkina's 817 against 835 affected people (review against completion report); Burkina's
additional financing date, 21 October 2014 (completion report) against 12 January 2015 (the Bank's
project record for P149556); Nepal's outcome, Moderately Satisfactory against Satisfactory; Brazil's
risk, Moderate against High, and Bank performance, Moderately Satisfactory against Moderately
Unsatisfactory; Nigeria's outcome, Satisfactory against Moderately Satisfactory; Burkina's outcome,
Highly Satisfactory against Satisfactory. Inside a single document: Nepal's social safeguards rating
(Satisfactory at para 33, moderately satisfactory at para 35); Brazil's additional financing
approval date (18 December 2008 in the data sheet, 17 December 2008 in the text, three times);
Nigeria's livelihood beneficiaries (35,977 against 15,977 + 20,509 = 36,486); Nigeria's displaced
(5,721 from 84 sites, 7,015 from 81). One more I found that the writer did not: the Fenjiang report
gives the reason for the household change as a **reduction** where its own table shows a rise from
10 to 15, and its Zhen'an monitoring section describes "four relocated enterprises" while the
explanation for the fall in affected people says "no affected enterprises and shops were totally
relocated". Both are internal to the report and are now described, not resolved, on the card.

**3. Faults appearing in more than one card.**
- **Figures lifted from a document's economic analysis and treated as its count.** Nigeria's 5,721 is
  the case that decided a correction, but the same habit shows in the batch's reliance on derived
  numbers generally. It is the fault to watch for next round: an outcome count belongs in the
  safeguards section, and a benefit-cost bullet is not one.
- **Absence claims that the same document refutes, written while the favourable half of a paragraph
  was quoted.** Patna ("the documents do not say which of the two sites each death occurred at, on
  what date") was refuted by an annex of the same report, which gives both sites and both months and
  a firmer cause. Nepal's "the report elsewhere reports" was the mirror image: a fact attributed to a
  document that does not carry it. Two cards, one habit.
- **A review sentence read out of the wrong section.** The Ethiopia "disagreement" came from reading
  a counterfactual in the Government Performance section as a finding about the Bank. Nothing else in
  the batch repeats it, but it cost a card a false conflict in its public confidence note.
- **`rg` written in a vocabulary the map does not use** — four cards, see below.

**4. Wrong in the card data outside the fields I was asked to check.**
- **`rg` is wrong on eight of the ten cards.** The map's own vocabulary, counted off `base.html`, is
  `Africa south of the Sahara` (330), `Latin America and the Caribbean` (222), `East Asia and the
  Pacific` (219), `South Asia` (131), `Europe and Central Asia` (102), `Middle East and North Africa`
  (48). The batch wrote `East Asia and Pacific` (three China cards), `Africa` (Mozambique, Ethiopia,
  Nigeria, Burkina Faso) and `Latin America and Caribbean` (Brazil). Batch A's file used the correct
  `East Asia and the Pacific`, so this is local to batch C. All eight corrected in the checked file.
  Nothing in the merge asserts the vocabulary, so these would have shipped as new region values and
  split the map's region filter.
- The **writer's report states that `metolong-dam` "currently carries `killed: 0`"**. It does not; the
  card has neither `killed` nor `killed_note`. The distinction matters because it is what makes a
  `fields_add.killed_note` safe.
- `corumana-dam-resettlement-mozambique` is the only case with no `ap` flag. That is correct, not an
  omission: its point is the dam itself rather than an administrative centre, and `ap` prints
  "placed approximately".
- `gameleira-agrovila-ceara`'s coordinates (-3.3671, -39.6159) sit about 15 km north of Itapipoca
  town, which is in the direction of the dam on the Trairi-Itapipoca-Tururu boundary. With `ap: true`
  and the point text explaining both, it stands, but it is not the town centre the point text names.
- `laibin-water-environment-displacement` records that the completion report cites the involuntary
  resettlement policy as OP/BP 4.11. Verified: the report really does write "the Involuntary
  Resettlement Policy (OP/BP 4.11)". The card is right and the document is wrong.
- Every rating on every card was read out of the completion report's own rating page and matches it;
  every review rating quoted matches the review. No rating was taken from the other document's
  column.

**5. Routes that failed.** None, in this check. All 32 source URLs returned 200 over
`documents1.worldbank.org`, `apublica.org` and `groundup.news/article-print/...`, the last being the
route the writer reported as the working one. The live query
`search.worldbank.org/api/v2/projects?id=P149556` answered and settled disagreement 13. No
permission prompt was raised and no host refused anything.

Nothing was merged, `build.py` was not run, git was not touched.
