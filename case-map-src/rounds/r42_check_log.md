# Round 42, checker's log

A fourth agent, not one of the three reviewers, testing the verdicts that would change the page.
Nineteen of the thirty-one entries were tested: the six `documented`, the four `duplicate`, the five
`suspected`, and four `overclaimed` of my own choosing. The other twelve `overclaimed` verdicts are
recorded in `r42_checked.json` as `not_tested` with `agree: null` — unchecked, not endorsed.
Data: `rounds/r42_checked.json`. `base.html` was read only; nothing was rewritten, built or committed.

The three reviewers' verdict counts add up as the brief said: 6 documented, 16 overclaimed,
5 suspected, 4 duplicate. **The brief's premise that `r42_b_report.md` is missing is wrong** — the
file exists, is 8,954 bytes, carries a verdict table, the four flagged cases, two least-sure calls,
three source defects and a routes section. Not a defect.

## Verdicts

| id | reviewer | mine | agree | the short reason |
| --- | --- | --- | --- | --- |
| `rankings-bent-for-money` | documented | documented | yes | WilmerHale opened in full; bending settled across two editions, money motive firm for China and "likely" for Saudi Arabia |
| `private-equity-with-development-money` | documented | documented | yes | ICAI opened; the channel is uncontested — but the title asserts nothing a reader could doubt |
| `companies-pay-armed-groups` | documented | documented | yes | DOJ release confirmed figure by figure; EDGAR index shows Freeport's disclosure in nine consecutive 10-Ks |
| `water-handed-to-companies` | documented | documented | yes, conditionally | IEG's 13%/70/46 verified verbatim; the title holds as a programme, not per city |
| `secret-loans-banks-traders` | documented | documented | yes | FCA notice and the Bank's "Hidden Debt" box both verified; three sovereigns, two kinds of arranger |
| `ratings-that-punish-relief` | documented | documented | yes, weakest of six | no agency notice opened by anyone; counter-evidence on bilateral-only relief is missing from the entry |
| `vulture-funds` | duplicate | duplicate | yes | pattern carries the ECB core; leftover is the poor-country cut, Donegal, Libertad, the UK and Belgian statutes |
| `bondholders-block-debt-relief` | duplicate | duplicate | yes | duplicate on the core, but the pattern does **not** carry the $42.5m missed payment as the reviewer says |
| `development-money-through-tax-havens` | duplicate | duplicate | yes on the duplicate, **no** on the leftover | the IFC count is not documented on what was opened — see below |
| `private-courts-for-investors` | duplicate | duplicate | yes | title asserts nothing open; the open part (arbitrator club, chill) is contested and unmeasured |
| `aid-cover-for-spies` | suspected | suspected | yes | correctly scoped; the Wikipedia leg is a standing unfixed defect |
| `ports-that-become-naval-bases` | suspected | suspected | yes | title hedged, record hedged, conviction matches |
| `pension-funds-buy-up-farmland` | suspected | suspected | yes | conviction honestly says "preliminary"; least examined of the five (no document opened) |
| `lenders-expect-the-riots` | suspected | suspected | yes | conviction matches; effect size still being re-estimated |
| `rescue-money-timed-for-elections` | suspected | suspected | yes | conviction does not lean on the academic result; the story does |
| `bribes-built-into-financed-contracts` | overclaimed | overclaimed | yes — narrower title concedes **too little** | FY2024 sanctions tables verified; the narrower claim is itself documented |
| `loans-cut-off-to-topple-governments` | overclaimed | overclaimed | yes — narrower title concedes **too much** | NSDM 93's own words and the Track II note verified; Chile's purpose is documented |
| `poor-countries-take-the-poison` | overclaimed | overclaimed | yes — narrower title concedes **too much** | "ends up in" drops the Amsterdam refusal, the $17,000 price and the Dutch concealment fine |
| `banks-that-bank-the-looters` | overclaimed | overclaimed | yes | "turned a blind eye" is the Senate's own heading and wording, verified twice in the report |

## The two the brief asked me to decide

