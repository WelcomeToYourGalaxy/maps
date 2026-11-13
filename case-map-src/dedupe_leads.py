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

CASE_TEXT = [(c['id'], ' '.join(strings(c))) for c in CASES]
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
    hits = [cid for cid, t in CASE_TEXT if n in t]
    ehits = [eid for eid, t in ENT_TEXT if n in t]
    raw = s.count(n)
    if hits:
        print(f'{n}  ON THE MAP: {", ".join(hits)}')
    else:
        new.append(n)
        extra = f'   (appears {raw}x in the file, all of it lead data)' if raw else ''
        print(f'{n}  not on the map{extra}')
    if ehits:
        print(f'      also named on entity records: {", ".join(ehits)}')

print(f'\n{len(new)} of {len(dict.fromkeys(nums))} are new: {" ".join(new)}')
print('\nA P-number missing here is not proof a project is absent: a case may carry the')
print('project under a name only, with no number. Confirm by place and years before')
print('writing a new case, and when you write one, put the P-number in its lender role.')
