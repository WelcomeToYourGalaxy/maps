# Fact-check log — r26f_textfix_9.json

Checked 11 November 2026. Every document below was opened by the checker. Where a claim was of
absence, the full document text was downloaded and searched, not sampled.

Documents opened:

- ICSID, *Aguas del Tunari S.A. v. Republic of Bolivia*, ARB/02/3, Decision on Respondent's
  Objections to Jurisdiction, 21 October 2005 — https://www.italaw.com/sites/default/files/case-documents/italaw10957_0.pdf
  (downloaded in full, 332,261 characters of extracted text, searched end to end)
- AidData project 71614 — https://china.aiddata.org/projects/71614/ (downloaded, full text searched)
- Global Energy Monitor, Barisal power station — https://gem.wiki/Barisal_power_station (opened)
- PT TJK Power, About Us — https://tjkpower.com/about-us/ (opened)
- Teras Batam, "PT Bright PLN Batam akan 'Pensiunkan' PLTU Tanjung Kasam" —
  https://www.terasbatam.id/pt-bright-pln-batam-akan-pensiunkan-pltu-tanjung-kasam/ (downloaded, full text read)
- IFAD Office of Evaluation, *Republic of Uganda, Vegetable Oil Development Project, Interim
  Evaluation*, EC-2010-63-W-P-4 — https://members.ifad.org/ec/63/docs/en/EC-2010-63-W-P-4-Interim-Evaluation-Report.pdf?attach=1
  (downloaded, 460,611 characters of extracted text, searched end to end)
- IFAD, *President's report: proposed loan to the Republic of Uganda for the Vegetable Oil
  Development Project — Phase 2*, EB-2010-99-R-19 — https://members.ifad.org/eb/99/docs/en/EB-2010-99-R-19.pdf?attach=1 (opened)
- IFAD project completion summary, VODP — https://www.ifad.org/documents/38714182/39729786/Vegetable+Oil+Development+Project+(VODP).pdf (opened)
- World Bank Projects API, search.worldbank.org/api/v3/projects (queried directly)
- AidData project 62206, Tanjung Kasam — https://china.aiddata.org/projects/62206 (opened)

Two IFAD URLs issued a 302 to members.ifad.org and were refetched at the redirect target, which
served the full PDF. No host refused service and no fetch was blocked by a permission denial.

---

## 1. cochabamba-water-war — **CORRECT**

One factual error: the corporate name's spelling. Everything else is verified.

Verified against the ICSID decision:

- **Para. 60, item 3** — "The remaining fifty five percent of the shares were owned by
  International Water (Tunari) Ltd ('IW Ltd') of the Cayman Islands. The shares of IW Ltd were 100
  percent owned by Bechtel Enterprise Holding, Inc., a company organized under the laws of the
  United States of America." 55% and the 100% Bechtel parentage verified.
- **Para. 60, item 2 and footnote 30** — "Riverstar International, S.A. of Uruguay owned twenty five
  percent of the shares"; footnote 30: "Riverstar is 100 percent owned by Abengoa of Spain." Verified.
- **Para. 60, item 1 and footnote 29** — "Twenty percent of the shares in AdT were divided between
  four Bolivian companies"; footnote 29 names them: "Constructora Petricevic, S.A.; Compañía
  Boliviana de Ingeniería, S.R.L.; ICE Agua y Energía, S.A.; and, Sociedad Boliviana de Cemento,
  S.A., each at 5 percent." All four names and the 5 percent each are correct; the entry's
  unaccented renderings match the document's names.
- **Para. 67** — "on November 9, 1999, Bechtel announced that it had reached an agreement with
  Edison, S.p.A. of Italy ... As a consequence, Edison would assume a 50 percent interest in IW Ltd."
  Verified. (Document punctuates the company as "Edison, S.p.A.")
- **Para. 70** — "On December 21, 1999, IW Ltd of the Cayman Islands 'migrated' to Luxembourg where
  it became known as International Water (Tunari) S.a.r.l. ... Finally, on December 22, 1999, IWT
  B.V. became the 100 percent shareholder of IW S.a.r.l." Verified.
