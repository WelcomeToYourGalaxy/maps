import json,sys,time
import os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));from sparql import q
L=json.load(open('data/list_titles.json'))
SRC={'atlantikbruecke':'Atlantik-Br%C3%BCcke','chevening':'Chevening_Scholarship','uchicago':'Chicago_Boys','eisenhower':'Eisenhower_Fellowships','faf':'French-American_Foundation','fulbright':'Fulbright_Program','ivlp':'International_Visitor_Leadership_Program','eton':'List_of_Old_Etonians_born_in_the_20th_century','rhodes':'List_of_Rhodes_Scholars','marshall':'Marshall_Scholarship','mps':'Mont_Pelerin_Society','cgsc':'United_States_Army_Command_and_General_Staff_College','whinsec':'Western_Hemisphere_Institute_for_Security_Cooperation','yseali':'Young_Southeast_Asian_Leaders_Initiative','ygl':'Young_Global_Leaders'}
out=[]
titles=sorted({t for v in L.values() for t in v})
T2Q={}
for i in range(0,len(titles),200):
    vals=' '.join('"%s"@en'%t.replace('\\','').replace('"','\\"') for t in titles[i:i+200])
    for b in q(f'''SELECT ?t ?item WHERE {{ VALUES ?t {{ {vals} }} ?a schema:name ?t; schema:isPartOf <https://en.wikipedia.org/>; schema:about ?item. ?item wdt:P31 wd:Q5. }}'''):
        T2Q[b['t']]=b['item'].rsplit('/',1)[1]
    time.sleep(1)
print('humans',len(T2Q),'of',len(titles))
qs=sorted(set(T2Q.values()))
POSR={}
for i in range(0,len(qs),150):
    vals=' '.join('wd:'+x for x in qs[i:i+150])
    for b in q(f'''SELECT ?p ?pos ?start ?end WHERE {{ VALUES ?p {{ {vals} }} ?p p:P39 ?st. ?st ps:P39 ?pos. OPTIONAL{{?st pq:P580 ?start}} OPTIONAL{{?st pq:P582 ?end}} }}'''):
        POSR.setdefault(b['p'].rsplit('/',1)[1],[]).append(b)
    time.sleep(1)
for sid,ts in L.items():
    for t in ts:
        p=T2Q.get(t)
        if not p: continue
        for b in POSR.get(p,[]):
            out.append({'p':p,'s':sid,'pos':b['pos'].rsplit('/',1)[1],'start':b.get('start'),'end':b.get('end'),'src':'https://en.wikipedia.org/wiki/'+SRC[sid]})
json.dump(out,open('data/list_alumni.json','w'))
print('rows',len(out))
