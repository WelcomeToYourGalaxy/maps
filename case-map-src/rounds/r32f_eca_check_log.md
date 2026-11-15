# Round 32, Europe and Central Asia batch — check log

Checked: `/home/claude/work/out32/eca.json` (writer) against the documents in
`/home/claude/work/cache/<PID>/`. Output: `/home/claude/work/out32/eca_checked.json`.

**Writer: 9 cases, 1 extend, 3 drops from 12 rows (75 per cent).
Checker: 6 cases, 1 extend, 6 drops from 12 rows (50 per cent).**

Three keeps cut: `muradiye-hepp-urgent-expropriation-van`,
`kurgan-tyube-istaravshan-utility-works-assets-removed`, `itagar-bridge-approach-shed-demolished`.
All three writer drops confirmed, one with its reason rewritten. Six corrections of substance on the
four keeps that survived unchanged in outcome, plus a shape fault in the extend that would have
applied nothing.

---

## Cuts, with the deciding document and sentence

### 1. `muradiye-hepp-urgent-expropriation-van` (P112578) — CUT

Two independent grounds.

**The lender link is in no document.** `grep -ril muradiye` over the whole 52-file cache returns one
file, `RP_2011-10-12_15287564.txt`, the reporting form. That file contains **no occurrence of
"World Bank", "IBRD", "loan", "credit", "CTF" or "financ"**. It calls itself
"REPORTING FORM FOR LAND ACQUISITION / SOCIAL IMPACTS OF **PORTFOLIO PROJECTS**", and the only tie
to anything is a reporting duty to the intermediary: "The Company will update TSKB periodically on
land acquisition and resettlement." The completion report (`ICR_2017-06-19_27699537.txt`) names no
sub-project; the borrower's annex gives only counts by type. What is left is the Bank's disclosure
filing — volume 13 of the RP762 series, and `p112` inside the filename — which is a catalogue entry,
not a statement by anyone that this loan paid for these plants. Round 31's fault 3 and the
intermediary precedent, where eleven entries died on exactly this.

**The tense, which would decide it even if the link held.** The form, dated 12 October 2011, is
written forward and the card converted it to the past:

| Document (lines 70–87) | Card |
|---|---|
| "For Muradiye 976.539 m2 of land **will be affected**" | "says 976,539 square metres of land **was affected**" |
| "the Energy Market Regulatory Authority **will file** urgent expropriation lawsuits" | "**which filed** urgent expropriation lawsuits" |
| "compensation discussions have **only recently been initiated**" | not on the card |

The only completed harm the form states is "There are only one masonry house on the land, that is
expropriated" — one structure, no person. Clauses in the same document that the card does not carry:
"There is no grievance until now for the construction of our HEPP project"; "no major complaints has
been arised"; "There are no vulnerable people inhabiting the Project area".

**What was left after the cut was tested on its own and also fails.** ICR paragraph 44,
"Resettlement in some sub-projects took place without a Resettlement Action Plan (RAP)", is a real
admission, but paragraph 43 of the same section says the 2,072 people affected across 35
sub-projects "were compensated for loss of assets (including land)", and paragraph 45 records the
remedy — framework rewritten in 2011, ex-post social audits of the sub-projects where resettlement
happened without a plan, a social development specialist posted in 2012, additional livelihood
measures for some affected people. "Some sub-projects" names no person and no place: thinner than
`bukoba-airport-resettlement-arrears`, which names a site and a count of cases. The Dikili plan of
1 December 2016 ("The expropriation process is still ongoing and compensations have not been paid
yet") is a plan describing an unfinished process, not an outcome.

The writer named this its own weakest entry and put the doubt in `confidence_note` rather than
burying it. The doubt is the reason for the cut.

### 2. `kurgan-tyube-istaravshan-utility-works-assets-removed` (P079027) — CUT

Deciding sentence, completion report paragraph 39 (line 1544): "There were 21 project affected
persons and in each case they received compensation in accordance with the action plans." The
borrower's annex Table 4 closes all five contracts with "The construction contractor compensated the
losses incurred according to the Action plan", including the Farkhor water tank, where "a different
plod of land was given to the owner by the local government of Farkhor" on top of 9,922 somoni.

The one remaining limb (b) candidate — land taken, loss of access — is removed by the Istaravshan
plan itself (lines 81–83, 131–137): "Tajikistan law does not require any permanent land acquisition
for 10 kv line and the farmer may continue to use the land below the line after installation"; the
loss of access to the 8-metre strip is temporary; each farm has no more than one pole; the contractor
had to restore the land. The Kurgan-Tyube assessment act is **signed by the householder**, prices the
fence and six trees at 14,060 somoni, and the annex says it was paid. No unpaid balance, no
relocation, no complaint, no claim anywhere in the set. A fence and six trees paid at market value to
a man who signed the assessment is not limb (b).

**A supplied cause, found in the same card.** It said the Kalai-baland compensation rose from 478.08
to 3,087.60 somoni "because 12 trees at two households were to be cut". The plan (lines 142–149)
gives the reason as arithmetic — "due to a miscalculation in the earlier RAP (0.62 x 4980 =
3087.60)" — and lists the 12 trees as a **separate** change in the same paragraph. This is CHECK20's
most frequent named fault, in the writer's own self-named weakest card. The card also omitted the
plan's statement that full compensation fell from 24,037.40 to 21,041.28 somoni.

