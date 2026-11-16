# Round 37, Batch C — writer's report

19 financings (Antigua and Barbuda, Bolivia x2, DPR Korea, Ethiopia, Grenada, Guyana x3,
Montenegro, North Macedonia, Peru, Samoa, Serbia, Uganda x2, Venezuela, Zambia x2).

**Outcome: 4 new cases, 2 extends, 13 drops.**

## New cases

| financing | case id | what decided it |
|---|---|---|
| G025 Zambia (rec 2234) | `chambishi-bgrimm-explosives-blast` | VOA (AFP/AP/Reuters): "a blast killed at least 51 people" at the Chinese-owned BGRIMM explosives factory on the grounds of the Chambishi copper mine; Mail & Guardian quotes the mines minister on the owners' failure to keep records of casual workers; Dow Jones Newswires (Oct 2005) describes "the graves of 49 workers killed in April". Deaths at a plant owned by a Chinese state group, not a disaster. |
| G591 Ethiopia (recs 92137, 92164) | `neshe-dam-compensation-oromia` | Müller-Mahn and Gebreyes, *Land* 8(9):135, read from the PDF: "Many respondents confirmed that compensation for land that was taken for the new dam was not paid as originally agreed"; approximately 1,200 households resettled for Neshe; families abandoned the new houses; almost 2,000 ha of the out-grower scheme left uncultivated after the sugar company stopped paying rent. |
| G116 Guyana (rec 36574) | `cjia-timehri-pit-collapse-death` | Liu Li, 23, an engineer for CHEC, buried and killed when a humus pit caved in on 17 Sept 2015; Zhang Yixun hospitalised (police via Demerara Waves; Stabroek News). Labour department preliminary report (Guyana Chronicle, 5 Oct 2015): accident unreported, both men had no prior experience, "no proof of such financial assistance was seen" on compensation to the family, no overtime paid to local workers. |
| G563 Antigua and Barbuda (recs 89551, 92146-8) | `booby-alley-housing-clearance` | Police statement, 5 Apr 2023, and Antigua News, 6-7 Apr 2023: Joel O'Marde shot with a rubber bullet and taken into custody while a High Court bailiff enforced an eviction writ at Booby Alley, then charged and bailed. Pointe Xpress, 5 Apr 2023: "More than two hundred and forty persons have been relocated", plus a $1,000 contempt fine. Site cleared by 12 Oct 2023. |

## Extends

| financing | case extended | what the extend adds |
|---|---|---|
| G065 Uganda (recs 30919, 36211) | `karuma-dam-evictions-awoo` | Both Eximbank agreements with amounts, dates, rates and disbursement record, and the record ids. Worker safety: Rogers Twine killed on 23 September by debris from a blast ordered without alerting him; eight deaths at the site before June of that year per a UEGCL presentation; three named workers hospitalised unrecorded; Energy Infratech's letters on blasting non-compliance and "coached reporting of witnesses" (The Independent, 12 Dec 2016); the 2018 truck crash with disputed toll (Nile Post). |
| G247 Peru (8 rows: 55426, 55427, 98774-6, 98780-1, 98783) | `las-bambas-2015` | Per-bank shares of the one $5.988bn facility (CDB ~50%, ICBC ~30%, Bank of China and Eximbank ~10% each) with each bank's record id, the 18-year maturity, $4.119bn drawn, the several guarantees, and the separate $969m acquisition facility's four records. Eight rows, one syndicate, one card. |

**Two numeric changes `fields_add` cannot make, for the lead to apply by hand:**
- `karuma-dam-evictions-awoo`: `killed` should become **1** (Rogers Twine; the project supervisor's own
  letters put the cause on blasting done without warning him). The eight site deaths stay uncounted in
  `killed_note` because no cause is given for them.
- Nothing numeric for `las-bambas-2015`.

## Drops

| financing | reason |
|---|---|
| G273 Zambia, Ndola stadium loan | Flag fired on the sentence naming the stadium after a president who died in 2008. Nothing adverse recorded in the whole record: no relocation, no accident, no complaint. |
| G127 Venezuela, CDB $1bn PxF for CVG | 15,700 characters of a failed iron-ore prepayment and a corruption prosecution. The arrests are of the state company's own president and managers for diverting $1.8 million, not of anyone harmed by or objecting to the project. No count of people relocated and no specific harm to identifiable people. |
| G625 Montenegro, ICBC in the Možura syndicate | The only death in the record is Daphne Caruana Galizia's murder in Malta in October 2017. No source ties her killing to this project; Reuters' finding is that 17 Black made EUR 4.6 million on the Možura equity sale, and the record says she did not know who owned 17 Black. Corruption without documented harm to identifiable people. |
| G316 Uganda, four industrial park substations | The compensation sentence is about delays over wetland ownership that let a claimant build a printery on a tower spot — the claimant's gain, not a harm to him. RAP "60% complete (427 out of 707 actions)" is a progress count, not a relocation count. No count of households moved and no documented harm to identifiable people. Search of Ugandan press on Luzira / Port Bell Market compensation returned other UETCL lines, not this one. |
| G408 Samoa, Apia Park stadium grant | A Chinese engineer killed falling from a beam-installing machine in February 2007, a second engineer hospitalised, a Samoan worker injured — all of it only in AidData's own record. Two searches and an RNZ fetch for March-April 2007 Samoa coverage found nothing outside it. Kept as a lead: a case here needs 2007 Samoa Observer archives. |
| G245 Grenada, St Mark's flood mitigation | The deaths are the rainy-season flooding's, which the works were built to stop. The harm is the disaster's. |
| G025-class relief rows: G125 Bolivia dengue cash | $300,000 after the January 2009 dengue epidemic: 18 deaths are the epidemic's, not the money's. |
| G559 Guyana, China CDC help with histoplasmosis | The 2 deaths and 27 sick are the April 2019 outbreak at the Matthew's Ridge mine; the money is the medical response to it. |
| G518 Bolivia, security equipment donation | Three police officers killed by a bombing in March 2004, before and unconnected to the donation. |
| G173 DPR Korea, crude oil donation | The death in the record is Kim Jong Il's. |
| G117 Guyana, medical training MoU | The flag fired on an objective to cut maternal deaths by 75%. Nothing adverse. |
| G185 North Macedonia, 23 school buses | The deaths are of 19 preschoolers in a crash in China two weeks before the donation, and 35 injured in Liaoning the day after. Neither is in North Macedonia and neither involves this money. |
| G186 Serbia, RMB 20m interest-free loan | The three deaths and 27 injuries are from the NATO strike on the Chinese embassy in 1999. Not harm from the financing. |

