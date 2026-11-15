import re,json,os
W='data/wp/'
def lines(f,a,b):
    L=open(W+f,encoding='utf-8').read().split('\n'); return '\n'.join(L[a-1:b-1])
SL={ # program id: (file, start line, end line)
 'atlantikbruecke':('Atlantik-Br%C3%BCcke.wiki',93,120),
 'chevening':('Chevening_Scholarship.wiki',51,187),
 'uchicago':('Chicago_Boys.wiki',33,59),
 'eisenhower':('Eisenhower_Fellowships.wiki',43,61),
 'faf':('French-American_Foundation.wiki',24,63),
 'fulbright':('Fulbright_Program.wiki',356,484),
 'ivlp':('International_Visitor_Leadership_Program.wiki',14,740),
 'eton':('List_of_Old_Etonians_born_in_the_20th_century.wiki',11,587),
 'rhodes':('List_of_Rhodes_Scholars.wiki',7,11162),
 'marshall':('Marshall_Scholarship.wiki',225,524),
 'mps':('Mont_Pelerin_Society.wiki',62,186),
 'cgsc':('United_States_Army_Command_and_General_Staff_College.wiki',126,184),
 'whinsec':('Western_Hemisphere_Institute_for_Security_Cooperation.wiki',197,408),
 'yseali':('Young_Southeast_Asian_Leaders_Initiative.wiki',34,58),
 'ygl':('Young_Global_Leaders.wiki',24,350),
}
out={}
for k,(f,a,b) in SL.items():
    t=lines(f,a,b)
    t=re.sub(r'<ref[^>]*/>','',t); t=re.sub(r'<ref.*?</ref>','',t,flags=re.S)
    ti=[]
    LINK=re.compile(r'\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]')
    def first(seg):
        for m in LINK.finditer(seg):
            x=m.group(1).strip()
            if ':' in x: continue
            return x[0].upper()+x[1:]
        return None
    segs=[]; row=None
    for line in t.split('\n'):
        st=line.strip()
        if st.startswith('{|') or st.startswith('|}'):
            if row: segs.append(row); row=None
            continue
        if st.startswith('|-'):
            if row: segs.append(row)
            row=''; continue
        if row is not None and (st.startswith('|') or st.startswith('!')):
            row+=' '+st; continue
        if row is not None and st and not st.startswith(('*','#','=')):
            row+=' '+st; continue
        if row: segs.append(row); row=None
        if st.startswith(('*','#')): segs.append(st)
    if row: segs.append(row)
    for seg in segs:
        x=first(seg)
        if x and x not in ti: ti.append(x)
    out[k]=ti
    print(k,len(ti))
json.dump(out,open('data/list_titles.json','w'),indent=0)
