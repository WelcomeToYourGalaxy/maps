# Round 21 ICIJ-5 company descriptions — independent check

**In:** 15 descriptions, 17 blanks, 9 discrepancy items across 7 cases.
**Out:** 15 descriptions (1 dropped, 1 blank recovered, 11 of the 14 kept entries corrected),
7 verified card edits across 6 cases, dry-run clean (`records applied 6 ; problems 0`).

Every fact below was checked against a document I opened myself in this pass: 18 WebFetches and
11 WebSearches, plus the session cache under `/home/claude/r21/cache/` (the World Bank ICRs and
ICR Reviews the cards rest on). `base.html` was not modified — the dry-run ran on a throwaway copy
of `base.html` and `merge_textfix.py` in a scratch directory, which was then deleted.

## 1. The two entries the job named as its own weakest

**`Koridori Srbije d.o.o.` — kept, and the weakness removed.** The one-document problem is fixed by
a second, official source the job did not find: the Ministry of Economy's *Uredba o utvrđivanju
liste društava kapitala i manjinskih društava kapitala* (Službeni glasnik RS 77/2024, 97/2025,
`privreda.gov.rs/.../Uredba%20o%20utvrdjivanju%20Liste%20drustava%20kapitala-1.pdf`) names
«Коридори Србије» друштво с ограниченом одговорношћу Београд at entry 9 of the **majority
state-ownership list, category 1 (national and strategic interest)**. That documents three things
the entry lacked: the legal form, majority state ownership, and that the company still exists in
its own right at the date of that list — which also settles the merger worry well enough to leave
the disc item as the job left it (unresolved, not a correction). I opened the 2013 conference
report myself: it is dated 3 October 2013 and does carry the 2009 establishment, the investor
function, the four responsible ministries and 104 employees. **One figure was wrong:** the entry
said "works worth EUR 1.4 billion then under way". The presentation gives a *total project value*
of EUR 1.4 billion (its finance table totals EUR 1,404 million of loans and donations) and gives
the works under way separately as 129.7 km at 167 locations. Corrected to both.
On the aggregator question: a status report the company wrote and presented about itself is its own
document, not a third-party profile, so COMP.md does not exclude it; its 13-year-old figures are
labelled in the entry.

**`Jiangxi Airport Group` — dropped.** Two of the three legs fail. (a) After removing the
inference, the description reduces to "the airport operator for Jiangxi province", which is the key
name translated — the MIN Holding restatement test. (b) The only figure is one holiday week
(2,849 flights, 389,000 passengers, 1-7 October 2026), not a size figure; I confirmed the report
(`m.gmw.cn/2026-10/09/content_1304573610.htm`) gives **no ownership, no legal name and no airport
count**, and names six airports with figures for only four. (c) The identity link to the body in
the 2019 report stays inferred. What is salvageable is a card fix, not a description — see §5.

## 2. Testing the 17 blanks rather than accepting the structural account

Seven tested, six hold, **one recovered**.

- **`Department of Local Infrastructure Development and Agricultural Roads (DOLIDAR)` — recovered,
  and now described.** The job's own route stopped one page short. `www.doli.gov.np/oldsite/?p=140`
  is the department's **Function** page and carries real substance beyond the name: implementing
  agricultural and rural road programmes; planning, monitoring and evaluating local roads,
  irrigation, water supply, bridges, housing and rural energy; norms, standards, manuals and
  training; resource maps and technical studies for local authorities; environmental assessment and
  disaster mitigation. One of its bullets places the duties "within the Ministry of Local
  Development". `doli.gov.np/doligov/bagmati/?p=369` prints the current header — "Department of
  Local Infrastructure (DoLI)", "Ministry of Urban Development" — with a Local Infrastructure
  Development Program Office (LIDPO) for Bagmati under it. That satisfies both limbs of the
  government-key rule (place in the state's structure, a named unit beneath) without any instrument
  for the renaming, which the entry says.
- **`Cameroon Army Corps of Engineers` — blank holds, but the route is now open.** New finding: the
  presidency publishes Ministry of Defence appointment orders as PDFs on `prc.cm/files/...`, and the
  order of 28 September 2022 lists a **"DIRECTION DU GENIE MILITAIRE" under the État-Major des
  Armées** — an official document placing a military engineering body in the defence structure. I
  still blanked it, because equating that staff directorate with the troops the ICR calls the "Army
  Corps of Engineers (ACE)" is the CMEC/CMC risk, and `cameroon-tribune.cm` (paywalled after three
  paragraphs) gives only "ce corps d'élite des Forces armées" that also builds civilian works.
  Worth recording for a later round: the ICR's own identification is strong (P079736 has ACE
  building Mora-Dabanga and Dabanga-Kousseri, the same roads Journal du Cameroun credits to the
  génie militaire), so what is missing is the **formal name and creating instrument**, not the
  corroboration.
