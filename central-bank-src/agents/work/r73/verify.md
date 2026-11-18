# Round 73 — independent verification

All 15 records checked against their own sources. Documents actually read: 5 PDFs downloaded and
grepped (SRB FY2012, SRB FY2014, ISL 2012, MDA hcc nr.6/2024, SEN Cour des comptes), 6 HTML pages
fetched and stripped (Curaçao Chronicle, cima.ky Jackman + cima.ky/the-board, norges-bank.no,
swedbank.com/the-share, nationalbanken.dk, finansdanmark.dk), the Taiwan .docx downloaded and
unzipped (text + docProps/core.xml) plus the Control Yuan closing table PDF, vfp.mv fetched, and
psmnews.mv, cgr.gob.ni x3 and the knipselkrant PwC PDF read through WebFetch.

All 15 are filed byte-identical to the .norm.json records (checked field by field against
corruption.json / events_gold.json).

## Defects

### 1. SRB FY2012 (DRI 400-264/2013-01) — wrong figure: cost stated as book value
Record: "the equipment's book value at 31 December 2012 was 24,128 thousand dinars".
Source: "исказану по набавној вредности од 24.128 хиљада динара, исправци вредности од 14.064
хиљаде динара и садашњој вредности од 10.064 хиљаде динара" (p.36) — 24,128 thousand is the
ACQUISITION cost; accumulated depreciation is 14,064 and the **book (net) value is 10,064
thousand dinars**. The emphasis paragraph likewise says "набавна вредност ... 24.128".
Also, the figure covers only "део укупно уговорених количина опреме" — part of the contracted
quantity, not the whole.
Fix: "the acquisition value of the part of the equipment concerned was 24,128 thousand dinars,
with accumulated depreciation of 14,064 and a net book value of 10,064 thousand dinars at
31 December 2012."

### 2. SRB FY2012 — "the seventh of nine" is not in the source and does not add up
Record detail: "This is the seventh of nine per-entity State Audit Institution reports on the
National Bank of Serbia (audit subject 1071 ..., financial years 2009 to 2017)."
The cited PDF says nothing about a register, a subject number or a series position. FY2012 is the
fourth of FY2009–FY2017, not the seventh. dri.rs returns 403 from here so the register could not be
re-read.
Fix: drop the ordinal, or state the register page as a second source and get the count right.

### 3. SRB FY2012 — "never delivered" overstates the finding
Record: part of the equipment "was never delivered to the Bank".
Source: "није у целости испоручен Народној банци Србије" — was not delivered IN FULL; Recommendation 5
calls it "плаћену а непреузету опрему" (paid for but not taken over) and says it was not delivered to
the Zavod za izradu novčanica i kovanog novca, Topčider.
Fix: "was not delivered in full".

### 4. NIC RIA-UAI-007-2022 — the removed "staff" accretion is still in the record
The record's own detail field states that the word STAFF was taken out, and then uses it two
sentences earlier: "a different audited process (**the staff savings and retirement fund**)".
This is live in corruption.json index 291 as filed. The resolution names the audited entity only as
the BCN's "Fondo de Ahorro y Retiro" and the official as head of the "Programa de Ahorro y Retiro";
it says nothing about whose savings it holds (confirmed on re-read).
Fix: delete "staff" from the detail field. Everything else in this record checks out exactly
(session 1265 / 6 Jan 2022 / unanimous; IN-014-004-21 of 14 Oct 2021; 1 Jan 2018–31 Dec 2019; the
three findings verbatim; IN-014-006-17 at 50%; 60 days + 30; article 77; four officials and titles).

