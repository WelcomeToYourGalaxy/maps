# -*- coding: utf-8 -*-
# Third edition engine changes: the keystone legal instruments layer and the atlas's notes on each actor.
sub("""fetch(LAWS.base + encodeURIComponent(id) + ".json")""", """fetch((id.charAt(0) === "_" ? LAWS.globbase : LAWS.base) + encodeURIComponent(id) + ".json")""")
sub("""  map.addSource("players", { type: "geojson", data: FC([]) });""", """  map.addSource("players", { type: "geojson", data: FC([]) });
  map.addSource("instr", { type: "geojson", data: FC(INSTR.map((x, i) => ptF(x.ll, { i, n: x.n, y: x.y || "", k: x.pro ? 2 : x.tier === "international" ? 0 : 1 }))) });""")
sub("""  map.getSource("arcsAll").setData(overviewArcs());
  setPlayers();""", """  addL({ id: "instr", type: "symbol", source: "instr", layout: { visibility: "none", "icon-image": "dia", "icon-size": ["interpolate", ["linear"], ["zoom"], 1, 0.34, 6, 0.5], "icon-allow-overlap": true },
    paint: { "icon-color": instrCol(), "icon-halo-color": P.halo, "icon-halo-width": 1.4 } });
  map.getSource("arcsAll").setData(overviewArcs());
  setPlayers();""")
sub("""  map.setPaintProperty("cty-line", "line-color", P.ln);""", """  map.setPaintProperty("cty-line", "line-color", P.ln);
  if (map.getLayer("instr")) { map.setPaintProperty("instr", "icon-color", instrCol()); map.setPaintProperty("instr", "icon-halo-color", P.halo); }""")
sub("""  vis("ex", S.ex);""", """  vis("ex", S.ex); vis("instr", S.instr || INSTEP);""")
sub("""  if (!!s.top !== TOPSTEP) { TOPSTEP = !!s.top; setPlayers(); }""", """  if (!!s.top !== TOPSTEP) { TOPSTEP = !!s.top; setPlayers(); }
  INSTEP = !!s.instr; vis("instr", S.instr || INSTEP);""")
sub("""  if (TOPSTEP) { TOPSTEP = false; setPlayers(); }""", """  if (TOPSTEP) { TOPSTEP = false; setPlayers(); }
  INSTEP = false; vis("instr", S.instr);""")
sub("""vis(id, S.players && !s.data && !s.net));""", """vis(id, S.players && !s.data && !s.net && !s.instr));""")
sub("""const hoverable = ["players", """, """const hoverable = ["instr", "players", """)
sub("""    else if (f.layer.id === "dots") tip(""", """    else if (f.layer.id === "instr") tip('<b>' + esc(p.n) + '</b><br><span class="mute">Legal instrument' + (p.y ? ' · ' + esc(p.y) : '') + '</span>', oe.clientX, oe.clientY);
    else if (f.layer.id === "dots") tip(""")
sub("""{ layers: ["players", "ex-story", "ex", "arcs-hit"]""", """{ layers: ["instr", "players", "ex-story", "ex", "arcs-hit"]""")
sub("""      if (f.layer.id === "players") return openPlayer(p.k, false);""", """      if (f.layer.id === "instr") return openInstr(p.i, false);
      if (f.layer.id === "players") return openPlayer(p.k, false);""")
sub("""  $$("[data-laws]", root).forEach(""", """  $$("[data-instr]", root).forEach((a) => a.addEventListener("click", (e) => { e.preventDefault(); openInstr(+a.dataset.instr, true); }));
  $$("[data-laws]", root).forEach(""")
sub("""else if (s[0] === "l") {""", """else if (s[0] === "i") openInstr(+s[1], false); else if (s[0] === "l") {""")
sub("""l: "list of laws" };""", """l: "list of laws", i: "legal instrument" };""")
sub("""  const owns = p.links || [], by = OWNED_BY[p.k] || [];""", """  if (p.atlas) h += atlasBlock(p);
  const owns = p.links || [], by = OWNED_BY[p.k] || [];""")
