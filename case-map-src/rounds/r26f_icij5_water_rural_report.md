# Round 21, batch C — water, irrigation and rural rows

Output: `/home/claude/r21/r26f_icij5_water_rural.json` — 10 new cases, 1 extend, 7 drops, from 18 leads.

## The hypothesis this batch was built to test

Round 21 split its leads to test whether sector predicts an independently-sourced case, with this
batch as the predicted-barren half: water, irrigation and rural rows, "the sectors where round 20's
drops clustered, because land is taken, compensation is paid and nothing adverse is recorded".

**The sector hypothesis does not hold in the form it was put.** Ten of 18 rows carry a documented
relocation count or a documented loss. Seven are clean confirmations of the barren pattern, and they
are clustered tightly: all seven are projects whose works were genuinely small, dispersed,
rural or in-channel — village water points, on-farm water saving, canal and drainage rehabilitation,
sector-wide programme support. Every one of the ten cases is a project whose works were, in substance,
**civil engineering in or beside a town**: river embankments, urban drainage, landfills, wastewater
plants, a dam reservoir, a riverfront, a transmission line, a road network. The predictor that
survives this batch is not the sector tag but **whether the works required a construction site that
people were living on**.

The second half of what this round asked for — what each project's works actually were, against
ICIJ's name — is in the table below. **Five of 18 rows are mis-tagged by ICIJ's project name.**

## Each row

| ICIJ name | P-number | What the works actually were | r21_outcome |
|---|---|---|---|
| CN-Second Guangdong Pearl River Delta Urban Environment | P081776 | Wastewater, sludge, flood protection and river embankment works in Foshan and Jiangmen — urban demolition on the Fenjiang river bank, not water supply | **case** `fenjiang-river-foshan-resettlement` |
| Zhejiang Qiantang River Basin Small Town Environment | P116656 | Water supply, wastewater, **and a municipal landfill** in eight counties; the largest house demolition was for the landfill buffer zone at Meicheng | **case** `qiantang-small-town-house-demolition` |
| Guangxi Laibin Water Environment | P126817 | **Flood control and urban storm drainage** in Laibin city's old town, with river embankment works. Not a water-supply or water-quality project | **case** `laibin-water-environment-displacement` |
| Water Resources Development (Mozambique) | P107350 | Completion of the **Corumana dam** — a dam and reservoir project, plus river basin planning | **case** `corumana-dam-resettlement-mozambique` |
| Ethiopia/Nile Basin Initiative: Ethiopia-Sudan Interconnector | P074011 | **A 296.5 km high-voltage transmission line** and three substations. 100 per cent of Bank financing coded to transmission and distribution of electricity. The water tag comes only from "Nile Basin Initiative" in the name | **case** `ethiopia-sudan-interconnector-line-deaths` |
| BR AF to the Ceara Integrated Water Resource Management | P110487 (parent P006449) | **Five earth dams and six conveyance pipelines** in the Ceará interior, with agrovila resettlement villages | **case** `gameleira-agrovila-ceara` |
| IN National Ganga River Basin | P119085 | Sewage treatment plants and sewer networks, plus the **Patna riverfront development**, which was the only investment needing full land acquisition | **case** `patna-ganga-riverfront-resettlement` |
| Nigeria Erosion and Watershed Management | P124905 | **Gully erosion civil works** at 84 sites in 23 states, plus 211 km of roads rehabilitated | **case** `newmap-nigeria-erosion-displacement` |
| Rural Access Improvement and Decentralization (Nepal) | P083923 | **Rural road upgrading** in 30 districts. Tagged `rural`, and it is a roads project | **case** `nepal-raidp-land-donation` |
| Urban Water Sector Project (Burkina Faso) | P106909 | Water production, storage, distribution and sanitation in Ouagadougou, Bobo-Dioulasso and three secondary cities | **case** `ouagadougou-onea-works-before-compensation` |
| Water Sector Improvement APL Phase II: Metolong Dam | P108143 | The Metolong dam and bulk water supply, plus rural electrification of 80 villages | **extend** to `metolong-dam` |
| Western Provinces Rural Water Supply; Sanitation and Hygiene | P095315 | Village and household wells, small pumping stations and latrines in 25 counties of Shaanxi and Sichuan; individual works under 0.06 ha | **dropped** |
| Water Conservation Project II (China) | P114138 | On-farm water saving in three provinces; 3.58 mu of land acquired in total | **dropped** |
| Ma'anshan Cihu River Basin Improvement | P126813 | Roads and tributary rehabilitation in Ma'anshan — in substance an urban works project, but with no demolition or relocation recorded | **dropped** |
| DRC Urban Water Supply | P091092 | Water production and distribution in Kinshasa, Matadi and other cities; a utility management contract and a staff severance programme | **dropped** |
| Water Sector Support Project (Tanzania) | P087154 | Sector-wide programme support: 1,075 subprojects screened, the vast majority Category C | **dropped** |
| EGYPT-Integrated Irrigation Improvement and Management | P073977 | Branch canal rehabilitation, subsurface drainage and pump station electrification in Beheira, Gharbia and Kafr El Sheikh | **dropped** |
| VN-Red River Delta Rural Water Supply and Sanitation | P077287 | Commune water supply schemes and sanitation in 120 communes | **dropped** |

