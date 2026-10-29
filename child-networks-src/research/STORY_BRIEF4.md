# Brief: the "Behind the scenes" writeup for each country — fourth version

These appear in each country's box on a public world map of child sexual abuse networks and child
trafficking (Welcome to Your Galaxy). The map is about large-scale patterns: how institutions, networks,
states and markets made abuse and trafficking possible and kept it going. It deliberately leaves out
isolated cases (one offender, one school or home, with nothing wider).

The owner rejected the previous version with these words: the writeups "are still not meta narratives
about what goes on in each country; they're still too much like compilations of big facts that
ultimately remain isolated. It's not a story about (what goes on in) the country."

## What a piece is now
An account of **how the abuse and trafficking of children works in this country** as a whole: the
system, not a sequence of inquiries. A reader should finish it knowing:
- which forms are documented there (for example: sale of children for sex to foreign visitors, abuse in
  church or state institutions, children moved across a border for sex work, online abuse paid from
  abroad, illegal adoption, armed groups), and which of them is the largest part of the record;
- how it operates: where children come from and why they are reachable (poverty, care systems,
  migration, conflict, an institution's control over them), who recruits, moves or abuses them, who pays,
  and where it happens;
- what lets it continue: who knew, who protected whom, which laws, deadlines, courts, police or
  institutions failed or were bypassed, how the country's place in cross-border flows matters;
- how the state and society have responded, and what that changed and did not change.

Write it as connected paragraphs, each paragraph about one part of that system (a form of abuse, a
mechanism, a response), not about one case. Cases and figures go inside the sentences as evidence for a
claim about the system ("Church authorities in X moved accused priests between parishes rather than
reporting them; the 2018 grand jury found 301 priests in six dioceses had been handled this way"), never
as the subject of a paragraph of their own. Join the parts by cause and consequence, so the pieces add up
to one picture of the country.

Use the patterns and their role notes: they say what part the country plays in each cross-country
structure (sending country, destination, home of the offenders, place of a cover-up, and so on). Use the
flows: they show where children are taken from and to. Use the indicators to say how large the problem
is thought to be and how the state is rated, saying whose measure it is. Use networks: they show which
organisations recur.

Do not list. If a paragraph reads as "In year A, inquiry X found…; in year B, inquiry Y found…", rewrite
it as a claim about what goes on, supported by the two findings.

## Plain writing — strict rules (unchanged)
- No opening generalisations or maxims about the world. Begin with this country: what is documented
  here and where.
- No closing punchlines, summaries that restate the piece, or "X shows that…", "the lesson is…". No
  questions to the reader.
- No contrasts built for effect ("not X but Y"), no colon reveals, no sentences that build up and land on
  a short final clause. No metaphors.
- No sentence may repeat what the previous one said in other words.
- No emotive or dramatic vocabulary: not "chilling", "sinister", "shocking", "horrifying", "haunting",
  "stark", "dark", "web", "machinery", "playbook", "laundered", "silence" as a figure of speech,
  "behind closed doors", "culture of".
- Plain words, short and medium sentences, active voice. Say who did it.
- Explain every institution, title and term in a few words on first use.

## The ending
One short final paragraph (one to three sentences) stating plainly where things stand: what continues,
what changed, what is not known. Same plain tone. No advice, no slogans.

## Length
200–400 words. Countries with little material get shorter pieces (as short as 80 words). Do not pad.

## Facts — hard rules (unchanged)
- Use ONLY what is in that country's packet. Add nothing from memory: no names, dates, numbers or places
  that are not in the packet. General explanations of how a legal or institutional mechanism works are
  allowed; specific facts must come from the packet. A claim about the system must be supported by the
  packet's cases, flows, role notes or indicators; do not generalise beyond what they support ("the
  records show", "in the cases on record" are fine ways to keep a claim within its evidence).
- Do not import facts that belong to another country unless the packet ties them to this country.
- Keep status words exact: convicted, charged, accused, acquitted, found by an inquiry, alleged by…,
  disproved, could not be confirmed. Never make an allegation sound proven.
- Numbers exactly as given. Name people only as the packet does, with their status. Never name a victim.
- A case whose packet entry reads as one offender at one place with nothing wider should not be used
  unless it is the only evidence of a wider pattern the packet documents.
- Where the record is thin, say what is and is not counted there and why, using the packet's figures.

## Output
JSON object at the output path you are given:
{"ISO3": {"story": "<paragraphs separated by \n\n>", "sources": ["<URLs from the packet you used>"]}, ...}
Every country in the input must appear. Save every ~5 countries (rewrite the whole file). Validate with
python3 -c "import json;json.load(open(PATH))". No web access.

Before saving each piece, reread it and check: does each paragraph describe part of what goes on in the
country, with cases as evidence? Does any sentence break a rule? Fix it.

## Example of the shape wanted (Philippines, from its packet)
Two forms of child sexual exploitation dominate the Philippine record, and both are paid for mainly by
men from abroad. One is the sale of children in bars and on the street in tourist districts. When the
mayor of Manila closed the Ermita bar district in 1992, the same year the United States left Clark Air
Base, many of its businesses moved to Angeles City and turned to foreign tourists; the US State
Department's 2025 report still names Angeles City as a place where children are sold for sex, and lists
Australia, Japan, New Zealand, Britain and the United States as the offenders' main home countries.

The other form takes place in homes. An adult the child knows, often a relative, is paid by a viewer
abroad to abuse the child on a live video call. It grew as street and bar exploitation fell: police raids
supported by the charity International Justice Mission from 2006 cut the number of children sold in bars
and on the street by 79 to 86 percent by 2016, while from 2014 to 2017 the number of Philippine internet
addresses used each month for this abuse rose more than twelvefold.

Because the buyers and their payments are abroad, Philippine police depend on foreign forces to find
cases: in 2017, 64 percent of cases taken up by the national police's anti-trafficking unit began with a
referral from another country. The money passes through foreign banks; in 2020 the Australian bank
Westpac agreed to a A$1.3 billion penalty that included failing to check payments that could be linked to
this abuse.

Exploitation in bars has fallen and exploitation in homes continues. The records of who pays are held
mostly in the countries the buyers live in.
