# Round 37, Batch A — writer's report

20 financings (Bangladesh, Indonesia, Iraq, Kazakhstan, Laos, Myanmar, Nepal, Pakistan, Vietnam).

**Result: 2 new cases, 4 extends, 2 already_on_map, 12 drops.** 9 WebSearch calls used; everything
else was `curl` plus local text extraction.

## New cases (2)

### 1. `padma-rail-link-gopibagh-evictions` — Padma Bridge Rail Link (G212, AidData 52663)
What decided it: AidData carries only a prospective figure — construction "is expected to impact the
living accommodations of 7,705 people" — which is an affected count and would be a drop on its own.
Two newspapers carry the outcome. The Business Standard (7 Oct 2019): the houses of the Gopibagh
Railway Colony "were demolished on January 22, 2019 as part of the Padma bridge rail link project.
Since then 108 Harijan families have been living under the open sky." The Daily Star (28 Apr 2023):
"In the first phase in 2019, 112 families were evicted... to date, no initiative has been taken to
rehabilitate them", 27 more families in December 2022, and around 55 houses demolished with 35
partly demolished. The harm is on the thing the credit financed: the colony stands in the path of
the Kamalapur-to-Jashore line and its depots and overpasses, and the credit financed 85% of the CREC
contract for that line.

### 2. `thar-block-1-varvai-tilvai-land` — Thar Coal Block-I (G230, AidData 53674 / 92627 / 92628)
AidData carries only "an estimated 600 families will be displaced". The forward rule is met on limb
(b) by the People's Map of Global China profile written by the Rural Development Policy Institute:
compensation of 180,000 rupees an acre paid only for surveyed land, nothing for leased (Yaksaala)
or common grazing (Gowchar) land, house compensation of 4.2 million rupees per family only part
paid, families at Bhave Jo Tar unable to leave because of it, Khario Ghulam Shah left with no land
to graze, Kohli Para fenced on three sides and not bought at all. Corroborated in direction by The
Express Tribune (2 Aug 2022): half the house cost paid, land acquisition incomplete, 660 acres at
Naqboli outstanding. The company's own press release (Business Recorder, 19 Nov 2021) says 450
families (266 Wervai, 184 Tilwayo) each got 4.25 million rupees and most had started moving in.
Both accounts are on the card.

## Extends (4)

- **`formosa-ha-tinh-marine-disaster`** (G633 + G634 — one plant, two financings). The case carried
  no lender but Formosa Plastics. Adds Bank of China (US$425m of the US$1bn tranche of a US$2.5bn
  2016 syndicated loan) and China Eximbank (RMB 400m for the two blast furnaces, built by MCC), plus
  `lk: cn` and `cp: aiddata`. **Deliberately not added: AidData attributes the 24 March 2015
  scaffolding collapse ("killing 16 construction workers and injuring 27") to "the project site".
  Saigoneer, citing Tuoi Tre, places the collapse at Son Duong Port, a project owned by Samsung C&T
  inside the Formosa industrial park, on the evening of 25 March 2015; wire reports give 13, 14 and
  16 dead. It is neither the steel plant's own works nor the blast furnaces the Chinese loans paid
  for, and it predates both loans. Next round should not pick it up from AidData.**
- **`jakarta-bandung-hsr-construction`** (G349). Adds the tranche split the card lacked: US$2.3805bn
  at 2% and an RMB tranche worth US$1.587bn at 3.46%, 40-year maturity, 10-year grace, no sovereign
  guarantee, first disbursement US$170m in May 2018 (AidData 61320 and 61321).
- **`upper-paunglaung-dam`** (G105). Card already had the Eximbank seller's credit and AidData 35828.
  Adds the underlying contract: US$80m, signed 14 February 2006, and that AidData's credit figure is
  an 85%-of-contract estimate, not a reported face value.
- **`thar-block-ii-sehnri-dars-gorano`** — surfaced while checking whether the Dodo Bheel death
  belonged to Block-1. It does not: SECMC's own response says "the incident that occurred in Thar
  Block II where a third-party contract worker - Mr. Dodo Bheel passed away", and HRCP says he was
  tortured by Sindh Engro Coal Mining Company security guards after 14 days' detention over scrap
  theft at Block-II. Adds the death, the torture allegation, the police baton charge and teargassing
  of the sit-in (HRCP; Aaj English), five guards booked, bail refused to the main accused on 28
  August 2021, 10 million rupees announced for the family, and the fact that of ICBC, CDB, CCB, CMEC,
  SPIC and SPIM, none responded to the Resource Centre and only SECMC did.
  **Numeric change needed by hand: this case has `killed: 0` and `killed_note: "No deaths reported."`
  Both are now wrong. `killed` should be 1 (a death a document ties to guards acting for the mine
  company) and the existing note text replaced, not appended to. `fields_add` cannot do either.**

## already_on_map (2)

- **G214 Banskhali** → `banskhali-coal-plant`. All four AidData rows (52792, 98804, 98814, 98815) are
  one US$1.782bn buyer's credit; the card already names all five Chinese banks, the Sinosure cover,
  the 2021 police shootings, the Digital Security Act arrest and AidData record 52792. Nothing added.