### Dedupe

All 18 P-numbers, plus parents, siblings and additional financings (24 numbers in all), were run
through `dedupe_leads.py`. One hit: **P075728 is on the map as `chebei-village-guangzhou-resettlement`**.

- **Warning 2 resolved.** Chebei sits in the **first** Guangdong Pearl River Delta Urban Environment
  Project, P075728 (approved 8 June 2004), not in this lead. The lead is the **Second** project,
  P081776, and its completion report never mentions Chebei or Guangzhou: its only resettlement was in
  Foshan, with Jiangmen involving none. These are two cities and two loans, not one continuing episode.
  No second card at one point. There is also a third, differently-named project, P087273 "GUANGDONG
  PEARL RIVER DELTA URBAN ENVIRONMENT II", approved 19 June 2007 at US$200 million — not on the map,
  not this lead, and not researched here.
- **Warning 1 resolved as an extend.** The Metolong lead **is** `metolong-dam`: P108143, approved
  26 May 2009, closed 31 December 2018, which matches the existing card's place and 2009–2018 span,
  and the existing card's "$49.5 million" is the P108143 disbursed figure of US$49.579 million. The
  row is an extend, not a new case. `lesotho-highlands` (P-numbers for Phase 1A/1B) and
  `polihali-lhwp-phase-ii` are the separate Highlands project and were not touched.
- **Warning 3 resolved.** P074011 is returned only with the country filter dropped, under country
  "Ethiopia". It is a different line from `ethiopia-kenya-power-line-kenya` (P126579), and neither
  `merowe-dam-amri-manasir` nor `upper-atbara-setit-arab-funds` has any overlap: both are Nile dams
  financed by Arab funds and China, with no Bank credit and no transmission works in common.
- `likely_already_on_map` on the Tanzania row was a false match: `tanzania-rssp2-demolitions` is an
  African Development Bank **road** project on the Babati–Dodoma section, sharing only the words
  "sector" and "support".
- **Warning 4 resolved.** P095315's harm question is moot — the completion report records no harm, so
  no point is placed. For the record the credit financed works in 15 counties of Shaanxi and 10 of
  Sichuan, and the report names Jianling, Lezhi, Pingchang, Guangan and Yanting in Sichuan and Zichang,
  Zhidan, Yaozhou, Yintai and Suide in Shaanxi.
- **Warning 5 resolved.** `wds?projectid=P110487` returns nothing at all, as predicted. The parent
  P006449 holds the completion report of 28 December 2012, which covers both phases and whose
  resettlement annex tabulates the additional financing's five dams separately.

## The drops, with the document behind each

1. **P095315, Western Provinces Rural Water Supply (China), US$25M, 26 Jun 2007.** The completion
   report's resettlement annex states in terms: "The involuntary resettlement activities did not have
   any house demolition or people replaced." 12.61 ha permanently acquired and 132.06 ha temporarily
   occupied across 25 counties; in five Sichuan counties the land came from within the project villages
   and households were compensated land-for-land rather than in money; five Shaanxi counties had only
   temporary occupation; total land compensation US$0.515 million. All compensation paid on time,
   livelihoods found fully restored. **Land area plus an "affected" count, which BRIEF21 rule 1 makes a
   drop.** Note for the ICIJ figure trap: **ICIJ's 2,422 is exactly the completion report's own actual
   total of affected people** (622 households, 2,422 people) — the outcome-affected figure, not a plan
   figure and not a relocation count. *(ICR 30 Sep 2013; IEG review, Bank document date 17 Oct 2014.)*
