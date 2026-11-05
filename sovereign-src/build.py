#!/usr/bin/env python3
"""Build ../outside_every_country.html from research JSON, the odds, patterns and about text.
python3 build.py [research_dir]   Research files: ocean, land, space, zones, entails, figures, sites and fix_*.json"""
import json,os,sys,base64,re
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(HERE,'content'))
from odds import ODDS,BANDS,EXTRA_ZONES
from patterns import PATTERNS
from about import ABOUT,METHOD
R=sys.argv[1] if len(sys.argv)>1 else os.path.join(HERE,'data','research')
J=lambda n:json.load(open(os.path.join(R,n+'.json'),encoding='utf8'))
def fix(recs,fname):
    p=os.path.join(R,fname+'.json')
    if not os.path.exists(p):return 0
    n=0;by={}
    for r in recs:by.setdefault(r['id'],[]).append(r)
    for x in json.load(open(p,encoding='utf8')):
        for r in by.get(x['id'],[]):
            f=x['field']
            if f=='sources':
                n_=x.get('new') or x.get('source')
                if isinstance(n_,dict) and n_.get('u') and not any(q['u']==n_['u'] for q in r['sources']): r['sources'].append(n_)
                continue
            if f not in r:continue
            v=r[f]
            if isinstance(v,str) and isinstance(x.get('old'),str) and x['old'] and x['old'] in v:
                r[f]=v.replace(x['old'],x['new']);n+=1
            elif not isinstance(v,str) or x.get('old') in (None,''): r[f]=x['new'];n+=1
            elif str(v)==str(x.get('old')): r[f]=x['new'];n+=1
            else: print('FIX MISS',x['id'],f,str(x.get('old'))[:60])
            s=x.get('source')
            if isinstance(s,str):s={'t':s,'u':s} if s.startswith('http') else None
            if s and s.get('u') and not any(q['u']==s['u'] for q in r['sources']): r['sources'].append(s)
    return n
ocean,land,space=J('ocean'),J('land'),J('space')
print('fixes',fix(ocean,'fix_ocean'),fix(land,'fix_land'),fix(land,'fix_land2'),fix(space,'fix_space'),fix(space,'fix_space2'))
for r in ocean:r['_f']='o'
for r in land:r['_f']='l'
for r in space:r['_f']='s'
def jl(n):
    p=os.path.join(R,n+'.json');return json.load(open(p,encoding='utf8')) if os.path.exists(p) else None
extra_zones=[];extra=[]
for n in('water','routes','beyond'):
    d=jl(n);extra_zones+=d['zones'];extra+=d['cases']
extra=[c for c in extra if c['id'] not in('bakov-russian-empire',)]
_seen=set();_e=[]
for c in extra:
    if c['id'] in _seen:continue
    _seen.add(c['id']);_e.append(c)
extra=_e+(jl('routes2') or [])+(jl('purchase') or [])+(jl('purchase2') or [])+(jl('gap1') or [])+(jl('gap2') or [])
combo_zones=[]
for n in('combo_sea','combo_space','combo_land','combo_people'):
    d=jl(n)
    if d:
        _seenz={z['id'] for z in combo_zones}
        for z in d['zones']:
            z['_band']={'combo_sea':'Combinations: sea and ice','combo_space':'Combinations: air and space','combo_land':'Combinations: land and legal status','combo_people':'Combinations: people, money and paper'}[n]
            if z['id'] not in _seenz:combo_zones.append(z)
        extra+=d['cases']
DROP={'space':{'dominion-of-melchizedek','aerican-empire','praxis','zuzalu','sovereign-order-of-malta','talossa'}}
space=[r for r in space if r['id'] not in DROP['space']]
fix(extra,'fix_routes');fix(extra,'fix_other');fix(extra,'fix_purchase')
_seen_c=set();extra=[c for c in extra if not (c['id'] in _seen_c or _seen_c.add(c['id']))]
for c in extra:
    c['status']=c.get('status') or 'dormant'
    if c['id']=='migingo-island':c['status']='operating';c['end']=None;c['stopped_by']=None
