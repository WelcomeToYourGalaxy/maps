# Lender offices dataset: notes

Read on 2026-11-03 (US Pacific time; the last fetches ran early on 2026-11-04 UTC). File: `offices.json`, 576 records.

## Rules followed
- Every office comes from a page that was actually opened (fetched) on the date above. The `src` field gives that page.
- Nothing was added from memory. If a page named a country but gave no city, the office was left out. Examples are listed under "Left out" below.
- Coordinates are city-level and every record has `"ap": true`. They come from the GeoNames `cities1000` gazetteer (download.geonames.org, read the same day). The one exception is Sandton, South Africa, which is not in that file, so its coordinates came from OpenStreetMap Nominatim.
- ISO3 codes come from the GeoNames `countryInfo.txt` file, plus XKX for Kosovo. Palestinian offices use PSE. EIB writes its West Bank and Gaza office as being in Jerusalem, so that record is plotted at Jerusalem.
- `kind` follows the lender's own wording. Headquarters are marked "headquarters". "Regional hub", "regional office", "regional representation", "regional division" and a lender's liaison or representative office in a donor capital are marked "regional office". Everything else (resident mission, country office, representative office in one country) is marked "country office".
- Duplicate check: no two records share the same lender + city + kind. Where a page described one office under two titles (for example AFD "East Africa Regional Office" and "Kenya Office" at the same address), the two were merged into one "regional office" record.

## Counts per lender
| key | records | directory used |
|---|---|---|
| wb | 100 | worldbank.org/ext/en/contacts ("Regions & Countries" contacts with office addresses) |
| ifc | 1 | ifc.org/en/contact-directory (headquarters only, see below) |
| miga | 19 | miga.org/contact |
| imf | 4 | imf.org/en/countries/resrep/index.md (regional offices whose city is stated) |
| idb | 0 | could not be opened |
| adb | 32 | adb.org/contacts |
| afdb | 0 | could not be opened |
| ebrd | 46 | ebrd.com/home/contacts/ebrd-contacts-list.html |
| eib | 63 | eib.org/en/contact/offices |
| aiib | 2 | aiib.org/en/contact/index.html |
| ndb | 6 | ndb.int/contact/ |
| cdb | 2 | cdb.com.cn/English/ (homepage footer, plus Hong Kong Branch named in homepage announcements) |
| cexim | 8 | english.eximbank.gov.cn contact page (headquarters); eximbank.gov.cn/aboutExim/organization/branch/ and each overseas office's own page |
| jica | 98 | jica.go.jp regional office directories (asia, oceania, america, africa, m_east, europe) and the structure page (headquarters) |
| jbic | 20 | jbic.go.jp/en/about/ ("Domestic and Overseas Network") |
| kfw | 79 | kfw-entwicklungsbank.de Local-presence pages (5 regions); kfw.de locations page; deginvest.de locations page (DEG offices are filed under kfw) |
| afd | 75 | afd.fr/en/our-network-africa, -latin-america, -orients, -three-oceans; headquarters from afd.fr/en/our-agencies-around-world |
| dfc | 1 | dfc.gov/who-we-are/contact (headquarters; no overseas offices are listed on the site) |
| fmo | 5 | fmo.nl/address |
| proparco | 15 | proparco.fr/en/our-regional-offices and each regional office's own page; headquarters from proparco.fr/en/contact |
| bii | 0 | could not be opened |

By kind: 18 headquarters, 107 regional offices, 451 country offices.

## Directories that failed
- **IMF**: imf.org returned HTTP 403 to direct requests. The resident-representative index was read once through the WebFetch tool. It lists 86 resident representative offices and 9 regional offices, but gives no cities for the resident offices. Only the 4 regional offices with a stated city were kept: Vienna, Riyadh, Paris and Brussels. No page stating the IMF headquarters address was opened, so IMF headquarters is not in the file. To fill this in, the 86 per-country pages (imf.org/en/countries/resrep/<iso3>) would need to be read for their addresses.
- **IFC**: the contact directory loads its office list with JavaScript from a separate data service. Querying that service was blocked by the session's permission system, so only IFC headquarters (from the directory page itself) is included. The where-we-work regional pages could not be read either.
- **IDB / IDB Invest** (iadb.org): HTTP 403 bot protection. The WebFetch fallback hit its hourly rate limit. Nothing included.
- **AfDB** (afdb.org): HTTP 403. The WebFetch fallback hit its rate limit. Nothing included.
- **BII** (bii.co.uk): HTTP 403. Nothing included.
- **China Development Bank**: the overseas-office pages (cdb.com.cn/English/gykh_512/zzjg/...) returned HTTP 412 (a bot challenge). Only headquarters and the Hong Kong Branch are included, both taken from the English homepage.

## Left out (page named the place but gave no city, or pointed to another country's office)
- **WB**: Guinea-Bissau, Belize, Haiti, Suriname, Venezuela, Djibouti, Egypt, Iraq, Jordan, Libya, Syria and West Bank & Gaza have no address or city on the page. Georgia and Bulgaria have a street address but no city. Contacts listed "in" another country's office were not repeated (for example Eritrea, South Sudan, Somalia, Seychelles, Equatorial Guinea, Gabon, Namibia and Philippines; the Philippines contact uses the Singapore address).
- **MIGA**: "presence in Panama" gives no city. Rome is a named contact location (Italy Country Head) and is included with a note in its name.
- **EBRD**: Canada, Czech Republic and Ukraine have no address. Estonia and Latvia point to the Vilnius office.
- **JICA**: Guatemala's address (Zona 10, Edificio Unicentro) gives no city. Kazakhstan is listed on the where-we-work page but has no entry in the office directory. Domestic Japanese branches were not included.
- **JBIC**: the Osaka Branch (domestic) was not included.
- **KfW**: Montenegro, Madagascar, Nigeria, Sierra Leone, Mauritania and Syria entries give only a Frankfurt phone or contact name. The Kyrgyzstan entry is headed "KfW Office Tashkent" but its address is in Bishkek; it was kept with the Bishkek address and a note in its name. KfW's domestic branches (Berlin, Bonn) and KfW IPEX-Bank were not included.
- **AFD**: "Central and East Asia Regional Office" is described only as "based in China", with no city.
- **Proparco**: the 11 "local branches" are named by country only (DRC, Lebanon, Palestine, Tunisia, Egypt, China, Bangladesh, Madagascar, Benin, Ghana, Senegal).
- **FMO**: none left out. The Costa Rica office sits inside Norfund's office in San Rafael de Escazú, so it is plotted at Escazú.

## Validation
`scripts/validate.py` checks the following and passes:
- lat/lng are numbers and within range
- iso3 is three capital letters
- lender keys and kinds come from the allowed sets
- every src is an http(s) URL
- no duplicate lender + city + kind
