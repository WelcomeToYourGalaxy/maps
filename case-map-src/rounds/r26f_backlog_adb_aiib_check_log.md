# Round 16 fact-check log — batch A (ADB / AIIB accountability-office leads)

Input: `/home/claude/r16/out_A.json` (7 cases, 7 drops). Output: `/home/claude/r16/checked_A.json`.

**Result: 6 cases kept, all 6 corrected, 1 cut. 8 drops (7 inherited, all confirmed; 1 new). 14 lead numbers, 6 to 19, each appearing once.**

Everything below was fetched with `curl` straight from the host and read from the file on disk, not
through a summarising fetch. Direct ADB document and project-page paths served without exception
(HTTP 200 every time). No host was blocked.

---

## Fetch failures, exactly as they occurred

- `https://www.adb.org/sites/default/files/Complaint/1051516/GEO-SUTIP%20T3-2nd%20Annual%20Monitoring%20report-11Nov2019.pdf`
  → **HTTP 404**. The same path with the double-encoded `%2520` that ADB's own site serves
  (`GEO-SUTIP%2520T3-...`) → **HTTP 200**, 6.4 MB. The `%2520` form is kept in the case's source URL.
- `https://www.adb.org/projects/50064-002/main` → **HTTP 404**. `50064-001` is the right id.
- `https://www.adb.org/projects/45148-002/main` → **HTTP 404**; the live sub-ids are 001, 004, 005, 007, 008.
- `https://www.adb.org/publications/rail-too-far`, `/a-rail-too-far`, `/rail-too-far-ospf-india`
  → **HTTP 404** (guessed slugs). The real slug is `/publications/india-delhi-meerut-transit-system-project-complaint`.
- **`business-humanrights.org` is not blocked and did not return a client error.** The writer recorded
  both the English and French Nenskra URLs as returning a client error. Fetched with an ordinary browser
  user-agent, the English URL returns **HTTP 200**, 135 KB. See lead 7.

---

## Cases kept

### lead 6 — `tbilisi-rustavi-ponichala-sutip` — kept, corrected

Opened and read in full: ADB CRP, *Second Annual Monitoring Report*, 11 November 2019 (58 pages,
9,622 words, downloaded); ADB *Semi-Annual Social Monitoring Report, January–June 2018*
(42414-043-smr-en.pdf, 2,962 words).

**The hedge survived and is correct.** The Panel's own words, verified at paragraph 2 of the report:
"while there was strong evidence of noncompliance (i.e., lack of assessment of vibration impact on
building 28a) and this was linked to **likely harm** to the third group of complainants, the new evidence
was not serious enough to merit a separate compliance review." And at paragraph 15: "no construction
activity had occurred in the areas where the complainants reside during the relevant monitoring period."
Both are in the case text, unpromoted. This was the thing I was asked to check hardest here, and the
writer got it right.

Corrections:
- **Un-hedged figures restored to the future tense the Panel uses.** The draft said "312 land plots,
  29.5 hectares and 692 structures to be demolished ... affecting 282 households and 33 businesses."
  The report (para. 11 of section III) says construction of Section 2 "**will involve** acquisition of 312
  land plots with 29.5 hectares of land areas, demolition of 692 structures ... A total of 282 households
  and 33 businesses **will be** affected." Now marked as planned figures, not counts.
- **57 trees re-attributed.** The report says "The CRP **was also informed** that 57 trees falling within
  the national red list ... have already been cut and removed". Now carried as what the Panel was
  informed, not as a Panel finding. Added that the fund had reportedly paid money compensation in advance.
- **Verb and agency fixed on the demolition.** The draft had the Municipal Development Fund demolishing
  a state-owned building "after a request on 11 January 2018". The SMR says the application
  (11.01.2018 N107, N108) came **from residents of building #8** asking for the state-owned two-storey
  building to be dismantled and the debris removed, and "The MDF satisfied their request". Added the
  next sentence too, which the draft dropped: one claimant whose property had been transferred to state
  ownership through expropriation "left the building on own accord, as a result of negotiations."
- Loan written as **3063-GEO**. Date label fixed: 18 July 2020 is "the revised project closure date **as
  per website disclosure**", not a bare fact.
- The 40/41 apartment inconsistency the writer flagged is real and is in one document: the narrative says
  a two-storey building with 40 apartments, the account of the 2015 Nord Est Progetti structural study
  says 41, and the table says all 192 properties including all 41 apartments were acquired. Both printed,
  no reconciliation, which is what the brief requires.
