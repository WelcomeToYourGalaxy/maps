# Suspected patterns: the brief

Rewritten 15 Nov 2026. Replaces every earlier version of this file.

A suspected pattern is **a large, well-known suspicion in the main vein of this map — outside money and
the harm it does — told as one continuous story for a reader who has never heard of it, and built
entirely from things already on the public record.** It lives in `window.HYPS` in `base.html`, renders
inside the "Patterns Behind the Scenes" section of the left-hand box under its own sub-heading,
"Suspected patterns", below the documented patterns, and opens its own card through `detailHyp()`.

## What the owner asked for, in their words, and what it rules out

15 Nov 2026, on the thirteen that were there: *none of the writeups should be about arguments
discovered by analyzing this map's data*; several were *dry* and *don't belong*; *I asked for spicy
hot topic exciting conspiracies that are large scale/global or intl in scale, just not too woo woo and
still remaining in the main vein of the topic, not tangential*; *it looks like you're trying to argue a
pattern forward from either little data or running with the narrative only, which makes it look like
the exact opposite of trustworthy. Pull from existing knowledge by researching this realm. An example:
Perkins disclosed CIA operatives in WB/IMF. That is not an argument extrapolated from the narrative,
nor pulled from the map's data*; and again *continuous organic rundowns written in captivating
storytelling manner for novices, like a scary story, not categorical snippets*.

So, concretely:

1. **Never built from this map's own data or method.** No entry may rest on a count of the cards, a
   finding from a research round, or how the map's researchers read documents. Those go in the
   handoff as research leads. All thirteen earlier entries were retired for this reason or for being
   dry; they are archived in `rounds/r27_hyps_retired.json` and must not come back.
2. **Built from the public record of the world.** Each entry joins things that are already
   documented — insider disclosures (Perkins, Stiglitz), leaked documents (IMF board minutes, World
   Bank memos), official investigations (WilmerHale), court rulings, peer-reviewed studies,
   investigative journalism — into the larger suspicion they point at. The pieces are sourced; the
   pattern that joins them is what is suspected.
3. **Spicy and big, not tangential and not woo.** The test: is this something an informed reader has
   heard argued about the IMF, World Bank, aid, debt or foreign investment, and does it change how
   they see who benefits? Is every load-bearing fact something a mainstream outlet, court, study or
   the institution itself has published? Both yes, it can go in.
4. **Fair.** Where a named living person is involved, give what the record says and their denial.
   Where a popular version of the story is false, say so in the story (Hambantota is the model: the
   debt-trap version fails, the dual-use version stands).

## The rules

1. **It is never a finding, and nothing on the map rests on one.** The dashed box and the "not
   documented" kicker stay.
2. **Title: a short plain statement of the suspicion.** "Aid programmes used as cover for spies", not
   a question and not a sentence about evidence.
3. **Every fact in the story comes from a page someone opened, and the page is in `sources`.** The
   card lists the sources under the story. Quotes under 15 words, one per source, paraphrase the rest.
4. **Every batch is checked by a separate agent before it goes on the page**, against the sources and
   against any case card the story mentions. Check figures against the card, not against the report
   the card came from.
5. **Link the map.** `case_ids` names cases on this map that show the same shape; `countries` names
   where the record sits. Every id must exist in `window.CASES`. Mentioning a documented pattern on
   the map (spy agencies and the lenders; money kept flowing after the killings; aid and UN votes;
   tied aid) is good where it genuinely bears on the story.
6. **A confirmed one graduates** into `PATS` with `status: "documented"` and `graduated_to`. **A
   refuted one stays** with `status: "refuted"` and `refuted_by`.
7. **It does not filter the cases.** `setHyp()` leaves every mark on the map where it is.

## How it is told

Four paragraphs, no headings, about 350 to 500 words:

1. **Open on a real scene and tell it completely**: a date, a place, a person doing something, then
   everything the story needs about that one case (the figures, what happened next, the denial).
   Then say plainly what is suspected and why it matters to the reader.
2. **A second, different case** from the record, with its figures and who disclosed or found it.
3. **More of the record from further out**: a third case, a study that counts many cases, the
   counter-evidence, and the cases or documented patterns on this map with the same shape.
