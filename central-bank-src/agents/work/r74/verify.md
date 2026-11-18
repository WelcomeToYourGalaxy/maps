# Round 74 independent verification

Scope: all 38 filed records. Note the brief's split is wrong: it is **17 revolving-door**
(corruption.json revolving_door, indices 374-390) and **21 events** (events_gold.json events,
indices 258-278), not 19/19.

**Filing integrity: clean.** All 38 records were filed field-for-field identical to
rd_a/rd_b/rd_c/ev_a/ev_b/ev_c .norm.json. No drift, no silent edits.

**Duplicates: none.** I checked every pair the brief named and every existing row for all 21
countries. CHN 258/259 are distinct instruments and both distinct from the Sept 2023 CCDI
record at 159. EGY 267 (statute) is distinct from 17 (2022 Amer resignation) and 54 (2015
pressure). HRV 262 (CON/2016/33, 15 June) is a different opinion on a different draft from 170
(CON/2016/52, 28 Oct). LBN 269 is distinct from 30. ZWE 263 from 60. SSD 268 (Dier Tong Ngor,
Jan 2022) from 106 (Johnny Ohisa Domian, June 2025). The nearest thing to a duplicate is COL
274 against 37 — same head of state, same complaint, different dates and different rate
decisions — and the record itself says a curator may prefer to treat them as one episode.

Method note: I pulled raw page text with curl wherever the host allowed (cbar.az, pbc.gov.cn,
hnb.hr, rbf.gov.fj, legislation.gov.au, parlament.gv.at, nao.go.tz, boi.org.il,
pagina12.com.ar, radiotamazuj.org, aljazeera.com, stjornarradid.is, asambleanacional.gob.ec,
lawphil.net, english.www.gov.cn, crhoy.com, vanguardia.com, kathmandupost.com,
forbesafricalusofona.com, bfa.ao, hsbc.com, bank.gov.ua, interfax.ru, ultimahora.com,
bes.media, blackrock.com, cgap.org, amwalalghad.com, caretas.pe, verangola.net, kyivpost.com,
unicreditbank.ru, sec filing PDF). Where a host blocks scripts (zimlii, hdfcbank,
graphiconline, rbnz, nirdhan, fin.parliament.go.ug, regalert) I say so and flag that the check
rests on the fetch tool's rendering.

---

## EVENTS — defects

### E1. CHN 2023 institutional reform (idx 259) — ATTRIBUTION. Serious.
**Claim:** "Source is the Chinese government's own English-language policy page
(english.www.gov.cn), which names the two transferred functions in those words"; weak_source
false.
**Source actually says:** the page is bylined **"China Daily"** and signed off **"He Qing is a
professor at the Renmin University of China's School of Finance and a key member of the China
Macroeconomy Forum. Hu Tong is an assistant researcher at the Renmin University of China's
School of Finance."** It is an outside academic commentary republished on gov.cn's policy-watch
section, not a government statement of the plan.
Two further problems on the same page:
- The record's source_title is "Reform plan to see new financial regulatory body". The page's
  own headline is **"Central bank reforms to strengthen monetary policy efficacy"**.
- The record files it as "a state decision removing functions and money-handling structures
  from the bank". The page says the opposite about its meaning: **"The more focused policymaking
  function of the PBOC will help modernize the central bank system and should not be simply
  taken as a lessening of the PBOC's role."** The record does not note that its own source
  disputes its reading.
The two transferred functions and the abolition of county-level sub-branches ARE on the page in
those words, and the "in March" / page-dated-17-April-2023 provenance is correct.
**Fix:** weak_source true; state in the detail that the text is a China Daily commentary by two
named Renmin University academics, not a government statement; correct the source_title; record
the page's own contrary reading. Better: replace with the State Council's plan text itself.

### E2. LBN judicial raid (idx 269) — ACCRETION.
**Claim:** "**Mount Lebanon** prosecuting judge Ghada Aoun".
**Source actually says:** only "a prosecuting judge" and "Judge Ghada Aoun". "Mount Lebanon"
appears nowhere on the Al Jazeera page. This is the invented-characterisation pattern the brief
warns about.
**Fix:** drop "Mount Lebanon" or source it.
Everything else in this record is exact: raid authorised "on Tuesday", strike begun
"Wednesday", three-day strike, charge of "falsifying the budget of Lebanon's central bank to
hide losses", permission "first given ... before another judicial authority revoked it", "She
entered the central bank's building but did not enter Salameh's office", published 20 Jul 2022,
month-only dating correctly justified.

