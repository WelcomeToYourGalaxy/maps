# Round 38, batch C — verification of a checker-authored card

Card under review: `costa-rica-route-32-worker-deaths-roundabouts`, the single case in
`rounds/r38_c_checked.json`, written by the batch's checker after it cut the writer's
`costa-rica-route-32-possession-before-payment`. Written by nobody who has checked it until now.

**Verdict: the card stands with corrections, and `killed` stays at 2.** Output:
`rounds/r38_c_verified.json`, one case, `extend` empty.

Everything below rests on documents opened here, not on the check log. Twenty-two sources, every
one fetched over `curl` with a browser user agent and returning 200 — the list and the status codes
are at the end. Added to what the checker had: the loan agreement annexed to Law 9293 (primary
text, AidData's copy, read with `pdftotext -layout`), Teletica's first report of the accident
(6 November 2025, 6.54 a.m.), El Observador and Semanario Universidad on Lanamme's report,
Semanario Universidad on the judgment, and Delfino, CRHoy, El Observador and Semanario Universidad
on the Comptroller General's order. Five WebSearch calls.

---

## 1. `killed: 2` — **stands**, and the note is rewritten so that it rests on what holds

### Does a document place the men at the works, working on this project, when they were killed?

Yes, four times over, and the two tests CHECK31 separates are applied separately.

- CRHoy, 6 November 2025, 6.44 p.m.: "René Marquetti, un obrero de nacionalidad cubana, falleció la
  mañana de este jueves en un accidente de tránsito en Limón 2000, luego de que un contenedor lo
  aplastara **mientras trabajaba en las obras de la ruta 32**." The same article has his work —
  excavation for pipes, concrete for drainage — and the Traffic Police's sentence, in which the
  container "cayó sobre varios trabajadores **que realizaban mejoras en la ruta**".
- CRHoy, 7 November 2025: Didier García Brenes was "una de las dos víctimas mortales ... cuando un
  contenedor cayó sobre varios trabajadores que laboraban en **las obras de ampliación de la ruta
  32**".
- La Teja, 7 November 2025: the group arrived by truck "pocos minutos después ... **a trabajar en
  las labores de ampliación de la carretera**".
- The public works ministry itself, the same morning: "El MOPT informó que el accidente sucedió en
  un lugar donde se realizan trabajos en la carretera", and El Observador adds "Las obras
  **formarían parte** de las labores de construcción y ampliación de la ruta 32" (El Observador,
  6 November 2025, 9.28 a.m.).

Two named men, a named date and hour, a named place, employment on the works in three independent
outlets and the responsible ministry placing the accident in a live work zone. This is not round
31's Abidjan–Lagos shape, where the cut to 0 rested on a collective cause for five unnamed dead, a
floor figure ("at least 22 accidents, including five fatalities") and a report that could not place
the deaths on the IDA-financed section.

### Who employed them? — **not settled; both printed, and the card's claim narrowed**

**A correction the card needed.** The card said "Teletica and La Teja report the two men killed on
6 November 2025 as CHEC workers", and `confidence_note` said "two of which put the dead men on
CHEC's payroll". Teletica's sentence is about a survivor, not the dead: "El cuñado de uno de los
trabajadores de **China Harbour Engineering Company (CHEC) que resultó herido** tras el vuelco de
un tráiler". Only La Teja puts the dead men at CHEC, and it is La Teja's own narration rather than
the survivor's quoted words, which the check log also had slightly wrong: "perdieron la vida el
cubano René Marquetti y Diddier García, **quienes eran compañeros de trabajo de Roberto en la
empresa China Harbour Engineering Company (CHEC)**". Against that, El Observador: the victims wore
vests with the MOPT insignia but "no son trabajadores directos de la institución, sino contratados
por una empresa que daba el servicio al Ministerio", unnamed.

Both readings are now on the card and in `confidence_note`, with what each outlet actually says
about whom. Not reconciled: CHECK20 bars a tidy reconciliation of two conflicting figures and this
is the same fault in a name field. It does not change the count either way — on both readings the
men were employed by a contractor working on these works, which is what the first test asks.

