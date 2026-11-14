# Round 21 company descriptions — ICIJ tranche 5

**32 names in. 15 descriptions written, 17 honest blanks.** The batch is almost all state
bodies — project management offices, municipal and district governments, roads and water
directorates, a national clean-river mission, an army engineering corps and two university
resettlement research centres — so the blank rate (53%) is close to round 20's and comes from the
same place: a completion report names an implementing agency and nothing else names it again.

**A route finding that shaped the whole pass, and should go in the next brief.** In this
environment WebFetch serves URLs that came back from a WebSearch result, and refuses URLs I built
myself: six constructed URLs returned `PROVENANCE_REQUIRED` with an unanswered permission prompt
(`arrsh.gov.al/historiku/`, `nmcg.nic.in/about_nmcg.aspx`, `doli.gov.np/introduction`,
`mpwh.gov.jo/EN/Pages/About_The_Ministry`, the `saiindia.gov.in` copy of CAG report 39/2017,
`sohidra.ce.gov.br/institucional/`, and a CGU redirect target). None of these is a blocked host —
every one of those bodies was then described or progressed from a search-returned URL on the same
or a sibling host. **Search for the page, then fetch the URL the search returns.** Two other
single-route failures, also not host blocks: `cge.ce.gov.br` returned `robots_disallowed`, and
`arrsh.gov.al`'s own PDF of the Road Authority law returned the site's WAF page
("requesti ... permban kod keqdashes").

Confirmed from round 20's notes: **`cag.gov.in` 302s its audit PDFs to a CloudFront host**
(`d1jmc0u14z2tmp.cloudfront.net`) — it did it again on report 39 of 2017. `faolex.fao.org/docs/pdf/`
served a statute text first time. The ampeid.org mirror of Mozambique's gazette documents served a
119,000-character ministerial regulation, truncated at 100,000 but with the article I needed well
inside it.

## What was written

1. **Public Enterprise Roads of Serbia** — the founding instrument itself: Government Decision
   05 no. 023/8228/2005 of 22 December 2005, in force 1 January 2006, Republic of Serbia as
   founder, core activity "the management of the state roads". Opened the decision on
   `putevi-srbije.rs`, plus Beta Briefing on the December 2025 conversion to a limited company and
   N1 on the 2025 accounts. Strongest entry in the batch.
2. **Koridori Srbije d.o.o.** — the company's own 2013 status report, hosted on the EU Danube
   Region transport programme site: established 2009, limited liability company, investor function
   in motorway construction, international tenders, expropriation, project documentation, four
   responsible ministries, 104 employees, EUR 1.4bn of works. **I did not write "state-owned"**:
   the only page calling it public-owned is the undated World Highways merger piece, and the
   company's own report names responsible ministries without naming an owner.
3. **General Roads Directorate (Albania)** — the Supreme State Audit's 2016 audit of the Albanian
   Road Authority, which both describes the functions (planning and contracting road studies,
   design, supervision and construction; a technical council approving designs and estimates;
   requesting expropriations) and says in its own words that the General Roads Directorate is
   today the Albanian Road Authority, under Law no. 10164 of 15 October 2009.
4. **Ministry of Public Works and Housing (Jordan)** — Jordan's e-government portal: roads,
   designs and studies for public, village and agricultural roads, government buildings, materials
   testing, road and building legislation; predecessor department from 1923, ministry from 1954.
5. **Department of Lands and Surveys (Jordan)** — the same portal plus the department's own history
   page: functions under bylaw no. 80 of 1999, including valuation for registration and land taken
   for the public interest, which is the function the case turns on. **Neither page names a parent
   ministry**, so none is claimed.
6. **National Directorate for Water Resources Management (DNGRH)** — Ministerial Diploma no. 12/2022
   of 25 January 2022, the internal regulation of Mozambique's Ministry of Public Works, Housing and
   Water Resources: article 7(a) lists DNGRH as a ministry unit and article 9 sets its functions,
   and it names the four departments beneath it. This is the clean case of the government-key rule
   being satisfiable: ministry named by the instrument, and named units beneath.
7. **National Mission for Clean Ganga** — the 2016 Authorities Order itself (ss. 31-47): a
   registered society that is also an authority under the Act, nodal agency for the order, basin
   management plan, power to direct state and district Ganga committees, CAG audit. See the
   discrepancy file for what the Order does **not** say about its ministry.
