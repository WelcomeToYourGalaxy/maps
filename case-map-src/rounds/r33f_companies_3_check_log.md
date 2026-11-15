# Check log — companies_3 (round 33, batch 3 of 3)

Independent check of 41 company and public-body descriptions. **Every cited page was opened**
(46 fetches). Nothing merged, built or pushed.

Headline: 39 descriptions submitted. **33 corrected, 6 left exactly as written, none emptied**, and
**1 of the 2 blanks filled** from a project document the writer had on disk. Final blank rate
1 of 41 (2.4%).

Of the 33 corrections: 22 removed or rewrote a claim the cited page does not make, 5 removed text that
restates the role the card already shows, and 6 tightened wording or length without a sourcing fault.
No description was cut in full, which is unusual for this map and is itself a finding — see section 9.

The dominant fault in this batch was not invention of nationality or a wrong parent. It was
**sourcing a claim to a page that does not make it** — eight cases — and **dates and years taken
from a document's own publication date rather than from the figure**, five cases.

---

## 1. Blank confirmed

**Dragonhart** — the writer's blank holds; note rewritten.
The writer blanked it on search grounds. The project's own land acquisition report of May 2018, on
disk at `cache/P113844/RP_2018-05-01_30330722.txt`, names the firm exactly once:

> "Maynilad conducted a site optioneering together with ALAI (the design consultant) and
> **Dragonhart (the contractor)** to come up with this alternative option."

That is the role the card already shows and nothing more — no sector, no ownership, no legal name.
Applying the standing test: strike the name and nothing is left. Blank holds, and the note now
records the document check rather than only the failed searches.

## 2. Blank filled by the checker

**Land Revenue Departments of Khyber Pakhtunkhwa and Azad Jammu and Kashmir** — retrievable, and
the writer did not open the document it was retrievable from. The resettlement plan at
`cache/P099040/RP_2007-10-01_8713349.txt`, section 1.5.2 "Provincial Revenue Department":

> "Under the national law, matters relating to land use and ownership are provincial subjects, and
> for the purposes of this project, the NWFP Revenue Department is empowered to carry out the
> acquisition of private land or built-up property for public purposes, including on behalf of
> another provincial or federal agency. For this purpose, the lead department must lodge an
> application with the NWFP government to depute a land acquisition collector (LAC) and other
> revenue staff."

Filled on that basis, for the provincial department only. The plan uses the province's then name
(North-West Frontier Province); the desc quotes that name rather than asserting the rename, which
no opened source states. **Nothing is said about the Azad Jammu and Kashmir body** — COMP's rule for
a two-entity key. The writer's claim that `kpbor.gov.pk` refused WebFetch was tested and holds:
the route returns `robots_disallowed`. `nha.gov.pk` was not retested, as the NHA entry no longer
depends on it.

## 3. Corrections, with the sentence that decided each

### Years and dates taken from a document's date, not from the figure (5)

- **Israel Electric Corporation** — "99.85 per cent of its shares **as of May 2025**" and
  "9,474 MW across 42 units **in 2024**". The presentation states "The state of Israel, which holds
  99.85% of the IEC's shares" with no as-of date, and the generation table carries no year. Both
  years came from the presentation's own date. Dropped the as-of date; dropped the capacity figure
  with it rather than publish an undated one. Customers (3.0m at 31/12/2024) and revenue
  (ILS 26,184m for 2024) are dated in the source and kept. Employees cut for length.
- **Bukhara Suvokova** — "A **2019** presidential decree converted…". The cited anhor.uz page gives
  neither the decree's number nor its year; the article is dated 27 November 2019. Corrected to
  "a presidential decree reported in November 2019".
- **Projects Implementation Unit, Uzbekistan** — "split **in February 2018**". The Tashkent Times
  report gives only its publication timestamp, 2018-02-14, and names no decree and no effective
  date. Corrected to "was reported in February 2018 to have been split", in the desc and in the
  discrepancy file.
- **Land Bank of the Philippines** — "Republic Act 3844 **of 1963** as amended (most recently by
  Republic Act **10878 in 2016**)". The governance report says only "R.A. 3844, as last amended by
  R.A. 10878"; both years exist on that page solely inside Official Gazette link URLs. A date off a
  URL is the named fault. Both years dropped; the amendment relationship is kept.
- **National Irrigation Administration** — "262 national irrigation systems with a combined service
  area of 980,108 hectares **as of December 2024**". The report's sentence carries no as-of date;
  the "As of December 2024" lines nearby attach to different figures. Date dropped.

### Claims the cited page does not make (8)

