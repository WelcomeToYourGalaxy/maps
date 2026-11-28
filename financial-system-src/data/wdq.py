import json, urllib.request, urllib.parse, os, ssl, sys, time
ca=os.path.expanduser('~/.ccr/ca-bundle.crt'); ctx=ssl.create_default_context(cafile=ca)
def run(q):
    u="https://query.wikidata.org/sparql?format=json&query="+urllib.parse.quote(q)
    r=urllib.request.Request(u,headers={"User-Agent":"wtyg-maps/1.0 (financial system story map; github.com/WelcomeToYourGalaxy)"})
    return json.load(urllib.request.urlopen(r,timeout=150,context=ctx))["results"]["bindings"]
