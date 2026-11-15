#!/usr/bin/env python3
"""Merge a round's agent output into the map's data files, refusing bad records.

Agents write one file each under agents/work/r<NN>/. This script reads those
files, validates every record, drops the ones already on the map, and appends
what survives. Run it with --dry first, always.

    python3 merge_links.py --dry agents/work/r53/*.json
    python3 merge_links.py       agents/work/r53/*.json

Each input file is a JSON object with a "records" list (a "notes" string is
read and ignored). A record's type is taken from its own fields:

    relation + entity + cb_iso3      -> a tie, into networks.json
    kind + date + summary            -> an event, into events_gold.json
    move + people                    -> a revolving-door record, into corruption.json
    category + status + people       -> a corruption case, into corruption.json

WHY EACH CHECK IS HERE. Every one of them exists because a record got through
without it and cost a round, or would have put something false on the map:

  vocabulary        a relation or entity_type outside the vocabulary renders as
                    raw text in the popup sentence, and a new relation also needs
                    a SAY entry in app.js, so it must be a deliberate decision
                    rather than an agent's phrasing
  union keys        a record keyed to ECB, BCEAO, BEAC or ECCB expands to every
                    member country, so a mistaken union key puts one false record
                    in eight to twenty boxes at once
  event kind        app.js counts an event only if its kind is not "other", so a
                    real episode filed as "other" shows in the box and is counted
                    nowhere -- it silently vanishes from the layer and the score
  case status       build_final.py refuses to build on a status that is on
                    neither the counted nor the not-counted list
  source_url        every record needs a readable source that states the fact;
                    a 404 or a dead host means nobody can check it
  detail length     each tie renders as a standalone sentence in a popup box, so
                    a detail too short to stand alone leaves the reader a stub
  own vault         "holds its gold reserves in custody" where the custodian is
                    the bank itself must name the place that holds it, or the
                    popup reads "X holds its gold reserves in custody" of itself
  duplicates        an agent re-finding a record already on the map is the normal
                    case, not an error; these are dropped quietly and counted
  same person       one source often documents two moves by one person, and
                    audit_data.py treats (iso3, source_url, people[:40]) as a
                    duplicate key, so those are collapsed on the way IN rather
                    than repaired afterwards

Node names are compared with accents, case, punctuation and filler words folded,
because the map once carried one party under five spellings, each drawing its own
diamond.
"""
import json, os, re, sys, unicodedata, subprocess
from collections import defaultdict

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
L = lambda n: json.load(open(os.path.join(A, n)))
W = lambda n, d: json.dump(d, open(os.path.join(A, n), 'w'), indent=1, ensure_ascii=False)

RELATIONS = {'audits its accounts', 'bribery or misconduct with the bank',
             'holds its gold reserves in custody', 'makes its banknote paper',
             'manages its reserves or programmes', 'member of the same forum', 'other',
             'prints its banknotes', 'prints some of its banknotes', 'sits on the board',
             'supplies its banknote substrate'}
ENTITY_TYPES = {'bank', 'central bank', 'central bank subsidiary', "central bank's own vault",
                "central bank's own works", 'firm', 'forum', 'international body', 'person',
                'state body', 'state mint', 'state printing works', 'state works'}
UKEYS = {'ECB', 'EMU', 'BCEAO', 'BEAC', 'ECCB'}
CC_COUNTED = {'official finding', 'charged', 'under investigation', 'convicted',
              'convicted (final)', 'convicted in absentia', 'resigned', 'fined or settled',
              'alleged', 'outcome not found', 'died; outcome not found',
              'tried (verdict not found)', 'Sejm vote pending'}
CC_NOT_COUNTED = {'acquitted', 'case dismissed', 'charge withdrawn', 'investigation closed',
                  'conviction annulled (time-barred)'}
FILLER = {'the', 'of', 'and', 'bank', 'banknote', 'printing', 'works', 'ltd', 'limited',
          'plc', 'sa', 'ag', 'nv', 'inc', 'llc', 'gmbh', 'co', 'company', 'group',
          'holding', 'holdings', 'doo', 'srl', 'spa', 'as', 'ab', 'oy', 'kk', 'pte'}
PLACE_WORDS = re.compile(r'vault|head office|headquarters|branch|depositor|domestic|'
                         r'mint|treasury|,', re.I)
MIN_DETAIL = 90


def fold(s):
    """Compare node names with accents, case, punctuation and filler folded."""
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()
    return ' '.join(sorted(w for w in re.findall(r'[a-z0-9]+', s) if w not in FILLER))


_url_cache = {}


