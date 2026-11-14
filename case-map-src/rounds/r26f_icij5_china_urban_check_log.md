# Check log — round 21, batch A (Chinese urban and airport rows)

Checked: `/home/claude/r21/r26f_icij5_china_urban.json` (6 cases) against the 31 cached documents
in `/home/claude/r21/cache/` for P123729, P127867, P098915, P092631, P070519, P123133, P112838.
Output: `/home/claude/r21/r26f_icij5_china_urban_checked.json`.

**Result: 5 kept with corrections, 1 dropped (Fuzhou). The Tianjin drop is confirmed.**

---

## 1. `shangrao-sanqingshan-airport-land-take` — KEPT, three corrections

### The rule-1 question, decided

BRIEF21 rule 1 says that where a document records **housing actually demolished**, homes were lost
and limb (b) is met **without a household count**; what it excludes is **land area plus a count of
"affected" people**. Shangrao is on the keeping side of that line and not at the edge of it. ICR
para 67 records 7,708 m² of existing structures of 21 households actually demolished, and the
Evaluation Group's review prints a demolition block in a table with its own household, area and
population rows: 16 households planned against 21, 5,760 m² against 7,708, 76 people against 96.
Houses came down and people lost them. Rule 1 asks nothing more, and the limb-(a) limits the brief
sets out — the hazard-relocation limit and the associated-facility limit — are limits on limb (a),
not on limb (b).

**Reading of the rule, stated plainly:** rule 1 makes homes lost sufficient on its own. It does not
require a recorded adverse outcome on top, and nothing in the forward rule does either. A land take
with no demolition and no recorded adverse outcome would be a drop under the rule's second half;
this is not that case. Kept.

### Correction 1 — a false absence claim, and the fault that mattered most in this batch

The card said of the Project Team's table: "that table is not in any document found, and nothing
from it is used here." **The table is printed in the Evaluation Group's review, pages 14 and 15,
immediately under the sentence that announces it.** It was found by reading the review rather than
grepping it. Its rows:

| | RAP planned | Actual | Increase |
|---|---|---|---|
| Total land (mu) | 2,241.9 | 2,913 | 30% |
| Arable land (mu) | 383.75 | 506.52 | 32% |
| Demolition — households | 16 | 21 | 31% |
| Demolition — area (m²) | 5,760 | 7,708 | 34% |
| Demolition — population | 76 | 96 | 26.32% |

The exclusion of this material was therefore made on a mistaken absence claim, and it cost the card
its only actual count of people: **96 people whose houses were demolished, against 76 planned.** Per
CHECK20 the figure is kept **attributed to the staff statement, not to a document**: it is in
`community` and `displaced_note` as a table the Bank's project team supplied to the evaluators.
`displaced` stays unset — the table's row label is "Population", with no relocation verb.

### Correction 2 — a loan covenant stated backwards

`conditions` said: "where the agreement's provisions conflicted with the safeguards instruments, the
latter prevailed." The Project Agreement for Loan 8256-CN, Section I, Part C, paragraph 6, says the
opposite: "In the event of any inconsistency between the provisions of the Safeguards Instruments
and the provisions of this Agreement or the Loan Agreement, **the provisions of this Agreement and
the Loan Agreement shall prevail**." Corrected.

### Correction 3 — the confidence note

Removed the clause resting on the false absence claim; added that the one people figure is the
project team's and not a document's.

### Selective quotation: tested and not found

Every favourable finding named in the task is on the card, and I found no sixth. ICR para 67:
monitoring showing better housing with better water, drainage and community services; semi-annual
external monitoring confirming compliance with the RAPs — both on the card. ICR para 46: the 2016
consultant survey of 30 households in Zunqiao, incomes RMB28,534 → RMB35,950 (26%), living area
388 → 472 m², agriculture's share 12.9% → 10.4% — all on the card, verbatim-accurate. Review: "There
were no delays in the payment of appropriate compensation" — on the card. Outcome and Bank
performance Highly Satisfactory — on the card, and the card also gives the ICR's own Satisfactory.
ICR para 65 (EMP implemented satisfactorily) and para 66 (grave relocation compensated per the RAP)
are also on the card. The card's `confidence_note` leads with the favourable material and says the
income survey covers 30 households out of the hundreds affected and was done by a project consultant.
Appraisal figures (150 ha, 26 ha cultivated, 2,500 people/500 households, 5,760 m²/76 people/16
households, 137 graves) all confirmed in PAD paras 44 and 54, with the appraisal's "will affect".

