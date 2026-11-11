# Fact-check log: batch 8b lender-condition entries

Independent check of `r26f_conds_research_8b.json` (60 cases, 3 with text). Output:
`r26f_conds_research_8b_checked.json`. All 60 keys kept; 57 blanks left blank.

Result: 1 entry confirmed, 2 corrected, 0 blanked.

---

## 1. `novi-sad-station-canopy-collapse` — confirmed, sourcing upgraded

**What I opened.** The Serbian Ministry of Finance publishes the ratifying law with the
full agreement text in English and Serbian:
`https://mfin.gov.rs/upload/media/al9Zd6_6018080bc2e98.pdf` (downloaded and converted to
text, so the clauses were read in the original, not through a summariser). I also re-read
the writer's Law Insider copy, `https://lawinsider.com/hr/contracts/keYMJEEIJJe`.

**The agreement is the right one.** Title page: "PREFERENTIAL BUYER CREDIT LOAN AGREEMENT
... for Section Novi Sad-Subotica-State Border (Kelebija)", No. PBC (2019) 4 (487),
between the Government of the Republic of Serbia represented by the Ministry of Finance
as Borrower and The Export-Import Bank of China as Lender, dated 25/4/2019. Recital
names the commercial contract of July 7, 2018 with the JV of China Railway International
Co. Ltd and China Communications Construction Company Ltd, total US$1,162,810,000, and
the facility of up to US$988,388,500.00.

**The quoted articles say what the entry says**, verbatim from the official PDF:

- Art. 2.4: "The entire proceeds of the Facility shall be applied by the Borrower for the
  sole purpose of the payment of approximately eighty five percent (85%) of the Commercial
  Contract amount, and not be used for payment of brokerage fees, agency fees or
  commission."
- Art. 2.5: "The goods, technologies and services purchased by using the proceeds of
  Facility shall be purchased from China preferentially according to the Commercial
  Contract."
- The 15:85 condition is in Appendix 1, Part A(5) and repeated in Appendix 2(6), not in
  Article 2.4: certified copies of documents evidencing "that the End-User has made
  sufficient payment to the Contractor, without utilizing the proceeds of the Loan, prior
  to each disbursement ... so that after such disbursement, the ratio of the aggregate
  Self-raised Fund to the Loan shall not be lower than 15:85". "End-User" (Art. 1.9) is
  the Government of Serbia through the Ministry of Construction, Transport and
  Infrastructure, or Infrastructure Railways of Serbia; the Serbian text of the same item
  says "српска страна" (the Serbian side), so the entry's "the Serbian side" is right.

**Harm is in the right section.** Vreme's account of the Chinese firms that rebuilt the
station (`vreme.com/en/vesti/srpski-poslovi-kineskih-firmi-koje-su-rekonstruisale-stanicu-u-novom-sadu-putevi-pruge-obilaznice/`)
says the Novi Sad station building was reconstructed as part of the Novi Sad–Subotica
section (108 km) by the CRIC&CCCC consortium, financed mainly by China Eximbank loans.
Worth noting for the card, though not a loan term: the contractor and the Serbian
authorities say the canopy itself was not part of the building's reconstruction.

**Changes made.**
- Added the Ministry of Finance PDF as the primary source, ahead of Law Insider.
- "a US$988,388,500 loan to Serbia's Ministry of Finance" → "a loan of up to
  US$988,388,500 to the Government of Serbia represented by the Ministry of Finance",
  which is what the agreement says.
- Attributed the 15:85 condition to Appendix 1 rather than leaving it next to the
  Article 2.4 sentence, and quoted "shall not be lower than 15:85" in full.
- The writer's `searched` line said the Belgrade–Stara Pazova agreement was US$350m.
  The Ministry of Finance copy of that agreement
  (`https://mfin.gov.rs/upload/media/0fVMlJ_6017f4923997e.pdf`) gives a facility of up to
  US$297,638,159.00 for Section Belgrade Center–Stara Pazova, commercial contract
  5 November 2016. Corrected in `searched`.
- `ct` (tied, fincov) and both `why` quotes stand.

## 2. `plan-colombia-aerial-spraying` — corrected: the quoted tests were from a different statute

**What held up.** The Congressional Research Service brief IB88093 does say, verbatim,
"The enacted bill included conditions on the use of funds for purchase of chemicals for
the aerial spraying program in Colombia", of P.L. 107-115. So the entry's core claim —
that Congress, not the agency, attached conditions to this money — is sound.

