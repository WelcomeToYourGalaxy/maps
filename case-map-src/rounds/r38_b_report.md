# Round 38, batch B — report

17 financings, 13 countries. Output: **1 new case, 4 extends, 4 already_on_map, 8 drops.**
WebSearch calls used: **6**. Everything else came over `curl` (AidData project pages, Malaysian
press, Nominatim).

---

## Every financing, with the sentence or absence that decided it

### 1 new case

**G201 — East Coast Rail Link Phase 1, Malaysia (China Eximbank, records 85858 / 73473 / 49309)**
→ **case `ecrl-gombak-demolitions-floods`**

The limb-(b) bucket in the batch was "land taken", and AidData's own sentence for it is weak: land
acquisition appears only in a list of 2018 implementation activities. The harm is in Malaysian press
and in a Selangor government statement:

- Sinar Harian, 14 December 2023: a Selangor lands and mines department census on 21 November 2023
  "mengesahkan 135 struktur terlibat dalam jajaran ECRL di Desa Mukmin… kesemua 135 struktur ini
  melibatkan seramai 157 orang ketua isi rumah", with a clearance order issued 13 December 2023 and
  a 15 January 2024 deadline. Ex-gratia: RM 3,000 moving cost, RM 1,500 a month rent for 24 months,
  structure payment, 49 flats at RM 79,000.
- Free Malaysia Today, 24 February 2024: "some 2,500 residents from 13 villages in Gombak intend on
  filling an injection after **151 homes were demolished** to make way for the project." Past tense,
  so this is the outcome rather than the plan.
- Malaysiakini, 11 October 2023: named residents of Kampung Sungai Salak on flash floods after tree
  and hillside clearing, and of Kampung Sungai Chinchin on cracked walls and broken tiles in houses
  and the Tabika Kemas Batu 7 kindergarten after piling began on 21 September 2023. The article also
  prints the project team's denial, which is on the card.
- Selangor Journal, 21 October 2024 (state media, quoting the chief minister): flash floods
  "resulting from the ongoing construction"; 21 houses in low-lying areas to move to rented homes at
  Malaysia Rail Link's cost; MRL "agreed to bear the cost of repairing damages to homes and roads
  caused by material explosions".

`displaced` is **omitted**. 157 is a count of household heads under an order to vacate, which the
`prospective_verb_only` screen bars from that field, and 151 is a count of houses, which the
structure rule bars. Both figures are in `displaced_note` with their verbs.

### 4 extends (all `fields_add` on `conditions`, no numbers set)

- **`souapiti-dam-guinea`** — the live AidData record (187) carries a collateral clause the card
  lacks: the loan was secured on SOGES S.A.'s future electricity sales receipts and on a
  lender-controlled escrow account rising from US$20m to US$90m, to be reached by March 2021; and
  Guinea funded its 15% share by selling its 51% SOGEKA stake to China Three Gorges for US$200m.
- **`lower-sesan-2-dam`** — record 62217 gives a 17-year maturity, 5-year grace, fixed 6.5%, and
  collateral the card lacks: all perpetual leasehold rights in the land and all plant machinery,
  plus the Royal Power Group and EVN International stakes in the project company.
- **`bishkek-chp-heat-failure`** — record 39620 gives the credit's reference number, its terms, full
  disbursement with US$389,924,333.33 outstanding on 31 December 2021 per Kyrgyz finance ministry
  data, and the 2021 payment suspension. None of that is on the card.
- **`celukan-bawang-coal-bali`** — record 49810 gives US$367m disbursed by end-2014 and a US$638m
  total plant cost; the card has neither.

### 4 already_on_map

- **G344 Techo airport, Cambodia → `techo-airport-land`.** The card already holds the 2,000 families
  at US$100 each and the May 2019 protest. The "arrest or detention" bucket is AidData's 2010
  sentence — ten villagers arrested blocking bulldozers — which belongs to the Heng Development land
  dispute that AidData says "pre-dates announcement of the airport", eight years before the CDB
  loan: it fails the time-overlap test. The 2009 shooting that wounded three villagers is from the
  same pre-loan dispute. Nothing added.
- **G360 Sorik Marapi, Indonesia → `sorik-marapi-gas-leak`**, already holds `killed: 5` from Kompas,
  and the card's lender line already carries the US$122.4m each and the 10-year maturity.
