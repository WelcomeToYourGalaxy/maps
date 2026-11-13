# Check log — round 20, batch A (ICIJ tranche 4, China urban and environment)

Checked file: `/home/claude/r20/r26f_icij4_china_urban_checked.json` — 11 keys, 9 kept, 2 dropped.
Every figure below was read out of the cached document with `grep` and `sed` on
`/home/claude/r20/cache/*.txt`; the two UNESCO pages were read with a fetch tool.
Nothing was merged, `build.py` was not run, git was not touched.

## 1. The two cuts

### `jiangsu-water-wastewater-resettlement` (P096926) — dropped
The writer named this as the one to cut first and it is a cut. The whole resettlement outcome is
paragraph 35 of the completion report, which I read in full (lines 960–1000 of the text layer):
"494 PAPs were properly resettled and/or compensated; … A total of 59 ha of land was acquired, and
1,043 ha of land was temporarily occupied during construction." Confirmed verbatim. Nothing else in
the document bears on the outcome.

- **Limb (a) fails.** "Resettled and/or compensated" is not a count of people relocated. There is no
  household figure, no demolition figure and no per-city figure anywhere in the outcome record.
- **Limb (b) fails.** The land take is the only harm left. It carries no identifiable people: no
  village, no site, no compensation rate, no count of anyone who lost a house, and the report records
  the whole thing as compliant — reduction of resettlement was a design criterion, public facilities
  were restored to high standards, grievance mechanisms were publicised, compliance satisfactory,
  "LA and resettlement generally proceeded smoothly". The appraisal plan for demolishing 117
  households' houses is a plan.

Verified en route and recorded for the drop: PAD figures (34 ha permanent of which 25 ha collective
from which 1,053 people derived part of their income; 350 ha temporary; 117 households / 417 people;
104 of those households and 355 of those people in Nanjing) all confirmed; ICR ratings Highly
Satisfactory, risk **Low** (data sheet line 191); IEG review lowered outcome to Satisfactory for lack
of evidence on wastewater treatment efficiency and raised risk to **Modest** over the Nanjing-Longtan
raw water intake 1.2 km downstream of a small oil wharf (review lines 440–441, 794–804) — all
confirmed, including the label substitution (see §5).

### `tai-basin-urban-environment-resettlement` (P057933) — dropped, on a document the card did not read to the end
This one the writer called honest but unexciting. It is worse than that: the card's one piece of
physical harm does not exist.

- Annex 4, Table 1 puts **all** of the project's 5,050.42 m² of "house demolition" in a single Suzhou
  sub-component (incoming wastewater control); both Wuxi rows and the other two Suzhou rows record no
  demolition at all.
- Annex 4 ¶11, on that same sub-component: "the area of house demolitions declined by 4,650 m2.
  Moreover, **no residential houses were involved**, and the number of demolished enterprises was
  reduced from eight to two." The card quoted the second half of that sentence and dropped the first
  half. That is the selective-quotation shape, in the usual direction, and it is what decided the cut.
- Limb (a) also fails, in both directions at once. ¶28 says "The total number of persons resettled
  under the project was 420", but Annex 4 Table 1 heads the identical figure "Affected people
  (# Persons)", and the breakdown (129 affected in Wuxi and 196 in Suzhou watercourse dredging, both
  with zero demolition) shows the 420 cannot be people physically relocated. The writer was right not
  to put 420 in `displaced`; it was wrong to describe the 5,050 m² as housing lost.
- What is left is 30.97 ha permanently acquired (against 25.34 planned) and 515.51 ha temporarily
  occupied, from people the report records as compensated above the plan standard, paid on schedule
  at the end of each year, moved to urban residence with rural social security and the local basic
  living safeguard, with employment over 96 per cent and average annual income up from RMB 5,860 in
  2002 to RMB 16,000 in 2010 (¶28; Annex 4 ¶¶7–16). Those last two figures were not on the card
  either.

