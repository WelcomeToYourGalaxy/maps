# Fact-check brief: new records from the expansion

You are checking new case records (ids starting `x-`) before they go on a public map of child abuse networks and child
trafficking. The owner has a strict no-fabrication standard. Read `research/SCHEMA.md` for the rules records must follow.

For each record in your assigned list:
1. Open its `url` (and `url2` if present). If it does not load, search for the same report or article and open a working
   official or major-outlet copy.
2. Check every specific fact in `n`, `d`, `cover`, `cite`, `victims`, `offenders`, `y0`, `y1`, `yf`, `first_report`,
   `status`, `place`: names, dates, numbers, who found what. Check that people are named only as SCHEMA.md allows and that
   status words match the source (convicted / found by an inquiry / charged / accused / acquitted / disproved).
3. Check the record is in scope (sexual abuse or exploitation of children in institutions or by networks, or trafficking,
   sale or illegal adoption of children) and that `ll` is plausible for `place`.

Write one entry per record, in this format, to the output path you are given:
```json
[{"id": "x-...", "verified": true, "url": "best working source url (only if different from the record's)", "cite": "only if url changes",
  "fixes": {"field": "corrected value", ...}, "drop": false, "note": "what you checked and changed, one or two plain sentences"}]
```
- `verified: true` only if the source you opened supports the record after your fixes.
- Put corrected values in `fixes` (use the record's own field names). Remove an unsupported sentence by giving a corrected `d`.
- Set `"drop": true` only if the record cannot be supported at all, is a duplicate of another record (say which), or is out of scope.
- Do not use Wikipedia as `url` if any official or major-outlet source exists; if only Wikipedia exists, keep it and say so in `note`.
- Write the file as you go and validate it with json.load before finishing. Do not edit any other file.
- Report back: how many verified, fixed, dropped, and anything left uncertain.
