# Check log: companies_2 (round 33, batch 2) — independent check

Writer's file: `out33/companies_2.json` (43 names, 35 descriptions, 8 blanks).
Checked file: `out33/companies_2_checked.json` (43 keys, exact input spelling and order; 38 descriptions, 5 blanks).
Discrepancies: `out33/companies_2_disc_checked.json` (9 verified, 2 added).

Every cited page was opened. Where a claim rested on a page that does not carry it, the claim was cut
or re-sourced. Three blanks were recovered from documents already on disk.

## 1. Descriptions cut (claims removed from a description that otherwise stands)

No description was emptied in full. Nine carried claims the cited page does not make; those clauses
were cut.

- **Office de Voirie et Drainage (OVD)** — cut "and roadside drainage". The JICA master plan describes
  OVD as "une entité en charge de l'entretien des voiries urbaines de la RDC", with construction and
  maintenance "particularly in the provincial capitals". Drainage appears only inside the body's own
  name. Standing name test: strip the name and nothing supports a drainage function.
- **Agence Djiboutienne d'Execution des Travaux d'Interet Public (ADETIP)** — cut "community projects,
  and supported small income-generating activities through micro-credit". The ADDS page attributes that
  to the two merged tools jointly ("have funded a wide experience in the fight against poverty"), not to
  ADETIP; the second ADDS page says nothing about ADETIP beyond its name. Figure-to-wrong-entity class.
  Also cut "public-interest construction works", which is the name restated, and replaced it with the
  mandate the project's completion report does state: "its mandate, which was to carry out public works
  using labor intensive methods", and "ADETIP, as a contract management agency, had a solid experience
  in implementing Bank-financed projects".
- **Empresa Pública Aguas de Manta (EPAM)** — cut "owned by the Manta municipal government". Ordinance
  023-2020 calls EPAM a "persona jurídica de derecho público" with "patrimonio propio" and lists the
  municipality as one funding source (Art. 5(a)). It never states ownership. The board chair stands:
  "El Alcalde o la Alcaldesa del cantón Manta, o su delegado" (Art. 6.1).
- **Municipal Development Fund of Georgia** — cut "lends to". The fund's history page states its aim as
  "making investments in local infrastructure and services" and does not mention lending.
- **National Agency for Cultural Heritage Preservation of Georgia** — cut Gremi from the list of
  museum-reserves. The Council of Europe report lists "Vardzia Historical-Architectural Museum-Reserve"
  and "Uplistsikhe Historical-Architectural Museum-Reserve" but "Gremi museum".
- **Companhia dos Caminhos de Ferro da Beira (CCFB)** — cut "the Indian state firms". The PIB release
  says only "RITES and IRCON hold controlling interest of 51 per cent, consisting of 26 per cent and 25
  per cent respectively"; it does not describe either as a public sector undertaking or a government
  company. Nationality-invention class, and the commonest fault in the brief. Also cut "from Beira to
  the Zimbabwe border": the release says the 317 km Machipanda line "connecting Beira to railways of
  Zimbabwe" and mentions no border.
- **Smith Warner International** — cut "shows projects in nine Caribbean countries and territories".
  The about page states no number; nine is the writer's count of a navigation menu. Also changed
  "shoreline management" to the page's own "zone management". Not repeated: the page's claim to be "the
  Caribbean's largest and most comprehensive" firm, which is self-description.
- **Departamento de La Guajira** — cut "made up of 15 municipalities" and "the country's regional tier of
  government". The DANE sheet states no municipality count (the 15 is a count of a chart's rows) and says
  nothing about Colombia's tiers of government. The named municipalities and the 1,002,394 projection
  for 2022 from "DANE - CNPV 2018" stand.
- **Commissioner of Revenue Administration, Tamil Nadu** — cut "village-level staff" (the page says only
  "upto grass root levels" and "from cities to the villages") and softened "leads disaster response" to
  distributing relief, the page's own wording being "provides food, clothes, shelter and also distributes
  essential commodities and financial assistance".
- **Ministry of Finance of Mongolia** — cut "acting as the central administrative body in charge of
  finance and budget". Section 1.1 of the strategy names only "the Central Administrative Body in Charge
  of Finance and Budget"; the Ministry of Finance appears in the document only as the source credit under
  the tables. Attribution-to-named-entity class.

