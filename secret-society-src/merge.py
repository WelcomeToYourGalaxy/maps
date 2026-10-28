#!/usr/bin/env python3
"""Merge the regional research files into data/cases.json and link archive entries.

    python3 merge.py <research_dir> <archive_html>

Each research file is a JSON array of case records (see build.py for the schema).
Records are de-duplicated on (country, year, normalised title). Where a case matches an
entry in the Welcome to Your Galaxy conspiracy archive, the archive title and its trust
rating are attached as `arch`, so the popup can point to it.
"""
import json, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))

# case text pattern -> archive title pattern. Only explicit pairings; nothing fuzzy.
ARCH_LINKS = [
    (r'Calvi|Ambrosiano', r'Calvi Murder; Banco Ambrosiano Collapse; P2 Lodge Member Directed'),
    (r'\bP2\b|Gelli|Propaganda Due', r'Italian Parliamentary Commission CONFIRMED . P2 Lodge'),
    (r'Gladio', r'Italy . Operation Gladio: NATO Stay-Behind'),
    (r'Snow White', r'Operation Snow White'),
    (r'Broederbond', r'Broederbond'),
    (r'Skull and Bones', r'Skull and Bones . Systematic CIA'),
    (r'Trilateral', r'Trilateral Commission . 19/20'),
    (r'\bBCCI\b|Credit and Commerce', r'Bank of Credit and Commerce International'),
    (r'Nugan Hand', r'Nugan Hand'),
    (r'Condor', r'Operation Condor . CIA-Coordinated'),
    (r'Letelier', r'Orlando Letelier'),
    (r'Bohemian', r'Bohemian Grove . Elite Annual'),
    (r'Masonic.*(police|judiciary)|Freemason.*(police|judiciary|Home Affairs)', r'UK Investigation: Masonic Network in Police'),
    (r'Hugo Black', r'Supreme Court Justice Was Documented KKK'),
    (r'Morgan affair|Anti-Masonic', r'Anti-Masonic Party'),
    (r'Bilderberg', r'Bilderberg Group . Coordinated'),
    (r'Council on Foreign Relations', r'Council on Foreign Relations . Submergence'),
    (r'Vatican Bank|\bIOR\b|Marcinkus|Sindona', r'Vatican Bank Scandal: IOR'),
]


def load_archive(path):
    if not path or not os.path.exists(path):
        return []
    lines = open(path, encoding='utf-8').read().split('\n')
    out = []
    for l in lines:
        for pre in ('const RAW=', 'const RAW_CIVILIAN='):
            if l.startswith(pre):
                out += json.loads(l[len(pre):].rstrip().rstrip(';'))
    return out


def norm(t):
    return re.sub(r'[^a-z0-9]+', ' ', t.lower()).strip()[:40]


CAP_BK = {'enforce': 'security', 'elected': 'legis', 'cabinet': 'cabinet', 'exec': 'exec', 'court': 'court'}


def capture_cases(seen):
    """The drug-capture map's records: trafficking organisations inside governments, and the
    banks, shippers, brokers and other firms they used or penetrated. Its own data, imported
    as organised crime reaching into governments and companies."""
    p = os.path.join(HERE, 'data', 'capture_import.json')
    if not os.path.exists(p):
        return []
    cap = json.load(open(p))
    sec = {s['k']: s['label'] for s in cap.get('sectors', [])}
    # The drug map's text lost "$" plus the first digit in a few places (a shell ate "$1", "$2"...).
    # Amounts restored from the sources named; where a figure could not be checked it is removed.
    FIX = [('more than .4 billion in a civil suit', 'more than $2.4 billion in a civil suit'),
           ('20 years with  million in forfeiture', '20 years with $1 million in forfeiture'),
           ('admitted taking more than .5 million in bribes; prosecutors put the laundered total at between .5 and .5 million over fourteen years.', 'admitted taking more than $3.5 million in bribes.'),
           ('already found .2 billion in cash-for-gold deals', 'already found more than $5.2 billion in cash-for-gold deals'),
           ('dealings with the Suncity junket operator, whose Sydney turnover it put above A0 million a week; it sought A00 million. The company argued a penalty above A00 million would render it insolvent, having A8 million in cash against more than A.1 billion in debt, and was rescued by a A00 million investment.',
            'dealings with the Suncity junket operator, and sought a penalty of A$400 million. The company argued a penalty that size would render it insolvent, and it was rescued by a A$300 million investment.')]
    for x in cap['cases'] + cap['entities']:
        for a_, b_ in FIX:
            if a_ in x['d']: x['d'] = x['d'].replace(a_, b_)
    out = []
    for c in cap['cases']:
        key = (c['c'], str(c['y']), norm(c['n']))
        if key in seen: continue
        seen.add(key)
        r = {k: c[k] for k in ('n', 'c', 'lat', 'lng', 'y', 'status', 'rank', 'd', 'cite') if k in c}
        r['bk'] = CAP_BK.get(c['bk'], 'security'); r['org'] = ''; r['src'] = 'drug map'
        if c.get('undone'): r['undone'] = c['undone']
        if c.get('url'): r['url'] = c['url']
        out.append(r)
    for e in cap['entities']:
        key = (e['c'], str(e['y']), norm(e['n']))
        if key in seen: continue
        seen.add(key)
        r = {k: e[k] for k in ('n', 'c', 'lat', 'lng', 'y', 'status', 'd', 'cite') if k in e}
        r['rank'] = e['role'] + (' (' + sec[e['s']].lower() + ')' if e['s'] in sec else '')
        r['bk'] = 'company'; r['org'] = ''; r['src'] = 'drug map'
        if r['c'] in ('Macau', 'Hong Kong'):
            r['c0'] = r['c']; r['rank'] += ', ' + r['c']; r['c'] = 'China'
        if e.get('undone'): r['undone'] = e['undone']
        if e.get('url'): r['url'] = e['url']
        out.append(r)
    return out