Everything else on the card checked out exactly (24.14 / 17.65, 6.83 / 7.69, 467.58, 47.93, 129, 95,
196, 291, 420 / 409, three against eight, loan cut US$61.0M → US$57.5M, IEG Bank performance
Unsatisfactory against the report's Moderately satisfactory, review Date Posted 01/09/2013). The
figures were right; the harm was not there.

## 2. The three the writer called thin — two kept, one cut

The cut is Tai Basin, above. For the other two I applied one line and applied it the same way: where a
document records **housing actually demolished**, homes were lost and limb (b) is met even without a
household count; where the only outcome is land area and a count of people "affected", it is not.

- **`second-shandong-environment-resettlement` (P077752) — kept.** 94,750.8 m² of house demolition
  against 131,799 planned, in a table whose separate column counts enterprise, institution and shop
  space (16,090.8 m² against 10,387.7), so the house column is residential; the appraisal planned the
  demolition of the residences of 606 urban and 120 rural households (726 in all, 2,669 people), and
  the ICR speaks of the vulnerable groups' standard of living "after land acquisition and housing
  demolition". Homes went. Every figure on the card confirmed against Annex 6 Table 1 and PAD ¶41:
  1,331.3 / 1,214 mu, 1,620.9 / 1,901.9, 4,220 / 4,718, Zaozhuang 753.4 mu / 77,056.7 m² / 3,548
  people / RMB 238.24M, Weifang 17,694.1 m² and 113, Heze 271, Gaomi 108, Qixia 121, Yantai 59,
  Huantai 177 mu and 83 people out in 2010, total compensation RMB 272.68M against 147.49M, 23 people
  in 9 households vulnerable, 4,801 across about 32 villages in 19 townships or districts, 315 /
  1,023, 606 / 2,282, 120 / 387, 28 / 719 including 598 floating, six institutions / 63, 42 shops /
  147, 734 temporary. The text-against-table conflict (4,200 against 4,220) is real and is on the card.
- **`liuzhou-environment-management-resettlement` (P081346) — kept.** 52,818 m² of housing demolished
  against 66,120 planned, with a separate enterprise count, and the project's own external monitor
  describing the same households' housing "before resettlement" and "after resettlement" changing from
  timber-brick to cement-brick with gas, telephone and sewerage installed. Homes went. Every number on
  the card confirmed line for line against the Annex 3 table, including all four components, both
  compensation footnotes, the cancelled 42 collection stations and the RMB 12,900 / 13,330 sample
  income figures.

## 3. `qufu-gupan-pond-demolition` — every element verified

| Claim | Source read | Result |
|---|---|---|
| 588 houses in the 13-ha area demolished in 44 days, except five designated historic buildings | ICR p.26 (text lines 1455–1457) | confirmed verbatim |
| Neither SACH, nor the World Bank, nor UNESCO was informed about the planned demolition | same paragraph | confirmed verbatim |
| Non-compliance found when the local implementation unit resettled residents without an approved resettlement plan | ICR Annex 7, Lessons Learned | confirmed verbatim |
| One major incident of non-compliance with OP/BP 4.12 | ICR safeguards section ¶ (line 1609) | confirmed |
| 38 COM 7B.11 (2014) | ICR line 1459 **and** UNESCO soc/2812 | confirmed; decision text read — clause 2 takes note of the redevelopment in the buffer zone, clause 3 "Expresses its concern about the potential impacts that this project may have on the attributes that sustain the Outstanding Universal Value (OUV) of the property, including its authenticity and integrity", clause 5 requests the ICOMOS mission |
| World Heritage Centre letter 9 December 2013; China's state of conservation report 28 March 2014; "partly funded by the World Bank"; 13.34 ha; "A total of 588 households have been moved since the first half of 2013" | UNESCO soc/2812 | all confirmed |
| ICOMOS reactive monitoring mission 9–12 December 2014 | UNESCO soc/3407 | confirmed |
| 40 COM 7B.32 (2016): 13.34 ha held 588 households, most built after the 1970s, a third dilapidated, five buildings saved | UNESCO soc/3407 | confirmed |
| No construction followed the demolition | UNESCO soc/3407: "No construction has been carried out following demolition" | confirmed |
| 790 households resettled, 588 Qufu and 202 Zoucheng, 3,612 people; 204 shops, 1,014 people; 86,300 m² against 40,524; 206.5 mu against 94.3; 346/1,211 and 342/1,198 planned; Zoucheng 33,274.86 and 2,051.88 m², 190/760 and 12/52; unlicensed 194/692 and 78/213; RMB 492.63M and 178.83M | ICR Annex 7 summary and Table 2 | all confirmed |
| Loan, dates, restructurings, ratings, ISR downgrades of 20 Mar 2015 and 20 Nov 2015 | ICR data sheet and ICRR | all confirmed; ICRR gives the same three ratings with "---" in every disagreement row |
| "some challenges" | ICRR line 698 | confirmed verbatim |
| Further contract for external monitoring of resettlement in Qufu added at restructuring | ICR line 590 | confirmed |

Both limits are on the card and are correctly stated: the 588 is the State Party's own figure in its
report to UNESCO, not a UNESCO finding, and the Committee's concern is the property's Outstanding
Universal Value, not the people moved.

**The 588 against 251.** Not reconciled, and I have not reconciled it. ICR p.29/Annex 7 Table 1 and
Table 2 give 588 households (and 588 as the figure for both the permanent occupation row and the urban
residential demolition row, with the note "The same 588 households"); the Lessons Learned section two
pages later says "Since the start of resettlement at Gupan Lake where the 251 households originally
lived, house value of the area has risen…". No document in the cache, and nothing on either UNESCO
page, explains the difference. The card states both figures and says no document explains it. Correct
handling; left as it is.

**One correction made.** The card had the lack of construction "damag[ing] the local government's
public credibility". UNESCO's 2016 report attributes the negative impact on public credibility to the
**suspension of the reconstruction project**, not to the demolition or the empty ground. Reworded.

Confidence left at `documented`. The independent element is real and outside the lender: the World
Heritage Centre's own correspondence, two Committee decisions and an ICOMOS field mission. A stricter
reading is available — the people figure exists only in the Bank's report and in China's report to
UNESCO, and the Committee was looking at the property — and the card already says exactly that.

## 4. The three staff statements

I ran `informed IEG`, `the project team`, `the World Bank team stated`, `team informed`, `provided
IEG` and `email to IEG` over all twelve reviews myself. Results:

- **Sichuan P110632**, review lines 511–525: "The project team informed IEG (email, October 29, 2017)
  that as of September 2017…" followed by the five county-by-county dates. Confirmed verbatim,
  including the detail that the review's Jialing date for the 14 households is **October 2017** while
  the report's own Annex 8 says May 2017. The card attributes the whole post-closing position to the
  email, in both `outcome` and `confidence_note`, and names no document for it. Correct.
  **Which limb survives without the email: both, and the harm with them.** The 348 households not
  resettled at closing, the county split 148/54/80/66, the 114 still not resettled at the completion
  mission of end-March 2017, the 58 in Zizhong scheduled to June 2018 and the 38 in Jialing to
  December 2018, and the 25 Jialing households who signed a willingness letter in December 2016 to
  wait until the end of 2018 are all in the completion report itself (¶¶29, 46–48 and Annex 8
  ¶¶9–13). The email adds only what happened after September 2017. Also at review line 430, an email
  of 28 September 2017 on the water and wastewater sub-components — not used by the card, correctly.
- **Liaoning Coastal P126611**, review lines 897–898: "548 households were physically resettled and
  received appropriate compensation **in a timely manner as confirmed by the Task Team in its June 3,
  2020 email to IEG**." Confirmed verbatim. The three figures themselves (760.6 mu, 1,843 persons /
  492 households, 548 physically resettled) are in the completion report ¶84, so only the timeliness
  rests on the email, which is what the card says.
