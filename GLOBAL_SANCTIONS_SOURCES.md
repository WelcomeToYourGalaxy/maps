# Global sanctions and designation lists — sources and method

Source catalogue and method notes for `global_sanctions.html`. Data files live in `global_sanctions_data/`.

The map carries **421,241 mapped listings** from **217 official lists** published by governments, the UN Security
Council, the EU and financial regulators. Lists are aggregated through OpenSanctions, which pulls each from its
issuing authority's own published file. Nothing is added, inferred or edited in the records themselves.

**54,355** designated targets publish neither an address nor a country — mostly crypto wallets, securities and
aircraft — and cannot be placed on a map.

## How complete this is

No government or body keeps a census of every official designation list in
the world, so completeness can only be measured against the fullest public
catalogue of them, which is OpenSanctions. Across the seven collections that
hold designation lists it publishes 226 sources that carry entries; this
build downloaded 228 lists in all.

| | Count |
|---|---:|
| Lists downloaded | 228 |
| Lists with at least one listing that could be placed | 217 (95%) |
| Lists publishing nothing placeable | 11 |
| Listings after de-duplication | 475,596 |
| Listings placed on the map | 421,241 (89%) |
| Listings with no usable country or address | 54,355 |

The eleven lists that carry nothing placeable publish entries with no
geography at all: crypto wallet addresses, proscribed organisation names,
broadcast equipment on the US FCC covered list, and similar.

## What period the data covers

These are the lists **as they stand now**, not an archive. When an authority delists a party, that record generally
disappears from its published file and so from this map. Of 529,801 source records checked, only 221 carried a
status other than active; the rest are live listings.

Where a list publishes when a designation began, those dates run from **1951 to the current year**, and the bulk
fall after 2014 — 2022 is the single biggest year, reflecting the Russian invasion of Ukraine. Roughly a third of
listings publish no date at all. The map does not yet filter by year; the dates are in the data if that is wanted.

## Kinds of list

| Kind | Listings | Share | What it is |
|---|---:|---:|---|
| Sanctions | 96,592 | 23% | Asset freezes, travel bans and trade restrictions imposed by governments or the UN Security Council. A listing is an executive decision by an authority, not a court verdict. |
| Warrants & criminal entities | 207,525 | 49% | People and companies wanted by police or prosecutors, including Interpol notices and national most-wanted lists. A warrant is an accusation that has not been tested in court. |
| Debarment | 188,392 | 45% | Companies and people barred from public contracts or development-bank funding, usually after a finding of fraud, corruption or collusion. |
| Regulatory watchlists | 134,486 | 32% | Firms and individuals flagged by financial regulators — unauthorised firms, investor warnings and licence refusals. |
| Wanted lists | 63,069 | 15% | Police most-wanted and fugitive notices. |
| Special-interest watchlists | 20,215 | 4.8% | Lists compiled for one specific concern, such as forced labour in supply chains or companies tied to a military. |
| Enforcement actions | 4,363 | 1.0% | Penalties, prosecutions and regulatory notices already issued against a party. |

A party can sit in more than one kind, so the shares add to more than 100%.

## What the listing is for — how this map classifies it

The lists do not publish a comparable field for *why* a party is designated. This classification is read from the
programme each listing cites — the executive order, regulation, resolution or register it names — and, where a
listing cites nothing, from the stated purpose of the list it sits on. **It is this map’s reading, not a field any
authority publishes, and no source endorses it.** The rules are in the repository so they can be checked.

