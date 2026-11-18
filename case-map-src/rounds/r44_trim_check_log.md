# Round 44 check log — length cuts and three residual fixes on suspected patterns

Checker: separate agent, 17 November 2026. Subject: `rounds/r44_trim.json` (nine story edits on four
`window.HYPS` entries, two added sources and three country-note recommendations) against
`docs/HYP.md`, `rounds/r43_hypfix_check_log.md`, the live `window.HYPS` in `base.html`, and the
documents themselves. Output data: `rounds/r44_trim_checked.json`. `base.html` was not touched,
nothing was built, nothing was committed.

**Verdict: apply all four, with the nine corrections in the checked file.** All four entries carry
`stands-with-corrections`; none is `cut`. No cut removed record the report does not disclose, and the
three repairs hold up against the documents. What I corrected is of one kind: four trims that saved a
word by weakening a claim's precision beyond what its page says, one that put a journalist's gloss in
a regulator's mouth, one new sentence that needed its attribution, and the Guatemala note.

## 1. The `old` strings and the word counts

I extracted `window.HYPS` from `base.html` by brace-matching and compared every `old` string myself.
All nine match a whole live story paragraph **exactly once** inside their entry, and no two edits in
an entry share an `old`. Three of the nine do not appear as literal byte strings in `base.html`
because the paragraph contains escaped quote characters in the source; they match the decoded entry,
which is what the merge applies to. The report's "matches once in the whole of `base.html`" is true
only after unescaping — worth knowing before anyone runs a byte-level dry run.

Counts recounted from the live text with my own counter:

| id | live | as delivered | after my corrections | writer's figure |
| --- | --- | --- | --- | --- |
| `rankings-bent-for-money` | 704 | 667 | 669 | 667 |
| `banks-that-bank-the-looters` | 631 | 616 | 621 | 616 |
| `water-handed-to-companies` | 626 | 612 | 616 | 612 |
| `aid-cover-for-spies` | 608 | 580 | 580 | 580 |

Every figure in the report is right.

## 2. Did any cut remove checked record?

I diffed each `old` against its `new` sentence by sentence rather than reading the report's account.
**Record-bearing text was removed in three places, not two.** All three are disclosed in the report,
but the brief I was given, following the report's summary line, understates the water card.

1. **`aid-cover-for-spies`, the fiscal-1990 sentence** (five US cabinet-level departments, police from
   125 countries, about $117 million). Genuine record: I reopened the Congressional Record item at
   irp.fas.org and the sentence is there verbatim in substance. This is a length cut the round-43
   checker asked for, not a defect fix. Nothing is stranded by it — see section 3.
