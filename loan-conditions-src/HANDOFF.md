# Loan conditions map: handoff

Live page: https://welcometoyourgalaxy.github.io/maps/loan-conditions.html
File in this repo: `loan-conditions.html`, one self-contained page with the data embedded gzip-compressed. Its atlas plate is `loan-conditions-atlas-plate.webp`.
Source and pipeline: this folder, `loan-conditions-src/`.

This file lists what is still open, with what has already been tried, so a new chat can pick any item up.

## How the page is built

1. `build_data.py` reads the downloaded sources and writes `data.json`. It holds every row's data.
2. `build_map.py` fills three placeholders in `template.html`:
   - `/*__DATA__*/` gets `data.json`, gzipped and base64-encoded. The page decompresses it with `DecompressionStream`.
   - `/*__BASEMAP_CONST__*/` gets `part_consts.js`.
   - `/*__BASES__*/` gets `part_bases.js`.

   The result is written to `loan-conditions.html`.
3. Tests run in headless Chromium with swiftshader:
   - `tests/t3.py` checks for page errors.
   - `tests/test2.py` checks every row, popup and tip.
   - `tests/t_pts.py` checks the point layers and the flat map.
4. Paths in the scripts are absolute (`/home/claude/work`, `/home/claude/dl`). Downloads were not kept, so a new session must fetch them again. Every source is listed below.
5. Commits are made as `Claude <noreply@anthropic.com>` and pushed to `main`.
6. The user's rules:
   - Never fabricate anything.
   - Include everything a source publishes.
   - No orange, yellow or neon colours.
   - Plain, short wording for novices.
   - Label any counting done by the map as "this map's own".

## Open items

### 1. IMF conditions before 1980 (own coding from IMF Archives board papers)

What exists:
- `imf-archive/` holds the pipeline. `data/` holds the outputs:
  - `pre80_coded_all.json`
  - `imf_conditions_1952_1979_own_coding.csv`: 1,234 conditions across 316 loans.
  - `imf_pre1981_documents.csv`: 6,118 papers, each with a PDF link.
- How the papers were found:
  - The IMF stores its archive PDFs in a public Azure container: `https://stoprdcom01e2.blob.core.windows.net/allfiles/IG/Production%20Hosting/Adlib/Public%20Documents/EB/<id>.PDF`.
  - Listing is allowed: `?restype=container&comp=list&prefix=...`. See `listblobs.py`.
  - All 12,294 files with ids 222000–239000 were downloaded (about 3.5 GB). That id range covers board papers from 1956 to 1981.
  - The first page of each was read (`get1.sh`). Its "Subject:" line gives the country and topic (`subjects.py`).
- The rule (`code_v2.py`, run by `code_all.py`):
  - Find the agreement's clause saying when the money stops or talks are required ("During any period … in which (1)…").
  - Count each listed item, plus each paragraph of the government's letter that the item points to.
  - Kinds: QPC is a binding number, SPC is a binding rule or step, IB/SB is a target that only triggers talks.
  - The policy area comes from keywords in the item, or in the opening of the paragraph it points to.

