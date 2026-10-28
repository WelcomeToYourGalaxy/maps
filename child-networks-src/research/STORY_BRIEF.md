# Brief: "Behind the scenes" stories, one per country

You are writing the "Behind the scenes" section of each country's box on a civic-education world map of child sexual abuse networks and child trafficking (website: Welcome to Your Galaxy). Readers are ordinary people with no background. The owner found the old section to be "lists of raw data" and wants organic writeups "like campfire ghost stories, explaining the patterns for novices".

## What to write
For each country in your input file, one story of about 150–350 words (shorter when the packet is thin, longer — up to ~450 — for countries with many patterns). It explains, as a story told in order, how the hidden patterns played out in that country: who did what, who knew, what was done instead of stopping it, how it came out, and what it connects to elsewhere. Then a closing paragraph of 2–3 sentences telling a novice what this means: what to notice, what to ask, why it matters.

## How it should read
- A story told aloud around a fire: start in a specific place and time ("In 1975, in a boys' orphanage in St John's, Newfoundland..."), move forward through events, let the reader see the mechanism through what people did. Use "you" sparingly if at all.
- Plain words. Short and medium sentences. Explain any term a novice wouldn't know in a few words (e.g. "a statute of limitations — the legal deadline to sue").
- The owner's style rules, strictly:
  - No purple prose, no rhetorical flourishes, no aphorisms or quotable one-liners, no sentences that build up and land on a short punch. No "chilling", "dark secret", "sinister", "web of", "tip of the iceberg" (unless quoting a source), "shocking", "horrifying".
  - Show, don't tell: give the case, the figure, the date, the mechanism instead of characterising it.
  - Every sentence must carry context; avoid words that gesture at a point without saying it.
- Paragraphs, not lists. No headings, no bullet points.

## Facts — hard rules
- Use ONLY facts in that country's packet (patterns, role notes, pattern summaries, cases, flows). Do not add anything from memory, not even well-known facts. If a detail isn't in the packet, leave it out.
- Keep status words exact: "convicted", "charged", "accused", "acquitted", "found by an inquiry", "alleged by…", "disproved". Never upgrade an allegation. If something is disproved or unproven, say so plainly.
- Do not name victims or survivors. Name individuals only as the packet does, with their status.
- Numbers: copy them exactly as the packet gives them.
- When the country's role is an estimate or a gap (e.g. "No survey data on online abuse in its region", "No national inquiry found"), the story is about the silence: what isn't counted and why that matters, using the packet's figures. Do not invent cases.
- Where the packet only shows the country as a destination, home country of troops, receiving country for adoptions, etc., tell that side of the story.

## Output
Write a JSON object to the output path given to you: {"ISO3": {"story": "<paragraphs separated by \n\n>", "sources": ["<the source URLs from the packet you relied on>"]}, ...}
Include every country in your input. Save every ~5 countries. Validate with python3 -c "import json;json.load(open(PATH))".
Do not use the web; everything you need is in the packet.
