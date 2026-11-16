#!/usr/bin/env python3
"""Round 63: link this round's records to the parties they name, BY HAND.

Keyed on (iso3, a distinctive token that must appear in that record's own text), and REFUSES to
write anything if a token matches no record or more than one, because `record_index` in
parties.json is a POSITIONAL pointer and nothing complains when it is wrong.

Head offices follow the standing rule: from the record's own text, else `agents/hq.json`, else the
spelling already on the map, else LEFT NULL. A null city is placed at the country centre and said
so in build_net's output; a null country leaves the party unplaced. Both are better than a guessed
marker, because the map's markers are fixed points. The firms left null here go on the needs_hq
list in the round's prep script.

Decisions:
* Citi is reused at the spelling already on the map, which `agents/hq.json` sources, rather than
  adding "Citibank Quito" as a second node. (Note for a later round: the map carries BOTH "Citi"
  and "Citibank, N.A." already, which is a pre-existing split worth folding.)
* Produbanco takes Ecuador with a null city: the record is an Ecuadorian CV naming the Ecuadorian
  bank whose board he sits on, so the country is established by the record, the city is not.
* Libya's four employers are all new and none has a sourced address. "Libyan Foreign Bank" and
  "Libyan Financial Services Company" take Libya because their own names state it; "Joumhourria
  Bank" and "Arab Italian Bank (UBAE)" take nothing, because their names do not and the rest would
  be my knowledge rather than the source's.
* A&T Bank published the Libyan biography but the page states no post for him there, so it is the
  source and not a party -- the same treatment Uganda Reinsurance Company got at round 62.
"""
import json
import os
import sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
L = lambda n: json.load(open(os.path.join(A, 'agents', n), encoding='utf-8'))

RD = 'employed an official before or after (revolving door)'
PRESS = 'pressured, dismissed or prosecuted bank officials'

T_RD = {
    ('ECU', 'Mosquera'): [
        ('Produbanco', 'Banco de la Produccion S.A. Produbanco', 'bank', None, 'ECU'),
        ('Citi', 'Citibank Quito', 'bank', 'New York', 'USA')],
    ('LBY', 'Keshlaf'): [
        ('Arab Italian Bank (UBAE)', 'Arab Italian Bank (UBAE)', 'bank', None, None),
        ('Libyan Foreign Bank', 'Libyan Foreign Bank', 'bank', None, 'LBY'),
        ('Libyan Financial Services Company', 'Libyan Financial Services Company',
         'company', None, 'LBY'),
        ('Joumhourria Bank', 'Joumhourria Bank', 'bank', None, None)],
}

T_EV = {
    ('SDN', 'Empowerment Elimination'): [
        ('Empowerment Elimination, Anti-Corruption and Funds Recovery Committee',
         'Empowerment Elimination, Anti-Corruption, and Funds Recovery Committee',
         'agency', 'Khartoum', 'SDN', PRESS)],
}

FIELDS = ('people', 'move', 'summary', 'source_title', 'kind', 'category')


def main():
    dry = '--dry' in sys.argv
    cor, par, evg = L('corruption.json'), L('parties.json'), L('events_gold.json')
    links = par['links']
    arrays = {'revolving_door': cor['revolving_door'], 'event': evg['events']}
    tables = [('revolving_door', T_RD, RD), ('event', T_EV, None)]
    have = {(x.get('record_type'), x['record_index'], x['party']) for x in links}
    new, bad = [], []
    for rtype, table, fixed_role in tables:
        recs = arrays[rtype]
        for (iso, tok), parties in table.items():
            hits = [i for i, r in enumerate(recs)
                    if r.get('iso3') == iso
                    and tok.lower() in ' '.join(str(r.get(f) or '') for f in FIELDS).lower()]
            if len(hits) != 1:
                bad.append('%s %s token %r: matched %d records, expected 1'
                           % (rtype, iso, tok, len(hits)))
                continue
            i = hits[0]
            for p in parties:
                party, stated, ptype, city, hiso = p[:5]
                role = fixed_role or p[5]
                if (rtype, i, party) in have:
                    continue
                new.append({'party': party, 'name_as_stated': stated, 'party_type': ptype,
                            'parent': None, 'hq_city': city, 'hq_iso3': hiso,
                            'cb_iso3': recs[i]['iso3'], 'role': role,
                            'record_type': rtype, 'record_index': i,
                            'source_url': recs[i].get('source_url')})
    if bad:
        print('REFUSED, nothing written:')
        for b in bad:
            print('  ' + b)
        return 1
    print('%d new party links' % len(new))
    for x in new:
        print('  %-14s [%3d] %-4s %-44s %s / %s'
              % (x['record_type'], x['record_index'], x['cb_iso3'], x['party'][:44],
                 x['hq_city'] or '(centre)', x['hq_iso3'] or '(unplaced)'))
    if dry:
        print('\n(dry run; nothing written)')
        return 0
    par['links'] = links + new
    json.dump(par, open(os.path.join(A, 'agents', 'parties.json'), 'w', encoding='utf-8'),
              indent=1, ensure_ascii=False)
    print('\nwritten: parties.json now holds %d links' % len(par['links']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