Still open:
- **70 loans whose papers were found but not counted.** Their conditions are ordinary promises in the letter, with no "the money stops if…" list. A person, or a careful reading pass, must decide which promises were conditions. Do not guess. The loans:
  - Argentina 1960-12-12
  - Belgium 1952-06-19
  - Bolivia 1964-09-01, 1962-08-08
  - Brazil 1961-05-18
  - Burundi 1965-01-26
  - Chile 1961-02-16, 1958-04-01, 1956-04-01
  - Colombia 1957-06-19
  - El Salvador 1959-10-01, 1958-10-01
  - France 1958-01-31, 1956-10-17
  - Guyana 1972-05-15, 1971-05-03, 1970-04-06, 1969-03-29
  - Haiti 1977-08-02, 1972-07-06, 1971-06-29, 1970-06-29, 1958-07-14
  - Honduras 1979-06-28, 1959-01-29, 1957-11-12
  - Indonesia 1961-08-16
  - Japan 1964-03-11, 1962-01-19
  - Korea 1977-05-06
  - Liberia 1976-01-14, 1974-08-14, 1973-05-17, 1972-03-01
  - Mexico 1959-03-05
  - Morocco 1965-09-23, 1959-11-15
  - Myanmar (Burma) 1973-02-02, 1969-11-24
  - Nicaragua 1958-09-15, 1957-10-07, 1956-11-21
  - Pakistan 1958-12-08
  - Panama 1974-10-16, 1973-08-03, 1972-06-22
  - Paraguay 1958-07-30, 1957-07-30
  - Peru 1963-03-01, 1959-03-01
  - Philippines 1967-01-05, 1965-04-12, 1964-04-12, 1963-04-12
  - Samoa 1978-02-06, 1977-01-31, 1975-11-12
  - South Africa 1961-07-06
  - Spain 1960-08-17, 1959-08-17
  - Sri Lanka 1971-03-18
  - Sudan 1968-12-05
  - Tunisia 1965-11-12
  - Turkey 1963-02-15
  - United Kingdom 1967-11-30, 1956-12-22
  - Uruguay 1976-08-04
  - Yugoslavia 1971-02-22, 1967-01-01, 1961-01-01
- **7 loans with no papers found:**
  - Finland 1952-12-05, Mexico 1954-04-16, Peru 1954-02-18. Board papers before 1956 seem to be outside ids 222000–239000.
  - Haiti 1960-10-01, Syria 1960-05-02, Uruguay 1961-06-06. They should be in range, but no first page matched.
  - Dominica 1979-09-01, an emergency loan.

  Next step: search the IMF Archives Catalog (archivescatalog.imf.org, database `ArchiveExecutive`) for these countries and years. The catalog's search result pages give the blob PDF link for each item.

  Warning: the catalog sits behind Akamai, which blocked the user's Chrome after about 70 quick searches. Space searches 8 or more seconds apart. The workspace shell gets 403 from the catalog, but the blob store works from the shell.

  The rest of the blob store is ids 240000–399999: about 140,000 files, 94 GB. Older papers may be there, but there is no title index. Checking first pages needs a smarter sample, such as the id ranges near known 1950s items (250376, 282872, 322487, 374987).
- **Accuracy checks still worth doing:**
  - 119 of the 1,234 conditions have no policy area ("OTH").
  - Some items are garbled because the scans are typewritten text read by machine.
  - Clauses that point to whole tables ("Table 2 of the memorandum") count once per clause item, not once per table line.
  - Spot-check against the text:

    ```
    python3 -c "import json;o=json.load(open('pre80_coded_all.json')); ..."
    ```

    Each record keeps `clauses` (the text as found) and `source` (the PDF).
- Yugoslavia's conditions are counted in the row total, but the map has no shape for it. This matches the other rows.

### 2. World Bank condition counts (this map's own rule)

- `wb_count.py` counts the numbered items under headings like "Prior Actions" in the agreement texts from Winter et al.
- 732 of 1,018 loans are counted.
- Against Winter et al.'s counts on 473 loans: mean 8.5 against 10.9, within 2 on 204 loans, correlation 0.33. That is weak.
- Open:
  - Improve the rule, or find why the two counts differ, for example lettered sub-items or schedules.
  - The 286 uncounted loans have texts with no numbered list.

### 3. Euro-area rescue fund (ESM) conditions

- The ESM publishes its programme conditions in a Power BI report. It was blocked from the shell, and nothing was obtained.
- The map's EU row lists programmes but not their individual conditions.
- Try the ESM's site in a browser, or look for a downloadable export.

### 4. IMF MONA codes the IMF does not define

- Codes `MD` (1,147 rows), `CAN`, `AC` and `WC` are shown exactly as given. The IMF's MONA labels page does not define them.
- Find an official definition before giving them any meaning.

### 5. Money-flow rows: known holes

- Profits that foreign owners take home are not shown, because the World Bank publishes no such series by country.
  - A possible lead is IMF balance-of-payments direct-investment income. It must be by country, from an official source.
