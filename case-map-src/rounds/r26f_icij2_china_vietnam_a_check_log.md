# Fact-check log: checked_G1.json (round 18, group G1)

Input `/home/claude/r18/out_G1.json`: 9 cases, 0 extend, 1 drop.
Output `/home/claude/r18/checked_G1.json`: **7 cases, 1 extend, 2 drops.** All 10 lead numbers appear
exactly once. Both files validate with python (`scripts/val.py`: 0 errors — required keys, enum values,
ids unique and absent from `cases.json`, no first person or process narration on any card).

## What was opened

Every document was fetched fresh with `curl` from `documents1.worldbank.org` into
`/home/claude/r18/chk_dl/` and read from disk with `pdftotext -layout`. Project document lists came
from `https://search.worldbank.org/api/v3/wds?format=json&projectid=<P>&rows=200`.

| Project | Documents read in full |
| --- | --- |
| P075730 Hunan Urban Development | ICR 25 Apr 2013 (ICR2616); full 31-document project list |
| P081161 Chongqing Small Cities | ICRR 3 Sep 2013; **PPAR 23 Jun 2014 (Report 88607)**; full 23-document list |
| P083322 Sichuan Urban Development | ICR 19 Jun 2014; ICRR 23 Feb 2015 |
| P128867 Jiangxi Wuxikou | ICR 26 Jan 2021; ICRR 28 Apr 2021 |
| P099112 Anhui Highway | ICR 12 Dec 2012; ICRR 3 Jun 2013; full 24-document list |
| P086508 Da Nang PIIP | ICR 19 Dec 2013; ICRR 23 Oct 2014 |
| P123384 Da Nang SCDP | ICR 20 Jan 2022; ICRR 28 Jun 2022 |
| P116398 Medium Cities | ICR 22 Dec 2022; ICRR 6 Jun 2023 |
| P073361 Natural Disaster Risk | ICR 2 Jun 2014; ICRR 8 Dec 2014 |
| P096925 Bengbu | ICR 7 Mar 2016; ICRR 17 Mar 2017 |

Independent searches run: Chinese for the Changshanyuan wastewater plant and the 2006 suicide attempt;
Vietnamese for Da Nang resettlement and compensation complaints under the World Bank credits. Both
returned nothing on these episodes (Chinese results were soil pollution coverage and unrelated
government PDFs; Vietnamese results were the Lang Van site, the Lien Chieu port road and the Yen River
embankment, all later and separate). The Inspection Panel's 2023 Vietnam cases were checked and concern
the Coastal Cities Sustainable Environment Project, P156143, not any lead here. `contested` therefore
stays on all seven cases.

## Ruling under the refined forward rule, case by case

The rule: **(a)** a document that counts people or households actually *relocated*, **or (b)** a
specific documented harm to identifiable people. Neither means a drop.

| Lead | Case | Limb (a)? | Limb (b)? | Ruling | Bucket |
| --- | --- | --- | --- | --- | --- |
| 15 | Hunan Urban Development | Yes — Annex 8 rows "number of resettled households/people" (Changsha 744/3,051) and "number of households relocated" (WWTP 26/110) | Yes — plan breach at the WWTP, suicide attempt, Huanghe Village complaint, Changsha per capita net income 21.2% below pre-resettlement in 2007, Zhuzhou transitional periods over two years | **Case** | (a) |
| 5 | Chongqing Small Cities | Yes — PPAR: 175 houses demolished in Qianjiang, 127 households resettled, 48 refusing the site | Yes — housing compensation below the rates agreed in the resettlement plan in Tongnan, land compensation delayed | **Case** | (a) |
| 2 | Sichuan Urban Development | Yes, with the verb inconsistency printed — 3,262 households, "affected by the resettlement" in the annex, "households that were relocated" in the body | Thin — two households in Suining unsettled before construction, road narrowed, footways unbuilt; ICR's own note of "reputational risks and controversy surrounding the land valuation and resettlement" | **Case** | (b), with one small documented shortfall |
| 16 | Jiangxi Wuxikou | Yes — 10,469 people in 2,331 households physically displaced, 9,402 to 29 sites | No | **Case** | (b) |
| 11 | Da Nang SCDP (now carrying both credits) | Yes — 1,076 relocated | Yes — 164 compensation cases pending at closing, post-closure action plan, negotiations still open when the report was written | **Case** | (a) |
| 7 | Medium Cities | Yes — 1,006 of 5,367 households relocated | Yes — OP/BP 4.12 breach in Phu Ly in 2015 and 2020: compensation for structures below replacement cost, technical assistance to vulnerable households not given, works begun before a compensation plan was submitted | **Case** | (a) |
| 13 | Natural Disaster Risk | Yes — "989 households had to resettle" | Partly — "slow flow of counterpart funds for resettlement compensation" named as a borrower shortcoming; and the Group twice records that the report gives no concrete evidence for its compliance claims | **Case** | (b) |
| 4 | Da Nang PIIP | Yes — 936 households resettled | No | **Extend** of lead 11's card, not a second case | (b) |
| 3 | Anhui Highway | **No** | **No** | **Cut** | (c) |
| 14 | Bengbu | **No** | **No** | **Drop affirmed** | (c) |