2. **`water-handed-to-companies`, the paragraph-28 sentence** (in the late 1980s a
   private-participation option would most likely have been turned down by the Bank, after other
   unsuccessful experiences in Indonesia) **and the old closing sentence** ("The Bank's own account,
   then, is that its loan helped Jakarta's privatisation along without the Bank having designed or
   wanted it"). This is record from the Bank's own completion report, and it is the cut the round-43
   checker named first and said it would make "without argument". The loss of "or wanted" follows
   consistently: that half rested on the sentence that went.
3. **`banks-that-bank-the-looters`, paragraph 4's closing sentence** ("Only leaks and occasional
   inquiries have shown any of it"). Not record — no figure, date, name, quote or attribution — and
   the paragraph stands without it. The writer's own doubt about it is reasonable but I would not
   spend words putting it back.

Nothing else is gone. Everything else in the nine edits is wording, and I checked the survivors one by
one: on the rankings card the four countries, the Jordan trip and its result, 30 places to 62nd, the
paid advisory contracts, the king's 2006 aim, the "likely" finding and the three possible motives, the
UAE by-product, Azerbaijan's audit and the three uncounted reforms, Djankov's stated disbelief, the
reported animus, the no-involvement finding, the cancellation, Romer's claim, retraction and
resignation, and Lopez-Claros's denial; on the banks card both Senate readings of the Riggs business,
the 60-plus accounts, the $13 million and $35 million, the $25 million and $16 million, the FSA's 42
relationships, 23 banks, $1.3 billion and 98 per cent, and the FinCEN Files figures; on the water card
the completion-report sentence with both halves and its quote.

Four trims saved a word by weakening a claim past its source, and I put those back:

- **The Jordan instruction.** "told the Doing Business team to drop Jordan from the top of the draft
  Top Improvers list" turns an instruction to change data into an instruction about a ranking.
  WilmerHale paragraph 20, which I read in the Bank's own copy of the report: Djankov "instructed the
  Doing Business team to find a way to alter the data such that Jordan fell from its first-place
  position in the Top Improvers list". Corrected to "to alter the data so that Jordan fell from the
  top of the draft Top Improvers list".
- **"then" before "the Bank's development economics director".** The report says "by then serving as
  the DEC Director". Restored.
- **"outstanding" before "loans"** on the banks card. It is part of the Senate report's own
  description of what the $700 million figure counts. Restored.
- **The second "often"** in "Banks can stop a suspicious payment but are often not required to; filing
  a report is enough." The live text hedged twice; the trim left an absolute statement about what the
  law requires. Restored.

One more correction of the same family, for a novice reader rather than a source: the trimmed
employing-workers sentence ran three "it"s with two different referents, so "an independent panel it
set up in 2013" is now "an independent panel the Bank set up in 2013". To pay for those six words I
recast "In neither the Saudi nor the Azerbaijan change did WilmerHale find evidence that the
president's office or the board was involved" as "WilmerHale found no evidence that the president's
office or the board was involved in either change" — same finding, five words shorter.

## 3. Does anything surviving now lack its support?

- **The employing-workers passage, the risk the cut list flagged: safe.** Every element survives — the
  higher scores for weaker worker protections until 2009, the indicator's name, the 2009 suspension
  after pressure from unions, the ILO and the US Congress, and the 2013 panel's recommendation to
  remove it permanently. Paragraph 1's suspicion sentence still ends on workers' protections with its
  support intact. **But the passage was touched, contrary to the report's "left untouched":** two
  sentences were merged with a colon and two noun phrases became pronouns. Nothing was lost by it;
  the report's wording is simply inaccurate, and it is the reason I read that passage word by word.
- **`aid-cover-for-spies` after the fiscal-1990 cut: nothing stranded.** Paragraph 3's quote "a dozen
  exemptions" has the 1974 ban in paragraph 2 as its antecedent, which stays. The claim the cut
  sentence had carried — that US police assistance continued and grew after the ban — now rests on
  that quote alone, which is thinner but is supported by the same page. No country note refers to the
  cut figures, and I searched the whole live entry outside the story for 117, 125, fiscal and 1990:
  `conviction`, `missing` and `would_settle` do not mention them.
- **`water-handed-to-companies`: the new sentence does the job the removed one did**, and
  "assigned consultants who advised privatisation" in the sentence before it is carried by the ICIJ
  piece, which I opened.
- **`banks-that-bank-the-looters`: both Senate readings are still attributed to the subcommittee** by
  the sentence's own opening ("The subcommittee gives the size of that business two ways"), so
  dropping "and, in its findings," strands nothing.
- I checked the same pattern across all four entries and found no other compressed sentence that
  leaves a later claim without its basis.

## 4. The three repairs

**"None of them was prosecuted" — the replacement stands.** I opened the entry's own WealthBriefing
report of 9 March 2001. Phillip Thorpe, the FSA's **managing director** (my brief called him the
regulator's chairman; the page does not), is quoted: "Potential breaches of the money laundering
regulations are also being discussed with the appropriate law enforcement authorities." The next
sentence of the report reads: "These include the police and the National Criminal Intelligence
Service." Both the quote and the gloss are there, and so are the other three caveats already on the
card. The replacement does not imply a prosecution: it says, in the past tense of a March 2001
report, that potential breaches were being discussed with law enforcement, and makes no claim about
charges or outcomes either way. **One correction.** As delivered the clause read "potential breaches
..., it said, were being discussed with the police and that service", which puts the publication's
own naming of the police and NCIS into the regulator's mouth — the regulator said "the appropriate
law enforcement authorities". It now reads "were being discussed with law enforcement authorities,
among them the police and that service". No quote was added, so the entry still holds one quote per
source.

**The water card's new joining sentence — supported, with its attribution added.** I opened the ICIJ
piece (Andreas Harsono, "Water and politics in the fall of Suharto"), which is already on the card. It
carries all three elements in three consecutive sentences: "Both organizations were encouraging
Indonesia at the time to privatize its utilities, according to World Bank loan documents. The World
Bank expected that the loans would facilitate privatization by bolstering the water and sewage
infrastructure, making the waterworks a more attractive investment. The World Bank also appointed
consultants to advise PAM Jaya on the privatization." So the sentence does not have to come down or
be narrowed. Two things did need fixing: ICIJ attributes both claims to World Bank loan documents, and
the new sentence sits directly after one that names the completion report, so an unattributed claim
reads as the completion report's; and ICIJ says "the loans", the Bank's and the Japanese fund's
together, not this loan alone. The sentence now opens "the Bank's loan documents show it was
encouraging Indonesia to privatise its utilities and expected the loans to make the waterworks a more
attractive investment".

**The three country notes on `aid-cover-for-spies`.** I opened National Security Archive EBB 324
myself. Brazil and Uruguay both check out: "Dan Mitrione, Director of the U.S. AID Office of Public
Safety (OPS) in Uruguay and the main American advisor to the Uruguayan police at the time, had been
held for ten days by MLN-Tupamaro insurgents", found dead on the morning of 10 August 1970, killed by
the Tupamaros; and "In the mid 1960's, he was hired by the U.S. AID Office of Public Safety to train
policemen in Brazil and Uruguay." The string 1964 does not occur anywhere in the briefing book, so
dropping "from 1964" from the Uruguay note is right and I would not restore it from anywhere else.
The second half of the Brazil note is in the Congressional Record item, which I reopened: "Spurred by
reports that United States trained and equipped police in Iran, Vietnam, Brazil, and other countries
were involved in torture, murder, and the suppression of legitimate political activity, I and others
in Congress prevailed and we banned foreign aid to police forces in 1974."

**Guatemala — my recommendation: the superlative comes off and the replacement stays, tightened.** I
opened the AHPN report (Del Silencio a la Memoria, volume 1, chapter II, at derechos.org/nizkor). It
states that declassified US documents record the Public Safety Program in Guatemala beginning in 1956,
on the basis of Fred G. Fimbres's report of 9 April 1956 for USAID's ICA, and that the strengthening
of coordination between Guatemala's security forces in the 1960s "surgió con la asesoría de la Oficina
para la Seguridad Pública de la USAID". I searched it for Centroamérica, más grande, el mayor and
largest: it ranks no country programme, so the superlative is unsupported whichever way the owner
decides. On the choice itself I side with keeping the country: `countries` is a per-country line
saying what the record there is, not a fixed claim, and the record there is substantial and now
sourced; dropping GTM would take Guatemala off a map of police-training cases because the old note
overclaimed, which punishes the country for the writer's predecessor. I did trim the note: the
"USAID's own five-year analysis covers 1967-1971" clause gives a document's date range and tells a
reader nothing about Guatemala. The note reads "US Public Safety Program from 1956; USAID's Office of
Public Safety advised the coordination of Guatemala's security forces in the 1960s." The writer's
flag is right and should stay on the record: the 1956 start predates the Office of Public Safety, so
the note keeps "Public Safety Program" for the 1950s and OPS for the 1960s.

Both added sources were opened by me and both are needed: EBB 324 for Uruguay and Brazil, the AHPN
report for Guatemala.

## 5. Word counts and the 650 question

**The writer is right, and 650 is not reachable on the rankings card without dropping record.** I
tested the arithmetic rather than taking it. Compressing Romer and Lopez-Claros to one sentence saves
12 words as delivered, not the 35 the round-43 checker estimated, because HYP.md's fairness rule
requires both the retraction and the denial to stay and both are long clauses. The 190-countries
explainer had about 4 spare words in it, not 15. After the two compressions the checker named, what is
left in the entry is countries, figures, findings, denials and the opening scene the brief requires.
I found roughly ten more words of wording slack across the entry and spent five of them paying for my
own corrections; the remainder would take it to about 665, not 650. Going below that means dropping
one of: the UAE by-product, the king's 2006 aim, the three-motive fairness finding, the
no-involvement finding or the 2013 panel. None of those should go for 15 words. The other three cards
are at 621, 616 and 580, all inside the 650 the round-43 checker recommended.

## 6. Quoting

Audited over the whole merged text of each entry, both quote characters, new sentences included. Every
entry holds at most one quote per source and every quote is under 15 words: the rankings card one
quote, "likely" (1 word, WilmerHale); the banks card one, "ranging from $400 to $700 million at a
time" (9 words, the Senate report); the water card one, "parallel to but facilitated by the Project"
(7 words, the Bank's completion report); the spies card one, 'a dozen exemptions' (3 words, the
Congressional Record item, in paragraph 3, which this round did not touch, and which stays the entry's
only quote from that source because round 43's de-quoting of the Cranston passage survives the trim).
No quote was added by any of the three repairs. There is not one curly quotation mark in the delivered
file or in my corrections.

## 7. Routes

**Served, fetched by me in this round:** `www.wealthbriefing.com` (FSA/Abacha report of 9 March 2001);
`www.icij.org/investigations/waterbarons/...` (Harsono); `nsarchive2.gwu.edu/NSAEBB/NSAEBB324/index.htm`;
`derechos.org/nizkor/guatemala/doc/pn3.html`; `thedocs.worldbank.org` (WilmerHale PDF, read as text);
`irp.fas.org/gao/920300-train.htm`.

**Failed, by route:** none. Every page I needed answered on the first request with the research
user-agent. No WebSearch calls were used.

**Not retried, on the writer's record:** `znetwork.org/znetarticle/...` (403),
`web.archive.org/web/2020/...` for the same page, `www.gao.gov/assets/id-76-*.pdf` (403),
`www.ojp.gov/ncjrs/virtual-library/abstracts/...`, `history.state.gov/search`,
`apps.dtic.mil/sti/tr/pdf/ADB117660.pdf`, `statecraft.org`. None of them bears on a claim that
survived this round.

## Safe to apply

All four entries are safe to apply from `rounds/r44_trim_checked.json`: `rankings-bent-for-money`,
`banks-that-bank-the-looters`, `water-handed-to-companies` and `aid-cover-for-spies`, each with the
corrections above already written into its `new` strings. The three country notes on
`aid-cover-for-spies` are hand edits after the merge: Uruguay and Brazil as the writer wrote them,
Guatemala with the tightened replacement note in the checked file, and the two added sources appended
to that entry's `sources`.
