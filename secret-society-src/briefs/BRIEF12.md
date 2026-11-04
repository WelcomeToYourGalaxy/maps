# Brief 12: bring writeups in line after the stricter case cut

The Infiltration Map just removed about 440 cases that were not directly infiltration. The test now: an outside party got its people, money or control INSIDE a government body, international body or company, and decisions or actions there served it (or it set out to make them). Cut were: mere membership of an office-holder in a lodge, club, church, alumni network or forum with nothing shown that the group steered through them; a banker or executive taking a post with no decision shown serving the former firm; open action from outside (public loan conditions, lobbying, donations, treaties, conquest); cases where infiltration was incidental; cases too vague to say who got inside what.

Each input item gives the current writeup text, the cases that REMAIN on the map (title, year, and a "why" line saying how each is infiltration), and the titles of the cases DROPPED for that country or pattern.

## Task
Edit each writeup so that:
- It no longer presents dropped material as infiltration. Remove or reframe sentences whose only support is a dropped case (e.g. "most of the cabinet belonged to X" when the X case was dropped as membership only). You may keep a dropped fact only as brief background if it is needed to understand a remaining case, and never call it infiltration.
- It still describes the pattern, using the remaining cases. Do not add new facts; use only the existing text and the remaining cases' titles and why lines.
- Keep the voice: plain, novice-friendly, pattern level not a list of cases (max two named cases per country, three per pattern), no purple prose, no punchline sentences, British spelling, paragraphs separated by "\n\n". Countries 120–300 words; patterns 200–380 words.
- Edit only what needs it; if the text is fine, return it unchanged.
- Country with no remaining cases: write a short plain estimate (100–160 words) from the Global Organized Crime Index material already in the text (or, if none, say plainly no documented case meets the map's test yet), and set "est": true.
- Pattern with fewer than 3 remaining cases, or whose premise rested on the dropped material: return {"retire": true, "reason": "..."}.

## Output
Same keys as input. Countries: {"<name>": {"d": "...", "est": bool}}. Patterns: {"<id>": {"summary": "...", "uncertain": "..."}} or {"retire": true, "reason": "..."}. Validate with python3 json.load. No web search. Reply with what you retired or marked est, and the names you changed substantially.
