# Round 20, ICIJ tranche 4 — entity descriptions: independent check

16 descriptions checked, 11 blanks examined. **13 of the 16 descriptions corrected, 2 dropped,
1 blank filled.** 14 reported discrepancies worked through: 6 confirmed and turned into card
corrections, 2 more card corrections added that the job did not propose, 1 withdrawn outright
because the card is right, the rest left as flags.

Outputs: `r26f_icij4_companies_checked.json` (15 entries), `r26f_icij4_companies_textfix.json`
(7 cases, 8 edits, dry-run validated against `base.html` — every `old` occurs exactly once).
Nothing merged, nothing built, no git.

## 1. The two the job named as its own weakest

**`Dar Rapid Transit Agency` — dropped.** The whole entry rested on one self-description line in
DART's own tender notice as republished by dgmarket. COMP.md excludes aggregators and HANDOFF
names them "the single commonest bad source"; a tender aggregator is the same problem in a
different dress, and the Government Notice itself was never reached. I looked for a qualifying
substitute and did not find one: the agency's establishment instrument appears nowhere in
tanzlii's infrastructure-and-transportation listing or its statutory-instruments pages; the one
DART-authored document I did open, a 2017 African Carbon Forum presentation by a DART transport
planning engineer hosted on unfccc.int, says only "DART Agency established 2007" and gives no
instrument, no ministry and no functions. The national audit office does have a performance audit
of BRT Phase II infrastructure, which would almost certainly carry the institutional sentence, but
that fetch was stopped by an unanswered permission prompt (see §7). Blank with a note; worth one
retry in a session where prompts are answered.

**`Direccion Provincial de Vialidad, Province of Santa Fe` — rewritten, ministry attachment
removed.** The job was right to distrust it, and the sources are weaker than it said. I opened
both. The budget document is a **two-page extract of the province's investment-project programming
for fiscal year 2009** — the entry gave no year — and in it the directorate appears only as the
*unidad ejecutora* of one project under the heading "Jurisdicción: 62 - MOP y Vivienda, Entidad:
601 - Vialidad". The document never expands "MOP y Vivienda", so "the Ministry of Public Works and
Housing" was the writer's expansion, and it nowhere states that the directorate sits under it. The
2025 tender page names "Organismo: Ministerio de Obras Públicas" and separately names the
directorate as the place of bid opening, and states no relationship between the two. Both supports
for the ministry attachment are gone. What survives and is in the new description: the Boulevard
Muttis 880 address, its own Dirección General de Proyectos at the same address (a named unit
beneath it, which is what the government-key rule asks for), the provincial-route repaving tender,
and the 2009 budget classification stated as a budget classification rather than as an
organisational fact.

## 2. The restatement test on every government entry

Applied to all 14 government entries. It bit twice.

- **`State Council Leading Group Office for Poverty Reduction`.** "that ran the state's poverty
  reduction work" has no support but the words 扶贫开发 inside the body's own name — the Xinhua
  report says nothing about what the office did, and I checked. Cut. **It also carried a date
  fault:** the entry said it "ceased to exist on 25 February 2021, when its sign was taken down".
  Xinhua says the opposite order — "'国务院扶贫开发领导小组办公室'的牌子此前已经永久摘下", the sign
  had *already* been permanently removed, and what happened at 16:00 on the 25th was the new
  National Administration for Rural Revitalization's sign going up at No. 1 Taiyanggong North
  Street, Chaoyang, Beijing. Rewritten to the order the source gives, and the entry now says the
  report does not record the office's functions.
- **`Resettlement Research Center, Hohai University` — dropped.** This is the clean fault-2 case of
  the batch, not Pöyry. Neither source names the key. Hohai's research-institution listing carries
  "Research Center of Reservoir Resettlement Economics, Ministry of Water Resources" and, I
  confirmed, contains no institution with "Immigration" in its name at all; the School of Public
  Administration page (which calls itself School of Public Management in its body text) says only
  that the school has "15 research institutions including Immigration Research Center, Applied
  Psychology Research Institute, Political Science Research Institute and Population and
  Development Research Center" and never uses the word resettlement. Two differently-named
  candidate units, no document joining either to the key. The entry also called Hohai "a Chinese
  public university whose field is water resources" — neither cited page says that, and 河海
  ("rivers and seas") inside the name is not a source. Blank. The two candidates are recorded here
  for the owner, not on the card.