- **Ministry of Industry, Commerce and Supplies, Nepal** — the whole second sentence went. It listed
  the Department of Industry, the Department of Commerce, the Office of the Company Registrar and
  Nepal Oil Corporation as sitting under the ministry; the site states no such thing, and those
  names appear only in the titles of recruitment and public notices. A grep hit read as a structure.
  "Industrial policy" and "domestic trade" also go: the page has no functions statement. Replaced
  with the four divisions the page does list.
- **Nepal Intermodal Transport Development Board** — "its depots include Birgunj, Biratnagar…". The
  presentation lists five dry ports but never says the board operates them; its stated functions are
  to "develop, manage and promote ICD terminals". Also "sets terminal charges" → the page says
  "prescribe criteria in determining the service charges". Both corrected.
- **Municipal Government of Rodriguez** — "the second most populous local government in Rizal after
  the city of Antipolo". The press release never says it; the ranking would have to be inferred from
  a top-ten table that omits most Rizal municipalities. Replaced with the ranking the release does
  print ("seventh among the region's cities and municipalities"). "Next to Metro Manila" also cut.
- **Palestinian Energy and Natural Resources Authority** — "Under Article 4 … it grants and approves
  transfers of distribution and generation licences … and works on renewable energy". The record
  ties neither to Article 4: licence transfers appear in the generation and distribution sections and
  renewable energy research in the distribution section. Split, so Article 4 carries only what the
  record's Article 4 abstract carries. Also noted: that page is a summary record, not the legal text.
- **Projects Implementation Unit, Uzbekistan** — "it oversees the construction works" and "picks
  farmers for demonstration plots with water user associations and local authorities". The report
  says grievances were resolved "by series of consultation and face-to-face meetings by PIU and
  construction supervision consultants" — it does not say the unit supervises works — and says the
  PIU began designing *selection criteria*, with monitoring consultants then working on them "with
  close coordination of local farmers associations, local government and communities". Not water user
  associations, and criteria rather than choosing. Both corrected.
- **Central Planning Division** — "coordinates and runs externally financed government projects".
  The manual names it the main coordinating body **of this project** and says nothing about external
  financing generally. Scoped to the project.
- **BOTAS** — "**imports** and transmits natural gas". The About Us page does not mention imports; it
  shows transmission, trading, storage and tariffs for crude oil, natural gas and port services.
  "Imports" cut.
- **AFAP** — "carries out the fiduciary work **for government ministries**". Neither the grant
  agreement nor the 2024 implementation report says that; the report shows one procurement run for
  the finance ministry, which does not carry the general claim. Cut. Also cut procurement and
  financial management from the desc as a restatement of the card's role.

### A statute's remit presented as the body's present remit (2 of 7 statutory entries)

Seven entries rest on a statute or a gazette. Five date the position correctly. Two did not:

- **Metropolitan Waterworks and Sewerage System** — the desc described MWSS wholly in the present
  tense out of Republic Act 6234 of 1971: "It builds, maintains and operates water and sewerage
  systems in and around Manila." Two other entries **in this same batch** contradict that:
  Manila Water and Maynilad each hold a 25-year concession granted in 1997 and running to 2037, and
  the card's own role calls MWSS the body that "owns the Metro Manila water and sewerage assets and
  holds the concessions." The statutory powers are now attributed to the Act, with the concession
  arrangement since 1997 stated after them.
- **Laguna Lake Development Authority** — the same shape, from Republic Act 4850 of 1966. Powers now
  read "Under that Act". Two wording errors inside it: the Act gives the Authority power to "act in
  coordination with existing government agencies in establishing water quality standards", not to set
  them; and the Act's city list is San Pablo, Manila, Pasay, Quezon and Caloocan, where the desc gave
  "several cities including Manila and Quezon City" — the Act says "Quezon", not Quezon City.

### Smaller factual corrections (9)

- **CFM** — "created out of a state enterprise by Decree 40/94" was close but the profile says a
  state company was created in 1989 and *transformed* into a public company by Decree 40/94 of
  13 September 1994; date added. "(about 700 km in total)" was the writer's own sum of 88 + 74 + 534;
  the three line figures are now given as the profile gives them.
- **OMVS** — the 800 GWh, 375,000 ha and drinking-water figures were credited to "a World Bank
  account". The page is a guest post on a World Bank blog **written by OMVS's own High Commissioner**,
  so the figures are the organisation's own claims about itself. Attribution corrected and the source
  year fixed from 2021 to 2014. The convention was *adopted* at Nouakchott; "signed at" softened.
