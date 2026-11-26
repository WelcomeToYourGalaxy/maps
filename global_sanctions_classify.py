import re, pickle, collections, json, sys
D='/home/claude/data'
B=pickle.load(open(D+'/built.pkl','rb'))
S=B['SOURCES']; SCH=B['SCH']; shards=B['shards']
# (key, label, severity, description, [regexes])
NAT=[
 ('terror','Terrorism & armed groups',5,
  'The listing is made under a counter-terrorism power: a designated terrorist organisation or financier, a proscription order, or a UN 1267/1373 listing.',
  r'\bSDGT\b|\bFTO\b|terroris|proscrib|al[- ]?qaida|al[- ]?qaeda|\bisil\b|\bisis\b|da\'?esh|taliban|hamas|hizball|hezboll|boko haram|(?:resolution|r\xe9solution|resoluci\xf3n|res\.|unscr|rcsnu|uscr)\s*(?:1267|1373|1988)\b|\b(?:1267|1373|1988)\s*\(|NS-PLC|\bSDT\b|terror'),
 ('war','War & territorial aggression',5,
  'The listing responds to an armed invasion or the annexation of territory — most of these are Russia-Ukraine measures.',
  r'EO ?14024|RUSSIA-EO|UKRAINE-EO|territorial integrity|sovereignty and independence|invasion of ukraine|annexation|crimea|donetsk|luhansk|situation in ukraine|BELARUS-EO|destabilis|destabiliz'),
 ('wmd','Weapons & proliferation',5,
  'The listing concerns nuclear, chemical, biological or missile programmes, or arms embargoes and arms trafficking.',
  r'\bNPWMD\b|\bWMD\b|proliferat|nuclear|ballistic|missile|chemical weapon|biological weapon|\bDPRK\b|north korea|arms embargo|\bAECA\b|\bITAR\b|defense trade|CBW\b|NPT\b'),
 ('atrocity','Human rights abuses & atrocities',4,
  'The listing is made under a human-rights power: killings, torture, repression, ethnic cleansing or genocide.',
  r'human rights|\bGLOMAG\b|magnitsky|genocid|atrocit|ethnic cleansing|crimes against humanity|torture|repression|political prisoner|war crime'),
 ('traffick','Human trafficking & forced labour',4,
  'The listing concerns forced labour, trafficking in persons, or goods made with forced labour.',
  r'forced labou?r|\bUFLPA\b|trafficking in persons|withhold release|human traffick|slavery|child labou?r'),
 ('drugs','Drugs & narcotics',4,
  'The listing is made under a narcotics power: kingpins, cartels, traffickers and their companies.',
  r'\bSDNTK\b|narcotic|kingpin|ILLICIT-DRUGS|drug traffick|\bcartel\b|fentanyl|cocaine|opioid|\bSDNT\b'),
 ('orgcrime','Organised crime & violence',4,
  'The listing concerns an organised criminal group, or a warrant for a violent offence.',
  r'\bTCO\b|transnational criminal|organi[sz]ed crime|mafia|yakuza|triad|\bgang\b|extortion|kidnap|homicide|murder|armed robbery|smuggl'),
 ('cyber','Cyber attacks & ransomware',4,
  'The listing concerns malicious cyber activity: intrusion, ransomware or election interference by digital means.',
  r'\bcyber\b|ransomware|malware|hacking|EO ?13694|CYBER2|election interference'),
 ('corrupt','Corruption & kleptocracy',3,
  'The listing concerns bribery, embezzlement, kleptocracy or the theft of state assets.',
  r'corrupt|kleptocra|briber|embezzl|misappropriat|illicit enrichment|foreign corrupt practices|\bFCPA\b'),
 ('fincrime','Financial crime & fraud',3,
  'The listing concerns fraud, money laundering, sanctions evasion or securities offences.',
  r'money launder|\bAML\b|\bfraud\b|ponzi|FinCEN|section 311\b|securities violation|FINRA|insider trading|evasion|shell compan|tax evasion'),
 ('export','Export control & military-industrial',2,
  'The listing restricts what may be sold to the party: export-control entity lists, military end users and military-linked companies.',
  r'entity list|bureau of industry|\bBIS\b|military end[- ]user|dual[- ]use|strategic high[- ]tech|chinese military|\bCMIC\b|1260H|denied persons|unverified list|end user list|export control'),
 ('procure','Debarment & procurement exclusion',1,
  'The party is barred from public contracts, development-bank funding or a public health programme, usually after a finding of fraud or non-performance.',
  r'debar|procurement exclusion|excluded from|ineligib|suspended and|provider exclusion|medicaid|medicare|\bSAM\b|contract exclusion|blacklist'),
 ('regulat','Regulatory & licensing action',1,
  'A financial or professional regulator has warned about, suspended or refused to authorise the party.',
  r'unauthoris|unauthoriz|investor warning|licence|license refus|suspension|regulatory notice|warning list|not authorised|disciplin'),
 ('warrant','Arrest warrant, offence not stated',3,
  'A police or prosecution body wants the party arrested but the list does not publish what for. Red notices and national wanted registers mostly fall here.',
  r'(?!x)x'),
 ('counter','Counter-sanctions & retaliation',2,
  'A government has listed the party in retaliation for sanctions imposed on it, rather than for conduct of the party\u2019s own.',
  r'(?!x)x'),
 ('region','Named for where it operates or who owns it',1,
  'The party is named because of where it is, what sector it is in, or who owns or controls it \u2014 the list alleges no offence. Research datasets and regional watchlists fall here.',
  r'(?!x)x'),
 ('country','Country programme',2,
  'A broad country sanctions programme — the party is listed because of where it operates or who it belongs to, not for a named offence.',
  r'\bCUBA\b|\bIRAN\b|\bSYRIA\b|VENEZUELA|BURMA|myanmar|ZIMBABWE|\bSUDAN\b|\bLIBYA\b|SOMALIA|\bYEMEN\b|NICARAGUA|BALKANS|\bIRAQ\b|LEBANON|\bMALI\b|HAITI|afghanistan|central african'),
]
RE=[(k,l,s,d,re.compile(r,re.I)) for k,l,s,d,r in NAT]
SEVOF={k:s for k,l,s,d in [(a,b,c,e) for a,b,c,e,_ in NAT]}
# where a whole list has one purpose and publishes no programme text, the list itself says what it is
SRCRULE=[(re.compile(x,re.I),k) for x,k in [
 (r'wanted|red notice|fugitive|most wanted|rozysk|search list',          'warrant'),
 (r'ukraine nsdc|war and sanctions|myrotvorets|wagner',                   'war'),
 (r'UFLPA',                                                               'traffick'),
 (r'uyghur region|long shadows|fractured veins|xinjiang',                 'region'),
 (r'targeting us citizens|counter[- ]sanction|retaliat',                  'counter'),
 (r'disreputable|suspended compan|business restriction|exclusion|debar|medicheck|ineligible|adverse action', 'procure'),
 (r'disqualified director|enforcement action|regulat|supervis|warning',   'regulat'),
 (r'terrorist|terror',                                                    'terror'),
 (r'end user list|entity list|high[- ]tech|military',                     'export'),
]]
counts=collections.Counter(); sev=collections.Counter(); assigned={}
for col,rows in shards.items():
    for r in rows:
        txt=' '.join(r[9] or [])+' || '+' || '.join(S[i] for i in r[4])
        hits=[]
        for k,l,s,d,rx in RE:
            if rx.search(txt): hits.append((s,k))
        if not hits:
            for rx,k in SRCRULE:
                if any(rx.search(S[i]) for i in r[4]): hits=[(SEVOF[k],k)]; break
        if not hits:
            r.append([]); counts['none']+=1; sev[0]+=1; continue
        hits.sort(reverse=True)
        keys=[k for _,k in hits][:3]
        r.append([ [x[0] for x in NAT].index(k) for k in keys ])
        for k in keys: counts[k]+=1
        sev[hits[0][0]]+=1
tot=sum(len(v) for v in shards.values())
print('total',tot)
print('unclassified: %d (%.1f%%)'%(counts['none'],100*counts['none']/tot))
for k,l,s,d,rx in NAT:
    print('  sev%d %-38s %7d  %5.1f%%'%(s,l,counts[k],100*counts[k]/tot))
print('severity bands:',dict(sorted(sev.items())))
pickle.dump({'shards':shards,'SOURCES':S,'SCH':SCH,'stats':B['stats'],'META':B['META'],
             'NAT':[[k,l,s,d] for k,l,s,d,_ in NAT]},open(D+'/built2.pkl','wb'),protocol=4)
