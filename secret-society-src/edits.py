"""Every change made to the Drug Underworld Map shell to produce this map.

Each entry is ('rep', old, new, count) — an exact replacement that must match `count`
times — or ('block', start_marker, end_marker, new) — everything from start_marker up to
(not including) end_marker is replaced. The build stops if any marker is missing, so a
change to the shell cannot silently drop an edit.
"""

TITLE = 'Secret Society Infiltration Map'
SUB = ('Where lodges, religious orders, policy clubs and covert networks reached inside '
       'governments — 193 states scored, and the cases a court, inquiry or government confirmed')

RUNDOWN = '''<div class="wire-lead">
      Nobody keeps a register of which officials belong to which society, and most of these organisations exist so that no such register can be compiled. Membership lists surface when a police raid finds one, as at Licio Gelli's villa in 1981; when a parliament orders one handed over, as Britain's did for Masonic police officers in 1999; or when a government falls and the next one opens the files, as in Turkey after 2016.<br><br>
      So this map does not claim to count infiltration. It carries layers that can each be checked, and keeps them apart.<br><br>
      The first is a 193-country score. Half of it is the documented record below, weighted by how far each case got and how high it reached. Three-tenths is organisational reach: how many of the {N_ORGS} tracked organisations have a documented national presence in the country. One-fifth is conditions, from the Global Organized Crime Index 2025: how freely officials act for hidden principals and how little stops them. Where a country has no documented case the score is a best-judgement estimate of likelihood, and its popup is marked as one.<br><br>
      The second layer is the documented record: {N_CASES} cases in which a court, a parliamentary or official inquiry, a government designation, a regulator or the organisation itself established that it had members or agents inside a public institution. Each names the office reached and the forum that found it. Roberto Calvi is one: chairman of Banco Ambrosiano and a member of the P2 lodge, found hanging under Blackfriars Bridge in London in June 1982. An Italian court ruled in 2005 that he was murdered. Ambrosiano collapsed owing about $1.3 billion, much of it through shell companies the Vatican Bank controlled, and in 1984 the Vatican paid creditors $241 million while admitting no liability.<br><br>
      The third layer is the organisations: {N_ORGS} headquarters, {N_BRANCHES} national branches and chapters, and {N_ROUTES} documented channels along which members, money or orders moved between them. A branch dot marks presence in a country, not proof of infiltration there.
      </div>
      '''

EST_CSS = '''<style>
  .est-band{background:#353a4c !important;color:#d6d0d6 !important;}
  .est-n{border-left-color:#7a6b92 !important;background:rgba(122,107,146,0.09) !important;color:#c9c2d2 !important;}
  .est-n b{color:#ddd3e6 !important;}
  .st-acknowledged{color:#c08a96;} .st-reported{color:#a59a96;} .st-annulled{color:#8f9aa8;}
  .st-active{color:#9fb7a6;} .st-dissolved{color:#8f9aa8;} .st-banned{color:#b07a86;} .st-dormant{color:#9a93a8;}
  .pres-h{font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--accent-hi);margin:11px 0 4px;}
  .pres-list{display:flex;flex-wrap:wrap;gap:4px 5px;}
  .pres-chip{font-size:10.5px;padding:2px 7px;border-radius:10px;cursor:pointer;
    background:rgba(255,255,255,0.045);border:1px solid rgba(255,255,255,0.10);color:#d9d4da;}
  .pres-chip:hover{background:rgba(255,255,255,0.10);color:#fff;}
  .pres-chip i{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:5px;vertical-align:0;}
  .pres-chip.est{border-style:dashed;color:#aaa3b2;}
  .org-cases{margin-top:10px;}
</style>
</head>'''

