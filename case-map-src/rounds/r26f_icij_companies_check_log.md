# Independent check of comp_out.json (27 descriptions, 11 discrepancy findings)

Checker: independent fact-checker. Did not write the input.
Outputs: `/home/claude/r17/comp_checked.json` (27 descriptions + `discrepancies` array), this log.

## Counts

- **Kept verbatim: 4** — Cuijiaying Complex Management Office; Guangdong World Bank Financed Projects
  Management Office; Liaoning Urban Construction and Renewal Project Office (LUCRPO); Nanning-Guangzhou
  Railway Company Limited (NGRC).
- **Corrected: 23**, of which 7 substantive (China Railway Corporation, Huai River Basin Commission,
  both Hubei keys, NHAI/MoRTH, Guiyang Municipal Government, Shiyan Municipal Government) and 16
  trims of unsourced qualifiers, loose wording or dead/mis-titled sources.
- **Blanked: 0.**
- **Sources removed: 4** (one dead, one unreachable, one superfluous, one no longer needed).
  **Sources added: 4.**

## On the zero-blank batch

The brief flagged a zero-blank batch as normally a warning sign. Tested, and on this batch the
writer's reason holds: all 27 keys are implementing agencies, project companies or supervising
bodies of specific World Bank loans, and each is not merely *named* but *characterised* in a
completion report that is on disk. I re-extracted the governing PDFs myself with `pdftotext -layout`
(into `/home/claude/r17chk/`) rather than trusting the writer's `.txt` files, and located the
supporting sentence for every clause I kept. No entry needed blanking. Two needed heavy cutting back
to what the documents say about the *body* rather than about its city (below).

That said, the batch is not clean. The failure mode here was not invention of whole entities; it was
**over-reach inside a true description** — a figure lifted across a three-year gap, a headquarters
city with no source, a remit widened past the sentence that carried it, and in one case dates that
are real but come from a different report than the one cited.

## Priority 1 — Hubei verdict: CONFIRMED

Every element of the writer's evidence checked line by line in the two PDFs.

**Fifth Inland Waterways, P085333** (`vfy/iw5_icr.pdf`):
- Abbreviation list: `HPTD  Hubei Provincial Transport Department`.
- Data sheet, `Implementing Agencies:` — one entry, `Hubei Provincial Transport Department`.
- Running text uses HPTD throughout (19 occurrences) and the full "Hubei Provincial Transport
  Department" again in the borrower's section. The word "Transportation" appears ten times in the
  report and **never** refers to the department (it is generic "transportation costs", "water
  transportation", etc.).

**Hubei Shiman, P081749** (`dlD/shiyan_icr.pdf`):
- Abbreviation list carries both, adjacent: `HPCD  Hubei Provincial Communications Department` and
  `HPTD  Hubei Provincial Transport Department`.
- Running text: "in the Hubei Provincial Transport Department (HPTD) management of the road sector".
- Bibliography: "Hubei Province, Hubei Provincial Transport Department. Information Provided by the
  Borrower Regarding Completion Report. Submitted by HPTD, March 2010".
- "Transportation Department" occurs **exactly twice**: the data-sheet `Implementing Agencies` field,
  and one sentence reading "This is the fourth Bank-financed highway project implemented by Hubei
  Provincial Transportation Department (HPTD, formerly HPCD)."

**One correction to the writer's framing.** That sentence is not in a financial-management *annex*.
It is in the main report's `Financial Management` subsection (the report's annexes begin later). The
substance — the sentence exists, it is the only "Transportation" sentence, and it records
"HPTD, formerly HPCD" — is right. The verdict is unaffected.

**The site claim is true, and I checked it independently.** No Hubei transport-department host can be
reached from this environment: `jtyst.hubei.gov.cn` and `jtt.hubei.gov.cn` and `hbjt.gov.cn` all fail
to connect through the agent proxy (connect_unreachable / connection reset). So the verdict rests on
the two Bank reports alone — and on those two reports it holds, because both *define* the acronym as
"Transport Department" and the department's own submission is filed under that name.

**Recommendation to the map: standardise on "Hubei Provincial Transport Department" and merge the two
entries.**

### Change made to both Hubei descriptions

Dropped the clause "it manages Hubei's road sector and was the executing agency for four earlier
World Bank transport loans in the province." The "four" belongs to a different entity and a different
sentence: iw5 says HPTD's *World Bank-Financed Projects Office* "had successfully managed four World
Bank transport projects", while the Shiman report calls Shiman itself "the fourth Bank-financed
highway project implemented by HPTD". Those two cannot both be read as "four earlier loans", and the
figure attaches to the office, not the department. This is fault 3 in miniature. Also added "the
World Bank's completion reports record" before the former-name claim, since HPCD is the reports'
statement rather than an independently verified renaming.

