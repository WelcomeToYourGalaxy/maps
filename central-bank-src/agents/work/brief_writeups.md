# Plain-language writeups for a public map of central banks (second pass)

The map shows who owns and steers each central bank, the corruption around it and its reach. Each place and outside party has a box of technical lists. You write the readable paragraph at the top of the box, for a reader who knows nothing about finance. It should read like a person explaining: what this is, then what has happened with it, in order, connected. Not a recital of scores and lists.

Input: a JSON file mapping a key to the box's text. "p:" keys are places, "n:" keys are outside parties.

## Content
- Place: who issues its money and what its central bank is; who owns it, naming shareholders if the text lists them; the main cases, firings and pressure, each with how it ended; other notable ties. Mention scores only in passing, in words (for instance "scores 54 of 100, where 100 means fully exposed to outside influence").
- Party: what it is and where it is based; which central banks it is tied to and how; what is reported, with figures and dates; how each matter ended.
- Explain a term the first time it appears. Dates in words ("30 May 2021", never 2021-05-30). Currency names, not codes.

## Rules
- Only facts in the text. Every name, number, date and outcome must appear there. No facts from memory. Exception: a short clause on what a very well known organization is, if you are certain.
- Each case line starts "years · category · status." That status is the record's current standing and must be conveyed. If it says acquitted, case dismissed, charge withdrawn or investigation closed, say so, even if the line describes a sentence first. If it says charged, under investigation or alleged, say it is unproven. Where the text says a person denies it, say so. Never leave an outcome out when the text gives one (an investigation "closed without charges" must be reported as closed).
- A career move is not an accusation. A tie is not wrongdoing.
- Never mention the box, the excerpt, the record, or that text is missing. If no outcome is given, just stop at what happened.
- Plain, direct sentences. No adjectives doing the work, no flourish, no closing moral or punchline. No "our". One paragraph, no bullets.
- Length: 40 to 90 words for most parties. 80 to 150 for places. Up to 200 words only for the fullest (US, Italy, Lebanon, Nigeria and the like).

No web use. Read the input, then Write a JSON object mapping every key to its paragraph at the output path. Write each by hand, without a template. Report only the count written.

## This pass
Some keys are places that already had a paragraph on the map and have since gained new records; write the paragraph fresh from the box text you are given, covering the new material in its place in the story. The rest are parties new to the map.