### E3. HRV CON/2016/33 (idx 262) — OVERSTATEMENT.
**Claim:** the ECB "found that draft amendments letting the State Audit Office audit the
central bank's operations, **and** letting the Croatian Parliament discuss and vote on its
annual report, **were not in line with** the principle of central bank independence".
**Source actually says:** the "not in line" finding is made only of the audit limb (§2.1.2:
"These provisions of the current Law on the State Audit Office in conjunction with the relevant
provisions of the draft law are not in line with..."). On the parliamentary vote the ECB says
only that it **"could affect the institutional independence of HNB"** (§2.2.3), and separately
that a right "to approve, suspend, annul or defer HNB's decisions **would be** contrary to" it.
The record's own detail field renders this correctly; the summary conflates the two limbs.
**Fix:** confine "not in line" to the audit limb; render the parliament limb as "could affect".
The quote, the 24 May 2016 request, the two-term cap and the completion-of-current-terms point
are all exact.

### E4. AUT works council objection (idx 273) — WRONG KIND / incomplete.
**Claim:** kind "attempted law change"; detail "The source is a submission on a draft, not a
statute, so no in-force check applies to it."
**Fact:** the draft **was enacted** as the Sonderpensionenbegrenzungsgesetz, BGBl. I Nr.
46/2014, and the new OeNB pension-contribution regime **has applied since 1 January 2015**. The
Constitutional Court upheld it (G 478/2015, 12 Oct 2016) and the 2013 contribution (G 405/2015,
14 Mar 2017). "Attempted" is wrong and the "no in-force check applies" line dodges the one
check that mattered.
**Fix:** re-kind as a law change the bank's works council objected to; say the bill became law.
**Attribution is handled correctly** — the record states plainly that the objection is the
Zentralbetriebsrat's, acting for staff and pensioners, and not a resolution of the bank's
governing organs, and that the subject is staff pensions. Both quotes are verbatim, as are
§ 21(1) NBG and the Art 130 / Art 123 TFEU points, the 6 May 2014 date and the file number.

### E5. ZWE Amendment Act 1 of 2010 (idx 263) — MISREAD PROVISION + currency statement.
**(a) Claim:** "required the Board to send its minutes to the Minister **within seven days of
each meeting**."
**Source actually says** (s.28(5), quoted): minutes must be submitted to the Minister "as soon
as practicable and in any case no later than seven days **after each following meeting**." That
is seven days after the *next* meeting, not of each meeting.
**(b) Claim:** "in the consolidation stated as current to 31 December 2021."
**Source carries two inconsistent statements:** "[This is the version of this document from 31
December 2021.]" and a consolidation note "This version is up-to-date as at **31st December
2016**." The record reports only the first.
**(c)** The record attributes s.28(4) to Act 1 of 2010 without noting the history note also
records an amendment by **Act 1 of 2014**.
The Act 1 of 2010 attributions at 6(1)(h), 6(1)(k), 49(5), 28(5), 21(2) and 29A are confirmed,
as is the Ministry of Finance employee on both the Board and the new Audit and Oversight
Committee.
**Fix:** correct the minutes wording; state the conflicting currency statements; add the 2014
amendment. Also unused and more on point: s.29A requires the committee to **report its
deliberations to the Minister**.
*Caveat:* zimlii 403s scripted requests here, so this rests on the fetch tool; the seven-day
wording is a direct quotation from it.