### 3. `itagar-bridge-approach-shed-demolished` (P098949) — CUT

The harm exists only in a plan written in the future tense. `RP_2014-05-01_19691599.txt`:
"The shed **is subject to** demolition as there is no other option of routing the construction area"
(line 263); "Further, the plot **will be used** for construction of the bridge approach road for
public needs" (line 330); "the PAP **shall get** financial compensation for the cost of labor and
materials for recovery of the building". The card's own `confidence_note` concedes "no document
states the date the shed was demolished". CHECK20: a plan saying a thing will be done is not harm.

Both outcome documents close it. Evaluation review, 31 May 2016 (line 514): "one micro-project
triggered the involuntary settlement policy. A land acquisition plan was prepared in line with the
operational manual, and the affected person was duly compensated." Field assessment, 16 February
2018 (lines 2020–2024): "There was one instance where a microproject triggered the land acquisition
policy, resulting in preparation of a land acquisition plan and compensation to the affected person",
and "no unresolved safeguards issues were reported at project close".

The feature that could have carried limb (b) — land taken with nothing paid for the land — is removed
by the plan: "The option of land compensation is not considered, as this would not comply with KR
land legislation or WB OP 4.12"; the user confirmed the unauthorised use and agreed to the
non-compensatory withdrawal in April 2014 and signed an act; he was paid 21,194 som under the
project's own framework although national law required nothing; "The PAP doesn't have any claims to
project implementers."

---

## The three writer drops

### `georgia-first-east-west-highway-18-plots-paid` (P083110) — DROP CONFIRMED
Paragraph 2.4.7 reads as quoted (lines 1114–1125): 23 plots expected, 8 found no longer affected,
3 added, "Eventually, only 18 land plots were included in the RAP and contracts for compensation were
signed with all 18 owners. All compensations were paid… GEL 55,133.85… No complaints were received."
2.4.8 confirmed. The tunnel collapse "without fatalities" confirmed at 2.2.2 (line 961). Checked
beyond the writer: `grep -i "fatal|accident|injur|death|safety"` across the whole completion report
returns no work-site death or injury — so the health and safety reading holds, which is the check
CHECK20 asks for and the one the Ukraine card failed.

### `bulgaria-municipal-infrastructure-dams-paid-before-take` (P099895) — DROP CONFIRMED, reason corrected
Every quoted sentence found in the file named: ICR paragraph 73 (lines 1513–1518); the 87 per cent /
30,288.85 lev table and "the lack of filed requests on part of the affected persons" in
`RP_2014-06-01_20034312.txt` (lines 402–412); the 1982 Plachkovtsi expropriation and
"A total of 4 persons affected have lived in the properties expropriated" in
`RP_2007-11-01_8947720.txt` (lines 211–212); the Evaluation Group's "legacy and not a current issue"
(lines 926–927).

**Correction to the reason.** The writer wrote that the 0.99 ha and 13 plots "appear in the
Evaluation Group's review because the review is reprinting the 2014 plan". They do not only appear
there: the **completion report states them itself** at paragraph 72 (line 1507), as land acquired
from private individuals in 2008–2014, and the review attributes them to the completion report's
paragraph 71, not to the plan. The plan-reprint call was therefore mis-reported, though the drop is
unaffected — the same paragraphs say the land acquired was compensated.