JS_A = r'''/* Some records on this map were reversed after the fact: a conviction annulled on appeal,
   a dissolution order stayed. The finding stands in the record and the popup says what
   happened to it, rather than leaving the status field to carry the whole story. */
function undoneHTML(x){ return x.undone ? '<div class="ci-undone"><b>What happened next</b><br>'+x.undone+'</div>' : ''; }
var ORGN = DATA.orgnames || {}, ORGT = DATA.orgtypes || {};
var ORG_BY_K = {}; ENTITIES.forEach(function(e){ ORG_BY_K[e.k]=e; });
var OUTCOME={convicted:'Convicted',indicted:'Indicted',settled:'Settled',inquiry:'Inquiry',
             acknowledged:'Acknowledged',designated:'Designated',reported:'Reported',
             acquitted:'Acquitted',annulled:'Annulled',investigation:'Investigating',alleged:'Alleged',
             active:'Active',dissolved:'Dissolved',banned:'Banned',dormant:'Dormant'};
function archHTML(x){
  return x.arch ? '<div class="ci-c">Also in the Welcome to Your Galaxy conspiracy archive: &ldquo;'+x.arch.t+
    '&rdquo; &mdash; archive trust rating '+x.arch.s+'/10</div>' : '';
}
function srcLink(x){ return x.url?' — <a href="'+x.url+'" target="_blank" rel="noopener" style="color:#8fb8c9;">source</a>':''; }
/* One row per organisation, so a country's list reads as comparable lines: name, type,
   status, founding year. The writeup, presence and citation sit behind the row. */
function entHTML(e, folded){
  var s=SMAP[e.s]||{}, col=(s.accent||'#8fb8c9'), kt=kindTag(e);
  var row='<div class="ent-row" style="border-left-color:'+col+';">'+
    '<span class="ent-name">'+e.n+'</span>'+
    '<span class="ent-kind" style="color:'+kt.c+'">'+kt.t+'</span>'+
    '<span class="ent-st st-'+e.status+'">'+(OUTCOME[e.status]||e.status)+'</span>'+
    '<span class="ent-yr">'+(e.y||'')+'</span>'+
    '<span class="ent-car">▾</span></div>';
  var nc=CASES.filter(function(c){ return c.org===e.k; });
  var ncc={}; nc.forEach(function(c){ ncc[c.c]=1; });
  var body='<div class="ci-fold'+(folded===false?' open':'')+'">'+
    '<div class="ci-m">'+(e.role?e.role+' &middot; ':'')+'<span style="color:'+col+'">'+(s.label||e.s)+'</span>'+
      (e.ended?(' &middot; '+e.y+'–'+e.ended):'')+'</div>'+
    '<div class="ci-d">'+e.d+'</div>'+
    '<div class="ci-m" style="margin-top:6px;">Documented presence in '+e.nr+' countr'+(e.nr===1?'y':'ies')+
      (e.ne?(', likely in '+e.ne+' more'):'')+' &middot; '+nc.length+' documented case'+(nc.length===1?'':'s')+
      (nc.length?(' in '+Object.keys(ncc).length+' countr'+(Object.keys(ncc).length===1?'y':'ies')):'')+'</div>'+
    (e.rsrc?('<div class="ci-c">Presence: '+e.rsrc+'</div>'):'')+
    undoneHTML(e)+'<div class="ci-c">'+e.cite+srcLink(e)+'</div></div>';
  return '<div class="ent-item">'+row+body+'</div>';
}
/* delegated: Leaflet rebuilds popup DOM on every open */
document.addEventListener('click',function(ev){
  var oc=ev.target && ev.target.closest ? ev.target.closest('[data-org]') : null;
  if(oc){ var o=ORG_BY_K[oc.getAttribute('data-org')]; if(o){ map.closePopup(); idxGoto(o.lat,o.lng,function(){ openEntity(o); }); } ev.stopPropagation(); return; }
  var r=ev.target && ev.target.closest ? ev.target.closest('.ent-row') : null;
  if(!r) return;
  var f=r.nextElementSibling;
  if(f && f.classList.contains('ci-fold')){
    var open=f.classList.toggle('open');
    var c=r.querySelector('.ent-car'); if(c) c.innerHTML=open?'▴':'▾';
  }
  ev.stopPropagation();
},true);
/* A branch dot is presence, not proof. Its popup says which organisation, whether the
   presence is documented or estimated, and lists any cases that organisation has in this
   country, so the reader can see at once whether presence ever became infiltration. */
function openGroup(g){
  var gt = GTMAP[g.ty], o = ORG_BY_K[g.k]||{};
  var cs = CASES.filter(function(c){ return c.org===g.k && c.c===g.c; });
  var h='<div class="popup-country">'+g.n+'</div>'+
    '<div class="ci-m">'+((gt&&gt.label)||'Organisation')+' &middot; '+g.c+'</div>'+
    (g.est ? '<div class="geo-n est-n"><b>Estimated presence.</b> No published list places this organisation here. It is drawn because its regional pattern, its neighbours or its own statements make a presence likely. Treat it as a lead.</div>'
           : '<div class="ci-d">Documented national presence'+(o.rsrc?(': '+o.rsrc):'')+'.</div>')+
    '<div class="geo-n"><b>Placed at:</b> '+g.geo+'. Where several organisations share a country their dots sit on a small ring around the capital.</div>';
  if(cs.length){ h+='<div class="m-h" style="margin-top:12px;">Cases here &mdash; '+cs.length+'</div>'; cs.forEach(function(c){ h+=caseHTML(c); }); }
  else h+='<div class="no-data" style="margin-top:8px;">No documented case for this organisation in '+g.c+'.</div>';
  h+='<span class="ci-more" data-org="'+g.k+'">Open '+g.n+'</span>';
  ptPopup(380).setLatLng([g.lat,g.lng]).setContent(h).openOn(map);
}

'''

JS_OPEN_ENTITY_EXTRA = r'''function openEntity(e){
  var cs=CASES.filter(function(c){ return c.org===e.k; }).sort(function(a,b){ return (a.y||0)-(b.y||0); });
  var h='<div class="popup-country">'+e.n+'</div>'+entHTML(e,false);
  if(cs.length){
    h+='<div class="m-h org-cases">Documented cases &mdash; '+cs.length+'</div>';
    cs.forEach(function(c){ h+=caseHTML(c); });
  }
  ptPopup(420).setLatLng([e.lat,e.lng]).setContent(h).openOn(map);
}
'''

