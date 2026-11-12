# Fact-check log: r26f_people_totals_3

Checked 2026-11-11. Independent check of 8 entries against the brief in `docs/PEOPLE.md`.
I opened every cited source myself and read the passage each figure rests on. No figure was
accepted from a search snippet, from the writer's note, or from memory.

Outcome: 1 confirmed unchanged, 3 corrected, 2 blanked, 2 `figure_for_owner` fields verified
and left unchanged (no `total` written for either, as instructed).

## Fetch failures encountered, by type

Three different kinds of failure came up, and they are not interchangeable:

- **Lapsed fetch permission** (`PROVENANCE_REQUIRED`): the permission request was never put to
  the user, or an earlier one went unanswered so later ones were not sent. Hosts affected:
  `www.sec.gov` (the Doe Run 10-K URL as written in the input), `documents.worldbank.org`
  (all five annual-report PDFs), `emcoholding.com`, `legalculturessubsoil.ilcs.sas.ac.uk`,
  `www.privinvest.com`. This is not the site refusing anything.
- **Server refusal**: `www.sec.gov` returned HTTP 403 with the body
  "SEC.gov | Your Request Originates from an Undeclared Automated Tool" to a plain `curl`.
  I did not spoof a user agent to get round it.
- **Robots block**: `www.renco-group.com` is `robots_disallowed`, as the writer recorded.

Two of these I worked around legitimately and the figures survive. For the SEC filing, one web
search surfaced the same document at the zero-padded EDGAR path
(`edgar/data/0001061112/...`), which WebFetch then opened in full; the source URL in the
checked file is updated to the one that opens. For the five World Bank annual reports, the
Bank publishes OCR text versions of the same documents at
`documents1.worldbank.org/curated/en/<id>/text/multi-page.txt`, which I downloaded by curl and
read directly - that is the same document, same page images, and all six (FY1991, 1992, 1993,
1997, 1998, 1999) came down intact.

---

## beny-steinmetz - BLANKED

**Opened:** his witness statement of 2 September 2015 in *BSG Resources Ltd v Republic of
Guinea*, ICSID Case No. ARB/14/22, on `icsid.worldbank.org`.

**Confirmed:** every figure the writer reported is in the document and accurately reported.
Para 3, "In 2003, these natural resource projects were consolidated into one company, BSGR".
Para 4, "The BSG group now operates in more than 20 countries worldwide". Para 12, BSGR
"has had operations in 14 countries" and "has employed over 8,000 people". Para 14, "BSGR has
evaluated and considered more than 120 prospective deals on four continents over the last
decade". Paras 1, 15, 16: "I am not a director of any company. I am not a shareholder" - he is
contracted as an adviser on a flat-rate fee.

**Cut, and why:** the whole sentence. Reporting accuracy is not the problem; provenance is.
(1) The document is a pleading he filed to win money from Guinea. Every number in it is his own
assertion about his own group, untested at the point of filing, and BSGR publishes no annual
report, so there is no audited or third-party figure to set beside it. The brief's standard is
a *sourced* figure; a self-serving claim in one's own arbitration is a claim, not a source.
(2) The 14-country and 8,000-employee claims carry no year and are phrased in the present
perfect, so they cannot be tied to any period - certainly not to the Simandou years the map's
case concerns. A "how much he oversaw" sentence that cannot say *when* says nothing.
(3) The same statement says he held no directorship and no shareholding in BSGR. The brief asks
for the output of the post through which the person acted. There is no post here to hang 14
countries and 8,000 employees on, and writing one would imply an authority he expressly denied
under oath in the document being cited for it. The brief's own instruction covers this case:
where there is no post with countable output, write `""`.

The source stays in `sources_add` so the owner can see what was considered.

---

## bill-turner - CONFIRMED UNCHANGED

**Opened:** Anvil Mining Limited's Annual Information Form for FY2007 (dated 28 March 2008) on
`announcements.asx.com.au`, in two passes (characters 0-100,000 and 100,000-200,000).

**Confirmed:** President and CEO and a director of Anvil Mining Limited from 8 January 2004;
managing director of Anvil Mining NL July 2003 to 8 January 2004; general manager July 1995 to
July 2003; director of Anvil Mining NL since 23 September 1996. Three producing DRC mines -
Dikulushi (commercial production since October 2002), Kulu, Kinsevere (mining from December
2006, HMS plant commissioned June 2007). Exploration interests in the DRC, Zambia and the
Philippines. "As of February 29, 2008, the AVM Group employs 4,390 people, of whom 2,750 are
direct employees."

**Tenure tie:** sound. The appointment date is in the same document as the company-scale
figures, so the figures fall inside his tenure. The headcount is February 2008, over three
years after the October 2004 Kilwa killings, and the sentence dates it explicitly rather than
letting a 2008 number stand in for a 2004 one. That is the right handling.

