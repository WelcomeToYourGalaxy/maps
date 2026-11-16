# Round 37, batch B — check log

Checker's own file: `r37_b_checked.json`. Writer's file: `r37_b.json`; writer's report: `r37_b_report.md`.

**Result: 3 cases in, 1 kept (corrected), 2 cut. 2 extends in, 2 kept, both corrected.**
Both cuts are the two entries the writer named as its weakest. Both were named accurately.

Every document below was opened and read in full, from the writer's cache at `/tmp/r37b/` where it
was there and from a fresh fetch otherwise. Every URL in the surviving entries was requested and
returned 200 (list at the end).

---

## CASE 1 — `karimenu-ii-dam-compensation` (Kenya): KEPT, nine corrections

### Forward rule
Limb (b), comfortably. Not a relocation verb: 28 counted claimants at a named site left unpaid in
phase one (The Star, 26 February 2020), buffer-zone compensation unpaid as at 13 September 2025 on
the implementing agency's chief executive's own statement (Capital FM), Sh4.2 billion recorded as
owed, and three affected people named in the reporting (Zipporah Wanjiru, Jackson Mbugua, Simon
Nguyai Timothy). Test 1: China Eximbank's US$200,530,600 loan disbursed US$146.5 million across two
Kenyan financial years and the dam was built, so the harm sits on the thing the money paid for.
Test 3: loan 14 February 2017, harm 2017 to 2025.

