# Round 38, batch C — report

17 financings. **2 cases, 2 already_on_map, 13 drops.** 11 WebSearch calls used.

Document cache: `/tmp/aid38c/` — AidData project pages for records 66093, 94030, 37364, 52888,
67648, 73925, 85322 (fetched by `curl`, served in full), the IDB Invest Environmental and Social
Review Summary for LD Celulose as `ldc_esrs.pdf` and `ldc_esrs.txt`, and the news pages listed
below as HTML.

Route note: AidData project pages serve over plain `curl`, but the **source URLs are not in the
page** — only the source *titles*, inside the React Router stream blob. Pulling the titles out and
searching for them by title is what found the Bosnian articles. Worth recording for round 39.

---

## Cases (2)

### 1. `bih-chinese-flood-machinery-sold` — Bosnia and Herzegovina (G428, record 66093)
Deciding sentences, from Radio Free Europe, 3 April 2019: police **seized 28 tractors and farm
machines** that had been sold and handed to third parties; the prosecutor put the group's unlawful
gain at **more than one million convertible marks**; and, separately, the prosecution says Mladina
**deceived more than 50 people** from 2015 on, taking 2,000–5,000 marks (once 20,000) from each to
"arrange" a tractor while presenting himself as a government commissioner or a consultant to the
Chinese embassy. The Chinese embassy in Sarajevo confirmed the donated equipment "was not handed to
the residents hit by the floods". Second source: index.hr, 2 April 2019 — eight detained in
operation "Farmer", equipment worth about 500,000 euros.

This is an **EMERGENCY RESPONSE sector row and the screen note about it was right to warn**: the
money did respond to the May 2014 floods. It is kept because the harm on the card is not the
flood's — it is the diversion of the machinery and the more-than-50 people charged for a tractor
they were entitled to. A reviewer who disagrees with that reading should drop it, and the drop
reason would be BRIEF36's relief rule.

Figures that disagree, both inside the same RFE article: its opening says China gave the tractors
**in 2012**; the prosecutor quoted lower down says China donated **in 2014**, which is the year
AidData gives for the grant agreement. Both are on the card's `confidence_note`. Also two amounts
for two different things: AidData's grant agreement at about 1 million marks / half a million euros,
and RFE's "more than six million marks" for the whole Chinese farm-equipment donation to Bosnia and
Herzegovina, a third of which the Council of Ministers directed to the Federation after the floods.

### 2. `costa-rica-route-32-possession-before-payment` — Costa Rica (G124, records 37364 + 39847)
Deciding sentence, CRHoy, 24 October 2022, quoting **CONAVI's own executive works report 48**
(cut-off September 2022): of 637 expropriations required, 182 plots were in the State's hands and
**another 164 had been entered into possession voluntarily under agreements with their owners while
the payment was being formalised**. Repeated at a second date by a **UN Office for Project Services**
report cut off at 31 March 2025, via La Nación, 9 May 2025: 107 files still in process, **67 of them
with voluntary entries into possession not made effective**, and 19 of the 475 available plots
awaiting demolition. Corroborated from the top: finance minister Nogui Acosta told the Legislative
Assembly's Limón commission on 2 November 2023 that **the works were started without the
expropriations ready** (Semanario Universidad).

Three counts of the expropriations needed do not line up and no document explains the gap: about
**1,400** properties before the works started (La República, 20 November 2017), **637** required
(CONAVI report 48, September 2022), **515** files handled (UNOPS, 31 March 2025). All three are on
the card.

Counts here are of **plots, not people**, so no `displaced` field; the reasoning is in
`displaced_note`.

---

## Already on the map (2)

- **G142 Ecuador, Coca Codo Sinclair (record 38935)** — `already_on_map: coca-codo-sinclair`. The
  live card already carries `killed: 13` with the December 2014 tunnel collapse and 12 injured, and
  already cites AidData record 38935 and the US$1.68 billion China Eximbank buyer's credit of
  3 June 2010 at 6.9%. The row adds no lender and no amount the card lacks. Nothing written.
- **G101 Honduras, Patuca III (record 35552)** — `already_on_map: patuca-iii-dam-landowners`. The
  card already names ICBC with the US$297.7 million buyer's credit of 22 September 2013, the
  sovereign guarantee, the phase-2 cost split, and AidData record 35552, and it already records that
  **phase 1 is where the land acquisition sat and that ICBC did not finance phase 1**. The row's
  land-taken sentence is that same phase-1 sentence. No extend: nothing to add.

