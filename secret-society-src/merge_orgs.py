#!/usr/bin/env python3
"""Combine organisation files into data/orgs.json.

    python3 merge_orgs.py <research_dir>

Sources: research/orgs.json (round 1), research/r2/*_orgs.json and *_channels.json
(round 2). Any organisation key used by a case but described nowhere gets a short entry
built from the case's own org_note, located at its earliest case, with its reach set to
the countries where it has cases.
"""
import json, os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
TY = {'freemasonry':'lodge','prc_state':'statenet','ndrangheta_masonry':'lodge','koreagate':'statenet','orange_order':'lodge',
 'knights_columbanus':'order','voice_of_europe':'statenet','p3':'lodge','p4':'lodge','idea_gr':'lodge','golden_dawn':'covert',
 'osti':'order','shinseiren':'order','colonia_dignidad':'order','foreign_state':'statenet','white_supremacist':'lodge',
 'know_nothing':'lodge','tammany':'lodge','jacques_cartier':'lodge','sac_fr':'covert','oas':'covert','westland_new_post':'covert',
 'reichsbuerger_reuss':'covert','asekatkenta':'covert','ib_sweden':'covert','white_hand':'lodge'}
NAME = {'freemasonry':'Freemasonry (other grand lodges)','prc_state':'PRC state proxies (United Front not named)',
 'ndrangheta_masonry':'Mafia-linked "covered" lodges','koreagate':'KCIA / Tongsun Park network','orange_order':'Loyal Orange Institution',
 'knights_columbanus':'Knights of Saint Columbanus','voice_of_europe':'Voice of Europe network','p3':'P3 association','p4':'P4 network',
 'idea_gr':'IDEA (Sacred Bond of Greek Officers)','golden_dawn':'Golden Dawn','osti':'Sovereign Order of the Initiatic Temple (OSTI)',
 'shinseiren':'Shinto Seiji Renmei','colonia_dignidad':'Colonia Dignidad','foreign_state':'State influence networks (several states)',
 'white_supremacist':'Organised white supremacist groups','know_nothing':'Order of the Star Spangled Banner (Know Nothings)',
 'tammany':'Society of St. Tammany','jacques_cartier':'Ordre de Jacques-Cartier','sac_fr':"Service d'Action Civique (SAC)",
 'oas':'Organisation armée secrète (OAS)','westland_new_post':'Westland New Post','reichsbuerger_reuss':'Reuss "Patriotic Union" (Reichsbürger)',
 'asekatkenta':'Weapons Cache network (Asekätkentä)','ib_sweden':'Informationsbyrån (IB)','white_hand':'White Hand (Bela ruka)'}

def main(rdir):
    base = json.load(open(os.path.join(rdir, 'orgs.json')))
    orgs, chans = base['orgs'], base['channels']
    for f in sorted(glob.glob(os.path.join(rdir, 'r2', '*_orgs.json'))) + sorted(glob.glob(os.path.join(rdir, 'r3', '*_orgs.json'))):
        for o in json.load(open(f)):
            if o['k'] in {x['k'] for x in orgs}:
                ex = next(x for x in orgs if x['k'] == o['k'])
                ex['reach'] = sorted(set(ex.get('reach', [])) | set(o.get('reach', [])))
                continue
            orgs.append(o)
    for f in sorted(glob.glob(os.path.join(rdir, 'r2', '*_channels.json'))) + sorted(glob.glob(os.path.join(rdir, 'r3', '*_channels.json'))):
        chans += json.load(open(f))
    for o in orgs:
        if o['k'] == 'wacl':
            o['c'], o['lat'], o['lng'] = 'Taiwan', 25.033, 121.565
    cases = json.load(open(os.path.join(HERE, 'data', 'cases.json')))
    ok = {x['k'] for x in orgs}
    by = {}
    for x in cases:
        if x['org'] not in ok: by.setdefault(x['org'], []).append(x)
    for k, cs in by.items():
        first = sorted(cs, key=lambda z: z['y'])[0]
        note = next((z.get('org_note') for z in cs if z.get('org_note')), '') or ''
        note = re.sub(r'^\s*(New key:\s*)?[a-z_]+\s*(=|:)\s*', '', note).strip()
        if k == 'freemasonry':
            note = 'Regular and irregular Masonic grand lodges not tracked separately on this map. Each case names the lodge involved.'
            hq, cn, lat, lng = 'London — first grand lodge, 1717; each country has its own grand lodges', 'United Kingdom', 51.515, -0.121
        else:
            hq, cn, lat, lng = first.get('city', ''), first['c'], first['lat'], first['lng']
        orgs.append({'k': k, 'n': NAME.get(k, first.get('org_label', k)), 'ty': TY.get(k, 'lodge'), 'hq': hq, 'c': cn, 'lat': lat, 'lng': lng,
                     'founded': '', 'status': '', 'd': (note[0].upper() + note[1:]) if note else NAME.get(k, k),
                     'cite': 'See the cases listed below.', 'reach': sorted({z['c'] for z in cs}),
                     'reach_src': 'countries where this map holds a documented case', 'reach_est': []})
        if k not in NAME: print('  check new org key:', k, '->', orgs[-1]['n'], orgs[-1]['ty'])
    json.dump({'orgs': orgs, 'channels': chans}, open(os.path.join(HERE, 'data', 'orgs.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(orgs), 'orgs,', len(chans), 'channels')

if __name__ == '__main__':
    main(sys.argv[1])
