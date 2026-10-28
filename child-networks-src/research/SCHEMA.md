# Research schema — Child abuse networks and child trafficking map

Every record must come from a source you actually opened (WebFetch) or a search result
whose text states the fact. No fabrication. If a figure or date can't be confirmed,
leave the field out rather than guess. Prefer official sources: court judgments, grand
jury reports, royal commissions, parliamentary inquiries, government reports, UN bodies,
then major news outlets (AP, Reuters, BBC, Guardian, NYT, Le Monde, Der Spiegel, etc.),
then Wikipedia only when it carries a clear citation you could not open yourself.

## Safety rules (hard)
- Never include anything that helps someone find or access abuse material: no site
  addresses, onion links, forum access methods, search terms, file names or technical
  evasion methods. Platform NAMES already published by police (e.g. "Welcome to Video",
  "Boystown", "Kidflix") are fine.
- Never name a victim or survivor unless they chose to speak publicly under their own
  name AND naming them is essential. Default: don't.
- Name offenders only when convicted, charged, found responsible by an official inquiry,
  or the subject of a named official finding. Anyone merely accused is described as
  "accused" / "alleged" with who alleged it; anyone acquitted says so.
- Claims that were investigated and found false or unsupported (e.g. Operation Midland /
  Carl Beech, "Pizzagate") are still recorded, with status "disproved", because the
  map shows how false claims and real cases interact. Say who disproved it.
- No graphic description of abuse. State what happened in plain, factual terms.

## Output: one JSON file, an object with these arrays

```json
{
  "cases": [ ... ],
  "nets":  [ ... ],
  "flows": [ ... ],
  "notes": "free text: gaps, things you could not verify, leads for later"
}
```

### cases[] — one per documented case, inquiry finding, prosecution or official report
| field | meaning |
|---|---|
| id | short slug, unique, e.g. "irl-ryan-report" |
| n | short title, e.g. "Ryan Commission — Irish industrial schools" |
| iso3 | ISO 3166-1 alpha-3 of the country where it happened (use "XKX" Kosovo, "VAT" Holy See) |
| also | optional array of other ISO3 countries involved |
| place | town/region, as precise as the source allows |
| ll | [longitude, latitude] of that place (4 decimals max). Country centroid only if no place; then set "llc": true |
| y0 | year the abuse/trafficking began (or earliest documented year) |
| y1 | year it ended / last documented year |
| yf | year of the key official finding / conviction / report |
| first_report | year the first documented complaint/report reached police, church, employer or officials, if the sources state it (key for the "delay" pattern) |
| setting | one of: "religious", "care" (orphanages, care homes, boarding/residential schools, youth services, state care), "elite" (politicians, wealthy, celebrities, entertainment, sport, schools for the elite), "organized" (organized crime, street grooming networks, brothels, pimping families, trafficking rings), "tourism" (travelling offenders, sex tourism), "online" (online platforms, livestreaming, forums, apps), "conflict" (armed groups, militaries, peacekeepers, aid workers in emergencies), "adoption" (adoption trafficking, stolen babies, forced removal of children by states) |
| kind | "sexual abuse", "sexual exploitation", "trafficking", "abuse material", "child removal", "forced labour", or combinations joined by " + " |
| status | one of: "convicted", "inquiry" (official inquiry/commission/grand jury found it), "acknowledged" (institution or state admitted it / apologised / paid redress), "settled", "charged", "reported" (credible major-outlet investigation, no official finding), "acquitted", "disproved", "alleged" (only allegations; say whose) |
| victims | number of victims stated by the source (integer), plus "victims_note" if it is an estimate/range |
| offenders | number of offenders/perpetrators stated (integer), optional |
| who | institution/organisation/network involved (free text) |
| net | key of a record in nets[] if it belongs to one |
| officials | true if public officials (police, judges, politicians, civil servants, intelligence, military) were themselves involved OR documented as having covered it up / obstructed — explain in d |
| cover | short text: documented cover-up, obstruction, transfer of offenders, destroyed records, intimidation, lenient deal — only if the source documents it |
| d | 2–5 sentences, plain factual English, numbers and dates, who found what |
| cite | the source(s) in words: "Commission to Inquire into Child Abuse (Ryan Report), 20 May 2009" |
| url | best source URL (the one you opened) |
| url2 | optional second URL |

### nets[] — institutions, organisations, networks, platforms that recur
| field | meaning |
|---|---|
| k | slug key, e.g. "catholic-church", "epstein-network", "welcome-to-video" |
| n | name |
| type | "religious" / "care" / "elite" / "organized" / "online" / "conflict" / "adoption" / "state" |
| iso3 | HQ country |
| hq | HQ city |
| ll | [lng, lat] of HQ |
| y0, y1 | active years (y1 omitted if active) |
| status | "active" / "dismantled" / "dissolved" / "convicted" / "reformed" etc. |
| reach | array of ISO3 where it is DOCUMENTED to have operated (with a case, branch or finding) |
| reach_est | array of ISO3 where presence is likely but not documented (say why in reach_note) |
| reach_note | text |
| d | 2–5 sentences |
| cite, url | source |

### flows[] — documented movements between places (people, children, offenders, money, transferred abusers)
| field | meaning |
|---|---|
| id | slug |
| n | title, e.g. "Nepal → India brothel trafficking" |
| type | "trafficking" (victims moved), "offenders" (travelling offenders / sex tourism), "transfer" (abusers moved by an institution to another place/country), "adoption" (children sent for adoption), "removal" (forced deportation/removal by a state), "money" (payments for abuse, e.g. livestream payments), "material" (where abuse material is hosted/sent) |
| from, to | place names |
| a, b | [lng, lat] of from and to |
| iso_a, iso_b | ISO3 |
| y0, y1 | years |
| size | number moved if a source states it (and "size_note") |
| net | optional nets[] key |
| d | 1–3 sentences |
| cite, url | source |

Aim for completeness within your domain: every country where an official finding exists.
Breadth across the world matters — Africa, Asia, Latin America, Middle East, Pacific —
not only Europe/North America. Where documentation is thin, record what exists and put
the gap in "notes".
