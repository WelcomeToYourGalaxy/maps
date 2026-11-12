# r26f_textfix_11 — fact-check log

Checked 2026-11-11. Every figure below was read on a page or file I opened myself in this
session. Where a document was not reachable, the failure mode is named exactly.

Verdicts: KEEP 5 (3, 7, 8, 10, 11) · CORRECT 6 (1, 2, 4, 5, 6, 9) · BLANK 0

---

## 1. tata-mundra — CORRECT

**Opened:** `https://cercind.gov.in/2025/orders/168-MP-2019.pdf` (served, read in full by
fetch); `https://disclosures.ifc.org/project-detail/SPI/25797/tata-ultra-mega` (served).

**Verified**
- Order date, petitioner, petition number: "Order dated 20th June, 2025", petitioner
  Coastal Gujarat Power Limited (CGPL), now Tata Power Company Limited, Petition
  No. 168/MP/2019 (On remand). ✓
- 4,150 MW installed, five × 830 MW: order para 1, the Commission's own description —
  "with an installed capacity of 4,150 MW (5×830 MW)." ✓
- 4,000 MW net, five × 800 MW, after the motor-driven boiler feed pump — "The net plant
  capacity is 4000 MW (5 units of 800 MW each) after accounting for the Motor Driven
  Boiler Feed Pump." ✓ **but this sentence sits in para 6, which the order labels the
  Petitioner's affidavit of 19.7.2024, not a finding of the Commission.**
- "net capacity remains 4,000 MW despite each unit being rated 830 MW" — "Despite each
  unit being rated for 830 MW, the net plant capacity remains 4,000 MW" ✓ **in para 17,
  which the order labels a summary of submissions.**
- PPA basis: supported by the Commission's own analysis — para 22, "must be aligned with
  the contracted power output under the Power Purchase Agreement (PPA)," "which is limited
  to 4000 MW"; para 14, expenditure "shall be done corresponding to installed capacity of
  4150 MW, but the Respondents shall be liable to pay the expenses on pro-rata basis
  corresponding to 4000 MW in terms of PPA." ✓
- IFC disclosure uses 4,000 MW: SPI 25797 — "Coastal Gujarat Power Limited (CGPL or the
  company) will build, own and operate a 4,000MW (5 units of 800 MW each)". 4150 and 830
  do not appear on that page. ✓

**What is wrong.** The entry says the Commission "gives … the net plant capacity as
4,000 MW … adding that the net capacity remains 4,000 MW despite each unit being rated
830 MW." Both of those sentences are the petitioner's, recorded in the order. The order's
own voice gives 4,150 MW installed (para 1) and the 4,150-for-cost / 4,000-for-PPA-liability
holding (paras 14, 22, 23). Attributing CGPL's affidavit to the regulator is the kind of
upgrade this standard forbids.

**Replacement for `companies[0].desc` → `new`:**

> that built and ran the supercritical coal-fired Mundra Ultra Mega Power Project in Gujarat. The plant's two capacity figures are different quantities, and a regulator's order sets both out: the Central Electricity Regulatory Commission, in its order of 20 June 2025 on CGPL's own petition 168/MP/2019, describes the project as having "an installed capacity of 4,150 MW (5×830 MW)", and records CGPL's affidavit that "[t]he net plant capacity is 4000 MW (5 units of 800 MW each) after accounting for the Motor Driven Boiler Feed Pump" and that "[d]espite each unit being rated for 830 MW, the net plant capacity remains 4,000 MW". The Commission's own finding is that the expenditure is computed on the 4,150 MW installed capacity but that the buyers' liability is limited to 4,000 MW, because the power purchase agreement "is limited to 4000 MW". The 4,000 MW figure is the one the IFC's disclosure uses.

**Weak point to keep in mind.** The contracted ex-bus output is lower again: the order
records 3,800 MW to the procurers (paras 8, 14). Any later sentence that treats 4,000 MW
as "what the plant sells" would be wrong.

---

## 2. shuakhevi-adjaristsqali — CORRECT

**Opened, all served:** IFC SII, ESRS and ED for project 33435 (the three URLs in
`sources_add`); ADB news release
`https://www.adb.org/news/ifc-adb-ebrd-tata-power-and-clean-energy-help-georgia-achieve-energy-self-sufficiency`;
ADB monitoring report `…/47919/47919-014-smr-en_1.pdf`; ADB semi-annual E&S monitoring
report (Jul–Dec 2016) `…/47919/47919-014-esmr-en_16.pdf`; ADB resettlement plan
`…/47919-014-rp.pdf`; EBRD `…/45335sep.pdf`.

**Verified**
- SII: "the construction and operation of the 184 MW Shuakhevi hydropower project",
  "consisting of 2 HPP schemes: the 178 MW Shuakhevi HPP and the 6 MW Skhalta HPP". 185 MW
  does not appear on that page. ✓
