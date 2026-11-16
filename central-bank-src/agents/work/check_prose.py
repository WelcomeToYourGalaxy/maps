#!/usr/bin/env python3
"""Find the two prose faults no other check reads for: a stranded splice, and a brief instruction
printed as a sentence. Run it beside the other four. (round 64)

1. A SPLICE. Replacing a fragment that had been cut off mid-word leaves the tail of the original
   behind. It has happened twice and survived a build, an audit and a push both times -- once as
   "...government papert 60.8 billion cedi for 2022." and once as "and its law scores 0." beside
   a stranded "...for every denomination.637 of 1 for written independence". Nothing reads prose
   for sense, so the signature is what gets checked: a LETTER, then a full stop, then a digit,
   with no space. An ordinary decimal has a digit before the point, so it does not match, and
   that distinction is the whole reason this is readable -- the obvious pattern, a full stop
   followed by a digit, returns every decimal figure on the map and gets ignored.

2. A BRIEF LEAK. The writeups brief tells the writer that a career move is not an accusation and
   a tie is not wrongdoing. Five of fourteen drafts at round 63 printed that rule as a closing
   sentence. Every word of it is in the brief and none is in the box, so the fact-leak check
   passes it, and it is exactly the closing moral the voice rules forbid: a tie stated plainly
   already reads as a tie, and a reader told it is not wrongdoing starts wondering who said it was.

Exits non-zero on a find, so it can gate a push.
"""
import json, os, re, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
w = json.load(open(os.path.join(A, 'writeups.json'), encoding='utf-8'))

SPLICE = re.compile(r'[A-Za-z]\.\d')
# Tightened at round 64 after the first full-corpus sweep. The loose form caught three
# LEGITIMATE lines -- "this is an allegation and no outcome is reported" states a case's
# evidentiary status, which the map does say and should. A leak tells the reader how to feel
# about a tie or a move; a status line says what the record is. Only the first is matched.
LEAK = re.compile(r'not an accusation|not wrongdoing|not an allegation of|is not evidence'
                  r'|does not imply|which is not to say|this does not mean'
                  r'|nothing in that is an allegation', re.I)

bad = 0
print(f'checked {len(w)} paragraphs')
for label, pat, why in (('SPLICE', SPLICE, 'a full stop joining a word to a digit'),
                        ('BRIEF LEAK', LEAK, 'a rule for the writer printed as a sentence')):
    hits = [(k, m) for k, v in sorted(w.items()) for m in pat.finditer(v)]
    if not hits:
        print(f'  no {label.lower()}')
        continue
    bad += len(hits)
    print(f'\n{len(hits)} {label} -- {why}:')
    for k, m in hits:
        v = w[k]
        print(f'  {k}\n      ...{v[max(0, m.start()-80):m.end()+60]}...')
sys.exit(1 if bad else 0)