cases=ocean+land+space
# zone assignment
ZMAP={'high-seas':'high-seas','territorial-eez':'eez-shelf','reef-seamount':'reefs-low-tide-elevations','platform':'abandoned-platforms','ship-flag':'ships-flag','seabed-undersea':'deep-seabed-area','disputed-islands':'disputed-islands','terra-nullius':'terra-nullius-land','antarctica-unclaimed':'antarctica-unclaimed','antarctica-claimed':'antarctica-claimed','arctic':'central-arctic-ocean-and-svalbard','inside-state':'inside-state','carve-out':'host-state-carve-outs','unrecognised-state':'unrecognised-state','non-territorial':'digital-no-territory','airspace':'airspace-over-states','stratosphere':'stratosphere-near-space','leo':'leo','geo':'geo','moon':'moon','mars':'mars-and-beyond','asteroids':'asteroids','lagrange':'lagrange-cislunar','digital':'digital-no-territory'}
ZOVER={'floating-island-french-polynesia':'territorial-sea','seapods-panama':'territorial-sea','oceanix-busan':'territorial-sea','aquarius-reef-base':'undersea-water-column','deep-vanguard-sentinel':'undersea-water-column','proteus-curacao':'undersea-water-column','ocean-spiral':'undersea-water-column','abaco':'inside-state','vemerana':'inside-state','coral-sea-kingdom':'inside-state','minerva-1982-and-fiji-tonga':'reefs-low-tide-elevations','kingdom-of-araucania-patagonia':'inside-state','kingdom-of-sedang':'inside-state','republic-of-madawaska':'inside-state','adiz-high-seas':'airspace-over-high-seas','tokyo-convention-aircraft-flag':'airspace-over-high-seas','dominion-of-melchizedek':'digital-no-territory','zuzalu':'inside-state'}
SKY={'venus-clouds','outer-moons','the-sun','interstellar-ships','orbital-megastructures','airborne-habitats','mars-and-beyond','asteroids','moon','lagrange-cislunar','geo','leo','stratosphere-near-space','airspace-over-high-seas','airspace-over-states'}
SEA={'inland-waters','new-land','floating-ice','ships-flag','high-seas','central-arctic-ocean-and-svalbard','eez-shelf','territorial-sea','reefs-low-tide-elevations','abandoned-platforms','disputed-islands','undersea-water-column','deep-seabed-area'}
LAW=set("clipperton-arbitration island-of-palmas sapodilla-cayes antarctic-claims-article-iv svalbard-treaty arktika-2007-flag hans-island eastern-greenland-case us-v-causby chicago-convention tokyo-convention-aircraft-flag adiz-high-seas china-balloon-2023 karman-line-debate loon-stratosphere iss-intergovernmental-agreement flags-of-convenience-space fcc-starlink-licensing swarm-spacebees-fcc kessler-limits artemis-accords ilrs moon-agreement for-all-moonkind unreal-estate-pop us-space-act-2015 luxembourg-space-resources-2017 uae-japan-space-resources international-seabed-authority sea-shepherd-piracy aquarius-reef-base deep-vanguard-sentinel proteus-curacao nansen-passport barlow-declaration tuvalu-digital-nation estonia-e-residency estonia-data-embassy second-life-embassies orbis-lease-salter moon-express-faa mcclean-rockall villa-las-estrellas esperanza-base-births arctic-sanctuary-greenpeace-flag t3-ice-island-escamilla ms-the-world starlink-mars-free-planet yemeni-mars-suit lonestar-lunar-data metals-company ocean-spiral bogota-declaration tongasat ss-rex-gambling-ships moon-agreement vast-haven-1 nasa-commercial-stations voyager-station".split())
ATTEMPT_KEEP={'bogota-declaration','tongasat','vast-haven-1','voyager-station','nasa-commercial-stations','ss-rex-gambling-ships'}
LAW-=ATTEMPT_KEEP
OUT={'operating':'going','dormant':'faded','forced-out':'stopped','court-defeated':'stopped','absorbed':'stopped','collapsed':'faded','never-built':'never','fraud':'fraud'}
OOVER={'prospera-zede':'going','network-state-school':'going','zad-notre-dame-des-landes':'stopped','ss-rex-gambling-ships':'stopped'}
HELD=set("sealand radio-caroline women-on-waves neutral-moresnet republic-of-cospaia couto-misto kowloon-walled-city freetown-christiania frestonia order-of-malta somaliland transnistria taiwan northern-cyprus wa-state zapatista-territories akhzivland cheran vatican-lateran-treaty conch-republic prospera-zede republic-of-kugelmugel ladonia".split())
RECD={'order-of-malta','vatican-lateran-treaty','somaliland','northern-cyprus','taiwan'}
seen=set();out=[]
for r in cases:
    assert r['id'] not in seen,r['id'];seen.add(r['id'])
    r['zid']=ZOVER.get(r['id'],ZMAP[r['zone']])
    z=r['zid'];r['group']='sky' if z in SKY else 'sea' if z in SEA else 'none' if z=='digital-no-territory' else 'land'
    r['kind']='law' if r['id'] in LAW else 'attempt'
    r['out']='law' if r['kind']=='law' else OOVER.get(r['id'],OUT[r['status']])
    r['held']=r['id'] in HELD;r['recd']=r['id'] in RECD
    r['body']='earth'
    r.setdefault('aka',[])
    if r['id'] in('moon-express-faa',):pass
    for k in('currency','passports','laws','stopped_by','pop','challenge','recognition','cost'):
        if r.get(k) in('None','none','-'):r[k]=None
    if r['start'] and r['start']<1000:pass
    for k in('zone','_f','status'):r.pop(k,None)
    out.append(r)
