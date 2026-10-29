# Expansion brief: complete the checklist of major official findings and kinds of patterns

The map (child abuse networks and child trafficking, now a layer of the anti-slavery map) must reach 100% of two
checklists, and show readers what those checklists are. Your job is to build your share of a checklist, mark what
the map already holds, and research every missing item into full records.

Read first:
- `research/SCHEMA.md` — the record format and the hard safety and sourcing rules. Every rule there applies.
- `research/existing_index.json` — the 564 cases already on the map (id, title, country, setting, status, year of finding).
  Match carefully: a finding may already be on the map under a different title (e.g. "Ryan Commission" vs "Commission to
  Inquire into Child Abuse"). Search titles, countries and years before deciding something is missing.

## What the map covers (scope)
Sexual abuse or sexual exploitation of children inside institutions or by organised networks, who shielded it, and the
trafficking, sale or illegal adoption of children (children given away under false papers or for money). Removals of
children by states with no documented sexual abuse and no sale or falsified identity are OUT of scope (they were taken
off the map on purpose). Abuse inside families (incest) on its own is out of scope unless the finding is about an
institution failing to act or an organised network.

## Checklist 1: major official findings
An item belongs on the checklist if ALL of these hold:
1. It is the published finding of an official body: a government-established inquiry, royal commission, commission of
   investigation, truth (and reconciliation) commission, parliamentary or congressional inquiry, grand jury report,
   attorney-general investigation report, ombudsman report, a review commissioned by a government, a court judgment that
   was the main finding on a whole network or institution, a UN commission of inquiry / fact-finding mission / UN-commissioned
   external review, or an ICC judgment; OR an independent investigation commissioned by a national-scale institution about
   itself (a national church, a national sports body, a national broadcaster, a religious order, a national youth
   organisation, a company of national standing).
2. Its subject is in scope (above).
3. Its reach is large: national or federal, OR a whole state/province/region, OR a whole institution, denomination,
   order, sector or programme in a country, OR it found 100 or more child victims.
Not on the checklist: single ordinary criminal trials, NGO or academic reports not commissioned by a government or the
institution, press investigations (these can stay on the map as cases but are not "official findings").

Find them systematically, not from memory alone. Useful starting points (open them; follow their sources):
- Wikipedia "Catholic Church sexual abuse cases by country" and each country article it links; "Anglican Church sexual abuse cases";
  "Sexual abuse scandal in …" articles; "List of child sexual abuse cases"; "Royal commission" lists; "Truth commission" lists.
- Government and parliament sites, national archives of inquiry reports, UN OHCHR commission of inquiry pages, UN SEA reports.
- National church conference sites that publish commissioned studies (Germany MHG, France CIASE, Portugal, Spain, Switzerland, Poland…).
- Bishop Accountability (bishop-accountability.org) lists of government and diocesan reports, by country — a good finding aid;
  cite the report itself, not the aid.
Then confirm each item from an official or major-outlet source you actually opened.

## Checklist 2: kinds of patterns (one agent only — see your assignment)
A fixed list of kinds, built from published typologies, each with a definition and its source:
- the institutional contexts examined by England and Wales's Independent Inquiry into Child Sexual Abuse (IICSA) and by
  Australia's Royal Commission into Institutional Responses to Child Sexual Abuse (institution types);
- the forms of sexual exploitation of children in the Luxembourg Terminology Guidelines / ECPAT typology;
- the forms of child trafficking in UNODC's Global Report on Trafficking in Persons (only the forms in scope: sexual exploitation,
  illegal adoption/sale, forced marriage where sexual exploitation is documented, recruitment by armed groups where sexual
  exploitation is documented, forced begging or criminality only where run by trafficking networks).
Merge overlaps into one clean list (about 20–35 kinds). For each kind, list the existing case ids that document it
(from existing_index.json) and, for any kind with fewer than 2 documented cases on the map, research cases to fill it
(prefer official findings; at least 2 per kind, from different countries where they exist).

## Output (one JSON file, path given in your assignment)
```json
{
  "checklist": [ {"name": "...", "iso3": "IRL", "body": "commission of investigation", "year": 2009,
                  "reach": "national | state | institution | 100+ victims", "url": "...", "case_id": "existing-or-new-id", "status": "on_map | added | excluded",
                  "why_excluded": "only if excluded: which rule"} ],
  "kinds": [ ...only the kinds agent... {"k": "slug", "label": "...", "definition": "...", "source": "...", "url": "...", "case_ids": ["..."]} ],
  "cases": [ ...new case records in SCHEMA.md format... ],
  "nets":  [ ...new network records, only if needed... ],
  "flows": [ ...new movement records, only if documented... ],
  "notes": "gaps, items you could not confirm, borderline calls"
}
```
- New case ids start with `x-` (e.g. `x-deu-mhg-2018`) so they cannot collide.
- `case_id` for an item already on the map is the existing id; for one you add, your new `x-` id.
- Every new case needs a `url` you opened, the forum that established it in `cite`, and `status` per SCHEMA.md
  (official findings are normally `inquiry`; a court verdict is `convicted`; an admitted institutional study is `acknowledged`).
- `d` is 2–5 plain sentences: who found what, when, with numbers. No dramatic words. Name offenders only as SCHEMA.md allows.
- Place each case at the town of the institution or the seat of the body that found it if no single site, with `llc: true`
  only when you truly have no place.
- Set `first_report` when the sources date the first complaint (it feeds the "years of waiting" pattern).
- Write the file as you go (rewrite it whole each time), so partial work survives. Validate it with `python3 -c "import json;json.load(open(PATH))"`
  before you finish. Do not edit any other file.
- Report back briefly: how many checklist items, how many were already on the map, how many you added, how many excluded and why,
  and anything you could not confirm.