- ESRS, both figures: "The proposed investment is a 184 MW hydropower scheme comprised of
  two dams" and, elsewhere, "namely the 185 MW Shuakhevi scheme, the 150 MW Koromkheti
  scheme and the 65 MW Khertvisi scheme". ✓
- Early Disclosure, date and figure: "Early Disclosure Date: May 24, 2013"; "The project
  consists of financing the 185 MW hydro power plant in Adjaritskali, southwest Georgia";
  "IFC is considering to invest in the first HPP (Shuakhevi 185 MW)". ✓
- ADB 187 MW, from ADB's own release of 19 March 2015: "The project will develop the
  187-megawatt Shuakhevi hydropower scheme," "consisting of the Shuakhevi and Skhalta
  hydropower plants located in the Adjara region, in southwest Georgia." ✓

**Searched for a reconciling document, as instructed, and found none — but found two
things that break the entry.**
1. ADB's monitoring report gives 187 MW with its own parts: "This 187-megawatt (MW)
   hydropower scheme includes a 178 MW Shuakhevi HPP on the Adjaristsqali River" "and a
   9-MW Skhalta HPP on the Skhalta River." 178 + 9 = 187. **So 184 MW is not "the only
   figure that adds up from its parts"** — that clause is false. ADB's Jul–Dec 2016 E&S
   monitoring report corroborates the 9 MW: the Skhalta powerhouse is "three units of 3 MW
   each".
2. ADB's Jul–Dec 2016 report **does label one figure**: "Gross electricity generation
   capacity (MW): 187 MW", with "Net electricity generation capacity (MW): will be updated
   on COD". That is a label on 187 MW, not a reconciliation of 184/185/187 — no document
   says that 184 or 185 is the net figure — but the flat "No document reconciles them"
   should not stand unqualified next to it.
3. There is also a fifth figure: EBRD's study gives "The total installed capacity of the
   Shuakhevi scheme will be 185 MW" with "A small-capacity HPP (10MW) … at Skhalta"; ADB's
   resettlement plan gives a 175 MW main HPP and a Skhalta of "10 MW" in the text and
   "9.8 MW" in its Table 1.1, with no total reconciliation stated.

**Replacement for `companies[0].desc` → `new`:**

> starting with the Shuakhevi and Skhalta plants. The sizes given for it do not agree, and the disagreement starts inside the IFC's own disclosure for project 33435: its Summary of Investment Information calls the financed project 184 MW and says it consists of the 178 MW Shuakhevi plant and the 6 MW Skhalta plant; its Environmental and Social Review Summary says 184 MW in one place and 185 MW in another; its Early Disclosure of 24 May 2013 says 185 MW. The Asian Development Bank's press release of 19 March 2015 says 187 MW, and ADB's monitoring reports break that down as a 178 MW Shuakhevi plant plus a 9 MW Skhalta plant, labelling the 187 MW a gross figure with the net figure left to be filled in at commercial operation. The EBRD's environmental study gives the scheme as 185 MW with a 10 MW Skhalta plant. The plants that differ between the accounts are Skhalta, at 6, 9 or 10 MW, and no document says which of 184, 185 and 187 MW the other figures are.

Also fix `companies[0].role` → `new`, which says "four different ways": the IFC's own
documents give three (184, 184/185, 185); the four-way count only works once ADB is added,
and five sources are now in play. Suggested: "Built and operates the Shuakhevi plant, whose
size its funders state four different ways".

---

## 3. antea-cement-kruja — KEEP

**Opened, both served:** `https://disclosures.ifc.org/project-detail/SPI/25886/antea-albania`
and `…/ESRS/25886/antea-albania`. I read both pages in full (rendered fetch plus a raw
pull of each: 11,631 and 43,956 characters of text).

**Verified**
- SPI, date and wording: "Date SPI Disclosed: Mar 26, 2008"; "with a production capacity of
  3300 tons per day clinker" "(or 1,400,000tons per year cement)" — including the missing
  space in "1,400,000tons". ✓
- ESRS, both: "proposes to construct a 3,300 tpd clinker production facility" and "capable
  of producing a total of 1.50 Million tons cement per year". ✓ So both documents are about
  cement and both describe the same 3,300 tpd clinker line. ✓
- Absence claim checked across the full text of both pages: neither contains "design
  capacity", "nameplate", "permitted capacity", "rated capacity" or "installed capacity"
  (zero hits for each on both). The SPI's only qualifier is "production capacity". ✓
- "Titan also gives 1.5 million tonnes" — now sourced, and expressly about cement: Titan's
  announcement via the Athens Exchange, 26 July 2007, "Cement capacity will be of a
  1.5-million-ton-per-annum". Titan's own newsroom page of 13/09/2010 says "The plant's
  total output is 1,5 m. tons per year" without saying cement or clinker. **Add the Athens
  Exchange announcement to `sources_add`; the entry currently asserts the Titan figure with
  nothing behind it.**