JS_GROUPS = r'''function drawGroups(){
  if(groupLayer){ map.removeLayer(groupLayer); groupLayer=null; }
  declClear(2);
  if(!NET_ON.groups){ declSoon(); return; }
  groupLayer=L.layerGroup();
  GROUPS.forEach(function(g){
    var gt = GTMAP[g.ty];
    if(gt && !GT_ON[g.ty]) return;
    if(g.est && !NET_ON.est) return;
    var tc = (gt && gt.accent) || '#a0606f';
    /* Documented presence is a solid disc. Estimated presence is a hollow ring in the same
       colour, so the two read apart at any zoom without a second legend. */
    var m=L.circleMarker([g.lat,g.lng],{
        radius: g.est?3.2:3.6, color: g.est?tc:'#0a0c16', weight: g.est?1.2:0.9, opacity: 0.9,
        dashArray: null, fillColor: tc, fillOpacity: g.est?0.12:1,
        pane:'pts',renderer:R_PTS,bubblingMouseEvents:false});
    m.bindTooltip(g.n+' — '+g.c+(g.est?' · estimated':''),{direction:'top',offset:[0,-4]});
    m.on('click',function(e){ openGroup(g); L.DomEvent.stop(e); });
    groupLayer.addLayer(m); declRegister(m,g.lat,g.lng,5,2);
  });
  groupLayer.addTo(map); declSoon();
}
'''

JS_D = r'''function caseHTML(c, folded){
  var kt=kindTag(c);
  var row='<div class="ent-row" style="border-left-color:'+kt.c+';">'+
    '<span class="ent-name">'+c.n+'</span>'+
    '<span class="ent-kind" style="color:'+kt.c+'">'+kt.t+'</span>'+
    '<span class="ent-st st-'+c.status+'">'+(OUTCOME[c.status]||c.status)+'</span>'+
    '<span class="ent-yr">'+c.y+'</span>'+
    '<span class="ent-car">▾</span></div>';
  var body='<div class="ci-fold'+(folded===false?' open':'')+'">'+
    '<div class="ci-m">'+c.rank+(c.on?(' &middot; <span class="org-link" data-org="'+c.org+'" style="cursor:pointer;text-decoration:underline dotted;">'+c.on+'</span>'):'')+' &middot; '+c.c+'</div><div class="ci-d">'+c.d+'</div>'+
    undoneHTML(c)+'<div class="ci-c">'+c.cite+srcLink(c)+'</div>'+archHTML(c)+'</div>';
  return '<div class="ent-item">'+row+body+'</div>';
}
/* Short tags for the merged record list. Cases carry the office they reached; organisations
   carry their type. The colour is the one that category already has on the map. */
var KIND_BK  = {exec:'Head of state', cabinet:'Minister', legis:'Legislature', court:'Judiciary',
                security:'Security', finance:'Finance'};
var KIND_SEC = {lodge:'Lodge', order:'Order', forum:'Forum', covert:'Covert network',
                statenet:'State network', lawnet:'Law network'};
function kindTag(x){
  if(x.bk) return {t:(KIND_BK[x.bk]||'Public office'), c:(BUCKET_OF[x.bk]||'#a88c96')};
  var sc=SMAP[x.s]||{};
  return {t:(KIND_SEC[x.s]||'Organisation'), c:(sc.accent||'#8fb8c9')};
}
/* Cases in this country, newest first, then the organisations headquartered here. */
function recordList(cs, es){
  var h='';
  if(cs && cs.length){
    cs=cs.slice().sort(function(a,b){ return (b.y||0)-(a.y||0); });
    h+='<div class="m-h" style="margin-top:12px;">The documented record &mdash; '+cs.length+' case'+(cs.length===1?'':'s')+'</div>';
    cs.forEach(function(x){ h+=caseHTML(x); });
  }
  if(es && es.length){
    h+='<div class="m-h" style="margin-top:12px;">Headquartered here &mdash; '+es.length+'</div>';
    es.forEach(function(x){ h+=entHTML(x); });
  }
  return h;
}
function bar(v,col){ return '<div class="cap-bar"><i style="width:'+(v*10)+'%;background:'+col+'"></i></div>'; }
/* Which organisations are present in a country: documented first, then estimated. Each
   chip opens the organisation. */
function presHTML(r){
  if(!r.pres || !r.pres.length) return '';
  var doc=r.pres.filter(function(p){return !p[1];}), est=r.pres.filter(function(p){return p[1];});
  function chips(list, cls){
    return '<div class="pres-list">'+list.map(function(p){
      var col=((SMAP[ORGT[p[0]]]||{}).accent)||'#888';
      return '<span class="pres-chip'+(cls?' '+cls:'')+'" data-org="'+p[0]+'"><i style="background:'+col+'"></i>'+(ORGN[p[0]]||p[0])+'</span>';
    }).join('')+'</div>';
  }
  var h='';
  if(doc.length) h+='<div class="pres-h">Organisations with a documented presence &mdash; '+doc.length+'</div>'+chips(doc,'');
  if(est.length) h+='<div class="pres-h">Presence likely, not documented &mdash; '+est.length+'</div>'+chips(est,'est');
  return h;
}
/* A jurisdiction holding records but outside the 193-state score set: the Holy See and Taiwan. */
var OFFSET_NOTE = {
  'Vatican City':'The score set covers UN member states. The Holy See is a permanent observer, not a member, so it carries records without a score. Its bank sits at the centre of the P2 and Ambrosiano record.',
  'Taiwan':'The score set covers UN member states, and the Global Organized Crime Index does not score Taiwan separately, so it carries records without a score. Its courts have tried more United Front cases than any other jurisdiction on this map.'
};
function offsetHTML(k){
  var h='<div class="popup-country">'+k+'<span class="cap-band" style="background:#4a5570;color:#f4efe8;">Not scored</span></div>';
  h+='<div class="no-data" style="margin-top:8px;">'+(OFFSET_NOTE[k]||'This jurisdiction is outside the 193-state score set, so it carries records without a score.')+'</div>';
  var _p=(DATA.offpres||{})[k]; if(_p) h+=presHTML({pres:_p});
  var ocn=CNOTES[k];
  if(ocn){
    h+='<div class="cnote"><div class="cn-h">The record</div><div class="ci-d cn-body">'+ocn.d+'</div>'+
       '<div class="ci-c">'+ocn.cite+'</div></div>';
  }
  h+=recordList(CASES.filter(function(c){return c.c===k;}),
                ENTITIES.filter(function(e){return e.c===k;}));
  return h;
}
function openOffset(k, lat, lng){
  map.flyTo([lat,lng],5,{duration:0.9});
  var p=visiblePad(), sz=map.getSize();
  var maxH=Math.max(220, sz.y - p.tl[1] - p.br[1] - 70);
  setTimeout(function(){
    L.popup({maxWidth:420, maxHeight:maxH, autoPan:true, keepInView:true,
             autoPanPaddingTopLeft:L.point(p.tl[0]+12, p.tl[1]+12),
             autoPanPaddingBottomRight:L.point(p.br[0]+12, p.br[1]+12)})
      .setLatLng(visibleCentre()).setContent(offsetHTML(k)).openOn(map);
  }, 950);
}
function countryHTML(k){
  var r=ROWS[k];
  var h='<div class="popup-country">'+k+'<span class="cap-band" style="background:'+shade(r.exp)+';color:#f4efe8;">'+bandName(r.exp)+'</span>'+
        (r.est?'<span class="cap-band est-band">Estimated</span>':'')+'</div>';
  h+='<div class="cap-grid">'+
     '<span class="lbl">Infiltration (composite)</span><span class="val">'+r.exp.toFixed(2)+'</span></div>'+bar(r.exp,shade(r.exp));
  h+='<div class="cap-grid">'+
     '<span class="lbl">Documented record</span><span class="val">'+r.doc.toFixed(2)+'</span>'+
     '<span class="lbl">Organisational reach</span><span class="val">'+r.reach.toFixed(2)+'</span>'+
     '<span class="lbl">Conditions</span><span class="val">'+r.cond.toFixed(2)+'</span>'+
     '<span class="lbl">&nbsp;&nbsp;state-embedded actors</span><span class="val">'+r.sea.toFixed(2)+'</span>'+
     '<span class="lbl">&nbsp;&nbsp;resilience</span><span class="val">'+r.res.toFixed(2)+'</span>'+
     '</div>';
  if(r.est){
    h+='<div class="geo-n est-n"><b>No documented case on this map yet.</b> The score is a best-judgement estimate: it rises with the number of tracked organisations present here and with how freely officials act for hidden interests. The organisations below are the likely channels.</div>';
  }
  var cn=CNOTES[k];
  if(cn){
    h+='<div class="cnote">';
    h+='<div class="cn-h">The record</div><div class="ci-d cn-body">'+cn.d+'</div>';
    h+='<div class="ci-c">'+cn.cite+'</div></div>';
  }
  h+=presHTML(r);
  var cs=CASE_BY_C[k]||[], es=ENT_BY_C[k]||[];
  h+=recordList(cs,es);
  h+='<div class="ci-c" style="margin-top:9px;">Conditions: GI-TOC Organized Crime Index 2025. The composite and the reach score are this map\'s own figures.</div>';
  return h;
}
'''