---

## 2. `xining-wusixi-road-demolition` — KEPT, two corrections

### What the RAP update of January 2018 actually says

I read it. Section 1.2.1, "The progress of resettlement at current stage", runs:

> "**According to monitoring report of the external monitoring agency**, the land acquisition and
> structure demolition of this project has all been completed by December 31, 2016. Totally
> 233,600m2 structures were demolished and 724.88mu land were acquired (except Chengxi Passenger
> Station). **However, the construction of resettlement complexes is about three years later than
> the original plan.** Of which, construction of Taobei Village Resettlement Complex was just
> started in October 2017; construction of Wangjiazhai Village Resettlement Complex was started in
> November 2017; and construction of Huangzhong County Resettlement Complex has not yet been
> started."

**The three findings asked about, settled:**

1. **The outcome areas are quoted from the absent monitor.** The 233,600 m², the 724.88 mu and the
   31 December 2016 completion date all sit under "According to monitoring report of the external
   monitoring agency". They are not the plan's own figures.
2. **The three-year delay is stated as fact in the plan's own voice.** The "However" sentence and
   the three complexes carry no attribution to the monitor. They are the preparers' own statement
   of where the resettlement stood, written by the project implementing unit, Xining Chengtong
   Transportation Construction & Investment Co., Ltd., off a field survey and public consultation
   that the Involuntary Resettlement Research Center of China Three Gorges University ran between
   7 and 20 January 2018 (confirmed at lines 288-300 of the plan). Both company entries on the card
   are accurate.
3. **Can a borrower-prepared document with an uncheckable attribution carry a case on its own?**
   On these facts, yes, and the card is `contested`, which is the right place to put it. Three
   reasons. First, BRIEF21 rule 2's test is whether the outcome document reprints the appraisal's
   figures: here it does not. The appraisal gives 150,661 m² and 788.09 mu; the plan gives 233,600 m²
   and 724.88 mu. Grepped: neither 233,600 nor 724.88 appears in the PAD, the ICR or the review.
   These are new figures, not a plan recycled. Second, the part that carries the harm — the delay
   and the unstarted Huangzhong complex — is the preparers' own, so the absent monitor is not
   load-bearing for it. Third, the card does not rest on the plan alone for the fact of a
   displacement: the structures demolished are recorded, and rule 1 makes homes lost sufficient.
   What the plan cannot support, and the card does not claim, is any count of households waiting or
   any duration of waiting.

### The appraisal reprint, confirmed in both outcome documents

ICR para 88: "the proposed investments at appraisal involved further land acquisition and
resettlement. The **envisaged** urban roads and public transport investments involved displacing 121
households (527 individuals)". The review drops the "envisaged": "The project's urban roads and
public transport investments involved displacing 121 households (527 individuals)" — the appraisal's
estimate presented as though it were an outcome, which is exactly the shape BRIEF21 rule 2 names.
The card's `displaced_note` says this and `displaced` is correctly unset.

### The 760 households, correctly named and not counted

PAD para 48: a due diligence review covering 2010-2012 activity — 520,487 m² of houses demolished,
368 ha acquired, 760 households resettled — carried out before project identification, found
compliant with Chinese land law and Qinghai regulation, living conditions restored. The card names
all of it in `community` and says in `confidence_note` that it is "not counted here as the project's
doing". Confirmed as the task describes it.

### Selective quotation: tested and not found

The review's social section contains the strongest counter-statement in the batch — "All resettlement
sites were completed prior to the closing of the Bank loan and each family received at least two sets
of the apartments" — and ICR para 90 adds villagers living in the same community without disruption,
savings turned into village enterprises, and the transitional fee changed from monthly to yearly after
an internal review. All of it is on the card, in `community`, `outcome` and `confidence_note`.

### Correction 1 — researcher voice in `conditions`

Removed: "The Project Agreement for Loan 8319-CN, dated 4 March 2014, is published only as a scanned
image with no text layer, so its covenants were not read." That is a record of the research process
and belongs in this log, not on a public card (CHECK20 §4). The silence the task asked me to confirm
now holds completely.

### Correction 2 — attribution sharpened

`confidence_note` now says the delay statement is the plan's own and not attributed to the monitor.

---

## 3. `nanjiangbin-road-slum-resettlement-fuzhou` — **DROPPED**