**Weak points.** (a) The ESRS's PS3 section writes the figure once as "a production of up
to 1.50 million tons of cement per year" — "up to" is a ceiling, and a hostile reader could
call that a design maximum. It is still not one of the four labels, and no document says it
is, so the entry's logic holds; but the sentence should not be stretched further than
"neither calls its figure design, nameplate, permitted or achieved". (b) Titan's 1.5 Mt
predates the IFC's 1.4 Mt by eight months, which is suggestive of a revision but is not
stated anywhere.

---

## 4. sahiwal-coal-plant-qadirabad — CORRECT (substantially)

**Opened, all served:** `https://www.pacra.com/finalPr/IjEwNDI4Ig==`;
`https://china.aiddata.org/projects/52659/` (raw HTML pulled and parsed, including all nine
staff comments and the full 65-item source list); GEM ownership API
`/entities/E100002007872`, `/owners`, `/owned`, `/ownership/graph`,
`/assets/L100000103133_G100000108714`; GEM wiki `Sahiwal_power_station`; NEPRA's generation
licence application bundle (`Generation License App of Hunaneg Shdong RUYI.pdf`, 385 pages,
838,498 characters of extracted text, read by grep over the whole file); NEPRA's upfront
coal tariff determination (`TRF-308 HUANENG UPFRONT COAL DETERMINATION 31-03-2015`,
19 pages); NEPRA's 2017 licence modification (231 pages).

**Verified**
- PACRA wording, exactly as quoted: "It is a wholly owned subsidiary of Huaneng Shandong
  Ruyi (Hong Kong) Energy Limited, a company incorporated in Hong Kong." ✓ **But the report
  is dated 22-Jul-22, not 2024 as `sources_add` says.** PACRA states no percentage anywhere.
- AidData 52659 does give the split: "a joint venture of Huaneng Shandong Power Generation
  Co. Ltd. (51% ownership stake) and Shandong Ruyi Science & Technology Group (49%
  ownership stake)". ✓