### Is a third party's speeding trailer a cause that ties the death to the project?

I opened `igoeti-sveneti-highway-worker-death-and-land-damage` in the live map and read its
reasoning rather than the check log's summary of it. Its `killed_note` says: one local employee of
the first road contractor, killed on the project section while performing a pavement test, "killed
by a speeding car whose driver ignored a road construction warning sign"; the completion report
calls it "the fatal accident on the Project section" and draws the lesson "that traffic safety
during construction works on roads remains a problem"; and then the operative sentence — "**The
cause the document gives ties the death to the works, so it is counted.**" The killer there is a
third party too. What did the tying was that a document recorded the death as an incident of the
works, in a work zone, during construction.

`beira-maputo-climate-works-deaths-compensation` counts, among five, "a worker hit by a third-party
vehicle while moving between work sites".

The same elements are present here, from documents outside the lender rather than from a completion
report — which BRIEF36 says is the whole evidence position for Chinese state credit, there being no
completion report to have. Workers on the works, in the work zone, during the working day, killed by
a vehicle that failed to negotiate a structure the works had built, with the responsible ministry
telling drivers that day to respect the signage because road works are under way.

And CHECK20's exclusion does not reach it. The excluded class, as round 37 applied it to
Cikampek-Palimanan, is "road-accident deaths **on a finished road**" — users of a completed
project. This road was not handed over: the contract ran until April 2026 and the Comptroller
found unfinished works after it expired.

**So the count holds, but only on that ground.** The roundabout-design theory carries no weight in
it, and the rewritten `killed_note` says so in terms: "They are counted because the documents place
them at work on the financed works when they died, and not because any document blames the
roundabout." Against the design theory: the Traffic Police's stated cause is speeding; the ministry
said the judicial authorities would determine the causes; the people who blamed the roundabouts are
hauliers, residents and the amparo petitioner, not an authority on causation; the judgment and
Lanamme's report predate the deaths; and the Comptroller's order of September 2026 does not mention
them. I checked that last point by reading two accounts of the order in full — neither Delfino's
nor Teletica's mentions any death.

Two things found here that cut *towards* the design theory, and which the card does not use as
cause because no document applies them to this crash: Lanamme had warned, in Teletica's own words
on the day, that eight of the nine roundabouts "pueden ocasionar algún tipo de problema, **como el
ocurrido este jueves**"; and heavy vehicles had already come off at these roundabouts — "Desde que
entraron en funcionamiento, se han registrado accidentes con vehículos pesados por la dificultad
para dar las vueltas requeridas" (El Observador), with a heavy truck failing to take a roundabout
and leaving the road in March 2025 (Semanario Universidad). The Comptroller's own list of what the
undersized design could cause includes "**vuelcos de vehículos pesados**". All of that is on the
card as the roundabouts' record; none of it is on the card as this crash's cause.

### The injured — a third reading was missing

The card gave two: four seriously injured (Teletica) and six injured (CRHoy). Teletica's **first**
report, 6.54 a.m., carries the Red Cross count: four patients attended, two taken urgently to the
Tony Facio hospital, two declared dead at the scene; El Observador has the same at 9.28 a.m., with
the incident reported at 6.40 a.m. Three readings, each now on the card with its outlet and its
time of day, unreconciled.

---

## 2. The three tests, on this harm — **all three pass, and the Burkina Faso error is not present**

**Were the roundabouts and the widening the Chinese money financed? Yes, at the level of the
contract, and I checked it in the loan text rather than in a summary.** AidData's description says
the proceeds were to finance 85% of a $465,593,387.06 EPC contract, CONAVI-CHEC-00. The agreement
annexed to Law 9293 — the primary document, read in full — says it itself: CONAVI and CHEC
formalised the Commercial Contract on 3 June 2013 "sobre la implementación del Proyecto para el
Diseño, Rehabilitación y Extensión de la Ruta Nacional No. 32 ... con un monto total de
465,593,387.06 dólares", and China Eximbank "acuerda suministrar un mecanismo de financiamiento ...
por un monto máximo total de hasta **85% del CC** al GRCR, para el fin de implementar el Proyecto.
Y el 15% restante del CC lo recaudará por sí mismo el GRCR." The facility is the RMB 628 million
concessional loan plus the US$296 million buyer's credit, disbursed in that order, at a blended rate
of about 3.5%.