for c in out:
    if c['id']=='rose-island' and c.get('challenge'):c['challenge']=c['challenge'].replace('after 55 days','after eight weeks')
MAN={'province-of-bumbunga':{'founder':'Alec Brackstone'},'zaqistan':{'founder':'Zaq Landsberg'},'viking-1':{'loc':'approx'},'global-country-of-world-peace':{'lat':41.01,'lon':-91.96,'loc':'approx','plat':41.01,'plon':-91.96},'kingdom-of-sedang':{'end':1890},'republic-of-madawaska':{'end':1827},'republic-of-lakotah':{'inhabited':True},'kingdom-of-elleore':{'currency':'Stamps and coins issued'}}
for c in out:
    c.update(MAN.get(c['id'],{}))
    if c['id']=='republic-of-indian-stream':c['mechanism']=c['mechanism'].replace('without a shot','without a shot that August, though a deputy was shot that October')
# hardware sites on the Moon and Mars
p=os.path.join(R,'sites.json')
if os.path.exists(p):
    for s in json.load(open(p,encoding='utf8')):
        if s['id'] in seen:continue
        out.append(dict(s,zid='moon' if s['body']=='moon' else 'mars-and-beyond',group='sky',kind='law',out='law',held=False,recd=False,built=True,inhabited=False,aka=[],currency=None,passports=None,laws=None,stopped_by=None,pop=None,challenge=None,recognition=None,cost=None,mechanism=None))
# spread coincident pins
pos={}
for c in out:
    if c.get('lat') is None:continue
    k=(c['body'],round(c['lat'],1),round(c['lon'],1));n=pos.get(k,0);pos[k]=n+1
    import math
    a=n*2.4;d=.09*math.sqrt(n)
    c['plat']=round(c['lat']+d*math.sin(a),4);c['plon']=round(c['lon']+d*math.cos(a),4)
# new records keep their own zid, kind and flags
for c in extra:
    c.pop('band',None)
    _g=c.get('group')
    c['group']=_g if _g in('sea','land','sky','none') else 'sky' if c['zid'] in SKY else 'sea' if c['zid'] in SEA else 'none' if c['zid'] in('digital-no-territory','no-territory-conceptual','exile-and-landless-authority') else 'land'
    c['out']='law' if c['kind']=='law' else OUT[c['status']]
    c['held']=bool(c.get('held'));c['recd']=bool(c.get('recd'));c['body']='earth';c['built']=bool(c.get('built'));c['inhabited']=bool(c.get('inhabited'))
    for k in('currency','passports','laws','stopped_by','pop','challenge','recognition','cost'):
        if c.get(k) in('None','none','-'):c[k]=None
    if c['id'] not in seen:
        seen.add(c['id']);out.append(c)
for c in out:
    if c.get('lat') is None or 'plat' in c:continue
    k=(c['body'],round(c['lat'],1),round(c['lon'],1));n=pos.get(k,0);pos[k]=n+1
    a=n*2.4;d=.09*math.sqrt(n)
    c['plat']=round(c['lat']+d*math.sin(a),4);c['plon']=round(c['lon']+d*math.cos(a),4)
