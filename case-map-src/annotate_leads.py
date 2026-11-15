#!/usr/bin/env python3
"""Annotate docs/leads_icij.json with round 31's outcomes.

Every round annotates the rows it worked so the queue count falls honestly and
the next round can see what has been tried. Earlier rounds wrote r17_outcome
through r22_outcome; this writes r31_outcome, r31_note and r31_case_id.

The lead file carries no P-numbers, so rows are matched back through
docs/leads_icij_pnumbers.json, which resolved them in this round, on the project
name and approval date together — the pair the resolver itself matched on.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEADS = '/home/claude/maps/case-map-src/docs/leads_icij.json'


def main():
    outcomes = json.load(open(os.path.join(HERE, 'r31f_icij7_outcomes.json')))
    merged = json.load(open(os.path.join(HERE, 'r31f_icij7.json')))
    resolved = json.load(open(os.path.join(HERE, 'resolved.json')))
    dry = '--dry-run' in sys.argv

    # pid -> (project, approved) from this round's own resolution
    by_pid = {}
    for r in resolved:
        if 'pid' in r:
            by_pid.setdefault(r['pid'], (r['project'], r['approved']))
            for s in r.get('sibling_pids', []):
                by_pid.setdefault(s, (r['project'], r['approved']))

    # build pid -> outcome
    res = {}
    for d in outcomes.get('dropped', []):
        if d.get('pid'):
            res[d['pid']] = ('dropped', d.get('reason') or '', None)
    for d in outcomes.get('already_on_map', []):
        if d.get('pid'):
            res[d['pid']] = ('already_on_map', d.get('note') or '', d.get('case_id'))
    for c in merged.get('cases', []):
        pid = None
        for l in c.get('lenders', []):
            import re
            m = re.search(r'\bP\d{6}\b', l.get('role') or '')
            if m:
                pid = m.group(); break
        if pid:
            res[pid] = ('case', c.get('title', ''), c['id'])
    for e in merged.get('extend', []):
        # an extend names the existing case, not a pid; recorded by case id only
        pass

    L = json.load(open(LEADS))
    leads = L['leads']
    idx = {}
    for i, row in enumerate(leads):
        idx[(row['project'], row['approved'])] = i

    applied, unmatched = 0, []
    for pid, (outcome, note, cid) in res.items():
        key = by_pid.get(pid)
        if not key or key not in idx:
            unmatched.append(pid); continue
        row = leads[idx[key]]
        row['r31_outcome'] = outcome
        if note:
            row['r31_note'] = note[:600]
        if cid:
            row['r31_case_id'] = cid
        applied += 1

    def worked(r):
        return any(k.endswith('_outcome') for k in r) or 'likely_already_on_map' in r
    conf = [r for r in leads if 'confirmed' in r['section'].lower()]
    still_open = sum(1 for r in conf if not worked(r))
    all_open = sum(1 for r in leads if not worked(r))

    L.setdefault('counts', {})
    L['counts']['r31_worked'] = applied
    L['counts']['open in the confirmed-displacement table'] = still_open
    L['counts']['open'] = all_open

    print(f"annotated {applied} rows; unmatched pids {unmatched}", file=sys.stderr)
    print(f"confirmed-displacement rows still open: {still_open}", file=sys.stderr)
    print(f"rows still open overall: {all_open}", file=sys.stderr)
    if dry:
        print("dry run; nothing written", file=sys.stderr)
        return
    json.dump(L, open(LEADS, 'w'), ensure_ascii=False, indent=1)
    print(f"written to {LEADS}", file=sys.stderr)


if __name__ == '__main__':
    main()