### E6. CRI legislative committee report (idx 272) — DATE PROVENANCE + ATTRIBUTION.
**(a) Claim:** the date "is the article's publication date of 18 April 2024, **which reports the
approval as having happened that day**; no separate approval date is printed."
**Source:** published 18 Apr 2024 14:50 by Alexánder Ramírez — confirmed. But the article
nowhere places the vote on that day: no "hoy", no weekday, no date in the body. The second
clause is an unsupported inference dressed as provenance.
**(b) Claim:** "the **report's** phrase being 'la urgente destitución del jerarca del Banco
Central de Costa Rica'."
**Source:** that is CRHoy's own sentence describing what the report recommends, not quoted
report text. (The two phrases the record does attribute to the report — "falta de cumplimiento
de normativas legales y éticas en la obtención de información" and "evidentemente precipitadas
y temerarias" — are correctly quoted from it.)
**Fix:** say the approval date is not printed, full stop; drop "the report's phrase" for the
first quotation.
The 6-3 split and all nine named deputies, the data-protection ground, SUGEF plus four
commercial banks, and the Valverde/Aguilar criticism are all verified.

### E7. ISL ministerial examination (idx 275) — VERB STRENGTH + date provenance.
**Claim:** "the Prime Minister **required** the Supervisory Board ... to produce a written
report"; "by letter dated 15 March the Prime Minister **demanded** further information".
**Source says** in both places "**óskaði ... eftir**" — requested, asked for. Nothing on the
page is a requirement or a demand, and the record's kind ("ministerial examination of the
bank") makes the force of the verb load-bearing.
**Also:** the record flags that the year for "12. nóvember sl." is derived, but not that its own
**date field** (2019-03-15) is derived the same way — the page prints "15. mars **sl.**" with no
year.
**Fix:** "requested"; say the date field's year is also derived from the page's 26 Apr 2019 date.
The quote, the three enumerated points, the 8 Nov 2018 judgment in case 463/2017, 21 February,
12 April, the Ombudsman's 22 Jan 2019 opinion and 4 Mar 2019 letter, the 27 Mar 2012 search and
the closing sentence are all exact.

### E8. URY Página/12 (idx 266) — HEDGED REPORT ASSERTED FLATLY + source_title.
**Claim:** "President Jorge Batlle **had proposed** Carlos Steneri as the next central bank
president."
**Source says:** "El presidente ya **habría** propuesto el viernes ... a Carlos Sténeri" — the
Spanish conditional of rumour. The paper does not vouch for it.
**Also:** source_title calls the piece a "report on the replacement of the Banco Central del
Uruguay's directors". Its actual headline is "El contagio argentino llevó la fiebre de la
renuncia a Uruguay" and its subject is economy minister Alberto Bensión's resignation; the
central bank decision is one paragraph.
**Fix:** "reportedly proposed"; give the article's own headline.
The load-bearing facts are verified verbatim: the Friday "cumbre" of Blanco and Colorado
leaders, "se decidió la sustitución de los tres directores del Banco Central", the criticism of
Rodríguez Batlle for the timing of the Banco Montevideo / Caja Obrera interventions, Medero's
prior resignation, and the correctly-reasoned month-only date.

### E9. AUS Reserve Bank Act s.11 (idx 260) — SUPERSEDED COMPILATION CITED.
**Claim:** read in "compilation No. 32 (1 March 2025)"; "that page reported compilation
C2026C00375".
**Fact:** C2026C00375 is **Compilation No. 33, compilation date 27 August 2026** — the current
one. The record names the current registration number while citing and reading the superseded
text. That is the defect class 7 miss.
I pulled No. 33: **s.11 is word-for-word identical** to No. 32 (subsections (2)-(7); no (1)), so
the substance and every subsection reference in the record stand.
**Fix:** cite Compilation No. 33, 27 August 2026.

### E10. ECU Código Monetario (idx 276) — KIND NOT SUPPORTED BY THE SOURCE.
**Claim:** kind "statutory arrangement **removing** the bank's control of monetary policy".
**Source:** the Assembly notice describes the *creation* of the Junta de Política y Regulación
Monetaria y Financiera and the BCE general manager's voice-without-vote. It nowhere says the
central bank previously held that control, or that anything was taken from it. (On the map's own
existing ECU row, index 138, the BCE's independence had already gone in 2008.)
**Fix:** re-kind to what the page supports — a law placing monetary and financial regulation in
an executive-branch body on which the central bank has no vote.
Every factual element is verified exactly: sesión 289, "Martes, 02 de septiembre del 2014",
partial objection resolved, text to the Registro Oficial, 53 of 56 observations by 94-27-2,
articles 18, 261 (except numeral 13) and 458 ratified by 95, the Junta's public-law character
and voting membership, and the BCE general manager "con voz pero sin voto".

### E11. PHL RA 11954 (idx 261) — UNSOURCED ASSERTION.
**Claim:** "the then governor publicly said the BSP could absorb the loss, so the record
asserts no objection by the bank."
**Source:** nothing of the kind is in lawphil's text of RA 11954, and no source is cited for it.
It is a bare factual assertion inside a detail field.
**Fix:** cite a source or drop it and say only that the statute records no objection.
Every statutory claim checks out verbatim: ss. 6(1)(a) and 51(a) (100% of BSP declared
dividends for the first and second fiscal years, up to the P50,000,000,000.00 initial
subscription), the Monetary Board recommendation power, s.57(a) expressly amending s.2 of RA
7653 as amended by RA 11211, s.58 effectivity on publication, "Approved: 18 JUL 2023", and the
quote field.

### E12. EGY Law 194 of 2020 (idx 267) — minor, plus no in-force check at all.
- **Claim:** Governor appointed "for a **renewable** four-year term". Article 17 says "for a term
  of four years, **renewable once**". The cap is dropped.
- The kind says the statute lets "the head of state appoint **and remove** the bank's governor".
  Article 24 conditions dismissal on the **Board's recommendation** and an opportunity to
  present a defence. The summary states this correctly; the kind does not.
- **No currency check was made** on a 2020 statute read only in a law-firm translation, with the
  Arabic original admittedly unopened. I could not find a live readable Arabic original either
  (the ebi.gov.eg PDF that search surfaces is a training-course brochure, not the law).
- Unused and more on point than what the record cites: **Article 48** of the same translation
  establishes, by presidential decree, a coordination council "to align the Bank's monetary
  policy with the Government's fiscal policy".
Articles 2, 17, 18 and 24 are otherwise verified verbatim, including all four dismissal grounds.

### E13. FJI Reserve Bank Act s.52 (idx 264) — in-force gap partly closed by me; one wrong statement.
The record says post-1985 amending Acts "were not opened". **I closed most of it:** the RBF's own
`Amendments.pdf`, sitting in the same `wp-content/uploads/2020/03/` directory as the Act the
record cites, lists every amendment the Bank publishes — ss. 2, 25, 30, 38, 40, 43, 57 — and
**section 52 is not among them**; and the Reserve Bank of Fiji (Budget Amendment) Acts 19 of
2025 and 22 of 2026 touch ss. 2, 7, 8, 22 and 55 only. **s.51(5) I could not clear** (PacLII
403s here), so the 40-per-cent figure remains unchecked against post-1985 Acts.
**Wrong statement:** the record says the date field carries "1983, the year of the principal Act
**as the Act is cited**". The 1985 edition's short title is bare — "This Act may be cited as the
Reserve Bank of Fiji Act". The 1983 comes from "**Act No. 14 of 1983**" printed in the document.
(Current Fijian practice does cite it as the "Reserve Bank of Fiji Act 1983", as the 2025 and
2026 amendment Acts do.)
s.52 and s.51(5) are quoted correctly word for word, including the quote field.

### E14. STP Barros dismissal (idx 278) — WEAK SOURCE NOT FLAGGED.
The record's own detail says both legs are press, neither article names a decree number, and no
primary instrument was located. The earlier article's facts are attributed to an unnamed
"**fonte oficial**" relayed **to Lusa** and republished by Forbes África Lusófona — third-hand,
which the record does not say. **weak_source is nonetheless false**, while GHA, KAZ, PER and the
EGY revolving-door record are flagged true on the same or better footing.
**Fix:** weak_source true; name the chain.
Content verified: both articles (1 Apr and 26 Mar 2022), Bom Jesus's quotes including "Não
tivemos outra alternativa senão preparar o decreto que [o] exonera", the MLSTP-PSD congress,
the lei orgânica ground, the restructuring ground in the earlier piece, Friday 25 March, the
Council of Ministers session, Eugénio Soares. The record handles the two different stated
grounds honestly.

## EVENTS — clean

- **CHN PBOC Law art. 5 (idx 258)** — clean. Verified verbatim against the PBOC's own PDF:
  adoption 18 March 1995, 2003 revision by the Tenth NPC Standing Committee's 6th Meeting of 27
  December 2003, Article 5 exact, Article 2 "under the leadership of the State Council", Article
  53 effective on promulgation, no repeal. *Two notes, not defects:* Article 7 of the same law
  (unmentioned) says the PBOC "shall, under the leadership of the State Council, independently
  implement monetary policy ... free from interference by local governments" — it reinforces the
  record rather than contradicting it. And the PBOC's own compliance subsite still publishes this
  2003 text in 2025, a better in-force citation than the 2015 PDF path.
- **ISR Yaron letter (idx 265)** — clean, verified line by line: 27 June 2023, to PM Netanyahu,
  Ministerial Committee on Legislation chaired by the Minister of Justice approved it 25 June
  2023, the bill's terms including the Advisory Committee and the Finance Minister's approval,
  "vehement opposition", the exact quote, "grants the Minister of Finance the authority to
  actively influence the interest rate in the economy", "crosses a significant red line",
  preliminary reading Wednesday 28 June 2023, request to remove it from the agenda immediately,
  copy to Smotrich. Best event record of the round.
- **TZA Controller and Auditor General (idx 270)** — clean, and the figure labels are right,
  which was the brief's specific worry. Verified: title "Annual General Report of the Controller
  and Auditor General On the Financial Statements of Public Authorities and Other Bodies for the
  financial year 2007/2008", submitted to "Your Excellency, Dr.Jakaya Mrisho Kikwete" under
  "Article 143 of the Constitution", signed Ludovick S. L. Utouh, "26th March, 2009"; §4.1.4
  heading "Irregular payments in respect of Insurance Premiums for BOT HQ Building Shs. 7.3
  Billion"; the missing-documents finding; "appear excessive"; the investigation direction
  quoted exactly; and the two USD labels exactly as printed — "From the total Insurance Premiums
  of US$ 6,302,823.42 paid by the Bank to its Insurance Broker between 20 February 2003 to 24
  July 2007 the Bank has in its possession Insurance Policies to support only US$ 2,478,388
  worth of premiums paid." The summary-of-recommendations quote and the EPA consultant note
  check out too. The USD detail sits in §8.6, not §4.1.4 — the source_title does say so.
- **NPL Finance Committee (idx 271)** — clean, and the attribution the brief flagged is handled
  correctly: the record says in terms that the officials' concerns are the newspaper's
  characterisation, not a statement by the bank. Five-to-three tenure cut with a two-year Cabinet
  extension, s.106(c) of the 2002 Act added by a 2016 amendment, the bank's proposal to remove
  it, Budhathoki's quote verbatim, the four named former governors/ministers, and the
  publication-date provenance all verified. *Omission, not a defect:* the article also reports
  that the central bank itself drafted the removal of the directive power as an **IMF Extended
  Credit Facility** condition and that the Finance Committee added items afterwards — the
  mechanism of the episode.
- **COL Petro (idx 274)** — clean. Quote exact, loss of independence, "llenar los bolsillos de
  los tenedores de títulos de la deuda pública nacional", and the 1991 Constitution
  coordination point correctly attributed as Petro's own interpretation ("según su
  interpretación"). Published 4 Apr 2026.
- **SSD Kiir decree (idx 268)** — clean. Decree read on the state broadcaster, "article 182/7 of
  the Transitional Constitution ... read together with section 38/1 of the Interpretation of
  laws", "with effect from 3 January 2022", "without giving reasons", published 4 Jan 2022.
- **UGA Protection of Sovereignty Bill (idx 277)** — core confirmed and the attribution is right
  (the record says the assertions are the bank's as reported by Parliament, not Parliament's
  findings): Tuesday 28 April 2026, the joint Legal and Parliamentary Affairs / Defence and
  Internal Affairs committees, Atingi-Ego with Nuwagaba and Twinemanzi Tumubweine, article 162,
  clause 13, US$1.5 billion remittances. **Caveat:** fin.parliament.go.ug fails TLS from here
  (not merely a script block), so both the record and my check rest on the fetch tool's
  rendering. The phrase "if recipients of larger sums had to register" and the list "monetary
  policy, exchange controls, banking supervision and financial stability" are **not
  independently confirmed**.

---

## REVOLVING DOOR — defects

### R1. UKR Rozhkova (idx 378) — PRIMARY SOURCE NO LONGER SERVES THE CONTENT. Serious.
**Claim:** the NBU's own biography page at `bank.gov.ua/en/about/structure/details?member=10`,
which the record says "was opened on 17 November 2026 and confirmed to serve Rozhkova's own
page" and which "describes the First Deputy Governor post as one she still holds".
**Today that URL serves** a page titled "Член ради" (Council member) under the NBU **Council**
section, carrying her name and nothing else — no biography, no bank employers, no dates.
`?member=11` now serves **Sergiy Nikolaychuk, "First Deputy Governor of the NBU"**, appointed by
the NBU Council on 15 August 2025. So every NBU date in the record (10 June 2015, 18 Jan 2016,
25 Oct 2016, 15 June 2018) and all three bank employers (ErsteBank PJSC, Finbank PJSC, Platinum
Bank PJSC) are now unverifiable at the cited URL — and the record itself records that it already
knew of her replacement. A numbered-slot URL was never a safe citation for a departed officer.
**Fix:** a stable source for the NBU leg — an archive copy, or the NBU's own appointment releases.
The private leg does hold: I verified the Kyiv Post piece carries "from a private-sector
manager", "she led Platinum Bank, the 22nd largest bank by assets in Ukraine in October 2016",
"led the bank up to mid-2015", Kaufman's indirect ownership and the 2017 collapse.

### R2. UKR Rozhkova — MATERIAL OMISSION from the very paragraph cited.
The Kyiv Post sentences the record relies on also say: "**in 2024, Ukraine's Supreme Court ruled
that Rozhkova and 11 others bore joint civil liability for the insolvency of Platinum Bank in
2017** – the Supreme Court ordered them to pay Hr. 1.5 billion ($35.2 million) in damages." On a
central-bank-capture map this is the most material fact on the page about this person and this
bank, and the record omits it. **Fix:** include it.

### R3. AZE Nağdəliyev (idx 388) — CAREER MISSTATED; weak row not disclosed.
**Claim:** move "from ... Kapital Bank (2007-2008) **to the Central Bank of Azerbaijan's
Monetary Policy Department in 2008, rising to** head of the Monetary and Exchange Rate Policy
division, **and Adviser to the Chairman from 3 November 2025**"; years "Central Bank of
Azerbaijan **from 2008**".
**Raw CBAR page** (curl, reads cleanly) continues past where the record stops: adviser to the
**World Bank** executive director 2018-2020; head of the Chairman's office at the Central Bank
2021-2022; adviser to the chairman August-September 2022; **adviser to the World Bank executive
director again 2022-2025**; then the 3 November 2025 appointment. He was not at the Central Bank
continuously "from 2008", and the 2025 senior post is 17 years and two World Bank stints removed
from the Kapital Bank job.
**On the row:** the private-to-public step the page actually supports is *leading specialist,
Documentary Operations Department, Kapital Bank* → *junior economist, Monetary Policy
Department*. That is not a senior official taking office.
**Not a defect:** the record is honest that the page states nothing about Atlantbank's or Kapital
Bank's ownership. The brief's worry about an invented "private commercial bank" characterisation
**does not apply** — the record makes no such claim. (It does apply to GHA; see R4.)
**Fix:** give the full sequence; say plainly the private employment ended in 2008 at junior grade.

### R4. GHA Asante-Asiedu (idx 375) — ACCRETION, and the row rests on it.
**Claim:** "The private side is Access Bank (Ghana) PLC, **a commercial bank** operating in
Ghana ... so no ownership claim is made here and **the record rests only on the employer being a
named commercial bank**."
**Source:** the Graphic Online article does not call it a commercial bank and says nothing of its
ownership, shareholders or listing. "Commercial bank" is the record's own word — and the record
then explicitly rests the row on it. This is the exact pattern the brief identified.
**Fix:** drop "a commercial bank" or source it. Also: the article gives **July 2017** for her
appointment as Group Head of Retail Banking, which the years field omits.

### R5. SGP Teo Swee Lian (idx 374) — UNSOURCED PRIVATE LEG, and self-contradictory.
**Claim:** "The private side is HSBC Holdings plc, **the publicly traded holding company** of
the HSBC banking group and **a bank holding company in its own right rather than a subsidiary of
any group**; the biography page itself does not state its ownership or listing, **and that is
said here rather than asserted**."
It **is** asserted, in the clause immediately before, with no source at all. Meanwhile CAN and
NZL in the same round each carry a documentary second source for exactly this leg, and both hold
up under checking (see R10).
**Fix:** cite HSBC Holdings plc's own annual report or listing document.
Career facts verified verbatim on HSBC's page. *Minor:* the page also lists **Singapore
Telecommunications Limited and the Dubai Financial Services Authority** among her prior
directorships; the record's list silently drops them.

### R6. IND Gopinath (idx 377) — MISQUOTED BASIS FOR THE PRIVATE LEG; second source has no URL.
**Claim:** "the bank's own page says only that it **ranks among the top 10 Indian banks by market
capitalisation**, which indicates a company listed in its own right rather than a subsidiary.
That is the whole evidence of its character here."
**Page says:** the Bank's rankings among all Indian banks with regard to **market capitalization,
profit after tax and balance sheet size** "remain amongst the top 10". That is not a statement
that it ranks top 10 by market capitalisation, and the listing inference is the record's own.
The page also **never** calls HDFC Bank a private sector bank. So the private leg of an Indian
row rests on an inference from a ranking sentence, for an employer whose listing is one lookup
away.
**Also:** the date and the three-year term rest on a second source (Business Standard, 2 January
2015) for which **no URL is given**, unlike CAN and NZL.
**Fix:** source the private leg from HDFC Bank's own annual report or exchange filing; add the
second source's URL.
RBI wording verified: "over 39 years of experience in financial sector policy formulation in
different capacities at RBI" and "As Deputy Governor of RBI for seven years and member of the
Board". *Minor:* her HDFC role appears on the page only via a linked appointment letter for the
"Part Time Non Executive Chairperson" post, thinner than "lists her at the bank as part-time
non-executive Chairperson" implies.
*(hdfcbank.com blocks scripts; this rests on the fetch tool, with the quoted strings returned as
direct quotations.)*

### R7. AGO Monteiro (idx 383) — OMISSION THAT MAKES THE MOVE LOOK DIRECT.
**Claim:** move "from Vice-Governor and Executive Administrator of the Banco Nacional de Angola
**(1990-2012) to** Independent Non-Executive Director of Banco de Fomento Angola (2023-2025)".
**The same CV lists, in between:** "**Secretária de Estado da Economia do Ministério da Economia
(MINEC), 2012-2017**" and "**Administradora Executiva do Fundo Soberano de Angola (FSDEA),
2018-2023**" — eleven years of state posts, including an executive directorship of Angola's
sovereign wealth fund, immediately before the BFA seat. The sibling Gaspar Martins record does
disclose its intervening posts (Finance Minister, UN representative); this one does not.
**Fix:** state the intervening posts.
Everything else verified verbatim: the six BNA roles and 1990-2012, INED 2023-2025,
Vice-President 2025, 2,409 shares, proposed President of the Remuneration Committee.

### R8. AGO Montenegro Duarte (idx 385) — FIGURE FROM A SELF-CONTRADICTORY DOCUMENT; weakest row.
**Claim:** "she holds **522 thousand** ordinary BFA shares representing less than one per cent of
the share capital."
**CV reads:** "Titular de **522** (**Quinhentas e vinte e duas mil**) acções ordinárias" — digits
say 522, words say 522,000. The record silently takes the words and presents it as settled.
**On the row:** her central bank post is "**Quadro Sénior**" in four directorates, undated, and on
the CV's own ordering the earliest thing in her career; the BFA seat is 2023, with the
state-owned Banco de Poupança e Crédito (1991-2006) in between. The record does not say the
central bank posts appear to predate 1991 or that some thirty years separate the two legs. It
does correctly flag BPC as state-owned and Mundial Seguros' ownership as unstated.
**Fix:** report the digits/words conflict; state the gap and the grade.

### R9. AGO x3 — SECOND SOURCE CITED WITHOUT A URL, and its actual news omitted.
All three records rest the ownership leg on "Ver Angola, 'BPI chega a acordo com Grupo Carrinho
para venda de participação no BFA'" with **no URL and no date** — unlike CAN and NZL, which
carry second_source_url.
I found it (verangola.net, **4 September 2026**). The figures the records quote are accurate:
"BFA's main shareholders **were** Unitel (**controlled by the State**, with a 36.90 percent
stake) and BPI (with 33.35 percent of the capital)", and BPI "sold 14.75 percent of BFA on the
stock exchange for €103 million" in September of the previous year. **But** the records use only
that background paragraph and never mention the article's actual news: **BPI has agreed to sell
its whole 33.35 per cent to Congolian Financial SA, part of the Carrinho group**, subject to
Unitel's right of first refusal.
Two further points on the brief's question:
- The mixed ownership is accurately represented as far as it goes, but **none of the three says
  the state-controlled holder is the largest single shareholder** — which a reader needs to weigh
  the row. (36.90 + 33.35 + 14.75 = 85%; ~15% is unaccounted for in all three records.)
- **Better evidence sits in the record's own primary source and is unused:** the BFA CVs
  repeatedly call the employer "**Banco de Fomento Angola, S.A., Sociedade Aberta**" — the
  employer's own description of itself as a publicly held company.
**Fix:** add the URL and date; add the sale; use the "Sociedade Aberta" wording; say Unitel is
the largest holder.

### R10. PER Palomino (idx 386) — WRONG LEG CHOSEN; 14-year gap undisclosed; false claim about the host.
The Caretas page reads fine to curl with `--compressed` — the record's claim that "its text
renders only through a browser: a direct curl of the same URL returns the page shell without the
biography" is **wrong**; it is a content-encoding matter, not JS. Having read it in full:
- **The article's subject is his appointment as a NEW BCRP director on 7 August 2026** by
  Resolución Suprema N.º 250-2026-PCM, alongside Choy and Yamada. The record does not mention
  this at all.
- **Between Merrill Lynch (to 2002) and the 2016 directorship** he was at the Instituto Peruano
  de Economía — director, consultant and "principal funcionario ejecutivo" **desde 2007**, and
  its president since 2022. A fourteen-year gap the record does not acknowledge.
- The 2000-2002 employer is named "**Merrill Lynch, Pierce, Fenner & Smith en Nueva York**".
- Most to the point: "**Actualmente integra, entre otros, los directorios de Laboratorios
  Portugal y Southern Copper Corporation**", and he chaired the audit committee of the **Bolsa de
  Valores de Lima** and sat on the boards of Aventura Plaza and Mall Aventura. He is taking a
  central bank directorship **while holding private company board seats** — a live, dated,
  on-the-page revolving-door fact the record passes over for a post he left twenty-four years ago.
**Fix:** rebuild on the 2026 appointment and the concurrent private directorships; disclose the
IPE years; correct the host claim. The Merrill Lynch quotes themselves are accurate.

### R11. EGY Amer (idx 390) — A STATE-LINKED BANK INSIDE THE PRIVATE LEG; the key fact unused.
The move field reads "from leading the corporate finance and investment banking business of
Citibank and Bank of America ... **and the deputy chairmanship of the Arab International Bank**,
to Deputy Governor of the Central Bank of Egypt". The **Arab International Bank** is a
treaty-based bank whose shareholders include the Egyptian state and other governments; it does
not belong in a private leg, and the summary separately says "the private side is Citibank and
Bank of America".
**Also unused — the most on-topic fact on the page:** it has him **simultaneously** Deputy
Governor of the CBE "since December 2007", Chairman of the state-owned **National Bank of Egypt**
"since 2008", Chairman of the Federation of Egyptian Banks, **a member of the CBE's board**, and
a director of National Bank of Egypt (UK) Limited. The concurrency of a state-bank chairmanship
with a central bank board seat is the capture point; the record does not note it.
**Fix:** remove the Arab International Bank from the private leg; record the concurrent offices.

### R12. SYSTEMATIC — the private-financial leg and weak_source are handled inconsistently across the batch.
**Four records settle the leg with a document, and all four hold up under my checking:**
- CAN: BlackRock's FY2025 10-K — verified: "Commission File No. 001-42297", "Common Stock, $.01
  par value", "BLK", "New York Stock Exchange".
- NZL: Harbour's Disclose filing — verified: "The ultimate parent, Jarden Group Limited, is 100%
  privately owned by directors, management and employees of that business" and "There are 125
  shareholders in Jarden Group Limited".
- RUS: UniCredit's own issuer report — verified: "100% голосующих акций АО ЮниКредит Банк
  принадлежит Группе UniCredit (UniCredit S.p.A.)", and the July 2008 Supervisory Board
  appointment in section 10.
- KAZ: finance.kz — verified: "Крупнейший акционер ForteBank Булат Утемуратов значительно
  увеличил свою долю ... до 90,92%, согласно данным из выписки состава акционеров на 1 июля
  2025 года", and he is called a "бизнесмен", not a "private person", exactly as the record says.
**Seven leave it "unsettled":** RWA (ING, BNP Paribas, Fortis, BNY Mellon), AZE, NPL, EGY
(Citibank, Bank of America), SGP (HSBC Holdings), IND (HDFC Bank), GHA (Access Bank Ghana) —
several of them listed companies for which a filing is the same single lookup that was done for
BlackRock.
**And weak_source is set arbitrarily on the same footing:** RWA (a CGAP speaker-bio page with no
dates for any of four bank posts and no ownership) is **false**; EGY (2012 trade press) and GHA
are **true**. PRY (private character resting only on a newspaper's phrase "el sector privado")
is **false**; KAZ, which has a named 90.92-per-cent shareholder from a second source, is
**true**. STP (press only, anonymous official source via Lusa) is **false**.
**Fix:** apply the CAN/NZL standard to the remaining rows and set weak_source by one rule.

### R13. RUS Alekseev (idx 379) — small misstatement about the source.
**Claim:** "The Interfax text read here carries the day and month '12 October' **but no year**,
and no year is asserted here from it."
**The page carries its date in machine-readable form:** schema.org `"datePublished":
"2020-10-05T13:59:00+03:00"` and `<time datetime="2020-10-05T13:59">`, with the dateline
"Москва. **5 октября**. INTERFAX.RU". So "12 October" is 12 October 2020 on the page's own
evidence; the record instead derives 2020 from a different document.
**Fix:** use the page's own date.
*Also unused:* the page quotes Alekseev on "**почти трех десятков лет, проведенных в
коммерческом банковском бизнесе**" — the source's own evidence for the commercial character of
his career.

## REVOLVING DOOR — clean (and notes)

- **CAN Boivin (idx 382)** — clean end to end. Quote verbatim on BlackRock's page; 10-K second
  source verified as above; the record is correctly silent on dates the page does not give.
- **NZL Hawkesby (idx 376)** — clean end to end, and the best-sourced record of the round. The
  RBNZ release confirms the title, the 18 March 2019 start, "in the competitive asset management
  industry as a senior member of the Wellington-based Harbour Asset Management team", the
  graduate role and "Head of Market Intelligence for the Bank of England", and confirms it says
  **nothing** about Harbour's ownership, his title there or his length of service — exactly as
  the record states. The Disclose filing's ownership passage is verbatim correct and the record's
  date-gap disclosure (1 July 2020 filing vs a March 2019 move, FirstCape only in 2024) is
  honest and right. *Minor:* the Investment News NZ article relied on for "head of fixed income"
  and "eight years" has no URL.
- **KAZ Zhandosov (idx 381)** — clean, both legs verified against raw pages, weak_source
  correctly true, and the record is accurate that the page gives no dates for the National Bank
  chairmanship.
- **PRY Carvallo (idx 380)** — content clean and verified verbatim ("como miembro titular del
  Directorio y gobernador alterno ante el Fondo Monetario internacional (FMI), de 2015 a 2020",
  "la entidad financiera Ueno", "el sector privado", March 2022, no start date for the return).
  Only issue is the weak_source inconsistency at R12.
- **NPL Rana (idx 389)** — source checks out exactly (founder Governor 26 April 1956 - 8
  February 1961, Nirdhan Bank Limited chairman 10 January 1999 - 17 September 2002, Himalayan
  Bank four years undated, nothing about ownership of either). Two things it should say and does
  not: the two offices are **thirty-eight years** apart, and Nirdhan is a **microfinance**
  institution (the host, Nirdhan Utthan Laghubitta, is a microfinance company), not a commercial
  bank. The page names no publisher; "published by Nirdhan Utthan Laghubitta" is inferred from
  the host.
- **RWA Hakuziyaremye (idx 387)** — content verified verbatim on the CGAP page, including the
  four named bank employers and the correct sequence through the trade and industry ministry.
  Carried in R12 for the unsettled private leg and the weak_source flag.
- **AGO Gaspar Martins (idx 384)** — clean. Verified verbatim: born 12 January 1940, proposed
  Presidente da Mesa da Assembleia Geral, Governador do BNA 1976-1977, Ministro das Finanças
  1977-1982, Representante Permanente 2001-2018, holds no ordinary shares, Fundo Soberano
  non-executive director since 2018, and the sovereign-fund seat correctly flagged as a state
  body recorded only as context. Carried in R9 for the shared second-source URL gap.

---

## HELD records — live readable sources found for two of the three

**MUS (Bank of Mauritius Act) — a readable source exists.**
`https://regalert.today/document/bank-of-mauritius-act-2004-4f4006de-0401-4689-9a8e-7614c62c5038/text`
carries the Act's text, headed "BANK OF MAURITIUS ACT 2004" / "Act 34/2004", "Proclaimed by
[Proclamation No. 40 of 2004] w.e.f. 10th November 2004" (s.72(2) from 10 January 2005). Section
5(2)(a): "determine, **with the concurrence of the Minister**, the accepted range of the rate of
inflation." Section 36(1) carries the same "with the concurrence of the Minister" wording for
notes, coins and digital currency. Its amendment notes run to **Act No. 3 of 2026**, which also
supplies the in-force check the held record lacked. It is a commercial consolidator that
disclaims authority against the Government Gazette, so it would file as a weak source — but it
is readable, which is what the hold turned on. *Caveat:* regalert 429s scripted requests here, so
I read it through the fetch tool; the two quoted phrases are direct quotations. bom.mu remains
unreachable (TLS failure).

**ZWE (Mushayavanhu / FBC) — a readable source carries both legs.**
`https://nehandaradio.com/2023/12/25/fbc-appoints-trynos-kufazvinei-as-new-group-ceo-to-replace-mushayavanhu`
(Nehanda Radio, 25 December 2023, republishing NewsDay): "He will replace John Mushayavanhu who
is leaving the **Zimbabwe Stock Exchange-listed** financial institution at the end of the month
after being appointed central bank governor", and "**Mushayavanhu takes over the reins at banks'
regulator on May 1**" — which also supplies the governorship start date the held record said was
absent. It does **not** carry his FBC career history (1997, 2004, June 2011), so a record filed
on it would be narrower and press-based (weak source). I re-confirmed that fbc.co.zw's notice,
the ZSE copy and FBC's 2023 annual report PDF all 404, and heraldonline.co.zw 403s.

**LBN (Andary) — no substitute found; the hold stands.** bdl.gov.lb returns 403 to every scripted
request from here, so the Banque du Liban vice-governor page the held reason proposes could not
be tested.

---

## Summary

Defects found: **14 in events, 13 in revolving door** (one of them, R12, systematic across seven
records). The most serious are **E1** (a China Daily commentary by two named academics filed as
the Chinese government's own policy page, weak_source false, wrong title, and the source's own
contrary reading suppressed), **R1** (the UKR record's primary source is a numbered-slot URL that
no longer serves any of the content claimed, for an officer the record knew had been replaced),
**R10** (the PER record chooses a 24-year-old post over the concurrent private directorships
printed on the same page, hides a 14-year gap, and misstates why the page could not be read),
**E4** (an enacted statute filed as an "attempted law change" with the in-force check waved
away), and **E5** (a provision misread — seven days after the *following* meeting, not of each
meeting — plus a suppressed conflict in the consolidation's own currency statement).

Cleanest records: **ISR**, **TZA**, **CHN art. 5**, **SSD**, **COL**, **NPL event** among events;
**NZL**, **CAN**, **KAZ** among revolving-door rows. Those nine I checked line by line against
raw source text and found nothing to correct.
