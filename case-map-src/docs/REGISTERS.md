# Registers of harm: what exists per kind of money, scanned 17 Nov 2026 (round 45)

Written because the coverage panel's low rows were being read as "work not done yet" when most of
them are "no list exists to work from". Each row below says whether a harvestable register of harm
exists, what it holds, and whether it is worked. **A register is a published list of instances of
harm. A list of deals is not a register** — it is a denominator, and dividing by it is what makes
those rows small.

| Kind of money | Register of harm | Size | State |
| --- | --- | --- | --- |
| World Bank / IFC | ICIJ's displacement index; the fourteen complaint offices | 968 projects (422 confirmed); 3,004 complaints | ICIJ 26% matched; complaints harvested whole |
| IMF | none anywhere | — | nothing to work |
| Chinese state loans | AidData's own harm-flagged text | 793 of 20,985 flagged | worked out: 111 researched, 178 left carry only a protest or pollution flag |
| Chinese state loans | Business & Human Rights Resource Centre | 679 allegations against Chinese companies abroad, 2013–2020; 102 more on transition minerals, 2021–22 | **unworked**, and it sits outside the lender |
| Foreign company projects | **OECD Watch complaint database** | 503 complaints under the OECD Guidelines | harvested 17 Nov; 90 already named in cases, 413 open |
| Foreign company projects | Environmental Justice Atlas | over 3,800 socio-environmental conflicts by Dec 2022 | unworked; not all involve a foreign company |
| Foreign company projects | BHRRC Transition Minerals Tracker | — | unworked |
| Private bank and bond lending | **BankTrack Dodgy Deals** | 319 profiles (210 projects, 109 companies) | unworked |
| Aid | none anywhere | — | nothing to work |
| Payment services | none anywhere | — | nothing to work |

## The two caveats that must travel with these sources

**BankTrack states its own selection bias.** Its page says a bank's list of Dodgy Deals "should not
be interpreted as the complete list of controversial projects this bank finances" and that the list
reflects BankTrack's and its partners' campaign priorities. It also says it cannot guarantee the
accuracy of every profile and that financing details appear only where available. So it is a place
to start research and never a denominator, and a case built from it still needs its own sources.

**An OECD Watch complaint is an allegation by the complainant, not a finding.** A complaint
"Rejected" by an NCP was often rejected on procedural grounds, which says nothing about whether the
harm happened; a complaint that reached "Agreement" does not establish that it did either. Test 2
still has to be met from sources outside the complaint.

## What was checked and is not worth working

- **Accountability Console** (Accountability Counsel): about 1,300 complaints to 13 accountability
  offices. The map already holds 3,004 complaints from fourteen offices, so this is a subset of work
  already done.
- **Equator Principles project database** (BankTrack): a list of financed projects, not of harm.
- **BankTrack Human Rights Response Tracking**: 368 communications over 29 cases and 64 banks since
  2021. Small, and it records whether a bank replied rather than what happened to people.

## Fetch notes

- `oecdwatch.org/complaint-sitemap.xml` lists every complaint page. 503 pages, all fetched over plain
  `curl` with no refusals, 17 Nov 2026. `www.oecdwatch.org` 301s to `oecdwatch.org`, and
  `/complaint-database/` returns a 404 body of normal size — go by the sitemap, not that page.
- Complaint pages are label-structured: Date filed, Keywords, Countries of harm, Current status,
  Sector, NCP, Allegations, Relevant OECD Guidelines, Outcome, Defendant, Company in violation,
  Other companies involved, Complainants, Affected people, Date rejected / concluded. Allegations
  text runs to a median of 1,260 characters and is complete on the page, not truncated.
- `banktrack.org`'s `robots.txt` names a sitemap that 404s. The deal index is
  `/show/dodgydeals/`, a single 1.5 MB page carrying every profile link.
- `ejatlas.org` serves a 637-byte shell: the cases load from an API, so it needs a different route
  than curl on the listing page.
