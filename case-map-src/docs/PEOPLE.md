# How much each person oversaw in total

The map's "People on the record" have short profiles that mention their part in harmful cases. The owner wants each profile to say, in one short sentence, how many projects, loans or deals the person worked on or oversaw in total, so a critique sits in context (e.g. one harmful project out of 2,500 approved on their watch).

Input: people_in.json (id, name, summary, posts with org/role/years, case_ids).

For each person, write `total`: one sentence, plain words, with a sourced figure. Examples of the right shape:
- "During his presidency, 1995 to 2005, the World Bank approved 2,912 projects (World Bank projects database)."
- "As Managing Director, 2000 to 2004, he oversaw 68 new IMF loan arrangements (IMF)."
- "As chief executive, 2012 to 2020, he ran a company with 45 mines in 11 countries (company annual report 2015)."
Pick the post through which they acted in the map's cases. If the person acted alone or in one post with no countable output (e.g. a minister who signed one deal, a guard commander), write "" and say why in "note".

Useful tool: the World Bank projects API returns counts without a web search, e.g.
https://search.worldbank.org/api/v2/projects?format=json&rows=0&strdate=1995-06-01&enddate=2005-05-31  (check that the date filter works by comparing two ranges; if it does not, find another way or leave blank). Annual reports of the IMF, regional development banks and companies give approval counts too.

Rules (non-negotiable):
- Every figure comes from a page you actually opened with WebFetch. No figures from memory or search snippets. Wikipedia not as sole source.
- If you computed a sum yourself, say so ("this map's sum of the bank's annual reports").
- Give sources: [{"title","publisher","year","url"}].

Budget: WebSearch is capped at about 200 calls per turn shared with another agent, so use at most 80 searches. Prefer fetching known pages (annual reports, the World Bank API). Start with the heads of lenders (presidents, managing directors, chief economists, vice presidents), then company executives, then others.

Output people_out.json: {"<id>": {"total": "...", "sources": [...], "note": "..."}} for every input id. Save progress every ~15 people. Validate with python. Reply briefly with counts.
