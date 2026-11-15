# Round 26f ICIJ tranche 6 — `conditions` prose for the eight China World Bank cases

Written against `docs/CONDR.md` and the round 20 section of `docs/HANDOFF.md`
("Conditions prose for the ten cases that arrived without it"). Output file:
`rounds/r26f_icij6_conds.json`, one object per case id with `conditions_add`, `ct` and `why`.

## Documents used

Seven of the eight projects had their appraisal document and completion report already on disk in
`/home/claude/r22/cache`. One fetch was made: the 2002 appraisal document for P068049, which the
cache did not hold. It came from the World Bank documents API
(`search.worldbank.org/api/v3/wds`, `qterm=Hubei Hydropower Development in Poor Areas appraisal`),
was downloaded from `documents1.worldbank.org/curated/en/152611468769172425/pdf/multi0page.pdf`
and converted with `pdftotext -layout`. It is saved as `P068049_PAD.pdf` and `P068049_PAD.txt` in
the same cache folder. Nothing was deleted.

Three appraisal templates are in play, as round 20 recorded, and they are not interchangeable:

| Project | Template | Where the obligations are printed |
|---|---|---|
| P069852 (2004) | prose | section G "Main Conditions", G.1 and G.2.1–G.2.3.5 |
| P068049 (2002) | prose | section G "Main Loan Conditions", plus Annex 6 for the disbursement condition |
| P091950 (2009) | prose + data-sheet repeat | section III.F, paragraphs 47–50; data sheet "Significant, non-standard conditions" |
| P114107 (2009) | prose + data-sheet repeat | section G, paragraph 105; Annex 7, paragraph 12 |
| P117656 (2011) | prose + data-sheet repeat | section III.E; data sheet |
| P118597 (2012) | data-sheet tables | "Legal Covenants" table, nine rows; no "Conditions" table printed |
| P126210 (2012) | data-sheet tables | "Legal Covenants" table, six rows; "Conditions" table reads "Not applicable" |
| P129431 (2013) | data-sheet tables | "Legal Covenants" table, two rows; "Conditions" table, one effectiveness row |

## Per case

### guizhou-heritage-sites-demolition (P091950)
- **No loan effectiveness condition.** PAD 7 Apr 2009, section III.F, paragraph 48: "Loan
  Effectiveness Condition: There is no loan effectiveness condition." Repeated in the data sheet.
- **Dated covenant, Community Project Management Group and Village Supervision Group at each
  selected minority village by 15 September 2009**, terms of reference, staffing and resources
  acceptable to the Bank, as set out in the Operation Manual for Community Participation. PAD
  paragraph 49; data-sheet "Dated Implementation Covenant".
- **Carry out the project in accordance with the OMCP; prior Bank approval for any amendment.**
  PAD paragraph 50(a).
- **Cause project participants to implement Guizhou Guidance No. 30 of 2007** (Provincial Party
  Commission and provincial government, 28 November 2007) on safeguarding ethnic minority
  interests and cultural heritage in rural tourism development. PAD paragraph 50(b).
- **Financial covenants:** PAD Annex 7, paragraph 34 — "No specific financial management covenants
  are applicable to the project except for those standard financial covenants such as project audit
  and interim financial reports."
- **No resettlement covenant among the three.** The consolidated RAP and RPF were prepared under
  OP/BP 4.12 (PAD paragraph 64). The temporary-resettlement rule broken at Huangping Jiuzhou is in
  the RPF: ICR00004154, 18 December 2017, footnote 7 and the safeguards paragraph, which says the
  renovation went ahead "without the appropriate procedures set forth in the RPF". The ICR prints
  no covenant-compliance table.
- `ct`: admin, safeguard.

### kunming-line-3-jinmasi-relocation (P117656)
- **Three disbursement conditions on the works category** (civil works, goods, consultant services
  and training): Subsidiary Agreement executed on behalf of the Kunming Municipal Government and
  Kunming Rail Transit Company; duly authorised or ratified and legally binding on both; and the
  company "has secured the land required for metro - public transport - bicycle integration
  according to the Integration Plan, in form and substance acceptable to the Bank." PAD 14 Apr
  2011, section III.E; identical text in the data sheet.
- **Annual action plan covenant**, by 15 February each year from 2012, with scope, schedule,
  financing plan and detailed budget including validated counterpart funds, for Bank review and
  approval; then carry out the works in accordance with the approved plan; then prior Bank
  concurrence for any modification or waiver. PAD section III.E, implementation covenants (a)–(c).
- **Reporting:** half-yearly reports on the Environmental Management Plan and the Resettlement
  Action Plan; semi-annual progress reports by 15 February and 15 August each year from August
  2011; mid-term review report by 31 December 2012. PAD section III.F, paragraph 40.
