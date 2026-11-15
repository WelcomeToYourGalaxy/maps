import json,urllib.request,urllib.parse,sys,time
UA={'User-Agent':'PipelineMap/0.1 (civic education map; github WelcomeToYourGalaxy)','Accept':'application/sparql-results+json'}
def q(query,tries=5):
    data=urllib.parse.urlencode({'query':query}).encode()
    for i in range(tries):
        try:
            r=urllib.request.urlopen(urllib.request.Request('https://query.wikidata.org/sparql',data=data,headers=UA),timeout=300)
            return [{k:v['value'] for k,v in b.items()} for b in json.load(r)['results']['bindings']]
        except Exception as e:
            print('sparql retry',i,str(e)[:200],file=sys.stderr); time.sleep(15*(i+1))
    raise SystemExit('sparql failed')
