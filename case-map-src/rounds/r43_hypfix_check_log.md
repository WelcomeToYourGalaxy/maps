# Round 43 check log — suspected-pattern fixes

Checker: separate agent, 17 November 2026. Subject: `rounds/r43_hypfix.json` (nine defect fixes and
four `case_ids` decisions) against `docs/HYP.md`, the live `window.HYPS` in `base.html`, and the
documents themselves. Output data: `rounds/r43_hypfix_checked.json`. `base.html` was not touched,
nothing was built, nothing was committed.

**Verdict: merge it, with the 18 corrections in the checked file.** Nine of twelve entries carry
`stands-with-corrections`, three `stands`, none `cut`. Every `old` string matches. Every priority
claim I was told to spot-check is in the document. Four things the fix got wrong are corrected in the
checked file; two of them are things the fix removed that are true and in the document it cited.

## 1. The `old` strings

I extracted `window.HYPS` from `base.html` by brace-matching and compared every `old` string myself,
rather than trusting the dry-run. All 16 of the writer's edits match the live entry **exactly once**
(story edits match a whole paragraph exactly, and the paragraph text occurs nowhere else in the
entry; `conviction` and `case_ids` match the field whole). The two edits I added match as well: the
file now holds 18 edits and `every old matches exactly once` is true for all of them. No two edits in
any entry share an `old`, so nothing can be applied twice or silently skipped. 31 entries in `HYPS`,
1,182 ids in `CASES`, both as the writer said.

## 2. New facts against documents

I opened every document a priority claim rests on, with my own fetches, and read the passage rather
than the report's account of it. Full passages are quoted in `what_i_verified_myself` per entry in
the checked file; the summary:

- **WilmerHale on `rankings-bent-for-money`** — all four additions check out against the Bank's own
  copy of the report. The scope sentence names China (DB2018) and Saudi Arabia, the UAE and
  Azerbaijan (DB2020), paragraph 1. The Jordan chain is paragraphs 20 and 21 and is exact, including
  the employee sent to Jordan reporting the data correct and the team then pivoting to boost Saudi
  Arabia past it. The UAE change following from the Saudi one on the similar tax system, and not
  affecting the UAE's ranking, is paragraph 21. Azerbaijan is paragraphs 23 and 36: changed downward
  on Djankov's own belief the reforms had not happened, "multiple employees" reporting an apparent
  personal animus, and no money anywhere in either paragraph. The "likely" finding is paragraph 33
  verbatim and the three possible motives are paragraph 35, the paid contracts being one of them.
  I specifically tested the card's claim that Jordan, not money, was *the first stated consideration*,
  because paragraph 19 mentions the Saudi advisory contracts earlier in the narrative: the report
  labels them itself — paragraph 34 "As to the first consideration" (Jordan), paragraph 35 "As to the
  second consideration" (the motives). The card's wording is the report's own structure, not a gloss.
- **Jabotabek completion report on `water-handed-to-companies`** — Report No. 18049, Loan 3219-IND,
  23 June 1998, served as text. The "parallel to but facilitated by the Project" sentence is in the
  Bank Performance summary and does carry both halves in one sentence, as the card says. Paragraph 28
  carries the "would have most likely been turned down by the Bank, following other unsuccessful
  experiences in Indonesia" passage. Both are paraphrased accurately.
- **Senate readings on `banks-that-bank-the-looters`** — both readings are in the report and now both
  on the card: "aggregate deposits ranging from $400 to $700 million at a time" in the executive
  summary, and balances and outstanding loans that "together approached $700 million" by 2003 in
  Finding (2). "More than 60 accounts and certificates of deposit" is the report's own phrase. The
  Turning a Blind Eye finding is quoted correctly and is now given as the subcommittee's finding.
  The three FSA fairness additions — turnover not necessarily proceeds of crime or money into
  Britain, a number of banks having reported suspicions in good time, and no power to name a bank —
  are all in the WealthBriefing report of 9 March 2001, in the FSA's words.
- **Congressional Record re-sourcing on `aid-cover-for-spies`** — page S2874 is in the item, and the
  $60 million, 34 countries, the training subjects, the equipment, the 1973 and 1974 bans, the dozen
  exemptions, the 125 countries and the $117 million are all there, in the wording the card uses.
  Cranston's intelligence-role line is verbatim and is his, not GAO's, so attributing it to him is
  right. The Wikipedia legs are genuinely absent: Engle, Abourezk, "1,500" and "52 countries" occur
  nowhere in the document.
- Also opened and checked myself: the UNDP policy brief (both tables, the combined $74.5 billion, the
  12 per cent ODA comparison, and the absence of any 19-country count), the Chad DSA footnote, the
  Christian Science Monitor of 8 October 1982, the Probe International page, FRUS Editorial Note 420,
  and Kenya Law's search API for both citations.