FIELDS = ('inf', 'who', 'tgt', 'rel', 'int', 'wide', 'lik')


def apply_classes(out):
    """Who reached in, into what, whether it still matters, how sure, how severe, how wide.
    Round-4 records carry these themselves; earlier ones were classified from their text."""
    p = os.path.join(HERE, 'data', 'classify.json')
    cls = json.load(open(p)) if os.path.exists(p) else {}
    miss = 0
    for r in out:
        c = cls.get(r.pop('c0', r['c']) + '|' + r['n'])
        if c:
            for f in FIELDS:
                if f in c and f not in r: r[f] = c[f]
        if not all(f in r for f in FIELDS):
            miss += 1
        if r.get('tgt') == 'company': r['bk'] = 'company'
        elif r.get('tgt') == 'intl': r['bk'] = 'intl'
    print('records without a full classification:', miss)


def main(rdir, arch_path):
    arch = load_archive(arch_path)
    seen, out, per = set(), [], {}
    RENAME = {'hizb_ut_tahrir': 'hizb_tahrir', 'iurd': 'uckg', 'mouride': 'mourides', 'bodu_bala_sena': 'bbs', 'bain_co': 'bain'}
    files = sorted(glob.glob(os.path.join(rdir, '*.json'))) + sorted(glob.glob(os.path.join(rdir, 'r2', '*_cases.json'))) + sorted(glob.glob(os.path.join(rdir, 'r3', '*_cases.json'))) + sorted(glob.glob(os.path.join(rdir, 'r4', '*_cases.json')))
    for f in files:
        try:
            recs = json.load(open(f))
        except Exception as e:
            print('skip', f, e); continue
        if isinstance(recs, dict):
            continue
        per[os.path.basename(f)] = len(recs)
        for r in recs:
            if not all(k in r for k in ('n', 'c', 'lat', 'lng', 'y', 'bk', 'status', 'd')):
                print('  incomplete:', f, r.get('n')); continue
            key = (r['c'], str(r['y']), norm(r['n']))
            if key in seen:
                continue
            seen.add(key)
            if r['c'] == 'China' and 'Taiwan' in (r.get('org_note', '') + r.get('city', '') + r['n']):
                r['c'] = 'Taiwan'
            r['org'] = RENAME.get(r.get('org', ''), r.get('org', ''))
            r.setdefault('rank', '')
            r.setdefault('cite', '')
            if isinstance(r['y'], str):
                m = re.search(r'\d{4}', r['y']); r['y'] = int(m.group(0)) if m else 0
            if r.get('url') and not re.match(r'https?://', r['url']):
                r.pop('url')
            text = r['n'] + ' ' + r['d']
            best = None
            for cp, ap in ARCH_LINKS:
                if re.search(cp, text, re.I):
                    for a in arch:
                        if re.search(ap, a['conspiracy']):
                            if not best or a['trust'] > best['trust']:
                                best = a
                    if best:
                        break
            if best:
                r['arch'] = {'t': best['conspiracy'], 's': best['trust']}
            out.append(r)
    out += capture_cases(seen)
    apply_classes(out)
    OVERRIDE = {"Blackburn 'Victory' police lodge": {'status': 'reported'}}
    for r in out:
        for k, v in OVERRIDE.items():
            if r['n'].startswith(k): r.update(v)
    up = os.path.join(rdir, 'r2', 'gaps_urls.json')
    if os.path.exists(up):
        for u in json.load(open(up)):
            for r in out:
                if r['n'] == u.get('n') and r['c'] == u.get('c') and u.get('url'):
                    r['url'] = u['url']
                    if u.get('cite'): r['cite'] = u['cite']
    json.dump(out, open(os.path.join(HERE, 'data', 'cases.json'), 'w'), ensure_ascii=False, indent=1)
    print(per, '->', len(out), 'cases;', sum(1 for r in out if r.get('arch')), 'linked to the archive')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
