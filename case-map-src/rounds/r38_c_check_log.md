# Round 38, batch C — check log

Submitted: 2 cases, no extends. **Kept 1 (rewritten), cut 1.** Output file carries
`cases` (1) and `extend` (empty array).

Documents opened: the writer's cache `/tmp/aid38c/` (RFE 29858844, index.hr, OCCRP, AidData
66093 and 37364, CRHoy 2022, La Nación 2025, Semanario Universidad 2023, La República 2017)
read in full as text; plus nine documents the writer did not have, fetched here over `curl`
with a browser user agent (all 200): RFE 31065234, AidData 39847, La República 27 Nov 2019,
La Nación 8 Aug 2024, CRHoy 6 Nov 2025 ×2, CRHoy 7 Nov 2025, La Teja 7 Nov 2025, Teletica
6 Nov 2025, El Observador 6 Nov 2025, Delfino 18 Sep 2025, Teletica 11 Sep 2026. Five
WebSearch calls.

---

## 1. `bih-chinese-flood-machinery-sold` — **CUT**

### The test-2 question, decided

The row is an AidData **Emergency Response** grant (sector field on record 66093; commitment
date 1 Jan 2014, start and end actual 23 July 2014) and the relief screen fired correctly.
The prosecutor quoted by Radio Free Europe states the chain plainly: China donated the
equipment in 2014 for returnees, and "Nakon poplava u maju 2014. godine Vijeće ministara BiH
donosi odluku da se trećina te opreme i mehanizacije preusmjeri Vladi FBiH" — after the May
2014 floods the Council of Ministers redirected a third of it to the Federation government.
BRIEF36 §2: the money responded to the harm, and when such a row is dropped the reason is
that the harm is the disaster's.

The writer's reading — that the harm is the diversion rather than the flood — is a fair
reading of test 2, and it was tested on its own terms rather than dismissed. It fails, for
four reasons, in descending order of weight.

**(a) The sentence that ties the harm to the money is not the embassy's.** This is the single
most important finding in the batch. The card says: "The Chinese embassy in Sarajevo said it
had learned from the media that the donated equipment had been sold, and that it had not been
handed to the residents hit by the floods", and `confidence_note` says "the Chinese embassy
confirmed the equipment did not reach flood-hit residents". The report calls it a quotation:
the embassy "confirmed the equipment 'was not handed to the residents hit by the floods'".
That string is not in the document. The RFE article has two sentences, and they are different
speakers:

- RFE's own framing sentence: "Iz Ambasade NR Kine u BiH, poslali su saopštenje u kojem je
  navedeno da je kineska vlada pružila pomoć BiH nakon poplava, **ne sluteći da** donirani
  traktori i oprema **nije predata** stanovnicima pogođenim poplavama." The clause about the
  equipment not being handed over sits inside RFE's "not suspecting that" — it is the
  journalist's assertion about what the embassy did not know, not the embassy's statement.
- The embassy's actual quoted words: "Od relevantnih medija u BiH nedavno smo dobili
  informacije da je donirana oprema prodavana i da je bila predmet malverzacija. **Nadamo se
  da će relevantne institucije BiH što prije saznati istinu**, jer vjerujemo da one imaju
  sposobnost rješavanja tih problema." The embassy says it learned from the media that the
  equipment was sold and that it hopes the institutions establish the truth.

So the one piece of non-allegation evidence that the entitled households went without is a
journalist's subordinate clause, and the half of the embassy's statement that cuts the other
way — hoping the truth will be established — was dropped. Selective quotation, in the
direction the fault always runs.

**(b) The only cohort with a count is the prosecution's allegation and is not about the
project's beneficiaries.** "Mladina je prevario više od 50 osoba" is introduced by "kako
tvrdi Tužilaštvo" — as the Prosecution claims. The conduct is dated in the document: "od
2015. godine **nakon što mu je prestao mandat** u Vladi FBiH" — from 2015, after his
government term ended, taking 2,000–5,000 KM (once 20,000) from people he promised to
"arrange" a tractor for while "lažno se predstavljajući kao vladin povjerenik ili kao
konsultant kineske ambasade". These are people defrauded by a private individual
impersonating an official, not people who lost land, livelihood, access or a payment owed by
the financed activity.

