# Round 38, batch A — writer's report

18 financings in. **3 cases, 0 extends, 15 drops.** No row was already on the map as the same
harm; the three live SGR/Kenya cases were checked and none carried what is written here.

Cache: no PDF cache was needed. Documents fetched to /tmp (hr.pdf Doga Dernegi Hunutlu report,
eh.pdf HEAL press release, oi.pdf Oakland Institute Lower Omo report, ti.pdf Transparency
International Rwanda expropriation assessment) are working files, not sources any card rests on
except where cited. 8 WebSearch calls used; everything else was `curl`.

## Cases written (3)

**sukulu-phosphate-osukuru-land** — Uganda, G327, AidData 60236, ICBC US$240m (4 Dec 2015).
Deciding sentences: "To my surprise, they have taken our money, our land and no land title has
been given to any of us" (Vincent Matano, Oil in Uganda, 8 July 2016, via CorpWatch and the
Business and Human Rights Resource Centre) and "only 123 out of 4,800 families have received any
compensation payment" (Matooke Republic, 16 December 2016). Land taken, 99-year leases signed
under pressure, titles never issued, payment to 123 of 4,800 families. `displaced` omitted.
The batch's own flagged sentence for this row (two finance officials jailed for taking a bribe)
is not the harm on the card.

**sgr-phase-1-miritini-allottees** — Kenya, G071, AidData 37103 and 31777, China Eximbank
US$1.9bn + US$1.6bn (11 May 2014). Deciding sentence, from the Court of Appeal's own account of
the case: the commission acquired 22.11 ha of plot MN/VI/4805 for the Mombasa-Nairobi railway and
paid Kshs 1,475,486,845 to the registered company, and the High Court found it had abused its
powers in refusing to pay four allottees — "the petitioners left without land" (Justice Eric
Ogola, reported in the Daily Nation, 2 December 2019).

**kibwezi-kitui-road-compensation** — Kenya, G220, AidData 53111 and 58152, China Eximbank
buyer's credit (29 Nov 2016). Deciding sentences: "About 5,000 land owners are crying foul over
the failure to compensate them" and shops "brought down without anyone talking of compensation"
(The Star, 6 December 2020); "yet to be fully compensated five years after the project commenced"
(The Star, 4 March 2022). The `relief_or_disaster_language` flag on this row fired on the words
"COVID-19 cases reported in Kitui" inside a list of construction delays; the money did not
respond to a disaster.

## Drops (15), each with the sentence or absence that decided it

1. **G388 Angola, Camacupa agro-industrial farm (CDB US$88.638m, 2012)** — the only limb-(b)
   sentence is AidData's own: "the project encountered several problems and delays related to to
   land expropriation during construction." It names no person, gives no count, and reports a
   delay to construction rather than a loss to anyone. A Portuguese-language search for
   Camacupa expropriation complaints returned nothing about this farm.
2. **G507 Angola, 3000 Sambizanga social housing units (CDB US$37m, 2016)** — the flagged
   sentence is "construction of 3,000 social housing units for families whose land was
   expropriated under a presidential order." The money paid for the replacement housing, so it
   followed the taking rather than causing it. VerAngola (13 December 2016) records the
   president saying about 9,400 houses were needed for the Sambizanga requalification and that
   only half the needed houses had construction contracts — a shortfall in the rehousing, with
   no count of families moved by this loan and no compensation finding against it.
3. **G310 DR Congo, Goma stadium (China Eximbank US$9.99m, 2015)** — "to cover the
   expropriations envisaged for the extension of the stadium." Envisaged; no count, no outcome.
4. **G290 Egypt, Benban solar plants (ICBC US$70m, 2017)** — the "land taken" flag fired on a
   MIGA political-risk insurance clause: guarantees "against the risks of Transfer and
   Convertibility Restrictions, Breach of Contract, Expropriation and War and Civil Disturbance."
   That is cover against expropriation of the investor, not land taken from anyone. The record
   also describes the site as "all desert land, largely unused and unpopulated", nearest village
   12 km away.
5. **G207 Nigeria, CNG Glass float glass plant (CDB US$26m, 2018)** — the same MIGA insurance
   clause, in the same shape: "against the risks of Expropriation, Transfer Restriction, and War
   and Civil Disturbance." No land taken from anyone is recorded; the plant sits inside the Ogun
   Guangdong Free Trade Zone on land already prepared and fenced.
6. **G308 Ethiopia, ZTE telecoms seller's credit (CDB US$1.5bn, 2007)** — the arrests are of a
   former ETC chief executive, 26 former executives and a manager recorded soliciting a bribe.
   A corruption prosecution of officials is not harm to identifiable people under limb (b).
