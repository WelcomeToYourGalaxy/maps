# Round 43: fixes to live suspected-pattern cards

Nine confirmed defects fixed and four empty `case_ids` fields decided. Edits are in
`rounds/r43_hypfix.json`, keyed by entry id, each as `{field, old, new}` with the whole paragraph as
`old` for every story change. `base.html` was not edited and nothing was built or committed. Every
`old` string was checked programmatically against the live `window.HYPS` and matches exactly once.

Every fact I put on a card comes from a document I opened myself in this round. Quotes are under 15
words and one per source. Where a document would not open, the fact came off the card rather than
being softened, and that is recorded both in the JSON and below.

## One thing to decide before this goes on the page

**The stories get longer, and four now overrun HYP's 350-to-500-word guide.** Words before and after:

| id | before | after |
| --- | --- | --- |
| `rankings-bent-for-money` | 472 | 686 |
| `banks-that-bank-the-looters` | 487 | 629 |
| `water-handed-to-companies` | 516 | 626 |
| `aid-cover-for-spies` | 522 | 596 |
| `ratings-that-punish-relief` | 440 | 591 |
| `carbon-credits-new-land-grab` | 475 | 554 |
| `companies-behind-coups` | 471 | 518 |
| `secret-loans-banks-traders` | 504 | 517 |
| `lending-to-known-thieves` | 456 | 499 |

Seven of the nine were already over 500 before I touched them. The growth is the cost of the
additions the brief required: two more countries and a second motive on the rankings card, both
halves of a sentence on the water card, a regulator's actual finding on the banks card, a
re-sourced paragraph on the spies card. I compressed each replacement twice and did not cut
anything load-bearing to get the counts down. If you want them back under 500, the place to cut is
`rankings-bent-for-money` paragraph 1, which spends about 60 words on the Georgieva scene and the
Doing Business explainer; I left it alone because the brief said to fix these defects and only these.

## Per entry

### 1. `water-handed-to-companies` — half-quote fixed

Paragraph 2 said only that "a 1998 Bank report said the loan had facilitated it". I opened the
report (Implementation Completion Report, Second Jabotabek Urban Development Project, Loan 3219-IND,
Report No. 18049, 23 June 1998) and the passage now carries both halves: the privatisation of PAM
JAYA's operations was an event "parallel to but facilitated by the Project", and it was not
envisaged by the government or the Bank at appraisal because private sector participation was still
a new concept then; and at paragraph 28, that had the government proposed such an option in the
late 1980s it would most likely have been turned down by the Bank, after other unsuccessful
experiences in Indonesia. The paragraph now states the conclusion plainly: the Bank's own account
is that its loan helped Jakarta's privatisation along without the Bank having designed or wanted it.
The report is added to `sources`; it was not there before.

**Flagged, not fixed, as instructed.** The Cochabamba loan condition in paragraph 1 — the $14
million World Bank water loan said to have been "conditioned on the city privatising its water" —
still rests on the Democracy Center, an advocacy source, and so does the $600 million debt-relief
claim on the `cochabamba-water-war` case card. I did not look for a better source and did not
invent one. That is the load-bearing claim in the entry's opening scene, and it is the weakest thing
on the card after this round.

### 2. `rankings-bent-for-money` — four countries, two motives

Opened the WilmerHale report in full from the Bank's own copy at `thedocs.worldbank.org`. Paragraph
2 now carries the United Arab Emirates and the Jordan instruction; paragraph 3 now opens on
Azerbaijan. Added:

- The scope: improper changes for China in Doing Business 2018 and for Saudi Arabia, the UAE and
  Azerbaijan in Doing Business 2020.
- Jordan, which is the **first** stated consideration in the Saudi change: in September 2019 Djankov
  told the team to find a way to drop Jordan from the top of the draft Top Improvers list; the
  employee he sent to Jordan reported Jordan's data was correct; the team then looked for ways to
  lift Saudi Arabia past it.
- The paid advisory contracts as **one of three** things the report says could have motivated him,
  under a finding it words as "likely" — not as the cause.
- The UAE change following mechanically from the Saudi one because of the similar tax system, and
  not moving the UAE's ranking.
- Azerbaijan changed **downward** on Djankov's own disbelief in the reforms, with several employees
  saying he appeared to harbour a personal animus against the country, and no money in it.
- One sentence covering both of the report's no-involvement findings (president's office, board).