The credit is therefore tied to the whole contract for this corridor, not to a named section — which
is the opposite of round 19's Burkina Faso finding, where a determination put the airport platform
outside the project, and of round 31's Abidjan–Lagos footnote, where IDA financed only Aboisso–Noé.
Nothing here carves the Limón end out.

And the roundabouts are works under that contract. The Comptroller General's order, reported by
Delfino on 11 September 2026, says the investigation concerns "las modificaciones introducidas
mediante las **adendas 7 y 8 del contrato CONAVI-CHEC-001**": addendum 7, authorised in June 2024,
temporarily replaced nine permanent works — three interchanges and six vehicular overpasses — with
seven roundabouts and two at-grade right-turn accesses, "principalmente ante los atrasos en la
obtención de terrenos mediante expropiaciones"; addendum 8 of June 2025 added two more roundabouts.

**The one real limit, now stated on the card.** The facility is capped at 85% of the contract *as
signed in 2013*. The cost rose to $552.5 million, the counterpart grew from $69 million to almost
$90 million, and addendum 7 allocated $900,000 for each of six roundabouts with $1,408,617.46 of
corrections on top. No document says whether loan proceeds or the national counterpart paid for the
addenda. `conditions` and `confidence_note` now say that rather than leaving the reader to assume
the credit paid for the roundabout the men died at.

Test 2, actual harm: two deaths. Test 3, timing: works ordered to start 20 November 2017 under the
credit, 82.4% of it consumed by September 2023, 91.85% of the project complete at December 2024,
contract expired April 2026; the deaths fall inside that.

---

## 3. `confidence: documented` — **stands.** Both documents exist and say what the card says

- **Judgment 2025-29197.** Delfino, 18 September 2025, carries the number, the date of 12 September,
  the drafting magistrate Ingrid Hess Herrera, both officials ordered by name (minister Efraím
  Zeledón Leiva, CONAVI executive director Mauricio Sojo Quesada), the petitioner Marco Vinicio Levy
  Virgo, the tramo "entre el cruce a Sarapiquí y Limón", and the operative words quoted: "Se ordena
  [...] que en el plazo de UN AÑO [...] se implementen las medidas técnicas y recomendaciones
  emitidas por el Lanamme". Semanario Universidad corroborates independently and adds the court's
  ground — the order was made "luego de determinar que hay **riesgo a la vida y la integridad
  física de los usuarios**" — and the specific corrections ordered. That ground is a finding of
  risk, so it is on the card as the roundabouts' record and not as harm; a risk is what test 2
  excludes.
- **Lanamme's report.** It has a number, which the card lacked: **EIC-Lanamme-INF-0287-2025**, from
  a study run between March 2023 and March 2025 (El Observador; Semanario Universidad). Added.
- **The Comptroller General's order.** It has a number too, which the card lacked: **oficio
  DFOE-CIU-0430**, issued Friday 11 September 2026 to the public works minister and CONAVI's
  executive director (Semanario Universidad). Four outlets report it — Teletica, Delfino, CRHoy,
  El Observador — and Delfino's account is far fuller than the one the card was built on; the
  substance now on the card is drawn from both and attributed.

**Neither primary document could be opened.** Named as routes, not as hosts, and each after
another was tried: `curl` to `cgrfiles.cgr.go.cr` — connection reset by peer; `curl` to
`documentos.cgr.go.cr` — proxy CONNECT tunnel 502; `curl` to
`www.cgr.go.cr/03-documentos/publicaciones/informes-dfoe.html` — 403, while `www.cgr.go.cr/`
itself returns 200; `curl` to the search endpoint `cgrbuscador.cgr.go.cr/BuscadorWebCGR/buscar` —
connection reset; WebFetch to the same endpoint — refused at the site as robots-disallowed.
`nexuspj.poder-judicial.go.cr/index.php/search` returns 200 with an 11 KB application shell on
every query — a shell route, not a dead link — and three guessed API paths under it returned 404 or
the same shell. `lanamme.ucr.ac.cr` serves (200 on a repository handle) but its
`simple-search` route 404s. So the judgment, the laboratory report and the audit reach the card
through the outlets that reported them, which `confidence_note` now states.

