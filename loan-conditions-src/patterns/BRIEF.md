# Brief: patterns behind the scenes of IMF and World Bank lending

You are researching "pattern layers" for a public, global map of the conditions the IMF, World Bank and other lenders attach to loans to governments. The map already shows country-by-country counts of conditions, loans, privatizations and documented cases of harm. A pattern layer maps one recurring structure that sits behind those loans across countries or over time: who really decided, who profited, who was rewarded or punished, and how. Each layer colours the countries by their role in the pattern, draws lines for the documented connections, and gives a summary, a dated timeline, sources, the claims that remain one author's alone, and what is still unproven.

## Hard rules
1. Never invent anything. Every fact must come from a source you opened (WebFetch). If you cannot open a source, do not cite it.
2. Separate three levels and never blur them:
   - **Confirmed**: stated by primary records (government archives such as FRUS, US Senate Church Committee reports, declassified CIA documents, IMF/World Bank archives and evaluations, court rulings, official inquiries) or by peer-reviewed research, or by two independent reputable outlets.
   - **One author's claim**: something a single memoir, book or witness says (for example John Perkins, *Confessions of an Economic Hit Man*) that primary records have not confirmed. These go only in `claims_per_author`, worded as "Perkins says ..." with the book and page or chapter where possible.
   - **Unproven**: what is suspected or argued but not established. These go in `uncertain`, in plain words.
3. Where the IMF, World Bank, a government or a company denies or disputes a claim, say so and cite the denial.
4. Statistical findings (for example, that countries voting with the US at the UN get IMF loans with fewer conditions) must name the study, its authors, year, sample and the finding as the authors state it, including how strong it is. Do not overstate.
5. Plain, short English for a novice reader. No flourish. Give figures, names, dates and mechanisms, not adjectives. Quotes: under 15 words, at most one per source; paraphrase the rest.
6. Do not use the words "brief", "I", or "sources opened" in any text field.

## Search budget
Web searches are shared with other researchers and capped. Use at most 25 web searches. Prefer WebFetch on pages you already know or find linked (FRUS at history.state.gov, CIA reading room, IMF and World Bank archives and evaluation pages, court rulings, Wikipedia pages to reach their cited primary sources). Stop searching when you hit 25 and write up what you have.

## Output
Write a JSON object `{"patterns": [...]}` to the file path you are given. Each pattern:

```
{
 "id": "kebab-case",
 "title": "short plain title (under 60 characters)",
 "kind": "axis | club | bloc | chain | scheme | wave",
 "summary": "one to two paragraphs: the structure, with the key figures, names and dates",
 "countries": [ {"iso3": "CHL", "role": "short role label", "note": "one or two sentences: this country's part, with figures and dates, naming the source"} ],
 "links": [ {"from": "who", "from_city": "city or null", "from_iso3": "USA", "to": "who", "to_city": "city or null", "to_iso3": "CHL", "label": "what flowed or happened (under 60 characters)", "years": "1970-1973", "a": [lng, lat], "b": [lng, lat]} ],
 "timeline": [ {"year": 1970, "event": "one sentence", "source_url": "https://..."} ],
 "confirmed_by": [ {"title": "source title, publisher, year", "url": "https://..."} ],
 "claims_per_author": [ {"author": "John Perkins", "work": "Confessions of an Economic Hit Man (2004)", "claim": "Perkins says ...", "status": "what records confirm or contradict, with source"} ],
 "uncertain": [ "plain sentence on what is unproven or disputed, and who disputes it" ]
}
```

- Use at most 4 distinct `role` labels per pattern (the map colours by role); put detail in `note`.
- `a` and `b` are [longitude, latitude] of the cities named (country centre if no city; then set the city to null). Lines are drawn from `a` to `b`.
- Every country listed must have a documented part in the pattern. Every timeline event needs a `source_url` you opened.
- Aim for depth: 6 to 25 countries per pattern where the record supports it, 8 to 20 timeline events, and every confirmed source listed.

Also add `"dropped": [{"idea": ..., "why": ...}]` for parts you could not document.
