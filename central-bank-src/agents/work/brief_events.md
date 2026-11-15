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

## Added at round 58, from mistakes round 57 made
7. **Never file an event with `kind` "other".** `app.js` counts an event only if its kind is not "other", so a real episode filed that way shows in the country box and is counted nowhere — it vanishes from the layer and the score silently. "other" is reserved for appointments and court rulings the layer deliberately excludes. Kinds are free text and render as written, so write a plain descriptive one: "parliamentary inquiry", "investigation of the bank", "statutory arrangement letting the government direct the bank", "public pressure", "dismissal".
8. **Do NOT list the central bank itself, or its own governor, as a party.** `parties` is for OUTSIDE parties. Round 57's agents offered seven central banks and two sitting governors as parties, and all nine had to be dropped by hand: a diamond for the bank itself would read on the map as an outside tie to itself.
9. **An appointment is not a move, but the articles an appointment order cites can be.** Macao was settled that way: an ordinary order appointing a board member cited the articles of the 1996 decree-law that put the board in the Chief Executive's gift, which both proved the statute in force and stated the arrangement. File the arrangement, say it rests on the order, and never file the appointment itself.
10. **A prosecution of an individual is not a move against the bank.** Settled rule: the acts that count are removed, suspended or pressed out, by a head of state, government, parliament or a currency union's heads of state. A sitting governor prosecuted for his own conduct in a previous job does not qualify, and nor does a regulator fining a governor over his own private business.
