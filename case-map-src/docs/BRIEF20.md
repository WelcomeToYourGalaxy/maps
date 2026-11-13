# Brief: Case Map, ICIJ tranche 4 (round 20)

You are researching leads for Case Map, a public map of documented harm tied to outside
lending and foreign investment. Your output is a JSON file of candidate cases. A separate
checker will verify every figure against the documents before anything is merged, so an entry
you cannot source will be caught and will cost the round a correction.

This brief replaces BRIEF19.md. It carries the same rules plus everything round 19 learned.

## The absolute rules

1. **No fabrication.** Every figure, date, name, place and quote must come from a page you
   actually opened in this session. If you did not open it, it does not go in the file. Never
   fill a gap from memory or from what a project of this type usually looks like. If you are
   not sure, leave the field out and say so in `confidence_note`.
2. **No researcher voice.** Cards are read by the public. Never write "I downloaded", "I read",
   "I could not find", "the card", "this entry", "we". Write the finding, not the search for it.
   Instead of "I could not find an independent report", write "No independent report was found."
   Scan your own output for the words I, we, my, our, card, entry, draft before you finish.
3. **Plain writing for a novice.** Short sentences. No purple prose, no flourish, no crescendo,
   no aphorisms. Name the thing and the number.
4. **Do not make editorial choices for the owner.** If a document publishes a figure, give it.
   Do not filter, round or soften. Where two documents disagree, give both and name each.

## The three tests a case must pass

A row becomes a case only if all three hold:
1. A documented link to an outside lender or foreign investor (named loan, credit, guarantee,
   equity or grant, with its number or project ID).
2. **Actual** harm, not feared, planned or projected harm. A resettlement plan saying people
   *will be* moved is not harm. A document reporting that people *were* moved, or were not paid,
   is.
3. The harm overlaps in time with the lender's involvement.

## The forward rule (what earns a card)

No numeric floor. A row earns a case if **either**:
- **(a)** a document counts people or households actually **relocated** (moved, resettled,
  physically displaced), or
- **(b)** a document records a **specific harm to identifiable people**: deaths, injuries,
  arrests, land taken, compensation unpaid or paid below replacement cost, livelihoods not
  restored, loss of access to a service or a road.

Neither limb met → drop the row, with `r20_outcome: "dropped"` and a one-line reason. A card
whose entire content is a count of people "affected" is a drop.

**Two limits on limb (a), both set by round 19.**
- **A relocation out of a hazard zone is not automatically harm.** Bogotá's Disaster
  Vulnerability Reduction project moved 1,067 families out of non-mitigable landslide and flood
  risk, to secure tenure, and was dropped: the completion report says the resettlement policy was
  not triggered for that component at all and the 1,067 is the project's own target output. Keep a
  hazard relocation **only** where a document records a loss on top of the move — compensation
  unpaid or below replacement cost, livelihoods not restored at the destination, recorded
  compulsion with a count, or a destination worse than the origin. "Unwillingness by some families
  to resettle", with no count and no loss attached, is not enough.
- **Check whether the harm is on the thing the credit actually financed.** A Burkina Faso card
  held 942 households from the airport platform; the appraisal records that Bank management
  examined the platform under the resettlement policy and concluded the road works did not require
  the airport, so it is not an associated facility. The credit financed access roads, where the
  documents count 20 households. The 942 came off.

## The ICIJ figure trap — read this twice

The `displaced` number in your lead rows is **ICIJ's estimate of project-AFFECTED people**. It is
**not** a count of people relocated. ICIJ searched Bank documents for "affected", "PAP" or
"displaced", used average household size where only households were counted, and included
temporary impacts. In several rows it is the **appraisal plan figure**, not the outcome.

Verified examples: Liaoning Medium Cities — ICIJ's 31,547 is to the person the figure in the
*original resettlement plan*; the outcome was 2,467 households and 6,080 people. Trung Son —
ICIJ's 10,591 is the appraisal's "about 2,327 households or 10,591 people will be resettled"; the
outcome was 695 households. Distribution Efficiency — ICIJ gives 31,581; the completion report
says five households were relocated.

Therefore:
- **Never put ICIJ's number in the `displaced` field.** `displaced` holds only a Bank-document
  count of people actually relocated.