- **SONADER** — "with its own legal personality and budget" → the page says "legal personality and
  financial independence". "Builds and maintains irrigation works such as canals, dykes and water
  channels" → the page says it monitors and maintains farm water infrastructure (water axes, barriers,
  canals); dykes and building are not there.
- **DGER Peru** — "assessing demand, networks and **project costs**" → the presentation gives
  current and 20-year demand, networks near the project area and social returns. No cost analysis.
- **DZMiUW** — "budget unit of the **Lower Silesian voivodeship** self-government" → the notice says
  "jednostka budżetowa samorządu terytorialnego", a local-government budget unit; the voivodeship
  level is an inference from the name. "Including drainage and land reclamation records" came from the
  contract description, not the stated field of work; cut.
- **RZGW Gliwice** — "covering towns in the Silesian region" → the statute assigns it the Mała Wisła,
  Upper Odra and Czadeczka water regions, and the 2018 jurisdiction annex includes gminas in Opole
  voivodeship as well as Silesian ones, so "Silesian" understates and misdescribes it.
- **MESP Kosovo** — "it puts the annual state of the environment report to the government" → the
  Government submits the report to the Assembly on the ministry's proposal, and the Environmental
  Protection Agency drafts it. Inspection count (about 200, with 118 prohibition decisions,
  7 criminal charges, 24 minor offence reports, 93 fines) added, as the desc had the inspections
  without the figures the same table gives.
- **Companhia Santomense de Telecomunicações** — "began with a fixed analogue network and later added
  mobile service" appears in neither cited page. Cut.
- **Road Development Agency, Zambia** — "sets maximum vehicle weights" → the report says it regulates
  the maximum weights permitted; Tolls Act number added (No. 14 of 2011).

### Role restatement removed (5)

`appears_on[].role` already carries these, so they were duplication rather than description:

- **Nepal Electricity Authority** — "generates, transmits and distributes power across the country"
  is almost verbatim the card's role. Replaced with the Act, the date and the merged bodies, plus the
  planning and tariff functions.
- **National Highway Authority** — "Pakistani government authority in charge of the national road
  network" restated both the name and the role's "federal body … that owns and manages the national
  highway network". The sourced content is the Economic Survey figure, which now leads.
- **Ukravtodor** — "Ukraine's national roads body, responsible for building, repairing and maintaining
  state-owned roads" is the card's role, and the cited successor page does not describe Ukravtodor's
  remit at all. Reduced to the succession, which is what the page supports.
- **Maynilad** — "as the private concessionaire of the Metropolitan Waterworks and Sewerage System"
  restated the role; the concession facts carry it instead.
- **AFAP** — procurement and financial management, as above.

### Length

**KEK** and **Israel Electric** each ran to four sentences and four figures against COMP's "1-2 short
sentences" and "one plain figure". KEK's end-2025 unit count and the 35 MW turbine upgrade were
checked and confirmed, then cut as operating detail rather than description. Neither cut rests on a
sourcing problem; both facts are in the log here if wanted.

## 4. Left exactly as written (6)

Ircon International, Electrocentro, Hidrandina, Manila Water, Ministry of Transport, Works, Urban
Development and Local Government (SVG), rePlan Inc.