`documented` is right on CHECK20 §3 either way: four independent outlets on the deaths, a court
record, a university laboratory report to that court and a national audit office, none of them the
lender's and none of them reporting on itself.

---

## 4. The ordinary faults, each by name

**Quoted words not in the quoted document.** Grepped every quoted string on the card against the
cited page. All present and exact: "tras acuerdos con los dueños por mientras se formaliza el pago"
(CRHoy 2022), "en apariencia ... exceso de velocidad" (CRHoy), "no son trabajadores directos de la
institución, sino contratados por una empresa que daba el servicio al Ministerio" (El Observador),
"Esta construcción está mal hecha" (Teletica), "funcionales y seguras", "16 gatos", "joder" (CRHoy,
6 November 2025), "en el plazo de UN AÑO" (Delfino). No invented string found.

**A finding stated more strongly than the cited documents state it — corrected.** The card had
Lanamme finding that the roundabouts "do not reach the minimum diameters set by international
standards", cited to Delfino and CRHoy. Delfino says "**no superan** los mínimos establecidos por
estándares internacionales"; CRHoy says "**ninguna alcanza un diámetro superior al mínimo
establecido**". Both mean the roundabouts do not *exceed* the minimum, which is weaker than not
reaching it. The stronger reading does exist — it is the report's own quoted conclusion, "se
evidenció que ocho de las nueve rotondas construidas **no cumplen** con los diámetros mínimos
recomendados por normativa internacional" — but it sits in El Observador and Semanario Universidad,
which the card did not cite. The card now gives Delfino's and CRHoy's wording for the finding, adds
the eight-of-nine conclusion with the report number, and cites the two sources that carry it.

**Selective quotation.** The check log's own claim is "Everything that cuts the other way is on the
card." Tested, and it fails in three places, all in the same direction.
1. The log says the favourable sentence in the Delfino article "is on the card": MOPT "ha defendido
   en varias ocasiones que las obras se construyeron como soluciones temporales debido a atrasos en
   las expropiaciones". **It is not on the card** — neither is the rest of that sentence, "y que
   planea sustituirlas por pasos a desnivel a partir de 2026". Added.
2. Teletica's report of 6 November 2025 ends: "Tan solo 12 días antes, la Presidencia de la
   República y el Conavi anunciaron licitaciones para construir pasos a desnivel ... como
   soluciones definitivas para algunas intersecciones donde ahora hay rotondas." The card took the
   hauliers' blame from that article and left this out. Added.
3. CRHoy of 6 November 2025 is the card's source for the president's dismissal of the protesters.
   The same article records him on 31 August 2025 calling the roundabouts "un problema serio" and
   saying they had always been put as "una solución temporal". The card quoted the dismissal and
   dropped the admission. Added.

**A figure with no date in its own sentence or cell.** The checker's own fix of the UN office
cut-off ("31 de marzo", with no year in the sentence) is confirmed against the article and kept. No
further instance found: every figure kept carries a date in its sentence or the date of the report
that carries it. One figure was missing and is added — La Nación of 9 May 2025 gives the project's
initial cost as $534 million, against the finance minister's $485.6 million and the contract's
$465,593,387.06. Printed in `whole` with its owner, unreconciled.