- **`Zhejiang Provincial Construction Commission Project Management Office` and `Xi'an Project
  Management Office` — blanks hold.** I ran round 20's municipal/provincial-server route properly:
  the one provincial-server document search returned
  (`zjjcmspublic.oss-...cloud.zj.gov.cn/.../6018df4c....pdf`) is the Zhejiang Provincial People's
  Government Gazette no. 12 of 2019 and does not mention a foreign-investment project office at all.
  Chinese searches on the offices' own names returned Bank press releases and unrelated provincial
  PDFs. The route works (the server serves, the gazette opened in full); the coverage does not reach
  these offices.
- **`Chancheng District Government` — blank holds.** Searches on the district government's own
  structure (机构设置 / 组成部门) returned Foshan land-resources attachment PDFs and press pieces
  about the district's development, i.e. the territory, not the body. Round 17's rule excludes that
  shape.
- **`Xining Chengtong Transportation Construction & Investment Co., Ltd.` — blank holds.** A search
  on the exact Chinese name returned no prospectus, rating report or registration page; the hits
  were other provinces' investment groups and sanctions-database entries, which do not qualify.
- **`Federal Ministry of Environment, National Project Implementation Unit` — blank holds, card
  fixed instead.** I opened the ministry's own updated Resettlement Policy Framework
  (`ead.gov.ng/.../UPDATED-NEWMAP-RPF-FEB.2018CLEAN-COPY.pdf`): it calls the body the **Federal
  Project Management Unit (FPMU)** throughout, says "The Federal Ministry of Environment established
  Federal Project Management Unit", and uses neither "National Project Implementation Unit" nor
  "National Project Management Unit". Everything else it says about the unit (support to state PMUs,
  monitoring and reporting to the Bank) is the card's role text. So there is nothing to describe
  that is not the role or the name — but the naming discrepancy is real and is now a card edit.

## 3. `EIT` — confirmed, stays blank

I grepped the three cached P006449 documents myself: `EIT` as a standalone token appears **0 times**
in `P006449_ICR.txt` (3,635 lines), `P006449_PAD.txt` (2,968 lines) and `P006449_ICRR.txt`. The key
rests on the Agência Pública field report alone, and the Natal contractor the name search turns up
is joined to the Gameleira works by nothing. The job's instruction to itself is right: do not fill
this key without a document naming the company's legal form, and the card should say the identity
is unsettled.

## 4. The three ownership-decay finds — all three verified, each phrased with its date

- **Albania.** Verified in the KLSH audit PDF: "sipas kontratave të nënshkruara nga **Drejtoria e
  Përgjithshme e Rrugëve (sot Autoriteti Rrugor Shqiptar)**", the Authority audited under Law no.
  10164 of 15.10.2009, and no date given for the change. The functions in the entry are the audit's
  own (programming investments, procuring studies and design, supervising works, the Technical
  Council approving terms of reference and cost estimates, expropriation requests to the Council of
  Ministers, the road inventory reported to the transport ministry). Card edit adds the present name
  without overwriting the old one.
- **Ethiopia.** Two corrections to the job's version. (a) **The December 2013 date does not hold.**
  The Addis Standard split story prints no date and dates the press conference to "Tuesday Dec.
  18th" — Dec 18 was a Tuesday in 2012, not 2013 — so the entry and the card now say 2013 on the
  strength of the regulations, not December 2013 on the strength of an undated page. (b) **The
  successor is Ethiopian Electric Utility, not a "service company".** ALN's 2024 Ethiopia power
  guide lists "Ethiopian Electric Power Establishment Regulation No. 302/2013 (381/2016 as amended)"
  and "Ethiopian Electric Utility Establishment Regulation No. 303/2013 (382/2016 as amended)",
  which is where the numbers come from; Addis Standard's own names (EEPO, EES) are transitional and
  are not used. (c) **A mis-titled citation:** the job cited `eng.addisstandard.com/?p=3519` as
  "Will Ethiopia sort out its energy puzzle?" — that is `?p=5228`; `?p=3519` is "Ethiopia splits
  state owned giant public utility into two". Title corrected to the page that was actually read.
  (d) The PolicyVault entry was dropped from the sources: I opened it, and it gives no regulation
  number and no date beyond "2013" (it is a database entry, the aggregator problem).
