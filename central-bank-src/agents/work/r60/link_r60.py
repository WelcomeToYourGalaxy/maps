#!/usr/bin/env python3
"""Round 60: link this round's records to the parties they name, BY HAND.

Same safety as rounds 57 to 59, and for the same reason: `record_index` in
parties.json is a POSITIONAL pointer into the cases, revolving_door and events
arrays, and nothing complains when it is wrong -- the party box simply shows
another country's facts under this party's heading. Round 11 removed one
duplicate case, 136 links went wrong, and it survived five rounds.

So every entry below is keyed on (iso3, a distinctive token that must appear in
that record's own text), and the script REFUSES TO WRITE ANYTHING if a token
matches no record or more than one.

Head offices come from the record's own text where it states one, else the
spelling already on the map, and are left null where no source establishes one --
build_net.py then places the party at the country centre and says so. A guessed
city puts a marker somewhere false, and the markers on this map are fixed points.

Decisions worth keeping:

* Names are qualified by country where the bare name is unique only inside its
  own country. The agent offered a bare "Ministry of Finance" for Palestine; the
  map's eight other finance ministries are all country-qualified, and a generic
  name is what collapsed four national audit offices into one diamond this round.
  "Banco Mercantil" is qualified for the same reason: the map already carries
  Bolivia's Banco Mercantil Santa Cruz, which is a different bank.
* ABN Amro, Rabobank, ING and Equity Bank already exist as nodes and are reused
  under the spelling on the map. Equity Bank's node is the Nairobi one, which is
  the same bank the South Sudan record names.
* Standard Lesotho Bank takes the name Standard Bank Group's own structure page
  prints; the central bank's board page calls it Standard Bank of Lesotho, which
  goes in name_as_stated.
* Somalia gets NO party. The source names TLG Financial Services and no source
  states what country it is in, so a node would be unplaceable; and the employers
  the record actually rests on, Citigroup and AIG, are named by the second source
  rather than by the record's own source_url, so linking them here would hang a
  party on a citation that does not name it.
* Palestine's two employers and its control bureau get no city: nothing opened
  states one. The bank's listing address appears only on third-party data sites.
* The two statutory arrangements link the office that holds the power, under the
  role round 57 added for exactly this shape. Guyana links the President, who may
  terminate the Governor's appointment; the Minister who sets exchange-rate policy
  is left unlinked because no role in the vocabulary fits directing policy rather
  than the board, and adding a role is a decision, not a side effect of a round.
  Uruguay links the Poder Ejecutivo, which may order the removal of directors.
* Uzbekistan and Canada get no party: both findings are the institution's own
  audit or disciplinary record, naming no outside body.
"""
import json
import os
import sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
L = lambda n: json.load(open(os.path.join(A, 'agents', n), encoding='utf-8'))

RD = 'employed an official before or after (revolving door)'
BOARD = "appoints or directs the bank's board"
PRESS = 'pressured, dismissed or prosecuted bank officials'
AUDIT = 'audited or investigated'