sub("""  if (LAWS) h += '<div class="psec">The law atlas</div>""", """  h += '<label class="chk"><input type="checkbox" data-lay="instr"' + (S.instr ? " checked" : "") + '><span class="sw dia" style="background:' + P.role[1] + '"></span>Legal instruments most responsible <span class="n" style="margin-left:auto">' + INSTR.length + '</span></label>' +
    '<div class="desc">The keystone treaties, laws, rulings and contracts compiled in the Environmental Law Atlas, each placed where it was adopted or decided. <span class="sw dia" style="background:' + P.role[0] + '"></span>international · <span class="sw dia" style="background:' + P.role[1] + '"></span>national · <span class="sw dia" style="background:' + P.role[2] + '"></span>written to protect. Click one for what it says and who stands behind it.</div>';
  if (LAWS) h += '<div class="psec">The law atlas</div>""")
sub("""/* ---------- the law atlas: lists fetched when asked for ---------- */""", r"""/* ---------- the keystone legal instruments and the atlas's notes on each actor ---------- */
const INSTR = D.instr || [], INSTRBY = {}; INSTR.forEach((x, i) => { INSTRBY[x.n] = i; });
let INSTEP = false;
const instrCol = () => ["match", ["get", "k"], 0, P.role[0], 1, P.role[1], P.role[2]];
const FLAGTXT = { foundational: "Foundational: sets up the framework the rest is built on", invasive: "Invasive: opens land, sea or seabed to extraction", destructive: "Destructive: licenses or subsidises the damage", suppressive: "Suppressive: blocks the people or courts that would stop it" };
const instrChip = (n) => INSTRBY[n] == null ? "" : '<div class="fref" data-instr="' + INSTRBY[n] + '" style="--fc:' + P.role[1] + '"><b>' + esc(n) + '</b></div>';
function atlasBlock(p) {
  const a = p.atlas; let h = '<div class="hp-h">From the Environmental Law Atlas</div><div class="hp-desc">' + esc(a.more || a.d) + '</div><div class="sub">' +
    [a.office && "Where it acts: " + a.office, a.now && "Who runs it now: " + a.now, a.status && "Status: " + a.status, a.ctl && "Control: " + a.ctl, "Weight in the atlas: " + a.w + " of 6"].filter(Boolean).map(esc).join("<br>") + '</div>';
  if (a.laws.length) h += '<div class="hp-h">Legal instruments it stands behind</div>' + a.laws.map(instrChip).join("");
  return h;
}
function openInstr(i, fly) {
  const x = INSTR[i]; if (!x) return;
  let h = '<div class="hp-k">Legal instrument · ' + esc(x.tier) + (x.br ? ' · ' + esc(x.br) : '') + (x.pro ? ' · written to protect' : '') + '</div><h3>' + esc(x.n) + '</h3>' +
    '<div class="hp-sub">' + esc([x.y, x.w].filter(Boolean).join(" · ")) + '</div>' +
    (x.fl.length ? '<div class="sub">' + x.fl.map((f) => esc(FLAGTXT[f] || f)).join("<br>") + '</div>' : '') +
    '<div class="hp-desc">' + esc(x.what) + '</div>' +
    (x.read ? '<div class="imp-box">' + esc(x.read) + '</div>' : '') +
    (x.who ? '<div class="hp-h">Who stands behind it</div><div class="hp-desc">' + esc(x.who) + '</div>' : '') +
    (x.body ? '<div class="sub">Body: ' + esc(x.body) + '</div>' : '') +
    (x.act.length ? '<div class="hp-h">Actors on this map tied to it</div><div class="chips">' + x.act.map(plChip).join("") + '</div>' : '') +
    '<div class="hp-src">' + (x.sn ? esc(x.sn) + ' — ' : '') + (x.src ? '<a href="' + esc(x.src) + '" target="_blank" rel="noopener">' + esc(host(x.src)) + '</a>' : '') +
    '<br><span class="mute">Compiled in the Environmental Law Atlas. Placed where it was adopted or decided.</span></div>';
  show('<div class="hp">' + h + '</div>', ["i", i]);
  if (fly) { S.instr = true; buildLeg(); paintOverview(); map.flyTo({ center: x.ll, zoom: Math.max(map.getZoom(), 3.5), padding: pad(), duration: 1200 }); }
}

/* ---------- the law atlas: lists fetched when asked for ---------- */""")

