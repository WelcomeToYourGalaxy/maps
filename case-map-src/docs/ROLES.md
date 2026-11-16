# Auditing `lenders[].role`

Each case on the map carries a `lenders` list, and each entry's `role` says what that lender did:
the project number, the loan or credit number, the amounts, the dates, the ratings, the safeguard
policies triggered, which agency implemented it, what the completion report and the Evaluation
Group's review each found. The field is figure-dense and no round has checked it as it was written.

You are auditing it. You are not rewriting it, not improving its prose and not adding to it. You
check each assertion against the document it is attributed to, and you correct what is wrong.

Input: a batch file of cases, each with `id`, `pid`, `title`, `place`, `iso3`, `start`, `end`,
`lenders`, `lk`, `ct`, `sources`, `cached_files` and `manifest_docs`.

Output: a JSON object keyed by case id:

```
{"<id>": {"corrections": [{"lender_index": 0,
                           "field": "role",
                           "was": "<the exact substring now on the card>",
                           "now": "<the corrected substring, or \"\" to delete it>",
                           "why": "<the document and the sentence that decides it>",
                           "class": "<one of the classes below>"}],
          "clean": true|false,
          "checked": "<one line: which documents you read>",
          "could_not_settle": ["<anything you could not resolve, and why>"]}}
```

`was` must be an exact substring of the live `role`, so the correction can be applied mechanically.
A case with nothing wrong gets `"corrections": []` and `"clean": true`. **A clean card is a result,
not a failure**: round 22 found 37 of 56 entries clean, including the most figure-dense ones.

## The mechanism, which round 22's audit named

**The field gets written from a completion report's data sheet and an Evaluation Group review's
table at once, and whichever copy of a figure is nearer goes in.** Every error class below follows
from that. So the test for almost every assertion is: *which document actually says this, and is
that the document the card names?*

## The error classes, each found in round 22

- **`date_unsupported`** — a date no cited document gives. A card gave "14 February 2012" where the
  report says the Board approved in February 2012, its data sheet gives 10 February as a
  restructuring date, and the project paper is dated 19 January.
- **`wrong_column`** — a figure from the wrong column of the financing table. An unlabelled cost
  that is the appraisal column read as the project's actual cost (appraisal 215.99, actual 193.01);
  a "132 per cent over" taken from the percentage-of-appraisal column where the overrun against the
  original appraisal is about 284 per cent.
- **`partial_list`** — a partial list of triggered safeguard policies read as the full list. One
  card named two of the five the report lists; another omitted Indigenous Peoples OP 4.10, which
  the appraisal's safeguards table carries and which was material to that card's subject.
- **`wrong_document`** — a statement attributed to the wrong document. An extension reason that is
  in the review, not the report; a "High" rating that is the review's table entry where the
  report's own section says Substantial.
- **`wrong_number`** — a wrong report number. A card cited ICR00004130 where the cover prints
  ICR00004124 and the other number appears nowhere in the document.
- **`wrong_category`** — a wrong environmental category. A card said A where the report's data
  sheet and the appraisal document both say "Partial Assessment (B)".
- **`wrong_agency`** — a wrong implementing agency, where the report names a principal agency and
  then other bodies for particular components.
- **`half_a_finding`** — half of a review's finding reported. A review that lowered borrower
  performance *as well as* Bank performance, with only one named; a review whose stated grounds for
  lowering a rating were omitted.

Round 33 added two more, and both are live here:

- **`review_prose_over_table`** — a figure taken from the review's prose where it has garbled the
  completion report's own results row. Three of one round-33 batch's worst errors were this: a
  baseline printed as an output, a reduction printed as a level, and two targets wrong by 250 and
  350. **Where the review's prose and the report's table disagree, the table wins.**
- **The date rule has a third leg: check the project's Implementation Status and Results Reports
  before you score a date as unsupported.** Two cards in round 34's third batch carried dates that
  appear nowhere in the completion report or the Evaluation Group review — an approval date and an
  effectiveness date — and on the cited documents alone both would have been called
  `date_unsupported`. The ISRs print them: "Bank Approval Date: 10-Sep-2021", "Effectiveness Date
  21-Dec-2004". Both cards were right. ISRs are the Bank's own record of approval, signing,
  effectiveness and closing, they are listed in the same API call, and **an audit that skips them
  turns correct dates into vaguer wrong ones**, which is worse than leaving them alone.
