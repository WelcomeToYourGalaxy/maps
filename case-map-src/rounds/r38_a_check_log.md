# Round 38, batch A — check log

Three cases in, three cases out. **No case cut.** All three corrected, one of them
substantially rewritten on new primary documents. Every `documented` claim tested and all three
held, one of them only after the evidence base was changed under it.

Documents opened by this check, each by name:

- CorpWatch, "Ugandan Villagers Say Chinese Phosphate Mine Cheated Them Over Land Titles",
  8 July 2016 — fetched over `curl`, read in full (about 3,600 words of page text, article body
  complete).
- Business and Human Rights Centre's extract of Edward Ssekika in Oil in Uganda, 8 July 2016 —
  fetched over `curl` on the second attempt, read in full (the page carries two paragraphs of the
  Oil in Uganda article and nothing more).
- Matooke Republic, 16 December 2016 — fetched over `curl`, article body read in full (18
  paragraphs).
- Daily Nation, "Court orders NLC to pay 4 in Mombasa for SGR land", 2 December 2019 — fetched
  over `curl`, article body read in full (31 paragraphs, no paywall truncation).
- judy.legal's publication of National Land Commission v Theresia Runji & 4 others, Court of
  Appeal, Civil Application 10 of 2020 — fetched; only the first three paragraphs of the ruling
  are published without a subscription, and that is all that was read there.
- kenyalaw.org: eleven judgments and rulings, through the route named below. Titles, courts,
  dates, parties and matching passages read; full texts not served.
- The Star, 6 December 2020, 4 March 2022 and 21 March 2023 — all three fetched over `curl` and
  read in full.
- Mzalendo's record of the parliamentary question (question 611) — read in full.
- Mzalendo's Hansard API record 929115 — the whole speech read; it carries no sitting date, as the
  writer said.
- AidData's full records 60236, 37103, 31777, 53111 and 58152, from the batch input's `full_text`
  block, and the live pages at china.aiddata.org for 60236, 37103 and 53111 (HTTP 200 each).

---

## The route the writer reported as failed, reopened

The writer recorded: "`https://new.kenyalaw.org/search/?q=Runji+National+Land+Commission` returns
HTTP 200 with a JavaScript-rendered result list and no results in the HTML ... The judgment was
therefore taken from judy.legal's published text and from the Daily Nation's report, and the High
Court judgment number is not stated."

That is a true statement about that route and a wrong conclusion about the document. The page the
writer loaded is a shell; the search endpoint behind it is
**`https://kenyalaw.org/search/api/documents/?search=<phrase>`**, which answers HTTP 200 with JSON
and is not challenged. Through it:

- the High Court judgment exists and is published: **Theresia Runji & 3 others v National Land
  Commission; Miritini Free Port Limited (Interested Party), Constitutional Petition 17 of 2018,
  [2019] KEHC 1994 (KLR), 12 November 2019**;
- so does the 20 November 2020 Court of Appeal ruling that judy.legal paywalls ([2020] KECA 185);
- so do five later rulings in the same dispute, running to **20 February 2026**;
- and so does a body of eight further Kenyan proceedings over the Kibwezi–Mutomo–Kitui–Migwani
  road, which the Kibwezi card did not have at all.

The individual judgment pages (`/akn/ke/judgment/...`) answer this client with **HTTP 202 and an
Amazon Web Services firewall challenge page** (`awswaf.com/challenge.js`), so full texts were not
served; `https://api.laws.africa/v3/akn/ke/judgment/keca/2024/1483/...html` answers **HTTP 403
"Permission Denied"**, and `services.kenyalaw.org` is not resolvable from here. A WebFetch of the
judgment page was **not sent at all**: it returned `PROVENANCE_REQUIRED` because an earlier
permission request was not answered in time. That is the shape CHECK31 warns about and it is
recorded here as a client-side failure, not a host refusal. Every string used from these documents
was confirmed as an exact phrase match inside the named document through the search endpoint, and
every URL put in `sources` was taken from the publisher's own `data-frbr-uri` attribute rather than
constructed. Each card now says, in `confidence_note`, that these documents were read through the
index and not in full, and states no outcome for any ruling whose result was not read.

