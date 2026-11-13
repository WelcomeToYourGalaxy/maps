# Round 20, batch A — ICIJ tranche 4, China urban and environment

Output: `/home/claude/r20/r26f_icij4_china_urban.json` — 11 cases, 1 drop, 0 extends, 0 already_on_map.
Cache: `/home/claude/r20/cache/` (see last section).

## 1. Row by row

| ICIJ row | P-number | Outcome | Reason |
|---|---|---|---|
| Liaoning Coastal Economic Zone Urban Infrastructure and Environmental Management (20 Mar 2013) | P126611 | **case** `liaoning-coastal-zone-resettlement` | Completion report: 548 households physically resettled, 760.6 mu taken affecting 1,843 people in 492 households. |
| Nanning Urban Environment (1 Jun 2010) | P108627 | **case** `nanning-urban-environment-resettlement` | 1,904 households / 7,968 people affected against 1,577 / 7,130 planned; land certificates owed to three village groups in Jiangnan District at closing, last due Dec 2018. |
| Jiangsu Water and Wastewater (2 Jun 2009) | P096926 | **case** `jiangsu-water-wastewater-resettlement` | Land taken (59 ha permanent, 1,043 ha temporary); 494 people "resettled and/or compensated". Weakest of the batch — see §2. |
| Sichuan Small Towns Development (10 May 2011) | P110632 | **case** `sichuan-small-towns-unfinished-resettlement` | 348 households not resettled when the loan closed; 114 still not resettled three months later; 605 households lost houses. Strongest of the batch. |
| China-Second Liaoning Medium Cities Infrastructure (26 Jun 2007) | P092618 | **dropped** | Neither limb met. See §1a. |
| Second Shandong Environment (27 Feb 2007) | P077752 (+ GEF P090377) | **case** `second-shandong-environment-resettlement` | 1,331.3 mu taken, 94,750.8 m² of housing demolished, 4,220 affected people. |
| Shanghai Urban Environment APL Phase 2 (5 Jul 2005) | P075732 | **case** `shanghai-urban-environment-apl2-resettlement` | 174 people in 44 households relocated, 598.5 mu taken. Second weakest — see §2. |
| Han River Urban Environment Improvement (29 Apr 2008) | P087224 | **case** `han-river-urban-environment-resettlement` | 671 households lost land, 83 lost houses (14,446.09 m²); 72 families moved to new apartments at Shayang. |
| Hubei Xiangyang Urban Transport (26 Apr 2012) | P119071 | **case** `xiangyang-panggong-resettlement-housing-delay` | 768 families resettled, 776 compensated; funds for resettlement housing were not available, work started only in 2016, Panggong roads delayed over two years. |
| Shandong Confucius and Mencius Culture Heritage (24 May 2011) | P120234 | **case** `qufu-gupan-pond-demolition` | 588 houses cleared in 44 days without informing SACH, the Bank or UNESCO; resettlement begun without an approved RAP; 790 households / 3,612 people resettled in all. Only `documented` case in the batch. |
| Tai Basin Urban Environment (3 Aug 2004) | P057933 | **case** `tai-basin-urban-environment-resettlement` | 30.97 ha taken, 5,050.42 m² of housing demolished, 420 affected people. |
| Liuzhou Environment Management (24 May 2005) | P081346 | **case** `liuzhou-environment-management-resettlement` | 545,100 m² of land taken, 52,818 m² of housing demolished, 2,254 affected people. |

### 1a. The drop

**P092618, China-Second Liaoning Medium Cities Infrastructure Project — dropped.** Neither limb of
the forward rule is met. The completion report of 23 December 2015 says only that "all APs were
properly resettled, and most opted to take monetary compensation", with no count anywhere of people
or households relocated and no recorded compensation failure. The only people figure in its
documents is the appraisal plan — 5,853 affected persons across 23 villages in 8 districts or
counties and 5 municipalities (PAD, 15 May 2007). The one household count in the completion report
is resettlement **avoided**: in Fushun the local government put the new sanitary landfill on a
former state-owned coal mine waste dump, which the report says avoided the resettlement of 238
rural households that would otherwise have been required. The other resettlement content is
implementation delay at Gaizhou, Panjin and Dawa, which is harm to the works, not to people; and
three landfill sites selected without broad public consultation that local people rejected, after
which one subcomponent was dropped and two found new sites. ICIJ gives 6,044 against the appraisal's
5,853 and the documents do not explain the difference.

### 1b. The two duplicate warnings, resolved

**Liaoning.** The existing case `liaoning-medium-cities-resettlement` is **P099992**, the *first*
Liaoning Medium Cities Infrastructure Project (approved 27 June 2006), in Liaoyang, Panjin, Jinzhou,
Fushun, Benxi and Dengta. Both leads in this batch are separate projects:

- P092618 (Second Liaoning Medium Cities, 26 Jun 2007) runs in Anshan, Haicheng, Gaizhou, Yingkou
  EDZ, Fushun, Panjin and Dawa — overlapping only at Fushun and Panjin — and is **dropped** anyway.
- P126611 (Liaoning Coastal, 20 Mar 2013) runs in Donggang, Kuandian, Longcheng District of
  Chaoyang, Lingyuan, Panjin and Suizhong, 2013–2019. One place in common with P099992 (Panjin) and
  no shared works.

Both leads are therefore new. The link worth recording, and recorded in the card, is that the **same
provincial office — the Liaoning Urban Construction and Renewal Project Office — is the implementing
agency for P099992 and for P126611**. Two loans, one office, not one episode. `dedupe_leads.py`
confirmed P092618, P126611, and the other ten numbers are absent from `window.CASES`; a sweep of all
1,026 cases for the place names Qufu, Zoucheng, Xinjin, Miyi, Zizhong, Jialing, Panggong,
Xiangcheng, Nanning, Jiangnan, Lingyuan, Donggang, Suizhong, Kuandian, Hanchuan, Shayang, Chongming,
Qingpu, Zaozhuang, Yantai, Weifang, Gaomi, Qixia, Heze, Taihu, Wuxi, Liuzhou, Danyang, Taixing,
Yancheng and Zhenjiang returned only `wuxikou-reservoir-chitan-resettlement`, which is Wuxikou in
Jiangxi, a different place.

**Han River at Xiangyang.** The existing case `cuijiaying-han-river-resettlement` is **P085333**, the
Fifth Inland Waterways Project, a navigation and hydropower complex on the Han River downstream of
Xiangyang, 2005–2011. Neither lead is a continuation of it:

- P087224 (Han River Urban Environment) builds wastewater and solid waste works in nine Han River
  cities. Grep of its ICR and PAD for "Cuijiaying", "inland waterway", "navigation" and "P085333"
  returns nothing. Its resettlement is at **Hanchuan** (land) and **Shayang** (housing), not at
  Xiangyang; Xiangfan/Xiangyang appears in its appraisal table with 0 mu of land acquisition, 0 m²
  of demolition and 0 affected people, only 31.63 mu of temporary occupation. Point placed at
  Hanchuan, 30.6563 / 113.8330 — 290 km from the Cuijiaying pin.
- P119071 (Xiangyang Urban Transport) builds roads and a bus corridor inside **Panggong, Xiangcheng
  District** of Xiangyang city, 2012–2019. Same grep returns nothing; no component is transferred
  from the waterways project. Point placed on Panggong subdistrict, 32.0086 / 112.1555, rather than
  on the city centre, which would have landed within 1.5 km of the Cuijiaying pin. The
  `confidence_note` states explicitly that the two are different loans a decade apart with no
  transferred component.

## 2. My two weakest entries

**`jiangsu-water-wastewater-resettlement` (P096926) — weakest.** The entire outcome record is one
sentence: "494 PAPs were properly resettled and/or compensated". That "and/or" is the problem — no
document says how many of the 494 lost a home rather than a strip of land or a share of income, so
the card carries no `displaced` field at all. What is left for harm is land taken: 59 ha permanently
and 1,043 ha temporarily, against an appraisal plan of 34 ha and 350 ha. The appraisal planned
demolition of the houses of 117 households / 417 people, 104 households of them in Nanjing, but a
plan is not harm. The completion report rates the project Highly Satisfactory and says resettlement
proceeded smoothly. If the checker wants to drop one card from this batch, this is it.

**`shanghai-urban-environment-apl2-resettlement` (P075732) — second weakest.** 44 households and 174
people, with independent monitoring under the project confirming full compensation in every case, no
appeal during construction, and retraining that the report says satisfied those who took it. The
scale is tiny and the only thing that makes it more than a "people affected" count is that the
completion report gives an explicit relocated figure. One item is genuinely odd and is flagged in
the card: the district-facility subprojects moved **174 people against a plan of 48, and 44
households against 16** — nearly four times the plan — while the project total ran 84 per cent below
plan because pipe-jacking eliminated the Western Trunk Sewer's 1,064 people entirely. The report
explains the fall and not the rise.

A third worth naming: `second-shandong-environment-resettlement`, `tai-basin-...` and
`liuzhou-...` all rest on limb (b) land taken plus square metres of housing demolished, with **no
count of people or households relocated in any document**. Each of those three ICRs says compensation
was above the planned standard, paid on time, with incomes restored. They are honest but unexciting.

## 3. Figures where two documents disagree

1. **Sichuan (P110632) demolished housing unit.** The ICR text says "the project actually demolished
   142,192.3 **m3** of houses"; the table on the same page heads the column "House demolition
   (**m²**)". Same document, same figure, two units.