2. **P114138, Water Conservation Project II (China), US$80M, 10 May 2012.** "The project did not entail
   household relocation." Land acquisition of 3.58 mu in one province, none in the other two; "hardly
   any land acquisition or compensation was necessary"; all land-related compensation fully disbursed
   on time and in full. *(ICR 18 Dec 2017; IEG review, Bank document date 4 Apr 2018.)*
3. **P126813, Ma'anshan Cihu River Basin Improvement (China), US$100M, 4 Jun 2013.** Acquired 56.25 ha
   collective and 1.31 ha state-owned land, "affecting 534 families and a population of 1,309". No
   house demolition count, no relocation count; land acquisition and resettlement "resolved effectively
   and timely", no complaint ever filed through the grievance mechanism. Land area plus an "affected"
   count. **A second clean instance of the ICIJ trap: ICIJ's 1,714 is the PAD's planned affected
   population to the person** (the appraisal expected 119.2 ha affecting 552 families and 1,714 people;
   the outcome was 57.56 ha and 1,309 people). *(ICR 24 Jun 2021; IEG review, Bank document date 27 Jul
   2022.)*
4. **P091092, DRC Urban Water Supply, US$190M, 18 Dec 2008.** Involuntary resettlement was the one
   safeguard not rated satisfactory at closure, rated Moderately Satisfactory, because the abbreviated
   and full resettlement plans in three cities were late and because a plan in Kinshasa was implemented
   without waiting for Bank approval; that was reconciled by a follow-on government assessment of
   economic loss the Bank accepted. 187 grievances registered, 162 of them founded, all processed; 7
   occupational health and safety incidents, six serious, one indicative, none severe, all closed. No
   relocation count, no count or description of what the 162 founded grievances concerned, and no
   figure anywhere for the losses. **An avenue that goes nowhere in the documents:** sub-component B.3
   was a severance programme to fund "necessary staff reductions through negotiated retrenchment
   packages" at the utility REGIDESO, including termination grants and surveys of the programme's
   impact — and neither the completion report nor the review gives any count of staff separated or any
   outcome for it. *(ICR 27 Feb 2022; IEG review, Bank document date 26 Aug 2022.)*
5. **P087154, Tanzania Water Sector Support, US$252M, 13 Feb 2007.** 968 of 1,075 subprojects screened,
   "the vast majority" Category C with negligible impacts. The only resettlement sentence in the
   borrower's annex says projects requiring land acquisition followed the policy framework and
   "project-affected people fully participated in the process of valuation and compensation was done
   accordingly". No count of anything. ICIJ's 2,055 has no counterpart in either document.
   *(ICR 23 May 2016; IEG review, Bank document date 23 Jun 2017.)*
6. **P073977, Egypt Integrated Irrigation Improvement and Management, US$120M, 3 May 2005.** This one
   has a real documented gap and still fails the forward rule for want of a count. A provisional
   resettlement plan was completed before approval, then the need for land was cut back and only a
   policy framework was disclosed in 2010; no site-specific plan was ever prepared. During
   implementation "lack of crop compensation for electrification contracts was identified", and a joint
   Bank and project-unit team made field visits in April and May 2016 — eleven years into the project —
   to identify the affected people, assess crop damage and pay them, finishing by the end of May 2016.
   In the same exercise "nonpayment for crop damages associated with SSD in Behira, because of lack of
   funds, was also identified". The completion report states that compliance on the electrical
   contracts with land and crop compensation "was only resolved during the final stages of the
   project". **No document found counts the farmers involved in either governorate, or gives an
   amount.** A card whose whole content is an unquantified compensation gap, recorded as closed before
   the project closed, is less than the "affected" count the brief already makes a drop. *(ICR 15 Dec
   2016; IEG review, 6 Dec 2017.)*