Set to `"status": "dropped"` with a full `drop_reason`. Not deleted.

**Each of the writer's three grounds, tested:**

**(a) "480 households stood in the Bank-financed road's path and were moved involuntarily."** The
first half is documented, the second is not. ICR para 38 and the equivalent passage at para 57 both
say "The road alignment itself **only affected** 480 households" — the verb is "affected". No
document separates the 480 from the other 2,520, gives them a different entitlement, or says any of
them were moved involuntarily. What the documents do say is that "after multiple consultations,
**following the community's request**, the FMG decided to resettle the entire population". The
involuntariness of the 480 is the writer's inference, not a finding.

**(b) "The Bank cut its own social safeguards rating to Moderately Satisfactory for 'considerable
delays and additional costs in resettlement'."** The quote is verbatim and correct (ICR p.8:
"Although the outcome was satisfactory, the considerable delays and additional costs in resettlement
lead to a moderately satisfactory rating for social safeguards"). But read against the review, which
I did, the delays named are delays to **the works** — "The Kuiqi bridge, the Third Ring Road and
Jinshan Bus Depot investment activities were all delayed mainly due to resettlement issues" — and the
additional costs fell on the Fuzhou Municipal Government, whose contribution rose from US$224.46m to
US$432.87m against a 62 per cent total cost overrun. These are losses to the project's schedule and
budget, not to identifiable people.

**(c) "Access ramps left unbuilt at closing for want of resettlement."** Confirmed (ICR paras 28 and
29; review section 4). Four non-motorised access ramps to the Kuiqi Bridge were unfinished at closing
"since necessary resettlements (**minor in scope**) were delayed", with no date offered. This is a
shortfall in the works. It is a loss of access to users of a bridge, not a loss recorded against the
people who were moved, and the same documents record the second closing extension as having been
granted to finish exactly these minor works.

**The one thing closest to a loss on top of the move,** which the writer found and put on the card:
ICR para 25, at the mid-term review — "as civil works on Kuiqi Bridge progressed, the land for
building resettlement houses for affected populations by its northern section remained unavailable."
That is people displaced for works that were going ahead with nowhere built to go. It does not carry
the case, for three reasons. The same report says at para 29 that the land acquisitions were "in the
end completed satisfactorily and without major complaints", and at para 26 that "consultations with
all the displaced populations and villagers affected by the project revealed that most people were
satisfied with their new situations". No count of the households waiting and no duration is given
anywhere. And the Kuiqi Bridge is a different contract and a different site from the Nanjiangbin Road
alignment the card is placed at — CHECK20's single-site rule. I dropped rather than rewrote: a card
recentred on the Kuiqi Bridge would have no count, no duration and no recorded loss.

**Against the move, the documents record only gains:** the RAP and RPF "successfully carried out
without any major complaints"; "Ex-post interviews with resettled people indicate a high level of
satisfaction"; 4,642 new apartments, "significant improvement in living conditions", and apartments
that "are household assets that can be transacted in the market" unlike the former homes; and the
practice adopted by the municipality as a new city resettlement policy. This is round 19's Bogotá
shape in full.

**Note on the card itself:** it was the most carefully balanced of the six, and its `confidence_note`
opens by saying both Bank documents treat the resettlement as a success. The drop is a judgement on
the documents, not on the drafting.

---

## 4. Tianjin (P098915) — **drop confirmed, all four points**

1. **GEF grant, green-building pilots on existing public land plus TA.** Cover and data sheet:
   TF-97018, "IN THE AMOUNT OF US$6,163,636", USD 6.16M disbursed, total project cost US$64.06m with
   the GEF share US$6.16m. ICR para 55: "All the project pilot investment on buildings were on
   existing public land."
2. **16 km² acquired in 2008, resettlement finished by early 2009, by the Tianjin Municipal
   Government before Bank project identification.** PAD paras 43-44: "in total, 16km2 land was
   acquired by the government from three villages, two state-owned enterprises, and a military
   enterprise within the project area… The resettlement process began in 2007 and all the land was
   acquired in 2008. All resettlement was completed in late 2008 or early 2009 by TMG… In summary,
   the resettlement process started before the Bank project identification and was completed by
   early 2009." Repeated at PAD Annex paras 32-34. The one exception is the Bayi Salt Plant's office,
   allowed to stay until about 2011.
