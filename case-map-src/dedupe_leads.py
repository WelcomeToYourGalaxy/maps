r"""python3 dedupe_leads.py P128276 P083929 ...   -- or --   python3 dedupe_leads.py --file nums.txt

Checks whether a World Bank P-number is already on the map.

WHY THIS SCRIPT EXISTS. The obvious recipe is wrong:

    grep -o 'P[0-9]\{6\}' base.html        # DO NOT USE THIS

base.html embeds ICIJ's own per-country lead tables (the "dl" and "dpy" arrays used by
the country panels), and every ICIJ project P-number is in there as LEAD data. So a grep
over the whole file matches almost any lead you are about to research and reports it as
already on the map. In ICIJ tranche 3, that recipe matched 35 of 36 leads; the true
number already on the map was 1. Three researchers hit it independently in one round.

This script parses window.CASES and searches only inside case objects, which is the only
place a P-number means "this project is already a case". It also searches window.ENT, so
a number recorded on a company or person is reported separately rather than missed.

ONE MORE FALSE MATCH, found in tranche 4. The Bank's document archive builds URLs whose
path segments carry a DIFFERENT project's number: the P081348 completion report sits under
a path containing P081340, and the P086446 appraisal under one containing P086101. A case's
sources therefore hold P-numbers that are nothing to do with it. So a hit inside a source
URL alone is reported separately as a probable false match, and only a hit in the card's
own text -- the lender roles above all -- is reported as ON THE MAP.
"""
import json, re, sys, os

f = os.path.dirname(os.path.abspath(__file__)) + '/base.html'
s = open(f).read()
d = json.JSONDecoder()

i = s.index('window.CASES = ') + 15
CASES, _ = d.raw_decode(s[i:])
j = s.index('window.ENT = ') + 13
ENT, _ = d.raw_decode(s[j:])

def strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o, list):
        for v in o: yield from strings(v)

def split_text(c):
    """Card text and source-URL text, kept apart: an archive URL can carry another
    project's number in a path segment."""
    urls = ' '.join(x.get('url') or '' for x in (c.get('sources') or []) if isinstance(x, dict))
    body = dict(c)
    body['sources'] = [{k: v for k, v in (x.items() if isinstance(x, dict) else [])
                        if k != 'url'} for x in (c.get('sources') or [])]
    return ' '.join(strings(body)), urls

CASE_TEXT = [(c['id'],) + split_text(c) for c in CASES]
ENT_TEXT = []
for group, items in ENT.items():
    if not isinstance(items, list): continue
    for x in items:
        if isinstance(x, dict):
            ENT_TEXT.append((f"{group}:{x.get('id') or x.get('name')}", ' '.join(strings(x))))

args = sys.argv[1:]
if args and args[0] == '--file':
    nums = re.findall(r'P\d{6}', open(args[1]).read())
else:
    nums = [a.upper() for a in args if re.fullmatch(r'[Pp]\d{6}', a)]
if not nums:
    print(__doc__); sys.exit(1)

print(f'{len(CASES)} cases, {len(ENT_TEXT)} entity records\n')
new = []
for n in dict.fromkeys(nums):
    hits = [cid for cid, t, u in CASE_TEXT if n in t]
    urlonly = [cid for cid, t, u in CASE_TEXT if n not in t and n in u]
    ehits = [eid for eid, t in ENT_TEXT if n in t]
    raw = s.count(n)
    if hits:
        print(f'{n}  ON THE MAP: {", ".join(hits)}')
    else:
        new.append(n)
        extra = f'   (appears {raw}x in the file, all of it lead data)' if raw else ''
        print(f'{n}  not on the map{extra}')
    if urlonly:
        print(f'      appears only inside a source URL on: {", ".join(urlonly)}')
        print(f'      -- probably an archive path segment, not this project. Open the card to be sure.')
    if ehits:
        print(f'      also named on entity records: {", ".join(ehits)}')

print(f'\n{len(new)} of {len(dict.fromkeys(nums))} are new: {" ".join(new)}')
print('\nA P-number missing here is not proof a project is absent: a case may carry the')
print('project under a name only, with no number. Confirm by place and years before')
print('writing a new case, and when you write one, put the P-number in its lender role.')