# plain-language rewrites
_by={c['id']:c for c in out}
for n in range(1,30):
    rw=jl('rw%d'%n) or {}
    for i,r in rw.items():
        c=_by.get(i)
        if not c:continue
        for k,v in r.items():
            if k in('why',):continue
            if k=='add_sources':
                for q in v:
                    if q.get('u') and not any(x['u']==q['u'] for x in c['sources']):c['sources'].append(q)
            elif k=='set':
                c.update(v)
                if 'status' in v and c['kind']!='law':c['out']=OOVER.get(i,OUT[v['status']])
                if 'lat' in v or 'lon' in v:c['plat'],c['plon']=c['lat'],c['lon']
            else:c[k]=v
for c in out:
    if c.get('lat') is not None and 'plat' not in c:c['plat'],c['plon']=c['lat'],c['lon']
for i,r in (jl('review') or {}).get('cases',{}).items():
    if i in _by:_by[i]['story']=r['story']
for _n in('left','close'):
    for i,r in (jl(_n) or {}).get('entries',{}).items():
        c=_by.get(i)
        if not c:print('NO ENTRY',_n,i);continue
        for k,v in r.items():
            if k=='add_sources':
                for q in v:
                    if q.get('u') and not any(x['u']==q['u'] for x in c['sources']):c['sources'].append(q)
            elif k=='drop_sources':c['sources']=[x for x in c['sources'] if x['u'] not in v]
            elif k=='set':
                c.update(v)
                if 'status' in v and c['kind']!='law':c['out']=OOVER.get(i,OUT[v['status']])
                if 'lat' in v or 'lon' in v:c['plat'],c['plon']=c['lat'],c['lon']
            else:c[k]=v
for c in out:
    if c['id']=='state-to-state-purchases':c['story']=c['story'].replace('on this list since 1958','in that list since 1958')
for c in out:
    if c['id']=='peanut-hole-okhotsk' and c.get('recognition'):c['recognition']=c['recognition'].replace('ruled for Russia','recommended in favour of Russia')
    if c['id']=='tiran-sanafir':c['end']=None
    if c['id'] in('peanut-hole-okhotsk','viking-1','province-of-bumbunga','zaqistan'):c.update(MAN.get(c['id'],{}))
    if c['id']=='rose-island':
        for k in('story','challenge','mechanism'):
            if c.get(k):c[k]=c[k].replace('55 days','about eight weeks')
    if c['id']=='hans-island' and not any('British_Arctic' in q['u'] for q in c['sources']):c['sources'].append({'t':'British Arctic Territories (Wikipedia)','u':'https://en.wikipedia.org/wiki/British_Arctic_Territories'})
    if c['id']=='hans-island':c['story']=c['story'].replace("the 1880 transfer of the Hudson's Bay Company's lands to Canada","the transfer of Britain's Arctic islands to Canada in 1880")
def cleansrc(l):
    o=[]
    for q in l or []:
        for u in str(q.get('u','')).split(' ; '):
            u=u.strip()
            if not u:continue
            t=q.get('t') or u
            if t.startswith('http'):t=re.sub(r'^https?://(www\.)?','',t).split('/')[0]
            if not any(x['u']==u for x in o):o.append({'t':t,'u':u})
    return o
for c in out:c['sources']=cleansrc(c.get('sources'))
def paras(t,n=65):
    if '\n\n' in str(t or ''):return '\n'.join(x.strip() for x in str(t).split('\n\n') if x.strip())
    t=' '.join(str(t or '').split());out_=[];cur=[];w=0
    parts=re.split(r'(?<=[.!])\s+(?=[A-Z0-9])',t);merged=[]
    for x in parts:
        if merged and re.search(r"(\b(Art|Arts|St|Mr|Mrs|Ms|Dr|Prof|Sgt|Capt|Gen|Col|Lt|No|vs|v|Inc|Co|Ltd|Jr|Sr|Rev|Hon|Mt|Ft|c|ca|U\.S|e\.g|i\.e)\.|\b[A-Z]\.)$",merged[-1]):merged[-1]+=' '+x
        else:merged.append(x)
    for x in merged:
        cur.append(x);w+=len(x.split())
        if w>=n:out_.append(' '.join(cur));cur=[];w=0
    if cur:
        if out_ and w<20:out_[-1]+=' '+' '.join(cur)
        else:out_.append(' '.join(cur))
    return '\n'.join(out_)
for c in out:c['story']=paras(c.get('story'))
# zones
zs={z['id']:z for z in J('zones')}
for z in combo_zones:zs[z['id']]=z
for z in extra_zones:
    z.pop('band',None);zs[z['id']]=z
