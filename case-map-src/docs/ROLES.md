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
  **It applies whether or not the card claims its list is complete.** Round 34's batches split on
  this — one left a card naming OP 4.12 alone because it claimed no full list, another corrected
  the identical shape, and their checker called the inconsistency the clearest process fault in the
  three audits. A card that names some of a project's triggered policies reads as naming them. The
  test is the appraisal document's own safeguards table: every policy marked triggered there
  belongs on the card. Policies added at a later restructuring are sourced to the completion report
  and the restructuring paper instead, the appraisal table being unable to carry them.
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

## An eleventh class, ruled in by round 34's checker

`wrong_scope` — a mis-stated statement of what a loan built or where: sections, route, components
or works, measured against the completion report's own component description. It is not
`partial_list`, whose test (is the policy marked triggered in the appraisal's safeguards table?) is
meaningless for a railway route, and not one of the nine that turn on which document, column or
speaker a figure came from — on the card below every amount and date is right. For example, One card says three loans financed "the
Khurja-to-Mughal Sarai freight line", where the completion report gives the three sections as
Khurja–Kanpur, Kanpur–Mughal Sarai and Ludhiana–Khurja, so with the third in the line runs Ludhiana
to Mughal Sarai. Every amount and date on that card is right. Round 34's auditors had to file two
such errors as unsettled because no class fitted.

## China loan numbers

**Read the suffix off the agreement cover, every time. Never infer it from the year or the number
series.** Round 34's first auditor proposed that pre-2005 China operations print "-CHA" and
2009–2010 ones "-CN"; its checker disproved that inside the same 87 cases. Loan 4881 is dated
18 March 2008 and prints `-CHA`; loan 4847 is dated 6 April 2007 and prints `-CN`. Three cards said
"-CN" where the cover says "-CHA"; one card correctly says "-CN" and must be left alone.

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
- **A citation's date is the Bank catalogue's `docdt`; a date in a card's prose is the document's
  own.** This was ambiguous in the first version of this brief: two auditors resolved it one way,
  their checker the other, and three corrections were spent on it. Settled:
  - In a `sources` entry the date sits beside a URL pointing at the Bank's catalogue record, so it
    is a **locator** for that record. The catalogue's `docdt` is right there even where the
    document's cover prints another day. Round 22's ruling stands: a review that prints no date
    anywhere, cited with the catalogue's date, is unattributed rather than wrong.
  - In prose — "the completion report of 22 December 2017" — the date is a **claim about the
    document** and may only be a date the document itself prints. Where the document's own copies
    disagree, print both with where each appears, or drop the date.
  - Why this is not pedantry: **one completion report can print two of its own dates.** ICR2972's
    cover reads "July 30, 2014" and its own data sheet reads "ICR Date: 07/31/2014". "The cover
    date" is therefore not uniquely a document's date, and a rule written only as "the cover wins"
    cannot be applied. The cover-beats-catalogue rule is for **loan and credit numbers**, which are
    facts about the operation, not for dates.
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
- **Ask for `repnb`.** Add it to the field list and the API returns the Bank's own report number —
  `ICRR0021994`, `ISR36770` — so a card citing "ICR2741" can be checked for the price of one field
  instead of by opening the document. Round 34 found cited report numbers that came from a
  catalogue file name rather than from the report. `harvest.py` now requests it and carries it into
  `harvest_manifest.json`, so projects harvested from round 35 on have it already; for an earlier
  project, make the call.
- A blank `docty` hides a document from a type filter, and the hidden file may be the project's only
  completion report. Check filenames, not just `docty`.
- Search `Aide Memoire` where no agreement or report is published: one carries a covenant-status
  annex reproducing three unpublished agreements with section numbers and compliance status.
- Read the loan or credit number off the document's **cover**, never off the catalogue title. They
  differed in six cases in round 33, and one file the archive titles "Conformed" is an unsigned
  draft with the number and date left blank.