`www.oilinuganda.org` and `oilinuganda.org` both fail at the egress gateway with
**502 to CONNECT (connect_unreachable)** — the site itself appears to be down, not blocked; the
Oil in Uganda material is carried through the Business and Human Rights Centre's extract, as the
writer did.

---

## sukulu-phosphate-osukuru-land (Uganda) — KEPT, corrected

### Verified
- "awarded 26.5 square kilometres", "could displace as many as 12,000 people in 14 villages",
  community dropping its opposition in exchange for titles, 30 million shillings (US$8,750) an
  acre for a 99-year lease, Henry Okwalanga's house — all in CorpWatch, 8 July 2016, verbatim.
- Rose Tibita's quotation, word for word, in both CorpWatch and the Business and Human Rights
  Centre extract. "One of the hundreds of residents affected ... in Osukuru and Rubongi sub
  counties" is the Centre's extract, exactly as the card had it.
- "surface rights agreement" is the source's own term, not the writer's: "She was forced to sign a
  surface rights agreement without knowing the contents of the contract". A correction considered
  and rejected.
- ABMAK Associates as "the law firm that handled the transaction" — the extract's own words.
  Another correction considered and rejected.
- Vincent Matano's quotation, verbatim in CorpWatch.
- Matooke Republic: "OVER 4,600 families", "only 123 out of 4,800 families have received any
  compensation payment", the Tororo District Council and Government condition to compensate all
  persons living on the land and evict no one and the company's default on it, Jackson Oryema's
  quotation, the unnamed district official on August 2014 and inflation, the 99-year-for-21-year
  leases, the spousal consent allegation, Emmanuel Osuna, and all four of Martin Orochi's
  statements including "just a fraudster" — all verbatim.
- AidData 60236: licence of 1 August 2013, loan of US$240 million on 4 December 2015, Sinosure
  insurance, 23rd Metallurgical as contractor, commissioning 24 October 2018, the 50,000-tonne
  trial batch, the mining-lease cancellation, the US$60 million withheld, the up-to-US$520 million
  facility.

### Corrections, each with the sentence that made it
1. **Selective quotation of the company's lawyers.** The card quoted "We are not one hundred
   percent clean, but this ... should be a case study" and dropped the two clauses around it in the
   same CorpWatch paragraph: "The lawyers say that they believe that they did an 'excellent' job of
   compensating the villagers" and "Even when you do everything well, they [NGOs] will still find
   something to complain about." Both added. The Centre's extract also ends Kusasira's account with
   the compensation being "commensurate with the 99 year lease", which the card dropped; added, and
   also noted in `confidence_note`.
2. **A reason dropped from the lender's own record.** The card's `outcome` had "ICBC withheld
   disbursements", and AidData gives two distinct reasons in two sentences: disbursements withheld
   "because of legal challenges facing the company", and the US$60 million withheld "due to the
   introduction of a new policy that required ICBC to lower its overseas loan centralization
   ratio". Both now in `lenders[0].role`.
3. **Coordinates: one record, two answers.** The card's point note said AidData gives 0.623611,
   34.153611 "for the plant site", about 4 km from the card's own coordinate, and left the reader to
   wonder which is right. AidData's location narrative also links
   `openstreetmap.org/node/2229128058`, and a Nominatim lookup of that node returns
   **"Sukulu, Tororo, Eastern Region, Uganda", 0.6593486, 34.1515704** — the card's coordinate
   exactly. So AidData gives the location two ways and the card uses the node AidData itself links.
   `point` now says that.
4. **Footprint (test 7).** Nothing on the card said which part of the complex the credit paid for.
   The credit part-financed the fertiliser plant contract; Orochi puts "the total project area of
   the Sukulu Phosphates Factory alone" at **600 acres – excluding the mining areas**, while the
   land complaints run across the 26.5 km² awarded for the whole complex. The 600-acre figure is
   now on the card and the mismatch is stated in `confidence_note`, with the two facts that hold
   the link: the borrower is the company that took all of it, and AidData records the loan as part
   of a larger US$620 million investment in that complex.
