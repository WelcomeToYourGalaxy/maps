# Round 37, batch B — writer's report

20 financings in. **3 new cases, 2 extends, 3 already on the map, 12 drops.**
Searches used: 6 WebSearch calls (budget was 30, ceiling 45). Everything else was `curl`
plus local text extraction; AidData's own project pages serve fine over `curl`.

## Outcome of every financing

| Financing | What it is | Outcome | What decided it |
|---|---|---|---|
| G299 Kenya | China Eximbank US$200.5m, Karimenu II dam | **case** `karimenu-ii-dam-compensation` | Agency's own statement, 26 Feb 2020: 228 of 246 phase-one claimants paid, 28 unpaid, contractor holding 136.5 of 171 acres. Buffer-zone compensation still unpaid in Sep 2025 (Capital FM). |
| G209 Kenya | ICBC US$900m export credit, Lamu coal (cancelled) | **case** `lamu-coal-kwasasi-land` | "We surrendered our land and moved out… We need our land back" — 975 acres taken 2016, unpaid in Aug 2020 (The Star); 1,000 acres and a five-year wait in Jul 2018 (The Standard). |
| G193 Ethiopia/Djibouti | China Eximbank US$2.49bn + US$491.8m, Addis–Djibouti railway | **case** `addis-djibouti-railway-compensation` | Railway corporation's own compensation department head told parliament of 25 birr/m² in one kebele against up to 300 birr/m² in another; MPs said some farmers were paid nothing while neighbours were paid (The Reporter, 31 Mar 2018). |
| G192 Sri Lanka | China Eximbank US$74.3m + US$55.4m, Southern Expressway Section IV | **extend** `southern-expressway-sri-lanka` | Same project, confirmed by place (Pinnaduwa–Godagama) and years; adds a lender the card lacked. The card's displacement findings are the ADB Compliance Review Panel's and predate the 2011 Chinese tranche — said so in the extend. |
| G088 Myanmar | CNPC US$32m compensation pledge | **extend** `myanmar-china-pipelines-land` | Same pipelines, same townships. Adds arrests and jail sentences the card had empty (`suppression` was ""), plus a second uncompensated-farmland protest (Feb 2015) and the per-acre mud-damage rate. |
| G004 Sudan | China Eximbank US$608m, Merowe dam | already_on_map | `merowe-dam-amri-manasir` already cites AidData record 178 and already carries the three resettlement-scheme loans in a lender role. |
| G017 Mozambique | China Eximbank US$681.6m + US$72.58m, Maputo–Katembe bridge | already_on_map | `maputo-katembe-bridge` already carries both loans and the 900/920-family resettlement and the 2014 strike. |
| G054 Nigeria | China Eximbank US$984.23m, Zungeru dam | already_on_map | `zungeru-dam-displacement` already cites AidData record 30371, the 98 communities, the 2024 court award and the January 2022 abduction note. |
| G405 Philippines | CDB memorandum of understanding, New Clark City | **drop** | No financing exists. BCDA's own release of 7 January 2018 describes an MOU "that will establish the framework for financing cooperation" over five years, to "determine the most cost effective and efficient financing option" — no loan, and AidData's status is "Pipeline: Pledge". The evictions in the record are on BCDA's Phase 1-A sports complex and the airport access road; the Clark government centre was financed by the Development Bank of the Philippines. Burkina shape: the harm is not on what the Chinese money paid for, because no Chinese money was committed. |
| G417 Viet Nam | Bank of China US$114m in a US$1.988bn syndicate, Vân Phong 1 coal plant | **drop** | The compensation sentence is about a different project — EVN's 500 kV substation and connection line, where 89 of 93 tower foundations had been paid for and "the rest of the people have not yet agreed to receive the money". People declining an offer is not compensation withheld, and no count of anyone moved for the plant site appeared. Bank of China is also one of seven commercial banks behind JBIC's US$1.199bn lead facility. |
| G181 Angola | China Eximbank US$2bn master loan facility | **drop** | The only flagged sentences are the 2017 conviction and suspended death sentence of a China Eximbank official, Dai Chunning, for bribery. Corruption in the lender's own ranks is not a documented harm to identifiable people under either limb of the forward rule. |
| G653 Sri Lanka | Xinhua subsidiary donation after 2016 floods | **drop** | Relief: the 102 deaths are the flood's, not the money's. |
| G651 Mozambique | Beijing Urban Construction Group flood relief | **drop** | Relief: the deaths and evacuations are the January 2013 flood's. |
| G063 Sudan | Sinohydro Bureau 7, 50,000 Sudanese pounds to flood victims | **drop** | Relief: "Hundreds were injured or killed" is the 2013 rainy-season flooding. |
| G090 Viet Nam | US$100,000 bird-flu emergency aid | **drop** | Relief: the 38.1m birds culled are the H5N1 outbreak's. |
| G115 Mali | Peacekeepers sent after the Air Algérie AH5017 crash | **drop** | Relief: the deaths are the crash's. |
| G008 Comoros | US$320,000 for a Guangzhou malaria study on Mohéli | **drop** | The flagged sentence is malaria mortality in under-fives, i.e. the disease the money treated. |
| G294 Niger | Anti-malarial medicine donation | **drop** | Same: the flag fired on "malaria-induced death rates". |
| G638 Solomon Islands | Road construction materials, Fataleka road | **drop** | The "death with a cause" flag fired on a donation ceremony and a road description. Nothing adverse is recorded at all. |
| G610 Solomon Islands | Embassy material donation, Fataleka community | **drop** | Same: a handover ceremony. The dedupe hint to `santa-cruz-lata-airfield` is a false hint — shared words are "islands", "province", "solomon". |