JS_OPEN_CASE = r'''function openCase(c){
  var h='<div class="popup-country">'+c.n+'</div><div class="ci-m" style="margin-bottom:8px;">'+
        '<span class="st-'+c.status+'">'+(OUTCOME[c.status]||c.status).toUpperCase()+'</span> &middot; '+c.rank+' &middot; '+c.y+' &middot; '+c.c+
        (c.on?(' &middot; <span data-org="'+c.org+'" style="cursor:pointer;text-decoration:underline dotted;">'+c.on+'</span>'):'')+'</div>'+
        '<div class="ci-d">'+c.d+'</div>'+undoneHTML(c)+'<div class="ci-c">'+c.cite+srcLink(c)+'</div>'+archHTML(c);
  ptPopup(400).setLatLng([c.lat,c.lng]).setContent(h).openOn(map);
}

'''

JS_KEYS = r'''function renderKeys(){
  Array.prototype.forEach.call(document.querySelectorAll('.key-tip'), function(t){ t.remove(); });
  var b=document.getElementById('legKeys'); b.innerHTML='';
  var counts=[0,0,0,0,0], est=0;
  Object.keys(ROWS).forEach(function(k){ counts[bandIdx(lensVal(ROWS[k]))]++; if(ROWS[k].est) est++; });

  keyHead(b, 'Country infiltration');
  var note=document.createElement('div'); note.className='key-note-line';
  note.textContent='Click a country for its scores, the organisations present there and any documented cases. '+
    est+' of '+Object.keys(ROWS).length+' countries have no documented case yet; their shading is an estimate.';
  b.appendChild(note);

  keyParent(b, BANDS[0][1], 'Severity', true, 'bar', 'sev', null, null, 0);
  if(KEY_OPEN.sev){
    BANDS.forEach(function(bd,i){
      keyRow(b, bd[1], bd[0], BAND_ON[i], 'band'+i, function(){
        BAND_ON[i]=!BAND_ON[i]; renderKeys(); buildHatches();
        if(geoLayer) geoLayer.setStyle(styleC);
      }, counts[i], 'key-child d2');
    });
  }

  keyParent(b, '#a88c96', 'Show one score at a time', true, 'bar', 'crit', null, null, 0);
  if(KEY_OPEN.crit){
    LENSES.forEach(function(L_){
      var on=(L_.k===LENS);
      keyRow(b, L_.accent, L_.label, on, 'bar', function(){ setLens(L_.k); },
             null, 'key-child d2'+(on?' key-sel':''));
      keyDesc(b, L_.desc, on, 3);
    });
  }

  keyHead(b, 'Points <span class="key-sub">◆ case &nbsp; ● organisation &nbsp; • branch</span>',
          0, true);

  keyParent(b, '#b05666', 'Documented cases inside government', CASE_ON, 'diamond', 'office', CASES.length, function(){
    CASE_ON=!CASE_ON; renderKeys(); drawCaseDots();
  }, 1);
  if(KEY_OPEN.office){
    CASE_BUCKETS.forEach(function(p,i){
      var n=CASES.filter(function(c){ return c.bk===p[0]; }).length;
      if(!n) return;
      var bon = CASE_ON && CBK_ON[p[0]];
      keyRow(b, BUCKET_COLOUR[i], p[1], bon, 'diamond', function(){
        CBK_ON[p[0]]=!CBK_ON[p[0]]; if(!CASE_ON) CASE_ON=true;
        renderKeys(); drawCaseDots();
      }, n, 'key-child d2');
      if(p[2]) keyDesc(b, p[2], bon, 3);
    });
  }

  var firmsOn = SECTORS.some(function(s){ return SON[s.k]; });
  keyParent(b, '#5d81a8', 'Organisations (headquarters)', firmsOn, 'circle', 'firms', ENTITIES.length, function(){
    var turnOn=!firmsOn; SECTORS.forEach(function(s){ SON[s.k]=turnOn; });
    renderKeys(); drawEntities(); buildIndex();
  }, 1);
  if(KEY_OPEN.firms){
    SECTORS.forEach(function(s){
      keyRow(b, s.accent, s.label, !!SON[s.k], 'circle', function(){
        SON[s.k]=!SON[s.k]; renderKeys(); drawEntities(); buildIndex();
      }, ENTITIES.filter(function(e){ return e.s===s.k; }).length, 'key-child d2');
      keyDesc(b, s.d, !!SON[s.k], 3);
    });
  }

  keyParent(b, '#d3cdc8', 'Branches & chapters (presence)', NET_ON.groups, 'circle', 'groups',
            GROUPS.length, function(){
    NET_ON.groups=!NET_ON.groups; renderKeys(); drawGroups();
  }, 1);
  if(KEY_OPEN.groups){
    GTYPES.forEach(function(t){
      var on = NET_ON.groups && GT_ON[t.k];
      keyRow(b, t.accent, t.label, on, 'circle', function(){
        GT_ON[t.k] = !GT_ON[t.k];
        if(!NET_ON.groups) NET_ON.groups = true;
        renderKeys(); drawGroups();
      }, gtCount(t.k), 'key-child d2');
    });
    var ne=GROUPS.filter(function(g){return g.est;}).length;
    keyRow(b, '#9a93a8', 'Estimated presence (hollow ring)', NET_ON.groups && NET_ON.est, 'circle', function(){
      NET_ON.est=!NET_ON.est; renderKeys(); drawGroups();
    }, ne, 'key-child d2');
    keyDesc(b, 'Countries where an organisation is likely present but no published list places it. Turn off to see documented presence only.', NET_ON.est, 3);
  }

  keyHead(b, 'Channels', 0, true);
  keyParent(b, '#d6c4cc', 'Documented channels', NET_ON.routes, 'bar', 'routes',
            ROUTES.length, function(){
    NET_ON.routes=!NET_ON.routes; renderKeys(); drawRoutes();
  }, 1);
  keyDesc(b, 'Lines joining the places named in a record: where money, members or orders moved between a headquarters and a government.', NET_ON.routes, 1);
}
'''

