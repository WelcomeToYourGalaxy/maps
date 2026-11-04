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