3. **Both documents state no land acquisition or resettlement occurred under the grant.** ICR para 55
   is exact: "Throughout implementation, **no additional land acquisition or resettlement occurred**
   and no social risks or negative impacts emerged." **One wording correction for the handoff:** the
   statement in both documents is "no **additional** land acquisition or resettlement", and the PAD's
   form of it is the PMO's report that no additional land would be required plus the task team's
   forecast. The report's summary table drops the word "additional" in one place. The drop stands on
   the time test and the harm-on-what-the-money-financed test either way.
4. **The ICIJ match is exact and should go in the handoff.** PAD Table A10-1, "Details of resettlement
   impacts under the SSTEC project", column "Total Project Affected Person (PAP)": Wuqi Village 1,057;
   Dongfeng Village 600; Qingtuozi village 500 (251 households). 1,057 + 600 + 500 = **2,157**, ICIJ's
   figure to the person. The table describes a pre-project due-diligence review of land taken in
   2007-2008. This is the cleanest demonstration in the batch that ICIJ's number is a
   project-affected-person count lifted from an appraisal annex, and in this instance from an annex
   describing a land take the Bank's money had nothing to do with.

Worth recording for whoever revisits this: Qingtuozi is **house demolition only**, 14,300 m², 251
households, 500 people — housing actually demolished with a household count, which under BRIEF21 rule
1 would meet limb (b) if the timing and financing tests were met. They are not: the demolition was
complete before the Bank identified the project, and the grant financed nothing on that land.

---

## 5. Every rating, read out of the document that gave it

I opened each ICR's own rating section and data sheet, and each review's own table, rather than
taking a rating out of the review's column for the report.

| Project | Rating | ICR, read from the ICR | Review, read from the review | Agree? |
|---|---|---|---|---|
| P123729 Shangrao | Outcome | **Satisfactory** (ICR para 39, data sheet) | **Highly Satisfactory** | **No** — real, the review prints a reason-for-disagreement paragraph |
| P123729 Shangrao | Bank performance | **Satisfactory** (ICR para, "Rating: Satisfactory, based on the discussion above") | **Highly Satisfactory** | **No** — "No shortcomings were identified in quality at entry and quality of supervision" |
| P123729 Shangrao | Quality of M&E | Substantial | Substantial | Yes |
| P092631 Xi'an | Outcome | Moderately Satisfactory | Moderately Satisfactory (weighted 3.6 on a split rating) | Yes |
| P092631 Xi'an | Risk to development outcome | **Moderate** (data sheet; §4 "Rating: Moderate") | **Modest** (§7a) | **Wording only** — see below |
| P112838 Wuhan | Outcome / Bank perf / M&E | Moderately Satisfactory / Moderately Satisfactory / Modest | same three | Yes |
| P123133 Qingyang | Outcome / Bank perf / M&E | Moderately Satisfactory / Satisfactory / Modest | same three | Yes |
| P127867 Xining | Outcome / Bank perf / M&E | Satisfactory / Satisfactory / Substantial | same three | Yes |
| P070519 Fuzhou | Outcome | Satisfactory | Satisfactory | Yes |
| P070519 Fuzhou | Risk to development outcome | **Low** (data sheet; §4 "Rating: Low") | **Moderate** (§7a) | **Yes, a real step** |

**The Xi'an Moderate/Modest disagreement is close to a manufactured one and I corrected the card.**
The review's §7 rationale is favourable throughout — proven competence in road maintenance, evident
government ownership, strong technical capacity — and states no disagreement with the report. The two
words are the two templates' labels at the same point on a scale, not two judgements. The card now
says the review records no disagreement and that its stated reasons are favourable. The Fuzhou step
(Low → Moderate) is genuine but that card is dropped.

**The two internal date conflicts, both confirmed:**
- **Fuzhou ICR**: cover page "November 11, 2013"; its own data sheet "ICR Date: 11/07/2013", which in
  the Bank's US format is 7 November 2013.
- **Xining ICR**: cover page "February 22, 2022", confirmed by rendering page 1. The archive `docdt`
  of 2021-02-22 is the writer's report of the API field; I did not re-query the API, so I confirm the
  cover date and take the API side on the writer's word.

---

## 6. The Qingyang appraisal contradiction — confirmed, and both figures are on the card