- GEM: the direct owners of the Hong Kong company are "Huaneng Shandong Power Generation"
  50.0% and "Jining Chengtou Holding Group" 50.0%; Shandong Ruyi is absent; the Hong Kong
  company owns the Pakistani company 100%. ✓ **But nothing in GEM's record carries the date
  30 June 2024.** The GEM wiki page has no percentages and no as-of date; the API entity and
  asset records have no as-of field; the underlying file is the Global Coal Plant Tracker,
  July 2026. The "dated 30 June 2024" must be dropped or sourced. (30 June 2024 is the date
  of AidData's last loan-outstanding figure, which may be where it drifted in from.)

**What is wrong, and it is the core of the entry.**
1. **"cites nothing for those percentages" is unsafe and effectively false.** AidData's
   record lists 65 sources, among them "Generation License App of Hunaneg Shdong RUYI",
   "Application for a Generation License of Huaneng Shandon Ruyi (Pakistan) Energy (Private)
   Limited", and Shandong Ruyi's 2018 bond credit rating report. It footnotes no individual
   fact — that is all that can be said.
2. **"NEPRA's tariff decision and licence name no shareholders" is false for the licence.**
   The generation licence application bundle NEPRA publishes contains, under the project
   feasibility study's heading "1.2 Investment mode": "Sahiwal 2x660MW coal-fired power
   plant shall be built in form of joint venture, and each shareholder's shares are as
   follows: • Huaneng Shandong Power Generation Co., Ltd. 51% • Shandong Ruyi Science &
   Technology Group Co., Ltd. 49%". The same bundle's prospectus says: "On May 22, 2014,
   Huaneng Shandong Ruyi (HK) Energy Limited was incorporated, with Huaneng Shandong Power
   Generation Co., Ltd. and Ruyi Group holding 50% of the shares respectively. On May 28,
   2014, Huaneng Shandong Ruyi (Pakistan) Energy (Private) Limited was incorporated as a
   wholly owned subsidiary of Huaneng Shandong Ruyi (HK) Energy Limited." And the
   memorandum of association in the same bundle lists the subscribers: "Huaneng Shandong
   Ruyi (HK) Energy (HK) Limited" with 99,995 shares "(ninety-nine thousand, nine hundred
   and ninety-five)" of the 100,000 authorised, and five named Chinese individuals with one
   share each.
   The **tariff** half of the claim does hold: the upfront coal tariff determination of
   31 March 2015 names no shareholders and states no shareholding percentages (its only
   "51%" is an indexation weight in the capital-cost formula; its "Sponsor 50% : 50%" is an
   efficiency-gain sharing ratio). The 2017 licence modification also names none.
3. So the split is not "unsettled" in the way the entry says. The 51/49 has a document; so
   does the 50/50 at Hong Kong level; and the Pakistani company's own constitutional
   documents put it at 100% Hong Kong.

**Replacement for `companies[0].role` → `new`:**

> Project company. Its shareholding is given two ways in documents NEPRA published with its generation licence application. The project's feasibility study, under "Investment mode", says the plant "shall be built in form of joint venture, and each shareholder's shares are as follows: Huaneng Shandong Power Generation Co., Ltd. 51%; Shandong Ruyi Science & Technology Group Co., Ltd. 49%" - the figures AidData repeats, without saying which of its 65 listed sources it took them from. The same bundle's prospectus says that on 22 May 2014 "Huaneng Shandong Ruyi (HK) Energy Limited was incorporated, with Huaneng Shandong Power Generation Co., Ltd. and Ruyi Group holding 50% of the shares respectively", and that on 28 May 2014 the Pakistani company "was incorporated as a wholly owned subsidiary of Huaneng Shandong Ruyi (HK) Energy Limited"; the memorandum of association in the same bundle records the Hong Kong company holding 99,995 of the 100,000 shares. The rating agency PACRA, in July 2022, likewise calls the Pakistani company "a wholly owned subsidiary of Huaneng Shandong Ruyi (Hong Kong) Energy Limited". Global Energy Monitor gives the Hong Kong company as 50% Huaneng Shandong Power Generation and 50% Jining Chengtou Holding Group, with Shandong Ruyi absent. NEPRA's tariff decision names no shareholders.

**`sources_add` fixes:** change the PACRA entry's year from 2024 to 2022, and add the NEPRA
generation licence application:
`https://nepra.org.pk/licensing/Licences/Licence%20Application/2015/Generation%20License%20App%20of%20Hunaneg%20Shdong%20RUYI.pdf`
(National Electric Power Regulatory Authority, 2015).

---

## 5. naga-cebu-kepco-coal-dust — CORRECT

**Opened, all served:** both Philippine Star articles at the URLs in `sources_add`;
`https://www.gem.wiki/Naga_power_station`; SPC Power Corporation's SEC Form 17-A for the
year ended 31 December 2022 (`philippines.mom-gmr.org/uploads/tx_lfrogmom/documents/186-2446_import.pdf`,
143,129 characters of extracted text, read through).

**Verified**
- 19 January 2023, exact wording: "KEPCO is in the process of selling its 60 percent stake
  in KEPCO SPC Power Corp. (KSPC)" ✓, date ✓.
- 21 October 2007, exact wording: "SPC said the company will invest 40 percent in the
  project while 60 percent of the total capitalization" "of the project will be provided by
  Kephilco." ✓, date ✓. Note the article says 60 per cent of the **project's** total
  capitalisation; the entry's "60 per cent of its capitalisation" is ambiguous and should
  read "of the project's total capitalisation".
- The trap: no conflation in the entry — the 60% is attached to KSPC, correctly. For the
  record, the 2023 article separately reports KEPCO selling "its 40 percent interest in SPC
  Power Corp.", and SPC Power's own 17-A top-20 list gives "KEPCO Philippines Holdings,
  Inc. … 568,098,817 … 37.96%" as of 31 March 2023. Two different holdings, neither the
  joint-venture split. ✓
- GEM's reversed 60/40: GEM does print "SPC Power Corp. was 'a subsidiary of Salcon Power
  (60%) and Korea Electric Power Company (KEPCO) (40%)'" — but that is the ownership of
  **SPC Power Corporation itself** in GEM's history of Naga-1 (retired 2015, now Therma
  Power Visayas), not the KSPC joint venture that owns Naga units 2-1 and 2-2. So it is
  about a different company, at the same site. Worth a line in the card if the 60/40 is
  going to be stated at all.

**What is wrong.** "No SPC Power Corporation filing states the split" is false. SPC Power
Corporation's annual report on SEC Form 17-A for 2022, under "The Parent Company also has
the following major associates", says: "(i) KEPCO SPC Power Corporation (KSPC). KSPC, 40%
owned by the Parent Company, was incorporated on June 22, 2005 primarily to build, operate,
maintain, own and manage the 2 x 100 Megawatt Circulating Fluidized Bed Combustion (CFBC)
Boiler Coal-Fired Power Plant in the City of Naga, Colon, Cebu." KEPCO's 60% is not in that
filing, but SPC's 40% is.