5. **Timing (test 3).** The card gave no sign that the land dealing predates the loan. The district
   official says compensation "should have been done by August 2014"; the loan was signed
   4 December 2015. Stated in `confidence_note`, together with what carries the overlap: the
   non-payment and the missing titles are recorded during and after the loan.
6. **An allegation reported as a fact.** "spousal consent rules were not followed and some forms
   were pre-signed" against Matooke Republic's "the spousal consent requirements were not followed
   in all cases as some forms had been allegedly pre-signed". Restored.
7. **"carbonatite" is in no cited document.** `ecosystem` opened "The deposit is the Sukulu
   carbonatite complex" with a CorpWatch citation; CorpWatch never uses the word. (It appears only
   inside the Chinese project title in AidData's staff comment.) Replaced with what CorpWatch does
   say: the 2008 Madhvani survey, the 206 million tonnes, and the government signing instead with
   Guangzhou Dong Song in late 2014.
8. **A present-tense office.** "The Tororo district chairperson Emmanuel Osuna" — Matooke places
   that at the time the project started, and CorpWatch of July 2016 names Apollo Jaramogi as the
   newly elected district chairman. Now "the Tororo district chairperson when the project started".
   Not a conflict between the sources, and not written up as one.
9. **"could displace"** → "the **planned** development could displace", CorpWatch's own qualifier.
10. **Source citation.** The cited BHRRC URL carries a typo ("decy") and redirects to the canonical
    page with HTTP 200 — a real resolution, not a dead link, but replaced with the canonical URL.
    The publisher has also renamed itself: the page is headed **Business and Human Rights Centre**,
    and the card said Resource Centre. Corrected in `sources`, in `community` and in
    `confidence_note`.

### `documented` — holds
Three sources outside the lender: a Ugandan reporter's article (through the Centre's extract), a
Ugandan weekly, and CorpWatch, with the company's own lawyers answering in two of them and the
Resident District Commissioner denying the claims in the third. Limb (b) is land taken under
99-year surface rights agreements from named people — Tibita, Matano, Oryema — with 123 of 4,800
families paid at the end of 2016 and no titles issued. Nothing here rests on the lender.

### Considered and not changed
- The 12,000-people and 14-village figures stay out of `displaced`; the `displaced_note` is right
  and says why.
- The flagged AidData sentence (two finance ministry officials jailed for a US$50,000 bribe) stays
  off the card. It is an anti-corruption prosecution of officials, not harm to identifiable people,
  and the writer was right to leave it.
- "No later record was found of land titles being issued" and similar passive absence statements
  are the map's own convention (245 instances across the 1,176 live cases, in `whole`,
  `displaced_note`, `confidence_note` and `outcome`), so they were not rewritten as researcher
  voice.

---

## sgr-phase-1-miritini-allottees (Kenya) — KEPT, substantially rewritten

This is the card the reopened route changed. The writer wrote that "the result of that appeal
application is unknown and the High Court judgment itself was never opened". Both are published.

### Verified
- Every figure and finding the card took from the Daily Nation of 2 December 2019 is in that
  article verbatim: the abuse of statutory powers, the unconstitutionality for want of a hearing,
  the missing notice of intention to acquire, the direction to tabulate, assess and compensate
  parcels 3912 and 3913/VI/MN at the date of acquisition plus interest at commercial rates, the
  "money has already been disbursed and the petitioners left without land" quotation in full,
  the entitlement to damages, Gikandi Ngibuini's argument, the Bombolulu eviction, the commission's
  no-evidence argument, Miritini Free Port's abuse-of-process answer, the unchallenged registered
  ownership of the undisputed part, and the judgment covering only the two parcels.
