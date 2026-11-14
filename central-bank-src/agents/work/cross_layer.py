#!/usr/bin/env python3
"""Which corruption cases also record a STATE action against the bank's leadership?

The two case layers answer different questions: `cc` asks whether there was
corruption inside the bank, `ev` asks whether the state moved against it. An
episode can be both, and several are currently filed only as corruption cases,
so the moves layer renders those countries blank.

This script lists the candidates and the reason each qualifies or does not.
The strict test, applied by hand below and NOT by regex:
  the source must state that an organ of the state - head of state,
  government, parliament, or a union's heads of state - removed, suspended or
  pressured the governor. A court dismissing a claim, a suspended sentence, a
  prosecution of an individual, or the bank's own board acting on its own
  officer does not qualify.
Run it after any round that adds a corruption case naming a removal.
"""
import json, os
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
L = lambda n: json.load(open(os.path.join(A, n)))
import sys as _s; _s.path.insert(0, os.path.join(A, '..'))
from cbnames import UNION

def expand(s):
    out = set()
    for x in s:
        out |= set(UNION.get('ECB' if x == 'EMU' else x, [x]))
        if x in UNION or x == 'EMU': continue
        out.add(x)
    return out

core = json.load(open(os.path.join(A, '..', 'out', 'core.json')))
places = set(core['E'])
ev = L('events_gold.json')['events']
have = expand({r['iso3'] for r in ev if r.get('kind') != 'other'}) & places

# Reviewed by hand at round 44 against the full text of each corruption case.
QUALIFIES = {
 'TZA': "President Kikwete dismissed governor Ballali in January 2008 after the Ernst & Young audit of the EPA account. Head of state removed the governor.",
 'NPL': "On 8 April 2022 the government suspended governor Adhikari and formed a three-member probe committee headed by a former Supreme Court judge; the Supreme Court stayed the suspension on 19 April and he returned.",
 'SOM': "Governor Abrar resigned after seven weeks, writing to the president that she had continuously been asked to sanction deals and violate her fiduciary responsibility. Executive pressure stated in her own resignation letter.",
 'BCEAO': "A summit of UEMOA heads of state required and accepted governor Dacoury-Tabley's resignation in January 2011. Expands to all eight member countries.",
}
MARGINAL = {
 'MDV': "Governor Naseer resigned in July 2019 after being summoned twice by parliament's public finance committee. Parliamentary pressure, but the summons concerned allegations against him personally and no organ of state is said to have required him to go.",
 'BDI': "The summary records a 'dismissed governor' but does not say who dismissed him. Unstated settles nothing - needs a source naming the actor.",
}
EXCLUDED = {
 'ALB': "The bank's own board dismissed Fullani; prosecutors arrested him. Internal action plus a prosecution, not the state moving on the institution.",
 'MNE': "The bank's own Council asked parliament to dismiss its deputy governor. Direction is bank to officer, not state to bank.",
 'ECCB members': "A US federal judge dismissed the Stanford claims. A court dismissing a claim is not a removal.",
 'EMU members': "The European Ombudsman recommended Draghi suspend his Group of Thirty membership. A recommendation about a membership, not a removal.",
 'BEAC members': "A presidential chief of staff resigned over the BEAC Paris findings. Not the bank's leadership and not a state action on the bank.",
 'TON': "A suspended sentence. Regex artifact.",
 'SMR': "The Tribunal dismissed the case. Regex artifact.",
 'PNG': "A stay was dismissed; no removal and no charge.",
}

gain = sorted(c for c in expand(set(QUALIFIES)) & places if c not in have)
print("places on the moves row now: %d of %d (%d%%)" % (len(have), len(places), round(100*len(have)/len(places))))
print("\nQUALIFIES under the strict test, and absent from the moves row: %d places" % len(gain))
print("  " + " ".join(gain))
for k, why in QUALIFIES.items():
    print("\n  %s: %s" % (k, why))
print("\nif cross-filed, the row would read %d of %d = %d%%"
      % (len(have)+len(gain), len(places), round(100*(len(have)+len(gain))/len(places))))
print("\nMARGINAL, left out pending a decision:")
for k, why in MARGINAL.items(): print("  %s: %s" % (k, why))
print("\nEXCLUDED, with the reason, so the list is not re-derived by regex:")
for k, why in EXCLUDED.items(): print("  %s: %s" % (k, why))