**What did not.** The tests the entry quoted came from the State Department's
"Memorandum of Justification Concerning the Aerial Eradication of Coca and Opium Poppy in
Colombia". I opened that document
(`https://corpora.tika.apache.org/base/docs/govdocs1/304/304931.html`) and asked it
directly: it is a December 2003 INL report, it cites the Foreign Operations appropriations
act in Division E of the Consolidated Appropriations Resolution, 2003, **P.L. 108-7**, and
it never mentions P.L. 107-115 or the FY2002 act. Its "not more than 20 percent of the
funds appropriated by this Act that are used for the procurement of chemicals" proviso,
and its wording "in accordance with EPA label requirements for comparable use in the
United States" and "unreasonable risks **of** adverse effects", are the FY2003 act's. The
entry attached them to P.L. 107-115 — failure 4 in the brief, a term from a different
instrument.

**Replacement.** I downloaded the enacted text of P.L. 107-115 from govinfo
(`https://www.govinfo.gov/content/pkg/PLAW-107publ115/html/PLAW-107publ115.htm`) and read
the Andean Counterdrug Initiative heading, 115 Stat. 2130–2131. Its proviso has no
20 percent cap; it says funds "that are used for the procurement of chemicals for aerial
coca fumigation programs may be made available for such programs only if" the Secretary of
State, after consultation with the Administrator of the EPA, the Secretary of Agriculture
and, if appropriate, the Director of the CDC, "determines and reports to the Committees on
Appropriations" that (1) fumigation is carried out in accordance with EPA regulatory
controls "as labeled for use in the United States" and after consultation with the
Colombian Government; (2) the chemicals "in the manner in which they are being applied, do
not pose unreasonable risks or adverse effects to humans or the environment"; and (3)
"procedures are available to evaluate claims of local citizens that their health was
harmed or their licit agricultural crops were damaged by such aerial coca fumigation, and
to provide fair compensation for meritorious claims"; and the funds "may not be made
available for such purposes after six months from the date of enactment of this Act unless
alternative development programs have been developed, in consultation with communities and
local authorities" in the departments concerned.