### Verified against the documents
- **Lender role**, every figure, against AidData record 58737 (page fetched, `china.aiddata.org/projects/58737/`, 200): US$200,530,600 signed 14 February 2017 to the AVIC & SMEDI joint venture; 85 per cent of a US$235,918,461 EPCF contract; final maturity 21 July 2042; 20 equal semi-annual instalments; disbursements US$13,364,912.29 in FY2020-21 and US$133,093,268.26 in FY2021-22; US$158,254,011.75 outstanding at 30 June 2022. All confirmed, exactly as the record states them.
- **600 / 171 / 429 acres**, confirmed: "The project requires the acquisition of 600 acres of land: 171 acres during phase 1 for the dam's embankment and water draw-off structures and 429 acres during phase 2 for the reservoir area."
- **1 August 2019 figures**, confirmed against The Star of that date (date taken from the article's own "News 01 August 2019 - 13:47" line, not the URL): "The CS said the government has already given 246 affected people Sh1.28 billion in compensation for their 171.6 acres in Phase I." Mbugua and Wanjiru quotations exact.
- **26 February 2020 figures**, confirmed: "So far, 228 have been compensated at a cost of Sh1.09 billion. Compensation for the remaining 18 PAPs and an additional 10 who arose out of subdivision of some parcels of land is ongoing"; "The contractor has access to 136.5 acres out of the 171 acres required for phase 1"; "The remaining 34.5 acres are critical to the completion of the diversion tunnel and construction of the water intake tower and bridge."
- **20 September 2023**, confirmed (article's own "News 20 September 2023 - 16:54"): "a record 150 acres of land has been affected by the constant backflow from the dam"; "The dam is complete and now the residents are suffering instead of benefiting."
- **13 September 2025**, confirmed (Capital FM's own "13th Sep 2025"): Kamau quotation exact; valuation with the National Land Commission; "by October we should see movement"; "Kamau conceded the process was behind schedule"; Simon Nguyai Timothy; "In September 2023, President William Ruto directed then-Water Cabinet Secretary Alice Wahome to settle Sh 4.2 billion owed to the affected families"; "commissioned in August 2022".
- **Coordinate.** The writer's report is right and I confirmed it independently. Nominatim's search for "Karimenu II Dam" returns OSM way 1423111416 at -0.9112190, 36.8578364, display name "Karimenu II Dam, Gituamba ward, Gatundu North, Kiambu, Kenya" — exactly the card's point, so `ap: false` is correct and "Gituamba ward" is sourced. AidData's record links OSM node 44931883, which the OSM API returns as `{"name":"Kiriko","place":"village"}` at -0.6666, 37.4000; reverse geocoding puts that at "Gathigiriri ward, Mwea East, Kirinyaga, Kenya", about 66 km north-east of the dam (the writer said about 60 km). Two different villages called Kiriko. AidData's *prose* ("at Kiriko in Gatundu North Sub-County") is right; only its coordinate link is wrong.

### Corrections made
1. **`companies[0].role`: a date attributed to a document that does not carry it.** The card dated the construction contract "signed 24 April 2017 (AidData record 58737; The Star)". AidData gives 24 April 2017; The Star of 26 February 2020 says the opposite: "The contract for the construction of the dam was signed in May 2017." The Star citation removed from that clause and **both dates printed in `confidence_note`**, unreconciled.
2. **Selective quotation, The Star, 1 August 2019.** The card took the residents' threat to block the works and dropped the two favourable clauses from the same article: "the ministry has a budget for compensation for Phase II, adding that money will be disbursed to the National Land Commission once the valuation has been done" and "The government will not touch anyone's land or properties including the crops and trees grown on the land until they are fully compensated." Both added.
3. **Selective quotation, The Star, 26 February 2020.** The card gave the 28 unpaid and dropped the agency's stated reasons, which are in the same statement: "The slow process of land acquisition by the National Land Commission is delaying construction"; "lack of funds to compensate 28 Project Affected Persons"; "Succession and family disputes have also been delaying land acquisition." All three added.
4. **Selective quotation, The Star, 20 September 2023.** Added Muriu's "the compensation deadlock was more of a budgetary issue" and his and Thang'wa's statements that the money would not be diverted and that the meeting agreed compensation would be paid.
5. **A quoted figure with its preposition changed.** The card had the buffer zone "about 50 metres **above** the top water line". Kamau said "about 50 meters **from** the top water line". Corrected.
6. **Resolution of one document's two readings.** AidData gives phase two as 429 acres required and as 383 acres surrendered and unpaid in early 2021. The card printed 429 in `community` and 383 in `confidence_note` with no statement of the relation. `confidence_note` now prints both together and says the record does not explain the difference. The "early 2021" date is AidData's own, in the same sentence as the figure.
7. **`whole`: a figure given two ways.** Capital FM says "nearly one million residents"; AidData says "an additional 850,000 people". Both now printed. "Gatundu" restored to the list of places served (Capital FM and The Star both include it; the card had dropped it). "excavator operators" corrected to "earthmover operators", which is what the article says.
8. **`place` and `point`.** `place` was "Kiriko, Gituamba ward…", which picks one of the four villages The Star names ("Kiriko, Gathanji, Buchana and Kariminu villages in Gatundu North subcounty"). `place` is now the ward; `point` names all four villages, gives the OSM way id, and states the AidData coordinate problem with the node id and the distance. Phrasing moved off "this record".
9. **`conditions`: material the writer left out that bears directly on the harm.** Added, from AidData record 58737: the 20 per cent advance payment of US$47,183,692 in mid-2017 against a bank guarantee; the parliamentary committee's 28 March 2019 site inspection finding no works 24 months after signature; that "Athi Water Services Board had not yet issued a commencement to proceed letter to the EPCF contractor because of land acquisition challenges"; and the request to the Auditor General for a special audit. This is the document's own link between the unacquired land and the contract.

### Considered and rejected
- Changing `confidence` to `contested`. Rejected: the harm is carried by two independent Kenyan news organisations and by the implementing agency's own public statements, which is not the lender reporting on itself. `documented` stands.
- Removing the SAIS-CARI / Boston University face values. Verified in staff comment 3 of record 58737 and correctly attributed; kept.
- Putting the 383-acre figure into `community`. It rests on AidData's prose, whose underlying report (People Daily) the writer could not open and nor could I. Leaving it in `confidence_note`, named as AidData's only, is the honest placement.
- Adding the unverified "383 acres" source. Not attempted beyond the writer's route; see routes below.

---

## CASE 2 — `lamu-coal-kwasasi-land` (Kenya): **CUT**. The link test, in full.

This is the card the task asked me to test hardest. Everything on it about the land is true and
better sourced than the card claimed. It still has to come off, and the reason is not the evidence.

### What I verified
- **The land harm.** The Star, 11 August 2020 (article's own "News 11 August 2020 - 10:23"): "At least 975 acres were acquired in 2016 at Kwasasi village in Hindi division for the project"; Hussein Fadhil's quotation exact, including "We surrendered our land and moved out…We need our land back"; Mohamed Omar "Some of us didn't have any other land and we have been renting since 2016"; "According to a past review by the National Land Commission, an acre at the site would go for Sh800,000." The Standard, 9 July 2018 (article's own "Jul. 9, 2018"): 1,000 acres; chairman Abdul Rahman Aboud; Swazuri "the farmers would soon be paid… at least Sh800,000 per acre"; "the farmers complained the money was not enough". Limb (b) is met several times over, with named people.
- **The lender joint, and it is stronger than the card said.** The card cited Standard Bank's 2015 annual report only "as cited by AidData". I opened the report itself: `https://thevault.exchange/?get_group_doc=18/1461565691-SBG_FY15_Annualintegratedreport.pdf` returns 200, 2.8 MB, and page 47 reads "In the rest of Africa, Standard Bank and ICBC have concluded debt financing agreements with a consortium of Kenyan investors for the building of the 1 000 megawatt Amu coal-fired power plant." That is a primary document, from one of the two banks, and the writer did not have to lean on AidData for it.
- **And what cuts the other way.** AidData record 52499: the 8 June 2015 instrument is an **indicative term sheet**; "The export credit financing agreement was reportedly finalized in 2015, but the official commitment date is unknown"; the whole record is titled and statused **Cancelled**; no disbursement is recorded anywhere. The Star, 18 November 2020: ICBC never announced anything and did not answer the paper's questions, and the Chinese embassy's press attaché said "Not a single Chinese company is involved in it now." Construction never started.

### Verdict on test 1 and test 3
**Test 1 (documented link): holds, but only as a link to a proposed financing.** The term sheet and
the Standard Bank report document a relationship between ICBC and the project. They do not document
any lending: no commitment date, no disbursement, and AidData files the financing as cancelled.
**Test 3 (timing): overlaps on one reading and inverts on the other, and the card does not say so.**
The Star puts the acquisition in 2016, after the June 2015 term sheet. But Aboud, in July 2018, said
"The farmers whose land was taken have been waiting for five years", which puts the taking at about
2013 — two years before the term sheet and before the project was even tendered. The Star's own
standfirst of 11 August 2020 says "975 acres acquired five years ago" while its body says 2016, so
one document gives it two ways as well. The card flagged the acreage conflict (975 against 1,000)
and missed the date conflict entirely.
**The test it fails outright is the one BRIEF36 names: which part of the project the Chinese money
paid for.** It paid for no part. Nothing was built. And the reason the landowners are unpaid is
stated in the sources themselves — the project never took off, so the compensation never came. The
harm here follows from the financing *not* happening. A card that hangs it on ICBC says the opposite
of what its own sources say. That is the Burkina shape with the sign reversed, and it is also the
test the writer itself applied to kill G405 New Clark City in the same batch ("no Chinese money was
committed"); the two cannot be decided differently.

**Note for the owner, because this is a judgment and not a factual failure.** The land harm is real,
documented, and has named claimants. If the map wants cases of harm from land acquired for projects
that then collapsed, this is a good one — but under a `land` mechanism and with the collapse as the
cause, not under a Chinese export credit that never disbursed. Reinstating it as written would put
ICBC's name on a taking ICBC did not finance. Three further things would have to be fixed first: the
2013/2016 date conflict, the Standard Bank report cited directly rather than through AidData, and
the ambassador's statement (below).
**One selective quotation found while deciding, worth recording because it cuts *for* the link, not
against it.** The card quotes the attaché's denial and drops, from the same article, "On June 18 last
year, former Chinese ambassador Wu Peng said they were ready to talk the other Chinese investor,
PowerChina, out of the project, should the government dim it unfit." The Chinese ambassador treating
PowerChina as "the other Chinese investor" contradicts the attaché's "not a single Chinese company".
Both belonged on the card.
**Other errors in the card, recorded so they are not re-made:** `whole` said "Amu Power's chairman of
the local farmers' association said the project would give jobs to about 3,000 young people" — Aboud
is the chairman of the Kwasasi Farmers Association and has no role at Amu Power; the sentence
invents an affiliation. The card also dropped "at least" from Swazuri's "at least Sh800,000 per
acre", and placed the Chinese embassy "in Nairobi", which the article does not say. The 16 November
2020 date for Save Lamu's announcement is AidData's, not The Star's, but the card attributed the
whole sentence to The Star.

---

## CASE 3 — `addis-djibouti-railway-compensation` (Ethiopia/Djibouti): **CUT** on limb (b)

### What I verified
Every quotation and claim in `community` against The Reporter of 31 March 2018 (`thereporterethiopia.com/4722/`, read in full, date and byline from the article's own "By Yonas Abiye / March 31, 2018"). All of it is accurate:
- "several farmers have not been compensated despite their farmlands being damaged"; "thousands of 'tearful' farmers complained that they have not been treated fairly"; "Some get higher payment while others received a lower amount of compensation for the same plot of land. There are other farmers as well who did not receive compensation at all while their neighbors were paid"; "the corporation made payments for those farmers who threatened, while powerless poor people have been denied compensation".
- The MP's quotation is exact, including the woman with cancer.
- Fadil Ibrahim "confirmed to the standing committee that there have been unequal payments for similar farmlands. He cited the case of two kebeles where in one kebele, 25 birr has been given per square meter, while up to a maximum of 300 birr was given per square meter in another." Exact, and the card correctly keeps his exculpatory answer in the same paragraph ("the payment they concluded was in accordance with the valuation they received from local administration") rather than dropping it. The second quotation is exact. **No selective quotation on this card.**
- Lender role: every figure confirmed against AidData record 70086's text — US$2,490,760,000 of 15 May 2013, 15-year maturity, six-year grace, LIBOR plus 3 per cent, Sinosure, and the three tranches at US$1,289,029,000 / US$981,260,000 / US$220,471,000, plus Djibouti's separate US$491,793,000 (record 46183).
- People's Map of Global China: "conditional on procurement of Chinese railway technology and contractors" confirmed; "the first modern cross-border Standard Gauge Railway (SGR) and the first fully electrified railway route in Africa" confirmed; "the majority of the track is unfenced at the request of the ERC" confirmed, which is where the card's `killed_note` clause comes from.

### Why it is cut
The forward rule. **Limb (a):** no document gives a count of people or households relocated — the
writer says so itself and I found none. **Limb (b): the harm is not to identifiable people.** The
affected are "several farmers" and "thousands of farmers" somewhere along a 759 km corridor, and the
one concrete locational fact in the whole record is "two kebeles" that the document explicitly does
not name. CHECK31 sets the standing edge at `bukoba-airport-resettlement-arrears` — "compensation
unpaid in five identified resettlement cases at a named site, where the people are neither named nor
counted" — and says anything thinner is not limb (b). This is thinner on both of Bukoba's two
anchors at once: no named site and no count of cases. It is a rate attached to somebody, somewhere.
The ERC department head's admission is good material and the harm kind (land taken, compensation
unpaid) is the right kind; the people are the problem.

### What would revive it
A count, or a named kebele, or the Pulitzer Center piece (Tom Gardner) if anyone can open it. I
tried four routes and could not — see below. I also chased what search returned: both Addis Ababa
University theses that come back for this query (`etd.aau.edu.et/handle/123456789/7571` and
`/6785`) are the **South Wello / Amhara** study of the Turkish-built Awash–Weldiya line, the same
trap the writer identified in its cached `ejdr.pdf`. They are not this railway. I confirmed that
from their own title pages.

### Errors in the card, recorded for whoever writes it next
- **Two contract values attached to their pre-increase signing dates.** The card has CREC "Held the US$1,841,470,000 engineering, procurement and construction contract… signed 25 October 2011" and CCECC "Held the US$1,401,800,000 contract… signed 16 December 2011". Staff comment 3 of record 70086 says the opposite: "When the commercial contract for the Sebeta-Adama–Meiso Section… was originally signed on October 25, 2011, it was worth $1,639,031,409.00. Its value was increased to $1,841,470,000.00 on November 5, 2012. When the commercial contract for the Meiso-Dewanle Section… was originally signed on December 16, 2011, it was worth $1,197,400,000.00. Its value was increased to $1,401,800,000.00 on November 2, 2012." Both cards' figures are the 2012 values printed against the 2011 dates.
- **One document, two route lengths.** Record 70086 says both "a 750.224 km railway from Sebeta to Nagad" and "The 759 km Addis Ababa–Djibouti Railway". The card prints 759 only.
- **Two accounts of the restructuring, unreconciled on the card.** AidData: "a 20-year maturity extension and a 4-year grace period extension". People's Map: "extending the repayment period from 10 to 30 years", and separately that the 2018 non-repayment "was deferred for one year". The card prints AidData's only.
- **`ap: true` is correct** and the writer was right to set it: the point is Mieso, chosen because the two Chinese-built sections meet there, and no harm is recorded at Mieso.

---

## EXTEND 1 — `southern-expressway-sri-lanka`: KEPT, three corrections

The dedupe is right: confirmed by place (Pinnaduwa–Godagama, Galle and Matara districts) and by
years. Every figure in the lender role confirmed against AidData records 45520 and 95928, both
fetched (200): US$74,329,906 under BLA201011 for Package 1 and US$55,369,520 under BLA201012 for
Package 2, both committed 17 February 2011; six-month LIBOR plus 2.40 per cent, 15-year maturity,
four-year grace, 0.7 per cent commitment fee, 0.3 per cent management fee, 6 per cent Sinosure
premium; CNTIC's EPC contract of 11 June 2010, work from April 2011 to January 2014, section open
16 March 2014.

**Point 7 of my instructions — whether the card now reads as though the Chinese money caused the
Panel's displacement findings — checked and it does not.** The writer disclosed it and I tightened
the disclosure. Corrections:
1. **Hedge restored.** AidData says the April 2022 default "reportedly affected all China Eximbank loans with amounts outstanding at the time of the announcement". The card had asserted it. "reportedly" restored.
2. **Packages identified by their own end points** (Pinnaduwa to Kodagoda, Kodagoda to Godagama), which is how the record describes them; the card gave only chainages.
3. **`confidence_note` rewritten** to put the dates in the open — the Panel reported in 2005, the loans were signed in February 2011, six years later — and to scope the absence claim to the document that carries it rather than leaving it as a general negative. Record 95928 added to `sources_add`, because the lender role cites it and the card did not carry it.

Not changed, deliberately: `lk_add: ["cn"]`. China Eximbank really did finance Section IV of this
project, so the Chinese-lender tag is factually right; the `confidence_note` now says plainly that
the harm findings are the ADB Panel's and predate the tranche. Flagging it rather than removing it.

## EXTEND 2 — `myanmar-china-pipelines-land`: KEPT, five corrections

Dedupe right: same pipelines, same townships (Kyaukphyu, Maday Island), overlapping years. The
extend's real value is the `suppression` field, which was empty on the card.

Verified: AidData record 34197 page fetched (200) and it does say what the writer said — "Flow Type
• Grant", "Commitment date Jan 1, 2013", status "Pipeline: Pledge", funding agency CNPC, and the
4 million kyat / US$4,625 per hectare figures with "some residents claim that they received no such
compensation" and the CNPC official's vacant-land answer. RFA of 2 August 2013 (date from the
article's own "2013.08.02") and RFA of 26 September 2013 via ecoi.net document 1268827 (ecoi's own
"Veröffentlicht: 26. September 2013"; the writer's `/dokument/259275` is the former id and redirects
there) both confirmed line by line, including the six charged on 19 April, the twice-refused
permits, the ten jailed for three months under Article 18, the 300 from 20 villages, Ko Nyi Nge,
Htein Lin, the 100 security force members and firefighters, and Phil Robertson's quotation.
Narinjara of 24 February 2015 confirmed: fifty farmers, 12 villages, 19 February, U San Shwe's
quotation, the September 2013 payment, 385,000 kyat an acre, U Wai Dawn.

Corrections:
1. **A fact attributed to the wrong body.** The card said "officials of the pipeline's operators refused to accept the letter". RFA says it was officials of **MOGE and Daewoo International** — Daewoo is a stakeholder, not an operator of the pipelines. Named correctly.
2. **Selective quotation, RFA 2 August 2013 — and the omission cost the card its best figure.** The paragraph the card used ends: "The protesters said they had received compensation payment for only half of the 400 acres [162 hectares] expropriated for the project, including a mountain owned by local residents from Maday Island, despite claims by CNPC representatives that the company had made the full payment." That is a count of land, a count of what was paid, and the company's denial, all in one sentence, and the writer dropped the whole thing. Added, with CNPC's denial attached, together with the protesters' other demands.
3. **Selective quotation, Narinjara.** The card gave the farmers' side and dropped the officials' answers in the same meeting: the deputy township administrator on the complaint letter sent up to district level, the township agriculture head's "The compensation is being processed, you should all believe that you will get it", and "In 2012 and 2013 MOGE paid compensation for farmland covered in mud." All three added.
4. **Hedge restored.** RFA says "According to reports, a number of Maday residents who worked as laborers for CNPC were also fired following the protest." "reportedly" restored; the card had asserted it.
5. **The record's status printed, and the two protest counts set against each other.** The lender role now carries AidData's "Pipeline: Pledge" status explicitly rather than only "unclear whether delivered", and `confidence_note` now says the two RFA reports give six charged in April and ten convicted in September over the same march.

Flagged, not changed: **CNPC now appears on this card in both `lenders` and `companies`.** It is the
pipelines' owner-operator in `companies` and, after this extend, a funder in `lenders`, on the
strength of a compensation pledge AidData files as a grant that never left "Pipeline: Pledge". The
round's unit is the financing and AidData lists CNPC as the funding agency, so the placement is
defensible and I left it, with the role rewritten to say plainly what the entry is. If the owner
would rather the `lenders` array held only lenders, this entry's content moves to `conditions`
without losing anything but the record id, which the dedupe needs.
Also noted: record 34197's `location_narrative` is "Near HSIPAW, Myanmar" — Shan State, 700 km from
Kyaukphyu — while its description is about Maday Island. The extend does not move the card's point,
so nothing turns on it, but it is another AidData coordinate not to trust.

---

## The item I was asked to settle and not act on: `merowe-dam-amri-manasir`

I opened all four records' own pages (`china.aiddata.org/projects/178|56927|56959|85574/`, all 200)
as well as their text in the batch file. **The records support the writer's reading, against the
staff comment, and the arithmetic settles it.**

What each record says in its own title and its own purpose text:
- **56927** — "Chinese Government provides **$37.7 million** loan for **New Amri** Agriculture Scheme (Merowe Resettlement) Project"; purpose text repeats "$37.7 million loan for New Amri Agriculture Scheme"; flow Loan, funding agency a Chinese government agency.
- **56959** — "China Eximbank provides **$80.75 million** seller's credit to CWE for **Kehaila East** Agriculture Scheme"; purpose "to provide reliable water access to irrigated agriculture in Merowe Dam resettlement areas"; funding agency China Eximbank.
- **85574** — "China Eximbank provides **$29.9 million** USD loan for **El Makabra** Agriculture Scheme"; funding agency China Eximbank.

What staff comment 7 on record 178 says: "the Chinese Government provided another $37.7 million for
the Kehaila East Agriculture Scheme, the El Makabra Agriculture Scheme (Merowe Resettlement) Project
(as captured via Project ID#56959), and $110.7 million for the New Amri Agriculture Scheme (Merowe
Resettlement) Project (as captured via Project ID#56927)."

The comment attaches $37.7 million to ID#56959, which is the record that holds $80.75 million, and
$110.7 million to ID#56927, which is the record that holds $37.7 million. And **$80.75m + $29.9m =
$110.65m**, which is the comment's $110.7 million to the nearest hundred thousand. So the comment has
the two sums transposed: the $110.7 million it gives to New Amri is the Kehaila East and El Makabra
total, and the $37.7 million it gives to those two is New Amri's.

The card currently reads "US$110.7 million for the New Amri resettlement farm scheme and US$37.7
million for the Kehaila East and El Makabra schemes", which follows the staff comment and is
contradicted by all three record titles and by the addition. **Three of three records against one
staff comment.** I have changed nothing. Two further things the owner may want while in that field:
the role names no amount for El Makabra separately, and the card's `cp` and `cx` are both empty
although its lender role cites AidData record 178 — the batch treated G004 as already-on-map and
made no extend, so nothing added the `aiddata` tag.

---

## 1. What I could not check, and what stopped it
- **Pulitzer Center, Tom Gardner, "In Ethiopia's Bushlands, Promised Riches of a Railway Boom Turn to Dust".** Four routes tried, four failures, named as routes: `GET https://pulitzercenter.org/reporting/ethiopias-bushlands-...` over curl with a desktop user agent → **403**; the same URL through WebFetch → **client_error**, nothing of the page; `GET https://pulitzercenter.org/node/16424` → **403**; `GET https://web.archive.org/web/20210119001259/https://pulitzercenter.org/reporting/...` over curl → the agent proxy reported `ws_closed_mid_exchange` on `web.archive.org:443` on five consecutive attempts, and over `http://` the proxy answered "Blocked by egress policy". The Wayback availability API itself answers fine and says a 200 snapshot of 19 January 2021 exists, so **the page is not gone** — three clients could not reach it. A fifth route, WebFetch on the Wayback snapshot, returned `PROVENANCE_REQUIRED`: a permission request went unanswered. **That is not a host refusal.** Anyone revisiting the Addis card should start there.
- **`preprints.org` manuscript 202308.1157** (returned by both searches for Ethiopian railway expropriation): `GET https://www.preprints.org/manuscript/202308.1157/v1/download` → **403**. Not pursued further; it may not be about this line at all.
- **The People Daily articles behind AidData's 383-acre figure.** Not retried; the writer reports 403 on two URLs on that host. The figure stays attributed to AidData alone, which is the honest placement, and `confidence_note` says so.
- **Accountability Counsel.** `GET https://www.accountabilitycounsel.org/client-case/kenya-lamu-coal-fired-power-plant/` → **404** (an HTML error page under a 404 status), so the writer's note that the complaint PDFs 404 is consistent with the client-case page also being gone from that path. Moot now that the Lamu card is cut.

## 2. Figures where documents disagree, left unreconciled
- **Karimenu II phase one:** Sh1.28 billion to 246 people (water cabinet secretary, The Star, 1 August 2019) against Sh1.09 billion to 228 people with 28 unpaid (Athi Water Works Development Agency, The Star, 26 February 2020). Both on the card.
- **Karimenu II contract date:** 24 April 2017 (AidData record 58737) against May 2017 (The Star, 26 February 2020). Both now on the card; the writer had resolved to AidData's silently.
- **Karimenu II phase two acreage:** 429 acres required and 383 acres surrendered, both in AidData record 58737, with no explanation of the difference. Both now printed together.
- **Karimenu II people served:** nearly one million (Capital FM) against an additional 850,000 (AidData). Both now printed.
- **Lamu land, date (new, and the card missed it):** acquired in 2016 (The Star body, 11 August 2020) against "waiting for five years" as at July 2018, i.e. about 2013 (Aboud, The Standard) — and The Star's own standfirst says "acquired five years ago" against its body's 2016.
- **Lamu acreage:** 975 (The Star) against 1,000 (The Standard). The card had this one.
- **Addis railway route length:** 750.224 km and 759 km, both in AidData record 70086.
- **Addis railway restructuring:** 20-year maturity extension plus four-year grace extension (AidData) against repayment period extended from 10 to 30 years (People's Map), and a one-year deferral (People's Map).
- **Addis railway contract values:** $1,639,031,409 at signature on 25 October 2011 rising to $1,841,470,000 on 5 November 2012, and $1,197,400,000 at signature on 16 December 2011 rising to $1,401,800,000 on 2 November 2012 (staff comment 3, record 70086) against the single later figures the card attached to the signature dates.
- **Myanmar protest numbers:** six villagers charged in April 2013 (RFA, 2 August 2013) against ten convicted in September 2013 over the same march (RFA, 26 September 2013). Both on the card; now said to be the same march.
- **Narinjara, one document two ways:** "12 villages in Kyauk Phyu Township" against a list of ten village names on Mala Island. Not put on the card — a list of names is not obviously a second count of villages, and manufacturing a conflict is its own fault. Recorded here.
- **AidData record 52499 internal error, not used:** "Amu Power Company Limited is 51% owned by Kenyan investment firm Centum Investments and 51% owned by Oman's Gulf Energy." The writer printed no percentages, which was right.

## 3. Faults appearing in more than one card
- **Selective quotation, running one direction, on three of the five entries** — the Karimenu card (three separate articles), the Lamu card, and the Myanmar extend (two articles). Six distinct favourable or official-answer clauses were dropped and none added. The one exception is instructive: on the Addis card, which has no such omission, the writer kept the ERC department head's exculpatory answer. So the fault is not uniform; it tracks how hard the writer was working to make a thin case stand.
- **A hedge dropped from a sentence otherwise reproduced faithfully** — twice ("reportedly affected all China Eximbank loans", "According to reports… were also fired"). Both restored.
- **A figure or date carried by one document attributed to two** — the Karimenu contract date (The Star added to AidData's 24 April), the Lamu 16 November 2020 announcement (AidData's date attributed to The Star), the Addis contract values (AidData's 2012 values against its own 2011 dates).
- **Silent resolution of two readings in one document** — Karimenu 429/383, Addis 750/759, Addis contract values. The commonest fault in this batch, exactly as BRIEF36 predicted.
- **AidData coordinates.** Two of the five records I checked point somewhere other than the site: 58737 at a different Kiriko 66 km away, 34197 at "Near HSIPAW" for a Rakhine matter. The writer found the first; the second is new.

## 4. Wrong in the card data, outside the fields I was asked to check
- `lamu-coal-kwasasi-land`, `whole`: "Amu Power's chairman of the local farmers' association" — Aboud chairs the Kwasasi Farmers Association and holds no position at Amu Power. The card manufactured an affiliation. (Entry cut, but this is a writing failure worth naming.)
- `lamu-coal-kwasasi-land`, `community`: "the Chinese embassy in Nairobi" — the article says only "the Chinese embassy".
- `lamu-coal-kwasasi-land`, `community`: "Sh800,000 an acre" drops The Standard's "at least".
- `addis-djibouti-railway-compensation`, `companies`: the two contract-value/date pairs above. `lenders[0].role` itself checked clean against record 70086, every figure.
- `karimenu-ii-dam-compensation`, `lenders[0].role`: checked clean, every figure, against record 58737. `conditions` understated the record — the advance payment, the parliamentary inspection and the Auditor General request were all in it and all bear on the land.
- The extends' shape is correct for `merge.py`: `lenders_add`, `lk_add`, `cp_add`, `sources_add` and `fields_add` all sit at the top level of each extend object, which is what the script reads. I verified against `merge.py` rather than assuming. Note that `merge.py` has **no `status` check**, so a dropped case left in the `cases` array would merge anyway; that is why the two cuts are removed from the file rather than marked.

## 5. Routes
Opened and returned 200, every URL in the surviving entries, requested fresh: `china.aiddata.org/projects/58737/`, `/45520/`, `/95928/`, `/34197/`, `/178/`, `/56927/`, `/56959/`, `/85574/`; `the-star.co.ke` (three articles, with and without `www`); `capitalfm.africa`; `rfa.org`; `ecoi.net` (`/de/dokument/259275` → `/de/dokument/1268827.html`, source URL updated to the canonical); `bnionline.net` (`/en/node/34621` → `/en/news/arakan-state/item/378-...`, updated); `thevault.exchange` (Standard Bank Group 2015 annual integrated report, 2.8 MB PDF, page 47 read); `nominatim.openstreetmap.org`; `api.openstreetmap.org`; `thereporterethiopia.com`; `thepeoplesmap.net`; `etd.aau.edu.et`.
Failed, each named as a route and not as a host: the five Pulitzer Center and Wayback routes above; `preprints.org` manuscript download, 403; `accountabilitycounsel.org` client-case page, 404; `webcache.googleusercontent.com`, 200 but serving a Google notice rather than any cached page.
