# Hypotheses: the brief

A hypothesis on this map is **a suspected pattern that is not documented yet, written as a question**,
with what suggests it, what would settle it either way, and what has already been looked at and not
found. It sits in `window.HYPS` in `base.html`, renders under Patterns in the left-hand box, and
opens its own card through `detailHyp()`.

It exists because the map had nowhere to put a suspicion. A researcher who noticed the same shape on
four cards had two options: write it up as a pattern, which claims more than the evidence carries, or
leave it out, which loses it. Both were wrong. A hypothesis is the third place.

## The rules, and the first one is the whole point

1. **A hypothesis is never a finding, and nothing on the map may rest on one.** No case's
   `confidence`, `displaced`, `killed` or card text may cite a hypothesis. The card says so in its
   own first line and that line is not to be softened.
2. **It is written as a question**, in the `question` field, and the question must be answerable.
   "Is compensation paid into court deposits routine?" is answerable. "Is the Bank acting in bad
   faith?" is not, and does not belong here.
3. **Every figure in `basis` comes from the map's own data or from a document already cited on a
   card.** No new claims, no outside figures that have not been through a check. If a figure comes
   from searching the text of the cards, say so in `looked_at` and call it a floor — that search
   finds only cases whose text already says the thing.
4. **`would_confirm` and `would_refute` are both required, and both must name a document, a count or
   a record.** A hypothesis you cannot imagine refuting is an opinion. Writing the refutation first
   is the test of whether it belongs here at all.
5. **`looked_at` is what keeps the next round from paying twice.** Say what was opened, what it
   lacked, and how much of it was read. This map's most expensive recurring mistake is an absence
   claim nobody tested.
6. **A confirmed hypothesis graduates.** Write it up in `PATS` with its sources, then set the
   hypothesis's `status` to `graduated` and point `graduated_to` at the pattern id. Do not delete it:
   the question and the path from suspicion to finding are worth keeping.
7. **A refuted hypothesis stays, with `status: "refuted"` and the reason in `refuted_by`.** A drop is
   output on this map. Somebody will have the same idea again and should find it already answered.
8. **A hypothesis does not filter the cases.** `setHyp()` deliberately leaves every mark on the map
   where it is, unlike `setPat()`, which shows only its own story. Opening a question must not change
   what the map appears to show.

## The shape

```
{
  id: "kebab-case",
  question: "The question, as a question.",
  status: "open" | "refuted" | "graduated",
  strength: "One line, honest, on how much it rests on. Say the number of cases.",
  why_it_matters: "Why the answer would change how the map is read or built.",
  basis: [ { what: "The observation, with its figures.", cases: ["case-id", ...] } ],
  would_confirm: "The document, count or record that would settle it yes.",
  would_refute: "The one that would settle it no.",
  looked_at: "What has been opened, what it lacked, how much was read.",
  places: ["ISO3", ...],        // optional; used to fly the map when no case_ids
  case_ids: ["case-id", ...],   // optional; cases it bears on
  graduated_to: "pattern-id",   // only with status graduated
  refuted_by: "What refuted it." // only with status refuted
}
```

`places` and `case_ids` drive where the map flies, through `entryPts()`. Case points are used when
there are any; otherwise the cases in the countries named. Every id must exist — check against
`window.CASES` before committing, because a bad id renders as a missing chip.

## Writing one

Plain, novice-friendly wording, short sentences, figures rather than characterisations, the same
standard as a card. Three things to avoid, each of which has already gone wrong on the cards:

- **Do not state the hypothesis in the basis.** The basis is what was observed; the question is what
  it might mean. "Four cards record compensation paid into court deposits" belongs in the basis.
  "Deposits are how land is taken without payment" is the question, and it goes in `question`.
- **Do not count a search of the cards as a count of the world.** Say which it is.
- **Do not let a hypothesis quietly turn into a lead list.** If the next step is research, it goes in
  the handoff's queue as well, and the hypothesis says what the research would settle.

## The six that are there now

Written 14 Nov 2026 from findings already in the rounds and from counts of the map's own data. None
has been tested. In rough order of how cheaply it could be settled:

| id | What would settle it |
| --- | --- |
| `site-people-lived-on` | Already scheduled: apply the resettlement-plan screen to the queue before researching, then compare |
| `thin-means-no-register` | Divide per-country case counts by per-country lending, both already on the map |
| `state-bodies-not-companies` | Classify all 1,138 company names into state bodies, firms and vehicles |
| `lender-record-understates` | Count the omissions across every paired completion report and review |
| `works-before-payment` | Code each ICIJ case for two dates: works begun, compensation paid |
| `compensation-into-court-deposits` | The deposit provision in each country's land acquisition statute |

Three of the six need no new fetches, only work over data that is already here.