Printed page 11: "Structure demolitions will affect **529 people** (143 families)." Printed page 26:
"The project will affect 201 families (862 people) by land acquisition and 143 families (**528
people**) by structure demolition." I located both by rendering pages and reading their printed page
numbers, so the page attribution in the report is right. The same document, the same 143 families,
two counts one apart. The card's `displaced_note` carries both — "the appraisal gives the people in
those 143 families as 528 in one passage and 529 in another" — and does not reconcile them. Correct
handling; left alone.

---

## 7. The `displaced` field, all six checked against the documents

| Case | `displaced` | Document's words | Verdict |
|---|---|---|---|
| Xi'an | 11,433 people | ICR para 37: "A total of 2,371 households (11,433 people) **were resettled** under this project." | **Correct.** Outcome, relocation verb, people-bearing. Set beside the appraisal's 527 households / 4,770 people in the same sentence, so it is not a reprint. |
| Qingyang | 226 households | ICR para 60: "the **relocation** of 226 households"; Table 4 column header "Number of Relocated households". | **Correct.** |
| Fuzhou | 3,000 households | ICR: "decided to **resettle** the slum's population (all 3,000 households)"; "Ex-post interviews with **resettled** people". | Verb is right, but the case is dropped, so the field goes with it. Had the case stood, the 3,000 mixes 480 in the road's path with 2,520 who moved at the community's request. |
| Wuhan | omitted | ICR para 78: "the project **affected** 1,055 families (with 3,265 people)". The only relocation verb — "took over six years until every displaced family was relocated" — carries no count. | **Correctly omitted.** |
| Xining | omitted | Only people-bearing count is the appraisal's 121 households / 527 people, reprinted. Outcome figures are areas. | **Correctly omitted.** |
| Shangrao | omitted | "7,708 m² of existing structures of 21 **affected** households"; the project team's table row is labelled "Population", 76 → 96, with no verb. | **Correctly omitted**, and the note now says why the 96 is not entered. |

---

## 8. The staff statement — confirmed excluded from the card, but the exclusion rested on an error

Nothing from the Project Team's table was on the card. Confirmed. But the card's reason for excluding
it — that the table "is not in any document found" — is false: the table is printed in the review
under the sentence that announces it. See item 1. I grepped all seven reviews for `informed IEG`, `the
project team`, `the World Bank team stated` and `provided`; this was the only hit in the batch that
carries a figure, so the writer's sweep was otherwise right.

---

## 9. The Project Agreements

**Five extracted cleanly and their dates are confirmed on the cover page.** Two of the five print the
date only as a handwritten entry that `pdftotext` mangles; I rendered both cover pages to images and
read them: Shangrao **"Dated June 4, 2013"**, Qingyang **"Dated July 12 2012"** — both exactly as the
cards have them. Fuzhou "Dated November 21, 2006", Wuhan "Dated June 11, 2010", Xi'an "Dated September
29, 2008", all in the text layer.

**Wuhan's quote and contrast — verified, and it is the strongest conditions material in the batch.**
Project Agreement for Loan 7864-CN, Section I, paragraph 9(b), verbatim: Wuhan shall, "where the
acquisition of land or assets or the displacement of people is unavoidable, **before initiating the
implementation of any works** which would result in such acquisition or displacement, make available
to such people compensation and, as applicable, **relocate and rehabilitate the displaced people in
permanent sites with adequate facilities**, including providing all related assistance required in
respect thereof, all in accordance with the RAP"; and where assistance is "of a transitory nature,
make arrangements prior to implementing any such works for the permanent and adequate relocation and
rehabilitation of such people". Against that, ICR para 77(c): at the Nanhu Village site "the land
approval, design, and urban planning of the resettlement site were delayed for over three years… 
Without further land-use approval for the Nanhu resettlement site from the new authorities,
resettlement site facilities, including electricity power, drinking water and gas supply, could not
be connected to the main pipelines." Both halves are on the card and both are accurate.

**Xi'an's is nearly as strong and is also on its card:** Loan 7558-CN, paragraph 4(b) requires
compensation "in accordance with the RAPs and the RPF… and **before the carrying out of the works**
which would result in such acquisition or displacement", against payments to 39 and 37 households
delayed and the 37 still in transitional housing when the loan closed.

**Qingyang's quotes verified verbatim:** "ensure that all land acquisition under the RAP required for
the purposes of carrying out works under the Project are financed exclusively out of Qingyang
Municipality's and Xifeng District's resources", "provide, promptly as needed, the resources needed
for this purpose", and semi-annual reporting "by March 15 and September 15 of each year, commencing on
March 15, 2013".