**(c) The flood-hit households are neither named nor counted.** The card says so itself. The
nearest thing to a statement that they went without is the Farmers' Association president's
characterisation ("Sramota je da naši poljoprivrednici voze traktore stare više od 40
godina..."), which carries no count. That is thinner than Bukoba, which CHECK31 sets as the
floor for limb (b).

**(d) The writer's own rule disposes of it.** The batch report's closing note: "Seven of
thirteen drops are an official or an executive prosecuted for stealing the money. That is a
recognisable class in this dataset and it is never limb (b)" — and it adds that such a
pre-screen "would have cleared ... most of G428's flag". This row is the eighth member of
that class.

### The absence claim the writer made, refuted

The report says "no verdict was reported in anything that opened, and searches for the case
outcome in Bosnian returned nothing relevant". One WebSearch found the follow-up on RFE's own
site: **"Bivši ministar iz BiH optužen za prisvajanje traktora koji je Kina donirala
poplavljenima", RFE, 23 January 2021** (https://www.slobodnaevropa.org/a/31065234.html).
It carries facts harder than anything on the card, and they cut against the card as written:

- The **Municipal Court in Sarajevo confirmed the indictment** of the Sarajevo Canton
  Prosecutor's Office against Desnica Radivojević for abuse of position or authority,
  confirmed to the FENA news agency by the prosecutor's office. A confirmed indictment is a
  court act; the April 2019 figures are not.
- What the confirmed indictment covers is **one tractor and trailer**: from July to December
  2014 he sought a tractor he had no right to, was not on the municipal register of
  agricultural holdings and his land was not flood-damaged, found a qualifying person in
  whose name a tractor would be fictitiously donated, and approved payment of 5,000 KM from
  the Federation budget, "čime je oštetio Budžet FBiH za iznos od 5.000 KM, a sebi pribavio
  protupravnu imovinsku korist u vrijednosti doniranog traktora i prikolice u ukupnom iznosu
  od **15.852,84 KM**". The victim named in the indictment is the Federation budget.
- "U **martu 2019**. godine izvedena je akcija kodnog naziva 'Farmer'" — which dates the eight
  detentions, and "Predmet protiv Radivojevića izdvojen je u odnosu na ostale osumnjičene,
  protiv kojih je istraga nastavljena": as of January 2021 the investigation against Mladina
  and the rest was still running. No verdict against anyone surfaced in four searches
  (Bosnian/Croatian terms for verdict, indictment, the operation name and the defendants'
  names). So the million marks and the 50-plus remain untested allegations, and the one
  charge a court has let through is worth 15,852.84 KM and 5,000 KM of public money.

### Figure-by-figure result on the cut card, for the record

Confirmed against the documents: 96 tractors with attachments, 37 motocultivators, 52
chainsaws, 26 milking sets, 22 milk coolers, 11 milk analysers (RFE, final paragraph, exact);
28 tractors and machines seized across the wider Federation area on Cantonal Court orders, as
**the Federal Police Administration confirmed** ("Kako su potvrdili u FUP-u") — the card says
"Police seized", which is right, and sensibly drops the police's "nezakonito"; one month's
custody for Mladina, Džafo and Jašarević with the other five released under restrictions;
Radivojević arrested 2 April 2019 in Sarajevo (index.hr: "uhićen je danas u Sarajevu",
confirmed by the Sarajevo canton prosecutor's office); eight detained in operation Farmer
"u nedjelju" (index.hr) suspected of unlawful resale of equipment worth about 500,000 euros;
Mladina chaired the allocation commission and was a former adviser to Nermin Nikšić; the
three allocation criteria; Nikšić's response.

Corrections that would have been needed had it been kept:
- **Whose sentence.** The "more than six million marks", the 2014 donation date, the Council
  of Ministers' decision and the three cantons are all inside the **prosecutor's** statement
  at the detention hearing, not RFE's reporting; the card attributes them to "Radio Free
  Europe". The million-mark gain is Željka Tomić-Anđušić's and the 10,000–15,000 KM per
  tractor is Nevena Alićehajić's; the card attributes both to the pair jointly.
- **index.hr's 500,000 euros** is the value the eight are *suspected* of reselling
  ("Njih se sumnjiči da su umiješani u nezakonitu preprodaju ... vrijedne oko 500 tisuća
  eura"), not a valuation the paper makes.
- **The `point` note is wrong about its source.** It says "cantons from AidData record 66093".
  AidData says "the Zenica-Doboj, Tuzla, Pasavina, and Brcko **districts**" (four, spelled
  Pasavina in the narrative and Posavina in the geospatial note); the three **cantons** come
  from the prosecutor via RFE.
- The date conflict the writer flagged is real and both halves are in the document: the lede
  says "traktora koje je Kina još **2012**. godine poklonila Bosni i Hercegovini" and the
  prosecutor says "NR Kina **2014**. godine donirala". The card handled this correctly.
- AidData's own "the equipment **reportedly** never reached those affected by the floods" is
  AidData prose with a hedge, and BRIEF36 says AidData prose is not a document.

The OCCRP page in the cache (`occrp.html`) is a different case entirely — 11 arrests on
10 September 2014 in operation "Brend" over phony meat companies and $7.6 million of unpaid
tax, involving the Lijanović brothers. Correctly not cited.

**Drop reason for `leads_aiddata.json` r36_outcome:** the harm is the disaster's — an
Emergency Response grant redirected to flood-hit households after the May 2014 floods; the
diversion is a domestic embezzlement whose counted victims are the prosecution's allegation
and the Federation budget, and the one confirmed indictment (Municipal Court Sarajevo,
January 2021) covers one tractor and trailer at 15,852.84 KM plus 5,000 KM of budget money.
No document names or counts a flood-hit household that went without.

---

## 2. `costa-rica-route-32-possession-before-payment` → **KEPT, rebuilt** as
`costa-rica-route-32-worker-deaths-roundabouts`

### The agreed-possession question, decided: not harm

An entry into possession agreed with the owner while payment is being formalised is not a
documented harm to identifiable people. The deciding sentence is the one the card is built
on, read whole (CRHoy, 24 October 2022, quoting CONAVI's executive works report 48):
"solo 182 (el 28,57%) de los terrenos está en poder del Estado y otros 164 poseen entrada en
posesión voluntaria **tras acuerdos con los dueños** por mientras se formaliza el pago." The
owners agreed; no deadline is stated; no sum is owed in any source; no owner is named; the
count is of plots. Against the standing edges: Bukoba has compensation unpaid in five
identified cases at a named site, and Hopewell has a payment recorded "Awaiting payment"
past a stated expected date with no amount six months later. Neither shape is present. The
map's rule that a hazard relocation is not automatically harm applies in the same form here:
an expropriation is not automatically harm, and a document has to record a loss on top of the
taking. One document records the opposite — that in some cases money had already been
**deposited for the owners** with the Attorney General's office and had to be returned when
the ministry dropped the files (La Nación, 8 August 2024).

Two further things settle it. The fallback the writer named — the finance minister's "se
iniciaron las obras sin tener las expropiaciones listas" — is one item in a list of the
loan contract's management problems, and is about delay. And the writer dropped a Costa Rican
sibling row in this same batch (G521, Barranca–Limonal) on exactly this ground: "'Only 8% of
necessary land expropriations had been made' is a **delay statistic, not a taking**." The
same standard applied to Route 32 cuts the possession-before-payment framing.

### So why the case survives: a real limb (b) was there and the batch missed it

Two named workers were killed and others seriously hurt on the financed works, and four
Costa Rican outlets covered it. The documents:

- **CRHoy, 6 November 2025**: "René Marquetti, un obrero de nacionalidad cubana, falleció la
  mañana de este jueves en un accidente de tránsito en Limón 2000, luego de que un contenedor
  lo aplastara **mientras trabajaba en las obras de la ruta 32**"; he did excavation for pipes
  and poured concrete for drainage; the accident was at about 6:05 a.m.; per the Traffic
  Police the trailer driver "en apariencia ... viajaba a exceso de velocidad".
- **CRHoy, 7 November 2025**: the second dead man, Didier García Brenes, 53, of Jicaral de
  Puntarenas, about 20 days on the job, "una de las dos víctimas mortales ... cuando un
  contenedor cayó sobre varios trabajadores que laboraban en **las obras de ampliación de la
  ruta 32**"; OIJ investigating.
- **La Teja, 7 November 2025**: the survivor Roberto Barrantes names the employer —
  Marquetti and "Diddier" García "eran compañeros de trabajo de Roberto en la empresa **China
  Harbour Engineering Company (CHEC)**" — says the group had arrived by truck minutes before
  "a trabajar en las labores de ampliación de la carretera", that the trailer "venía a alta
  velocidad, por eso fue que no agarró la vuelta, pegó contra el muro", and that the two who
  died were having breakfast with their backs turned. He hurt his ribs, an ankle and his nape.
- **Teletica, 6 November 2025**: "murieron dos hombres y otros **cuatro** resultaron
  gravemente heridos"; the injured man whose brother-in-law it interviews is "uno de los
  trabajadores de China Harbour Engineering Company (CHEC)"; hauliers and residents blame the
  roundabouts ("Esta construcción está mal hecha", Jorge Mena); Lanamme-UCR had warned that
  eight of the nine roundabouts opened on the road can cause problems.
- **El Observador, 6 November 2025** (page's own date line, 9:28 a.m.): the trailer overturned
  and struck two people; the victims wore MOPT vests but "no son trabajadores directos de la
  institución, sino contratados por una empresa que daba el servicio al Ministerio"; MOPT said
  the accident was where road works are under way; "Las obras **formarían parte** de las
  labores de construcción y ampliación de la ruta 32."

`killed: 2` follows the map's own precedent, not a new rule. CHECK31 separates the two tests:
which credit paid for the works decides whether the death belongs to the project, and whether
a cause is stated decides whether it is counted. The loans financed 85% of the CHEC EPC
contract for this widening; two sources put the men on CHEC's payroll; a cause is stated. The
closest live card is `igoeti-sveneti-highway-worker-death-and-land-damage`, `killed: 1`, a
worker "killed by a speeding car whose driver ignored a road construction warning sign" while
testing pavement on the project section; `beira-maputo-climate-works-deaths-compensation`
counts "a worker hit by a third-party vehicle while moving between work sites". CHECK20's
exclusion is for road accidents **on a finished road** — users of a completed project — which
this is not.

Everything that cuts the other way is on the card: the two men were at breakfast when it
happened; the Traffic Police's stated cause is a speeding trailer, not the works; El
Observador's employer line contradicts Teletica's and La Teja's; and no document connects the
accident to the roundabout design, so the card says that in `killed_note` and in
`confidence_note` rather than letting the Lanamme warning and the court judgment imply it.

### The two independent findings that put the case outside the lender

- **A court finding.** Delfino.cr, 18 September 2025: the Constitutional Chamber "declaró con
  lugar un recurso de amparo contra el ... MOPT y el ... Conavi, por las deficiencias de
  seguridad detectadas en las rotondas construidas en la Ruta Nacional 32, en el tramo entre
  el cruce a Sarapiquí y Limón", in judgment **2025-29197** of 12 September, written by
  magistrate Ingrid Hess Herrera, ordering the minister and CONAVI's director to implement
  Lanamme's measures "en el plazo de UN AÑO". Lanamme's report to the court: the roundabouts
  meet the contract's parameters but do not exceed the minimums of international standards and
  lack technical justification against the originally planned grade separations. The sentence
  that cuts the other way is in the same article and is on the card: MOPT "ha defendido en
  varias ocasiones que las obras se construyeron como soluciones temporales debido a atrasos
  en las expropiaciones".
- **A national audit finding.** Comptroller General's report, reported by Teletica,
  11 September 2026: the temporary roundabouts added by the last contract addenda do not meet
  the requirements for heavy trucks and were designed for 20 km/h and light vehicles; Lanamme
  and the Directorate General of Traffic Engineering had both warned of visibility and turning
  radii; the road still runs on temporary solutions with no financial plan for the definitive
  grade separations; CONAVI ordered **74** expropriation files dropped to justify using the
  right of way and had to reverse it after the Attorney General's warnings; the executing unit
  admitted losing supporting documents to a raid and seizure by the Public Prosecutor's
  Office; the report follows the expiry of the CHEC contract and the dissolution of the
  executing unit in April. This is the evidence class BRIEF36 asks for, and it was not in the
  batch.

`confidence` stays **documented**, now on four outlets, a Constitutional Chamber judgment, a
university laboratory report to that court and the Comptroller General — none of them the
lender's.

### The absence claim on the card, refuted

`confidence_note` said: "Three counts of the expropriations needed do not line up and the
documents do not explain the gap." Both halves are wrong, and one of the missing figures is
in an article the card already cites.

1. **There are at least six counts, not three.** The card missed the one in its own source:
   Semanario Universidad, 2 November 2023, two paragraphs below the sentence the card quotes —
   "uno de los mayores riesgos son los atrasos en las expropiaciones, ya que **se requerían
   581 expropiaciones y a la fecha sólo hay 238 a nombre del Estado**." And La Nación of
   8 August 2024 gives two more from the UN Office for Project Services report: "actualmente
   se requieren **496** terrenos, de los cuales ya hay 362 inscritos a nombre del Estado, por
   lo que aún hay pendientes 134 gestiones. En tanto, el recuento hecho en marzo contemplaba
   **569** expropiaciones, de las cuales se habían completado 345 y quedaban en trámite 245
   expedientes." Note that the March figures in that sentence do not add up (345 + 245 = 590
   against 569); both are printed as the article gives them and not reconciled.
2. **Two documents explain the reductions.** La República, 27 November 2019, quoting the
   executing unit: "Con esta medida de **limitar el proyecto al derecho de vía** se calcula
   que pueden existir alrededor de 700 expropiaciones" — the fall from about 1,400 to about
   700. And La Nación, 8 August 2024: "El MOPT desistió de al menos **73** expropiaciones por
   considerar que ya no serán necesarias ... principalmente por el cuestionado cambio en los
   diseños que sustituye los pasos a desnivel e intercambios por **rotondas**", published
   across 47 pages of Alcance 135 to La Gaceta 141 of 1 August. The Comptroller General puts
   the same decision at 74 files and says it was reversed. Both counts are on the card with
   their owners; neither is picked over the other.
3. The card also dropped the figure in the sentence **immediately after** its CRHoy quote —
   "de los 637 trámites requeridos, ya **606** adquisiciones se presentaron ante la ...
   (DABI)" — and the minister's "la empresa tenía a disposición un **54%** del derecho de vía
   liberado". Both cut against the picture of a state not acting. The 606 is now on the card.

### Other corrections made to the Costa Rica card

- **`id`** changed from `possession-before-payment`, which named a harm that has been removed,
  to `worker-deaths-roundabouts`. No case with either id is on the map (checked all 1,176
  live cases; nothing in Costa Rica or anywhere mentions Route 32 or CHEC, so no duplicate and
  no extend is due).
- **Coordinate and `ap`.** The writer put the point on Siquirres, mid-corridor, with
  `ap: true`. The harm is now at a roundabout by the Limón 2000 entrance and no source gives a
  coordinate for it, so the point moves to the Limón end of the route **as AidData itself
  gives it** (OpenStreetMap 9.9919, -83.0248 in record 37364), `ap` stays true, and `point`
  says plainly that it stands for the corridor and that the roundabout's own location is not
  published. That is round 32's precedent — flag the placement rather than invent one.
- **A figure dated from a byline.** The card dated the UN office report's cut-off "31 March
  2025" four times. The article's sentence says only "con cierre al **31 de marzo**"; the year
  comes from the 9 May 2025 byline, which BRIEF36 bars. The card now gives the cut-off as
  "31 March" with the reporting date attached.
- **Attribution of the valuation sentence.** The card gave "the State's valuation covers the
  land only, not the cost of moving a business, customers lost or other losses to the owner"
  to "lawyer Natiuska Traña of Pacheco Coto". In the article that sentence is unattributed
  narration after "agregó Traña", and it is a statement about Costa Rican expropriation
  practice in general, not a finding about any Route 32 owner. Removed rather than re-sourced:
  with the possession claim gone it supports nothing on the card.
- **Law 9293's approval date, printed both ways**: AidData says the government approved the
  two agreements on 10 March 2015; Semanario Universidad's account of the finance minister's
  appearance says "En febrero de 2015 se aprobó la Ley 9293". Both are in `lenders[0].role`.
- **`lenders[0].role` additions, all verified in AidData 37364 and 39847**: the $396 million
  total for the two agreements; the 0.25% commitment and management fees; the AidData staff
  comment that the China-Latin America Finance Database treats the project as a single $395
  million loan. Everything the writer had in that field — both signing dates, the loan number
  1420202052013211015, the rates, maturities and grace periods — is confirmed verbatim.
- **AidData record 39847 was cited in the prose but missing from `sources`.** Added; it
  resolves (RMB 628 million concessional loan, $105,605,312 in constant 2023 USD).
- **`conditions`**: the 85% of the $465,593,387.06 CONAVI-CHEC-00 contract is exact. Added
  that the expropriations and utility relocation were the national counterpart's, with all
  three published counterpart figures and their dates ($69m in 2017, more than $55m in 2022,
  almost $90m in 2023) rather than one.
- **`outcome`**: minister named (Luis Amador); added the State's broken four-month promise,
  the 84.3% physical progress at September 2023, AidData's 91.85% at December 2024 with a
  28 May 2025 target, and the Comptroller's 30-day order. Corrected the May 2025 statement:
  the executing unit's head said the **four lanes of the main trunk along 104 km** between the
  Río Frío junction and the centre of Limón would be functional in October with minor works to
  follow — not "sections".
- **`suppression`** was empty and is now filled from CRHoy, 6 November 2025: the October–
  November 2024 protests against the roundabouts, the president calling the movement "16
  gatos", the then minister saying the group wanted to "joder" the government, and the
  president saying he would apply the law against people protesting. The protests are not the
  harm — BRIEF36 is right that a protest is not harm on its own — but they belong beside a
  documented harm.
- **Two source citations were unusable as cited.** The La Nación 2024 slug reads "mopt
  renuncio a 73 expropiaciones" but the page's headline is "MOPT desiste de expropiar 73
  terrenos en ruta 32 al optar por cuestionadas rotondas"; the title is now the page's. The
  Semanario Universidad `?p=295773` form resolves with a redirect to a canonical slug, which
  the card now uses.
- `kind` absent and no `displaced` key on the card; `displaced_note` explains that the counts
  are of plots and files. Verified programmatically on the output, along with all 24 keys
  `merge.py` asserts.

### Corrections considered and rejected

- **Calling 107 km and 104 km a conflict.** AidData and CRHoy give the project's extent as 107
  km; La Nación's 104 km is the length of the main trunk whose four lanes the executing unit
  said would be functional in October 2025. Different quantities, so no conflict is announced;
  each figure stays with its own sentence.
- **Calling CRHoy's "$465 millones son financiados por el Exim Bank" a conflict with La
  República's "$396 millones son vía empréstito con el Eximbank".** They measure different
  things at different dates and the card uses neither as the loan amount; the loan figures come
  from AidData's two records. Noted below, not on the card.
- **Counting the 19 plots awaiting demolition as harm.** Structures, not people, and pending.
- **Counting the 700 right-of-way occupations (La República, 2017) as harm.** A pre-works
  count of occupations with no removal recorded anywhere.
- **Using the 14 November 2025 La Nación report of a worker injured by a falling tree on Route
  32.** Read in full: that man was on a MOPT/CONAVI clearance crew working on a landslide at
  km 31, with the road closed since 3 November 2025. Different works, not the widening.
- **Adding the 12 November 2025 Delfino item on the Constitutional Chamber giving CONAVI three
  days to account for wildlife crossings.** Only the headline was seen; `ecosystem` is left
  empty rather than built on a headline. A lead for round 39.
- **Keeping the expropriation material as the harm but marking it `contested`.** Rejected: the
  defect is not thin evidence of a harm, it is the absence of a recorded loss. The material is
  kept as context in `community` and explicitly not as harm.

---

## End-of-log items

**1. What could not be checked.** No verdict in the Bosnian case was found; what exists is the
confirmed indictment of one defendant (January 2021) and a statement that the investigation
against the others continued. Four searches on Bosnian and Croatian terms. Lanamme's report
EIC-Lanamme-INF-0287-2025 and the Comptroller General's report on Route 32 were read only
through press accounts (Delfino, CRHoy, Teletica); the reports themselves were not opened, and
the card attributes each finding to the outlet that reported it. CONAVI's executive works
report 48 and the UN Office for Project Services reports likewise reach the card only through
CRHoy and La Nación, which is stated on the card.

**2. Figures where documents disagree, left unreconciled.**
- Injured at Limón 2000 on 6 November 2025: four seriously injured (Teletica) against six
  injured (CRHoy). Both on the card.
- Employer of the dead men: CHEC (Teletica, La Teja) against a company contracted to the
  ministry, unnamed (El Observador). Both on the card.
- Expropriation files dropped after the redesign: at least 73 (UN office report via La Nación,
  August 2024) against 74 (Comptroller General via Teletica, September 2026). Both on the card.
- Law 9293's approval: 10 March 2015 (AidData) against February 2015 (Semanario Universidad).
  Both on the card.
- Within one article: the March count of 569 required with 345 completed and 245 in process
  (La Nación, 8 August 2024). Printed as given.
- Not used on the card, so recorded here only: the share financed by Eximbank is "$465
  millones" of a cost of more than $521 million in CRHoy (October 2022) and "$396 millones ...
  vía empréstito" within a $465 million investment in La República (November 2017); the
  national counterpart is $69m, more than $55m and almost $90m in three sources at three dates.
- Bosnia: China gave the tractors in 2012 (RFE's lede) against 2014 (the prosecutor, in the
  same article, and AidData's grant year). The writer handled this correctly.

**3. Faults appearing in more than one card.** Both cards rest their decisive link on a
sentence whose speaker is not the speaker the card names: the Bosnian card gives a journalist's
clause to the Chinese embassy, and the Costa Rican card gives La República's general statement
about expropriation valuations to a named lawyer. Both cards also carry an absence claim that
one fetch refuted — a verdict search that stopped too early, and "the documents do not explain
the gap" when two of them do. That is one habit, not three faults: a sentence or an absence
accepted without going back to the paragraph.

**4. Wrong in card data outside the fields asked about.** The Bosnian card's `point` cites
AidData for "cantons" when AidData says "districts" and lists four of them including Brčko,
while the card's `place` lists three. The Costa Rican card's `place` and `point` named the
corridor's west end as the "Route 4 junction" while two of its own sources call it the Río Frío
junction; AidData settles it — "the Route 4 junction at Frío river" — and the rebuilt card uses
that wording so the sources can be matched to the card. `ct: ["tied"]` on the Costa Rica card
is sound on AidData's own record: the EPC contract with CHEC was signed the same day as the two
loans that were to fund 85% of it.

**5. Routes that failed, named as routes.** None failed. Every URL on the output card was
fetched here over `curl` with a browser user agent and returned 200: china.aiddata.org,
larepublica.net, crhoy.com, nacion.com, lateja.cr, teletica.com, observador.cr, delfino.cr,
semanariouniversidad.com (which 301s from the `?p=` form to a slug), slobodnaevropa.org,
index.hr. No host refused anything. The writer's route note stands and is worth keeping for
round 39: AidData project pages serve in full over `curl`, the source **titles** are in the
`window.__reactRouterContext` blob and the source **URLs** are not in the page at all, so
sources have to be found by searching their titles. Separately, the full project narrative and
the structured fields (sector, flow type, commitment and actual dates, agencies, loan terms)
render from the plain HTML with scripts stripped — no JavaScript execution needed.

**6. For round 39.** The Route 32 row shows the shape this tranche keeps producing: the
AidData text and the flagged sentences pointed at expropriation delay, which is not harm, while
the harm — two workers killed, four to six hurt, a Constitutional Chamber judgment and a
Comptroller General's report — was in the national press of the same corridor and none of it is
in AidData's record. Searching the project's name plus a worker-death term in the national
language found it in one search. The Barranca–Limonal row dropped as #8 in this batch deserves
the same single search before it is left dropped.
