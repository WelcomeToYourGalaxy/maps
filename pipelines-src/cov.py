import json,collections,process as PR
POS=PR.POS
H=json.load(open('data/uni/holders.json')); E=json.load(open('data/uni/edu.json')); D=json.load(open('data/uni/inst.json'))
qid=lambda s:s.rsplit('/',1)[1]
pp=collections.defaultdict(dict)
for r in H:
    p,pos=qid(r['p']),qid(r['pos'])
    if pos in POS: pp[p][pos]=POS[pos]
edu=collections.defaultdict(set)
for r in E: edu[qid(r['p'])].add(qid(r['u']))
print('people',len(pp),'with edu',sum(1 for p in pp if edu[p]))
rank=collections.Counter(max(r for i,r in v.values()) for v in pp.values()); print('by top rank',sorted(rank.items()))
# map people
rec=json.load(open('/home/claude/maps/pipelines-src/data/records.json')); mp={r[0] for r in rec}
print('map people',len(mp),'in universe',len(mp&set(pp)))
inst=collections.defaultdict(set)
for p,us in edu.items():
    if p in pp:
        for u in us: inst[u].add(p)
c=[len(v) for v in inst.values()]
print('institutions',len(inst))
for t in [1,2,3,5,10,20,50,100]: print(' >=',t,sum(1 for x in c if x>=t))
Q=json.load(open('data/qids.json')); mq={x for v in Q.values() for x in v}
print('map school qids',len(mq),'present in inst',len(mq&set(inst)))
# share of people with edu linked to a map school qid directly
lk=sum(1 for p in pp if edu[p]&mq); print('people with edu at a map qid (direct)',lk)
det={}
for r in D:
    u=qid(r['u']); e=det.setdefault(u,{})
    for k in ('lab','coord','cty','inc','parent','wp'):
        if k in r: e.setdefault(k,r[k])
print('inst with coords',sum(1 for u in inst if 'coord' in det.get(u,{})),'with coord+>=1')
top=sorted(inst,key=lambda u:-len(inst[u]))[:60]
for u in top: print(len(inst[u]),u,det.get(u,{}).get('lab'),'*' if u in mq else '')