- **Serbia.** Verified twice over, and softened. Beta Briefing (22.12.25) names seven enterprises
  including "the Putevi Srbije road company" under the Law on managing companies owned by the
  Republic of Serbia; Biznis.rs (23.12.25) names six of them and says the change appears in the
  latest Official Gazette. **Neither gives a decision date, a Gazette issue number or an effective
  date, and Biznis.rs is forward-looking** ("will be converted"), so "the government converted it"
  was too strong: both entry and card now say a December 2025 decision published in the Official
  Gazette changes the legal form, with no effective date given. I also opened the founding decision
  itself (`putevi-srbije.rs/images/pdf/regulativa/decision.pdf`): 05 no. 023/8228/2005 of 22
  December 2005, in force 1 January 2006, founder the Republic of Serbia, seat Belgrade, core
  activity "the management of the state roads" — all as the job had it.

## 5. The three claims said to be unsupported — one of them is supported, and that matters

- **"all seven airports in Jiangxi" is the World Bank's own words, not an invention.** The cached
  ICR Review for P123729 says, twice, "the Jiangxi Airport Group (JAG, **which currently operates
  all seven airports in Jiangxi**)". The fault is the card's present tense on a 2019 "currently",
  not fabrication, so the fix dates the claim and adds the six airports the October 2026 report
  names, rather than deleting it. Had the disc item been applied as written, a sourced Bank
  statement would have been removed.
- **The NMCG ministry line is also sourced — elsewhere — and needs no fix.** The disc item is right
  that the 2016 Order does not place NMCG under the Department (I confirmed on the Order: s.31(1)
  society and authority; the Department appears only as supplying a Joint Secretary to the governing
  council under s.35(1)(b) and as support to the Empowered Task Force under s.17(5)). But the card's
  line traces to the completion report, not the Order: P119085's data sheet gives the implementing
  agency as "**Ministry of Jal Shakti, Department of Water Resources, River Development and Ganga
  Rejuvenation, National Mission for Clean Ganga**", and its footnote 5 records the transfer of the
  Ganga programme from MoEF to MoWRRD&GR with effect from 1 August 2014 and that department's
  incorporation into the new Ministry of Jal Shakti in May 2019. Two further attempts at an
  independent government source failed (the Standing Committee on Water Resources report truncated
  before its Namami Gange chapter; the March 2025 PIB document mentions no reporting line), so the
  Order's silence is not a contradiction. No card edit; the disc item should be recorded as
  "sourced in the ICR, not in the Order".
- **The Nigerian name is a real discrepancy and is fixed the round-17 way.** Both names on the card,
  with who calls it which — data sheet versus the report's own body and the ministry's framework —
  and **the key is untouched**, so the `merge_codesc.py` join still matches.
- **Nepal's DOLIDAR likewise.** The card's "local development ministry" is supported for the project
  period: the ICR (P083923) says "The Ministry of Federal Affairs and Local Development's Department
  of Local Infrastructure Development and Agricultural Roads (DOLIDAR)". The card now carries that,
  the department's own older "Ministry of Local Development" wording, and the current DoLI /
  Ministry of Urban Development publication, with the missing instrument stated.

## 6. The other corrections, by fault class

**Claiming more than the cited page says (6 entries).**
- `Energoinvest`: the article says "**The government** still owns 67%" and does not say which
  government. "The Federation of Bosnia and Herzegovina government held 67%" was the writer's
  expansion — removed. The article also does not mention substations or water works (those come
  from the company's own services page, which does: Substations, Transmission lines, Thermal power,
  Hydropower, waterways and water treatment) and does not state Sarajevo as the founding city (the
  company page gives the Sarajevo seat), so the entry now attributes each to the page that carries
  it, and the 67% is dated to the 2021 report.
- `Cameroon Railways (CAMRAIL)`: "The private operator" is not in the source, which says "l'unique
  concessionnaire du réseau ferroviaire au Cameroun" — changed to sole concessionaire. The tax and
  investment figures carry **no year** in the article ("chaque année"), which the entry now says;
  they were stated by the company at a business meeting of 26-27 February 2025.