## Priority 1 — Anhui (lead 3): cut

Verified where the figures are. The completion report's resettlement passage, in both the Bank's
section (p. 8) and the borrower's section, gives **only areas**: 2,510.09 mu acquired and 31,194 m²
demolished. No count of people or households appears anywhere in it. The 2,550 households / 9,496
persons and the 412 households are in the Independent Evaluation Group's review, which says in terms:
"The project team provided additional information on the number of people affected by the resettlement,
which were 2,550 households with 9,496 persons. The team confirmed that all 412 households affected by
house demolition built new houses with adequate facilities."

**Ruling.** A number the Bank's project staff supplied orally or in correspondence to the Bank's
evaluators during the review, recorded nowhere else, is not a document that counts households
relocated — least of all when the one document that should carry it, the completion report, does not.
Limb (a) is not satisfied in substance. Limb (b) fails outright: compensation recorded as fully paid at
plan rates, no death, injury, arrest, protest, dispute or complaint in either document, and the
follow-up studies (264 households; 217 directly affected households) report living standards restored
or improved. The works are a 1,160 km province-wide scatter of 24 road segments with no named village
or community. Nothing carries the card. **Cut**, which is also the writer's own recommendation.

## Priority 2 — Chongqing (lead 5): verified, and materially rewritten

The non-disclosure claim holds: the project's 23-document list contains the Group's review, the Group's
assessment report, the appraisal document, two resettlement plans and implementation status reports, and
**no completion report**. Every quoted figure was found in the review as quoted (11,663 affected,
275.78 ha, 108,770.36 m², Annex 7; 48 households roughly 200 people, ICR p. 24; Tongnan rates lower than
the plan's, later corrected; ratings table).

**The writer missed the document that changes this case.** The review recommended the project for
further assessment with the Qianjiang resettlement as its first reason, and that assessment exists: the
Group's **Project Performance Assessment Report of 23 June 2014**, written after a field mission. It
records, for Qianjiang, a new 12.8 km road that "required the demolition of 175 houses to secure the
right of way", of whose residents "127 households were resettled quickly, while 48 households did not
accept a proposed relocation site." The 48 asked to be resettled near the road, which the authority
granted, and asked for full site infrastructure (which the report calls a normal request) and
foundations able to carry high-rise buildings (which it calls not normal); the county government paid
for it at an extra cost of more than US$1 million, the mission saw the piling under way, and households
in temporary housing told it they looked forward to building, moving in and renting out. It also records
nine other resettlement cases affecting 14,158 people at about US$36 million.

Corrections made:
- **`displaced` 48 → 175**, relabelled as the Qianjiang households whose houses were demolished, with
  127 resettled quickly and 48 refusing the site, and with the project-wide 11,663 "affected" stated as
  not a relocation count. The card no longer lets 48 read as the episode's scale; the title was changed
  for the same reason, from "48 households in Qianjiang still not resettled" to name the Tongnan
  compensation shortfall and the 175 houses.
- The PPAR account of the 48 added, so the card does not present as abandonment what the Bank's
  evaluators describe as households holding out and winning a better site.
- A genuine conflict between the Group's own two documents printed unreconciled: the September 2013
  review records housing compensation rates below the plan's in Tongnan, later corrected; the June 2014
  assessment says that in all ten resettlement cases compensation "were reportedly compliant" with the
  Bank's policy.
- The quotation of the borrower-performance reason was corrected to the document's exact string, which
  prints "completion,e.g.," without the space.
- PPAR added as a source.

The case stands on limb (b) (Tongnan) and now also on limb (a) (127 households resettled, 175 houses
demolished).

## Priority 3 — the two Da Nang credits: one card, not two

Absorption verified from the documents, not from inference. The SCDP completion report has a
**Component 5, "Transferred Activities from Da Nang Priority Infrastructure Investment Project"**,
original cost US$36.8 million, actual US$26.94 million, covering the southern road link to the Hoa
Phuoc–Hoa Khuong road, the Hoa Xuan wastewater plant, the Son Tra upgrade, the Phu Loc bridge and the
Phu Loc river embankment, with the associated supervision and safeguards monitoring. The PIIP completion
report says its resettlement was completed satisfactorily "except for those acquisitions and
resettlements which were transferred" to SCDP. The Group's PIIP review puts the transferred works at
US$16.6 million, 25 per cent of the appraisal estimate.

**Verdict: the writer was wrong to write two cases.** Same city, identical coordinates, continuous
2008–2022, and the later credit swallowed the earlier one's leftover land acquisition. Two pins at one
point for one episode. The PIIP is also the weaker of the two: bucket (b), no documented failure, its
monitoring consultant certifying that almost all affected people restored assets and livelihoods. So
lead 11's card is kept as the single Da Nang card, broadened to say it took over the earlier credit's
works, and **lead 4 is an `extend` of it**, carrying the earlier credit's loan detail, its resettlement
counts, its ratings, its sources and its ICIJ figure in `add` blocks. Nothing from the PIIP is lost; it
simply does not get its own pin.

## Priority 4 — the three reported conflicts, checked for manufacture

1. **Da Nang PIIP 936 vs 796 — the writer's attribution was wrong.** The card said both figures were
   the completion report's own. `grep` of the completion report finds **936 twice (Bank section and
   borrower section) and 796 nowhere**; the only other match for 796 is "1,796,000" in a cost table.
   796 is the Independent Evaluation Group's figure, in its list of project outputs — and the same
   review prints 936 in its safeguards section. So the conflict is real but it is between two
   documents, and one document contradicts itself. The report also says the number "increased by 12%
   compared with the original 711 planned", and 711 × 1.12 = 796.3, which is very likely where the
   Group's 796 came from; that arithmetic is in no document and is correctly not offered as an
   explanation. The extend block now attributes each figure to the document that prints it.