- **Para. 72** — "the Parties agree that these changes meant that as of December 1999 AdT was no
  longer held by a Cayman Islands corporation ... the Parties also appear to accept that 55 percent
  of AdT's upstream ownership passed through Dutch companies after December 22, 1999, Bolivia
  disputes the substance of these Dutch entities, describing them as mere shells." Verified.

**"The decision does not mention United Utilities" — VERIFIED.** The PDF was downloaded and its full
extracted text (332,261 characters, the complete decision including the dissenting declaration of
José Luis Alberro-Semerena and the appendices) was searched case-insensitively for "united
utilities". Zero occurrences. The absence claim holds for the whole document, not just the opening.

**The spelling error.** The entry writes "Bechtel Enterprise Holdings, Inc." That is not the
document's spelling at para. 60. The decision is internally inconsistent across its length — a
full-text search returns five spellings:

| Spelling | Where |
|---|---|
| Bechtel Enterprise Holding, Inc. | **para. 60** (the paragraph the entry cites) |
| Bechtel Enterprises Holding, Inc. | footnote 268 (to para. 321) and nearby |
| Bechtel Enterprises Holding Inc. | para. 329(a) |
| Bechtel Enterprises Holdings, Inc. | declaration of José Luis Alberro-Semerena, ¶ 12 |

Since the entry attributes the ownership structure to para. 60, it must use para. 60's spelling.

**Exact replacement.** In the `new` text, replace

> was itself 100% owned by Bechtel Enterprise Holdings, Inc. of the United States

with

> was itself 100% owned by Bechtel Enterprise Holding, Inc. of the United States

Supporting sentence (para. 60): "The shares of IW Ltd were 100 percent owned by Bechtel Enterprise
Holding, Inc., a company organized under the laws of the United States of America."

**Second, smaller correction — recommended.** The entry's "In December 1999 the holding migrated to
Luxembourg and then to a Dutch company" reads as though the holding company itself moved to the
Netherlands. Para. 70 describes something different: IW Ltd migrated to Luxembourg on 21 December
1999, and on 22 December a Dutch company (IWT B.V.) became its 100 percent shareholder. Replace

> In December 1999 the holding migrated to Luxembourg and then to a Dutch company, which is how the Netherlands-Bolivia treaty came into it (paras 70, 72).

with

> On 21 December 1999 IW Ltd migrated from the Cayman Islands to Luxembourg, becoming International Water (Tunari) S.a.r.l., and on 22 December a Dutch company, International Water (Tunari) B.V., became its sole shareholder, which is how the Netherlands-Bolivia treaty came into it; Bolivia calls the Dutch entities mere shells (paras 70, 72).

**Weak points to note even once corrected:**
- The entry presents the para. 60 structure as settled fact. It is the tribunal's recital of the
  position "at the time the Concession was concluded in September 1999," and the entry's "as at
  September 1999" correctly carries that. Good as written.
- The December 1999 restructuring is contested: para. 72 records that Bolivia does not clearly
  accept AdT's chart and describes the Dutch entities as shells. The corrected wording above carries
  that; the original `new` text did not.
- Dropping Wikipedia removes the only source for the United Utilities claim. The ICSID decision does
  not mention the company, which is an absence, not a refutation — United Utilities' involvement in
  International Water elsewhere is not addressed by this document either way. "The decision does not
  mention United Utilities" is the right phrasing and should not be hardened into a denial.

---

## 2. barishal-coal-plant-evictions — **CORRECT**

The first edit is fully verified. The second edit contains one false statement about a source.

### Edit 1 — verified in full

From https://china.aiddata.org/projects/71614/ , read 11 November 2026:

- **One facility, US$427.5 million, April 2020, three lenders, borrower BEPCL.** Project narrative:
  "In April 2020, China Eximbank, the Beijing Branch of Bank of China Limited, and the Singapore
  Branch of Bank of China Limited signed a $427.5 million syndicated loan (facility) with Barisal
  Electric Power Company Limited (BEPCL)". Verified.
- **Commitment date 1 April 2020.** Key dates block: "Commitment date Apr 1, 2020". Verified.
- **Equal split and the caveat.** Staff comments: "The individual contribution from each lender to
  the syndicated loan is unspecified. For the time being, AidData assumes equal contributions
  ($142.5 million) across the three lenders ... This issue warrants further investigation." Verified,
  including the "warrants further investigation" wording.