## Priority 2 — NHIIP verdict: CONFIRMED

All four limbs verified in `vfy/nhiip_icr.pdf` and against the live Bank projects API:

| Claim | Found |
|---|---|
| Data sheet names one implementing agency | Yes: `Republic of India` / `Ministry of Road Transport and Highways`, single row |
| Bank project record gives only that ministry | Yes: `impagency = "Ministry of Road Transport and Highways"` for P121185 |
| Report presents NHAI as the IA of the NHDP | Yes: "The National Highways Authority of India (NHAI) was the main implementing agency for the NHDP" |
| NHAI tied to a separate loan | Yes: "the NHAI Technical Assistance (TA) Loan (P121515)" |
| Purpose "was to assist MoRTH in improving the non-NHDP network" | Yes, verbatim |

I fetched the projects API myself for P121185, P098078, P074688 and P125996; all four of the writer's
API claims in this batch returned exactly what it said they would. The writer did not save those
responses to disk, which is why they were not re-checkable from the working directory — worth saving
next time.

**NHAI should come off `nhiip-india-corridor-land-acquisition`.** Exact recommended wording:

- Company name: `Ministry of Road Transport and Highways`
- Role: `Borrower's implementing agency; state public works departments carried out the land acquisition`
- Description (now in the output file): "The Ministry of Road Transport and Highways is a ministry of
  the Government of India; the Bank's completion report records that it was assigned the development
  of the 'non-core' national highways — those outside the National Highways Development Programme and
  Bharatmala, about 43 per cent of India's primary highway network."

The writer's NHAI half — accurate in itself, drawn from the NHAI Act 1988 — has been **cut**, and the
Act dropped as a source. By COMP.md fault 2, a body that does not belong on the case should not be
described on it; describing it in full invites the reader to think the Bank named it. If the owner
keeps NHAI anywhere it belongs to P121515, where the Act citation can be revived.

## Priority 3 — the other nine discrepancies

| # | Finding | Verdict |
|---|---|---|
| 3 | LUCRPO name and parent department | **Confirmed** |
| 4 | Huai body is a ministry field body, not a national implementing body | **Confirmed in substance; rename rejected** |
| 5 | Five Vietnamese PCs; fifth is "Ho Chi Minh Power Corporation" | **Confirmed** |
| 6 | Bank uses "Vietnam Electricity (EVN)" | **Confirmed** |
| 7 | P074688 names three power corporations the card omits | **Confirmed, and stronger than reported** |
| 8 | Guangdong IA of record is the provincial Transport Department | **Confirmed** |
| 9 | GuiGuang incorporated before effectiveness | **Confirmed in substance; sourcing and one date corrected** |
| 10 | Shaanxi name possibly stale | **Confirmed as a flag; no change** |
| 11 | GXWCDC "Waterways" spelling variant | **Confirmed; no change** |

Details on the three that are not plain confirmations:

**#4 Huai — the rename is rejected.** The ICR data sheet does read "Huai River Basin Commission" and
the API does give "Ministry of Water Resources" for P098078, so the level-of-government point stands
and the role should change. But the writer also recommended renaming the card from "Huai River Water
Resources Commission". I opened the gov.cn page it cited. Two problems. First, the **cited title is
wrong**: the writer called it 取水许可和水资源费征收管理条例, the water-abstraction permit regulation;
the page is actually 水利部职能配置、内设机构和人员编制规定, the provisions on the Ministry of Water
Resources' functions and structure. Its Article 6 says what the writer said it says — 长江、黄河、
淮河、海河、珠江、松辽水利委员会、太湖流域管理局 are 水利部派出的流域管理机构, the seven basin
agencies the ministry dispatches, exercising water administration in their jurisdictions — so the
substance survives and I have corrected the title. Second, that same article names the body
**淮河水利委员会**, of which "Huai River Water Resources Commission" is the literal rendering. The
card's name is therefore the body's legal name, not an error, and the batch key is the Bank report's
variant. Standardise for the map's own consistency if you like, but neither name is wrong, and the
writer's reason for preferring the Bank's variant does not survive the decree it cited.
I also removed **"based in Bengbu, Anhui"** from the description: it is in neither source. The ICR
mentions a "Bengbu-Fushan Section" as a stretch of river. That is a headquarters claim with no page
behind it — fault 1.