2. **Natural Disaster Risk 4,168 — a real conflict of units, not of quantity.** Paragraph 47 of the
   completion report: "This affected 4,168 households, of which 989 households had to resettle".
   Annex 4 totals the same 4,168 in a column headed "Affected people" over "(No. of persons)", planned
   total 3,644. Same quantity, same date, two different units in one report. Kept and printed. Two
   quote defects fixed: the document prints "and/ or", and the annex heading is two stacked lines, so
   it is no longer quoted as one contiguous string.
3. **Sichuan 3,262 — one thing described twice, with two verbs.** The annex says "about 10,788 people
   in 3,262 households were affected by the resettlement (either by land acquisition, house demolition,
   or both)"; the body says "the 3,262 households that were relocated"; the body elsewhere says "the
   actual impact of the project on land acquisition, house demolition, and relocated households was
   less than anticipated in the RAP". Same number, same date, same population. The card already framed
   it as one figure with two verbs rather than as two figures in disagreement, which is right; no
   change needed beyond adding that the ICR uses "relocated" in a third place.

Three of four reported conflicts in the last round were one thing described twice. Here one of three
was (Sichuan), one was mis-attributed (Da Nang), and one is genuine (4,168 households/persons).

## Priority 5 — ratings, verified from the two columns

- **Chongqing**, ICRR table: outcome Satisfactory → Moderately Satisfactory; risk Moderate →
  Significant; Bank performance Moderately Satisfactory both; borrower Satisfactory → Moderately
  Satisfactory, reason column "There were still some pending issues to be addressed at project
  completion,e.g., resettlement activity in Qianjiang county"; Quality of ICR Satisfactory. **All as
  reported.**
- **Anhui**, ICRR: outcome Moderately Satisfactory → Satisfactory, the others unchanged. **As
  reported** (the case is cut on other grounds).
- **Sichuan**: the completion report's data sheet prints "Risk to Development Outcome: Substantial"; the
  Group's table prints **Significant in both columns**, its own and the one for the ICR, with no reason
  for disagreement. **As reported.** The card prints both labels with who prints which and does not
  call it a disagreement about the level — these are two different rating vocabularies.