- **US$557.89 million is the project, not the loan.** "The $557.89 million independent power plant
  (IPP) project was financed according to a 76.6:33.4 debt-to-equity ratio." Verified.
- **No disbursement or first-issuance date.** The record carries a commitment date, actual start
  (1 Jan 2019), planned end (12 Jan 2022), actual end (31 Dec 2022) and originally scheduled last
  repayment (1 Jul 2034). There is no disbursement or first-issuance field or date. Verified.
- **Sovereign guarantee 23 December 2020.** "the Ministry of Finance of Bangladesh issued a sovereign
  guarantee in support of the loan on December 23, 2020". Verified.
- **No September 2021 date.** The downloaded page was searched for "September" and for "2021". The
  word September does not occur anywhere. The only 2021 date is "a Sinosure credit insurance policy
  went into effect on October 27, 2021." The entry's claim that the page does not date the signing to
  September 2021 is verified, and nothing on the page carries a September 2021 date.

One nuance worth recording: record 71614 is AidData's record for *Bank of China (Beijing Branch)'s
participation*, and its own commitment figure is US$142.5 million (US$147,022,070 in constant 2023
USD). The US$427.5 million is the facility that record sits inside. The entry's wording — "AidData's
record for the project ... gives one syndicated loan facility of US$427.5 million ... AidData divides
it equally at US$142.5 million each" — states this correctly.

### Edit 2 — one element false

The entry says of the Global Energy Monitor page: "that page could not be opened to check." It
opens. https://gem.wiki/Barisal_power_station was fetched successfully and does carry the claim: the
page states the syndicate of the Export-Import Bank of China and the Bank of China issued the first
loan in May 2021, citing a 12 May 2021 article, and describes the financing as having "successfully
completed the financing and closure." A no-fabrication card cannot say a page would not open when it
does.

**Exact replacement.** Replace the `new` text

> Global Energy Monitor reports that the syndicate issued its first loan in May 2021, completing the financing; that page could not be opened to check, and AidData's record gives no disbursement date. With the facility signed in April 2020 and the sovereign guarantee given on 23 December 2020, a first issuance in May 2021 does not conflict with the signing date.

with

> Global Energy Monitor's Barisal power station page reports that the syndicate of China Eximbank and Bank of China issued the first loan in May 2021, citing a 12 May 2021 report, and describes the financing as closed at that point. AidData's record gives no disbursement date. With the facility signed in April 2020 and the sovereign guarantee given on 23 December 2020, a first issuance in May 2021 does not conflict with the signing date.

Supporting material: the Global Energy Monitor page's financing section attributes the first loan to
May 2021 and cites a 12 May 2021 source; AidData's record 71614 carries a commitment date of
1 April 2020 and a sovereign guarantee of 23 December 2020 and no disbursement date.

**Weak points:**
- The reconciliation in the last sentence is a reading, not a sourced statement. It is a defensible
  one — a facility signed in April 2020 and a first drawdown thirteen months later are ordinary
  project-finance sequence, and no source says the two conflict — but no document says so. If the
  owner wants only sourced sentences on the card, that sentence should be dropped and the two dates
  left to stand side by side with their sources named.
- Global Energy Monitor names the borrower as "Barisal Power Generation Co., Ltd." in its financing
  section while AidData names BEPCL. The card need not resolve that, but it should not silently
  treat GEM's borrower and AidData's as the same entity.

---

## 3. tanjung-kasam-coal-dust-batam — **CORRECT**

The `conditions` edit is clean. The `outcome` edit's central move — reconciling 130 MW and 110 MW —
is not supported by the Teras Batam article and must be rewritten.

### `conditions` edit — verified, KEEP as written

PT TJK Power's About Us page describes the plant as "Tanjung Kasam Power Plant (PLTU) (2x65 MW)".
"2 x 65 MW, that is 130 MW installed" is verified.

### `outcome` edit — the reconciliation fails

Verified parts:

