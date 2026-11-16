#!/usr/bin/env python3
"""Match the map's own World Bank projects against ICIJ's 968 rows, from the map's side.

Round 33's forward match (lead row -> P-number -> case) found 244 of 968, but it
could only use the 181 rows a previous round had resolved, so it under-counts by
construction. This goes the other way: take every P-number the map carries, ask
the Bank what that project is called and when its board approved it, and look for
a lead row with the same approval date. Matching from the side with 322 items
instead of 968 removes the ambiguity the forward direction has.

The date is the identifier. ICIJ copied each row's approval date from the Bank's
own record, so an exact date match plus a country match is near-conclusive; the
name is used only to rank candidates that share a date.
"""
import json, os, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
API = 'https://search.worldbank.org/api/v3/projects'
CACHE = os.path.join(HERE, 'pcache')
# ICIJ prints every month as a three-letter abbreviation with a full stop:
# "Jun. 24, 2008". An earlier spelling of this map ('March', 'April', 'June',
# 'July', 'Sept') silently failed on five of the twelve and left 527 of 968 rows
# undated, which halved the match before it started.
MONTHS = {m: i + 1 for i, m in enumerate(
    ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])}
STOP = set('project the of and for a an in to development second third first phase '
           'program programme additional financing support improvement sector '
           'national rural urban emergency credit loan ii iii iv i'.split())


def tok(s):
    return {w for w in re.findall(r'[a-z]+', (s or '').lower()) if len(w) > 2 and w not in STOP}


def parse_icij_date(s):
    """ICIJ prints 'Jan. 19, 2006'. Return 'YYYY-MM-DD' or None."""
    m = re.match(r'([A-Za-z]+)\.?\s+(\d{1,2}),\s*(\d{4})', (s or '').strip())
    if not m:
        return None
    mon = MONTHS.get(m.group(1)[:3].lower())
    if not mon:
        return None
    return '%s-%02d-%02d' % (m.group(3), mon, int(m.group(2)))


def fetch(pids):
    """Fetch a batch of project records, cached one file per batch."""
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, pids[0] + '_%d.json' % len(pids))
    if os.path.exists(path):
        return json.load(open(path))
    url = ('%s?format=json&rows=%d&fl=id,project_name,boardapprovaldate,'
           'countryshortname,regionname&id=%s' % (API, len(pids) + 5, ','.join(pids)))
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                d = json.load(r)
            # never cache an error body served with status 200
            if 'projects' not in d:
                raise ValueError(str(d)[:200])
            tmp = path + '.tmp'
            json.dump(d, open(tmp, 'w'))
            os.replace(tmp, path)
            return d
        except Exception as e:
            if attempt == 3:
                print('  FAILED %s: %s' % (pids[0], e), file=sys.stderr)
                return {'projects': {}}
            time.sleep(3 * (attempt + 1))


def main():
    pid_to_cases = json.load(open(os.path.join(HERE, 'icij_pidmap.json')))
    leads = json.load(open('/home/claude/maps/case-map-src/docs/leads_icij.json'))['leads']

    by_date = {}
    for n, r in enumerate(leads):
        d = parse_icij_date(r.get('approved'))
        if d:
            by_date.setdefault(d, []).append(n)
    print('lead rows with a parsable approval date: %d of %d'
          % (sum(len(v) for v in by_date.values()), len(leads)))

    pids = sorted(pid_to_cases)
    recs = {}
    for i in range(0, len(pids), 40):
        batch = pids[i:i + 40]
        recs.update((fetch(batch) or {}).get('projects') or {})
        print('  fetched %d/%d' % (min(i + 40, len(pids)), len(pids)), file=sys.stderr)
    print('project records returned: %d of %d' % (len(recs), len(pids)))

    hits, nodate, nomatch = [], [], []
    for p in pids:
        rec = recs.get(p)
        if not rec:
            nomatch.append((p, 'no project record'))
            continue
        bad = (rec.get('boardapprovaldate') or '')[:10]
        if not bad:
            nodate.append(p)
            continue
        cands = by_date.get(bad) or []
        if not cands:
            nomatch.append((p, 'no lead row approved ' + bad))
            continue
        pname, pcountry = rec.get('project_name') or '', (rec.get('countryshortname') or '').lower()
        best, score = None, -1
        for n in cands:
            r = leads[n]
            sc = len(tok(pname) & tok(r.get('project')))
            if pcountry and any(pcountry == c.lower() for c in (r.get('countries') or [])):
                sc += 3
            if sc > score:
                best, score = n, sc
        hits.append({'pid': p, 'lead_index': best, 'score': score, 'date': bad,
                     'bank_name': pname, 'icij_name': leads[best].get('project'),
                     'section': leads[best]['section'],
                     'case_ids': pid_to_cases[p]})
    print()
    print('map P-numbers matched to an ICIJ row by exact approval date: %d' % len(hits))
    print('   of those, country or name agrees (score > 0): %d'
          % sum(1 for h in hits if h['score'] > 0))
    print('   date-only, name and country both disagree: %d'
          % sum(1 for h in hits if h['score'] <= 0))
    print('map P-numbers with no ICIJ row on that date: %d' % len(nomatch))
    print('map P-numbers whose record carries no approval date: %d' % len(nodate))
    json.dump({'hits': hits, 'nomatch': nomatch, 'nodate': nodate},
              open(os.path.join(HERE, 'icij_reverse.json'), 'w'), ensure_ascii=False, indent=1)
    print('\nwritten icij_reverse.json')


if __name__ == '__main__':
    main()
