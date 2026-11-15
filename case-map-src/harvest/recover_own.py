#!/usr/bin/env python3
"""Harvest outcome documents the projectid query missed but a title search found.

Two different things came out of the title search and they must not be confused:

* Documents whose own `projectid` field is the lead's own P-number. `wds?projectid=`
  did not return them, the title search did. Uruguay P057481 is the example: its
  Evaluation Group review of 1 May 2014 is filed under its own number and the
  projectid query returned nothing. These are harvested straight onto the lead,
  no judgement required. Add it to the list of reasons a report that looks
  undisclosed is not.

* Candidate parents. The mechanical token test is not safe for these. It matched
  Benin's Transport Infrastructure Rehabilitation and Maintenance Project to
  Uruguay's Transport Infrastructure Maintenance and Rural Access on the words
  "transport" and "maintenance". A country check kills that one, but the class of
  error stands, so parents are recorded in the brief as candidates to verify and
  are never attached as though they were the project's own documents.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import harvest  # noqa: E402

STOP = set('''project the of and for a an in on to development second third first
phase additional financing program programme sector support improvement
improvements ii iii iv v af add addl supplemental'''.split())


def toks(s):
    s = (s or '').replace('&amp;', '&').lower()
    return set(t for t in re.findall(r'[a-z0-9]+', s) if t not in STOP and len(t) > 3)


def main():
    REC = json.load(open(os.path.join(HERE, 'icr_recovery.json')))
    M = json.load(open(os.path.join(HERE, 'harvest_manifest.json')))
    R = json.load(open(os.path.join(HERE, 'resolved.json')))
    by_pid = {r['pid']: r for r in R if 'pid' in r}

    own_recovered, parent_flags = {}, {}
    for r in REC:
        pid = r['pid']
        lead_toks = toks(r['project'])
        lead_ctry = {c.lower() for c in r['countries']}

        # 1. documents filed under the lead's own number
        own = [h for h in r.get('title_search_hits', [])
               if pid in re.findall(r'\bP\d{6}\b', str(h.get('projectid') or ''))]
        got = []
        for h in own:
            tag = 'PPAR' if 'Performance Assessment' in h['docty'] else (
                'ICRR' if 'Report Review' in h['docty'] else 'ICR')
            kind, path, size = harvest.fetch_doc(pid, tag, h['docdt'], h['id'],
                                                 h.get('txturl'), h.get('pdfurl'))
            if kind in ('txt', 'pdf', 'cached'):
                entry = {'tag': tag, 'docty': h['docty'], 'docdt': h['docdt'],
                         'title': h['title'], 'id': h['id'], 'route': kind,
                         'path': os.path.relpath(path, HERE), 'bytes': size,
                         'found_by': 'qterm title search; wds?projectid= missed it'}
                M.setdefault(pid, {'pid': pid, 'docs': []})
                if not any(d.get('id') == h['id'] for d in M[pid]['docs']):
                    M[pid]['docs'].append(entry)
                got.append(entry)
        if got:
            own_recovered[pid] = [f"{g['tag']} {g['docdt']}" for g in got]

        # 2. candidate parents, country-checked, recorded not attached
        cands = []
        seen = set()
        for h in r.get('title_search_hits', []):
            for p in re.findall(r'\bP\d{6}\b', str(h.get('projectid') or '')):
                if p == pid or p in seen:
                    continue
                shared = lead_toks & toks(h.get('title'))
                title_ctry = (h.get('title') or '').split(' - ')[0].strip().lower()
                ctry_ok = any(c in title_ctry or title_ctry in c for c in lead_ctry) if lead_ctry else False
                if len(shared) >= 2 and ctry_ok:
                    seen.add(p)
                    cands.append({'pid': p, 'title': h['title'][:150],
                                  'docty': h['docty'], 'docdt': h['docdt'],
                                  'shared_words': sorted(shared)})
        for c in r.get('parent_candidates', []):
            if c['pid'] in seen or c['pid'] == pid:
                continue
            shared = lead_toks & toks(c.get('name'))
            ctry = (c.get('country') or '').lower()
            if len(shared) >= 2 and any(x in ctry or ctry in x for x in lead_ctry):
                seen.add(c['pid'])
                cands.append({'pid': c['pid'], 'title': c.get('name'),
                              'docty': 'project record', 'docdt': c.get('date'),
                              'shared_words': sorted(shared)})
        if cands:
            parent_flags[pid] = cands

    json.dump(M, open(os.path.join(HERE, 'harvest_manifest.json'), 'w'), indent=1)
    json.dump({'own_recovered': own_recovered, 'parent_candidates': parent_flags},
              open(os.path.join(HERE, 'icr_notes.json'), 'w'), indent=1)

    print(f"outcome documents recovered under the lead's OWN number: "
          f"{len(own_recovered)} leads", file=sys.stderr)
    for p, v in own_recovered.items():
        print(f"  {p} {by_pid[p]['project'][:46]!r} -> {v}", file=sys.stderr)
    print(f"\nleads with a country-checked parent candidate to VERIFY: "
          f"{len(parent_flags)}", file=sys.stderr)
    for p, v in parent_flags.items():
        print(f"  {p} {by_pid[p]['project'][:42]!r}", file=sys.stderr)
        for c in v:
            print(f"      {c['pid']} {str(c['title'])[:80]!r} shared={c['shared_words']}",
                  file=sys.stderr)


if __name__ == '__main__':
    main()