- `Hohai University`: the figures' year came from the page's last-updated stamp, which is the "never
  take a figure's year from the article's date" trap in mild form — now "its own international
  school page, last updated in January 2015, gave…". "Run directly by the Ministry of Education" is
  the page's own "under the direct administration of Ministry of Education of China": kept.
- `Superintendencia de Obras Hidraulicas (SOHIDRA)`: "created in 1987" overstates the document,
  which says only that in 1987 the state put in place its institutional structure and gives no
  creation date for SOHIDRA itself — now "part of the water-sector structure the state set up in
  1987". The "vinculada à SRH" link and the works list are verbatim.
- `Office National de l'Eau et de l'Assainissement (ONEA)`: "it is responsible for the dam's upkeep
  and maintenance" omits the division the decree makes — article 3 gives ONEA routine upkeep and
  leaves major repairs bearing on the dam's stability and safety to the State. Added, with the
  symbolic 1 FCFA fee and the 1 July 2001 start.
- `Public Enterprise Roads of Serbia`, `Koridori Srbije`: see §4 and §1.

**Verified unchanged in substance (4):** `General Roads Directorate` (functions re-sourced to the
audit's own wording), `Department of Lands and Surveys` (bylaw 80/1999 clause 3 functions, 1857
origin, and no parent ministry claimed — correct, neither page names one), `National Directorate
for Water Resources Management (DNGRH)` (article 7(a) listing, article 9's 19 functions, the four
departments — the cleanest entry in the batch), `National Mission for Clean Ganga`,
`Secretaria dos Recursos Hidricos do Ceara` (Law 11,306 of 1 April 1987, direct administration,
Decrees 32,957 of 13 February 2019 and 33,215 of 19 August 2019), `Ministry of Public Works and
Housing` (1923 "Al Naf'a" department, transport ministry 1939, Ministry of Public Works 1954 — the
1939 step was missing and is added).

**The restatement test on the government entries.** Applied to all 15 and to the seven blanks I
tested. It took out `Jiangxi Airport Group`. It did not take out DNGRH, SRH, SOHIDRA, ONEA, NMCG,
the two Jordanian bodies, the two Serbian ones, Albania's directorate or the recovered Nepali
department: each has a function list, an instrument, or a named unit beneath that survives deleting
the name. None of the 15 descriptions describes a territory.

## 7. What I could not check, and what stopped it

- **The date Albania's directorate became the Road Authority.** The only document that equates them
  does not give it, and `arrsh.gov.al`'s own PDF of Law 10164 returns the site's WAF page (the job's
  finding, not retested). The entry and card therefore say "today", with no date, as the audit does.
- **Koridori Srbije's founding act and current accounts.** The Serbian State Audit Institution's
  2022 audit of the company exists at `dri.rs/storage/upload/documents/revision/2022/2022-4-Koridori
  Srbije.pdf` and would settle both, but the fetch returned **robots_disallowed**. That is a
  route-level refusal on one path, not a host block — `dri.rs` was not otherwise tested, and the
  ownership question was answered from the Ministry of Economy list instead.
- **An independent source placing NMCG under the Department of Water Resources.** Two tries: the
  Standing Committee report (`eparlib.sansad.in/.../18_Water_Resources_11.pdf`) served but was
  truncated at 100,000 of 256,453 characters, before its Namami Gange chapter; the PIB document
  carries no reporting line. Not a failed route — a page-length limit and a document that does not
  say it.
- **Ethiopian Electric Power's establishment regulation in its own text.** Not reachable here: the
  gazette is not online by any route search returned, and the number comes from a law firm's table
  of applicable laws. A later round wanting the primary text should try the FDRE gazette or
  `leap.unep.org`'s FAOLEX records, which do serve for other Ethiopian instruments.
- **Jiangxi Airport Group's ownership.** Three Chinese searches (ownership, establishment, company
  profile) returned only the holiday-traffic report, stock-exchange PDFs for unrelated issuers and
  aggregator profiles. Nothing was refused; nothing exists on the open web that search reached.

## 8. Faults appearing in more than one entry

1. **A relationship or attribute the cited page does not carry — 6 of 14 kept entries**, and it is
   the same fault round 20 found in 8 of 16: Energoinvest's government (which one?), CAMRAIL's
   "private", ONEA's undivided maintenance duty, SOHIDRA's creation date, Serbia's completed
   conversion, Koridori's "works under way". In every case the page supports something adjacent and
   weaker.
