#!/usr/bin/env python3
"""Round 64: link the parties named in this round's new events and cases into parties.json.

merge_links.py files a record but writes NO party links -- that is a separate hand step, and a
record filed without its parties is on the map in prose and absent from every layer that counts
ties. This is the r57 pattern with one addition: besides matching exactly one record on
(iso3, date) or (iso3, years), each entry carries a TOKEN that must appear in that record's own
text. If a record has been reordered, rewritten or replaced under us, the token fails and the
script writes nothing at all rather than hanging a party on the wrong country's facts.

Eritrea's three parties: the President is named as the actor but the party node is
"Government of the State of Eritrea", which is both the convention for the eight comparable
board-appointment records (Comoros, Macao, Bhutan, Djibouti, Syria, Cabo Verde) and the
proclamation's own definition in Article 2(13). The Ministry of Finance and the Auditor General
are country-qualified because round 60 had to split three generic audit-office nodes that were
silently merging four countries' institutions into one diamond.
"""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
L = lambda n: json.load(open(os.path.join(A, n), encoding='utf-8'))
BOARD = "appoints or directs the bank's board"
SITS  = 'sits on the board'
INVEST = 'audited or investigated'
PRESS = 'pressured, dismissed or prosecuted bank officials'
FUND = "directs the bank's management of a state fund"  # new at round 64, with its SAY and REL entries

# (iso3, date) -> (token that must appear in the record, [(party, name_as_stated, type, city, iso3, role)])
EV = {
 ('TLS', '2011-09-28'): ('Artigo 11', [
    ('Government of Timor-Leste', 'the Government', 'government', 'Dili', 'TLS', FUND),
    ('Ministry of Finance of Timor-Leste', 'the Minister of Finance', 'government', 'Dili', 'TLS', FUND)]),
 ('MKD', '2025-01'): ('16/25', [
    ('Assembly of the Republic of North Macedonia', 'a group of members of the Assembly',
     'government', 'Skopje', 'MKD', PRESS)]),
 ('ERI', '1997-01-21'): ('Proclamation 93/1997', [
    ('Government of the State of Eritrea', 'the President of the State of Eritrea', 'government', 'Asmara', 'ERI', BOARD),
    ('Ministry of Finance of Eritrea', 'a representative of the Ministry of Finance', 'government', 'Asmara', 'ERI', SITS),
    ('Auditor General of Eritrea', 'the Auditor General', 'agency', 'Asmara', 'ERI', SITS)]),
}
# (iso3, years) -> same
CS = {}

def main():
    dry = '--dry' in sys.argv
    cor, evg, par = L('corruption.json'), L('events_gold.json'), L('parties.json')
    ev, cs, links = evg['events'], cor['cases'], par['links']
    have = {(x['record_type'], x['record_index'], x['party']) for x in links}
    new, bad = [], []
    for rows, key_of, rtype, table in ((ev, lambda r: (r['iso3'], str(r.get('date'))), 'event', EV),
                                       (cs, lambda r: (r['iso3'], str(r.get('years'))), 'case', CS)):
        for k, (token, parties) in table.items():
            hits = [i for i, r in enumerate(rows) if key_of(r) == k]
            if len(hits) != 1:
                bad.append(f'{rtype} {k}: matched {len(hits)} records, expected 1'); continue
            idx = hits[0]
            blob = json.dumps(rows[idx], ensure_ascii=False)
            if token not in blob:
                bad.append(f'{rtype} {k}: token {token!r} is not in the matched record -- '
                           'the record has changed or the index has moved'); continue
            for party, stated, ptype, city, iso, role in parties:
                if (rtype, idx, party) in have: continue
                new.append({'party': party, 'name_as_stated': stated, 'party_type': ptype, 'parent': None,
                            'hq_city': city, 'hq_iso3': iso, 'cb_iso3': rows[idx]['iso3'], 'role': role,
                            'record_type': rtype, 'record_index': idx,
                            'source_url': rows[idx].get('source_url')})
    if bad:
        print('REFUSED, nothing written:'); [print('  ' + b) for b in bad]; sys.exit(1)
    print(f'{len(new)} new party links')
    for x in new:
        print(f'  {x["record_type"]:6s}[{x["record_index"]:3d}] {x["cb_iso3"]}  {x["party"][:52]:54s} {x["role"]}')
    if dry: print('\n(dry run; nothing written)'); return
    par['links'] = links + new
    json.dump(par, open(os.path.join(A, 'parties.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'\nwritten: parties.json now holds {len(par["links"])} links')

main()