- **Financial covenants:** PAD Annex 7, paragraph 27 — "No specific financial covenants are
  applicable to the project except for standard financial covenants, e.g., project audit and
  interim financial reports."
- The RAP appears only in the reporting requirements; no covenant in section III.E requires it to
  be carried out.
- `ct`: admin, safeguard, land.

### hunan-gansu-small-towns-demolition (P118597)
All nine rows of the PAD data-sheet "Legal Covenants" table, 23 April 2012, each recurrent and
yearly, binding each provincial implementing entity:
1. Project Implementation Arrangement — maintain a Provincial Project Leading Group or Coordinating
   Group, a Provincial Project Management Office and a County Project Management Office.
2. Project Implementation Plan — carry out activities in accordance with the Plan and the Project
   Agreement.
3. Safeguards Framework-RAP — "shall, apply and caused to be applied the measures and actions set
   forth in its RAP in a timely and efficient manner satisfactory to the Bank."
4. Safeguards Framework-ECOP and PMP — implement the environmental codes of practice and the pest
   management plan; Gansu also its EMDP, Hunan its EMP.
5. Process Framework — "carry out measures for improving the living standard of Displaced Persons
   affected by the Project", and put provisions into the implementing contracts to ensure the ECOP
   and EMP requirements are met.
6. Monitoring and Reporting — "engage and retain the services of independent consultants to carry
   out external monitoring and reporting, and implement the recommended measures." This is the
   covenant behind the third-party monitoring the ICR's demolition figures rest on.
7. Implementation — shall not "amend, suspend, fail to enforce or waive the applicable RAP, ECOP,
   PMP, EMP, EMDP or any annual implementation plan without the prior written approval of Bank".
8. Annual Implementation Plan — furnish to the Bank by 31 December each year from 31 Dec 2012.
9. Financial Management Manual — apply it in implementation.
- Compliance: ICR00004709, 24 September 2019, paragraph 102 (interim financial reports late, "not
  in compliance with financial covenants in legal documents") and paragraph 103 (procurement
  "carried out satisfactorily in accordance with the legal covenants").
- `ct`: safeguard, admin, fincov.

### wushan-hospital-landslide-resettlement (P126210) — records a near-nothing
- All six rows of the PAD data-sheet "Legal Covenants" table, 10 May 2012: maintain the project
  management and implementation units with qualified and adequate staff; "Ensure adequate funding
  for counterpart requirements"; "Before first disbursement to Project County, on-lending World
  Bank loan proceeds on terms and conditions satisfactory to the World Bank"; annual work plan to
  the Bank for no objection by 15 December; mid-term review by 31 August 2015; Project Operational
  Manual cleared by the Bank by 30 August 2012.
- **The PAD "Conditions" table has one row and it reads "Not applicable"** — no condition of
  effectiveness or disbursement.
- **None of the six names land acquisition or resettlement.** RAPs for Wanzhou and Wushan were
  prepared, submitted 19 January 2012 and found acceptable (PAD section IV.E, paragraph 55), but
  the covenant table does not require their implementation.
- Two sentences in ICR00004869, 29 October 2021, Annex 6 (post-closing report) say outright what
  was not required: paragraph 3 — the emergency preparedness and response plan "was not prepared
  for the World Bank-financed project, and the World Bank's role is limited to the provision of
  technical support in the review process as part of a 'no regrets' risk management contribution by
  the World Bank"; paragraph 10 — the extra livelihood support discussed for the resettled
  household "is not part of the RAP entitlement matrix. Rather, this is a 'beyond compliance'
  suggestion".
- `ct`: fincov, admin.

### xuancheng-industry-zone-house-demolition (P129431) — records a near-nothing
- PAD 20 May 2013, data-sheet "Conditions" table, one row, type Effectiveness: Xuancheng
  Municipality, through XETDZ, shall enter into a Subsidiary Agreement with XETDZ CIC.
- Data-sheet "Legal Covenants" table, two rows: (1) due 30 June 2014, XETDZ CIC "shall have entered
  into a contract for the construction, and at least 5 years of operation and maintenance, of the
  wastewater treatment plant of the Project, with an entity or entities duly qualified to perform
  such tasks, all under terms and conditions acceptable to the Bank (PA, Schedule, Section IV,
  A. 1)"; (2) recurrent yearly, "For each of the Borrower's fiscal years starting 2018, the
  Wastewater Treatment Plant, should have total revenues equivalent to not less than its total
  operating expenses, excluding depreciation (PA, Schedule, Section IV, A.2)".
- Compliance: ICR00005311, 23 February 2021, paragraph 97 — "All the legal covenants were complied
  with on time."