I left out two things the checker mentioned. The accelerated Protecting Minority Investors
methodology change is real and verified (paragraph 24) but costs 40 words for a detail the brief did
not ask for. The employees' "pay-to-play" remark is an impression the report records, not a finding,
and the card does not mention it at all, so there was nothing to harden; adding it would have been
a new claim, not a fix. Both are in `what_i_verified` if you want them.

I also rewrote the `conviction` line, which said the rankings were changed "for China and Saudi
Arabia" — the same two-country framing as the defect. It now names all four and the "likely" finding.

### 3. `carbon-credits-new-land-grab` — date corrected, appeal added

Verified both citations through `kenyalaw.org/search/api/documents/`, which serves JSON. The
judgment is *Osman & 164 others v Northern Rangelands Trust & 8 others* (Petition E006 of 2021)
[2025] KEELC 99 (KLR), Environment and Land Court at Isiolo, **24 January 2025** — not the 31st. The
appeal is *Northern Rangelands Trust v Osman & 164 others* (Civil Appeal (Application) E019 of 2026)
[2026] KECA 1774 (KLR), Court of Appeal at Meru, ruling **25 September 2026**, with the Trust as
appellant. Both added to `sources`.

**What the appeal decided is unknown and the card now says so.** The judgment pages are walled; as
instructed I did not try to get past them, and a second search on the neutral citation returned no
snippet of the holding. The card says the judgment is under appeal, gives the appeal's date, and
states that nothing here says what the appeal decided or whether the January ruling still stands. It
does not imply an outcome either way. The `conviction` line now also says the ruling is under appeal.

Noticed in passing, outside this fix: the map already holds
`northern-rangelands-isiolo-conservancies` (Kenya, 2007-2025), which is the case this paragraph is
about, and it is **not** in this entry's `case_ids`. Worth adding in a later pass.

### 4. `ratings-that-punish-relief` — the $74.5bn figure, and an agency's own voice

Opened the UNDP policy brief. There is no "19" in it. Table 1 covers **13** African economies
(domestic-currency bonds); Table 2 covers **16** (Eurobonds); the union is **21** countries; and the
brief says that combining both tables the full cost of rating idiosyncrasies in Africa is estimated
at $74.5 billion in "excess interest and foregone funding", nearly 12 per cent more than all of
Africa's net official development assistance in 2020. The four table totals sum to $74,483 million,
so the figure is a combined total with no country count attached, not an "up to". Corrected in the
story **and** in the `conviction` line, which carried the same error.

**Counter-evidence added, from Fitch's own publication.** The 9 February 2021 rating action
commentary at `fitchratings.com` returns HTTP 200 and a script-built shell with about 620 characters
of navigation and no content — I could not open it. What I did open is Fitch's own "Frontier Markets
Quarterly – 1Q21" (April 2021), which lists "Ethiopia CCC 09-Feb-2021 Downgrade" in its rating-action
table and, under the heading "Common Framework Raises Risk of Default", gives Fitch's reasoning: the
downgrade was triggered by Ethiopia's intention to use the Common Framework, which raises the
possibility of restructuring debt owed to private creditors and would qualify as a distressed debt
exchange, leading to a restricted-default rating. Fitch draws the distinction itself: unlike the
DSSI, which took effect in May 2020, the Common Framework requires comparable treatment by private
creditors. So the card now says, in paragraph 3, that the trigger in the agency's own telling is not
asking for relief but asking private lenders to share in it, and that the bilateral-only suspension
scheme carried no such consequence. That narrows the claim rather than widening it, as the brief
asked. It is Fitch's own publication describing its own action, not the action notice; say so if
anyone asks. Added to `sources`.

### 5. `banks-that-bank-the-looters` — the range, and the regulator's actual finding

Opened the Senate subcommittee report. Both readings are in it, as the checker said, and the card
now gives both: aggregate deposits "ranging from $400 to $700 million at a time" (executive summary)
and, in the findings, balances and outstanding loans that together approached $700 million by 2003.
The $700 million figure stands; "up to" is gone.

On the regulator: paragraph 2 opened "Britain found the same thing with Nigeria", which read as a
second finding of knowing handling. It now opens by saying the regulator found something narrower,
and sets out what the FSA actually found: 42 personal and corporate account relationships at 23
banks, $1.3 billion of **turnover** on them between 1996 and 2000, 98 per cent of it at 15 banks
with significant weaknesses in anti-money-laundering **controls** — plus three things the card did
not carry and the fairness rule wants: the FSA said the turnover figure did not necessarily
represent proceeds of crime or money received into Britain; a number of the banks had reported their
suspicions to the national criminal intelligence service in good time; and the FSA had **no power at
that date** to name any bank, which is different from choosing not to. None was prosecuted.
Paragraph 1 also now gives the Riggs finding as the subcommittee's own — Turning a Blind Eye,
little or no attention to its obligations — rather than as established knowledge.

