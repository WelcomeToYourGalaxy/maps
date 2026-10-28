# Brief: keep or drop each case

The map is a world map of child sexual abuse networks and child trafficking. The owner has decided its
point is **large-scale patterns, not individual cases**, and asked: "delete any one-time incidents not
connected to anything larger."

For each case record in your input, decide KEEP or DROP using only the record's own text.

KEEP if the record shows any of these (give the number):
1. A systemic finding: an inquiry, commission, grand jury, court-ordered review, government, UN or NGO
   report, audit, survey or study that covers many cases, an institution, a region or a country.
2. A network or ring: several offenders acting together, or an organisation, criminal group, platform,
   forum or armed group whose members or users abused or traded children.
3. Institutional handling: a church, order, school, care system, club, company, agency, army or UN
   mission knew and moved, protected, paid off, failed to report or concealed the offender, so the case
   shows how the institution behaves, not only what one person did.
4. Officials took part, protected the offender or obstructed the case (police, prosecutors, judges,
   politicians, ministers, soldiers, intelligence, diplomats).
5. Movement across borders or regions as part of a trade or practice: a trafficking route, travelling
   offenders as a recurring flow, an abuser transferred abroad, adoption from one country to another,
   deportation or removal of children.
6. A law, ban, suspension, settlement, bankruptcy or policy that responded to a pattern.
7. The record is itself about a recurring practice in a place (e.g. a red-light district, a sex-tourism
   destination, an industry, a custom such as child marriage or ritual servitude), or it documents a
   false claim that became a public movement (e.g. a viral hoax, a moral panic, a police operation built
   on a false story).

DROP if it is a one-time incident: one offender (or one household) abusing one or a few children, with
none of the above — no network, no institution protecting him, no officials involved, no cross-border
trade, no systemic finding — even when the offender was famous or was convicted. Also DROP an
individual's allegation, charge or acquittal that is not tied to any of the above.

When a record is borderline, decide by asking whether a reader would learn anything about a pattern from
it that the pattern's other records do not already show. If not, DROP.

## Output
Write a JSON list to the output path you are given:
[{"id": "...", "decision": "keep" | "drop", "rule": <1-7 or null>, "reason": "<one short line>"}, ...]
Every id in your input must appear exactly once. Validate with python3 json.load. No web access.