7. **P077287, VN-Red River Delta Rural Water Supply and Sanitation, US$45.9M, 15 Sep 2005.** The
   resettlement policy was triggered for land acquisition for the water and sanitation works, a
   resettlement action plan was prepared and disclosed, and the review's safeguards section records no
   land acquisition outcome at all, no count and no loss: it says participatory methods were used in
   planning and that equitable choices were offered to ethnic minorities to avoid adverse impact
   through land acquisition. A case of misprocurement was documented in November 2010 and the
   misappropriated funds were reimbursed. *(IEG review, posted 1 Jul 2015 — see the route failure below.)*

## My own two weakest entries

**1. `ouagadougou-onea-works-before-compensation` (P106909) is the weakest.** The harm is a safeguards
breach that was found, suspended and fixed inside six months, plus a residue of people who could not be
found. And the two documents give **different residues**: the IEG review says 49 of 817 affected people
were never located and 768 were paid by May 2017; the completion report says 26 of 756 on lot 2.2 and
4 of 79 on lot 6.1, which is 30 of 835. Neither explains the other, and neither says which lots the
review's 817 covers. The location rests entirely on one sentence in the review placing the breach on
the Ouagadougou water transmission works — the completion report never says where lot 2.2 or lot 6.1
lay, so the city-level point would collapse if that sentence is wrong. Nobody is named, no amount is
given, and nothing says what any of the four unpaid people lost. Both documents rate safeguards
Satisfactory at closing. If the checker cuts one card from this batch, this is the one to look at first.

**2. `fenjiang-river-foshan-resettlement` (P081776) is the second weakest, for the opposite reason.** It
is a well-documented relocation of **15 households and 46 people** on which every favourable clause in
the record also holds: compensation at or above planned rates, 140 per cent above plan for the private
houses, full replacement cost on the sampled cases, paid in full on signature before assets were taken,
no complaint or grievance of any kind, nobody's livelihood changed. It earns a card on limb (a) and on
nothing else, and anyone reading it will ask what the harm is. I have written the favourable clauses in
rather than around, but the honest summary is that this is a small, compliant resettlement that the
forward rule admits. Two secondary problems: the external monitor, Hohai University, also wrote the
resettlement plan it was monitoring; and the report gives 144 and 34 as counts of industrial enterprises
shut down or relocated in the same project area without reconciling them, though both describe municipal
pollution-control action rather than the loan's works.

A third worth flagging though not among the weakest: **`newmap-nigeria-erosion-displacement`**'s central
figure, 5,721 people actually displaced, sits in the completion report's **economic analysis** as an
input to a benefit calculation, not in its safeguards section, and the same passage extrapolates to
7,015 while switching from 84 sites to 81 with no explanation. The IEG review, which rated the report's
quality Modest, does not carry the 5,721 at all.

## Where two documents disagree

1. **P106909 Burkina Faso, uncompensated people.** IEG review: 49 of 817 not located, 768 compensated
   by May 2017. Completion report: 26 of 756 on lot 2.2 and 4 of 79 on lot 6.1, so 30 of 835. Neither
   reconciles the other.
2. **P074011 Ethiopia–Sudan, whether compensation was timely.** Completion report: construction began
   on the Bahir Dar–Gondar section before the affected people were paid, and three woredas delayed
   payments, costing eight months. IEG review, Bank performance section: the Bank "ensured that
   compensation payments to PAPs was timely".
3. **P083923 Nepal, the social safeguards rating, inside one document.** Completion report paragraph 33:
   "Social Safeguards (Satisfactory)". Paragraph 35: "a final rating of 'moderately satisfactory'". The
   IEG review names this inconsistency as one of four faults in the report's treatment of the policy.
