# CHECK48 — checking round 48's cases

You are one of six checkers, one per writer. Your file is `case-map-src/rounds/r48_out_<N>.json` and
the batch it came from, `rounds/r48_batch_<N>.json`.

**You open every source yourself.** A checker that reads the card and judges it has done nothing.
The checkers cut between a third and a half of what writers submit, and that is the mechanism that
makes this map trustworthy rather than large. Round 46's checkers made 79 corrections across 13
drafted cases and cut 3. Round 47's made 22 across 17 desk pairs.

## The failure family to hunt first

Round 47's corrections were almost all one thing: **a claim reaching past the document cited for
it.** The specimens were a conditional recommendation written as a finding, a date lifted from a
final statement and attached to the agreement, a party named in a document that does not name it,
and two invented distances.

So for every figure, date, name, quote and distance on the card: open the document in `sources` that
is cited for it and find it there. If it is not there, it is a correction, whether or not it is true.

Then the four specific traps:

1. **A cited document that denies the link.** Round 46's Bahrain card cited the UK contact point's
   assessment as its link evidence; that assessment says at paragraph 26 that the information does
   not link the companies to any abuses. **Read what each document concludes, not only what it
   describes.**
2. **"The company's position was not obtained" with the company's own filing in `sources`.** An
   annual report, information form or regulatory filing *is* the company's answer.
3. **Wikipedia where a primary or press source exists.** Check whether one does.
4. **Buyer mistaken for owner.** Round 46's Nikomas card named the brand that bought the shoes; the
   qualifying link was the contract manufacturer that put about US$100 million into the plant.

## The tests and the chain

Re-apply them yourself; do not take the writer's reading.

Three tests, all of which must hold: an outside funder or foreign owner tied to what happened; harm
that actually happened to people or a named ecosystem; timing that overlaps.

The chain, owner then lender or insurer then buyer then licensor, with the line above buyer. A
contractor, supplier or buyer fails test 1. A paid auditor, certifier, consultant, ratings agency or
law firm fails test 1. An event rights-holder, licensor, franchisor, promoter or sanctioning body
fails test 1 and sits below a buyer. **A contact point accepting a complaint says nothing about test
1** — the Guidelines bind a company that neither caused nor contributed to the harm.

**The complaint is not the source.** `allegations` is OECD Watch's write-up of the complainants' own
filing. Test 2 has to be met from outside it. Where the only source is the complaint, the case is
`contested` at best; where there is nothing behind it but the complaint, it is a drop.

## Fields that are checked mechanically, and are usually wrong in the same ways

- **`cx` carries the OECD Watch slug in position 1, not the title** — the convention changed on
  20 November 2026. Position 2 is the subtitle and **must not be empty**: the page displays
  `h[2] || h[1]`, so an empty subtitle shows a reader a slug. Check each slug against the lead's
  `slug` field character for character.
- **Every complaint of a multi-lead event is named.** The batch's `these_leads_are_one_event` lists
  them. A seven-lead event with three complaints in `cx` has lost four.
- **`ap` on a new complaint record flags an approximate map pin, not acceptance.** BRIEF47 line 93
  and CHECK47 line 36 define it as acceptance; they are wrong, and a card written on that definition
  is a correction. `base.html` renders `ap` as `(placed approximately)`. Acceptance lives in `st`.
- **`h` is whether harm on the ground is recorded**, by the complaint or by the case — not
  acceptance. A disclosure or due-diligence shortfall with no harm recorded is `false`.
- **`killed` is 0, not null**, where deaths were considered and not counted, with the account in
  `killed_note`.
- **`lat`/`lng` on a complaint record are the case's own coordinates**, with `pt` saying so. A
  coordinate that appears in no document is an invention.
- **`lk` includes `fdi`; `cp` includes `ncp`; `cp` holds office codes only** — no entity records.
- **Quotes under fifteen words, one per source.** Count them.
- `mechanism` is one of `privatization`, `austerity`, `project`, `land`, `trade`, `debt`. `ct` is at
  least one settled key that is not `research`.

## Where you find yourself rewriting rather than correcting

**Stop.** A checker that writes a card has written a card nobody checked. Where the fix is a
reshaping of the case rather than a correction or a cut, say so in your report and hand it on: the
new shape goes to a second reviewer before it merges. That is how round 46's Ayoreo case was
handled, and the review confirmed the source wording word for word and added two reports.

Round 38 is the warning. A card stood at `killed: 2` with eleven corrections outstanding, three of
four omissions favouring the card, after the checker's own claim that everything cutting the other
way was already on the card proved false in three places.

## What to return

`case-map-src/rounds/r48_chk_<N>.json`, in the same shape as the writer's file so it merges directly,
with the corrections applied and the cuts removed, plus one key of your own:

```json
{
 "cases": [ ... ], "complaints": [ ... ], "whole": { ... }, "ct": { ... }, "events": [ ... ],
 "check": {
   "corrections": [ {"case_id": "...", "field": "...", "was": "...", "now": "...", "document": "<the URL you read it in>"} ],
   "cuts":        [ {"event_key": "...", "fails": "test 2", "why": "...", "document": "..."} ],
   "reshaped":    [ {"case_id": "...", "why_a_second_reviewer_is_needed": "..."} ],
   "opened":      ["every URL you opened"],
   "refused":     ["every URL that refused, and how"]
 }
}
```

A cut is recorded with the test it fails and the document you read it in — the lead stays in the
queue with the reason, and is never deleted.

## Report back

How many corrections, across how many cases, and the family each belonged to. How many cases you
cut and on which test. Anything you handed on as reshaped. Every host that refused and how. And any
place where the *brief* was wrong rather than the writer — round 48 already knows of one, the `ap`
definition in BRIEF47 and CHECK47, and there may be more.