### 5. ISL (Ríkisendurskoðun 2012) — a party's own assertion attributed to the audit office
Record: "The same chapter records that the Governor was at one and the same time the highest head of
the Bank's foreign-exchange surveillance and chairman of the board of the Bank's own private limited
company".
Source (ch. 8, p.31): that clause sits inside the excluded bidder's own public statement, in Icelandic
reported speech — "Í yfirlýsingu sem umræddur aðili sendi frá sér ... Seðlabankastjóri, sem var hvort
tveggja í senn æðsti yfirmaður gjaldeyriseftirlitsins og stjórnarformaður einkahlutafélags bankans,
**hafi tilkynnt** sér það ...". Ríkisendurskoðun is reporting what the affected party said, not making
the finding. The office's own finding on the dual role is the separate, milder one the record already
has (the 19 January 2011 memorandum: sitting on the boards "væri óheppileg").
Fix: attribute the dual-role sentence to the statement issued by the excluded bidder.
Everything else verified: the 19.01.2011 memorandum from the ríkisendurskoðandi to the
seðlabankastjóri exists and is described as the record says; "ekki efni til að gera athugasemdir við
söluferlið" ✓; Sjóvá sale halted over the foreign-exchange investigation and completed after the
bidder withdrew ✓; prosecutor dropped it in 2012 ✓; ch.6 figures 345 / 75 / 267.2 ma.kr. ✓; cover
"JÚNÍ 2012" and the index page gives 27.06.2012 ✓; quote verbatim ✓.

