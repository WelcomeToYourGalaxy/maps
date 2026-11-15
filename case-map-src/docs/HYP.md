# Suspected patterns: the brief

A suspected pattern is **the same kind of write-up as a pattern, about something this map has seen
more than once and cannot yet state as a finding.** It lives in `window.HYPS` in `base.html`, renders
under the patterns in the left-hand box as "Suspected patterns", and opens its own card through
`detailHyp()`.

It is not a question-and-answer format and must not be written as one. It reads like a pattern,
because it is one in every respect except conviction: a title that states the thing, a summary with
the figures, what it would mean if it holds, the countries and what was seen in each. What makes it
different from `PATS` is three extra fields — what is missing, what would settle it, what would
refute it — and a dashed card that says it is not documented.

It exists because the map had nowhere to put a pattern it was not yet sure of. A researcher who saw
the same shape on four cards could write it up as a pattern, which claims more than four cards carry,
or leave it in a round report, where the next chat has to rediscover it. Rounds 19, 20, 21 and 22 each
produced findings of exactly that kind.

## The rules

1. **It is never a finding, and nothing on the map may rest on one.** No case's `confidence`,
   `displaced`, `killed` or card text may cite a suspected pattern. The dashed box and the
   "not documented" kicker are what keep it from being read as one, and they are not to be softened.
2. **Write the title as a statement, like a pattern's.** "The works came first and the payment after",
   not "Did the works come first?". The card's own furniture carries the uncertainty; the title
   carries the content.
3. **Every figure in the summary comes from this map's own data or from a document already cited on a
   card.** No new claims and no outside figures that have not been through a check. If a figure comes
   from searching the text of the cards, say so and call it a floor — that search finds only cases
   whose text already says the thing.
4. **`would_settle` and `would_refute` are both required, and both must name a document, a count or a
   record.** A suspected pattern nobody can imagine refuting is an opinion. Writing the refutation
   first is the test of whether it belongs here at all.
5. **`missing` says what has not been done, not what is unknowable.** It is the honest version of the
   conviction line and it is what stops a later round re-running work.
6. **A confirmed one graduates.** Write it into `PATS` with its sources, set the suspected pattern's
   `status` to `documented` and point `graduated_to` at the pattern id. Do not delete it: the path
   from suspicion to finding is worth keeping.
7. **A refuted one stays**, with `status: "refuted"` and the reason in `refuted_by`. A drop is output
   on this map. Somebody will have the same idea again and should find it already answered.
8. **It does not filter the cases.** `setHyp()` deliberately leaves every mark on the map where it is,
   unlike `setPat()`, which shows only its own story. Opening a suspected pattern must not change
   what the map appears to show.
9. **It must be global or international in scale, and about who is arranging things.** The owner's
   verdict on the first six, written 14 Nov 2026, was that they were "kind of small scale": they
   described the lending record and this map's own research rather than the world. An entry that
   could be written about one project or one country is a card or a note on a card, not a suspected
   pattern. The nearest documented example of the right size is `intel-contractors-lenders`, which
   carries John Perkins's account of US intelligence inside World Bank and IMF lending with the
   checkable part separated from the claim.
10. **Four things carry an entry of that size, and without all four it does not go in.** A claim
   stated as what is probably happening, structural and with no named living person or company
   accused inside it; a **measured regularity** behind it — a count, a share, a repeat-appearance
   rate, a voting threshold — every figure from a page the writer opened and cited; a sentence
   saying **why it stays hidden**, naming the record that is not published or the register that
   does not exist; and the nearest documented cases on this map, with what they do and do not
   establish. Round 23's own experience is the test of the rule: of eight directions tried, three
   were dropped for want of a regularity that was both global and about money crossing a border —
   the revolving door, where what exists is regional or biographical and a list of biographies is
   not a rate; intelligence services after 1990, where the only measurable thing is the
   declassification system rather than the lending; and advisers on both sides of a privatisation.
11. **Do not reach across maps for its shape.** The other maps in this repo are separate work with
   separate subjects, and some of them have their own suspected-pattern data in their own shape. This
   brief governs this map only.

## The shape