I could not open the FSA's own March 2001 press release, so the 42 accounts and the $1.3 billion
rest on the WealthBriefing report of it, which quotes the FSA directly. That is the same footing as
before, not worse.

### 6. `lending-to-known-thieves` — Brussels, and who says what about the debt

Opened the Christian Science Monitor piece of 8 October 1982. Its dateline is Brussels and its text
reads "A report has just been leaked here", so the leak was in Brussels. "Leaked from Zaire" is
corrected to "leaked in Brussels", with the month added.

On the debt, the card now does what this map's rule requires and gives who says what: the Monitor,
which reported the leak, puts Zaire's international debt at $4.1 billion; Probe International says
Zaire owed $5 billion when Blumenthal wrote. Both pages opened.

**Not changed, as the checker directed:** the "50 to 80 per cent" figure in paragraph 2 is verbatim
in the Wall Street Journal mirror already in the entry's source list. Not a defect.

### 7. `companies-behind-coups` — two unsupported claims removed, replaced with the record

Opened FRUS 1952-1954 vol. IV, Editorial Note 420, already in the entry's sources. It records the
26 February 1953 order expropriating about 234,000 acres at Tiquisate, the February 1954
announcement of a further 172,532 acres at Bananera, government agrarian bonds offered as
compensation in both, and Washington's written objection that deferred payment in bonds was not
prompt and effective compensation and that the amount was inadequate under international law. It
contains nothing about United Fruit's own tax declaration. So the tax-valuation claim is **removed**
and replaced with those facts, which are stronger and are in the document the entry leans on.

The story's "and that this has not stopped" is **removed**. The paragraph now ends: nothing on the
open record shows whether that has continued since the 1970s. That is what the entry's own fourth
paragraph says.

### 8. `secret-loans-banks-traders` — Chad's 98 per cent is 2017

Opened the Chad Joint World Bank-IMF Debt Sustainability Analysis of July 2019. Footnote 2 to its
external-debt table reads: "Glencore loan accounts for about 98 percent of commercial debt stock in
2017." The card said "98 per cent of the government's foreign commercial debt by the end of 2016",
wrong on the year and loose on the denominator; both corrected, with the document named. Added to
`sources`.

**Residual.** The same wrong year is in this entry's `countries` array — the TCD note reads
"Glencore held 98 per cent of foreign commercial debt at end-2016." The delivery format only covers
`story`, `conviction`, `sources` and `case_ids`, so I could not write that edit. It should read
"Glencore loan was about 98 per cent of the commercial debt stock in 2017." The 2016 oil-revenue
figures ($231m of $271m) were not re-verified; they rest on IMF Country Report 17/246, and imf.org
refused all three reviewers, so I did not retry it.

### 9. `aid-cover-for-spies` — the Wikipedia leg removed after two rounds

The Office of Public Safety paragraph is re-sourced on the item already fifth in the entry's own
list: the Congressional Record of 5 March 1992 (Senate, page S2874), Senator Cranston releasing the
GAO report *Foreign Aid: Police Training and Assistance*, reproduced by the Federation of American
Scientists. Opened in full. The paragraph now gives, from that document: the public safety programme
set up in the early 1960s; $60 million a year training police in 34 countries by 1968, in subjects
including interrogation, riot control and counterinsurgency techniques, with weapons and
communications equipment supplied; Cranston's statement, introducing the report, that US
"intelligence agencies were given an important role" in the development and execution of the
programmes; the 1973 and 1974 bans and the dozen exemptions granted since; and five US departments
training police from 125 countries in fiscal 1990 at about $117 million. I attribute the
intelligence-role line to Cranston, because it is his characterisation introducing the GAO report
and not a GAO finding.

**What came off the card**, because this document does not contain it and no other opened page does:
"about 1,500 advisers to at least 52 countries", Byron Engle described as a CIA operative, Senator
James Abourezk, and the torture accusation that travelled with them.

**Residual.** The Wikipedia item is still first in this entry's source list, and the `countries`
notes for Uruguay, Brazil and Guatemala were sourced through it and the ZNetwork Mitrione piece.
After this edit no sentence in the story rests on Wikipedia, which is the defect the checker
reported. The source list and those three notes still want a pass.