JS_STATUS = r'''var STATUS_RANK = {convicted:8, inquiry:7, acknowledged:7, settled:6, designated:6, indicted:5,
                   reported:3, annulled:2, acquitted:1, active:0, dissolved:0, banned:0, dormant:0};
var STATUS_LABEL = {convicted:'convicted', inquiry:'inquiry finding', acknowledged:'acknowledged',
                    settled:'settled', designated:'designated', indicted:'indicted', reported:'reported',
                    annulled:'annulled', acquitted:'acquitted', active:'active', dissolved:'dissolved',
                    banned:'banned', dormant:'dormant'};
'''

JS_WIRE_VOCAB = r'''var W_ANCHOR = [
 'freemason','masonic','masonry','grand lodge','grand orient','grande loge','p2 lodge','propaganda due',
 'secret society','secret societies','opus dei','unification church','moonies','family federation',
 'scientology','gülen','gulen','fetö','feto','muslim brotherhood','hizb ut-tahrir','broederbond',
 'skull and bones','bohemian grove','bilderberg','trilateral commission','le cercle','gladio',
 'stay-behind','united front','shincheonji','nippon kaigi','soka gakkai','fellowship foundation',
 'prayer breakfast','el yunque','ordo iuris','order of malta','vatican bank','legion of christ',
 'rashtriya swayamsevak','atlas network','nxivm','massoneria','massone','loggia','franc-maçon',
 'francmason','masón','masones','maçonaria','maçom','freimaurer','vrijmetselaar','масон','ماسون',
 'mason','tarikat','cemaat','cult'
];
var W_INST = [
 'official','officer','police','minister','ministry','cabinet','mayor','governor','senator','congress',
 'parliament','lawmaker','legislator','judge','prosecutor','general','army','military','intelligence',
 'central bank','regulator','government','president','prime minister','party','inquiry','commission',
 'infiltrat','dissolution','dissolve','ban','designat','indict','convict','sentenc','charged','arrest',
 'raid','purge','dismiss','expel','member','funcionario','policía','fiscal','juez','ministro','gobierno',
 'diputado','procureur','juge','ministre','gouvernement','député','beamter','staatsanwalt','minister',
 'regierung','abgeordnete','funzionario','procura','magistrat','governo','deputato','полиц','прокур',
 'министр','правительств','депутат','hakim','savcı','emniyet','bakan','milletvekili','kabine','poder'
];
var W_VETO = [
 'masonic temple wedding','concert','festival','netflix','hbo','prime video','season','episode',
 'trailer','box office','biopic','streaming','starring','novel','book review','film review',
 'video game','videojuego','recipe','obituary','horoscope','travel guide','tourism','real estate',
 'for sale','auction','museum exhibition','basketball','football club','transfer window'
];
'''