- Title changed from "homes bought out, red-list trees felled" to the figures: "435 properties bought
  out, 57 red-list trees cut".

Verified unchanged: 243 of 244 under LARP 2a with GMP Pharmaceutical Company the remainder; all 192 and
all 151 and all 41 under LARP 2b; the 160,000 m³ dump (the Panel's words: "According to estimates
prepared by MDF"); the retaining wall in the Mtkvari bed; the 560 m / 880 m / 188 m noise package; the
95 visually impaired residents split 10 / 8 / 35 / 42; the complainants' properties not being required
by the project; $73m of $118.2m, category A resettlement / B environment.

### lead 12 — `peshawar-landfill-ghari-faiz-ullah` — kept, **confidence downgraded to `contested`**

Opened: ADB, *Implementable Corrective Action Plan*, April 2023 (51036-002-ecar-en_1.pdf, **137 pages**,
36,483 words — the writer said 64 pages; the page footers read "Page n of 64" but the file is 137 pages).
Read the main body in full, roughly the first 30 pages, and searched the annexes for every figure used.
Also ADB project page 51036-002, and ADB's Accountability Mechanism Annual Report 2022 page for CRP 2022/5.

**Both quoted items verified verbatim.** Paragraph 8: the process "did not meet the principles of ADB's
Safeguard Policy Statement (SPS) 2009 as the land was acquired using section-17/4/6 the urgency clause of
the Land Acquisition Act (LAA) 1894 which denies the people right to appeal and record their concerns".
Paragraph 36: "The Independent Valuation Study (IVS) worked out the differential of 31.43 % for the 99
acres' land affected in the land fill site", PKR 157,808,199 (LAC) against PKR 207,411,811 (IVS), gap PKR
49,603,612. Paragraph 7: "Payments to 85 landowners of PKR 39 million is pending". CAP budget grand total
PKR 238,752,828. All five consultation quotes verified word for word.

**The timing test, tested, and the answer is mixed — which is why this is now `contested`.** The
continuing non-payment *is* documented as continuing during the loan: ADB's own April 2023 plan, sixteen
months after the 10 December 2021 approval, still records 85 of 234 owners and PKR 39 million unpaid, and
records the site as having been "used as an open waste dumping site" since handover in 2018. But the same
document says, in a sentence the draft omitted: **"The land was acquired by LG&RD as a part of its
development plan for the city and not in anticipation of ADB's financing."** That is the lender's own
statement that the 2017 taking was not for its money. Against it: ADB brought the site into its project,
made the plan a condition, required the 31.43 per cent differential to be paid, and records that the KP
Government "requested the Mission to use part of the ADB loan proceeds for the purpose of land
acquisition and resettlements (to reimburse compensation payments ...)". Both sides are now in
`confidence_note`; neither is reconciled.

Other corrections:
- "24 subprojects approved" **cut** — not on ADB's project page and not found anywhere I opened.
- CRP 2022/5 paraphrase fixed to ADB's own words: ADB's page says the complainants "withdrew their
  complaint **following receipt of adequate compensation**", not "after receiving what they considered
  adequate compensation" — the draft's version shifts a bank statement into a complainant belief.
- **One unverified internal-inconsistency claim removed.** The draft asserted the document "says all the
  scavengers are teenage boys aged 13 to 18 while its Annex 3 lists ages from 5 to 53". That is an absence
  / inconsistency claim about a 137-page document and I did not substantiate it, so it is out rather than
  repeated.
- Added, because the source publishes it and the owner decides what to leave out: 98 per cent of the land
  is barren storm-water catchment; 20.8 per cent came from one owner holding 20.59 acres with only 1.5
  acres agricultural; 29 of the 85 unpaid owners are women; the vulnerability split is 63 total = 43
  landowners (39 below poverty line on under PKR 20,000/month, 4 women-headed) + 20 waste collectors.
- Loan numbers and dates verified against ADB's page: loan 4160-PAK $380.00m and grant 0816-PAK $5.00m,
  approved 10 Dec 2021, signed 15 Dec 2021, effective 11 Apr 2022, closing 30 Jun 2028; AIIB loan
  8412-PAK $200.00m cofinancing, **approval 16 Dec 2021, signing 15 Dec 2021** (as ADB prints it),
  effective 11 May 2022. Category A environment, A involuntary resettlement. Up to 3.5 million people.

### lead 14 — `sahiwal-piciip-land-and-sewage` — kept, **land half entirely re-sourced; Devdiscourse removed**

This was the first thing I was asked to settle, and the answer is that the figures are right but the
source was wrong. ADB publishes its own account.

Opened and read in full: **ADB, *Taking Less Land: An OSPF-Led Solution for a Wastewater Treatment Plant
Project*, Office of the Special Project Facilitator, 2025** (publication 1074476, 3,481 words); ADB CRP
*Report on Eligibility, Request 2026/6*, 25 September 2026 (**read in full, body and both annexes**);
ADB social monitoring reports 46526-007-smr-en_10 (6th semiannual, Jan 2023), _16, _17, _19, _21
(semestral Jul–Dec 2024), _23 (semestral Jan–Jun 2025); ADB project page 46526-007; ADB Accountability
Mechanism Annual Report 2025.

**Every one of the four figures the writer flagged is verified, from ADB's own text:**
- "The complainants are composed of **18 households**, who were the owners or occupiers of **40 acres** of
  the **196.35 acres** acquired by the PMU to build a wastewater treatment plant in Sahiwal."
- "the total land area slated for denotification had to be reduced from **20.220 acres to 15.275 acres**."
- "On **20 January 2024**, OSPF's facilitation ended in a joint meeting in Lahore, where the complainants
  and the project team signed a memorandum of understanding."
- The 6–7 May 2024 Sahiwal meeting "resulted in **17 out of 18 households** submitting their applications
  for compensation vouchers and receiving their payments ... even as one household faced delays due to the
  need to transfer land records to legal heirs."

196.35 acres is independently confirmed in ADB's borrower-prepared social monitoring reports, which add
figures the draft did not have: **142 displaced persons, 271 trees, 10 irrigation tube wells and 21
building structures** affected by the plant land take. So the land is not merely notified — ADB's
publication says "acquired" — and the land half stands on ADB's own documents alone. The question of
whether the 2026 sewer works could stand alone does not arise.

Corrections:
- Loan number added: **3562-PAK** (ADB project page; the CRP report's footnote 3 prints "Loan 2562-PAK",
  which the project page contradicts — I used the project page). Cofinancing 0.00.
- **Verb fixed.** The draft: "the Punjab Board of Revenue then **ruled** that land could not be denotified
  for some owners only". ADB's text: the Board of Revenue **advised** that the Land Acquisition Rules did
  not permit the agreed denotification, and it was the PMU's **legal team** that told it the Board
  *believed* all original owners must be given the chance to buy back. Three different acts. Rewritten.
- **The "about three months" of standing sewage was promoted and is now un-promoted.** That figure is from
  the complaint only. What the Panel records the authorities accepting (para. 45) is that overflowing and
  stagnant sewage "was occurring as described by the Complainants **during the time the bypass was
  created**", and that it was dewatered "within 48 hours of the complaint being registered". The Panel's
  own finding (para. 64) is that the complainants experienced the impacts "**variously between the periods
  of April to May 2026**". Both durations are now printed with their sources and no reconciliation is
  offered. The draft's `ecosystem` field asserted three months as fact, attributed to the CRP; fixed.
- **"Grave inconvenience" re-attributed.** The draft wrote that the Panel "records that the complainants
  ... 'faced grave inconvenience'". Paragraph 47 reads "the **Complainants said** that until the dewatering
  was carried out, the Complainants and their families faced grave inconvenience". It is their statement
  to the Panel.
- The draft's claim that the Panel "found these construction impacts real and recognised by the project"
  is replaced with the Panel's actual sentence, which is stronger and more specific (para. 64, quoted in
  the case).