**Replacement for the last sentence of `companies[0].role` → `new`** (replace "No SPC Power
Corporation filing states the split."):

> SPC Power Corporation's own annual report on SEC Form 17-A for 2022 states its side of it - "KEPCO SPC Power Corporation (KSPC). KSPC, 40% owned by the Parent Company, was incorporated on June 22, 2005" - but no filing found states KEPCO's 60%. Global Energy Monitor prints a 60/40 the other way round, Salcon Power 60 and KEPCO 40, but that is the ownership of SPC Power Corporation itself in its account of the retired first Naga plant, not of the joint venture.

**Caveat on provenance.** The copy of the 17-A I read is a mirror hosted by the Media
Ownership Monitor, not PSE EDGE or the Philippine SEC. The cover sheet is the authentic
Form 17-A cover (S.E.C. Registration No. AS094002365, SPC Power Corporation, formerly
Salcon Power Corp.), but before this goes in the card the same text should be re-read on
PSE EDGE (`edge.pse.com.ph`, company id 237) and that URL cited instead.

---

## 6. barishal-coal-plant-evictions — CORRECT

**Opened:** `https://china.aiddata.org/projects/71614/` (served; raw HTML parsed, full
narrative and all five staff comments read); `https://www.energytransitionbd.org/infrastructure/barishal-350-mw-bepcl-coal-power-plant-phase-2`
(served; raw HTML parsed, 6,235 characters of text, every citation anchor extracted);
`https://www.gem.wiki/Barisal_power_station` (served).

**Verified**
- AidData gives the 92/4/4 and all three names in full: "a special purpose vehicle and
  joint venture of Barisal Energy (DFC) Holding Limited (92% ownership stake), Sinohydro
  (Hong Kong) Holdings Limited (4% ownership stake) and ISO Tech Electrification Company
  Limited (4% ownership stake) that was legally incorporated in October 2017". ✓ (AidData
  writes "ISO Tech", the entry "Iso Tech".)
- BWGED's figures: "BEDICL invested $149.04 million, while ITECL and SHKHL invested $6.48
  million each, holding 92%, 4%, and 4% share of the project." ✓ — so the dollar figures
  are BWGED's, not AidData's; AidData gives none.
- GEM: "PowerChina owns 96% of the shares", "Barisal Electric Power Company Limited (BEPCL)
  is a joint venture between Chinese state-owned company PowerChina" "and Bangladeshi
  company ISO Tech Electrification Company Limited", with the unit table giving "Power
  Construction Corporation of China Ltd [96.0%]; small shareholder(s) [4.0%]" — Iso Tech
  named, no percentage against it. ✓ GEM does not mention Sinohydro at all.

