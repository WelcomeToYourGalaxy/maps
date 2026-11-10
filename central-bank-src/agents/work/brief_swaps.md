# Research brief: central bank swap lines

A public civic-education map draws currency swap lines between central banks: agreements to lend each other currency. You are adding sourced records. Today is 2026-11-10.

## Hard rules
1. No fabrication. WebSearch, then WebFetch the exact page and confirm it states the agreement. Never from memory or a snippet.
2. Prefer the central banks' own announcements (PBoC, Fed, ECB, BIS), then wire services. Local languages fine, write in English. Wikipedia only as a last resort, `weak_source: true`.
3. Record the amount and currency exactly as the source gives them, the signing date, the term, and whether it was renewed or has expired. If the page does not say whether it is still in force, set `status` to "unknown".
4. Don't duplicate: `have_swaps.json` holds all 229 swap records already on the map, with provider, counterparty, amount and source.
5. pbc.gov.cn is often unreachable from here. Try it once; if it fails, use a mirror or a wire story instead of retrying.

## Budget
At most 25 WebFetch calls, at most 3 at a time; a shared hourly limit applies — if WebFetch reports it, save and stop. Save as you go.

## Output
Write valid UTF-8 JSON with the Write tool to the exact path you are given. Match the field names used in `have_swaps.json` exactly, and add `"quote"` (under 25 words, word for word from the page) to each record.
```json
{"swaps":[ { …same fields as have_swaps.json…, "quote":"…" } ], "not_found":[{"pair":"CHN-UZB","note":"what you searched"}], "leads_not_opened":["https://…"]}
```
Report back in three lines or fewer: records, WebFetch calls, anything doubtful.