A third entry failed the related rule — *a description of the territory is not a description of
the body* — in the opposite direction from the usual: `Accra Metropolitan Assembly` correctly left
out the census figures, but what remained was thin when the Assembly's own page carries real
structure. It now has section 12(3) of Act 936 as the Assembly's own account of what establishes
it and sets its functions, the 34-member composition of the General Assembly (20 elected, 10
government appointees, 3 MPs, plus the Metro Chief Executive who chairs the Executive Committee),
and the ten Sub-Metropolitan District Councils named as subordinate bodies on the History page.
The entry had asserted the subordinate councils without the number and without that page.

## 3. The 41 per cent blank rate — tested on four, and the explanation holds for three

- **`Anhui Provincial Transport Department` — the blank was wrong; description written.** The job
  said no provincial duties-and-structure document could be reached and that the page it opened
  was a municipal bureau describing itself. The document I opened on the same municipal host
  (`jtj.huainan.gov.cn`) is not the municipality's: its cover names the issuer as **安徽省交通运输厅,
  October 2022**, and it is the provincial department's own expressway traffic-enforcement station
  layout plan. It carries sentences about the department itself, not about Anhui: in 2003 the
  department, with the provincial office of establishment, applied the separation of government
  from enterprise and moved the road-administration functions then carried by expressway operating
  companies to the former Provincial Highway Administration Bureau; the provincial government
  tasked it with selecting enforcement-station sites with expressway owners and supervising
  construction within three years; and it issued a province-wide three-year plan for standardising
  comprehensive transport administrative enforcement. That is a place in the state's structure and
  a named unit beneath it. **The lesson is the one round 12 already wrote: a body's own document
  can sit on another body's host.** The search that finds it is for the department's name plus
  职能/职责, with the municipal hosts read rather than skipped.
- **`Naya Raipur Development Authority` — blank stands.** I could not reach the authority's own
  portal (`nrda.co.in`, stopped by the dead permission prompt) and no gazette notification
  surfaced; every result naming "Nava Raipur Atal Nagar Vikas Pradhikaran" is an encyclopedia,
  a property portal or a news aggregate. The rename flag is correctly left on the card.
- **`Poyry Energy Ltd` — blank stands, but see §4: the job's reason for it is wrong.**
- **`Chongqing Project Management Office` — blank stands, and tested properly.** I searched the
  Chongqing municipal transport bureau's own budget disclosures and opened one of them; it lists no
  unit whose name contains 世界银行, 世行 or 项目管理办公室. A loan project office that does not
  appear in its parent's budget establishment is not a standing unit of the government, which is
  what the four PMO blanks turn on.

So the structural explanation survives for the Chinese loan offices and bureaux but **not for the
provincial department**, and the job's own sentence — "a provincial transport department is a
routine body, but 'routine' is not a source" — was true of the search it ran, not of the record.

## 4. `Poyry Energy Ltd` — the job's finding is wrong in a way that matters

The report says "the name matches no corporate record". It matches several. **Pöyry Plc's own
annual report for 2008** (the company's own report; I opened the group-companies listing at pages
36-37) lists **21 group companies with "Energy" in the name, across 13 countries**, including an
exact-name match:

- "Pöyry Energy Ltd — Thailand, Bangkok — 100.0"
- "Pöyry Energy AG — Switzerland, Zurich — 100.0"
- "Pöyry Energy Limited — United Kingdom, Horsham — 100.0"
- "Pöyry Energy Oy — Finland, Espoo — 100.0"
- "Pöyry Energy GmbH — Austria, Vienna — 74.9"; and seventeen more.

So the blank is still right, for the opposite reason: not that no entity bore the name, but that
too many near-identical ones did, and nothing says which prepared the Rogun ESIA. That is fault 2
exactly — the group facts describe the parent. Following the round-17 precedent the card is not
renamed; it now carries the ambiguity with the four closest names, sourced to Pöyry's own annual
report. **I did not carry the ÅF/AFRY facts onto the card**: the job's source for the 21 February
2019 completion and the AFRY renaming is a press release I did not open, and this file only
publishes what I opened myself. If the owner wants the acquisition on the card, that press release
needs opening first. The route that would settle the entity outright is the Rogun ESIA's own
cover page; the World Bank documents API fetch that would find it was stopped by the dead
permission prompt.