- **G398 Ramu, Papua New Guinea → `ramu-nickel-basamuk`.** AidData's death sentence is "a man died
  from a 'cocktail of heavy metals,' the lawsuit alleges". The card holds `killed: 0` with that
  allegation in `killed_note`. **Not raised.** The card's lender entry already carries both the
  US$560m China Eximbank facility and the US$473m shareholder loan with their terms.
- **G469 Barishal, Bangladesh → `barishal-coal-plant-evictions`**, already holds the BWGED figures
  (153 families affected, 142 evicted by force) and Transparency International Bangladesh's account
  of threats and assaults, and already names AidData's US$390.5m assumed face value. See the figure
  disagreement below.

The two other already-carried entries, **G358 Lower Sesan 2** (`displaced: 5000`, HRW) and
**G005 Souapiti** (`displaced: 16000`, HRW), are recorded as extends above: their harm figures were
already on the cards and the extends add loan terms only.

### 8 drops

- **G060 Zimbabwe, ZBC broadcasting van.** The arrest is of the broadcaster's own chief executive:
  "Zimbabwe Broadcasting Corporation (ZBC) CEO, Happison Muchechetere, was arrested and accused of
  inflating the cost of the van to $1,050,000". A fraud prosecution of an official is not a harm to
  identifiable people under limb (b). No count of anyone affected.
- **G444 India, CDB loan to Sistema Shyam.** The "land taken" flag fires on loan boilerplate: the
  events of default include "any legal proceeding initiated with a view to the seizure, compulsory
  acquisition, expropriation or nationalisation of all or a material part of the undertakings,
  assets… of SSTL". That is a covenant about the borrower's own assets, not land taken from anyone.
- **G361 Malaysia, Trans-Sabah Gas Pipeline / Multi-Product Pipeline.** The arrest flag is Bank
  Negara's six charges against the state borrower SSER, fined RM 18 million on 5 April 2019 for
  disbursing 88% of contract value against 11.4% and 14.5% completion. Public money lost, no
  documented harm to identifiable people.
- **G356 Malaysia, Edra acquisition.** The arrest flag is the 2016 Interpol red notice for Jho Low
  in the 1MDB investigation. Nothing adverse recorded to any identifiable person from the
  acquisition loan.
- **G194 Mongolia, New Century Education.** "In 2013, Mongolia's Anti-Corruption Agency detained ZTE
  managers for alleged bribery". Detention of the contractor's own managers, denied by ZTE; no harm
  to schools, teachers or pupils recorded.
- **G180 Nauru, offer to repay the General Electric debt.** Fails test 1 before it reaches the
  arrests: "there is no evidence that the Chinese Government ultimately followed through on its debt
  relief commitment", and the row is a null-amount pipeline commitment. The four opposition MPs
  charged with sedition in April 2004 were charged by Nauru's own authorities after blocking the
  president's flight; no document ties that to money that never moved. (A separate lead worth
  someone's time: the 1999 US$99m General Electric Capital loan to the Nauru Phosphate Royalties
  Trust, its default, receivership and the public debt crisis — mechanism `debt`, not this batch.)
- **G121 Pakistan, Safe City Islamabad (Huawei, China Eximbank).** The arrest bucket turns out to be
  an absence of arrests: senior police officers told Dawn in July 2022 that "no criminals, suspects
  or proclaimed offenders were arrested through the CCTV system". The project director's death in
  September 2022 is recorded by police as "an apparent suicide", with no cause tied to the project.
  Two searches for an arrest, detention or prosecution of an identifiable person through the
  Islamabad system returned only the Rs 17.4 billion 2025 AI-camera expansion, which is a later
  procurement, and May 2023 "technical evidence" work by **Punjab** police on the Lahore Punjab Safe
  City system, a different financing. Dropped for want of harm to an identifiable person.
- **G380 Philippines, Chico River Pump Irrigation Project.** The "death with a cause" bucket is the
  murder of Macli-ing Dulag in April 1980, which belongs to the Marcos-era, World Bank-linked Chico
  River Dam Project — already on the map as `chico-river-dam` with `killed: 1` — and predates this
  2018 China Eximbank credit by 38 years. For the irrigation project itself, what the record carries
  is procedural: the certification precondition was issued on 23 May 2019 after construction had
  begun, and the Cordillera People's Alliance says free, prior and informed consent was not obtained
  in Katabbogan and Pinococ. China Dialogue (via Eco-Business, March 2021) records the dismantling
  of the Dulag monument in January 2021 by the public works department because it "obstructed" a
  road, and a shoot-to-kill order against CPA chairperson Windel Bolinget, but it ties neither to
  this project — attributing them to it would be supplying a cause from nearby text. No count of
  land taken, compensation withheld or anyone harmed. Dropped.