**`water-handed-to-companies` — documented, but only read as a programme.** The IEG evaluation states
it in the Bank's own evaluators' words: "Thirteen percent of projects dealing with urban WSS aimed to
introduce PSP. Seventy of these projects have closed, and 46 had managed to involve the private
sector as planned", with the international private sector focusing on large and medium-size cities
while local firms took the rural work. That is a lender designing projects across its portfolio to
bring foreign operators into city water, which is what the title says if "the lenders' advice" means
the programme. It is not a per-city claim, and on the entry's own second city the Bank's document
says the opposite. So: `documented`, with the reviewer's fallback title the safer option if the owner
reads the title city by city.

**`companies-pay-armed-groups` — documented, and on firmer ground than the reviewer had.** Two guilty
pleas would be two instances. The thing that makes it a practice is Freeport: SEC full-text search
returns the phrase "support costs for government-provided security" in nine consecutive Freeport
10-Ks, FY2017 through FY2025, including the filing the reviewer cited. A payment practice restated in
every annual report for nine years and defended rather than denied is ordinary disclosed business,
not an exposed scandal. Two fixes first: the conviction line's "routinely" has nothing behind it, and
the DOJ release records that the AUC *demanded* the payments, that Castaño implied failure could bring
physical harm to Banadex personnel and property, and that Chiquita represented them as made under
threat of violence — none of which the entry gives, and HYP's fairness rule wants it.

## The tax-haven leftover: I disagree with the reviewer

Reviewer C says the leftover — the lenders' own portfolio, from Oxfam's count of IFC clients — "reads
as documented" and belongs beside the existing pattern. On what has been opened it does not meet
REVIEW42's bar. It is an advocacy group's count of IFC disclosures, known in this round through an
Oxfam press release and the Bretton Woods Project; the briefing itself opened for nobody. And the
claim carrying the weight — that the IFC disputed the reading rather than the numbers — is in neither
document: I read the Bretton Woods Project article in full and it carries no IFC response at all, only
Jim Yong Kim saying that moving state assets to tax havens "can have a tremendous negative effect on
our mission". The IFC investments dataset at `finances.worldbank.org` redirects to a script-built
page, so the count cannot yet be reproduced from the lender's own data. Keep the leftover attributed
to Oxfam, inside the existing pattern or as a suspicion; do not present it as established until the
count is rebuilt from IFC disclosures or an IFC reply is opened.

## Defects: confirmed, refuted, and one the brief did not list

**1. The "50 to 80 per cent" figure on `lending-to-known-thieves` — REFUTED.** The figure is
verifiable, in a source already in the entry's own list. The Wall Street Journal piece (Glenn R.
Simpson, 19 August 1998) mirrored at `archive.globalpolicy.org/socecon/bwi-wto/simpson.htm` says the
report cited "numerous reports of diversion of 50% to 80% of funds budgeted for project land
acquisition and resettlement assistance". The same page carries the 20-to-30 per cent estimate, the
"no reason to believe the rate of diversion is any smaller in bank projects" line, and a 25-per-cent
threshold for the worst ministries. Reviewer C's note that this mirror does not carry the 50-80 figure
is wrong. No page fix needed. The House of Commons appendix is still unreachable (403, Cloudflare
challenge, both hostnames) but is no longer needed for this figure.

**2. The half-sentence quotation on `water-handed-to-companies` — CONFIRMED.** The 1998 Jabotabek
completion report says the privatisation of PAM JAYA's operations was "parallel to but facilitated by
the Project, was not envisaged by GOI and the Bank at appraisal as private sector participation was
still a new concept at that time", and at paragraph 28 that "In the late 1980s, private sector
participation (PSP) ... was still a new concept for both GOI and the Bank; had GOI proposed a PSP
option, it would have most likely been turned down by the Bank, following other unsuccessful
experiences in Indonesia." The story takes the clause that helps and drops the clause in the same
sentence that cuts against. Fix needed whatever the verdict.

