# Research: what did the lender require?

Each case on the map names an outside lender (World Bank, IFC, ADB, a Chinese state bank, a commercial bank, etc.), but its write-up does not say what that lender required in return for the money. Find out.

Input: a batch file of cases (id, title, place, years, lender keys, lenders with roles, current conditions text, sources).

For each case, look for the documented terms attached to THAT lender's money for THAT project or programme, at the time of the harm:
- Policy conditions (prior actions, structural benchmarks, tranche conditions): privatization, price or subsidy changes, taxes, spending cuts, devaluation, trade opening, labour or land law changes, user fees, investment codes.
- Project loan terms: resettlement or environmental plans required (e.g. "the loan required a Resettlement Action Plan", "IFC Performance Standards applied as a condition of financing"), repayment security (sovereign guarantee, collateral, escrow, oil- or revenue-backed repayment), tied procurement (must use the lender country's contractor).
Good sources: the lender's own project page or loan/financing agreement, project appraisal document, program document, IMF letter of intent or press release, Inspection Panel / CAO / Accountability Mechanism reports, AidData records, reputable research.

Output conditions_out file: {"<id>": {"conditions_add": "1-3 plain sentences saying what the lender required, credited to the source, e.g. 'The 2009 loan agreement required the government to carry out a resettlement plan (World Bank, Project Appraisal Document).'", "ct": [types from the list below], "why": {"<type>": "short quote from conditions_add"}, "sources_add": [{"title","publisher","year","url"}], "searched": "one line"}}
Types: priv, prices, tax, cuts, deval, trade, labour, land, fees, invest, law, repay, tied, safeguard, fincov, admin, none ("none" only if a source says no condition was attached).
- `fincov` — financial covenants and use-of-proceeds terms: a required rate of return, a self-financing or debt-to-equity ratio, an offtake undertaking, a restriction on what the money may be spent on, a required escrow or minimum balance.
- `admin` — institutional or planning covenants: create an agency, adopt an action plan or manual, set up a unit or committee, submit plans for the lender's review.
If nothing is found, give "conditions_add": "", "ct": [] and say what you tried in "searched".

Rules (non-negotiable):
- Every fact comes from a page you actually opened with WebFetch. No figures from memory or search snippets. Wikipedia not as sole source.
- Advice, recommendations or "pressure" are not conditions unless a source says the money depended on them. Say "required" only when the source does.
- Plain words for a novice. No opinion words.

Budget: WebSearch is capped at about 200 calls per turn shared with two other agents. Use at most 60 searches. Open each case's own sources and lender project pages first. WebFetch has an hourly limit shared with other agents; if you hit it, wait for the next UTC hour.
Save progress every ~10 cases. Validate with python. Reply briefly with counts.

## These are retries

Every case in these batches has been looked for once already and came back without a documented term. Each record carries `previously_searched`, the note from that attempt, and most carry some `conditions` text that describes the money without naming a term it depended on. Do not repeat the route that already failed: go to a different document type (the financing agreement rather than the project page), a mirror, or a different institution in the same deal. If you reach the same dead end, say so in `searched` and name the host that refused, so a later round knows a mirror is needed rather than another search.

## Where the documents actually are

- **ADB is the most productive route.** Its document paths fetch directly: `https://www.adb.org/sites/default/files/project-documents/<proj>/<proj>-rrp-en.pdf`. The Recommendation of the President reports carry full covenant summaries.
- **EBRD** blocks automated fetching; accountability-mechanism mirrors describe complaints but not financing terms.
- **AfDB** returns client errors on project pages and appraisal paths; the Early Warning System mirror often records no project information.
- **IDB**: `iadb.org/document.cfm` and `mici.iadb.org` refuse direct fetches; the Accountability Console mirrors the MICI reports and works.
- **IFC**: `disclosures.ifc.org` project pages refuse direct fetches.
- Working hosts: `documents.worldbank.org` and `documents1.worldbank.org` PDFs, adb.org document paths, sec.gov/Archives, AidData records, the Early Warning System and Accountability Console mirrors, and most PDF appraisal documents.
- A blocked lender site is not evidence that no condition existed. Record it as blocked.

## The five failures that get entries rejected

1. **A lender's general policy read as a term of this loan.** This is the commonest by far. "IFC applies the Performance Standards" is a policy; "the Performance Standards applied as a condition of this financing" needs a source that says so about this deal.
2. **A government's own plan or law presented as a lender requirement.** If the borrower adopted it, say the borrower adopted it.
3. **A recommendation, an action plan agreed after a complaint, or pressure, written up as a condition.** Only "required" when the source says the money depended on it.
4. **A term from a different loan, a later loan, or a different lender in the same deal**, attached to this one.
5. **A date mismatch:** a covenant from an agreement signed after the harm happened.