**Shangrao's is where the one covenant error was** — see item 1, correction 2.

**Xining's silence holds, and is now complete.** `pdftotext -layout` on P127867_PA.pdf returns 129
bytes, all of it the repeated "Public Disclosure Authorized" stamp. `pdfinfo` gives Creator
"Image2PDF Command Line Software", 7 pages, no text layer. I grepped all six cards for `prevail`,
`conflict`, `inconsist` and `Project Agreement`: no claim about Xining's covenants appears on any
card in either direction. I removed the one sentence that mentioned the agreement at all, because it
was a note about the research rather than a finding.

---

## 10. Other corrections made

- **Wuhan `displaced_note`** contained a garbled clause: "That is **to the person** the appraisal plan
  figure: the Project Appraisal Document of 2 March 2010 states…". Corrected to "That is the appraisal
  plan figure". The PAD quote itself is verbatim-correct ("Housing demolition will entail the
  relocation of 391 households with 1,486 people, 218 shops (with 556 employees), and 21 enterprises")
  and the 48.2 ha appraisal land figure is confirmed at two places in the PAD.

---

## Required closing items

### 1. Anything I could not check, and what stopped me

- **The `wds` `docdt` fields.** Two card-level date claims rest on the Bank's API record rather than a
  document: Xining's review (29 June 2022), the five other reviews' dates, and the reported 2021-02-22
  `docdt` conflict on the Xining ICR. I read every document from the cache per the brief and did not
  re-query the API, so these I take on the writer's word. Each card already says the review's date is
  an unverified archive field, which is the right disclosure.
- **The external monitoring reports.** Three sets are cited by Bank documents and none is in the
  cache: the Xining external monitoring agency's report behind the 233,600 m² and 724.88 mu, the ten
  monitoring reports behind Qingyang's Table 4, and the sixteen reports by Wuhan University's Center
  for Involuntary Resettlement Research (January 2011 – July 2018). I could not confirm the writer's
  report that none is in the Bank's archive, because confirming an absence needs the searches the
  writer ran and I read from disk. Each card states the dependence.
- **The Shangrao Project Team's table at source.** I read it as printed in the review. The underlying
  table the team supplied is not a document.
- **Independent, non-Bank sources.** I ran none. The writer reports two searches per case returning
  nothing; all five surviving cards are `contested` and each `confidence_note` says the lender is
  reporting on its own project, so nothing turns on it.

### 2. Figures where two documents disagree

| Quantity | One figure | The other |
|---|---|---|
| Qingyang, people in the 143 house-demolition families | **529** — PAD printed page 11 | **528** — PAD printed page 26. Same document, same families. |
| Fuzhou, date of the completion report | **11 November 2013** — cover page | **7 November 2013** — its own data sheet, "ICR Date: 11/07/2013" |
| Fuzhou, date of the mid-term review | **30 November 2009** — ICR para 24 body text | **2 December 2009** — ICR data sheet, "Mid-term Review… 12/02/2009". **A second internal date conflict in the same report, not reported by the writer.** The card uses the data sheet's 2 December. Both are the same document; neither is wrong to prefer, but the conflict should be on the record. Moot, as the case is dropped. |
| Xining, structures demolished | **150,661 m²** planned — PAD para 51, reprinted in the RAP update | **233,600 m²** actually demolished — RAP update, quoting the external monitor |
| Xining, land acquired | **788.09 mu** planned — RAP update's own survey summary | **724.88 mu** acquired — RAP update, quoting the external monitor. Note the planned figure is also given as 52.8 ha in PAD para 51, which is 792 mu; the 788.09/52.8 pair is a rounding, not a conflict. |
| Xi'an, households resettled | **2,371 (11,433 people)** given as the project total — ICR para 37 | ICR para 32 says "2,371 families had already been resettled at that point" in June 2016, with "the final group of 76 families" still to come — which would make the total 2,447. 39 + 37 = 76, so the final group is the two delayed groups. **An internal inconsistency in the same report, not reported by the writer.** The card uses para 37's stated total, which is the right choice; worth a line in the handoff. |
| Wuhan, land required | **48.2 ha** at appraisal — PAD | **31 ha** at completion — ICR para 78 |
| Shangrao, land planned | **150 ha / 2,500 people / 500 households** — PAD para 44 | **2,241.9 mu planned (≈149.5 ha)** — project team's table in the review. Same quantity in two units, not a conflict. |
| Shangrao, outcome and Bank performance | **Satisfactory** — ICR | **Highly Satisfactory** — review, with a stated reason |
| Fuzhou, risk to development outcome | **Low** — ICR | **Moderate** — review |
| Xi'an, risk to development outcome | **Moderate** — ICR | **Modest** — review, with no disagreement stated. Treated as a wording difference, not a conflict. |

