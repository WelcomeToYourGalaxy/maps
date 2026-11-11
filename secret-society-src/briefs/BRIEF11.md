# Brief 11: tighten the infiltration test, and add a "why it counts" line to every case

The Infiltration Map (a globe for general-audience novices) shows cases where an outside party got inside a government, an international body or a company. The owner says some entries still are not directly about infiltration. Their examples: "Skull and Bones member Steven Mnuchin as Treasury Secretary" (one official who happened to belong to a university secret society, with nothing showing the society steered anything through him), and a lender/creditor case they did not see as infiltration.

## The test (apply strictly to every case)

KEEP only if the record itself shows ALL of:
1. An outside party: a foreign government or spy service, a crime group, a company or industry, a bank or banking family, a secret society or lodge, a religious movement, an elite club or policy network, a political or armed movement, or a lender.
2. Its people, money or control got INSIDE a government body, an international body or a company: agents or members placed in posts, officials or staff paid or recruited, secret ownership or control, the outside party writing the institution's rules or laws, its own executives moved into the post that regulates or buys from it.
3. And through that, decisions or actions inside the institution served the outside party (or the outside party clearly set out to make them do so — recruitment of a spy inside a ministry counts even if caught early).

DROP when:
- It is only that an office-holder belonged to a club, society, lodge, church or alumni network, with nothing in the record showing the group used them to steer decisions or worked to place its members in office. (Keep group-level cases where the record shows the group placing members or steering policy: e.g. the Broederbond running apartheid governments, P2's members across the state, Nippon Kaigi's agenda pursued by its cabinet members, a church's own party holding seats to pursue its aims.)
- It is only that someone from a company or bank took a government post, with no decision shown that served their former firm or industry. (Keep when the record shows what they then did for it, e.g. a bank chief becoming regulator and rewriting rules his former industry wanted.)
- An outside party acted openly from outside: a lender's public loan conditions, a treaty, sanctions, a public lobbying campaign, an open contract, a takeover, a war, a hack, a disinformation campaign — unless the record shows the outside party's people placed inside running an institution or officials secretly working for it. (Creditors' agents directly running a country's tax collection or customs DO count: their own people sit inside and run a state function. Say so plainly in the why line.)
- Infiltration is incidental to the story (a crime or scandal where officials are a side detail), or it is a crime by an institution's own people with no outside party.
- The record is too vague to say who got inside what.

Be decisive and consistent. Do not stretch to keep a case; if you would have to invent the inside angle, drop it.

## For every case you keep, write "why"

One plain sentence, about 15–30 words, for a novice, saying how this is infiltration: who the outside party is, what it got inside, and whose interests decisions then served. Do not repeat the description; sum up the mechanism. No flourishes or punchlines; no "This is a classic example". Model:
- "The cartel's money put the official in charge of fighting it on its side, so the state's own police protected its shipments."
- "A foreign intelligence service recruited someone inside the defence ministry to pass it secrets that ministry was meant to keep."
- "Bank executives moved into the office that regulates banks and then loosened the rules their former industry had asked to change."
Use only facts in the record. British spelling.

## Output

JSON array, one object per input case, same order: {"i": <i>, "verdict": "keep"|"drop", "why": "<keep only>", "reason": "<drop only, one sentence>"}. Write it to the output path given, validate with python3 json.load, and confirm every input i appears. No web search needed. Reply with counts kept and dropped and every dropped title with its reason in a few words.


## Settled rulings (10 November 2026) — apply these, do not re-argue them

These were open questions put to the owner, who asked for the most defensible reading. Each is written so a later round can reverse it knowingly.

1. **An insider of the same institution is not an outside party.** Mohamed bin Hammam's $40,000 envelopes for Caribbean Football Union delegates stay off the map: he was himself president of Asian football and a candidate in FIFA's own presidential election, so this is vote-buying inside football's own governance. The confederation question is not what decides it — the outside/inside structure is. The same rule disposes of the seven near-identical FIFA guilty pleas.

2. **A named ruling house in an absolute monarchy counts as a named office.** Strukton's payment for a "high-ranking member of the ruling family" in Riyadh stays. But where a prosecutor says money was paid to an agent *in order to* bribe and does not say it reached anyone, the record is `probable`, not `established`, and the "why" line must use the prosecutor's wording. Strukton has been moved to `probable` on that ground. Congo/Petronor was already `probable` and is unaffected.

3. **Buying the outcome of your own case is in scope.** A defendant, litigant or applicant who pays a judge, prosecutor or official so that their own matter is decided their way is an outside party whose money got inside the body that decided it. The Kyiv judge Chaus record, the NABU prosecutor record and the immigration-officer records stay. The payer may be identified by role rather than by name ("a defendant seeking a suspended sentence") as long as the record says so. What remains out is an institution's own staff defrauding that institution, with no outside party — the reason national anti-corruption agencies' own procurement-fraud bulletins are not a source for this map.

4. **An official paid to issue documents is infiltration; a state-run passport programme is not.** Both Samoa records stay. REVIEW's exclusion has been reworded to say so.

5. **A sanctions designation's own assertion caps a record at `probable`.** Where the only evidence that the outside party got inside is an executive designation saying so — no court finding, no independent reporting, no documented appointment or seat — the record is `probable`. Nine records were moved down on this ground. Designations stay `established` where the placement is a matter of public record anyway (a seat held, a post appointed to, a commission's finding) or where independent sources are cited alongside. A multilateral debarment after the lender's own sanctions process (African Development Bank, World Bank) is an adjudication, not an assertion, and stays `established`.

6. **A designation that names no payer still counts if it names a class of payer and the decision.** The Treasury finding that Zimbabwe's president shields gold and diamond smugglers and takes bribes from them stays, at `probable`, because the record says in its own text that the release names no payer. Dropping a US government finding about a head of state would be filtering the data, not applying the test.

7. **Open, declared arrangements are still out.** The Djibouti drop stands: Chinese loans and a declared military base are open arrangements, and a warning about leverage is not a finding of control inside the government. The second Djibouti drop — budget ministry officials arrested with traders — stands too, as the ministry's own officials with no outside party identified.

8. **Herbalife/China is closed, not a lead.** The SEC order was read in full; it anonymises every body. See `data/removed_records.json`.

9. **Alexion/Turkey and Alexion/Russia are recovered.** The SEC order (34-89214) names commissions in Turkey's Ministry of Health and chief non-staff specialist advisers to Russia's Ministry of Health. Both are now on the map, placed at the seat of the national ministry. This is the template for the other city-inference drops: go to the underlying order, not the press release.
