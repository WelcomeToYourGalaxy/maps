#!/usr/bin/env python3
"""Round 64: remove the writeups brief's own rules from the paragraphs that printed them.

Round 63 found this in five of fourteen drafts in one batch and fixed those five. It never swept
the corpus. The first full sweep (agents/work/check_prose.py) finds it in 87 places: "Moving
between jobs is not wrongdoing" 23 times, "This is a career move, not an accusation" 10 times,
and so on. Every word of those is in the brief and none is in any box, which is why the fact-leak
check passes them -- and they are the closing moral the voice rules forbid. A tie stated plainly
already reads as a tie; a reader told it is not wrongdoing starts wondering who said it was.

Two kinds of repair. Where the sentence is nothing but the moral, the sentence goes. Where it
carries a fact as well, only the clause goes. Nothing is reworded: no sentence gains a word it
did not have, so no claim can change. Anything the table does not match is listed for hand work
rather than guessed at.
"""
import json, os, re, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
P = os.path.join(A, 'writeups.json')
w = json.load(open(P, encoding='utf-8'))
dry = '--dry' in sys.argv

# whole sentences that say nothing but the moral -- the sentence is removed
DROP = [
 "Moving between jobs is not wrongdoing.",
 "This is a career move, not an accusation.",
 "The source records a career move, not an accusation.",
 "The source gives a career path, not an accusation.",
 "A board seat is not an accusation.",
 "A board seat is not wrongdoing.",
 "A career move is not an accusation.",
 "That is a career move, not an accusation.",
 "Moving between jobs is not an accusation of wrongdoing.",
 "It is a career move, not an accusation of wrongdoing.",
 "The movement between the two posts is a career record, not an accusation.",
 "The move itself is not an allegation of wrongdoing.",
 "A tie is not wrongdoing by the company.",
 "A tie is not wrongdoing by dfcu Bank.",
 "The tie is the stock, not wrongdoing by Apple.",
 "Moving between a bank and the body that oversees banking is a career move, not an accusation.",
 "Taking a job in private banking after public office is a tie, not an allegation of anything improper.",
]
# clauses inside a sentence that carries a fact -- only the clause is removed
TRIM = [
 (", and a career move is not an accusation:", ":"),
 (", and moving between jobs is not wrongdoing:", ":"),
 (", and taking a job is not an accusation:", ":"),
 (", which is a career move and not an accusation:", ":"),
 (", which is not an accusation:", ":"),
 (", and it is not an accusation:", ":"),
 (", and a career move is not an accusation.", "."),
 (", which is a career move and not an accusation.", "."),
 (", which is not an accusation.", "."),
 (", a career move and not an accusation.", "."),
 (", and the move is not an accusation.", "."),
 (", not an accusation, and nothing improper is recorded.", "."),
 ("; a job move is not an accusation.", "."),
 ("; that move is not an accusation.", "."),
 (", and it is an audit role, not an accusation.", ", and it is an audit role."),
 (", not an allegation of anything.", "."),
 ("The tie is shared membership of the forum and is not wrongdoing.",
  "The tie is shared membership of the forum."),
 ("Four of the ties are careers or paid work, not wrongdoing.",
  "Four of the ties are careers or paid work."),
 ("Most of the ties are careers, and moving between jobs is not wrongdoing.",
  "Most of the ties are careers."),
 ("Being named in the case is not an accusation against him, and no outcome is given.",
  "No outcome is given."),
]

LEAK = re.compile(r'not an accusation|not wrongdoing|not an allegation of', re.I)
n_drop = n_trim = 0
for k, v in list(w.items()):
    if not LEAK.search(v):
        continue
    t = v
    for s in DROP:
        while s in t:
            # take the sentence and the single space that preceded it, if there was one
            i = t.index(s)
            j = i - 1 if i and t[i-1] == ' ' else i
            t = t[:j] + t[i + len(s):]
            n_drop += 1
    for old, new in TRIM:
        while old in t:
            t = t.replace(old, new, 1); n_trim += 1
    t = re.sub(r'  +', ' ', t).strip()
    w[k] = t

print(f'removed {n_drop} whole sentences and {n_trim} clauses')
left = sorted(k for k, v in w.items() if LEAK.search(v))
if left:
    print(f'\n{len(left)} NOT matched by the table -- hand work:')
    for k in left:
        m = LEAK.search(w[k])
        print(f'  {k}\n      ...{w[k][max(0,m.start()-110):m.end()+70]}...')

# no edit may leave broken punctuation or a dangling space
for k, v in w.items():
    for bad in ('  ', ' .', ' ,', '..', ',.', ' :', '::'):
        assert bad not in v, f'{k}: edit left {bad!r} in the text'
    assert v == v.strip(), f'{k}: leading or trailing space'
print('\npunctuation checks passed')

if dry:
    print('(dry run; nothing written)'); sys.exit(0)
json.dump(w, open(P, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('written: writeups.json')
