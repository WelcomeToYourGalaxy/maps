# Round 26f — `conditions` for ten China World Bank cases (ICIJ tranche 4)

Output: `/home/claude/r20/r26f_icij4_conds.json`, ten records, each one edit setting
`conditions` from empty. Dry-run against `base.html` shows all ten ids present, all ten
`conditions` fields empty, no problems. Not merged. No `ct` set or proposed.

All thirty documents (ICR, ICRR, PAD for each of the ten projects) were already in
`/home/claude/r20/cache/` and were read from disk. No fetch was made.

Every entry rests on the appraisal document's own conditions-and-covenants section, which is
where the World Bank prints the terms in obligation language (`shall`, `condition of
effectiveness`, `condition of disbursement`). Three different PAD templates are in play: the
2004–2010 vintage prints a prose section ("Loan conditions and covenants") plus a data-sheet
repeat; the 2012–2013 vintage prints a "Legal Covenants" and "Conditions" table in the data
sheet; P121414 prints a single "Conditions and Legal Covenants" table.

## Source of each obligation

**zhanghu-railway-resettlement (P122319)** — `P122319_PAD.txt`
- Data-sheet "Legal Covenants" table, lines 236–244: the single safeguards-monitoring covenant,
  quoted close to verbatim ("implement and cause the Provinces to implement the Project in
  accordance with the Safeguards Instruments… including monitoring on a six monthly basis").
  The same table has no "Conditions" block, so no effectiveness or disbursement condition.
- Data-sheet "Safeguard Policies Triggered" table, lines 219–230: OP/BP 4.01, 4.04, 4.11, 4.12.
- Social section, paras 48 and 51 (lines 825–859): RAP, RPF and SA required; plan acceptable to
  the Bank; contents (grievance handling, internal and external monitoring, implementation
  arrangements, financing source); disclosure in China 4 January 2012.
- Risk matrix, line 1664: the county-level commitment letters on implementing the RAP.
- Procurement, para 25 (lines 1265–1267): procurement plans and their updates subject to the
  Bank's prior review and no objection before implementation.

**luan-huaibei-urban-transport-resettlement (P111421)** — `P111421_PAD.txt`
- Section III.E "Loan Conditions and Covenants", paras 29–32 (lines 712–733), and the data-sheet
  repeat at lines 277–295. The data sheet's "Loan effectiveness:" line is blank, i.e. no
  non-standard effectiveness condition.
- On-lending chain and currency risk: para 29. Organisational structure: para 30. The four-part
  covenant making Anhui cause each city to implement its RAP and EMP, prepare annual work plans,
  engage supervision consultants and engage M&E consultants with six-monthly reports to the Bank
  and act on their recommendations: para 31. Six-monthly reports and the mid-term report due
  15 August 2013: para 32.
- Category B and the triggered policies: data sheet, lines 275–276.
- The last sentence (that the monitoring covenant is the route by which the households were
  counted) is an inference from the covenant plus `P111421_ICR.txt` paras on the external
  monitoring consultant's findings; it is phrased as a mechanism, not as a document quote.

**zhegan-line-railway-resettlement (P075602)** — `P075602_PAD.txt`
- Section C.5 "Loan conditions and covenants", lines 671–700, with the data-sheet repeat at
  lines 250–270. "Condition o f effectiveness": the legal opinion confirming the RAP Arrangements
  with Hunan, Jiangxi and Zhejiang are legally binding (line 673–677). Definition of "RAP
  Arrangements" at line 717.
- "Other covenants" 1(a)–(c): minimise involuntary loss; carry out the EMP, RAP and RAP
  Arrangements satisfactorily; furnish proposed revisions for Bank approval (lines 680–690).
- Covenants 2–4: power supply agreements by 1 August 2006, EMU timetable by 31 December 2004,
  operating rules by 1 August 2006 (lines 691–700); twice-yearly financial monitoring reports and
  yearly results reports from the data-sheet list, item 4.
- Category A from the data sheet; OP/BP 4.12 at line 248.

**nanchang-line-2-demolition (P132154)** — `P132154_PAD.txt`
- Data-sheet "Legal Covenants" table, lines 256–291: implementation arrangements (Project Leading
  Group, PMO); Integration Plan; "cause NM and URC to implement the Safeguards Instruments";
  reporting by 31 March and 30 September; financial management system and interim unaudited
  reports; audited statements within six months.
- Data-sheet "Conditions" block, lines 292–297: the Subsidiary Agreement as the one effectiveness
  condition.
- Safeguards table, lines 243–254: OP/BP 4.01, OP 4.11, OP/BP 4.12; Category A.
- Para 69 (lines 1226–1231): RAP prepared under Chinese law and OP 4.12, RPF for components that
  might change location, both disclosed.
- That the compensation was client-financed is already in the case's lender role; it is repeated
  here only to make clear that the covenant still bit.

**henan-towns-water-land-acquisition (P081348)** — `P081348_PAD.txt` and `P081348_ICR.txt`
- PAD section C.6 "Loan/credit conditions and covenants", lines 588–620, with the data-sheet
  repeat at lines 257–285: the two effectiveness conditions; the three implementation covenants;
  the financial covenant; the financial-management covenant; and the disbursement covenant tying
  subproject eligibility to a signed subsidiary loan agreement and a confirming legal opinion.
- The resettlement obligation is in `P081348_ICR.txt` Table 2.5 / Table 2.7 "Status of compliance
  with covenants" (lines 1363–1375 and 1424–1440): Project Agreement Schedule 2, paragraph 4(b),
  six-monthly M&E reports on the EMP (dam safety included) and the RAP under terms of reference
  satisfactory to the Bank — recorded "Partially complied with". The same tables record Article 2,
  Section 2.03(b)(i) (a plan for continued achievement of the objectives by 31 December 2013) as
  "Not complied".
- Triggered policies at PAD lines 252–255; Category B from the case's lender role.

**sichuan-wudu-canal-resettlement (P121414)** — `P121414_PAD.txt`
- The single "Conditions and Legal Covenants" table, lines 240–347: thirteen numbered items, all
  under the Project Agreement, no effectiveness condition. Items used: 1 (organisational
  structure to 31 December 2017); 2 (apply the PIP, RAP, EMP, PMP, annual implementation plan and
  annual dam safety action plan satisfactorily, no amendment, suspension or waiver without the
  Bank's prior concurrence); 3 (measures satisfactory to the Bank for improving the living
  standard of Displaced Persons in accordance with the RAP; EMP provisions and sanctions in works
  contracts); 4 (independent consultants for annual external monitoring and reporting, with the
  recommendations implemented, to improve compliance with the RAP); 5–7 (Dam Safety Panel, dam
  safety plans, periodic inspection); 8–9 (six-monthly reports, mid-term review by 30 June 2015);
  12 (WUAs under the WUA Manual).
- Safeguards table, lines 225–236: OP/BP 4.01, 4.04, OP 4.09, OP/BP 4.12, OP/BP 4.37. Category A
  from the case's lender role.

**yining-urban-roads-demolition (P126454)** — `P126454_PAD.txt`
- Data-sheet "Legal Covenants" table, lines 225–247: the five covenants, including "Yining
  Municipality shall implement the EMP, RAP and EMDP" and the two six-monthly reporting
  covenants, and the mid-term progress report due 30 June 2015. No "Conditions" block follows the
  table, so no effectiveness or disbursement condition.
- Safeguards table, lines 213–223: OP/BP 4.01, 4.11, 4.12.
- Paras 36–39 (lines 1388–1414): the EMDP developed to meet local Uygur communities' needs; the
  RAP prepared "as required by OP4.12"; both disclosed.
- The absence of any figure: `P126454_ICRR.txt`, already quoted in the case's lender role (the
  US$19.5 million appears in no cost table; land acquisition expenses are not mentioned in the
  PAD, the loan agreement or the ICR).

