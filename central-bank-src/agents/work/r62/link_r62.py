#!/usr/bin/env python3
"""Round 62: link this round's records to the parties they name, BY HAND.

Same safety as rounds 57 to 61: every entry is keyed on (iso3, a distinctive
token that must appear in that record's own text), and the script REFUSES TO
WRITE ANYTHING if a token matches no record or more than one. `record_index` in
parties.json is a POSITIONAL pointer and nothing complains when it is wrong --
the party box simply shows another country's facts under this party's heading.

Decisions:

* Country-qualified names where the bare name is unique only inside its own
  country. "National Bank" is the clearest case on the whole map: twenty-two
  nodes already contain those words, so Sudan's two employers go in as "National
  Bank (Sudan)" and "Workers National Bank (Sudan)". Bolivia's Banco Union needs
  it for a sharper reason -- a node named "Banco Union" ALREADY EXISTS and it is
  Paraguay's, so an unqualified name would have put a Bolivian employer onto a
  Paraguayan bank's marker.
* "Ministry of Finance of Tonga", "Government of Samoa" and
  "Laaulialemalietoa Leuatea Polataivao Schmidt" are reused at exactly the
  spelling already on the map, so they gain a link rather than a second diamond.
* El Nilein Bank is entered once, under the spelling its own group history uses,
  with the Central Bank of Sudan's spelling kept in name_as_stated.
* Gazprom PJSC, Gazprombank JSC and Gazprom Transgaz Belarus are NOT linked.
  They own Belgazprombank, which is why that move is not counted, but they did
  not employ the official and no role in the vocabulary fits "owns the
  employer". The shareholding is quoted in the record's own text.
* Vanuatu's record also names the Chamber of Commerce, Airports Vanuatu and
  VANAIR as earlier posts. Only the employer the move itself names is linked;
  an airline and an airport are not what this row is about and would add
  diamonds that say nothing.
* Uganda Reinsurance Company published the Kaboyo biography but the page states
  no role for him there, so it is the source and not a party.
* Samoa's second-reading event takes "pressured, dismissed or prosecuted bank
  officials", which is what the map already uses for a law change, and the same
  two parties as the April record.
"""
import json
import os
import sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
L = lambda n: json.load(open(os.path.join(A, 'agents', n), encoding='utf-8'))

RD = 'employed an official before or after (revolving door)'
PRESS = 'pressured, dismissed or prosecuted bank officials'

T_RD = {
    ('MAC', 'Well Link'): [
        ('Well Link Bank', 'Well Link Bank, Ltd.', 'bank', 'Macao', 'MAC'),
        ('A&P Investment Fund Management', 'A&P Investment Fund Management',
         'asset manager', 'Macao', 'MAC')],
    ('UGA', 'Alpha Capital'): [
        ('Alpha Capital Partners', 'Alpha Capital Partners', 'asset manager', 'Kampala', 'UGA')],
    ('KOR', 'Seoul Foreign Exchange'): [
        ('Seoul Foreign Exchange Brokerage', 'Seoul Foreign Exchange Brokerage',
         'brokerage', 'Seoul', 'KOR')],
    ('SDN', 'Elneilin'): [
        ('El Nilein Bank', 'Elneilin Bank', 'bank', 'Khartoum', 'SDN')],
    ('SDN', 'Workers National'): [
        ('National Bank (Sudan)', 'National Bank', 'bank', 'Khartoum', 'SDN'),
        ('Workers National Bank (Sudan)', 'Workers National Bank', 'bank', 'Khartoum', 'SDN')],
    ('BOL', 'Banco de la Union'): [
        ('Banco Unión S.A. (Bolivia)', 'Banco de la Union S.A.', 'bank', 'La Paz', 'BOL'),
        ('Banco de Cochabamba S.A.', 'Banco de Cochabamba S.A.', 'bank', 'Cochabamba', 'BOL'),
        ('Compañía Boliviana de Seguros S.A.', 'Compania Boliviana de Seguros S.A.',
         'insurer', 'La Paz', 'BOL')],
    ('MRT', "Caisse Nationale d'Assurance Maladie"): [
        ("Caisse Nationale d'Assurance Maladie (Mauritania)", 'CNAM',
         'agency', 'Nouakchott', 'MRT')],
    ('CUB', 'CADECA'): [
        ('Banco Popular de Ahorro', 'Banco Popular de Ahorro', 'bank', 'Havana', 'CUB'),
        ('CADECA S.A.', 'CADECA S.A.', 'company', 'Havana', 'CUB')],
    ('TON', 'Royal Oceania'): [
        ('Ministry of Finance of Tonga', 'the Tonga Ministry of Finance',
         'government', 'Nukuʻalofa', 'TON')],
    ('VUT', 'Marakon Alilee'): [
        ('Ministry of Trade, Commerce, Industry and Tourism (Vanuatu)',
         'the Ministry of Trade, Commerce, Industry and Tourism',
         'government', 'Port Vila', 'VUT')],
    ('BLR', 'Belgazprombank'): [
        ('Belgazprombank', 'Belgazprombank OJSC', 'bank', 'Minsk', 'BLR'),
        ('Belarusbank', 'Belarusbank', 'bank', 'Minsk', 'BLR')],
}

T_EV = {
    ('WSM', 'second reading'): [
        ('Government of Samoa', "Samoa's government", 'government', 'Apia', 'WSM', PRESS),
        ('Laaulialemalietoa Leuatea Polataivao Schmidt',
         'Prime Minister Laaulialemalietoa Leuatea Polataivao Schmidt',
         'person', 'Apia', 'WSM', PRESS)],
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
        print('  %-14s [%3d] %-4s %-46s %s'
              % (x['record_type'], x['record_index'], x['cb_iso3'], x['party'][:46], x['hq_city']))
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