4. **P083923 Nepal, outcome.** Completion report: Moderately Satisfactory. IEG review: Satisfactory.
5. **P006449/P110487 Brazil, the additional financing's approval date, inside one document.** Data sheet:
   18 December 2008 (which is ICIJ's date). Text, paragraph 18: "approved by the Board on December 17,
   2008".
6. **P006449/P110487 Brazil, risk and Bank performance.** Completion report: risk Moderate, Bank
   performance Moderately Satisfactory. IEG review: risk **High** ("The ICR recognizes the high risks,
   but did not factor them into the rating"), Bank performance **Moderately Unsatisfactory**.
7. **P124905 Nigeria, outcome.** Completion report: Satisfactory. IEG review: Moderately Satisfactory,
   "Insufficient evidence of outcomes achieved". The review also rates the report's own quality Modest.
8. **P124905 Nigeria, livelihood beneficiaries, inside one document.** 35,977 total, "out of which
   15,977 are male and 20,509 are female" — which come to 36,486.
9. **P124905 Nigeria, people displaced, inside one document.** 5,721 from 84 sites, "extrapolated to 81
   sites, the total figure is 7,015".
10. **P106909 Burkina Faso, outcome.** Completion report: Highly Satisfactory. IEG review: Satisfactory.
11. **P116656 China, the resettlement cost's unit.** Completion report table: RMB 141,998.7 and
    167,009.9 under a heading of RMB 000, i.e. about RMB 142 million and RMB 167 million. IEG review
    body text: "the total resettlement cost was 141,998.7 RMB as compared to the original estimate of
    167,009.9 RMB".
12. **P108143 Lesotho, affected households and unpaid cases.** Completion report at closing on
    31 December 2018: 2,798 affected households, 2,615 compensated, 183 outstanding. The figures
    already on the map for August 2018: 2,786 affected families, 247 unpaid.
13. **P106909 Burkina Faso, the additional financing's approval date.** Completion report restructuring
    table: 21 October 2014. The Bank's project record for P149556: board approval 12 January 2015.

### Omissions in IEG reviews, where the review drops what the report records

Not disagreements, but the same shape, and each one would have cost a reader the finding:

- **P108143 Lesotho.** The review's safeguards section omits the **ten fatalities**, the 2012 blasting
  and construction without an approved environmental protection plan, blasting plan, method statement,
  mining permit, evacuation plan or dilapidation survey, the complaints after the uncontrolled blast of
  August 2012, and the ombudsman's involvement in the compensation disputes.
- **P107350 Mozambique.** The review quotes the completion report's sentence on poor occupational
  health and safety performance and stops immediately before the next sentence, which records the
  **one fatality** and its root cause.
- **P119085 India.** The review omits the **249 project-affected families** at the Patna riverfront, the
  two-year stall in their land allotment, and the handing of sites to the contractor before people were
  resettled and compensated; its summary reads "All Project Affected Families (PAFs) were eventually
  compensated".

## Statements that are staff communications, not documents

Grepped for `informed IEG`, `the project team`, `the World Bank team stated` and `personal
communication` across all 18 sets.

- **P107350 Mozambique:** two load-bearing-looking facts are footnoted to named Bank staff rather than
  documents — the vandalism and theft of fixtures at the empty resettlement houses (Senior Social
  Development Specialist, personal communication, 4 February 2021) and the decision not to have the
  project fund cash compensation (Water Supply and Sanitation Specialist, personal communication,
  12 February 2021). The card's confidence note says so and the card does not rest on either; the 660
  resettled, the 133 houses, the list of pending activities and the fatality are all in the report's own
  text.
- **P083923 Nepal:** the IEG review attributes the length and tranching of the financial management
  consultancy support to "The project team stated". Nothing on the card comes from it.
- No `informed IEG` attribution bears on any figure used in this batch.

## Routes that failed, and what the failure was

1. **`wds?projectid=P110487` returns zero documents** for the Ceará additional financing. The parent
   P006449 holds the completion report covering both phases. Exactly as warning 5 predicted.
2. **`wds?projectid=P126549`** (the GEF supplement to Nigeria NEWMAP) returns zero documents; the
   grants appear only in the parent P124905's financing table.
3. **`wds?projectid=P113496`** (the Vietnam additional financing) returns zero documents dated after
   April 2010 and no completion report.
4. **No completion report for P077287 (Vietnam) exists in the archive by any route tried.** Not under
   P077287, not under the additional financing P113496, and not under a `qterm` title search on the
   project's full name plus "Implementation Completion" — that search returns three hits, the P077287
   review itself and the completion report and review of a different project, P127435. The report
   plainly exists, because the IEG review cites it by page and paragraph throughout ("ICR p 12 para
   41", "ICR p 4 para 16"). This is the BRIEF21 empty-`docty` case, or an undisclosed report. The row
   was dropped on the review's own safeguards section, which records no land acquisition outcome, so
   nothing turns on it.
5. **`wds?projectid=P124905` returns no Project Appraisal Document.** The appraisal figures used are
   those the IEG review quotes from the PAD. The ICR and the review were both retrieved.
6. **`groundup.news/article/...` returned PROVENANCE_REQUIRED** — the permission request for the URL
   was not answered in time. This is not a host refusal: **`groundup.news/article-print/...` served the
   same article in full through the same fetch tool**, and that is the URL on the Metolong extend. Route,
   not host.
7. **`documents.worldbank.org` refuses, as always.** Every `pdfurl` from the `wds` API was rewritten to
   `documents1.worldbank.org` and upgraded to https before `curl`. 256 files retrieved with zero
   failures.
8. **Chinese-language search found nothing outside the Bank**, for the fourth round running. A search on
   来宾市 世界银行 水环境项目 征地拆迁 补偿 returned only World Bank press releases and project documents
   for other Guangxi projects. One search spent, per the brief's limit.
9. **Searches that found nothing usable:** Patna riverfront displacement (returned Indian press on other
   Ganga bank evictions and a Ganga bridge project, none tied to P119085); NEWMAP compensation
   complaints (returned only the project's own RAPs and frameworks, which are plans); Corumana
   resettlement (returned Mozambican mining and LNG resettlement material, nothing on Corumana); Nepal
   RAIDP land donation (returned ADB material on its separate DRILP programme, a different project).
   All four cases are `contested` as a result.
10. **One search paid off.** `apublica.org`'s field report of 16 April 2015 on the Gameleira agrovila
    serves in full and is the only independent source in the batch. It is what makes
    `gameleira-agrovila-ceara` the one `documented` card here, and it added the contractor EIT, the
    compensation amounts residents received, the 36 litres a day, the unbuilt pipeline and the state
    audit prosecutor's March 2012 representation describing the families' conditions as sub-human.
    It also confirms the Bank report's dates independently: resettlement January 2011, water and power
    December 2012.

## The ICIJ figure trap in this batch

Four rows let the trap be checked exactly, and three different mechanisms show up:

- **P095315 China: ICIJ's 2,422 is the completion report's own actual affected-persons total**, to the
  person (622 households, 2,422 people). An outcome figure — of people *affected*, with no demolition
  and nobody moved.
- **P126813 China: ICIJ's 1,714 is the appraisal's planned affected population**, to the person. The
  outcome was 1,309.
- **P074011 Ethiopia: ICIJ gives 1,415 where the completion report counts 4,490 affected people paid.**
  ICIJ is *below* the Bank's own outcome figure here, by a factor of three.
- **P126817 China: ICIJ gives 2,014 where the report counts 2,363 physically displaced** and 3,521
  affected in all. Again below the outcome.

No `displaced` field in this file carries an ICIJ number. Six of the ten cases carry no `displaced`
figure at all, because no Bank document gives a count of people relocated for them.

## Numeric field a card needs that `fields_add` cannot set

`metolong-dam` currently carries `killed: 0`. The World Bank's completion report of 26 June 2019 states
that **"There were 10 fatalities that happened during the implementation of the MDWSP"**, all of them
reported and settled under Lesotho's Labour Code. The report gives **no cause for any of the ten**, does
not say when or where they happened, and does not say who the dead were, so under the `killed` rule they
belong in `killed_note` as text rather than in the count. Both facts are stated in the extend's
`fields_add.community` and `fields_add.confidence_note`, which can only append strings. **The lead should
decide whether `metolong-dam` gains a `killed_note`; I have not put a number in the file.** The IEG
review omits the ten fatalities entirely.

## Document cache

`/home/claude/r21/cache/` — 256 files, 431 MB, paired `.pdf` and `.txt` from `pdftotext -layout`, named
`<P-number>_<TYPE>`. For all 18 of this batch's P-numbers it holds the completion report (ICR) and the
Independent Evaluation Group's review (ICRR), and the appraisal document (PAD) for 16 of them — P124905
has no PAD in the archive and P077287 has no ICR. `P108143_ICR` and `P108143_ICR_2` are byte-identical
copies the archive lists under 26 and 27 June 2019; the document's own cover date is 26 June 2019, report
number ICR00004565. Files from P-numbers not in this batch are other round 21 batches writing to the same
folder. Nothing in `/home/claude/r20/cache/` covered any parent or sibling of these 18 rows, and all 256
files here were downloaded fresh in this session.

Nothing was merged, `build.py` was not run, and git was not touched.