---

## My own two weakest entries

1. **`ecrl-gombak-demolitions-floods` — the 151 demolished homes.** This is the case's hardest
   outcome figure and it is second-hand: Free Malaysia Today reporting what another report said,
   inside an article whose subject is the chief minister calling the objectors outsiders. No
   government count of demolished homes was found, and the Malay Mail and The Vibes reports of "89
   families affected" (February 2023, Klang) could not be read, so that figure is not on the card.
   If a checker cannot stand the 151 up, the case still holds on the Sinar Harian census (135
   structures, 157 household heads, clearance order dated) and the Selangor Journal statement, but
   the `displaced_note` would need the 151 removed.
2. **The `celukan-bawang-coal-bali` extend.** It adds a disbursement figure and a project cost and
   nothing about harm. It is the thinnest thing in this file and the lead should feel free to cut it
   without loss.

---

## Figures where two documents disagree

- **Barishal (G469).** The live card says AidData's record read on 11 November 2026 gives one
  syndicated facility of US$427.5m with a commitment date of 1 April 2020. The round-38 batch text
  for record 71614 says the facility was signed in September 2021 with a 15-year maturity, a
  sovereign guarantee dated 23 December 2020 and Sinosure cover from 27 October 2021, and that
  AidData assumes a face value of US$390,523,000. Same publisher, two read dates. Not patched.
- **Souapiti (G005).** The batch's AidData text gives the credit a 20-year maturity, 7-year grace
  and 2% interest. The live AidData page for record 187, opened 15 November 2026, gives 15-year
  maturity, 5-year grace and 4.6038%. The extend therefore carries **only** the collateral clause
  and the SOGEKA sale, which both versions agree on, and no maturity or rate.
- **ECRL (G201).** The batch text dates the preferential buyer's credit to 2018 at RM 39.1 billion;
  the live records date it to on or around 1 April 2017 and split it RM 37.7bn drawn (85858) /
  RM 37.4bn cancelled (73473). The card uses the live records and names both record numbers.
- **ECRL line length.** 655 km (BenarNews) against 665 km (New Straits Times). Both are in `whole`.

## For the lead: two things `fields_add` cannot do

- **`celukan-bawang-coal-bali`.** Its `whole` field says no measured output was found. AidData's
  record 49810 states: "As of May 17, 2017, the power plant had generated 5.2 billion kilowatt
  hours, accounting for 40% of Bali's total power supply and allowing Bali to stop relying on power
  generation and supply from Java." That is a measured output figure and it contradicts the existing
  sentence, so it needs a rewrite of `whole`, not an append. Not put in the file.
- **`souapiti-dam-guinea`.** With the escrow and sales-receipt collateral now on the card, its `ct`
  should gain **`repay`** beside `tied`. `ct` cannot be appended here.

## Routes that failed, named as routes

- `nst.com.my` article pages over `curl` return 200 but the body is script-rendered and absent from
  the response; the **`/amp/` path on the same host serves the full text** and is what was used.
- `thestar.com.my` serves the headline and first paragraph, then a subscription wall, over `curl`.
  The Star's RM 50.27 billion construction-cost figure was therefore **not** used.
- `malaymail.com` and `thevibes.com` article pages over `curl` return 200 with no article body
  (script-rendered). The "89 families" figure was dropped rather than taken from a search title.
- `mrl.com.my` (the project owner) returns a page whose only content is "This site requires
  JavaScript to function properly."
- Nominatim returns nothing for "Desa Mukmin, Gombak, Selangor, Malaysia" in any spelling tried; it
  does return Kampung Sungai Chinchin and Taman Sri Gombak, and the point uses Sungai Chinchin.
- None of the above is a host refusal. `china.aiddata.org/projects/<id>/` served every record in
  full over plain `curl`, as BRIEF36 said it would.

## Cache

Downloaded pages are in `/tmp/r38b/` as raw HTML, named by an md5 prefix of the URL, plus
`aid187.html`, `aid39620.html`, `aid49810.html`, `aid62217.html`, `aid73473.html`, `aid85858.html`
(AidData records), `benar_ecrl.html`, `eco.html` and `nstamp.html`. `/tmp/strip.py` is the
tag-stripper used to read them. The folder is temporary; nothing was written into the repo outside
`rounds/r38_b.json` and this report.