- **G600 Java 9 and 10** → `suralaya-java-9-10`. Card already carries Bank of China in the 11-bank
  US$2.6bn syndicate with AidData 92603 and the CAO findings. AidData's extra detail (15.25-year
  maturity, pledge of PT Barito Wahana Tenaga shares, Greenpeace's modelled 4,700 lifetime premature
  deaths) duplicates or sits beside what the card has from CREA and CAO; left alone.

## Drops (12), each with what decided it

1. **G351 Cikampek-Palimanan toll road (ICBC Indonesia, IDR 366bn of a 22-bank syndicate).** The only
   people-figures are affected counts: "some 5,617 Project Affected People (PAP), mainly due to land
   acquisition" and 1,527 PAPs registered for a livelihood restoration programme with an 87%
   satisfaction result against a 75% target. The deaths are "30 car accidents" in the ten days after
   the road opened — road-accident deaths on a finished road, which the `killed` rule excludes. No
   count relocated and no recorded compensation shortfall. **Closest call after Patuakhali.**
2. **G556 Nam Dinh 1 (six AidData rows, one US$1.89bn syndicate).** "roughly 300 households will need
   to relocated and receive compensation" — prospective. BankTrack's profile (last updated 13 Aug
   2020, marked no longer maintained) says "about 300 households are being relocated and will only
   receive minimal compensation" with no source and no count. AidData: as of July 2022 no evidence
   construction had commenced, and ACWA Power wrote off SAR 80.9m of project costs. Nothing moved.
3. **G267 Patuakhali 1320 MW (RNPL / NORINCO, US$1.77bn, China Eximbank + Bank of China).** AidData:
   "expected to displace 350 families". The Daily Star (9 Jan 2021) records 915.74 acres acquired in
   Londa, Dhankhali and Nishanbaria for Tk164.61 crore and Tk869 crore budgeted for "land acquisition
   and development and rehabilitation of 281 families" — the project's own plan figure, from its
   executive director. No document counts families moved and none records compensation withheld or a
   forced eviction. **This is my closest call; see weakest entries below.** Note for the next round:
   this is a different plant from `payra-1320mw-coal-bcpcl` (BCPCL at Dhankhali) and from the
   Ashuganj/CEEC plant, though all three sit in Kalapara. The LNSP "30,000 families displaced"
   figure (The Daily Star, 11 May 2019) covers 15 projects across three unions, not this plant.
4. **G386 Upper Yeywa-Shwesaryan transmission line (US$101.98m PBC, 2013).** The relocation figure in
   the record — "Two villages with a total of 143 households and 486 inhabitants will be affected by
   the reservoir and need relocation" — is prospective and belongs to the Upper Yeywa dam, not to the
   line and substation this credit financed. AidData states plainly that Shan groups' claim that
   China Eximbank finances the dam is not independently confirmed. Harm on a different asset, in the
   shape of round 19's Burkina Faso finding.
5. **G140 Pak Lay hydropower (Laos).** The 5,010 to be resettled is a design figure and AidData says
   it has found no evidence any China Eximbank loan agreement was ever finalised; the PowerChina /
   CEIEC proposal "petered out". Fails test 1.
6. **G437 Lompatan Harimau dam (Indonesia).** AidData: "AidData has not identified that China
   Eximbank ever issued a loan for this project." The 15,000 is what the Rokan Dam Rejection
   Alliance said the dam "allegedly would displace". No lender, no built project, no actual harm.
7. **G648 Bank of China Rp200m to the Indonesian Red Cross for Sentani flood victims.** Relief: the
   harm is the disaster's, not the money's. The deaths in the record are the 16 March 2019 flood's.
8. **G234 China's US$1m flood and landslide aid to Nepal.** Relief: the "more than 110 people killed
   by landslides and flooding" are the disaster's dead.
9. **G546 PLA "Peace Train-2019" medical assistance (Laos).** Relief in the same shape: the 13 deaths
   and 29 injuries are a tourist bus crash 40 km from Luang Prabang on 19 August 2019, which the PLA
   medical teams responded to.
10. **G171 Chinese Embassy donates office and educational equipment to Iraq's Ministry of Foreign
    Affairs.** The casualties in the record are the 19 August 2009 truck bombing's; the donation came
    after it. Relief in substance, and nothing adverse is recorded.
11. **G484 CNPC AktobeMunaiGas funds a museum and monument to Aliya Moldagulova (Kazakhstan).** The
    "death" flag fires on a Soviet sniper killed in action in 1944. Nothing adverse is recorded.
12. **G555 China donates equipment to Sindh Police (Pakistan).** Three cars, fifty walkie-talkies,
    printers and monitoring equipment. The deaths in the record are two Sindh police officers killed
    defending the Chinese consulate in a November 2018 attack, eleven months earlier. No harm to
    anyone is recorded, and nothing ties the equipment to a later act.

## My own two weakest entries

