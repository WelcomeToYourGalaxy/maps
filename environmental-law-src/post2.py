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
