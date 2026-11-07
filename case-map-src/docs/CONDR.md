# Research: what did the lender require?

Each case on the map names an outside lender (World Bank, IFC, ADB, a Chinese state bank, a commercial bank, etc.), but its write-up does not say what that lender required in return for the money. Find out.

Input: a batch file of cases (id, title, place, years, lender keys, lenders with roles, current conditions text, sources).

For each case, look for the documented terms attached to THAT lender's money for THAT project or programme, at the time of the harm:
- Policy conditions (prior actions, structural benchmarks, tranche conditions): privatization, price or subsidy changes, taxes, spending cuts, devaluation, trade opening, labour or land law changes, user fees, investment codes.
- Project loan terms: resettlement or environmental plans required (e.g. "the loan required a Resettlement Action Plan", "IFC Performance Standards applied as a condition of financing"), repayment security (sovereign guarantee, collateral, escrow, oil- or revenue-backed repayment), tied procurement (must use the lender country's contractor).
Good sources: the lender's own project page or loan/financing agreement, project appraisal document, program document, IMF letter of intent or press release, Inspection Panel / CAO / Accountability Mechanism reports, AidData records, reputable research.

Output conditions_out file: {"<id>": {"conditions_add": "1-3 plain sentences saying what the lender required, credited to the source, e.g. 'The 2009 loan agreement required the government to carry out a resettlement plan (World Bank, Project Appraisal Document).'", "ct": [types from the list below], "why": {"<type>": "short quote from conditions_add"}, "sources_add": [{"title","publisher","year","url"}], "searched": "one line"}}
Types: priv, prices, tax, cuts, deval, trade, labour, land, fees, invest, law, repay, tied, safeguard, none ("none" only if a source says no condition was attached).
If nothing is found, give "conditions_add": "", "ct": [] and say what you tried in "searched".

Rules (non-negotiable):
- Every fact comes from a page you actually opened with WebFetch. No figures from memory or search snippets. Wikipedia not as sole source.
- Advice, recommendations or "pressure" are not conditions unless a source says the money depended on them. Say "required" only when the source does.
- Plain words for a novice. No opinion words.

Budget: WebSearch is capped at about 200 calls per turn shared with two other agents. Use at most 60 searches. Open each case's own sources and lender project pages first. WebFetch has an hourly limit shared with other agents; if you hit it, wait for the next UTC hour.
Save progress every ~10 cases. Validate with python. Reply briefly with counts.
