# Check log — companies_1, round 33 (independent check)

Checker: separate agent from the writer. Brief read in full: `docs/COMP.md` (writer's brief),
`docs/CHECK31.md` and `docs/CHECK20.md` (checking standard).

Input: `/home/claude/work/r33in/companies_1.json` (43 names)
Writer's output: `/home/claude/work/out33/companies_1.json` (33 descriptions, 10 blanks)
Writer's discrepancies: `/home/claude/work/out33/companies_1_disc.json` (8 entries)
Checked output: `/home/claude/work/out33/companies_1_checked.json` (43 keys, exact spelling)
Checked discrepancies: `/home/claude/work/out33/companies_1_disc_checked.json` (12 entries)

**Every cited page was opened.** 31 web pages and PDFs were fetched and read, plus 11 project
documents from `/home/claude/work/cache/<PID>/`. No description is carried whose source was not
opened. Where a source would not yield a claim, the claim is gone.

Headline counts: **1 description cut to blank. 26 of the remaining 32 descriptions substantively
corrected and 5 more tightened or extended. 7 of the writer's 10 blanks recovered from documents;
3 confirmed. Final file: 39 descriptions, 4 blanks.**

**2 of the writer's 8 discrepancies corrected, 1 of them substantively wrong; 4 new discrepancies
filed.**

---

## 1. Description cut

### Ministry of Education and Science (Albania) — blanked

Decided by what is *not* in either cited source. The European Commission's Eurydice page gives the
ministry as "Ministry of Education (ME) [Ministria e Arsimit]", "Ministry of Education and Sport",
"Ministry of Education and Sports" and "Ministry of Education, Sports and Youth". The ministry's own
site at `arsimi.gov.al` gives "Ministry of Education" in the page title, heading and footer
("© Ministry of Education 2026 - All rights reserved."). **Neither page uses the title in the key.**
The writer described the present-day ministry and then added a sentence hedging about the titles —
which both admits the problem and leaves the description attached to the wrong body.

The key itself is right for the case: the project's completion report (P078933,
`ICR_2014-03-28_19368623`, abbreviation list line 83 and body) uses "Ministry of Education and
Science (MoES)". But a document naming the body is not a document describing it. Blank until a page
describing a ministry under that title is opened.

---

## 2. Blanks recovered (7)

The writer reported 10 blanks (23 per cent), at the top of COMP.md's honest range. Seven of the ten do
not hold. Every one was recoverable from a document already on disk; in each case the writer had
looked only for a web page about the body.

| Entry | Recovered from |
|---|---|
| Expropriation Commission, Ministry of Public Works and Transport | Resettlement plan, P086807, `RP_2012-11-26_17031801`, glossary: *"Expropriation Commission — Special commission for application of the expropriation procedure in case of the Sanitary Landfill in Bajkaj in the MoPWT"*, plus the RAP cost section: its costs come from the MoPWT budget "for the functioning of the special expropriation commission for covering the costs of any fees for the registration of new ownership titles and issuing of Certificates of Ownership for all PAPs" |
| PFCTCAL Project Implementation Unit | Completion report, P116323, `ICR_2019-12-18_31675125`, para 54: *"During the first part of the preparation phase, 2007-2009, the PIU was under the Ministry of Transport, while between 2009 – 2012 the GoCI assigned the PIU to the Ministry of Economy and Finance (MEF)"*, with the staffing at the outset in the same paragraph |
| Project Coordination Unit, MINHDU (Cameroon) | Credit agreement, P084002, `AGR_2007-11-15_9340875`, definition 9: the unit is *"to be established and operating pursuant to the Project Implementation Act"*; appraisal document `PAD_2007-05-01_7726672` paras 47-48 for the remit and staff; resettlement plan `RP_2011-03-01_23855026` section 2.4 for every post |
| Jiangxi Administration of Navigation Affairs | Loan agreement, P101988, `AGR_2008-11-28_10331738`, definition 12: *"'JANA' means the Jiangxi Administration of Navigation Affairs within JPCD established for carrying out waterway development and maintenance in Jiangxi"*; appraisal document para 20 and annex 7 para 18 (*"JANA will arrange domestic loans"*) |
| Fenghua Investment Co., Ltd. | Appraisal document, P106956, `PAD_2010-01-26_11768237`, para 7: *"FCIC was established in March 2007 under the Company Law of China, with a charter and business license, and a registered capital of RMB 500 million"*, and paras 9 and 57 on the consolidation of the 13 city investment companies |
| Turpan Prefecture Water Resources Bureau | Appraisal document, P111163, `PAD_2010-05-19_12342782`, paras 33-35, which place the prefecture bureau between the regional (Xinjiang) Water Resources Bureau and the county bureaus and give the prefecture's composition |
| Unité de Coordination de Projets (UCoP), DR Congo | Completion report, P088619, `ICR_2012-12-21_17132031`, para 19: *"The existing project coordinating unit in the Ministry of Planning (Unité de Coordination de Projets – UCoP), already implementing the EESRSP, was charged with project preparation to overcome capacity constraints"*, and para 75 on the government using the existing EESRSP structures (UCoP, BCECO, URMF) with autonomy in financial management and administrative capacities |

