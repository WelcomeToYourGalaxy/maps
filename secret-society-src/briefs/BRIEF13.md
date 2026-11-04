# Brief 13: tidy organisation descriptions after the stricter case cut

The Infiltration Map removed cases that were not directly infiltration (membership only, a post with no decision shown serving the outside party, open action from outside, incidental or too vague). Each item in the input is an organisation still on the map: its name, its current description "d", the cases that REMAIN linked to it (title, year, country, and a "why" line), and the titles of its cases that were DROPPED.

Rewrite "d" so it no longer presents dropped material as infiltration and is carried by the remaining cases. 50–110 words, plain and novice-friendly, British spelling, no purple prose or punchlines. First sentence: what it is and how it gets inside institutions (whom it places, pays or controls, and where). Then the key evidence from the remaining cases. Use only facts in the existing text and the remaining cases' titles and why lines; add nothing new. If the text is already fine, return it unchanged. Also return "reach": the sorted list of countries of the remaining cases.

Output JSON {"<key>": {"d": "...", "reach": [...]}} for every input key to the output path given; validate with python3 json.load. No web search. Reply with the count changed and two samples.
