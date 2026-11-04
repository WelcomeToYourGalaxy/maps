# Round 13 fact-check

You are an independent fact-checker for "Case Map", a public map of documented harm tied to outside lending and foreign investment. Read /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/CHECK2.md (and the CHECK.md and BRIEF2.md it points to) and /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/BRIEF13.md first.

- Open the sources yourself. Every figure, date, name and quote must be in a page you opened; fix or remove anything that is not. Plain, novice-friendly wording.
- Apply the three tests (link, actual harm, timing). A foreign company that was only a contractor, supplier or buyer does not pass the link test alone.
- If the core harm rests on EJAtlas alone, drop the case. If only the outside link rests on a single source, keep it as contested with a clear confidence_note.
- Deaths count only when caused by the company, the project, or forces acting for them; others go in killed_note, uncounted, with who reported them.
- Check coordinates sit on the place named.
- No duplicates: existing cases are in /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/cases.json; convert a duplicate to an "extend" or drop it.

Write the corrected file in the same shape ({"cases", "extend", "dropped"}) and a log ending in _log.json to the paths you are given. Validate both with python. Reply briefly with the most serious corrections and anything dropped.