- **`date_not_in_the_cell`** — a figure carrying a date the document does not give in the same
  sentence or table cell. A year taken from a cover, a news timestamp, a hyperlink URL, or an "as
  of" belonging to a different number.

## The test that matters most, found in round 34

Round 22 named the mechanism as *which document says this figure?* Round 34 found the sharper
version: **whose finding is this sentence?** Four of one batch's ten corrections were a claim moved
to the document that merely repeated it, and it ran in both directions.

- A review's **Lessons** section reprinting the completion report's own lesson, credited to the
  evaluators. One review's "better safeguards oversight would have prevented…" sits under a heading
  reading "Lessons — Adapted from ICR (paras 119–123)".
- The report's own unevidenced assertion credited to the evaluators who **doubted** it. Land
  acquisition "almost completed" is one completion report's claim; the review then says it is
  unevidenced, and the card had it the other way round.

Two checks follow. Before accepting any statement attributed to a review, read **the heading of the
section it sits in** — if the heading says the material is adapted from the completion report, the
finding is the report's. And read **the next sentence**: a review often quotes a report's claim in
order to dispute it, and a card that stops at the quotation reverses the review's meaning.

## A class the ten do not cover

`scope_misstated` — what a loan built, or where. One card says three loans financed "the
Khurja-to-Mughal Sarai freight line", where the completion report gives the three sections as
Khurja–Kanpur, Kanpur–Mughal Sarai and Ludhiana–Khurja, so with the third in the line runs Ludhiana
to Mughal Sarai. Every amount and date on that card is right. Round 34's auditors had to file two
such errors as unsettled because no class fitted.

## China loan numbers

Read the agreement cover. Pre-2005 China operations print "-CHA" where the Bank's catalogue titles
say "-CN"; 2009–2010 China loans really are "-CN". Two of round 34's corrections were "-CN" written
where the cover says "-CHA", and the direction matters.

## Rules

- **No fabrication.** Every correction rests on a sentence in a document you actually opened. If
  you cannot open the document, the assertion is `could_not_settle`, not a correction.
- **Never construct a URL.** Bank URLs come from the batch's `manifest_docs`, from
  `harvest_manifest.json`, or from an API response you can re-run. The Bank's newer
  `curated/en/099.../pdf/P<number>` shape is guessable, which is exactly why it must not be guessed.
- **Do not change a figure to one you prefer.** Where a document gives a figure two ways, the card
  should print both with where each appears, or neither. That is a correction only if the card
  currently prints one as settled.
- **Do not add material.** A term, figure or finding the card omits is not an error unless the card
  claims completeness (a policy list, a ratings pair, "the only"). Note it in `could_not_settle` for
  a later round rather than writing it in.
- **Citation style is not a fact.** Round 22 found that 39 of 46 cited reviews print no date
  anywhere while the cards cite one from the Bank's catalogue — unattributed, not wrong. Leave it.
- Plain words, short sentences, no researcher voice anywhere in a corrected substring.

## Where the documents are

Most cases in an early-round batch have **no** cached documents — the harvest came later. Routes
that worked in round 33:

- `search.worldbank.org/api/v3/wds?format=json&projectid=<P-number>&rows=1` returns the Bank's own
  document count for a project. Drop `rows=1` and add `&fl=docdt,display_title,pdfurl,docty` to list
  them. `projectid` works as a filter; `docty` does not.
- Fetch the PDF from **documents1**.worldbank.org. `documents.worldbank.org` refuses. A
  `/pdf/` path also serves as `/text/`, but `/text/` **301s to `/txt/`** and returns a 316-byte
  redirect body without `curl -L` — which a round could easily record as an empty document.
- A blank `docty` hides a document from a type filter, and the hidden file may be the project's only
  completion report. Check filenames, not just `docty`.
- Search `Aide Memoire` where no agreement or report is published: one carries a covenant-status
  annex reproducing three unpublished agreements with section numbers and compliance status.
- Read the loan or credit number off the document's **cover**, never off the catalogue title. They
  differed in six cases in round 33, and one file the archive titles "Conformed" is an unsigned
  draft with the number and date left blank.
