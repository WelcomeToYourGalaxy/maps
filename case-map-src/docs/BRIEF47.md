# BRIEF47 — the OECD Watch extend round (round 47, desk)

You are a **writer** on the Globalization Case Map. This round adds no new cases. Every lead in
your batch is an OECD Watch complaint that a machine pass thinks concerns an event **already on the
map as a case**. Your job is to decide, from documents, whether that is true, and where it is true
to produce the records that tie the complaint to the case.

Round 46's worst failure was a card citing as its link evidence the very document that denies the
link. **Read what a document concludes, not only what it describes.**

## What you are given

`case-map-src/rounds/r47_batch_<N>.json` — a list of pairs. Each pair carries:

- `complaint` — the OECD Watch record as harvested in round 45: the allegations text, the NCP's
  outcome text, who filed it, the respondent company, the country, the filing date, the status.
- `case` — the map case the machine matched it to: title, place, coordinates, dates, lenders,
  companies, the community/suppression/ecosystem/outcome prose, and the URLs already in `sources`.
- `cmp_record_exists` and `cmp_record` — whether this complaint already has a record in the map's
  complaints layer, and its fields if so.
- `machine_match_on` — the company words the machine matched on. **This is a hint, not evidence.**
  Three of round 46's twelve machine hints were wrong.

The harvested text is the primary material and it is usually enough. You may fetch
`complaint.url` to confirm or to resolve a conflict. If a fetch returns `PROVENANCE_REQUIRED`,
that is an unanswered permission prompt, not a refusal: record it and decide on the harvested text,
or return `unresolved`. **Never alter a URL or spoof an agent to get round a refusal.**

## The one question

**Does the complaint concern the same operation, at the same site, as the case?**

That is the whole test for this round. Three things follow from it, and getting them wrong is how
this round goes bad:

1. **Do not re-run test 1 on the case.** The case already exists and has already passed the tests.
   A complaint filed against a contractor, a buyer, a certifier or a licensor can still be a true
   record *of this case's events*, and tying it to the case claims nothing about whether that
   respondent is a qualifying funder. Your verdict is about identity of the event, nothing else.
2. **The same company in the same country is not the same operation.** A complaint about a firm's
   conduct at mine A does not belong on the case about mine B. Where the complaint is about the
   same company at a different site or a different operation, the verdict is `false_match`, and say
   in `requeue_note` whether it looks like a lead for a case of its own.
3. **A complaint filed against several respondents over one event is one event.** Several pairs in
   this round are the same complaint filed against a parent, a subsidiary, a lender and a pension
   fund. Each gets its own record and its own link to the same case. Do not merge them and do not
   drop the duplicates — OECD Watch files them separately and the map's complaints layer counts them
   separately.

What makes the identity: the project or operation named, the site or district, the dates, and the
respondent's stated role in that operation. Name which of these you relied on. A match on country
and sector alone is not identity.

## What to return

Write `case-map-src/rounds/r47_out_<N>.json`: a JSON object with one key, `pairs`, holding one entry
per pair in your batch, in the batch's order. **Every pair gets an entry**, including false matches.

```json
{"pairs": [
 {
  "pair_id": "<copy from the batch>",
  "verdict": "extend" | "false_match" | "unresolved",
  "why": "Two or three sentences arguing the verdict from the documents. Name the operation, the site and the respondent's role, and say which text you read it in.",
  "identity_evidence": ["the project named in the complaint and in the case", "the district", "the dates", "..."],
  "fetched": ["any URL you opened"],

  "complaint_link": {"k": "ncp:<exact complaint title>", "cs": "<case id>"},

  "complaint_record": null,

  "complaint_h": {"k": "ncp:<exact complaint title>", "h": true},

  "extend": {
    "id": "<case id>",
    "cp_add": ["ncp"],
    "sources_add": [{"title": "<complaint title>", "publisher": "OECD Watch", "year": <year_filed>, "url": "<complaint.url>"}],
    "fields_add": {}
  },

  "requeue_note": ""
 }
]}
```

Rules for the fields:

- **`complaint_link`** — give it on every `extend`. `k` must be the batch's `cmp_key`, character for
  character. The merge looks the record up by that key and silently does nothing if it is wrong.
- **`complaint_record`** — only where `cmp_record_exists` is false. Then build the full record from
  the harvested complaint, in this shape, and leave `complaint_link` out (the record carries `cs`
  itself):
  `{"k": <cmp_key>, "o": "ncp", "t": <complaint.subtitle>, "y": <year_filed>, "lat": <case.lat>, "lng": <case.lng>, "place": <complaint country, and the case's place>, "pt": "<what the point is: use the case's own site, and say so>", "ap": <true where the NCP accepted the complaint for examination, false where it rejected it>, "al": <allegations, as harvested>, "fi": <any note on where it was filed, or omit>, "st": "accepted"|"rejected"|"concluded"|"agreement"|"no resolution"|"under review" — follow the status in the harvested record, lowercased, "u": <complaint.url>, "h": <see below>, "cs": [<case id>], "company": <company_in_violation>, "ncp": <complaint.ncp>}`
  Use the case's coordinates, because the complaint is about the case's own site, and say that in
  `pt`. Do not invent a coordinate.
- **`complaint_h`** — `h` is whether **harm on the ground** is recorded, by the complaint or by the
  case. It is not whether the NCP accepted the complaint. A disclosure or due-diligence shortfall
  with no harm recorded is `false`. Where the case records deaths, displacement, pollution or
  violence at that operation, it is `true`. Give the flag on every `extend`; say in `why` which way
  you set it and from what.
- **`extend.cp_add`** — always `["ncp"]` on an extend.
- **`extend.sources_add`** — the OECD Watch complaint page. Leave it out only where that exact URL
  is already in `case.source_urls`.
- **`extend.fields_add`** — optional, and at most **one sentence**, appended to `outcome`, naming the
  complaint and what the NCP did with it. Write it only where the harvested outcome text supports
  every word of it, and name the NCP in it. A rejected complaint with no finding usually warrants
  nothing here; leave `fields_add` as `{}`. **Do not write a sentence that the harvested text does
  not carry.** Do not touch any other field.
- **`verdict: "unresolved"`** — where the harvested text cannot settle identity and the fetch you
  needed was refused. Say what would settle it. An unresolved pair is requeued, not guessed.

Conventions that hold on this map and are checked:

- No Wikipedia where a primary or press source exists.
- Nothing in `why` that the documents do not carry. A figure attributed to a document that does not
  contain it is the failure this round's checkers look for first.
- British spelling in prose, plain language, no rhetorical flourish.

## Report back

End your turn with a short report: how many extends, how many false matches, how many unresolved,
and any pair where the machine hint was wrong in a way a later round should know about.
