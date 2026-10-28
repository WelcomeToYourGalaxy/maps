# Brief: rewrite the "Behind the scenes" country writeups

These sit in each country's box on a public world map of child sexual abuse networks and child
trafficking (Welcome to Your Galaxy). The first version failed: the owner's verdict was that they are
"still largely repeated facts and assuming that novice reader has background context to piece it into
something meaningful."

Your job is to rewrite each country's piece so a reader who knows nothing — no history, no institutions,
no acronyms — finishes it understanding **how the thing worked**, not just **that it happened**.

## The rule that matters most
Facts are the evidence, not the content. Every fact in the piece must be doing one of three jobs:
showing a mechanism, showing its scale, or showing what happened to it afterwards. If a fact is in the
packet but does none of those three in your piece, leave it out. A piece with four facts fully explained
beats one with fifteen listed.

Before you write a country, decide in one sentence: **what is the mechanism this country shows?**
(For example: "an institution that moves an abuser instead of reporting him", "a state that takes
children from the families it is suppressing", "a trade that moved indoors when the law reached the
streets", "a country that has never been measured".) Write the piece to teach that one mechanism, using
that country's record as the worked example. Where a country shows two or three mechanisms, take them in
turn, but name each one before you illustrate it.

## Explain, never assume
- Name the role of every person, body and term the first time: not "the Ryan Commission" but "a nine-year
  public inquiry with the power to compel evidence, known after its chairman as the Ryan Commission";
  not "Savile" but "Jimmy Savile, one of the BBC's best-known television presenters"; not "a nuncio" but
  "the Vatican's ambassador"; not "Tier 2" but "the second of four grades the US State Department gives
  governments for their effort against trafficking".
- Explain what a mechanism *is* before or as you show it: what a statute of limitations is and what
  running out of time does to a case; why bankruptcy caps what survivors can recover; why troops can only
  be tried by their own country; why "reports to the CyberTipline" measure how many people use American
  apps as much as how much abuse there is.
- After a fact, say what it meant. "Which meant…", "the effect was…", "so when X happened, Y could not".
  A date or a number on its own is noise to a novice.
- Say why the people involved did it: what protecting the institution got them, what the money was for,
  why an official looked away. Motive is what makes a mechanism make sense.

## Shape
- 200–400 words of story, then a closing paragraph of 2–3 sentences: what this country teaches a reader
  about how these things work, and what to ask when they next read a headline. Make the closing specific
  to this mechanism, never generic.
- Start somewhere concrete — a place, a year, a decision. Move forward in time. Paragraphs, no headings,
  no bullet points, no lists of names or places strung together with commas.
- Plain words, short and medium sentences. The owner's style rules are strict: no purple prose, no
  flourishes, no aphorisms, no sentence that builds up and lands on a short punch. Banned: "chilling",
  "sinister", "shocking", "horrifying", "dark secret", "web of", "tip of the iceberg" (unless quoting a
  source), "haunting", "stark".
- Do not restate what the box already shows (the score, the number of cases). Do not open two countries
  with the same sentence shape.

## Facts — hard rules
- Use ONLY what is in that country's packet (patterns, role notes, pattern summaries, cases, flows) and
  its `previous_draft`. Add nothing from memory, not one date, not one name. If you need a fact to make
  the mechanism clear and it is not in the packet, rewrite around it.
- The general explanation of how a mechanism works (what a legal deadline is, why moving an abuser
  protects the institution) is yours to write in plain words — that is not a new fact and is wanted.
- Keep status words exact: "convicted", "charged", "accused", "acquitted", "found by an inquiry",
  "alleged by…", "disproved", "could not be confirmed". Never upgrade an allegation. Say plainly when a
  claim was investigated and found false.
- Numbers exactly as the packet gives them. Name individuals only as the packet does, with their status.
  Never name a victim or survivor.
- Where the country's role is a gap (no survey data, no national inquiry, few reports), the mechanism is
  the silence: explain who does the counting, why this country is missing from it, and what that does to
  the world totals. Invent no cases.
- Where the country appears only as a destination, a troop-sending country, or a receiving country for
  adoptions, write that side of it and explain the exchange.

## Output
Write a JSON object to the output path you are given:
{"ISO3": {"story": "<paragraphs separated by \n\n>", "mechanism": "<your one-sentence answer to 'what mechanism does this country show'>", "sources": ["<URLs from the packet you used>"]}, ...}
Every country in your input must appear. Save every ~5 countries. Validate with
python3 -c "import json;json.load(open(PATH))". No web access; the packet is all you have.

## Worked example — the difference
Packet facts: Manila's mayor closed the Ermita district in 1992; businesses moved to Angeles City;
Clark Air Base closed the same year; the 2025 US trafficking report still names Angeles City and others;
IJM found street and establishment cases fell 79–86% in target cities 2006–2016 while Philippine internet
addresses used for exploitation rose more than twelvefold 2014–2017.

Too thin (what the first version did): "In 1992 the mayor of Manila, Alfredo Lim, closed the Ermita
district, where the sex industry had been concentrated. Many of the businesses moved north to Angeles
City. The US Clark Air Base there had closed the same year. The 2025 trafficking report still names
Angeles City, Boracay, Olongapo, Puerto Galera and Surigao."

What is wanted: "Shutting a red-light district rarely ends the trade inside it. It moves it, because the
buyers and the people selling children to them are still there the next morning. In 1992 Manila's mayor,
Alfredo Lim, closed the Ermita district, where the city's sex industry had been concentrated. The
businesses reopened north of the city in Angeles City, a town that had grown up around the US Clark Air
Base and had just lost it — the base closed the same year — leaving bars with no customers and a new
clientele of foreign visitors. Thirty-three years later the US government's own trafficking report still
lists Angeles City among the places where children are sold, which is the clearest measure of what the
1992 closure achieved: it changed the address."
