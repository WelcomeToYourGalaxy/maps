# Round 21, batch B — non-China road and urban rows

Output: `/home/claude/r21/r26f_icij5_road_other.json` — 6 new cases, 1 extend, 4 drops.
Document cache: `/home/claude/r21/cache/`.

## 1. Row by row

| ICIJ project | P-number | `r21_outcome` | Reason |
|---|---|---|---|
| CORRIDOR X HIGHWAY PROJECT (Serbia, 9 Jul 2009) | **P108005** | **case** `corridor-x-dimitrovgrad-bypass-serbia` | 3 households physically displaced on the Dimitrovgrad bypass with no moving or transitional allowance paid; one household's car repair workshop expropriated with no compensation for the business or the lost income; over 100 households affected by blasting; 3 construction deaths. |
| Kiribati Road Rehabilitation Project (1 Mar 2011) | **P122151** | **dropped** | No relocation count and no recorded loss. Outcome is 8,256 m² of land strips and 131 trees belonging to 348 households, which the ICR calls "a minor portion of affected households' yards with no serious impacts on incomes or livelihoods"; 317 affected people compensated with 22 held in escrow; 111 complaints, all resolved on an independent NGO's review. BRIEF21 rule 2: land area plus an "affected" count. |
| Abidjan-Lagos Trade and Transport Facilitation (Ghana-filed, 23 Mar 2010) | **P096407** | **case** `agona-elubo-corridor-compensation-ghana` | At closing the involuntary resettlement policy was not complied with because approximately 11 per cent of affected people in Ghana were still unpaid. Weakest entry — see §2. |
| Kenya Transport Sector Support Project (21 Apr 2011) | **P124109** | **extend** to `webuye-interchange-traders` | Same P-number as the existing case. The 2021 ICR, not used by that case, adds the audit finding behind the Panel case, four OP 4.12 non-compliances, a worker killed by an excavator on the Kakamega–Webuye section, a dog bite, three further grievance cases and a 2022 Panel non-registration. |
| JO Amman Development Corridor (3 Jun 2004) | **P081505** | **case** `amman-development-corridor-land` | 3,028 people lost land, housing or other assets; about 300 owners and occupants had to find new homes; the borrower's own post-compensation interviews record widespread concern about slow payment, with waits well over a year; 500 ha taken from 240 plots and 778 people at Madounah for a customs depot and inland port that were never built. |
| Nigeria Lagos Urban Transport Project 2 (29 Jun 2010) | **P112956** | **case** `lagos-brt-ikorodu-market-traders` | 2,231 affected people; plantain traders moved off the Mile 12 terminal onto a three-year lease that expired and had to move again; Ikorodu roundabout traders moved to Agric and some moved back; 8 compensation payments uncollected at closing. LAMATA's own lesson in the ICR: the Ayangbunren Market traders "were displaced from one uncertain future to another equally uncertain future". |
| Rajasthan Road Sector Modernization (29 Oct 2013) | **P130164** | **dropped** | ICR: "There were no major resettlement issues. Most roads were built or upgraded in the right-of-way. Land acquisition was mainly handled through voluntary donations." No relocation count, no recorded loss. The one non-compliance is works finished on 26 roads before forest clearance — a legal and ecosystem matter, not a counted harm to people. |
| Strategic Roads Infrastructure Project (Indonesia, 6 Jul 2006) | **P079906** | **dropped** | ICR: "All land acquisitions which took place in SRIP's subprojects were carried out in a satisfactory manner… All cash compensation was paid at or above market price." Five subprojects needed tracer studies for land taken by local governments before the Bank came in; the ICR records no shortfall from them. No relocation count, no recorded loss. |
| East-West Highway Improvement 3 (Georgia, 10 Sep 2009) | **P112523** | **dropped** | Outcome is 2,393 people (617 households) "affected" and 736 land plots, 131.8 ha, acquired. The project's own 2009 RAP states "No physical relocation of households is required"; the only demolitions were three petrol stations. BRIEF21 rule 2 again. "Resettlement activities still not completed" at closing referred to two access roads, finished November 2016 and expected April 2017. |
| CEMAC – Transport-Transit Facilitation (26 Jun 2007) | **P079736** | **case** `baoro-bouar-road-house-damage-car` | 1,350 complaints on the Baoro–Bouar road in the Central African Republic; 518 validated for compensation, of which 429 for houses cracking from vibration; of the 89 due money, 51 paid FCFA 2,168,000 and 48 unpaid for FCFA 2,425,500; 61 never reviewed. Plus Cameroon labour-law non-compliance by the Army Corps of Engineers including non-payment of wages, and one project fatality. |
| Transport Project (Albania, 22 Feb 2007) | **P078949** | **case** `milot-rreshen-road-compensation-albania` | 23 households lost their homes and were relocated, 12 lost commercial structures, 338 lost land. The 2010 Law on Property Valuation "led to a reduction in the rate of compensation paid to Project-affected persons" for the second round of acquisitions, and its single-bank payment rule "significantly delayed payments of due compensations" for rural people without bank accounts. |