### 6. CYM (Taron Jackman) — the private leg the record rests on is not financial
The record says the private finding "rests on the Deloitte partnership alone" and calls Deloitte's
Cayman practice the financial leg because it "sells audit, regulatory and risk advisory work to the
financial-services industry". Two problems:
(a) Deloitte is a professional-services firm. Selling advisory work TO the financial sector is not
being a financial counterparty. assign_rd_all.md: "**Private but not FINANCIAL is logged, not
filed** ... find the financial leg rather than accepting the one the source leads with."
(b) The page does state a financial private employer, and the record discards it on a mistaken
rationale: "Mr. Jackman moved to Barclays Bank & Trust (Cayman) Limited ('Barclays'), **a Class A
Registered Bank in the Cayman Islands**, where he worked his way to the position of Chief Operating
Officer." The brief's own list of what counts as stated includes "describing it as a commercial or
private bank"; a Class A Registered Bank is exactly that. The record's reason for excluding it — that
the page "makes no ownership statement" — applies the ownership test to a sentence that already
describes the employer as a licensed bank.
Also accretion: "audit" is not on the page for the Deloitte Cayman practice (he worked in the audit
department at Price Waterhouse; at Deloitte the page gives consulting and risk advisory only).
Fix: rest the record on Barclays Bank & Trust (Cayman) Limited and say which kind of ownership it is
(an unlisted subsidiary of a listed group, with a source for the group's listing), or log rather than
file it. Verified clean otherwise: Partner 2004 to retirement in 2025 ✓, ten years at Barclays to COO
✓, Price Waterhouse audit department ✓, no appointment date on the page ✓, and cima.ky/the-board
lists him as a serving Director ✓ (Greg Swart, the map's existing CYM record, is on the same board —
distinct person, no duplicate).

### 7. TWN (Control Yuan correction of the Central Mint) — the derived date is contradicted by the
same file's metadata
The record dates the correction 2025-03 from the .docx's dcterms:created = 2025-03-20T00:58Z and says
so. But docProps/core.xml also carries **cp:lastPrinted = 2025-02-04T03:32Z** and cp:revision = 2 —
the file was printed six weeks BEFORE the "created" timestamp, so that timestamp is a re-save, not the
document's origin, and the correction existed by 4 February 2025 at the latest. A 2025-03 date derived
from dcterms:created is therefore unsafe and probably a month or more late.
Fix: either date it 2025-02 at the latest (disclosing lastPrinted as the basis) or, better, leave the
day/month out and date it 2025 from the ROC-114 file series, noting the committee closed the case on
4 June 2025. Everything else verified against the .docx text: 顯有怠失 ✓, the quote character-for-
character ✓, the 18 August 2022 (111) revision of the MOL guidelines ✓, OSH Act ✓, Constitution
art.97(1) and Control Act art.24 ✓, "移送中央銀行督促所屬中央造幣廠確實檢討改善見復" ✓, complainant
as 原任副廠長 A君 and 葉〇〇 only ✓. Second source verified: table 114財正0002, closed 114.06.04,
Central Bank's reply that the Mint revised the plan in 114年5月 and that its handling 容有加強空間 ✓.

### 8. CUW PwC — "handed over" is the record's word, not the report's
Record: "the final report was handed over on 17 April 2014."
Source: 17 April 2014 is the date of the formal presentation and final discussion in Curaçao; the
summary states no handover date for the full report.
Fix: "formally presented and discussed on 17 April 2014".
Everything else in this record is on the document: cover "Onderzoek CBCS", "FINAAL CONCEPT",
4 August 2014 ✓; commissioned by the two finance ministers as representatives of the
Vermogensgerechtigden ✓; 10 October 2010 to 31 May 2013 ✓; president's dominant position and no
collegial governance ✓; seventh RvC member 26 March 2012, quorum and validity disputes, three members
absent from 12 September 2012 ✓; no VvV meeting since 10 October 2010, contrary to the statute ✓;
Harbour bond transactions unusual and at odds with the monetary and investment policy, reported to the
RvC too little and too late ✓; RvC never decided to start the investigation into the president ✓;
31 January 2013 request ✓; fieldwork May and June 2013 ✓; findings 25 November 2013 ✓; disclaimers on
not auditing the information and not examining individual integrity ✓.

## Minor points, listed because they are claims in the records
- **NOR (Børsum):** "the bank is listed in its own right, not a subsidiary and **not state-owned**".
  The cited evidence is only the listing sentence (verified verbatim: "Swedbank's A shares are listed
  on NASDAQ OMX Stockholm in the Large Cap segment"), and the record itself says the shareholder table
  was not read. A listing does not settle the absence of state ownership. Drop "not state-owned" or
  source it. Norges Bank page otherwise verified word for word, including the quoted appointment and
  work-experience sentences.
- **DNK (Nødgaard):** the private leg is Finance Denmark, a trade and employers' association, not a
  financial undertaking — the same "private but not financial" question as CYM, though weaker because
  its members are the banks. The source offers a genuinely financial seat the record does not use:
  "Member of the Board of Directors, Chairman of Audit Committee PKA 2017-2024". Also the quoted
  Finance Denmark sentence is cut mid-sentence without an ellipsis: the page continues ", as well as
  data centres, IT and fintech companies." Everything else on the page verified exactly.
- **MDA:** "The audit was carried out under art.32(7) of Law no.260 ... and art.21(2) of Law no.548".
  The decision says the audit was carried out "în temeiul art.31 alin.(3) și art.32 alin.(7) din Legea
  nr.260"; art.32(7)+art.21(2) is footnote 5, attached to the sentence about the Court's confined
  remit, which is what the record goes on to describe. Add art.31(3) or reword. Every figure, name,
  title and date in the MDA record is otherwise printed in the decision (192.0 mil / 16.9%; 147.4 mil
  / 65.3%; 1.2 mil to retired former employees with no distinct rules; the 2021 working group's
  referral never sent to the Competition Council — quote verbatim; 3.2 mil and IAS 16; Holercani
  Oficiul de protocol nr.9 from the 1998 Government order, unregistered, also found in 2015 at
  footnote 8 = Decision no.22 of 06.07.2015; the four officials and their exact titles).
- **CUW Girobank:** the article reads "inadequate oversight by the Central Bank of Curaçao and Sint
  Maarten (CBCS) **and the bank's Supervisory Board (RvC)**" — ambiguous as to whose RvC. The record
  resolves it to Girobank's ("Girobank and its Supervisory Board (RvC)"). The source does not settle
  it. Everything else matches the page, including the quote character for character, the 4 December
  presentation with no year printed, the 170-million-guilder Dutch loan and 98% of depositors, the
  2013 emergency regulation and 2019 moratorium, and that no individuals are named.
- **SEN:** the record's bookkeeping about its own grep is slightly off — 15 "BCEAO" hits is right, but
  11 are account-name rows (the 12th non-finding hit is the abbreviations list), and of the remaining
  three one is not used in the record (p.~"maintenir leur capacité à mobiliser des ressources auprès
  de la BCEAO"). The substance is exactly right: the 29 December 2023 transfer of 15 billion CFA out
  of the Trésorier général's compte règlement at the BCEAO into an account in his own name at bank
  B.A., positioned 2 January 2024 and moved the same day into the State account managed by the
  finance minister and used at once for unauthorised expenditure ✓; article 125 of decree 2011-1880
  of 24 November 2011 and "seuls les comptables deniers et valeurs sont habilités" ✓; the finding on
  ministers irregularly binding the State ✓; February 2025 Rapport définitif, CABF ✓. counterparty_only
  is correct — no finding in the report is against the central bank.

## Clean
- **SRB FY2014 (400-538/2015-07):** clean. 387 procedures / 3,302,577 thousand dinars, section 2.11,
  JN 89/2014, four bidders, award to the bidder whose samples were tested earlier as existing supplier
  to Topčider, the incomplete industrial-trials report, the chosen bidder's written undertaking,
  Recommendation 2 in full, the Law on Public Procurement 124/2012 and 14/2015, both opinions
  unmodified, signed Radoslav Sretenović — all verified. Quote verbatim.
- **NIC RIA-119-14:** clean. 20 February 2014, IN-014-025-2012 of 31 December 2012, IT administration
  in the División Internacional by the Bank's own internal audit unit, 30 January 2011 to 30 September
  2012, the four findings as described, no administrative irregularities and no responsibility, 90 days
  from notification, no officials named — all verified.
- **NIC RIA-UAI-505-2025:** clean. Session 1429 of 15 May 2025, IN-014-005-24 of 20 November 2024,
  1 January–31 December 2023, all areas submitted timetables, none of the four recommendations in
  IN-014-002-23 (approved by RIA-UAI-649-2024) implemented at 0%, no responsibility, reporting through
  SIIRCI once the cronograma falls due, all ten officials and titles — all verified. Not a duplicate of
  the filed RIA-UAI-649-2024 record: different report, year and conduct.
  *Cross-check for the owner of the earlier record:* the filed RIA-UAI-649-2024 record (corruption.json
  index 281) says the Consejo confirmed two of four findings and made "the recommendations attached to
  the two confirmed findings" binding, while RIA-UAI-505-2025 speaks of **four** recommendations in
  IN-014-002-23. The new record follows its source; one of the two descriptions of 649-2024 is wrong
  and it is probably the older record's.
- **MDV (Majlis committee):** clean. VFP verified: 2024-07-17 14:21:35 timestamp, "On Wednesday"
  (17 July 2024 was a Wednesday), Deputy Speaker and Dhiggaru MP Ahmed Nazim, unanimous support, going
  to the full house then the president, illness and the written reply blaming the government for
  ignoring the central bank's advice, motion submitted 2 July, "the past seven months". PSM News
  verified for everything the record attributes to it: the committee is the Public Accounts Committee
  (its headline), passed by a majority of attending members, three declined invitations and a written
  report, the committee's finding that he had not performed his duties effectively "particularly while
  the government was raising funds from the domestic market", no advice since 17 November 2023 on the
  MMA Act's key objectives, and the vote against a further written chance. The record's disclosed
  margin conflict and disclosed date provenance are both accurate.
- **Row placement:** no wrong-row defects. CUW Girobank is a supervisory FAILURE with the CBCS as
  subject, which brief_depth.md admits expressly. SEN is correctly counterparty_only. TWN is the
  Control Yuan correcting a central bank subsidiary and transmitting it through the Central Bank with a
  duty to report back — state action on the bank's own works, not the bank as regulator; it sits on the
  pressure row defensibly, though it is the row's thinnest subject matter (a workplace-bullying
  complaint, nothing about the bank's leadership or autonomy).
- **Duplicates:** none. The two CUW records are separate episodes from each other and from the Tromp
  conviction (index 18) and the Algemene Rekenkamer record (index 283). No TWN or MDV event collides
  with the existing 1979 TWN or 2021 MDV events. No CYM/NOR/DNK person collides with Swart, Tangen or
  Rohde.
- **Known-host annotations** (cgr.gob.ni, psmnews.mv, knipselkrant PwC PDF) were not re-reported; the
  documents behind all four do say what the records claim. Worth one note for the filer: the PwC record
  cites a URL that serves a 404 to every reader, which is in tension with brief_common.md rule 1
  ("a source URL that a reader can open"). The record discloses this fully; it is a filing decision,
  not a new finding.
