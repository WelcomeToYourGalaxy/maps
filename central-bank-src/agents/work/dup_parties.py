#!/usr/bin/env python3
"""Find two spellings of one party anywhere on the map.

WHY THIS EXISTS. merge_links.py folds an incoming entity name before comparing
it, but it compares against what is already on the map FOR THAT CENTRAL BANK.
A firm arriving under a new spelling, for a country that holds no record of it,
is not a duplicate by that test -- so the script passes it and the map gains a
second diamond for one firm. Round 49 carried the World Bank's reserve-advisory
programme under five names, a party with 24 ties rendering as five parties.
Round 59 took three more spellings the same way: Oberthur Fiduciaire S.A.S.
beside Oberthur Fiduciaire, G+D Currency Development GmbH beside
Giesecke+Devrient, and two further spellings of Papierfabrik Louisenthal.

Until now the only check was grepping networks.json by hand for a distinctive
word before adding a party. This does that comparison for the whole map at once.

It reads the node list out of a BUILT page, not out of one data file, because
NET.nodes is much larger than networks.json's link entities: it also holds every
party from corruption.json cases and revolving-door records, via parties.json.
Deriving the live set from one data file is what deleted 1,218 writeups at
round 49.

    python3 agents/work/dup_parties.py dist/central_bank_independence.html

Exits 1 if it finds anything, so it can gate a push. Three tests, loosest last:

  fold      identical under merge_links.py's own fold (accents, case,
            punctuation and legal-form filler removed) -- always a duplicate
  subset    one name's folded words are a subset of the other's and the
            shorter has at least two words -- "oberthur fiduciaire" inside
            "oberthur fiduciaire sas"; usually a duplicate
  token     the two share a distinctive token (a word of 5+ characters that
            appears in fewer than four parties on the whole map) -- worth a
            look, often a parent and a subsidiary that are genuinely separate

A parent and its subsidiary are NOT a duplicate: the map deliberately keeps
World Bank Treasury separate from the RAMP programme, because one record is a
Treasury cooperation agreement that does not mention RAMP. So read the groups
rather than folding them automatically.
"""
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict

FILLER = {'the', 'of', 'and', 'bank', 'banknote', 'printing', 'works', 'ltd', 'limited',
          'plc', 'sa', 'ag', 'nv', 'inc', 'llc', 'gmbh', 'co', 'company', 'group',
          'holding', 'holdings', 'doo', 'srl', 'spa', 'as', 'ab', 'oy', 'kk', 'pte',
          'sas', 'sarl', 'aps', 'bv', 'dd', 'ad', 'jsc', 'ojsc', 'pjsc', 'llp'}


def words(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()
    return [w for w in re.findall(r'[a-z0-9]+', s) if w not in FILLER]


def fold(s):
    return ' '.join(sorted(words(s)))


def fold_de(s):
    """The same fold with German transliterations collapsed.

    NFKD plus an ASCII strip turns 'ü' into 'u', never into 'ue', so the two
    ordinary spellings of a German name do not collide: round 61 found the map
    drawing Orell Fuessli, Orell Fussli and Orell Fuessli Security Printing Ltd
    as three parties for one banknote printer, four ties between them. This is a
    SEPARATE test rather than a change to fold(), because collapsing 'ue' into
    'u' in general would also merge genuinely different names.
    """
    out = []
    for w in words(s):
        for a, b in (('ue', 'u'), ('oe', 'o'), ('ae', 'a')):
            w = w.replace(a, b)
        out.append(w)
    return ' '.join(sorted(out))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'dist/central_bank_independence.html'
    m = re.search(r'const D = (\{.*?\});\n', open(path, encoding='utf-8').read(), re.S)
    if not m:
        print('could not find const D in ' + path)
        return 2
    D = json.loads(m.group(1))
    nodes = D['NET']['nodes']
    ties = Counter(l['n'] for l in D['NET']['links'] if l.get('n') is not None)
    ties.update(l['tn'] for l in D['NET']['links'] if l.get('tn') is not None)
    name = {i: n['name'] for i, n in enumerate(nodes)}
    ws = {i: set(words(n['name'])) for i, n in enumerate(nodes)}

    def show(label, groups):
        if not groups:
            return 0
        print('\n' + label)
        for g in groups:
            print('  ' + ' | '.join('%s (%d ties)' % (name[i], ties.get(i, 0)) for i in g))
        return len(groups)

    # 1. identical under the fold
    byfold = defaultdict(list)
    for i, n in enumerate(nodes):
        byfold[fold(n['name'])].append(i)
    same = [sorted(v) for k, v in byfold.items() if k and len(v) > 1]

    # 1b. identical once German transliterations are collapsed
    byde = defaultdict(list)
    for i, n in enumerate(nodes):
        byde[fold_de(n['name'])].append(i)
    seen0 = {frozenset(g) for g in same}
    same_de = [sorted(v) for k, v in byde.items()
               if k and len(v) > 1 and frozenset(v) not in seen0]

    # 2. one folded word set inside another
    seen = {frozenset(g) for g in same} | {frozenset(g) for g in same_de}
    subset = []
    items = [(i, ws[i]) for i in range(len(nodes)) if len(ws[i]) >= 2]
    for a, wa in items:
        for b, wb in items:
            if a < b and wa != wb and (wa <= wb or wb <= wa):
                if frozenset((a, b)) not in seen:
                    subset.append((a, b))
                    seen.add(frozenset((a, b)))

    # 3. a distinctive token shared by two parties
    tok = defaultdict(set)
    for i in range(len(nodes)):
        for w in ws[i]:
            if len(w) >= 5:
                tok[w].add(i)
    token = []
    for w, ids in sorted(tok.items()):
        if 2 <= len(ids) <= 3:
            ids = sorted(ids)
            for a in range(len(ids)):
                for b in range(a + 1, len(ids)):
                    k = frozenset((ids[a], ids[b]))
                    if k not in seen:
                        token.append((ids[a], ids[b]))
                        seen.add(k)

    n = 0
    n += show('Identical under the fold -- these are one party under two names:', same)
    n += show('Identical once German ue/oe/ae are collapsed -- one party, two spellings:', same_de)
    n += show('One name inside the other -- almost always one party:', subset)
    n += show('Share a distinctive word -- read these, a parent and a subsidiary are not a duplicate:', token)
    print('\n%d parties, %d groups to read' % (len(nodes), n))
    if n:
        print('Fold a duplicate into the name already carrying the most ties, keep the')
        print("source's own wording in name_as_stated, and migrate any writeup key the")
        print('rename orphans rather than deleting it.')
    return 1 if n else 0


if __name__ == '__main__':
    sys.exit(main())
