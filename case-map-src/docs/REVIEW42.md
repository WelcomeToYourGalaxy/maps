# REVIEW42 — sorting suspected patterns from actual ones

The owner's finding, 17 Nov 2026: **the map mixes potential patterns with actual ones, and some of
the former are the latter.** Thirty-one entries sit under "Suspected patterns" and some of them
assert things the public record has settled. An entry that presents a settled fact as a suspicion
understates the map, and it also makes the genuinely open suspicions look weaker by sitting beside
facts. Your job is to sort them, one by one, against the test below.

## The test

For each entry, state what its **title asserts** in one sentence. Then ask what the record does with
exactly that assertion. There are four verdicts.

1. **`documented`** — an official investigation, a court judgment or convictions, the institution's
   own admission, a regulator's finding, or an uncontested documentary record establishes the thing
   the title asserts, as a general practice and not only as one anecdote. The practice existing is
   enough; it does not have to be universal. Example of the shape: an independent law-firm
   investigation commissioned by the institution itself that finds its staff altered published data
   settles that the data was altered.
2. **`suspected`** — the pieces are documented and the pattern joining them is not. This is the right
   verdict when what is unresolved is **intent, design, or whether the practice is systematic** —
   when the facts are four exposed instances and the suspicion is that it is standing practice.
3. **`overclaimed`** — the title asserts more than the record carries, but a narrower statement of
   the same thing is documented. Give the narrower title and say which part is documented and which
   part remains suspected. This is likely to be the commonest verdict.
4. **`duplicate`** — the documented core is already a pattern on the page. You are given the thirteen
   in `documented_patterns_on_the_page`. Name the one it duplicates and say whether anything in the
   entry is left over that the existing pattern does not cover.

## What does NOT make something documented

- That it is widely believed, widely reported, or that the story is famous.
- That one instance is proven. One proven instance makes the instance documented, not the pattern —
  unless the record also establishes the practice beyond it.
- That a named insider disclosed it. A disclosure is a claim by a person; say whose claim it is.
- That the institution was accused, sued or criticised. An allegation is not a finding.
- Your own reasoning joining two documented facts. That is exactly what `suspected` is for, and this
  map's own rule is that an entry may never be built from an argument the map itself constructs.

## What you must not do

- **Do not rewrite the stories.** You classify. If an entry needs its story changed, say so in one
  line and leave the writing to a later pass.
- **Do not promote on a source you have not opened.** Every verdict of `documented` must name at
  least one document you opened yourself, with its date and what it says. If you cannot open it, the
  verdict is not `documented`, whatever the entry's own sources list says.
- **Do not take the entry's `conviction` field as the answer.** Several are well-scoped and will
  agree with you. Check it rather than copying it.
- Quotes under 15 words, one per source.

## Routes

Shell curl works: `curl -sSL -A 'Mozilla/5.0 (research; welcometoyourgalaxy maps)' <url>`. PDFs:
curl then `pdftotext -layout`. documents1.worldbank.org serves; documents.worldbank.org redirects to
it and serves. imf.org, bis.org, govinfo.gov, sec.gov/Archives, courtlistener.com, oecd.org and
eur-lex.europa.eu serve. The peachjam judgment indexes (kenyalaw.org, tanzlii.org, ulii.org and the
rest) answer `https://<host>/search/api/documents/?search=%22<exact phrase>%22` as JSON — quote the
phrase — while their judgment pages are walled; do not try to get past a challenge, record it.

## What to return

`rounds/r42_<x>.json`, an object keyed by entry id:

```
{"<id>": {
  "title_asserts": "<the assertion in one sentence>",
  "verdict": "documented" | "suspected" | "overclaimed" | "duplicate",
  "why": "<two or three sentences>",
  "settled_by": [{"what_it_is":"","date":"","url":"","what_it_establishes":""}],
  "still_open": "<what remains unresolved, if anything>",
  "narrower_title": "<only for overclaimed>",
  "duplicates_pattern_id": "<only for duplicate>",
  "left_over_after_the_duplicate": "<only for duplicate>",
  "documents_i_opened": [{"url":"","what_it_is":""}],
  "routes_that_failed": [{"url":"","how_it_failed":""}]
}}
```

Plus `rounds/r42_<x>_report.md`: your verdicts in a table, the two you are least sure of and why, and
any entry whose sources do not support what its story already says — that last is a defect worth more
than the classification.