8. **Office National de l'Eau et de l'Assainissement (ONEA)** — the 2003 Ziga dam concession decree
   on FAOLEX, whose preamble cites Decree 85-387 of 22 July 1985 creating ONEA and Decree 94-391 of
   2 November 1994 turning it into a state company, and whose articles give the 40-year concession
   from 1 July 2001 and the maintenance duty.
9. **Secretaria dos Recursos Hidricos do Ceara** and 10. **SOHIDRA** — both from the national water
   agency's synthesis of Ceara's first Progestao cycle (August 2019): SRH created by state Law
   11,306 of 1 April 1987, a body of the direct state administration, with its structure set by two
   2019 decrees; SOHIDRA "vinculada a Secretaria dos Recursos Hidricos", the executing body for
   water works, created in 1987, building dams, transfer axes, canals, pipelines, wells and supply
   systems. The federal water agency is a government source, not a lender's project document.
11. **Ethiopian Electric Power Corporation (EEPCo)** — Addis Standard on the December 2013 split,
    plus the PolicyVault entry for the 2013 Council of Ministers regulation establishing Ethiopian
    Electric Power. **I did not write that EEPCo was formally dissolved by a numbered regulation**;
    no text I opened says that.
12. **Energoinvest** — bne IntelliNews (founded 1951 in Sarajevo; substations, transmission lines,
    hydro and thermal plants, mainly Africa and the Middle East; Federation government holds 67%;
    over 54,000 staff before the war) and the company's own services page. Identity to the firm in
    the case rests on the completion report's own words, "Energoinvest of Bosnia & Herzegovina".
13. **Cameroon Railways (CAMRAIL)** — Financial Afrik, March 2025: 918 km Transcamerounais, took
    over Regifercam under the 1999 concession, Bollore then Africa Global Logistics, the tax and
    investment figures it states itself. No shareholding percentages are claimed because the
    article gives none.
14. **Hohai University** — its own international school page: founded 1915, run directly by the
    Ministry of Education, water conservancy specialism, 46,921 students and 3,409 faculty, figures
    dated 2015 on the page and labelled as such.
15. **Jiangxi Airport Group** — a CCTV/Guangming report of 9 October 2026 naming the airports it
    runs and its holiday traffic. **Ownership is not claimed**: no page opened says who owns it, so
    the card's "provincial airport operator" is carried by the airports it runs, not by a stated
    shareholder.

## Why each blank is blank

**Nine Chinese project offices, municipal bodies and local companies** — nothing beyond the Bank's
own documents names any of them. Searched for each in Chinese (own name plus 简介/成立/国有/国资委,
and for the investment company its bond and rating paper trail): **Xi'an Project Management
Office**, **Wuhan Urban Construction Utilization of Foreign Investment Project Management Office**,
**Qingyang Project Management Office**, **Shangrao Sanqingshan Airport Construction Office**,
**Zhejiang Provincial Construction Commission Project Management Office** (searched the provincial
construction department's foreign-investment office; the municipal-host route from round 20 turned
up only unrelated provincial PDFs), **Qingyang Municipal Water Supply and Sewage Company**,
**Xining Chengtong Transportation Construction & Investment Co., Ltd.** (no prospectus, rating
report or registration page found), **Shangrao Sanqingshan Airport Company Limited** (only airport
pages, not the company). On the standing test, every available description of these would be a
restatement of the name.

**Three governments: Xining Municipal Government, Laibin Municipal Government, Chancheng District
Government.** Blanked on the rule rather than for want of searching: what is available about them
is a description of the territory they govern — a prefecture-level city in Guangxi, a district of
Foshan — which the round-17 rule excludes, and the rest ("the municipal government of X") is the
name again. A city government's own departmental list would satisfy the named-unit-beneath limb,
but the cards already print the municipal bodies and offices involved, so the entry would restate
the role.

**Center for Involuntary Resettlement Research, Wuhan University** and **Involuntary Resettlement
Research Center, China Three Gorges University.** Searched both in Chinese. Nothing names either
centre — no university page, no founding notice. This is round 20's blanked university centre
again, on the same test: "a resettlement research centre at X University" is the name.

**Cameroon Army Corps of Engineers.** The works are corroborated outside the Bank — Journal du
Cameroun (12 July 2022) records that "le genie militaire a construit la route
Maroua-Mora-Dabanga-Kousseri" in the Far North, the Boko Haram-affected region the restructuring
was about, and distinguishes the genie from the Bataillon d'intervention rapide, which got the
Ekondo Titi-Kumba road. But nothing opened gives the corps' formal name, the instrument that
created it, or where it sits in the defence ministry, so there is no description, only a practice.
The VOA copy on globalsecurity.org failed with a client error.

