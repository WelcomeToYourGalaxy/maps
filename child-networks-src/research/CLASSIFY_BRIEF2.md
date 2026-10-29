# Brief: a second pass — drop cases confined to one institution

The map is about large-scale patterns. The owner has already had one-time incidents removed, and now says that
reports covering a single school or a single children's home "veer into isolated cases", which they leave out on
purpose. Apply that to every record in your input.

DROP a record if its subject is confined to ONE institution or ONE site (one school, one boarding school, one
children's home or orphanage, one hospital or clinic, one club or team, one camp, one parish, one monastery or abbey,
one shelter, one detention centre) or to ONE offender, AND the record shows no link to anything wider. This applies
even when the institution's own report counted many victims or several offenders, and even when the institution hid
it internally.

KEEP a record confined to one institution only if the record itself shows at least one of these:
- the case is part of a wider documented structure: a network or ring reaching beyond the institution, offenders
  moved to or from other institutions or countries, or the institution's national body / order / denomination /
  government directing or covering it up beyond the one site;
- officials outside the institution (police, prosecutors, judges, ministers, civil servants, politicians, soldiers,
  intelligence) took part, protected offenders or obstructed the case;
- it was the trigger or a named part of a national inquiry, law or wave of findings that is about many institutions
  (say which), so that a reader needs it to follow that wider pattern;
- children were trafficked, sold or adopted across borders through it.

KEEP every record whose subject is wider than one institution: a whole diocese, order, denomination, sector, care
system, region, country, platform, network, armed group, trade, route or practice, or a finding covering several
institutions.

Use only the record's own text. When unsure, ask whether the record shows something about a pattern beyond its one
institution. If not, DROP.

## Output
Write a JSON list to the output path you are given:
[{"id": "...", "decision": "keep" | "drop", "rule": null, "reason": "<one short line>"}, ...]
Every id in your input must appear exactly once. Validate with python3 json.load. No web access.