**shaying-river-sanba-village-resettlement (P118647)** — `P118647_PAD.txt` and `P118647_ICR.txt`
- PAD section III.E, lines 702–706, quoted: "No non-standard conditions" for effectiveness, and
  standard covenants only on procurement, financial management and safeguards. Data-sheet
  "Loan/credit effectiveness: None." at lines 283–284.
- OP/BP 4.12 and the RP/RPF at para 46 (line 757); the scale figures at para 47.
- The standard reporting package: `P118647_ICR.txt` para 48 (lines 933–936) — interim financial
  reports, annual audited reports, periodic safeguards reports, regular progress reports — and
  para 56 (line 1023) for the independent monitoring consultants.
- Sanba and what followed: `P118647_ICR.txt` paras 57–58 (lines 1026–1042). The six-monthly
  interim reports, the continued provincial monitoring and the grievance mechanism are explicitly
  placed there under the later Anhui Rural Road Program, after this loan closed on
  31 December 2017.

**tongliang-road-land-lease-compensation (P086446)** — `P086446_PAD.txt` and `P086446_ICR.txt`
- PAD section C.6, lines 859–885, with the data-sheet repeat at lines 348–367: "Loan Effectiveness:
  None"; the one disbursement condition on subsidiary loan or implementation agreements; the five
  implementation covenants (a)–(e).
- Triggered policies at lines 339–342; Category B from the case's lender role.
- Six RAPs / abbreviated RAPs and the Consolidated RAP translated into English for the Bank's
  review and approval: PAD paras 60 (lines 1150–1156) and the translation-waiver box at lines
  262–273.