- **Liuzhou P081346**, review lines 371, 467 and 561–562: confirmation of compliance with the
  environmental safeguard "was provided subsequently by the project team", and IEG's criticism that
  the ICR should have discussed category A environmental compliance more fully. Confirmed, and the
  card uses neither. Also line 269 (least-cost confirmation) and line 493 (six external audits) — not
  used.
- Nothing else in any card rests on a staff statement. Shanghai APL2's review carries two (financial
  data for four subprojects, and additional information of 18 August 2016 on studies and training) and
  P092618's review one (a dropped non-revenue-water indicator); none is used.

## 5. The label substitutions and the wrong column

Each read out of the completion report's own text, not out of the review's column:

| Project | Report's own word, and where | Review's column for the report | Verdict |
|---|---|---|---|
| Sichuan P110632 | **Moderate**, data sheet line 210 | Modest | substitution confirmed |
| Han River P087224 | **Moderate**, data sheet line 226 | Modest | confirmed |
| Nanning P108627 | **Moderate**, data sheet line 177 | Modest | confirmed |
| Shanghai APL2 P075732 | **Moderate**, data sheet line 204 and §4 line 1541 | Modest | confirmed |
| Jiangsu P096926 | **Low**, data sheet line 191 | Negligible | confirmed |
| Shandong 2 P077752 | **Low or Negligible**, data sheet line 212; §4 rating "Low" | Negligible to Low | confirmed |
| Liuzhou P081346 | **Low or Negligible**, C.1 line 165; §4 rating "Negligible" | Negligible to Low | confirmed |
| Liuzhou P081346 Bank performance | **Satisfactory**, C.1 line 166 and §5.1(c) line 1240 | **Moderately Satisfactory** | confirmed — the review's column is simply wrong, and the card gives the report's own value as the report's rating and names both |