## 3. The Fitch substitution on `ratings-that-punish-relief` — the call

**Adequate, and the narrowed claim is what the document supports — with two sentences of it narrowed
further and the whole block moved out of paragraph 3.**

I fetched Fitch's "Frontier Markets Quarterly – 1Q21" myself (footer: www.fitchratings.com | April
2021). Its Middle East & Africa table lists "Ethiopia CCC 09-Feb-2021 Downgrade", and under the
heading "Common Framework Raises Risk of Default" it says the downgrade "was triggered by its
intention to make use of the CF, which raises the possibility of a restructuring of debt to the
private-sector that would qualify as a distressed debt exchange under Fitch's sovereign rating
criteria", and that "Unlike the DSSI, which took effect in May'20, the CF ... requires countries to
seek debt treatment by private creditors comparable to that of official bilateral creditors."

This is Fitch in its own voice, about its own action, two months after it, with the action in its own
rating table. A quarterly newsletter is weaker than the action commentary in one respect only: being
a summary, it could leave a second reason out. Nothing the card claims turns on there being only one
reason, so the card does not have to come down. Two sentences did need narrowing, and that came from
reading the document:

- "the bilateral-only suspension scheme carried no such consequence" → "which did not require private
  creditors to take part". The document says the DSSI, unlike the CF, did not require comparable
  private treatment. It does not say the DSSI carried no rating consequence, and Fitch's handling of
  DSSI participation was itself argued over at the time. The card was claiming one step more than the
  page.
- "counts as a distressed debt exchange and leads to a restricted-default rating" → "would count ...
  and would lead to". The RD sentence is conditional and sits in the Newsreel, where its antecedent
  ("The latter") is ambiguous enough that the indicative should not be built on it.

