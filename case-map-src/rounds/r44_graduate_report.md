# Round 44: graduations and merges

Data: `rounds/r44_graduate.json`. `base.html` was read only; nothing was rewritten, built or committed.

Five of the six moved, not six. Four merges written. One recommended to stay a suspicion, with reasons.

## Job A: five graduated, one held back

Each new pattern carries only the fields the thirteen live patterns all carry - `id`, `title`, `kind`,
`years`, `summary`, `implications`, `countries`, `timeline` - plus `confirmed_by` (the sources, which
`detailPattern` renders as the card's source list and which every live pattern has), `case_ids`,
`claims_per_author` where a load-bearing claim comes from one advocacy or interested source, and
`uncertain` for the caveats. No `computed`, no `counts`, no `method`, no `links`: nothing was invented
to fill a shape, and `links` would have needed coordinates nobody has established.

| HYPS entry | new pattern | what the pattern asserts |
| --- | --- | --- |
| `rankings-bent-for-money` | `doing-business-data-changed` | The Bank's own commissioned investigation found data changed for four countries in two editions, two of them raised for countries whose money or support the Bank needed, one cut on an official's private view |
| `secret-loans-banks-traders` | `hidden-loans-banks-traders` | A regulator's final notice, the Bank's own box naming three IDA countries with hidden debt, and named banks and traders in Mozambique, Congo, Chad and Greece |
| `companies-pay-armed-groups` | `payments-to-armed-forces-abroad` | Two guilty pleas for payments demanded under threat, one army payroll out of company records, and one company's nine consecutive annual disclosures |
| `water-handed-to-companies` | `city-water-into-private-hands` | The Bank's evaluators' own portfolio count: 13% of urban water projects aimed to bring private operators in, 46 of 70 closed projects managed it |
| `private-equity-with-development-money` | `for-profit-health-who-it-reached` | Retitled: the lenders' own papers did not ask who the money would reach, and where it was asked the answer was better-off patients |

The three carry conditions were met:

- **`companies-pay-armed-groups`.** "Routinely" is gone from the conviction, replaced by what is
  established plus the reason no count exists. The threat is on the record in both the pattern and
  the HYPS story: the Justice Department's release says the payments began after Carlos Castano
  implied to a Banadex executive that failure to pay could bring physical harm to Banadex personnel
  and property, and that Chiquita "represented that the payments had been made under threat of
  violence". I fetched that release myself and read it in full; it also carries the outside counsel's
  advice that the company could not do indirectly what it could not do directly, that a duress
  defence weakens with repetition, and that it should leave Colombia - which is why the threat does
  not excuse the payments, and both halves are now on the card. The Freeport series is in the
  sources: I ran the EDGAR full-text query myself and got nine hits, every one a Freeport-McMoRan
  10-K (CIK 0000831259) for financial years 2017 to 2025, filed February 2018 to February 2026. The
  pattern says plainly that this is the SEC's index and not the filings (sec.gov/Archives refuses a
  client with no contact address, and none was invented), so no amount disclosed inside those filings
  is given, and `uncertain` records that the index does not reach filings before 2001.
- **`secret-loans-banks-traders`.** "Routine" is gone from the conviction. The banks-and-traders
  claim rests on named firms in named countries - Credit Suisse and VTB in Mozambique, Glencore and
  Trafigura in Congo, Glencore in Chad, Goldman Sachs in Greece - and the pattern says in its own
  text that of the three sovereigns in the Bank's hidden-debt box only Congo's entry names a type of
  arranger and Togo's names none. I opened the Bank's 4 October 2018 board paper and the FCA final
  notice myself and verified both passages verbatim, including the 147,190,200 pound penalty.