- **2x65 MW, 130 MW installed, from the operator's own site.** https://tjkpower.com/about-us/ :
  "Tanjung Kasam Power Plant (PLTU) (2x65 MW)". Verified.
- **130 MW is AidData's figure.** AidData project 62206 (Tanjung Kasam, Telaga Punggur, Batam) gives
  the plant's capacity as 130 MW, and its alternate titles include "2x65MW Tanjung Kasam Power
  Station Project". Verified.
- **Ownership chain.** The About Us page says TJK Power is a joint venture resulting from a strategic
  partnership between PT Petra Unggul Sejahtera — itself a partnership of China Huadian Engineering
  Co. Ltd, PT Inta Daya Perkasa and Batam Power Ventures Pte. Ltd — and PT PLN Batam. Verified. The
  page gives no percentages; the entry does not claim any. (AidData 62206 separately gives 90% Petra
  Unggul Sejahtera / 10% PT PLN Batam for PT Tanjung Kasam Power.)
- **Commercial operation dates.** The About Us page dates Unit 1 to 25 October 2012 and Unit 2 to
  1 November 2012. Verified.
- **The Teras Batam quote, date and speaker.** The article says: "PLTU Tanjung Kasam sudah beroperasi
  sejak 2012 lalu dengan daya mampu sebesar 2 x 55 Mega Watt (MW)." It attributes this to "Direktur
  Utama PT Bright PLN Batam Nyoman S Astawa dalam konferensi pers secara daring, Kamis (4/11/2021)" —
  a president director, an online press conference, Thursday 4 November 2021. All verified. The
  entry's "daya mampu sebesar 2 x 55 Mega Watt", the 4 November 2021 date, the speaker's name and his
  title are correct.

**What fails.** The entry asserts that the two figures "are measuring different things rather than
disagreeing," on the ground that *daya mampu* is deliverable rather than installed capacity. Two
problems:

1. The article never contrasts *daya mampu* with installed capacity. It does not use *kapasitas
   terpasang* or any equivalent anywhere.
2. In its own narration, independent of the quote, the article describes the generating equipment
   itself as 55 MW units: "PLTU Tanjung Kasam mulai beroperasi secara penuh pada akhir tahun 2012
   lalu dengan mesin pembangkit 55 MW x 2" — "began full operation at the end of 2012 with
   generating machines of 55 MW x 2." A unit rating is not a derating. The article is presenting the
   plant as built from two 55 MW machines, which is in conflict with the operator's 2x65 MW.

So the honest position is a disagreement between sources, attributed, not a reconciliation. *Daya
mampu* does in Indonesian power-sector usage mean available capacity, and that may well be the
explanation — but the card would be asserting an explanation the article does not give while the same
article's own wording points the other way. Under a no-fabrication standard that does not pass.

**Exact replacement.** Replace, in the `outcome` edit's `new` text, everything after the first
sentence — that is, replace

> On capacity the two figures are measuring different things rather than disagreeing: PT TJK Power's own site gives the plant as 2 x 65 MW, 130 MW installed, which is the figure AidData uses, while PLN Batam's president director gave its daya mampu, the capacity it can actually deliver, as 2 x 55 MW at a press conference on 4 November 2021.

with

> The sources do not agree on capacity. PT TJK Power's own site gives the plant as 2 x 65 MW, 130 MW, which is the figure AidData uses. Teras Batam, reporting an online press conference on 4 November 2021, quotes PT Bright PLN Batam's president director Nyoman S Astawa saying the plant has operated since 2012 "dengan daya mampu sebesar 2 x 55 Mega Watt" - with an available capacity of 2 x 55 MW - and the same article describes the plant as running on "mesin pembangkit 55 MW x 2", two 55 MW generating sets. Daya mampu normally means the output a plant can actually deliver rather than its nameplate rating, which would make the two figures compatible, but neither source says so and the article's own wording treats 55 MW as the units' rating.

Supporting sentences, both from the Teras Batam article: "PLTU Tanjung Kasam sudah beroperasi sejak
2012 lalu dengan daya mampu sebesar 2 x 55 Mega Watt (MW)." and "PLTU Tanjung Kasam mulai beroperasi
secara penuh pada akhir tahun 2012 lalu dengan mesin pembangkit 55 MW x 2."

