# BRIEF36 — the first AidData tranche

Read **BRIEF20 in full first**, then BRIEF22's forward rule, then this. This file is a delta: it
covers only what is different about Chinese state finance, and everything different about it is a
trap the World Bank rounds never had to handle.

Your inputs are in `docs/`:

- `leads_aiddata.json` — the 793 flagged rows, now annotated with `r36_*` fields. Read the `fields`
  block before the rows.
- `aiddata_candidates.json` — pre-extracted candidate sentences for 592 of those rows, with the
  field each sentence came from.
- `aiddata_full_text.json.gz` — the full, untruncated AidData record for all 793. **Use this, not
  the lead file's `description`.** The lead file capped that field at 1,200 characters and cut 411
  of the 793 rows; the source carries 2.3 times the text, and for 210 rows every candidate sentence
  sits past where the lead file stopped.

## The one thing to carry into this round

**AidData has no field for harm, and the rows were selected by searching its free text for words.**
So a flag is not evidence, and the absence of one is not evidence either. Three consequences, all of
them measured rather than guessed:

1. **A row is a financing, not a project.** AidData files one row per lender in a syndicate. The
   793 rows are **653 financings**: four rows for the Banskhali power plant, eight for one Peruvian
   syndicated loan, six for Nam Dinh, three for Lower Sesan 2. `r36_financing` groups them.
   **Research the financing once.** Writing one card per row would put four cards on one power
   plant, which is round 18's two-cards-at-one-point fault arriving by a new route.
2. **143 rows are disaster or humanitarian relief**, and they are the worst trap in this dataset
   because they look like the strongest rows. The description of a flood-relief grant recites the
   deaths and the displacement — 389 deaths from a typhoon, 25 killed in a flood, 32 by the
   Nyiragongo eruption — so the row flags for both "people killed or hurt" and "displaced or
   resettled" and ranks near the top. **The money responded to the harm. It did not cause it.**
   Those fail test 1 and test 3 outright. They carry `r36_relief`. Do not write one up, and when you
   drop one, say in the drop reason that the harm is the disaster's.
3. **The "protest or unrest" flag is mostly noise, from one search term.** Of the 376 rows carrying
   it, only **142** have a real protest, riot, unrest or clash word. 234 fire on some form of
   "demonstration" alone, and 153 of those are a **demonstration farm, demonstration centre or
   "gave a demonstration"** on an agricultural or medical aid project. They carry
   `r36_demonstration_only`. A protest flag on its own was never going to carry a case anyway: a
   protest is not harm under test 2 unless something happened to the people protesting.

## Where to start, and why it is not the top of the rank

`r36_decisive_evidence` marks the **87 rows, 59 financings** that carry a relocation count, a death
with a cause, or compensation withheld — the three kinds of sentence that decide a case under the
forward rule. That is the front of the queue. It is not the same as the highest `r36_rank_score`,
because the score gives a point to protest and pollution and those two decide nothing on their own.

**Work the 59 financings first.** Spread them across writers by country route, not by sector: round
21 tested sector and it failed.

## The forward rule, unchanged, and what it means here

A case needs **either (a) a document that counts people or households actually relocated, or (b) a
specific documented harm to identifiable people** — deaths, injuries, arrests, land taken,
compensation unpaid or below replacement cost, livelihoods not restored. Neither limb is a drop. A
card whose entire content is a count of people "affected" is a drop. **A relocation verb is not a
count** — round 32's checkers cut 12 of 45 keeps and eleven went that way.

Two things about applying it to this material:

- **AidData's own text is not a document in the sense the rule means.** It is AidData's summary of
  sources it lists, and its figures are often a news report's. Where a candidate sentence carries a
  figure, **open the source AidData cites and read the figure there.** The card cites that source,
  not AidData, unless AidData is the only thing that carries the fact — and then say so.
- **There is no completion report here.** The Bank rounds rested on the lender's own outcome
  document, which is why 29 of 30 cases in round 17 came out `contested` on a single source. Chinese
  state lenders publish nothing comparable. So the evidence is press, court records, national audit
  offices and NGO field reports — which is harder to find and **better**, because it sits outside
  the lender. Expect a lower yield and a higher share of `documented` cases than any ICIJ tranche.

## Which lender goes in `lenders[0]`

Use `lk: "cn"`. The financing group tells you every Chinese lender on the deal; name them all, with
the amount each put in where AidData gives it, and put the lead arranger or the policy bank first.
**Do not write the syndicate total as one lender's loan.** Round 32 caught the inverse fault twice
(Morupule B, Mafinga-Igawa) and it decides whether the harm sits on the thing the money financed.

Check which part of the project the Chinese money paid for before tying harm to it. Round 19's
Burkina finding is the shape: 942 households were compensated on an airport platform the Bank's own
determination put outside the project, and the credit financed the access roads.

## Dedupe before you spend a search

`r36_dedupe_hint` carries a case on the map in the same country sharing three or more distinctive
words. **35 rows share four or more and most of them are genuinely the same project already on the
map** — Sorik Marapi, Ramu, Caculo Cabaça, Letpadaung, Tagaung Taung, Myitsone, Lower Sesan 2, Mes
Aynak, Merowe, Kamchay, Celukan Bawang, Coca Codo Sinclair, Techo airport, Teluk Sepang, Isimba,
Barishal, Suki Kinari, Indorama Eleme, Southern Expressway. Confirm by place and years, then make it
an **extend** rather than a new case where the row adds a lender or a figure the card lacks. Round
18's trap applies: `merge.py` reads an extend's `lenders_add` and the rest at the **top level**, and
it will print "extended N" having applied nothing. Check the case actually changed.

Two of those hints are false and show what the hint is worth: lead 187 matches `ebola-imf-wage-limits`
on the words Guinea, Liberia and Sierra Leone, and lead 88644 matches
`chashma-right-bank-irrigation` on Pakistani province names. Shared country words are not a shared
project.

## Drops are the round's output, same as always

Record every drop with the sentence or the absence that decided it, in the lead row's own
`r36_outcome` and `r36_note`. A drop with a named reason is finished work. The three standing
classes here, each of which should say which it is:

- the harm is the disaster's, not the money's (`r36_relief`)
- the flag was a demonstration farm, so nothing adverse is recorded at all
- the dataset records a protest and no harm to anyone in it

## Standing rules that this material breaks most often

- **Never take a number out of a table by grep.** Print the block from header row to footnote.
- **No figure carries a date unless the document gives that date in the same sentence or table
  cell.** Not from a URL, not from a filename, not from the article's own timestamp.
- **Where one document gives a figure two ways, print both with where each appears, or print
  neither.** A results annex and a summary table are two places.
- **Research-process voice never reaches a card.** No "searches returned nothing", no "none of the
  documents read here". CHECK20 §4 bars it and it still arrives every round.
- **Name your own two weakest entries.** It has worked in every round that asked, and it is what
  lets your checker go straight to the weak points.

## Budget

Expect this round to be search-bound, which is the opposite of the ICIJ rounds. Those ran on `curl`
and `pdftotext` against a document archive and one batch used two searches in total. **There is no
archive here**, so the work is search and fetch. WebSearch is capped at about 200 calls per turn
shared across every agent in the turn, so **three writers at about 30 searches each**, not six.
Scale checkers one for one: three writers means three checkers, each seeing none of the writing.