2. **Sichuan ICR's own date.** Data sheet: "ICR Date: 04/14/2017". Cover page: "May 31, 2017".
3. **Sichuan disbursement.** ICR data sheet: US$93.32M. IEG data sheet: US$93,574,827.58.
4. **Shandong 2 (P077752) affected population.** ICR Annex 6 text: "Population affected by the
   project was **4,200** persons". The table immediately below totals **4,220**.
5. **Liaoning Coastal (P126611) land taken.** ICR: "760.6 **mu**". IEG review: "a total of 760
   **cubic meter** of land". A unit error in the review; mu is an area.
6. **Liuzhou (P081346) Bank performance — the review's column for the ICR is wrong.** ICR C.1:
   Bank Performance **Satisfactory**. The IEG review's ratings table prints the ICR's Bank
   performance as **Moderately Satisfactory**. This is exactly BRIEF20 trap 1; both are named in the
   card and the ICR's own value is the one given as the report's rating.
7. **Qufu (P120234) Gupan Pond households.** ICR p.29 and Annex 7: **588** houses demolished / 588
   households resettled in Qufu. ICR lessons section: "resettlement at Gupan Lake where the **251**
   households originally lived". No document reconciles 588 with 251.
8. **Risk-rating label substitutions in the IEG review tables** (five of them, all in the newer
   template, all noted in the cards):

   | Project | ICR's own word | IEG table's word for the ICR |
   |---|---|---|
   | Sichuan P110632 | Moderate | Modest |
   | Han River P087224 | Moderate | Modest |
   | Nanning P108627 | Moderate | Modest |
   | Shanghai APL2 P075732 | Moderate | Modest |
   | Jiangsu P096926 | Low | Negligible |
   | Shandong 2 P077752 | Low or Negligible | Negligible to Low |
   | Liuzhou P081346 | Low or Negligible | Negligible to Low |

9. **Rating disagreements between the two bodies**, each named with its document in the cards:
   Nanning (MS → MU on outcome, Bank and borrower), Shanghai APL2 (MS → MU on all three, risk
   Modest → Substantial), Jiangsu (Highly Satisfactory → Satisfactory), Tai Basin (Bank performance
   Moderately satisfactory → **Unsatisfactory**, two notches), Liuzhou (outcome S → MS), Han River
   (risk → Substantial), Xiangyang (outcome MS → **Satisfactory**, upward; M&E Modest → Substantial),
   Second Liaoning and Sichuan and Qufu (no disagreement).

## 4. "Informed IEG" — staff statements, not documents

Grepped every review for `informed IEG`, `the project team` and `the World Bank team stated`. Three
findings that matter, all attributed to the staff statement in the card and never to a document:

- **Sichuan P110632**: the entire post-closing position on the 114 unresettled households is an
  **email from the project team to IEG dated 29 October 2017**. The review has no document for it.
  There is a second one at line 430 (email of 28 Sep 2017) on water/wastewater, unused.
- **Liaoning Coastal P126611**: "548 households were physically resettled and received appropriate
  compensation **in a timely manner as confirmed by the Task Team in its June 3, 2020 email to
  IEG**". The timeliness is not in any document.
- **Liuzhou P081346**: two confirmations of compliance supplied by the project team where the review
  says the ICR did not mention it (lines 269, 372, 467). Not used.

## 5. Selective-quotation check

Every card carries the favourable clause from the same paragraph as the damaging one. Specifically:
Sichuan carries the households' own choice to wait while drawing subsidies, the above-replacement
compensation top-ups and "no complaints were received"; Xiangyang carries the satisfactory housing,
the satisfied residents, the absence of complaints and the 4–5x asset values; Nanning carries the
March 2017 finding that Village Group No. 11 had in fact been fully compensated — the single most
important counter-clause in the batch, since the implementation status reports had flagged it as
incomplete compensation; Han River carries the Shayang "best practice" programme and the survey
satisfaction; Qufu carries the destination housing, the 500-metre distance, the preserved
neighbourhood and the risen house prices. No cause has been supplied for any shortfall that the
documents do not themselves give — the Sichuan delay cause ("large resettlement sites built by local
governments for this and other domestic projects, delayed and not under the Bank project's control")
is the report's own words.

## 6. Independent sourcing — one case out of eleven

Ten cases are `contested`: they rest on the Bank's completion report, its appraisal document and the
Independent Evaluation Group's review of its own completion report. The lender is reporting on its
own project. Searches in English and in Chinese (`世界银行 四川小城镇发展项目 拆迁 安置 新津 米易 资中
嘉陵 348户`) returned only World Bank documents and Bank-derived aggregators
(ewsdata.rightsindevelopment.org, which republishes Bank PDFs). As BRIEF20 predicted, this was
stopped after two searches and the position is stated in every `confidence_note`.

**`qufu-gupan-pond-demolition` is `documented`**, on UNESCO:
- World Heritage Centre letter to China, 9 December 2013, on the razing of historic housing in the
  buffer zone.
- China's reply of 28 March 2014: the work is "a comprehensive renovation project (partly funded by
  the World Bank)", covers **13.34 ha** of the buffer zone, and "**A total of 588 households have
  been moved since the first half of 2013**" — a figure matching the Bank's ICR exactly.