- **Da Nang SCDP**: Quality of M&E Substantial → Modest, reason "Weaknesses in outcome indicators; M&E
  data was not used to inform AF"; outcome and Bank performance Moderately Satisfactory in both
  columns; Quality of ICR Substantial. **As reported.**
- **Hunan — the absence claim holds.** The project's document list runs to 31 documents and contains no
  Implementation Completion Report Review, and a title search of the Bank's document service for an
  Independent Evaluation Group review of this project returns reviews of five other Hunan projects and
  none of this one. The card now says how the absence was established rather than asserting it.
- Also verified: Medium Cities (Satisfactory / Satisfactory / Substantial / Substantial, no
  disagreement) and Wuxikou (Highly Satisfactory, Satisfactory, M&E High in both columns, Quality of ICR
  Substantial).

## Priority 6 — independent sources

Two searches re-run by hand (above). Nothing independent found; the flags stay. For China and Vietnam
the Bank's own documents really are the whole record on these episodes, and each card says so.

## Priority 7 — the Bengbu drop: affirmed

Verified every figure: 901 mu / 60 ha permanently acquired against about 182 ha planned; 35,572.3 m²
demolished against 103,160.3 m² planned; 5,824 project-affected people at closing against 11,128 at
appraisal; 273 households / 1,094 people for the two roads added at restructuring. All are "affected".
The 40 displaced households in Huaiyuan County are the nearest thing to a relocation count and they
fail limb (b) on the documents' own account: each had signed an agreement for a named apartment by the
end of May 2015, had received all other compensation, and was paid 30 months of transitional housing
rent into a bank account by the county government, to be doubled if the wait ran longer; they chose the
unfinished Jiankang Huayuan site over a completed one about a kilometre away because it was closer to
the centre with better infrastructure and transport. The report also records compensation standards
raised to replacement cost at the time of implementation rather than the plan's rates of two years
earlier. **Drop affirmed**, with the reason extended to rule on the 40 explicitly, and with a note that
Bengbu is the same point as the map's existing `huai-river-flood-drainage-resettlement`
(32.9156, 117.3892), so a case here would have needed a duplicate check too.

## Priority 8 — quote sample

Every quoted string on every card was grepped against the exact file cited
(`scripts/qcheck.py`). Results: all substantive quotes found in the document cited, with four
typographic defects corrected —

- Chongqing: "some pending issues to be addressed at project completion, e.g., ..." → the document
  prints "completion,e.g.,".
- Natural Disaster Risk: "and/or" → "and/ or".
- Natural Disaster Risk: "Affected people (No. of persons)" quoted as one string; it is two stacked
  lines of a table heading, now described as such.
- Medium Cities: "works' terrain" straight apostrophe → the document's curly one.

Two quotes were found in a document other than the one the card cited, and both were re-attributed:
"796 households were resettled, compared to 711 originally planned" (the Group's review, not the
completion report) and "almost all Project affected people have been able to restore their lost assets
and livelihoods" (the Group's review quotes it without "(DPs)"; the completion report's own wording
includes it). A sourced fact in the wrong document is still a sourcing failure, and the 796
mis-attribution was the more serious of the two because it turned a disagreement between two documents
into a self-contradiction inside one.

## Other corrections

**Hunan (lead 15) — two material ones.**
1. The card said "No village is named anywhere in it." **False.** Annex 8 records that in June 2009
   villagers of **Huanghe Village** put their dissatisfaction with the resettlement arrangement to the
   World Bank, that a Bank team visited the village with the provincial project office, and that a
   solution was reached through consultation. Added. This is the only named community anywhere in the
   batch.
2. The card said "per capita net income rose in each section after resettlement". **Incomplete in a
   way that understated the documented harm.** Annex 8 reports that in the Changsha section per capita
   net income in 2007 was **21.2 per cent below the pre-resettlement level**, which it attributes to
   the acquisition and resettlement then under way, to "the failures in implementing the production
   resettlement measures and rehabilitating production of resettled people", and to resettled people
   spending their time building houses rather than producing; income then grew in 2008 and 2009. The
   per-section rises (Xiangtan 29.3%, Zhaoshan 58.8%, Zhuzhou 60.5%, Leidashi 74.3%) are now given
   individually. Also added: the complaint mechanism at the wastewater plant "was not working
   satisfactorily" before May 2007, and all residents of Leidashi town had to be moved.
