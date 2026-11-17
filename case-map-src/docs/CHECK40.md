# CHECK40 — checking an outside-sourcing batch

You are a separate agent from the writer. Your job is to cut what does not hold. On this map the
checkers cut between a third and a half of what writers submit, and that is the mechanism that makes
the map trustworthy rather than large. **A check that finds nothing has usually not looked.**

You have the writer's `rounds/r40_<x>.json`, its `_report.md` (read the weak calls it names — they
are where to start), the batch input `docs/r40_batch_<x>.json`, and BRIEF40.

## What this round can get wrong, specifically

1. **A judgment that names the project but not the card's harm.** The commonest failure of this job.
   A contractor's payment dispute, an income-tax appeal naming a concessionaire, an employment case
   against the utility — all name the project exactly and settle nothing about the people on the
   card. If the outside source does not carry the card's own harm to these people at this place, the
   card does not become `documented`.
2. **A match made through the works rather than the parties.** Matching chainage, authority and dates
   is an inference. Say so on the card if that is what it rests on, and do not promote a card whose
   link to the lender's money runs through geography alone. Check whether a document names the loan
   and the parcels together.
3. **The financing boundary.** Rounds 31 and 38 both nearly repeated the Burkina airport error: check
   which operation paid for the works the judgment is about, including after any transfer of a road
   to another programme, and whether the lender funded that stretch at all.
4. **Deaths.** Count in `killed` only deaths the documents tie to the project, the company or forces
   acting for them. A judgment recording a death without that tie does not move the count.
5. **A promotion to `documented` that the source cannot carry.** Read the writer's
   `what_it_does_not_settle` against its `what_the_outside_source_settles` and see whether the
   promotion survives its own caveats.
6. **An absence claim.** Did the writer try the parties' names and the works' name? Was the failure a
   route failure — an AWS or Cloudflare challenge on a judgment page while the search API served —
   rather than an empty index? Those are different findings and must not be written down the same
   way. **Name the route that failed, never the host.**
7. **Quotes and figures.** Every one must come from a page that was opened. Quotes under 15 words,
   one per source. If a figure came from a snippet rather than the document, it must say so.

## Your own limits

You may find a judgment page unreachable where the search API serves. Record that, and do not treat
a snippet as the document. **Do not solve or work around a bot challenge**; record it as a route
failure and move on.

## What to return

`rounds/r40_<x>_checked.json` — the writer's object with your corrections applied, each case gaining:

```
"check": {"verdict": "stands" | "stands-with-corrections" | "cut" | "downgraded",
          "corrections_made": [], "what_i_verified_myself": [],
          "what_i_could_not_verify": [], "routes_that_failed": []}
```

and `rounds/r40_<x>_check_log.md` saying what you changed and why. **If you cut a card's promotion,
say what would be needed to earn it.** If you find yourself writing a new claim rather than checking
one, flag it in the log as writer-work done by a checker, because nobody checks that.