2. **A figure's year taken from its container** — Hohai (page stamp), CAMRAIL (meeting date), and in
   the opposite direction Jiangxi (a holiday week standing in for a size figure).
3. **A citation whose title is not the page** — one (the Addis Standard swap of `?p=3519` and
   `?p=5228`), the same class as round 20's three dead-or-mis-titled URLs. A mechanical title
   re-fetch at the end of a batch would still be worth its cost.

## 9. Routes, named as routes

**Worked:** search-then-fetch, every time (the job's finding holds — 18 of 18 fetches of
search-returned URLs served, including three PDFs over 100,000 characters). `privreda.gov.rs`
serves ministry regulation PDFs — the route that rescued Koridori Srbije, and the general lesson is
that **a Serbian company's ownership is in the Ministry of Economy's list of state-owned capital
companies, not in the company's own pages**. `prc.cm/files/...` serves presidency and defence
appointment orders, which name directorates inside Cameroon's Ministry of Defence — untried before
this pass. `doli.gov.np/oldsite/` serves a Nepali department's pre-rename pages alongside its
current ones on the same host, which is how a renamed body can be described without an instrument.
`klsh.org.al`, `faolex.fao.org/docs/pdf/`, `progestao.ana.gov.br`, `ampeid.org`, `ead.gov.ng`,
`casemine.com`, `dls.gov.jo`, `portal.jordan.gov.jo`, `form.jordan.gov.jo`, `energoinvest.ba`,
`intellinews.com`, `financialafrik.com`, `addisstandard.com`, `biznis.rs`, `betabriefing.com`,
`aln.africa`, `eparlib.sansad.in`, `static.pib.gov.in`, `m.gmw.cn`, `putevi-srbije.rs`,
`transport.danube-region.eu` and `zjjcmspublic...cloud.zj.gov.cn` all served.

**Failed, as routes and not as hosts:** one PDF path on `dri.rs` returned robots_disallowed (the
host is otherwise untested here); `cameroon-tribune.cm` serves but paywalls after the opening
paragraphs (a paywall, not a refusal); two long PDFs were truncated at 100,000 characters by the
fetch tool, not by their servers, and the missing part was re-reachable in principle with an offset.
Nothing in this pass justifies adding a host to a blocked list.

## 10. Addendum — SOHIDRA: groundwater or hydraulic works (conflict resolved, no disagreement)

Asked to settle this against the P006449 completion report, I read the three places named and agree
with the whole-picture-text checker, on the documents rather than on its say-so:

- **Acronym list (line 135):** "SOHIDRA  Superintendência de Obras Hidráulicas do Ceará  **Hydraulic
  Works Company**".
- **Paragraph 943:** a state company (COGERH) was created in 1993 to manage bulk water, "alongside
  **an agency responsible for construction of hydraulic works (SOHIDRA)**".
- **The supervision paragraphs** (the report's account of the builder left supervising itself):
  "None of the works had supervision contracts in place as the Government decided to discontinue
  supervision activities through external firms (**supervision was done through SOHIDRA**) … This
  decision had impact in the quality of supervision of works and environmental mitigation activities
  as **SOHIDRA does not have enough staff** to carry out the required close supervision of all
  works", and, later, that the Government decided "to continue supervision of works via the State
  superintendence responsible for surveillance of contractors' performance (SOHIDRA), **which is not
  adequately staffed**". The ICR also lists SRH as the main implementing agency with COGERH and
  SOHIDRA executing.

**There was no conflict to resolve in my file: nothing in it ever carried a groundwater reading.**
The string "groundwater" appears zero times in `r26f_icij5_companies_checked.json`; my entry already
read "the water-works executing body of the state of Ceará … builds and supervises dams, integration
axes, canals, pipelines, wells and water supply systems". The "wells" (*poços*) in that list is one
item of the works list in ANA's Progestão synthesis, not a groundwater remit, and it is the only
thing in the entry that could be misread that way.

**Change made anyway, in place, key untouched:** the entry now leads with the identification in the
report's own words — the state's hydraulic works agency, the body that builds the works — quoting
the acronym list and paragraph 943, with the ICR added to its sources. The point is to make the
contested fact explicit in the text so this cannot be read two ways again. The supervision facts
above were deliberately **not** put in the `desc`: they are the case's role, which COMP.md keeps off
the description, and the card already carries them.

The entry count is unchanged at 15, the file still validates, and nothing else was touched. The
textfix file and its dry-run are unaffected.