- **`displaced` holds a people-bearing unit** — people, households or families. Not structures.
  A card holding `displaced: 147` for 147 shops removed was corrected: all 105 cases on the map
  that carry the field count people, households or families. A structure count goes in the note.
- Put ICIJ's number in `displaced_note`, named as ICIJ's and with what it counts. Start such a
  note with the figure, e.g. "ICIJ gives 7,461 for this project, which is its count of
  project-affected people and not a count of people moved."
- Give the unit and the source in the first words of `displaced_label`.
- **Never convert households to people or back**, and never reconstruct ICIJ's arithmetic. One
  writer proposed 773,838 ÷ 131,955 = 5.86 as an average household size; the project's own four
  provincial resettlement plans give 4.4, 4.93, 4.3 and 4.59, and no document states 5.86. Say the
  documents do not explain the gap and stop.
- **Two of three exact matches were in the appraisal document, not the completion report**, so
  read the appraisal (PAD) as well as the completion report (ICR) when the numbers do not line up.
- **Check the document's verb.** Bank documents say "affected by" far more often than
  "relocated", and the gap between those two verbs is the whole finding. A draft that turned
  "affected by" into "displaced" had to be corrected.

## Reading Bank documents: five traps that have each cost a round

1. **The completion report (ICR) and the Independent Evaluation Group's ICR Review rate the same
   project and often disagree.** Never state one rating and cite both documents. Name each rating
   with the document that gave it. **Read every ICR rating out of the ICR itself** — the Group's
   review prints a column for the report's own ratings and that column is sometimes wrong. On one
   project the review's column said "Significant" where the report says "Substantial", and
   "Moderately Unsatisfactory" where the report says "Moderately Satisfactory" twice.
2. **The newer review template has no efficiency row and no relevance row.** Those two must be
   read out of the **body text of both documents**. A card reporting that the documents agree on
   efficiency, based on the table, is making a claim the table cannot support.
3. **The two bodies use different label sets** — Modest against Moderate, Negligible against
   "Negligible to Low" — so an apparent agreement can be a substitution. Label substitutions ran
   at four of six projects in one batch. Always read both columns.
4. **"The project team informed IEG that…" is not a document.** Grep every review for
   `informed IEG`, `the project team` and `the World Bank team stated` before using anything out
   of it; one 2025 review carried nine such attributions. A case was cut whose only household
   figures existed solely as something staff told the evaluators. Where such a fact is worth
   keeping, attribute it to the staff statement, not to a document. The sharpest example: on one
   project the report's own indicator table gives 55 per cent, "no change from baseline", and the
   review gives 77 per cent attributed to the project team — 22 points apart, with neither
   document explaining the gap.
5. **When a review recommends a project for further assessment, go and find the Project
   Performance Assessment Report (PPAR).** It is field-based and is often the only such document
   in a set. On one project it reversed the sense of the case. It is filed under the same
   projectid but often under a joint title covering two projects, so a title search misses it —
   look in the projectid document list.

## Selective quotation — the fault that decided three drops in round 19

Five of nine cards in one batch, and five of ten in another, quoted a damaging clause and dropped
the favourable clause **from the same paragraph**. It ran in one direction every time. Three cases
died on it: a Bank finding about delayed compensation whose stated consequence five words later
was delay to the civil works; a grievance log of "over 4000 complaints **or requests**" where the
card had dropped "or requests" and the Panel had determined the alleged harm was not occurring;
and a card whose three harm strands were all sourced to the Evaluation Group's "interaction with
the TTL" rather than to any document.

**Before you write a quote, grep the same document for the sentence that cuts the other way, and
read the whole paragraph the quote sits in.** Same fault one level up: do not list the indicators
from a table that were met and leave out the ones in the same table that were not.

**And do not supply a cause for a shortfall from nearby text.** One card attributed 1,093
unfinished households "to unfinished works in four areas"; the report gives no reason at all, the
review says "due to delays of construction work", and the nearest "four" in the document is "4
local technical offices".

## Dates

**Take a document's date off the document, never off its URL or filename.** Three of round 19's
four date errors came from trusting an archive filename. One completion report sits at a URL
ending `...01312018` and is dated 18 January 2018. One review has 26 June in its URL and 11 June
in its own `Date Posted` line. **If the cover page gives only a month, the card gives only a
month** — inventing a day to fill a date field looks like precision and nothing marks it as a
guess. Never take a figure's year from the article's date.