JS_METHOD = r'''function renderMethod(){
  var n=Object.keys(ROWS).length;
  var sev=Object.keys(ROWS).filter(function(k){return ROWS[k].exp>=7.5;}).length;
  var est=Object.keys(ROWS).filter(function(k){return ROWS[k].est;}).length;
  var M=DATA.meta||{};
  var byStatus={}; CASES.forEach(function(c){ byStatus[c.status]=(byStatus[c.status]||0)+1; });
  var ccount={}; CASES.forEach(function(c){ ccount[c.c]=1; });
  var h='';
  h+='<div class="m-p">Four layers with different standing. Keep them apart when citing. The index panel lists each one separately &mdash; countries by the score in force, cases by the office they reached, organisations by type, branches by country.</div>';

  h+='<div class="m-h">Layer 1 &mdash; country score, '+n+' countries</div>';
  h+='<div class="m-p"><b>Documented record</b> = for each case in the country, a weight for how far it got (conviction 1.0, inquiry finding or acknowledgement 0.9, designation or settlement 0.8, indictment 0.7, press or academic report 0.45, annulled 0.3, acquitted 0.2) times a weight for the office reached (head of state 1.0, minister 0.85, security services and courts 0.8, central bank and finance 0.75, legislature and local office 0.65). The sum is put on a 0&ndash;10 log scale, with 10 set at the 95th percentile ('+(M.dcap||'')+') so one country cannot flatten the rest.</div>';
  h+='<div class="m-p"><b>Organisational reach</b> = the tracked organisations with a documented national presence in the country, each weighted by type (covert and state-run networks 1.2, lodges and orders 1.0, forums and law networks 0.8). Presence that is likely but undocumented counts at half. A documented case also counts as proof of presence. Scaled 0&ndash;10 against the 92nd percentile.</div>';
  h+='<div class="m-p"><b>Conditions</b> = the mean of two Global Organized Crime Index 2025 indicators: state-embedded actors, and resilience inverted. It is the one independent, expert-scored series covering all 193 states that measures officials acting for interests outside the state. It was built for organised crime, not secret societies, and is used here only for what it measures: how much room any hidden network would have.</div>';
  h+='<div class="m-p"><b>Composite</b> = 0.5 &times; documented + 0.3 &times; reach + 0.2 &times; conditions. Result: <b>'+sev+' of '+n+'</b> countries at severe. <b>'+est+'</b> countries have no documented case, so their composite is reach and conditions alone. That is the best-judgement estimate of where infiltration is likely, and those popups are marked Estimated. Because the documented half is zero for them, an undocumented country cannot score above 5.</div>';

  h+='<div class="m-h">What the score is not</div>';
  h+='<div class="m-warn">It is not a count of infiltrated institutions. The documented half measures what forums have found, which tracks how free a country\'s parliament, courts and press are as much as how penetrated its government is. Italy scores high partly because its parliament published the P2 list. A country whose lodges have never been raided scores lower than it may deserve.</div>';
  h+='<div class="m-p">Weights are this map\'s own judgement and are stated so they can be argued with. Select a single score in the map key to see any one of the three parts on its own.</div>';

  h+='<div class="m-h">Layer 2 &mdash; documented cases, '+CASES.length+' in '+Object.keys(ccount).length+' jurisdictions</div>';
  h+='<div class="m-p">Each case is a named event in which an organisation had members or agents inside a public institution, with the office reached and the forum that established it. They are bucketed by office: '+
     CASE_BUCKETS.map(function(p){ return CASES.filter(function(c){return c.bk===p[0];}).length+' '+p[1].toLowerCase(); }).join(', ')+'.</div>';
  h+='<div class="m-p">By status: '+Object.keys(byStatus).sort(function(a,b){return (STATUS_RANK[b]||0)-(STATUS_RANK[a]||0);}).map(function(s){ return '<span class="st-'+s+'">'+byStatus[s]+' '+(STATUS_LABEL[s]||s)+'</span>'; }).join(', ')+'. A <b>reported</b> case rests on major news or academic work with no forum behind it, and is weighted at less than half a conviction. Annulled and acquitted cases stay on the map with their outcome, because the original finding and its reversal are both part of the record &mdash; Turkey\'s Ergenekon and Sledgehammer convictions are the clearest example.</div>';
  h+='<div class="m-p">Where a case also appears in the Welcome to Your Galaxy conspiracy archive, its popup gives the archive entry and the archive\'s trust rating.</div>';
  h+='<div class="m-warn">Membership is not misconduct. Most of the people named in these cases were members of lawful organisations. A case is here because a forum found that the organisation, through them, reached into an office &mdash; a parallel chain of loyalty, a placement strategy, a channel for money or orders &mdash; not because membership itself is an offence.</div>';

  h+='<div class="m-h">Layer 3 &mdash; organisations, '+ENTITIES.length+' across '+SECTORS.length+' types</div>';
  h+='<div class="m-p">Each organisation is plotted at its headquarters. Its popup gives where its presence data come from and lists every case it has on the map. Types: '+SECTORS.map(function(s){return s.label.toLowerCase()+' ('+ENTITIES.filter(function(e){return e.s===s.k;}).length+')';}).join(', ')+'.</div>';

  h+='<div class="m-h">Layer 4 &mdash; branches and chapters, '+GROUPS.length+' dots</div>';
  h+='<div class="m-p">One dot per organisation per country where it has a national presence: a grand lodge, a national church, a regional office, a member delegation, a school network. <b>'+GROUPS.filter(function(g){return !g.est;}).length+'</b> are documented, from the sources named in each organisation\'s popup. <b>'+GROUPS.filter(function(g){return g.est;}).length+'</b> are estimates, drawn as hollow rings: places where no published list confirms a presence but the organisation\'s regional pattern makes one likely.</div>';
  h+='<div class="m-warn">A branch is a country, not an address. Dots sit at the capital on a small fixed ring so that twenty organisations in one capital remain clickable. They never move with zoom. Presence is the channel infiltration would use; it is not evidence that it happened.</div>';

  h+='<div class="m-h">Layer 5 &mdash; channels, '+ROUTES.length+' drawn</div>';
  h+='<div class="m-p">Each channel joins the places named in a record &mdash; a head office and the subsidiaries it moved money through, a command centre and the services it coordinated, a church and the parliament it lobbied. The line is drawn along the shortest path over the globe and split at the date line. It shows that something moved between the places, not the route it took.</div>';

  h+='<div class="m-h">The live wire</div>';
  h+='<div class="m-p">Headlines are leads, not findings. A harvester in the maps repository reads Google News in several languages every six hours and keeps an item only if it names one of the tracked organisations, a public institution, and an act that ties the two together. Nothing in the wire enters the score or the case layer until it earns a forum and a citation.</div>';

  h+='<div class="m-h">Checking the record</div>';
  h+='<div class="m-p"><b>Convicted, acquitted, annulled</b>: a court ruled. <b>Indicted</b>: charges filed, nothing tested. <b>Inquiry</b>: a parliamentary or official commission reported a finding. <b>Designated</b>: a government banned the organisation or expelled people for belonging to it &mdash; an executive act, which in some countries has been used against critics. <b>Acknowledged</b>: the organisation or the government admitted it. <b>Settled</b>: money paid, liability usually denied. <b>Reported</b>: documented by major outlets or historians only.</div>';

  h+='<div class="m-h">Sources</div>';
  h+='<div class="m-p">Conditions: Global Organized Crime Index 2025, Global Initiative Against Transnational Organized Crime. Geometry: world-atlas 50m via jsDelivr. Capitals: countryinfo. Case and organisation citations are on each record. Basemap: the painted plate shared with the other Welcome to Your Galaxy maps, crossfading to Esri World Imagery as you zoom in.</div>';
  document.getElementById('methodBody').innerHTML=h;
}


'''


