"""Fact-check patches (research/verify_*.json) applied to raw research records.
A verified non-encyclopedia source replaces the encyclopedia link, which is kept as the second link;
'fixes' overwrite fields with corrected values."""
import glob, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
KEYMAP = {'st': 'status', 'v': 'victims', 'fr': 'first_report', 'iso': 'iso3'}


def load():
    out = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'research', 'verify_[A-Z].json'))):
        for pt in json.load(open(f)): out[pt['id']] = pt
    return out


def apply(c, patches):
    pt = patches.get(c.get('id'))
    if not pt: return c
    if pt.get('verified') and pt.get('url') and 'wikipedia.org' not in pt['url']:
        if c.get('url') and c['url'] != pt['url'] and not c.get('url2'): c['url2'] = c['url']
        c['url'] = pt['url']
        if pt.get('cite'): c['cite'] = pt['cite']
    for k, v in (pt.get('fixes') or {}).items():
        c[KEYMAP.get(k, k)] = v
    return c