### `albania-secondary-local-roads-bridge-expropriation-ofid` (P107833) — DROP CONFIRMED, reason rewritten
The forward-rule failure is sound and decides it: paragraph 40 and the 2018 assessment report give
no count, no area, no amount and no stated loss, and both say the affected persons were compensated
in accordance with Albanian law and satisfactorily to the Bank.

**The OFID lender-link argument is overstated and I have demoted it.** The writer's two sentences are
real — the annex says "The Works will be financed through OFID funding" and paragraph 40 says "Works
on both bridges are financed by OFID" — but read whole, the same paragraph calls OFID "**parallel
co-financing of the SLRP**", that is co-financing of this project; the bridge came to light "during
the improvement of the local road 'Ura e Gorices – Fshat Mbreshtan'", a road this credit paid for;
the annex says the Albanian Development Fund "prepared the necessary documentation to comply with the
World Bank's Social and Environmental Safeguard policies to enable the land and properties … to be
expropriated"; another bridge in the same annex was paid for "utilizing money saved from within the
Bank/OFID-financed project"; and the 2018 assessment report, which visited the site, does not mention
OFID at all when it recounts the episode. The lender-link test was not doing real work here; the
forward rule was.

---

## Corrections on the keeps

### `bilotserkivka-m03-bypass-house-damage` (P127156) — kept, four corrections

1. **An absence claim refuted by the cited document.** `killed_note` read "No death caused by the
   works is recorded." Completion report paragraph 75 (lines 1500–1501): "During project
   implementation several health and safety related accidents took place in the project construction
   sites, leading in some of these cases to fatalities. There was inadequate reporting of these
   incidents during the earlier part of the project implementation." No count, no date, no site, so
   `killed` stays 0 and the sentence goes in `killed_note` uncounted. Footnote 18's analysis of
   "fatal crashes" is of road crashes, not these accidents; the report does not resolve the two.
   This is CHECK20's health-and-safety-section warning, and the one card in the batch that failed it.
2. **A supplied cause for how a count moved.** The card gave 106 → 124 (30 Nov 2017) → 122
   (31 Oct 2018) and explained the fall by "three plots on the Poltava bypass were avoided". The
   movement in Addendum No.2's own table is 121 → 122: +2 on the Bilotserkivka lot, −1 on the Poltava
   bypass where a plot with three heirs was counted as one after payment. The three avoided plots are
   a separate list in the same document. Corrected to what each document says.
3. **A chain the documents do not make.** Addendum No.1 (Dec 2017) records the cracked walls.
   Addendum No.2 attributes the acquisition of 3 plots, 1 house and the resettlement of 1 person at
   Bilotserkivka to a **design change for two cattle passes**, and never mentions the cracks. No
   document says the acquired house is the cracked house. The card now says so.
4. **Material the writer missed, cutting both ways.** Addendum No.2 contains a named case study:
   Oleksiy Nechay, born 1940, retired, living on a pension, 60 square metre house built in the 1960s,
   power of attorney to his grandson Sharay Artem of 30 August 2018, the grandson to buy and move him
   to Poltava so no further relocation help was needed. That is far stronger limb (b) than "one PAP".
   The same pages say the contractor held the owners' written consent as of 2 October 2018 "to carry
   out civil works on their land plots before the payment of compensation", and that no works were
   being done on the plot with the house. Added, both sides. Also added the clause the card dropped
   from the sentence it quoted half of: social safeguard compliance "was mainly rated as satisfactory
   and social impact and risk related to land acquisition and resettlement was assessed as moderate".

### `balakhani-landfill-families-and-waste-pickers` (P110679) — kept, `displaced` corrected 14 → 6