- Saudi Arabia and Qatar (AidData TUFF datasets) cover only the years those datasets cover (about 2010–2013).
- Bilateral debt by creditor uses the World Bank International Debt Statistics `DT.DOD.BLAT.CD` with counterpart `all`, saved by `ids_get.py`. Other series by creditor (debt service, interest) were not fetched.

### 6. Point layers (added 24 Oct 2026), and more that could be added

- On now:
  - World Bank project sites. Source: AidData/World Bank Geocoded Research Release Level 1 v1.4.2; 61,243 locations of 5,684 projects approved 1995–2014.
  - Chinese state-financed project sites. Source: AidData GeoGCDF 3.0 (`github.com/aiddata/gcdf-geospatial-data`, folder `latest/geojsons`). There are 9,405 projects, each shown at one point inside its outline.
- Not found yet:
  - World Bank project locations after 2014. The Projects API v2 no longer returns `locations`.
  - Other lenders' project sites, for example AidData's geocoded releases for the African Development Bank or Asian Development Bank, if any exist.
  - Points for protests against austerity or IMF programmes. They need an open, citable, geocoded dataset that ties each protest to a condition. ACLED is licensed; general protest datasets (Mass Mobilization) were left out on purpose because they are not about conditions.

### 6b. Added 25 Oct 2026

- **Country row "Sales of state firms and services, as the World Bank recorded them"** (`D.wbpriv`): every row of the World Bank Privatization Database files `PrivatizationData88_99.xls` (8,339 rows) and `PrivatizationData00_08.xls` (1,858 rows), 10,197 in all. The originals are no longer on rru.worldbank.org; copies are in `github.com/pudo/dpkg-wb-privatization` (public, cloned with git). Country names matched to ISO3 from the map's own World Bank names plus a short manual list; "Serbia and Montenegro" has no shape. The 2000–2008 file is described as deals of US$1 million or more, but 5 rows are below that; the fine print says so.
- **Point layer "Where a loan condition led to harm"** (`D.cases`, 151 cards, `cases/`):
  - 105 from the globalization map (`globalization.html`, kinds privatization, trade, austerity), copied as published there (`cases/from_glob.json`).
  - 46 new (`cases/checked*.json`), researched to `cases/BRIEF.md` and then fact-checked by separate agents to `cases/CHECK.md`. Eight researched cases were dropped on review, and the researchers' own drops are in `cases/dropped_all.json` with reasons.
  - Leads not researched because the search allowance ran out: Nigeria NEPA, Dominican Republic power, Lagos/Nairobi/Maputo water, Ghana gold, Bolivia COMIBOL, Iraq 2019, Lebanon, Senegal, Burkina Faso 2008, Philippines, El Salvador, Brazil 1998–99, India farmer debt, Nicaragua/Honduras coffee, pension privatizations.
  - Company head-office cities the checkers found no source for are blanked (`cases_build.py`, `NOHQ`).
  - Contested cases are drawn as rings. Kinds can be switched off one by one.
- **Point layer "Services taken back into public hands"** (`D.pf`): all 1,787 published cases of the Public Futures database (University of Glasgow / TNI), fetched from its site API (`https://publicfutures.org/api/cases/<id>`, plus `/api/classification-types`, `/api/classification-options`, `/api/economic/services`, `/api/economic/sectors`). Placed by `pf_build.py` and `pf_pass2.py`: 1,270 at the OpenStreetMap place the database links (Nominatim lookup), 490 by searching the place name (approximate), 27 at the middle of the country because no place matched. Four Argentine province links in the database pointed outside Argentina and were re-placed by province name.
- Rebuilding without re-fetching: `data.json` can be decoded from the live page (the gzip/base64 string in `LC_DATA_GZ`); then run `cases_build.py` and add `pf_rows.json` as `D.pf`.

### 6c. Added 25 Oct 2026 (second round)