**What is wrong.**
1. **"BWGED citing a PowerChina press release" is false.** The citation that follows
   BWGED's finance paragraph is "Power. IN-EN, 2021", linking to
   `https://power.in-en.com/html/power-2387617.shtml` ("Bangladesh Barissa project achieves
   financing closure", 12 May 2021) — a Chinese energy trade-news site. The only
   PowerChina-related citation on the page is a China Daily article of 19 December 2018
   ("POWERCHINA's subsidiary inks agreement for power station in Bangladesh"), cited for a
   2018 design-services agreement, not for the shareholding. BWGED also cites GEM as a
   reference, so the two are not independent of each other.
2. BWGED does **not** name "Barisal Energy (DFC) Holding Limited". It writes "BEDICL" and
   nowhere expands it; separately, under "Sponsors", it describes BEPCL as "a Joint Venture
   Company (JVC) of Sinohydro (Hong Kong) Holdings Limited (SHKH) and ISO Tech
   Electrification Company Limited (ITECL)" — leaving the 92% holder out entirely. Saying
   the two databases "both give" the same three-named split overstates BWGED.
3. "No document reconciles 96% with 92/4/4" survives everything I could open. GEM's 96% is
   PowerChina at group level and 92+4 = 96 arithmetically, but no document says that is
   what GEM's 96% is, so the entry is right not to say it either.

**Replacement for `companies[1].role` → `new`:**

> Bangladeshi joint-venture partner. The 4% is sourced; the plant company's structure is given three ways and they do not agree. AidData's record gives a three-way split - Barisal Energy (DFC) Holding Limited 92%, Sinohydro (Hong Kong) Holdings Limited 4% and ISO Tech Electrification Company Limited 4%. The Bangladesh Working Group on External Debt's database gives the same 92/4/4 but names the holders only as "BEDICL", "SHKHL" and "ITECL", recording that "BEDICL invested $149.04 million, while ITECL and SHKHL invested $6.48 million each", and citing a Chinese trade-press report of the project's financing close; elsewhere on the same page it describes the plant company as a joint venture of Sinohydro and Iso Tech alone. Global Energy Monitor instead says PowerChina owns 96% and names Iso Tech without a percentage. No document reconciles 96% with 92/4/4.

**Failed URL, and which kind of failure.** `https://pr.powerchina.cn/2434.html` **did not
open, and the failure was at the host, not a permission prompt.** Direct curl returned
`curl: (35) Recv failure: Connection reset by peer`, with the proxy logging
`pr.powerchina.cn:443 — ws_closed_mid_exchange`; the rendered fetch returned
`failed at its site (client_error)` with nothing retrieved. Two different clients, two
host-side failures, no permission dialogue involved. The press release remains unread, so
it cannot be cited; and since BWGED does not cite it either, it should be dropped from the
entry rather than carried as a pending check.

---

## 7. equatorial-palm-oil-jogbahn — KEEP, with one clause to fix

**Opened:** `https://landmatrix.org/media/uploads/epo-jv-biopalm-energy.pdf` (served;
21 pages, read in full as text).

**Verified**
- Date: "Publication of this document 10 December 2010". ✓
- Incorporation and ownership, verbatim from the definitions: "'BioPalm Energy' or 'BEL'
  BioPalm Energy Limited, a company incorporated in Singapore with company registration
  number 201007394Z, which is a wholly owned subsidiary of Siva Ventures". ✓ — covers both
  the registration number and "wholly owned by Siva Ventures".
- Chennai: "The Siva Group was founded in 1986 by Mr. Chinnakannan Sivasankaran, and is a
  Chennai, India-based conglomerate". ✓ And the definitions give "Siva Ventures: Siva
  Venture Limited, a company incorporated in India, having its registered office at
  Sterling Towers, 327, Anna Salai, Teynampet, Chennai – 600 006, India".
- BioPalm's own address: the circular gives only a country — the group structure chart
  labels it "Biopalm Energy Limited, Singapore". No street address for BioPalm anywhere in
  the document. ✓

**What to fix.** "no document gives a street address" reads, placed where it is, as being
about the whole chain, and the circular plainly does give one — for Siva Ventures. Tighten
it so the absence claim is only about BioPalm.

**Replacement for the clause "no document gives a street address, so the map marker is only
as precise as the country":**

> the circular gives BioPalm's country but no street address for it, giving one only for Siva Ventures, at Sterling Towers, 327 Anna Salai, Teynampet, Chennai - 600 006, so the marker for BioPalm is only as precise as the country

Minor: the circular writes "Siva Venture Limited" (singular) in its definitions and "Siva
Ventures" in the body; the entry's "Siva Ventures Ltd" is the body usage and is fine.

---

## 8. penarroya-cobrac-santo-amaro-lead — KEEP (the removal is right)

**Searched for any documentary basis for "Rieux, France" as a corporate seat of COBRAC or
of Société Minière et Métallurgique de Peñarroya, and found none.**
- The Brazilian Ministry of Health's human-health risk assessment for Santo Amaro da
  Purificação (the ARSH study, 492,549 characters of extracted text, read by grep over the
  whole file) contains the word "Rieux" **zero** times, while describing COBRAC's ownership
  at length.
- The entry's own stated basis, Portuguese Wikipedia, is not a document; and the French
  Wikipedia article on Peñarroya, which does discuss the seat, does not mention Rieux
  either — it says the seat was in Paris.
- The nearest thing to a Rieux connection I could find is a Hauts-de-France heritage
  inventory dossier (IA60001782) for a former chemical works "puis Penarroya (détruit)" in
  the Oise. **That page would not open:** `inventaire.hautsdefrance.fr` served a
  bot-protection interstitial — "Les robots IA perturbent le Web, JavaScript est nécessaire
  pour accéder à cette page" — so I cannot confirm its commune. Either way a works is not a
  corporate seat. Do not reinstate Rieux on the strength of it.

**Reported, not assumed, for a possible later edit.**
- **Peñarroya's own seat.** No primary document opened. French Wikipedia says "Le siège
  central reste à Paris (au 12, place Vendôme)"; the International Directory of Company
  Histories entry for Metaleurop S.A. says Peñarroya's "headquarters were at the famed
  Place Vendôme in Paris, where the company would remain for more than 80 years". Both
  secondary. The 1930 dating of a 12 place Vendôme address is **not** verified by anything
  I opened.
- **Fontenay-sous-Bois, and it is a real primary document.** Commission Decision of
  26 June 1990 relating to a proceeding pursuant to Article 86 of the EEC Treaty
  (IV/32.846 – Metaleurop SA), at `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:31990D0363`,
  is addressed to "Metaleurop SA, 118 Péripole, 44 rue Roger Salengro, 94126
  Fontenay-sous-Bois, Cedex, France", and states that "the main shareholders in Peñarroya,
  now known as Metaleurop SA, are Preussag and Imetal". So the renamed entity's seat at
  Fontenay-sous-Bois is documented, with a street address, as at June 1990. (The previous
  researcher's "1990 European Commission decision" is this one; note that
  CELEX 31990M0004, which a search will surface alongside it, is Renault/Volvo and has
  nothing to do with Peñarroya — I checked.)
- **The 1987 change of control: supported, but not as "Companhia Adubos Trevo" alone.** The
  Ministry of Health study says: "Em 1987 a Companhia Adubos Trevos, de Porto alegre, rio
  Grande do sul, associada a Companhia Paulista de Metais adquirem o controle acionário da
  empresa. Em 1989 a empresa é incorporada a Plumbum Mineração e Metalurgia S/A". So in 1987
  Companhia Adubos Trevo of Porto Alegre, **together with Companhia Paulista de Metais**,
  acquired the controlling shareholding; incorporation into Plumbum followed in 1989. Its
  introduction adds that COBRAC was "de capital francês e nacional, originalmente subsidiada
  pelo grupo Penarroya", operated 1960–1993, and that "Em 1989 a COBRAC foi incorporada à
  Plumbum Mineração e Metalurgia Ltda., pertencente ao Grupo Trevo." A future edit must not
  drop Companhia Paulista de Metais.

---

## 9. cbg-sangaredi — CORRECT (one word: which fiscal year)

**Opened:** Alcoa's FY2016 10-K cover (`sec.gov/Archives/.../d298292d10k.htm`), FY2017
10-K cover (`.../d502924d10k.htm`), and — on a second attempt, successfully — the **FY2025**
10-K (`sec.gov/Archives/edgar/data/1675149/000119312526077167/aa-20251231.htm`, accession
0001193125-26-077167, filed 26 February 2026), identified from Alcoa's filing index at
`data.sec.gov/submissions/CIK0001675149.json`.

**Verified**
- FY2016: "ALCOA CORPORATION", "Delaware", "390 Park Avenue, New York, New York 10022-4608",
  "For The Fiscal Year Ended December 31, 2016". ✓
- FY2017: "ALCOA CORPORATION", "Delaware", "201 Isabella Street, Suite 500, Pittsburgh,
  Pennsylvania 15212-5858", "For The Fiscal Year Ended December 31, 2017". ✓
- **Most recent 10-K I could open, FY2025** (year ended 31 December 2025): cover gives
  "201 Isabella Street , Suite 500 , Pittsburgh , Pennsylvania (Address of principal
  executive offices)", and its Item 2 Properties adds "Alcoa Corporation's principal
  executive office, located at 201 Isabella Street, Pittsburgh, Pennsylvania 15212-5858, is
  leased." ✓ So the present-tense claim is good as of the FY2025 filing and does not rest
  on 2017.

