# Round 78 — gold custodians and outside reserve managers

Run 20 November 2026. The repo was attached mid-round; everything below came out of the
scripts, except where it says otherwise.

## Environment notes for the next round

The scripts hardcode `/root/cb`. In a fresh container: `ln -sfn <repo>/central-bank-src /root/cb`,
`unzip geo/cities1000.zip` in place (gitignored, 32 MB), and
`pip install --break-system-packages pycountry shapely`. Then `build_final.py` runs clean and
`mk_have.py` works. Without the build there is no `dist/central_bank_independence.html` and
`mk_have.py` dies on it.

`mk_targets.py` knows only corruption_cases, revolving_door and governor_removals. Neither of
this round's two rows can be sliced with it. That is why round after round works the other
rows: the tool that enforces derived targets does not cover these two. Adding them is probably
worth more than any single round of research.

## Gold custodians — 60 of 108 = 56%, and 100% is not available

`to80.py` puts the ceiling at 76 of 108 = 70%. The 32 net places in the silent column have had
their own documents read end to end and those documents name nobody. There is no further
document to find for them, so no number of rounds converts them.

This round moved three places, and all three moves lower the ceiling rather than raising
coverage:

- **PNG** — the host was not blocked. The 2024 annual report served to an ordinary fetch; only
  truncation had hidden it. Note 1(k): "Gold reserves placed on deposit with a financial
  institution", naming no institution and no location. Confirms the standing decision to keep
  PNG out of `gold_abroad_undisclosed`.
- **PER** — read in a real browser. Nota 6 ORO, printed page 215, splits 552,033 troy oz of
  commemorative coins in the Bank's own vault from 562,647 oz of good-delivery bars
  "depositadas en bancos de primera linea del exterior bajo la modalidad de deposito a plazo".
  No institution named. The deposits earn 0.01-0.15 per cent and the interest is booked to
  "Depositos en bancos del exterior" (nota 3).
  **Open question for the curator.** Three rules point different ways: the metal is physical and
  abroad with nobody named, which is the third-state test; it sits on term deposit and earns
  interest, which is gold lending and not custody; and the interest lands on the foreign-bank
  deposits line, which the row excludes outright. Tajikistan was admitted on refinery metal and
  not on its account lines. Peru sits between the two and is left unfiled.
- **OMN** — the IMF's 2025 Central Bank Transparency Code review records that the CBO publishes
  a quarterly Statement of Financial Position and Income Statement and does not publish full
  annual audited statements with notes. If that holds there is no gold note to obtain, and Oman
  is not a blocked host but a place with no document. `to80.py` has no class for that, and the
  difference matters: a blocked host can convert, an unpublished one cannot.

Three of fifteen blocked-column places were misclassified. On that rate the browser job is ten
or eleven hosts and the 70 per cent ceiling is itself too high.

### The browser method, proven

Peru's Incapsula wall does not stop a real browser. The memoria PDF that returns a 5,996-byte
wall body to every script loads in Chrome as 61 pages. Read the balance sheet for the note
number, then type the page into the viewer's page box and screenshot. About ten browser calls
per host from a standing start.

Injecting pdf.js into the bank's page to extract text wholesale was refused as undermining
oversight, which is the same line the brief draws about user-agent spoofing. So every quote
taken this way is read off a screenshot and is `verbatim_unverified` by standard 2.

Documents located but not yet read: Malta (Part III of the Annual Report 2025) and North
Macedonia (nbrm.mk serves its audited IFRS statements; MKD sits in the silent column but the
brief's prose calls it Cloudflare-blocked, and the document appears reachable).

## Outside reserve managers — 81 of 144 = 56%, and the lever is a third state, not more rounds

`searched.json` and `gaps.json` disagree badly on this row. Of the 29 places `to80.py` calls
"never worked", most have a `managers_unavailable` record: MNE, MDV, SMR, BMU, KGZ, UZB, ALB,
DNK, TUR, MAC, WSM, FJI, NPL, BHR, SDN, POL, SRB, UKR and GMB were all worked and found
internal or silent. The "never worked" count is an artefact of `mk_searched.py` not reading
`gaps.json`. **Fix that before planning another round against those 29.**

Of the 116 `managers_unavailable` records, 93 mention external management. Reading them, they
split three ways, and only one of the three is what section 4 of the brief described:

- the bank's own source **states it uses outside managers and names none** — 17 places
- the bank was read and **manages internally** — the larger group: ARG, AUS, AUT, BEL, BLZ, BRB,
  BTN, CAN, COD, COM, DEU, DJI, ESP, ETH, FJI, GIN, GRC, IRQ, NPL, SDN, SMR, STP, SUR, SWE,
  TUN, TUR, VUT, WSM and others. These are true negatives, not withheld names.
- **not reached** — BDI, BGD, CUW, DOM, DZA, FRA, IND, MDG, PHL, PRT, SGP and others.

The row has no counting state for the first group, though the gold row has exactly that in
`gaps.json['gold_abroad_undisclosed']`. Proposed, in
`agents/work/r78/managers_external_undisclosed.json`:

```
AZE BHS BRN CHE CHN CYM FIN HKG HRV HTI MOZ MUS NAM NLD PAK THA ZAF   (17, bank's own source)
ARE                                                                    (1, weak_source: trade press)

  81 of 144 = 56%   now
  98 of 144 = 68%   with the 17
  99 of 144 = 69%   counting ARE
 110 of 144 = 76%   the target, so 11 further places
```

Every entry carries the document and, where a round recorded one, the quote. Nothing here is a
new claim: each is a reclassification of a record an earlier round already made. All are marked
`verbatim_unverified` because the quotes were copied out of `managers_unavailable` prose rather
than re-extracted from the sources.

**This changes the row's headline number, so it is a proposal and not a merge.** Adopting it
needs the same two things the gold third state has: a `..._note` string in `gaps.json` setting
out the test, and the counting change in `coverage.py`. The test should be the strict one used
here — *the bank's own published source states that outside parties manage part of its reserves,
and names none of them* — which is why ARE is flagged and the internal-management places are
excluded.

### Where the remaining 11 would come from

Not from the "never worked" 29; most of those are already negatives. From the not-reached group,
and the brief already points at the two likeliest: the RBI Annual Report chapter on Management
of Foreign Exchange Reserves, and the BSP financial statements note on investments in foreign
securities. Singapore's full MAS Annual Report financial statements, Portugal's Relatorio de
Atividade e Contas, and the Dominican Republic's transparency-section statements are the next
three. If those five are confirmations, the row reaches 103 of 144 = 72 per cent; 76 per cent
needs all of them plus six more, and on this round's evidence the supply of confirmations is
thinner than the supply of internal-management negatives.

## Not done

Malta and North Macedonia gold reads. The ten or eleven genuinely blocked gold hosts. The
not-reached managers documents. TED was tried and is a dead end for this row: its structured
`winner-name` fields are empty for pre-2023 notices, and none of Denmark, Finland, Poland or
Croatia appears under CPV 66140000 or 66150000.
