# Brief: Case Map, ICIJ tranche 5 (round 21) — read BRIEF20.md first, then this

`docs/BRIEF20.md` is your brief in full: the absolute rules, the three tests, the forward rule, the
ICIJ figure trap, the document routes, the dedupe rules, the `killed` rule and the output format.
**Read it before this file.** What follows is what round 20 added, and every item on it decided a
card.

## The two rules that decided ten cards in round 20

**1. Housing demolished against land area.** Where a document records **housing actually
demolished** — in a table, with a separate enterprise column — homes were lost and limb (b) is met
**without a household count**. Where the outcome is **land area plus a count of "affected"
people**, it is not. That kept two cards and cut two. A card whose whole content is hectares plus
an "affected" figure is a drop.

**2. An outcome document that reprints the appraisal's figures is not an outcome.** This is the
harder version of the ICIJ figure trap and it decided two drops. The appraisal figure does not only
sit in the appraisal: **the completion report reprints it, where a reader takes it for an outcome.**

On one project, paragraph 37 of the completion report reproduced the appraisal word for word —
1,635.1 mu in 39 villages affecting 888 households comprising 3,549 people, house demolition
affecting 132 households and 538 people — and where the appraisal wrote "538 people in 132
households **will be relocated**", the completion report's verb was "**affected**". No outcome count
of anyone moved, none of land actually taken.

**The test: grep the appraisal for every resettlement figure the completion report gives. If it is
there, the report is repeating a plan.** The verb usually gives it away.

## What this round is testing, and why your batch is what it is

Round 19 ruled out region as a predictor of an independently-sourced case. Round 20 confirmed that
ICIJ's `complaint` flag predicts it — and used up every flagged row in the confirmed-displacement
table. **No sorting key is left**, so round 21 is built to test the one hypothesis round 20's own
results suggested: that **sector** predicts yield.

The batches are split so the two halves are comparable:
- **a_productive_china** and **b_productive_other** — airport, urban and road rows, the sectors
  where round 20's cases survived.
- **c_barren** — water, irrigation and rural rows, the sectors where round 20's drops clustered,
  because land is taken, compensation is paid and nothing adverse is recorded.

**The sector tag in your lead rows comes from ICIJ's project name only.** It is a hint about what
the works are, not a finding. **Report in your own report what each project's works actually were,
from the documents** — that is half of what this round is for. A row tagged `water` whose works
turn out to be an urban demolition is a result, not an error.

Do not let the hypothesis decide a card. If a barren-sector row carries a documented relocation
count or a documented loss, it is a case, and that is the most useful thing you can find.

## Three document-system findings from round 20, each of which cost a round something

1. **A completion report with an empty `docty` field is invisible to `wds?projectid=`** under its
   own number, its parent and its sibling. One report was found only by a `qterm` title search. Add
   that to the reasons a report that looks undisclosed is not.
2. **Conformed Project Agreements are published for 2004-2010 China loans and hold the safeguards
   covenants.** Search `qterm=<loan number> agreement`, then swap the host to `documents1`. Round
   20 wrote two absence claims — that no term required a resettlement plan to be carried out — and
   both were refuted by the Project Agreement, which required implementation **before any works
   began**. **Never write an absence claim about loan terms on this vintage without that search.**
3. **Nine of twelve Evaluation Group reviews in one sub-batch print no date anywhere on the page.**
   Only three carry a `Date Posted` line. For the rest the source date is the Bank's `docdt` field
   from the `wds` API, which is not a filename date but is unverified at document level — say so on
   the card. And take every other date off the cover page, never off a URL or filename.

## Two route notes

- **`curl` to a Cloudflare-fronted host returns a JS interstitial, not the page** — `whc.unesco.org`
  did this while serving in full through a fetch tool. Name the route that failed, never the host.
  A list of "blocked hosts" in this project has been wrong twelve times, every time because an
  unanswered permission prompt or a one-route failure was recorded as a host refusal.
- **A project filed under country "Africa" or a regional name is returned by no member-country
  query.** One Tanzanian project answered only to a global `qterm` on its full name.

## Dedupe: one more false match

`dedupe_leads.py` now keeps card text and source-URL text apart, because the Bank's archive builds
URLs whose path segments carry **other projects' numbers** — one completion report sits under a path
containing a different P-number. A URL-only hit is reported separately and is probably an archive
path segment. Open the card before calling anything a duplicate.

Your lead rows carry `_local_match`: existing cases in the same country sharing a distinctive word.
In round 20 it flagged three leads and all three took real document work to settle — two were
separate projects sharing a province and an implementing office, one really was the parent of a case
already on the map and became an extend. **The match tells you where to spend the documents, not
what the answer is.**

## Output

Exactly as BRIEF20.md specifies, with `r21_outcome` in place of `r20_outcome` in your report. Cache
every document to the folder named in your task as paired `.pdf` and `.txt`, named by P-number and
document type — the checker, the whole-picture job and the description job all read it, and in two
rounds running the whole-picture job has used none of its search budget because the cache was there.
