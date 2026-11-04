# Brief 7: update country writeups after new cases were added

Read secret-society-src/briefs/BRIEF2.md fully (voice, the CORRECTION section on writing at the level of the pattern, at most two named cases, merged section, no fabrication) and secret-society-src/briefs/REVIEW.md (what is not infiltration).

Each input item has the country's "current_text" (already in the right style) and its full list of "cases", with "new": true on cases just added. Revise the writeup so the overall picture reflects the new cases too — e.g. if new cases show a decades-long pattern of foreign intelligence penetration, or cartel capture of a ministry, the writeup should now describe that pattern. Keep what is good; do not turn it into a list of the new cases; still at most two named cases, 150–300 words, 2–4 paragraphs separated by "\n\n", the part about what it means for people woven in. Historical material only where its effect is still felt or it explains today's pattern. If a country had "est": true but now has documented cases, set "est": false and write from the record.

Output JSON {"<country>": {"d": "...", "est": bool}} for every input country to the path given; validate with python3 json.load. Use your own scratch folder. Reply with the count and the shortest sample.