Two notes for the record. The Liuzhou report is internally inconsistent on risk in a way the card does
not mention: C.1 says "Low or Negligible" and §4 says "Negligible". The Shandong 2 report has the same
shape (C.1 "Low or Negligible", §4 "Low"). Neither affects a card claim.
Rating **disagreements** between the two bodies were also checked case by case and all are as the
writer reported, with the right document attached to each: Nanning MS→MU on outcome, Bank and borrower
with the delayed restructuring named as the reason; Shanghai MS→MU on all three and risk
Moderate→Substantial; Jiangsu HS→S; Tai Basin Bank performance Moderately satisfactory→Unsatisfactory;
Liuzhou S→MS on outcome with efficiency rated modest "because of lack of information and analysis";
Han River risk→Substantial on institutional sustainability; Xiangyang outcome MS→**Satisfactory**
upward and M&E Modest→Substantial; Qufu and Sichuan no disagreement at all.

## 6. The two duplicate findings — both spot-checked against the map itself

- **Liaoning.** Read the existing card out of `case-map-src/base.html`:
  `liaoning-medium-cities-resettlement` is **P099992**, IBRD-48310, US$218M, approved 27 June 2006,
  2006–2013, placed at 41.2733 / 123.1773, in "Liaoyang, Panjin, Jinzhou, Fushun and Benxi
  municipalities and the county town of Dengta", `displaced` 6,080. The new case is P126611,
  IBRD-82360, 2013–2019, in Donggang, Kuandian, Longcheng District of Chaoyang, Lingyuan, Panjin and
  Suizhong (ICR lines 460–461), placed at 40.9718 / 119.2696 — about 330 km away, one city in common,
  no shared works, different loan, different decade. **Not a duplicate.** The shared implementing
  agency is confirmed from both documents: the existing card and the P126611 data sheet (line 169)
  both name the Liaoning Urban Construction and Renewal Project Office. The card says so.
- **Han River at Xiangyang.** The existing `cuijiaying-han-river-resettlement` is **P085333**, Fifth
  Inland Waterways, 2005–2011, 57 households / 223 people, implemented by the Hubei Provincial
  Transport Department, placed at 32.0107 / 112.1347.
  - P087224 is placed at Hanchuan, 290 km away. Its PAD Table 3 is in the cache and I read it: the
    Xiangfan row is **0.00 mu of rural land acquisition, 0.00 m² of house demolition, 0 people in all
    four people columns, 31.63 mu temporary, RMB 3.81M** — the writer's claim is exact. Greps of ICR
    and PAD for Cuijiaying, navigation, inland waterway and P085333 return nothing, which I re-ran.
  - P119071 is placed at Panggong, 32.0086 / 112.1555, which is **about 2.0 km** from the Cuijiaying
    pin (not within 1.5 km, so the move did what it was meant to do, but the two pins will still sit
    close together in the same city). It is a different loan, a decade later, urban roads and a bus
    corridor against a navigation and hydropower complex downstream, a different implementing agency,
    768 families against 57 households, and no transferred component. **Not one continuing episode.**
    The card's `confidence_note` says this; I left that sentence in place and would keep it.