- **Neither covenant names resettlement.** The RAP of April 2013 and the RPF were prepared (PAD
  section IV.F, paragraphs 63–65, repeated in Annex 3, paragraphs 50–52). For plots sold after the
  closing date the PAD records a promise and not a term: "the client has agreed that any land
  acquisition and resettlement activities will be undertaken in a manner consistent with the
  provisions set out in the RPF."
- `ct`: fincov, admin.

### moba-gorge-forest-land-compensation (P114107)
- Emergency project paper 22 January 2009, section G "Terms and conditions for project financing",
  paragraph 105: "Negotiations and Board presentation: None"; "Effectiveness: None".
- Four disbursement conditions: payment of the front-end fee; adoption of the Operations Manual,
  including the ESSAF and the Financial Management Manual, by Sichuan and Gansu; approval of
  sub-projects by the Bank and by government; adoption of the Procurement Plan by the two
  provinces. Annex 7, paragraph 12, repeats three of the four.
- Five implementation covenants (a)–(e) in the same paragraph, of which (b) "apply the OM, the
  ESSAF and the FMM in carrying out the project", (c) sub-project eligibility and Bank prior review
  and approval, and (d) "implement sub-projects in accordance with implementation plans to be
  prepared, and plans to mitigate any adverse environmental and social impacts to be prepared
  pursuant to the ESSAF" are the load-bearing ones for land and people.
- What the ESSAF covers on resettlement: PAD section IV.F, paragraph 86 — procedures for
  identifying eligible project-affected people, determining compensation, exploring and
  implementing rehabilitation measures, and management and monitoring.
- Non-compliance: ICR00003783, 27 February 2017, paragraph 49 — compensation of forest land for the
  Moba Gorge reservoir "was below agreed rates and is being rectified by GPG"; Annex 6 for the
  loan-closure undertaking by Longnan municipal government.
- **Flag for the checker:** the PAD data sheet carries the line "Significant, non-standard
  conditions, if any: None" immediately above the same four disbursement conditions on the same
  page. The entry does not quote that line and does not read it as denying them; the three
  following lines ("Negotiations and Board presentation: None", "Effectiveness: None",
  "Disbursement: (i)…(iv)") are the sub-items under that heading.
- `ct`: safeguard, admin.

### zhamushui-guangrun-resettlement-postponed (P068049)
All from the 2002 appraisal document, section G "Main Loan Conditions", for Loan 4666-CHA:
- **Effectiveness condition:** execution of the subsidiary loan agreements between the government
  and Hubei, and between Hubei and the project companies through their prefecture and county
  governments, satisfactory to the Bank.
- **Disbursement condition:** Bank approval of the Environmental Management Plans for the
  transmission lines associated with the four project components, for disbursement categories
  3(a)–(d). Annex 6, paragraph 4.
- **Involuntary resettlement (Hubei):** cause each project county "to enter into arrangements
  satisfactory to the Bank with the project company located in such county" for the resettlement,
  compensation and rehabilitation of all persons affected by its part of the project "in accordance
  with the respective RAPs and RPFs"; equivalent arrangements for environmental mitigation under
  the EMPs. A separate, county-specific resettlement covenant required Hunan's Longshan County to
  agree with Hubei's Laifeng County by October 2002 on carrying out the Najitan RAP — that one
  belongs to the Najitan component and is not in the entry.
- **Poverty alleviation:** Poverty Alleviation Enhancement Plans for each project county by
  31 December 2003; each project county to establish a poverty alleviation enhancement fund and
  devote 20 per cent of the fiscal revenues the project brings it, for at least five years after
  operations begin.
- **Project management and flow of funds:** Hubei to maintain a project management office with
  terms of reference and resources satisfactory to the Bank; on-lending to the project companies on
  the same terms as the Bank loan with the companies bearing the foreign exchange risk; semi-annual
  progress reports; audited financial statements within six months and semi-annual unaudited
  financial monitoring reports within 45 days.
- **Debt service reserve account:** before commissioning its first generating unit, a project
  company must open one and pay all net revenues into it until it holds the next six months'
  principal and interest, then maintain that balance.
- **Excluded under the ordinary-commercial-terms rule**, though printed in the same section: the
  1.2 debt service ratio, the 80:20 debt-to-equity limit, the 20 per cent working-expenses-to-
  operating-revenues ratio, the dividend restriction, and the loan's 30-year maturity, 5-year grace
  and 0.25 per cent front-end fee.