**#7 P074688 — stronger than the writer reported.** The writer rested this on the API record alone and
called it an "optional addition". The **completion report's own data sheet** lists all five
implementing agencies: Central Power Corporation (former Power Company No. 3), Northern Power
Corporation (former Power Company No. 1), Southern Power Corporation (former Power Company No. 2),
Vietnam Electricity, and Ministry of Industry and Trade (former Ministry of Industry). That makes the
omission a plain gap in the card, not a judgement call. Upgraded in the output.

**#9 GuiGuang — real facts, wrong report, wrong restructuring.** The dates are genuine, but **they are
not in the GuiGuang report the writer cited** (P107559). I grepped it for "June 4", "2007", "November
28" and "2011": nothing. They are in the **NanGuang** report (P112359), whose 25 August 2011
restructuring endorsed *both* NGRC and GGRC as implementation entities: "Guiyang-Guangzhou Railway
Company Limited (GGRC) (incorporated on June 4, 2009) to succeed the Preparation Group of the
GuiGuang Railway Company (formed on November 28, 2007)". So the writer's "25 August 2011
restructuring" is the **NanGuang project's** restructuring, not GuiGuang's: the GuiGuang project's
own two restructurings were 8 February 2013 and 24 December 2015, and it was the 2013 one that
recorded "the incorporation of the GuiGuang Railway Company Preparation Group as the Guiyang-
Guangzhou Railway Co Ltd in the project documents". Corrected in both the description's sources and
the discrepancy's recommendation. The card's "created during implementation" is still wrong — loan
approved 16 April 2009, effective 26 August 2009, company incorporated 4 June 2009.

## Priority 4 — the two compound keys

**`Northern, Central, Southern, Hanoi and Ho Chi Minh City Power Corporations` → split into five.**
The Distribution Efficiency ICR enumerates them as five distinct subsidiaries with five acronyms
(HNPC, NPC, CPC, SPC, HCMPC) and reports targets per corporation. One sourced description covers all
five, so the split costs nothing and the reader gets five bodies instead of one phrase. Use the
report's names, including **"Ho Chi Minh Power Corporation"** — the "City" in the current key is not
in the report.

**`National Highways Authority of India / Ministry of Road Transport and Highways` → not a split, a
removal.** This interacts with finding 2 as the brief anticipated. Splitting would leave NHAI on a
case the Bank's data sheet and project record do not put it on. Remove NHAI and keep the Ministry as
a single entry.

## Priority 5 — city descriptions standing in for government bodies

**Shiyan Municipal Government — cut back, not blanked.** The writer's description was almost entirely
about the city, and the passage is genuinely in the Shiman report: "the SME would serve Shiyan city,
an industrial center with a strong automobile industry, mineral resources and tourist attraction and
a population of over 3 million." But that sentence describes what the expressway serves, not what the
municipal government is. The only thing the report says about the body as a body is that it required
the connecting road, and that a "Shiyan City Communications Bureau (SCCB)" handles operations and
maintenance of the local-road programme. Cut to: "The municipal government of Shiyan, a city in Hubei
province, China. Its Shiyan City Communications Bureau is responsible for operating and maintaining
the city's local roads." Thin, and honestly thin. I kept it rather than blanking because that one
structural fact — a named bureau beneath it — is a real statement about the body.

**Guiyang Municipal Government — same test, same treatment.** The writer's area figure (8,034 km²),
district breakdown and "Guizhou then ranked lowest of China's provinces for GDP per head" are all in
the Guiyang ICR and all about the municipality and the province, not the government. Cut. What the
report does give about the body: it is the city-level government of Guiyang, capital of Guizhou; its
departments include a Municipal Development and Reform Commission (GMDRC), a Municipal Finance Bureau
(GMFB) and a Municipal Road Division; and the project leading group it formed was led by a vice-mayor.
That is a description of a government, and it is what the entry now says.

## Priority 6 — restraint claims, all six checked