- judy.legal's published opening of the Court of Appeal ruling carries the 22.11 Ha of plot
  MN/VI/4805, the Kshs 1,475,486,845, Petition 17 of 2018, the letters of allotment of 2000 and the
  commission's denial.
- AidData 37103 and 31777: the two agreements of 11 May 2014, US$2,003,584,028.87 revised to
  US$1,903,404,827.42, Libor plus 3.6 per cent, 15.25-year maturity, Sinosure, the US$1.6 billion
  preferential credit at 2 per cent with 20.25-year maturity, the on-lending to Kenya Railways, the
  escrow and take-or-pay arrangements, the 1.5 per cent Railway Development Levy, completion on
  31 May 2017, and the loss and default figures.

### Corrections, each with the sentence that made it
1. **The appeal outcome was on the record and the card said it was not.** Replaced "no public
   record of the result of that application, or of payment to the four, was found" with what the
   record shows: a stay of execution granted by the Court of Appeal —
   "[d] There is an order of stay of execution of the judgment herein issued by the Court of
   Appeal" ([2024] KEHC 13399, 25 October 2024) — and, in [2026] KEHC 1857 of 20 February 2026,
   "Since the orders for stay of execution of the judgment have not been varied, reviewed" and that
   to execute the judgment "would be an exercise in futility". Eleven years after the January 2015
   acquisition notice, the judgment in the four's favour is unexecuted. That is the limb-(b) harm
   persisting, documented, and the card now carries it.
2. **A figure given two ways, resolved silently.** The card printed Kshs 1,475,486,845 alone. The
   Court of Appeal ruling of 20 November 2020 gives **1,475,486,845**; the High Court judgment of
   12 November 2019, the High Court ruling of 23 July 2018 and the Court of Appeal ruling of
   25 October 2024 all give **1,475,486,485**. Both now printed with where each appears, and no
   reconciliation offered.
3. **A manufactured conflict, removed.** The card presented the names as a disagreement between the
   court record and the Daily Nation — "the court record gives Theresia Runji, Marieta Gitonga
   Chege, Naomi Kiio and Sammy M. Kara, and the Daily Nation gives Theresa Runji, Marieta Gitonga,
   Naomi Kiio and Sammy Macharia". The court record itself carries both forms: [2019] KEHC 1994
   reads "the four squatters: Theresa Runji, Sammy Macharia Kara, Naomi Kio and Marieta ...". The
   Nation's forms are variants inside the record, not a second account. Rewritten as variation
   within the record. The fourth petitioner is now named **Sammy Macharia Kara** on the card, which
   is the court's own full form and reconciles the two.
4. **The money conflict was the wrong conflict.** The Nation's "Sh1.4 billion and another
   Sh360,000" is not a competing figure for the same thing: the court records a **further
   interruption award of Kshs 360,000,000** ([2018] KEHC 5280, [2019] KEHC 1994, [2024] KECA 1483).
   The interruption award is now on the card and the Nation's figure is noted against it.