## 5. The 14 reported discrepancies, one by one

**Confirmed and now card corrections (6):**

1. **DNV dissolved — `santa-fe-road-19-expropriation`.** Decree 461/2025 opened on
   argentina.gob.ar. Article 1 dissolves the Dirección Nacional de Vialidad; Article 6 substitutes
   Article 2 of Decreto-Ley 505/58 so that "EL MINISTERIO DE ECONOMÍA, tendrá a su cargo el
   estudio, construcción, conservación, mejoramiento" and that "En todas las disposiciones del
   presente y su reglamentación en las que se mencione a la DIRECCIÓN NACIONAL DE VIALIDAD …
   deberá entenderse que dicha referencia corresponde al MINISTERIO DE ECONOMÍA"; Article 37 puts
   it in force on publication. Signed 07/07/2025, published 08/07/2025. Written in the standing
   form — the DNV held the role at the time, the 2025 decree dissolved it.
2. **The founding instrument — same case.** Confirmed: the decree recites "Que mediante el
   Decreto-Ley N° 505/58 se constituyó la mencionada Dirección Nacional como organismo autárquico"
   and **Ley 11.658 of 1932 appears nowhere on the page.** Both sides are on the card: the decree
   recites the 1958 decree-law, and the 1932 law is the date usually cited. A 1958 decree-law
   reconstituting a body is not necessarily its creation, and the card no longer has to choose.
3. **Ghana's ministry merged out of existence — `kwabenya-landfill-expropriation`.** Confirmed from
   the NDPC plan, **with a correction to the discrepancy as reported**: the merged predecessor the
   plan names is the **Ministry of Local Government, Decentralisation and Rural Development**, a
   longer title than the card's and than the key's. The job's description silently treated the two
   as the same body and attached the successor's mandate to the card's name. Both the card fix and
   the description now say the card's name is the one the project documents use, and give the
   plan's own name for the predecessor. The plan is also internally inconsistent about the third
   merged ministry — "the Ministry of Sanitation" in Chapter One, "the Ministry of Sanitation and
   Water Resources" in the Executive Summary — and the card gives both.
4. **Barqi Tojik's legal name and the 2018 split — `rogun-stage1-resettlement`.** Confirmed from
   the audited accounts themselves (Note 1: "Open Joint Stock Holding Company "Barqi Tojik" … was
   registered in the Ministry of Justice of the Republic of Tajikistan on June 3, 1999"; sole
   shareholder the Government). **I replaced the job's source for the split.** It cited an
   Asia-Plus news report saying two companies "were established"; the accounts' own Note 2 cites
   "Decree of the Government of the Republic of Tajikistan # 234 of April 28, 2018" and says ten
   subsidiaries **are to be** merged into new OJSCs for transmission and distribution grids, with
   management unable yet to assess the effect. The primary document is better and its tense is
   more careful, so the card carries that and not the news report.
5. **KURA's remit — `nutrip-road-compensation-arrears`. Confirmed, with a second side the job
   missed.** KURA's own page states the remit **twice and not identically**: under "Our Mandate"
   as "the Management, Development, Rehabilitation and Maintenance of all national urban roads",
   and under "Who we are" as "national trunk roads within urban areas". The card's "urban roads" is
   therefore closer to one of the body's own two formulations than the discrepancy allowed. The fix
   gives both wordings rather than replacing one claim with another, plus the 4,625 km.
6. **TAA operates rather than owns — `bukoba-airport-resettlement-arrears`.** Confirmed from G.N.
   No. 404 of 1999 on TanzLII: established "as an Executive Agency in relation to the Department of
   Aerodromes", commenced 29 November 1999, role "to operate, manage, maintain and develop
   Government-owned airports in a professional and cost-effective manner", responsible minister the
   Minister for Communications and Transport. "Owns" overstated it and is corrected.

