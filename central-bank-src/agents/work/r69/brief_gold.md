# Round 68 — gold custodians

Read `brief_common.md` first.

## What this row records
**Where a central bank's monetary gold physically sits, and who holds it.** The
relation is `holds its gold reserves in custody`. It is not how much gold the
bank has — the map already has tonnage from another dataset — and it is not who
manages or invests the gold.

## The rules that decide a record
- **A place must be named.** A bank recorded as holding its OWN gold must name
  the vault and the city: every self-custody node on the map is named
  `"<Bank> vaults, <City>"` or `"<Bank> strongroom, <City>"`. A statement that
  the bank "has in its custody" 19 tonnes, with no vault and no city, is held,
  not filed. This refusal has already cost one country a round, so check it.
- **Gold held in accounts for yield is not custody.** One bank names six
  institutions holding 19.91 tonnes in gold *accounts*; none was filed.
  Likewise gold **lent**, or **deposited at interest**, does not say where the
  metal sits. Custody, earmarking and allocated holdings do.
- **"On deposit with" is ambiguous and is not enough on its own.** One bank's
  accounts say its gold is "on deposit with the Federal Reserve Bank" — no city,
  no named Reserve Bank, no custody wording. That is held, and it is held
  correctly: naming New York would be your inference and not the source's.
- **A country-level answer naming no institution is a blank, not a record.**
  "London", "primarie banche centrali", "abroad", "specialised foreign
  repositories", "a financial institution", "foreign banks" — all blanks.
  Several banks publish exactly this, and each is a documented blank worth
  recording.
- **Keep storage and management apart in the wording.** A bank holding gold "as
  bailee" leaves ownership with the depositor.

## Where the answer actually is — in order of what has worked
1. **The note to the audited financial statements**, not the bank's gold page or
   its reserves web page. Four countries disclosed a location table only there.
   Search for the statements PDF, download it, and grep it.
2. **The FX-reserves STRUCTURE or COMPOSITION section, which is a different
   section from the gold note.** This is the most recently found lever and it
   overturned a country that had been a "confirmed blank" for several rounds:
   its gold note named no institution, while its annual report's "Structure and
   profitability of FX reserves" itemised the reserves as foreign securities
   59.16%, FX in accounts abroad 22.04% and **gold in the bank's own vaults
   13.26%** — which placed the whole holding. **Read that section before calling
   a bank silent.**
3. **The accounting-policy note**, which can sit two thousand lines before the
   reserves note.
4. **A counterparty-concentration or credit-risk table**, which sometimes names
   the holder against the gold line where the narrative does not. Note the trap:
   a table that lists an institution against *cash and securities* and not
   against gold has not named a gold custodian.
5. **The last pages of the report.** One bank's audit and reserves disclosures
   sit on pages 246-249 and are image-only scans that `pdftotext` returns blank
   while the rest of the document extracts perfectly. OCR the last pages before
   calling a report silent.

## Routes that are dead — do not spend a call on them
- **The custodian's side.** The Bank of England publishes monthly custody
  tonnage and the number of central bank account holders and has **refused** to
  publish their identities. The Banque de France says the details are
  confidential. The Federal Reserve Bank of New York the same. **Custodian
  identity on this row comes from the depositor's side only.**
- Asking a bank directly. Four have refused a storage-location request and five
  more did not reply.

## Your assignment
Every code below came out of a script that read the live data this session: it is
the gold row's absent list, **minus** the 107 places that already carry a
documented negative in the map's own `gold_unavailable` file. So these 27 are the
places that have not been closed and have no custodian:

```
AIA ATG CUB DMA ERI ESP GRC GRD IRN KNA LAO LCA LKA MRT MWI NPL NZL
PSE SOM SSD TJK TKM TLS TWN VCT VNM YEM
```

Two things to know about that list before you spend anything on it:

- **AIA ATG DMA GRD KNA LCA VCT are the eight Eastern Caribbean states** and
  they share one central bank. That bank has been confirmed to hold **no gold at
  all** — its full Independent Auditors' Report and Financial Statements to 31
  March 2025 were read in three passes, 241,961 characters, and the word gold
  does not appear. **Do not research them.** They appear on the absent list
  because the row's denominator counts places, not because they are open. Seven
  of your twenty-seven are therefore already answered; say so in `blanks` and
  move on.
- **PSE has no currency of its own**, so treat a gold claim for it with care.

**MWI is the single best lead on this row** and it is the one I am handling
myself, not you: the bank ran a domestic gold purchase programme and reversed it
in 2026, so its statements should say where the metal sits, but its document
list loads by script and blocks automated readers. **Skip MWI.**

That leaves **CUB ERI ESP GRC IRN LAO LKA MRT NPL NZL SOM SSD TJK TKM TLS TWN
VNM YEM** as your real work. ESP GRC LKA NPL TWN are each recorded in this
project's notes as publishing a gold line or valuation and naming no custodian,
**but their full annual reports were not all read** — so they are unworked rather
than closed, and the FX-reserves-structure lever above has not been tried on
them. Start with the ones that publish audited statements in a language you can
grep.

## Output
```json
{"records": [{"cb_iso3": "XXX", "country": "", "central_bank": "",
  "entity": "Holder as the map should name it",
  "name_as_stated": "as the source words it",
  "entity_type": "central bank | bank | central bank's own vault | international body | firm",
  "entity_hq_city": "City or null", "entity_hq_iso3": "ABC or null",
  "relation": "holds its gold reserves in custody",
  "detail": "At least 90 characters: the amount, the date, the wording the source uses, and the vault and city if it names them.",
  "source_title": "", "source_url": "https://…", "weak_source": false,
  "quote": "under 25 words, word for word"}],
 "blanks": [{"iso3": "XXX", "kind": "confirmed blank | vein closed | not reached | refused",
   "note": "The document, the year, the section and the page or note number, and what it says instead."}],
 "checked_not_in_assignment": [], "leads_not_opened": []}
```
Head office keys for a tie are **`entity_hq_city`** and **`entity_hq_iso3`**. A
self-custody node's city is the city of the vault.