- **Shop losses: checked, and the draft did not promote them.** They appear only as the complainant's own
  words ("financial business loss of shops"), in the complaint annex. Left as an allegation, and the
  `confidence_note` says the Panel made no finding on them.
- **Two ADB documents disagree and both are now printed.** The publication says 18 households; the
  monitoring report for Jul–Dec 2024 says the 15.275 acres "belongs to 16 DPs"; the Accountability
  Mechanism Annual Report 2025 calls the avoided acquisition "15–20 acres". No source explains the gaps.
- The draft's note that the Panel report "was cut off part way through Management's response at paragraph
  25" was an artefact of how it was fetched. I downloaded the PDF; the text is complete and I read all of it.
- Complaint ids added: **SPF-2022-16-02-0136** and **SPF-2023-07-04-0146** (named in footnote 2 of ADB's
  publication), in `cx` and `complaint_links`.
- The complainants' own words from their complaint form added, since ADB publishes them.

### lead 15 — `batumi-bypass-land-valuation` — kept, **loan number settled; EUR figure re-sourced**

The second thing I was asked to settle. **Loan 3520-GEO *is* the Batumi bypass loan**, from an ADB source
that names the project: ADB's project page for **50064-001, "Batumi Bypass Road Project"**, lists under
Source of Funding, verbatim:

- `Loan 3520-GEO: Batumi Bypass Road Project` — Ordinary capital resources — `US$ 114.00 million`
- `Loan 8328-GEO: Batumi Bypass Road Project` — Asian Infrastructure Investment Bank — `US$ 114.00 million`

with milestones: loan 3520 approved **28 Mar 2017**, signed **12 Jun 2017**, effective 11 Oct 2017,
closing 31 Dec 2023 revised 31 Dec 2026; loan 8328 approved **15 Jun 2017**, signed **17 Jun 2017**,
effective 12 Oct 2017. So the loan number and both signing dates are right, and the AIIB loan now has its
own number, which the draft did not have.

The writer's warning about its third source was accurate and I removed the source. I downloaded
`50064-001-smr-en_23.pdf`: its title page reads "Project Number: 50064-001 / Compliance Report No. 2 /
Georgia: Batumi Bypass Road Project" but the subtitle and body are "LARP for Lot 2 – Stage 1:
Poti–Grigoleti: Construction of Poti Bridge and Access Roads, Segment 3: Km 0.452 – Km 0.880" (15 hits
for Poti/Grigoleti against 6 for "Batumi bypass"). The project covers more than the bypass — ADB's own
Lessons Learned lists 200 km of highways, a new Poti Bridge and a Bakurtsikhe–Tsnori road under the same
loan — so the document is correctly filed but is not about the bypass. It is gone; the loan facts now come
from the project page.

**The money figures disagree and are all printed, unreconciled**, because no source explains the gaps:
AIIB's own document (verified verbatim): "Total Project Cost: USD 315.2 million; USD 114.0 million (AIIB),
EUR 108.2 (ADB), and USD 87.2 million (Govt. of Georgia)". ADB's Lessons Learned: "The $228 million Batumi
Bypass Road Project is ADB's first cofinanced project with the Asian Infrastructure Investment Bank in
Georgia". ADB's project page: ADB 114.00, counterpart 87.20, project cost 201.20. The draft presented EUR
108.2m as ADB's share flatly; it is now given as AIIB's figure for ADB's share, beside ADB's own $114.00m.

OSPF figures, read in full in ADB's Lessons Learned publication (641201, 7,314 words), all verified:
963 privately owned parcels, 46 hectares of private land to be acquired, 741 affected households
comprising 4,051 affected persons, 369 households "have been or will be" physically displaced. Colliers
International verified: engaged by ADB's Central and West Asia Department as external valuation expert
under International Valuation Standards 2017, inspection and valuation 5 March 2019, effective valuation
date 1 November 2016, "determined that the value of the property was about 20% higher than the original
project valuation", negotiated contract signed 27 June 2019, "full payment of the amount was confirmed on
**29 June 2019**".

Corrections:
- **A hedge was dropped and is restored.** The draft: "562 households, 3,024 people, **are** severely
  affected". The source: "562 AHs, comprising 3,024 APs, **have been or will be** severely affected".
- Added OSPF's own hedge, which the draft omitted: it "found that there was indeed a **possibility** of
  undervaluation of the complainant's property and urged the RD to reopen the case."
- Added that the government's position was that the compensation was fair and the claim unsubstantiated —
  the other side, which the draft left out.
- Project approval date **28 March 2017** added; `end` set to 2019.
- Title changed to "one house priced 20 per cent below an independent valuation", which is what the
  document found.

### lead 18 — `kolkata-keiip-tranche2-vendors` — kept, `contested`, **275 figure re-attributed**

Opened: ADB CRP *Report on Eligibility, Request 2026/4*, dated **2 September 2026**
(IND-Kolkata-ER-ForWeb.pdf, 45,454 words). Read paragraphs 1–70 in full and searched the annexes for
every figure and quote used.