Two more were confirmed in substance and only tightened to the source's own words: **Energy Water and
Sanitation Authority** (every date checks out — the repealing law of 31 January 2014 and the July 2014
incorporations from Rwanda Energy Group's history, the Prime Minister's Order of 16 August 2014 from
WASAC's; "wholly state-owned" became "100 per cent government shareholding", the source's phrase), and
**MINAGRI** (the National Agricultural Policy's 2018 date and PSTA5 both confirmed on the page, mission
wording brought back to the page's).

Four of these deserve naming because they are the batch's hardest facts and they hold exactly:

- **Electrocentro**: FONAFE at 100.00% of 597,014,055 shares as of 10.12.2022, and
  "Al cierre a noviembre 2022, se ha atendido a 920 092 clientes." Customer figure correctly dated to
  November 2022, not to the report.
- **Hidrandina**: 8,570.14 km², FONAFE "más del 95% del capital social", 1,091,095 customers and 758
  direct employees, each tied to 2024 in the report.
- **Manila Water**: 52.16 / 19.01 / 12.26 per cent, 24 cities, 1,400 km², IPO 18 March 2005, term
  extended to May 2037 — every one on the profile.
- **BOTAS** current assets: the audit table gives 506,171,471 in the "Dönen" column in **thousands**
  of lira, and the desc's "about 506 billion lira" reads the unit correctly.

**rePlan Inc.** is worth a line in the other direction: the key carries "Inc." and the article never
does. The writer said so in the desc ("which the trade press reports under the name rePlan") instead
of smoothing it over. That is the right handling of a name mismatch and it should be the pattern.

## 5. Discrepancy file

Seven entries submitted. **All seven hold on the source they cite**, and all seven are phrased with a
date rather than as an overwrite. Two needed correction and I added two more:

- **Bukhara Suvokova** — "being procured by … Bukhara Suv Ta'minoti **under Uzsuvtaminot**". The AIIB
  notice names JSC Bukhara Suv Taminoti as purchaser; Uzsuvtaminot appears only as the contact and
  submission address, not as a parent. Corrected there and in the desc. The decree year also fixed
  (see above). The restructuring paper gives no date for the 14-Suvokova reform, now said.
- **Manila Water** — "the Ayala group, **which led the company at the time of the case documents**, is
  now a minority holder". The cited profile gives today's holdings only and says nothing about Ayala's
  position in 2008. Characterisation removed; the holdings stand.
- **Added: Central Planning Division** — the 2014 operations manual confirms the ministry name on the
  card, and the 10 November 2017 gazette gives the post as Minister of Finance, Economic Planning,
  Sustainable Development and Information Technology. Both readings given, neither overwriting.
- **Added: AFAP** — the Bank's own documents spell it "Administração de **Projetos**" (plural) and the
  grant agreement never defines the acronym AFAP; the card has "Projecto".

## 6. Voice and tone

Grepped all 41 `desc` values for "I ", "we ", "our ", "my ", "searches", "this pass", "read here",
"this card", "the writer": **no hits**, before or after my edits. No opinion words found. Two notes
(the two blanks) carry research process, which is where it belongs.

## 7. Could not settle

- **Nepal Electricity Authority, "several power development boards"** — the About Us page says the
  merger took in "several related development boards" without naming them. Kept at the page's level of
  precision; the individual boards are unverified.
- **Guinea's accession to OMVS** — the ECOLEX record shows three signatories in 1972; the 2014 post
  names Guinea as a member and refers to "l'adhésion de la Guinée" without a date. "Joined later" is
  all either page supports; no year is claimed.
- **Khyber Pakhtunkhwa = North-West Frontier Province** — universally known, but no opened source in
  this batch states the rename, so the desc uses the plan's own wording and makes no identity claim.
- **AJK land revenue body** — nothing opened describes it. Stated in the note, not the desc.
- **BOTAS state ownership** — the company's own page says nothing about ownership; "state" rests on the
  Court of Accounts listing it first among the 25 enterprises subject to Decree-Law 233. That is
  sufficient but it is a second-hand route, recorded here.
- **Second figure, NIA** — the same paragraph gives 980,108.68 ha aggregate and 876,564.65 ha
  firmed-up. Not reconciled; both are now in the desc.

## 8. Routes that failed, named as routes

- `kpbor.gov.pk` — WebFetch returns `robots_disallowed`. Confirmed, not inherited.
- `officialgazette.gov.ph/1971/06/19/republic-act-no-6234/` — WebFetch `client_error`. Worked around:
  the Act text was read instead at `lawphil.net/statutes/repacts/ra1971/ra_6234_1971.html`, which
  gives the full sections. **The writer's source for RA 6234 was digest.ph, a commercial legal site
  whose statute body is behind a login**, so the facts came off a third-party editorial summary. Source
  replaced with the LawPhil text, from which every clause in the desc was read directly.
- No other route failed. No hourly limit was hit.

## 9. The one finding for the next brief

**Make the writer state, for every figure and every date, the words in the document that fix it.**

Five of this batch's errors are a date or year the document does not attach to the figure — a share
percentage dated to the slide deck's cover, a ministry split dated to a news timestamp, a statute's
year read off a hyperlink, a service area dated from an "as of" line belonging to a different number,
a decree's year read off the article reporting it. None is a careless invention; each is a plausible
year sitting one line away from the figure. They are invisible in a finished sentence and all five
survived a batch that otherwise handled hard ownership percentages correctly.

A rule that would have caught all five: **no figure may carry a date unless the document states the
date in the same sentence or table cell as the figure; if it does not, publish the figure undated or
not at all.** That also answers the batch's low blank rate. The 5% held up, and in fact fell to 2.4%:
one blank was retrievable and got filled, the other holds, and no description had to be emptied. The
rate was honest, and the reason is visible in the inputs — this batch is nearly all state utilities,
ministries and statutory agencies, which publish about themselves, where the round's other two batches
carried private contractors that do not. What was stretched was not
whether a fact existed but **how precisely it was pinned**, and that is what the next brief should
make expensive.
