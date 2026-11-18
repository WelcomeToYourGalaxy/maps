# BRIEF45 — the OECD Watch round, the first register for foreign company projects

**The job is to turn OECD Guidelines complaints into cases, or to drop them.** This is the largest
single addition available to the map from any register left: 413 complaints never worked, against a
measured conversion of 30–60% for complaint registers. It is also the first register that attaches
harm to a *foreign company* rather than to a lender, which is the row the map is thinnest on.

## What you are given

`docs/leads_oecdwatch.json` — all 503 complaints OECD Watch publishes, harvested from its own pages
on 17 Nov 2026. Fields per record:

- `title`, `subtitle`, `url`, `filed`, `concluded`, `status`, `sector`, `ncp`, `countries`
- `allegations` — what the complainants said happened. Median 1,260 characters, complete, not a
  summary of a summary.
- `outcome` — what the NCP did, where the page records one (444 of 503 have it).
- `defendant`, `company_in_violation`, `other_companies`, `complainants`, `affected`
- `already_on_map` — the case id, where the complaint is already named in a case's `cx`. **90 are.
  Skip every one of them.**
- `harm_flags` / `severe_flags` — a regex sorting aid over the allegations and outcome text, nothing
  more. A flag is not evidence and its absence is not an absence of harm.
- `company_appears_in_cases` — 28 records name a company already in a case, so those may be an
  extend rather than a new case.
- `score` — the sort already applied to the file. Descending.

**Work the file in order.** The 138 records with a severe flag and harm outside a rich country sit at
the top; they are the ones most likely to meet test 2.

## The thing that will trip this round

**A complaint is an allegation by the complainant. The complaint is not the source.** Everything
below follows from that:

- A complaint recorded as `Rejected` was usually rejected on procedural grounds — the NCP found the
  Guidelines did not apply, or the parties were out of scope. **That says nothing about whether the
  harm happened.** Do not drop a lead because of its status, and do not write "the NCP rejected the
  claim" as if it were a finding on the facts.
- A complaint recorded as `Agreement` does not establish that the harm happened either. It records
  that the parties settled something.
- So **test 2 has to be met from outside the complaint**: a court record, a state audit, a national
  newspaper, an inspection report, a company filing. Where the only source is the complaint itself,
  the case is `contested` at best, and a lead with nothing but the complaint behind it is a drop.
- `allegations` is written by OECD Watch from the complainants' filing. Quote it as what the
  complainants alleged, never as what occurred.

## Tests, unchanged

1. **An outside funder or foreign owner is tied to what happened.** Here that is the foreign company
   named in `defendant` or `company_in_violation`, operating outside its home country. A complaint
   against a company in its own country is not this map's subject unless a foreign parent is tied to
   the harm. 77 of the 413 name harm only in a rich country — check who the harm fell on before
   spending a fetch.
2. **The harm actually happened to people or to a named ecosystem.** A failure to disclose, to
   consult or to answer a letter is not harm under this test. Neither is a protest, unless something
   happened to the people in it.
3. **The timing overlaps.** The company's involvement and the harm have to be in the same period.

## What to write

Full card fields on the first pass, as rounds 37 and 38 did, because it retires the follow-on round:
`whole`, `conditions` and at least one non-`research` `ct`, written from the same documents you
already opened. `lk` includes `fdi`; add `ncp` to `cp`, and add the complaint to `cx` as
`["ncp", "<title exactly as in the file>", "<subtitle>", null, null]` so the dedupe in
`triage_oecdw.py` finds it next time.

## Quotes and sourcing

Every figure, date, name and quote comes from a document you opened. Quotes under fifteen words, one
per source. Where sources disagree, say who says what in `confidence_note`. Where the lender or the
company disputes the record, that belongs in `confidence_note` too and the case stays `contested` —
a disputed record is the field working, not a sourcing failure.

## Workflow

Draft → a separate checker that opens the sources itself → merge → `build.py` → headless test →
update `HANDOFF.md` and this brief → commit → push. The checker never trusts the writer's citations.