5. **A judgment with no date.** The card dated nothing. The judgment is dated **12 November 2019**
   ([2024] KECA 1483: "Ogola, J.) dated 12th November, 2019 in Constitutional Petition No. 17 of
   2018"). The Daily Nation of 2 December 2019 reports it as made "on Monday"; both are stated and
   the publication date is not used as the event date.
6. **The acquisition date.** [2024] KECA 1483 records that in **January 2015** the public was
   informed that the Government of Kenya intended to acquire the 22.11 Ha, and the Nation gives the
   commission's **decision of 1 December 2015**. Both added; they support `start: 2015`, which the
   card asserted without a document.
7. **"part of the same land"** was a resolution. The record says the letters of allotment of 2000
   were for the suit property, and the High Court treated parcels 3912 and 3913/VI/MN as its
   disputed part. Rewritten to the record's own shape.
8. **A third party dropped.** The judgment holds that registration of the disputed part under
   **Miqdad Enterprises** was illegal because done in violation of an order. Added; it is part of
   how the parcels moved.
9. **The counterpart share, two ways in one record.** AidData says the loans financed 90 per cent
   with "the remaining 10% ... paid by Kenya Railways Corporation", and in another sentence calls
   "the Kenyan government's portion (15%) of the project (commercial contract) cost". Both now in
   `conditions`, unreconciled.
10. **The line's length, two ways in one record.** AidData's description says 485 km, its location
    note says 475 km. Both now in `whole`.
11. **A date attached to the wrong event.** The card had "In July 2022 Kenya received overdue
    repayment notices ... and local media reported a default". AidData puts the settlement notes in
    July 2022 and the media reports of default in **October 2022**. Separated.
12. **The arrests over this very subject were missing.** The batch's own flagged sentences for this
    financing are Reuters' report that the chairman of the National Land Commission, Mohammed
    Abdalla Swazuri, and the managing director of Kenya Railways, Atanas Kariuki Maina, were among
    18 arrested on suspicion of corruption over land allocation for the railway, in an investigation
    "centers on allegations that officials siphoned taxpayer money through [fraudulent] compensation
    claims for land used for the railway". The writer rightly refused it as harm, and then left it
    out altogether — on a card whose whole subject is the commission's handling of compensation for
    SGR land at Mombasa. Added to `whole` as context, attributed to Reuters as quoted in AidData,
    not to AidData itself.
13. **`point`** now names the OpenStreetMap node (44927918) that the coordinate came from, which
    Nominatim returns at -4.0035480, 39.5783392 — the card's coordinate to five decimals.

### `documented` — holds, and is now much stronger
A published national court record plus a national newspaper's report of the judgment, neither of
them the lender or the lender's agent. CHECK20 §3 names a court record as grounds for `documented`.
The card discloses that the judgments were read through kenyalaw.org's search index and not in
full, and states no result for rulings whose result was not read.

### The point already occupied (test 6)
The coordinate sits **about 280 m** from `mombasa-mariakani-jomvu-evictions` (-4.0022, 39.5805),
which is also in Jomvu Kuu ward and also starts in 2015, and about **2.4 km** from
`kenya-sgr-cargo-directive`, whose point is the Mombasa SGR terminus — which is at Miritini. The
reason for a new case at that point: different works (the Mombasa–Nairobi railway, not the
Mombasa–Mariakani highway), different lenders (China Eximbank, not AfDB/EIB/KfW/EU), different
parcels (MN/VI/4805, not the road reserve at km 10+700 to 11+450), different people (four allottees,
not the 126 complainants and about 180 structures of May 2015), and a different harm from the
cargo-directive card (land acquisition, not job losses). The two Kenya cases in this batch are not
the same episode: Mombasa railway 2014–2026 against a Kitui–Makueni road 2016–2025. It is not a
duplicate, but it is the closest two `lk:cn` points on the map and worth the lead knowing.

---

## kibwezi-kitui-road-compensation (Kenya) — KEPT, corrected and newly sourced

The writer named this its weakest entry and asked a specific question: "whether any National Land
Commission or Auditor-General document counts the parcels and the payments on this road." No such
counting document was found — but the question was pointed at the wrong archive. Kenya's courts and
its statutory Land Acquisition Tribunal have been adjudicating claims over this road's compulsory
acquisition since 2018.

### Verified
- The Star, 6 December 2020: "About 5,000 land owners are crying foul over the failure to compensate
  them for land taken for tarmacking of the 172-kilometre Kibwezi-Kitui-Migwani road"; Michael
  Kivoto on the defunct Kitui County Council allocations and "only for the buildings to be brought
  down without anyone talking of compensation"; the court cases and the lawyers' fees; the
  depression; "the delegation of 26 persons that met Kalonzo".
- The Star, 4 March 2022: "The project displaced about 5,000 persons who either lost their land,
  homes and business premises"; "demanding Sh1.6 billion in compensation"; "yet to be fully
  compensated five years after the project commenced"; the demonstration outside the county
  commissioner's office "on Thursday, March 3" with the page's own dateline of 04 March 2022;
  Joseph Wambua's and Kanini Kitili's words; Dorcas Rono's "We would like to assure you that we
  shall follow up this issue".
- The Star, 21 March 2023: "about 5,000 title owners who were relocated"; "wallowing in poverty
  despite having been pushed out"; completion in May 2022; Sinohydro; the Kibwezi East MP.
- Parliament's record of the question, in full: "The Member for Kibwezi West (Hon. Mwengi Mutuse,
  MP)", the 2017 acquisition, the review-upwards request, "No response recorded yet", status
  Pending. The page's "Last updated 2 Jul 2026" is a page timestamp and was correctly not used.