| Claim | Verdict |
|---|---|
| GXWCDC carries no stated owner | **True.** iw4 names no owner; the description says so explicitly |
| Guangdong WB PMO described only by placement in the Department of Finance and its own supervising-not-implementing statement | **True.** Data sheet: "Guangdong World Bank Financed Projects Management Office, Department of Finance"; borrower comments: "GDPMO regard itself as the supervising agency, not the implementing agency of the project". Kept verbatim |
| CCMO and LUCRPO described only as units created to run one loan | **True** for both, and both verified against the reports' own sentences. Kept verbatim |
| SMEC figure is the 2016 one (~5,800), not the site's "16,000+" | **True, and the exclusion is right.** The press release's About-SMEC note gives "5,800 employees and an established network of more than 75 offices". The "16000 + Employees" tile on smec.com sits at the end of a paragraph about drawing on capabilities from across the Surbana Jurong Group; the page does not attribute it. Good restraint |
| Kunming Railway Bureau's post-2017 company name not claimed | **True.** The entry says the 18 were re-registered without naming the Kunming company — correct, since the Chinese article names Chengdu and Shenyang as examples but not Kunming |
| "Shaanxi Provincial Communications Department" left alone, not silently modernised | **True.** The ICR name is kept and the possible rename is flagged, not applied. The Hubei / Guangdong / Guangxi rename evidence it relied on is real: Shiman has "HPTD, formerly HPCD"; the iw4 data sheet has "Guangdong Provincial Transport Department (Former Guangdong Provincial Communications Department)" and "Guangxi Transport Department (Former Guangxi Communications Department)". `jtyst.shaanxi.gov.cn` is unreachable from here too |

## Substantive corrections not covered above

**China Railway Corporation — figure attached to the wrong year and entity.** The writer wrote
"Registered capital was RMB 1.74 trillion and it managed a 124,000 km network in 2017." The 124,000 km
is Caixin, September 2017 — right. The RMB 1.74 trillion is from the Railway Gazette piece on the
**June 2019** restructuring, where it is the registered capital of China State Railway Group, the
successor. Two years and one corporate reorganisation apart. Likewise "It has no shareholders'
meeting; the Ministry of Finance performs that role for the State Council" is the Railway Gazette
describing the 2019 entity, not CRC in 2017. Both moved to the 2019 clause where they belong, and
Caixin's 2.1 million staff put in as the 2017 figure. Also added the 18 bureaux, which Caixin and the
China Securities Journal both carry.

**Chengdu and Kunming Railway Bureaux — dead source replaced.** The cited China Daily URL
(`chinadaily.com.cn/cndy/2017-11/22/content_34838863.htm`) returns **404**. I cannot tell whether it
worked when the writer fetched it, but it cannot stand as a citation now. The China Securities Journal
article carries the same facts and more precisely: as of 17 November 2017 all 18 railway bureaux under
China Railway Corporation had completed their business-registration change; each renamed 中国铁路XX局
集团有限公司; "原成都铁路局… 更名为中国铁路成都局集团有限公司"; and they remain wholly owned by CRC.
That is a direct source for the Chengdu company name the entry gives. Added Caixin for the count of 18
to both entries.

**Changji Railway Company — "runs" corrected to "owns".** The ICR says Changji "owns both the
Changchun-Jilin Railway (111 km) and Jilin-Hunchun Railway (360 km)", but it is the regional
administrations that operate services: "The RAs, as the train operating companies, earn revenue from
passengers". April 2011 formation, the Changchun-Hunchun naming, Shenyang as major shareholder and the
RMB 1.2 billion 2016 revenue all verified.

**Guangdong Provincial Waterway Bureau — hierarchy hedged, other bodies' facts removed.** The report
never says the bureau sits *under* the provincial transport department; it writes "GDTD/GPWB", names
the department as implementing agency in the data sheet, and describes the transport departments
supervising and coordinating. Changed "working under" to what the report actually does. Also removed
"local waterway bureaus do routine maintenance and dredging on budgets allocated by the provincial
government" — true, but it describes the *local* bureaus, not this provincial one, and inside a
one-line description of GPWB a reader takes it as GPWB's.

**Ministry of Agriculture and Rural Development — dead source replaced.** The Viet Nam News article
cited for the merger returns **403**. The merger itself is correct: USDA Foreign Agricultural Service
reports MARD merged with the Ministry of Natural Resources and Environment to form the Ministry of
Agriculture and Environment, which "began operating under the new structure on March 1, 2025".
Substituted. Decree 105/2022 Article 1 checked word for word against the FAOLEX PDF; the remit list is
accurate (added "and control" to "disaster prevention", as in the decree).

**Ministry of Industry and Trade — remit trimmed and dated; source weakness noted.** Decree 189/2007
Article 1 checked; the remit is accurately summarised, and "It replaced the former Ministry of
Industry" is independently confirmed by the Rural Energy 2 data sheet's "Ministry of Industry and
Trade (former Ministry of Industry)". Two cautions now in the entry's note: the English text was
opened on **LuatVietnam, a commercial legal database**, not a Vietnamese government site (unlike the
MARD decree, which is on FAOLEX — the brief's assumption that both came via FAOLEX is not what the
writer cited); and Decree 189/2007 is the founding decree, superseded by later ones, so the remit is
now dated in the description rather than given in the present tense.