- Committee decision **38 COM 7B.11** (38th session, 2014): concern about potential impacts on
  Outstanding Universal Value, authenticity and integrity.
- **ICOMOS Reactive Monitoring mission, 9–12 December 2014** — a field mission, and the only one in
  this batch.
- 2016 state of conservation and decision **40 COM 7B.32**: the 13.34 ha held 588 households, most
  built after the 1970s, about a third dilapidated, five buildings saved as historically valuable;
  **no construction followed the demolition**, which the report says damaged the local government's
  public credibility.

Two honest limits on that, stated in the card: the 588 figure is China's own statement to UNESCO,
not a UNESCO finding; and UNESCO's concern is for the heritage site, not for the people moved. On
the people, the Bank's ICR remains the only source.

## 7. Routes: what worked and what failed

**Worked.** Projects API with `countrycode_exact=CN&qterm=` found all twelve P-numbers in two
batched calls; matching on approval date was essential — "Liaoning Medium Cities" returns three
P-numbers (P099992/2006, P092618/2007, P099224/2008) and "Second Shandong Environment Project"
returns the IBRD number P077752 and the GEF number P090377 on the same approval date of 27 February
2007. `wds?projectid=` + `curl` to `documents1.worldbank.org` + `pdftotext -layout` delivered 37 of
37 documents. Nominatim returned every place asked for, in Latin script for all but one
(Panggong subdistrict needed `庞公街道 襄城区 襄阳市`; the Latin query would not have found it).

**Failed, with the failure named, not the host:**

1. **`wds?projectid=P075732` does not return the Shanghai APL2 completion report.** Nor does
   `projectid=P070191` (the parent) or `projectid=P096923` (the sibling, APL III) — those return
   their own ICRs. Only the ICR *Review* is filed under P075732. **Route that worked:** a `qterm`
   title search, `qterm=Shanghai Urban Environment APL 2 Implementation Completion`, which returned
   ICR3543 filed under P075732 but titled "China - Second Phase of the Shanghai Urban Environment
   Adaptable Program Loan (APL) Project" with a blank `docty`, which is why the projectid listing
   misses it on a document-type filter. The `docty` field being empty, not the host, was the failure.
2. **`curl` to `whc.unesco.org` returns a Cloudflare JavaScript interstitial**, not the page: a
   5,384-byte body reading "Just a moment... Enable JavaScript and cookies to continue". Not a host
   refusal and not a block — the same URL served fine through WebFetch, three times. Anyone caching
   UNESCO state-of-conservation pages for this project should use a fetch tool, not curl, and the
   two stub files were deleted from the cache so they do not mislead.
3. **UNESCO SOC pages cannot be reproduced verbatim through WebFetch** — the fetch declined to
   reproduce the full report text and returned a structured summary instead. The figures used in the
   card (588 households, 13.34 ha, decision numbers, mission dates) were each returned in two
   separate fetches of two different pages and agree; no sentence is quoted as UNESCO's wording
   except the two short phrases that both fetches returned identically.

Nothing was blocked. No permission prompt went unanswered.

## 8. Document cache

`/home/claude/r20/cache/`, every file as a paired `.pdf` and `.txt` (`pdftotext -layout`), named
`<P-number>_<type>`. 37 files for this batch (other round-20 batches are writing to the same folder):

- **ICR + ICRR + PAD** for all twelve leads: P126611, P108627, P096926, P110632, P092618, P077752,
  P075732, P087224, P119071, P120234, P057933, P081346.
- **P108627_INT** — Integrity Vice Presidency redacted report, February 2016, covering Nanning plus
  the Second Guangdong Pearl River Delta and Yunnan Urban Environment projects. Company names
  redacted; the Bank debarred "Company A" and "Company B" with conditional release, and on Nanning
  the finding is that Company A misrepresented the availability of its key personnel in its
  technical proposals. Nothing on resettlement.
- `P075732_ICR` is the one that is **not** findable via `projectid=P075732`; it is cached so the
  next job does not have to repeat the title search.
- Working document lists per project are in `/home/claude/r20/work/docs_P*.txt` if a later job needs
  the full filing (Implementation Status Reports, audit reports, the nine Liaoning Coastal
  resettlement plan volumes, the eleven Jiangsu resettlement plan volumes).

No Project Performance Assessment Report exists for any of the twelve; no review recommended one.
No Inspection Panel case was found for any of the twelve.

Nothing was merged, `build.py` was not run, git was not touched.