### 3. Faults appearing in more than one card

**One, and it is a near miss rather than a repeat.** The only fault that recurred in substance is the
**absence claim about a document the researcher had already downloaded**: Shangrao's "that table is
not in any document found", refuted by page 14 of the very review the card cites. The related
near-miss is the Xining `conditions` sentence, which stated an absence correctly (the agreement is a
scan) but stated it on a public card, where it reads as a research note. Both come from the same
habit — writing what was not found into the card rather than into the log. **Everything else was
confined to one card each**, which is the better news in this batch: no figure was sourced to the
wrong document, no rating was taken out of the review's column for the report, no cause was supplied
from nearby text, and no quotation I checked was selective.

### 4. Anything wrong in the card data outside the fields I was asked to check

- **The reversed covenant in Shangrao's `conditions`** — see item 1, correction 2. A loan term stated
  backwards, in a field I was asked about only in general terms. Corrected.
- **The garbled clause in Wuhan's `displaced_note`** — corrected.
- **All 24 source URLs resolve, every one with HTTP 200, and the byte count each returns matches the
  cached PDF exactly, file by file.** That is a stronger check than title-matching: the documents
  cited are the documents read. No 404, no 403, no redirect to a different file.
- **Companies arrays** read correctly against the documents. The Xining entries for Xining Chengtong
  Transportation Construction & Investment Co., Ltd. and the Involuntary Resettlement Research Center
  of China Three Gorges University are confirmed at lines 288-300 of the RAP update, with the 7-20
  January 2018 survey dates exact. Wuhan's Center for Involuntary Resettlement Research entry is
  confirmed, including the 16 reports and the January 2011 – July 2018 span. No oversight or
  civil-society body is listed beside an agency that caused harm on any card. The Shangrao entry for
  the Shangrao Sanqingshan Airport Construction Office correctly separates what the municipal
  government did from what the office did.
- **Voice:** I scanned every string field and every nested `name`/`role` for first person, "this
  card", "the writer" and the rest. The only hits were the substring "us" inside "US$". Clean, except
  for the Xining research-process sentence noted above, which the pattern does not catch and which I
  removed.
- **Cost and date figures in `lenders[0].role`,** which I spot-checked on all six: Shangrao's
  US$105.13m → US$125.46m and US$55.13m → US$76,066,127, the RMB478m counterpart and the RMB350m
  Civil Aviation Development Fund grant are all in ICR paras 56 and the cost tables; Wuhan's US$192m →
  US$520m resettlement cost and the 183.6 per cent increase are at ICR lines 717 and 1291; Xining's
  US$83.7m counterpart for resettlement-related activities and the quoted "The project did not finance
  land acquisision" are at ICR lines 1687 and 552 — the misspelling is the Bank's own and the card
  quotes it as found.

### 5. Routes that failed, named as routes

- **`pdftotext -layout` on `P127867_PA.pdf` returns 129 bytes.** The file is intact and downloads
  fine; `pdfinfo` shows Creator "Image2PDF Command Line Software" and no text layer. A format failure,
  not a route failure and not a host refusal.
- **`pdftotext` on `P123729_PA.pdf` and `P123133_PA.pdf` mangles the handwritten cover date** into
  "Dated 2 / 4 4 ,2013" and "AGREEMENT dated   2   , 2012". Both dates were read by rasterising page 1 with
  `pdftoppm` and reading the image. **A text-extraction route that fails on a handwritten field is
  recoverable by the rasterise route — worth adding to the method, since conformed Project Agreements
  of this vintage date themselves by hand.**
- **`pdftoppm` prints "Missing language pack for 'Adobe-GB1'" on these files.** Cosmetic: the Latin
  text renders correctly and the images were legible. Not a failure.
- **No network route failed.** Every one of the 24 source URLs answered 200 over HTTPS through the
  proxy on the first attempt. Nothing in this batch supports a claim that any host is blocked.

Nothing was merged, `build.py` was not run, git was not touched.