**Noted, not changed:** the source contradicts itself slightly. The per-site direct-employee
figures (Dikulushi 1,020, Kulu 340, Kinsevere 850, other 540 locations 360) sum to 2,570, not
the 2,750 the document states. The sentence quotes the document's own stated total and does not
reproduce the breakdown, so nothing in the sentence is wrong. Flagging it so the owner is not
surprised later.

---

## ira-rennert - CORRECTED

**Opened:** Doe Run Resources Corporation Form 10-K for FY ended 31 October 2001, on SEC EDGAR
(after recovering a working URL - see the fetch-failures section).

**Cut and corrected:** the writer's sentence said Doe Run "ran eight production shafts along
Missouri's Viburnum Trend". The filing says the Missouri operations *have* eight production
shafts along about 40 miles of the trend, of which **six are currently operating**, with
Viburnum-29 and West Fork on care and maintenance; Item 1 itself refers to "six production
shafts". "Ran eight" counts two idle shafts as working mines. The sentence now reads "held
eight production shafts along Missouri's Viburnum Trend, six of them operating and two on care
and maintenance".

**Confirmed, unchanged:** Rennert is Renco's "Chairman and Chief Executive Officer"; Renco is
owned by trusts he established "for himself and members of his family"; "Mr. Rennert controls
the Company and its subsidiaries" (sole stockholder DR Acquisition Corp., a wholly-owned Renco
subsidiary). La Oroya bought from Centromin 23 October 1997; Cobriza acquired August 1998.
Employees as of 31 October 2001: US 400 active salaried, 1,138 active hourly; Peru 955 active
salaried, 2,131 active hourly, 1,475 contractors. Net sales FY2001: US $303.1m, Peru $434.3m
(consolidated $737.5m after intercompany eliminations).

**Tenure tie:** sound, and honestly labelled. The sentence attributes the figures to Doe Run,
not to Renco Group, which is what the source supports; `renco-group.com` is robots-blocked and
no group-wide Renco figure exists on any page opened. Rennert's control is stated in the same
filing as the figures, in the same fiscal year, so the figures are of his watch.

---

## iskandar-safa - CORRECTED

**Opened:** *Republic of Mozambique v Credit Suisse International and others*, High Court of
Justice, Business and Property Courts, judgment of 29 July 2024, in two passes (characters
0-100,000 and 100,000-200,000).

**Cut and corrected:** the writer's sentence said Safa "signed three supply contracts in 2013
and 2014". The judgment nowhere records him signing any of the three. The signatories it names
are:

| Contract | Signed | Privinvest entity | Signatories named |
|---|---|---|---|
| Proindicus (maritime surveillance) | 18 January 2013 | Privinvest Shipbuilding SAL | not given in the passages opened |
| EMATUM (tuna fleet) | 2 August 2013 | Abu Dhabi Mar LLC | Mr Allam (CFO); Mr do Rosario and another for EMATUM |
| MAM (shipyard) | 1 May 2014 | Privinvest Shipbuilding Investments LLC | Mr Boustani for Privinvest; Mr do Rosario for MAM |

Safa appears in the judgment as a 33 per cent owner of Privinvest, not as a signatory. The
sentence now says he **approved** the group's three supply contracts, which is the finding the
court actually made, and gives the window as "signed between January 2013 and May 2014" from
the dates above rather than a bare "2013 and 2014".

**Confirmed, unchanged:** para 26, his chairmanship was "executive, and full-time executive",
and he "insisted on and had a close grasp of matters"; para 29, "I am satisfied no major
activity proceeded without his knowledge and approval, including of the figures"; para 7,
"after change orders and increases, a total of approaching US$2 billion" and "more than 12% of
GDP". Para 30 records his own evidence that he was "the final decision-maker to say whether I
approve the transaction" but not the contract's content - which is exactly what the corrected
wording now claims and no more.

**Two things the owner should know, not in the sentence:** at para 23 the judge "did not accept"
Safa or Boustani "as a consistently truthful witness"; at para 34(b) the judgment sets out only
what the outcome on the Safa claims *would have been*, because he died before judgment, with
the consequences reserved at para 34(a).

**Also checked and left out:** no group-wide count of shipyards, employees or countries survives.
The undated CEO Magazine interview claiming 2,000 vessels delivered has no date and no yard,
employee or revenue count. `privinvest.com` could not be opened (lapsed fetch permission).

---

## joseph-stiglitz - `figure_for_owner` VERIFIED, UNCHANGED. No `total` written.

**Opened:** World Bank Annual Reports 1997, 1998 and 1999 (the Bank's own OCR text versions of
the same documents - see fetch failures); the Nobel Prize biographical page; the World Bank
projects API.

