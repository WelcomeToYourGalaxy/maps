import json, urllib.request, urllib.parse, os, ssl, sys, time
ca=os.path.expanduser('~/.ccr/ca-bundle.crt'); ctx=ssl.create_default_context(cafile=ca) if os.path.exists(ca) else None
CLS={"bank":"Q22687","exchange":"Q11691","central":"Q66344","invbank":"Q319845","creditunion":"Q745877","insurer":"Q140435124","hedge":"Q105611","pension":"Q182103","pe":"Q5418962","sovfund":"Q1061648","crypto":"Q25401607","asset":"Q4230006","rating":"Q765517","regulator":"Q105062392","devbank":"Q5266746","invest":"Q1752459"}
def run(q):
    u="https://query.wikidata.org/sparql?format=json&query="+urllib.parse.quote(q)
    r=urllib.request.Request(u,headers={"User-Agent":"wtyg-maps/1.0 (finance story map)"})
    return json.load(urllib.request.urlopen(r,timeout=120,context=ctx))["results"]["bindings"]
for k,q in CLS.items():
    if os.path.exists(k+".json"): continue
    sp="""SELECT ?i ?iLabel ?c ?ccLabel WHERE { ?i wdt:P31/wdt:P279* wd:%s . OPTIONAL{?i wdt:P625 ?c1} OPTIONAL{?i wdt:P159 ?h . ?h wdt:P625 ?c2} BIND(COALESCE(?c1,?c2) AS ?c) FILTER(BOUND(?c)) OPTIONAL{?i wdt:P17 ?cc} FILTER NOT EXISTS {?i wdt:P576 ?x} SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }""" % q
    try:
        b=run(sp); json.dump(b,open(k+".json","w")); print(k,len(b))
    except Exception as e: print(k,"ERR",str(e)[:120])
    time.sleep(2)