# (iso3, token) -> [(party, name_as_stated, party_type, hq_city, hq_iso3), ...]
T_RD = {
    ('HND', 'Cerrato'): [
        ('Banco Mercantil (Honduras)', 'Banco Mercantil, S.A.', 'bank', 'Tegucigalpa', 'HND'),
        ('Banco Ficohsa', 'Banco Financiera Comercial Hondureña, S.A. (Banco Ficohsa)', 'bank', 'Tegucigalpa', 'HND'),
        ('Intermediaria Financiera, S.A. (Grupo FICOHSA)', 'Intermediaria Financiera, S.A.', 'company', 'Tegucigalpa', 'HND')],
    ('GMB', 'Jabby'): [
        ('FirstBank Gambia Limited', 'FirstBank Gambia Limited', 'bank', 'Banjul', 'GMB'),
        ('First Bank of Nigeria', 'First Bank of Nigeria Limited', 'bank', 'Lagos', 'NGA')],
    ('LSO', "'Nete"): [
        ('Standard Lesotho Bank Limited', 'Standard Bank of Lesotho', 'bank', 'Maseru', 'LSO'),
        ('Stanlib', 'Stanlib', 'company', 'Maseru', 'LSO')],
    ('SLV', 'Barraza'): [
        ('Banco Agrícola', 'Banco Agrícola, S.A.', 'bank', 'San Salvador', 'SLV'),
        ('Bancolombia', 'Bancolombia S.A.', 'bank', 'Medellín', 'COL')],
    ('COD', 'Ilondo'): [
        ('Rawbank', 'Rawbank', 'bank', 'Kinshasa', 'COD')],
    ('NIC', 'Rivas'): [
        ('Banco de la Producción (Banpro)', 'Banco de la Producción, S.A. (Banpro)', 'bank', 'Managua', 'NIC'),
        ('Grupo Promerica', 'Grupo Promerica', 'company', 'Panama City', 'PAN')],
    ('ABW', 'Domhoff'): [
        ('ING', 'ING', 'bank', 'Amsterdam', 'NLD'),
        ('ABN Amro', 'ABN AMRO', 'bank', 'Amsterdam', 'NLD'),
        ('Rabobank', 'Rabobank', 'bank', 'Utrecht', 'NLD'),
        ('Banco Sicredi', 'Banco Sicredi', 'bank', 'Porto Alegre', 'BRA')],
    ('IRN', 'Seif'): [
        ('Karafarin Bank', 'the privately owned Karafarin Bank', 'bank', 'Tehran', 'IRN')],
    ('MMR', 'Than Lwin'): [
        ('Kanbawza Bank (KBZ)', 'the Kanbawza Bank', 'bank', 'Yangon', 'MMR')],
    ('MMR', 'Khin Saw Oo'): [
        ('AYA Bank', 'AYA Bank', 'bank', 'Yangon', 'MMR')],
    ('PSE', 'Shunnar'): [
        ('Palestine Islamic Bank', 'the Palestine Islamic Bank', 'bank', None, 'PSE'),
        ('Tamkeen Insurance Company', 'Tamkeen Insurance Company', 'company', None, 'PSE')],
    ('IRQ', 'al-Heims'): [
        ('Trade Bank of Iraq', 'the Trade Bank of Iraq', 'bank', 'Baghdad', 'IRQ')],
    ('BTN', 'Penjore'): [
        ('National Pension & Provident Fund of Bhutan', 'National Pension & Provident Fund', 'other', 'Thimphu', 'BTN')],
    ('SSD', 'Othow'): [
        ('Equity Bank', 'Equity Bank', 'bank', 'Nairobi', 'KEN'),
        ('Ivory Bank', 'Ivory Bank', 'bank', 'Juba', 'SSD')],
    ('SDN', 'Al-Zubair'): [
        ('Saudi Sudanese Bank', 'Saudi Sudanese Bank', 'bank', 'Khartoum', 'SDN'),
        ('Bank of Sahel and Sahara Community', 'Bank of Sahel and Sahara Community', 'bank', 'Tripoli', 'LBY')],
}

T_EV = {
    ('GUY', 'section 29'): [
        ('President of Guyana', 'the President', 'government', 'Georgetown', 'GUY', BOARD)],
    ('URY', '197'): [
        ('Government of Uruguay', 'el Poder Ejecutivo', 'government', 'Montevideo', 'URY', BOARD)],
    ('CUW', 'Gibson'): [
        ('Richard Gibson', 'the finance minister, Richard Gibson', 'person', None, None, PRESS)],
}

T_CASE = {
    ('PSE', 'Control Bureau'): [
        ('Financial and Administrative Control Bureau (Palestine)',
         'the Financial and Administrative Control Bureau', 'agency', None, 'PSE', AUDIT),
        ('Ministry of Finance of Palestine', 'the Ministry of Finance', 'government', None, 'PSE', AUDIT)],
}

FIELDS = ('people', 'move', 'summary', 'source_title', 'kind', 'category')


def find(records, iso, tok):
    hits = [i for i, r in enumerate(records)
            if (r.get('iso3') == iso)
            and tok.lower() in ' '.join(str(r.get(f) or '') for f in FIELDS).lower()]
    return hits


def main():
    dry = '--dry' in sys.argv
    cor, par = L('corruption.json'), L('parties.json')
    evg = L('events_gold.json')
    links = par['links']
    arrays = {'revolving_door': cor['revolving_door'], 'event': evg['events'], 'case': cor['cases']}
    tables = [('revolving_door', T_RD, RD), ('event', T_EV, None), ('case', T_CASE, None)]
    have = {(x.get('record_type'), x['record_index'], x['party']) for x in links}
    new, bad = [], []
    for rtype, table, fixed_role in tables:
        recs = arrays[rtype]
        for (iso, tok), parties in table.items():
            hits = find(recs, iso, tok)
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
