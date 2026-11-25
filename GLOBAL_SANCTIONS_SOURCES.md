# Global sanctions and designation lists — sources

Source catalogue for `global_sanctions.html`. Data files live in `global_sanctions_data/`.

The map carries **421,241 mapped listings** from **217 official lists** published by governments,
the UN Security Council, the EU and financial regulators. Lists are aggregated through OpenSanctions,
which pulls each from its issuing authority's own published file. Nothing is added, inferred or edited here.

**54,355** designated targets publish neither an address nor a country — mostly crypto wallets,
securities and aircraft — and cannot be placed on a map.

## Kinds of list

| Kind | Listings | What it is |
|---|---:|---|
| Sanctions | 96,592 | Asset freezes, travel bans and trade restrictions imposed by governments or the UN Security Council. A listing is an executive decision by an authority, not a court verdict. |
| Warrants & criminal entities | 207,525 | People and companies wanted by police or prosecutors, including Interpol notices and national most-wanted lists. A warrant is an accusation that has not been tested in court. |
| Debarment | 188,392 | Companies and people barred from public contracts or development-bank funding, usually after a finding of fraud, corruption or collusion. |
| Regulatory watchlists | 134,486 | Firms and individuals flagged by financial regulators — unauthorised firms, investor warnings and licence refusals. |
| Wanted lists | 63,069 | Police most-wanted and fugitive notices. |
| Special-interest watchlists | 20,215 | Lists compiled for one specific concern, such as forced labour in supply chains or companies tied to a military. |
| Enforcement actions | 4,363 | Penalties, prosecutions and regulatory notices already issued against a party. |

The sanctions layer loads with the map. The others load when their box is ticked.

## Location precision

Each point says in its popup how precisely it is placed.

| Precision | Listings | What it means |
|---|---:|---|
| Street address | 7,716 | The list publishes a street address and it resolves to that address. |
| City or locality | 197,844 | The list publishes a town, city or district; the point sits at its centre, not at the entity’s address. |
| Country only | 215,681 | The list publishes only a country, or an address nothing could resolve; the point sits at the country’s centre. |

City-level and country-level points are **not** the entity's address. Street-level points come either from
the geocoded address set built for the original OFAC map or from a street geocoder; city points are resolved
against the GeoNames gazetteer (237,395 places, with multilingual name variants) constrained to the country
the list names.

## How the files fit together

- `global_sanctions.html` — the map. Loads MapLibre GL and the Culprits basemap module, then fetches the data below.
- `global_sanctions_data/meta.json` — list names, descriptions, groupings, counts.
- `global_sanctions_data/<kind>.json.gz` — one gzipped shard per kind of list.

## Lists carried

### Multilateral — UN and other global bodies

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

### United States

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

### European Union institutions

- EU Council Official Journal Sanctioned Entities — 14,138 mapped listings
- EU Financial Sanctions Files (FSF) — 9,507 mapped listings
- EU Consolidated Travel Bans — 4,770 mapped listings
- EU Sanctions Map — 2,201 mapped listings
- EU ESMA Suspensions and Removals — 2,022 mapped listings
- Europe Most Wanted Fugitives — 57 mapped listings
- EU ESMA Sanctions — 22 mapped listings
- EU Early Detection and Exclusion System (EDES) — 5 mapped listings

### United Kingdom

- UK FCDO Sanctions List — 9,586 mapped listings
- UK Companies House Disqualified Directors — 5,885 mapped listings
- UK National Crime Agency Press Releases — 87 mapped listings
- UK HMT/OFSI Investment Bans — 39 mapped listings
- DPRK Reports — 5 mapped listings

### Russia & Ukraine

- Ukraine NSDC State Register of Sanctions — 27,280 mapped listings
- Russian PMC Wagner mercenaries (Myrotvorets list) — 3,928 mapped listings
- Ukraine War and Sanctions — 2,477 mapped listings
- Ukraine SFMS Blacklist — 2,286 mapped listings
- Russia Personal Sanctions Targeting US Citizens — 2,140 mapped listings
- ACF List of War Enablers — 33 mapped listings
- Russian Persons of Interest published by Dossier Center — 12 mapped listings

### Europe — national lists

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

### Middle East & North Africa

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

### Asia & Pacific

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

### Canada

- Canadian Consolidated Autonomous Sanctions List — 7,532 mapped listings
- Canadian Named Research Organizations list — 230 mapped listings
- Canadian Listed Terrorist Entities — 144 mapped listings
- Canadian Consolidated Autonomous Sanctions List on the Russian invasion of Ukraine — 62 mapped listings
- Canadian Freezing Assets of Corrupt Foreign Officials Act — 8 mapped listings

### Africa

- South Africa Targeted Financial Sanctions — 2,289 mapped listings
- South Africa Wanted Persons — 456 mapped listings
- Nigeria Sanctions List — 55 mapped listings
- Kenya FRC Domestic Terrorism List — 17 mapped listings

### Latin America & Caribbean

- Brazil National Register of Disreputable and Suspended Companies — 16,788 mapped listings
- Argentina RePET Sanctions — 2,423 mapped listings
- Brazil List of Individuals Disqualified from Public Service — 619 mapped listings
- Brazil Ministry of Labour and Employment slavery prevention list — 501 mapped listings
- Brazil Register of Persons Disqualified from Senior Roles — 307 mapped listings
- Brazil List of Debarred Bidders — 81 mapped listings
- Brazil Entities Prohibited from Offering Auditing Services — 2 mapped listings

### Other authorities

- Netherlands Police Nationale Opsporingslijst — 15 mapped listings

---

Entities appear on several lists at once, so the per-list figures sum to more than the total.
Each popup links the record back to its source lists for checking.