**On the earlier failure.** The first attempt at the FY2025 10-K failed with
`PROVENANCE_REQUIRED` — "the user did not answer an earlier permission request in time" —
**a permission failure, not a host refusal.** It then downloaded without difficulty once the
request went out with a declared contact in the User-Agent, which is what sec.gov requires;
`www.sec.gov/Archives` returns HTTP 403 "Your Request Originates from an Undeclared
Automated Tool" to an undeclared client. Nothing on sec.gov is blocking this map.

**Replacement for `companies[2].desc` → `new`:**

> A US aluminium company incorporated in Delaware with its principal executive offices at 201 Isabella Street, Suite 500, Pittsburgh, Pennsylvania, per the cover of its Form 10-K for 2025; it gave 390 Park Avenue, New York in its 10-K for 2016, the year it was separated from Alcoa Inc., and Pittsburgh from the 2017 10-K onwards. It

**`sources_add` fix:** keep the FY2017 10-K (it carries the 2017 half of the sentence) and
add the FY2025 one, since that is what the present tense now rests on:
`https://www.sec.gov/Archives/edgar/data/1675149/000119312526077167/aa-20251231.htm`
(Alcoa Corporation, Form 10-K for the fiscal year ended 31 December 2025, cover page; US
Securities and Exchange Commission, 2026). The FY2016 10-K should be cited too, at
`https://www.sec.gov/Archives/edgar/data/1675149/000119312517083862/d298292d10k.htm`.

---

## 10. kangqiao-lead-poisoning-johnson-controls — KEEP

**Opened:** the Form 10-K itself, from the SEC — `sec.gov/Archives/edgar/data/833444/000083344425000097/jci-20250930.htm`,
accession 0000833444-25-000097, filed 14 November 2025. 3,101,711 bytes of filing, from
which I extracted **507,549 characters** of text and searched **all** of it.

**Verified**
- Cover: "JOHNSON CONTROLS INTERNATIONAL PLC (Exact name of registrant as specified in its
  charter) Ireland 98-0390500 (Jurisdiction of Incorporation) (IRS Employer Identification
  No.) One Albert Quay , Cork , Ireland , T12 X8N6 ( 353 ) 21-423-5000 (Address of Principal
  Executive Offices and Postal Code)", "For the Fiscal Year Ended September 30 , 2025". ✓
- Item 2, the sentence in full: **"The Company has properties in almost 60 countries
  throughout the world, with its world headquarters located in Cork, Ireland and its North
  American operational headquarters located in Milwaukee, Wisconsin USA."** ✓ Both halves of
  the entry's claim are in that one sentence.
