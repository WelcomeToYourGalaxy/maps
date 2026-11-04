# Independent fact-check of new cases for the "Globalization Map"

You did not write these cases. Check them as an outside reviewer. Rules for what a case must meet are in /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/BRIEF.md (read it). The site keeps a strict no-fabrication standard.

For every case:
1. Open every source URL. Confirm each figure, date, name, count of dead, arrests and quote word for word against what the page actually says. Fix anything wrong; remove anything no opened source supports. Replace dead links with a working source for the same fact, or drop the fact.
2. Re-run the three tests (link, harm, timing) yourself. If the World Bank/IMF link rests only on a government statement or critics, the case must be "contested" with the reason. If timing fails, drop the case.
3. Check that nothing overstates: the lender's share among co-lenders is stated; measures the lender did not require are not presented as its conditions; the lender's or government's denial is included where one exists.
4. Check lat/lng sit on the place named in "point".
5. Check lk, rg, levers and lvwhy match the text. Plain words, no opinion words, no "I"/"brief"/"sources opened" in text fields, quotes under 15 words and at most one per source.

Write the corrected file in the same shape ({"cases": [...], "dropped": [...]}, adding to "dropped" any case you remove, with the reason) and a log [{"id", "change", "why"}]. Validate both with python. Reply with the most serious corrections and any case dropped.
