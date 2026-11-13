# Brief: Case Map, ICIJ tranche 3

You are researching leads for Case Map, a public map of documented harm tied to outside
lending and foreign investment. Your output is a JSON file of candidate cases. A separate
checker will verify every figure against the documents before anything is merged, so an
entry you cannot source will be caught and will cost the round a correction.

## The absolute rules

1. **No fabrication.** Every figure, date, name, place and quote must come from a page you
   actually opened in this session. If you did not open it, it does not go in the file. Never
   fill a gap from memory or from what a project of this type usually looks like. If you are
   not sure, leave the field out and say so in `confidence_note`.
2. **No researcher voice.** Cards are read by the public. Never write "I downloaded",
   "I read", "I could not find", "the card", "this entry", "we". Write the finding, not the
   search for it. Instead of "I could not find an independent report", write "No independent
   report was found." Scan your own output for the words I, we, my, our, card, entry before
   you finish.
3. **Plain writing for a novice.** Short sentences. No purple prose, no flourish, no
   crescendo, no aphorisms. Name the thing and the number.
4. **Do not make editorial choices for the owner.** If a document publishes a figure, give
   it. Do not filter, round or soften. Where two documents disagree, give both and name each.

## The three tests a case must pass

A row becomes a case only if all three hold:
1. A documented link to an outside lender or foreign investor (named loan, credit, guarantee,
   equity or grant, with its number or project ID).
2. **Actual** harm, not feared, planned or projected harm. A resettlement plan saying people
   *will be* moved is not harm. A document reporting that people *were* moved, or were not
   paid, is.
3. The harm overlaps in time with the lender's involvement.

## The forward rule (what earns a card this round)

No numeric floor. A row earns a case if **either**:
- **(a)** a document counts people or households actually **relocated** (moved, resettled,
  physically displaced), or
- **(b)** a document records a **specific harm to identifiable people**: deaths, injuries,
  arrests, land taken, compensation unpaid or paid below replacement cost, livelihoods not
  restored, loss of access to a service or a road.

Neither limb met → drop the row, with `r19_outcome: "dropped"` and a one-line reason.

## The ICIJ figure trap — read this twice

The `displaced` number in your lead rows is **ICIJ's estimate of project-AFFECTED people**.
It is **not** a count of people relocated. ICIJ searched Bank documents for "affected", "PAP"
or "displaced", used average household size where only households were counted, and included
temporary impacts. In several rows it is the **appraisal plan figure**, not the outcome.

Verified examples: Liaoning Medium Cities — ICIJ's 31,547 is to the person the figure in the
*original resettlement plan*; the outcome was 2,467 households and 6,080 people. Trung Son —
ICIJ's 10,591 is the appraisal's "about 2,327 households or 10,591 people will be resettled";
the outcome was 695 households. Distribution Efficiency — ICIJ gives 31,581; the completion
report says five households were relocated.

Therefore:
- **Never put ICIJ's number in the `displaced` field.** `displaced` holds only a Bank-document
  count of people actually relocated.
- Put ICIJ's number in `displaced_note`, named as ICIJ's and with what it counts. Start such a
  note with the figure, e.g. "ICIJ gives 7,461 for this project, which is its count of
  project-affected people and not a count of people moved."
- **Two of the three exact matches were in the appraisal document, not the completion report.**
  So read the appraisal (PAD) as well as the completion report (ICR) when the numbers do not
  line up.

## Document routes that work

- **Find the P-number first.** Projects API:
  `https://search.worldbank.org/api/v3/projects?format=json&countrycode_exact=KE&qterm=Electricity+Expansion`
  (use the ISO-2 country code). **Match on approval date, not on the name** — three distinct
  P-numbers carry the name "MDTF KP Emergency Roads Recovery Project".
  - This API orders results by **descending P-number, not relevance**, so older projects fall off
    page one. For anything approved before about 2010, re-run with `&os=20&rows=100` and sort
    locally.
  - **Regional projects are not returned under a member country's code.** Drop the country filter
    for those. The DRC's code in this API is **ZR**, not CD.
- **List the project's documents:**
  `https://search.worldbank.org/api/v3/wds?format=json&projectid=P103037`
- **Fetch PDFs from `documents1.worldbank.org`** — not `documents.worldbank.org`, which
  refuses. **The `wds` API hands back `pdfurl` on the refusing host**, so rewrite the host and
  upgrade `http` to `https` before fetching. Download with curl, then **read from disk with
  `pdftotext -layout`**. Never try to read a PDF through a fetch tool.
- **`wds?projectid=` returns only documents filed under that exact number.** A completion report
  is often filed under a parent or sibling project. Check those before concluding it is missing.