**Weak points:**
- The card gives Batam demand as 383 MW from The Jakarta Post. Teras Batam gives 384 MW
  ("kebutuhan listrik di Batam sebesar 384 MW") with the same 30 percent share. A one-megawatt
  difference between two papers needs no resolution, but if the card carries a demand figure it
  should say whose.
- The sources_add entry titled "About Us (plant capacity 2x65 MW, ownership, commercial operation
  dates)" is dated "year: 2026". The page carries no publication date; 2026 is the access year. That
  is a defensible convention but should be consistent with how the map dates other undated pages.
- AidData 62206 describes the plant as having "two 115 MW generators" while giving 130 MW capacity,
  which is internally inconsistent on AidData's side. Nothing in the edit depends on it, but it is a
  reason not to lean on AidData as the arbiter of the capacity question.

---

## 4. kalangala-oil-palm — **CORRECT**

Two of the entry's elements are wrong: the UNOPS handover month and the reason for the Bank's
withdrawal. The financing elements are verified, and the US$52 million question is now resolved.

Source: IFAD Office of Evaluation, *Republic of Uganda, Vegetable Oil Development Project, Interim
Evaluation*, EC-2010-63-W-P-4, opened in full.

Verified:

- **US$20 million IFAD loan, April 1997.** Para. 34: "The VODP was approved by the Executive Board in
  April 1997 and the loan became partially effective in July 1998." Para. 35: "Total project costs
  were originally estimated at US$60 million, consisting of an IFAD loan of US$20 million, US$33.1
  million in cofinancing from a private-sector parter, and contributions of US$3.8 million and US$3.1
  million, respectively from the Government and the beneficiaries." IFAD's own project summary gives
  the approval date as 29 April 1997. Verified.
- **Private and government cofinancing.** Verified from para. 35 as quoted, which also names
  beneficiary contributions of US$3.1 million — a third cofinancier the entry does not mention.
  BIDCO/OPUL is the private partner (para. 28; the completion summary names it).
- **No World Bank or IDA money.** The evaluation's full text was searched: "IDA" does not occur
  anywhere in the document. The World Bank appears only as cooperating institution, in the appraisal
  mission and in the mid-term review. Verified.
- **World Bank as cooperating institution only, ending 2004.** Para. 253: "The World Bank acted as
  cooperating institution for VODP until August 2004, having been closely involved in project
  formulation and appraisal." Para. 41: "The project was supervised by the World Bank between 1998
  and 2004 and by the United Nations Office for Project Services (UNOPS) between 2004 and 2008.
  Since 1 January 2009, it has been directly supervised by IFAD." **The August 2004 date is
  verified** — it is in para. 253 in those words.

**Error 1 — UNOPS took over in September, not August.** The entry says the Bank was cooperating
institution "only until August 2004, when UNOPS took over." Para. 254 gives a different month for the
handover: "UNOPS took over from the World Bank as cooperating institution in September 2004." The
Bank's role ran to August 2004; UNOPS began in September 2004.

**Error 2 — the reason was environmental safeguards generally, not forestry safeguards.** The entry
says the Bank "withdrew over its forestry safeguards policy." The evaluation's stated reason is
broader. Para. 46: "Nevertheless, the World Bank was concerned about compliance with its internal
environmental safeguards policies and felt unable to continue as cooperating institution." The
document's full text contains no reference to a forestry policy, OP 4.36, or any forest-specific
safeguard as the Bank's reason. Forest degazetting appears in para. 45 as one strand of public
opposition to the project, alongside tax concessions, perceived land giveaways, squatter displacement
and biodiversity — and para. 45 records that "The policy of degazetting public forests was
abandoned." Attributing the Bank's withdrawal to a forestry policy reads a specific cause into a
general one and attaches it to the wrong paragraph.

**Exact replacement.** Replace, in the `new` text,

> and records the Bank as the project's cooperating institution only until August 2004, when UNOPS took over and the Bank withdrew over its forestry safeguards policy.

with

> and records the Bank as the project's cooperating institution only until August 2004, with UNOPS taking over in September 2004; the evaluation says the Bank "was concerned about compliance with its internal environmental safeguards policies and felt unable to continue as cooperating institution."