## My two weakest entries

1. **`addis-djibouti-railway-compensation`.** The whole harm is one article in The Reporter
   (Ethiopia), 31 March 2018. It is good material — the corporation's own Right of Way and
   Compensation Department head confirming unequal rates, with figures — but it is one source,
   there is no count of anyone moved, the two kebeles are unnamed, and the MPs' statements are
   reported speech from a hearing with no published committee document behind it. The Pulitzer
   Center piece that would corroborate it (Tom Gardner, "In Ethiopia's Bushlands, Promised
   Riches of a Railway Boom Turn to Dust", cited by The People's Map) would not open: see routes
   below. The point is also district-level at best — `ap: true`, set at Mieso because that is
   where the two Chinese-built sections meet, not because harm was recorded there.
2. **`lamu-coal-kwasasi-land`.** The land harm is solid and doubly sourced, but the lender link
   is the weak joint: an indicative term sheet, a financing AidData marks cancelled, a withdrawal
   announced by an NGO rather than the bank, and a Chinese embassy attaché on the record saying
   no Chinese company was ever involved. It is filed `contested` for exactly that. The two farmer
   groups also pull in opposite directions — the Kwasasi Farmers Association demonstrated *for*
   the plant while demanding payment, Save Lamu against it — and both are on the card so the
   quotation is not one-sided.

## Figures where sources disagree (both printed on the cards)

- Karimenu II phase one: **Sh1.28 billion to 246 people** (water cabinet secretary, The Star,
  1 Aug 2019) against **Sh1.09 billion to 228 people** with 28 unpaid (Athi Water Works
  Development Agency statement, The Star, 26 Feb 2020).
- Karimenu II loan face value: **US$200,530,600** (Kenya's external public debt register, which
  AidData follows) against **US$31 million** (SAIS-CARI) and **US$229 million** (Boston
  University) — all three per AidData's staff comments.
- Lamu land: **975 acres acquired in 2016** (The Star) against **1,000 acres** (The Standard).
- Lamu ICBC share: **US$900 million export credit** (AidData) against **US$1.2 billion, 60 per
  cent of a US$2 billion cost** (The Star).
- Lamu capacity: **981.5 MW** (AidData) against **1,050 MW** (both Kenyan papers).
- Lamu tribunal ruling: **June 2019** (The Star) against **26 July 2019** (AidData).
- Addis–Djibouti first tranche: AidData's record text says **$1.2 billion** in one row title and
  **$1,289,029,000** in the description; its own project page for record 70086 is headed
  **$1.28 billion**. The card uses $1,289,029,000.

## Routes that worked and routes that failed

Worked over `curl` with a desktop user agent: `china.aiddata.org/projects/<id>/` (HTML, full
description renders without JavaScript — records 45520, 52499, 58737, 34197, 70086 all read),
`the-star.co.ke`, `standardmedia.co.ke` (the `/amp/` path), `capitalfm.africa`,
`thereporterethiopia.com`, `thepeoplesmap.net`, `bcda.gov.ph`, `rfa.org`, `ecoi.net`,
`bnionline.net`, `api.openstreetmap.org` and `nominatim.openstreetmap.org`.

Failed, with the exact route:
- `GET https://peopledaily.digital/news/...` and its `/amp` variant → **403** with a browser user
  agent (two articles, including the one AidData's 383-acre figure appears to rest on). Other
  pages on that host were not tried.
- `GET https://nation.africa/kenya/counties/kiambu/poor-millionaires-...` → **403** with a browser
  user agent.
- `GET https://pulitzercenter.org/reporting/ethiopias-bushlands-promised-riches-railway-boom-turn-dust`
  → **403** over `curl` with two different user agents, and the fetch tool returned
  `client_error` with nothing of the page. Not a host-wide block statement — that one URL on that
  host, two methods.
- `GET https://www.accountabilitycounsel.org/wp-content/uploads/2019/05/updated-summary-of-complaint-english-17-page.pdf`
  and `.../2018/04/cao-complaint-re-fi-investment-in-lamu-coal-plant.pdf` → **404** (both served
  an HTML error page with a 404 status). So the Save Lamu / Kwasasi Mvunjeni complaint to the IFC
  ombudsman is *not* on the Lamu card; the quotation from it on the card is attributed to
  AidData's record, which carries it. A later round should find the complaint through
  `accountabilitycounsel.org/client-case/kenya-lamu-coal-fired-power-plant/` and add the `cao`
  complaint tag.

## Document cache

`/tmp/r37b/` holds every page fetched, named by an md5 prefix of its URL, plus `ad<record>.html`
for the five AidData project pages and `ejdr.pdf`/`ejdr.txt`. Note `ejdr.pdf` (Adane, Zeleke and
Seyoum, "Impacts of Railway Development Induced Land Displacement… South Wello Zone") is **not**
about this railway — it is the Awash–Weldiya line in Amhara, Turkish-built — and was not used.
It is a cheap trap for the next writer searching "Ethiopia railway displacement".

## For the next round

- AidData's **coordinate for record 58737 is wrong**: it points to a village called Kiriko at
  −0.6666, 37.4000 (OSM node 44931883), outside Gatundu North and about 60 km from the dam. The
  card uses the dam's own OSM location, −0.91122, 36.85784. Other AidData coordinates in this
  batch (Lamu, Zungeru) checked out.
- **Merowe's resettlement-scheme loans need a correction that an extend cannot make.** The
  existing card says China provided "US$110.7 million for the New Amri resettlement farm scheme
  and US$37.7 million for the Kehaila East and El Makabra schemes". AidData's own row titles in
  this batch give record 56927 as **$37.7m for New Amri**, record 56959 as **$80.75m seller's
  credit to CWE for Kehaila East**, and record 85574 as **$29.9m for El Makabra** — while
  AidData's staff comment 7 on record 178 says the opposite assignment. AidData contradicts
  itself; the four records should be opened one by one before anyone rewrites that lender role.
- The `r36_decisive` bucket "death with a cause" fired on a **donation ceremony** twice in this
  batch (G638, G610) and on disease mortality three times. In batch B it never once marked a real
  project death. The relocation-count and compensation-withheld buckets did all the work.