- **17 more condition-harm cases** (`cases/batchE.json`, `batchF.json` → checked to `cases/checked3.json`, `checked4.json`), 168 in all. Leads still not researched: Lagos and Nairobi water, Mongolia, Philippines rice tariffication, Nicaragua/Honduras coffee credit, Ecuador's 2025 public-job cuts (a possible contested case; source in `batchF.json` "dropped").
- **Point layer "Protests against governments, 1990–2020"** (`D.mm`, `mm_build.py`): every one of the 15,239 protest events in the Mass Mobilization Project file `mmALL_073120` (Harvard Dataverse doi:10.7910/DVN/HTTWYL, v5.1). Placed by matching the free-text location to GeoNames (cities of 1,000+ and first-level regions) inside the event's country: 12,726 at a named town, 142 at a named region's largest town, 2,371 at the capital (no town named or matched). USSR events are searched in all 15 former republics. The menu filters by demand (prices and taxes, wages, land), by records whose notes mention the IMF or World Bank (49), and by shootings or killings. It is the largest part of the page (about 4 MB compressed).
- **Section "Patterns behind the scenes"** (lender `Pat`; `D.pats`; each row colours countries by role, draws arcs for documented links, and lists timeline, sources, statistical studies, one author's claims and unproven points):
  - Researched (`patterns/BRIEF.md`, researcher files `R1`–`R4.json`, checked to `patterns/checked1`–`4.json` per `patterns/CHECK.md`): Cold War reward and punishment; dictators' debts; inflated forecasts and insiders (Perkins kept in claims_per_author only); the economists' pipeline; Washington's hold on the IMF and World Bank; the revolving door; rescue loans that paid foreign lenders; investors suing after privatization.
  - Computed from the map's own data (`waves_build.py` → `waves.json`): waves of IMF lending; sold off then taken back; price protests in IMF program years; waves of IMF conditions.
  - Row "Who wins the contracts the World Bank pays for" (`D.wbca`, `wbca_build.py`): all 506,812 contracts in the World Bank's three contract-award files (FY2001–2016 DS01004, FY2017–2019 DS04691, FY2020 on DS00005, financesone.worldbank.org). Firm names are as written (no merging of spellings). Capitals from GeoNames (`cap.json`) anchor the lines.
- `assemble.py` puts everything together: `data_base.json` (old rows plus privatization database) + cases + Public Futures + protests + contracts + capitals + patterns.
- Research note: in these sessions WebFetch only opens pages a web search returned, and the searches are capped per turn across all agents. IMF and World Bank PDFs download fine with curl.
- Ideas for more pattern layers not yet done: arms and military aid alongside lending; tied aid (OECD tying status is already a row); the IMF's gold and SDR allocations by quota; debt service as a share of revenue over time.

### 7. Map behaviour

- Flat map: edge clamping is done by hand (`keepWorldInView`), because MapLibre 5.24's `setMaxBounds` throws after switching projection.
- Stars: drawn on a seeded canvas (`#stars`) behind the map.
- Dot colours: the dots change with each background (`PTCOL`).

## Sources to fetch again

| Source | Where |
|---|---|
| IMF Monitor (Kentikelenis et al.) | Harvard Dataverse |
| IMF lending arrangements | IMF lending page |
| MONA | User-supplied `Combined.xlsx` (imf.org/mona) |
| World Bank Projects API v2/v3 | search.worldbank.org/api |
| Winter et al. 2025 conditions | doi:10.7910/DVN/AF3EZP |
| IDB | IDB open data |
| OECD CRS, DAC7B, PPFD | sdmx.oecd.org (dcd-public and public endpoints) |
| AidData GCDF 3.0, How China Lends, TUFF | aiddata.org; TUFF CSVs via raw.githubusercontent.com |
| Paris Club | clubdeparis.org pages, served via bercy1.applis.finances.gouv.fr |
| EU MFA | Council report ST 11024/26 ADD 1, Annex 2 |
| EU programme pages | economy-finance.ec.europa.eu |
| WDI and IDS | api.worldbank.org/v2; IDS is source 6 with counterpart areas |
| IMF Archives | Blob store above; catalog at archivescatalog.imf.org |
| Geocoded World Bank | github.com/AidData-WM/public_datasets, `geocoded/WorldBank_GeocodedResearchRelease_Level1_v1.4.2.zip` |
