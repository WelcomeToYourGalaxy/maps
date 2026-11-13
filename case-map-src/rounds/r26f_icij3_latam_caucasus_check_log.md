# Check log, tranche 3 batch C

Eight cards checked against the documents. **Five kept, three dropped.** Every figure, date, name
and quoted phrase in the five kept cards was checked against the cited document. All nineteen
source URLs were fetched and returned HTTP 200, and each document's report number and date were
read out of the file to confirm the citation matches what is at the URL.

Corrected file: `/home/claude/r19/checked_C.json`. Nothing merged, `build.py` not run, nothing pushed.

## Confidence values reset

The writer used high/medium/low. All eight are now `documented` or `contested`.

| Case | Was | Now | Why |
|---|---|---|---|
| south-west-roads-turkestan-sairam-compensation | high | **documented** | The core harm does not rest on the Bank reporting on itself. The Inspection Panel visited Turkestan, Sairam, Yntymak and Temirlanovka between 26 September and 1 October 2011 and recorded its own field findings. An Inspection Panel finding is a documented-grade source. |
| hanoi-ring-road-2-relocation | high | **contested** | Rests on the Bank's completion report and the Evaluation Group's review of that report. No independent source. |
| bahia-viver-melhor-ii-resettlement | high | **contested** | Same: completion report plus the Evaluation Group's review of it. |
| bogota-high-risk-area-resettlement | medium | **contested** (dropped) | Same. |
| baku-shamakhi-highway-land-acquisition | low | **contested** (dropped) | Same. |
| rurrenabaque-airport-land-compensation | medium | **contested** | Same. |
| philippines-nrimp2-unpaid-land-claims | medium | **contested** | Same, and part of the account rests on what Bank staff told the evaluators. |
| colombia-mass-transit-cartagena-vendors | low | **contested** (dropped) | Same. |

Every `confidence_note` on a `contested` card now says plainly that the Evaluation Group reviews
the completion report rather than visiting the site, so both documents are the lender reporting on
its own project.

---

## The five specific questions in the task

### 1. `baku-shamakhi-highway-land-acquisition` (P118023) — **DROPPED**

Opened the completion report and read the passage. Paragraph 110, page 25, is the whole record and
the card reports it accurately: "Overall, the project managed impacts on 441 affected people,
including fourteen cases of economic displacement." The 2014 downgrade and the litigation clause are
in the same paragraph.

Two sentences decide it, and the card quoted around both:

- The same paragraph: "Before works commenced, the PIU ensured that owners and users of the impacted
  land were fully compensated in accordance with the RAPs."
- The Evaluation Group review: "The project complied with the social safeguards... The PIU ensured
  that owners and users of the impacted land were fully compensated before works commenced."

So the document's affirmative finding is that compensation was paid in full and in advance. What is
left is a count of people "affected" plus fourteen economic displacements with no person, no place
in the corridor, no amount, no litigation outcome, no count relocated and no independent source.
Limb (b) requires a specific documented harm to identifiable people; nothing here records
compensation unpaid, compensation below replacement cost, a livelihood not restored or a loss of
access. The brief's rule — a card whose entire content is a count of people "affected" is a cut —
applies directly. The coordinate problem is real as well: Shamakhi town is one end of the road, and
the Evaluation Group review notes land acquisition was needed only for 9.75 km of privately owned
land plus the Shamakhi bypass, so the point is not a place where land was taken.

### 2. `colombia-mass-transit-cartagena-vendors` (P082466) — **DROPPED**

Read the completion report. Confirmed it counts plans and properties and never counts people:
paragraph 23 and annex page 54 give 28 resettlement action plans, 23 complete as of December 2012
with all their properties acquired, five outstanding, one (Itagüí section 5) dropped after design
changes. US$2.62 million of a US$3.50 million budget. Footnote 12 is the Cartagena finding, and it
reads exactly as the writer said: "Transcaribe has carried out all of the actions required to
implement the resettlement plan according to policy, but the local administration has not yet
executed the plan due to institutional weaknesses and political instability."

Searched both documents for any statement that vendors were removed. There is none. The Evaluation
Group repeats the same two sentences and adds nothing. Both documents carry the opposite finding:
"Despite these issues, all resettlement processes were satisfactorily undertaken in compliance with
Bank policy." The recorded fact is an unexecuted plan, not a harm. Neither limb is met and the
documents do not establish that anyone lost anything, so it is cut as the task directed.