| What it is for | Listings | Share | Band | Definition |
|---|---:|---:|---:|---|
| Debarment & procurement exclusion | 198,607 | 47% | 1 | The party is barred from public contracts, development-bank funding or a public health programme, usually after a finding of fraud or non-performance. |
| Arrest warrant, offence not stated | 58,468 | 14% | 3 | A police or prosecution body wants the party arrested but the list does not publish what for. Red notices and national wanted registers mostly fall here. |
| War & territorial aggression | 40,158 | 9.5% | 5 | The listing responds to an armed invasion or the annexation of territory — most of these are Russia-Ukraine measures. |
| Export control & military-industrial | 23,521 | 5.6% | 2 | The listing restricts what may be sold to the party: export-control entity lists, military end users and military-linked companies. |
| Terrorism & armed groups | 23,376 | 5.5% | 5 | The listing is made under a counter-terrorism power: a designated terrorist organisation or financier, a proscription order, or a UN 1267/1373 listing. |
| Financial crime & fraud | 21,818 | 5.2% | 3 | The listing concerns fraud, money laundering, sanctions evasion or securities offences. |
| Regulatory & licensing action | 16,859 | 4.0% | 1 | A financial or professional regulator has warned about, suspended or refused to authorise the party. |
| Country programme | 14,026 | 3.3% | 2 | A broad country sanctions programme — the party is listed because of where it operates or who it belongs to, not for a named offence. |
| Human trafficking & forced labour | 11,814 | 2.8% | 4 | The listing concerns forced labour, trafficking in persons, or goods made with forced labour. |
| Weapons & proliferation | 6,917 | 1.6% | 5 | The listing concerns nuclear, chemical, biological or missile programmes, or arms embargoes and arms trafficking. |
| Drugs & narcotics | 4,940 | 1.2% | 4 | The listing is made under a narcotics power: kingpins, cartels, traffickers and their companies. |
| Human rights abuses & atrocities | 2,430 | <1% | 4 | The listing is made under a human-rights power: killings, torture, repression, ethnic cleansing or genocide. |
| Counter-sanctions & retaliation | 2,071 | <1% | 2 | A government has listed the party in retaliation for sanctions imposed on it, rather than for conduct of the party’s own. |
| Organised crime & violence | 1,813 | <1% | 4 | The listing concerns an organised criminal group, or a warrant for a violent offence. |
| Corruption & kleptocracy | 1,005 | <1% | 3 | The listing concerns bribery, embezzlement, kleptocracy or the theft of state assets. |
| Cyber attacks & ransomware | 667 | <1% | 4 | The listing concerns malicious cyber activity: intrusion, ransomware or election interference by digital means. |
| Reason not stated | 17,101 | 4.1% | — | Neither the listing nor the list it sits on says what the designation is for. |

## How grave — this map’s severity bands

A 1-to-5 band assigned from the classification above. Each listing takes the highest band of its reasons. The lists
do not rank themselves against each other, so this scale is ours alone and exists to make the map filterable.

| Band | Listings | Share | What falls in it |
|---|---:|---:|---|
| Not stated | 17,101 | 4.1% | The lists this party is on do not say what the designation is for, so no band is assigned. |
| 1 — Exclusion from contracts or a licence | 211,912 | 50% | Barred from public contracts, a funding programme or a licence. An administrative penalty, usually about money or performance rather than violence. |
| 2 — Restricted trade | 23,806 | 5.7% | Export controls, military-industrial listings and broad country programmes. The restriction is on what may be sold to the party, or on where it operates. |
| 3 — Financial crime, corruption or an untested warrant | 79,189 | 19% | Fraud, laundering, bribery, or an arrest warrant whose offence the list does not publish. |
| 4 — Grave harm to people | 20,702 | 4.9% | Drugs, organised crime and violence, trafficking and forced labour, human-rights abuses, cyber attacks. |
| 5 — Terrorism, war or weapons of mass destruction | 68,531 | 16% | Counter-terrorism designations, war and territorial aggression, and nuclear, chemical, biological or missile proliferation. |

## What comes from the lists, and what this map adds

Every popup is split. Above the dashed rule, each line is as the authority
publishes it: the name, the entity type, which lists the party is on, the
address, the country, the wording of the measure, aliases, reference
numbers, date of birth, and when the list last changed. The coordinates are
this map's geocoding of the published address.

Below the dashed rule, marked "not from the list", are four things no
authority publishes and that this map works out:

| Added by this map | How it is derived |
|---|---|
| What it is for | Keyword rules over the programme each listing cites; failing that, the stated purpose of the list it sits on |
| How grave | A 1-5 band mapped from the category above |
| Most likely in practice | A sentence written per category, further split for health-programme and development-bank exclusions. Where the authority publishes the offence itself, the map says so and offers no guess |
| Placed by | Whether the point sits on a street, a town centre, or a country centre |