**Withdrawn — the card is right (1):**

7. **National Land Commission's valuation-and-payment role — `nutrip-road-compensation-arrears`.**
   The job flagged the card's "values and pays for land taken by compulsory acquisition" as
   unsupported and asked for a Land Act citation. I opened the Act — Part VIII of the Land Act
   (Cap. 280, Act 6 of 2012) — and the card is correct in both halves. Acquiring authorities
   "submit a request for acquisition of land to the Commission" (s. 107(1)), which the Commission
   may reject (107(3)); if it proceeds it "cause[s] the affected land to be mapped out and valued
   by the Commission" (107(4)); it appoints and holds the inquiry, receives written claims and has
   "all the powers of the Court to summon and examine witnesses" (s. 112); it "shall prepare a
   written award" and "make a separate award of compensation" for each interested person, the award
   being conclusive evidence of "the value, in the opinion of the Commission, of the land"
   (s. 113); and it "shall, promptly pay compensation in accordance with the award" (s. 115(1)),
   from funds the acquiring authority "shall deposit with the Commission" (s. 111(1A)). **No card
   correction.** The role simply sits in the Land Act rather than in the Article 67(1) list on the
   Commission's own history page, and the description now carries it with section numbers. One
   caveat recorded rather than hidden: the text I read is the revision as at 4 November 2025, so
   subsections 107(3A) and 111(1A) are later amendments; 107(4), 113 and 115 carry the substance.

**Left as flags, correctly (3), one of them now with evidence:**

8. **Nanchang's registered name — `nanchang-line-2-demolition`.** Flag kept and tightened. The
   filing gives 南昌轨道交通集团有限公司 and **no English name anywhere in the document**, which the
   job's description did not say: it presented "Nanchang Rail Transit Group Co., Ltd." as the
   registered name when it is a translation. Both the description and the card fix now mark it as
   a translation.
9. **Naya Raipur → Nava Raipur Atal Nagar Vikas Pradhikaran — `sutp-brts-corridor-displacement`.**
   Flag correctly kept; no notification or own-portal page reachable (§3). No card change.
10. **Huzhang / Zhanghu ordering — `zhanghu-railway-resettlement`.** Flag kept, and it is no longer
    empty. Two documents I opened show **both orderings are in official use, for different lines**:
    China's environment ministry, approving the new Datong–Zhangjiakou passenger line in July 2015,
    calls the existing conventional line 呼张铁路 ("Huzhang") and names 怀安站 on it as the new
    line's western starting point; the new passenger line's published environmental impact report
    is titled 新建张家口至呼和浩特铁路 ("Zhanghu"), a double-track passenger line of about 286 km
    from Zhangjiakou South to Hohhot East. So the case id and the company key are each tracking a
    real name, and neither is a typo. Still no state register entry for the company, so the key
    stays as the completion report has it. (The 2015 approval's 建设单位 is 中国铁路总公司, not the
    project company, which is consistent with the card already naming China Railway Corporation.)

**The remaining reported items (KeNHA "right but unspecific", HDBRTS's absent department and
incorporation date) are not discrepancies and I have not made cards of them.** One small
overclaim from the KeNHA page did need fixing in the description: its own page says KeNHA was
"inaugurated in September 2008", not that it "began operations" then.

## 6. The Nanchang figures, converted by hand