The entry is rewritten from that text. The 2003 Memorandum of Justification was dropped as
a source. P.L. 107-115 was enacted in January 2002, inside the card's 2000–2015 spraying
period, so the date test is met for that part of the period; the entry now says so plainly
rather than implying the conditions covered the whole run of spraying. `ct` stays
safeguard + admin; both `why` quotes were rewritten to the statutory wording ("licit
agricultural crops", "risks or adverse effects") and both now appear verbatim in both the
entry and the statute.

## 3. `lawpita-baluchaung-karenni` — corrected: quote capitalisation, and "partially untied" explained

**What held up.** I downloaded the JICA PDF
(`https://www.jica.go.jp/english/our_work/evaluation/oda_loan/post/2002/pdf/070_full.pdf`;
the evaluation PDFs do open even though JICA project pages do not) and read section 1.5,
"Outline of Loan Agreement": Loan Amount 3,530 million yen; Loan Disbursed Amount
3,460 million yen; Exchange of Notes September 1987; Loan Agreement November 1987;
Interest Rate 2.50% p.a.; Repayment Period (Grace Period) 30 years ( 10 years );
Procurement **Partially Untied**; Final Disbursement Date May 1995. Section 1.4 gives the
Borrower/Executing Agency as the Electric Power Corporation (EPC). Report date May 2002,
field survey September 2001. Loan, year and amount all confirmed.

**What did not.** Two things.
- The report writes "Partially Untied"; the entry quoted it as "Partially untied". Fixed.
- "Partially untied" was left bare under `ct: tied`, which on a map that defines `tied` as
  "must use the lender country's contractor" reads as more than the source supports. Japan's
  foreign ministry defines the three categories in its ODA loan implementation procedures
  (`https://www.mofa.go.jp/policy/oda/guide/1998/3-5.html`): tied loans are those "in which
  goods and services are procured from Japan only", while "For partially untied loans, the
  eligible source countries are developing countries on the DAC's LDC list and Japan." I
  added that definition to the entry, so it records a real procurement restriction without
  claiming the loan forced Japanese suppliers. `ct: tied` kept, as the only procurement
  type in the brief's list.
- The entry called the document a "post-evaluation report"; JICA's own series name is the
  ex-post evaluation. Title corrected in `sources_add`.

Note for whoever assembles the card: the case's existing `conditions` text already carries
these same loan terms, so this entry is largely a duplicate of what is on the card.

---

## Spot-check of 10 blanks whose `searched` line blames a host

Tested the hosts independently with curl (which does not apply WebFetch's robots and
search-result rules) to separate "the host refuses" from "the search was thin".

| Case | Host blamed | What I found |
|---|---|---|
| `xe-pian-xe-namnoy-collapse` | peoplepower21.org | **Refusal confirmed.** The page returns an 811-byte body containing only an obfuscated script that sets a `CUPID` cookie and reloads with `&ckattempt=1`. No content is served to a non-browser client. Exactly as described. |
| `jalaur-dam-tumandok-killings` | peoplepower21.org, proximoinfra.com | peoplepower21.org as above. proximoinfra.com serves its home page (HTTP 200) but is a subscription trade service; the paywall claim is consistent and I found no free copy of the KEXIM financing report. |
| `rapu-rapu-cyanide-spills-2005` | miningnews.net | **Refusal confirmed.** HTTP 403 on the site root and on an article path. |
| `phnom-penh-sugar-kampong-speu` | oecd.org | **Refusal confirmed, and stronger than described.** Both `oecd.org` and `mneguidelines.oecd.org/database/instances/au0012.htm` return HTTP 403. One route not tried: the OECD Watch mirror of the complaint, `oecdwatch.org/complaint/ec-and-idi-vs-australia-and-new-zealand-banking-group/`, serves fully (HTTP 200). It is a complaint record, so it is unlikely to carry ANZ's loan covenants, but it is a reachable document on this case that the round did not open. |
| `theun-hinboun-expansion` | banktrack.org download | Partly. banktrack.org itself serves normally (home page and `/search` return 200); the project slugs I guessed 404, so I could not reproduce the specific download that returned unreadable binary. The host does not refuse; the single file did. |
| `jirau-dam-esbr-madeira` | recommon.org | **Claim overstated.** recommon.org serves normally (HTTP 200), and its site search works. What it holds on Jirau is two Italian articles — one on the Petrobras scandal reaching Amazon dams (2015) and one on green bonds (2014) — i.e. the green-bond angle the round already had and correctly set aside. The host is not blocked; there is simply nothing there on a lender's condition. Blank stands. |
| `chitwan-wwf-ranger-custody-death` | buzzfeednews.com, kathmandupost.com | **Claim overstated as host refusal.** Both serve content to curl (HTTP 200 on the home page and a dated section page). The refusal is at the fetch-tool level, not the host. Neither is a financing document, so neither would have changed the result. Blank stands. |
| `salonga-wwf-ecoguards-usaid-kfw` | buzzfeednews.com, kfw.de | Same for BuzzFeed. kfw.de serves its home page (HTTP 200); I could not test the specific human-rights due-diligence PDF without its URL. "Host refused" is too broad for kfw.de; "that PDF would not fetch" would be accurate. |
| `kotopanjang-dam` | jica.go.jp/oda/project/IP-358 | **A reachable document exists, and it was worth saying what is in it.** `https://www.jica.go.jp/oda/project/IP-358/index.html` serves fully to curl (the English path 404s; the Japanese path works). The pages carry `<meta name="robots" content="noindex,nofollow">`, which is a fair basis for a fetch tool to decline, so "robots_disallowed" is honest. Content: Kotapanjang Hydroelectric Power and Associated Transmission Line Project (1), L/A signed December 1990, loan amount ¥12.5 billion — a date and an amount, and no rate, term or procurement condition. It would not have filled the blank. |
| `thilawa-sez-resettlement` | jica.go.jp project pages | Same host behaviour as above: the pages are served to curl but carry `noindex,nofollow`. JICA publishes no `robots.txt` (the path returns the site's 404 page), so the refusal is driven by the page meta tag. |

**Summary of the spot-check.** Six of the ten name a host that genuinely will not serve
content to an automated client (peoplepower21.org, miningnews.net, oecd.org and
mneguidelines.oecd.org, plus the two JICA page sets by robots meta tag). Four overstate a
fetch-tool refusal as a host refusal (recommon.org, buzzfeednews.com, kathmandupost.com,
kfw.de at host level, banktrack.org at host level). Two reachable documents exist that the
round did not open — the OECD Watch mirror of the ANZ/Phnom Penh Sugar complaint and the
JICA IP-358 project page — and on inspection neither carries a lender condition, so no
blank should be reopened on the strength of them. I did not research the blanks beyond
this check.

---

## Validation

`r26f_conds_research_8b_checked.json` parses as JSON, holds all 60 original keys, every
`ct` value is from the brief's list, every entry with text has a non-empty `ct` and every
blank has an empty `ct` and a `searched` line, every `why` type appears in its entry's
`ct`, and every `why` quote appears verbatim in its own `conditions_add`.
