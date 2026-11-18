# Round 44, checker's log: graduations and merges

A separate agent from the writer. Data: `rounds/r44_graduate_checked.json` — the writer's object with
my corrections applied and a top-level `check` block per new pattern and per merge target.
`base.html` was read only; nothing was rewritten, built or committed.

Thirty corrections applied across the five new patterns and the four merges. Nothing cut.

**Three things moved under me during this pass, all at 19:12.** They change two of my findings and
I have re-run the affected checks rather than leave the earlier version standing.

- `r44_graduate_report.md` did not exist when I was dispatched and I worked without it. The writer
  wrote it at 19:12, along with a thirty-seventh `pats_edits` operation (`offshore-routing-lost-tax`
  gaining the case id `amulsar-gndevaz-jermuk`). I read both afterwards. The report is candid and it
  names the right weakest call. One of its own figures is now out of date: it says 36 pattern edits,
  and there are 37, the last carrying no `old` string.
- **The rendering fault is already fixed in `base.html`.** When I read `hypsHTML()` it filtered on
  `status` for its count and not for its list, and `detailHyp()` always printed the "not documented"
  kicker; that was my blocking finding, and the writer had found it independently. A commit at
  19:12 fixed it: the list now filters on `status !== "documented"`, `detailHyp()` returns early for
  an entry with `status: "documented"` and `graduated_to` and renders a button to the pattern
  instead, and the heading comment records why. I re-read both functions in the current file. The
  finding stands as history, not as a blocker, and section 7 is rewritten accordingly.
- **The same commit changed four `HYPS` entries**, two of them the cards that feed graduations. I
  re-extracted `window.PATS` and `window.HYPS` from the new file and re-ran every string match:
  all 37 `pats_edits` and all 10 `hyps_edits` still match exactly once. It also caught one defect in
  the suspicion card that is also in this pattern, which I have now fixed here too — see the Jordan
  instruction below. That commit also snapshotted my then-unfinished `r44_graduate_checked.json`; the
  file as it now stands is the finished one, and I committed nothing myself.

## 1. The five new patterns

All five hold. All five needed corrections. None has a `counts` or `computed` block, and none was
invented to fill a shape: of the thirteen live patterns, `money-kept-flowing` has a `counts` block
and `companies-come-from` a `computed` one, and the five new entries have neither. Every `case_id`
in them exists in `window.CASES`. Every `iso3` appended to a merge target is new to that pattern, so
no country entry is duplicated.

**`doing-business-data-changed`** — stands with four corrections. I opened the WilmerHale report at
the Bank's own copy and read it against every claim in the entry. The four-country scope, China's
seven places to 78th during the capital increase, the two kinds of pressure, the September 2019
instruction to drop Jordan, the employee sent to Jordan, the pivot to Saudi Arabia, the finding
worded as likely with its three factors, the UAE change made because the tax systems were similar
and not moving its ranking, Azerbaijan's frozen reforms and the personal animus, and the absence of
any evidence that the president's office or the board was involved in the 2020 changes: all verified
in the report's own words. What I changed:

- the entry said three reforms *its own internal audit had confirmed* were left uncounted. The report
  says the audit confirmed the large majority of Azerbaijan's reforms, and that three topics were
  frozen anyway. The suspicion card already puts it that way; the pattern had made it stronger, which
  at a graduation is where it costs most. Reworded to the report's own account.
- the pay-to-play sentence was attributed to employees. It is the investigators' own analysis of the
  risks of paid advisory work, written after they record that numerous employees raised concerns
  about the Bank's financial interest in those contracts. Reattributed, and still marked as a risk the
  report describes rather than a finding, which is what round 42 asked.
