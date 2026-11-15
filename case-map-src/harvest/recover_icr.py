#!/usr/bin/env python3
"""Recover completion reports for projects where projectid returned none.

`wds?projectid=` returns only documents filed under that exact number, so a
report filed under a parent or a sibling is invisible. The handoff's routes 4
and 5 are the fix: check the parent and sibling numbers, and before accepting
that a report is undisclosed, try a qterm title search on the project name plus
"Implementation Completion Results".

Many of these rows are additional financings, so the parent is found by stripping
"Additional Financing" and its variants from the ICIJ project name and searching
the Bank's projects API for the remaining name in the same country.
"""
import json, os, re, subprocess, sys, time, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import harvest  # noqa: E402

AF = re.compile(r'\b(?:additional\s+financing|add(?:l|itional)?\.?\s*fin(?:ancing)?|'
                r'\bAF\b|supplemental|second\s+additional\s+financing)\b[:\-\s]*', re.I)


def curl_json(url, tries=4):
    for a in range(tries):
        r = subprocess.run(['curl', '-sS', '--max-time', '90', url],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip().startswith('{'):
            try:
                return json.loads(r.stdout)
            except json.JSONDecodeError:
                pass
        time.sleep(2 * (a + 1))
    return {}


def title_search(name):
    """qterm title search for a completion report."""
    q = urllib.parse.quote(f'{name} Implementation Completion Results Report')
    d = curl_json("https://search.worldbank.org/api/v3/wds?format=json&rows=25"
                  f"&qterm={q}&fl=docdt,display_title,pdfurl,txturl,docty,projn,projectid")
    out = []
    for k, v in (d.get('documents') or {}).items():
        if k == 'facets' or not isinstance(v, dict):
            continue
        dt = harvest.cdata(v.get('docty'))
        if 'Implementation Completion' not in dt and 'Performance Assessment' not in dt:
            continue
        out.append({'docty': dt, 'docdt': (harvest.cdata(v.get('docdt')) or '')[:10],
                    'title': harvest.cdata(v.get('display_title'))[:170],
                    'projectid': harvest.cdata(v.get('projectid')),
                    'id': v.get('id') or k.lstrip('D'),
                    'txturl': harvest.cdata(v.get('txturl')),
                    'pdfurl': harvest.cdata(v.get('pdfurl'))})
    return out


def parent_candidates(name, countries):
    base = AF.sub('', name).strip(' -:')
    if base.lower() == name.lower().strip(' -:'):
        return []
    q = urllib.parse.quote(base)
    d = curl_json(f"https://search.worldbank.org/api/v3/projects?format=json&rows=30&qterm={q}"
                  "&fl=id,project_name,boardapprovaldate,countryshortname")
    cands = []
    want = {c.lower() for c in countries}
    for pid, p in (d.get('projects') or {}).items():
        ctry = (p.get('countryshortname') or '').lower()
        if want and not any(w in ctry or ctry in w for w in want):
            continue
        cands.append({'pid': pid, 'name': p.get('project_name'),
                      'date': (p.get('boardapprovaldate') or '')[:10],
                      'country': p.get('countryshortname')})
    return cands[:8]


def main():
    M = json.load(open(os.path.join(HERE, 'harvest_manifest.json')))
    R = json.load(open(os.path.join(HERE, 'resolved.json')))
    OUT = {'ICR', 'ICRX', 'PPAR'}

    need = []
    for rec in R:
        if 'pid' not in rec:
            continue
        pids = [rec['pid']] + rec.get('sibling_pids', [])
        tags = set()
        for p in pids:
            for d in M.get(p, {}).get('docs', []):
                if d.get('route') in ('txt', 'pdf', 'cached'):
                    tags.add(d['tag'])
        if not (tags & OUT):
            need.append(rec)
    print(f"projects with no completion report or PPAR: {len(need)}", file=sys.stderr)

    report = []
    for n, rec in enumerate(need, 1):
        r = {'pid': rec['pid'], 'project': rec['project'],
             'countries': rec['countries'], 'approved': rec['approved'],
             'status': rec['status']}
        hits = title_search(rec['project'])
        r['title_search_hits'] = hits
        r['parent_candidates'] = parent_candidates(rec['project'], rec['countries'])

        # harvest any new project number the search or the parent lookup turned up
        extra = set()
        for h in hits:
            for m in re.finditer(r'\bP\d{6}\b', str(h.get('projectid') or '')):
                extra.add(m.group())
        for c in r['parent_candidates']:
            extra.add(c['pid'])
        extra.discard(rec['pid'])
        extra -= set(rec.get('sibling_pids', []))
        r['extra_pids'] = sorted(extra)
        got = {}
        for p in sorted(extra):
            h = harvest.harvest_pid(p)
            tags = sorted({d['tag'] for d in h.get('docs', [])
                           if d.get('route') in ('txt', 'pdf', 'cached')})
            if tags:
                got[p] = tags
                M[p] = h
        r['harvested'] = got
        r['recovered_outcome_doc'] = any(set(t) & OUT for t in got.values())
        report.append(r)
        if n % 5 == 0:
            print(f"  {n}/{len(need)}", file=sys.stderr)

    json.dump(M, open(os.path.join(HERE, 'harvest_manifest.json'), 'w'), indent=1)
    json.dump(report, open(os.path.join(HERE, 'icr_recovery.json'), 'w'), indent=1)
    rec_n = sum(1 for r in report if r['recovered_outcome_doc'])
    print(f"\nrecovered a completion report or PPAR for {rec_n} of {len(need)}", file=sys.stderr)
    for r in report:
        mark = 'OK ' if r['recovered_outcome_doc'] else '-- '
        print(f"  {mark}{r['pid']} {r['project'][:46]!r} "
              f"extra={r['extra_pids']} got={list(r['harvested'])}", file=sys.stderr)


if __name__ == '__main__':
    main()
