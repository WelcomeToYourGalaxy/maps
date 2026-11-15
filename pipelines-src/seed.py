# id | kind | Wikipedia title (en)
SEED = """
uchicago|econ|University of Chicago
puc_chile|econ|Pontifical Catholic University of Chile
berkeley|econ|University of California, Berkeley
ui_feb|econ|Faculty of Economics and Business, University of Indonesia
harvard|econ|Harvard University
hiid|econ|Harvard Institute for International Development
mit|econ|Massachusetts Institute of Technology
lse|econ|London School of Economics
yale|econ|Yale University
stanford|econ|Stanford University
itam|econ|Instituto Tecnológico Autónomo de México
cema|econ|Universidad del CEMA
uniandes|econ|University of the Andes (Colombia)
pucrio|econ|Pontifical Catholic University of Rio de Janeiro
fgv|econ|Fundação Getulio Vargas
nes|econ|New Economic School
hse|econ|Higher School of Economics
ceu|econ|Central European University
jvi|econ|Joint Vienna Institute
penn|econ|University of Pennsylvania
ena|elite|École nationale d'administration
scpo|elite|Sciences Po
polytechnique|elite|École Polytechnique
oxford|elite|University of Oxford
cambridge|elite|University of Cambridge
hks|elite|Harvard Kennedy School
sfs|elite|Walsh School of Foreign Service
sais|elite|Paul H. Nitze School of Advanced International Studies
sipa|elite|School of International and Public Affairs, Columbia University
fletcher|elite|The Fletcher School at Tufts University
spia|elite|Princeton School of Public and International Affairs
coleurope|elite|College of Europe
lkyspp|elite|Lee Kuan Yew School of Public Policy
todai|elite|University of Tokyo
snu|elite|Seoul National University
tsinghua|elite|Tsinghua University
pku|elite|Peking University
mgimo|elite|Moscow State Institute of International Relations
iheid|elite|Graduate Institute of International and Development Studies
paris|elite|University of Paris
makerere|elite|Makerere University
forthare|elite|University of Fort Hare
aub|elite|American University of Beirut
louvain|elite|Université catholique de Louvain
mbrsg|elite|Mohammed Bin Rashid School of Government
matsushita|elite|Matsushita Institute of Government and Management
lbsnaa|state|Lal Bahadur Shastri National Academy of Administration
csa_pk|state|Civil Services Academy (Pakistan)
ksg|state|Kenya School of Government
ranepa|state|Russian Presidential Academy of National Economy and Public Administration
psc_sg|state|Public Service Commission (Singapore)
enap|state|Escola Nacional de Administração Pública
ena_sn|state|École nationale d'administration (Senegal)
cps|state|Central Party School of the Chinese Communist Party
celap|state|China Executive Leadership Academy Pudong
mjnls|state|Mwalimu Julius Nyerere Leadership School
lenin|state|International Lenin School
kutv|state|Communist University of the Toilers of the East
sunyatsen|state|Moscow Sun Yat-sen University
rudn|state|Peoples' Friendship University of Russia
hps_cpsu|state|Higher Party School of the CPSU
hcma|state|Ho Chi Minh National Academy of Politics
kimilsung_hps|state|Kim Il Sung Higher Party School
nicolopez|state|Ñico López Higher Party School
winneba|state|Kwame Nkrumah Ideological Institute
komsomol|state|Komsomol
cyl|state|Communist Youth League of China
eton|prep|Eton College
harrow|prep|Harrow School
winchester|prep|Winchester College
rosey|prep|Institut Le Rosey
doon|prep|The Doon School
aitchison|prep|Aitchison College
andover|prep|Phillips Academy
groton|prep|Groton School
royal_college_ma|prep|Royal College (Morocco)
llg|prep|Lycée Louis-le-Grand
gordonstoun|prep|Gordonstoun
alliance_ke|prep|Alliance High School (Kenya)
budo|prep|King's College Budo
achimota|prep|Achimota School
victoria_alex|prep|Victoria College, Alexandria
mayo|prep|Mayo College
ygl|fellow|Forum of Young Global Leaders
shapers|fellow|Global Shapers
rhodes|fellow|Rhodes Scholarship
marshall|fellow|Marshall Scholarship
fulbright|fellow|Fulbright Program
chevening|fellow|Chevening Scholarship
commonwealth|fellow|Commonwealth Scholarship and Fellowship Plan
ivlp|fellow|International Visitor Leadership Program
yali|fellow|Young African Leaders Initiative
yseali|fellow|Young Southeast Asian Leaders Initiative
eisenhower|fellow|Eisenhower Fellowships
faf|fellow|French-American Foundation
atlantikbruecke|fellow|Atlantik-Brücke
bap|fellow|British-American Project
gmf|fellow|German Marshall Fund
aspen|fellow|Aspen Institute
schwarzman|fellow|Schwarzman Scholars
yenching|fellow|Yenching Academy
obama|fellow|Obama Foundation
daad|fellow|German Academic Exchange Service
jica|fellow|Japan International Cooperation Agency
itec|fellow|Indian Technical and Economic Cooperation Programme
turkiye_burs|fellow|Türkiye Scholarships
whinsec|mil|Western Hemisphere Institute for Security Cooperation
cgsc|mil|United States Army Command and General Staff College
usawc|mil|United States Army War College
ndu|mil|National Defense University
sandhurst|mil|Royal Military Academy Sandhurst
rcds|mil|Royal College of Defence Studies
saintcyr|mil|École spéciale militaire de Saint-Cyr
frunze|mil|Frunze Military Academy
nanjing|mil|PLA Army Command College
iadc|mil|Inter-American Defense College
ilea|mil|International Law Enforcement Academy
fbina|mil|FBI National Academy
fuhsingkang|mil|Fu Hsing Kang College
kgb_school|mil|Academy of the Federal Security Service of the Russian Federation
svr_academy|mil|Foreign Intelligence Academy
leadership_inst|ideas|Leadership Institute
atlas|ideas|Atlas Network
mps|ideas|Mont Pelerin Society
iea|ideas|Institute of Economic Affairs
heritage|ideas|Heritage Foundation
fedsoc|ideas|Federalist Society
kas|ideas|Konrad Adenauer Foundation
fes|ideas|Friedrich Ebert Foundation
ndi|ideas|National Democratic Institute
iri|ideas|International Republican Institute
ufm|ideas|Francisco Marroquín University
rss|ideas|Rashtriya Swayamsevak Sangh
fellowship|ideas|The Fellowship (Christian organization)
madinah|faith|Islamic University of Madinah
azhar|faith|Al-Azhar University
qom|faith|Hawza of Qom
mustafa|faith|Al-Mustafa International University
haqqania|faith|Darul Uloom Haqqania
deoband|faith|Darul Uloom Deoband
imamhatip|faith|Imam Hatip school
gulen|faith|Gülen movement
navarra|faith|University of Navarra
iese|faith|IESE Business School
strathmore|faith|Strathmore University
anahuac|faith|Anahuac University Network
pea|faith|Pontifical Ecclesiastical Academy
regent|faith|Regent University
goldman|firm|Goldman Sachs
mckinsey|firm|McKinsey & Company
wb_ypp|firm|World Bank Young Professionals Program
imf_icd|firm|IMF Institute for Capacity Development
"""
ROWS=[l.split('|') for l in SEED.strip().splitlines()]
