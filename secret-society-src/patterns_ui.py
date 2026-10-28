"""Second set of shell edits: the patterns-behind-the-scenes layer, the time box, and the
behind-the-scenes section of every country box.

Patterns follow the same data shape as the central bank map's PAT records (id, title, kind,
summary, countries with role and note, links, timeline, confirmed_by, uncertain,
implications) so the two maps read the same way.
"""

HTML_PAT = '''  <div id="patBox">
    <div class="bx-head"><span>Patterns behind the scenes</span><span class="bx-tog">&minus;</span></div>
    <div id="patBody" class="bx-body"><div id="patList"></div><div id="patDetail"></div></div>
  </div>

  <div id="wireBox" class="collapsed">'''

HTML_TIME = '''  <div id="timeBox">
    <div class="bx-head"><span>Through time</span><span class="bx-tog">&minus;</span></div>
    <div id="timeBody" class="bx-body"><div id="timeChart"></div><div id="timeCtl"></div></div>
  </div>

  <div id="indexPanel">'''

CSS = '''<style>
  .pat-row{padding:7px 8px;margin:0 0 5px;border-left:3px solid var(--pc,#7a2f40);border-radius:0 6px 6px 0;
    background:rgba(255,255,255,0.03);cursor:pointer;}
  .pat-row:hover{background:rgba(255,255,255,0.07);}
  .pat-row .pt{font-size:12px;color:#ece6e6;font-weight:600;line-height:1.3;}
  .pat-row .pm{font-size:9.5px;color:#8f97ab;margin-top:2px;letter-spacing:.2px;}
  .pat-lead{font-size:10.5px;color:#9aa2b4;line-height:1.5;margin-bottom:8px;}
  .pat-back{cursor:pointer;color:#c4a5ae;font-size:10.5px;margin-bottom:7px;display:inline-block;}
  .pat-back:hover{text-decoration:underline;}
  .pat-title{font-size:14px;color:#f0ece4;font-weight:600;line-height:1.3;margin-bottom:3px;}
  .pat-kind{font-size:9px;letter-spacing:1px;text-transform:uppercase;color:#8f97ab;margin-bottom:8px;}
  .psec{font-size:9.5px;letter-spacing:1.4px;text-transform:uppercase;color:var(--brass);margin:12px 0 5px;
    padding-bottom:3px;border-bottom:1px solid rgba(170,140,150,0.2);}
  .pat-p{font-size:11.5px;color:#c3c8d6;line-height:1.6;}
  .pat-imp{font-size:11.5px;color:#ddd6dc;line-height:1.6;padding:8px 10px;background:rgba(122,47,64,0.12);
    border-left:3px solid #8c2f3e;border-radius:0 6px 6px 0;}
  .pat-role{display:flex;align-items:center;gap:7px;font-size:11px;color:#c3c8d6;margin:3px 0;}
  .pat-role i{width:11px;height:11px;border-radius:2px;flex:none;}
  .pat-role .n{margin-left:auto;font-family:'DejaVu Sans Mono',monospace;font-size:10px;color:#8f97ab;}
  .tl-row{font-size:10.5px;color:#c3c8d6;line-height:1.45;margin:4px 0;}
  .tl-row b{font-family:'DejaVu Sans Mono',monospace;color:#c9a9b0;font-weight:400;margin-right:5px;}
  .tl-row a{color:#8fb8c9;}
  .pat-src{font-size:10px;color:#8b93a6;line-height:1.5;margin-top:6px;}
  .pat-src a{color:#8fb8c9;}
  .pat-unc{font-size:10.5px;color:#a9a1b0;line-height:1.5;margin-top:6px;font-style:italic;}
  .pat-chip{display:inline-flex;align-items:center;font-size:10.5px;padding:2px 8px;border-radius:10px;cursor:pointer;
    background:rgba(255,255,255,0.045);border:1px solid rgba(255,255,255,0.12);color:#e0dade;margin:2px 4px 2px 0;}
  .pat-chip:hover{background:rgba(255,255,255,0.1);}
  .pat-chip i{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:5px;}
  .pc-item{margin:6px 0 8px;}
  .pc-item .pc-role{font-size:9.5px;letter-spacing:.6px;text-transform:uppercase;color:#a99aa2;margin-left:4px;}
  .pc-item .ci-d{margin-top:3px;}
  .bts{border-left-color:#8c2f3e !important;background:rgba(140,47,62,0.07) !important;}
  .bts .cn-h{color:#c9a9b0 !important;}
  .bts .imp-h{margin-top:9px;}
  .bts .est-tag{font-size:9px;letter-spacing:.8px;text-transform:uppercase;color:#a99ab8;margin-left:6px;}
  #timeChart svg{display:block;width:100%;}
  #timeChart rect.b{fill:#6f5a68;cursor:pointer;} #timeChart rect.b:hover{fill:#a58594;}
  #timeChart rect.b.on{fill:#9c6f7e;} #timeChart rect.hl{fill:#c9a9b0;pointer-events:none;}
  #timeChart text{fill:#8b93a6;font-size:8.5px;font-family:'DejaVu Sans Mono',monospace;}
  #timeCtl{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin-top:7px;font-size:10.5px;color:#9aa2b4;}
  #timeCtl input[type=number]{width:62px;background:rgba(10,14,23,0.85);color:#cdd6e6;border:1px solid var(--accent-soft);
    border-radius:5px;font-size:10.5px;padding:2px 4px;font-family:inherit;}
  #timeCtl .tc-reset{cursor:pointer;color:#c4a5ae;margin-left:auto;}
  #timeCtl .tc-reset:hover{text-decoration:underline;}
  .time-note{font-size:10px;color:#8b93a6;line-height:1.45;margin-top:6px;}
  #patBody{max-height:44vh;}
</style>
</head>'''