## 2. Descriptions corrected (the fact held, the framing or the date did not)

- **Ministerio de Ambiente, Vivienda y Desarrollo Territorial** — "to a new Ministry of Housing, City and
  Territory" → "to the Ministry of Housing, City and Territory". Decreto 3570 recites the escisión and
  the rename but treats the housing ministry as existing and does not create it.
- **Aguas de La Guajira S.A. E.S.P.** — added "private", documented ("una empresa privada constituida
  como sociedad anónima"; Table 1 class "Privada") and material to a reader.
- **Roads Department of Georgia** — "under the Law on Roads of 1994" → "under Georgia's Law on Roads".
  Article 9(2)(a) ("design, construct, modernise, reconstruct, rehabilitate and maintain international and
  intrastate importance roads") and Article 22¹(3) (appeal to the Ministry of Infrastructure) were read in
  the consolidated text served at matsne.gov.ge, whose version banner reads 25/06/2026-16/09/2026, not in
  the 1994 original. The 2023 figures (6,970 km, 1,511 km international, 238 staff, local roads with
  municipalities) are confirmed from the department's own presentation, dated 4 April 2023.
- **Lands Commission, Ghana** — "remodelled by the Lands Commission Act, 2008" → established under both
  Article 258 and Act 767, which is what the page says. Also rewritten to stop restating the card's
  `role`, which already gives public-land management and the land register.
- **Ministry of Information and Communication Infrastructure (MOICI), The Gambia** — cut "responsible for
  communications and information technology policy", which the infographic states for DOSCIT and for
  MOCDE but not for MOICI, and replaced it with the dated name chain the source does give (2002 DOSCIT,
  2009 MOCIIT, 2011 MOICI, 2022 split). This is the batch's clearest instance of the risk named in the
  task: a body described by a remit documented for its successor.
- **Gambia Telecommunications Company Limited (GAMTEL)** — the 2022 revenue and loss are now marked as
  draft. Table 4 labels the 2022 row "(Draft)" and the following paragraph notes "the 2022 financial
  statement still in draft stage". Ownership confirmed verbatim: "with the Gambia government owning 99%
  of its shares and Gambia Ports Authority (GPA) owning 1% of its shares". The 1,046 staff figure is at
  31 December 2017 and is quoted by the audit from an Ernst & Young report, so it is now attributed to
  the audit's citation rather than to the company.
- **Agency for State Roads** — rewritten with both names and dates. The 2008 body is named "Agency for
  Public Roads" on the source page; the key's name appears only in the 2012 law's transfer clause. Also
  "North Macedonian" → "Macedonia, now North Macedonia": the agency existed from 2008 to 2012, before the
  country's renaming.
- **Royal Caribbean** — the described entity is now named as Royal Caribbean Group, which is what the
  filing describes and what holds the brands; and "operated 66 ships ... for 2024" was split, since 16.5
  billion dollars of revenue and 2.9 billion of net income are for 2024 while the 66 ships are the "About
  Royal Caribbean Group" statement in the January 2025 release. Figure's-year class.
- **Administracao de Infra-estruturas de Agua e Saneamento (AIAS)** — "created ... to manage public water
  supply and wastewater and stormwater drainage systems" → the remit Article 4 of Decree 112/2020 actually
  gives: main counterpart of the public and private operators of those systems, manager of investment
  programmes in them, able to delegate their operation by management contract or concession. AIAS is not
  described as operating them.
- **Directorate General of Highways, Indonesia** — the remit was cited to Permen PUPR 11/2016, which does
  not state it: that regulation only places the Balai Besar / Balai Pelaksanaan Jalan Nasional under the
  directorate general (Pasal 4(2), Pasal 12(2)) and names the ministry. Re-sourced to Permen PUPR 13/2020,
  Pasal 183 ("mempunyai tugas menyelenggarakan perumusan dan pelaksanaan kebijakan di bidang
  penyelenggaraan jalan") and Pasal 184(b) ("pelaksanaan kebijakan di bidang penyelenggaraan jalan
  nasional"). The 47,603 km figure is confirmed as 47.603,39 km for Semester I 2023.
- **Ministry of Public Works and Transport, Lesotho** — kept, with the ministry list and the roads page as
  sources, but it remains the thinnest entry in the batch: the two gov.ls pages establish only that the
  ministry exists (list entry 21) and that the Roads Directorate "was established as a department under
  the Ministry of Public Works and Transport" and later "as a corporate body by the Roads Directorate Act
  of 2010". Neither page says what the ministry does. The second fact survives the name test, so the entry
  stands rather than going blank; it is flagged here for the next round.
- **Customs Administration** — "clears and inspects imported goods" → the page's own competences, "Customs
  supervision, customs clearance of goods, customs control, excise surveillance throughout the territory",
  which are not limited to imports. Also dropped "a body within the Ministry of Finance", which restates
  the card's `role` ("A unit of the Ministry of Finance"). The 2025 figure is confirmed: "total revenues
  collected from imports and domestic trade amounted to 131,634.3 million denars", "EUR 2,140.39 million".
- **Housing Fund of the Ministry of Urban Development, Djibouti** — dated. The delegate ministry through
  which the fund works "was created in 2011", after the 2004-2009 case on the card, so the arrangement is
  now given as of 2018 and the relaunch as a step reported as under way in 2018.
- **Unité Centrale d'Exécution, Haiti** — cut "road, drainage and airport projects". The cited tender
  notice covers drainage works at Cap-Haïtien only; roads and airports came from the card, not the page.
  The 2016 financing agreement adds the one institutional fact ("the Project central implementing unit
  within said ministry"), and the notice supplies the procurement function and its date, 26 April 2025.
- **Comité Permanent d'Acquisitions à l'Amiable** — kept, with the predecessor's location added: the
  framework says the Comité d'Évaluation sat at the MTPTC and has stopped functioning, which bears on a
  card about an MTPTC project.
- **Ministry of Finance of Mongolia** — the debt figure is now marked preliminary. Table 2's 33,384.6
  carries the asterisk for "Preliminary performance"; section 2.3 gives "41.8 percent, or MNT 33.4
  trillion, by the end of 2024".

## 3. Blanks recovered, and from what

The writer reported 8 blanks (19%) and called five of them "no page names the exact entity". Three of
those five are describable from documents already in `cache/<PID>/`. Blanks now stand at 5 (12%).

- **Ahwaz Water and Wastewater Company** — recovered. The writer declined it as a parent-for-subsidiary
  risk. That reasoning was sound as to the Khuzestan provincial company, and the two are confirmed
  different: the appraisal document's sector section says "thirty-three provincial and city WWCs provide
  supply water and wastewater services", so city companies exist alongside provincial ones. But the
  entity in the key is itself a party to a World Bank document: `AGR_2004-07-17_5179860.txt` is the
  "AHWAZ Project Agreement ... between INTERNATIONAL BANK FOR RECONSTRUCTION AND DEVELOPMENT and AHWAZ
  WATER AND WASTEWATER COMPANY", with a subsidiary loan agreement on-lending part of the US$279 million
  loan to it. The appraisal document's financial annex gives figures for this company: "Based on audited
  accounts for the past four years, Ahwaz WWC has been incurring significant net losses", "Water losses
  were as high as 46% in 1999100 and have come down to about 37.7% in 2002103". Annex 15 gives its
  organisation chart, headed by a General Assembly and a Managing Director. The completion report carries
  an "From Ahwaz Water and Wastewater Company (AWWC) ICR" annex. No figure was taken from the Khuzestan
  company or from the national engineering company.
- **State Commission for Roads and Bridges, Iraq** — recovered. The 2014 loan agreement's definitions
  section settles the entity the writer could not confirm: "'State Commission for Roads and Bridges' and
  the acronym 'SCRB' mean the commission within the Ministry of Construction and Housing, or any successor
  thereto". The appraisal document puts its project management team "at SCRB within the Ministry of
  Construction and Housing in Baghdad", with the Kurdistan component at GDRB. The 2023 completion report
  gives the restructuring and so explains the Roads and Bridges Directorate the writer found in Iraqi
  tender notices: "the creation of the Ministry of Construction, Housing and Public Municipalities
  (MOCHPM) followed by a further change to subordinate RBD as a department under the MOCHPM with the
  responsibility for strategic planning and management of national roads network and expressways".
- **Unité de Coordination des Projets (UCoP), Ministry of Planning** — recovered, from the agreement's
  definitions section exactly as the task anticipated. The 2007 financing agreement: "'UCOP' means Unite
  de Coordination du Projet, established and operating pursuant to Decree 03/023 dated September 10,
  2003". The 2008 resettlement policy framework adds the ministry and the structure: "L'UCOP est placée
  sous l'autorité du Ministère du Plan", "L'UCOP consiste en une structure légère et souple composée
  d'une Coordination centrale, d'une Direction des Opérations et d'une Direction Administrative et
  Financière", "L'UCOP ne dispose pas au sein de son équipe d'un responsable environnemental et social",
  and records the extension of its remit by decree n°05/30 of 12/05/2005 and by a later amendment. The
  completion report confirms the ministry: "the existing Project Coordinating Unit in the Ministry of
  Planning (UCoP, already implementing the Bank-funded EESRSP and ELCISP)". Not used: the report's
  "Currently reflections are ongoing on how to assure continued use of the capacities developed in project
  implementation, potentially as a private sector entity", which is speculation, and the fall in its
  activity, which was dropped when the entry was shortened.

## 4. Blanks that stand (5), with the documents read

Each note was rewritten to name the document opened, because a blank whose reason is "nothing was found"
cannot be audited.

- **China First** — the February 2019 mission report was opened in full. It calls the firm only
  "l'entreprise China First", gives its site camp on avenue Gazumbu and its administrative office at
  "l'avenue Maman Yemo, n°419, Quartier Industriel dans la Commune deManika", and notes it had produced a
  site ESMP for the same project at Kisangani. All of that is what it did at project sites. No sector
  beyond contracting, no ownership, no size, and no nationality: the name is not a source for Chinese
  ownership. Blank is right.
- **Fundación MANA** — the June 2011 social evaluation and indigenous resettlement plan was opened: "La
  Fundación MANA, suscribió el contrato No. 013 del 31 de marzo de 2.009, con la Gobernación de La Guajira,
  para realizar los estudios y diseños de proyectos para el desarrollo socioeconómico y ambiental en la
  zona de influencia de la Laguna facultativa del Municipio de Riohacha". One contract's scope is not the
  body's business, and the card's `role` already carries it. Blank is right.
- **SAL Consult Limited** — the resettlement plan it wrote (RP1149) was opened. It yields the firm's name
  as author and a post box: "SAL Consult Limited, P O Box GP20200, Accra". An independent search returned
  only aggregator listings. Blank is right; the Accra address on the card is at least documented.
- **Mirai Construction Company Limited** — the Abbreviated Land Acquisition Plan was opened: "The Contract
  for the Coastal Protection Phase 1 and 2 was awarded to Mirai Construction Company Limited for a
  contract price of EC$6,683,042.53." A contract price is not a company. Blank is right.
- **Hanson – Rodríguez, S.R.L.** — the corrective resettlement plans and the completion report were
  opened. The plans call it "la Empresa Hanson – Rodríguez, Empresa consultora que tiene a cargo las
  labores de Supervisión Técnica del Proyecto, designada por el INDRHI", which restates the card's `role`.
  Blank is right.

## 5. Discrepancies: verified, corrected, added

All nine the writer filed hold on the source cited; all nine are phrased with a date rather than as an
overwrite, which was the specific thing to test. Four were sharpened:

- **ADETIP** — the writer's entry blamed the card. The conflict is inside the project's own completion
  report, which says both that Parliament created a new agency into which ADETIP "would be folded" and,
  twelve pages later, that the government broadened ADETIP's mandate and "Its name was changed to ADDS".
  Both sentences are now quoted and left unreconciled.
- **Agency for State Roads** — confirmed, with the date of the 2008 amendments (11 July 2008) and a note
  that the source page itself uses two names for the same body and does not explain the change.
- **Comité Permanent d'Acquisition à l'Amiable** — confirmed, with the framework's statement that the
  predecessor committee sat at the MTPTC and no longer functions.
- **Housing Fund, Djibouti** — confirmed, with the caveat the writer left out: the delegate ministry was
  created in 2011, after the case, so the entry corrects the ministry's name as of 2018 only.

Two were added:

- **Unité de Coordination des Projets (UCoP)** — the card's name is plural; the 2007 agreement and the
  2008 framework both give "Unité de Coordination du Projet", singular, and the completion report gives
  two further spellings.
- **State Commission for Roads and Bridges, Iraq** — the ministry name on the card belongs to the later
  period; the 2014 agreement puts the commission in the Ministry of Construction and Housing, and in the
  later period the body is the Roads and Bridges Directorate.

None of the nine failed.

## 6. Figures left unreconciled (both sides given)

- **REGIDESO's incorporation.** The 2023 annual report says "Depuis le 4 septembre 2014, elle est
  transformée en société commerciale" as a société anonyme, and elsewhere "Société Anonyme depuis 2014",
  but its own timeline also carries a 2010 SARL conversion and a 2008-2009 date. The description keeps
  2014, which the document states twice, and the conflict is recorded here.
- **Aguas de La Guajira's start of service.** 1 December 2000 (Table 1), 1 May 2001 (section 1.2.1), "el
  año 2001" (section 1). The description says "from the start of the 2000s".
- **UCoP's founding decree.** Decree 03/023 of 10 September 2003 (financing agreement) against décret
  présidentiel n° 03/024 of 10 September 2003 (resettlement framework). The description gives the month
  and year only.
- **CDR Lebanon's project total.** The article's body gives "USD 10.9 billion"; its own headline gives 11
  billion, and its tables carry unit errors ("USD 710 billion", "10.880 million"). The description keeps
  10.9 billion, from the body text.
- **Jordan's Ministry of Tourism and Antiquities.** The portal says the 1967 royal decree also placed the
  Department of Antiquities "under its umbrella", that the Antiquities Law No 21 of 1988 did so, and that
  "In 1989 the Department of Antiquities became part of the Ministry of Tourism, which thus became the
  Ministry of Tourism and Antiquities". The description keeps 1989 for the name, which is the only date
  the page attaches to the name.

## 7. Routes that failed, and the alternative tried

- `binamarga.pu.go.id/index.php/profil/tugas-dan-fungsi` — the fetch was refused at the site by
  robots.txt, so nothing of the page was retrieved. This is a route failure at one path, not a blocked
  host: the Indonesian ministry's own data host `data.pu.go.id` answered normally, and the remit was
  recovered on a second route, `peraturan.bpk.go.id`, which served Permen PUPR 13/2020. No claim was left
  unsourced by it.
- No other fetch in this check failed. Every other URL in the writer's `sources` resolved and carried
  content matching its title. The writer's own report of hosts refusing by robots or client error was not
  re-tested except where a blank rested on it (Ahwaz, where the company's site was reported as refusing);
  that blank was recovered from documents instead, so the host question did not have to be settled.

## 8. Anything I could not settle

- **Royal Caribbean's relation to the Labadie concession.** The SEC filing describes Royal Caribbean
  Group; the card's role says the right of way "is a concession from the Haitian state to Royal
  Caribbean". Which entity in the group holds that concession is not stated by either document. The
  description now names the group and says nothing about the concession.
- **CN-TIPPEE's legal status.** The loan agreement gives its founding order, its mandate and its
  direction by a permanent secretary, but neither Gabonese source states whether it is a public
  establishment, and the ministry attachment the writer cited rests on a letterhead
  ("MINISTÈRE DE L'ECONOMIE ET DE LA RELANCE" above "COMMISSION NATIONALE DES TIPPEE") rather than on a
  statement in the text. Both the "public body" claim and the ministry were cut for that reason; the
  Gabonreview training item was cut with them as incidental.
- **Whether ADETIP's labour-intensive mandate survived into ADDS.** The completion report states the
  mandate and the merger but not what became of the mandate. Not claimed.

## 9. The finding for the next round's brief

**For a public body, the writer's standard reflex — search the web for the body's own page — is the wrong
first move, and it is what produced every one of this batch's recoverable blanks and its worst
corrections.** Three of five "no page names the exact entity" blanks were sitting in the definitions
section of a loan agreement already on disk, under `cache/<PID>/AGR_*.txt`; the Ahwaz company was a
signatory to one. In the other direction, the pages that do exist are nearly always the *successor's*
page, and they describe the successor: MOICI's remit came off MOCDE's infographic, the Agency for State
Roads' creation off a page that names the 2008 body differently, the Djibouti housing fund's ministry off
a ministry created two years after the case closed, and Indonesia's directorate general off a regulation
that does not mention its tasks. The brief should tell writers to read the loan or financing agreement's
definitions section and the appraisal document's institutional-arrangements section **before** searching,
and to check any web-sourced remit against the date range in `appears_on` before writing it in the present
tense.
