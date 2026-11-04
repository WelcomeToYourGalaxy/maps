# Brief: audit and rewrite entries on the "Infiltration Map"

The map (welcometoyourgalaxy.github.io/maps/secret_society_infiltration.html) shows cases where an outside force got inside a government, an international body or a company. Readers are general-audience novices. The site keeps a strict no-fabrication standard.

The owner complained about two things:
1. Some entries are not infiltration at all. Example: Erik Prince's security firms openly signing contracts with Ecuador, Haiti and DR Congo, and a UN panel finding he broke the Libya arms embargo. Those are mercenary contracting and sanctions-breaking, not infiltration.
2. Many descriptions leave gaps a novice cannot fill. Example: "Sky Global / Sky ECC" opens "Its chief executive was indicted..." without saying what the company is, who got inside what, or why this counts as infiltration. (That one is really a company selling encrypted phones that criminals used; police then hacked it. Selling a product to criminals is not someone getting inside the company to steer it.)

## Step 1 — the test (apply to every entry)

An entry counts as infiltration only if ALL of these hold:
- **An outside party** (a government or spy service, a crime group, a company or industry, a bank or banking family, a secret society or lodge, a religious movement, an elite club or policy network, a political/armed movement, a lender) —
- **gets its people, its money, or its control inside** a government body, an international body, or a company (placing members or agents in posts, paying officials, secret membership of office-holders, secretly owning or controlling the organisation, writing its rules or laws from outside, recruiting insiders) —
- **so that decisions there serve the outside party**, in a way that is hidden, undeclared, or goes beyond what was openly agreed.

**ALSO COUNTS (correction — this is central to the map):** office-holders who belong to a society, lodge, order, religious movement or network that works to get its members into office or to steer policy from inside — the Orange Order, the Afrikaner Broederbond, Freemasonry/P2, Nippon Kaigi, Opus Dei, the RSS, the Unification Church, the Gülen movement — counts EVEN WHEN THE MEMBERSHIP IS OPEN, when the record shows its members holding posts (e.g. "15 of Japan's 19 cabinet ministers belonged to Nippon Kaigi"). Keep those and write them as such. A foreign government paying or recruiting officials, MPs or aides counts. Unauthorised foreign "police stations" or plots run on another country's soil count only if the record shows someone inside the host's institutions working for them.

**ALSO COUNTS — the revolving door:** a company's, bank's or industry's own people moving into the government posts that regulate, tax or buy from it (e.g. a Goldman Sachs executive becoming the finance minister or a central banker; an industry lawyer writing the law that governs the industry) counts, when the record shows them in that post. Write it as that: who moved from where into which post, and what they then decided.

Fails the test (verdict "drop"): open, declared contracts or sales (a mercenary firm hired by a government; a company selling phones, guns or software to criminals); ordinary crimes or fraud by an organisation's own people with no outside party; a firm merely failing anti-money-laundering checks (a casino or bank fined for weak monitoring) unless the record shows a crime group placed or paid staff inside it or controlled it; sanctions-breaking or smuggling with no one inside an institution; police hacking a criminal network; organisations merely existing or being designated.

Borderline: if the record itself contains a real infiltration angle (e.g. a cartel owning the casino, a minister secretly on a payroll, a senator's own companies running the operation), keep it and rewrite so that angle leads. Do not stretch: if you have to invent the angle, drop.

## Step 2 — rewrite every entry you keep (field "d", and "n" if unclear)

- First sentence says plainly **who got inside what, and how** — e.g. "The Sinaloa Cartel paid Mexico's top federal security official to protect its shipments."
- Explain in a few words anything a novice would not know: what an organisation is, what an office does, what a term means (racketeering, designation, junket, lodge...). Name people and organisations instead of "its", "the company", "the network" with no antecedent.
- Then: how it came to light, what happened (verdict, inquiry, charges), and what it changed or still affects. Keep it connected — no list of disconnected facts.
- Plain, direct sentences. No purple prose, no rhetorical flourishes, no sentences that build to a punchline, no aphorisms. Show the mechanism and figures rather than characterising them ("shocking", "vast" etc. are banned).
- About 60–130 words.
- **No fabrication.** Keep every date, figure and name that is in the original record, and do not change them. You may add widely established background context (what Blackwater is, what Interpol does). Any NEW specific fact (a date, number, name, verdict) must be confirmed with WebSearch first, and then its source must be appended to "cite". If unsure, leave it out.
- "n" (title): short, plain, says who and what (e.g. "Sinaloa Cartel paid Mexico's security chief"). Max ~70 characters. Rewrite only if the current one is unclear or misleading.
- If the category fields are wrong for the rewritten entry, you may correct: "inf" (one of state, crime, corp, money, lodge, faith, elite, movement, lender), "who" (short name of who reached in), "tgt" (gov, intl, company).
- Write in British spelling, matching the existing text.

## Output

Write a JSON array to the output path you are given, one object per input entry, in the same order:
```
{"i": <same i>, "verdict": "keep" | "drop", "reason": "<one sentence, only for drop>",
 "n": "<title, always present>", "d": "<new description, keep only>", "cite": "<only if you appended a source>",
 "inf": "...", "who": "...", "tgt": "..."   // only if changed
}
```
Every input entry must appear in the output. Validate the file parses as JSON (python3 -c "import json;json.load(open(PATH))") before finishing. Reply with just the count kept, dropped, and two example drops.
