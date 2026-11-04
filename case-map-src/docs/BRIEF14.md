# Round 14: complaints to lenders' complaint offices that have no case card yet

Follow /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/BRIEF13.md (and the BRIEF.md and BRIEF2.md it points to) for the rules and the case shape. Existing cases: /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/cases.json (708; do not repeat; use "extend" for an existing episode).

Your leads are complaint records already on the map as points. Each has k (key), o (office), t (title), y (year filed), place, lat/lng, al (what complainants said), fi (what the office found), st (status), u (the office's case page), h (true if harm on the ground was recorded). The complaint itself documents the lender link (the office only takes complaints about projects its lender finances); confirm the lender's financing and its timing from the office page or the lender's project page.

For each lead:
1. Screen it. Drop with a one-line reason if it is about procurement, a contract dispute between companies, staff matters, access to information only, a project in a high-income country with no harm to people or nature, a complaint found ineligible with no harm documented anywhere, or harm only feared.
2. For the rest, look for actual harm on the ground — displacement, lost land or income, pollution with measured or official effects, health harm, repression, arrests, killings — in the office's own reports (eligibility, compliance or dispute-resolution reports) and in outside sources (press, NGO field research, courts, UN). The office's finding of harm counts as a credible source; outside sources strengthen it.
3. Write a full case where the three tests pass. Put the complaint's key in "complaint_links": [{"k": "<complaint k>", "cs": "<your case id>"}] and set cp to the office key. If one case covers several complaints (same project), link them all.

Prioritise complaints where the office itself found harm or non-compliance, and those with deaths, displacement or repression. Quality over count; aim for 20–40 cases.

Output: {"cases": [...], "extend": [...], "complaint_links": [...], "dropped": [{"candidate": "<complaint k>", "reason"}]} to the file you are given; account for every lead. Validate with python (keys, valid lk/rg/levers/mechanism values, unique ids not in cases.json). Reply with counts, one line per kept case, main drop reasons, anything contested.