1. **`thar-block-1-varvai-tilvai-land`.** The whole harm finding rests on one document, the People's
   Map of Global China profile, and the company says the opposite about the same families. Marked
   `contested` for exactly that. Two further soft spots a checker should hit: (a) the lender shares
   are AidData's equal-split assumption for CDB and China Eximbank, with only ICBC's US$358.5m
   actually reported, and no source names a lead arranger, so `lenders[0]` is CDB only because
   AidData's primary record is CDB's; (b) the loan proceeds financed the two Shanghai Electric EPC
   contracts, i.e. mainly the power plant, while most of the land harm is in the mine's villages —
   Bhave Jo Tar and Kohli Para are the two that sit against the plant. The card says which money
   paid for what, but a checker may judge the mine-side harm as sitting on ICBC's separate
   US$1 billion mine loan rather than on this syndicate.
2. **The Patuakhali (RNPL) drop.** I may have dropped a keeper. 915.74 acres were acquired from three
   named villages and the project budgeted for rehabilitating 281 families, which is land taken from
   identifiable people; what is missing is any document recording that anyone was moved, paid late,
   paid short or evicted. The RPCL social impact assessment is the document that would settle it and
   I could not open it (see routes below). If a checker can read that PDF, this row should be looked
   at again before the round closes.

## Figures where sources disagree

- Padma rail link, families evicted in 2019: **112** (The Daily Star, 28 Apr 2023) against **108**
  (The Business Standard, 7 Oct 2019). Both are on the card.
- Thar Block-I, whether people had moved by late 2021: company says most of 450 families had
  started moving into new houses (Business Recorder, 19 Nov 2021); the People's Map profile updated
  7 Dec 2021 says physical displacement had not yet taken place. Both are on the card.
- Thar Block-I project cost: **US$1.9122 billion** (AidData) against **US$2.5 billion** (People's Map,
  split US$1.44bn plant / US$1.08bn mine). Both are on the card.
- Thar Block-I block size: **155 km2** (the ESIA for Sinhar Vikian Varvai Block-I) against **122 km2**
  (NS Energy, via the People's Map). Both are on the card.
- Formosa 2015 scaffolding collapse deaths: **16** (Saigoneer citing Tuoi Tre; Australia Asia Worker
  Links; AidData) against **13** and **14** in wire reports. Not used on any card, for the reason above.

## Routes that failed, with the exact failure

- `https://rpcl.portal.gov.bd/.../SIA Report (Volume-IV).pdf` — `curl` aborted with "SSL certificate
  problem: self-signed certificate", both with the default store and with `--cacert
  ~/.ccr/ca-bundle.crt`. The host serves a self-signed certificate. Verification was not disabled.
  This is one path on one host, not a block on Bangladeshi government sites.
- `dawn.com` (articles 1632710, 1633476, 1634204, 1646493) and `upi.com`, `gem.wiki` — returned the
  Cloudflare interstitial "Just a moment... Enable JavaScript and cookies to continue" to `curl`
  with a desktop user agent. A browser tool would likely get through. Nothing from these pages is
  cited; the Dodo Bheel facts came from `business-humanrights.org`, `arynews.tv` and
  `english.aaj.tv`, all of which served over `curl`.
- `business-humanrights.org` returned **HTTP 429 Too Many Requests** on the third fetch in quick
  succession, then served normally after a 15-20 second pause. Rate limit, not a refusal.
- `tuoitrenews.vn` returned an empty body to `curl`; the same Tuoi Tre reporting was read via
  Saigoneer, which cites it.
- `acjce.com/.../Research-Study-Coal-rush...pdf` returned HTTP 200 with an HTML body, not a PDF, so
  the two Rural Development Policy Institute reports were not read and are not cited.

## Document cache

No PDFs were obtained, so there is no PDF cache for this batch. Working HTML and extracted text sit
in `/tmp` (`pm.html` People's Map profile, `bh.html` and `secmc.html` and `nchr.html` Resource
Centre pages, `br.html` Business Recorder, `ds2.html` and `ts.html` Daily Star, `crec.html`), and
the per-financing AidData full texts are in `/tmp/ft/NN_Gxxx.txt`. `/tmp` is not durable; everything
cited is a live URL in `sources`.

## For the next round

- The Dodo Bheel death is the single strongest piece of evidence found in this batch and it belongs
  to a case already on the map, Thar Block II. The Resource Centre's timeline shows the lenders
  themselves — ICBC, CDB, CCB — were asked to respond and did not, which is the sort of lender-side
  silence worth capturing as a pattern across the Chinese tranche.
- AidData's descriptions repeat an incident from a neighbouring project as if it were the financed
  project's own, twice in this batch: the Samsung C&T port scaffolding collapse written into both
  Formosa records, and the Upper Yeywa dam's reservoir relocation figure written into the record for
  a transmission line. Both would have produced a wrong card. Check whose asset the incident sits on
  before trusting an AidData sentence about it.
- Three Kalapara coal plants (BCPCL Payra, RPCL-NORINCO, Ashuganj-CEEC) share a district, a
  capacity and partly a village name. Only the first is on the map. Any future row from that area
  needs matching on the joint-venture company, not the place.