## 7. The drop the writer made: P092618

Checked as a case, and the drop holds. I read the land acquisition and resettlement passages of the
completion report (¶¶44–47), the borrower's §2.9 and §5, and the review's safeguards section.

- No outcome count of anything, anywhere: the only outcome sentence is "Based on the available
  records, all APs were properly resettled, and most opted to take monetary compensation" (¶46).
  There is no mu figure, no m² figure, no household figure and no person figure in the outcome record,
  and the review only quotes that sentence back.
- No compensation failure: compensation rates "in strict conformity with the applicable policies",
  temporary occupation compensated, grievance mechanisms publicised, most affected people positive in
  a sampling satisfaction survey, and the 2014 restructuring made conditional on disclosing
  satisfactory environmental and resettlement documents, with compliance "achieved very promptly".
- The only household figure is resettlement **avoided** — 238 rural households in Fushun, because the
  local government put the landfill on a former state-owned coal mine waste dump (¶46). Confirmed.
- The only people figure is the appraisal plan: 5,853 persons, 23 villages, 8 districts or counties, 5
  municipalities, with 1,689 mu permanent, 14,347 m² of planned housing demolition and 1,091 mu
  temporary (PAD ¶36). A plan is not harm.
- The three landfill sites selected without broad consultation and rejected by local people cost one
  sub-component and moved two others; the Gaizhou, Panjin and Dawa delays are delays to works.

So: neither limb, and the round-17 lesson does not rescue it, because that lesson needs a documented
resettlement and this document counts nobody. ICIJ's 6,044 against the appraisal's 5,853 is unexplained
by the documents, as the writer says. I left the key out of the checked file, as the writer did, rather
than invent a card to drop; the finding is here.

## 8. Case-by-case corrections to the cards that stay

- **`sichuan-small-towns-unfinished-resettlement`** (strongest of the batch; every figure confirmed —
  2,387.32 and 526.95 mu, 2,802 households / 8,720 people, 142,192.3 against 127,872.9, 605 against
  528 in a table headed "Affected households by losing houses", 39,867.25 for 34 enterprises, Liujiang
  19.7 mu / 19 households / 83 people in Yang and Lianghe villages, the WERP staffing paragraph, "No
  complaints were received throughout the project", the top-ups to replacement cost at implementation
  time, the ICR's own m³/m² conflict, ICR Date 04/14/2017 against the cover's May 31, 2017, and
  US$93.32M against US$93,574,827.58):
  - **Absence claim refuted by the document itself.** The card said the report does not say "what the
    monthly transition subsidy was worth". Annex 8 ¶11 gives it: "monthly transitional subsidies of
    240 yuan per person" in Zizhong. Removed from the absence list and the figure added to the card,
    scoped to Zizhong, which is the only place the report gives it.
  - "changed their minds back and forth" → the report says they changed their mind, once, and says the
    mission *was informed* of it; reworded, and the report's own reason for the choice (the originally
    planned site is closer to where they had lived) added, which the card had left out.
  - "No document was found recording whether those dates were met" → replaced with what the filing
    actually is: the review of 4 December 2017 and a 2017 audit report are the last items, and neither
    records it.