"Most likely in practice" describes what listings of that kind usually
concern. It is not a statement about the individual party, and it never
draws on anything beyond the category and the kind of list.

## Corrections made after an accuracy audit

Every classification rule was run against all 421,241 listings and its
matches inspected. Four rules were matching text they were never meant to:

| Rule | What it hit by mistake | Effect | Fix |
|---|---|---|---|
| `1988` in the terrorism rule, for UN Resolution 1988 | the date 1988 in `1988-05-09` | 711 listings, mostly US state Medicaid pharmacies and care homes, were labelled terrorism and graded severity 5 | resolution numbers must now be cited as resolutions |
| `SDT` for Specially Designated Terrorist | the letters inside `USDT`, a crypto address | 12 listings labelled terrorism | word boundary on both sides |
| `gang` | the end of names such as Namgang | 31 listings labelled organised crime | word boundary on both sides |
| `311` for the FinCEN provision | any number ending 311 | 417 listings labelled financial crime | must now read "section 311" |

A fifth was a judgement error rather than a coding one. Three Xinjiang
datasets — one from Sheffield Hallam University and two from the Center for
Advanced Defense Studies — name companies that operate in a region or are
linked to a state corporation. They allege no offence, and treating them as
forced-labour findings put 10,982 companies in that category. They now sit
in a category of their own, "named for where it operates or who owns it".
The US UFLPA list, which is a government finding of forced labour, stays
where it was.

After these corrections the terrorism category holds 22,870 listings, down
from 23,376, and every sample checked sits on a list that is explicitly a
counter-terrorism register.

## A caveat on the Atlas basemap

The Atlas painting is artwork, not a survey. Its continents are drawn at
sizes and positions of the artist's choosing — Australia, for instance, is
painted larger than it is and slightly out of place. The plate is now
stretched across 83.16 degrees north and south rather than 85.05, which is
the extent at which its pixels are square and which brings Africa, Europe
and the Americas onto the relief beneath. Australia and the far north will
still not register exactly, and no single setting can make them.

## Plain-language glosses in the popup

The lists publish their reasons in their own shorthand. A World Bank
debarment reads `CROSS-DEBARMENT: IDB - 2020-12-23 - 2029-12-22 ·
Corrupt Practice, Fraudulent Practice`; an OFAC listing reads `SDNTK`;
a Brazilian procurement bar cites `LEI 8666 - ART. 87`. None of that
means anything to a reader meeting it for the first time.

The popup therefore prints the authority's wording unchanged, and
underneath it a short "what that wording means" block. The glossary
holds about ninety terms, each one checked against the issuing body's
own published description: the five sanctionable practices the
development banks define, the cross-debarment agreement of 2010, OFAC
programme tags, the US export-control registers, US state Medicaid
exclusions, UN Security Council instruments, the Brazilian procurement
and improbity laws, and the UK Company Directors Disqualification Act.
Of the 287,611 listings that carry any wording, 91.8% match at least
one term. Where nothing matches, the popup says the authority does not
explain the entry further rather than inventing a reading.

The glossary explains vocabulary. It does not add facts to a record,
and it is held separately in the page source so it can be checked line
by line.

### Reference numbers

The lists publish identifying numbers without saying what they are.
The consolidated source carries them as one undifferentiated field, so
the type is not recoverable from the data. Rather than guess, the map
runs each value against the check-digit formula of the formats that
have one, and names the format only when the value satisfies it:

| Format | Listings labelled |
|---|---:|
| Tax number (INN) — Russia and neighbouring states | 21,453 |
| Brazilian company number (CNPJ) | 9,837 |
| Brazilian personal tax number (CPF) | 8,108 |
| IMO ship number | 3,660 |
| Legal Entity Identifier (LEI) | 441 |

The INN, CNPJ and CPF checks are additionally restricted to records
whose country field matches, which removes most coincidental passes. A
LEI is also given a link to the GLEIF register so the company can be
looked up. The remaining four-fifths of values are shown as published,
with a note that the list does not state what they are.