def url_ok(u, waived):
    if not u:
        return False, 'no source_url', False
    if u in waived:
        return True, '', False
    if u in _url_cache:
        return _url_cache[u]
    try:
        r = subprocess.run(['curl', '-sSL', '--max-time', '25', '-o', '/dev/null',
                            '-w', '%{http_code}', u], capture_output=True, text=True, timeout=40)
        code = (r.stdout or '').strip()[-3:]
        # an unreachable host gives curl code 000 with a non-zero exit, which is not a
        # success -- require a real 2xx or 3xx.
        # 401, 403 and 429 are different in kind: the page is there and the host is
        # refusing an automated request. Several of this map's sources do that (acp.cd,
        # cbe.org.eg, the Cloudflare-fronted banks), and they read fine through WebFetch.
        # Those are reported for a hand check rather than called dead, because treating a
        # bot block as a 404 would throw away good records.
        if code in ('', '000'):
            res = (False, 'source_url host could not be reached', False)
        elif code in ('401', '403', '429'):
            res = (False, f'source_url returned {code}: the host refuses automated requests. '
                          f'Open it with WebFetch or a browser; if the page states the fact, '
                          f're-run with --url-ok ' + u, True)
        elif code.isdigit() and 200 <= int(code) < 400:
            res = (True, '', False)
        else:
            res = (False, f'source_url returned {code}', False)
    except Exception as e:
        res = (False, f'source_url could not be fetched ({type(e).__name__})')
    _url_cache[u] = res
    return res


def kind_of(r):
    if r.get('relation') and r.get('entity'):
        return 'tie'
    if r.get('kind') and r.get('summary') and 'move' not in r:
        return 'event'
    if r.get('move'):
        return 'rd'
    if r.get('category') and r.get('status'):
        return 'case'
    return None