### 3. `bogota-high-risk-area-resettlement` (P085727) — **DROPPED**, and this is the precedent

The 1,067 figure is solid: results framework indicator, and paragraph 56 repeats it ("the District
Social Integration Secretariat exceeded the original goal of relocating up to 700 families; at
Project closing 1,067 families were resettled"). The 367 at Nueva Esperanza is in the indicator
comment. Limb (a) is met on its face.

It fails test 2. On the document's own account this is not resettlement for a project's convenience;
it is the relocation itself that the loan was bought to deliver, and the document reports it as a
benefit to the people moved:

- The appraisal target was "up to 700 households have been earmarked for resettlement to safer
  locations with secure housing tenure" — the move was the project's output, and exceeding it is
  reported as success.
- Paragraph 75: the project "was expected to have a major beneficial impact on that population
  group", poor and socially vulnerable people living in high-risk areas.
- Paragraph 76: "The resettlement was carried out minimizing the disruption of the livelihood of
  people living in the high-risk areas, and ensuring that displaced people were treated equitably."
- Paragraph 83: "no negative social or environmental impacts were at project closing identified as
  a result of project activities."

The point that settles it is paragraph 43. OP 4.12 was triggered **for the construction works, not
for this component**: "The OP 4.12 was triggered mainly to prevent that any person or group of
persons were affected by acquisition of land or property to carry out reconstruction or retrofitting
works." Paragraph 44 says the only land or property acquisition impacts identified outside the
relocation programme were in the health sector, handled under an abbreviated resettlement plan for
fewer than 200 people affected, with not a single complaint filed. So the Bank did not classify
these 1,067 families as people displaced to make way for its works; it classified them as
beneficiaries of a hazard-relocation programme.

**How the scope decision applies.** The standing decision — a documented resettlement is harm whether
or not the lender recorded a failure — exists so that a case is not thrown out because the Bank
rated itself satisfactory. It is a rule about who gets to certify that a displacement was harmless.
It is not a rule that every movement of people financed by a loan is harm regardless of why they
moved. The distinction the task names is the operative one, and this case is squarely on the
hazard-relocation side of it. The only sign of compulsion is one clause in paragraph 83,
"unwillingness by some families to resettle", which carries no count, no names and no recorded loss,
so it cannot carry limb (b) by itself.

**Precedent for the rest of the list.** A preventive relocation out of a hazard zone is kept only
where a document records a loss on top of the move: compensation unpaid or below replacement cost,
livelihoods not restored at the destination, people moved against their will with that recorded as
such, or a destination the documents show was worse. A bare count of households moved to safety,
with the lender reporting a benefit and no negative impact, is dropped. If an independent field
study of these 1,067 families later turns up, the case comes back on that source.

### 4. Bahia (P081436) — both figures real, both measured, field corrected in its label

Both are in the one completion report, and they measure different things:

- **1,332 households** — results framework indicators A2 and A3, "households removed from high risk
  areas or unhealthy conditions", measured at 31 October 2013 against a target of 983. Repeated in
  the ICR narrative (footnote 23) and in annex A3.
- **1,750 families** — footnote 23, page 10: "At the time of Project closing a total of 1,750
  families had been resettled of whom 62 percent had opted for new housing, 21 percent for cash
  compensation, 12 percent for assisted purchase, and 5 percent for continued legal proceedings."

So 1,332 is the subset removed from risk or unhealthy areas and 1,750 is the total actually resettled
at closing from all causes. Both count people actually relocated, and 1,750 is the wider of the two,
so **`displaced: 1750` is correct and stays.** The label was changed to carry the other quantity:
"families resettled in total at project closing, of whom 1,332 came from high-risk or unhealthy
areas", and `displaced_note` now names each figure, what it measures, where in the document it sits
and the date it is measured at. The `community` sentence now says the 1,750 is a footnote total
"from all causes" so the two are not read as rival counts of the same thing.

Every other Bahia figure was checked and confirmed in the report: 832 pending at closing reduced to
795 by January 2014; of the 795, 661 new housing, 82 judicial compensation, 26 cash, 26 monitored
indemnification (Table 2); by area 318 São Bartolomeu, 198 Parque São Bartolomeu, 145 Mangueira III,
123 Sussuarana III / Baixa da Paz, 10 Encosta de Pirajá, 1 Avenida Anchieta; 535 of the 661 expected
by August 2014; 293 households left in situ for an effective total of 1,625; housing indicator 1,009
of 2,000 with 164 cash compensations excluded; Feira de Santana 14 of 358 (4 per cent) against a
national 12 per cent; loan IBRD-73440 US$49.30 million fully disbursed; 33 months of extension; 84
per cent counterpart ratio. The reason the 164 were excluded is also as the card states (paragraph
39: the unit "could not guarantee whether their new homes purchased were an improvement on the
previous residence, or how effectively the compensation money was spent").

**Two rating errors found and corrected — see the disagreements section.**

### 5. Kazakhstan (P099270) — both points confirmed

**The 2017 flooding is nowhere treated as established harm.** Checked every field. It appears only in
`outcome`, and only as a claim with all three positions attached: the requesters' claim (eight houses
flooded, material damage, one household compensated), Management's answer (general snowmelt and
rainfall across Kazakhstan, not the roadworks, plus a hydrological study commissioned in January
2021), and the Panel's 13 April 2021 eligibility finding of no plausible link with a recommendation
of no investigation, approved by the Board on 26 April 2021. `community` does not mention it.
`displaced`, `killed` and `displaced_note` do not carry it. `confidence_note` says it is set out as a
claim. The writer's handling is correct and I left it as it stands.