**Ankang Municipal Communications Bureau — "in southern Shaanxi" removed.** True of Ankang, but not
in the completion report. Everything else verified: AMCB administers and maintains local roads,
directly maintains provincial roads, monitors road conditions, and county road administration bureaus,
townships and villages handle the rest.

**Shaanxi Provincial Communications Department — "including the province's expressways" removed.** The
report's support is narrower: data-collection equipment "for the allocation of maintenance resources
and the correct prevention of the deterioration of the provincial and national roads under its
responsibility". The department did implement the Ankang-Maoba expressway, but that is its role on
this project, not a stated general remit — and COMP.md says not to restate the role.

**Guangzhou Sewerage Treatment Company — "set up shortly before 2004" dated properly.** The ICR says
GSTC "had just been created at appraisal" and was formed "as a financial autonomous enterprise before
appraisal"; the data sheet dates appraisal to 9 December 2003. Changed to "created shortly before the
project's appraisal in December 2003" rather than inferring a calendar year.

**SMEC — sector list replaced with the source's own wording.** "transport, energy, water and
built-environment infrastructure" is the shape of SMEC's current market menu, not a statement in
either cited page. The press release says "specialising in major infrastructure projects" and gives
the service span "from feasibility studies and detailed design, through to construction supervision
and commissioning". Used that. Note the press release calls it "Australian-based SMEC Holdings
Limited", so the nationality claim is sourced, not inferred from the name.

## Also checked, and clean

- Cuijiaying Complex Management Office: iw5, "HPTD created a special purpose unit, the Cuijiaying
  Complex Management Office (CCMO) … CCMO's key staff came from HPTD … also responsible for managing
  and operating the facility upon the completion of its construction." Exact.
- NGRC: "incorporated on July 2009" succeeding a preparation group "formed in September 2008". Exact.
- GXWCDC: "already operating similar complexes at Guigang and Guiping"; "has undertaken the
  construction of another navigation complex at Yuliang, and is also embarking on … a second ship
  lock" at Guigang. Exact.
- MoR FCTIC: "responsible for managing relations with foreign lenders to investment projects" (Third
  National Railway) and "FCTIC managed procurement" (NanGuang). Both limbs sourced.
- Tongyuan: footnote 11 of the Guiyang ICR, holding transferred in 2010 from the Guiyang State Assets
  Management Commission to the newly established GTDIG. Exact.
- Five Vietnamese power corporations: the EVN holding-company structure, the 220 kV / 110 kV franchise
  split, the 30 MW direct-purchase threshold, the PCom subsidiaries and the 2011 75-per-cent rural
  figure are all in one paragraph of the Distribution Efficiency ICR. Exact.
- SMEC's role on the Orissa card, which the batch's `uses` quotes: the Government of Odisha's section
  reads "The services of first CSC (SMEC) was terminated in Aug 2010 due to misrepresented facts."
  Verbatim, and the report gives no further detail — the card's framing is fair.

## Patterns worth carrying forward

1. **A sourced fact in the wrong document is still a sourcing failure.** The GuiGuang dates were real
   and sat one PDF away from the citation given. Grep the *cited* file for the *claimed* string before
   accepting a citation, not just the claim for plausibility.
2. **Watch figures that cross a corporate reorganisation.** CRC's registered capital, a 2019 number,
   was presented as a 2017 one. The general rule "never take a figure's year from the article's date"
   has a sibling: never take a figure's *entity* from the article's subject when the article is about
   a renaming.
3. **A sentence about what a project serves is not a description of a body.** Both municipal-government
   entries failed the same way, from the same kind of sentence ("the expressway would serve X city,
   an industrial center with…"). For a government key, require a sentence about the body's place in
   the state's structure or about a named unit beneath it, and accept a thin description over a rich
   one about its territory.
4. **Context sentences about neighbouring bodies leak into one-line descriptions.** The Guangdong
   bureau picked up the local bureaus' maintenance arrangements; the Hubei department picked up its own
   project office's loan count. In a one-liner the reader has no way to see the subject change.
5. **Dead and mis-titled citations: three of about thirty URLs.** One 404 (China Daily), one 403
   (Viet Nam News), one page whose title was a different regulation entirely (gov.cn). All three
   substantively right, all three unusable or misleading as cited. Worth a mechanical URL-and-title
   re-fetch pass at the end of every batch.
6. **Save API responses to disk.** All four World Bank projects-API claims checked out when I
   re-fetched them live, but nothing on disk could have shown that; the only JSON files saved were
   document-search results from a different endpoint.