**Confirmed, number by number:**
- AR1998, Appendix 14: `Grand total  105  17,282.0  124  7,060.4  229  24,342.4` - 105 IBRD
  loans, 124 IDA credits, 229 operations. Matches.
- AR1999, Appendix 14: `Bankwide total  131  22,182.3  145  6,811.8  276  28,994.1` - 131, 145,
  276. Matches.
- 229 + 276 = 505, and the field says plainly this is this map's sum of the two reports.
- Both appendices carry the footnote quoted: "Supplements are included in the amount but are not
  counted as separate lending operations. Joint IBRD/IDA operations are counted only once, as
  IBRD operations."
- Officer lists, each headed with its own date: "OFFICERS OF THE WORLD BANK ... June 30, 1997",
  "... June 30, 1998", "... June 30, 1999", each naming "Senior Vice President, Development
  Economics, and Chief Economist  Joseph E. Stiglitz". Verified in all three reports.
- Nobel biographical page: "I left the World Bank in January 2000." Verified.
- Projects API, 1 July 1997 to 30 June 1999: `total 597`. Matches the field exactly, and the
  field is right that this is not a lending total and not comparable with 505.

**Does it state plainly what it counts?** Yes. It names the instrument (IBRD loans and IDA
credits approved by the Board), the counting conventions, what is excluded (IFC, MIGA, GEF,
Montreal Protocol, guarantees, recipient-executed trust funds, carbon offset, special financing,
debt reduction), why those two fiscal years and not four, that the two partial years are left
out, and that the 505 is a sum made here rather than a published figure. A reader can tell what
they are looking at.

**One addition the owner may want, not an error:** the AR1999 appendix carries a further
footnote, "Excludes an IDA HIPC grant of $150 million to Mozambique". That is an exclusion from
the *amounts*, not from the count of 276, so the 505 is unaffected.

Whether to use this figure is the owner's decision. I take no position on it.

---

## lawrence-summers - `figure_for_owner` VERIFIED, UNCHANGED. No `total` written.

**Opened:** World Bank Annual Reports 1991, 1992 and 1993 (Bank OCR text versions); the World
Bank projects API.

**Confirmed, number by number:**
- AR1991, Table 7-1: `Grand total  126  16,392.2  103  6,293.3  229  22,685.5` - 126 IBRD
  loans, 103 IDA credits, 229 operations. Matches.
- AR1992, Table 7-1: `Grand total  112  15,156.0  110  6,549.7  222  21,705.7` - 112, 110, 222.
  Matches.
- 229 + 222 = 451, and the field says plainly it is this map's sum.
- Both tables carry the footnote quoted, word for word: "Supplements are included in the
  amounts, but are not counted as separate lending operations. Joint IBRD/IDA operations are
  counted only once, as IBRD operations."
- Officer lists: "Officers and Department Directors of the World Bank / June 30, 1991" and
  "... June 30, 1992" both name "Vice President, Development Economics and Chief Economist
  Lawrence H. Summers". The 1993 list names "Vice President and Chief Economist, Development
  Economics ... D.C. Rao (Acting)". All three verified. Pinning the window to the two full
  fiscal years in which he is recorded in the post, rather than guessing at calendar dates, is
  the right call given that no non-Wikipedia page gives his start and end dates.
- Projects API, 1 July 1990 to 30 June 1992: `total 309`. Matches the field exactly, and the
  field is right that 309 against the reports' 451 for the same window means the API's
  early-1990s coverage is incomplete and should not be used here.

**Does it state plainly what it counts?** Yes - same structure as the Stiglitz field, and it is
explicit that the part of fiscal 1993 he served is not in the 451.

Whether to use this figure is the owner's decision. I take no position on it.

---

## lenir-perez - BLANKED

**Opened:** the Estrategia y Negocios profile on `revistaeyn.com`.

**Confirmed about the source:** the writer's description of it is accurate. It carries the label
"POR E&N PARA EMCO HOLDING", is dated 17 December 2021, names "Lenir Perez Solis" as president
of Emco Holding Inc (commercially Grupo Emco), and puts group assets above $700 million for
2021. Other figures in it: sales projected above $1,000 million for 2022; Palmerola
International Airport over $200 million, opened 11 December 2021; Tocoa iron-pellet plant $200
million, over 800 jobs now and over 3,000 once operating; El Salvador cargo terminal phase 1
$13.3 million and phase 2 $49 million; cold chain over $125,000; Puente Alto Energy about 4,000
million lempiras for 100 MW; AeroMetro in Guatemala with no figure given.

**Ruling: the figure goes.** Three independent reasons, any one of which would be enough:

1. **It is not an independent source.** "POR E&N PARA EMCO HOLDING" means the subject's own
   company commissioned a profile of the subject. The $700 million is Grupo EMCO's own unaudited
   claim about itself, with no filing, auditor, registry or regulator behind it. Disclosing that
   inline tells the reader the number is weak; it does not make it checked. The brief asks for a
   sourced figure, and the whole point of the no-fabrication standard is that a figure traces
   back to someone other than the person it flatters.