## Location precision

| Precision | Listings | Share | What it means |
|---|---:|---:|---|
| Street address | 7,716 | 1.8% | The list publishes a street address and it resolves to that address. |
| City or locality | 197,844 | 47% | The list publishes a town, city or district; the point sits at its centre, not at the entity’s address. |
| State or province | 5,315 | 1.3% | The list publishes no town, but the address names a state or province; the point sits at the centre of that state. |
| Country only | 210,366 | 50% | The list publishes only a country, or an address nothing could resolve; the point sits at the centre of the country’s main landmass. |

Country points were taken from the median position of that country's towns, which the dense east of the
United States dragged as far as Indiana — 53,477 listings sat there. They are now the area centroid of the
country's largest landmass, computed from Natural Earth: 39.50N 99.06W for the United States, in northern
Kansas, within about 40 km of the published geographic centre of the contiguous states. Distant territories no
longer pull the point, so France sits in France rather than mid-Atlantic. A few city-states and small island
states are not in the Natural Earth country file; their original point already stood on the country and was
left alone.

A state tier was added at the same time. Where a list gives no town but the address ends in a state or
province — `NV`, `(MD)`, `Arenzville, IL`, `CABO VERDE/MG` — the point now sits at the centre of that state
rather than the centre of the country. Natural Earth's admin-1 file covers the United States, Brazil, Russia,
Canada, India, Indonesia, China, Australia and South Africa, which is where almost all of these addresses are.

City-level and country-level points are **not** the entity's address. Street-level points come from the geocoded
address set built for the original OFAC map or from a street geocoder; city points are resolved against the
GeoNames gazetteer (237,395 places with multilingual name variants) constrained to the country the list names.

To improve this, run `refine_sanctions_geocoding.py` (in this repository). It walks the addresses that are not yet
at street level through a street geocoder, saves progress as it goes, and writes replacement data files. It takes
hours, so run it in the background and copy the output over `global_sanctions_data/` when it finishes.

## How the files fit together

- `global_sanctions.html` — the map. Loads MapLibre GL and the Culprits basemap module, then fetches the data below.
- `global_sanctions_data/meta.json` — list names, descriptions, groupings, counts, classifications.
- `global_sanctions_data/<kind>.json.gz` — one gzipped shard per kind of list.
- `global-sanctions-atlas-plate.webp` — the Atlas basemap plate, cartouche repainted for this map.
- `refine_sanctions_geocoding.py` — the geocoding refinement script described above.

## Lists carried, by issuing authority

### United States — 248,738 listings (59%)

US federal lists: Treasury (OFAC) sanctions, Commerce export controls, State Department designations, plus federal and state exclusion registers for public programmes.