### Dedupe
`dedupe_leads.py` (1,026 cases → now reports 1,052) on all 13 numbers: P124109 → `webuye-interchange-traders`; P121185 → `nhiip-india-corridor-land-acquisition`; P126321 → `nutrip-road-compensation-arrears`. The other ten were new and were confirmed new by place and years.

### The three flagged collisions, settled
1. **Rajasthan P130164 vs NHIIP P121185** — both approved 29 October 2013; separate projects, no shared corridor. P121185 is national highways under the national road authority. P130164 is Rajasthan's own Public Works Department: about 2,500 km of **rural** roads (2,334 km built), PWD institutional reform, and road safety on demonstration corridors (the only RAP published is for the Deeg–Alwar–Behror SH-14 safe-demo corridor, in 2018). Dropped on its merits, not as a duplicate.
2. **Kenya P124109 / P126321 / `webuye-interchange-traders`** — P124109 **is** the project behind `webuye-interchange-traders`, so it is an extend, not a new pin. P126321 (National Urban Transport Improvement) is a different project on different roads (A104 James Gichuru–Rironi, Kisumu and Meru bypasses) and is already on the map as `nutrip-road-compensation-arrears`. Nothing in the 2021 P124109 ICR overlaps it.
3. **Georgia P112523 vs `east-west-highway-khevi`** — different works: P112523 is the Ruisi–Agara bypass on the E60, closed 2016; the existing case is the Rikoti Pass and Khevi, from 2020. Not a duplicate. P112523 dropped on its merits.

### Regional projects (warnings 1 and 4)
Both were found by dropping the country filter, as BRIEF20 says. P079736 is filed under country **"Central Africa"** and P096407 under **"Western Africa"**; neither is returned by a member-country query.
- **P079736**: the counted harm — 1,350 complaints, 429 for cracked houses, 48 claims unpaid — is all on the Baoro–Bouar road in the **Central African Republic**, so `iso3: CAF` with `iso3_more: [CMR, TCD]`. In Cameroon all complaints were about land lost to machinery and were closed; in Chad none was received. The labour-law harm and the one fatality are in Cameroon and are named as such on the card.
- **P096407**: the harm sits in **Ghana** (the 110 km Agona Junction–Elubo section), so `iso3: GHA` with `iso3_more: [BEN, TGO]`. Togo's RAP was called best practice; Benin drew "serious concerns" with both environmental and social measures, with no figures.

### Warning 5 (early approval)
P081505 was found at `&rows=100` with no offset needed once the `qterm` was narrowed to "Amman Development Corridor"; the plain country query buried it. `&os=20&rows=100` was not needed in the end.

## 2. The two weakest entries

**Weakest: `agona-elubo-corridor-compensation-ghana`.** It rests on **one** document. The Bank's completion report for P096407 is not disclosed — not under its own number, not under the second-phase number P116323, and not by a `qterm` title search — so the Independent Evaluation Group's review is the only route to its findings. Within that review:
- The only outcome finding is "approximately 11% of PAPs still needed to be paid" at closing, quoted from ICR paragraph 82. **No number of people is attached to it.**
- The affected-person counts (Ghana 744 households / 2,094 people; Benin 101/404; Togo 379/1,920) are **the appraisal's plan figures**, printed word for word at paragraph 97 and in the safeguards annex of the PAD of 25 February 2010, which costed the Ghana plan at about US$7.8 million in cash compensation. The review reprints them without saying so. This is BRIEF21's rule 2 at one further remove — the *review* reprinting the appraisal.
- The later figures (5,416 PAPs, GHC 24.8 million, 5,396 compensated, 20 remaining as of 28 August 2017) are **"The project team provided following additional information to IEG"** — BRIEF20 trap 4. They are on the card attributed to the project team, never to a document.
- The review states that compensation was completed within a month of closing and that full RAP implementation was achieved in August 2017.
If the checker wants a defensible floor here, the whole card reduces to: at closing, roughly one in nine affected people on a 110 km road had not been paid, and the Bank's own policy was in breach. That may not clear the bar.

