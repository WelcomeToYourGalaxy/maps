#!/usr/bin/env python3
"""Resolve open ICIJ confirmed-displacement rows to World Bank P-numbers.

The lead file carries ICIJ's project name, approval date and country but no
P-number. The Bank's projects API filters on board approval date, which the
handoff records as the decisive matching field, so the route is: query a narrow
date window with no country filter (regional projects are not returned under a
member country's code), then score candidates on country and name.

Writes resolved.json with one record per row: the chosen P-number, the score,
and every other candidate in the window so an ambiguous match can be read.
"""
import json, os, re, sys, time, urllib.parse, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
LEADS = os.path.join(HERE, '..', 'maps', 'case-map-src', 'docs', 'leads_icij.json')
CACHE = os.path.join(HERE, 'api_cache')
os.makedirs(CACHE, exist_ok=True)

STOP = set('''project the of and for a an in on to development second third first
phase additional financing program programme sector support improvement
improvements ii iii iv v'''.split())


def norm_tokens(s):
    s = s.replace('&amp;', '&').lower()
    toks = re.findall(r"[a-z0-9]+", s)
    return [t for t in toks if t not in STOP and len(t) > 2]


def parse_date(s):
    # ICIJ prints e.g. "Jan. 19, 2006"
    s = s.strip().replace('.', '')
    for fmt in ('%b %d, %Y', '%B %d, %Y'):
        try:
            import datetime
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def fetch_window(d0, d1):
    key = f"win_{d0}_{d1}.json"
    path = os.path.join(CACHE, key)
    if os.path.exists(path) and os.path.getsize(path) > 50:
        return json.load(open(path))
    url = ("https://search.worldbank.org/api/v3/projects?format=json&rows=300"
           "&fl=id,project_name,boardapprovaldate,countryshortname,regionname,"
           "projectstatusdisplay,lendprojectcost,totalamt"
           f"&strdate={d0}T00:00:00Z&enddate={d1}T00:00:00Z")
    for attempt in range(4):
        r = subprocess.run(['curl', '-sS', '--max-time', '90', url],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip().startswith('{'):
            try:
                d = json.loads(r.stdout)
            except json.JSONDecodeError:
                time.sleep(3 * (attempt + 1)); continue
            json.dump(d, open(path, 'w'))
            return d
        time.sleep(3 * (attempt + 1))
    return {'projects': {}, '_failed': True}


def main():
    L = json.load(open(LEADS))
    leads = L['leads']

    def worked(r):
        return any(k.endswith('_outcome') for k in r) or 'likely_already_on_map' in r

    rows = [r for r in leads
            if 'confirmed' in r['section'].lower() and not worked(r)]
    print(f"open confirmed rows: {len(rows)}", file=sys.stderr)

    out = []
    import datetime
    for n, r in enumerate(rows, 1):
        d = parse_date(r['approved'])
        rec = {'project': r['project'], 'approved': r['approved'],
               'iso3': r['iso3'], 'countries': r['countries'],
               'displaced': r['displaced'], 'cost': r['cost'],
               'status': r['status'], 'complaint': r.get('complaint')}
        if d is None:
            rec['error'] = 'unparsed approval date'
            out.append(rec); continue
        d0 = (d - datetime.timedelta(days=3)).isoformat()
        d1 = (d + datetime.timedelta(days=3)).isoformat()
        data = fetch_window(d0, d1)
        projs = data.get('projects', {}) or {}
        want_name = set(norm_tokens(r['project']))
        want_ctry = set(c.lower() for c in r['countries'])
        cands = []
        for pid, p in projs.items():
            pname = p.get('project_name') or ''
            got = set(norm_tokens(pname))
            inter = want_name & got
            overlap = len(inter) / max(1, len(want_name))
            ctry = (p.get('countryshortname') or '').lower()
            cmatch = any(c in ctry or ctry in c for c in want_ctry) if want_ctry else False
            bad = (p.get('boardapprovaldate') or '')[:10]
            exact_date = bad == d.isoformat()
            score = overlap * 100 + (25 if cmatch else 0) + (10 if exact_date else 0)
            cands.append({'pid': pid, 'name': pname, 'date': bad,
                          'country': p.get('countryshortname'),
                          'region': p.get('regionname'),
                          'cost': p.get('lendprojectcost'),
                          'overlap': round(overlap, 2), 'ctry': cmatch,
                          'score': round(score, 1), 'shared': sorted(inter)})
        cands.sort(key=lambda c: -c['score'])
        rec['window'] = [d0, d1]
        rec['n_in_window'] = len(cands)
        rec['candidates'] = cands[:6]
        if cands and cands[0]['score'] >= 55:
            rec['pid'] = cands[0]['pid']
            rec['match_score'] = cands[0]['score']
            rec['match_name'] = cands[0]['name']
            # flag a close runner-up
            if len(cands) > 1 and cands[1]['score'] >= cands[0]['score'] - 15:
                rec['ambiguous'] = True
        out.append(rec)
        if n % 20 == 0:
            print(f"  {n}/{len(rows)}", file=sys.stderr)

    json.dump(out, open(os.path.join(HERE, 'resolved.json'), 'w'), indent=1)
    got = sum(1 for r in out if 'pid' in r)
    amb = sum(1 for r in out if r.get('ambiguous'))
    print(f"resolved {got} of {len(out)}; {amb} flagged ambiguous", file=sys.stderr)


if __name__ == '__main__':
    main()