# ================= fourth edition
sub("""["players", "players-fp", "players-lab"].forEach((id) => vis(id, S.players));""", """["players", "players-fp", "players-lab"].forEach((id) => vis(id, S.players && !INSTEP));""", 0)
sub("""vis("instr", S.instr || INSTEP);""", """vis("instr", S.instr || INSTEP || !!(S.sel && S.sel[0] === "i"));""", 0)
sub("""  if (fly) { S.instr = true; buildLeg(); paintOverview(); map.flyTo(""", """  if (fly) { map.flyTo(""")
sub(""" · <span class="sw dia" style="background:' + P.role[2] + '"></span>written to protect. Click one""", """. Click one""")
sub("""const instrCol = () => ["match", ["get", "k"], 0, P.role[0], 1, P.role[1], P.role[2]];""", """const instrCol = () => ["match", ["get", "k"], 0, P.role[0], P.role[1]];""")
sub("""'<br><span class="mute">Compiled in the Environmental Law Atlas. Placed""", """'<br><span class="mute">' + (x.added ? 'Added by this map to the atlas\\'s compilation. Placed' : 'Compiled in the Environmental Law Atlas. Placed') + '""")
sub("""  const a = p.atlas; let h = '<div class="hp-h">From the Environmental Law Atlas</div>""", """  const a = p.atlas; let h = '<div class="hp-h">From the Environmental Law Atlas</div>' + (a.name && a.name !== p.n ? '<div class="sub">Listed in the atlas as: ' + esc(a.name) + '</div>' : '') + '""")
sub(r"""esc(s.t).replace(/\n\n/g, "<br><br>") + '</div>' +""", r"""esc(s.t).replace(/\n\n/g, "<br><br>") + '</div>' +
    (s.more ? '<details class="cb-more" style="margin:6px 0"><summary>' + esc(s.more[0]) + '</summary><div class="sl-m" style="max-height:34vh;overflow:auto">' + s.more[1] + '</div></details>' : '') +""")
sub("""else if (k === "c") openCountry(v, true); else openExample(+v, true);""", """else if (k === "c") openCountry(v, true); else if (k === "i") openInstr(+v, true); else openExample(+v, true);""", 0)
sub("""if ((p.n + " " + p.city + " " + p.c).toLowerCase().includes(q))""", """if ((p.n + " " + p.city + " " + p.c + " " + (p.atlas ? p.atlas.name : "")).toLowerCase().includes(q))""")
sub("""  EX.forEach((e) => { if ((e.n + " " + e.c).toLowerCase().includes(q))""", """  INSTR.forEach((x, i) => { if ((x.n + " " + x.w).toLowerCase().includes(q)) out.push(["i", i, x.n, "legal instrument · " + (x.y || "")]); });
  EX.forEach((e) => { if ((e.n + " " + e.c).toLowerCase().includes(q))""")