- The Senate speech, in full: the officers of the commission "reviewing the awards downwards",
  "after two months, an officer comes and tells them they have reviewed the award downwards by a
  very big margin", "Issues of compensation, pollution and Corporate Social Responsibility (CSR)
  ... are very serious", and "Last week, I led a delegation of persons affected by the project from
  Kitui Township to the NLC". No sitting date in the record, as the card says.
- AidData 53111 and 58152: the agreement of 29 November 2016, 85 per cent of KES 50 billion of
  commercial contracts, 472 km in three phases, Phase 1 of 192 km at KES 23 billion, the
  US$418,578,082.97 estimate, 15-year maturity and 3 per cent, debt-register number 2016052, the
  53 per cent completion in May 2019 against 15 February 2021, the delay list, and the noise and
  dust complaints.
- The company name is not a conflation by the writer: AidData's own sentence is "China Hydropower
  International Co., Ltd (中水电国际公司) -- also known as Sinohydro -- is the contractor". A
  correction considered and rejected.
- The `relief_or_disaster_language` screen flag fires on "COVID-19 cases reported in Kitui" inside
  a list of construction delays, exactly as the writer said. The money did not respond to a
  disaster.

### Corrections, each with the sentence that made it
1. **A `point` justification that the source does not support.** The card said the point was
   "Kitui town, where those affected gathered at the county commissioner's office in December 2020
   and March 2022". The December 2020 report describes a delegation travelling to meet Kalonzo
   Musyoka — "the delegation of 26 persons that met Kalonzo" — not a gathering at the county
   commissioner's office, and gives no place for that meeting. Rewritten to the March 2022
   demonstration and the senator's delegation "from Kitui Township", both of which are in the
   documents, with the road's course taken from AidData's description rather than from The Star's
   length figure. The coordinate itself is right: Nominatim returns Kitui town (node 44933078) at
   -1.3666000, 38.0166000.
2. **Four court and tribunal records added.** Each verified as an exact phrase match in the named
   document and each tied to this road by the document's own words:
   - *Daniel Muema Joel & 21 others v National Land Commission & 2 others*, Case No. 47 of 2018,
     Environment and Land Court, ruling of 20 September 2019 — "DANIEL MUEMA JOEL & 21
     OTHERS.........PLAINTIFFS/APPLICANTS ... VERSUS NATIONAL LAND COMMISSION........1ST
     DEFENDANT/RESPONDENT SINOHYDRO", "The Plaintiffs are seeking for an order of injunction
     restraining the Defendants", and "of the suit land by the Defendants is for the purpose of
     constructing the Kibwezi[-Mutomo-Kitui-Migwani] Road".
   - *Ravaspaul Kyalo Mutisya v National Land Commission*, [2022] KEELC 881, 8 March 2022 —
     "building that was under construction and excavated his land to construct the
     Kibwezi-Mutomo-Kitui-Kabati-Migwani", "was to be part of the land to be acquired by the
     Respondent for construction of".
   - *Kitheka & 2 others v Kenya National Highways Authority & another*, Environment and Land
     Appeal 38 of 2021, ruling of 22 July 2024 — "the Plaintiffs' properties for purposes of
     compulsory acquisition to pave the way for the construction of the
     Kibwezi-Mutomo-Kitui-Kabati-Migwani (A9/B64)".
   - *Mulu & 55 others v National Land Commission & 2 others*, Land Acquisition Petition E038 of
     2024, Land Acquisition Tribunal, judgment of 2 December 2025 — "acquisition of parcels of land
     said to be required for the Kibwezi – Mutomo – Kitui –Migwani", "PAPs were compulsorily
     acquired by the government for the construction of".
   Four more proceedings over the same road were found and left off the card for want of a read
   text: Geoffrey Muluvi v Kenya National Highway Authority [2020] KEHC 6027 (15 May 2020), Muluvi
   v KeNHA [2022] KEELC 14866 (16 November 2022), Peter Kitheka & 2 others v KeNHA [2022] KEELC 627
   (22 March 2022), Kyambia & 10 others v KeNHA [2024] KEELC 226 (23 January 2024), Kiema & another
   v NLC [2025] KELAT 169 (8 May 2025) and Mutisya v Chairman, NLC [2025] KEELC 7949 (16 October
   2025). No outcome is stated for any of them, on or off the card.
