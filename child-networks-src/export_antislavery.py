#!/usr/bin/env python3
"""export_antislavery.py -- carry the child abuse networks map into the anti-slavery map.

    python3 build.py && python3 export_antislavery.py [path/to/anti-slavery-map]

Writes, in the anti-slavery repo:
  child_networks.json   the built data (cases, networks, lines, patterns, country writeups, indicators)
  engine/child.js       this map's app, adapted to run inside that map: it draws on that map's MapLibre map,
                        puts its key and the basemap chooser in that map's "Map key", adds its country section
                        to that map's country box, and keeps that map's colors.
Then run engine/inline.py in that repo to fold engine/ into index.html.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEST = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(HERE)), 'anti-slavery-map')
D = json.load(open(os.path.join(HERE, 'data', 'built.json')))
src = open(os.path.join(HERE, 'shell', 'app.js')).read()


def rep(a, b, n=1):
    global src
    c = src.count(a)
    assert c == n, (a[:80], c)
    src = src.replace(a, b)


def cut(start, end, new, keep_end=False):
    """Replace from `start` up to (not including) `end`."""
    global src
    i = src.index(start); j = src.index(end, i)
    src = src[:i] + new + (src[j:] if keep_end else src[j + len(end):])


# ---------------------------------------------------------------- wrapper: wait for the data and the map
rep('''(function () {
"use strict";
if (typeof navigator !== "undefined" && navigator.userAgent === "node") return;
''', '''(function () {
"use strict";
if (typeof window === "undefined" || !window.maplibregl || !window.CulpritsBasemaps) return;
function boot() {
  fetch("child_networks.json", { cache: "no-store" }).then((r) => r.ok ? r.json() : null).catch(() => null)
    .then((j) => j || (window.__BUNDLED && window.__BUNDLED["child_networks.json"]) || null)
    .then((D) => { if (!D) { console.warn("[child networks] child_networks.json not found"); return; }
      const go = () => { try { start(D); } catch (e) { console.error("[child networks]", e); } };
      if (window.__shimIsReady) go(); else (window.__shimReady = window.__shimReady || []).push(go); });
}
function start(D) {
mountUI();
''')

# ---------------------------------------------------------------- colors: the anti-slavery map's earth tones
cut('/* ---------- colors ---------- */', 'const ramp = ', '''/* ---------- colors ---------- */
// One set for every basemap, from the host map's own tones: its olive, dark to pale, for the countries,
// and muted earth colors for the eight settings (no yellow, no orange, no neon).
const EARTH = ["#23271a", "#41472e", "#666d4c", "#989d80", "#d1d4c1"];
const RAMPS = { night: EARTH, outlines: EARTH, satellite: EARTH, atlas: EARTH, hell: EARTH };
const PAL8 = ["#e4d4ad", "#9fb6cc", "#b99ad0", "#c98ac0", "#7fb3d0", "#8fc1a9", "#c98f7a", "#b9bf86"];
const SETPAL = { night: PAL8, outlines: PAL8, satellite: PAL8, atlas: PAL8, hell: PAL8 };
const CATC = ["#d1d4c1", "#989d80", "#5f6646", "#33381f"];
const OTHER = "#8b8578", NODATA = "rgba(0,0,0,0)";
let BASE = "atlas";
''', keep_end=True)

# ---------------------------------------------------------------- the map is the host map's
cut('const BM = CulpritsBasemaps.create("map",', 'function hideNames() {', '''const BM = window.__BM;
const map = window.cnMap = window.__ml;
BASE = BM.current() || "atlas";
proj = (map.getProjection && map.getProjection() && map.getProjection().type) || "globe";
(window.__bmListeners = window.__bmListeners || []).push((k) => { BASE = k; if (!S.names) setTimeout(hideNames, 0); if (ready) { order(); update(); } });
// The host map's panels: the two columns on the left and the column on the right.
function panelRight() { let r = 0; ["#sidebar", "#helpPanel", "#indexPanel", "#wirePanel"].forEach((s) => { const e = $(s); if (!e) return; const b = e.getBoundingClientRect(); if (b.width && b.right < innerWidth * 0.6) r = Math.max(r, b.right + 10); }); return r; }
function rightBox() { const e = $("#rightbar"); if (!e) return 0; const b = e.getBoundingClientRect(); return b.width && b.left > innerWidth * 0.5 ? innerWidth - b.left + 10 : 0; }
function hideNames() {''', keep_end=False)
src = src.replace('function hideNames() {function hideNames() {', 'function hideNames() {')

rep('''function order() { const st = map.getStyle(); if (!st) return; const mine = new Set(IDS); const first = st.layers.find((l) => !mine.has(l.id) && (l.type === "symbol" || l.id === "labels")); IDS.forEach((id) => { if (map.getLayer(id)) map.moveLayer(id, first ? first.id : undefined); }); }''',
    '''// Country fills sit under the host map's outlines; lines, networks and case dots sit above them.
function order() { window.__cnLayers = { bottom: ["c-fill", "c-dots"], top: IDS.filter((x) => x !== "c-fill" && x !== "c-dots") }; if (window.__lmap) window.__lmap._reorder(); }''')

# ---------------------------------------------------------------- layers: no second set of borders; clicks shared with the host
rep('''  map.addLayer({ id: "c-fill", type: "fill", source: "ctry", filter: ["!=", ["get", "iso3"], ""], paint: { "fill-color": NODATA, "fill-opacity": ["interpolate", ["linear"], ["zoom"], 0, 0.82, 5, 0.7, 8, 0.45] } });
  map.addLayer({ id: "c-est", type: "line", source: "ctry", filter: ["in", ["get", "iso3"], ["literal", []]], paint: { "line-color": "#f0ece4", "line-width": 0.6, "line-opacity": 0.35, "line-dasharray": [1, 2] } });
  map.addLayer({ id: "c-line", type: "line", source: "ctry", paint: { "line-color": "#05061a", "line-width": 0.5, "line-opacity": 0.8 } });
  map.addLayer({ id: "c-sel", type: "line", source: "ctry", filter: ["in", ["get", "iso3"], ["literal", []]], paint: { "line-color": "#f0ece4", "line-width": 1.6, "line-opacity": 0.95 } });
  map.addLayer({ id: "c-hov", type: "line", source: "ctry", filter: ["in", ["get", "iso3"], ["literal", []]], paint: { "line-color": "#f0ece4", "line-width": 1.1, "line-opacity": 0.7 } });''',
    '''  map.addLayer({ id: "c-fill", type: "fill", source: "ctry", filter: ["!=", ["get", "iso3"], ""], paint: { "fill-color": NODATA, "fill-opacity": FILLOP } }, "anchor-mid");''')
rep('''IDS.push("c-fill", "c-est", "c-line", "c-dots", "ln-dot", "ln-dash", "ln-solid", "ln-head", "ln-end", "net-node", "cs-pt", "c-sel", "c-hov"); order();''',
    '''IDS.push("c-fill", "c-dots", "ln-dot", "ln-dash", "ln-solid", "ln-head", "ln-end", "net-node", "cs-pt"); order();''')
cut('  map.on("click", (e) => {', '  map.on("mouseout", () => { tip(null); hov(null); });\n', '''  // The host map handles country clicks and hover; a case, a network or one of these lines claims the pointer first.
  window.__cnClaimClick = (e) => {
    const cp = q(e.point, ["cs-pt"], 5)[0]; if (cp) { openCase(cp.properties.i); return true; }
    const np = q(e.point, ["net-node"], 6)[0]; if (np) { openNet(np.properties.i); return true; }
    return false;
  };
  window.__cnClaimMove = (e) => {
    const xy = [e.originalEvent.clientX, e.originalEvent.clientY];
    const cp = q(e.point, ["cs-pt"], 5)[0];
    if (cp) { const c = C[cp.properties.i]; map.getCanvas().style.cursor = "pointer"; tip("<b>" + esc(c.n) + "</b><br><span class=m>" + esc(setLabel(c.set)) + " · " + esc(STAT[c.st][0]) + (yrs(c) ? " · " + yrs(c) : "") + "</span>", ...xy); return true; }
    const np = q(e.point, ["net-node"], 6)[0];
    if (np) { const n = N[np.properties.i]; map.getCanvas().style.cursor = "pointer"; tip("<b>" + esc(n.n) + "</b><br><span class=m>" + esc(n.hq || "") + " · documented in " + (n.reach || []).length + " countr" + ((n.reach || []).length === 1 ? "y" : "ies") + "</span>", ...xy); return true; }
    const ln = q(e.point, ["ln-solid", "ln-dash", "ln-dot"], 2)[0];
    if (ln && ln.properties.t) { tip(ln.properties.t, ...xy); return false; }   // a line shows its label but leaves the country under it hovered
    tip(null); return false;
  };
  map.on("mouseout", () => { tip(null); });
''')
rep('''  map.setPaintProperty("c-fill", "fill-opacity", plain ? 0 : ["interpolate", ["linear"], ["zoom"], 0, 0.82, 5, 0.7, 8, 0.45]);''',
    '''  map.setPaintProperty("c-fill", "fill-opacity", plain ? 0 : FILLOP);''')
rep('''  map.setPaintProperty("c-line", "line-opacity", plain ? 0.25 : 0.8);
  map.setFilter("c-est", ["in", ["get", "iso3"], ["literal", est]]);
  map.setFilter("c-sel", ["in", ["get", "iso3"], ["literal", S.sel ? [S.sel] : []]]);
''', '')
rep('const ptOf = (k) => P[k] && P[k].pt;', '''const ptOf = (k) => P[k] && P[k].pt;
// Lighter than on its own map: the host map is read against its painted plate and imagery.
const FILLOP = ["interpolate", ["linear"], ["zoom"], 0, 0.6, 3, 0.5, 5, 0.26, 8, 0.12];''')
rep('"circle-stroke-color": "#05061a", "circle-stroke-width": 0.8,', '"circle-stroke-color": "#0b1112", "circle-stroke-width": 0.8,')
src = src.replace('"#05061a"', '"#0b1112"')

rep('el.className = "win card";', 'el.className = "cnui cnwin";')
rep('const WINS = {}; let zTop = 950, cascade = 0;', 'const WINS = {}; let zTop = 1150, cascade = 0;')
rep('let zBox = 960;', 'let zBox = 1200;')
# The flat map fills the page behind the host's panels, as that map always did.
rep('else { const z = Math.max(0, Math.log2(Math.min(fb.fw - 20, (fb.H - 40) * 1.55) / 512)); map.flyTo({ center: [10, 22], zoom: z, padding, duration: 1200 }); }',
    'else { const z = Math.max(0, Math.log2(Math.min(fb.W, fb.H * 1.6) / 512)); map.flyTo({ center: [10, 25], zoom: z, padding: { left: 0, right: 0, top: 0, bottom: 0 }, duration: 1200 }); }')
# ---------------------------------------------------------------- ids that clash with the host page
src = src.replace('<div id="legend"></div>', '<div id="cnLegend"></div>').replace('$("#legend")', '$("#cnLegend")')
src = src.replace("'<div id=\"cnt\">'", "'<div id=\"cnCnt\">'").replace('<div id="cnt">', '<div id="cnCnt">')
src = src.replace('$("#keyBody")', '$("#cnKeyBody")').replace('$("#trBody")', '$("#bmBody")')

# ---------------------------------------------------------------- the country box: the host's, with this map's section added
rep('function detail(k) {', 'function countryHTML(k, embed) {')
rep('''  h.push('<div class="hp-k">Country</div><h3>' + esc(p.n) + '</h3>');''', '''  if (!embed) h.push('<div class="hp-k">Country</div><h3>' + esc(p.n) + '</h3>');''')
rep('''  $("#detBody").innerHTML = h.join(""); wireBox();
}
function select(k, fly) {''', '''  return h.join("");
}
function detail(k) { $("#detBody").innerHTML = countryHTML(k); wireBox(); }
// A country goes to the host map's own box (its services, drill-down and this map's section below them).
function select(k, fly) {
  if (window._openUnitByIso && window._openUnitByIso(k)) { S.sel = k; paint(); return; }
  openChildCountry(k, fly);
}
function openChildCountry(k, fly) {''')
rep('''function wireBox() {
  $("#detBody").querySelectorAll''', '''function wireBox() { wireIn($("#detBody")); }
function wireIn(root) {
  root.querySelectorAll''')
for t in ('[data-net]', '[data-k]', '[data-case]'):
    rep('  $("#detBody").querySelectorAll("%s")' % t, '  root.querySelectorAll("%s")' % t)

# ---------------------------------------------------------------- init, about, keys
cut('/* ---------- about and sources ---------- */', '\n})();', '''/* ---------- coverage: the two checklists, so readers can see how complete this layer is ---------- */
const CIDX = {}; C.forEach((c, i) => { CIDX[c.id] = i; });
function covStats() {
  const cv = D.COV || { findings: [], kinds: [] };
  const fs = cv.findings.filter((f) => !f.ex), fOn = fs.filter((f) => f.cid);
  const ks = cv.kinds, kOn = ks.filter((k) => k.cids.length);
  return { fs, fOn, ks, kOn, ex: cv.findings.filter((f) => f.ex) };
}
function drawCoverage() {
  const el = $("#cnCov"); if (!el) return;
  const s = covStats(); if (!s.fs.length && !s.ks.length) { el.innerHTML = ""; return; }
  const pc = (a, b) => b ? Math.round(100 * a / b) : 0;
  el.innerHTML = '<div class="psec" style="margin-top:6px">How complete this is</div>' +
    (s.ks.length ? '<div class="lg"><span>Kinds of abuse and trafficking with documented cases</span><span class="n">' + s.kOn.length + ' of ' + s.ks.length + ' (' + pc(s.kOn.length, s.ks.length) + '%)</span></div>' : '') +
    (s.fs.length ? '<div class="lg"><span>Major official findings on the map</span><span class="n">' + s.fOn.length + ' of ' + s.fs.length + ' (' + pc(s.fOn.length, s.fs.length) + '%)</span></div>' : '') +
    '<p class="lsrc">The kinds come from four published lists: those of the inquiries in England and Wales and in Australia, the international guidelines on terms for the sexual exploitation of children, and the UN’s report on trafficking in persons. A major official finding is a report by an inquiry, commission, grand jury, parliament, court, UN body or an institution’s own commissioned investigation that covers a whole country, state, institution or 100 or more children. ' +
    'Everything else on the map is a small part of all the connected cases ever documented (roughly 1 to 5 percent, by this map’s estimate), and most abuse is never reported at all.</p>' +
    '<p class="lsrc"><a href="#" id="covF">See the findings checklist</a> · <a href="#" id="covK">See the kinds</a></p>';
  $("#covF").addEventListener("click", (e) => { e.preventDefault(); openList("Major official findings: the checklist", findingsHTML()); });
  $("#covK").addEventListener("click", (e) => { e.preventDefault(); openList("Kinds of abuse and trafficking: the checklist", kindsHTML()); });
}
function caseLink(id) { const i = CIDX[id]; return i == null ? '' : '<a href="#" data-case="' + i + '">on the map</a>'; }
function findingsHTML() {
  const s = covStats(), rows = s.fs.slice().sort((a, b) => ((P[a.iso] || {}).n || "").localeCompare((P[b.iso] || {}).n || "") || (a.y || 0) - (b.y || 0));
  return '<p>' + s.fOn.length + ' of ' + s.fs.length + ' major official findings on the checklist are on the map. Each row names the body, its year, how far it reached and its report.</p>' +
    '<table class="all cklist"><thead><tr><th>Country</th><th>Finding</th><th>Year</th><th></th></tr></thead><tbody>' +
    rows.map((f) => '<tr><td>' + esc((P[f.iso] || {}).n || f.iso || "International") + '</td><td>' + esc(f.n) + '<br><span class="note">' + esc([f.body, f.reach].filter(Boolean).join(" · ")) + '</span></td><td>' + esc(f.y || "") + '</td><td>' + (f.url ? link("report", f.url) : "") + (f.cid ? '<br>' + caseLink(f.cid) : "<br>not yet") + '</td></tr>').join("") + '</tbody></table>' +
    (s.ex.length ? '<p class="lsrc" style="margin-top:12px">Considered and left out (' + s.ex.length + '): ' + s.ex.map((f) => esc(f.n) + (f.why ? ' (' + esc(f.why) + ')' : '')).join("; ") + '.</p>' : '');
}
function kindsHTML() {
  const s = covStats();
  return '<p>' + s.kOn.length + ' of ' + s.ks.length + ' kinds have documented cases on the map.</p>' +
    s.ks.map((k) => '<div class="lg" style="display:block;padding:7px 0"><b>' + esc(k.label) + '</b> <span class="n">' + k.cids.length + ' case' + (k.cids.length === 1 ? '' : 's') + '</span><br><span class="note">' + esc(k.def) + (k.src ? ' Source: ' + (k.url ? link(k.src, k.url) : esc(k.src)) + '.' : '') + '</span>' +
      (k.cids.length ? '<br><span class="note">' + k.cids.slice(0, 12).map((id) => { const i = CIDX[id]; return i == null ? '' : '<a href="#" data-case="' + i + '">' + esc(C[i].n) + '</a>'; }).filter(Boolean).join(" · ") + (k.cids.length > 12 ? ' · and ' + (k.cids.length - 12) + ' more' : '') + '</span>' : '') + '</div>').join("");
}
function openList(title, html) {
  const p = $("#guidePanel"), t = $("#guideTitle"), b = $("#guideBody"); if (!p || !b) return;
  t.textContent = title; b.innerHTML = '<div class="pb-body cnui cn-about cnwin" style="position:static;resize:none;border:0;box-shadow:none;background:none;display:block">' + html + '</div>'; b.scrollTop = 0;
  p.classList.add("open"); p.setAttribute("aria-hidden", "false"); wireIn(b);
}
/* ---------- about and sources: shown in the host map's guide reader ---------- */
function openAbout() {
  const p = $("#guidePanel"), t = $("#guideTitle"), b = $("#guideBody");
  if (!p || !b) return;
  t.textContent = "Child abuse networks and child trafficking: about and sources";
  b.innerHTML = '<div class="pb-body cnui cn-about">' + D.ABOUT + '</div>'; b.scrollTop = 0;
  p.classList.add("open"); p.setAttribute("aria-hidden", "false");
}
document.addEventListener("keydown", (e) => { if (e.key !== "Escape") return; if ($("#patBox").classList.contains("open")) closePat(); else if (S.selCase != null || S.selNet != null || $("#det").classList.contains("open")) deselect(); });
init();
}
/* ---------- the page furniture this layer adds to the host map ---------- */
function mountUI() {
  const lb = document.getElementById("legBody"), keyHost = document.getElementById("cnKeyHost"), bmHost = document.getElementById("bmBar");
  const bm = document.createElement("div"); bm.id = "bmBox"; bm.className = "cnui cn-blk"; bm.innerHTML = '<div id="bmBody"></div>';
  const sec = document.createElement("div"); sec.id = "cnSec"; sec.className = "cnui cn-blk";
  sec.innerHTML = '<div class="cn-head">Child abuse networks and child trafficking</div>' +
    '<p class="lsrc" style="margin:2px 0 6px">Organised abuse, sale and trafficking of children, the institutions that shielded it, and the patterns that repeat across countries. Click a dot or a diamond for its record; click a country for this layer\\'s section on it.</p>' +
    '<div id="cnCov"></div><div id="cnKeyBody"></div><div class="psec">Charts</div><div id="dockBtns"></div>' +
    '<p class="lsrc" style="margin-top:8px"><a href="#" id="cnAbout">About this layer and its sources</a></p>';
  if (bmHost) bmHost.appendChild(bm); else if (lb) lb.insertBefore(bm, lb.firstChild); else document.body.appendChild(bm);
  if (keyHost) { sec.querySelector(".cn-head").remove(); keyHost.appendChild(sec); } else if (lb) lb.appendChild(sec); else document.body.appendChild(sec);
  const add = (html) => { const d = document.createElement("div"); d.innerHTML = html; const el = d.firstChild; document.body.appendChild(el); return el; };
  add('<div id="det" class="cnui cnbox scroll hp mbox" role="dialog" aria-label="Details"><div class="grip" title="Drag to move"></div><button id="detX" type="button" title="Close">×</button><div id="detBody"></div></div>');
  add('<div id="patBox" class="cnui cnbox scroll hp mbox" role="dialog" aria-label="Pattern behind the scenes"><div class="grip" title="Drag to move"></div><button id="patX" type="button" title="Close">×</button><div id="patBody"></div></div>');
  add('<div id="ttip" class="cnui"></div>');
  const ab = document.getElementById("cnAbout"); if (ab) ab.addEventListener("click", (e) => { e.preventDefault(); if (window.__cnAbout) window.__cnAbout(); });
}
boot();
})();''')

# The original init(): keep the parts that build this layer, drop the ones that belonged to its own page.
i = src.index('function init() {'); j = src.index('\n}\n', i)
src = src[:i] + '''function init() {
  window.__cnAbout = openAbout;
  if (document.getElementById("cnKeyHost")) S.layer = "none";
  buildKey(); buildTr(); buildDock(); stars(); computeDoc(); drawSwatches(); drawCoverage();
  // the patterns list gets its own panel
  const pb = document.getElementById("cnPatHost"), pl = $("#patList");
  if (pb && pl) { const ip = $("#patI"), hd = ip && ip.previousElementSibling; [hd, ip, pl].forEach((x) => { if (x) pb.appendChild(x); }); if (hd) hd.style.marginTop = "0"; }
  // clear and restore this layer, for the host's goal and lens choices
  let saved = null;
  window.cnHide = () => { if (saved) return; saved = { pts: S.pts, linesOn: S.linesOn, nets: S.nets, layer: S.layer }; S.pts = false; S.linesOn = false; S.nets = false; S.layer = "none"; syncToggles(); update(); };
  window.cnRestore = () => { if (!saved) return; Object.assign(S, saved); saved = null; syncToggles(); update(); };
  function syncToggles() { const t = (id, v) => { const e = $("#" + id); if (e) e.checked = v; }; t("ptsOn", S.pts); t("linesOn", S.linesOn); t("netOn", S.nets); const l = $("#layer"); if (l && !/^pat_/.test(S.layer)) l.value = S.layer; }
  fetch(BOUND_URL).then((r) => r.json()).then((geo) => { addLayers(geo); ready = true; update(); }).catch((e) => { console.warn("boundaries", e); });
  $("#detX").addEventListener("click", deselect);
  $("#patX").addEventListener("click", closePat);
  dragBox($("#det")); dragBox($("#patBox"));
  drawLegend(); drawList();
  hookInfo();
}
/* ---------- this layer's section in the host map's country box ---------- */
let NAMEISO = null;
function nameIso() {
  if (NAMEISO) return NAMEISO;
  NAMEISO = {};
  const put = (n, k) => { if (n && k && P[k]) NAMEISO[String(n).trim().toLowerCase()] = k; };
  Object.keys(P).forEach((k) => put(P[k].n, k));
  const td = window.trackerData || {}; Object.keys(td).forEach((k) => put(td[k] && td[k].name, k));
  const isn = window.ISO_NAME || {}; Object.keys(isn).forEach((k) => put(isn[k], k));
  return NAMEISO;
}
function hookInfo() {
  const orig = window.showInfoPanel; if (typeof orig !== "function" || orig.__cn) return;
  const w = function (html) { const r = orig.apply(this, arguments); try { addPanel(String(html || "")); } catch (e) { console.warn("[child networks] panel", e); } return r; };
  w.__cn = true; window.showInfoPanel = w;
  const oh = window.hideInfoPanel;
  if (typeof oh === "function" && !oh.__cn) { const wh = function () { const r = oh.apply(this, arguments); const cb = document.getElementById("cnCountry"); if (cb) cb.classList.remove("open"); if (S.sel) { S.sel = null; paint(); } return r; }; wh.__cn = true; window.hideInfoPanel = wh; }
}
function addPanel(html) {
  const m = html.match(/<div class="popup-country">([^<]*)/); if (!m) return;
  const head = html.slice(m.index, m.index + m[0].length + 400);
  if (/fed-badge|High Seas|>International</.test(head.split("</div>")[0])) return;
  NAMEISO = null;
  const k = nameIso()[m[1].trim().toLowerCase()]; if (!k) return;
  const box = document.getElementById("cnCountry");
  if (box) {
    const b = box.querySelector(".cnc-body");
    b.innerHTML = '<div class="hp-k">Child abuse networks and child trafficking</div><h3>' + esc(P[k].n) + '</h3>' + countryHTML(k, true);
    wireIn(b); box.classList.add("open"); box.scrollTop = 0; if (window.__uiPlace) window.__uiPlace();
  } else {
    const body = $("#infoBody"); if (!body) return;
    const d = document.createElement("div"); d.className = "cnui cn-panel hp"; d.id = "cnPanel";
    d.innerHTML = '<div class="cn-panel-h">Child abuse networks and child trafficking</div>' + countryHTML(k, true);
    const old = document.getElementById("cnPanel"); if (old) old.remove();
    body.appendChild(d); wireIn(d);
  }
  S.sel = k; paint();
}''' + src[j + 2:]

# The original's "Escape" and page-only handlers were inside the removed about block.
src = src.replace('const BOUND_URL = "https://welcometoyourgalaxy.github.io/culprits/data/boundaries.geojson";',
                  'const BOUND_URL = "https://welcometoyourgalaxy.github.io/culprits/data/boundaries.geojson";')
# fitView and wholeWorld padding use freeBox, which now reads the host's panels.

os.makedirs(os.path.join(DEST, 'engine'), exist_ok=True)
open(os.path.join(DEST, 'engine', 'child.js'), 'w').write(src)
D2 = dict(D); D2['ABOUT'] = D['ABOUT']
json.dump(D2, open(os.path.join(DEST, 'child_networks.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print('wrote', os.path.join(DEST, 'engine', 'child.js'), len(src), 'bytes;', os.path.join(DEST, 'child_networks.json'),
      round(os.path.getsize(os.path.join(DEST, 'child_networks.json')) / 1e6, 2), 'MB')