7. **G295 Ethiopia, Omo Kuraz 5 sugar plant (ICBC US$550m, 2015)** — the arrest is of the
   contractor's own project head, Yuan Jialin, for allegedly paying a bribe. Not community harm.
   The documented Lower Omo displacement (Oakland Institute, 2023) is attributed to the Kuraz
   sugar programme and the Gibe III dam as a whole, not to the plant this credit financed, and
   AidData's record places the plant in two different places — Jawi District in Amhara in its
   location narrative and a Lower Omo coordinate in its map link — so the footprint cannot be
   fixed. Dropped rather than forced.
8. **G289 Guinea-Bissau, rice donation (US$3m, 2018)** — "It is unknown whether the police
   department was able to arrest the minister." An arrest that may not have happened, of a
   minister, is not harm to identifiable people.
9. **G216 Kenya, Kisumu-Malaba SGR section (China Eximbank US$3.7bn pledge, 2016)** — "His
   request was rejected." No money, so test 1 fails. Its arrest sentences are the Phase 1 text
   repeated.
10. **G422 Lebanon, Palestinian camp grants (US$680,000 and US$500,000, 2009)** — the grant was
    *for* land expropriation at Nahr el-Bared, and "The land expropriation will be implemented
    through the Lebanese Council for Development and Reconstruction." Prospective, no count, and
    the money is post-war camp reconstruction.
11. **G224 Rwanda, Huye-Kibeho-Munini road (China Eximbank RMB 550m, 2018)** — all three
    limb-(b) sentences are projections from the loan agreement's annex: "1,647 properties will
    be expropriated", "407 properties will be expropriated", "The total estimated cost for
    project expropriation is equivalent to FRW 3,441,108,941." No outcome document was found for
    this road. The dedupe hint to `rwanda-hillside-irrigation-relocation-deaths` is false: it
    matches on "province", "rwanda" and "southern" only.
12. **G271 Rwanda, Bugesera airport road (China Eximbank RMB 340m, 2018)** — AidData's own
    sentence is praise for compensation having been paid. Rwanda Today (21 March 2019) says
    people expropriated for the Sonatubes-Gahanga-Akagera road three years earlier were still
    waiting for compensation, but every person it names lives in Gatsibo district on a different
    project, the Nyagatare-Rukomo road, and it gives no count for this road. The project's own
    figures are prospective: "over 320 properties will be affected" and Rwf4.5 billion earmarked
    (The New Times, via House in Rwanda). Nearest miss of the batch.
13. **G441 Turkey, Emba Hunutlu coal plant (CDB, ICBC and Bank of China, US$460m each, 2019)** —
    "In 2015, the land was expropriated, with the price being set at 100 lira per square meter."
    A price, with no count of owners, no record of payment withheld and no named person. The
    documented objections are to health effects and to the loggerhead and green turtle nesting
    beach at Sugözü (HEAL, TEMA, WWF-Türkiye press release, 25 April 2019), and the 2012
    permitting meeting met protests — a protest that was held. A Turkish-language search for a
    worker death on the site returned nothing. The second insurance-clause flag is Sinosure
    cover against expropriation, as in Egypt and Nigeria.
14. **G442 Turkey, Efeler geothermal expansion (ICBC Turkey US$30m, 2019)** — screened out on
    its own sentence, the BRIEF22 shape: "land acquisition for the project was completed on a
    willing-buyer/willing-seller basis, and no direct/indirect physical displacement or
    disruptions in livelihood occurred", with compensation assessed as satisfactory. The second
    sentence is a monitoring commitment for a transmission line.
15. **G217 Zambia, Lusaka-Ndola dual carriageway (China Eximbank and Jiangxi Bank, 2018)** — the
    "arrest" is a former minister saying the contractor "should be summoned ... and to show
    cause why he should not be arrested". Nobody was arrested and no harm to anyone is recorded.
    On land: the contractor had "identified project-affected persons (PAPS) and property and
    services that may require to be relocated", and work then stopped in June 2021 before
    construction began in earnest.

## My own two weakest entries

**1. kibwezi-kitui-road-compensation.** The figure of about 5,000 comes from one newspaper, The
Star, and that newspaper describes it three different ways in three years — land owners, persons
who lost land or homes or business premises, and title owners who were relocated. It is kept out
of `displaced` for that reason, but it is also the only scale the card has. The downward revision
of awards rests on a single Senate speech whose sitting date the record carried here does not
give, so no date is stated for it. The parliamentary question is a question, not a finding: its
own record shows no answer. If a checker wants one thing verified first, it is whether any
National Land Commission or Auditor-General document counts the parcels and the payments on this
road.