def main():
    argv = sys.argv[1:]
    waived = set()
    args = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--url-ok':
            waived.add(argv[i + 1]); i += 2; continue
        if a.startswith('--url-ok='):
            waived.add(a.split('=', 1)[1]); i += 1; continue
        if not a.startswith('--'):
            args.append(a)
        i += 1
    dry = '--dry' in argv
    if not args:
        sys.exit(__doc__)

    cor, evg, nets = L('corruption.json'), L('events_gold.json'), L('networks.json')
    places = set(json.load(open(os.path.join(A, '..', 'out', 'core.json')))['E'])

    have_tie = {(fold(l['entity']), l.get('cb_iso3'), l.get('relation')) for l in nets['links']}
    have_case = {(c.get('iso3'), (c.get('source_url') or ''), (c.get('people') or '')[:40])
                 for c in cor['cases']}
    have_rd = {(c.get('iso3'), (c.get('source_url') or ''), (c.get('people') or '')[:40])
               for c in cor['revolving_door']}
    have_ev = {(e.get('iso3'), (e.get('source_url') or '')) for e in evg['events']}

    filed = {'tie': [], 'event': [], 'rd': [], 'case': []}
    refused, dropped, handcheck_list = [], [], []

    # read every file first, so same-person collapsing can run across files
    incoming = []
    for f in args:
        try:
            d = json.load(open(f))
        except Exception as e:
            refused.append((f, '-', f'file would not parse: {e}'))
            continue
        for r in (d.get('records') or []):
            incoming.append((os.path.basename(f), r))

    # collapse same person, same source, same country BEFORE validating
    groups = defaultdict(list)
    singles = []
    for src, r in incoming:
        if kind_of(r) == 'rd':
            groups[(r.get('iso3'), r.get('source_url'), (r.get('people') or '')[:40])].append((src, r))
        else:
            singles.append((src, r))
    collapsed = 0
    for k, rows in groups.items():
        if len(rows) == 1:
            singles.append(rows[0])
            continue
        src, base = rows[0][0], dict(rows[0][1])
        base['move'] = ' ; '.join(dict.fromkeys(x[1].get('move', '') for x in rows if x[1].get('move')))
        base['summary'] = ' '.join(dict.fromkeys(x[1].get('summary', '') for x in rows if x[1].get('summary')))
        base['years'] = ' / '.join(dict.fromkeys(x[1].get('years', '') for x in rows if x[1].get('years')))
        singles.append((src, base))
        collapsed += len(rows) - 1

    for src, r in singles:
        k = kind_of(r)
        label = f"{r.get('iso3') or r.get('cb_iso3') or '?'} {(r.get('entity') or r.get('people') or (r.get('summary') or '')[:40])[:46]}"
        if k is None:
            refused.append((src, label, 'could not tell what kind of record this is'))
            continue
        iso = r.get('cb_iso3') if k == 'tie' else r.get('iso3')
        if not iso:
            refused.append((src, label, 'no country code'))
            continue
        if iso in UKEYS:
            refused.append((src, label, f'keyed to the currency union {iso}; a union key expands '
                                        f'to every member country, so confirm this is about the '
                                        f'union bank itself before filing by hand'))
            continue
        if iso not in places:
            refused.append((src, label, f'country code {iso} is not a place on the map'))
            continue

        if k == 'tie':
            if r['relation'] not in RELATIONS:
                refused.append((src, label, f"relation {r['relation']!r} is not in the vocabulary; "
                                            f"a new relation also needs a SAY entry in app.js"))
                continue
            if r.get('entity_type') not in ENTITY_TYPES:
                refused.append((src, label, f"entity_type {r.get('entity_type')!r} is not in the "
                                            f"vocabulary"))
                continue
            det = r.get('detail') or ''
            if len(det) < MIN_DETAIL:
                refused.append((src, label, f'detail is {len(det)} characters; it renders as a '
                                            f'standalone sentence in a popup and needs {MIN_DETAIL}'))
                continue
            if (r['relation'] == 'holds its gold reserves in custody'
                    and r.get('entity_hq_iso3') == iso and not PLACE_WORDS.search(r['entity'])):
                refused.append((src, label, 'a bank holding its own gold must name the place that '
                                            'holds it, or the popup says the bank holds its gold '
                                            'in custody of itself'))
                continue
            key = (fold(r['entity']), iso, r['relation'])
            if key in have_tie:
                dropped.append((src, label, 'already on the map')); continue
        elif k == 'event':
            if (r.get('kind') or '').strip().lower() == 'other':
                refused.append((src, label, 'kind "other" is not counted on the layer or in the '
                                            'score; it is for appointments and court rulings only'))
                continue
            if len((r.get('summary') or '')) < MIN_DETAIL:
                refused.append((src, label, 'summary too short to stand alone in a box')); continue
            if (iso, r.get('source_url') or '') in have_ev:
                dropped.append((src, label, 'already on the map')); continue
        elif k == 'case':
            if r['status'] not in CC_COUNTED | CC_NOT_COUNTED:
                refused.append((src, label, f"status {r['status']!r} is on neither list; "
                                            f"build_final.py refuses to build on it"))
                continue
            if len((r.get('summary') or '')) < MIN_DETAIL:
                refused.append((src, label, 'summary too short to stand alone in a box')); continue
            if (iso, r.get('source_url') or '', (r.get('people') or '')[:40]) in have_case:
                dropped.append((src, label, 'already on the map')); continue
        else:
            if len((r.get('summary') or '')) < MIN_DETAIL:
                refused.append((src, label, 'summary too short to stand alone in a box')); continue
            if (iso, r.get('source_url') or '', (r.get('people') or '')[:40]) in have_rd:
                dropped.append((src, label, 'already on the map')); continue

        ok, why, handcheck = url_ok(r.get('source_url'), waived)
        if not ok:
            (handcheck_list if handcheck else refused).append((src, label, why)); continue

        filed[k].append(r)
        if k == 'tie':
            have_tie.add((fold(r['entity']), iso, r['relation']))
        elif k == 'event':
            have_ev.add((iso, r.get('source_url') or ''))
        elif k == 'case':
            have_case.add((iso, r.get('source_url') or '', (r.get('people') or '')[:40]))
        else:
            have_rd.add((iso, r.get('source_url') or '', (r.get('people') or '')[:40]))

    NAME = {'tie': 'ties (networks.json)', 'event': 'events (events_gold.json)',
            'rd': 'revolving door (corruption.json)', 'case': 'corruption cases (corruption.json)'}
    print(f"read {len(incoming)} records from {len(args)} file(s)"
          + (f"; collapsed {collapsed} same-person-same-source duplicates on the way in" if collapsed else ""))
    for k in ('case', 'rd', 'event', 'tie'):
        if filed[k]:
            print(f"\nWOULD FILE {len(filed[k])} {NAME[k]}:" if dry else f"\nFILED {len(filed[k])} {NAME[k]}:")
            for r in filed[k]:
                print(f"  {(r.get('cb_iso3') or r.get('iso3')):5s} "
                      f"{(r.get('entity') or r.get('people') or r.get('summary'))[:72]}")
    if dropped:
        print(f"\nDROPPED {len(dropped)} already on the map:")
        for s, l, w in dropped:
            print(f"  {l[:60]:60s}  {w}")
    if handcheck_list:
        print(f"\nNOT FILED, NEEDS A HAND CHECK {len(handcheck_list)} "
              f"(the host blocks automated requests; the page may be perfectly good):")
        for s_, l, w in handcheck_list:
            print(f"  {l[:52]:52s}  {w}")
    if refused:
        print(f"\nREFUSED {len(refused)}:")
        for s, l, w in refused:
            print(f"  {l[:52]:52s}  {w}")
    if not any(filed.values()):
        print('\nnothing to file')

    if dry:
        print('\n(dry run; nothing written. Re-run without --dry to file.)')
        return 0
    if filed['case'] or filed['rd']:
        cor['cases'] += filed['case']; cor['revolving_door'] += filed['rd']
        W('corruption.json', cor)
    if filed['event']:
        evg['events'] += filed['event']; W('events_gold.json', evg)
    if filed['tie']:
        nets['links'] += filed['tie']; W('networks.json', nets)
    if any(filed.values()):
        print('\nwritten. Now: rebuild, then run fix_record_index.py, audit_data.py, '
              'coverage.py and check_scores.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