**Second weakest: `lagos-brt-ikorodu-market-traders`.** Everything is from the Bank's ICR and the IEG review of it, and the sharpest sentence — the Ayangbunren traders "displaced from one uncertain future to another equally uncertain future" — is **LAMATA's own**, in the borrower annex, so the project is criticising itself rather than an outsider finding anything. The ICR says all 2,231 affected people "have been compensated appropriately as planned". It never says how many traders moved from any one market, how many moved back to Ikorodu station, or how many plantain traders were on the expired Ajelogo lease. Four searches of Lagos press on Mile 12, Ikorodu and Ayangbunren returned demolitions at those places that are **not** this project (a Lagos-State-funded Agric-to-Arepo/Isawo road, and later Ikorodu Garage and right-of-way clearances), and the 2016 FIWON/WIEGO field report on Lagos market demolitions does not mention the bus corridor. The limb-(a) case is that traders were moved and then moved again; the counts are of "affected", not of moved.

## 3. Figures and ratings where two documents disagree

| Project | Figure/rating | Document A | Document B |
|---|---|---|---|
| P108005 Serbia | Bank performance | ICR (24 Mar 2020): **Satisfactory** | IEG review: **Moderately Satisfactory**, downrated for site-safety management after the fatal accidents |
| P108005 Serbia | Expropriation on Bank-financed sections | PAD (12 Jun 2009): 230 ha expected (50 + 130 + 50) | ICR: 322.7 ha / 2,092 cases on those sections, 371.8 ha / 2,491 cases with Lot 6 |
| P108005 Serbia | Structures expropriated, Dimitrovgrad bypass | RAP: **33** | Road enterprise's own records: **30** cases (the evaluation attributes the gap to cases bundling a house with auxiliary structures) |
| P081505 Jordan | Outcome / Bank performance | ICR (10 Jun 2013): Moderately Unsatisfactory / Moderately Unsatisfactory | IEG review (posted 25 Feb 2014): **Unsatisfactory / Unsatisfactory** |
| P081505 Jordan | Board approval date | ICR data sheet and projects API: **3 June 2004** | IEG review data sheet: **15 June 2004** |
| P081505 Jordan | Land acquisition and compensation | ICR text: "about US$ 160 million equivalent" | ICR cost table: **US$158.43 million** actual against US$40.90 million at appraisal |
| P112956 Nigeria | Outcome | ICR (25 Oct 2017): **Satisfactory** | IEG review: **Moderately Satisfactory** (modest efficiency; 200 % cost overruns on Mile 12–Ikorodu "that cannot be fully explained by inflation and construction cost", 27 km cancelled) |
| P079736 CEMAC | Bank performance | ICR (29 Oct 2021): **Moderately Satisfactory** | IEG review: **Moderately Unsatisfactory** |
| P079736 CEMAC | Grievance outcome | ICR: 48 of 89 money claims **unpaid**, 61 of 1,350 complaints **never reviewed** at closing | IEG review: "The GRM functioned well and this mechanism made it possible to capture and process **all** the complaints" |
| P079736 CEMAC | Where the halted road is | ICR: Baoro–Bouar is in the **Central African Republic** | IEG review: "the abrupt halt on the construction of the Baoro-Bour road in **Chad**" |
| P096407 Ghana | PAP counts | PAD (25 Feb 2010), para 97: Ghana 744 hh / 2,094 persons | IEG review prints the same numbers as the project's PAP counts without naming them as the plan's |

## 4. What the works actually were — the sector hypothesis

BRIEF21 asked for this from the documents, not from ICIJ's project names. Eight of eleven rows are tagged `road` and one `urban`; the works diverge from the tag in three cases.