**The verification document exists and says it, but not in the voice the draft gave it.** Paragraph 31:
"**The Response stated** that 121 PAPs under Package SD13 and 154 PAPs under Package WS16 were identified
through a field verification conducted immediately before the implementation." It is **ADB Management's
response to the Panel in a complaint against ADB**, summarised by the Panel — not a Panel finding and not
an independent verification. The draft called it "ADB's own verification identified 275 affected persons"
and said in `confidence_note` that "What is not in dispute is that 275 roadside vendors lost trade". Both
are now rewritten: it is the financier's own count, the only count there is, untested by the Panel or
anyone else. That is still enough for test 2 — the lender records 275 people losing income to its works —
but it is not an uncontested fact.

**The ineligibility tells nothing, as instructed, and the case does not rest on it.** Paragraph 70: the
determination "should not be understood as a finding on ADB's compliance or noncompliance ... the alleged
harms, or the causal relationship between the alleged harms and the ADB-financed project." Paragraph 68:
it "should not be understood as accepting or rejecting either the Complainants' allegations or
Management's positions." Both now in the case.

**Both sides present, neither reconciled**, as required: the complainants' dismantled-shops account
(verbatim: "prohibited from returning to our sites of operation and some of us even detained, when
attempting to"; "hand-held tea or other carts"; "We are still waiting to have our previous shops back,
and with them, our former earnings"; INR 15,000 each on **18 August 2019**; shops held 25 to 30 years;
about 124 others on their list; Growthwatch India as representative) **and** Management's position
(verbatim: "ADB staff found no records showing that the Project required the permanent demolition of
roadside shops"; the verification "confirmed there was no physical displacement or permanent loss of
livelihood"; the 2019 Indian Social Action Forum / NGO Forum on ADB review of four shopkeepers finding
their structures intact and paid; the KMC road widening begun **17 February 2023**, which ADB says it
neither financed nor supervised).

Also verified: 30 days of livelihood assistance raised from an initial 10-day assessment and exceeding the
approved entitlement matrix; 24 estimated against 121 verified for SD13 with "does not indicate any
concealment or underreporting"; 1,647 grievances, 81 under SD13, 29 under WS16; Simplex Infrastructures
Ltd awarded SD13 on 11 November 2016; Furnace Fabrica India Ltd and Ramky Infrastructure Ltd JV awarded
WS16 on 28 March 2017, works from 19 May 2017 to 28 February 2023; open-cut trunk sewer restored 31
December 2022; loan closing 31 August 2023 (memo of 20 October 2022, never further extended), financial
closing 14 June 2024, complaint filed 13 June 2026, cutoff 31 August 2025.

Corrections: attribution throughout; "found the complaint ineligible on 2 September 2026" → "in its Report
on Eligibility dated 2 September 2026" (that is the report's date; the PDF prints no separate
determination date); added the Panel's finding that the data sheet was "not self-explanatory" and that the
representative "could reasonably have understood 14 June 2024 to be the relevant date"; title rewritten so
the two accounts sit side by side rather than the count reading as settled.

### lead 19 — `malolos-clark-railway-row-pampanga` — kept, corrected

Opened and read in full: both VERA Files articles; ADB's complaint register page for the 2026 complaint.

All six items I was asked to verify check out, in VERA Files' own words:
- "As of October 2024, the DOTr has 'successfully acquired' **31 parcels** of land across the alignment.
  This totals to **4.9 hectares** out of the estimated **45.5 hectares**".
- "In Pampanga alone, out of **1,936** ISFs, only **112** have been relocated" — and "Less than 5% of the
  total ISFs affected by the MCRP have been verified and resettled **as of September 2024**".
- "San Fernando has **67 row houses built and occupied in Barangay Calulut as of October 2024**, while 312
  housing units in Barangay Panipuan are ready for occupancy."
- Rosa Lebosana, 41, Barangay Maimpis, 50 m² house since 2003, "the house was surveyed and tagged on
  **Nov. 9, 2018**" and "**Six years after the first tagging**, Lebosana said the Department of
  Transportation (DOTr) has not followed through."
- JICA's 2018 census 1,416 potentially affected households; ISFs affected up about 108.70% against NHA's
  2024 data; relocation site 9.7 km away with an NHA housing loan and an LGU land title.
- "Without these prerequisites, **the demolition of houses along the main railway line cannot proceed**."

