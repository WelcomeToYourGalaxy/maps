# Suspected patterns: the brief

A suspected pattern is **the same kind of write-up as a pattern, about something this map has seen
more than once and cannot yet state as a finding.** It lives in `window.HYPS` in `base.html`, renders
under the patterns in the left-hand box as "Suspected patterns", and opens its own card through
`detailHyp()`.

It is not a question-and-answer format and must not be written as one. **The card shows one
continuous rundown and nothing else** — the `story` field, told straight through for a reader new to
the subject. The fields behind it stay in the data as the test an entry has to pass, and are not
drawn: `summary`, `implications`, `missing`, `would_settle`, `conviction`, `looked_at`. What marks it
off from `PATS` is that dashed card saying it is not documented, and the closing paragraph of the
story, which says what the thing rests on and what would settle it.

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
4. **`would_settle` is required and must name a document, a count or a record**, and the story's last
   paragraph has to carry it in plain sentences. A `would_settle` naming a document that will never be
   released is not a test. **`would_refute` is deleted.** The owner's ruling, 14 Nov 2026: the
   category was not needed. Do not reintroduce it, in the data or in the prose. Whether an entry can
   be knocked down is still the test of whether it belongs here, but it is a question the writer
   answers before writing, not a field on the card.
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
  story: ["Four paragraphs. The whole of what the card shows. See 'How it is told' below."],
  summary: "Two to four paragraphs, pattern style: what was seen, with its figures. Not displayed.",
  implications: "What it would mean if it holds. Not displayed.",
  missing: "What has not been done. Not displayed.",
  would_settle: "The document, count or record that would confirm it. Not displayed.",
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

## How it is told: one continuous rundown

The owner's instruction, 14 Nov 2026: *continuous organic rundowns written in captivating storytelling
manner for novices, like a scary story, not categorical snippets like What would refute it, What would
settle it, etc.* And on the writing the first thirteen were given: *the writing is horrible*. It was
rewritten from scratch, not edited, against the four guides in the owner's GMO-map repo
(`guides/*.pdf`), which are the house voice for this kind of prose.

**Four paragraphs, in this order, with no headings between them:**

1. What is probably happening, hedged in the sentence itself, **and why it matters to the reader**,
   said plainly. A novice must never reach the end of a paragraph wondering what the point was.
2. Why it is likely: the measured regularity, with its figures, and the documented case on this map
   that shows the same shape.
3. What makes it possible — how few people decide, which record is not published.
4. What would settle it, as plain sentences naming the documents or the count.

**Spell out every implied connection.** If eighty-five per cent of the votes are needed and one
member holds more than fifteen per cent, write the subtraction down. The reader is not to be left
assembling the argument.

**What not to do**, from the owner's instruction: no faux-gravitas, portentous phrasing, manufactured
significance, contrived contrasts, repetitive sentence rhythms or formulaic transitions. Named
offenders to avoid reinventing: "What matters as much as...", "The trade is protected by...", "The map
holds nothing on this, and says so." No aphorisms, no compressed metaphors, no sentence that exists to
sound quotable, nothing written to seem literary or sophisticated. The unease comes from the
specifics — how small the room is, how much money is in it, what nobody publishes — and never from an
adjective, a rhetorical question or a one-line punch at the end. It should read as though a thoughtful
person wrote it first, not as though AI prose was edited to sound human.

Working length is about 400 to 500 words. The thirteen here run 392 to 527. Figures and quotes carry
the weight, so cut adjectives before cutting a number.

**Quoting.** One quote per source, under fifteen words, and paraphrase everything else from that
source. Several of these entries previously took three or four quotes from one charter or one paper.

**Stale counts are a live risk.** The prose repeats totals that later rounds move. Round 22 took the
map from 1,072 cases to 1,093, from 127 countries to 129, from 1,138 company names to 1,177, and it
moved Ghana 16 to 17, Uganda 24 to 25 and Senegal 13 to 14 — all of which were still being asserted
in these entries until they were rewritten. **Recount every map-derived figure in `window.CASES`
before publishing a round**, and prefer a count that was measured to one that was inherited.

## Writing one

Plain, novice-friendly wording, short sentences, figures rather than characterisations, the same
standard as a card. Four things to avoid:

- **Do not state the suspicion as though it were observed.** The summary is what was seen; the
  implications are what it might mean. Keep them in their own fields.
- **Do not count a search of the cards as a count of the world.** Say which it is.
- **Do not let one become a lead list in disguise.** If the next step is research, it goes in the
  handoff's queue as well, and the story's last paragraph says what that research would settle.
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

## The rewrite of 14 Nov 2026

All thirteen stories were written from scratch in one pass, from the figures already checked in the
`summary`, `missing`, `would_settle` and `countries` fields, so no new sourcing was done and no new
claim entered. Every figure in the new prose was then matched mechanically against those fields: one
did not match, a derived "no other member is above 7 per cent", and it was replaced with the figure
the source actually gives, Japan's 6.88 per cent. `would_refute` was deleted from all thirteen,
`detailHyp()` now renders `story` alone, and the tooltip over the section heading was rewritten,
since it had described the labelled rows that are gone.

**Four of the thirteen still argue from this map's own method rather than from the world**:
`site-people-lived-on`, `lender-record-understates`, `state-bodies-not-companies` and
`thin-means-no-register`. Each was rewritten so its first paragraph states a claim about the world —
the lender writes down in advance whether a project will take anyone's home; the published verdict on
a project is cleaner than the staff report under it; the body that takes the land is usually an arm of
the borrower's own state; blank space on the map means no register exists, not that nobody was hurt.
If the owner would rather they went, the sibling infiltration map retired its equivalents to its
handoff and a project doc, which is where that kind of writing usually belongs.
