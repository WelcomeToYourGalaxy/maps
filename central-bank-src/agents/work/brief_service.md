# Research brief: central bank auditors and banknote printers

A public civic-education map records who audits each central bank's accounts and who prints its banknotes or makes its banknote paper. You are adding sourced records. Today is 2026-11-10.

## Hard rules
1. No fabrication. WebSearch, then WebFetch the exact page and confirm it names the firm. Never from memory or a snippet.
2. Best sources, in order: the bank's own annual report or financial statements (the independent auditor's report page names the firm), an EU Council decision approving a euro-area bank's auditor, a national audit office report, the printer's own contract announcement, then wire services. Wikipedia only as a last resort, `weak_source: true`.
3. Give the financial year the appointment covers, as the page states it.
4. A client list on a supplier's marketing page is weak: record it, and say in `detail` that it is a client list in a third-party announcement and not confirmed by the bank.
5. Don't duplicate: `have_service.json` lists the auditors and printer links already on the map.

## Budget
At most 25 WebFetch calls, at most 3 at a time; a shared hourly limit applies — if WebFetch reports it, save and stop. Save as you go. Annual-report PDFs are long: ask WebFetch to quote the auditor's name and the year.

## Output
Write valid UTF-8 JSON with the Write tool to the exact path you are given:
```json
{"auditors":[{"cb_iso3":"ABC","auditor":"Firm name as written","auditor_hq_city":"City or null","auditor_hq_iso3":"ABC or null","year":"financial year 2025","source_title":"…","source_url":"https://…","quote":"under 25 words, word for word"}],
 "printers":[{"entity":"Firm","entity_type":"firm | central bank's own works | central bank subsidiary","entity_hq_city":"City","entity_hq_iso3":"ABC","cb_iso3":"ABC","relation":"prints its banknotes | makes its banknote paper","detail":"One sentence.","as_of":"2025","source_title":"…","source_url":"https://…","quote":"…"}],
 "not_found":[{"iso3":"ABC","note":"what you searched and opened"}]}
```
Report back in three lines or fewer: records, WebFetch calls, anything doubtful.
