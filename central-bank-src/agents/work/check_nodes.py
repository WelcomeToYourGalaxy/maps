#!/usr/bin/env python3
"""Find party paragraphs that state a tie count the box no longer supports.

WHY THIS EXISTS. check_scores.py catches a COUNTRY paragraph quoting a stale
exposure score, which happens every round. Nothing did the same for a PARTY
paragraph, and party paragraphs routinely open by counting: "tied to eight
central banks", "audits the accounts of two central banks". That number goes
stale the moment a tie is added to the party -- by a new record, or by folding a
duplicate spelling of the firm into it -- and no build, audit or draft check
reads prose for arithmetic.

Round 61 found KPMG's paragraph saying "tied to eight central banks" when the
node held fifteen, with Malta, the Dominican Republic, Fiji, Lebanon, Oman,
Angola and Jordan all missing from a paragraph that enumerates the rest. It had
been accumulating ties for several rounds, and the round-60 pass that rewrote
party paragraphs only covered the nodes that round had folded, so a node whose
ties grew for any other reason was never looked at.

    python3 agents/work/check_nodes.py dist/central_bank_independence.html

Reports, for each party paragraph that states a count, the number it states and
the number its box actually holds. It does not rewrite: the fix is a rewritten
paragraph, not a substituted digit, because a paragraph that counts usually
enumerates too, and the missing ties have to be written in.

Counting distinct central banks, not links: a party with two dated mandates at
one bank is tied to one bank, which is what the prose means.
"""
import json
import re
import sys

WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
         'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
         'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
         'nineteen': 19, 'twenty': 20}

# Only the map's OWN phrasing counts. A paragraph may also quote a source's claim
# about the firm -- "a release says it supplies more than 50 central banks", "63
# central banks own the BIS" -- and those are facts about the firm, not counts of
# what this map holds, so they must not be flagged. The map's own phrasing is
# "tied to N central banks", which is what the writeup brief produces.
# The map's own phrasings. "audits the accounts of N central banks" counts as much as
# "tied to N central banks": PwC's paragraph used the first form and went unchecked for
# a round after the second was added.
# The map's own phrasings, and WHICH ties each one is a claim about. "tied to N central
# banks" counts every tie; "audits N" counts only the audit mandates. Comparing an
# "audits" sentence against the whole tie count cries wolf -- PwC audits ten of the
# thirteen central banks in its box, and both numbers are right -- and a check that
# cries wolf gets ignored, which is how a check dies.
PAT = re.compile(r'(?P<verb>tied to|audits the accounts of|audits|prints the notes of|prints)\s+'
                 r'(?P<n>' + '|'.join(WORDS) + r'|\d{1,3})\s+(?:of them|central banks)\b', re.I)
# The INVERTED form, added at round 68 after it hid a stale count for several rounds.
# RAMP's paragraph said "Fourteen central banks are tied to it" while its box held
# twenty-four, and this check printed "none stale" every round, because the pattern
# above only matches the active phrasing the writeups brief produces. A writer who
# opens a paragraph with the count rather than the firm produces the passive form
# instead, and nothing read it. It is the map's own count either way.
# The same guard applies as above: this must not match a SOURCE's claim about the
# firm, so the subject has to be "it" or "the firm" -- "63 central banks own the BIS"
# and "more than 50 central banks use it" do not match, because "own" and "use" are
# not this map's tie wording.
PAT_INV = re.compile(r'(?P<n>' + '|'.join(WORDS) + r'|\d{1,3})\s+central banks\s+'
                     r'are\s+tied\s+to\s+(?:it|the firm|this firm)\b', re.I)
RELS = {'audits': ('audits its accounts',),
        'audits the accounts of': ('audits its accounts',),
        'prints': ('prints its banknotes',),
        'prints the notes of': ('prints its banknotes',)}


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'dist/central_bank_independence.html'
    m = re.search(r'const D = (\{.*?\});\n', open(path, encoding='utf-8').read(), re.S)
    D = json.loads(m.group(1))
    N, WR = D['NET'], D['WR']
    names = [n['name'] for n in N['nodes']]
    banks, byrel = {}, {}
    for l in N['links']:
        for f in ('n', 'tn'):
            i = l.get(f)
            if i is None:
                continue
            cb = l.get('cb')
            if cb:
                banks.setdefault(i, set()).add(cb)
                byrel.setdefault((i, (l.get('role') or '').lower()), set()).add(cb)

    def count_for(i, verb):
        rels = RELS.get(verb.lower())
        if not rels:
            return len(banks.get(i, ()))
        out = set()
        for (j, role), cbs in byrel.items():
            if j == i and any(r.split()[0] in role for r in rels):
                out |= cbs
        return len(out)

    stale, checked = [], 0
    for i, nm in enumerate(names):
        t = WR.get('n:' + nm)
        if not t:
            continue
        m2 = PAT.search(t)
        verb = m2.group('verb') if m2 else None
        if not m2:
            m2 = PAT_INV.search(t)
            verb = 'tied to'          # the inverted form always counts every tie
        if not m2:
            continue
        checked += 1
        raw = m2.group('n').lower()
        said = WORDS[raw] if raw in WORDS else int(raw)
        actual = count_for(i, verb)
        if said != actual:
            stale.append((nm, said, actual, verb.lower()))

    print('checked %d party paragraphs that state a count' % checked)
    if not stale:
        print('none stale')
        return 0
    print('\n%d state a count their box does not support:' % len(stale))
    for nm, said, actual, verb in sorted(stale, key=lambda x: -abs(x[1] - x[2])):
        print('  %-44s "%s" %-3d box holds %d' % (nm[:44], verb, said, actual))
    print('\nRewrite these paragraphs rather than substituting the digit: a paragraph that')
    print('counts its ties usually enumerates them, so the missing ones have to be written in.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
