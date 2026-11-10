# Research brief: governor firings and pressure on central banks

A public civic-education map records documented moves against central banks: a governor removed, suspended, prosecuted, pushed out, publicly attacked by a head of government, reserves frozen or seized, or the bank's law changed to take power from it. You are adding sourced records, 1990 to 2026. Today is 2026-11-10.

## Hard rules
1. No fabrication. WebSearch to find a source, then WebFetch that exact page and confirm the page states the fact. Never write from memory or from a search snippet.
2. Every name, date and figure in `summary` must be on the page you cite. If the page won't load, find another source or drop it.
3. Say what the source says. "The president dismissed X", "X resigned, saying…", "the finance ministry asked for…". If the source gives no reason, say no reason is given. Don't infer motives.
4. Prefer official sources and the bank itself, then wire services and major outlets. National outlets and local languages are fine; write in English. Wikipedia only as a last resort, `weak_source: true`.
5. People only in their public role. Plain words for a novice, one to three sentences, no adjectives doing the work.
6. Don't duplicate what is already recorded: `have_events.json` lists iso3, date, kind and source for every event already on the map.

## Budget
At most 25 WebFetch calls, at most 3 at a time, and a shared hourly limit applies: if WebFetch reports the limit, save your file and stop. Don't work around it. Save as you go.

## Output
Write valid UTF-8 JSON with the Write tool to the exact path you are given:
```json
{"events":[{"iso3":"ABC","country":"…","date":"2019-07-06","kind":"dismissal | resignation under pressure | prosecution | public pressure | law change | reserves frozen | other",
 "summary":"One to three sentences.","source_title":"Headline (Outlet)","source_url":"https://…","weak_source":false,
 "quote":"under 25 words, word for word from the page",
 "parties":[{"party":"Clean name","name_as_stated":"as worded","party_type":"person | agency | company | government | bank | court | international body | other","hq_city":"City or null","hq_iso3":"ABC","role":"pressured, dismissed or prosecuted bank officials"}]}],
 "leads_not_opened":["https://…"], "searched_none":[{"iso3":"ABC","note":"what you searched"}]}
```
If a date is only a month or a year, write what the source gives (`2019-07` or `2019`).
Report back in three lines or fewer: how many events, WebFetch calls used, anything doubtful.
