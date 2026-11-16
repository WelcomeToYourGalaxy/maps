#!/usr/bin/env python3
"""Round 63: decide each incoming record by hand, keyed on a distinctive token.

Refuses to write anything if a token matches no record or more than one, so a
decision cannot land on the wrong record. Carries the reasoning for each.
"""
import json
import sys

R = '/root/cb/agents/work/r63/'

EV = [
    ('Dabanga', dict(), None,
     "SUDAN, a record and not a place — Sudan already counts on this row. On 9 February 2020 the "
     "transitional government's Empowerment Elimination, Anti-Corruption and Funds Recovery "
     "Committee dissolved the Central Bank of Sudan's board, along with eleven other banks' boards, "
     "and dismissed nine of the bank's managers, over alleged links to the deposed Bashir "
     "government. `dismissal` is an existing counted kind with 57 uses, so no new vocabulary. The "
     "summary says in terms that the report names no individual and sets out no evidence, which is "
     "the honest shape for a mass dismissal by a political committee."),

    ('loc.gov/item/eritrean-proc-93-1997',
     dict(kind="statutory arrangement letting the head of state appoint and pay the bank's board",
          quote='all nominated members of the Board shall be submitted to the President'),
     None,
     "ERITREA, and it takes the last unworked place off this row's list. Two things were decided "
     "here. FIRST, whether it belongs at all: the brief told the agent that a removal GROUND in a "
     "statute is not an event, which is why Armenia, Belgium, Denmark, Finland, France and "
     "Luxembourg were all closed — nearly every central bank law has a dismissal clause, and "
     "Eritrea's is in fact a normal protection (the Governor may be relieved only for just cause "
     "after consultation with the legislature). **That clause is NOT why this counts.** What counts "
     "is the rest of Proclamation 93/1997: the President appoints the Governor and the Deputy "
     "Governor, the names of all nominated Board members are submitted to the President for "
     "appointment, the Board seats the Finance Ministry's representative and the Auditor General, "
     "the Governor's pay is set by the President, and a director who resigns does so by letter to "
     "the President with the resignation taking effect only once the President accepts it. That is "
     "executive control of who runs the institution, which is exactly what the map's twenty-five or "
     "so `statutory arrangement ...` records already carry. SECOND, the kind string: the agent "
     "coined one, and here that is correct practice rather than a mistake, because this row's "
     "vocabulary is deliberately bespoke — `statutory arrangement placing the bank under the head "
     "of state`, `... letting the head of the executive appoint the bank's board`, `... "
     "subordinating the bank to the King and the finance ministry` are each used once. Shortened to "
     "match that family's length. The quote was trimmed from 17 words to 12 for the standing "
     "under-15-word limit."),
]


def pick(records, token, label):
    hits = [i for i, r in enumerate(records)
            if token.lower() in json.dumps(r, ensure_ascii=False).lower()]
    if len(hits) != 1:
        sys.exit('REFUSED: %s token %r matched %d records, not 1' % (label, token, len(hits)))
    return hits[0]


def main():
    d = json.load(open(R + 'cases_events.json'))
    ev = d['events']
    keep = []
    for token, over, _, why in EV:
        i = pick(ev, token, 'ev')
        r = dict(ev[i])
        r.update(over)
        r['_why'] = why
        keep.append((i, r))
    chosen = {i for i, _ in keep}
    missed = [i for i in range(len(ev)) if i not in chosen]
    if missed:
        sys.exit('REFUSED: events on neither list: %s' % [ev[i].get('iso3') for i in missed])
    if d.get('cases'):
        sys.exit('REFUSED: %d cases arrived and none is on a list' % len(d['cases']))

    recs = []
    for _, r in keep:
        q = (r.get('quote') or '').strip()
        if q and len(q.split()) >= 15:
            sys.exit('REFUSED: quote for %s runs %d words' % (r.get('iso3'), len(q.split())))
        r.pop('_why', None)
        recs.append(r)
    json.dump({'records': recs}, open(R + 'to_merge.json', 'w'), ensure_ascii=False, indent=1)
    for i, r in keep:
        print('%-4s %-12s %s' % (r['iso3'], r['date'], r['kind']))
        print('       quote %d words' % len((r.get('quote') or '').split()))
    print('\nwrote ' + R + 'to_merge.json')


if __name__ == '__main__':
    main()