- US SAM Procurement Exclusions — 88,917 mapped listings
- US Trade Consolidated Screening List (CSL) — 36,191 mapped listings
- US OFAC Specially Designated Nationals (SDN) List — 29,091 mapped listings
- US OFAC SDN List (address-level build) — 21,069 mapped listings
- US California Medicaid Suspended and ineligible providers — 17,118 mapped listings
- US Health and Human Services Inspector General Exclusions — 16,047 mapped listings
- US FINRA Enforcement Actions — 14,595 mapped listings
- US FINRA Barred Individuals — 9,361 mapped listings
- US Texas Medicaid Provider Exclusions — 9,159 mapped listings
- US New York State Medicaid Exclusions — 6,245 mapped listings
- US Pennsylvania Medicheck list — 4,506 mapped listings
- US OCC Enforcement Actions — 4,199 mapped listings
- US Michigan Medicaid Sanctioned Provider List — 3,958 mapped listings
- US Louisiana Department of Health Adverse Actions List — 3,074 mapped listings
- US New Jersey Ineligible Medicaid Providers — 2,580 mapped listings
- US Arkansas Medicaid Excluded Provider List — 2,312 mapped listings
- Iran UANI Business Registry — 2,137 mapped listings
- US Delaware Medicaid Sanctioned Providers — 1,455 mapped listings
- US Nebraska Medicaid Sanctioned Providers — 1,365 mapped listings
- US Minnesota Health Care Programs Excluded Providers — 1,229 mapped listings
- US Ohio Medicaid Excluded and Suspended Providers — 1,127 mapped listings
- US Maryland Sanctioned Providers — 945 mapped listings
- US SEC Actions Due to Harmed Investors — 849 mapped listings
- US Iowa Medicaid Terminated Provider List — 802 mapped listings
- US Directorate of Defense Trade Controls AECA Debarments — 790 mapped listings
- US South Carolina Excluded Providers — 787 mapped listings
- US Alabama Medicaid Suspended Providers — 760 mapped listings
- US Maine Medicaid Excluded Providers — 727 mapped listings
- US OFAC Consolidated (non-SDN) List — 690 mapped listings
- US Georgia Healthcare provider exclusions — 661 mapped listings
- US FDIC Failed Banks — 634 mapped listings
- US Federal Reserve Enforcement Actions — 576 mapped listings
- US State Department Cuba Sanctions — 556 mapped listings
- US Anti-Kleptocracy and Human Rights Visa Restrictions — 547 mapped listings
- US Nevada Medicaid Sanctions — 541 mapped listings
- US OFAC Consolidated non-SDN List (address-level build) — 523 mapped listings
- US BIS Denied Persons List — 432 mapped listings
- US FinCEN 311 and 9714 Special Measures — 390 mapped listings
- US Special Legislative Exclusions — 339 mapped listings
- US Kentucky Terminated and Excluded Providers — 336 mapped listings
- US CFTC Enforcement Actions — 294 mapped listings
- US FBI Most Wanted — 277 mapped listings
- US Colorado Medicaid Terminated Provider List — 265 mapped listings
- US Massachusetts Suspensions and Exclusions from MassHealth — 258 mapped listings
- US Advisory on North Korean Joint Ventures — 229 mapped listings
- US Missouri Medicaid Provider Terminations — 215 mapped listings
- US UFLPA Entity List — 211 mapped listings
- US Office of Antiboycott Compliance Requester List — 208 mapped listings
- US Washington State Provider Termination and Exclusion List — 198 mapped listings
- US Department of State Foreign Terrorist Organizations — 192 mapped listings
- US Alaska Medical Assistance Excluded Provider List — 191 mapped listings
- US Arizona Medicaid Suspensions and Terminations — 184 mapped listings
- US FDA Clinical Investigator Disqualification Proceedings — 177 mapped listings
- US Kansas Medicaid Terminated Provider List — 175 mapped listings
- US Mississippi Medicaid Terminated Provider List — 162 mapped listings
- US North Carolina Excluded Providers List — 154 mapped listings
- US West Virginia Medicaid Provider Exclusions and Terminations — 139 mapped listings
- US DoD Chinese military companies — 137 mapped listings
- US North Dakota Medicaid Terminated Provider List — 131 mapped listings
- US DEA Fugitives — 106 mapped listings
- US Montana Medicaid Excluded and Terminated Providers — 99 mapped listings
- US Oregon State Medicaid Fraud Convictions — 94 mapped listings
- US Department of State Terrorist Exclusion — 79 mapped listings
- US Wyoming Medicaid Provider Exclusion List — 77 mapped listings
- US OFAC Enforcement Actions — 75 mapped listings
- US CBP Withhold Release Orders and Findings — 61 mapped listings
- US New Hampshire Medicaid Exclusion and Sanction List — 61 mapped listings
- US Directorate of Defense Trade Controls Penalties & Oversight Agreements — 60 mapped listings
- US Indiana Medicaid Terminated Provider List — 51 mapped listings
- US FinCEN Enforcement Actions — 38 mapped listings
- US Hawaii Medicaid Exclusions and Reinstatements — 32 mapped listings
- US BIS Alleged Antiboycott Violations — 30 mapped listings
- US Public Alert: Unregistered Soliciting Entities (PAUSE) — 28 mapped listings
- US Secret Service Most Wanted Fugitives — 28 mapped listings
- US Washington DC Excluded Parties List — 25 mapped listings
- US Tennessee Terminated Providers List — 20 mapped listings
- US BIS Military-Intelligence End Users — 15 mapped listings
- US BIS Export Violations — 6 mapped listings
- US NFA Enforcement and Regulatory Actions — 4 mapped listings
- US Immigration and Customs Enforcement Most Wanted Fugitives — 3 mapped listings