sub("""ixE.map(ixRow).join("") + '</details></details>';""", """ixE.map(ixRow).join("") + '</details><details><summary>Legal Instruments (' + INSTR.length + ')</summary>' + INSTR.map((x, i) => [x.n, "i", i, String(x.y || "")]).sort(az).map(ixRow).join("") + '</details></details>';""")
# the network view: the atlas's actors grouped by field, tied to the instruments they stand behind
sub("""<div id="infoBtn" class="card" role="button" tabindex="0">""", """<div id="netBtn" class="card" role="button" tabindex="0">Network</div><div id="infoBtn" class="card" role="button" tabindex="0">""")
sub("""<div id="chapBox"></div>""", """<div id="net" class="card scroll"><div id="netHead"><b>The Network of Actors and Laws</b><span>The actors of the Environmental Law Atlas, grouped by field, each tied to the legal instruments it stands behind. Circles are actors and larger ones carry more weight; diamonds are instruments, pale for international and darker for national. Hover to trace a body's ties; click to open it.</span></div><div id="netBody"></div></div>
<button id="netClose" class="btn" type="button">Close</button>
<div id="chapBox"></div>""")
sub("""</style>""", """#net{inset:0;z-index:1001;border-radius:0;border:0;display:none;overflow:auto;padding:14px 18px 18px;background:rgba(5,8,10,.975)}
#net.open{display:block}#netClose{position:fixed;top:12px;right:12px;z-index:1002;display:none}#net.open+#netClose{display:block}
#netHead{max-width:900px;margin:0 90px 4px 0;font-size:12.5px;color:var(--mute);line-height:1.45}#netHead b{display:block;font:400 19px/1.3 'Marcellus',Georgia,serif;letter-spacing:1.6px;text-transform:uppercase;color:#f0ece4;margin-bottom:2px}
#netBody svg{display:block;width:100%;height:auto;min-width:1100px}#netBody text{font-family:'Marcellus',Georgia,serif;fill:#e8e6e1;pointer-events:none}
#netBody .ln{stroke-width:.8;opacity:.45;fill:none}#netBody .nd{cursor:pointer}#netBody svg.hot .ln{opacity:.04}#netBody svg.hot .nd{opacity:.25}#netBody svg.hot .on{opacity:1!important}#netBody svg.hot .ln.on{stroke-width:1.4}
</style>""")
sub("""  $("#detX").addEventListener("click", closeDet);""", """  $("#detX").addEventListener("click", closeDet);
  $("#netBtn").addEventListener("click", () => { drawNet(); $("#net").classList.add("open"); }); $("#netClose").addEventListener("click", () => $("#net").classList.remove("open"));""")