JS_PAT = r'''
/* ===================================================================== patterns
   Each pattern colours the countries by the role they play in it, draws the documented
   connections between its places, narrows the points to its own organisations, and opens
   a write-up: what is documented, a timeline, what is not proven, the sources, and what it
   means for a reader who has not followed all of it. Same record shape as the central bank
   map's patterns. */
var PATS = DATA.patterns || [], PAT_BY = {}, ACTIVE_PAT = null, patLayer = null;
PATS.forEach(function(p){ PAT_BY[p.id]=p; });
var PAT_PAL = ['#a3404f','#5d81a8','#7d6da6','#4f8c85','#a67f74','#848a58','#9a93a8','#6a7f99'];
var BTS = DATA.bts || {};
function patStyle(f){
  var k=keyOf(f);
  var r = k ? ACTIVE_PAT.cmap[k] : null;
  if(r==null) return {fillColor:'#0b0e16',fillOpacity:0.42,color:'rgba(170,140,150,0.10)',weight:0.4};
  return {fillColor:PAT_PAL[r%PAT_PAL.length],fillOpacity:0.58,color:'rgba(235,225,230,0.55)',weight:0.8};
}
function patOrgOn(o){ return !ACTIVE_PAT || ACTIVE_PAT.orgs.indexOf(o)>=0; }
function patCaseOn(c){ return !ACTIVE_PAT || (ACTIVE_PAT._cs || (ACTIVE_PAT._cs = (function(){ var s={}; ACTIVE_PAT.cids.forEach(function(i){ s[i]=1; }); return s; })()))[c.i]===1; }
function drawPatLinks(){
  if(patLayer){ map.removeLayer(patLayer); patLayer=null; }
  if(!ACTIVE_PAT) return;
  patLayer=L.layerGroup();
  var keep=[];
  (ACTIVE_PAT.links||[]).forEach(function(l){ var parts=geodesicPath(l.p||[l.a,l.b]); if(parts.length) keep.push({l:l,parts:parts}); else keep.push({l:l,parts:null}); });
  keep.forEach(function(o){ if(o.parts) patLayer.addLayer(L.polyline(o.parts,{color:'#0a0c16',weight:4,opacity:0.55,interactive:false,pane:'lines',renderer:R_LINES})); });
  keep.forEach(function(o){
    var l=o.l;
    if(!o.parts){
      var c=L.circleMarker((l.p&&l.p[0])||l.a,{radius:6,color:'#e6d6dc',weight:1.4,fillOpacity:0,pane:'lines',renderer:R_LINES});
      c.bindTooltip(l.from+' → '+l.to+(l.label?(': '+l.label):''),{sticky:true}); patLayer.addLayer(c); return;
    }
    var pl=L.polyline(o.parts,{color:'#e6d6dc',weight:1.8,opacity:0.95,pane:'lines',renderer:R_LINES});
    pl.bindTooltip(l.from+' → '+l.to+(l.label?(': '+l.label):'')+(l.years?(' ('+l.years+')'):''),{sticky:true});
    pl.on('mouseover',function(){ pl.setStyle({weight:3,color:'#ffffff'}); });
    pl.on('mouseout',function(){ pl.setStyle({weight:1.8,color:'#e6d6dc'}); });
    patLayer.addLayer(pl);
  });
  patLayer.addTo(map);
}
function setPattern(id){
  ACTIVE_PAT = id ? PAT_BY[id] : null;
  if(geoLayer) geoLayer.setStyle(styleC);
  drawCaseDots(); drawEntities(); drawGroups(); drawRoutes(); drawPatLinks();
  renderPatterns(); renderTime(); buildIndex();
  var pb=document.getElementById('patBox');
  if(ACTIVE_PAT && pb.classList.contains('collapsed')){ pb.classList.remove('collapsed'); var t=pb.querySelector('.bx-tog'); if(t) t.innerHTML='−'; }
  if(ACTIVE_PAT && ACTIVE_PAT.view) map.flyToBounds(ACTIVE_PAT.view,{duration:0.8,paddingTopLeft:[340,80],paddingBottomRight:[300,40]});
  fitPanels();
}
function seriesSVG(s){
  if(!s || !s.length) return '';
  var mx=Math.max.apply(null,s.map(function(x){return x[1];}).concat([1])), W=270, H=56, bw=W/s.length;
  var h='<svg viewBox="0 0 '+W+' '+(H+12)+'">';
  s.forEach(function(x,i){
    var bh=H*x[1]/mx;
    h+='<rect x="'+(i*bw+0.5).toFixed(1)+'" y="'+(H-bh).toFixed(1)+'" width="'+Math.max(1,bw-1.2).toFixed(1)+'" height="'+bh.toFixed(1)+'" fill="#9c6f7e"><title>'+x[0]+'s: '+x[1]+'</title></rect>';
    if(i===0 || i===s.length-1 || (x[0]%50===0)) h+='<text x="'+(i*bw).toFixed(1)+'" y="'+(H+10)+'" fill="#8b93a6" font-size="8">'+x[0]+'</text>';
  });
  return h+'</svg>';
}
function patDetailHTML(p){
  var h='<span class="pat-back" data-patclear="1">← All patterns</span>';
  h+='<div class="pat-title">'+p.title+'</div><div class="pat-kind">'+(p.kind||'')+' &middot; '+p.span[0]+'–'+p.span[1]+'</div>';
  h+='<div class="pat-p">'+p.summary+'</div>';
  h+='<div class="psec">Countries by role &mdash; '+Object.keys(p.cmap).length+'</div>';
  p.roles.forEach(function(r,i){
    var n=0; Object.keys(p.cmap).forEach(function(k){ if(p.cmap[k]===i) n++; });
    if(n) h+='<div class="pat-role"><i style="background:'+PAT_PAL[i%PAT_PAL.length]+'"></i>'+r+'<span class="n">'+n+'</span></div>';
  });
  h+='<div class="psec">Documented cases per decade &mdash; '+p.ncases+'</div>'+seriesSVG(p.series);
  if(p.orgs && p.orgs.length){
    h+='<div class="psec">Organisations in this pattern</div><div>'+p.orgs.map(function(k){
      var o=ORG_BY_K[k]; if(!o) return '';
      return '<span class="pat-chip" data-org="'+k+'"><i style="background:'+((SMAP[o.s]||{}).accent||'#888')+'"></i>'+o.n+'</span>';
    }).join('')+'</div>';
  }
  if(p.links && p.links.length){
    h+='<div class="psec">Connections drawn &mdash; '+p.links.length+'</div>'+p.links.map(function(l){
      return '<div class="tl-row">'+l.from+' → '+l.to+(l.label?(': '+l.label):'')+(l.years?(' <span style="color:#8b93a6">'+l.years+'</span>'):'')+'</div>'; }).join('');
  }
  if(p.timeline && p.timeline.length){
    h+='<div class="psec">Timeline</div>'+p.timeline.map(function(t){
      return '<div class="tl-row"><b>'+t.year+'</b>'+t.event+(t.url?(' <a href="'+t.url+'" target="_blank" rel="noopener">source</a>'):'')+'</div>'; }).join('');
  }
  if(p.uncertain) h+='<div class="pat-unc"><b>Not proven:</b> '+p.uncertain+'</div>';
  if(p.confirmed_by && p.confirmed_by.length) h+='<div class="pat-src">Sources: '+p.confirmed_by.map(function(c){
      return c.url?('<a href="'+c.url+'" target="_blank" rel="noopener">'+c.title+'</a>'):c.title; }).join(' &middot; ')+'</div>';
  if(p.implications) h+='<div class="psec">What this means</div><div class="pat-imp">'+p.implications+'</div>';
  return h;
}
function renderPatterns(){
  var L_=document.getElementById('patList'), D_=document.getElementById('patDetail');
  if(ACTIVE_PAT){ L_.innerHTML=''; D_.innerHTML=patDetailHTML(ACTIVE_PAT); return; }
  D_.innerHTML='';
  var h='<div class="pat-lead">The cases on this map are not isolated. These are the arrangements that recur across them &mdash; the same people, banks, lodges and services turning up in different countries and decades. Pick one to colour the map by it.</div>';
  PATS.forEach(function(p,i){
    h+='<div class="pat-row" data-pat="'+p.id+'" style="--pc:'+PAT_PAL[i%PAT_PAL.length]+'"><div class="pt">'+p.title+'</div>'+
       '<div class="pm">'+Object.keys(p.cmap).length+' countries &middot; '+p.ncases+' cases &middot; '+p.span[0]+'–'+p.span[1]+'</div></div>';
  });
  L_.innerHTML=h;
}
/* Patterns a country plays a part in, then its behind-the-scenes write-up. */
function patsHTML(k){
  var ps=PATS.filter(function(p){ return p.cmap[k]!=null; });
  var b=BTS[k], h='';
  if(b){
    h+='<div class="cnote bts"><div class="cn-h">Behind the scenes'+(b.est?'<span class="est-tag">estimate</span>':'')+'</div><div class="ci-d cn-body">'+b.d+'</div>'+
       (b.imp?('<div class="cn-h imp-h">What this means</div><div class="ci-d cn-body">'+b.imp+'</div>'):'')+'</div>';
  }
  if(ps.length){
    h+='<div class="pres-h">Patterns behind the scenes &mdash; '+ps.length+'</div>';
    ps.forEach(function(p){
      var ri=p.cmap[k], note=(p.cnotes||{})[k]||'';
      h+='<div class="pc-item"><span class="pat-chip" data-pat="'+p.id+'"><i style="background:'+PAT_PAL[ri%PAT_PAL.length]+'"></i>'+p.title+'</span>'+
         '<span class="pc-role">'+p.roles[ri]+'</span>'+(note?('<div class="ci-d">'+note+'</div>'):'')+'</div>';
    });
  }
  return h;
}
document.addEventListener('click',function(ev){
  var t=ev.target && ev.target.closest ? ev.target.closest('[data-pat],[data-patclear]') : null;
  if(!t) return;
  ev.stopPropagation();
  if(t.hasAttribute('data-patclear')){ setPattern(null); return; }
  var id=t.getAttribute('data-pat');
  map.closePopup();
  setPattern(ACTIVE_PAT && ACTIVE_PAT.id===id ? null : id);
},true);

/* ===================================================================== time
   Cases per decade. Click a bar to keep only that decade's cases on the map, or type a
   range. When a pattern is open its own cases are drawn over the bars. */
var YR_MIN=9999, YR_MAX=0;
CASES.forEach(function(c){ if(c.y){ YR_MIN=Math.min(YR_MIN,c.y); YR_MAX=Math.max(YR_MAX,c.y); } });
var YR=[YR_MIN,YR_MAX];
function yrOK(c){ return !c.y || (c.y>=YR[0] && c.y<=YR[1]); }
function renderTime(){
  var d0=Math.floor(YR_MIN/10)*10, d1=Math.floor(YR_MAX/10)*10, dec=[];
  for(var d=d0; d<=d1; d+=10) dec.push(d);
  var cnt={}, pc={};
  CASES.forEach(function(c){ if(!c.y) return; var d=Math.floor(c.y/10)*10; cnt[d]=(cnt[d]||0)+1;
    if(ACTIVE_PAT && patCaseOn(c)) pc[d]=(pc[d]||0)+1; });
  var mx=Math.max.apply(null, dec.map(function(d){return cnt[d]||0;}).concat([1]));
  var W=270, H=64, bw=W/dec.length;
  var h='<svg viewBox="0 0 '+W+' '+(H+12)+'">';
  dec.forEach(function(d,i){
    var n=cnt[d]||0, bh=H*n/mx, on=(YR[0]<=d && YR[1]>=d+9);
    h+='<rect class="b'+(on&&(YR[0]!==YR_MIN||YR[1]!==YR_MAX)?' on':'')+'" data-dec="'+d+'" x="'+(i*bw+0.5).toFixed(1)+'" y="'+(H-bh).toFixed(1)+'" width="'+Math.max(1,bw-1).toFixed(1)+'" height="'+Math.max(0.5,bh).toFixed(1)+'"><title>'+d+'s: '+n+' cases</title></rect>';
    if(pc[d]){ var ph=H*pc[d]/mx; h+='<rect class="hl" x="'+(i*bw+0.5).toFixed(1)+'" y="'+(H-ph).toFixed(1)+'" width="'+Math.max(1,bw-1).toFixed(1)+'" height="'+ph.toFixed(1)+'"></rect>'; }
    if(d%50===0 || i===0) h+='<text x="'+(i*bw).toFixed(1)+'" y="'+(H+10)+'">'+d+'</text>';
  });
  h+='</svg>';
  var shown=CASES.filter(function(c){ return yrOK(c) && patCaseOn(c); }).length;
  document.getElementById('timeChart').innerHTML=h;
  document.getElementById('timeCtl').innerHTML='From <input type="number" id="yr0" value="'+YR[0]+'"> to <input type="number" id="yr1" value="'+YR[1]+'">'+
    '<span class="tc-reset" id="yrReset">All years</span>'+
    '<div class="time-note" style="flex-basis:100%">'+shown+' cases on the map'+(ACTIVE_PAT?(' in &ldquo;'+ACTIVE_PAT.title+'&rdquo; (pale bars)'):'')+'. Click a bar to keep one decade.</div>';
  document.getElementById('yr0').onchange=function(){ YR[0]=+this.value||YR_MIN; drawCaseDots(); renderTime(); };
  document.getElementById('yr1').onchange=function(){ YR[1]=+this.value||YR_MAX; drawCaseDots(); renderTime(); };
  document.getElementById('yrReset').onclick=function(){ YR=[YR_MIN,YR_MAX]; drawCaseDots(); renderTime(); };
  Array.prototype.forEach.call(document.querySelectorAll('#timeChart rect.b'),function(r){
    r.onclick=function(){ var d=+r.getAttribute('data-dec'); if(YR[0]===d && YR[1]===d+9){ YR=[YR_MIN,YR_MAX]; } else { YR=[d,d+9]; } drawCaseDots(); renderTime(); };
  });
}
'''