3. **The absence claim answered as far as it can be.** `outcome` now says claims over the
   acquisition were still before the Land Acquisition Tribunal in December 2025, which is what the
   record shows, before "No record of payment was found".
4. **The speaker's own qualification, dropped.** The Senate speech ends "I want to declare my
   interest in this matter. I come from Kitui County where the longest section of that road passes
   through." The card rested the downward revision of awards on that speech and did not say that.
   Added to `confidence_note`.
5. **AidData's own uncertainty about the loan, dropped.** The record notes that Kenya's project
   monitoring system lists two loans for this road, of US$212.8 million and US$206,134,747.16, and
   that "It is unclear if these records refer to different projects". Added to `lenders[0].role`,
   beside the US$418,578,082.97 estimate the card already carried.
6. **Two length figures and two start dates, now both printed.** The Star gives 172 km and AidData
   gives Phase 1 as 192 km of 472 km; The Star says the project was launched by President Kenyatta
   in 2017 and AidData says construction began on 6 December 2016. Stated in `confidence_note`
   without reconciliation.

### `documented` — holds, and no longer marginal
As submitted this card rested on one newspaper, a parliamentary question that presupposes the
delay rather than finding it, and one senator's speech. That is thin for `documented`, and it was
the writer's own worry. It now rests additionally on seven years of Kenyan court and tribunal
proceedings by named claimants — 22 plaintiffs in 2018, 56 petitioners whose tribunal judgment is
dated December 2025 — over compulsory acquisition for this road. Limb (b) is land and shops taken
with compensation unpaid, and the identifiable people are Kivoto, Wambua, Kitili, Mutisya, Joel,
Kitheka and Mulu. Nothing rests on the lender.

### Considered and not changed
- The "about 5,000" stays out of `displaced`; the `displaced_note` sets the three descriptions
  side by side, which is the right handling.
- The Kibwezi East / Kibwezi West discrepancy stays printed both ways.
- "3 March 2022" was questioned under the no-dates-from-timestamps rule, because the caption gives
  only "Thursday, March 3". The year is fixed by the page's own printed dateline, "04 March 2022 -
  10:04", which is text on the page and not the URL, and 3 March 2022 was a Thursday. Left as is.
- The question's reference to "parking for lorries in Kibwezi Town" was not added; the card's
  subject is the road and the acquisition year is already stated.
- Kalonzo Musyoka's "although the tarmacking of road had brought good tidings for locals" was
  weighed as a dropped favourable clause and left off: the card's `whole` already carries the
  road's benefits at length, from The Star and AidData, so the balance is not one-directional.

---

## Answers to the standing questions