- **`water-handed-to-companies`.** Graduated only at the portfolio level, and the title says so. I
  opened the 2010 Independent Evaluation Group evaluation myself and verified the 13%/70/46 sentence,
  the list of the 24 projects that did not manage it (Bolivia cancelled all its contracts), and the
  split where international firms take large and medium-size cities. The pattern also carries the
  counter-evidence I found in the same chapter - the evaluators write that the formal private sector
  "has not played the investment role that had been hoped for" and that public providers remain the
  norm - and the Jakarta clause that cuts against the story, as round 43 fixed it. The Cochabamba
  loan condition stays where it belongs: in `claims_per_author`, attributed to the Democracy Center,
  with a note that no Bank document stating it has been opened.

### `private-equity-with-development-money`: retitled, not promoted as written

The checker was right that the old title asserts a channel nobody disputes, and the document makes it
worse than that: I opened the ICAI review and its own framing of the fund channel runs the other way
- "only 17% through funds" between 2012 and late 2017, a fall, as CDC moved to direct equity and
debt. So the channel is not just uncontested, it is shrinking.

What is contested in the same document is whether anyone checked who the money reached. ICAI reports
that the investment committee papers for more than three-quarters of its sample did not consider
which socio-economic groups would benefit, and its worked example is a health investment: the papers
for an Indian healthcare fund argued the fund would improve affordability without considering who
would benefit, and CDC later told ICAI that the commitment to target half low-income households was
"an ambition rather than a requirement" and that the funded services had largely reached those on
above-average incomes. That is a statutory scrutiny body's finding, the institution's own admission,
and a claim the institutions answer in substance (the IFC says private providers add capacity). So
the new title is **"Money for health put into for-profit care without checking who it reached"**, and
the HYPS title is edited to match. Oxfam's hospital findings sit in `claims_per_author`, attributed,
with the companies' replies; Abraaj is in as what the same absence of checking looks like at fund
level.

### `ratings-that-punish-relief`: recommended to stay a suspicion

My call, and it is a close one. Round 43 did open an agency document in its own voice, which the
round 42 checker did not have: Fitch's *Frontier Markets Quarterly - 1Q21*, which lists "Ethiopia CCC
09-Feb-2021 Downgrade" in its own rating-action table and says the downgrade was triggered by
Ethiopia's intention to use the Common Framework, which raises the possibility of restructuring
private-sector debt that would qualify as a distressed debt exchange, unlike the earlier payment
suspension scheme. The narrowed claim - the trigger is private-creditor involvement, not asking for
relief - is close to verbatim in the agency's own publication.

I still would not put it on the page as documented, for three reasons. It is one agency, one country,
one action: Moody's and S&P notices remain unopened, and the Moody's review of Pakistan is known only
through a footnote in an Oxfam brief. The document is a quarterly summary, not the action commentary,
so it could omit a second reason. And the counter-evidence in the Oxfam brief - Moody's saying
bilateral-only relief could ease funding pressures and possibly help ratings, Fitch and S&P
supporting participation to the extent it stayed bilateral - is still not on the card, and the
checker made carrying it a condition of any move. A pattern resting on one agency's summary of one
downgrade would be the thinnest thing in `PATS`.

What I did instead: a title edit, narrowing the suspicion to what the Fitch document supports -
**"Credit ratings cut when debt relief would reach private lenders"** - so the title stops asserting
more than the conviction line already concedes. I did **not** write the counter-evidence into the
story, because the Oxfam *Passing the Buck on Debt Relief* brief is not in the entry's source list
and the `hyps_edits` shape this round has no way to add a source. That is one round-43-style fix,
clearly specified, left for whoever runs the next text pass: add the brief, then add the Moody's,
Fitch and S&P bilateral-relief sentences to paragraph 1. After that, and with one agency notice for a
second country, it can graduate.

## Job B: four merges

Each merge adds only the leftover, as the checker listed it.