### Europe — national lists — 78,500 listings (19%)

Lists each European country keeps in addition to the EU’s: national asset freezes, terror-financing registers and company restrictions.

- Poland Wanted Persons — 54,220 mapped listings
- Monaco National Fund Freezing List — 12,105 mapped listings
- French National Asset Freezing System — 12,084 mapped listings
- Switzerland SECO Sanctions/Embargoes — 11,063 mapped listings
- Belgian Financial Sanctions — 9,425 mapped listings
- Slovenia Business Restrictions — 6,117 mapped listings
- Swiss FINMA Warning List — 2,458 mapped listings
- Moldovan Sanctions for Terrorism and Proliferation of WMD — 1,684 mapped listings
- Polish Sanctions Countering Money Laundering and Terror Financing — 1,206 mapped listings
- Romania Government Decision No. 1.272/2005: List of Suspected Terrorists — 385 mapped listings
- RISE Moldova People of interest — 378 mapped listings
- Estonia International Sanctions Act List — 338 mapped listings
- Lithuania Designated Persons Under Magnitsky Amendments — 290 mapped listings
- Polish List of Persons and Entities Subject to Sanctions — 122 mapped listings
- Switzerland Asset Freezes of Foreign Politically Exposed Persons — 113 mapped listings
- Latvia FIU Sanctions and Asset Freezes — 103 mapped listings
- Latvia's Magnitsky Law Sanctions List — 52 mapped listings
- Austrian National Bank Regulations on Terrorism Financing Restrictions — 47 mapped listings
- Liechtenstein Posted Workers Act (EntsG) Sanctions — 46 mapped listings
- Czech National Anti-Terrorism Designations (Government Regulation No. 210/2008) — 39 mapped listings
- Germany BKA Wanted Fugitives — 32 mapped listings
- Czech Republic National Sanctions — 30 mapped listings
- Guernsey FSC Prohibitions and Disqualified Directors — 29 mapped listings
- Moldovan Ban List of Economic Operators — 22 mapped listings
- Norges Bank Investment Management observation and exclusion of companies — 19 mapped listings
- Swiss FINMA Final Rulings — 19 mapped listings
- Germany Banned organizations involved in foreign-related extremism — 17 mapped listings
- Lithuanian International Sanctions — 16 mapped listings
- Isle of Man FSA Disqualified Directors — 14 mapped listings
- Serbian Domestic List of Designated Persons — 7 mapped listings
- Bulgaria National Terrorism Financing List — 6 mapped listings
- France AMF Illegal Financial Services list — 4 mapped listings
- Ireland Unlawful Organisation (Suppression) Orders — 3 mapped listings
- France AMF Regulatory sanctions — 3 mapped listings
- Lithuania Illegal Financial Services — 1 mapped listings

### Asia & Pacific — 45,715 listings (11%)

National sanctions, export-control and terror lists across Asia and the Pacific, including Japan’s end-user lists and Taiwan’s high-tech controls.

