# BRIEF40 — the outside-sourcing pass

**The job is not to add cases. It is to move a case from `contested` to `documented` by finding the
harm on its card recorded somewhere outside the lender** — a national judgment, a tribunal ruling, a
state audit report, a gazette notice, a national newspaper. The map's harm is currently mostly harm
the lender wrote down about itself, which is a floor rather than a measure. That is the defect this
round exists to narrow.

## What you are given

`docs/r40_batch_<x>.json`. Each entry has the card as it stands and a list of `candidates` — hits
from that country's national judgment index, already searched for you. **Nothing in that list has
been opened.** `on_target: true` means the title shares two or more non-boilerplate words with the
phrase searched; it is a sorting aid and not a verdict.

## Routes

- The eleven peachjam indexes (Kenya Law, TanzLII, ULII, ZambiaLII, GhaLII, MalawiLII, NigeriaLII,
  SierraLII, LesothoLII, ZimLII, NamibLII) answer
  `https://<host>/search/api/documents/?search=%22<exact phrase>%22` as JSON, over plain `curl` with
  a declared user-agent. **Quote the phrase.** Unquoted it is a relevance search capped at 10,000.
- Indian Kanoon: `https://indiankanoon.org/search/?formInput=%22<phrase>%22`, HTML. Titles sit in
  `class="result_title"`. Read a judgment at `https://indiankanoon.org/doc/<id>/`.
- **The ordinary `/search/?q=` web page on every peachjam site is JavaScript-rendered and carries no
  results in its HTML.** If you read that page you will record an absence that is not there. This has
  happened on this map thirteen times. Use the API path.
- Download a PDF with `curl` and read it from disk with `pdftotext -layout`. Do not read a large PDF
  through a fetch tool.
- If a route fails, **record which route failed, not which host**. A 403 to `curl` is not a refusal
  by the host.

## The standard — unchanged, and it is what the round turns on

1. **The outside source must carry the card's own harm**, not merely mention the project. A judgment
   about a contractor's payment dispute on the same road does not make the eviction `documented`.
2. **Same people, same parcel, same works, same dates.** Name the parties, the case number and the
   date. A judgment between similarly named parties about a different parcel is a different dispute.
3. **No fabrication.** Every figure, date, name and quote must come from a page you actually opened.
   If it will not open, the fact does not go in. Quote under 15 words, once per source.
4. **`documented` needs the harm itself outside the lender.** If the outside source confirms the
   project and the acquisition but the harm still rests on the lender's own report, the card stays
   `contested` — say so, and say what the outside source did and did not settle.
5. **Deaths**: count in `killed` only deaths caused by the project, the company or forces acting for
   them. A judgment that records a death without tying it to the works does not move the count.
6. **A correction to the card counts as a result.** If what you open contradicts the card, say so.
   Rounds 31 to 38 found that the most valuable thing a round produces is usually a correction.
7. **An empty result is not an absence** until you have tried the parties' names and the works' name
   from the card. Say which phrases you tried.

## What to return

One JSON file, `rounds/r40_<x>.json`, an object keyed by case id. For each:

```
{"<case-id>": {
  "outcome": "documented" | "contested-but-strengthened" | "no-outside-source-found" | "correction-only",
  "confidence": "documented" | "contested",
  "confidence_note": "<replacement, or null to keep>",
  "sources_add": [{"title":"","publisher":"","year":0,"url":""}],
  "field_changes": {"<field>": "<new value>"},
  "corrections": ["<what the card got wrong, with the document that shows it>"],
  "what_the_outside_source_settles": "",
  "what_it_does_not_settle": "",
  "phrases_tried": [], "documents_opened": [{"url":"","what_it_is":"","date_read_off":""}],
  "routes_that_failed": [{"url":"","how_it_failed":""}]
}}
```

Plus `rounds/r40_<x>_report.md`: what moved, what did not, and the weak points in your own work,
named. **Name your weakest call.** A checker reads this next, and a checker that finds nothing is a
checker that was not told where to look.
