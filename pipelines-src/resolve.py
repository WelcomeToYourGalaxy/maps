import json,urllib.request,urllib.parse,sys,time
sys.path.insert(0,'.')
from seed import ROWS
UA={'User-Agent':'PipelineMap/0.1 (civic education map; contact via github WelcomeToYourGalaxy)'}
def get(url,params):
    u=url+'?'+urllib.parse.urlencode(params)
    for i in range(6):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60))
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(10*(i+1))
out={}
titles=[r[2] for r in ROWS]
for i in range(0,len(titles),20):
    chunk=titles[i:i+20]; time.sleep(2)
    d=get('https://en.wikipedia.org/w/api.php',dict(action='query',format='json',redirects=1,prop='pageprops|extracts|coordinates|info',inprop='url',exintro=1,explaintext=1,exlimit=20,titles='|'.join(chunk)))
    q=d['query']; m={t:t for t in chunk}
    for n in q.get('normalized',[]): 
        for k,v in m.items():
            if v==n['from']: m[k]=n['to']
    for n in q.get('redirects',[]):
        for k,v in m.items():
            if v==n['from']: m[k]=n['to']
    pages={p['title']:p for p in q['pages'].values()}
    for t in chunk:
        p=pages.get(m[t],{})
        out[t]=dict(title=p.get('title'),qid=p.get('pageprops',{}).get('wikibase_item'),url=p.get('fullurl'),extract=p.get('extract',''),coords=p.get('coordinates'),missing='missing' in p)
json.dump(out,open('data/wiki.json','w'),indent=1)
for r in ROWS:
    o=out[r[2]]
    if o['missing'] or not o['qid']: print('MISSING',r)
print('done',sum(1 for v in out.values() if v['qid']))