- Taiwan Strategic High-Tech Commodities Entity List — 20,169 mapped listings
- India National Stock Exchange Debarred Entities — 14,419 mapped listings
- Australian Sanctions Consolidated List — 6,433 mapped listings
- Pakistan NACTA Proscribed Persons — 5,211 mapped listings
- Japan Economic Sanctions and List of Eligible People — 5,120 mapped listings
- New Zealand Russia Sanctions — 2,805 mapped listings
- Hong Kong Targeted Financial Sanctions (Cap. 537) — 1,841 mapped listings
- Japan METI End User List — 1,753 mapped listings
- Japan METI Russian List — 1,481 mapped listings
- Indonesian List of Suspected Terrorists and Terrorist Organizations — 1,299 mapped listings
- Australian Sanctions Imposed on Sponsors of Skilled Foreign Worker Visas — 681 mapped listings
- China Sanctions Research — 410 mapped listings
- Thailand Designated Persons List — 336 mapped listings
- Philippines GPPB Consolidated Blacklisting Report — 125 mapped listings
- Malaysia MOHA Sanctions List — 109 mapped listings
- Nepal Prohibited Persons or Groups according per National Strategy and Action Plan (2076-2081) — 107 mapped listings
- Philippines Anti-Money Laundering Council Sanctions — 100 mapped listings
- Philippines Top Most Wanted Persons in the Cordillera Regions — 84 mapped listings
- Malaysia Securities Commission AOB Enforcements — 77 mapped listings
- Indian Ministry of Home Affairs Banned Organizations — 73 mapped listings
- Singapore Targeted Financial Sanctions — 60 mapped listings
- Hong Kong ICAC Wanted Persons — 60 mapped listings
- Malaysia Securities Commission Investor Alert List — 53 mapped listings
- Australia Listed Terrorist Organisations — 52 mapped listings
- Kyrgyz National List — 38 mapped listings
- Azerbaijan Domestic List — 37 mapped listings
- Georgian Otkhozoria–Tatunashvili List — 33 mapped listings
- New Zealand Designated Terrorist Entities — 31 mapped listings
- India NIA Most Wanted — 29 mapped listings
- Vietnam MPS List of Terrorist Organizations and Individuals — 15 mapped listings
- Singapore MAS Enforcement Actions — 6 mapped listings
- Malaysia Financial Consumer Alert List — 5 mapped listings
- Taiwan MOJ Counter-Terrorism Financing Act Sanctions — 4 mapped listings

### Russia & Ukraine — 37,895 listings (9.0%)

Ukraine’s national sanctions register and blacklist, built mainly around the invasion, together with Russia’s own retaliatory listings.

- Ukraine NSDC State Register of Sanctions — 27,280 mapped listings
- Russian PMC Wagner mercenaries (Myrotvorets list) — 3,928 mapped listings
- Ukraine War and Sanctions — 2,477 mapped listings
- Ukraine SFMS Blacklist — 2,286 mapped listings
- Russia Personal Sanctions Targeting US Citizens — 2,140 mapped listings
- ACF List of War Enablers — 33 mapped listings
- Russian Persons of Interest published by Dossier Center — 12 mapped listings

### Multilateral — UN and other global bodies — 22,294 listings (5.3%)

Lists issued by the UN Security Council and other bodies that are not a single country. UN listings bind every member state, which then copies them into its own law.

- Companies Operating in the Uyghur Region — 8,848 mapped listings
- INTERPOL Red Notices — 6,238 mapped listings
- C4ADS Long Shadows (Xinjiang) — 3,375 mapped listings
- UN Security Council Consolidated Sanctions — 2,289 mapped listings
- Asian Development Bank Sanctions — 1,947 mapped listings
- WorldBank Debarred Providers — 1,897 mapped listings
- African Development Bank Debarred Entities — 1,873 mapped listings
- Inter-American Development Bank Sanctions — 1,741 mapped listings
- EBRD Ineligible Entities — 1,717 mapped listings
- OHCHR List of Companies Linked to Illegal Settlement in the West Bank — 211 mapped listings
- Global Energy Ownership Tracker — 170 mapped listings
- The Sentry Atlas — 76 mapped listings
- UN Security Council 1718 Designated Vessels List — 61 mapped listings
- C4ADS Fractured Veins (Xinjiang Mining Industry) — 53 mapped listings
- Wikidata Entities of Interest — 11 mapped listings
- Netherlands National "Sanctionlist Terrorism — 5 mapped listings
- Russian Oligarch/Billionaires Database — 1 mapped listings

### Latin America & Caribbean — 20,652 listings (4.9%)

National registers from Latin America, including Argentina’s terrorism register and Brazil’s register of suspended companies.