Supporting sentences: para. 253, "The World Bank acted as cooperating institution for VODP until
August 2004"; para. 254, "UNOPS took over from the World Bank as cooperating institution in September
2004"; para. 46, "Nevertheless, the World Bank was concerned about compliance with its internal
environmental safeguards policies and felt unable to continue as cooperating institution."

### The US$52 million figure cited elsewhere on the map from The Ecologist — resolved

These are two different loans for two different phases, not a discrepancy.

- **Phase one (VODP)**, the project this evaluation covers: IFAD loan of US$20 million, Executive
  Board approval April 1997, total cost originally US$60 million.
- **Phase two (VODP2)**: IFAD, *President's report ... Vegetable Oil Development Project — Phase 2*,
  EB-2010-99-R-19, Ninety-ninth Session of the Executive Board, Rome, 21-22 April 2010, proposes an
  IFAD loan of **SDR 33.5 million (approximately US$52 million)** against a total project cost of
  US$147.23 million, with cofinancing from Oil Palm Uganda Limited (US$70.38 million), the Kalangala
  Oil Palm Growers Trust (US$5.48 million), an SNV grant (US$0.34 million), an IFAD grant (US$1
  million), the borrower (US$14.14 million) and beneficiaries (US$3.90 million).

So The Ecologist's US$52 million is the phase-two loan approved in April 2010, not the 1997 loan. Any
card carrying US$52 million should say it is the phase-two loan and date it to 2010; a card carrying
US$20 million should say it is phase one and date it to April 1997. The two should not be presented
as competing figures for the same money. The evaluation itself never mentions US$52 million — its
full text was searched and the figure does not occur — because it predates phase two's approval and
was written to prepare for "a possible follow-up phase of the project" (para. 1).

### The World Bank projects API claim — verified with a caveat

The claim "A search of the World Bank projects API for Uganda with oil palm, Kalangala or vegetable
oil returns nothing" holds. Queried directly at search.worldbank.org/api/v3/projects: "Kalangala"
returns total 0. "oil palm" returns 70 projects and "vegetable oil" returns 5, and no Uganda project
appears among them. Caveat for whoever repeats this: the API's country filter parameters did not
constrain the result set in these queries — the keyword results came back global — so the absence of
Uganda was established by reading the returned project list, not by trusting the filter. The claim is
sound, but it is an absence in a search index, which is weaker evidence than the evaluation's
positive statement that the Bank's role was supervisory and that no IDA money was involved. The
evaluation should carry the weight here, with the API search as corroboration.

**Weak points:**
- "for phase one" is the card's framing, not the evaluation's. The evaluation does not use "phase
  one"; it calls the project VODP and refers to "a possible follow-up phase" (para. 1). The framing
  is accurate in hindsight, since VODP2 followed in 2010, but the document does not supply the term.
- The entry says "private and government cofinancing" and omits the beneficiaries' US$3.1 million,
  which para. 35 lists alongside them.
- The entry retains "The Bank says its role was only supervisory work under a contract that ended
  before the oil palm investment." The evaluation does not support the second half: the Bank's
  supervision ran to August 2004, and the oil palm subproject began implementation in July 2003
  (para. 34, "implementation of the oil palm subproject began only in July 2003"), with the Bank
  "instrumental in pushing for a revised EIA and reappraisal of the project" and leading the
  technical review mission and mid-term review (para. 253). On the evaluation's account the Bank's
  contract did not end before the oil palm investment; it ended after that subproject was under way,
  and the Bank shaped it. That sentence is the Bank's own characterisation and should be marked as
  such, or checked against whatever Bank statement it came from, which was not supplied to this check.
- "The case still carries a World Bank lender key, which is under review" is an internal note about
  the map's data, not a sourced claim. Fine to keep, but it is housekeeping text on a public card.

---

## Nothing was left unopened

Every URL in the brief opened. The two IFAD URLs redirected from webapps.ifad.org to
members.ifad.org and served in full at the redirect target. No host refused service; no fetch failed
for want of a permission. The one claim in the records that a page could not be opened (Global Energy
Monitor, record 2) was tested and is false.
