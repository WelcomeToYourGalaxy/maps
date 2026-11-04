# Round 13: remaining Environmental Justice Atlas leads

You research new cases for "Case Map", a public map of documented harm tied to outside lending, loan conditions and foreign investment.

Read first: BRIEF.md and BRIEF2.md in /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/. Rules in short:
- Three tests: (1) a documented link to an outside lender, financier, export credit or aid agency, foundation or a foreign company investing/owning (lk "fdi"); (2) actual harm on the ground — displacement, lost land or livelihood, pollution with measured or officially recorded effects, repression, arrests, killings — not expected or feared harm; (3) timing: the outside money or company overlaps or precedes the harm.
- A foreign company that was only a contractor or equipment supplier, or only a buyer, does not pass test 1 on its own.
- Strict no-fabrication: every figure, date, name and quote comes from a page you open. Plain, novice-friendly wording; no purple prose.
- EJAtlas is a lead and a usable source, but the core harm and the outside link must be confirmed by a second credible source (court, government, UN body, complaint office, lender's own documents, established press, peer-reviewed study, NGO with field research). If only the link rests on one source, mark contested with a clear confidence_note; if the harm can't be confirmed outside EJAtlas, drop.
- Deaths are counted only when caused by the company, the project, or forces acting for them (police or army guarding or clearing for it). Other deaths go in killed_note, uncounted.
- Use the existing case shape exactly (all keys incl. ecosystem, levers, lvwhy). Example cases: /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/cases.json (692, all on the map — do not repeat; if an existing case covers the episode and you have a new co-lender or investor, write an "extend").
- EJAtlas API (use curl): https://ejatlas.org/api/v1/conflicts/?format=geojson and https://ejatlas.org/api/v1/conflicts/<slug>/en/ . Previously downloaded records: /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/ej/det/ and .../w/r11ej/det/.
- Prefer leads with an outside lender, and leads where repression or displacement is recorded. Quality over count. Wikipedia rate-limits; space out requests. Searches are shared and limited: prefer opening pages directly.

Output: {"cases": [...], "extend": [...], "dropped": [{"candidate", "reason"}]} to the file you are given; account for every lead. Validate with python (keys, valid lk/rg/levers/mechanism values, unique ids not in cases.json). Reply with counts, one line per kept case, main drop reasons, anything contested.