- **Before accepting that a completion report is undisclosed**, try a `qterm` title search on the
  project's full name plus "Implementation Completion Results". Some reports genuinely are not
  disclosed; for those the Evaluation Group's review cites the report by paragraph and is the only
  route. Say so in `confidence_note` when that is what a card rests on.
- **`wds` title fields are sometimes CDATA dicts** — `docna` comes back as `{"cdata!": "..."}` —
  which throws on naive slicing. Unwrap before use.
- Documents worth opening, in order: Implementation Completion and Results Report (ICR), the
  Independent Evaluation Group's ICR Review, the Project Appraisal Document (PAD), the
  Resettlement Action Plan / Resettlement Policy Framework, Implementation Status Reports
  (ISRs) for the years harm appears, and any Inspection Panel report.
- **Other hosts:** `iadb.org` and `mici.iadb.org` serve over `curl` (a fetch tool returns
  boilerplate). `business-humanrights.org` serves with a browser user agent. `irm.afdb.org`
  and Creamer Media return 403 from bot challenges, not host blocks — try curl with a UA.
- Independent sources are welcome alongside the Bank's: Inspection Panel cases, national audit
  reports, court judgments, named news reports, academic field studies. Label a single thesis
  or survey as what it is.

## Dedupe before you research

The map already holds 1,008 cases. **Dedupe on the Bank's P-number**, not on the project name —
ICIJ's names differ from the Bank's. Use the script:

    python3 /home/claude/maps/case-map-src/dedupe_leads.py P128276 P083929 P075941

**Do not grep `base.html` for P-numbers.** The file embeds ICIJ's own per-country lead tables, so
every ICIJ project number is already in it as lead data and a whole-file grep reports almost every
lead as a duplicate. The script parses `window.CASES` and searches inside case objects only.

If the script says a number is on the map, open that case and decide: if your documents add
materially new facts, write an **extend** (see below) instead of a new case; if not, mark the row
`r19_outcome: "already_on_map"` with the case id.

**A number missing from the script's output is not proof the project is absent.** A case may carry
the project under a name only, with no number — that is how three already-mapped projects came up
as fresh leads in one tranche. Confirm by place and years before writing a new case, and put the
P-number in the lender role of any case you write.

## The `killed` rule

`killed` is a counted number and holds deaths **caused by the project, the company, or forces
acting for them**. Anything else — road-accident deaths on a finished road, deaths from a
disease outbreak, a floor like "over 30 deaths were reported" — goes in `killed_note` as text
and `killed` stays 0. A figure that spans several contracts is not that project's figure:
check what the footnote counts.

## Output format

Write one JSON object keyed by case id. See `/home/claude/r19/EXEMPLAR.json` for a real card.
Required fields:

    id            kebab-case, specific: "kibera-mukuru-railway-relocation"
    title         plain noun phrase naming the harm
    place         most specific place the documents name, ending in the country
    iso3          three-letter code; add "iso3_more": [..] for extra countries
    lat, lng      decimal degrees for a real named point
    point         what the coordinate is, and where it came from
    start, end    integers (years)
    mechanism     "project" for a loan-financed project
    lenders       [{"name","role"}] — role carries loan numbers, amounts, dates, ratings,
                  each with its document and date in parentheses
    companies     [{"name","role"}] — contractors and operators the documents name, with the
                  role each actually played. Use the full legal name the document gives.
    community     what happened to people, in plain prose, with figures and their sources
    suppression   arrests, intimidation, force used against people who objected; "" if none
    killed        integer, per the rule above
    killed_note   text, uncounted deaths
    outcome       where it stands now
    sources       [{"title","url","date"}] — every document you actually opened
    confidence    "documented" | "contested" — these are the ONLY two values this map uses.
                  Use "contested" if the lender or another source disputes the link, OR if the
                  core harm rests on a single source. A case resting only on the Bank's own
                  completion report and evaluation is "contested", because the lender is
                  reporting on its own project. Otherwise "documented".
    confidence_note  what is solid and what is thin, in the card's public voice

Optional: `displaced` (count actually relocated), `displaced_note`, `displaced_label`,
`ecosystem`, `conditions`.

For an **extend** to an existing case, write instead:

    {"<existing-case-id>": {"extend": true,
      "lenders_add": [...], "sources_add": [...],
      "fields_add": {"community": " Extra sentence."}}}

`fields_add` **appends** a string to an existing field. It cannot set a number — if you need
to change a numeric field, say so in your report instead and do not put it in the file.

## When you are done

Write your file, then write a short report that:
1. Lists each row: case / extend / dropped / already_on_map, with its reason.
2. **Names your own two weakest entries** and says exactly what is thin about each.
3. Lists any figure where two documents disagree, with both figures and both documents.
4. Notes any route that failed and what the failure was (the route, not just the host).

Do not merge anything into the map. Do not run build.py. Do not push. Leave that to the lead.