4. **What is still hidden and what record would settle it**, in plain sentences. No labelled fields.

The story only ever moves outward: the opening example, the suspicion, other examples, the wider
record, what would settle it. **Once paragraph 1 is done, no later paragraph goes back to add detail
to the opening example.** The owner, round 28: opening on a great example and moving to the larger
pattern works, but a second paragraph that returns to the same example *jumps from small example to
big picture back down to the same small example*, which is repetitive and breaks the flow. Naming, in
paragraph 4, which records about it would settle the question is fine.

The unease comes from the specifics (how much money, who knew, what was kept secret), never from
adjectives, rhetorical questions, aphorisms or a one-line punch at the end. No purple prose, no
crescendo sentences, no manufactured significance. Spell out every connection a novice would need.

## The shape

```
{
  id, title, kind: "suspected", years: [first, last],
  conviction: "One line: what is on the record and what is suspected. Not displayed.",
  story: ["four paragraphs"],
  missing: "What has not been done. Not displayed.",
  would_settle: "The obtainable record that would settle it. Not displayed.",
  countries: [{ iso3, role, note }],
  case_ids: ["case-id", ...],
  sources: [{ title, publisher, year, url }],
  status, graduated_to, refuted_by     // only once it stops being open
}
```

`entryPts()` flies to the case points when there are any, otherwise to the cases in the countries
named.

## The twenty-one that are there now (round 28)

| id | Title | Built on |
| --- | --- | --- |
| `aid-cover-for-spies` | Aid programmes used as cover for spies | Abbottabad vaccination; Office of Public Safety 1962-74; ZunZuneo; Timor-Leste bugging under an aid project |
| `forecasts-inflated-to-sell-loans` | Forecasts inflated so countries borrow more | Perkins; Wapenhans 1992; Ansar and Flyvbjerg's 245 dams; IMF WP/20/229; Yacyretá |
| `lending-to-known-thieves` | Lenders kept funding dictators they knew were stealing | Blumenthal report on Zaire; 1997 Jakarta memo; Bataan |
| `aid-into-offshore-accounts` | Aid money turns up in Swiss bank accounts | Andersen, Johannesen and Rijkers 2020 and its handling; Ndikumana and Boyce on capital flight |
| `rescues-that-rescue-banks` | Rescue loans that rescue the banks, not the country | Leaked IMF board minutes of 9 May 2010; ESMT 2016; Mexico 1995 and the tesobonos |
| `lenders-expect-the-riots` | The lenders expect the riots their conditions cause | Stiglitz and the leaked Ecuador strategy; Walton and Seddon; Abouharb and Cingranelli; Kenya 2024 |
| `rankings-bent-for-money` | Global rankings bent for countries with money to give | WilmerHale on Doing Business (China, Saudi Arabia); Romer; employing workers indicator |
| `secret-loans-banks-traders` | Secret loans arranged by banks and traders, kept from the public | Mozambique; Congo and Chad trader loans; AidData $385bn; Goldman and Greece |
| `rescue-money-timed-for-elections` | Rescue money timed to keep friendly governments in power | Russia 1996; Argentina 2018 and 2025; Dreher et al. 2008 |
| `ports-that-become-naval-bases` | Chinese-financed ports that may be future naval bases | Djibouti; Ream; AidData 2023 shortlist; Chatham House on Hambantota |
| `poor-countries-take-the-poison` | Poor countries chosen to take rich countries' toxic waste | Probo Koala; the 1991 Summers memo; Koko 1988; plastic waste after China's 2018 ban |
| `markets-opened-for-subsidized-food` | Markets forced open for rich countries' subsidized food | Haiti rice and Clinton's apology; Ghana poultry; US-grown food aid |
| `carbon-credits-new-land-grab` | Carbon credits driving a new land grab | Ogiek evictions; Blue Carbon deals; Northern Kenya soil-carbon ruling |
| `loans-cut-off-to-topple-governments` | Loans cut off to bring down governments the West dislikes | Helms notes and Chile 1970-73; Shultz letter on Nicaragua 1985; IDB loans withheld from Haiti 2001 |
| `spying-at-the-negotiating-table` | Spying on poor countries to win resource and trade deals | Timor-Leste cabinet bugged 2004 and Witness K; GCHQ at the 2009 G20; NSA and Petrobras |
| `bribes-built-into-financed-contracts` | Bribes built into the contracts that loans pay for | Lesotho Highlands convictions; Siemens 2008 settlement and World Bank debarment |
| `aid-traded-for-arms-sales` | Aid money used to win arms sales | Pergau dam ruling 1994; BAE radar sale to Tanzania |
| `advisers-who-profit-from-the-sell-off` | Foreign advisers who profit from the privatisations they design | Harvard's Russia project and the 2005 settlement; loans-for-shares 1995 |
| `seed-laws-for-seed-companies` | Seed laws pushed on poor countries that restrict farmers' own seed | Enabling the Business of Agriculture; CAFOD on World Bank seed conditions; Oakland Institute |
| `pension-funds-buy-up-farmland` | Pension funds and university endowments behind land grabs | Harvard endowment and TIAA farms in Matopiba (GRAIN, Rede Social) |
| `development-money-through-tax-havens` | Development money that flows through tax havens | Oxfam 2016 on IFC clients in sub-Saharan Africa |

