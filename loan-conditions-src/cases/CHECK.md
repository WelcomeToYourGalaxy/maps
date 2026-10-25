# Fact-check brief

You are checking case cards for a public map of IMF and World Bank loan conditions. You did not write them. The owner's rule is: never publish anything a source does not support.

For each case in your file:
1. Open every source URL listed (WebFetch). Note any that will not open.
2. Check every factual claim in `conditions`, `lenders`, `community`, `suppression`, `killed`, `killed_note`, `outcome`, `companies` (including HQ city) and the dates against what the sources actually say.
3. Check that a source documents the IMF or World Bank link to the specific measure. If the card overstates the link, say so.
4. Check that any text in quotation marks matches the source word for word and is under 15 words, with at most one quote per source.
5. Check `lat`/`lng` fall on the place the card names.

Fix problems directly in the case: reword overstated claims to what the source supports, remove claims no opened source supports, correct numbers and dates. If the IMF/World Bank link to the measure cannot be supported at all, set `"remove": true` on the case and give the reason in `"check_note"`. If the link is real but disputed, make sure `confidence` is `"contested"` with both sides in `confidence_note`.

Add to every case `"check_note"`: one or two plain sentences listing what you changed (or "No changes needed").

Keep the same JSON shape. Plain, short English; no flourish. Do not use the words "brief", "I", or "sources opened" in any text field.

Write the corrected list (all cases, including any marked remove) as a JSON array to the output path you are given.