- **Phase boundary, stated in the entry:** those covenants name the four original project companies
  and counties. The Guangrun component, which includes the Zhamushui dam, was added by an amendment
  to the Loan Agreement in July 2006 with its own Project Agreement prepared in January 2007
  (ICR0000339, 14 June 2012, paragraphs 15–16). Neither that completion report nor PPAR 127227 of
  18 June 2018 prints what the amendment or the Guangrun Project Agreement required. A Guangrun
  resettlement plan dated 7 December 2005 exists (ICR Annex 5, paragraph 4; RP332 is in the case's
  sources).
- `ct`: safeguard, fincov, admin.

### wuhan-middle-ring-resettlement-overrun (P069852)
- PAD 12 February 2004, section G.1: "Standard conditions of effectiveness" — nothing non-standard
  before effectiveness.
- **The resettlement covenant, G.2.3.2(ii):** "Wuhan shall carry out the EMPs, RAPs and the RPF, in
  a manner satisfactory to the Bank, in particular: (a) Prior to commencing any work not included
  in the RAP, prepare a RAP in accordance with the RPF. (b) Prior to commencing any work not
  included in the EMP, prepare an EMP satisfactory to the Bank." The Sanjintan – Ping'anpu Middle
  Ring resettlement plan of 1 July 2007 (RP603, in the case's sources) is that covenant in
  operation: a plan prepared three years after appraisal for work not in the original RAP.
- G.2.3.2(i): no change to the agreed road programme unless compatible with the Wuhan Urban
  Transport Strategy and a full feasibility study acceptable to the Bank is carried out.
- G.2.3.1: maintain the Municipal Project Leading Group until project completion with terms of
  reference acceptable to the Bank; maintain a Project Office with units for land acquisition and
  resettlement, environmental management, procurement, financial management, construction
  management, project management and monitoring and reporting, "adequately resourced with suitably
  qualified staff"; annual work programme and budget to the Bank by 30 November each year from 2004
  and then implement what is agreed; keep the construction supervision team in place throughout.
- G.2.1 accounts and audit; G.2.2 semi-annual progress and procurement reports from 31 July 2004,
  annual reports by 15 February each year from 2005, mid-term review by 31 May 2006.
- G.2.3.3 road maintenance management system by 31 December 2006 and annual reviews with the Bank;
  G.2.3.4 annual review of public transport reform and a rolling five-year plan from the public
  transport companies; G.2.3.5 technical assistance, training and studies, with action plans on the
  studies' recommendations to be implemented.
- **No completion report for this project is in the cache**, and the Evaluation Group's review
  ICRR13574 of 27 June 2011 prints no covenant-compliance table, so nothing is cross-checked
  against compliance here.
- `ct`: safeguard, admin.

## My own two weakest entries

**1. `zhamushui-guangrun-resettlement-postponed`.** The only entry with a phase gap inside it. The
works that caused the harm were added to the loan in July 2006 and given their own Project
Agreement in January 2007, and neither of those two documents is published or quoted in the
completion report or the performance assessment. Everything in the entry is from the 2002 appraisal
document, whose covenants name "the four project companies" and "each of the project counties" —
the four original ones. The entry says so in its last two sentences, but a reader could still carry
the 2002 resettlement and poverty-fund covenants onto Guangrun, which is exactly failure 8 in
`CONDR.md`. If the checker can find the July 2006 amendment or the January 2007 Guangrun Project
Agreement through the documents API, that would settle it; if not, the honest version of this entry
may be shorter than what is written.

**2. `wuhan-middle-ring-resettlement-overrun`.** The covenant text itself is solid — it is quoted
verbatim from the appraisal document's own conditions section, and the July 2007 Sanjintan –
Ping'anpu plan matches it. The weakness is on the other side: there is no completion report in the
cache, only the Evaluation Group's review of it, and that review prints no covenant-compliance
table. So this is the one entry of the eight where the obligations are not cross-checked against a
document saying whether they were met, against a case whose own figures show resettlement at three
times the planned scale. The 2004 appraisal document is also the oldest of the eight, so its
"Standard conditions of effectiveness" line is the thinnest of the three ways these documents
record an absence of non-standard conditions.

Two further points a checker should test rather than take from me:
- The absence of a resettlement covenant in `wushan-hospital-landslide-resettlement` and
  `xuancheng-industry-zone-house-demolition` rests on the 2012–2013 data-sheet covenant table being
  the appraisal document's complete list of the loan's legal covenants. If that table is a summary
  rather than the whole schedule, both near-nothings weaken, though neither entry says the loan
  required nothing — each prints the covenants it did carry.
- `moba-gorge-forest-land-compensation` reads the data-sheet line "Significant, non-standard
  conditions, if any: None" as a heading above its own sub-items rather than as a statement, on the
  strength of the four disbursement conditions printed directly beneath it and the identical list in
  section G, paragraph 105. Worth a second pair of eyes on the page image.