**The October 2026 complaint is recorded as an allegation, correctly.** ADB's register page verified:
"Date Received | Request ID — 07 Oct 2026 | SPF-2026-43-04-0263 / Project Number 52083-001 / Sector
Transport / Issues **House demolition without compensation** / Status 7 October 2026". It is a register
issue line with no outcome, and the case says so.

Corrections:
- **SPF-2026-43-04-0263, the complaint actually quoted in the case text, was missing from `cx` and
  `complaint_links`.** Added to both.
- Added **Italian-Thai Development Public Company Limited** (Bangkok) as the N-03 civil works contractor,
  which VERA Files names and the draft dropped; the 30-per-cent-workable figure is now attached to the
  company it describes, as the source attaches it.
- $2.75bn ADB / $2bn JICA, $1.3bn first tranche, P66.83bn at the 11 July 2019 rate, validity extended
  21 Dec 2021 → 21 Dec 2022 → 30 Jun 2024, P47.40bn disbursed by Dec 2023, P74.67m commitment fees in
  2022 at 0.15% a year, 12.3% EIRR and "the analysis shows the project remains viable in all cases",
  four ROWSA staff at the start and 48 by October 2024 against a target of 137, 28.97% complete in San
  Fernando, 2027 → 2028 → 2029 — all verified word for word.

---

## Cut

### lead 16 — `colombo-wastewater-house-damage-cmc` — **CUT. A grievance that was settled, not documented harm.**

Asked to say plainly which it is, and it is the latter.

I downloaded ADB's *Final Report of the Special Project Facilitator*, SPF-2019-12-03-0092, October 2023
(project 36173-013, loans 2557 and 2558) and **read all 2,340 words of it**. The absence claim in the
draft is correct and I can now stand behind it on a full reading: the report names no street, no ward, no
cracks, no structural finding and no number of affected houses.

The reason to cut is not the scale. It is that **nothing in the record says what the damage was or that
the project caused it.** The one payment tied to the house is SLRs121,000, paid 5 December 2017, which the
report calls "the estimated cost of repair works directly related to his house" — a repair estimate the
implementing agency paid, not a survey of damage. Where the report mentions damage at all it is as the
complainants' claim: paragraph 13, "They **alleged** that they were entitled to further compensation for
construction damage." And the project fact sheet printed in the same report says the works were limited to
upgrading existing sewerage within existing physical facilities and that the project "will not require
permanent or temporary land acquisition and **there will be no impact on permanent structures or other
assets**." The health claim was rejected by the Colombo Municipal Council as not caused by construction.
Everything was paid or approved before closure: ADB's own finding, paragraph 15, is that "almost all the
requests of complainants for payment relating to the impact of the Project on their property and
well-being have already been paid and/or have been approved by CMC", and the Special Project Facilitator
advised the complainants that the council's final offer "appeared to be consistent with ADB policies". The
case closed because the parties could not agree on advance payment of *future* hospital bills and the
council would not continue. The two earlier complaints were found ineligible and carry no findings.

A repair estimate paid out, with no document recording either the damage or its cause, is a settled
grievance. Under test 2 it does not pass.

---

## The merge-critical Colombo project numbers — **both confirmed, and an EIB Colombo case is a different project**

Checked against ADB's and the EIB record's own pages, not the writer's note.

1. **ADB project 36173-013, "Greater Colombo Wastewater Management Project"** — ADB's project page lists
   `Loan 2557-SRI` (ordinary capital resources, US$80.00 million) and `Loan 2558-SRI`, approved 28
   September 2009, and gives **`Cofinancing 0.00`** for both loans. There is no EIB money in this project.
   Confirmed as the writer said.

2. **ADB project 45148, "Greater Colombo Water and Wastewater Management Improvement Investment Program"**
   — confirmed as the separately numbered later program, with live sub-ids 004 (Facility Concept), 005
   (Tranche 1, loans 2947/2948-SRI), 007 (Tranche 2, loans 3029/3030/8282-SRI) and 008 (Tranche 3, loans
   3348/3349-SRI). **And ADB's own pages for 45148-008 and 45148-004 list, under Source of Funding, a
   `European Investment Bank` loan of `US$ 50.00 million`.** The Early Warning System record for
   EIB-20140457 gives "Bank reported 50" (EUR 50m, converted to $53.51m at the 20 January 2017 rate), a
   voting date of 20 January 2017, project cost $166.94m, and describes the project as "As part of the
   Greater Colombo Water and Wastewater Management Improvement Investment Program initiated by the Asian
   Development Bank (ADB)".