Three of these are the ones the writer called "donor-project unit with no existence outside one
project". That reason does not survive contact with the documents: the agreements define the units'
legal basis and the completion reports describe their placement and staffing. **A blank is right only
if nothing describes the body; it is not right because no website does.** Said plainly, the writer
treated "no company page" as "no source".

The Fenghua recovery needed a judgement about identity. The registered name in both the appraisal
document and the completion report is *Fenghua City Investment Company Ltd. (FCIC)*, not the key's
name. This is not a parent described as the subsidiary: the completion report names FCIC as the PIU
for the Chunhu Town Infrastructure Development component, which is exactly what the card attaches to
this key, so the identity link is in a document rather than inferred from a resemblance. Filed as a
naming discrepancy.

The UCoP recovery also corrects the card by addition rather than contradiction: the card's role gives
the unit no placement, and the completion report puts it in the Ministry of Planning.

### Blanks confirmed (3), plus 1 newly blank

- **NEPEC 11** — checked further than the writer did: the Bank's appraisal document and completion
  report on disk for P112516 were searched and name no NEPEC 11. The card's own role attributes the
  name to the newspaper *Mmegi*.
- **K & G Construction** and **CB Construction** — the project documents on disk for P111928 name
  neither firm. (`Anthony Thurton & Associates` *is* named there, at `RP_2014-08-20_20160197` line
  205, consistent with the card.)
- **Ministry of Education and Science** — newly blank, above.

---

## 3. The two "thin but sourced" entries the writer flagged

Both were checked against the cited page. **Both hold, and the writer was right to decline to infer
"economic planning and project approval" from the name.**

- **Ningbo Municipality Development and Reform Commission.** The China Daily (Ningbo) page names
  "Ningbo Municipal Development and Reform Commission" under "Administrative Authority", gives the
  acceptance location as the "Service Center of Ningbo municipal Development and Reform Commission"
  and the responsible office as "The administrative examination and approval office". The one
  function carried is on the page. One caution now on the card's record rather than buried: the
  page's legal basis is a procedure on tax rebates for foreign-invested enterprises buying
  domestically made equipment, so the confirmation letter's use is narrower than "foreign investment
  approval" in general. Naming variance filed.
- **Gansu Provincial Development and Reform Commission.** The list and its two categories (projects
  "Expected to Start Construction" and "Preparatory" projects) are on the SMM page. Two cautions,
  both now recorded: the article names the issuer **"Gansu Provincial National Development and Reform
  Commission"**, which is not the key's title, and it reports only the hydrogen entries of the list
  rather than the list. I added one fact from the Bank's appraisal document for P091949, which uses
  the key's exact title and places the provincial project management office under the commission's
  Social Development Division.

