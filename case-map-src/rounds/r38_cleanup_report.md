# Round 38 cleanup — the Samoa case and four company descriptions

Two jobs, five items. Nothing else in the repo was touched; nothing was merged, built or committed.

## Job 1 — AidData financing G408, Apia Park stadium, Samoa

### What I opened

- `docs/leads_aiddata.json`, lead 64861, the single row in financing group G408 (`r36_financing_rows: 1`),
  carrying `r36_buckets: ["death with a cause"]` and `r36_decisive_evidence: true`, with round 37's
  `r37_outcome: "live_lead"`.
- `docs/aiddata_full_text.json.gz`, `records["64861"]`, the untruncated record. The lead file's
  `description` was cut 890 characters short, and the sentences that decide the case sit past the cut:
  the February 2007 death, the second engineer's hospitalisation and the Samoan worker's injury are
  all in the full text and none of them is in the lead file.
- **RNZ Pacific**, `https://amp.rnz.co.nz/article/de5d86a0-4ee4-4b08-a8ec-9e047606cecd`, opened with
  WebFetch, twice. It carries: a Chinese man killed and two other workers injured in an incident
  "in February" during construction of the Apia Park stadium; Leulua'ialii Olinda Woodroffe, a
  New Zealand-based Samoan lawyer, saying someone is trying to cover the incident up and that
  Qindao Construction Group Ltd hired her to investigate the death and the injuries; South Pacific
  Games chief executive Fonoti Manogiamanu Etuale saying police investigated thoroughly, that the
  company's general manager Hai Wang told him the lawyer was hired to help recover an insurance
  claim on a damaged beam that was being moved during the works when the fatal accident happened,
  and that "there has been no cover up of the death of the Chinese worker".
- **US embassy Wellington cable 000773 of 25 October 2007**, via Scoop
  (`https://www.scoop.co.nz/stories/WL0710/S00127.htm`). Confirms the Chinese low-interest loans and
  grants for the main Games venues and that the construction loans had since been forgiven. It does
  not mention Apia Park by name, the contractor, Chinese labour or any accident.
- **Samoa News**, `https://www.samoanews.com/node/87555`, "Chinese laborers try to get Apia Park up
  to scratch". Dated 13 April 2016 on the page, and about a different, later renovation by Shanghai
  Construction Company. No death, no injuries. Not used.
- **Digital Pasifik** items 539780 and 524798, both of which searches surfaced on this query. They
  turned out to be unrelated RNZ Pacific items (a Cook Islands stadium funding story with display
  date 22/03/2007, and a 2013 Samoa assault story). Not used, but they establish that Digital Pasifik
  carries RNZ Pacific items with display dates — a route to a date for the RNZ article that I did
  not manage to land, because no search surfaced our article there.

### Routes that failed, named as routes

- `curl` to `web.archive.org` — both the availability API and the CDX API — returns
  **"Blocked by egress policy"** from this container. So no Wayback copy could be checked by shell.
  This is a client-side block, not evidence that no snapshot exists.
- `https://web.archive.org/web/2008/http://www.pireport.org/...` through WebFetch — refused with
  **`PROVENANCE_REQUIRED`** (the URL had not come back in a search result, so it needed a permission
  answer that did not arrive). Do not read this as "no archive copy".
- `http://www.pireport.org/articles/2007/02/09/1-dead-2-hurt-apia-games-project-accident`, the
  article AidData cites as "1 DEAD, 2 HURT IN APIA GAMES PROJECT ACCIDENT" — **`PROVENANCE_REQUIRED`**
  through WebFetch. Its text is not held here. It is the one source that would have made this case
  `documented`, and it is AidData's own citation, so it existed.
- `https://www.rnz.co.nz/international/pacific-news/de5d86a0-...` (canonical host, uuid path) —
  **`PROVENANCE_REQUIRED`** on this attempt; round 37 recorded it as a 404. The AMP host is the
  working route and WebFetch is the working client, exactly as round 37's checker found.
- `https://www.airuniversity.af.edu/CASI/...AVIC...` — **client_error at the site**, nothing retrieved.
- `http://www.smedi.com/` — **`PROVENANCE_REQUIRED`**, because no search surfaced the firm's own site.
- Samoa Observer for 2007: searches restricted to `samoaobserver.ws`, `samoanews.com`,
  `pireport.org`, `rnz.co.nz` and `scoop.co.nz` returned only untitled Samoa Observer category URLs
  with no 2007 content; the Observer's online archive did not surface anything from February 2007.
  Recorded as not found, not as not existing.

### What decided the call

It is a case, and it is `contested`.

- **The forward rule, limb (b).** A specific documented harm to identifiable people: one worker dead,
  two injured, on the works the money paid for. Not a relocation count, not an "affected" figure.
- **The `killed` test.** RNZ Pacific ties the death to the project works by cause in its own words:
  the fatal accident happened while a beam was being moved during the construction of the stadium,
  and the firm holding the construction contract is named in the same report. AidData adds the
  mechanism — a fall from a machine being used to install beams. So `killed: 1`, not a
  `killed_note` with `killed: 0`.