- "in accordance with the legal agreements": `P086446_ICR.txt` lines 1410–1411 (Social Safeguards).
- "finally corrected per the Bank requirements": `P086446_ICR.txt` Annex 7, lines 2586–2587,
  quoted verbatim from the borrower's own account.

**guangxi-poor-rural-land-acquisition (P071094)** — `P071094_PAD.txt`
- Section G.1 "Effectiveness Condition", lines 1661–1667: the three conditions (implementation
  agreements with the three provinces; the DFID–borrower–Bank tripartite arrangement; the first
  DFID trust-fund deposit).
- Section G.2, "Disbursement Conditions", lines 1668–1684: the province-by-province financial
  management training conditions (Yunnan's additional participatory-planning requirement is in
  the document but was cut from the prose for length). Cross-check in Annex 7, line 3615, which
  calls the training "a condition for loan disbursement".
- "Implementation" covenants, lines 1690–1715: the CLG and the provincial and county PMOs with
  composition and resources acceptable to the Bank; annual action and work plans by 31 October;
  the 50 per cent expenditure floor on components 2–6; and farmers not required to contribute to
  cost recovery for those components.
- "Project Design" covenants, lines 1742–1750: carry out the project in accordance with the PIM,
  which contains the EMP, the overall RPF, the Ethnic Minority Planning Framework and six EMDPs,
  the Participation Manual, the Phasing Plan and the Procurement Manual, with no amendment
  without the Bank's prior concurrence.
- Triggered policies and the "limited and scattered" land acquisition with RPF and first-year
  RAPs: lines 1433–1439 and 1537–1542.

## My own two weakest entries

1. **henan-towns-water-land-acquisition.** The entry's last sentence says neither the PAD's
   covenant list nor the ICR's compliance tables prints a term requiring the resettlement plan
   itself to be carried out. That is accurate about those two documents, but neither is the loan
   agreement, and the ICR's compliance tables list only four covenants, which is plainly a
   selection rather than the whole schedule. The conformed Loan Agreement 4829-CN was not opened
   (not in the cache). If anyone retries this case, that document would settle whether the
   absence is real or only an absence from the summaries.

2. **tongliang-road-land-lease-compensation.** Same shape of weakness, and one step further: the
   ICR says external monitoring was carried out "in accordance with the legal agreements", so the
   agreements clearly carried a safeguards term that neither document prints. The entry says so
   explicitly rather than filling the gap, but it means the covenant picture for this loan is
   knowably incomplete. Loan Agreement 7920-CN was not in the cache either.

A third to watch, less weak but worth flagging: **shaying-river-sanba-village-resettlement**
carries no project-specific condition at all. The entry is built on the PAD saying so in its own
words, which is the strongest kind of absence available, but it is still an absence, and a reader
could mistake the sentence about the Anhui Rural Road Program undertakings for a condition of
this loan if the entry were trimmed further.

## Cases where no obligation was found

None. All ten projects carry printed obligations in their appraisal documents, so no entry
records a bare absence. Two entries record a *partial* absence, and both are stated as such
rather than papered over:

- **yining-urban-roads-demolition** — the duty to carry out the resettlement plan is covenanted,
  but no sum of money for compensation or land acquisition appears in the loan agreement, the
  cost tables or the ICR. Searched: `P126454_PAD.txt` and `P126454_ICRR.txt`, which is where the
  Independent Evaluation Group states the absence.
- **henan-towns-water-land-acquisition** and **tongliang-road-land-lease-compensation** — the
  covenant lists carry reporting and monitoring duties on the resettlement plans but no printed
  duty to carry them out. Searched: each PAD's conditions-and-covenants section and data-sheet
  repeat, and each ICR for the words covenant, legal agreement, requirement and resettlement.

## Notes for the owner

- One figure to check against the case data, not acted on here: the `P118647` PAD data sheet lists
  Environmental Assessment, Natural Habitats and Involuntary Resettlement as the triggered
  policies (lines 276–278), while the case's lender role names environmental assessment, physical
  cultural resources and involuntary resettlement. The `P111421` PAD data sheet likewise lists
  only OP/BP 4.01 and OP/BP 4.12 (lines 275–276) where the case names three. Both entries were
  written so as not to turn on the disputed policy. The ICRs are the likely source of the case's
  lists; reconciling them is a `textfix` job, not a conditions job.
- Entry lengths run 179–287 words against a map median of 47 and a previous maximum of 280. These
  ten documents are unusually covenant-rich, and the longest entries are the two with three
  conditions and a dozen covenants each. If the owner wants them inside the existing range, the
  administrative covenants (reporting dates, financial statements, mid-term reviews) are what to
  cut first; the resettlement and effectiveness terms are the load-bearing part.
