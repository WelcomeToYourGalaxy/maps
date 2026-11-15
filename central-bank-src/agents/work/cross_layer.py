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
 'SWZ': "Filed at round 53, and it widens the test. No governor was removed, so this does not "
        "turn on the round-44 removal rule but on the 'pressured' half of it, with the head of "
        "state as the actor: governor Majozi Sithole said a royal command required him to attend "
        "a meeting about Farmers Bank on 14 July 2017; in May 2018 the finance minister told the "
        "bank that King Mswati III had ordered an investigation into its reluctance to license "
        "the venture; a conditional licence followed in September 2018 after a royal command; and "
        "when the bank revoked that licence in October 2020 a minister-chaired appeal overrode "
        "the revocation. What the state did is to order an investigation into the bank's own "
        "supervisory decision and then reverse it, which is the same shape as Uganda's audit of "
        "the bank closures. Found by reading writeups.json, not by a search: the facts had been "
        "in the Eswatini paragraph for rounds while the moves layer rendered the country blank.",
 'VUT': "Filed at round 54, and found the same way as Eswatini: by grepping writeups.json for the "
        "absent list, not by a search. The Ombudsman of Vanuatu's report of 3 July 1996 finds at 6.2 "
        "that 'The Minister of Finance applied pressure to the Governor of the Reserve Bank for him to "
        "execute the documents', and at 7.4 that the governor 'so executed the Guarantees under "
        "pressure from the Minister of Finance'. No governor was removed, so this turns on the "
        "'pressured' half of the rule with a minister as the actor, and the actor is named by the "
        "state's own Ombudsman rather than by the press. The corruption findings against the governor "
        "stay in the corruption case; the event records only what the minister did.",
 'PNG': "REVERSED at round 54, on the reasoning, and not quietly. Round 44 excluded Papua New Guinea "
        "with 'a stay was dismissed; no removal and no charge' -- judged against the removal half of "
        "the rule, which was the only half there was at the time. Two things have changed since. "
        "Round 53 widened the test with Eswatini, where nothing was removed and the record turns on "
        "what the state did to the institution. And the test the exclusion should always have been "
        "measured against was already on the map: Slovenia is filed as a move for 6 July 2016, when "
        "police searched the premises of Banka Slovenije in a criminal investigation in which the "
        "governor was a suspect, with no removal and no charge of the governor at that point. Papua "
        "New Guinea is that shape exactly -- the National Fraud and Anti-Corruption Directorate "
        "searched the Bank of PNG's offices in August and September 2023 in an investigation into the "
        "then acting governor. The round-44 reason is not wrong about the facts; it applied a narrower "
        "rule than the one the map now follows, and keeping it would have left the layer inconsistent "
        "with its own Slovenian record. She has not been charged and nothing is proven, and the record "
        "says so. Papua New Guinea separately gained a second, unrelated record this round, the "
        "government-ordered review of the Central Banking Act 2000 of 13 May 2021.",
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
 'TON': "Two separate things, both excluded. The 2017-19 forgery case is a suspended sentence on a "
        "member of staff, which was the round-44 reason here and is a regex artifact. The newer case, "
        "reviewed at round 54, is a real candidate and still does not qualify: Tonga's "
        "Anti-Corruption Commissioner sued the National Reserve Bank and its directors over a 2024 "
        "staff payment, and on 20 November 2025 the Court of Appeal dismissed the proceeding, finding "
        "no reasonable cause of action against the bank and that the claim against the directors "
        "failed too. A state body did take the bank to court, but 'a court dismissing a claim' is "
        "named in the exclusions, and here the appellate court held there was no cause of action "
        "against the institution at all. Filing it would say more than the source does.",
 'SMR': "The Tribunal dismissed the case. Regex artifact.",
 'BIH': "Reviewed at round 54. A criminal complaint -- the source does not say whose -- accused "
        "governor Senad Softic over an office building in Pale and a land purchase in Sarajevo, and "
        "the BiH Prosecutor's Office said in February 2023 it had opened a case and was verifying the "
        "allegations, which the bank denied amounted to an investigation. No organ of the state "
        "removed, suspended or pressed the governor, nothing was searched or seized, and the "
        "complaint was not brought by a state body. This is a prosecution of an individual, which the "
        "exclusions name.",
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