```
{
  id: "kebab-case",
  title: "A statement, like a pattern's title.",
  kind: "suspected",
  years: [first, last],
  conviction: "One line on how much it rests on. Say the number of cases or documents.",
  summary: "Two to four paragraphs, pattern style: what was seen, with its figures.",
  implications: "What it would mean if it holds.",
  missing: "What has not been done.",
  would_settle: "The document, count or record that would confirm it.",
  would_refute: "The one that would refute it.",
  countries: [ { iso3: "ISO3", role: "short", note: "what was seen there" } ],
  case_ids: ["case-id", ...],
  looked_at: "How much has been read so far.",
  status: "documented" | "refuted",   // only once it stops being open
  graduated_to: "pattern-id",         // with status documented
  refuted_by: "What refuted it."      // with status refuted
}
```

`case_ids` and `countries` drive where the map flies, through `entryPts()`: case points when there
are any, otherwise the cases in the countries named. **A note on that code**, because it caught a
round out: `entryPts()` originally read a flat `places` array of ISO3 strings and ignored
`countries`, so an entry with empty `case_ids` flew nowhere whatever its `countries` said. It now
reads both, and `countries` is the field to write. Entries written before that fix may carry a
`places` array as well; leave it. Every id must exist in `window.CASES` — check
before committing, because a bad id renders as a missing chip.

## Writing one

Plain, novice-friendly wording, short sentences, figures rather than characterisations, the same
standard as a card. Four things to avoid:

- **Do not state the suspicion as though it were observed.** The summary is what was seen; the
  implications are what it might mean. Keep them in their own fields.
- **Do not count a search of the cards as a count of the world.** Say which it is.
- **Do not let one become a lead list in disguise.** If the next step is research, it goes in the
  handoff's queue as well, and `would_settle` says what that research would settle.
- **Do not write one from a single case.** One case is a card. Two is a coincidence. The six that are
  there rest on between four cases and three independent research batches.

## The thirteen that are there now

Written 14 Nov 2026 from findings already in the rounds and from counts of this map's own data. None
has been tested. In rough order of how cheaply each could be settled:

| id | What would settle it | New fetches |
| --- | --- | --- |
| `site-people-lived-on` | Apply the resettlement-plan screen to the queue before research, then compare | no |
| `thin-means-no-register` | Divide per-country case counts by per-country lending; WDI and IDS are both on the map | no |
| `state-bodies-not-companies` | Sort all 1,138 company names into state bodies, firms and vehicles | no |
| `lender-record-understates` | Count the omissions across every paired completion report and review | only where a cache has lapsed |
| `works-before-payment` | Code each ICIJ case for two dates: works begun, compensation paid | yes |
| `compensation-into-court-deposits` | The deposit provision in each country's land acquisition statute | yes |

Three need no new fetches, only work over data that is already here, so none of them is blocked by an
API limit.

**Seven more were added on 14 Nov 2026 under rules 9 and 10**, in `rounds/r26f_hyps_global.json` with
its check log: `shareholder-votes-shape-the-conditions`, `small-circle-decides-the-claims`,
`index-sets-bond-market-access`, `standard-setters-no-legal-force`,
`resource-backed-loans-unpublished-terms`, `money-through-banks-no-named-borrower` and
`donors-pay-for-the-preparation`. An eighth, on debt restructured in creditor committees, was cut by
the checker: its own second sentence contradicted its title, since the Paris Club publishes that it
has 22 permanent members, and its private half restated the documented pattern `who-owns-the-debt`
from the same report.

**What that check found, and it is the error list for the next round of this job.** A figure
attributed to a card that the card does not carry — an IMF withholding of about US$1.3 billion put on
`argentina-december-2001`, which says the Bank raised its commitment to as much as US$22 billion and
cut off support in December 2001. Three more of the same kind: a dataset's largest recipient of
resource-backed loans given as global where the report says sub-Saharan Africa; 500,000 *barrels*
under garnishment turned into creditors holding under US$500 million; and "the only card that touches
correspondent banking" where a text search finds three. **Check every figure against the card, not
against the report it came from.** Two further faults: an entry whose claim was refuted by the paper
it cited, where the index provider's own criteria are quantitative and set no lower bound on ratings,
so the entry was rebuilt on that paper's stronger finding — for countries inside the index at higher
weights, their own debt, deficits and GDP stop predicting bond market access; and five `would_settle`
fields naming documents that would never be released (room documents, committee records, plenary
records, supervision files, administration agreements), all rewritten onto published records.
**A `would_settle` that names an unobtainable document is not a test, and writing it is the commonest
way this field goes wrong.**