Every detail of the 2021 case was verified against the Panel's own case page, which returns HTTP 200
and carries the eligibility findings verbatim, including "no material increase in the rate of road
accidents in Shakpak Baba" and "the acceptable state and maintenance of cattle crossing culverts".
The village, district and the "only one household was compensated" claim are in the 11 February 2021
notice of registration, paragraph 1 and paragraph 8. One spelling corrected: the notice gives
**Tulkubassiy** district, not "Tulkibas". Corrected in `place` and `outcome`.

**"Seven of eight paid" is the Panel's own field finding.** Paragraph 45: "During its visit to Sairam,
the Panel team confirmed that seven of the Requesters had received compensation and were satisfied."
Confirmed as the Panel team's own observation on its 26 September to 1 October 2011 visit. The
officials' version is in the same paragraph and attributed to them: "Project officials in Shymkent
informed the Panel team that all but one of the eight Requesters had agreed on the compensation, and
were paid accordingly."

**But these two are not a disagreement, and the writer's report calls them one.** "All but one of the
eight" and "seven of the eight" are the same number. The quantities differ only in who observed them
— officials' report versus the Panel team's visit — and they agree. This is the invented-conflict
fault the brief warns about. The card itself does not claim a conflict; it carries only the Panel's
version, so nothing in the card needed fixing on this point. Item 3 of the writer's report should be
struck.

---

## Per-case corrections

### `south-west-roads-turkestan-sairam-compensation` — KEPT, `documented`

Confirmed: loan IBRD-76810 US$2.125 billion approved 30 April 2009, signed 13 June 2009, effective
9 December 2009; US$2,102,277,467.99 disbursed, US$366,300,126 borrower, total
US$2,468,577,593.99; category A; OP/BP 4.12; closing 31 December 2024; outcome Satisfactory, Bank
performance Satisfactory, M&E Substantial in both documents' ratings tables, which agree. Corridor at
US$7.5 billion with 37 per cent government financing (Panel report). The 2011 requester (Bauyrzhan
Isaliev of the National Analytical Information Resource, on his own behalf and for NAIR and 24
project-affected people), the four places, the Turkestan commercial facility built in 2008 to open in
2009, the paperwork and technical-certificate dispute, the suspended works, the stated fourth court
application, the Sairam 49-year leases, Management's confirmation of the one-day incursion with
initial scraping and removal of topsoil, the entitlement matrix one-year-versus-remaining-years
conflict, the unseen leaflet, Yntymak's 5 km and 35–40 versus 15–20 metres, Management's agreement
that the Temirlanovka EIA was "largely generic", the Tugai forest and Arys river claims, several
thousand grievances with no exact data recorded, the 42 km of Otar-Uzynagash unfinished after a
terminated contract, the 2010 first request at paragraph 39 — all confirmed.

Corrected:

1. **Safeguard rating attributed to the wrong document, and the two documents do not agree.** The card
   said "safeguard compliance was rated Moderately Satisfactory at closing" and cited both the
   completion report and the Evaluation Group review. The completion report says something narrower:
   paragraph 76, the project's **environmental performance** was rated Moderately Satisfactory **for
   much of the implementation period**. The Evaluation Group broadens this to "safeguard compliance...
   mostly rated Moderately Satisfactory throughout implementation" and separately states "At closing,
   the project's safeguard compliance was rated Moderately Satisfactory." The card now gives both
   wordings with the document that gave each.
2. **The waiver was attributed partly to the completion report, which does not mention it.** The word
   does not appear in the completion report. The waiver is the Panel report's, paragraph 9 and
   paragraphs 15 and footnote 4: reclassification to category A after appraisal, senior management
   agreeing a waiver be sought from the Board concurrently with approval, Board approval on 30 April
   2009. Re-attributed to the Panel report, with the Board date added.
3. **Selective quotation.** The card carried Management's confirmation of the incursion without the
   sentence five paragraphs later that cuts the other way. Added: "Management also observed that the
   requesters did not claim that any material harm resulted from the incursion and proposed no
   specific remedial measures." Also noted in `confidence_note`.
4. **An account from staff, not a document.** `ecosystem` said works were halted, archaeologists were
   engaged and the finds went to a museum. That is not in the completion report, which says only that
   ancient burial sites were found along the Otar-Uzynagash section and were documented by local
   archaeologists. The halting and the museum come from the Evaluation Group review, where they are
   introduced as "The World Bank team stated (August 29, 2025)". Re-attributed, with that said plainly.
5. "acceptable design" corrected to the Management Response's word, "appropriate design".
6. `displaced_note` and `confidence_note`: "opened here" removed (researcher voice).

Tests: documented lender link (IBRD-76810); actual harm — the Turkestan family told to stop a
completed commercial facility in early 2009 with compensation never paid through three court filings
and a fourth planned, and works begun in Sairam on leased land for which compensation was disputed
and unpaid, confirmed by Management, with the eighth leaseholder saying he settled for less than he
was owed; timing overlap throughout 2009–2024. Limb (b) met on compensation unpaid and land taken.

### `hanoi-ring-road-2-relocation` — KEPT, `contested`

Every figure confirmed. Paragraphs 60 and 76 both give "1,541 PAHs, including 714 relocated", and the
Evaluation Group repeats it. Paragraph 76 carries the mid-term findings word for word as the card has
them: following Hanoi People's Committee regulation rather than the framework, no assistance for
illegal residential land, "replacement cost not replacing PAHs' losses", an earlier cut-off date under
the Land Law, disputed eligibility where occupation was classed as illegal, and no assistance for
unregistered businesses. Paragraph 77 carries the rest: social safeguards moderately satisfactory at
closing per the final supervision mission, all activity complete except two outstanding cases,
income-loss and business-restoration payments "very slow", and the request to the Committee to speed
up payment in Tay Ho, Cau Giay and Dong Da. CT1 and the Dao Tan redesign confirmed. Financing
confirmed line by line against the ICR table: IDA-43470 155,210,000 revised 115,901,593 disbursed
107,388,341; TF-58293 9,800,000 of which 6,422,455; borrower 139,680,000 revised 329,300,000 actual
181,409,261; total project cost 304,690,000 at appraisal, 295,220,057 at completion. Nothing corrected
in the figures.

Limb (a) met: 714 households relocated. Limb (b) also met: replacement cost below what households
lost, and no assistance for unregistered businesses.

### `bahia-viver-melhor-ii-resettlement` — KEPT, `contested`

Figures as above. Two rating errors corrected, both in `lenders[0].role`:

1. **Risk to development outcome.** The card said both documents rated it Significant. The completion
   report's ratings summary (C.1) says **Substantial**. Only the Evaluation Group says Significant.
   The Evaluation Group's own comparison table misreports the completion report's rating as
   "Significant", which is how this got in. Corrected and both now named with their document.