| Row | ICIJ `_sector` | What the documents say the works were | Earned a case? |
|---|---|---|---|
| Serbia P108005 | road | Motorway sections on E-75 and E-80 with tunnels; large rural expropriation; blasting beside villages | **yes** |
| Albania P078949 | road | 26 km two-lane road **plus flood protection embankments on both banks of the Mati river**; homes taken | **yes** |
| Jordan P081505 | road | 40 km limited-access ring road **plus a 500 ha customs depot and inland-port land programme** — the depot was never built | **yes** |
| Nigeria P112956 | urban | Road widening with a BRT corridor, bus terminal and depot; **market and street-trader relocation** was the harm | **yes** |
| CEMAC P079736 | road | Road rehabilitation **plus a rail component with CAMRAIL, customs buildings and a road station**; works handed to an army engineering corps for security | **yes** |
| Ghana P096407 | road | 110 km coastal highway **plus trade-facilitation single windows, joint border posts and customs reform**; the road was the only component with resettlement | **yes (thin)** |
| Kenya P124109 | road | 221 km of roads with interchanges **plus Mombasa airport runway and civil aviation reform** | extend |
| Kiribati P122151 | road | 29 km of urban road on South Tarawa; impacts were strips of yard and fruit trees, not structures | no |
| Rajasthan P130164 | road | **About 2,500 km of rural roads plus PWD institutional reform and road safety** — not highway corridors; land by voluntary donation | no |
| Indonesia P079906 | road | 245 km of national road betterment, bypasses and ring roads across seven provinces | no |
| Georgia P112523 | road | One bypass (Ruisi–Agara) on the E60 with landslide and river-protection works; RAP says no physical relocation required | no |

**The result: 6 cases from 11 rows in sectors round 20 found productive, with no complaint flag on any of them, so the complaint flag is not the only predictor.** But the pattern that actually separates the six from the four is not the sector tag: it is **whether the works took houses or trading places**. The four drops all took strips of land, yards, trees or rural donations and recorded compensation paid at or above market price; the six cases all took homes, shops or market pitches, or shook houses until they cracked. Georgia and Kiribati are tagged `road` exactly like Serbia and Albania; what separates them is that nobody lost a dwelling or a livelihood site. A finer predictor than sector, for whoever builds round 22's leads, would be whether the project's own RAP says physical relocation is required — Georgia's says it is not, and Georgia is a drop.

**On the complaint flag:** one row did in fact draw Panel attention despite ICIJ's `complaint: false` — Kenya P124109, which is already on the map because of it, and which drew a second, non-registered request in April 2022. ICIJ's flag is not a reliable negative.

## 5. Routes that worked and routes that failed

Worked:
- Projects API with `countrycode_exact` and a narrow `qterm` found 9 of 11 P-numbers on the first page. The two regional projects needed the country filter **dropped**, as BRIEF20 says.
- `wds?projectid=` plus host rewrite to `documents1.worldbank.org` and `http`→`https`, `curl` to disk, `pdftotext -layout`. 49 documents, no failures.
- `qterm` title search with `docty_exact=Implementation+Completion+and+Results+Report` found three ICRs that `wds?projectid=` had **not** returned on page one: **P108005 (24 Mar 2020), P124109 (29 Jan 2021)**. This is BRIEF21 finding 1 recurring.
- N1 (Serbia) served in full through the fetch tool. Ghanaian Times served in full through the fetch tool.
- Nominatim found every point except one; the Jordan site needed the Arabic form — "Al-Madounah, Jordan", "Madouneh", "Al Madouna" all returned nothing, while **"Maduna, Amman, Jordan"** returned وادي الماضونة, Marka district, at 31.9376 / 36.1351.

Failed, by route not by host:
- **`wds?projectid=P096407` returns no Implementation Completion and Results Report**, and neither does a `qterm` title search on the project's full name plus "Implementation Completion", nor the sibling number P116323 (which has its own 2019 ICR for the Côte d'Ivoire second phase). The report appears genuinely undisclosed; the IEG review of 27 February 2018 is the only route to it. The host served everything else asked of it.
- **`curl -L` to `irep.ntu.ac.uk` for a Nottingham Trent thesis PDF (`/id/eprint/55297/1/2576438_Nwagboso.pdf`) returned HTML, not a PDF** — `pdftotext` reported "May not be a PDF file" and failed on the hex strings of an HTML page. That is one route failing on one URL; the host was not retried through the fetch tool and is **not** a blocked host.
- **Guardian Nigeria served the article "Pains in Ikorodu, as road project devours homes, shops" with no publication date on the page**, so it was not usable; its subject also turned out to be a Lagos-State-funded road (Agric Bus Stop to Arepo via Isawo), not the Bank-financed Mile 12–Ikorodu corridor.
- Searches that returned nothing on the project asked about: Albanian-language sources on the Milot–Rrëshen expropriations; Jordanian sources on the Amman Development Corridor and Madounah acquisitions; French-language sources on house damage and compensation on the Baoro–Bouar road; Lagos press on the Ayangbunren market or the Mile 12 plantain traders in connection with the Bank project. Those four are why five of the six cases are `contested`.