## Document routes that work

- **Find the P-number first.** Projects API:
  `https://search.worldbank.org/api/v3/projects?format=json&countrycode_exact=KE&qterm=Electricity+Expansion`
  (ISO-2 country code). **Match on approval date, not on the name** — three distinct P-numbers
  carry the name "MDTF KP Emergency Roads Recovery Project".
  - The API orders results by **descending P-number, not relevance**, so older projects fall off
    page one. For anything approved before about 2010, re-run with `&os=20&rows=100` and sort
    locally.
  - **Regional projects are not returned under a member country's code.** Drop the country filter
    for those. The DRC's code in this API is **ZR**, not CD.
- **List the project's documents:**
  `https://search.worldbank.org/api/v3/wds?format=json&projectid=P103037`
- **Fetch PDFs from `documents1.worldbank.org`** — not `documents.worldbank.org`, which refuses.
  **The `wds` API hands back `pdfurl` on the refusing host**, so rewrite the host and upgrade
  `http` to `https` before fetching. Download with `curl`, then **read from disk with
  `pdftotext -layout`**. Never read a large PDF through a fetch tool: two "reading limits" in an
  earlier round were artefacts of the fetch method, and the file on disk carried what the fetch
  said was missing.
- **`wds?projectid=` returns only documents filed under that exact number.** A completion report
  is often filed under a parent or sibling number. Always check parents and siblings before
  concluding a document does not exist.
- **Before accepting that a completion report is undisclosed**, try a `qterm` title search on the
  project's full name plus "Implementation Completion Results". Some reports genuinely are not
  disclosed; for those the Evaluation Group's review cites the report by paragraph and is the only
  route. Say so in `confidence_note` when that is what a card rests on.
- **`wds` title fields are sometimes CDATA dicts** — `docna` comes back as `{"cdata!": "..."}` —
  which throws on naive slicing. Unwrap before use.
- Documents worth opening, in order: the ICR, the Evaluation Group's ICR Review, the PAD, the
  Resettlement Action Plan or Policy Framework, Implementation Status Reports for the years harm
  appears, any PPAR, and any Inspection Panel report.
- **Other hosts:** `iadb.org` and `mici.iadb.org` serve over `curl` (a fetch tool returns
  boilerplate). `business-humanrights.org` serves with a browser user agent. `irm.afdb.org` and
  Creamer Media return 403 from bot challenges, not host blocks — try `curl` with a UA. For
  Chinese-language sources, searching the village or township name in Chinese is worth one or two
  searches; three rounds of Chinese cases have found nothing outside the Bank, so do not spend
  more than that.
- **Nominatim sometimes needs the local script.** "Shakpak Baba, Turkestan Region, Kazakhstan" in
  Latin script returns nothing while "Шақпақ баба" returns the village. Bank documents also spell
  the same place two ways in one report.
- Independent sources are welcome alongside the Bank's: Inspection Panel cases, national audit
  reports, court judgments, named news reports, academic field studies. Label a single thesis or
  survey as what it is.

## Cache every document to disk

Download each PDF to the cache folder named in your task, keep it as paired `.pdf` and `.txt`
(from `pdftotext -layout`), and **name the files by P-number and document type**. The checker,
the whole-picture-text job and the description job all read the same documents, and in round 19
two of those jobs used zero of their search budget because the cache was there. Say in your
report where the cache is and what is in it.

## Dedupe before you research

The map holds **1,026 cases**. **Dedupe on the Bank's P-number**, not on the project name — ICIJ's
names differ from the Bank's. Use the script:

    python3 /home/claude/maps/case-map-src/dedupe_leads.py P128276 P083929 P075941

**Do not grep `base.html` for P-numbers.** The file embeds ICIJ's own per-country lead tables, so
every ICIJ project number is already in it as lead data, and a whole-file grep reports almost
every lead as a duplicate — it matched 35 of 36 leads in one round when the true number was one.
The script parses `window.CASES` and searches inside case objects only.

If the script says a number is on the map, open that case and decide: if your documents add
materially new facts, write an **extend**; if not, mark the row `r20_outcome: "already_on_map"`
with the case id.