**Whose sentence each number is in.** Audited every number on the card against the page. Confirmed
exactly: 637 / 182 / 28.57% / 164 / 606 / 54% / $25 million / 71.65% against 89.33% / the State's
broken four-month promise / "No estamos en capacidad como país para asumir más costos" (all CRHoy,
24 October 2022); 1,400 properties, about 700 right-of-way occupations, $465 million of which $396
million by Eximbank loan and $69 million national counterpart (La República, 20 November 2017);
"limitar el proyecto al derecho de vía ... alrededor de 700 expropiaciones" (La República, 27
November 2019); 581 required and 238 in the State's name, almost $90 million counterpart, 84.3%
physical progress, $485.6m to $552.5m, September 2020 to December 2024, February 2015 for Law 9293,
and the works started without the expropriations ready (Semanario Universidad, 2 November 2023);
at least 73 dropped, 496 / 362 / 134, March's 569 / 345 / 245, and the money deposited with the
Attorney General's office being returned (La Nación, 8 August 2024); 515 / 408 / 89 / 107 / 67 /
475 / 92% / 19 and the 104 km main trunk functional in October (La Nación, 9 May 2025); loan
number, rates, maturities, grace periods, fees, the $396 million total, 91.85% at December 2024 and
the 28 May 2025 target, the single-$395-million characterisation by the China-Latin America Finance
Database (AidData 37364 and 39847).

**One single-source figure needed a second reading, from the same document — corrected.** The card
had the Comptroller putting "the number of expropriation files CONAVI ordered dropped at 74".
Teletica alone gives 74. Delfino's account of the same order gives **13** files, named to the
Sinaí, La Unión and Matina overpasses and the Siquirres and Moín interchanges, asked for without
technical grounds the day before addendum 7 was authorised. CRHoy, El Observador and Semanario
Universidad give no number at all. Both counts are now on the card with their owners and what each
is attached to. Nothing is reconciled.

**The deadline the Comptroller set, three ways.** Teletica's 30 days is now printed beside
Semanario Universidad's 30 October 2026 and 30 March 2027 and Delfino's 30 July 2027, each
attributed. The card had only Teletica's.

**One detail of the survivor's account corrected.** The card said the men were at breakfast "with
their backs to the road". La Teja says "estaban de espaldas **al tráiler**" and "estaban a la
orilla del camión de nosotros, estaban paraditos en la pura puerta". Corrected to the trailer and
their own truck.

**`kind`.** Absent, and correctly so: the batch file's hard rules say "Do NOT set `kind`: all 93
existing `lk:cn` cases carry none, and round 37 found `kind:'off'` would file Chinese credit with
the World Bank's." Verified absent in the output.

**`displaced`.** Absent, not 0, per the same rules ("Never write `displaced: 0`"), with the
reasoning in `displaced_note`. Verified absent.

**Coordinates and `ap`.** 9.9919, -83.0248 is AidData's own point for the Limón end of the route,
and I confirmed it in record 37364's location narrative — the OpenStreetMap directions link runs
`9.9919,-83.0248` to `10.2110,-83.8975`. `ap: true` is right because the point stands for the
corridor end and not for the roundabout, and `point` says so. The card's absence claim — "no source
gives a coordinate for that roundabout" — was tested against all sixteen sources the card had and
the six added, and holds.

**No researcher's voice.** Grepped the whole card for first person, "this card", "this entry", "the
writer", "searches returned" and "no document read". Nothing.

**Every URL resolves and its title matches the page.** All 22 checked: 200 on every one, including
the six added. Two titles verified against the page's own `<title>` and heading because the check
log had corrected them: La Nación's "MOPT desiste de expropiar 73 terrenos en ruta 32 al optar por
cuestionadas rotondas" and the Semanario Universidad canonical slug. Both right as now cited.

**Companies array.** CHEC and CONAVI, both put on this project by AidData's record and by the
Comptroller's order; no oversight or civil-society body sitting beside them. CONAVI's role
description was checked against the state's structure — a body under the public works ministry,
with expropriation files passing to the ministry's DABI, which CRHoy's 2022 article confirms.
Correct.

---

## 5. The expropriation material the checker cut — **the cut is upheld, and I looked for the loss
on top of the agreement**