---

## 4. Corrections, with the sentence that decided each

Grouped by the fault class, because the pattern matters more than the instance.

### 4a. Nationality, place and legal form claimed beyond the page (6 entries)

This remains the commonest invention, exactly as COMP.md says.

- **Consórcio Via Amarela** — "five **Brazilian** construction companies" and "**temporary** grouping".
  The Jornal do Brasil page says only *"composto pelas empresas OAS, CBPO (do grupo Odebrecht),
  Queiroz Galvão, Camargo Corrêa e Andrade Gutierrez"*. Nationality and legal character both cut.
  The page does load, contrary to any expectation that a 2007 URL would be dead.
- **Kribi Power Development Company** — "A **Cameroonian** electricity company". The MIGA page states
  the government of Cameroon's 44 per cent holding; it does not state the company's nationality.
  Changed to "an electricity company in Cameroon".
- **Siemens France** — "the **German** technology group Siemens AG". The boilerplate says
  *"Siemens France Holding est une filiale de Siemens AG, entreprise technologique"*. No nationality.
- **Wärtsilä** — no nationality was claimed, and that was right: a Nasdaq Helsinki listing is not a
  statement that the company is Finnish. Flagged here as the one entry that got this test right.
- **Delvina Municipality** — "in **Vlore county**" and "in **southern Albania**". The audit report
  never names the county. It mentions *"Prefekti Qarkut Vlorë"* confirming staffing figures, which is
  an inference from a mention, not a statement. Both cut. The card's own `place` field already
  carries the region.
- **Municipality of Shkodra** — "in **northern Albania**" cut, and "**elected** mayor" cut: the site
  links to a mayor, a council and a "Zgjedhjet Vendore 2023" page but nowhere states the offices are
  elective. Law 139/2015 on local self-government added from the site's own legal-basis line.
- **Thimphu Thromde** — "**Bhutan's capital**" cut. Neither cited page says it. An uncontroversial
  fact with no cited source is still unsourced.
- **COHAB-Santista** — "A **public** housing company" and "serving the **Baixada Santista coastal
  area** of São Paulo state". The filed report states neither: it does not say who owns or controls
  the company, and it names Santos and its hillside estates without listing municipalities served.
  The area claim is read off the company's own name.

### 4b. A figure attached to the wrong entity, or conflicting figures merged (4 entries)

- **CNEEC — figure removed entirely.** The writer carried "Its general contract with the Botswana
  Power Corporation for the Morupule B coal-fired plant was reported at about 970 million US
  dollars." Three faults in one figure. (i) **Wrong entity**: the Bank's procurement annex records
  that "the EPC Contract was awarded to CNEEC-SBW", a consortium of China National Electric Equipment
  Corporation **with Shenyang Blower Works** — a figure attached to a consortium the company sits in,
  which is COMP.md fault 3 verbatim. (ii) **Three irreconcilable figures**: the trade article's
  "$970 million"; the Bank's bid opening price "CNEEC-SBW US$697,800,000.00"; and the Bank's
  evaluated price after adjustments "CNEEC-SBW US$918.91 million". No source reconciles them, so none
  is carried and all three are recorded here. (iii) **Generalisation from one project**: "acts as
  general contractor on power plant projects" became the trade article's own "a company engaged in
  general contracting and the supply of mechanical and electric equipment", with the sector supported
  instead by the Bank's Table 26, "CNEEC experience in select thermal power plants" (China,
  Indonesia, Malaysia, Azerbaijan) — noting that the table is credited to BPC, not to CNEEC.
- **Siemens France** — the €1.9 billion was attributed to *Siemens France Holding*. The page
  attributes it to *Siemens France*: *"Au 30 septembre 2021, date de clôture du dernier exercice,
  Siemens France a enregistré … un chiffre d'affaires de 1,9 milliard d'euros"*. Siemens France
  Holding is named in the same boilerplate as the Siemens AG subsidiary. The figure has been moved
  back to the entity the page gives it to. "from continuing operations" cut as not on the page.