---

## Drops (13), each with the sentence or the absence that decided it

| # | Financing | Why |
|---|---|---|
| 1 | **G203 Philippines** (49601) | The arrest is Leila de Lima's 2017 detention. No document ties it to a 14-million-peso donation of law-enforcement equipment she signed letters for. The harm, if any, is not the money's. Status is also "Pipeline: Pledge". |
| 2 | **G584 Uzbekistan** (91901, 91917) | The only limb-(b) sentence is "Zeromax's chief executive, Miridal Djalalov, was **allegedly** detained for 'questioning.' He was later released." A company executive, allegedly, released — not harm to people on the pipeline route. One search in Russian for land taken or compensation along the Uzbek sections of Lines A and B returned nothing on this project. |
| 3 | **G594 Argentina** (92332) | The "land taken" sentence is a collateral clause: collection rights assigned "in the event of termination, **expropriation** or rescue of the Concession Contract". A contract term, not an event. |
| 4 | **G215 Belarus** (52888, 97749) | `every_limb_b_sentence_carries_a_screen_flag: true`, and the screen was right. The arrest is the **dissident journalist taken off the plane forced down in Minsk on 23 May 2021** — nothing to do with the Nezhinsky potash mine. Two Russian-language searches for land taken, houses demolished or a worker killed at the Slavkaliy site returned nothing. **Belarus has 0 cases on the map and this round does not change that.** |
| 5 | **G628 Brazil** (95937) | Loan **cancelled**, so no money moved; the arrest is Wesley and Joesley Batista jailed September 2017 to February/March 2018 in the JBS corruption case, which is not harm to identifiable people from a project. |
| 6 | **G509 Brazil, LD Celulose** (73925) | Decisive sentence, opened at source — IDB Invest Environmental and Social Review Summary, §4.5.b: land acquisition for the transmission line, water system and access road "impacted directly less than 50 landowners (28 along the transmission line, 12 along the water system, and 4 along the access road); ii) **there is no physical displacement, nor permanent or significant impact on livelihoods**; and iii) the percentage of land affectation is less than 10% of each property." §4.5.a adds "land acquisition will be conducted by willing-buyer willing-seller and **there is no right of expropriation granted by the government**." The flagged "PS5 Land Acquisition and Involuntary Resettlement" was a list of performance standards. |
| 7 | **G110 Colombia** (36063) | The sentence is an absence: "There were no further records as to whether this land acquisition ever happened, or how the remainder of the funds were to be used." |
| 8 | **G521 Costa Rica, PIT / Barranca-Limonal** (85322) | "Only 8% of necessary land expropriations had been made" is a **delay statistic, not a taking**. The MOPT internal audit report DAG-2021-0170, via CRHoy and La Nación: at 5 January 2021, 33 of 394 plots registered to the State, 11 processes annulled, 350 in process. La Nación, 18 November 2025: the contractor abandoned the works in November 2022 and won **$13 million from the State**, and the state re-let the job. Money and loss flow to the contractor, not from the project to any identifiable person. No harm document. |
| 9 | **G447 Serbia** (67648) | "There is, however, evidence that some preliminary (pre-construction) activities have taken place, such as land expropriation." No count, no owner, no loss. A Serbian-language search for expropriation, plots or compensation on the Obrenovac–Novi Beograd heating pipeline found only signing and financing coverage. |
| 10 | **G450 Ukraine, loan-for-grain** (67803) | The arrest is Ihor Yakubovych, former chairman of the State Food and Grain Corporation, detained in August 2021 after trying to leave the country, in an embezzlement case. An official prosecuted for stealing the loan is not harm to identifiable people under test 2. |
| 11 | **G188 Ukraine, Aerial Express** (42494, 42577, 67775) | The arrest is Vladyslav Kaskiv, former head of the State Agency for Investment, **detained in Panama** in September 2016 — an official, abroad, in a corruption case. Second tranche never disbursed. |
| 12 | **G134 Venezuela, Sinovensa** (38053) | `every_limb_b_sentence_carries_a_screen_flag: true`. The arrests are Sinovensa's own president and three directors, taken by military counter-intelligence in October 2019 for embezzlement and bid-rigging. The April 2020 Morichal fire is in the record, with oil workers telling Reuters the bush was unmaintained, the plant's firefighters under-resourced and earlier spills never cleaned up — but no death, injury or loss to an identifiable person is recorded, so neither limb is met. |
| 13 | **G617 Venezuela, Abreu e Lima** (94030) | The sentence — "The project also involved the controversial expropriation of land and homes from local farmers" — carries **no count, no place inside the state, and no source that opened**. Two Spanish-language searches for expropriation of land or homes at the El Tigre–Pariaguán soy complex returned nothing on it; the two El Vistazo articles behind AidData's record that did open (25 July 2015, 6 September 2016) are about output and about INTI land-title arrears in Anzoátegui generally, not about anyone losing land to this project. AidData's prose is not a document, so the figure comes off and the row is dropped. |

