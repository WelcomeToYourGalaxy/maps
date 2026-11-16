#!/usr/bin/env python3
"""Round 65: give three party paragraphs the facts their own boxes withhold.

`build_net.py` appends a career record's summary to a party's detail only when the party's name is
NOT already in the detail. The side effect is that the extra facts in the summary -- who owns the
employer, what the body does -- are withheld from exactly the parties the record names, and handed
instead to the other parties in the same record. Belgazprombank's own box does not carry its own
shareholding; Belarusbank's does, because Belarusbank is not named in the move sentence.

Round 65 MEASURED the fix this document proposed ("append unless the summary adds nothing") and it
is worse than the current behaviour: 419 of 551 career links withhold a summary, 375 of them would
gain a sentence, and the summaries overwhelmingly restate the move with a source attribution
("BlackRock's leadership page states Hildebrand joined BlackRock in 2012 after serving as chairman
of the SNB governing board"). So the change would print the same fact twice in 375 boxes to repair
three. The narrow fix is the right one, and it belongs in the party's own paragraph, which is where
a reader looks anyway.
"""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
P = os.path.join(A, 'writeups.json')
w = json.load(open(P, encoding='utf-8'))
dry = '--dry' in sys.argv

EDITS = {
 'n:Belgazprombank': (
   "Belgazprombank is a bank in Minsk, Belarus.",
   "Belgazprombank is a bank in Minsk, Belarus, and almost all of it belongs to the Gazprom group. "
   "Its shares are held by Russia's Gazprom PJSC and Gazprombank JSC at 49.66 per cent each, "
   "Gazprom Transgaz Belarus at 0.49 per cent and the Belarusian state, through its Ministry of "
   "Energy, at 0.097 per cent."),
 'n:CADECA S.A.': (
   "CADECA S.A. is a company in Havana, Cuba.",
   "CADECA S.A., in Havana, is Cuba's state currency-exchange entity."),
 'n:Well Link Bank': (
   "Well Link Bank is a bank in Macao.",
   "Well Link Bank is a bank in Macao, and its own history page describes it as a fully licensed "
   "commercial bank registered in Macao. That is what makes the career below a move into private "
   "banking rather than between state bodies."),
}
for k, (old, new) in EDITS.items():
    t = w[k]
    assert t.count(old) == 1, f'{k}: fragment appears {t.count(old)} times'
    i = t.index(old)
    print(f'  {k}\n     ...{t[i:i+len(old)+120]!r}...')
    w[k] = t.replace(old, new)
    assert '  ' not in w[k] and ' .' not in w[k], f'{k}: edit left broken spacing'

if dry:
    print('\n(dry run; nothing written)'); sys.exit(0)
json.dump(w, open(P, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('\nwritten: writeups.json')