Checked against the filing, not against a summary. "截至 2019 年 3 月底，公司注册资本和实收资本均为
26.15 亿元，南昌市国资委持股 100.00%" and "截至 2019 年 3 月底，公司合并资产总额 724.95亿元，
所有者权益 382.28亿元（其中少数股东权益 1.10亿元）". 亿 is 10^8, so 26.15亿 = RMB 2.615 billion and
724.95亿 = RMB 72.495 billion. **The job's figures are right and its warning about the summariser's
factor-of-ten error is sound** — I converted from the Chinese characters and arrived at the same
numbers. The filing also yields two things the entry did not use and now does: the business scope
("负责轨道交通项目的工程投资、建设、工程咨询、设计、负责轨道交通的营运、负责轨道交通的通讯及其他
特许经营权的经营") and "公司是南昌市轨道交通投资建设和运营管理的实施主体", so the sector claim no
longer rests on the words inside the company's name. Owners' equity of 382.28亿元 (RMB 38.228bn) is
available if wanted. The filing gives no incorporation date and no approving body.

## 7. Closing items

**Could not check, and what stopped it.** Four things, all stopped by the same mechanism: **an
early permission prompt went unanswered, and from that point every fetch needing a new permission
failed immediately with `PROVENANCE_REQUIRED` and the message that the earlier request had not been
answered in time.** This is the exact failure mode the handoff warns has been misrecorded as a host
refusal eleven times, so it is named as a mechanism here and not as a list of hosts:
- the national audit office's BRT Phase II performance audit, which is the best candidate source
  for `Dar Rapid Transit Agency` — note that a *different* path on the same audit office host
  fetched normally in this same session, which is the proof that this is not a host refusal;
- the World Bank documents API query that would locate the Rogun ESIA cover and settle which Pöyry
  entity prepared it;
- `nrda.co.in`, the Naya Raipur authority's own portal;
- a TanzLII site search for the DART establishment order — again, TanzLII's `/en/akn/...` document
  path fetched normally in the same session.
Each of these is worth exactly one retry in a session where prompts are answered. None of them is
evidence that any host refuses.

**Faults appearing in more than one entry.**
- **Claiming more than the page says — 8 of the 16.** Nationality was not the vector this time
  because almost every entry is a government body; the vector was **an institutional relationship
  the page does not state**. Santa Fe's ministry attachment, Pimpri Chinchwad's "overseen by the
  state's Urban Development Department through the Director of Municipal Administration" (the CAG
  chapter says the UDD issued notifications and that the DMA was responsible for preparing the
  account code — it never says either oversees the corporation), TANROADS "constituted by order
  under the Executive Agencies Act" (the audit cites Rule 3(3) of the Executive Agencies (TANROADS)
  (Amendment) Order No. 350 of 2009 and names no Act), Ghana's successor mandate attached to the
  predecessor's name, KeNHA's "began operations", Nanchang's English name, Hohai's field, and
  TAA's "Aerodromes (Licensing and Control) Act", which I removed because I could not find it in
  the order I read. **This is one fault with one shape, and it is worth putting in the writer's
  brief in these words: for a government body, the sentence "X sits under Y" needs a page that
  says X sits under Y — a budget heading, a tender's organismo field, a shared document, or a
  ministry that supervises one named function are each short of it.**
- **A missing year on a figure — 3 entries.** The Santa Fe budget extract (2009), the CAG
  Maharashtra classification (year ended 31 March 2015) and the TANROADS kilometres (the Roads Fund
  Board's annual report of June 2019, as cited by the audit) all carried the claim without the
  date. COMP.md asks for the year on every figure and the writer dropped it wherever the figure
  came from an audit rather than from a filing.
- **Restatement of the name — 2 entries** (§2), both Chinese or Chinese-university bodies, where
  the name is a functional description in translation and reads like a sourced sector claim.

**Routes.** Working, as routes: `saiindia.gov.in/uploads/download_audit_report/...` serves the
Indian audit chapters and appendices directly, confirming the job's finding; the Tanzanian audit
office's `/uploads/reports/...` path serves; `static.sse.com.cn/disclosure/bond/announcement/...`
serves Chinese bond disclosures including rating reports; `mee.gov.cn/gkml/...` serves Chinese
environmental approvals, which name project lines and 建设单位 and are the cheapest official route
into Chinese railway and water projects; `tanzlii.org/en/akn/tz/act/gn/...` serves Tanzanian
establishment orders; `faolex.fao.org/docs/pdf/` serves statute texts and is the route that settled
the Kenyan Land Act — read it with `offset`, since Part VIII sits past 150,000 characters;
`web.lib.aalto.fi/fi/old/yrityspalvelin/pdf/<year>/` serves Finnish listed companies' own annual
reports, and the group-companies listing is near the end of the file, so go in at offset. **A route
that looks like a dead end and is not:** Chinese provincial departments' own documents are hosted on
*municipal* government servers, so a municipal host in the results is worth opening even when the
target is provincial — that is what filled the Anhui blank.