- Brazil National Register of Disreputable and Suspended Companies — 16,788 mapped listings
- Argentina RePET Sanctions — 2,423 mapped listings
- Brazil List of Individuals Disqualified from Public Service — 619 mapped listings
- Brazil Ministry of Labour and Employment slavery prevention list — 501 mapped listings
- Brazil Register of Persons Disqualified from Senior Roles — 307 mapped listings
- Brazil List of Debarred Bidders — 81 mapped listings
- Brazil Entities Prohibited from Offering Auditing Services — 2 mapped listings

### European Union institutions — 16,314 listings (3.9%)

Lists adopted by the Council of the EU and published in the Official Journal. They apply across all member states directly.

- EU Council Official Journal Sanctioned Entities — 14,138 mapped listings
- EU Financial Sanctions Files (FSF) — 9,507 mapped listings
- EU Consolidated Travel Bans — 4,770 mapped listings
- EU Sanctions Map — 2,201 mapped listings
- EU ESMA Suspensions and Removals — 2,022 mapped listings
- Europe Most Wanted Fugitives — 57 mapped listings
- EU ESMA Sanctions — 22 mapped listings
- EU Early Detection and Exclusion System (EDES) — 5 mapped listings

### United Kingdom — 15,565 listings (3.7%)

UK lists since it left the EU sanctions regime: the FCDO sanctions list and the Treasury’s investment bans.

- UK FCDO Sanctions List — 9,586 mapped listings
- UK Companies House Disqualified Directors — 5,885 mapped listings
- UK National Crime Agency Press Releases — 87 mapped listings
- UK HMT/OFSI Investment Bans — 39 mapped listings
- DPRK Reports — 5 mapped listings

### Middle East & North Africa — 10,615 listings (2.5%)

National terror-financing and asset-freeze registers across the region, several of them implementing UN Security Council Resolution 1373.

- Egypt Domestic Terrorist List — 3,654 mapped listings
- Türkiye Asset Freezing Sanctions List (MASAK) — 3,223 mapped listings
- Qatar Unified Record of Persons and Entities on Sanction List — 2,147 mapped listings
- Türkiye Ministry Of Interior Terrorist Wanted List — 1,607 mapped listings
- Israel Terrorists Organizations and Unauthorized Associations lists — 1,517 mapped listings
- Saudi Arabia National Terrorism List (UNSCR 1373) — 771 mapped listings
- Israel Prevention of Distribution and Financing of WMDs designations — 606 mapped listings
- United Arab Emirates Local Terrorist List — 509 mapped listings
- Türkiye Capital Markets Board Banned List — 337 mapped listings
- Iran Sanctions List — 307 mapped listings
- Tunisia National Counter-Terrorism List — 169 mapped listings
- Kingdom of Jordan National Sanctions List — 61 mapped listings
- Palestine National Terrorist Designations (UNSCR 1373) — 59 mapped listings
- Iraq Terrorist Fund Freezing Lists — 33 mapped listings
- Israel Sanctioned Crypto Wallets List — 7 mapped listings

### Canada — 7,887 listings (1.9%)

Canadian lists: autonomous sanctions under the Special Economic Measures Act, listed terrorist entities, and named research organisations.

- Canadian Consolidated Autonomous Sanctions List — 7,532 mapped listings
- Canadian Named Research Organizations list — 230 mapped listings
- Canadian Listed Terrorist Entities — 144 mapped listings
- Canadian Consolidated Autonomous Sanctions List on the Russian invasion of Ukraine — 62 mapped listings
- Canadian Freezing Assets of Corrupt Foreign Officials Act — 8 mapped listings

### Africa — 2,809 listings (<1%)

National sanctions and terrorism-financing lists published by African states.

- South Africa Targeted Financial Sanctions — 2,289 mapped listings
- South Africa Wanted Persons — 456 mapped listings
- Nigeria Sanctions List — 55 mapped listings
- Kenya FRC Domestic Terrorism List — 17 mapped listings

### Other authorities — 15 listings (<1%)

Lists whose publisher is not tied to one country.

- Netherlands Police Nationale Opsporingslijst — 15 mapped listings

---

Entities appear on several lists at once, so the per-list figures sum to more than the total. Each popup links the
record back to its source lists for checking.