`displaced: 14` came from the **plan** (`RP_2011-05-01`, line 169, "The six families have a total of
14 members"), not from an outcome document, and it is also the number ICIJ gives for this project.
The outcome documents count families: the completion report says the six families "were offered
apartments in Baku" and the government compensated "those living on the Balakhani site with improved
housing"; the assessment report of 13 September 2021 says they "were provided with new housing" —
the only completed relocation verb in the set. `displaced` is now 6 families with the unit in the
label, which is how 100 of the 1,136 cards already on the map carry a household-or-family count. The
14 and the ICIJ coincidence are stated in `displaced_note`.

Everything else verified verbatim: the court order sentence and "On the insistence of the World Bank
and all Government stakeholders the court order was never enacted" (lines 272–276); the 144
project-affected people and "Most continued employment either safely at the landfill…" (ICR lines
1184–1187); "only 14 of the 100 to 110 waste pickers accepted" and the 11 still working
(PPAR lines 1053–1065). The PPAR's "reportedly stated" is kept as "reportedly" on the card.

### `tuz-golu-gas-storage-informal-households` (P093765) — kept, two corrections. The batch's strongest.

The `displaced: 17` holds and survives every test asked of it.
- **People-bearing unit, outcome document, relocation verb attached.** Completion report paragraph 95
  (lines 1934–1940), verbatim as quoted, including "before having to vacate the land in December
  2018". Corroborated from the other side by the borrower's annex paragraph 50 (lines 3512–3515):
  "additional livelihood compensation payments were made by BOTAS to the four households, which
  consist of 17 persons."
- **Plan-reprint call: negative.** Neither "17 individuals", "four households", "informal" nor
  "vacate" appears in any of the four plans in a resettlement context. The nearest hit, "a total of
  17 land owners" in `RP_2014-02-25_19151204.txt`, is a different quantity. The writer's account of
  the false "Page 17" pair is accurate.
- **Works this credit financed.** The annex places the households "in UGS 8"; the completion report's
  own Phase 1 milestone list names UGS 8 as one of this project's caverns (line 3347). Link holds.
- **The favourable clause in the same paragraph was not dropped.** "this group was satisfactorily
  compensated by BOTAS in April 2018 and made eligible for priority hiring" is on the card. So is the
  paragraph that cuts hardest the other way — the 2016 plan completion report's 19 of 31 surveyed
  owners expecting to be affected positively, 16 already holding other land, and "No specific
  complaint has been recorded from affected land owners" — all found at lines 628–700 as quoted.
  This is the one card in the batch where the counter-clause search returned nothing the writer had
  hidden.
- **Hazard relocation with a loss on top.** The move was "due to safety concerns", but the loss is
  documented: informal for 20–30 years, not recognised under the Expropriation Law, "therefore
  excluded from the LAP", and the Bank had to intervene before compensation happened.

Corrections: the loan number is **7342-TU** in the completion report (lines 2907, 3010, 3402), not
7342-TR as the card had it — this is the class CHECK31 names. And the `point` note now says what the
report says, that the storage area is about 15 kilometres south of Sultanhanı town (line 2985), since
the card's coordinate is the town.

### `shkodra-lezha-school-sites-land-cleared` (P078933) — kept, selective quotation corrected

Annex 10 paragraph 72 was quoted from its last two sentences only. The card now also carries, from
the same paragraph: the municipality "closed access to the structure by walling it off to students";
"it was confirmed that the municipality remains in compliance with safeguards policies, although the
legal situation of this structure has not yet been clarified"; and that expropriation was expected if
the claim were confirmed. Paragraph 69's "However, no new construction had actually begun under the
project when the discrepancy was discovered" added, with the Shkodra plan's paragraph 2 ("As
originally designed, the Project did not involve application of OP 4.12 because no new school
construction had been contemplated during Project preparation") — which is both the limit on the
lender link and, with the plan's own first sentence that the city "plans to construct a new school
building with support from the Education Excellence and Equity Project", the thing that makes the
link hold. "Delays cost the project about 23 months" tightened to the report's own words, "the
23-months it took to resolve the safeguards issues" (line 704).

Verified verbatim and left alone: the "Complicating matters, in June 2008…" quotation; the May 2008
date, the 4,000 m² enclosure, 3,600 m² grapes, 400 m² cherries, the toolshed, the raki; the District
Court decision and the April 2009 appeal (plan lines 69–73); the plan's three footnote clauses
cutting the other way (5–10 per cent of annual income, the garden he still operates, retail-price
assumption) — the writer carried all three, which is the balance CHECK20 asks for; the Hafizi
family's 873 m², 20,000 lek per m², 17,460,000 lek, eight co-owners at 1/12 to 1/3; "ultimately the
land owner was fully compensated for the value of the land". Ratings and financing (IDA-41800,
XDR 10.50M / 9.83M, quality at entry Moderately Unsatisfactory) match the report's own tables.

### `bajkaj-landfill-land-taken-before-payment` (P086807) — kept, a figure error and a missing counter-clause

**Figure error.** The card gave the total compensation to the Bukhara household as 2,583,000 soums.
That is the trees sub-total; the plan's line (g) is "TOTAL compensation to party = (e) + (f) = (g) =
2 583 000 + 258 300 = **2 841 300** soums". (Correction applied to the Bukhara card — see below.)