**3. The carbon-credits judgment is under appeal — CONFIRMED, with a date correction.** Kenya Law's
index gives the judgment as *Osman & 164 others v Northern Rangelands Trust & 8 others*, Petition
E006 of 2021, [2025] KEELC 99 (KLR), **24 January 2025** — not 31 January as the reviewer's report has
it; the entry's "In January 2025" is fine. The appeal is *Northern Rangelands Trust v Osman & 164
others*, Civil Appeal (Application) E019 of 2026, [2026] KECA 1774 (KLR), Court of Appeal, ruling
delivered **25 September 2026**, with NRT as appellant. There is also a 2 April 2025 ELC ruling in the
same petition. Judgment pages are walled (the search API answers, the documents do not), so I have
index metadata only and cannot say what the September 2026 ruling decided — in particular whether a
stay was granted. The story reads as though the ruling stands unchallenged; it needs a clause saying
an appeal is on foot, and should not claim more than the index supports.

**4. The WilmerHale countries omitted from `rankings-bent-for-money` — CONFIRMED, and there is a
second omission of the same kind.** The report's scope sentence names "China (Doing Business 2018) and
Saudi Arabia, the United Arab Emirates, and Azerbaijan (Doing Business 2020)". The story names only
China and Saudi Arabia. Azerbaijan is the one that breaks the money framing: its reforms were
"frozen" on Djankov's own disbelief, multiple employees said he "appeared to harbor a personal animus
against the country", and he then accelerated a methodology change after being told it would cut
Azerbaijan's score. The UAE change followed Saudi Arabia's mechanically and did not move its ranking.
The second omission, which no reviewer reported: the Saudi change's **first** stated consideration is
an instruction to find a way to drop **Jordan** from the Top Improvers list — a team member was sent
to Jordan, found its data correct, and the team then pivoted to boosting Saudi Arabia past it. The RAS
motive is one of three factors listed under a "likely" finding, not the single cause. The report also
records employees' concern that Doing Business RAS work "can lead to the impression of a pay-to-play
scheme" — an impression recorded, not a finding, and the entry should not harden it.

**5. The Senate figure on `banks-that-bank-the-looters` — PARTLY REFUTED.** Both readings are in the
report. The findings say the Equatorial Guinea relationship had "balances and outstanding loans that
together approached $700 million", which is the reviewer's point. But the executive summary separately
says "aggregate deposits ranging from $400 to $700 million at a time" — deposits alone. So the card's
"balances of up to $700 million" is supported; the fix is smaller than reported: give the range rather
than "up to". The reviewer's neighbouring points are confirmed — "turned a blind eye to evidence
suggesting the bank was handling the proceeds of foreign corruption" is the Subcommittee's own wording,
twice, and the plea was for failing to report suspicious transactions.

**6. Not on the brief's list, and the one I would fix first: `ratings-that-punish-relief`, "19 African
countries ... up to $74.5 billion".** Reviewer B reported it and I confirmed it against the UNDP
brief. The brief studies two samples — 13 African countries for domestic-currency bonds and 16 for
Eurobonds — and says "Combining the numbers from both tables, the full cost of credit rating
idiosyncrasies in Africa is estimated to be US$74.5 billion in excess interest and foregone funding".
No "19" appears, and $74.5 billion is a combined total, not an "up to". The entry's "more than the
continent receives in aid each year" is supported ("nearly 12% per cent more than all of Africa's net
official development assistance in 2020"). The wrong figure is in the story **and** in the conviction
line, so both need changing before either is used again.

Two further story-level notes found in passing, for whoever rewrites:
`ratings-that-punish-relief` omits the counter-evidence in the Oxfam brief — Moody's said DSSI relief
on bilateral debt could ease funding pressures and possibly help ratings, and Fitch and S&P supported
countries joining to the extent it applied only to bilateral debt; the punishment attaches to
private-creditor involvement, which is narrower and more interesting than the title.
`loans-cut-off-to-topple-governments` omits the counter-evidence in its own primary: the Senate report
records that the IMF extended Chile about $90 million during 1971 and 1972.

## What is safe to move, and what needs work first

**Nothing should move without an edit.** In order of readiness:

- **`secret-loans-banks-traders`** — closest to safe. Both load-bearing documents verified against
  their own words. Change needed: drop "routine" from the conviction, and do not lean the
  banks-and-traders claim on the Bank's hidden-debt box alone, which names an arranger type only for
  Congo.
- **`companies-pay-armed-groups`** — safe once "routinely" goes from the conviction and the Chiquita
  paragraph carries that the payments were demanded under threat. The Freeport nine-year 10-K series
  should be in the sources; it is the strongest leg and is not there.
- **`rankings-bent-for-money`** — safe once the story carries the UAE and Azerbaijan, the Jordan
  instruction, and the Saudi motive as a "likely" finding among several factors. As written it
  presents a four-country, two-motive investigation as a two-country money story.
- **`bribes-built-into-financed-contracts`** — not one of the six, but the clearest graduation
  candidate on the page: graduate under the reviewer's narrower title rather than keep as a suspicion.

**Needs work before it can move:**

- **`water-handed-to-companies`** — fix the half-quote first; then decide whether the title is read as
  a programme (documented) or city by city (overclaimed). The Cochabamba loan condition still rests on
  an advocacy source.
- **`ratings-that-punish-relief`** — the $74.5bn figure is wrong in two places, the counter-evidence
  is missing, and no agency's own notice has been opened by anyone. Open Fitch's 9 February 2021 action
  commentary before promoting.
- **`private-equity-with-development-money`** — documented on the test as written, but the title
  asserts a channel nobody disputes. Promoting it as written would put a dry pattern on the page while
  the story's actual claims stay open; better retitled around something contested.

**The four duplicates are merges, not promotions.** `vulture-funds` into `holdout-funds-rich-courts`
keeping the poor-country count, Donegal, Libertad and the UK and Belgian statutes.
`bondholders-block-debt-relief` into `who-owns-the-debt`, but someone must first open a document that
states the $12.9 billion and the single private creditor — both World Bank DSSI pages load their
figures by script. `development-money-through-tax-havens` into `offshore-routing-lost-tax` with the IFC
count attributed to Oxfam, not presented as established. `private-courts-for-investors` into
`company-sued-the-state`, which the Reko Diq and Occidental awards widen past privatised services; if
anything stays as a suspicion it must be retitled to assert the arbitrator concentration or the
regulatory chill, which are the only open parts.

**The five suspected stay where they are.** All five are correctly scoped and their conviction lines
match the record. Two process notes: `pension-funds-buy-up-farmland` and
`bondholders-block-debt-relief` were classified with no document opened at all, and
`aid-cover-for-spies` still rests on Wikipedia for a paragraph where a Congressional Record source is
already in its own list — a defect first reported on 15 November 2026 and still unfixed.

## Routes

Served: `thedocs.worldbank.org`, `documents1.worldbank.org`, `icai.independent.gov.uk`,
`justice.gov/archive`, `fca.org.uk`, `hsgac.senate.gov`, `intelligence.senate.gov`, `au.int`,
`global-prod.acquia.undp.org`, `worldbank.org/content/dam`, `archive.globalpolicy.org`,
`brettonwoodsproject.org`, `oxfamitalia.org`, `efts.sec.gov` (EDGAR full-text search API),
`kenyalaw.org/search/api/documents/` (JSON, as REVIEW42 said).

Refused, recorded and not worked around: `sec.gov/Archives` (403, "Your Request Originates from an
Undeclared Automated Tool" — SEC wants a contact address in the User-Agent and I did not invent one,
so the Freeport 10-K body was read only through the EDGAR search index, not the filing);
WebFetch on the same filing returned PROVENANCE_REQUIRED; `publications.parliament.uk` (403,
Cloudflare, both hostnames); `new.kenyalaw.org` search API (301); Kenya Law judgment pages (walled,
index only); `finances.worldbank.org` (302 to `financesone.worldbank.org`, which serves a script-built
page, so the IFC investment dataset could not be queried); `policy-practice.oxfam.org` (404);
`african-markets.com` (site in maintenance behind a challenge);
`applications.byblosbank.com` (TLS verification failed — not disabled, request abandoned);
`fitchratings.com` and `spglobal.com` (walled for all three reviewers, not retried).
