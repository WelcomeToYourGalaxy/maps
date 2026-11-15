#!/usr/bin/env python3
"""Round 61: link this round's records to the parties they name, BY HAND.

Same safety as rounds 57 to 60: every entry is keyed on (iso3, a distinctive
token that must appear in that record's own text), and the script REFUSES TO
WRITE ANYTHING if a token matches no record or more than one. `record_index` in
parties.json is a POSITIONAL pointer, and nothing complains when it is wrong --
the party box simply shows another country's facts under this party's heading.

Decisions:

* Roles follow what the map already does for each event kind, checked against
  parties.json rather than guessed: a law change or a public-pressure episode
  takes "pressured, dismissed or prosecuted bank officials" (9 and 21 existing
  uses), an audit or inquiry takes "audited or investigated" (6).
* Names are qualified by country wherever the bare name is unique only inside
  its own country. "State Audit Office of the Republic of Macedonia" matters
  because the map already carries the State Audit Offices of Hungary and of
  Thailand, and a bare "State Audit Office" is exactly the generic name that
  merged four countries' audit offices into one diamond at round 60.
* BNP Paribas, the Asian Development Bank and Standard Lesotho Bank Limited
  already exist as nodes and are reused under the spelling on the map. BNP
  Paribas El Djazair is kept separate from its parent, as the map keeps Societe
  Generale Albania separate: it is a local subsidiary, and the record's point is
  that the parent owns it 100%.
* Liberty Life Lesotho is NOT the existing "Liberty Mutual Insurance Company"
  node, which is a different firm in a different country.
* Four Tajik records name one employer, Spitamen Bank, so it gets one node with
  four links -- which is right: it is one party that took four of the National
  Bank's officials onto its boards.
* Commentators are not parties. The Bahamas record names the opposition finance
  spokesman who asserted the breach, and the Namibia record names an opposition
  party leader who put a figure on the bank's losses. Neither acted on the bank,
  and no role in the vocabulary fits "said so", so they stay in the record's text
  and off the ties layer. The same reasoning leaves the IMF off the Samoa event:
  it warned the finance minister against the change, which is not acting on the
  bank.
* Samoa's audit record links the Audit Office that made the finding. The Ministry
  of Finance, at which the recommendations were aimed, is named in the record but
  not linked, because its role here is "the recommendations were addressed to it"
  and the vocabulary has nothing for that short of "other".
"""
import json
import os
import sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
L = lambda n: json.load(open(os.path.join(A, 'agents', n), encoding='utf-8'))

RD = 'employed an official before or after (revolving door)'
PRESS = 'pressured, dismissed or prosecuted bank officials'
AUDIT = 'audited or investigated'
GOT = 'received money, favors or contracts from the bank'

T_RD = {
    ('CUW', 'Jardim'): [
        ('Banco di Caribe', 'Banco di Caribe', 'bank', 'Willemstad', 'CUW'),
        ('United Group Holdings', 'United Group Holdings', 'company', 'Willemstad', 'CUW')],
    ('DZA', 'Lebbou'): [
        ('BNP Paribas El Djazaïr', 'BNP Paribas El Djazaïr', 'bank', 'Algiers', 'DZA'),
        ('BNP Paribas', 'BNP Paribas France', 'bank', 'Paris', 'FRA')],
    ('LSO', 'Mohasoa'): [
        ('Liberty Life Lesotho', 'Liberty Life Lesotho', 'company', 'Maseru', 'LSO'),
        ('Standard Bank Group', 'Standard Bank Group', 'bank', 'Johannesburg', 'ZAF')],
    ('DOM', 'Hazoury'): [
        ('Banco de Reservas', 'Banco de Reservas', 'bank', 'Santo Domingo', 'DOM')],
    ('TJK', 'Khuseynova'): [('Spitamen Bank', 'CJSC "Spitamen Bank"', 'bank', 'Dushanbe', 'TJK')],
    ('TJK', 'Dzhabirova'): [('Spitamen Bank', 'CJSC "Spitamen Bank"', 'bank', 'Dushanbe', 'TJK')],
    ('TJK', 'Hamralizoda'): [('Spitamen Bank', 'CJSC "Spitamen Bank"', 'bank', 'Dushanbe', 'TJK')],
    ('TJK', 'Samandarzoda'): [('Spitamen Bank', 'CJSC "Spitamen Bank"', 'bank', 'Dushanbe', 'TJK')],
    ('AFG', 'Ahmady'): [
        ('T. Rowe Price', 'T. Rowe Price', 'company', 'Baltimore', 'USA'),
        ('Acadian Asset Management', 'Acadian Asset Management', 'company', 'Boston', 'USA'),
        ('Fortress Investment Group', 'Fortress Investment Group', 'company', 'New York', 'USA')],
    ('BTN', 'Damche Tenzin'): [
        ('Bank of Bhutan', 'Bank of Bhutan Limited', 'bank', 'Thimphu', 'BTN')],
    ('TLS', 'Helder Lopes'): [
        ('Asian Development Bank', "the Asian Development Bank's initiative", 'international body',
         'Manila', 'PHL')],
}

T_EV = {
    ('MKD', '11-107/8'): [
        ('State Audit Office of the Republic of Macedonia', 'Drzaven zavod za revizija',
         'agency', 'Skopje', 'MKD', AUDIT),
        ('Branislav Gulev', 'Branislav Gulev', 'person', 'Skopje', 'MKD', AUDIT)],
    ('WSM', 'Attorney-General'): [
        ('Government of Samoa', "Samoa's government", 'government', 'Apia', 'WSM', PRESS),
        ('Laaulialemalietoa Leuatea Polataivao Schmidt', 'Prime Minister Laaulialemalietoa Leuatea '
         'Polataivao Schmidt', 'person', 'Apia', 'WSM', PRESS)],
    ('NAM', 'smelling of corruption'): [
        ('Netumbo Nandi-Ndaitwah', 'President Netumbo Nandi-Ndaitwah', 'person',
         'Windhoek', 'NAM', PRESS)],
}

T_CASE = {
    ('BHS', '232.3'): [
        ('Ministry of Finance of The Bahamas', 'the Bahamian government', 'government',
         'Nassau', 'BHS', GOT)],
    ('WSM', 'Audit Office'): [
        ('Samoa Audit Office', 'the Samoa Audit Office', 'agency', 'Apia', 'WSM', AUDIT)],
}

FIELDS = ('people', 'move', 'summary', 'source_title', 'kind', 'category')


def main():
    dry = '--dry' in sys.argv
    cor, par, evg = L('corruption.json'), L('parties.json'), L('events_gold.json')
    links = par['links']
    arrays = {'revolving_door': cor['revolving_door'], 'event': evg['events'], 'case': cor['cases']}
    tables = [('revolving_door', T_RD, RD), ('event', T_EV, None), ('case', T_CASE, None)]
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