pf=jl('fix_routes') or [];pf2=jl('fix_other') or []
for x in pf+pf2:
    f=x.get('field','')
    if not f.startswith('zone:'):continue
    o=zs.get(x['id'])
    if not o:continue
    m=re.match(r'zone:(\w+)(?:\[(\d+)\])?(?:\.(\w+))?$',f)
    if not m:continue
    a,i,sub=m.groups();cont=o;key=a
    if a=='sources':
        n_=x.get('new') or x.get('source')
        if isinstance(n_,dict) and n_.get('u') and not any(q['u']==n_['u'] for q in o['sources']):o['sources'].append(n_)
        continue
    if i is not None:
        cont=o[a];key=int(i)
        if sub:cont=cont[key];key=sub
    try:
        if x['old'] in cont[key]:cont[key]=cont[key].replace(x['old'],x['new'])
        else:print('ZFIX MISS',x['id'],f)
    except Exception as e:print('ZFIX ERR',x['id'],f,e)
    s_=x.get('source')
    if s_ and s_.get('u') and not any(q['u']==s_['u'] for q in o['sources']):o['sources'].append(s_)
for e in EXTRA_ZONES:zs[e['id']]=e
class _:pass
ent=J('entails')
pz=os.path.join(R,'fix_zones.json')
if os.path.exists(pz):
    n=0
    for x in json.load(open(pz,encoding='utf8')):
        pool=zs if x['file']=='zones' else {e['id']:e for e in ent}
        o=pool.get(x['id']);
        if not o:continue
        m=re.match(r'(\w+)(?:\[(\d+)\])?(?:\.(\w+))?$',x['path']);f,i,sub=m.groups()
        cont=o;key=f
        if i is not None:
            cont=o[f];key=int(i)
            if sub:cont=cont[key];key=sub
        try:
            v=cont[key]
            if x['old'] in v:cont[key]=v.replace(x['old'],x['new']);n+=1
            else:print('ZFIX MISS',x['id'],x['path'])
        except Exception as e:print('ZFIX ERR',x['id'],x['path'],e)
        s=x.get('source')
        if s and s.get('u') and not any(q['u']==s['u'] for q in o['sources']):o['sources'].append(s)
    print('zone fixes',n)
for z in zs.values():
    z['facts']=[f.replace('What the AI claim omitted: (1)','Common summaries say the country below owns the air. That leaves out: (1)') for f in z.get('facts',[]) if not f.startswith('Note on the AI')]
rwz=jl('rw_zones') or {'zones':{},'entails':{}}
for i,r in rwz['zones'].items():
    if i in zs:
        for k,v in r.items():
            if v not in(None,''):zs[i][k]=v
for e in ent:
    for k,v in rwz['entails'].get(e['id'],{}).items():
        if k=='figure' or v not in(None,''):e[k]=v
for n in range(1,6):
    for i,r in (jl('essays%d'%n) or {}).items():
        if i in zs:
            zs[i]['essay']=r['essay']
            for q in r.get('add_sources',[]):
                if q.get('u') and not any(x['u']==q['u'] for x in zs[i]['sources']):zs[i]['sources'].append(q)
_rev=jl('review') or {}
for i,r in _rev.get('essays',{}).items():
    if i in zs:
        zs[i]['essay']=r['essay']
        for q in r.get('add_sources',[]):
            if q.get('u') and not any(x['u']==q['u'] for x in zs[i]['sources']):zs[i]['sources'].append(q)
for _n in('review1','review2','cr1','cr2','cr3'):
    for i,r in (jl(_n) or {}).get('essays',{}).items():
        if i in zs:
            zs[i]['essay']=r['essay']
            for q in r.get('add_sources',[]):
                if q.get('u') and not any(x['u']==q['u'] for x in zs[i]['sources']):zs[i]['sources'].append(q)
_e2=dict(jl('entails2') or {})
for i,r in _rev.get('entails',{}).items():
    _e2[i]={'what':r['what'],'add_sources':(_e2.get(i,{}).get('add_sources',[])+r.get('add_sources',[]))}
for e in ent:
    r=_e2.get(e['id'])
    if r:
        e['what']=r['what']
        for q in r.get('add_sources',[]):
            if q.get('u') and not any(x['u']==q['u'] for x in e['sources']):e['sources'].append(q)
_cons=jl('consistency') or {}
OWN=jl('own') or {}
COV=jl('coverage') or {}
SHORT=open(os.path.join(HERE,'content','short.html')).read() if os.path.exists(os.path.join(HERE,'content','short.html')) else ''
for i,e_ in _cons.get('essays',{}).items():
    if i in zs:zs[i]['essay']=e_
