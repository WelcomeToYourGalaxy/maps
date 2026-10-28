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


def main(rdir, arch_path):
    arch = load_archive(arch_path)
    seen, out, per = set(), [], {}
    RENAME = {'hizb_ut_tahrir': 'hizb_tahrir'}
    files = sorted(glob.glob(os.path.join(rdir, '*.json'))) + sorted(glob.glob(os.path.join(rdir, 'r2', '*_cases.json'))) + sorted(glob.glob(os.path.join(rdir, 'r3', '*_cases.json')))
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