- **`vulture-funds` into `holdout-funds-rich-courts`.** Added: the UN independent expert's 2010 report
  of 54 commercial-creditor cases against 12 heavily indebted poor countries, 1998-2008; Donegal
  International's purchase of Zambia's Romanian debt for about $3.2 million against a $29.8 million
  principal, the 2005 London suit for more than $55 million and the about $15.5 million Zambia paid
  in 2007 while receiving relief, with the judge's finding on Donegal's witnesses; the ARA Libertad
  held at Tema from 2 October 2012 and released in December after the ITLOS order; and the UK's 2010
  Act and Belgium's 2015 law, which NML Capital challenged and the Belgian Constitutional Court
  upheld. Countries appended: Zambia, Ghana, Belgium. The pattern's `uncertain` line said UK law
  limits "are not covered here", which the merge makes false, so that clause is edited.
- **`bondholders-block-debt-relief` into `who-owns-the-debt`.** The condition held: I searched the
  pattern and Zambia's missed $42.5 million payment is genuinely not there, so it is part of the
  leftover and is added, with the 13 November 2020 default and the 2021 budget comparison, the 2024
  bondholder deal, and Debt Justice's five-country $20-to-$30-billion estimate. **I did not write the
  $12.9 billion or the single private creditor.** Both World Bank DSSI pages still load their figures
  by script and imf.org refused the IMF paper (403). What I did open is Debt Justice's October 2021
  briefing, which is a better document for the leftover and which nobody in rounds 42 or 43 had: for
  the 46 countries that applied, 23% of external payments suspended between May 2020 and June 2021,
  $10.3 billion suspended and $0.6 billion cancelled against $36.4 billion still paid; other
  governments suspending 48%, multilaterals cancelling 5%, private lenders 0.2% - which it identifies
  as one Italian bank suspending payments by Zambia; private creditors receiving $14.9 billion, more
  than any other group; UK commercial lenders suspending nothing and receiving $3.2 billion; China
  suspending $5.7 billion. It is attributed to Debt Justice in `claims_per_author` and the summary
  says it is their reading of the IMF report and the Bank's database, with their own caveats about
  rounding, withheld creditor names and anticipated amounts in `uncertain`.
- **`development-money-through-tax-havens` into `offshore-routing-lost-tax`.** The count is
  attributed to Oxfam, in the summary text and in `claims_per_author`. Oxfam's briefing itself still
  would not open (oxfam.org.au 403, the library and CDN hosts empty or 403), so the figures come from
  two documents I did open: Oxfam's own press release (51 of 68 companies, 84% of IFC investment in
  the region in 2015, $1.20 billion in 2010 rising to $2.87 billion in 2015) and the Bretton Woods
  Project's report, which also carries Jim Yong Kim's statement. **I did not write that the IFC
  disputed the reading rather than the numbers.** It is in neither document; the Bretton Woods
  Project article carries no IFC response, and `uncertain` now says so plainly and records that the
  IFC dataset redirects to a script-built page, so the count cannot be rebuilt from the lender's own
  data.
- **`private-courts-for-investors` into `company-sued-the-state`.** Occidental is already in that
  pattern, in the summary and in Ecuador's country note, so the only real leftover is Reko Diq: the
  12 July 2019 award of $5.976 billion against Pakistan, its composition, the comparison with the $6
  billion IMF loan, the two figures for what the company had spent, and the 2022 settlement. Pakistan
  appended to countries. I did **not** add the 1,332-case count, which the checker named as a
  widener: it is nowhere in the entry's story, so writing it would need the UNCTAD note opened, and
  this round did not open it. The pattern's `claims_table` and `totals` count only treaty claims tied
  to cases on this map, so Reko Diq stays out of both, and `uncertain` now says so.

### What I recommend for the four HYPS entries

All four get `status: "documented"` and `graduated_to` the pattern that absorbed them, which is what
rule 6 gives for a confirmed suspicion and is the honest record: the core is documented and it now
lives in a pattern.