zones=[]
for b,ids in BANDS:
    for i in ids:
        z=zs[i];a=ODDS[i];z['band']=b;z['odds']=dict(build=a[0],law=a[1],money=a[2],hold=a[3],recog=a[4],why=(jl('odds_new') or {}).get(i,a[5]));zones.append(z)
for z in combo_zones:
    o=z['odds'];z['band']=z.pop('_band');z.setdefault('who_owns','');z.setdefault('hook','');z.setdefault('can_you_build','');z.setdefault('facts',[]);zones.append(z)
for z in zones:
    if z['id'] in _cons.get('odds_why',{}):z['odds']['why']=_cons['odds_why'][z['id']]
    _o=OWN.get(z['id']);
    if _o:z['odds'].update(own=_o['own'],own_people=_o.get('own_people'),own_why=_o['own_why'])
    else:z['odds'].update(own=0,own_people=None,own_why='');print('NO OWN',z['id'])
assert len(zones)==len(zs),set(zs)-{z['id'] for z in zones}
for c in out:assert c['zid'] in zs,c['id']
ZID={z['id'] for z in zones};ids={c['id'] for c in out}
PATTERNS=jl('patterns_final') or jl('patterns_new') or PATTERNS
for p_ in PATTERNS:
    miss=[i for i in p_['cases'] if i not in ids]
    if miss:print('pattern missing',p_['id'],miss)
    p_['cases']=[i for i in p_['cases'] if i in ids]
# charts
att=[c for c in out if c['kind']=='attempt']
open_z=(SEA|SKY|{'terra-nullius-land','antarctica-unclaimed','antarctica-claimed'})-{'inland-waters'}
own=[c for c in att if c['zid'] in open_z]
assert not [c for c in own if c['recd']]
ST={
 'Navy, troops or police':"migingo-island denard-comoros seychelles-1981-coup wonga-coup-equatorial-guinea operation-red-dog-dominica biafra-1967 assange-ecuador-embassy rose-island rem-island minerva minerva-1982-and-fiji-tonga operation-atlantis xlii-seastead-phuket vemerana liberland free-republic-of-verdis kingdom-of-sedang kingdom-of-araucania-patagonia wrangel-island-expedition republic-of-indian-stream freedomland-kalayaan principality-of-trinidad republic-of-artsakh rojava occupation-of-alcatraz capitol-hill-occupied-protest republic-of-texas-group republic-of-madawaska",
 'Court ruling':"catalonia-2017 cyberbunker knock-john-radio-essex radio-390-red-sands grand-capri-atlantis-isle-of-gold forvik nemitz-eros tongasat prospera-zede",
 'New law aimed at them':"radio-caroline rem-island ss-rex-gambling-ships",
 'Regulator or fraud case':"new-utopia kingdom-of-enenkio dominion-of-melchizedek network-state-school",
 'Host government withdrew':"floating-island-french-polynesia akon-city bitcoin-city prospera-zede",
 'Treaty or deal between neighbours':"neutral-moresnet republic-of-cospaia couto-misto no-mans-land-cimarron-territory kowloon-walled-city free-state-of-bottleneck kingdom-of-enclava",
}
fv={x['label']:x for x in J('figures')}
def F(l):return fv[l]
treat=[("UN members","UN member States"),("UNCLOS (law of the sea)","UNCLOS parties"),("Outer Space Treaty","Outer Space Treaty parties"),("BBNJ (high-seas nature treaty)","BBNJ Agreement parties"),("Liability Convention","Liability Convention parties"),("Artemis Accords","Artemis Accords signatories"),("Registration Convention","Registration Convention parties"),("Antarctic Treaty","Antarctic Treaty parties"),("Svalbard Treaty","Svalbard Treaty parties"),("Moon Agreement","Moon Agreement parties")]
orb=[("Vanguard, 1957","Launch cost to LEO, Vanguard (1957)",1000),("Space Shuttle, 1981","Launch cost to LEO, Space Shuttle (1981)",1000),("Ariane 5G, 1996","Launch cost to LEO, Ariane 5G (1996)",1000),("Soyuz, 1966","Launch cost to LEO, Soyuz (1966)",1000),("Saturn V, 1968","Launch cost to LEO, Saturn V (1968)",1000),("Falcon 9, 2010","Launch cost to LEO, Falcon 9 (2010)",1000),("Falcon Heavy, 2018","Launch cost to LEO, Falcon Heavy (2018)",1000)]
def m(v):
    if v>=1e9:return '$%g bn'%(v/1e9)
    if v>=1e6:return '$%g m'%(v/1e6)
    if v>=1e3:return '$%s'%format(int(v),',')
    return '$%g'%v
