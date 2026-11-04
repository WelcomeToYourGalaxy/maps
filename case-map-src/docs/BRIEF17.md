# Round 17: new cases where outside lending is tied to documented harm

Follow BRIEF13.md (and the BRIEF.md and BRIEF2.md it points to) in /tmp/claude-0/-home-claude/0a3e9cf9-63dc-591c-bbdc-8d8be4643750/scratchpad/w/ for the rules, the three tests and the case shape. Where those files give older counts or older lists of lk keys, this file wins. Existing cases: /tmp/claude-0/-home-claude/0a3e9cf9-63dc-591c-bbdc-8d8be4643750/scratchpad/w/cases.json (821, all on the map; do not repeat an episode; use "extend" for an existing one). Open leads left by earlier rounds: backlog.json in the same folder.

Owner's standards:
- No fabrication. Every figure, date, name and quote comes from a page you actually opened. If a source will not open, remove the fact or drop the case. Disputed figures say who says what.
- Link: documented outside lender, development financier, public fund or foreign investor/owner tied to what happened. A foreign company that was only a contractor, supplier or buyer does NOT pass.
- Actual harm: people displaced, land or income lost, poisoned, jailed or killed, or land and water damaged. Feared or "at risk" harm does not count.
- Timing: the outside money or company was involved when the harm happened.
- If the lender or other sources dispute the link, set confidence "contested" and give both sides in confidence_note. If the core harm rests on EJAtlas alone, drop it.
- Count in `killed` only deaths caused by the project, the company or forces acting for them. Everything else goes in killed_note, uncounted, with who reported it. Settlements without admission of liability leave deaths uncounted.
- Workplace pay or dismissal disputes alone are not cases.
- Plain wording for a novice. No opinion words or purple prose. Show figures. Credit figures to who reported them.

Valid values:
- mechanism: project, austerity, land, privatization, debt, trade
- lk: wb, ifc, miga, imf, icsid, idb, adb, afdb, ebrd, eib, aiib, reg, cn, bil, eu, priv, fdn, fdi
- rg: Africa south of the Sahara / East Asia and the Pacific / Europe and Central Asia / Latin America and the Caribbean / Middle East and North Africa / South Asia
- levers: deval, prices, cuts, tax, priv, trade, land, fees, labour, project, finance (plus lvwhy: {lever: short reason})
- cp: ip, cao, mici, am, irm, ipam, eibcm, ppm, icm, aiddata, ncp, jica, dfc, afd
- Keys in every case: id, title, place, iso3, lat, lng, point, start, end, mechanism, lenders[{name, role}], conditions, companies[{name, role, hq, hq_lat, hq_lng}], community, suppression, killed, killed_note, outcome, sources[{title, publisher, year, url}], confidence, confidence_note, lk, cp, rg, cx, ecosystem, levers, lvwhy. Optional: ap (true if point approximate), displaced, displaced_note, displaced_label, iso3_more.

Tools: WebSearch and WebFetch reach the web; the shell mostly cannot, so do not retry a refused request through other commands. Prefer opening pages directly. If a site declines, note it and move on.

Check each candidate against cases.json by iso3, nearby coordinates, project name and years BEFORE writing it. Earlier rounds repeatedly re-found Rempang, Okomu, Sino-Metals and similar. Check coordinates sit on the place named.

Output {"cases": [...], "extend": [...], "dropped": [{"candidate", "reason"}]} to the file you are given. Validate with python (keys, valid values, unique ids not in cases.json). Reply briefly with counts, one line per kept case, and anything contested. Quality over count: a smaller set of well-documented cases beats a padded list.
