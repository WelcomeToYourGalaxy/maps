#!/usr/bin/env python3
"""Annotate docs/leads_icij.json with round 32's outcomes.

Earlier rounds wrote r17_outcome through r22_outcome and then r31_outcome; this
writes r32_outcome, r32_note and r32_case_id, so the queue count falls honestly
and the next round can see which rows have been tried.

Round 32's outcomes are in the six checked batch files themselves: each record
carries its own P-number, so no separate outcomes file is needed. Rows in the
lead file carry no P-number, so they are matched through
docs/leads_icij_pnumbers.json on project name and approval date together - the
pair the resolver matched on.
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEADS = '/home/claude/maps/case-map-src/docs/leads_icij.json'
PID = re.compile(r'\bP\d{6}\b')


def pid_of(rec, key):
    if rec.get('pid'):
        return str(rec['pid']).strip()
    for lender in rec.get('lenders', []) or []:
        m = PID.search(lender.get('role') or '')
        if m:
            return m.group()
    m = PID.search(key)
    return m.group() if m else None


def main():
    resolved = json.load(open(os.path.join(HERE, 'resolved.json')))
    dry = '--dry-run' in sys.argv

    by_pid = {}
    for r in resolved:
        if 'pid' in r:
            by_pid.setdefault(r['pid'], (r['project'], r['approved']))
            for s in r.get('sibling_pids', []):
                by_pid.setdefault(s, (r['project'], r['approved']))

    res = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'checked32', '*_checked.json'))):
        for key, rec in json.load(open(f)).items():
            if not isinstance(rec, dict):
                continue
            pid = pid_of(rec, key)
            if not pid:
                continue
            st = rec.get('status')
            if st == 'dropped':
                res[pid] = ('dropped', rec.get('drop_reason') or '', None)
            elif st == 'already_on_map':
                res[pid] = ('already_on_map', rec.get('note') or '', rec.get('case_id'))
            elif 'fields_add' in rec or st == 'extend':
                res[pid] = ('extend', rec.get('note') or '', rec.get('id'))
            else:
                res[pid] = ('case', rec.get('title') or '', rec.get('id') or key)

    L = json.load(open(LEADS))
    leads = L['leads']
    idx = {}
    for i, row in enumerate(leads):
        idx[(row['project'], row['approved'])] = i

    applied, unmatched = 0, []
    for pid, (outcome, note, cid) in res.items():
        key = by_pid.get(pid)
        if not key or key not in idx:
            unmatched.append(pid)
            continue
        row = leads[idx[key]]
        row['r32_outcome'] = outcome
        if note:
            row['r32_note'] = note[:600]
        if cid:
            row['r32_case_id'] = cid
        applied += 1

    def worked(r):
        return any(k.endswith('_outcome') for k in r) or 'likely_already_on_map' in r

    conf = [r for r in leads if 'confirmed' in r['section'].lower()]
    still_open = sum(1 for r in conf if not worked(r))
    all_open = sum(1 for r in leads if not worked(r))

    L.setdefault('counts', {})
    L['counts']['r32_worked'] = applied
    L['counts']['open in the confirmed-displacement table'] = still_open
    L['counts']['open in all tables'] = all_open

    print('round 32 outcomes found: %d' % len(res))
    print('rows annotated: %d' % applied)
    print('unmatched P-numbers: %d %s' % (len(unmatched), sorted(unmatched)[:12]))
    print('open in the confirmed-displacement table: %d' % still_open)
    print('open in all tables: %d' % all_open)
    if dry:
        print('dry run, nothing written')
        return
    tmp = LEADS + '.tmp'
    json.dump(L, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, LEADS)
    print('written')


if __name__ == '__main__':
    main()