costs=[("Freedom Ship, reported",16e9,"Freedom Ship reported cost"),("Pangeos floating city, estimate",8e9,"Pangeos estimated cost"),("ISS, per year",3e9,"ISS annual cost"),("Shuttle, per launch",1.5e9,"Shuttle cost per launch"),("Haven-1, spent so far",1e9,"Haven-1 committed spending"),("Oceanix Busan, higher figure",627e6,"Oceanix Busan, at $10,000 per m²"),("Launch insurance cap",5e8,"Launch third-party insurance cap"),("Starship launch, as reported",9e7,"Starship dedicated launch for Starlab"),("Falcon 9 launch, 2026",74e6,"Falcon 9 dedicated launch, early 2026"),("Seat on a trip to the ISS",55e6,"Axiom seat price to ISS"),("Small deep-sea platform",5e7,"Small deep-sea platform"),("New Utopia actually raised",24000,"New Utopia raised"),("US renunciation fee",450,"US renunciation fee, current")]
for c in costs:assert c[2] in fv,c[2]
hr=sum(1 for c in own)
charts=dict(cover=dict(n='0 of %d'%hr,t="attempts on open sea, ice, reefs, seabed, unclaimed land, in the air or in space have been recognised as a state by any UN member. Recognition went to %d others: mostly peoples on land they already held, through secession or war, older bodies such as the Vatican and the Order of Malta, and three private land deals made before 1900."%sum(1 for c in att if c['recd'])),
 farcap="Laws and courts appear on paper more often than people live on the ground. Recognition means by at least one UN member. None of those recognised began on open sea, ice or in space.",
 endcap="Laws, treaties and court tests are left out of this count.",
 stoppers=[dict(l=k,ids=[i for i in v.split() if i in ids]) for k,v in ST.items()],
 treaties=[dict(label=a,value=F(b)['value'],note=F(b)['note']+'.') for a,b in treat],
 orbit=sorted([dict(label=a,value=int(F(b)['value']*k),note='In 2018 dollars, at full payload (Jones).') for a,b,k in orb],key=lambda x:-x['value']),
 costs=[dict(label=a,value=b,s=m(b),note=F(c)['note']+'. '+F(c)['source']['t']) for a,b,c in costs])
data=dict(cases=out,zones=zones,entails=ent,patterns=PATTERNS,geo=json.load(open(os.path.join(HERE,'data','zones.geojson'))),charts=charts,short=SHORT,coverage=COV,about=ABOUT,method=METHOD.replace('__NA__',str(len(att))).replace('__NL__',str(len(out)-len(att))).replace('__NS__',str(len({s['u'] for c in out for s in c['sources']}|{s['u'] for z in zones for s in z['sources']}|{s['u'] for e in ent for s in e['sources']}))))
for f in data['geo']['features']:
    if f['properties']['zone']=='central-arctic':f['properties']['zone']='central-arctic-ocean-and-svalbard'
if os.environ.get('DUMP_ALL'):
    json.dump({'cases':out,'zones':zones,'entails':ent},open(os.environ['DUMP_ALL'],'w',encoding='utf8'),ensure_ascii=False,indent=0)
def b64(p):return 'data:image/webp;base64,'+base64.b64encode(open(p,'rb').read()).decode()
t=open(os.path.join(HERE,'app_template.html'),encoding='utf8').read()
t=t.replace('__PLATE__',b64(os.path.join(HERE,'data','plate.webp'))).replace('__MOON__',b64(os.path.join(HERE,'data','moon.webp'))).replace('__MARS__',b64(os.path.join(HERE,'data','mars.webp')))
t=t.replace('__BASEMAPS__',open(os.path.join(HERE,'basemaps.js'),encoding='utf8').read())
t=t.replace('__DATA__',json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
o=os.path.join(HERE,'..','outside_every_country.html');open(o,'w',encoding='utf8').write(t)
print(len(att),'attempts',len(out)-len(att),'law',len(zones),'zones',len(ent),'needs',len(own),'open-zone attempts',os.path.getsize(o)//1024,'KB')