- **SNH** — "In 2020 **national crude output was 26.6 million barrels**" cut. Two reasons: the report
  gives 26.556 million barrels, and more importantly this is a figure for Cameroon's production, not
  for the company, and a national figure sitting in a company description reads as the company's own
  output. The sales figure is kept and made exact: *"Recettes totales (ventes de pétrole brut et de
  gaz naturel) 784,871 millions dollars US"*, against the writer's rounded 785 million. A second
  figure in the same report is recorded unused: the managing director cites 38.402 million barrels of
  oil equivalent for total national hydrocarbon production — a different quantity from the crude
  figure, not a conflict with it.
- **Ghana Highway Authority** — the two pages the writer cited disagree and the writer gave only one
  side. GHA's own profile: *"trunk road network totalling 15,000 km and related facilities in
  Ghana"*. SIGA, the writer's second source: *"GHA's 13,367 km trunk roads make about 33% of Ghana's
  total road network of 40,186 km."* Both are now on the card, attributed. Not reconciled — a tidy
  reconciliation would be a claim neither page makes.
- **KEC India** — selective within one table. The filing reports "Total employees (D + E) 6,543" and,
  separately, 32,479 workers. Giving only 6,543 reads as the whole workforce. Both now carried. The
  turnover is restated in the filing's own unit, "19,177.75 crore rupees", with a plain gloss, since
  converting crore to millions is arithmetic the source does not do.

### 4c. A clause in the same paragraph that cuts the other way, dropped (2 entries)

This is the fault CHECK20 names as deciding more drops than any other, and it is here twice.

- **Gobierno Autónomo Municipal de El Alto.** The writer wrote that its duties "include basic
  services **such as water and sanitation**". The report says water and sanitation is a municipal
  competence **and then says it is not the municipality that runs it**: in practice water supply and
  sanitation are run by the public utility EPSAS, which also serves La Paz and nearby municipalities.
  The competence was kept and the utility dropped. Corrected to carry both.
- **Municipality of Santos Secretariat of Government.** "supporting other secretariats' projects" is
  not a SEGOV task in the plan. The only trace is a single SEINFRA item marked as having SEGOV
  support — that is one other secretariat's project naming SEGOV, read as a general function. Cut.
  Also cut: "information technology governance **inside the council**" — the plan's IT items refer to
  the municipal *Plano Diretor de Tecnologia da Informação*, not the city council, and the City
  Council is not mentioned in the section at all. Two items in the same section that the writer left
  out are now in, since omitting them would be selective in the other direction: the AI item
  ("Fomentar iniciativas de inteligência artificial na Gestão Pública") and the IT master plan items.

### 4d. Sources outside the allowed classes (2 entries — the heaviest cuts in the batch)

COMP.md allows: the company's own site or annual report, an exchange or regulator filing, a
government register, or a reputable news outlet. Two entries rested on commercial aggregator
profiles, which are none of these.

