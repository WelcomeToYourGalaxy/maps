# Brief: the "Behind the scenes" writeup for each country — third version, written from scratch

These appear in each country's box on a public world map of child sexual abuse networks and child
trafficking (Welcome to Your Galaxy). The map is about **large-scale patterns** — how institutions,
networks, states and markets made abuse and trafficking possible and kept it going — not about
individual crimes.

The owner rejected the last version as "filled with dramatic prose, purple writing, circular sentences"
and asked for writing that aims "not for a compilation of facts but the narrative". Write each piece
from scratch from the packet. There is no previous draft to follow.

## What a piece is
A plain, connected account of how the patterns in this country worked, in the order things happened:
who did what, why they did it, what it allowed, and what happened afterwards. Like a careful chapter in
a reference book written for someone who knows nothing about the subject. Facts are joined by cause and
consequence ("because", "so", "after", "which meant", "as a result"), not listed.

Not a compilation: choose the few cases and figures that carry the story and leave the rest out. Usually
two to five cases are enough. A case or figure belongs only if the account needs it to show how the
pattern worked, how large it was, or what came of it.

## Plain writing — strict rules
- No opening generalisations or maxims ("Shutting a district rarely ends the trade", "Institutions protect
  themselves"). Begin with something that happened: a place, a year, an institution, a decision.
- No closing punchlines, summaries that restate the piece, or lines such as "X shows that…", "the lesson
  is…", "this is the measure of…", "what this teaches", "the clearest sign". No questions to the reader.
- No contrasts built for effect ("not X but Y", "less A than B"), no colon reveals, no sentences that build
  up and land on a short final clause. No metaphors.
- No sentence may repeat what the previous one said in other words. Each sentence adds something new.
- No emotive or dramatic vocabulary: not "chilling", "sinister", "shocking", "horrifying", "haunting",
  "stark", "dark", "web", "machinery", "playbook", "laundered", "exported" (unless quoting), "silence"
  used as a figure of speech, "behind closed doors".
- Plain words, short and medium sentences, active voice. Say who did it.
- Explain every institution, title and term in a few words on first use: "the Royal Commission, a
  national public inquiry with the power to require documents"; "the nuncio, the Vatican's ambassador";
  "a statute of limitations, the legal deadline for bringing a case".

## The ending
One short final paragraph (one to three sentences) that states plainly what this means today for the
country or for children there: what continues, what changed, what remains unknown. State it as a
conclusion drawn from the account, in the same plain tone. No advice, no questions, no slogans.

## Length
150–350 words in total. Countries with little material get shorter pieces. Do not pad.

## Facts — hard rules
- Use ONLY what is in that country's packet (patterns, role notes, pattern summaries, cases, flows,
  networks). Add nothing from memory: no names, dates, numbers or places that are not in the packet.
  General explanations of how a legal or institutional mechanism works (what extradition is, why a
  peacekeeper can only be tried at home) are allowed and wanted; specific facts must come from the packet.
- Do not import facts that belong to another country, even if a pattern summary mentions them, unless the
  packet ties them to this country.
- Keep status words exact: convicted, charged, accused, acquitted, found by an inquiry, alleged by…,
  disproved, could not be confirmed. Never make an allegation sound proven.
- Numbers exactly as given. Name people only as the packet does, with their status. Never name a victim.
- Where the country's role is only a gap (no surveys, no inquiry, few reports), write briefly and plainly
  about what has and has not been counted there and why, using the packet's figures. Do not invent cases.

## Output
JSON object at the output path you are given:
{"ISO3": {"story": "<paragraphs separated by \n\n>", "sources": ["<URLs from the packet you used>"]}, ...}
Every country in the input must appear. Save every ~5 countries. Validate with
python3 -c "import json;json.load(open(PATH))". No web access.

Before saving each piece, reread it once and delete any sentence that breaks a rule above.

## Example of the register wanted (Philippines, from its packet)
In 1992 the mayor of Manila, Alfredo Lim, closed Ermita, the district where most of the city's bars and
brothels were. The same year the United States closed Clark Air Base in Angeles City, north of Manila,
and the bars there lost the soldiers who had been their customers. Many of the businesses from Ermita
moved to Angeles City and began serving foreign tourists. In its 2025 report on trafficking, the US State
Department still listed Angeles City among the places in the Philippines where children are sold for
sex, and said most foreign offenders come from Australia, Japan, New Zealand, Britain and the United
States.

From 2006 the charity International Justice Mission worked with Philippine police on raids in several
cities, and by 2016 it found that the number of children sold in bars and on the street there had fallen
by 79 to 86 percent. Over a similar period, from 2014 to 2017, the number of Philippine internet
addresses used each month for the sexual exploitation of children rose more than twelvefold. Much of the
abuse had moved into homes, where an adult the child knew was paid by a viewer abroad to abuse the child
on a live video call. Because the buyers and the payments were abroad, in 2017, 64 percent of the cases
taken up by the Philippine police's anti-trafficking unit began with a referral from a foreign police force. In 2020 the Australian bank Westpac agreed to pay a A$1.3 billion
penalty that included failing to check payments that could be linked to this abuse.

Raids reduced the number of children sold in bars, and the abuse continued in homes, paid for from
abroad. Most of the people paying live in a few wealthy countries, and the records of their payments and
messages are held there.