- **`nanning-urban-environment-resettlement`** (1,904 / 7,968 against 1,577 / 7,130, 2,687.073 mu,
  4,428.86 and 89,696.84 m² against 34,871, the four village groups and their three dates, the 10 April
  2017 letter, the 13.22 mu finding of March 2017 with the project office's emails of 19 and 21 March,
  the 10 Tianyu households, the Zhuang social assessment, the restructuring at 92 per cent disbursed —
  all confirmed):
  - **Favourable clause added.** ¶91 of the same report says "all the compensation is completed and the
    issuance of remaining land certificate is a matter of time, as the necessary documents have been
    submitted by village groups". The card carried only ¶50's "delayed because of the incomplete
    documentations that they submitted". Both are now on the card.
  - The four village groups are in **Nanxiang Village** (¶50); the card placed them in Jiangnan
    District, which is where the resettlement office that signed their agreements sits. Corrected to
    say both.
  - **Factual error in the integrity finding.** The card said debarment fell on the company "and a
    subsidiary". The redacted report (lines 73–75, 114) sanctions Company A **and Company B**, which
    share a parent company; the sanction extends to entities they control. Corrected.
  - Certificate absence claim reworded as above; the review's missing date disclosed, as on the other
    newer-template cards.
- **`xiangyang-panggong-resettlement-housing-delay`** (776 compensated / 768 resettled, the mid-term
  review of 2015, funds unavailable for resettlement housing, work starting only in 2016 and some
  finished in 2017, roads delayed more than two years, two extensions to 31 July 2019, the three bodies
  and their uncoordinated timelines, the 2015 cash-compensation policy, the December 2017 social
  specialist mission, satisfactory housing, satisfied residents, no complaints, RMB 28,000→44,000,
  4–5× asset values, the customary-practices and half-of-participants findings, twelve environmental
  monitoring reports — all confirmed):
  - **Sourced to the wrong document.** The comparison with Xiangyang's own growth is the **completion
    report's** parenthesis, not the review's: "with an annual growth rate of 11.5% (which is more than
    the GDP growth in Xiangyang)". Reattributed, with the rate given.
  - The household splitting is "voluntary" in the report; added.
