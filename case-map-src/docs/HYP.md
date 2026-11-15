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

Four paragraphs, no headings, about 400 to 500 words:

1. **Open on a real scene** from the record — a date, a place, a person doing something — then say
   plainly what is suspected and why it matters to the reader.
2. **What is already documented**, with its figures and who disclosed or found it.
3. **More of the record**, including the counter-evidence and denials, and the cases on this map with
   the same shape.
4. **What is still hidden and what record would settle it**, in plain sentences. No labelled fields.

The unease comes from the specifics — how much money, who knew, what was kept secret — never from
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

## The thirteen that are there now (15 Nov 2026)

| id | Title | Built on |
| --- | --- | --- |
| `aid-cover-for-spies` | Aid programmes used as cover for spies | Office of Public Safety 1962-74; ZunZuneo; CIA fake vaccination in Abbottabad |
| `forecasts-inflated-to-sell-loans` | Forecasts inflated so countries borrow more | Perkins; Wapenhans 1992; Flyvbjerg's 245 dams; IMF WP/20/229 |
| `lending-to-known-thieves` | Lenders kept funding dictators they knew were stealing | Blumenthal report on Zaire; 1997 Jakarta memo; Bataan |
| `aid-into-offshore-accounts` | Aid money turns up in Swiss bank accounts | Andersen, Johannesen and Rijkers 2020 and its handling |
| `rescues-that-rescue-banks` | Rescue loans that rescue the banks, not the country | Leaked IMF board minutes of 9 May 2010; ESMT 2016 |
| `lenders-expect-the-riots` | The lenders expect the riots their conditions cause | Stiglitz and the leaked Ecuador strategy; Walton and Seddon; Abouharb and Cingranelli; Kenya 2024 |
| `rankings-bent-for-money` | Global rankings bent for countries with money to give | WilmerHale on Doing Business; Romer; employing workers indicator |
| `secret-loans-banks-traders` | Secret loans arranged by banks and traders, kept from the public | Mozambique; Congo and Chad trader loans; AidData $385bn; Goldman and Greece |
| `rescue-money-timed-for-elections` | Rescue money timed to keep friendly governments in power | Russia 1996; Argentina 2018 and 2025; Dreher et al. 2008 |
| `ports-that-become-naval-bases` | Chinese-financed ports that may be future naval bases | Djibouti; Ream; AidData 2023 shortlist; Chatham House on Hambantota |
| `poor-countries-take-the-poison` | Poor countries chosen to take rich countries' toxic waste | The 1991 Summers memo; Probo Koala |
| `markets-opened-for-subsidized-food` | Markets forced open for rich countries' subsidized food | Haiti rice and Clinton's apology; Ghana poultry; Mexico corn |
| `carbon-credits-new-land-grab` | Carbon credits driving a new land grab | Blue Carbon deals; Ogiek evictions; Northern Kenya soil-carbon ruling |

Directions that fit the standard and are not yet written: the 1974 US-Saudi petrodollar arrangement
and the debt crisis it fed; Harvard's advisers and Russia's privatisation; debt-for-nature swaps with
unpublished terms; vulture-fund lobbying; the US and European hold on the two top jobs.

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