2. **Wrong shape.** The brief asks how many projects, loans or deals the person oversaw. This is
   a dollar asset total. The article gives no count of group companies, no group headcount and no
   project count, so there is nothing in it to convert into the shape the brief asks for.
3. **Mixed periods.** The piece runs 2021 actuals together with 2022 projections, so even taken
   at face value the figure is not cleanly of one period.

**Other routes tried and failed:** `emcoholding.com` and the ILCS subsoil-companies entry on
Inversiones Los Pinares were both refused with `PROVENANCE_REQUIRED` - a lapsed fetch
permission, the requests were never put to the user, not a server or robots block. The UN
special-procedures letter of 3 November 2021 on the Guapinol case gives case detail (one Los
Pinares mining licence; 217 hectares opened to mining inside the Carlos Escaleras national
park), which is not company scale.

The E&N source and its figures stay recorded in the entry's `note` and `sources_add`, labelled
for what they are, so the owner can see what was rejected and why.

---

## ly-yong-phat - CORRECTED: the ~40,000 ha sum cut, Oddar Meanchey hectares removed

**Opened:** the Licadho statement of 21 August 2014 on `licadho-cambodia.org`; the ActionAid
Cambodia and Oxfam GB report *The Bitter Taste of Sugar* (May 2015), first 100,000 characters.

**What survives, and is now the whole sentence.** Licadho states that the Koh Kong Plantation
Co. concession agreement is **dated 2 August 2006 and was signed by Ly Yong Phat**, who is named
as the company's Director; that a concession for adjacent land went to Koh Kong Sugar Co. the
same day; that together the two form a "20,000 hectare industrial sugar plantation"; and that
per the Ministry of Commerce website he "completely divested his shares in the Koh Kong sugar
plantations in December 2009". (The same page records the Ministry listing him as "former
Chairman and Agent of Registration" of Koh Kong Plantation Company Ltd, and KSL and Ve Wong now
holding 70/30.) This rests on a document he put his own name to, in one year, from one source,
with the end of his interest stated. It is in his name and it is dated. It stays.

**What is cut: the Oddar Meanchey 19,736 hectares, and therefore the ~40,000 ha sum.**

The hectares themselves are solid - the ActionAid report gives Angkor Sugar 6,523, Cambodia Cane
and Sugar Valley 6,595 (6,596 in one MAFF memo entry), Tonle Sugar Cane 6,618, total 19,736,
contracts signed 24 January 2008, applications 8 March 2007, MAFF/COM approval 18 December 2007.
The problem is whose they are. The report's own wording, under the heading "Connection to
Senator Ly Yong Phat and the LYP Group", is: "There is also some reported affiliations between
the three companies with CPP Senator Ly Yong Phat and his company LYP Group" - resting on a
shared head-office address per the Ministry of Commerce website and a commune councillor, Um
Sokhon, saying the concessionaires "are under the control of Yong Phat". (The writer's
paraphrase "reportedly affiliated" is fair; the exact phrase is the one above.) Licadho is
blunter: the three companies were "believed to be owned wholly or partly by **Mitr Phol**", and
of Ly Yong Phat it says only that he "is clearly affiliated in some way with these businesses".

A reported affiliation of unstated kind, against a *named other owner*, is not a holding and not
a post. The brief asks what the person oversaw through a post; "affiliated in some way" supports
no number in his name.

**On whether a sum across the two sources was sound: no, on three counts.**
- It adds hectares established by a concession agreement he personally signed to hectares
  linked to him only by inference, so the two halves carry different standards of proof and the
  combined figure inherits the weaker one while reading as though it inherited the stronger.
- It spans concessions granted two years apart (August 2006 and January 2008), one of which he
  had divested by December 2009, so "about 40,000 hectares" is never true of any single moment.
- It rounds 20,000 + 19,736 to "about 40,000", which buries the fact that half the total is
  contested. A reader cannot see the seam.

The ActionAid/Oxfam report is dropped from `sources_add`, since no figure now rests on it. It
remains worth citing in the map's case text for the Oddar Meanchey displacement itself - the
objection is to putting its hectares in his name, not to the report.

**Also checked and left out, as the writer had it:** the Phnom Penh Post article listing six
concessions totalling about 61,000 hectares (including Phnom Penh Sugar 8,343 ha and Kampong
Speu Sugar 10,000 ha registered to his wife) carries no publication date, so it cannot be cited.
The US Treasury designation of 12 September 2024 calls L.Y.P. Group his conglomerate and names
four hotels and resorts he owns or controls, but gives no group-scale count. LYP Group's own
brochure and profile pages carry no company count, employee count or hectare figure.