### A near-miss worth recording
The Ghanaian Times of 18 August 2026 reports a "Coalition of Lot 1 Abidjan-Lagos Corridor Road Affected Persons" — **more than 7,000 farmers, landowners and property developers** on the Elubo–Agona Nkwanta section, unable to farm or build for almost three years, who petitioned President Mahama in April 2026 and got no reply, and whom an unnamed Ministry of Roads and Highways source said are ECOWAS's responsibility, not the Ministry's. This is **Lot 1 of a later corridor project**, nine years after P096407 closed, and no source found links it to that credit. It is not used as corroboration on the Ghana card. It may be a lead in its own right for whoever builds the next round.

## 6. Dates

Four of the six Independent Evaluation Group reviews cited here **print no date anywhere on the page** (P108005, P079736, P112956, P096407); the dates on those cards are the Bank's `docdt` catalogue field and each card says so. Two do print one: P081505 "Date Posted : 02/25/2014" and P078949 "Date Posted : 09/27/2013", both matching `docdt`. Every other date on every card was taken off a cover page or a data sheet, never off a URL or filename.

## 7. Notes for the lead

- **`killed` on the extend.** `fields_add` cannot set a number. `webuye-interchange-traders` currently carries no `killed` field. The 2021 ICR records a **fatal accident on site involving the operator of an excavator** on the Kakamega–Webuye section, reported to the police at the time, with the Bank team following up with the roads authority to ensure the family was compensated under Kenyan law. If that case should carry `killed: 1` with a note, it has to be set by hand — the extend states the facts in `fields_add.community` but cannot set the integer.
- `corridor-x-dimitrovgrad-bypass-serbia` carries `killed: 3`, both documents' figure for construction deaths across E-75 and E-80, attributed by both to unsatisfactory management of site safety. IEG notes the ICR never says whether there was negligence.
- `baoro-bouar-road-house-damage-car` carries `killed: 1` for a September 2019 fatality on the **Cameroon** works, while the card's point is in the Central African Republic. The `killed_note` says so plainly. If the convention is that `killed` must sit in the card's own country, this should be moved into `killed_note` text with `killed: 0`.
- Serbia's point is on **Dimitrovgrad town** with `ap: true`, not on a village: the Bank's evaluation locates the affected structures at "CM Dimitrovgrad" and "CM Gradinje", N1 locates the cracked houses in "Gradina". Both villages are on the same bypass section and no document found says they are the same place. The card says so.

## 8. Document cache

`/home/claude/r21/cache/` is **shared with the other round-21 batches** — as of writing it holds 128 paired `.pdf`/`.txt` documents across 36 P-numbers. The **49** fetched for this batch, all paired `.pdf` and `.txt` from `pdftotext -layout` and named `<P-number>_<type>`, are:

- **P108005** (Serbia): ICR, ICRR, PAD, RAP_Dimitrovgrad, RAP_Grdelica, RAP_VladicinHan, RAP_addendum2015, **RAP_E80_eval2016** (the end-of-term impact evaluation of resettlement — the field document the Serbia case turns on)
- **P122151** (Kiribati): ICR, ICRR, PAD, RP_2010, RP_2013
- **P096407** (Abidjan-Lagos): ICRR, PAD, RAP_Ghana (43 MB, Agona Junction–Elubo). No ICR exists to cache.
- **P081505** (Jordan): ICR, ICRR, PAD, RAP_main
- **P112956** (Nigeria): ICR, ICRR, PAD, RAP_Mile12
- **P130164** (Rajasthan): ICR, PAD, RAP_SIA
- **P079906** (Indonesia): ICR, ICRR, PAD
- **P112523** (Georgia): ICR, ICRR, PAD, RAP_2009
- **P079736** (CEMAC): ICR, ICRR, PAD
- **P078949** (Albania): ICR, ICRR, PAD
- **P124109** (Kenya): ICR, ICRR, IP_RR_2020, IP_NONREG_2022

`/home/claude/r20/cache/` (232 files, 115 documents) was checked first and held none of these eleven projects' documents. It holds P126321, Kenya's National Urban Transport project, which is a different project from P124109, and a Ghana urban sanitation project under another number. Nothing in this batch was already cached, so all 49 were fetched. Working files, including the `wds` and download scripts, are in `/home/claude/r21/work/`.

Nothing was merged, `build.py` was not run, and git was not touched.