sub("""/* ---------- the law atlas: lists fetched when asked for ---------- */""", r"""/* ---------- the network view ---------- */
function drawNet() {
  const W = 1700, H = 1080, cx = W / 2, cy = H / 2, FN = { energy: "Energy", mining: "Mining", land: "Land, Farming and Forests", trade: "Trade and Investment", ideology: "Courts, Think Tanks and Doctrine" };
  const order = ["energy", "trade", "mining", "ideology", "land"], acts = PLAY.filter((p) => p.atlas), pos = {}, ipos = {}, cen = {};
  let s = "", lines = "", nodes = "";
  order.forEach((f, fi) => {
    const arr = acts.filter((p) => p.atlas.field === f).sort((a, b) => b.atlas.w - a.atlas.w), ang = (-90 + fi * 72) * Math.PI / 180, c = [cx + Math.cos(ang) * 470, cy + Math.sin(ang) * 300], R = Math.max(60, 4.6 * arr.length + 30);
    cen[f] = { c, R, ang };
    arr.forEach((p, i) => { const a = i / arr.length * 2 * Math.PI - Math.PI / 2; pos[p.k] = [c[0] + Math.cos(a) * R * (i % 2 ? 1 : 0.62), c[1] + Math.sin(a) * R * (i % 2 ? 1 : 0.62), f]; });
    s += '<text x="' + c[0] + '" y="' + (c[1] - R - 54) + '" text-anchor="middle" font-size="15" style="letter-spacing:1.5px;text-transform:uppercase;fill:#b9c7b4">' + esc(FN[f]) + '</text>';
  });
  const byF = {}; INSTR.forEach((x, i) => { const cnt = {}; x.act.forEach((k) => { if (pos[k]) cnt[pos[k][2]] = (cnt[pos[k][2]] || 0) + 1; }); const f = Object.keys(cnt).sort((a, b) => cnt[b] - cnt[a])[0] || "none"; (byF[f] = byF[f] || []).push(i); });
  order.forEach((f) => { const ls = byF[f] || [], g = cen[f]; ls.forEach((i, j) => { const a = j / Math.max(1, ls.length) * 2 * Math.PI + 0.2, rr = g.R + 26 + (j % 3) * 9; ipos[i] = [g.c[0] + Math.cos(a) * rr, g.c[1] + Math.sin(a) * rr]; }); });
  (byF.none || []).forEach((i, j, arr) => { ipos[i] = [60 + (W - 120) * (j + 0.5) / arr.length, H - 34 - (j % 3) * 11]; });
  const col = (f) => ({ energy: "#9a8fb8", trade: "#b98a96", mining: "#a9a59a", ideology: "#b0708a", land: "#8fae9a" })[f];
  INSTR.forEach((x, i) => { x.act.forEach((k) => { if (pos[k]) lines += '<path class="ln" data-a="' + k + '" data-i="' + i + '" stroke="' + col(pos[k][2]) + '" d="M' + pos[k][0].toFixed(1) + ' ' + pos[k][1].toFixed(1) + ' L' + ipos[i][0].toFixed(1) + ' ' + ipos[i][1].toFixed(1) + '"/>'; });
    nodes += '<rect class="nd" data-i="' + i + '" x="' + (ipos[i][0] - 3.2).toFixed(1) + '" y="' + (ipos[i][1] - 3.2).toFixed(1) + '" width="6.4" height="6.4" transform="rotate(45 ' + ipos[i][0].toFixed(1) + ' ' + ipos[i][1].toFixed(1) + ')" fill="' + (x.tier === "international" ? "#c9d3cf" : "#7f9488") + '" stroke="#05080a" stroke-width=".8"><title>' + esc(x.n) + '</title></rect>'; });
  acts.forEach((p) => { const q = pos[p.k], r = 3 + p.atlas.w * 1.7;
    nodes += '<circle class="nd" data-a="' + p.k + '" cx="' + q[0].toFixed(1) + '" cy="' + q[1].toFixed(1) + '" r="' + r + '" fill="' + col(q[2]) + '" stroke="#05080a" stroke-width="1.2"><title>' + esc(p.n) + '</title></circle>' +
      (p.atlas.w >= 5 ? '<text x="' + q[0].toFixed(1) + '" y="' + (q[1] - r - 4).toFixed(1) + '" text-anchor="middle" font-size="11" style="paint-order:stroke;stroke:#05080a;stroke-width:3px">' + esc(p.n.length > 30 ? p.n.slice(0, 29) + "…" : p.n) + '</text>' : ''); });
  if ((byF.none || []).length) s += '<text x="60" y="' + (H - 66) + '" font-size="11.5" style="fill:#b9c7b4">Instruments with no single named actor</text>';
  $("#netBody").innerHTML = '<svg viewBox="0 -40 ' + W + ' ' + (H + 40) + '">' + lines + s + nodes + '</svg>';
  const svg = $("#netBody svg");
  const lit = (sel) => { svg.classList.add("hot"); $$(sel, svg).forEach((l) => { l.classList.add("on"); const a = $('.nd[data-a="' + l.dataset.a + '"]', svg), b = $('.nd[data-i="' + l.dataset.i + '"]', svg); if (a) a.classList.add("on"); if (b) b.classList.add("on"); }); };
  $$(".nd", svg).forEach((n) => {
    n.addEventListener("mouseenter", (e) => { n.classList.add("on"); lit(n.dataset.a ? '.ln[data-a="' + n.dataset.a + '"]' : '.ln[data-i="' + n.dataset.i + '"]'); const t = n.dataset.a ? PBY[n.dataset.a].n : INSTR[+n.dataset.i].n; tip('<b>' + esc(t) + '</b><br><span class="mute">' + (n.dataset.a ? 'Weight ' + PBY[n.dataset.a].atlas.w + ' of 6 · ' + PBY[n.dataset.a].atlas.laws.length + ' instruments' : 'Legal instrument · ' + (INSTR[+n.dataset.i].y || "")) + '</span>', e.clientX, e.clientY); });
    n.addEventListener("mouseleave", () => { svg.classList.remove("hot"); $$(".on", svg).forEach((x) => x.classList.remove("on")); tip(null); });
    n.addEventListener("click", () => { tip(null); $("#net").classList.remove("open"); if (n.dataset.a) openPlayer(n.dataset.a, true); else openInstr(+n.dataset.i, true); });
  });
}

/* ---------- the law atlas: lists fetched when asked for ---------- */""")