- "a panel the Bank set up in 2013 recommended removing it permanently" rests on a trade union
  federation page that refuses automated requests, and nobody has opened it in this round. I replaced
  it with what two pages I did open support: the Bretton Woods Project's 2009 article (the April 2009
  decision, the criticism from trade unions and the Bank's own evaluation unit, and the IFC's
  statement that it would now reward worker protections, which is the record that the old system did
  the opposite) and the Congressional Research Service report already in the sources, which states
  that pressure from Congress and the ILO led to the suspension. I added the Bretton Woods Project's
  July 2014 article, which I opened, for the panel's June 2013 review and the complaint that its
  recommendations went unimplemented — counter-evidence the entry did not have — and repointed the
  2013 timeline entry at it.
- `uncertain` now records that the two senior Middle East and North Africa officials whom Djankov
  named as the impetus for the Saudi change both denied suggesting that Jordan be displaced. HYP's
  fairness rule wants the denial, and it was missing.
- the Jordan instruction read "find a way to drop Jordan from the top of the draft Top Improvers
  list". The report says he "instructed the Doing Business team to find a way to alter the data such
  that Jordan fell from its first-place position". Altering the data is the whole of it; the shorter
  form reads as a ranking decision rather than a data change. Corrected in the summary and in the
  2019 timeline entry. A checker working in parallel caught the same thing on the suspicion card at
  19:12, which is the strongest confirmation of it I could have.

**`hidden-loans-banks-traders`** — stands with one cut. Round 42's two conditions are met and I
verified both. "Routine" is gone: the only occurrences of "routine" and "routinely" anywhere in the
delivery are inside `old` strings being replaced. The banks-and-traders claim does not rest on the
Bank's hidden-debt box: it rests on named firms in named countries, and the entry says in its own
summary and again in `uncertain` that of the three sovereigns in the box only Congo's entry names a
type of arranger and Togo's names none. I opened the FCA final notice of 19 October 2021 and the
Bank's 4 October 2018 board paper and verified both passages word for word, including the
147,190,200 pound penalty and the quoted finding about informing the IMF.

The cut: the entry said the July 2019 Chad debt sustainability analysis records that in 2016 $231
million of the government's $271 million in net oil revenue went to Glencore. I opened that document's
full text and searched it: no 231, no 271, no 85 per cent of net oil revenue, anywhere in it. The 98
per cent of commercial debt stock is there, in footnote 2, and carries the same point, so the figures
are cut from the summary and from the Chad country note rather than carried on a document that does
not hold them. The IMF country report on Chad, where the figure may sit and which is in the suspicion
card's own source list, refuses automated requests (403 over curl and over WebFetch; no contact
address was invented). **The suspicion card makes the same misattribution**, and that is now recorded
in `uncertain` as a card defect for the next text pass.

**`payments-to-armed-forces-abroad`** — stands with three corrections, and it is the best-evidenced
of the five. All three of round 42's conditions are met, and I checked each myself rather than taking
the writer's word:

- "routinely" is gone from the conviction line;
- the payments being demanded under threat is in the pattern's summary and in the story edit to the
  suspicion card, in the Justice Department's own terms — Castano implying physical harm to Banadex
  personnel and property, and Chiquita representing that the payments were made under threat of
  violence — and, importantly, the other half is there too: counsel's advice that it could not do
  indirectly what it could not do directly, that a duress defence weakens with repetition, and that
  the company should leave Colombia. The threat is recorded without becoming an excuse;
- the nine-filing series is in `confirmed_by`, and I ran the query. The SEC full-text index returns
  total 9 for "support costs for government-provided security" in 10-K filings, every hit
  Freeport-McMoRan (CIK 0000831259), period endings 2017-12-31 through 2025-12-31, filed 20 February
  2018 through 13 February 2026 — including the 13 February 2026 filing the timeline names. The
  entry's claim is exact, and it says plainly that this is the index and not the filings.

I dropped "where the AUC was killing civilians" from the clause about Uraba and Santa Marta: the
release does not say it, and the 2024 jury verdict two sentences later carries the killings. I added
to `uncertain` that the Lafarge payment figures differ by source — about $6 million reaching the
groups against $10.24 million including intermediaries — which the Syrian plant's case card records
and the entry did not. And I repointed the two EDGAR links from the search API, which hands a reader
raw JSON, at the full-text search page that runs the same query.