The deciding sentence is exact in the source, read whole: "solo 182 (el 28,57%) de los terrenos está
en poder del Estado y otros 164 poseen entrada en posesión voluntaria **tras acuerdos con los
dueños** por mientras se formaliza el pago" (CRHoy, 24 October 2022, from CONAVI's executive works
report 48). No deadline stated, no sum owed, no owner named, and the unit is plots. The 67
unperfected voluntary entries at the 31 March cut-off have the same shape (La Nación, 9 May 2025).
Against the map's standing edges — Bukoba's compensation unpaid in five identified cases at a named
site, Hopewell's payment "Awaiting payment" past a stated expected date with no amount six months
later — neither shape is present.

I then looked specifically for the loss the ruling might be hiding, in six sources and in two
accounts of the Comptroller's order, and it is not there:

- **Unpaid sums.** None named anywhere. What one document records is the opposite movement: "los
  fondos para pagar a los dueños ya habían sido depositados en la cuenta de la Procuraduría General
  de la República, por lo que también deben regresar a manos del MOPT y suspender los procesos de
  escritura pública" (La Nación, 8 August 2024). That is the State unwinding a payment it had
  already made, not a payment withheld. It leaves an owner whose file was dropped with the process
  cancelled, but no source says any such owner was left out of pocket or with damaged land; the
  works to be demolished at those crossings are the project's own walls, not owners' property.
- **A deadline passed.** The only deadline in the expropriation material runs the other way — the
  State's own broken promise to complete the procedures in four months, which is the ministry
  failing the contractor, and which CHEC turned into a $25 million claim.
- **An owner who did not agree.** No source names one. La República of 20 November 2017 prints a
  general account of what happens in Costa Rican practice when an owner rejects the State's offer,
  which the checker rightly removed from the card as a statement about practice rather than about
  any Route 32 owner; I confirmed the sentence is unattributed narration in that article.
- **A loss recorded elsewhere.** The Comptroller General did find a loss, and it is to the State:
  $1,408,617.46 of extra payments for roundabout redesign, "**daño patrimonial directo a la
  Hacienda Pública** derivado de la defectuosa planificación y mala práctica técnica". Damage to
  the treasury is not harm to identifiable people. And the remedy the Comptroller ordered —
  inventory every file with its number, area, state of process and "dinero erogado" — implies no
  such per-owner record was before it.

So the expropriation material stays where the checker put it, as context in `community`, expressly
not as harm. The forward rule is met on limb (b) by the two deaths alone.

---

## End-of-log items

**1. What could not be checked.** The Constitutional Chamber's judgment 2025-29197, Lanamme's report
EIC-Lanamme-INF-0287-2025 and the Comptroller General's oficio DFOE-CIU-0430 were not opened; the
routes that failed are named in §3. Each finding on the card is attributed to the outlet that
reported it, and `confidence_note` now says the three documents reach the card that way. CONAVI's
executive works report 48 and the UN Office for Project Services reports likewise reach the card
only through CRHoy and La Nación, which the card states. The Judicial Investigation Organisation's
investigation into the crash has no published outcome: searched, and nothing after 7 November 2025
names either dead man.

**2. Figures where documents disagree, left unreconciled, all on the card.**
- Hurt at Limón 2000 on 6 November 2025: four patients with two taken urgently to hospital (Red
  Cross, via Teletica 6.54 a.m. and El Observador 9.28 a.m.) / four seriously injured (Teletica,
  2.30 p.m.) / six injured (CRHoy, 11.58 a.m.).
- Time of the crash: about 6.00 a.m. (CRHoy) / 6.05 a.m. (CRHoy) / reported at 6.40 a.m. (Red
  Cross, via El Observador).
- Employer of the dead men: CHEC (La Teja, for the dead; Teletica, for an injured man in the same
  group) / an unnamed company contracted to the ministry (El Observador).
- Lanamme on the diameters: none exceeds the established minimum (Delfino; CRHoy) / eight of the
  nine do not meet the minimum recommended diameters (El Observador; Semanario Universidad,
  quoting the report).
- When and how the roundabouts replaced the grade separations: a government decision in 2023,
  formalised that October (CRHoy) / addendum 7 of June 2024 and addendum 8 of June 2025
  (Comptroller General, via Delfino).
