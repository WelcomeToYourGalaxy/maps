# CHECK47 — checking the OECD Watch extend round (round 47)

You are an **independent checker** on the Globalization Case Map. A writer has judged a batch of
pairs, each pair being an OECD Watch complaint that a machine pass matched to a case already on the
map. You check every pair in the batch, including the ones the writer rejected.

**A checker that reads the writer's reasoning and judges it has done nothing.** Open the documents
yourself. Round 46's checkers made 79 corrections across 13 drafted cases, and the fault they found
most often was a claim attributed to a document that does not contain it.

## What you check, in this order

1. **The verdict.** Does the complaint concern the same operation, at the same site, as the case?
   That is the only test in this round. Read the complaint's own allegations and outcome text in
   `case-map-src/rounds/r47_batch_<N>.json`, and the case's prose in the same file.
   - A match on country and sector alone is **not** identity. Nor is the same company at a different
     site or a different operation: that is a `false_match`, however strong the name match.
   - **Do not cut on test 1.** The case already exists and has passed the tests. A complaint against
     a contractor, buyer, certifier, licensor or pension fund can still be a true record of this
     case's events. If the writer cut a pair on the respondent's role rather than on identity of the
     event, that cut is wrong — reverse it and say so.
   - One complaint filed against several respondents over one event stays several records, each
     linked to the same case. A writer who merged or dropped the duplicates is wrong.
   - **Read what a cited document concludes, not only what it describes.** Where the NCP's own
     outcome text says the material does not link the respondent to the harm, that bears on the
     verdict and the writer must have dealt with it.
2. **Every claim in `why` and `identity_evidence`.** Each must be in the harvested text or in a
   document you opened. Strike anything that is not, and name what you struck.
3. **The records.**
   - `complaint_link.k` must equal the pair's `cmp_key` character for character. The merge looks the
     record up by that key and silently does nothing if it is wrong, so check it literally.
   - `complaint_link` is given only where `cmp_record_exists` is true; `complaint_record` only where
     it is false. Not both, and never neither on an extend.
   - A `complaint_record` must carry every field the brief lists, must use the case's own
     coordinates with `pt` saying so, and its `al`, `st`, `y`, `company`, `ncp` and `u` must match
     the harvested complaint. `ap` is whether the NCP accepted the complaint for examination.
   - `h` is **harm on the ground**, recorded by the complaint or by the case — not whether the NCP
     accepted the complaint. A disclosure or due-diligence shortfall with no harm recorded is
     `false`. Check the writer's flag against the case's own community, suppression, ecosystem and
     killed fields.
   - `extend.sources_add` is the OECD Watch complaint page, and is left out only where that exact
     URL already sits in `case.source_urls`. Check the URL against the pair's `complaint.url`.
   - `extend.fields_add`, where present, is at most one sentence appended to `outcome`, and **every
     word of it must be carried by the harvested outcome text**. Cut the sentence if it says more
     than the text does, names the wrong NCP, or states an outcome the text does not state. Cutting
     it is not a cut of the pair.
   - Nothing may touch any field other than `cp`, `sources` and `outcome`.

## What to return

Write `case-map-src/rounds/r47_chk_<N>.json`, the **merged-ready** file:

```json
{
 "complaints": [ <every complaint_record you passed, unchanged or as you corrected it> ],
 "complaint_links": [ <every complaint_link you passed> ],
 "extend": [ <every extend you passed, each with its "complaint_h" folded in as the "complaint_h" key> ],
 "check_log": [
   {"pair_id": "...", "writer_verdict": "...", "checker_verdict": "extend|false_match|unresolved",
    "corrections": ["each correction, in a sentence"], "opened": ["URLs you opened"],
    "note": "anything a later round should know"}
 ]
}
```

`extend` entries take the shape `merge.py` expects:
`{"id": "<case id>", "cp_add": ["ncp"], "sources_add": [...], "fields_add": {...},
"complaint_h": [{"k": "...", "h": true}]}`
— note `complaint_h` is a **list** inside the extend entry. One extend entry per pair is fine even
where two pairs share a case; `merge.py` applies them in order and de-duplicates sources and `cp`.

Give a `check_log` entry for **every** pair in the batch, passed or not.

If a fetch returns `PROVENANCE_REQUIRED`, that is an unanswered permission prompt and not a host
refusal: record it in the log and decide on the harvested text, or return `unresolved`. Never alter
a URL or spoof an agent to get round a refusal.

## Report back

End your turn with: how many pairs you passed as extends, how many you cut to `false_match`, how
many you reversed in either direction, how many corrections you made in total, and the single worst
fault you found.
