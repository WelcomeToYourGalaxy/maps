# Research brief: the revolving door between central banks and private finance

A public civic-education map records officials who moved between a central bank and private finance (banks, asset managers, hedge funds, private equity, insurers), or the IMF and World Bank. These are career moves, not accusations, and the map says so. You are adding sourced records. Today is 2026-11-10.

## Hard rules
1. No fabrication. WebSearch, then WebFetch the exact page and confirm it states the move. Never from memory or a search snippet.
2. The page must name both the central bank role (with dates if given) and the private employer. A biography page on the bank's own site, the firm's site, or a wire story all count. Wikipedia only as a last resort, `weak_source: true`.
3. Write the move as a plain line: "from Goldman Sachs partner to Governor", "from Deputy Governor to Swiss Re board of directors". Give dates the page gives. No wrongdoing is implied and none should be suggested.
4. If a page shows an ethics finding or a cooling-off rule, say so in `summary`, with the source.
5. Don't duplicate what is already recorded: `have_rd.json` lists iso3, people, move and source for each move on the map.
6. Beyond the leads you are given, cover the names in your assignment.

## Budget
At most 25 WebFetch calls, at most 3 at a time; a shared hourly limit applies — if WebFetch reports it, save and stop. Save as you go.

## Output
Write valid UTF-8 JSON with the Write tool to the exact path you are given:
```json
{"records":[{"iso3":"USA","country":"United States","central_bank":"Federal Reserve System","years":"2006-2014",
 "people":"Name (role at the bank, with dates)","move":"from X to Y","summary":"One or two sentences, only what the page says.",
 "status":"career move, no finding","source_title":"Headline or page title (Outlet)","source_url":"https://…","weak_source":false,
 "quote":"under 25 words, word for word",
 "parties":[{"party":"Firm","name_as_stated":"as worded","party_type":"bank | company | international body | other","hq_city":"City","hq_iso3":"ABC","role":"employed an official before or after (revolving door)"}]}],
 "checked_none":["Name: page opened, names no private finance employer"], "leads_not_opened":["https://…"]}
```
Report back in three lines or fewer: records, WebFetch calls, anything doubtful.
