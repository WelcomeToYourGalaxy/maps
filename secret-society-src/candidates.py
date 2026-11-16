#!/usr/bin/env python3
"""The candidate pipeline: capture a lead the moment it is found, verify it later.

Why this exists. HANDOFF.md has carried this line since 3 November 2026: "Leads named by
last round's agents but not confirmed are not stored; run the scopes again." Every round
since has thrown away the leads it could not finish and paid to rediscover them. An agent
that runs out of budget half way through a document loses everything it had read.

So discovery and verification are separated. data/candidates.json holds leads with their
source locator and the verbatim excerpt that supports them. **build.py does not read it**,
so nothing here reaches a reader until it has been written up as a record and merged into
cases.json. A candidate is not a case and is never counted as one.

Statuses, in order:
  discovered             found mechanically; excerpt and locator captured, nobody has read it
  apparently_qualifying  read, and it looks like it meets BRIEF11's test
  awaiting_verification  claim written, sources being checked
  verified               written up as a full record and merged into cases.json
  rejected               read and it fails the test; reason recorded
  duplicate              the case is already in cases.json or removed_records.json
  upgrade                not a new case, but new facts for a record already held

Commands:
  python3 candidates.py harvest <symbol> ...   capture every candidate paragraph as discovered
  python3 candidates.py stats                  counts by status, by document, by country
  python3 candidates.py list <status> [n]      show candidates in a status
  python3 candidates.py set <id> <status> [note]
"""
import json, os, re, sys, collections, datetime, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
D, WORK = os.path.join(HERE, 'data'), os.path.join(HERE, 'work')
CAND = os.path.join(D, 'candidates.json')
TEXT = os.path.join(WORK, 'text')

BODY = re.compile(r'\b(police|gendarm|customs|judge|prosecut|magistrat|court|minist|mayor|'
                  r'senator|deputy|parliament|army|military|navy|intelligence|border|port|'
                  r'central bank|tax|revenue|immigration|commissioner|governor)\w*\b', re.I)
TIE = re.compile(r'\b(infiltrat|collusion|collud|complicit|facilitat|bribe|bribery|corrupt|'
                 r'embezzl|divert|kickback|protect|payroll|supplied|tipped off|member of|'
                 r'recruited|on behalf of|in exchange for)\w*\b', re.I)
NAME = re.compile(r'\b[A-Z][a-z]{2,}(?:\s+(?:[A-Z][a-z]{2,}|al|bin|de|van))+\b')
STOP = re.compile(r'^(The|This|These|Security Council|United Nations|Panel of|Group of|'
                  r'Member States?|Annex|Table|Human Rights|See also|In addition|Islamic Republic)', re.I)


def _load():
    if os.path.exists(CAND):
        return json.load(open(CAND, encoding='utf-8'))
    return {'note': 'Leads captured at discovery. build.py does not read this file. '
                    'A candidate is not a case.', 'candidates': []}


def _save(c):
    json.dump(c, open(CAND, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def _known():
    """Titles and description text of everything already decided, for duplicate flagging."""
    cases = json.load(open(os.path.join(D, 'cases.json'), encoding='utf-8'))
    rem = json.load(open(os.path.join(D, 'removed_records.json'), encoding='utf-8'))['cases']
    blob = ' '.join((c.get('n', '') + ' ' + (c.get('d') or '')) for c in cases + rem).lower()
    return blob


def harvest(symbols):
    c = _load()
    have = {x['sha'] for x in c['candidates']}
    known = _known()
    today = datetime.date.today().isoformat()
    added = dup = 0
    for sym in symbols:
        fn = os.path.join(TEXT, sym.replace('/', '_') + '.txt')
        if not os.path.exists(fn):
            print(f'  {sym}: not indexed'); continue
        txt = open(fn, encoding='utf-8').read()
        page = 0
        for block in re.split(r'\n(?=\s*(?:\d{1,3}\.\s|\[\[page))', txt):
            m = re.search(r'\[\[page (\d+)\]\]', block)
            if m:
                page = int(m.group(1))
            w = block.split()
            if not (35 <= len(w) <= 700):
                continue
            if not (BODY.search(block) and TIE.search(block)):
                continue
            names = sorted({n for n in NAME.findall(block) if not STOP.match(n)})
            if len(names) < 2:
                continue
            body = ' '.join(w)
            sha = hashlib.sha1(body[:400].encode()).hexdigest()[:12]
            if sha in have:
                continue
            have.add(sha)
            # rough duplicate flag: do two of this paragraph's names already appear together
            hits = sum(1 for n in names if n.lower() in known)
            status = 'duplicate' if hits >= 2 else 'discovered'
            if status == 'duplicate':
                dup += 1
            else:
                added += 1
            c['candidates'].append({
                'id': f'{sym.replace("/", "_")}-p{page}-{sha}', 'sha': sha,
                'symbol': sym, 'page': page, 'names': names[:8],
                'excerpt': body[:900], 'words': len(w),
                'claim': None, 'cells': None, 'status': status,
                'discovered': today, 'note': 'names already in the dataset' if status == 'duplicate' else None})
        print(f'  {sym}: harvested')
    _save(c)
    print(f'\n{added} new candidates, {dup} flagged as probable duplicates, '
          f'{len(c["candidates"])} in the file')


def stats():
    c = _load()['candidates']
    print(f'{len(c)} candidates in data/candidates.json\n')
    print('by status:')
    for k, v in collections.Counter(x['status'] for x in c).most_common():
        print(f'  {k:22s} {v:5d}')
    print('\ntop documents by candidates not yet rejected or duplicated:')
    live = [x for x in c if x['status'] in ('discovered', 'apparently_qualifying', 'awaiting_verification')]
    for k, v in collections.Counter(x['symbol'] for x in live).most_common(14):
        print(f'  {k:18s} {v:4d}')
    print(f'\n{len(live)} live candidates awaiting a reading.')


def show(status, n=12):
    c = [x for x in _load()['candidates'] if x['status'] == status]
    print(f'{len(c)} in status {status}; showing {min(n, len(c))}\n')
    for x in c[:n]:
        print(f'[{x["id"]}] {x["symbol"]} p.{x["page"]} names={x["names"][:5]}')
        print(f'  {x["excerpt"][:520]}\n')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, a = sys.argv[1], sys.argv[2:]
    if cmd == 'harvest':
        harvest(a)
    elif cmd == 'stats':
        stats()
    elif cmd == 'list':
        show(a[0], int(a[1]) if len(a) > 1 else 12)
    elif cmd == 'set':
        c = _load()
        for x in c['candidates']:
            if x['id'] == a[0]:
                x['status'] = a[1]
                if len(a) > 2:
                    x['note'] = a[2]
        _save(c); print('ok')
    else:
        sys.exit(__doc__)