- **AGETUR.** The decree page the writer cited was opened. It gives the full name and the delegated
  project-owner role (in the attached loan agreement, section 3.01(f): *"l'Agence d'Exécution des
  Travaux Urbains (AGETUR), pour la maîtrise d'ouvrage déléguée du Projet"*) and **says nothing about
  legal form, capital, shareholders or date of creation**. Everything the writer had on those points
  — created October 1990, capital of 100 million CFA francs, becoming a public limited company with a
  board in 2002, the shareholder list, capital of 1.2 billion CFA francs in 2019 — came from a
  DevelopmentAid directory profile alone. All cut. Replaced from a primary document on disk: the IDA
  credit agreement for P082725 defines AGETUR as *"a private company established and operating under
  the Borrower's laws and regulations pursuant to its statutes dated June 20, 2002"*. Note that this
  **conflicts with the directory's "public limited company"**; the credit agreement is preferred and
  the directory's version is not carried.
- **SERHAU.** The Cities Alliance / FSM Toolbox PDF was opened and carries only the acronym expansion
  and one sentence that SERHAU SA attended a review session. It supports none of the writer's
  content. The rest — March 1993, a predecessor government urban planning service created in 1986,
  the 48 per cent public / 52 per cent private split with the state, OPT, SBEE and local authorities,
  the September 2001 capital increase — came from a Devex profile alone. Cut. What then survived of
  the writer's first sentence ("carries out urban planning, housing and local development studies")
  **is a restatement of the company's own name** and fails the standing test, so it is also gone. The
  entry is now one sentence from the credit agreement: a private company under Beninese law, statutes
  dated 16 September 2004. Thin, sourced, honest. Note the statute date conflicts with the
  aggregator's 1993 creation date; only the agreement's date is carried.

### 4e. A date taken from the wrong field (1 entry)

- **Anthony Thurton & Associates.** "in March 2023 it **was awarded** a 22-month contract". The CDB
  page gives **no award date**; 13 March 2023 is the *"Commencement Date of Contract"*. Corrected to
  the commencement date. Two further cuts on the same entry: the scope on the page is *"provide
  technical support to the Executing Agency during the implementation of the BNTF 10 Project"*, not
  the writer's "review designs, prepare detailed designs and estimates and inspect construction",
  which is not on the page; and "a Belizean **consulting engineering** firm … It designs and
  supervises small public works" — the page gives the country as Belize and the award as consultancy
  services, and one contract does not establish a line of business. Value made exact at 165,093.75
  Belize dollars.

### 4f. The standing test applied, name stripped from description

Per the task: if removing the company's name leaves a claim with no support, the claim restates the
name. Applied to every sector and function claim in the batch. It changed four entries.

- **Consórcio Via Amarela** — "formed to build Line 4 of the São Paulo underground" cut: it restates
  both the name and the card's role. Stripped of the name, the membership list still stands on the
  source, so the entry survives as the membership alone.
- **SERHAU** — the business description is the name. Cut (above).
- **Ministère des Infrastructures, des Transports et de l'Habitat, Burkina Faso** — "The government
  department in Burkina Faso that handled roads, transport and housing" is the ministry's title in
  other words. It is kept only as the frame for the one independent fact, the minister's own
  network figures.
- **Ministry of Education and Science** — the surviving content after the title-mismatch cut would
  have been the name. Blank.

Two entries were examined under this test and kept: **Ningbo** and **Gansu** DRCs, whose single
functions are specific procedures on a page rather than readings of "development and reform".

### 4g. Smaller corrections, each from the cited page

- **Dirección Nacional de Vialidad** — decree number 461/2025 added; the carrying-on-of-functions
  wording tied to article 36 of that decree. Unreconciled: the FAQ page puts the body in the orbit of
  the Secretaría de Transporte within the Ministry of Economy; Resolución 1136/2025 puts it "bajo la
  órbita del MINISTERIO DE ECONOMIA" with no secretariat. Both given.
- **Tamiz Shahar** — "retaken by Azerbaijan" replaced with the page's own framing ("territories its
  own site describes as freed from occupation"), so the card is not adopting a characterisation as
  its own. Dates confirmed: creating decree 6 August 2008, start of work 12 March 2009 after state
  registration, Azerbaijan Investment Holding order 22 September 2021.
- **Ghana Highway Authority** — "bridges, culverts and ferries" corrected to the ferries and traffic
  devices the page lists; bridges and culverts are on neither page. Toll collection on the
  government's behalf added from the page's own function list. "keeping the body in being" **kept**:
  SIGA states Act 540 "continued the Authority in existence".
- **Belize Social Investment Fund** — "run with community groups, non-governmental organisations and
  local councils" cut; neither page says it. The Act's own object wording substituted for the
  writer's paraphrase, and the two-year appointment limit added from section 10(2).
- **Dangriga Town Council** — confirmed in full against the Act, including Dangriga as item 3 of the
  seven towns in the Schedule and section 3(3) "The Council shall consist of a Mayor and six other
  members duly elected". Section numbers added. The single change: "elected local authority" trimmed
  to "local authority", since the Act makes the *members* elected and does not characterise the
  council that way.
- **CAGECE** — every figure confirmed. One correction: the report gives *"receita bruta na ordem de
  R$ 919,5 milhões"* — gross revenue — and the writer labelled it water and sewerage revenue.
  "publicly traded" added from *"sociedade de economia mista de capital aberto"*.
- **Metrô** — all four facts confirmed; municipal law 6,988 added.
- **Prefeitura Municipal de São Paulo** — "an **elected** city council that passes the laws and
  **checks its accounts**" corrected twice: the document does not say the council is elected, and it
  assigns account scrutiny to the Tribunal de Contas *assisting* the Câmara ("Auxilia a Câmara de
  Vereadores na fiscalização das contas públicas"). The council's stated role is creating laws and
  scrutinising the Prefeitura. Budget approval date 21 December 2023 added.
- **Gobierno Autónomo Municipal de La Paz** — "road works" corrected: the services list gives *"PLANES
  DE INTERVENCION VIAL"* — road intervention plans — and road construction and maintenance appear
  only as a strategic objective, not a service. Execution rate 79.06 per cent added.
- **El Alto** — area corrected from "about 385" to the report's 384.7 km²; the population figure
  labelled as an INE *projection* rather than a count; "second largest city" replaced with the
  report's "segunda ciudad más poblada de Bolivia, después de Santa Cruz de la Sierra".
- **Thimphu Thromde** — section 300 of the Local Government Act 2009 added as the authority for the
  Thromde Rules 2011, and the duties tied to rule 8, which carries every one the writer listed.
- **MACOM** — PACOM's expansion added and corrected: the report gives *Programme d'Appui aux
  Communes*; the longer "Programme d'Appui à la Conduite d'Opérations Municipales" belongs to MACOM
  itself. The inter-ministerial committee confirmed and named: *"PACOM is headed by a national
  inter-ministerial Committee (Comité Consultatif de Gestion)"* and *"in which MACOM assumed the
  secretary-ship, sheltered in the BNEDT (formerly DCGTx)"*. Cut: the writer's gloss of BNETD as "the
  country's national office for technical studies and development" — the report gives the acronym and
  the former name and no expansion.
- **BCECO** — "education, health, local development and **roads**" corrected: the page gives
  *"les infrastructures, la santé, l'éducation, l'eau et l'énergie"* plus local development and
  institutional support, and roads is not among them. "covering the whole life of a project from
  preparation to closure" cut as not on the page. Corroborated from a second document: the completion
  report for P088619 calls BCECO "an autonomously functioning government entity".
- **Secrétariat Permanent, PDU (DR Congo)** — two corrections. The ministry placement rests on the
  document's own header and not its body, and is now phrased that way. And "handing those tasks to a
  separate coordination unit **once construction began**" is corrected: the document says approval of
  categorisation passes to the head of a project management unit (CCGEP) in the *implementation
  phase*, which is not the same thing.
- **Mali ministry** — the 2002 decree's duty list extended with the topographic and cartographic
  duty the writer omitted, and the 2012 successor titles given exactly, with article numbers.
- **Burkina Faso ministry** — seminar dates corrected from "June 2005" to 13-15 June 2005, and the
  network figure broken out as the speech gives it (6,700 national, 3,600 regional, 5,000
  departmental). The writer's aims clause ("better targeted public road investment and a sustained
  maintenance strategy") is **not** the aim the document states — the document gives the programme's
  major objective as fighting poverty and ensuring sustainable human development. Cut rather than
  swapped, because a stated policy aim is not a description of what the ministry is.

---

## 5. The writer's 8 discrepancies, verified

Each was checked against the source it cites. **Five of the eight are renamings or ownership changes,
as the writer reported, and all five are phrased with a date rather than as an overwrite** — that
part of the writer's practice held up.

| # | Entry | Outcome |
|---|---|---|
| 1 | KPDC / Globeleq | **Stands.** 56/44 split, AES share acquisition and 12 June 2014 guarantee date all on the MIGA page. Already dated. |
| 2 | KEC India name | **Stands.** KEC International Limited, Mumbai registered office, RPG Group flagship, all in the filing. Registered office address added. |
| 3 | Wärtsilä diacritics | **Corrected.** The writer said the site "gives the name as Wärtsilä Corporation". The About page carries no full legal name. "Corporation" dropped — and the writer's own source block spelled the publisher "Wartsila Corporation" without diaereses, in an entry about dropped diaereses. |
| 4 | Siemens France name | **Corrected, substantively.** The writer concluded "'Siemens France' is a descriptive label rather than a registered company name". The page does not support that — it is the page's own reporting entity for revenue and headcount. And "Siemens SAS" is in the article's lead-in, not in the boilerplate as the writer stated. Reduced to which name appears where. |
| 5 | Mali ministry title | **Stands.** Both Journal Officiel PDFs confirm it. Exact successor titles and article numbers added; the 2002 decree now cited alongside the 2012 one. |
| 6 | DNV ministry | **Corrected.** The writer's entry ended "It sat under the public works ministry at the time of the case" — which no cited page states. It restates the card and reads as a confirmation of it. Removed, and replaced with the real unreconciled difference between the two pages on whether a secretariat sits between agency and ministry. |
| 7 | Tamiz Shahar | **Stands.** 22 September 2021 order confirmed. The card's 14 October 2009 date is not contradicted: the page's 2008 and 2009 dates are for different events, which is not a conflict. |
| 8 | COHAB-ST short form | **Stands.** The filed report uses COHAB-ST. |

### Four new discrepancies filed

9. **CNEEC** — the card says "Electronic"; the Bank's appraisal document for P112516 and the trade
   press both say "Electric". And the EPC contract went to the **CNEEC-SBW consortium** (with
   Shenyang Blower Works), not to the company alone.
10. **Fenghua Investment Co., Ltd.** — the appraisal document and completion report both name the
    entity *Fenghua City Investment Company Ltd. (FCIC)*.
11. **Ministry of Education and Science** — the completion report for P078933 uses **both** titles for
    its own implementing ministry: "Ministry of Education and Science (MoES)" in the abbreviation
    list and body, "Ministry of Education and Sports" in its own data sheet. Reported unreconciled.
12. **Ningbo Municipality Development and Reform Commission** — three renderings across the card and
    its sources: the card's "Municipality", the commission's own listing "Municipal", and the Bank's
    appraisal document "Ningbo Development and Reform **Committee**".

---

## 6. Voice and tone

Every `desc` was grepped for `I `, `we `, `our `, `my `, `searches`, `this pass`, `read here`,
`the writer`, `this card`, `this entry`. **No hits in any description.** The writer kept the research
process in its `note` fields, where it belongs. Opinion words and flourish: none found in the
descriptions; the one evaluative phrase available in a source and rightly not used was the Bank's
"The selection of the Provincial Development and Reform Commission as PPMO was a sound decision".

One tone correction was made for a different reason — Tamiz Shahar's "territories retaken by
Azerbaijan" — because it has the card adopting a contested characterisation in its own voice rather
than attributing the source's.

Role restatement against `appears_on[].role`: checked on all 33 descriptions. Four cases found and
fixed, listed at 4f above.

---

## 7. Anything I could not settle

1. **Unreconciled, inside one document — PFCTCAL PIU.** The completion report says both that the unit
   "is the same structure handling four other World Bank projects" (para 49, naming PAMOSET, the
   Greater Abidjan Port-City Integration Project, the Abidjan Urban Mobility Project and PRICI) and
   that it "was newly created and its staff had no experience and exposure to Bank-financed or other
   IFIs projects" (para 59). These can be sequenced by date, but no document does that, so neither is
   carried on the card. Both are recorded.
2. **Unreconciled, across two cited pages — Ghana Highway Authority**: 15,000 km (GHA) against
   13,367 km (SIGA). Both on the card.
3. **Unreconciled, across two cited pages — DNV**: whether the transport secretariat sits between the
   agency and the Ministry of Economy. Both on the card.
4. **Unreconciled, inside one document — Albania's education ministry**: "Science" against "Sports",
   see discrepancy 11.
5. **Three figures for one contract — CNEEC**: $970m, US$697,800,000 and US$918.91 million. None
   carried, all recorded.
6. **No verified URLs for the recovered entries.** Seven descriptions and three discrepancies now rest
   on cached World Bank project documents under `/home/claude/work/cache/<PID>/`. The documents are
   named exactly (PID plus cached filename plus paragraph) but the `url` field is left empty rather
   than filled with a constructed `documents.worldbank.org` link — a guessed URL is the fault
   CHECK20 names ("shipped a 404, a 403 and a citation carrying the wrong regulation's title — all
   substantively right, all unusable as cited"). **These URLs need resolving before merge.**
7. **MACOM's source class.** The MIT Urban Upgrading country assessment report is not one of
   COMP.md's listed classes, though it is closer to a published field study than to a directory. It
   is the only source for the entry. Flagged rather than cut; a second source would settle it.
8. **BNETD** is named on the MACOM page without expansion, so what BNETD is cannot be stated.

### Routes that failed, named as routes

- **Turpan Prefecture Water Resources Bureau.** The writer called this a blocked host. One
  alternative route was tried as instructed: a Chinese-language web search for the bureau's functions
  and structure (吐鲁番地区水利局 职能 机构). It returned JICA report PDFs, an unrelated county
  government site and a World Bank blog — no page describing the bureau. **That route failed. The
  blank did not survive anyway**, because the project's own appraisal document on disk describes the
  bureau's place in the water administration. This is the pattern CHECK31 warns about: the inherited
  "blocked host" note was half right about the web and wrong about the conclusion.
- No permission prompt went unanswered, and no host refused a request in this check. 31 of 31
  attempted fetches returned content.
- Four fetches returned a partial-page note (the CAGECE report, the Metrô report, the KEC filing, the
  El Alto report, the mediacongo PDF, the Delvina audit, the SERHAU PDF). Every claim kept from those
  was inside the part returned; nothing was taken on faith about the unread remainder, and the SERHAU
  entry was cut rather than assumed to be supported further down.

---

## 8. The one finding for the next round's brief

**Put it in the brief that the project documents already on disk are a source for describing a body,
not just for the case.** Seven of the writer's ten blanks — 70 per cent of them, and 16 per cent of the
whole batch — were lying in loan agreements and completion reports in `cache/<PID>/`, which the
writer had the paths to. The writer's notes show what happened: each says some version of "no company
page, register entry or news article could be opened", and three say the body has "no existence
outside one project". Both are statements about the web, offered as conclusions about the world. A
credit agreement's definitions section is a primary legal document that gives a unit's legal basis,
and a completion report gives its placement and its staff — which is exactly what COMP.md asks a
description to contain, and more reliable than the directory profiles the writer *did* accept for
AGETUR and SERHAU. The brief should say: **before writing a blank for a government body or a project
unit, read the definitions section of the loan or credit agreement and the institutional arrangements
annex of the appraisal document.** The second-order benefit is visible in this batch: those documents
would also have caught the two aggregator-sourced entries, since they define both AGETUR and SERHAU
as private companies with statute dates that contradict the directories.