- **Why `contested` and not `documented`.** Outside AidData the harm rests on one openable source.
  AidData alone carries the beam-installing machine, the second engineer's hospitalisation and the
  Samoan worker's injury; its cited Pacific Islands Report article is not held here; and no police,
  coroner's or labour-inspection finding is. BRIEF20's rule — core harm on a single source is
  `contested` — applies directly.
- **Dates.** The RNZ page carries no headline, no byline, no date and no programme name; asked
  twice, it gave only "in February". So its source entry carries `"year": null`, and the card says
  February 2007 is AidData's date and not the report's. Nothing was dated off the URL.
- **Name mismatch, printed rather than smoothed.** AidData's description names Qingjian Group,
  "known at the time as the Qingdao Construction Group Corporation"; its `Implementing Agencies`
  field names **Chongqing Construction Engineering Group**; RNZ spells it **Qindao Construction
  Group Ltd**. The card prints all three and says which firm employed the dead man is not settled.
- **Not claimed:** no name for the dead man (no source gives one), no day in February, no
  compensation, and no suppression — the cover-up allegation is a lawyer's claim about an accident
  inquiry, not force used against people who objected, so `suppression` is `""`.
- `ct: ["tied"]` rests on the record itself: the grant was spent through a contract with a Chinese
  company, and the Chinese ministry that provided the money also signed off the finished works.

## Job 2 — four company descriptions

Three written, one of them thin; **no blanks**. Each rests on a page opened with WebFetch.

1. **AVIC International Holding Corporation** — UK **Companies House** overseas-company record
   FC028179 (a government register). Gives the name exactly as the key has it, country of
   incorporation CHINA, home registry China's State Administration for Industry and Commerce, a
   Chaoyang, Beijing address, objects "International aviation, trade and logistic, real estate &
   hotels management", and the former name China National Aero-Technology Import & Export Corporation
   to 25 October 2010. **Not written:** state ownership, or that it is AVIC's trading arm — no page
   I opened says either of the company in the key, and the Hong Kong-listed AVIC International
   Holdings Limited is a different entity (fault 2). No incorporation date and no size figure,
   because the register gives none.

2. **Shanghai Municipal Engineering Design Institute (Group) Co., Ltd** — **ENR, 2017 Top Chinese
   Design Firms**. Its row: rank 12 (and 12 in 2016), "Shanghai Municipal Engineering Design
   Institute (Group) Co. Ltd., Shanghai", total design revenue $367.13 million. The sector is ENR's
   classification and the city is the table's location column, so neither is read off the name — the
   restatement test is met, barely. The revenue is written **undated**: the table attaches no fiscal
   year to it. **Not written:** owner, parent, founding year, staff count. The firm's own site could
   not be opened (route named above); Devex and DevelopmentAid profiles are barred by COMP.md, and
   the only other hits were a Shanghai planning-bureau PDF and a conference sponsor page.

3. **Athi Water Works Development Agency** — the agency's **own About page** (awwda.go.ke). States
   it was established under the Water Act 2016 "vide Legal Notice No. 28 of 26th April 2019", that it
   is one of nine water works development agencies "established under the Ministry of Water,
   Sanitation & Irrigation", its functions, and its three counties. So "X sits under Y" has a page
   that says it, and it is written as the agency's own account. **Not written:** the page's
   5,800.4 km2 and 9,320,287 population, which describe the territory and not the agency, and
   nothing about the predecessor Athi Water Services Board, because nothing I opened states the
   succession. The Auditor-General's report on the agency for the year ended 30 June 2021 is
   catalogued at the Kenyan parliament library (item 85d9f2ae-fddf-4186-998c-477e2a9bd5db) and its
   catalogue record carries no institutional description; the PDF itself was not read, and it is the
   obvious next route if a richer description is wanted.

4. **China Gezhouba Group Corporation (CGGC)** — the **Chinese government Belt and Road Portal**
   page "CGGC of Energy China", which names the company exactly as the key does. Dated chain: dam
   construction begun 30 December 1970, renamed the 330 Engineering Bureau 1974, parent group
   established 1994, Shanghai listing 1997, main businesses fully listed by share swap 2007, Energy
   China's 2021 acquisition and merger leaving it unlisted. Revenue RMB 115 billion is the figure the
   page attaches to 2020 in the same passage. **Not written:** the page's "national team", "global
   business card", "over 5,000 projects" and "100 world records" claims, and its 2016 "revenue
   exceeded RMB 100 billion" line, which it gives as a level sustained since rather than a year's
   figure. **Caution:** this page treats CGGC and the Shanghai-listed China Gezhouba Group Co., Ltd.
   as one story; the listing and delisting sentences are attributed to the page, not asserted on my
   own account.

### Case-data discrepancy noticed

On `karimenu-ii-dam-compensation`, the Athi Water role text puts the agency "under the Ministry of
Water and Sanitation"; the agency's own page gives the ministry as Water, Sanitation and Irrigation.
Nothing changed. The agency under this name was created in 2019, after the 2017 contract, which the
card already handles by noting AidData names it in its earlier form.

## Single weakest entry

**Shanghai Municipal Engineering Design Institute (Group) Co., Ltd.** It rests on one row of one
trade-press ranking table — sector, city and an undated revenue figure, with no ownership and no
founding date. It is honest and it is thin, and it is the entry a checker should hit first.