3. The Annex 8 per-section figures were re-added by hand and match: 3,051 + 810 + 65 + 1,963 + 175 +
   110 = 6,174 people, 744 + 331 + 12 + 714 + 54 + 26 = 1,881 households. The card's note that the
   rows carry different labels section to section is correct and now quotes the labels.

**Sichuan (lead 2).** The two-household refusal in Suining was attributed on the card to the
Independent Evaluation Group alone; it is in the completion report as well, in near-identical words, so
it is now given as both documents'. Added the completion report's own risk passage: the appraisal
document judged most risks moderate "with just two deemed substantial (delay in land sales and
inadequate compensation levels)" and the overall risk profile "should have been at least 'substantial'
if not 'high'", given "the reputational risks and controversy surrounding the land valuation and
resettlement". A duplicated sentence in `confidence_note` was removed. The Panzhihua / Ertan dam
dedupe note was checked: `ertan-dam-resettlement` exists at 26.8208, 101.7811, dated 1991–2006; the
note is accurate and this card's point is Mianyang, 500 km away.

**Wuxikou (lead 16).** Added two things the card omitted: the results framework's own indicator, "No.
of people relocated with proper compensation and livelihood restoration", target 10,104, recorded at
10,469 at 20 June 2020; and the borrower section's different split of the same 10,469 — 9,587 people
from 2,332 local households plus 882 from organisations and enterprises, of whom 7,872 resettled
together, 648 scattered and 1,067 taking cash — against the Bank section's 2,331 households. The
components reconcile exactly (8,520 + 882 = 9,402; + 1,067 = 10,469), so this is not printed as a
conflict. Everything else verified against the report, including 99.56 / 95.58 / 97.79 per cent
satisfaction, RMB 16,678 against RMB 16,521, the city dike figures and the 8.87 m³/s ecological flow.

**Da Nang SCDP (lead 11).** Title changed from "164 cases unresolved" to "164 compensation cases
unresolved" (the document's "cases" are compensation cases, and the earlier wording could read as 164
households left in the open). Cross-reference to a separate PIIP card removed. Verified: 143.72 ha
(printed "143,72" in the report), 71.75 ha agricultural, 4,730 PAPs against 2,855 at appraisal, 1,076
relocated, 4,566 compensated, 164 pending, 94 further households compensated July–December 2021, 83 per
cent satisfied, 1,200 graves and one pagoda, and the State Audit findings.

**Medium Cities (lead 7).** Figures verified in both documents: 5,367 households affected, 1,006
relocated, and footnote 36's three grounds of the OP/BP 4.12 breach word for word. The Group's added
findings — houses damaged by construction, unclear ownership requiring lengthy verification, households
not cooperative, residents demanding excessive compensation — all verified in the review, and the card
correctly marks the last two as the Group's characterisation.

## Dedupe

Checked all seven kept cases against `cases.json` (987 records) by iso3, by coordinates within 100 km,
by project name and by years, and against `out_G2.json` and `out_J.json`. No overlaps. The nearest
neighbours, all checked and all different projects and episodes: `da-nang-quang-ngai-expressway` (84 km
from the Da Nang point, 2011–2019), `vietnam-urban-water-wastewater-below-replacement` (32 km from Phu
Ly, credit IDA-49480, Ninh Binh and Thai Hoa), `vietnam-water-resources-assistance-resettlement`
(P065898), `haiphong-bac-son-nam-hai-road` (IDA-49000), `ertan-dam-resettlement` and
`huai-river-flood-drainage-resettlement`.

## Patterns worth carrying forward

1. **When an Independent Evaluation Group review recommends a project for further assessment, look for
   the Project Performance Assessment Report.** It is the only document in this batch written after a
   field visit, and on Chongqing it reversed the sense of the case's central fact. It is filed under the
   same projectid but often under a joint title with another project, so a title search will miss it;
   the projectid document list will not.
2. **"In the same report" is a claim that needs grepping.** The Da Nang 936/796 pair was presented as
   one report contradicting itself and is in fact two documents, one of which contradicts itself. The
   verb test the brief applies to figures applies equally to the sentence "the same report says".
3. **An absence claim about a named community is as checkable as any other, and was false here.**
   "No village is named" was wrong on Hunan on a full read of Annex 8, and the village that was named
   had complained to the Bank. Worth grepping every "no village/community is named" line against the
   document before it ships.
4. **Income figures stated as a direction of travel hide the dip.** Hunan's card said incomes rose;
   the annex records a 21.2 per cent fall first, attributed to failures in implementing the production
   resettlement measures. Carry the series, not the end point.