## My two weakest entries

1. **`neshe-dam-compensation-oromia`.** Everything that earns the case comes from one 2019 journal
   article, and inside that article the figures come from interviews, not records: "Exact figures are
   difficult to find, but… approximately 1200 in the case of the Neshe dam." So `displaced: 1200` is an
   interview estimate in a peer-reviewed paper, which is weaker than any count the map's Bank cases
   carry. The paper also quotes people displaced by the *Fincha* and *Amerti* dams — earlier stages, one
   financed by the European Economic Community — and those quotes are kept off the card on purpose;
   a checker should verify none leaked in. Loan size is given two ways (US$137m construction cost in the
   paper; $147.3m contract and $125.2m of loans in AidData) and both are printed. Marked `contested`.
2. **`booby-alley-housing-clearance`.** The relocation count, the contempt fine and the signed agreement
   all come from one statement by the project's own mobilisation manager in Pointe Xpress, which is
   government-owned, so the number and the "free of charge" framing are the project's account of itself.
   No court record for the writ, the fine or the charges was located; the arrest rests on a police
   statement and on Antigua News. What residents received for their chattel houses is nowhere in the
   sources. The two dates for the 150-unit agreement (August 2021 in the Observer, 18 August 2022 in
   Antigua News) are both printed because neither could be resolved.

## Figures where sources disagree (all printed on the cards)

- Chambishi dead: 51 (police via VOA) / "over 50" (mines minister via Mail & Guardian) / 49 graves
  (Dow Jones Newswires, 12 Oct 2005).
- Neshe cost: US$137m construction cost (Land 8(9):135) / $147.3m contract and ~$125.205m of loans
  (AidData). Capacity: 95 MW and 38 m high (Land) / 97 MW (AidData).
- CJIA collapse time: about 10.40 am (public infrastructure ministry via Stabroek News) / about
  12.35 pm (police via Demerara Waves).
- Karuma 2018 truck crash: at least three dead (The East African, via Nile Post) / several injured and
  no fatalities (the dam's management).
- Booby Alley 150-unit agreement: August 2021 (Antigua Observer) / 18 August 2022 (Antigua News).

## Routes: what opened and what did not

Opened and read: voanews.com, mg.co.za, minesandcommunities.org (Dow Jones reprint),
stabroeknews.com (non-print article URL), demerarawaves.com, guyanachronicle.com,
antiguaobserver.com, antigua.news, pointville.ag, rnz.co.nz, OpenStreetMap API
(way/251021938, way/845221791, way/581161502, way/1081942197, relation/11166939).

Routes that failed, by route:
- `https://www.mdpi.com/2073-445X/8/9/135` and `.../pdf` → 403 from the Akamai edge. The same paper
  downloaded fine from `https://mdpi-res.com/d_attachment/land/land-08-00135/article_deploy/land-08-00135.pdf`
  (3.0 MB) and was read with `pdftotext -layout`. MDPI is not blocked; its www host refuses curl.
- `stabroeknews.com/.../print` paths → "Page not found"; `www.stabroeknews.com/.../print/` → 403
  "requires an authentication". The plain article path worked. Later in the session the whole site
  answered "Temporarily Offline | Webservice currently unavailable", so the 25 Sept and 3 Oct 2015
  follow-ups were not read.
- `miningnews.net` (two article paths) → Cloudflare JavaScript interstitial.
- `theeastafrican.co.ke` article path → Cloudflare 1020 block page.
- `kaieteurnewsonline.com/2015/09/18/...` → HTTP 429 rate limit, not a block.
- `amp.rnz.co.nz/article/...` → proxy CONNECT tunnel failed, 502. The canonical `www.rnz.co.nz` path
  worked.

## Cache

Documents are at `/tmp/r37c/`: `land.pdf` and `land.txt` (the Neshe field study),
`chec_probe.html` (the Guyana labour department probe as reported), plus the OSM JSON used for the
four coordinates (`neshe_way.json`, `bg.json`, `bb.json`, `cjf.json`). Nothing is cached under the repo.

## For the next round

- The eight-row Peruvian syndicate is one facility and the rows split by bank share; the shares are in
  record 55426's description, not in each bank's own row. Expect the same shape wherever AidData
  says "Linked to Project ID#".
- Three financings in this batch were relief or response money whose flag fired on the harm the money
  answered (Bolivia dengue, Guyana histoplasmosis, Grenada flooding) even though they do not carry
  `r36_relief`. The relief trap is wider than that field.
- Two financings flagged "death with a cause" on a death in **China** or in a **third country**
  (the Liaoning school-bus crash behind the North Macedonia bus grant; Caruana Galizia's murder in
  Malta behind the Montenegro wind park). A country-of-death check would clear both cheaply.
- Samoa's Apia Park death (record 64861) is a real forward-rule fact with no source outside AidData
  reachable from here; a round with access to 2007 Pacific newspaper archives should revisit it.
