#!/usr/bin/env python3
"""Round 62: build the writer agents' input files, and verify them before dispatch.

Three traps have bitten this step before, and this script is written against all
three:

1. SPLIT EACH BOX ON "Source says: " AND SEND WHOLE BLOCKS, never a character
   window. Round 17 used a window, cut records mid-sentence, and all four writer
   agents reported ties arriving named but undescribed -- so they left them out.
2. A record with unnamed employers has NO party block and lives in the box head,
   past any head cap. Kuwait's Al-Rumaih sits at character 3,866. So the head is
   not capped at all here.
3. VERIFY BEFORE DISPATCHING. Round 16 shipped eight paragraphs written from
   excerpts that did not contain the new record at all. This script asserts that
   a distinctive token from each of this round's new records appears in that
   key's input, and that no input ends mid-sentence.

Three batches, because the three jobs are different:
  places.json  country boxes whose score moved or which gained a record
  newnodes.json party boxes that have no paragraph at all
  folded.json  party boxes that gained ties when duplicate spellings of one firm
               were folded together, so their paragraph now describes less than
               the box holds
"""
import json
import os
import re
import sys

R = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(R, '..', '..', '..')

BOXES = json.load(open(os.path.join(R, 'boxes.json'), encoding='utf-8'))
WR = json.load(open(os.path.join(A, 'agents', 'writeups.json'), encoding='utf-8'))

# country boxes: the 16 whose exposure score moved, plus the six that gained a
# record whose score could not move (three public-only career moves, Curacao,
# and the two new auditors)
# country boxes: the four whose exposure score moved (KOR, MAC, UGA, WSM) plus
# every other place that gained a record this round -- the eight listed-not-counted
# career moves, the Georgia printer and the three gold custodians, none of which
# can move a score.
PLACES = ['ECU', 'LBY', 'SDN', 'SRB', 'IRL', 'COL', 'TLS']

FOLDED = []

# a distinctive token from each record filed this round, by the key whose input
# must contain it
TOKENS = {
    'p:ECU': 'Mosquera', 'p:LBY': 'Keshlaf', 'p:SDN': 'Empowerment Elimination',
    'p:SRB': 'NBS vaults', 'p:IRL': 'UBS Asset Management', 'p:COL': 'Wellington',
    'p:TLS': 'Barings',
}


def blocks(txt):
    """The box, split into whole blocks: the head, then one block per record."""
    parts = txt.split('Source says: ')
    out = [parts[0].rstrip()]
    for p in parts[1:]:
        out.append('Source says: ' + p.rstrip())
    return [b for b in out if b.strip()]


def entry(key):
    box = BOXES[key]
    return {'key': key,
            'current_paragraph': WR.get(key),
            'box_blocks': blocks(box)}


def write(name, keys):
    missing = [k for k in keys if k not in BOXES]
    if missing:
        print('REFUSED: these keys have no box: %s' % missing)
        return None
    data = [entry(k) for k in keys]
    bad = []
    for e in data:
        joined = ' '.join(e['box_blocks'])
        tok = TOKENS.get(e['key'])
        if tok and tok.lower() not in joined.lower():
            bad.append('%s: this round\'s token %r is not in its own input' % (e['key'], tok))
        # Blocks must reconstruct the box. Splitting on the delimiter cannot truncate
        # by construction, which is the point -- a character window can, and that is
        # what sent four agents the wrong input at round 17. This asserts it rather
        # than trusting it. A block legitimately ENDS with its source title, which
        # carries no full stop, so "ends without punctuation" is not the test.
        rebuilt = ' '.join(x.strip() for x in e['box_blocks'])
        if re.sub(r'\s+', ' ', rebuilt) != re.sub(r'\s+', ' ', BOXES[e['key']]).strip():
            bad.append('%s: the blocks do not reconstruct the box' % e['key'])
    if bad:
        print('REFUSED, nothing written for %s:' % name)
        for x in bad:
            print('  ' + x)
        return None
    p = os.path.join(R, name)
    json.dump(data, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    chars = sum(len(' '.join(e['box_blocks'])) for e in data)
    print('%-14s %2d keys, %6d characters of box text' % (name, len(data), chars))
    return p


def main():
    ok = True
    ok &= bool(write('places.json', ['p:' + c for c in PLACES]))
    newnodes = sorted(k for k in BOXES if k not in WR)
    ok &= bool(write('newnodes.json', newnodes))
    if FOLDED:
        ok &= bool(write('folded.json', ['n:' + n for n in FOLDED]))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