For `private-courts-for-investors` I recommend **no retitled survivor**. The only open parts are the
arbitrator concentration and the regulatory chill. The 15-arbitrators-55% figure is a 2012 advocacy
count whose published rebuttal is already in the entry's own source list, and the chill is unmeasured
by anyone - the entry says so itself. A suspicion has to be built from a record someone has opened,
and in two rounds nobody has opened that report. If the owner wants a survivor, it should be written
fresh in a later round, titled around the concentration ("A small group of arbitrators decides most
investor-state cases") and only after the 2012 count is re-verified from the report itself and the
Kluwer rebuttal is carried in the same paragraph. Keeping the present entry and renaming it would
leave a card whose story is about Reko Diq and Occidental under a title about arbitrators.

## Two things for whoever merges this

1. **A documented HYPS entry still renders as a suspicion.** `hypsHTML()` excludes `status ===
   "documented"` from the count only; the list maps every entry, and `detailHyp()` always prints the
   "Suspected pattern - not documented" kicker and the dashed box. Merge this file as it stands and
   nine entries will sit under "Suspected patterns" with a dashed "not documented" box while their
   content is on the page as documented patterns. Either filter the list and the card on `status`, or
   have `detailHyp` show a line pointing at `graduated_to`. That is a `base.html` change and this
   round did not touch `base.html`.
2. **`pats_edits` uses `append_to` for three arrays, not one.** The brief's shape named
   `countries`; sources and attributed claims also have to go somewhere, so there are
   `append_to: "confirmed_by"` and `append_to: "claims_per_author"` entries as well, in the same
   `{id, append_to, value}` form. An unsourced addition would be worse than an extra operation. `merge_pats.py`, written for this round by
   another agent while I was working, accepts `append_to` on any list field, so one
   `append_to: "case_ids"` operation is also in the file: it moves
   `amulsar-gndevaz-jermuk` from `development-money-through-tax-havens` to
   `offshore-routing-lost-tax`, which carried only `mopani-mufulira`. Every `old` string in the file was checked
   against the live `window.PATS` and `window.HYPS`: 36 pattern edits and 6 entry edits, each
   matching exactly once.

## My weakest call, named

**Graduating `city-water-into-private-hands`.** The title is defensible only as a statement about a
programme, and the evidence for it is a single sentence in one 2010 evaluation - 13% of projects
aimed to introduce private sector participation, 46 of 70 closed projects managed it. Read city by
city the pattern fails on its own second case, because the Bank's completion report says Jakarta's
privatisation was neither envisaged nor wanted by the Bank and would probably have been refused a
decade earlier. I carried that clause into the pattern and put the limits in `uncertain`, but a reader
who takes the title as a claim about each city will be misled, and the strongest single city claim -
Cochabamba's conditioned loan - still rests on an advocacy source. If the owner reads the title that
way, this one should come back down.

Second weakest: the retitle of `private-equity-with-development-money`. The new title is better
supported than the old one, but it rests on one scrutiny body's review of one institution's sample;
no equivalent audit of the other four lenders' investment papers has been opened.

## Routes

Served: `efts.sec.gov` (EDGAR full-text search API), `justice.gov/archive`, `fca.org.uk`,
`documents1.worldbank.org` (both the 2010 IEG evaluation and the 2018 board paper),
`icai.independent.gov.uk`, `debtjustice.org.uk` (PDF), `brettonwoodsproject.org`, `oxfam.ca`.

Refused, recorded, not worked around: `sec.gov/Archives` (refuses a client with no contact address;
none was invented, so the Freeport filings were confirmed through the search index only);
`imf.org` (403 on both the policy-paper page and the media PDF path, so the IMF's September 2021 DSSI
report was not opened and its $10.3 billion figure is given as Debt Justice's reading);
`oxfam.org.au` (403), `oxfamilibrary.openrepository.com` (empty body), `www-cdn.oxfam.org` (403), so
Oxfam's IFC briefing remains unopened; `search.worldbank.org/api/v3/wds` answers but returns nothing
for the DSSI figure queries; `fitchratings.com` action commentaries and Moody's and S&P notices were
not retried, on the record of four earlier agents.