- **`liaoning-coastal-zone-resettlement`** (all three figures, the email, the 760-cubic-metre unit
  error, the Kuandian due diligence in place of a plan, the Lingyuan consultation report naming women,
  disabled and elderly interviewees, the grievance mechanism and absence of any appeal, the
  disclosure dates of 16 October and 14 December 2012, the Panjin counterpart cut from 30 to 10 per
  cent, the borrower's share falling from US$189.5M to US$52.59M — all confirmed):
  - "No document found says where the 548 households were…" was an absence claim over a filing that
    includes nine volumes of site-specific resettlement plans which I did not open. Rescoped to what I
    did read: neither the completion report nor the review says which city, when, what they were paid
    or how many people.
- **`han-river-urban-environment-resettlement`**: no substantive correction. 1,432.53 mu / 95.5 ha, 671
  households, 14,446.09 m² on 83 households, the 88-household survey with its two unexplained
  percentages, the six cash and 72 apartment households at Shayang with the amenities listed, the
  Hanchuan "waste land" that was fishing ponds, the Xiaochang consultation, "all affected households
  were relocated" in the borrower's §15, the odour and groundwater exceedances, and every appraisal
  figure including the nine-city table — all confirmed. Source title left as it is; `displaced` 83
  households is the demolition count and the label says so.
- **`shanghai-urban-environment-apl2-resettlement`**: kept. Checked for the fault the task named and
  it is not there: the card does not turn the rise into a failure — it appears once, in
  `confidence_note`, as a limit, and the favourable material is all on the card (independent monitoring
  confirmed full compensation as stipulated in every plan, no appeal during construction, no negative
  impact on surroundings, rural households paid for farming and crop losses, retraining through village
  committees with those who took it "very satisfied", no ethnic minorities or vulnerable groups
  affected). All figures confirmed against ¶ and Annex 10 Table 10.1, including the DFV +263 per cent
  and +175 per cent rows and the 1,064 that pipe-jacking eliminated. The absence claim stands after I
  read both the safeguards paragraph and Annex 10 in full: the report explains the fall and gives no
  reason for the DFV rise.
  - Removed "This is the thinnest resettlement record of the batch" (batch voice) and the sentence about
    how the report is filed in the Bank's document system (research process — that belongs here, §11).
  - Source title corrected to the appraisal document's own title.
- **`second-shandong-environment-resettlement`**: source title corrected from "Second Shandong
  Environmental Project" to the cover's "Second Shandong Environment Project".
- **`liuzhou-environment-management-resettlement`**: the toilet count. The card gave 43 public toilets
  from the borrower's annex; the Bank's own section (lines 963–965) says public opposition and land
  acquisition difficulties "led to the construction and installation of only 42 public toilets and 30
  portable toilets", 68 per cent of target. Both now on the card, each attributed to its section.
- **Voice.** "Three earlier tranches of Chinese cases have had the same result, so the search was kept
  short" appeared on ten of the eleven cards. It is a record of the research process and has no
  precedent on the map (0 occurrences in `base.html`, against 8 for "Searches in English and in
  Chinese", which I kept). Removed from all ten. No first-person pronoun, "this card", "the draft" or
  "the writer" anywhere in the file.

## 9. Sources

All 48 URLs fetched. 46 return 200. The two UNESCO pages return 403 to `curl` and serve normally
through the fetch tool — see §11. Every appraisal document cover date matches the date on the card
(P126611 8 Feb 2013, P108627 19 Apr 2010, P110632 8 Apr 2011, P077752 30 Jan 2007, P087224 24 Mar
2008, P119071 26 Mar 2012, P120234 22 Apr 2011, P081346 27 Apr 2005, P057933 29 Jun 2004, P075732 8
Jun 2005), and each cached PDF is the document the title claims. The integrity report is dated
"February 2016" on its cover and the card gives month only, correctly.

## 10. Required closing items

### (1) What I could not check
- **Whether the Sichuan dates were met and whether the Nanning certificates were issued.** The Bank's
  filing for each project ends before the answer; the later items are financial audit reports. Both
  cards now say what the filing contains instead of claiming no document exists.
- **Where the Liaoning Coastal 548 households were.** Nine volumes of site-specific resettlement plans
  exist (seven of the nine in Chinese only); they are plans written in 2012 and cannot give the
  outcome, so I did not open them, and I rescoped the card's claim rather than let it stand over
  documents I had not read.
- **UNESCO's exact wording.** The fetch tool returns the pages' substance and short phrases but
  declines to reproduce the reports whole, so the two quoted phrases are the ones both fetches
  returned identically. Everything used from UNESCO was returned twice.
- **The 588 against 251 at Gupan Pond.** Unresolvable from any document in the cache or on either
  UNESCO page. Left unreconciled on the card, which is the right answer.

### (2) Figures where two documents disagree
1. **Sichuan P110632 demolished housing unit** — ICR text "142,192.3 **m3**" (line 1352) against the
   table on the facing page headed "House demolition (**m²**)" (line 1365). Same document.
2. **Sichuan ICR date** — data sheet "ICR Date: 04/14/2017" (line 185) against cover page "May 31,
   2017" (line 41). Same document. The card gives 31 May 2017 and names both.
3. **Sichuan disbursement** — ICR data sheet US$93.32M against IEG data sheet US$93,574,827.58.
4. **Sichuan Jialing 14 households** — ICR Annex 8: resettled by **May 2017**; the review's email of 29
   October 2017: completion "by Oct. 2017". Not on the card; worth knowing that the email revised the
   report's date.
5. **Shandong 2 affected population** — ICR Annex 6 text "4,200 persons" against the table below it
   totalling **4,220**. On the card.
6. **Liaoning Coastal land taken** — ICR "760.6 **mu**" against the review's "760 **cubic meter** of
   land". On the card.
7. **Liuzhou Bank performance** — ICR C.1 **Satisfactory** against the review's column for the ICR,
   **Moderately Satisfactory**. On the card.
8. **Liuzhou public toilets built** — Bank's section **42** against the borrower's section **43**. Now
   on the card.
9. **Liuzhou risk** — ICR C.1 "Low or Negligible" against ICR §4 "Negligible". Same document. Not on
   the card; does not affect a claim.
10. **Shandong 2 risk** — ICR data sheet "Low or Negligible" against §4 "Low". Same document.
11. **Qufu Gupan Pond households** — ICR p.29/Annex 7 **588** against the lessons section **251**. On
    the card, unreconciled.
12. **Qufu / Tai Basin / Shanghai hectare roundings** — 13 ha (ICR) against 13.34 ha (UNESCO);
    598.5 mu as "40 ha" in the Shanghai text and "39.9 ha" in its annex; 697.65 mu as 46 ha and 46.5 ha
    in the same two places. Trivial, and the cards use the body's figures.
13. **Seven label substitutions plus one wrong column**, listed in §5.

### (3) Faults appearing in more than one card
- **The process sentence about earlier tranches** — ten of eleven cards. One edit, ten times.
- **Absence claims written as "no document was found"** — three cards (Sichuan, Nanning, Liaoning
  Coastal), and one of them (the Sichuan subsidy) was flatly refuted by an annex of the document the
  card cites. This is the same fault the brief says has cost the map the most, and it ran in a batch
  whose writer had already been warned about it.
- **The review's date taken from the Bank's document-system record** — nine of the twelve reviews carry
  no date on the page at all (only P077752, P057933 and P081346 print a `Date Posted` line, and those
  three match). Three cards disclosed this and three did not; I verified every date against the
  project document listings rather than the URL, and added the disclosure where it was missing.
- **A favourable clause in the quoted paragraph left out** — Tai Basin ("no residential houses were
  involved", which decided the cut) and Nanning (¶91, "all the compensation is completed … the
  necessary documents have been submitted"). Two cards out of eleven, both in the same direction.

### (4) Things wrong in the card data outside the fields I was asked to check
- **`nanning-urban-environment-resettlement` `outcome`** called the second sanctioned company "a
  subsidiary". The integrity report makes Company A and Company B sister companies under a common
  parent. Corrected.
- **`xiangyang-panggong-resettlement-housing-delay` `community`** attributed the growth comparison to
  the review; it is the completion report's. Corrected.
- **`second-shandong-environment-resettlement` `sources`** carried the wrong project title
  ("Environmental" for "Environment"). Corrected.
- **`shanghai-urban-environment-apl2-resettlement` `sources`** gave the appraisal document a title it
  does not have. Corrected.
- `companies` arrays: every entity checked against the documents. Each is the implementing agency or, on
  Xiangyang, the three bodies the report itself names as having failed to coordinate; no oversight or
  civil-society body is listed beside any of them; the government bodies' roles describe their place in
  the state's structure. The Qufu entry correctly identifies the implementation unit as the body that
  cleared the housing without an approved plan, which is what the report says. No change.
- `lk`, `cp`, `cx`, `rg`, `kind`, `killed`, `killed_note`, `suppression` consistent across all cards;
  `killed` 0 everywhere, with no death recorded in any of the documents I read.
- `displaced` fields: 790 (Qufu, households resettled), 605 (Sichuan, households losing houses), 768
  (Xiangyang, families resettled), 548 (Liaoning, households physically resettled), 174 (Shanghai,
  persons in the table's "Resettled PAPs" row), 83 (Han River, households whose houses were
  demolished). Each is a document's own count of people or households moved, each label says which, and
  no card converts households into people. The four cards with no `displaced` field are the ones whose
  documents count only "affected" people. Correct throughout.

### (5) Routes that failed, named as routes
- **`curl` to `whc.unesco.org`** returns a Cloudflare interstitial, so both UNESCO URLs answer 403 to
  `curl -L` while serving their full content through the fetch tool, which I used four times across the
  two pages without a refusal. The failing route is `curl` against a Cloudflare-fronted host, not the
  host. Anyone re-checking these two sources must use a fetch tool.
- **The fetch tool declines to reproduce the UNESCO state-of-conservation reports verbatim**, returning
  substance and short phrases instead. That is a route limit on quoting, not on reading.
- No permission prompt went unanswered. No host refused anything. 46 of 48 URLs answered 200 to plain
  `curl`.