**`city-water-into-private-hands`** — stands with five corrections, and it is the weakest of the five,
for the reason the writer names in its own report. I opened the 2010 evaluation and the 1998
completion report in full. The portfolio sentence is verbatim, the 24 breakdown is there, the
"has not played the investment role that had been hoped for" quotation is the evaluators' own, and
"international firms tend to ignore smaller, more remote towns" is theirs too. Round 42's confirmed
half-quote defect is fixed: both clauses of the Jakarta sentence and paragraph 28's "would have most
likely been turned down by the Bank" are in the pattern. What I changed:

- the entry accounted for only part of the twenty-four projects that did not bring private operators
  in, and dropped the six countries in the same sentence — Guinea, Jordan, Kosovo, Sierra Leone,
  Trinidad and Tobago, and the West Bank and Gaza — where the evaluation says private companies ran
  the services efficiently for several years and the contracts simply were not renewed. That is the
  same class of defect round 42 confirmed in this entry's Jakarta quotation, committed again a
  paragraph earlier. Restored, with a line in `uncertain` saying the twenty-four are not all failures
  of delivery.
- Cochabamba's "bills rose by more than half on average" is attributed to the Democracy Center, and
  Bechtel's own figure added — an average rise of 35 per cent, about half of it to meet requirements
  the government had set — which the case card carries and the pattern did not.
- "soldiers shot dead a 17-year-old" is softened to what the case card records: Daza was shot dead,
  the army captain filmed firing live rounds was acquitted by a military court, and the US State
  Department said at least three of the four civilians killed that month were likely killed by
  security forces. The wounded figures are brought to the card's own numbers and months.