2. **Quality of supervision.** The card said Moderately Unsatisfactory with no attribution. The
   completion report rates it **Moderately Satisfactory** twice — table C.2 and paragraph 72 — and
   says so again in paragraph 73 ("given the U rating for Quality at Entry and the MS rating for
   Quality of Supervision"). Only the Evaluation Group rates it Moderately Unsatisfactory. Corrected
   and attributed.

Also corrected: the completion report's quality at entry rating (Unsatisfactory) added, since it was
the reason overall Bank performance fell; "No document opened here records" rewritten.

Limb (a) met: 1,750 families resettled. Limb (b) also met: 795 cases unfinished in January 2014, 661
of them waiting for housing that was promised for August 2014 and August 2015.

### `rurrenabaque-airport-land-compensation` — KEPT, `contested`

Confirmed from the completion report: paragraph 55 on the two landowners, the outstanding payments,
the valuation dispute, the Bank-hired third party, the January 2018 settlement and works starting May
2018; paragraph 67 on 69 grievance cases with three open at closing (two supplier non-payment, one
gender-based violence), the five-month post-closing action plan, the completed therapy, the continuing
legal process, and the CIPTA pickup and two motorcycles delivered in 2017 with legal transfer pending;
paragraph 68 on 28 airport grievance cases and four post-closing complaints about unpaid workers and
subcontractors; AASANA dissolved 1 December 2021 with staff dismissed until the second quarter of 2022;
social safeguards "Satisfactory, but with implementation shortcomings"; 8.5 ha cleared for runway
visibility, about 1,500 animals rescued, environmental liabilities 73 to 18 to 13, the old Muije bridge
beams; IDA-49230 109,500,000 revised 104,005,075 disbursed 80,588,861, borrower 19,700,000 revised to
zero. The Evaluation Group confirms that the pending grievance cases "have been resolved to date".

Corrected:

1. **Title overstated.** "land taken from two owners without payment" — payment was settled in January
   2018, and the expropriation was done by the local government before the Bank became involved.
   Retitled "Rurrenabaque airport: land taken from two owners, payment withheld to 2018", and
   `confidence_note` now says the expropriation predated the Bank.
2. **Ratings missing, and the two documents disagree.** Added, each with its document: the completion
   report rates outcome and Bank performance Moderately Satisfactory, the Evaluation Group rates both
   Moderately Unsatisfactory.
3. `ecosystem`: "about 1,500 animals... were moved" changed to the document's word, "rescued", under an
   assisted migration plan.
4. "opened here" removed; the disbursement difference between the two documents noted.

Limb (b) met: compensation withheld from two identifiable landowners for years during the loan, plus
workers and suppliers unpaid by a subcontractor and a gender-based violence case in the project's own
grievance mechanism.

### `philippines-nrimp2-unpaid-land-claims` — KEPT, `contested`

Confirmed: paragraph 46 on the failure to pay land acquisition claims for linked works built with
government funding beside roads improved under the loan, the misunderstanding of OP 4.12, "Better
safeguards due diligence by the Bank would have also helped to identify these issues earlier", the
right-of-way reduction in the agreed action plan, compensation at two locations unpaid at closing, and
at the time of writing one location paid and the second in escrow awaiting a court decision. Paragraph
115: "DPWH allowed linked road improvement works to proceed without compensation being paid, a clear
non-compliance with Bank involuntary resettlement policy" — confirmed as the completion report's own
words. Paragraph 45: safeguards "fluctuating from Satisfactory at commencement to Moderately
Unsatisfactory". Paragraph 47 and the Evaluation Group both place the debarment of eight contractors
under the earlier phase, NRIMP-1, so the `confidence_note` sentence is right. IBRD-75520 US$232
million approved 13 May 2008, effective 16 April 2009, US$187.84 million disbursed, US$44.2 million
(19 per cent) undisbursed, restructurings 6 December 2012 and 23 December 2014, closing 31 December
2016, AusAID co-financier, category B. Both documents agree on every rating: outcome, risk,
Bank performance and borrower performance all Moderately Satisfactory.

Corrected — **this is the same fault as the Kazakhstan museum sentence**:

1. **A fact that exists only as something staff told the evaluators.** `community` stated that action
   was held up by "changes in field office leadership, including the creation of a new administrative
   region that took over supervision of the sub-project with the delayed compensation". Grepped the
   completion report for "region", "new region" and "leadership": the claim is not there. It is in the
   Evaluation Group review, inside a bullet that opens "The project team informed IEG that during
   supervision...". Removed from `community` and moved into `outcome`, said plainly as what the Bank's
   project team told the evaluators.
2. The same bullet is the only source for "this issue is resolved for most of the PAPs" and the escrow
   funds being kept aside. `outcome` now attributes that to the project team as well, rather than
   presenting it as the Evaluation Group's own record.
3. "opened here" removed.

Limb (b) met: compensation owed to project-affected persons at two locations unpaid at closing, in the
completion report's words a clear non-compliance.

---

## 1. What could not be checked

- **Whether an independent source exists on any of the five kept cases.** Searched for independent
  reporting on the Hanoi Ring Road 2 resettlement and on the Bahia Viver Melhor II resettlement and
  found nothing on point: the Hanoi results are all for other Ring Road projects in Hanoi and Thu Duc,
  and the Bahia results are later Bahia state programmes and unrelated World Bank frameworks. Two
  searches is not an exhaustive test, so the absence claims on these cards are what they say they are
  — nothing was found — and not proof that nothing exists.
- **Whether the Bahia 795 pending cases were ever closed, and how the Philippine court case ended.**
  The last document in each chain is the Evaluation Group review, and neither follows up. The cards say
  so.
- **The two Philippine locations with unpaid claims, and the compensation amounts in Azerbaijan and
  Bolivia.** Not in any disclosed document. Nothing to check against.
- **The amounts and outcomes of the Turkestan litigation.** The Panel report ends with the requester
  saying he would file a fourth court application. Nothing later was found.
- **The Nueva Esperanza point in Usme.** Moot now the Bogotá case is dropped, but the writer's note is
  right that the neighbourhood is not separately mapped.

## 2. Figures where two documents disagree

1. **Bahia, risk to development outcome.** **Substantial** (World Bank Implementation Completion and
   Results Report, 30 April 2014, ratings summary C.1) against **Significant** (Independent Evaluation
   Group ICR Review, 11 June 2014, section 7a). The Evaluation Group's own comparison table prints
   "Significant" in the column headed ICR, which is not what the completion report says.
2. **Bahia, quality of supervision.** **Moderately Satisfactory** (completion report, table C.2 and
   paragraphs 72 and 73) against **Moderately Unsatisfactory** (Evaluation Group review, section 8b).
3. **Bolivia, outcome and Bank performance.** Both **Moderately Satisfactory** (completion report, 31
   May 2024) against both **Moderately Unsatisfactory** (Evaluation Group review, 4 September 2024),
   the outcome because of the weighting after restructuring and Bank performance because of quality at
   entry. The review's own table states the disagreement.
4. **Bolivia, amount disbursed.** **US$80,588,861** (completion report financing table) against
   **US$80,588,721.14** (Evaluation Group data sheet). A difference of US$139.86.
5. **Kazakhstan, what was rated Moderately Satisfactory.** The completion report, paragraph 76, rates
   the project's **environmental performance** Moderately Satisfactory **for much of the implementation
   period**. The Evaluation Group review attributes to that same paragraph a broader claim — the
   project's **safeguard compliance** was "mostly rated Moderately Satisfactory throughout
   implementation" — and separately states that **at closing** safeguard compliance was Moderately
   Satisfactory, which the completion report nowhere says.
6. **Hanoi, revised IDA credit.** The Evaluation Group's text says the credit of US$155.21 million was
   "revised down at restructuring to US$122.32 million of which US$113.81 million was disbursed". The
   completion report's financing table shows the credit revised to US$115,901,593 with US$107,388,341
   disbursed, and US$122,324,048 / US$113,810,796 as the **totals of credit plus Global Environment
   Facility grant**. Not a real disagreement — the review has mislabelled a total as the credit — and
   the card uses the completion report's figures. Noted in `confidence_note` so no one reconciles them
   later.

**Not disagreements, though they were offered as such.** The writer's report lists two that do not
survive checking. "All but one of the eight" and "seven of the eight" in Sairam are the same number
observed by two parties who agree (Panel report, paragraph 45). And the corridor cost of US$7.5
billion against the project cost of US$2.47 billion is a whole corridor against one loan, which the
card already distinguishes. The Bahia 832-at-closing against 795-in-January-2014 is a change over
time, as the writer said, and both are in the completion report.

## 3. Faults appearing in more than one card

1. **A fact or a figure that exists only as something Bank staff told the evaluators, written up as if
   it were in a document.** Two cards. Philippines: the new administrative region that took over
   supervision of the sub-project with the delayed compensation, and the statement that the issue is
   now resolved for most affected persons — both inside an Evaluation Group bullet opening "The project
   team informed IEG that...". Kazakhstan: works halted, archaeologists engaged, finds transferred to a
   museum — inside "The World Bank team stated (August 29, 2025)". The Kazakhstan review has nine such
   attributions. Anything taken from a 2025 Evaluation Group review of a Bank project needs the phrase
   "the World Bank team stated" grepped before the sentence is used, because in the newer review
   template a large share of the substance arrives that way.
2. **A rating stated once and sourced to both documents at the same time.** Three cards: Bahia (two
   ratings, both wrong), Kazakhstan (safeguards) and Bolivia (ratings omitted, and the two documents
   turn out to differ on both of the ones that matter). The newer Evaluation Group template prints an
   ICR column in its own ratings table, and in Bahia that column misquotes the completion report. The
   table is not a safe source for what the completion report said; the completion report's own C.1 and
   C.2 are.
3. **Researcher voice surviving as "opened here".** Five cards: "No Bank document opened here gives",
   "not published in any document opened here", "No document opened here records". All rewritten.
4. **A card kept on the strength of a resettlement the lender reports as a benefit.** Two cards, Bogotá
   and Cartagena, and Baku-Shamakhi is a third variant of the same thing: the harm the card asserts is
   the shape of the project rather than anything the documents record happening to a person. The common
   test that catches all three is to ask what sentence in the document says someone ended up worse off,
   and then to read the sentence after it.

## 4. Things wrong in the card data outside the fields I was asked to check

1. **`companies` is carrying government bodies, not companies, on four cards.** Bogotá lists the
   Secretaría Distrital de Integración Social and IDIGER; Hanoi lists the Hanoi People's Committee and
   the Hanoi Department of Transport; Philippines lists the Department of Public Works and Highways;
   Kazakhstan lists the Committee for Roads. These are ministries, city governments and state
   institutes. The brief says `companies` holds "contractors and operators the documents name". No
   contractor is named on any of the eight cards, because the completion reports do not name them — the
   Philippine, Azerbaijani and Bolivian reports all discuss contractor conduct without giving a single
   contractor's name. Left as the writer had them, since changing the meaning of a field is the lead's
   call, but the field is being used for implementing agencies and the map may want a separate key.
2. **`companies` on the Philippines card lists "Road Watch" as a company.** It is a civil society
   oversight body under the project's anti-corruption measures, named in the completion report. It is
   not a contractor or an operator and it did no harm; listing it beside the Department that allowed
   works without compensation reads as an accusation the documents do not make. Recommend the lead
   remove it.
3. **Bolivia `lenders[0].role` named the wrong triggered policies against the wrong field.** The role
   gave category B triggering OP 4.10, OP 4.11 and OP 4.12, while `ecosystem` gave category B
   triggering OP 4.04 and OP 4.36. Both lists are correct and both are in paragraphs 67 and 69 of the
   completion report, but split across two fields they read as a contradiction. Not changed; flagging
   it.
4. **Kazakhstan `companies[1].role` on KazAvtoZhol is wrong.** The card calls it "State road operator,
   named in the completion report as a co-implementing body the Bank supervised alongside the Committee
   for Roads". The completion report says something different: KazAvtoZhol (JSC National Company
   KazAvtoZhol, KAZh) was **created in 2013 as a joint stock company under the Committee for Roads, at
   the Bank's own recommendation and with the project's support**, to separate road operations from the
   policy-making the Committee retained. It is an output of the loan, not a co-implementer the Bank
   supervised, and it did not exist for the first four years of the loan or at the time of the 2010 and
   2011 Inspection Panel cases. Left in place, because correcting it may mean moving the entity out of
   `companies` altogether, but the role text as written is not supported.
5. **`end` on the Azerbaijan card is 2021 while `start` is 2010, and the only dated harm event in it is
   the 2014 rating downgrade.** Moot now it is dropped, but it is the shape of a card with no event in
   it: a start, an end and no date in between.
6. **The writer's dedupe finding is worth acting on and is not a card fault.** `grep -o 'P[0-9]\{6\}'`
   on `base.html` matched all twelve leads because the file also embeds ICIJ's per-country displacement
   lists as lead data. Brace-matching the case objects and searching only inside them returns no match
   for any of the sixteen P-numbers checked. The round's dedupe should use the case-object form.