Directions that fit the standard and are not yet written: debt-for-nature swaps with unpublished
terms; vulture-fund lobbying; the US and European hold on the two top jobs. The 1974 US-Saudi
petrodollar arrangement was considered in round 28 and left out as too far from aid and lending.

## The 15 Nov 2026 check

A separate checker opened the sources for all thirteen: about 330 claims, 53 fixes applied
mechanically, none cut. Log: `rounds/r27_hyps_check.json`; the checked data: `rounds/r27_hyps_new.json`.
What it caught, as classes to watch for next time: a figure taken from a page that never loaded (the
CIA reading-room link opens only the home page); a source's "around" turned into "more than"; a
share ("half in Switzerland") the paper never states; a payment attributed to three countries' regulators
when only two were paid; a figure on a map card (Yacyretá) quoted differently from the card; an
agency named as doing something no source names it doing. Weakest two after fixes:
`aid-cover-for-spies` (the Office of Public Safety case now rests mainly on Wikipedia) and
`secret-loans-banks-traders` (the Congo paragraph was rebuilt on Debt Justice and the IMF after the
Global Witness pages would not load).

## The round 28 check

Three separate checkers: one on the eleven retold entries (diffed against the round 27 text, so only
new or moved claims were re-checked) and two on the eight new ones. 61 fixes applied mechanically,
none failed. Log: `rounds/r28_hyps_check.json`; draft `rounds/r28_hyps_draft.json`; checked data
`rounds/r28_hyps_final.json`. What it caught, as classes to watch for next time:

- **The structure rule broke again in drafting.** Five new or retold entries slipped back to the
  opening example in paragraph 3 (Abbottabad, Greece, Lesotho, Pergau, Timor, the Harvard and TIAA
  farms). Check for this on every draft, not only the old ones.
- **A source's preliminary finding written as a ruling** (Incra on TIAA), and **a court action
  attributed to the wrong body** (the Bahia court on Harvard's tract, not Incra).
- **Study scope misstated**: Ndikumana and Boyce's $443bn and $195bn cover 33 countries, not 40.
- **A one-source figure where a better one exists**: the tesobonos now use Lustig (Brookings 1995),
  and Chile's lending collapse uses the 1975 Senate report instead of a school project page.
- **A claim that both cases ended the same way when they did not** (Greek bondholders took a write-down
  in 2012; Pergau ended in a ruling, not a settlement).
- **FOIA credited with documents that were already public** (the 2001 Harrington letter on Haiti).

Weakest after fixes: `spying-at-the-negotiating-table` (paragraph 3 is a single sentence; a third
documented case would strengthen it) and `pension-funds-buy-up-farmland` (rests largely on GRAIN,
Rede Social and Chain Reaction Research; the Incra finding is preliminary).