def edit_list():
    E = []
    R = lambda a, b, c=1: E.append(('rep', a, b, c))
    B = lambda a, b, c: E.append(('block', a, b, c))
    R('<title>Drug Underworld Map — the drug underworld inside states and companies</title>',
      '<title>' + TITLE + ' — lodges, orders and networks inside governments</title>')
    R('<h1>Drug Underworld Map</h1>', '<h1>' + TITLE + '</h1>')
    R('<div class="subtitle">Where the drug underworld sits inside governments and companies — 193 states scored, and the cases that reached a court</div>',
      '<div class="subtitle">' + SUB + '</div>')
    B('<div class="wire-lead">\n      There is no census', '<div class="sub-h" id="methodSubHead">', RUNDOWN)
    R('<span><b id="cSevere">0</b> severe</span><span><b id="cCases">0</b> cases</span><span><b id="cEnt">0</b> firms</span>',
      '<span><b id="cSevere">0</b> severe</span><span><b id="cCases">0</b> cases</span><span><b id="cEnt">0</b> organisations</span>')
    R('<option value="off">List: officials &amp; state cases</option>', '<option value="off">List: documented cases</option>')
    R('<option value="firm">List: companies &amp; firms</option>', '<option value="firm">List: organisations</option>')
    R('<option value="grp">List: crime groups</option>', '<option value="grp">List: branches &amp; chapters</option>')
    R('--accent:#8e1420; --accent-hi:#c9a227; --accent-soft:rgba(201,162,39,0.30);',
      '--accent:#7a2f40; --accent-hi:#c4a5ae; --accent-soft:rgba(170,140,150,0.30);')
    R('--bone:#d8cdb4; --ink:#0a0c14; --brass:#c9a227;', '--bone:#d3cdc8; --ink:#0a0c14; --brass:#a88c96;')
    R('</style>\n</head>', EST_CSS)
    R("var BUCKET_COLOUR = ['#f6288f','#cc36f2','#633ff3','#168cf3','#12d9be'];",
      "var BUCKET_COLOUR = ['#b05666','#8e6aa6','#6f8fb5','#5f9b94','#848a58','#a67f74'];")
    R("var NET_ON = {groups:true, routes:true};", "var NET_ON = {groups:true, routes:true, est:true};")
    R("map.attributionControl.addAttribution('Scores: GI-TOC Organized Crime Index 2025 · Boundaries: Natural Earth / geoBoundaries');",
      "map.attributionControl.addAttribution('Conditions: GI-TOC Organized Crime Index 2025 · Boundaries: Natural Earth');")
    R("'[capture] unmatched geometry names:'", "'[societies] unmatched geometry names:'")
    R("console.error('[capture] '+step[0]", "console.error('[societies] '+step[0]", 2)
    B('/* Four records on this map ended by executive act', 'function openEntity(e){', JS_A)
    B('function openEntity(e){', '/* ---- overlap resolution', JS_OPEN_ENTITY_EXTRA + '\n')
    B('function drawGroups(){', '/* ---- geodesic shaping', JS_GROUPS)
    R("'<div class=\"ci-m\">Trafficking corridor &middot; '+r.p.length+' waypoints'+",
      "'<div class=\"ci-m\">Channel &middot; '+(ORGN[r.org]?('<span data-org=\"'+r.org+'\" style=\"cursor:pointer;text-decoration:underline dotted;\">'+ORGN[r.org]+'</span> &middot; '):'')+r.p.length+' places'+")
    R("""        '<div class="ci-c">The curve is the true shortest path between the waypoints, not a straight '+
        'line drawn on a flat map. It is not a surveyed track: it does not follow roads or shipping '+
        'lanes.</div>').openOn(map);""",
      """        '<div class="ci-c">The line joins the places named in the record along the shortest path over '+
        'the globe. It shows that something moved between them, not the route it took.</div>').openOn(map);""")
    R("(r.trim?(' &middot; '+r.trim+' endpoint'+(r.trim>1?'s':'')+' trimmed'):'')+", "")
    B('function caseHTML(c, folded){', '/* Centre the country in the strip of map', JS_D)
    B('function openCase(c){', '/* The old #unitPanel', JS_OPEN_CASE)
    B('function renderKeys(){', '/* ---- index ----', JS_KEYS)
    B('var STATUS_RANK = {', '/* CASE_BUCKETS is ordered from the presidency downward', JS_STATUS)
    R("title: 'Officials',", "title: 'Cases',")
    R("title: 'Firms',", "title: 'Organisations',")
    R("title: 'Groups',", "title: 'Branches',")
    R("groups: [['sector','Group: sector'],", "groups: [['sector','Group: type'],")
    R("['exp','Sort: host exposure']", "['exp','Sort: country score']")
    R("['noted','Sort: researched first']", "['noted','Sort: documented first']")
    R("if(sort==='noted')   return (typeof b.note==='number')-(typeof a.note==='number') ||",
      "if(sort==='noted')   return (a.est||0)-(b.est||0) ||")
    R("'The figure is the exposure score of the jurisdiction the group sits in, not a measure of the group.</div>'",
      "'The figure is the score of the country the branch sits in, not a measure of the organisation.</div>'")
    R("var WIRE_ARCHIVE_URL = 'wire.json';", "var WIRE_ARCHIVE_URL = 'secret_society_wire.json';")
    R("var WIRE_ARCHIVE_ALT = 'https://welcometoyourgalaxy.github.io/capture-wire/wire.json';",
      "var WIRE_ARCHIVE_ALT = 'https://welcometoyourgalaxy.github.io/maps/secret_society_wire.json';")
    R("var WIRE_LS = 'capture.wire.v1';", "var WIRE_LS = 'societies.wire.v1';")
    R("from=(i===0?'wire.json alongside this file':'capture-wire on GitHub Pages')",
      "from=(i===0?'the archive beside this file':'the maps site')")
    R("'<div class=\"wnote\">No archive reachable. This box reads <code>wire.json</code> '+",
      "'<div class=\"wnote\">No archive reachable. This box reads <code>secret_society_wire.json</code> '+")
    B('var W_ANCHOR = [', 'function _wireTopical(it){', JS_WIRE_VOCAB)
    B('function renderMethod(){', '/* One handler for every panel', JS_METHOD)
    return E


EDITS_JS = True
