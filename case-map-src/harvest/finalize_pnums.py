#!/usr/bin/env python3
"""Purge HTTP-200-with-error-body cache entries, re-resolve, and finalise.

Three corrections over the first pass:

1. The projects API answers HTTP 200 with a JSON error body when its own
   backend search service times out ({"Debug":true,"error":"Error: connect
   ETIMEDOUT ...","RequestUrl":...}). The first pass cached one of those as a
   valid empty window and reported the lead as having no project in the Bank's
   records. Any cached file without a "projects" key is deleted and re-fetched.

2. ICIJ's approval date is not always the Bank's board approval date. It matched
   to within three days on 177 of 181 rows, but three rows are weeks or months
   out, all of them trust-fund or additional-financing operations. Those are
   pinned by name here.

3. Six rows match two P-numbers carrying an identical name AND an identical
   approval date. That is the Bank filing one operation under two numbers, and a
   completion report may sit under either, so both are carried rather than one
   being chosen.
"""
import json, os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'api_cache')

# Pinned by name through a qterm search; ICIJ's date is wrong for each.
PINNED = {
    'Regional Development Project|Mar. 20, 2012': 'P126033',
    'Mauritania Road Corridor ACGF|Jun. 15, 2010': 'P112131',
    'Community-led Infrastructure Development for the Urban Poor in Ulaanbaatar Phase 2|May. 3, 2011': 'P125863',
    'AF: ARTF-2nd Judicial Reform Project|Jun. 1, 2012': 'P118028',
}


def bad_cache(path):
    try:
        d = json.load(open(path))
    except Exception:
        return True
    return 'projects' not in d


def main():
    purged = []
    for fn in sorted(os.listdir(CACHE)):
        if not fn.startswith('win_'):
            continue
        p = os.path.join(CACHE, fn)
        if bad_cache(p):
            purged.append(fn)
            os.remove(p)
    print(f"purged {len(purged)} poisoned cache files: {purged}", file=sys.stderr)

    # re-run the resolver with the cache holes
    r = subprocess.run([sys.executable, '-I', os.path.join(HERE, 'resolve_pnums.py')],
                       capture_output=True, text=True)
    print(r.stderr.strip(), file=sys.stderr)

    R = json.load(open(os.path.join(HERE, 'resolved.json')))

    # verify no window is an error body any more
    still = [fn for fn in os.listdir(CACHE)
             if fn.startswith('win_') and bad_cache(os.path.join(CACHE, fn))]
    if still:
        print(f"WARNING still-bad cache: {still}", file=sys.stderr)

    for rec in R:
        key = f"{rec['project']}|{rec['approved']}"
        if key in PINNED:
            rec['pid'] = PINNED[key]
            rec['match_note'] = ("pinned by name through a qterm search; ICIJ's "
                                 "approval date differs from the Bank's board "
                                 "approval date for this operation")
            rec.pop('ambiguous', None)
        # Carry a sibling P-number where two records are the same operation.
        #
        # The test must include the country. A looser version of this, matching
        # on shared name tokens alone, paired Albania's Education Excellence and
        # Equity Project with The Gambia's Third Education Project on the single
        # word "education", and put Gambia's completion report, appraisal
        # document and three resettlement plans into Albania's brief. It did the
        # same to a Kenya row with a Central African Republic project and to a
        # Turkey row with a Belarus one. Every genuine pairing found in round 31
        # shares a country, so requiring it costs nothing.
        cands = rec.get('candidates') or []
        if len(cands) > 1 and 'pid' in rec:
            top = cands[0]
            tc = str(top.get('country') or '').strip().lower()
            sibs = [c['pid'] for c in cands[1:]
                    if c['date'] == top['date']
                    and str(c.get('country') or '').strip().lower() == tc
                    and c['name'].strip().lower()[:40] == top['name'].strip().lower()[:40]]
            if sibs:
                rec['sibling_pids'] = sibs
                rec['match_note'] = (rec.get('match_note', '') +
                    ' two P-numbers carry an identical name and approval date; '
                    'both are harvested because a completion report may be filed '
                    'under either').strip()
                rec.pop('ambiguous', None)

    got = [r for r in R if 'pid' in r]
    print(f"resolved {len(got)} of {len(R)}", file=sys.stderr)
    print(f"with siblings: {sum(1 for r in R if r.get('sibling_pids'))}", file=sys.stderr)
    print(f"still ambiguous: {[r['project'] for r in R if r.get('ambiguous')]}", file=sys.stderr)
    unres = [r['project'] for r in R if 'pid' not in r]
    print(f"still unresolved: {unres}", file=sys.stderr)

    # the harvest list: every distinct number to fetch
    pids = []
    for r in R:
        if 'pid' in r:
            pids.append(r['pid'])
            pids.extend(r.get('sibling_pids', []))
    pids = sorted(set(pids))
    print(f"distinct P-numbers to harvest: {len(pids)}", file=sys.stderr)
    json.dump(R, open(os.path.join(HERE, 'resolved.json'), 'w'), indent=1)
    json.dump(pids, open(os.path.join(HERE, 'harvest_pids.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