**2. sgr-phase-1-miritini-allottees.** The harm is four people, and the court record behind it is
only partly public: judy.legal publishes the opening of the Court of Appeal ruling and then asks
for a subscription, so the result of that appeal application is unknown and the High Court
judgment itself was never opened. The two sources disagree on two of the four names and on the
money paid to the registered owner. There is also a filing question for the lead to settle: this
is the third SGR card on the map, and the first two (`kenya-sgr-cargo-directive`, Mombasa, and
`sgr-phase-2a-kajiado-blasting-nairobi-park`) sit on the same lender and, in the first case, the
same city — written as a separate case because the harm, the parcels and the phase are different,
but it is one point about 10 km from an existing card.

## Figures where two documents disagree

- Sukulu: "OVER 4,600 families" and "4,800 families" in the same Matooke Republic article of
  16 December 2016; no explanation given, both printed on the card.
- Miritini: Kshs 1,475,486,845 paid to Miritini Free Port (Court of Appeal record) against
  "Sh1.4 billion and another Sh360,000" (Daily Nation, 2 December 2019). Both printed.
- Miritini petitioners: Theresia Runji / Marieta Gitonga Chege / Sammy M. Kara (court record)
  against Theresa Runji / Marieta Gitonga / Sammy Macharia (Daily Nation). Both printed.
- Kibwezi: "Kibwezi East MP" (The Star, 21 March 2023) against "the Member for Kibwezi West"
  (Parliament's own record of the question). Both printed.
- Omo Kuraz 5 loan face value: US$550 million in official sources, US$700 million in a 2017
  SAIS-CARI report (AidData's note). Row dropped, so not carried.

## Routes that failed, named as routes

- `https://www.gem.wiki/EMBA_Hunutlu_power_station` over `curl` with a browser user agent:
  **HTTP 403 with a Cloudflare "Just a moment..." interstitial**. The mirror
  `https://cavac.at/cavacopedia/Emba Hunutlu power station` answers **HTTP 410** with its own
  notice about scrapers. Neither is a host block on the project's facts; both pages were worked
  around with the HEAL press-release PDF and Turkish press.
- `https://www.monitor.co.ug/uganda/special-reports/tororo-locals-cry-out-for-jobs-better-pay-at-phosphate-plant-1774152`
  over `curl` with a browser user agent: **HTTP 403, Cloudflare "Sorry, you have been blocked"**.
  Monitor's Tororo reporting was not used; the same ground is covered by Matooke Republic and
  CorpWatch.
- `https://new.kenyalaw.org/search/?q=Runji+National+Land+Commission` returns **HTTP 200 with a
  JavaScript-rendered result list and no results in the HTML**, and the page carries a notice
  prohibiting automated scraping. The judgment was therefore taken from judy.legal's published
  text and from the Daily Nation's report, and the High Court judgment number is not stated.
- `https://dogadernegi.org/.../hunutlu-raporu.pdf` downloaded (HTTP 200, 3.0 MB) but
  `pdftotext -layout` yields 83 lines, so the report is scanned images; nothing was taken from it.
- `https://info.mzalendo.com/api/v0.1/hansard/entries/929115/` serves the speech text but exposes
  no sitting date, and `hansard/sitting/` is **HTTP 404**. Hence the undated attribution.

## What the next round should know

1. **Three of this batch's eighteen "land taken" flags were political-risk insurance clauses**
   (Egypt Benban/MIGA, Nigeria CNG Glass/MIGA, Turkey Hunutlu/Sinosure). The trigger word is
   "Expropriation" capitalised inside a list of covered risks. A cheap pre-screen on
   "against the risks of" would have removed all three before a writer opened them.
2. **Two were corruption prosecutions of officials or of the contractor's own staff** (Ethiopia
   ZTE, Ethiopia Omo Kuraz 5, plus Uganda Sukulu's flagged sentence and Kenya SGR's). The
   "arrest or detention" bucket in this remainder is mostly anti-corruption arrests, not force
   used on people who objected. Of the seven financings carrying that bucket, none held an arrest
   of an objector. Worth a sub-flag separating "arrest of an official" from "arrest of a resident".
3. **The yield came from outside the flagged sentence every time.** All three cases rest on press
   or court records found by searching the project name plus "compensation", not on the candidate
   sentence. The flags pointed at the right financings in two of three cases (Kibwezi, Sukulu)
   and at the wrong harm in all three.
4. Round 37's `prospective_verb_only` screen was right on both Rwanda rows: the only figures that
   exist for the Huye-Kibeho-Munini and Bugesera airport roads are pre-works valuations. If a
   later round revisits Rwanda, the thing to look for is a Rwanda Transport Development Agency or
   Auditor-General outcome report, not press.
