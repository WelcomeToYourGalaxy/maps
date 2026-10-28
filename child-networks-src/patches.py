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
    if isinstance(c.get('d'), str):
        c['d'] = c['d'].replace('The record also cites', 'Earlier sources not re-checked for this map also cite').replace('is cited by the record for', 'is cited, though it could not be opened for this map, for').replace('The record also cite ', 'Earlier sources not re-checked for this map also cite ').replace('(not re-confirmed in this pass)', '(not re-checked for this map)')
    return c


def dropped():
    """Case ids classified as one-time incidents not connected to a larger pattern (research/classify_out_*.json)."""
    out = set()
    for f in sorted(glob.glob(os.path.join(HERE, 'research', 'classify_out_*.json'))):
        for r in json.load(open(f)):
            if r.get('decision') == 'drop': out.add(r['id'])
    return out
