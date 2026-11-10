# Research brief: "Central bank capture" map

A public civic-education map (welcometoyourgalaxy.github.io/maps/central_bank_independence.html) records who owns and steers each central bank and the documented corruption in and around it. You are adding sourced records. These name real people, so accuracy matters more than volume. A short list of solid records is a success. So is "searched, found nothing".

## Hard rules
1. No fabrication. Use WebSearch to find a source, then WebFetch that exact page and confirm the page itself states the fact. Never write a record from memory or from a search snippet alone. If the page won't load, find another source or drop the record.
2. Every claim in `summary` must appear in the source you cite. Names, dates, amounts and outcomes are copied from it. Don't add context from elsewhere.
3. Status must match where the matter actually stands in the source. If someone was charged, write "charged", never imply guilt. Say what the source says: "prosecutors accused", "the court convicted". If you find a later acquittal or dropped charge, the record must say so and use status "acquitted".
4. Prefer, in order: court or prosecutor documents, audit or official inquiry reports, the central bank itself, major news outlets and wire services, national newspapers. Local-language sources are welcome; write the summary in English. If only Wikipedia states it, set `weak_source: true`. Don't use blogs, partisan sites or anonymous claims. A claim resting on one author alone goes in with status "alleged" and summary starting "Claim, not confirmed:".
5. The case must involve the central bank itself: its governor, board, staff, its money, or its supervisory failure as found by an official body. A corrupt commercial bank alone doesn't count. A politician's general corruption doesn't count.
6. Only people acting in a public or corporate role. No home addresses, family details beyond what is the core of the case, or anything about private individuals not central to it. Unnamed staff stay unnamed.
7. Plain words for a novice. Give the case, figure and mechanism. No adjectives like "shocking" or "massive". One to three sentences.
8. Don't filter by what seems important: include each distinct documented case you find, within the time budget.

Date range 1990 to 2026 unless told otherwise. Today is 2026-11-10.

## Budget
About 60 to 80 tool calls in total. Cover every bank on your list with at least one real search (try the local language where it helps). Move on after two or three empty searches.

## Output
Write valid UTF-8 JSON with the Write tool to the exact path you are given, saving as you go so partial work survives. Report back in two or three lines only: counts and anything unusual.

```json
{
 "records": [ {
   "iso3": "ABC",
   "country": "…",
   "central_bank": "…",
   "category": "…",
   "years": "2011-2014",
   "people": "Name (role); Name (role)  or  'staff (unnamed)'",
   "summary": "…",
   "status": "…",
   "source_title": "Headline (Outlet)",
   "source_url": "https://…",
   "weak_source": false,
   "quote": "A short phrase, under 25 words, copied word for word from the source, that backs the main claim. In the source's language.",
   "parties": [ {
      "party": "Clean name of the organization or person",
      "name_as_stated": "As the source words it",
      "party_type": "person | agency | company | government | bank | court | international body | other",
      "hq_city": "City of its head office, or null if a person or unknown",
      "hq_iso3": "ABC",
      "role": "one role from the list below"
   } ]
 } ],
 "searched_none": [ {"iso3":"ABC","note":"what you searched, in a few words"} ]
}
```

`parties` lists outside parties named in the record: companies, banks, courts, prosecutors, investigators, inquiry bodies, government bodies, and people outside the bank who are central to it. Don't list the central bank itself. May be empty.

Allowed `role` values:
- "paid or bribed the bank's officials"
- "received money, favors or contracts from the bank"
- "received leaked information"
- "owned or ran an asset officials held"
- "employed an official before or after (revolving door)"
- "pressured, dismissed or prosecuted bank officials"
- "audited or investigated"
- "other"

## Added rules (November)
- A shared hourly limit applies to WebFetch: at most 25 calls, at most 3 at a time, likeliest pages first. If it reports the limit, save and stop. Don't get around it.
- WebFetch answers through a small model, so ask it to quote names, dates and amounts as written, and check it actually said so. Don't rely on search result titles.
- A year or amount not on the page does not go in the record. Don't fill gaps from memory, including head offices unless well known.
- Staff below senior management: give the role, not the name, unless the name matters to the case.
- An outsider's failed attempt against a bank is not a case. Misconduct by a commercial bank alone is not a case.
- Report in two or three lines: records, WebFetch calls used, whether the limit hit, anything doubtful.
