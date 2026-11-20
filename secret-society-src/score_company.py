#!/usr/bin/env python3
"""Pull COMPANY-cell candidates out of the Romanian corpus.

    python3 score_company.py cache/dna_ro.jsonl dna_company.jsonl

bk: company under ruling 17 is a body that sells goods or services or is a
state-owned enterprise, and ruling 12 adds public hospitals and state
authorities reached through their own officers. In the Romanian corpus that is
hospitals, the regii and companii nationale, the county water and heating
companies, the port administrations and the agricultural research stations.

Requires: a bribery or influence charge (abuse of office alone names no payer
and fails BRIEF11 limb 1), a facts section, and a company-class body.
"""
import json,sys,re,os

SRC='/home/claude/repo/secret-society-src/data'

BRIBE=re.compile(r'(?i)luare de mit|dare de mit|trafic de influen|cump[ăa]rare de influen|mituire')
FACTS=re.compile(r'(?i)(stare de fapt|starea de fapt)')
# a company-class body: it sells a service or is state-owned
COMPANY=re.compile(r'(?i)\b(spital\w*|institutul (?:de|clinic|na[țt]ional)|'
 r'serviciul de ambulan[țt][ăa]|centrul medical|policlinic\w*|sanatoriu\w*|'
 r'c\.?n\.? [A-ZȘȚĂÂÎ]|companie na[țt]ional|compania na[țt]ional|'
 r'regia (?:autonom|na[țt]ional)|societatea na[țt]ional|s\.?c\.? [A-ZȘȚĂÂÎ][\w\-]* s\.?[ar]\.?|'
 r'apele rom[âa]ne|administra[țt]ia bazinal|administra[țt]ia porturilor|'
 r'aeroportul|c\.?f\.?r\.?|c\.?e\.? (?:oltenia|hunedoara)|complexul energetic|'
 r'termoficare|ap[ăa] canal|apa (?:nova|serv|brasov|vital)|salubritate|'
 r'transport (?:local|public|urban)|sta[țt]iunea de cercetare|'
 r'universitatea|facultatea|casa (?:de asigur|na[țt]ional)|'
 r'direc[țt]ia (?:de )?(?:s[ăa]n[ăa]tate|silvic)|romsilva|unifarm|hidroelectrica|'
 r'romgaz|transgaz|transelectrica|po[șs]ta rom[âa]n|metrorex|tarom)\b')
SKIPDOC=re.compile(r'(?i)bilan[țt]ul de activitate|raport(?:ul)? (?:anual|de activitate)|'
 r'situa[țt]ia statistic')
NAME=re.compile(r'\b[A-ZĂÂÎȘȚ]{3,}(?:[\s\-][A-ZĂÂÎȘȚ]{2,}){1,3}\b')

def main():
    cf,outf=sys.argv[1],sys.argv[2]
    held=json.load(open(os.path.join(SRC,'cases.json'),encoding='utf-8'))
    rm=json.load(open(os.path.join(SRC,'removed_records.json'),encoding='utf-8'))['cases']
    used=set()
    for x in held+rm:
        for m in re.finditer(r'dna\.ro/comunicat\.xhtml\?id=(\d+)',str(x.get('url',''))):
            used.add(int(m.group(1)))
    st={'total':0,'held':0,'skipdoc':0,'nobribe':0,'notice':0,'nocompany':0,'kept':0}
    out=[]
    for line in open(cf,encoding='utf-8'):
        r=json.loads(line); st['total']+=1
        if r['id'] in used: st['held']+=1; continue
        t=r['text']
        if SKIPDOC.search(t[:600]): st['skipdoc']+=1; continue
        if r['words']>6000: st['skipdoc']+=1; continue
        if not BRIBE.search(t[:3000]): st['nobribe']+=1; continue
        if not FACTS.search(t): st['notice']+=1; continue
        if not COMPANY.search(t[:3500]): st['nocompany']+=1; continue
        out.append({'id':r['id'],'url':r['url'],'date':r['date'],'year':r['year'],
                    'words':r['words'],'names':sorted(set(NAME.findall(t[:2200])))[:6],
                    'text':t})
        st['kept']+=1
    out.sort(key=lambda r:-r['year'])
    with open(outf,'w',encoding='utf-8') as f:
        for r in out: f.write(json.dumps(r,ensure_ascii=False)+'\n')
    print(st)
main()