- **Absence claim, checked over the whole document, not a sample:** "glendale" appears
  **0** times in all 507,549 characters. For comparison, in the same pass: "milwaukee" 3
  (Item 2; the Gumm v. Molinaroli venue; the auditor's signature block), "cork" 6,
  "albert quay" 2, "world headquarters" 1. ✓

**One fix, to the source rather than the text.** The URL in `sources_add`
(`https://www.investors.johnsoncontrols.com/~/media/Files/J/Johnson-Controls-IR-V2/quarterly-reports/2025/fy2025-form-10-k-jci-plc.pdf`)
**would not open:** curl failed with `(56) CONNECT tunnel failed, response 502` — a transport
failure between the proxy and that host, not a permission prompt and not a refusal by
Johnson Controls. I verified against the SEC-filed original instead, so the citation should
point there:
`https://www.sec.gov/Archives/edgar/data/833444/000083344425000097/jci-20250930.htm`.

---

## 11. bhabadah-waterlogging-kjdrp — KEEP

**Opened:** `https://pani.bwdb.gov.bd/archive/pdf/274.pdf` (served; 18 pages, converted and
read in full).

**Verified.** The file is a BWDB compilation of successive "Achievement at a Glance" reports,
one per year from 1994 onwards, each headed "BANGLADESH WATER DEVELOPMENT BOARD /
ACHIEVEMENT AT A GLANCE". The 2009 instalment is headed "UPTO JUNE, 2009". ✓ Under its
heading "2 ACHIEVEMENT OF MAJOR PHYSICAL COMPONENTS", with the column headers "Pre-Ind.
Post-Ind. Total":

```
a) Embankment                   2977    7247    10224   Km
    i Coastal (115 Polders)     2138    2392    4530    Km
   ii Others                     839    4855    5694    Km
```

2,977 + 7,247 = 10,224 km, with 4,530 km coastal. ✓ All four numbers confirmed, in the right
columns.

**Is "reported a total of … as at June 2009" fair to a bare table cell?** Yes. The wording
claims only that BWDB reported the figures and what period they cover, and both of those come
from the document's own furniture: the publisher is named in the page heading, the period in
"UPTO JUNE, 2009", and the row and column labels supply "Embankment", "Pre-Ind.", "Post-Ind.",
"Total" and "Coastal". The entry does not say the figures were built in that year, measured in
any particular way, or verified — which is right, because the table says none of that.

**Weak points.** (a) "Pre-Ind." is 2,977 km in every instalment from 1996 to 2009, and the
coastal row is unchanged at 2,138/2,392/4,530 from 2006 to 2009, so these are carried-forward
cumulative totals, not fresh measurements. The entry's "reported a total of" is compatible
with that; "had built", the old wording being replaced, was not, so the edit is an improvement.
(b) The 2009 instalment dates the pre-independence period as "(1944-71)" where the 1994
instalment used "(1959-71)". Nothing in the entry turns on it, but do not quote a
pre-independence start year from this file.

---

## URLs that failed, and how

| URL | Failure | Kind |
|---|---|---|
| `https://pr.powerchina.cn/2434.html` | curl `(35) Recv failure: Connection reset by peer`, proxy logged `ws_closed_mid_exchange`; rendered fetch returned `failed at its site (client_error)` | **host-side**, both clients; no permission prompt involved |
| `https://www.investors.johnsoncontrols.com/~/media/…/fy2025-form-10-k-jci-plc.pdf` | curl `(56) CONNECT tunnel failed, response 502` | transport/proxy; not a refusal by the host, not a permission prompt |
| `https://www.sec.gov/Archives/…/aa-20251231.htm` (first attempt) | `PROVENANCE_REQUIRED` — permission request unanswered | **permission**; the file opened on retry with a declared contact in the User-Agent |
| `https://www.sec.gov/Archives/…/jci-20250930.htm` (first attempt) | `PROVENANCE_REQUIRED` — permission request unanswered | **permission**; opened on retry, same fix |
| `https://inventaire.hautsdefrance.fr/dossier/IA60001782` | bot-protection interstitial: "Les robots IA perturbent le Web, JavaScript est nécessaire pour accéder à cette page" | host-side, JavaScript gate |
| `https://www.gem.wiki/*` | HTTP 403 to plain curl | host-side user-agent filter; the pages opened fine through the rendered fetch, so **not** a blocked host |
| `https://www.cetem.gov.br/antigo/santo_amaro/sacsa/I_SACSA_JOAO_VICTOR_SANTOS_2013.pdf` | curl `(60) SSL certificate problem: unable to get local issuer certificate` | host-side certificate chain; not needed in the end |

Nothing here is a blocked host in the sense the map's notes have used. `cercind.gov.in`,
`disclosures.ifc.org` (SPI, ESRS, SII and ED paths all served), `nepra.org.pk`,
`pani.bwdb.gov.bd`, `landmatrix.org`, `china.aiddata.org`, `energytransitionbd.org`,
`api.globalenergymonitor.org`, `eur-lex.europa.eu`, `gov.br`, `philstar.com`, `adb.org`,
`ebrd.com`, `pacra.com` and `sec.gov/Archives` all served on first or second attempt.
