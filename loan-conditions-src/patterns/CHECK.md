# Fact-check brief for pattern layers

You are checking "pattern layers" for a public map of IMF and World Bank loan conditions. You did not write them. The owner's rule: never publish anything a source does not support. Read /home/claude/work/patterns/BRIEF.md first for the format and the three levels (confirmed, one author's claim, unproven).

For each pattern in your file:
1. Open every URL in `timeline[].source_url` and `confirmed_by[].url` (WebFetch). Note any that will not open; remove a timeline event whose only source will not open and that no other opened source supports.
2. Check every figure, name, date and claim in `summary`, each country's `note`, each `links[].label` and `years`, and each timeline `event` against what the sources say. Correct numbers and dates; reword overstated claims to what the source supports; delete claims no opened source supports.
3. Make sure nothing that is only one author's word (a memoir, a single book, a single witness) appears as fact in `summary`, `note`, `links` or `timeline`. Move it to `claims_per_author` worded as "[Author] says ...", with `status` saying what records confirm or contradict.
4. Statistical studies: check the sample, period and finding against the paper's abstract or text, and that the strength is not overstated.
5. Check quotations are word for word, under 15 words, at most one per source.
6. Check `a` and `b` coordinates fall on the named cities (or country centres when the city is null), as [longitude, latitude].
7. If a whole pattern cannot be supported by opened sources, set `"remove": true` with the reason in `"check_note"`.

Add `"check_note"` to every pattern: a few plain sentences on what you changed. Keep the same JSON shape. Plain, short English. Do not use the words "brief", "I", or "sources opened" in any text field.

Use at most 10 web searches; rely on WebFetch of the cited URLs.

Write the corrected list (all patterns) as a JSON array to the output path you are given.