# ================= fifth edition
sub("""{ i, n: x.n, y: x.y || "", k: x.pro ? 2 : x.tier === "international" ? 0 : 1 }""", """{ i, n: x.n, y: x.y || "", k: x.pro ? 1 : 0 }""")
sub("""const instrCol = () => ["match", ["get", "k"], 0, P.role[0], P.role[1]];""", """const GOODC = "#dfe8d8", BADC = "#7d3f4c";
const instrCol = () => ["match", ["get", "k"], 1, GOODC, BADC];""")
sub("""<span class="sw dia" style="background:' + P.role[1] + '"></span>Legal instruments most responsible""", """<span class="sw dia" style="background:' + BADC + '"></span>Keystone legal instruments""")
a = h.index("""'<div class="desc">The keystone treaties, laws, rulings and contracts"""); b = h.index("""</div>';""", a) + len("""</div>';""")
h = h[:a] + """'<div class="desc">The treaties, laws, rulings and contracts that set the pattern for the rest, each placed where it was adopted or decided. <span class="sw dia" style="background:' + GOODC + '"></span>written to protect · <span class="sw dia" style="background:' + BADC + '"></span>licenses, shields or suppresses. Click one for what it says and who stands behind it.</div>';""" + h[b:]
sub("""fill="' + (x.tier === "international" ? "#c9d3cf" : "#7f9488") + '\"""", """fill="' + (x.pro ? GOODC : BADC) + '\"""")
sub("""diamonds are instruments, pale for international and darker for national.""", """diamonds are instruments, pale where written to protect and dark where they license, shield or suppress.""")
sub("""The actors of the Environmental Law Atlas, grouped by field""", """The actors behind the keystone legal instruments, grouped by field""")
sub("""    (s.more ? '<details class="cb-more\"""", """    (s.netbtn ? '<div class="sl-m" style="margin-top:8px"><button type="button" class="btn" id="slNet" style="margin:0 0 5px">Open the network view</button><br>' + esc(s.netbtn) + '</div>' : '') +
    (s.more ? '<details class="cb-more\"""")
sub("""  $("#slideX").addEventListener("click", () => {""", """  if ($("#slNet")) $("#slNet").addEventListener("click", () => { pauseTL(); drawNet(); $("#net").classList.add("open"); });
  $("#slideX").addEventListener("click", () => {""")
sub("""'<a href="' + esc(p.url) + '" target="_blank" rel="noopener">' + esc(host(p.url)) + '</a>'""", """(p.url ? '<a href="' + esc(p.url) + '" target="_blank" rel="noopener">' + esc(host(p.url)) + '</a>' : '')""")
sub("""(p.cite ? esc(p.cite) + ' — ' : '')""", """(p.cite && p.url ? esc(p.cite) + ' — ' : '')""")
for x, y in [("From the Environmental Law Atlas", "Background"), ("Listed in the atlas as: ", "Also listed as: "), ("Weight in the atlas: ", "Weight: "),
             ("""(x.added ? 'Added by this map to the atlas\\'s compilation. Placed' : 'Compiled in the Environmental Law Atlas. Placed')""", """'Placed'"""),
             (""" Compiled in the <a href="' + LAWS.full + '" target="_blank" rel="noopener">Environmental Law Atlas</a>.""", ""),
             ("""'<div class="desc"><a href="' + LAWS.full + '" target="_blank" rel="noopener">Open the full law atlas in its own map</a></div>'""", "''")]:
    sub(x, y)
h = re.sub(r'"full":"[^"]*",', "", h, 1)
assert "Environmental Law Atlas" not in h and "destruction-environment-law-map" not in h, [h[m.start()-80:m.start()+60] for m in re.finditer("Environmental Law Atlas|destruction-environment-law-map", h)][:3]