On Bajkaj itself, everything verified: the quotation "the contractor accessed the land before
compensations were paid, which caused tensions, consequently work stoppages at the landfill site from
November 2013 to February 2014" is exact (line 416); 3.23 ha, 21 plots, 20 owners, 19,547,136 lek,
15,055,387 lek paid as of January 2015, 32,320 of 54,235 m²; Table 1's named owners and the four
plots taken in full at 892, 1,859, 2,349 and 7,123 m². The ICR safeguards annex paragraph 7 reads as
quoted (lines 3935–3940). Added the counter-clause the card omitted from the same annex: "A RAP for
landfill construction was prepared and implemented in compliance with World Bank operational policy
(OP 4.12)", and that there had been no new complaints since April 2014. Flagged on the card that
Table 1 is headed "as per RAP", with the corrected Table 1/1 giving the same totals.

### `bukhara-sewer-pump-station-cleared-plot` (P112719) — kept, a figure error and a missed annex

Total compensation corrected to 2,841,300 soums (2,583,000 for planting + 258,300 disturbance and
inconvenience allowance at 10 per cent). Added: the plan's Annex 7 is "The signed copy by the house
holder for the partly cash compensation" — the card said no document says what was finally paid,
which overstated the gap; and the framework's own requirement that "all compensation and other
entitlements will need to be paid prior to proceeding with the civil works", which is what was
breached here. Everything else verified: decision 1067 of 24 August 2010, "but unfortunately the
nearby householder was informed only verbally about the project"; Toychiev Nurjon of Sitora St. 50;
"have already been dismantled by the contractor"; "storage house was demolished"; the 1,200 m² fence,
88 m by 2.5 m; the 21 young plants set by the Bukhara City Beautification Department as a third
party; the completion report's "there were instances of project-affected persons not being
compensated for project impacts on time". The card is right that the late-compensation sentence names
no site and cannot be tied to this household, and says so.

### `jale-albania` — extend kept, but its shape would have applied nothing

**Shape.** The object is correctly at top level with `extend`, `lenders_add`, `sources_add`,
`fields_add` — no round-18 nesting under an `add` key, and `fields_add` holds two strings only. But
`merge.py` line 44 adds a lender only if its **name** is not already on the case:
`[l for l in x.get('lenders_add', []) if l.get('name') not in {m['name'] for m in c['lenders']}]`.
The live `jale-albania` card already carries a lender named exactly "World Bank (IDA)", so the
`lenders_add` entry — and with it the P-number, the credit agreement, the 25 per cent disbursement,
the 17-month suspension and the June 2010 lifting — **would have been silently dropped while the
merge printed "extended 1"**. Same class of failure as round 18, different mechanism. I removed the
inert `lenders_add` and moved its facts into the `fields_add` prose, where they will land, and added
`"id": "jale-albania"` so `merge.py`'s `x['id']` resolves whatever the assembler does with the dict
key. (The round-31 east-and-southern-Africa checked file added `id` the same way.)

**Duplication.** The appended community text repeated "15 buildings at Jale in April 2007", which the
live card's `community` already carries in its first sentence. Trimmed. The rest does not duplicate:
the requesters' allegations, management's denial, the Panel's root-cause finding, the "serious
errors" admission, the Management Action Plan and the OP 4.12 footnote are all new against the live
card, and all verified in the completion report at paragraphs 42–45 and annex paragraphs (lines
2040–2135). The appended outcome does not contradict the live card's "The Panel found the project was
linked to the demolitions", but it is a weaker statement of the same finding; both are on the record.

---

## Figures where documents disagree — left unreconciled, both sides given

1. **Bilotserkivka, affected people at one date.** Addendum No.1, 9 December 2017: **124** as of
   30 November 2017. Addendum No.2, December 2018: **121** as of 30.11.2017, in a table column headed
   "Number of PAPs as 30.11.2017 (Addendum No.1)", and its own executive summary says "As of
   December 9, 2017 the total number of PAPs was 121". Same quantity, same date, two numbers from the
   project's two addenda. Neither explains it. **The writer did not report this one**, and instead
   reported the 124 → 122 movement as explained, which it is not.