## The four empty `case_ids`

Rule 5 wants them filled; three of the four should stay empty, and I did not force a link.

- **`development-money-through-tax-havens` → `amulsar-gndevaz-jermuk`.** The map's own record for that
  case says the IFC invested $16.4 million in the developer, Lydian, from 2007, and describes Lydian
  as a holding company incorporated in Jersey whose shares traded in Toronto, with the mine in
  Armenia. Development money into a company held in a secrecy jurisdiction where it does no business
  is the shape the title names. **The caveat, and it matters:** Oxfam's count, which the story rests
  on, is of IFC clients in sub-Saharan Africa in 2015, and Armenia is not in it. The link is by
  shape, not by Oxfam's sample. If you read `case_ids` strictly as cases the cited evidence covers,
  drop it. I rejected three weaker candidates: `aperam-jequitinhonha` (IFC client incorporated in
  Luxembourg, but Luxembourg is where the steelmaker actually is), `canbalam-barillas` (its IFC
  client CIFI is genuinely based in Panama City), `united-cacao-pucallpa-uchunya` (a Cayman company,
  but financed through London's AIM, not by a development lender).
- **`spying-at-the-negotiating-table` → stays empty.** I searched all 1,182 ids and the full JSON of
  every case for espionage, intelligence, surveillance, bugging, Timor Sea and Greater Sunrise.
  There is no case about spying of any kind on this map. The only Timor-Leste case is roadside
  demolitions on a road project; Brazil has no Petrobras case. The field cannot be filled until the
  map has such a case; the obvious one to research is the 2004 bugging of Timor-Leste's cabinet,
  which the story already tells.
- **`banks-that-bank-the-looters` → stays empty.** No case shows a Western bank holding money stolen
  from a poor country's public. The two nearest: `bnp-paribas-sudan-letters-of-credit` is a Western
  bank's guilty plea, but for sanctions breaches over letters of credit, not for holding stolen
  money; `mozambique-bank-privatisations` has a KPMG audit finding management looted more than $40
  million, but from a domestic bank sold under a lender-backed privatisation. Neither is plainly the
  same shape.
- **`debt-for-nature-deals` → stays empty.** I listed all 19 Ecuador cases and the single Belize
  case and searched every case for swap, conservation fund, Galápagos and debt-for-nature. Nothing
  matches a swap that moves decisions over a country's waters or forests into a fund outside its
  government. The nearest Ecuador cases are a debt audit and a bondholder payment; the Belize case
  is about market vendors.

## Routes

**Served:** `documents1.worldbank.org` (the Jabotabek completion report as `.txt`, and the Chad
DSA); `thedocs.worldbank.org` (the WilmerHale report); `kenyalaw.org/search/api/documents/` (JSON,
both citations); `global-prod.acquia.undp.org` (the UNDP brief PDF); `your.fitch.group` (Fitch's own
Frontier Markets Quarterly PDF); `hsgac.senate.gov` (the Senate Riggs report PDF);
`irp.fas.org` (the Congressional Record item); `csmonitor.com`;
`journal.probeinternational.org`; `wealthbriefing.com`; `history.state.gov`.

**Refused or empty, recorded and not worked around:**

- `www.fitchratings.com/research/sovereigns/fitch-downgrades-ethiopia-to-ccc-09-02-2021` — HTTP 200
  but a script-built body of about 620 characters, navigation only. Same for its search page. So the
  rating action commentary itself was not opened; Fitch's own quarterly newsletter was used instead.
- `kenyalaw.org` judgment document pages — walled, as REVIEW42 and the checker said. The search API
  answers; the documents do not. No attempt was made to get past it.
- `documents1.worldbank.org/.../text/multi-page.txt` answers 301 to `/txt/`; it serves if you follow
  redirects.
- Not retried, on the checker's record that they are walled for everyone: `imf.org` (403, so IMF
  Country Report 17/246 behind Chad's 2016 oil-revenue figures is still unopened),
  `publications.parliament.uk` (403, and no longer needed),
  `webarchive.nationalarchives.gov.uk` (405, the FSA's own 2001 release), `spglobal.com`,
  `moodys.com`.
- `sec.gov/Archives` was not needed in this round and was not touched; it wants a contact address in
  the User-Agent and I did not invent one.

Nothing was fabricated, nothing was softened to keep it on a card, and no document was cited that I
did not open myself in this round.