- Jakarta's "35, 40 and 30 per cent in three years" is corrected to the card's years: 2001, 2003, 2004.
- `uncertain` now carries the claim-amount divergence the card records ($25 million on PBS's account,
  at least $50 million on the Democracy Center's).

**`for-profit-health-who-it-reached`** — stands with five corrections. On the question I was asked:
**the retitle fixes the near-tautology.** The old title asserted a channel nobody disputes. The new
one asserts a failure of checking, and that is a finding, in a statutory scrutiny body's own words,
which the institutions answer in substance. I opened the Independent Commission for Aid Impact's
March 2019 review in full: paragraph 4.91 says the investment committee papers "for more than
three-quarters of our sample did not consider this issue", its worked example is a health investment,
and CDC told the commission that the fund's commitment to target half low-income households "was an
ambition rather than a requirement" and that the funded services "have largely reached those on
above-average incomes". Figure 12 gives health at 6 per cent of the portfolio in 2011 and 7 per cent,
258.8 million pounds, in 2017, and the 61/22/17 split is there. Every figure in the entry's first
paragraph is verified. This is not a pattern going up dry.

But its one cross-institution claim was wrong, and I opened Oxfam's report to find it:

- the 358 investments are those of **four European** development finance institutions — BII, DEG,
  Proparco and the European Investment Bank — made between 2010 and 2022. The World Bank Group is not
  one of the four. The entry said five institutions including the World Bank. Corrected in the
  summary, the implications and `claims_per_author`, keeping that several of the hospitals examined
  had World Bank Group money as well (Oxfam records CARE Hospitals as funded by BII, Proparco and the
  World Bank, and Hygeia as having had at least eleven investments from DEG, EIB, Proparco and the
  IFC). This is the "study scope misstated" class HYP.md records from round 28.
- "kept one woman's mother's body for two years": the report says bodies of people who had died were
  held for up to two years, and gives at least three months for the newborn and eleven for the
  schoolboy. The maximum had been attached to one named family. Corrected.
- "more than nine years' income": the report says nine years. That is the "a source's 'around' turned
  into 'more than'" class from the 15 November check. Corrected, with the report's figure for the
  poorest half added.
- "could not find a single disclosed evaluation": scoped to the four institutions, and the report's
  own partial exception restored — a 2017 case study of a Narayana Health facility, done as a pilot
  for the British institution's impact framework, whose authors found little evidence available to
  understand the real impact.
- `uncertain` now carries the commission's more positive examples from the same paragraph: a Kenyan
  fund aiming at firms serving people in informal settlements, and India and Nigeria funds backing
  firms that buy from smallholders.

Because all four Oxfam errors are also on the suspicion card, which round 43 did not touch, I added
four `hyps_edits` story corrections to the card itself, so the page does not keep the wrong version
under a "not documented" box.

## 2. The three conditions round 42 set

Verified myself, not taken from the writer: **`payments-to-armed-forces-abroad`** — "routinely"
dropped, the threat recorded, the nine filings in the sources and independently reproduced from the
SEC index. **`hidden-loans-banks-traders`** — "routine" dropped, and the banks-and-traders claim
rests on named firms, with the limits of the Bank's box stated twice in the entry's own text. Both
conditions met in full.

## 3. `ratings-that-punish-relief` left as a suspicion

The right answer, and I would leave it there. The writer's reasoning is sound and I add one point in
its favour: the entry is in much better shape than round 42 described, because round 43's fixes are
live. The $74.5 billion is now correctly given as a combination of two tables covering 13 and 16
countries, the entry says in its own words that the brief attaches no country count to the total, the
Fofack figure is correctly attributed, and UNDP's own alternative explanation — that the costs could
come from thin data and subjective methods rather than conscious bias — is in the story.

What has not changed is the thing that matters for a graduation: the mechanism the title now names
rests on a single document, Fitch's quarterly review of frontier markets, which is the agency's own
publication but is a market summary rather than the commentary for the action. Moody's reason is
known through a wire report and S&P's through nothing. No agency's own notice has been opened by
anyone across five agents. One agency, one country, one action, through a newsletter, is not enough
to take the dashed box off — and the counter-evidence round 42 found in the Oxfam brief (Moody's
saying bilateral-only relief could ease funding pressures, Fitch and S&P supporting participation to
that extent) is still not on the card.

What would carry it, named precisely: Fitch's 9 February 2021 rating action commentary and Moody's
March 2021 review-for-downgrade release, opened in their own voice, plus the Oxfam brief added as a
source so the three agencies' bilateral-relief statements can go into paragraph 1. I did not retry
`fitchratings.com` or `spglobal.com`; they were walled for three reviewers and nothing suggests that
has changed.

One reservation about the title edit, which I left in place. "Credit ratings cut when debt relief
would reach private lenders" states a fact rather than the suspicion, which HYP rule 2 asks a title
to state, and it will sit above a box saying the pattern that joins the facts is not proven. It is a
better title than the old one and it concedes what round 42 said it should, so I would not hold the
round for it, but the owner may prefer a form that keeps it a suspicion.

## 4. `for-profit-health-who-it-reached`: the retitle, and whether it is still dry

Answered in section 1. It is not dry and it should not stay a suspicion. The pattern asserts that the
institutions putting public money into for-profit health care could not say from their own papers who
it would reach — a finding, in the watchdog's own words, about one named institution and its own
sample, which the institution itself conceded. The channel claim nobody disputes is gone from the
title, and the document cuts against it anyway: the commission records that the share of new
investments going through funds fell to 17 per cent as CDC moved to direct equity and debt, and the
entry says so in `uncertain`.

## 5. The two hard conditions on the merges

**`who-owns-the-debt`** — met, and then improved on. The $12.9 billion and the single private creditor
appear nowhere in the edits; I searched the whole delivery for both. What stands in their place is
Debt Justice's October 2021 briefing, which I opened in full and verified figure by figure: the 46
countries, 23 per cent suspended or cancelled against 77 per cent still paid, $10.3 billion suspended
and $0.6 billion cancelled against $36.4 billion paid, other governments 48 per cent, private lenders
0.2 per cent "(one Italian bank suspended debt payments by Zambia)", private creditors receiving
$14.9 billion against bilateral $11 billion and multilateral $10.4 billion, UK-based private lenders
suspending nothing and receiving $3.2 billion, China suspending $5.7 billion. The "single private
creditor" is now named for what the document says it was. Zambia's $42.5 million is also met: I
opened the Reuters report and the figure is there, with the finance minister's statement on the day
the grace period expired. Two corrections: "multilateral institutions cancelled 5%" is corrected to
suspended 5 per cent, almost all of it cancellation by the IMF, which is what the briefing says; and
the `uncertain` note claiming the $42.5 million was "not from a creditor or government statement" is
wrong — the non-payment was stated by Zambia's finance minister — and is corrected.

**`offshore-routing-lost-tax`** — met in both parts, and the only item in this round that needed no
correction. The sentence round 42 barred, that the institution disputed the reading rather than the
numbers, appears nowhere. The count is attributed to Oxfam three times over: in the summary, in
`claims_per_author`, and in `uncertain`, which adds that no IFC reply appears in either document
opened. I opened Oxfam Canada's release of 11 April 2016 and verified its numbers — 51 of the 68
companies, 84 per cent of IFC investment in the region in 2015, $1.20 billion in 2010 rising to $2.87
billion in 2015 — and confirmed that the release carries no IFC response, which is what the entry
says. One note on the thirty-seventh operation, added during my pass: the Armenian case it moves
across is a genuine shape match (the IFC put $16.4 million into a developer incorporated in Jersey),
but Armenia is not in Oxfam's 2015 sub-Saharan count, so it illustrates the pattern rather than
belonging to the count.

## 6. The thirty-seven `old` strings

Checked by extracting `window.PATS` and `window.HYPS` from `base.html` and counting occurrences, not
by trusting the writer or the script. **Every one matches exactly once.** Thirty-three of the
thirty-seven `pats_edits` operations carry an `old` string (eight are `field`/`old`/`new` edits;
twenty-eight are `append_to`, which carry no `old`), and all six of the writer's `hyps_edits` string
edits match once, as do the four I added. I re-ran the check against the file as it stands after the
writer's 19:12 change.

I also read `merge_pats.py`, which another agent wrote for this round. It does refuse a near match:
`cur.count(old) != 1` is refused, the story edits require the string in exactly one paragraph, and
the whole run is all-or-nothing with nothing written if anything is refused. It also checks every
`case_id` against `window.CASES` and refuses a `graduated_to` that names no pattern. Two notes for
whoever runs it: it looks for a `check` key with verdict `cut` **inside each `pats_add` object**,
while this round's `check` block is top-level as specified, so that guard is inert against this file —
harmless here because nothing was cut, but it should not be relied on; and its progress line prints
`sources=` from a `sources` key, while the new patterns use `confirmed_by` like the live patterns, so
it will print zero sources for entries that have twelve.

## 7. The four merged `HYPS` entries, and the thing that stops the round

`status: "documented"` with `graduated_to` is what HYP rule 6 gives, and for the five graduations it
is exactly right. For a merge it is the only field available and it is defensible, but it says
something not quite true: the entry did not become that pattern, part of it was absorbed into an
older pattern with a different scope. Worse, in one case the leftover is not absorbed at all.
`private-courts-for-investors` is marked documented and graduated with no edits whatsoever, so the
card keeps asserting "Private tribunals that can order countries to pay companies billions" — which
the merge now puts on the page as documented — while the parts that are genuinely open, the
arbitrator concentration and the regulatory chill, go unasserted. Round 42 made a retitle the
condition for keeping it. The writer argues for no survivor instead, and gives a good reason (the
2012 count is an advocacy figure whose published rebuttal is already in the entry's own sources, and
nobody has opened the report in two rounds). I agree with the writer's conclusion and not with
leaving the entry as it is: it should either be retired out of `HYPS` into the retired file, or
rewritten fresh in a later round around the concentration. Marking it documented and leaving the
title alone is the one option that should not ship.

**The rendering fault: found by the writer, found again by me, and fixed at 19:12 by someone else.**
When I read them, `hypsHTML()` filtered on `status !== "documented"` for its count only, the list
below mapped every entry, and `detailHyp()` always printed the "Suspected pattern · not documented"
kicker and the dashed box. Applied as it stood, this file would have left a line reading "22
suspected, not documented" above thirty-one listed items, nine of which opened with a box saying no
case on the map rests on them while the same Jakarta paragraphs, the same Chiquita payments and the
same Oxfam hospitals sat higher up the page as established patterns. That is rule 1 inverted, and it
was the thing that would have stopped the round.

It no longer is. The commit at 19:12 filters the list on `status`, returns early from `detailHyp()`
for an entry with `status: "documented"` and `graduated_to`, and gives that entry a button through to
its pattern. I re-read both functions in the current `base.html` to confirm it rather than take the
commit message's word. So the duplication problem is closed, and what remains for the four merged
entries is the narrower question of what their cards should say.

## Routes

Served, each opened by me: `thedocs.worldbank.org` (WilmerHale report),
`documents1.worldbank.org` (the 2018 board paper, the Chad analysis, the 2010 evaluation and the 1998
Jakarta completion report — the text URLs answer 301 and serve on redirect), `fca.org.uk`,
`justice.gov/opa/pr/2007` (the 2007 Chiquita release), `efts.sec.gov` (the full-text index),
`icai.independent.gov.uk`, `medbox.org` (Oxfam's report), `debtjustice.org.uk`, `oxfam.ca`,
`brettonwoodsproject.org` (the 2009, 2013 and 2014 articles), `everycrsreport.com`, `corpwatch.org`,
`aljazeera.com`, `felixsalmon.com` (the Donegal judgment), `dandc.eu`.

Refused, recorded, not worked around: `imf.org` (403 Access Denied on the Chad country report, over
curl and over WebFetch, so the $231m/$271m figures could not be checked anywhere and were cut);
`justice.gov/opa/pr/credit-suisse-...` (200 with an Akamai interstitial challenge and no article text,
so the $547 million and the bribe figures rest on earlier rounds and on the FCA notice);
`ituc-csi.org` (403, Cloudflare, twice, so the 2013 panel's recommendation is unopened);
`sec.gov/Archives` (not attempted: it refuses a client with no contact address and none was invented);
`issuu.com` (serves the Business Ready report's listing, not its text).

## Which of the nine are safe to apply

As data, after the corrections in `r44_graduate_checked.json`: **eight of the nine are safe.**
`doing-business-data-changed`, `hidden-loans-banks-traders`, `payments-to-armed-forces-abroad`,
`city-water-into-private-hands` and `for-profit-health-who-it-reached` are safe to add, and the merges
into `holdout-funds-rich-courts`, `who-owns-the-debt` and `offshore-routing-lost-tax` are safe to
apply. The ninth, the merge into `company-sued-the-state`, is safe in its own text — I found nothing
wrong with the Reko Diq paragraph — but it should not be applied while
`private-courts-for-investors` is marked documented and graduated with its title untouched. Decide
that entry first: retire it or rewrite it.

The rendering condition I was going to attach to all nine is already satisfied: the 19:12 commit
filters graduated entries out of the suspected list and points their cards at the patterns that
absorbed them, so applying this file no longer puts the same material on the page twice.

Three qualifications on the five, all for the owner rather than for me, and the first two already in
the entries' own `uncertain` lines: `city-water-into-private-hands` is a claim about a programme and
not about each city, and read city by city it fails on its own Jakarta case;
`for-profit-health-who-it-reached` rests on one scrutiny body's review of one institution's sample;
and the Jakarta paragraph of the suspicion card was rewritten at 19:12 to say that the loan documents
show the Bank was encouraging Indonesia to privatise its utilities and expected the loans to make the
waterworks a more attractive investment. That sentence is not in the 23 June 1998 completion report,
which I opened in full, and nobody in this chain has opened the 1991 appraisal document where it might
be. The pattern does not carry it, and should not until that document is opened.
