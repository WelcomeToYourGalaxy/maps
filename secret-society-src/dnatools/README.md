# Romanian DNA corpus triage tools

Written in round 31 (20 November 2026) and committed because the equivalent from
rounds 17–30 — `rjn.py`, the reader that filtered judgments on their narrative
opener — was never committed and had to be rebuilt from scratch. The round-30
handoff recommended a round built on `rjn.py`; that round could not be run as
written.

These read the crawl output of `harvest_dna.py` (one JSON object per line, fields
`id`, `url`, `date`, `year`, `text`). They expect the `.jsonl` files in
`/home/claude/work/r31/scratch_romukr/` — **change that glob to wherever your
crawl lives.**

## What each one does

- `idx.py` — dedupe the crawl by id and classify each document as a press
  release or a court judgment.
- `scan.py` — the one that matters. Finds a document's facts passage
  (*stare de fapt* / *situația de fapt*) and keeps it only where it opens with a
  **narrative** (`în perioada`, `la data de`, `în cursul anului` …) rather than
  with the court's list of exhibits. Of 5,891 documents crawled in round 31, 648
  passed this plus a corruption-offence test. **Only about a quarter of facts
  passages open with a narrative**; the rest open with the evidence list and say
  nothing about what happened, which is what makes the corpus affordable.
- `brief.py`, `list.py` — one-line summaries over an id range, for triage at
  volume before opening anything in full.
- `g.py` — grep the whole corpus with context. This is also the free outcome
  check: search a defendant's surname and the later judgment is usually there.
- `r.py` — print one document by id, with an offset.
- `f.py` — find the facts-passage openers in a single document.

## Two things the corpus does that cost records before they were written down

1. **A judgment that merely ratifies a guilty plea agreement** (*acord de
   recunoaștere a vinovăției*) recites the agreement and the sentence and often
   no facts at all, so it names no body and no decision and fails the test.
   Check for a facts passage before reading further.
2. **A DNA page carries its own later `Actualizare` block at the bottom with the
   final outcome.** Two of round 31's five "written as resolved and are not"
   corrections were sitting at the foot of the page the record already cited.
   **Read to the bottom of every DNA page.** A release stops at "sent for trial";
   the update says what the court did.

Round 31 read 2.4 documents per record written, for 17 records, on two WebSearch
calls and no WebFetch.