2. **Bajkaj, how many were owed.** Borrower's land acquisition completion report, October 2014:
   21 plots, **20 land owners**, 13 paid, **7** outstanding. Bank's completion report, 27 April 2016,
   safeguards annex paragraph 7: 3.2 hectares "from **21** project-affected people", 13 full
   payments, **8** pending. Neither document reconciles them. For the record, and without asserting
   it as the explanation: the borrower's own payment table has 21 rows, 13 carrying a payment and 8
   blank, and two of the blank rows carry the same owner's name, Teki Dauti. No document makes that
   observation, so the card leaves the figures as they stand.
3. **Bajkaj, why seven were unpaid — inside one document.** Executive summary and section 3.3: the
   seven "are either deceased or living abroad, mostly in Greece". Section 3.2: seven "have not
   applied for compensation", migration for three, death of the proprietor for four. Verified at
   lines 666–685. Compatible, not identical; both on the card.
4. **Shkodra orchard, date and size.** Completion report Annex 10: "in **June 2008** … demolition of
   a **5,000 M2** orchard". Site plan, 15 April 2010: "In **May 2008** … demolished the existing
   improvements", about **4,000 m²** (3,600 grapes + 400 cherries). Both verified; unreconciled.
5. **Shkodra compensation deadline.** Amended financing agreement: **30 April 2010**. Completion
   report: the ministry "had complied with this covenant by **May 2010**". Both at line 3212.
6. **Balakhani, what happened to the waste pickers.** Completion report, 28 February 2019: 144
   project-affected people, "Most continued employment either safely at the landfill, or with Tamiz
   Shahar in the sorting facility with benefits, including pension." Field assessment, 13 September
   2021: 100 to 110 waste pickers, 14 accepted, **11** working at the facility at the mission. Both on
   the card. Neither says what the rest live on.
7. **Jale, when the Panel investigation opened — inside one document.** Page 13 and footnote 11:
   "On November 1, 2007, the Executive Directors of the World Bank authorized an Inspection Panel
   (IP) investigation". Paragraph 24: "on **January 9, 2009**, the IP opened an investigation that
   resulted in a 17-month suspension of project disbursements". Both verified (lines 756, 1557–1560).
   **The writer's report reconciles these** by saying the 2009 date is the suspension date elsewhere
   in the report. That is a claim the document does not make: paragraph 24 says the Panel *opened an
   investigation* on that date. The report does carry "Following a suspension of disbursements in
   January 2009" at line 758, which is consistent with the writer's reading, but no sentence states
   the reconciliation. Left unreconciled here. Nothing on the card turns on it — the extend uses only
   the 1 November 2007 authorisation and the 17-month suspension.
8. **Istaravshan farm area.** Borrower's annex: six small farms "having a total area of 3,936 ha".
   Same annex: nine farms at Vakhdat with 0.92 ha between them. Istaravshan plan: individual farms of
   0.096 to 1.9 ha. Verified at ICR lines 3681 and 3692. The annex is nowhere corrected. The writer
   reported this and declined to fix it, which is right. Row now dropped, so it does not reach a card.

---

## Checks that came back clean

- **Source URLs.** All 45 URLs in the file (including `sources_add`) matched entries in
  `harvest_manifest.json` by exact string after the single `documents.worldbank.org` →
  `documents1.worldbank.org` host rewrite, and every `date` on a source matched the manifest's
  `docdt` for that document. None constructed. The one spot-check I made against a cover page
  (P086807 ICR) agreed with the manifest date. The three `RP_2007-11-01_*` files for Bulgaria are a
  trap the writer did not fall into — the cited URL resolves to `8947720`, which is the one holding
  the Plachkovtsi passage.
- **Facts resting on staff statements to evaluators.** `grep -rn "informed IEG|the project team|
  World Bank team stated|team informed"` across all eight kept and dropped projects' caches. Eight
  hits, none of them a fact used on any card. The Balakhani "11 waste pickers" is attributed in the
  report to the Evaluation Group's own mission, not to Bank staff.
- **The three reworded quotations.** All three verified against the files and all three are honest.
  (i) ICR 2,072 sentence, footnote marker `11` after "people": the card breaks the quote at that
  point and both halves are verbatim (line 1155). (ii) PPAR 11-waste-pickers, page break after
  "Currently, as": the quoted span begins at "only 11 waste pickers" and is continuous (lines
  1063–1066). (iii) PPAR six-projects, page break before "restricted by third party use": the card
  ends the quote at "was" and puts the four words outside the quotation marks (lines 2013–2020).
  None is a paraphrase inside quotation marks.