**Verdict for the main session: an EIB Colombo wastewater case would be a distinct project, not the same
one.** It belongs to ADB project 45148, tranche 3 / project 3, where ADB's own page names the EIB's $50
million as a co-financing source — a different ADB project number, different loan numbers, a different
decade and a different catchment (the EWS record describes Colombo's **south** catchment). The ADB
complaints in this batch's lead are all against 36173-013, which has no co-financier at all. The second
checker's EIB Colombo item can stand as its own case without colliding with anything here, and if it is
written it should carry ADB as co-financier under 45148 rather than EIB alone. Nothing in my batch
overlaps it, because lead 16 is cut.

---

## Drops — all 8 checked, all stand

### Already on the map (confirmed against `/home/claude/cases.json`, 947 records)

| lead | drop target | in cases.json | checked |
|---|---|---|---|
| 10 | Nepal transmission / FPIC | `lapsiphedi-substation-tamang` | **Yes.** Its `cx` already carries `CRP 2025/7`, `SPF-2025-08-02-0199` (two records) and `CRO 2025-15-a`, ADB as lender, Lapsiphedi ward 3 Kathmandu, 2017–. No new co-lender, so no extend. |
| 11 | Karachi BRT Red Line | `karachi-brt-red-line-university-road` | **Yes.** Already names ADB, AIIB, Agence Française de Développement **and** the Green Climate Fund, and already carries seven 2026 SPF register entries. Nothing to add, so no extend. |
| 13 | Jalalpur Irrigation | `jalalpur-canal-land-flooding` | **Yes.** ADB-only lender, Jhelum to Khushab, 2018–, with eight-plus SPF register entries from 2023 to 2026 in `cx`. No extend. |

### Dropped on the merits

- **lead 7, Nenskra — drop stands, and the open item is closed.** I retried the
  business-humanrights.org page the writer could not open. **It returns HTTP 200** with an ordinary
  browser user-agent — the recorded "client error" was a fetch-method artefact, exactly the failure mode
  CHECK16 warns about. It is dated **10 October 2017, not later**, and is only a pointer to the same
  Bankwatch report plus a company response from JSC Nenskra Hydro. I then went to the underlying report
  itself: Bankwatch, *Failing local communities: Report on the Land Assessment and Livelihoods Restoration
  Plan for the Nenskra Hydropower Project*, September 2017, downloaded and **read in full, 9,138 words**.
  Every loss in it is prospective — households "would lose" compensation, "will lose" access and income,
  pastures and cabins described as inside the "land take area". It records **no completed acquisition and
  no completed loss**. So the one item that would have shown land was actually acquired does not show it.
  The writer did not stop early; it just could not open the page, and the page was not what it thought.
- **lead 8, Assam Solar — drop stands, now on ADB's own words.** ADB's Accountability Mechanism Annual
  Report 2025: the CRP "found preliminary evidence of noncompliance in several areas" and "recommended
  that the Board authorize a compliance review. However, after the Government of India formally withdrew
  its request for ADB financing, the complaint no longer related to an ADB-financed project and fell
  outside the compliance review mandate." A hedged preliminary finding about the lender, with no ADB money
  ever in place. Tests 1, 2 and 3 all fail.
- **lead 9, Georgian Railway green bond — drop stands, and the Panel's reasoning now comes from ADB
  rather than from press reporting of it.** The draft quoted the Panel through Sakartvelos Ambebi. ADB's
  own Annual Report 2025 states it directly: "the CRP determined that the complaint was not admissible.
  The CRP found that **ADB financing had not been used for new railway lines or tunnel-related works, and
  that the alleged impacts related to activities outside the scope of ADB financing**." ADB's register
  gives complaint 2025-118, received 17 October 2025, project 55132-001, forwarded to the CRP 7 November
  2025. The harm is real and documented; the link is not. Correctly dropped on the link test. The
  writer's note that this becomes a case if a future document ties the blasting to an ADB-financed
  component is the right standing instruction.
- **lead 17, Delhi–Meerut — drop stands, checked against the one document the writer named but did not
  open.** I downloaded ADB's publication *A Rail Too Far? India's Delhi–Meerut Regional Rapid Transit
  System Investment Project Complaint* (publication 1064011) and **read it in full, 3,410 words**. It
  records **no damage found**. The structural work is baseline only: an independent structural engineer
  was brought in "to conduct a baseline survey to assess the structural stability of the homes **before**
  the beginning" of works, pre-construction surveys of 14 of the 16 apartments had been done, and the
  company "agreed to fix any damage reported by the experts **after** construction". On land: 24
  apartments were initially declared as needing purchase, after the alignment changed only eight "needed
  to be acquired", and the company reached agreements with three of those eight. No completed
  acquisition, no completed move, no recorded damage. Measures to catch damage if it happens are not
  damage, as the writer said. Drop confirmed.

---

## Dedupe and coordinates

Checked each kept case against `cases.json` by iso3, project name, years and coordinates within ~50 km.
Three near-coincidences, all different projects and all genuinely new:

- Sahiwal (30.666, 73.106) sits about 14 km from `sahiwal-coal-plant-qadirabad` (30.7153, 73.2389). Same
  city, different project, different lender role — a coal plant, not ADB water and sanitation. Not a
  duplicate.
- Peshawar landfill (33.88, 71.55) sits about 15 km from `peshawar-brt-traders-underpasses` (34.0151,
  71.5823). Different project (BRT traders, not the solid-waste landfill). Not a duplicate.
- Ponichala (41.645, 44.875) sits about 10 km from `aes-telasi-tbilisi` (41.7225, 44.7925), which is
  electricity disconnections. Not a duplicate.

Coordinates spot-checked against the named places: Sahiwal city ≈ 30.67 N 73.11 E; Ponichala is in
southern Tbilisi on the Rustavi highway; the Batumi bypass runs east of Batumi (41.65 N 41.64 E); Ghari
Faiz Ullah near Shamshato camp lies south of Peshawar; M.G. Road Kolkata ≈ 22.58 N 88.36 E; Barangay
Maimpis, San Fernando ≈ 15.03 N 120.69 E. All six kept cases carry `ap: true`, which is right — every one
is a district- or corridor-level point and none of the documents gives coordinates.

---

## Patterns worth carrying forward

1. **ADB publishes its own version of nearly every OSPF case, and it is findable.** The Sahiwal land half
   rested on a Devdiscourse rewrite; ADB's own 2025 publication *Taking Less Land* carries every figure,
   and its social monitoring reports carry more. The pattern: for any OSPF problem-solving case, look for
   an ADB "problem-solving impact story" or "Lessons Learned" publication plus the project's
   `-smr-en_N.pdf` series before accepting any aggregator. In this batch that route replaced one bad
   source and verified or added figures in four cases.
2. **Download the PDF; do not read it through a fetch tool.** Two of the draft's self-reported limits —
   "cut off part way through Management's response at paragraph 25" (Sahiwal) and "I read about 50 of its
   64 pages" (Peshawar, actually 137 pages) — were artefacts of the fetch method, not of the documents.
   `curl` plus `pdftotext` gave complete text in every case, and it is what makes an absence claim worth
   anything.
3. **"This host returned a client error" was wrong again, for the tenth time in this project.**
   business-humanrights.org returns HTTP 200 with a browser user-agent. It cost the writer the one item it
   itself identified as decisive.
4. **A figure in a Management Response is not a verified figure.** The Kolkata 275 reads in the Panel's
   report as "The Response stated that...". Two of this batch's four attribution errors were of this
   shape: a lender's self-report, or a complainant's statement to the office, written up as the office's
   finding. Worth a standing check: for every number, ask whose sentence it is in.
5. **The hedge check came out better than expected.** Of the three places a hedge could have been promoted,
   the writer preserved two cleanly (the Tbilisi "likely harm", which it flagged itself, and the Batumi
   "have been or will be" on physical displacement) and lost two smaller ones (the Batumi "severely
   affected", the Sahiwal three months). The flagged weak points were all real weak points — the writer's
   self-assessment was accurate every time, which made this check much faster.
6. **ADB's own documents sometimes say the harm pre-dates the money, in plain words.** The Peshawar plan's
   "not in anticipation of ADB's financing" is the kind of sentence worth grepping for in any legacy-issue
   corrective action plan: it is the lender disclaiming the link, and it belongs in `confidence_note`
   rather than being left out.
7. **ADB's `%2520` URLs.** Several of ADB's older complaint-document paths are served only in
   double-encoded form; the clean `%20` version 404s. Keep the URL exactly as the search result gives it.