**1. What could not be checked, and what stopped it.** The full texts of the eleven kenyalaw
judgments: `/akn/ke/judgment/...` answers this client **HTTP 202 with an AWS WAF challenge**;
`api.laws.africa/v3/...` answers **403**; `services.kenyalaw.org` does not resolve; a WebFetch was
**never sent** (`PROVENANCE_REQUIRED`, an unanswered permission request). Phrase-level verification
through `kenyalaw.org/search/api/documents/` stood in for reading them. The result of every
appellate and tribunal ruling is therefore unknown and is stated nowhere. Oil in Uganda's own site
is unreachable at the gateway (502 to CONNECT, both with and without `www`). The writer's other
named failures were re-checked and stand as recorded: gem.wiki 403 behind Cloudflare,
cavac.at 410, monitor.co.ug 403, the Doga Dernegi PDF a scan, and no sitting date in Mzalendo's
Hansard record.

**2. Figures where documents disagree, left unreconciled.**
- Kshs 1,475,486,845 ([2020] KECA 185) against Kshs 1,475,486,485 ([2019] KEHC 1994, [2018] KEHC
  5280, [2024] KECA 1483). One of these is a transposition in a court record and no document says
  which.
- The Daily Nation's "another Sh360,000" against the courts' interruption award of Kshs 360,000,000.
- AidData 37103 on counterpart financing: "the remaining 10%" against "the Kenyan government's
  portion (15%)".
- AidData 37103 on the line: 485 km in the description, 475 km in the location note.
- AidData 53111's 192 km Phase 1 against The Star's 172 km road.
- AidData 53111's construction start of 6 December 2016 against The Star's 2017 launch.
- Matooke Republic's "OVER 4,600 families" against "4,800 families" in the same article.
- AidData 60236's two locations for the same site, 0.623611/34.153611 against the node it links.
All printed on the cards with where each appears. One claimed disagreement was removed as
manufactured: the petitioners' names.

**3. A fault in more than one card.** Two, both structural rather than careless.
- **A single-source reading accepted because the second source was behind a wall.** Both Kenya
  cards were written as if Kenya's case law were unreachable, and both gained a primary court
  record once one endpoint on the same host was tried. The lesson is narrower than "try harder":
  `kenyalaw.org/search/api/documents/?search=<phrase>` is a working, unchallenged, phrase-exact
  index of Kenyan judgments, gazettes and cause lists, and it should go into the round notes.
- **A figure resolved rather than printed twice.** Four instances across the three cards (the two
  Kshs figures, the 10/15 per cent, the 485/475 km, the two Sukulu coordinates). The writer handled
  this well where it knew of the conflict — the 4,600/4,800 and the three descriptions of the 5,000
  are both printed properly — and missed it wherever the second reading sat in a different part of
  the same document. That is the same place CHECK20 says to look: the annex, not the body.

**4. Anything wrong in the card data outside the fields asked about.** `lenders[0].role` was read
against the documents on all three cards. Two faults: the Sukulu role dropped both of AidData's
stated reasons for withholding, and the Kibwezi role dropped AidData's own statement that it cannot
tell whether one loan or two is recorded. The SGR role is accurate in every figure and term. In
`companies`, ABMAK's role was slightly overstated as having handled "the land transactions" where
the source says "the transaction" — corrected and the citation moved to Oil in Uganda, which is
where the statement is. No oversight or civil-society body is listed beside a harm-causing agency
on any of the three.

**5. Routes that failed, named as routes, not as hosts.** Listed in full above. None of them is a
host block: kenyalaw.org served a JSON search endpoint to the same client that its judgment pages
refused; business-humanrights.org answered 429 to the first request and 200 to the second five
seconds later; the BHRRC URL's 404 was a path error on my part and the card's own URL redirects to
a live page.

## Structural checks
`cases` and `extend` at the top level, `extend` an empty **array**. All 24 keys merge.py asserts
present on all three cases; `mechanism: "project"` valid on all three. **No `kind` on any case** —
consistent with all 93 live `lk:cn` cases. **No `displaced` field at all**, so no `displaced: 0`;
the reasoning sits in `displaced_note` on all three. `ap: true` on all three, which is right: a
village, a suburb and a town. `ct` values (`tied`, `repay`) and `rg` ("Africa south of the Sahara")
match live values. No case id collides with the 1,176 live cases. No researcher voice: every first
person on the three cards is inside a quotation.