def edit_list():
    E = []
    R = lambda a, b, c=1: E.append(('rep', a, b, c))
    R('  <div id="wireBox">', HTML_PAT)
    R('  <div id="indexPanel">', HTML_TIME)
    R('</style>\n</head>', CSS)
    # choropleth: pattern colouring when a pattern is open
    R("function styleC(f){\n  var k=keyOf(f);", "function styleC(f){\n  if(ACTIVE_PAT) return patStyle(f);\n  var k=keyOf(f);")
    # points obey the time filter and the open pattern
    R("  CASES.forEach(function(c){\n    if(!CBK_ON[c.bk]) return;",
      "  CASES.forEach(function(c){\n    if(!CBK_ON[c.bk]) return;\n    if(!yrOK(c) || !patCaseOn(c)) return;")
    R("  ENTITIES.forEach(function(e){\n    if(!SON[e.s]) return;",
      "  ENTITIES.forEach(function(e){\n    if(!SON[e.s]) return;\n    if(!patOrgOn(e.k)) return;")
    R("  if(!NET_ON.groups){ declSoon(); return; }\n  groupLayer=L.layerGroup();",
      "  if(!NET_ON.groups || ACTIVE_PAT){ declSoon(); return; }\n  groupLayer=L.layerGroup();")
    R("  if(!NET_ON.routes) return;", "  if(!NET_ON.routes || ACTIVE_PAT) return;")
    # pattern code sits before the geometry fetch so everything it names exists
    R("fetch('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json')", JS_PAT + "\nfetch('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json')")
    R("   drawCaseDots(); drawEntities(); buildIndex(); renderMethod();",
      "   drawCaseDots(); drawEntities(); buildIndex(); renderMethod(); renderPatterns(); renderTime();")
    return E