- How many works were substituted: nine permanent works for seven roundabouts and two at-grade
  accesses, plus two more roundabouts (Comptroller General, via Delfino) / twelve overpasses for
  ten roundabouts and two at-grade crossings (La Nación, August 2024) / nine roundabouts built
  (Lanamme).
- Expropriation files dropped: at least 73 (UN office report via La Nación, August 2024) / 74
  (Comptroller via Teletica) / 13 (Comptroller via Delfino).
- The Comptroller's deadline: 30 days (Teletica) / 30 October 2026 and 30 March 2027 (Semanario
  Universidad) / 30 July 2027 for the land report (Delfino).
- The project's initial cost: $465,593,387.06 contract (loan agreement; AidData) / $485.6 million
  (finance minister, November 2023) / $534 million (La Nación, 9 May 2025).
- Law 9293's approval: 10 March 2015 (AidData) / February 2015 (Semanario Universidad).
- The contract number: CONAVI-CHEC-00 (AidData) / CONAVI-CHEC-001 (Comptroller, via Delfino).
- Within one article: the March count of 569 required with 345 completed and 245 in process, which
  does not add up (La Nación, 8 August 2024). Printed as given.
- Not used on the card: "$465 millones son financiados por el Exim Bank" (CRHoy, 2022) against the
  two loans' $396 million; the card takes the loan figures from the agreement text and AidData, so
  CRHoy's conflation of the contract value with the financing is recorded here and not printed.

**3. Faults appearing more than once.** One habit, in one direction: a sentence from a source read
far enough to supply the damaging half and not the rest. It produced the Lanamme wording that is
stronger than the two cited articles say, the MOPT defence the log believed it had put on the card,
Teletica's tender announcement twelve days before the deaths, and the president's "problema serio"
admission in the article the card quotes for his dismissal of the protesters. Three of the four
omissions favour the card's case, which is the direction CHECK20 says this fault always runs. The
second recurrence is thinner but real: a figure or a name taken from the nearest outlet without
asking whether a second account of the same document reads differently — Teletica's 74 against
Delfino's 13, and Teletica's 30 days against two dated deadlines.

**4. Wrong in the card data outside the fields asked about.** Three things, all now corrected or
recorded. `conditions` gave the 85% without the agreement's other half, that the Government was to
raise the remaining 15% itself, and without the blended rate of about 3.5% and the disbursement
order, all of which are in the primary text. `outcome` carried the Comptroller's 30-day order as
the only reading. `whole` said the roundabouts replaced the grade separations "from 2023", which is
CRHoy's date for the political decision and not the contract's: the addenda are June 2024 and June
2025. `start: 2017` is kept — AidData gives 20 November 2017 as the actual start of the financed
works, with the commitment at 3 June 2013, and `lenders[0].role` carries both.

**5. Routes that failed, named as routes.** All 22 source URLs returned 200 over `curl` with a
browser user agent, including the six added here: china.aiddata.org, larepublica.net, crhoy.com,
nacion.com, lateja.cr, teletica.com, observador.cr, delfino.cr, semanariouniversidad.com,
docs.aiddata.org. One note worth keeping: `crhoy.com` without the `/nacionales/` path segment
returns 308 and needs `-L`; the writer's bare URL is not dead. The routes that did fail are the
five CGR routes, the three guessed `nexuspj` API paths and the Lanamme `simple-search` route, all
named in §3; `www.cgr.go.cr/`, `nexuspj.poder-judicial.go.cr/` and `lanamme.ucr.ac.cr` all answer,
so none of them is a refusing host.

**6. For round 39.** Two leads, neither used here. The Delfino item of 12 November 2025 on the
Constitutional Chamber giving CONAVI three days to account for wildlife crossings on Route 32 is
still only a headline on this card's record, and `ecosystem` is still empty; the Comptroller's
earlier report of 30 May 2022 on deficiencies in the project's conceptualisation and its
complementary works, mentioned in CRHoy of 24 October 2022, has not been read by anyone on this
card. And the standing-rule problem that produced this review is worth recording as settled once:
a checker-authored card was reviewable on its own evidence, and the review changed eleven things in
it without changing its verdict.