**Separately, this block broke the structure rule and I moved it.** As delivered, paragraph 3 opened
by returning to the 9 February 2021 Ethiopia downgrade, which is paragraph 1's opening example —
the failure HYP records from round 28 ("jumps from small example to big picture back down to the same
small example"), which broke in five entries that round. I dropped the writer's paragraph 3 edit and
added a paragraph 1 edit that inserts the Fitch reasoning right after the Fitch sentence already
there. Nothing is lost, the counter-evidence still lands, paragraph 3 keeps the agencies' settlements,
and the entry comes in 21 words shorter than the writer's version.

## 4. Removals

- **`companies-behind-coups`, the compensation figure.** Confirmed: FRUS Editorial Note 420 contains
  nothing about United Fruit's own tax declaration. I searched it for tax, declare, valuation and
  value. The claim could not stand on that document, and what replaced it — 234,000 acres at
  Tiquisate on 26 February 1953, 172,532 acres at Bananera in February 1954, agrarian bonds, and
  Washington's written objection that bonds were not prompt and effective compensation and the amount
  inadequate under international law — is in the note, word for word in substance. Note for the
  owner: the tax-valuation story is told in published histories of the coup; it is not fabricated,
  it just needs a page someone opens if it is to come back.
- **`companies-behind-coups`, "this has not stopped".** Confirmed as rightly removed: nothing supports
  it, the entry's latest case is 1973, and paragraph 4 already says the records that would show
  whether companies still do this are classified or private. The replacement agrees with paragraph 4.
- **`aid-cover-for-spies`, the 1,500 advisers, 52 countries, Byron Engle as a CIA operative, and
  Abourezk.** Confirmed absent from the Congressional Record item. Rightly removed.
- **`aid-cover-for-spies`, the torture accusation — WRONGLY REMOVED, and I put it back.** The writer
  dropped it with the Wikipedia legs, saying the document does not contain it. It does, twice, in
  Cranston's own remarks: accusations that the programmes "turned a blind eye, or worse, to violation
  of human rights, such as torture and summary execution, by recipient security forces", and
  "Spurred by reports that United States trained and equipped police in Iran, Vietnam, Brazil, and
  other countries were involved in torture, murder, and the suppression of legitimate political
  activity, I and others in Congress prevailed and we banned foreign aid to police forces in 1974."
  Without it the paragraph had also lost the reason Congress acted, and paragraph 3's "congressional
  pressure in one" had lost its referent. The paragraph now carries the second passage, from the same
  page, attributed to Cranston.
- **`aid-cover-for-spies`, the programme's name — also put back.** Cranston's remarks say
  "Channelled mostly through the AID Office of Public Safety", so the name is in the document.
  Without it the paragraph no longer connected to the entry's own `countries` notes, its source list
  or HYP's own table, all of which call it that.
- **`rankings-bent-for-money`, the Saudi king's 2006 statement — removed silently, and I put it
  back.** It is not in the writer's list of removals: "In 2006 Saudi Arabia's king had said he wanted
  the country among the top ten by 2010" was live, had passed an earlier check, and is the Saudi
  side's own stated aim. Dropping it in a round told to fix nine named defects is a change nobody
  asked for.
- I diffed every `old` against its `new` sentence by sentence to find removals the report did not
  mention. The two above are the only ones; everything else the fix dropped is disclosed.

## 5. The case link, and the three empty fields

- **`development-money-through-tax-havens` → `amulsar-gndevaz-jermuk`: survives rule 5, keep it.**
  Rule 5 says `case_ids` "names cases on this map that show the same shape". It does not require the
  cited evidence to cover the case. The shape is on the card itself: the IFC invested $16.4 million
  in Lydian from 2007, and Lydian is recorded as a holding company incorporated in Jersey, registered
  in Alberta, traded in Toronto, with the mine in Armenia. The writer's caveat is right and should
  stay on the record — Oxfam's count is of IFC clients in sub-Saharan Africa in 2015 and Armenia is
  not in it — but the story never claims otherwise, so no story edit follows from the link.
- **The three empty fields are genuinely empty.** I did not take the writer's word for this: I
  searched the full JSON of all 1,182 cases myself. No espionage case (every hit for spy, bugging,
  wiretap, surveillance, CIA, ASIS, NSA, Timor Sea or Greater Sunrise is incidental — surveillance of
  a dam site, a mine security chief's wiretapped order to kill, a contractor's aerial surveillance).
  No case of a Western bank holding a poor country's stolen public money (the nearest,
  `mozambique-bank-privatisations`, is a domestic bank looted by its own management). No
  debt-for-nature case (the only hits are a passing "debt swap" in the Greek bondholder exchange and
  a conservation group's Galápagos work inside a Cambodian REDD case). Leaving all three empty was
  right.

## 6. Length

Totals after my corrections (my counter, within a few words of the writer's):

| id | live | after round 43 as checked |
| --- | --- | --- |
| `rankings-bent-for-money` | 472 | 704 |
| `banks-that-bank-the-looters` | 489 | 633 |
| `water-handed-to-companies` | 516 | 626 |
| `aid-cover-for-spies` | 525 | 610 |
| `ratings-that-punish-relief` | 446 | 576 |
| `carbon-credits-new-land-grab` | 476 | 554 |
| `companies-behind-coups` | 471 | 520 |
| `secret-loans-banks-traders` | 506 | 519 |
| `lending-to-known-thieves` | 460 | 503 |

**Justified, with one exception.** The four big overruns buy things the brief required: two more
countries, a motive finding and a fairness finding on the rankings card; both halves of the Bank's
sentence on the water card; the regulator's actual finding and its three caveats on the banks card;
a whole paragraph re-sourced off Wikipedia on the spies card. None of it is decoration. The exception
is the water card, where 110 words go to fixing a half-quote: the first sentence of the new passage
fixes the defect on its own, and the paragraph-28 sentence (about 45 words) corroborates rather than
carries. That is the one place I would cut without argument.

**Where I would cut if the owner wants them under 500.** Not where the writer suggests. The Georgieva
scene in `rankings-bent-for-money` paragraph 1 is the brief's required opening — "open on a real
scene and tell it completely" — and cutting 60 words out of it trades a rule the owner wrote for a
guide. In order:

1. `water-handed-to-companies`: drop the paragraph-28 sentence. −45, to about 580.
2. `rankings-bent-for-money`: compress the Romer and Lopez-Claros episode in paragraph 3 to one
   sentence (−35, keeping the warning), compress the Jordan trip to a clause (−12), and shorten
   paragraph 1's "Doing Business ranked 190 countries..." explainer (−15). To about 640. Do not touch
   the employing-workers passage: paragraph 1's suspicion sentence ends on workers' protections and
   that passage is the only thing on the card that supports it.
3. `aid-cover-for-spies`: drop the fiscal-1990 sentence (125 countries, $117 million), which is a
   different era from the paragraph's subject. −35, to about 575.
4. `banks-that-bank-the-looters`: give one reading of the deposits in the sentence and the other in a
   clause. −25, to about 605.

Even with all of that, four entries stay near 600. Getting them to 500 means dropping checked record.
My recommendation is to take those four cuts and treat about 650 as the ceiling for these four,
rather than cutting the record back to fit the guide. Seven of the nine were already over 500 before
the round, so the guide is already not what this section does.

## 7. Quoting

Audited over the whole merged text of each entry, both quote characters, not just the new sentences.
**One violation, corrected.** `aid-cover-for-spies` would have carried two quotes from the same
source: the new paragraph 2's "intelligence agencies were given an important role" and paragraph 3's
existing "a dozen exemptions", both from the Congressional Record item at irp.fas.org. I de-quoted
the new one and kept the attribution to Cranston, because paragraph 3 is not in this round's edit set.
After that, every one of the twelve entries holds at most one quote per source and every quote is
under 15 words: 7 words (the Bank's completion report), 1 (WilmerHale), 5 (UNDP), 9 (the Senate
report), 7 (the Monitor), 3 (Cranston).

**Also a style correction, in six places.** The writer's replacements used curly quotation marks.
There is not one curly quote character in any of the 31 live entries; these six would have been the
only ones on the page. Converted to straight double quotes.

## Residuals — all three are real and need hand edits after the merge

1. **`secret-loans-banks-traders` `countries`.** Confirmed. The TCD entry reads note "Glencore held
   98 per cent of foreign commercial debt at end-2016." The July 2019 DSA says 2017 and says
   commercial debt *stock*. The writer's proposed replacement wording matches the document.
2. **`aid-cover-for-spies` Wikipedia source and three country notes.** Confirmed. The Wikipedia
   "Office of Public Safety" item is still first in `sources`, and the URY, BRA and GTM notes came
   through it and the ZNetwork piece. I tested whether the GAO document could re-source them: it
   cannot. Brazil appears there only in the torture-reports sentence; Uruguay and Guatemala only in
   1990-era passages about narcotics and justice training. Those three notes need other documents.
   After the merge no sentence in the story rests on Wikipedia, which was the defect.
3. **`carbon-credits-new-land-grab` missing `case_ids` entry.** Confirmed.
   `northern-rangelands-isiolo-conservancies` exists in `window.CASES` (Kenya, 2007–2025) and is not
   in this entry's `case_ids`, which hold `embobut-sengwer`, `alto-mayo-redd-disney-evictions`,
   `southern-cardamom-redd-chong`, `kasigau-redd-wildlife-works-abuse` and `mai-ndombe-redd` —
   while paragraph 3 is about exactly that case. It should be added.

## Three things found in passing, for the owner, not fixed here

- **`rankings-bent-for-money` paragraph 4** still said "whether China and Saudi Arabia were
  exceptions" — the same two-country framing as the defect this round was fixing, left untouched
  because the writer's brief named the paragraphs it named. I added an edit for it rather than leave
  the defect half-fixed on the page.
- **`banks-that-bank-the-looters`, "none was prosecuted"** is unsourced live text. No document I
  opened says it, and the entry's own WealthBriefing source says the FSA was discussing potential
  breaches of the money laundering regulations with law enforcement, including the police and NCIS.
  Outside this round's defects; worth a round of its own.
- **`water-handed-to-companies` paragraph 2** now says the Bank assigned consultants who advised
  privatisation and, two sentences later, that the Bank had not designed or wanted it. Both are
  sourced, from different pages, but a novice may read them as a contradiction.

## Routes

**Served, fetched by me in this round:** `thedocs.worldbank.org` (WilmerHale PDF);
`documents1.worldbank.org` (Jabotabek completion report and Chad DSA, both as `.txt`, following the
301 from `/text/` to `/txt/`); `your.fitch.group` (Fitch Frontier Markets Quarterly PDF);
`global-prod.acquia.undp.org` (UNDP policy brief PDF); `www.hsgac.senate.gov/wp-content/uploads/...`
(Senate report PDF); `irp.fas.org` (Congressional Record item); `kenyalaw.org/search/api/documents/`
(JSON, four separate queries); `csmonitor.com`; `journal.probeinternational.org`;
`www.wealthbriefing.com`; `history.state.gov`.

**Failed, by route:**

- `https://www.fitchratings.com/research/sovereigns/...` — HTTP 200 with a script-built body and no
  article text. The 9 February 2021 rating action commentary was not opened by me either.
- `https://kenyalaw.org/akn/ke/judgment/...` — judgment and ruling document pages are walled. The
  search API at `kenyalaw.org/search/api/documents/` answers. No attempt was made to get past the
  wall.
- `https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/ACF5F8.pdf` — my first guess at the
  Senate report's path returned 200 but a different document; the URL in the entry's own source list
  serves the report. My own error, recorded so nobody repeats it.
- Not retried, on the record of earlier reviewers: `imf.org` (403 — IMF Country Report 17/246, behind
  Chad's 2016 oil-revenue figures, is still unopened), `webarchive.nationalarchives.gov.uk` (405 —
  the FSA's own March 2001 release), `publications.parliament.uk` (403), `spglobal.com`,
  `moodys.com`.
- `sec.gov/Archives` — not needed and not touched. It wants a contact address in the User-Agent and
  none was invented.

No WebSearch calls were used. Nothing on any card was taken from a page I did not open myself, except
where an entry's live text was outside this round's defects and is recorded as not re-opened.