- **Voice.** No "I", "we", "our", "my", "this card", "this entry", "the writer" anywhere in the file;
  the only `\bI\b` hit is "Muradiye I", a plant name.
- **Plan-reprint call, every card carrying a figure.** Tuz Gölü: negative, shown above. Bajkaj:
  Table 1 is headed "as per RAP" and the corrected table and the payment table give the same totals,
  now flagged on the card. Bulgaria: the writer's call was wrong in the writer's favour (the figures
  are in the completion report's own text, not only reprinted in the review) and the drop is
  unaffected. Ukraine: the 106 is explicitly the original plan's figure and is labelled as such.
  Muradiye: the whole card was a plan read as an outcome, which is the cut.

---

## What I could not check, naming the route

- **Nothing was blocked and no host refused anything.** I re-fetched no Bank document, as instructed,
  and every document a card cites was present in `cache/<PID>/` and readable.
- **The one thing I cannot settle from the documents I have** is whether this loan financed the
  Muradiye plants. The route that would settle it is a Bank document naming the sub-project — a
  sub-loan list, an ISR, or the project's own sub-project register. The completion report names no
  sub-project at all, so that route does not exist inside the harvest. A fetch of TSKB's own
  portfolio disclosures might settle it; I did not attempt it, because the card is cut either way on
  the tense, and because the instruction was not to re-fetch Bank documents.
- **Outcome of the Bukhara rebuilding and of the Bilotserkivka move.** No document in either cache
  records either. The route that would close them is a later supervision report or a borrower
  completion report for the specific contract; neither exists in the harvest, and both cards say so.
- **I did no outside-the-lender searching of my own.** The writer reports about 11 searches, all
  returning nothing usable, with the lines it tried named. I did not duplicate them. All six keeps
  are therefore `contested`, which is correct under CHECK20's rule: every one rests on the lender's
  own documents, its borrower's annexes and its own evaluation unit.

## Card data wrong outside the fields I was asked to check

- **`lk` and `cp` are absent from every card in this batch.** Round 31's checked files carried both
  (`r31f_latam_checked.json` has `['lk','cp']` on its cases), and `merge.py` reads `c['lk']` and
  `c['cp']` directly in its extend path and asserts both present in `KEYS` for new cases. If the
  assembler that converts this dict-keyed file into merge.py's `{"cases": [...]}` shape does not
  supply them, the merge will fail an assertion on the first case. Worth confirming before the merge,
  not a fact fault.
- **`conditions` and `rg` likewise absent**, and in `KEYS`.
- **`lenders[0].role`, read against the documents on all nine original keeps.** One error found, the
  Tuz Gölü loan number (7342-TR for 7342-TU). Everything else checked out against the reports' own
  tables: P127156 (450/450/540, 20 Sep 2012, 24 Dec 2012, 30 Jun 2021, split rating);
  P110679 (29.5 + 47.1 = 76.6, 17 Jun 2008, 31 Jul 2009, 31 Aug 2018 against 30 Sep 2013);
  P078933 (IDA-41800, XDR 10.50M/9.83M, restructurings 19 Mar 2010 and 22 Mar 2012, quality at entry
  Moderately Unsatisfactory); P086807 (four restructurings, outcome Moderately Satisfactory, risk
  Substantial, quality at entry Moderately Unsatisfactory); P093765 (Moderately Satisfactory,
  efficiency Modest, safeguards at closing Moderately Satisfactory, 709.69 of 938.69);
  P079027 (the PAD quotation at line 3088, exact but for a slash the text extraction lost). That is
  one error in nine — far better than round 22's 19 in 46, and it is the first round where the field
  looks as though it was written from the documents rather than from a data sheet.
- **Research-process prose in `confidence_note`.** Eight of the nine cards ended `confidence_note`
  with a sentence of the form "Searches of X-language sources for … returned nothing about Y". CHECK20
  §4 bars a record of the research process from a public card. Twenty-one of the 1,136 live cards do
  something like it, so the convention is not unknown, but this batch does it uniformly and in the
  heaviest form. I replaced each with the documentary form ("No independent report of Y was found")
  and left the substance. Worth a line in the next writer brief.

## Did the briefs help or mislead?

**CHECK20 and CHECK31 both did real work, and each one named in advance a fault I then found.**
CHECK20's "read the health and safety section and not only the project-history annex" is exactly what
produced the Ukraine `killed_note` correction — paragraph 75 of that report sits in the factors
section, nowhere near the safeguards section the card was written from. CHECK20's "a cause supplied
for a shortfall from nearby text" produced two of the four Ukraine corrections and the Tajikistan
miscalculation finding, which were the same fault in two cards. CHECK31's `lenders[0].role` audit
instruction produced one error in nine, which is a small return but it is the only route to that
field. CHECK31's warning that the briefs make selective quotation *easier* was right in one direction
and wrong in another: the candidate sentences did hand the writer half-sentences (the Shkodra wall,
the Ukraine safeguards rating), but on Tuz Gölü, which no pattern caught, the writer went to the
whole paragraph and carried every clause that cut the other way. The grep-hit fault and the
whole-paragraph discipline fell on opposite sides of the same batch.

**Where the briefs misled: the plan-reprint check in its mechanical form.** On Bulgaria it pointed at
0.99 ha and 13 plots as a plan reprinted in the review, and the writer reported it that way. The
figures are in the completion report's own paragraph 72. The check is built to find plan figures
masquerading as outcomes, and here it found outcome figures that happen to match a plan — the
converse — and the brief's framing ("the review is reprinting the plan") was taken over without being
tested against the completion report's own text. The check still earned its place: it is what sent
the writer to the sentence that settled the drop.

**BRIEF31's withdrawal of the BRIEF22 screen was right and visible in the result.** Three of the six
surviving cases have a null sentence of exactly the withdrawn form sitting in a document they rest
on: Bilotserkivka, whose Addendum No.1 says "No physical resettlement was induced at any stage of
the acquisition"; Bukhara, whose plan says "It is not expected that there will be any residential
structures that will need to be acquired in the project site"; and Shkodra, whose completion report
says "no new construction had actually begun under the project when the discrepancy was discovered".
Under the withdrawn rule all three would have been screened out, and all three carry a named person
and a documented loss.

## Is the 75 per cent rate sound?

**No. It was written to a looser line than the rest of the round, and the looseness is of one kind:
three cards treat a recorded and settled transaction as a harm.**

The six cards that survive share a shape. Something was done to an identifiable person *and the
record does not close*: a contractor on 20 named owners' land before anyone was paid, with 7 or 8
still unpaid when the borrower wrote (Bajkaj); a house cracked by works 10 metres away, and a named
pensioner's house taken, with the project's completion report never coming back to either
(Bilotserkivka); 17 informal residents of 20–30 years excluded from the land acquisition plan, who
needed the Bank's intervention before anyone paid them, and whose destination no document gives
(Tuz Gölü); six families on a landfill against whom a court granted a forcible eviction order
(Balakhani); an orchard demolished before the policy applied, a school built on a family's land, a
wall built across a claimed structure and unresolved at closing (Shkodra); a contractor clearing a
named household's plot before the plan existed and before any survey of what was on it, with the
compensation reconstructed backwards from an assumed maximum (Bukhara).

The three I cut do not have that shape. Itagar is a plan in the future tense with an outcome document
saying the person was duly compensated and nothing is unresolved. Kurgan-Tyube is five assessed
damages, all paid, the claimant's own signature on the assessment, and a plan stating that the land
was not acquired and the farmer may keep using it. Muradiye is a plan for an expropriation that had
not yet been filed in court, attached to a project that no document says paid for it. In each, every
document says the affected people were paid, nobody was relocated, and nothing is outstanding — the
position the writer itself identified on Kurgan-Tyube and then kept anyway, "on 'land taken' and
assets destroyed with named claimants, and nothing more". That reasoning treats limb (b)'s "land
taken" as satisfied by any land that changed hands. Limb (b)'s other examples are all harms that
*persisted* — compensation unpaid or below replacement cost, livelihoods not restored, loss of access
— and `bukoba-airport-resettlement-arrears`, the standing edge, is unpaid compensation in identified
cases. A fence paid for at market value to a man who countersigned the valuation is on the other side
of that line.

At 50 per cent the batch sits inside the round's range rather than above it, and the three cuts all
came from the same place, which suggests one mis-set threshold rather than nine weak judgements. The
writer's own self-assessment found two of the three, and stated the doubt on both plainly instead of
hiding it; the third, Itagar, it did not flag, and that is the one where the tense of the only
harm-bearing document should have stopped the card before the forward rule was reached.