**A number missing from the script's output is not proof the project is absent.** A case may carry
the project under a name only, with no number — that is how three already-mapped projects came up
as fresh leads in one tranche. Confirm by place and years before writing a new case, and **put the
P-number in the lender role of every case you write**, so the next round's dedupe can see it.

Your lead rows carry a `_local_match` field: existing cases in the same country sharing a word
with the lead. It is a hint, not a finding. Two projects in the same province match each other.

## The `killed` rule

`killed` is a counted number and holds deaths **caused by the project, the company, or forces
acting for them**. Anything else — road-accident deaths on a finished road, deaths from a disease
outbreak, a floor like "over 30 deaths were reported" — goes in `killed_note` as text and `killed`
stays 0. A figure that spans several contracts is not a single site's figure: check what the
footnote counts. **Read the health and safety section, not only the project-history annex**: on one
project a writer found 2 deaths in the annex and the safety section records 7, and the causes
decide the count — contractor non-compliance and rushing to meet a deadline are the project's own
doing. Contrast a project where four worker deaths were attributed to illness unrelated to the
work; those stay uncounted in `killed_note`.

## Output format

Write one JSON object keyed by case id. See `/home/claude/r20/EXEMPLAR.json` for two real cards.
Required fields:

    id            kebab-case, specific: "kibera-mukuru-railway-relocation"
    title         plain noun phrase naming the harm
    place         most specific place the documents name, ending in the country
    iso3          three-letter code; add "iso3_more": [..] for extra countries
    lat, lng      decimal degrees for a real named point
    point         what the coordinate is, and where it came from
    start, end    integers (years)
    mechanism     "project" for a loan-financed project
    lenders       [{"name","role"}] — role carries the P-number, loan numbers, amounts, dates,
                  ratings, each with its document and date in parentheses
    companies     [{"name","role"}] — contractors and operators the documents name, with the role
                  each actually played, in the full legal name the document gives. These reports
                  usually name the implementing agency and not the contractor; where that is so,
                  say what the agency is and do not pad the array. For a government body, give a
                  sentence about its place in the state's structure or a named unit beneath it —
                  a description of the city it serves is not a description of the body. Do not
                  list an oversight or civil-society body beside the agency that caused the harm.
    community     what happened to people, in plain prose, with figures and their sources
    suppression   arrests, intimidation, force used against people who objected; "" if none
    killed        integer, per the rule above
    killed_note   text, uncounted deaths
    outcome       where it stands now
    sources       [{"title","url","date"}] — every document you actually opened
    confidence    **"documented" or "contested" — these are the only two values this map uses.**
                  `contested` if the lender or another source disputes the link, **or if the core
                  harm rests on a single source**. A case resting only on the Bank's own
                  completion report and the Evaluation Group's review of that report **is
                  `contested`**: the lender is reporting on its own project. `documented` where
                  independent press, a court record, an Inspection Panel finding, a field study or
                  a national audit corroborates the harm.
    confidence_note  what is solid and what is thin, in the card's public voice

Optional: `displaced` (count actually relocated), `displaced_note`, `displaced_label`,
`ecosystem`, `conditions`, `ap` (true where the point is district- or city-level rather than the
exact site).

For an **extend** to an existing case, write instead, with all five keys at the **top level** of
the object — not nested under an `add` key, which merges silently as nothing:

    {"<existing-case-id>": {"extend": true,
      "lenders_add": [...], "lk_add": [...], "cp_add": [...], "sources_add": [...],
      "fields_add": {"community": " Extra sentence."}}}

`fields_add` **appends** a string to an existing field. It cannot set a number — if a numeric
field needs changing, say so in your report and do not put it in the file.

## When you are done

Write your file, then write a short report that:
1. Lists each row: case / extend / dropped / already_on_map, with its reason.
2. **Names your own two weakest entries** and says exactly what is thin about each. This has
   worked in every round that asked, and it is what lets the checker go straight to the weak
   points. One entry a writer called doomed came out better documented than drafted.
3. Lists any figure where two documents disagree, with both figures and both documents.
4. Notes any route that failed and **what the failure was — the route, not just the host.** An
   unanswered permission prompt is not a host refusal. A list of "blocked hosts" in this project
   has been wrong ten times, every time in that shape.
5. Says where the document cache is and what is in it.

Do not merge anything into the map. Do not run build.py. Do not push. Leave that to the lead.