---

## My own two weakest entries

**1. `bih-chinese-flood-machinery-sold` — weakest overall.** Two faults. First, the money is
relief: BRIEF36 says relief money fails tests 1 and 3, and the only reason this is not that is a
reading that the harm is the diversion rather than the flood. That reading is mine and a checker
may reject it. Second, **the sale, the one-million-mark gain and the more than 50 people defrauded
are all the prosecution's case as reported in April 2019**, not a court finding; no verdict was
reported in anything that opened, and searches for the case outcome in Bosnian returned nothing
relevant. What is hard is only: eight detained, a former minister arrested on 2 April 2019, four
held one month, 28 machines seized, and the Chinese embassy's statement that the equipment did not
reach flood-hit residents. Confidence is set to `contested` for exactly this.

**2. `costa-rica-route-32-possession-before-payment`.** The harm is counted in **plots, not
people**, and no document names a single owner who was not paid or a sum owed. "Voluntary entry into
possession while the payment is being formalised" is land in use before payment, which is the limb-(b)
shape, but it is not the same as compensation refused, and the owners agreed to it. If a checker
holds that an agreed entry into possession is not a harm, the card falls to the finance minister's
sentence alone that works began without the expropriations ready — and that sentence is about
project delay, not about a person's loss.

---

## Routes that failed, named as routes

- **AidData project page → source URLs**: `curl https://china.aiddata.org/projects/<id>/` returns
  the whole record including the list of source **titles**, but **no source URLs anywhere in the
  HTML**. The titles sit inside the `window.__reactRouterContext` stream as an interned string
  array, so they have to be sliced out by hand. Not a host refusal; the data simply is not served.
- **WebSearch on Bosnian and Serbian query strings** returned mostly off-topic Serbian farmer-protest
  and Serbian-politics results; the Bosnian machinery case was found only by searching AidData's own
  source title. Three further searches for the case's verdict, and for harm at the Belarus potash
  mine and the Serbian heating pipeline, returned nothing on topic. Nothing was blocked.
- Every page actually quoted on a card opened over `curl` with a browser user agent:
  slobodnaevropa.org, index.hr, crhoy.com, nacion.com, semanariouniversidad.com, larepublica.net,
  diarioelvistazo.com, idbinvest.org (PDF), occrp.org. **No host refused.**

## For round 39

- **Europe and Central Asia and MENA stay thin, and this queue did not fix it.** Belarus, Uzbekistan
  and Serbia each had exactly one flagged sentence and in all three it was about an executive, a
  journalist or a contract clause. Bosnia produced the one case. If coverage of those regions is the
  goal, the AidData harm flags are not the route — a complaint-mechanism or court-record route would
  be.
- **`names_another_country` earned its keep exactly as predicted**: Belarus (journalist arrested off
  a plane, UK/US/Canada sanctions) and Ukraine (Kaskiv detained in Panama) were both killed by it.
- **`relief_or_disaster_language`**: Bosnia is the one row in this batch where the relief reading
  does *not* dispose of the case, and it needed the full text to see that. Round 31's
  one-real-case-in-nine finding held here.
- **Seven of thirteen drops are an official or an executive prosecuted for stealing the money.**
  That is a recognisable class in this dataset and it is never limb (b). A pre-screen that asks
  "was the arrested person a project official?" would have cleared G203, G584, G628, G450, G188,
  G134 and most of G428's flag without a search.