**EIT (Brazil).** Blanked on identity, which matters more here than sources. The key is a bare
acronym: `EIT` appears nowhere in the project's own completion report or appraisal document (I
grepped the cached `P006449_ICR.txt` and `P006449_PAD.txt` — 13 hits for Gameleira, 19 for SOHIDRA,
0 for EIT), and comes only from the Agencia Publica report. Searching it returns a Natal-based
contractor, EIT Construcoes S.A. / "Empresa Industrial Tecnica", with a CNPJ and a judicial
recovery, but nothing ties that company to the Gameleira works, and the recovery dates do not
obviously match the card's "entered judicial recovery during construction" in 2011. The federal
comptroller's report on an "EIT" was the one document that could have settled it and its redirect
target was refused. **Do not fill this key without a document naming the company's legal form.**

**Federal Ministry of Environment, National Project Implementation Unit (Nigeria).** The one source
that describes the body contradicts its name (see the discrepancy file), and everything else it says
about the unit — technical support to state PMUs, reporting to the Bank — is already the card's
role text. There was nothing left to write that was not either the role or the name.

**Department of Local Infrastructure Development and Agricultural Roads (DOLIDAR), Nepal.** The
closest thing to a description is the department's own objective statement on its old site ("to
undertake infrastructure development programmes in accordance with decentralization policies") and
a 2018 Itad policy brief saying it was created in the 1990s and funded and guided district offices
on local road network management. Neither names its parent ministry, and the Itad brief is
consultancy grey literature. Current official pages publish under a different name and a different
ministry, with no instrument linking the two (recorded as a discrepancy). On the government-key
rule that is a blank, and it is the blank I am least comfortable with.

## My own two weakest entries

1. **Koridori Srbije d.o.o.** Every fact rests on one document, a conference status report the
   company wrote about itself, hosted on an EU programme site and dated 3 October 2013. It does not
   name the legal act that created the company, it does not name an owner, and its figures are
   thirteen years old. The entry says "its own 2013 status report" so the reader can see that, but
   a second, official source — the Serbian business register or the founding government decision —
   would replace most of it, and the unresolved merger question hangs over whether the company
   still exists in that form.
2. **Jiangxi Airport Group.** Built from a single state-media holiday-traffic story because the
   provincial SASAC and company pages did not come back in search. It gives no ownership, no
   corporate name (the article says only 江西机场集团), no airport count and no annual figure, so a
   holiday week stands where a size figure should. The identity link between the "Jiangxi Airport
   Group" of the 2019 completion report and today's 江西机场集团 is inferred from the province and
   the business, not documented.

Behind those, **SOHIDRA** is thin by design: one sentence of substance, "vinculada a SRH" and the
list of works it executes, from one document; and **EEPCo**, where the split is reported by one
outlet on a page that prints no date, and the regulation entry gives no regulation number.

## Discrepancies — `r26f_icij5_companies_disc.json`

Nine items across seven cases. The three that matter:

- **Albania's General Roads Directorate no longer carries that name** — the state audit office
  writes "Drejtoria e Pergjithshme e Rrugeve (sot Autoriteti Rrugor Shqiptar)". The card describes
  it in the present tense. Same shape as round 20's dissolved Argentine roads directorate.
- **EEPCo stopped existing as a single body in December 2013** — split into Ethiopian Electric
  Power and a separate distribution utility. The card calls it "the Ethiopian state electricity
  utility" in the present tense.
- **Serbia's Putevi Srbije was converted from a public enterprise into a limited company** by a
  government decision published in December 2025, which the name on the card ("Public Enterprise
  Roads of Serbia") now predates.

Then: **Nigeria's national unit is the ministry's own "Federal Project Management Unit"**, not the
"National Project Implementation Unit" the card names; **Nepal's DOLIDAR now publishes as the
Department of Local Infrastructure under the Ministry of Urban Development**, with no instrument
found for the change; **"all seven airports in Jiangxi"** is unconfirmed, the latest report naming
six; **the 2016 Ganga Order does not place NMCG under the Department of Water Resources** the card
names, which needs its own source; and one internal note — **the Ethiopia completion report calls
Energoinvest a subcontractor in its text but records a turn-key contract awarded to it in its
annex**. Each is phrased with its date and as what the source says, and nothing was changed.
