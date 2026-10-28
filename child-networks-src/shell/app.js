
(function () {
"use strict";
if (typeof navigator !== "undefined" && navigator.userAgent === "node") return;
const $ = (s) => document.querySelector(s);
const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const fmt = (n, d) => n == null ? "" : Number(n).toLocaleString("en-US", { maximumFractionDigits: d == null ? 2 : d, minimumFractionDigits: 0 });
const P = D.P, C = D.C, N = D.N, F = D.F, PAT = D.PAT || [];
const ISOS = Object.keys(P).sort((a, b) => P[a].n.localeCompare(P[b].n));
Object.keys(P).forEach((k) => { P[k].iso = k; });
const link = (t, u) => u ? '<a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(t || "source") + '</a>' : esc(t);
const avg = (a) => a.reduce((x, y) => x + y, 0) / a.length;
const median = (a) => { if (!a.length) return null; const s = a.slice().sort((x, y) => x - y), m = s.length >> 1; return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };

/* ---------- colors ---------- */
// Each basemap: [accent, accent-hi, page], a five-step ramp from its own tones, and the point colors for the eight settings.
const UI = { night: ["#5600DC", "#a99cff", "#06071a"], satellite: ["#3f6e69", "#9fc9c1", "#0b1017"], atlas: ["#4b6075", "#b9c8d8", "#0b1017"], hell: ["#82303a", "#e0a3a5", "#1e080b"], outlines: ["#38586b", "#a9c2d6", "#0b1017"] };
const RAMPS = {
  night:     ["#2b2452", "#45398a", "#6d5fbb", "#a195e0", "#ddd6fa"],
  outlines:  ["#20364a", "#31546f", "#4d7a9c", "#86aac8", "#cddfee"],
  satellite: ["#1d3836", "#2c5753", "#477d77", "#7fafa7", "#c6e2dc"],
  atlas:     ["#23304a", "#384c6f", "#587198", "#8fa6c6", "#d2ddec"],
  hell:      ["#3a1519", "#5c2229", "#883a43", "#ba6f76", "#ecc3c5"],
};
// Point colors per basemap, in setting order: religious, care, elite, organized, tourism, online, conflict, adoption.
const SETPAL = {
  night:     ["#c3a8ef", "#86b0e6", "#ef9db4", "#cfb2aa", "#86cdc4", "#b9c6ea", "#e0707f", "#b7bf8a"],
  outlines:  ["#b9a4df", "#8db6dc", "#e3a0b2", "#c9b3a9", "#8fc8bf", "#bcc8e2", "#d87683", "#b5bc8e"],
  satellite: ["#cbb6e6", "#a4c4e2", "#f0b4c0", "#e0c9bd", "#a6dbd2", "#d3dbef", "#f08e98", "#cfd6a2"],
  atlas:     ["#5e4a86", "#3e6a96", "#a24a63", "#7c5c50", "#2f7a72", "#5a6688", "#86303e", "#5f6a32"],
  hell:      ["#d8c4f0", "#a9c7e8", "#ffd0da", "#e8d3c8", "#a9ddd5", "#dfe4f4", "#ffffff", "#d6dcae"],
};
const CATC = ["#3a6db8", "#c97585", "#a9cfe6", "#4f8f5a"];
const OTHER = "#8b8996", NODATA = "#3d3e4a";
let BASE = "night";
const ramp = () => RAMPS[BASE] || RAMPS.night;
const hex = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
function mix(a, b, t) { const A = hex(a), B = hex(b); return "#" + A.map((x, i) => Math.round(x + (B[i] - x) * t).toString(16).padStart(2, "0")).join(""); }
function seqColor(t) { const r = ramp(); t = Math.max(0, Math.min(1, t)); const x = t * (r.length - 1), i = Math.min(r.length - 2, Math.floor(x)); return mix(r[i], r[i + 1], x - i); }
const SETS = D.SETS;                       // [[key, label, description], ...]
const SETK = SETS.map((s) => s[0]);
const setColor = (k) => (SETPAL[BASE] || SETPAL.night)[Math.max(0, SETK.indexOf(k))];
const FLOWT = D.FLOWT;                     // [[type, label, description, style], ...]
const FLOWC = { trafficking: 0, offenders: 1, transfer: 2, adoption: 3, removal: 3, money: 2, material: 2 };
const flowColor = (t) => { const pal = SETPAL[BASE] || SETPAL.night; return ({ trafficking: pal[3], offenders: pal[4], transfer: pal[0], adoption: pal[7], removal: pal[6], money: pal[2], material: pal[5] })[t] || OTHER; };
const STAT = D.STAT;                       // {status: [label, weight, plain]}

/* ---------- state ---------- */
const YMIN = D.META.ymin, YMAX = D.META.ymax;
const S = { layer: "all", from: YMIN, to: YMAX, sets: new Set(SETK), pts: true, ring: true, nets: false, flows: new Set(), patOnly: false,
  sel: null, selCase: null, selNet: null, hov: null, q: "", names: true, unproven: true };

/* ---------- which cases count ---------- */
const COUNTS = (c) => STAT[c.st] && STAT[c.st][1] > 0;
function inWindow(c) {
  const a = c.y0 || c.yf || c.y1, b = c.y1 || c.yf || c.y0;
  if (a == null && b == null) return true;
  return Math.max(a, b) >= S.from && Math.min(a, b) <= S.to;
}
const caseOn = (c) => S.sets.has(c.set) && inWindow(c) && (S.unproven || COUNTS(c));
const casesOf = (k) => C.filter((c) => (c.iso === k || (c.also || []).includes(k)) && caseOn(c));
// How much one case adds to its country's documented record: how firmly it was established, how many children,
// whether officials took part or covered it up. A country named in a case as a second place gets half.
function caseWeight(c, k) {
  const st = STAT[c.st]; if (!st || st[1] <= 0) return 0;
  const v = c.v ? 1 + Math.log10(1 + c.v) / 2 : 1;
  return st[1] * v * (c.offc ? 1.3 : 1) * (c.iso === k ? 1 : 0.5);
}
let DOC = {}, DOCCAP = 1;
function computeDoc() {
  DOC = {};
  C.forEach((c) => { if (!caseOn(c)) return; [c.iso].concat(c.also || []).forEach((k) => { if (P[k]) DOC[k] = (DOC[k] || 0) + caseWeight(c, k); }); });
  const vs = Object.values(DOC).filter((v) => v > 0).sort((a, b) => a - b);
  DOCCAP = vs.length ? vs[Math.min(vs.length - 1, Math.round(0.95 * (vs.length - 1)))] : 1;
}
const docScore = (k) => DOC[k] ? Math.min(100, 100 * Math.log1p(DOC[k]) / Math.log1p(DOCCAP)) : 0;

/* ---------- indicator parts, each 0 (least) to 1 (most) ---------- */
const TIPV = { "1": 0.1, "2": 0.4, "2W": 0.65, "3": 0.9, "SC": 0.85 };
const TIPL = { "1": "Tier 1", "2": "Tier 2", "2W": "Tier 2 Watch List", "3": "Tier 3", "SC": "Special case (not ranked)" };
const MAXPREV = D.META.maxprev, MAXNCM = D.META.maxncm;
function marketParts(p) {
  const i = p.ind || {}, out = [];
  if (i.ht25 != null) out.push(["Trafficking market (GI-TOC 2025)", i.ht25 / 10, fmt(i.ht25, 1) + " of 10"]);
  if (i.prev != null) out.push(["People in modern slavery (Walk Free 2023)", Math.log1p(i.prev) / Math.log1p(MAXPREV), fmt(i.prev, 1) + " per 1,000"]);
  if (i.ncmpc != null) out.push(["Reports of online child abuse (NCMEC)", Math.log1p(i.ncmpc) / Math.log1p(MAXNCM), fmt(i.ncmpc, 0) + " per 100,000 people"]);
  return out;
}
function shieldParts(p) {
  const i = p.ind || {}, out = [];
  if (i.sea != null) out.push(["Officials working with criminals (GI-TOC)", i.sea / 10, fmt(i.sea, 1) + " of 10"]);
  if (i.res != null) out.push(["Little stands in the way (GI-TOC resilience, inverted)", (10 - i.res) / 10, "resilience " + fmt(i.res, 2) + " of 10"]);
  if (i.vws != null) out.push(["Weak help for victims and witnesses (GI-TOC, inverted)", (10 - i.vws) / 10, "support " + fmt(i.vws, 1) + " of 10"]);
  if (i.tip != null && TIPV[i.tip] != null) out.push(["US State Department ranking, 2025", TIPV[i.tip], TIPL[i.tip]]);
  return out;
}
const partScore = (ps) => ps.length ? 100 * avg(ps.map((x) => x[1])) : null;
// The combined score: documented record 35%, the trade's likely size 40%, how little stops it 25%.
// Where nothing is documented in the chosen years the combined score rests on the indicators alone and is marked an estimate.
function allScore(p) {
  const m = partScore(marketParts(p)), s = partScore(shieldParts(p)), d = docScore(p.iso);
  if (m == null && s == null) return p.proxy ? null : (d ? { v: d, est: false, only: "doc" } : null);
  const parts = [], w = [];
  parts.push(d); w.push(0.35);
  if (m != null) { parts.push(m); w.push(0.40); }
  if (s != null) { parts.push(s); w.push(0.25); }
  const tw = w.reduce((a, b) => a + b, 0);
  return { v: parts.reduce((a, x, i) => a + x * w[i], 0) / tw, est: d === 0, d, m, s };
}

/* ---------- the layers the key offers ---------- */
const L = [];
function seq(id, group, label, o) { L.push(Object.assign({ id, group, label, kind: "seq" }, o)); }
function cat(id, group, label, o) { L.push(Object.assign({ id, group, label, kind: "cat" }, o)); }
seq("none", "Plain", "No country colors", { dom: [0, 1], f: () => "", get: () => null, desc: "Countries are left uncolored so the basemap, the points and the lines show clearly. Click any country for its box.", src: "" });
seq("all", "The big picture", "Likely scale and impunity (everything combined)", { f: (v) => fmt(v, 0) + " of 100",
  get: (p) => { const r = allScore(p); return r ? { v: r.v, est: r.est } : null; },
  desc: "How likely it is that children are being abused, sold or trafficked here by organised groups or inside institutions, and how little stands in the way. Thirty-five percent is the documented record on this map in the chosen years; forty percent is how large the trade is estimated to be (trafficking market, modern slavery, reports of online abuse); twenty-five percent is how little stops it (officials working with criminals, weak resilience, weak help for victims, the US ranking). Where nothing is documented here in the chosen years, the score rests on the indicators alone and its box says it is an estimate. Light means more.",
  src: "This map's cases; GI-TOC Global Organized Crime Index 2025; Walk Free Global Slavery Index 2023; NCMEC CyberTipline 2024; US Trafficking in Persons Report 2025." });
seq("doc", "The big picture", "Documented record (cases found by courts, inquiries and investigations)", { dom: [0, 100], f: (v) => fmt(v, 0) + " of 100",
  get: (p) => { const n = casesOf(p.iso).length; return n ? { v: docScore(p.iso), n } : null; },
  desc: "Every case on this map in the chosen years and kinds, weighted by how firmly it was established (a conviction or an official inquiry counts more than a press report; acquittals and disproved claims count nothing), by how many children it involved, and by whether officials took part or covered it up. A high score means much has been exposed here, which is also a measure of how much has been looked for: countries that held inquiries show up; countries that never did stay dark.",
  src: "The cases on this map; each links its source." });
seq("market", "The big picture", "Likely size of the trade (indicators only)", { f: (v) => fmt(v, 0) + " of 100",
  get: (p) => { const v = partScore(marketParts(p)); return v == null ? null : { v }; },
  desc: "The average of three estimates, each scaled 0 to 1: GI-TOC's score for the human trafficking market (2025), Walk Free's estimate of people in modern slavery per 1,000 (2023), and NCMEC's reports of suspected online child sexual abuse per 100,000 people (2024). None counts child sexual abuse alone; together they show where the trade is likely large. Light means more.",
  src: "GI-TOC 2025; Walk Free 2023; NCMEC 2024." });
seq("shield", "The big picture", "How little stands in the way (indicators only)", { f: (v) => fmt(v, 0) + " of 100",
  get: (p) => { const v = partScore(shieldParts(p)); return v == null ? null : { v }; },
  desc: "The average of: how far state officials work with criminal groups (GI-TOC state-embedded actors), the country's resilience to organised crime and its help for victims and witnesses (both inverted), and the US State Department's 2025 trafficking ranking. Light means less stands in the way.",
  src: "GI-TOC 2025; US Trafficking in Persons Report 2025." });
SETS.forEach((s) => seq("set_" + s[0], "Documented cases, by setting", s[1], { log: true, f: (v) => fmt(v, 0) + (v === 1 ? " case" : " cases"),
  get: (p) => { const n = casesOf(p.iso).filter((c) => c.set === s[0]).length; return n ? { v: n } : null; }, desc: s[2] + " Count of cases on this map in the chosen years. Light means more.", src: "The cases on this map." }));
seq("offc", "Documented cases, by setting", "Cases where officials took part or covered up", { log: true, f: (v) => fmt(v, 0) + (v === 1 ? " case" : " cases"),
  get: (p) => { const n = casesOf(p.iso).filter((c) => c.offc && COUNTS(c)).length; return n ? { v: n } : null; },
  desc: "Cases in which police, prosecutors, judges, politicians, civil servants, soldiers or intelligence officers took part, or were documented as having ignored, buried or obstructed it. Light means more.", src: "The cases on this map." });
seq("delay", "Documented cases, by setting", "Years from the first complaint to the first action (median)", { f: (v) => fmt(v, 0) + (v === 1 ? " year" : " years"),
  get: (p) => { const ds = casesOf(p.iso).filter((c) => COUNTS(c) && c.fr && c.yf && c.yf >= c.fr).map((c) => c.yf - c.fr); return ds.length ? { v: median(ds), n: ds.length } : null; },
  desc: "For cases whose sources date the first complaint to police, an employer, a church or officials, the years until the first conviction, charge or official finding. The middle value of this country's cases. Light means longer.", src: "The cases on this map." });
seq("ht25", "Measured elsewhere", "Human trafficking market, 2025 (GI-TOC, 1–10)", { dom: [1, 10], f: (v) => fmt(v, 1), get: (p) => p.ind && p.ind.ht25 != null ? { v: p.ind.ht25 } : null,
  desc: "Expert-assessed scale and influence of the human trafficking market, all forms and ages, 1 (no market) to 10 (pervasive). Light means more.", src: "Global Initiative Against Transnational Organized Crime, Global Organized Crime Index 2025." });
seq("htchg", "Measured elsewhere", "Change in the trafficking market, 2021 to 2025", { dom: [-2.5, 2.5], f: (v) => (v > 0 ? "+" : "") + fmt(v, 1), get: (p) => p.ind && p.ind.ht25 != null && p.ind.ht21 != null ? { v: p.ind.ht25 - p.ind.ht21 } : null,
  desc: "GI-TOC's human trafficking score in 2025 minus 2021. Light means it grew.", src: "GI-TOC Global Organized Crime Index 2021 and 2025." });
cat("tip", "Measured elsewhere", "US State Department trafficking ranking, 2025", { classes: [["1", "Tier 1: meets the minimum standards"], ["2", "Tier 2: does not, making significant efforts"], ["2W", "Tier 2 Watch List"], ["3", "Tier 3: does not, not making significant efforts"]],
  other: "Special case (not ranked)", get: (p) => p.ind && p.ind.tip ? (p.ind.tip === "SC" ? { v: null, other: true } : { v: p.ind.tip }) : null,
  desc: "How the US government ranks each government's efforts against trafficking. Tier 1 does not mean a country has no trafficking. The US ranks itself.", src: "US Department of State, Trafficking in Persons Report, June 2025." });
seq("prev", "Measured elsewhere", "People in modern slavery per 1,000 (Walk Free 2023)", { log: true, f: (v) => fmt(v, 1), get: (p) => p.ind && p.ind.prev != null ? { v: p.ind.prev } : null,
  desc: "Estimated people in forced labour, forced marriage and forced commercial sexual exploitation, all ages, per 1,000 population. Modelled from surveys; Walk Free warns that national estimates are not hard findings. Light means more.", src: "Walk Free, Global Slavery Index 2023, Table 26." });
seq("ncm", "Measured elsewhere", "Reports of suspected online child sexual abuse per 100,000 people (NCMEC 2024)", { log: true, f: (v) => fmt(v, 0), get: (p) => p.ind && p.ind.ncmpc != null ? { v: p.ind.ncmpc } : null,
  desc: "Reports to the US National Center for Missing & Exploited Children's CyberTipline, sorted by where the uploader appeared to be, per 100,000 people. Mostly sent by US platforms; a country's count depends on how many people use those platforms. Light means more.", src: "NCMEC, CyberTipline reports by country, 2024." });
seq("sea", "Measured elsewhere", "Officials working with criminals (GI-TOC, 1–10)", { dom: [1, 10], f: (v) => fmt(v, 1), get: (p) => p.ind && p.ind.sea != null ? { v: p.ind.sea } : null,
  desc: "How far criminal actors are embedded in the state: officials who take part in or protect organised crime. Light means more.", src: "GI-TOC Global Organized Crime Index 2025." });
seq("res", "Measured elsewhere", "Resilience to organised crime (GI-TOC, inverted)", { dom: [0, 9], f: (v) => fmt(10 - v, 2) + " of 10", get: (p) => p.ind && p.ind.res != null ? { v: 10 - p.ind.res } : null,
  desc: "Twelve measures of how well the state and society resist organised crime: leadership, transparency, courts, police, victim support, prevention and others. Shown inverted: light means weaker.", src: "GI-TOC Global Organized Crime Index 2025." });
PAT.forEach((pt) => {
  const roles = pt.roles && pt.roles.length ? pt.roles.slice(0, 4) : [...new Set(pt.countries.map((c) => c.role))].slice(0, 4);
  const RC = {}; pt.countries.forEach((c) => { RC[c.iso3] = c; });
  L.push({ id: "pat_" + pt.id, group: "Patterns behind the scenes", label: pt.title, kind: "cat", pat: pt,
    classes: roles.map((r) => [r, r]), other: "Other role", get: (p) => { const c = RC[p.iso]; return c ? (roles.includes(c.role) ? { v: c.role, note: c.note } : { v: null, other: true, note: c.note }) : null; },
    desc: pt.summary, src: "" });
});
const layer = () => L.find((l) => l.id === S.layer) || L[1];
function dom(l) {
  if (l.dom) return l.dom;
  const vs = ISOS.map((k) => { const r = l.get(P[k]); return r && r.v > 0 ? r.v : null; }).filter((v) => v != null);
  return vs.length ? [Math.min(...vs), Math.max(...vs)] : [0, 1];
}
function colorOf(l, r, d) {
  if (!r) return NODATA;
  if (l.kind === "cat") { if (r.v == null) return OTHER; const i = l.classes.findIndex((c) => c[0] === r.v); return i < 0 ? OTHER : CATC[i]; }
  if (r.v == null) return NODATA;
  let t;
  if (l.log) { const a = Math.log10(Math.max(d[0], 1e-6)), b = Math.log10(d[1]); t = b > a ? (Math.log10(Math.max(r.v, d[0])) - a) / (b - a) : 1; }
  else t = (r.v - d[0]) / ((d[1] - d[0]) || 1);
  return seqColor(t);
}

/* ---------- map ---------- */
function freeBox() {
  const el = map ? map.getContainer() : $("#map"), W = el.clientWidth || 1200, H = el.clientHeight || 800;
  let Lf = 0, R = 0; try { Lf = panelRight(); R = rightBox(); } catch (e) {}
  if (W - Lf - R < 240) { Lf = 0; R = 0; }
  return { W, H, L: Lf, R, fw: W - Lf - R };
}
function startZoom() {
  let fb; try { fb = freeBox(); } catch (e) { const el = $("#map"); fb = { fw: (el.clientWidth || 1200) - 720, H: el.clientHeight || 800 }; }
  return Math.max(0.2, Math.log2(0.86 * Math.max(220, Math.min(fb.H - 40, fb.fw - 20)) * Math.PI / 512));
}
let proj = "globe", ready = false;
function freeFlat() {
  try {
    if (proj === "mercator") map.setTransformConstrain((ll, z) => ({ center: new maplibregl.LngLat(Math.max(-360, Math.min(360, ll.lng)), Math.max(-84, Math.min(84, ll.lat))), zoom: Math.max(0, z) }));
    else map.setTransformConstrain(null);
  } catch (e) {}
}
const BM = CulpritsBasemaps.create("map", { initial: "night", projection: "globe", plate: window.PLATE_IMG, center: [12, 22], zoom: startZoom(),
  onApply: (k) => { BASE = k; if (!S.names) setTimeout(hideNames, 0); const u = UI[k] || UI.night, rs = document.documentElement.style; rs.setProperty("--accent", u[0]); rs.setProperty("--accent-hi", u[1]); rs.setProperty("--bg", u[2]); if (ready) { order(); update(); } },
  onReady: () => init() });
const map = window.cnMap = BM.maplibre;
map.addControl(new maplibregl.NavigationControl({ showCompass: false }), "bottom-right");
map.once("idle", () => { const a = map.getContainer().querySelector(".maplibregl-ctrl-attrib"); if (a) { a.classList.remove("maplibregl-compact-show"); a.removeAttribute("open"); } });
function panelRight() { try { const r = $("#key").getBoundingClientRect(), w = map.getContainer().clientWidth; if (r.width && r.right < w * 0.6) return r.right + 10; } catch (e) {} return 0; }
function rightBox() { try { const r = $("#rcol").getBoundingClientRect(), w = map.getContainer().clientWidth; if (r.width && r.left > w * 0.5) return w - r.left + 10; } catch (e) {} return 0; }
function hideNames() {
  const st = map.getStyle(); if (!st) return; const mine = new Set(IDS);
  st.layers.forEach((l) => { if (!mine.has(l.id) && (l.type === "symbol" || l.id === "labels")) map.setLayoutProperty(l.id, "visibility", "none"); });
}
function wholeWorld() {
  const fb = freeBox(), padding = { left: fb.L, right: fb.R, top: 0, bottom: 0 };
  if (proj === "globe") map.flyTo({ center: [12, 22], zoom: startZoom(), padding, duration: 1200 });
  else { const z = Math.max(0, Math.log2(Math.min(fb.fw - 20, (fb.H - 40) * 1.55) / 512)); map.flyTo({ center: [10, 22], zoom: z, padding, duration: 1200 }); }
}
const IDS = [];
function order() { const st = map.getStyle(); if (!st) return; const mine = new Set(IDS); const first = st.layers.find((l) => !mine.has(l.id) && (l.type === "symbol" || l.id === "labels")); IDS.forEach((id) => { if (map.getLayer(id)) map.moveLayer(id, first ? first.id : undefined); }); }

const tt = $("#ttip");
function tip(html, x, y) { if (!html) { tt.style.display = "none"; return; } tt.innerHTML = html; tt.style.display = "block"; const r = tt.getBoundingClientRect(); let Lx = x + 14, T = y + 12; if (Lx + r.width > innerWidth - 6) Lx = x - r.width - 12; if (T + r.height > innerHeight - 6) T = y - r.height - 10; tt.style.left = Lx + "px"; tt.style.top = T + "px"; }

const BOUND_URL = "https://welcometoyourgalaxy.github.io/culprits/data/boundaries.geojson";
const BYNAME = { "Kosovo": "XKX", "Somaliland": "SOL", "Northern Cyprus": "CYN" };
let SHAPED = new Set();
// Straight lines in longitude and latitude, never crossing the 180° edge; densified so the globe draws them as paths, not chords.
function straight(a, b, n) { n = n || 24; const o = []; for (let i = 0; i <= n; i++) { const t = i / n; o.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t]); } return o; }
// A gentle bow, so a line and its return trip do not sit on top of each other.
function arc(a, b, n, bend) {
  n = n || 32; bend = bend == null ? 0.12 : bend; const dx = b[0] - a[0], dy = b[1] - a[1], o = [];
  for (let i = 0; i <= n; i++) { const t = i / n, h = 4 * t * (1 - t) * bend; o.push([a[0] + dx * t - dy * h, a[1] + dy * t + dx * h]); }
  return o;
}
const ptOf = (k) => P[k] && P[k].pt;

function addIcons() {
  const mk = (name, draw) => { const c = document.createElement("canvas"); c.width = c.height = 32; const g = c.getContext("2d"); g.fillStyle = "#fff"; g.strokeStyle = "#fff"; draw(g); map.addImage(name, { width: 32, height: 32, data: g.getImageData(0, 0, 32, 32).data }, { sdf: true, pixelRatio: 2 }); };
  mk("diamond", (g) => { g.beginPath(); g.moveTo(16, 2); g.lineTo(30, 16); g.lineTo(16, 30); g.lineTo(2, 16); g.closePath(); g.fill(); });
  mk("tri", (g) => { g.beginPath(); g.moveTo(4, 8); g.lineTo(28, 16); g.lineTo(4, 24); g.closePath(); g.fill(); });
}
function addLayers(geo) {
  geo.features.forEach((f) => { const p = f.properties; if (!p.iso3 || p.iso3 === "-99") p.iso3 = BYNAME[p.name] || ""; });
  SHAPED = new Set(geo.features.map((f) => f.properties.iso3).filter(Boolean));
  addIcons();
  map.addSource("ctry", { type: "geojson", data: geo });
  map.addLayer({ id: "c-fill", type: "fill", source: "ctry", filter: ["!=", ["get", "iso3"], ""], paint: { "fill-color": NODATA, "fill-opacity": ["interpolate", ["linear"], ["zoom"], 0, 0.82, 5, 0.7, 8, 0.45] } });
  map.addLayer({ id: "c-est", type: "line", source: "ctry", filter: ["in", ["get", "iso3"], ["literal", []]], paint: { "line-color": "#f0ece4", "line-width": 0.6, "line-opacity": 0.35, "line-dasharray": [1, 2] } });
  map.addLayer({ id: "c-line", type: "line", source: "ctry", paint: { "line-color": "#05061a", "line-width": 0.5, "line-opacity": 0.8 } });
  map.addLayer({ id: "c-sel", type: "line", source: "ctry", filter: ["in", ["get", "iso3"], ["literal", []]], paint: { "line-color": "#f0ece4", "line-width": 1.6, "line-opacity": 0.95 } });
  map.addLayer({ id: "c-hov", type: "line", source: "ctry", filter: ["in", ["get", "iso3"], ["literal", []]], paint: { "line-color": "#f0ece4", "line-width": 1.1, "line-opacity": 0.7 } });
  const dots = ISOS.filter((k) => !SHAPED.has(k) && P[k].pt).map((k) => ({ type: "Feature", properties: { iso3: k }, geometry: { type: "Point", coordinates: P[k].pt } }));
  map.addSource("dots", { type: "geojson", data: { type: "FeatureCollection", features: dots } });
  map.addLayer({ id: "c-dots", type: "circle", source: "dots", paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 3.2, 6, 6], "circle-color": NODATA, "circle-stroke-color": "#05061a", "circle-stroke-width": 0.8, "circle-pitch-alignment": "map" } });
  // pattern lines, flows, network reach
  const lp = { "line-color": ["get", "col"], "line-width": ["get", "w"], "line-opacity": ["get", "o"] };
  map.addSource("lines", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
  map.addLayer({ id: "ln-solid", type: "line", source: "lines", filter: ["==", ["get", "sty"], "solid"], layout: { "line-cap": "round" }, paint: lp });
  map.addLayer({ id: "ln-dash", type: "line", source: "lines", filter: ["==", ["get", "sty"], "dash"], paint: Object.assign({ "line-dasharray": [2.2, 1.6] }, lp) });
  map.addLayer({ id: "ln-dot", type: "line", source: "lines", filter: ["==", ["get", "sty"], "dot"], layout: { "line-cap": "round" }, paint: Object.assign({ "line-dasharray": [0.4, 1.6] }, lp) });
  map.addSource("heads", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
  map.addLayer({ id: "ln-head", type: "symbol", source: "heads", layout: { "icon-image": "tri", "icon-size": 0.42, "icon-rotate": ["get", "rot"], "icon-rotation-alignment": "map", "icon-allow-overlap": true, "icon-ignore-placement": true }, paint: { "icon-color": ["get", "col"], "icon-opacity": ["get", "o"] } });
  map.addSource("ends", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
  map.addLayer({ id: "ln-end", type: "circle", source: "ends", paint: { "circle-radius": 3, "circle-color": ["get", "col"], "circle-stroke-color": "#05061a", "circle-stroke-width": 1, "circle-pitch-alignment": "map" } });
  // network headquarters
  map.addSource("nets", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
  map.addLayer({ id: "net-node", type: "symbol", source: "nets", layout: { "icon-image": "diamond", "icon-size": ["get", "s"], "icon-allow-overlap": true, "icon-ignore-placement": true },
    paint: { "icon-color": ["get", "col"], "icon-halo-color": "#05061a", "icon-halo-width": 1.4, "icon-opacity": ["get", "o"] } });
  // cases, clustered so a city with thirty cases is one number until you zoom in
  map.addSource("cases", { type: "geojson", data: { type: "FeatureCollection", features: [] }, cluster: true, clusterRadius: 22, clusterMaxZoom: 7 });
  map.addLayer({ id: "cs-cluster", type: "circle", source: "cases", filter: ["has", "point_count"], paint: { "circle-radius": ["interpolate", ["linear"], ["get", "point_count"], 2, 7, 20, 11, 150, 16], "circle-color": "rgba(10,11,28,.86)", "circle-stroke-color": "#d8d5e6", "circle-stroke-width": 1, "circle-pitch-alignment": "map" } });
  map.addLayer({ id: "cs-cluster-n", type: "symbol", source: "cases", filter: ["has", "point_count"], layout: { "text-field": ["get", "point_count_abbreviated"], "text-font": ["Jost-Regular"], "text-size": 10.5, "text-allow-overlap": true, "text-ignore-placement": true }, paint: { "text-color": "#f0ece4" } });
  map.addLayer({ id: "cs-pt", type: "circle", source: "cases", filter: ["!", ["has", "point_count"]], paint: {
    "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, ["get", "r"], 8, ["*", 1.6, ["get", "r"]]],
    "circle-color": ["get", "col"], "circle-opacity": ["get", "fo"],
    "circle-stroke-color": ["case", ["==", ["get", "ring"], 1], ["get", "col"], "#05061a"], "circle-stroke-width": ["case", ["==", ["get", "ring"], 1], 1.4, 0.9], "circle-stroke-opacity": ["get", "so"],
    "circle-pitch-alignment": "map" } });
  IDS.push("c-fill", "c-est", "c-line", "c-dots", "ln-dot", "ln-dash", "ln-solid", "ln-head", "ln-end", "net-node", "cs-cluster", "cs-cluster-n", "cs-pt", "c-sel", "c-hov"); order();

  const q = (pt, layers, r) => { r = r || 4; const ls = layers.filter((x) => map.getLayer(x)); return ls.length ? map.queryRenderedFeatures([[pt.x - r, pt.y - r], [pt.x + r, pt.y + r]], { layers: ls }) : []; };
  map.on("click", (e) => {
    const cl = q(e.point, ["cs-cluster"], 5)[0];
    if (cl) { map.getSource("cases").getClusterExpansionZoom(cl.properties.cluster_id).then((z) => map.easeTo({ center: cl.geometry.coordinates, zoom: Math.min(z + 0.3, 12), duration: 600 })).catch(() => {}); return; }
    const cp = q(e.point, ["cs-pt"], 5)[0]; if (cp) { openCase(cp.properties.i); return; }
    const np = q(e.point, ["net-node"], 6)[0]; if (np) { openNet(np.properties.i); return; }
    const k = (q(e.point, ["c-dots", "c-fill"], 3)[0] || {}).properties; if (k && P[k.iso3]) select(k.iso3, false);
  });
  map.on("mousemove", (e) => {
    const xy = [e.originalEvent.clientX, e.originalEvent.clientY];
    const cl = q(e.point, ["cs-cluster"], 5)[0];
    if (cl) { map.getCanvas().style.cursor = "pointer"; hov(null); tip("<b>" + cl.properties.point_count + " cases here</b><br><span class=m>Click to zoom in and separate them.</span>", ...xy); return; }
    const cp = q(e.point, ["cs-pt"], 5)[0];
    if (cp) { const c = C[cp.properties.i]; map.getCanvas().style.cursor = "pointer"; hov(null); tip("<b>" + esc(c.n) + "</b><br><span class=m>" + esc(setLabel(c.set)) + " · " + esc(STAT[c.st][0]) + (yrs(c) ? " · " + yrs(c) : "") + "</span>", ...xy); return; }
    const np = q(e.point, ["net-node"], 6)[0];
    if (np) { const n = N[np.properties.i]; map.getCanvas().style.cursor = "pointer"; hov(null); tip("<b>" + esc(n.n) + "</b><br><span class=m>" + esc(n.hq || "") + " · documented in " + (n.reach || []).length + " countr" + ((n.reach || []).length === 1 ? "y" : "ies") + "</span>", ...xy); return; }
    const ln = q(e.point, ["ln-solid", "ln-dash", "ln-dot"], 3)[0];
    if (ln && ln.properties.t) { map.getCanvas().style.cursor = ""; tip(ln.properties.t, ...xy); return; }
    const f = (q(e.point, ["c-dots", "c-fill"], 3)[0] || {}).properties, k = f && f.iso3;
    map.getCanvas().style.cursor = k && P[k] ? "pointer" : "";
    hov(k && P[k] ? k : null);
    if (!k || !P[k]) { tip(null); return; }
    const l = layer(), r = l.get(P[k]);
    tip("<b>" + esc(P[k].n) + "</b><br>" + valText(l, r, P[k]), ...xy);
  });
  map.on("mouseout", () => { tip(null); hov(null); });
}
function hov(k) { if (k === S.hov) return; S.hov = k; if (map.getLayer("c-hov")) map.setFilter("c-hov", ["in", ["get", "iso3"], ["literal", k ? [k] : []]]); }
const setLabel = (k) => (SETS.find((s) => s[0] === k) || [k, k])[1];
const yrs = (c) => { const a = c.y0, b = c.y1; if (!a && !b) return c.yf ? String(c.yf) : ""; if (!b || a === b) return String(a || b); return a + "–" + b; };
function plainRank(l, r) {
  if (!r || r.v == null || l.kind !== "seq" || l.id === "none") return "";
  const vs = ISOS.map((k) => { const x = l.get(P[k]); return x && x.v != null ? x.v : null; }).filter((v) => v != null);
  if (vs.length < 5) return "";
  const below = vs.filter((v) => v < r.v).length / vs.length;
  return below >= 0.5 ? "higher than " + Math.round(100 * below) + "% of the " + vs.length + " places with a figure" : "lower than " + Math.round(100 * vs.filter((v) => v > r.v).length / vs.length) + "% of the " + vs.length + " places with a figure";
}
function valText(l, r, p) {
  if (!r) return '<span class="m">' + (l.id === "doc" || l.id.startsWith("set_") || l.id === "offc" ? "Nothing documented on this map in the chosen years" : l.pat ? "No role in this pattern" : "No figure from this source") + '</span>';
  let s = l.kind === "cat" ? (r.v == null ? l.other : (l.classes.find((c) => c[0] === r.v) || [0, l.other])[1]) : l.f(r.v);
  if (r.est) s += ' <span class="m">· estimate: nothing documented here in these years</span>';
  if (p.proxy && (l.id === "all" || l.id === "market" || l.id === "shield")) s += '<br><span class="m">' + esc(p.proxy) + '</span>';
  const pr = plainRank(l, r); if (pr) s += '<br><span class="m">' + pr + '</span>';
  if (r.note) s += '<br><span class="m">' + esc(r.note.length > 220 ? r.note.slice(0, 217) + "…" : r.note) + '</span>';
  return s;
}

/* ---------- points ---------- */
function patCids() { const l = layer(); return l.pat && S.patOnly ? new Set(l.pat.cids || []) : null; }
function drawCases() {
  const src = map.getSource("cases"); if (!src) return;
  if (!S.pts) { src.setData({ type: "FeatureCollection", features: [] }); return; }
  const only = patCids(), feats = [];
  C.forEach((c, i) => {
    if (!caseOn(c) || !c.ll) return;
    if (only && !only.has(i)) return;
    if (c.llc && !S.ring) return;
    const weak = !COUNTS(c), sel = S.selCase === i || (S.sel && (c.iso === S.sel));
    feats.push({ type: "Feature", properties: { i, col: weak ? "#9a98a6" : setColor(c.set), r: c.v ? Math.min(7.5, 3 + Math.log10(1 + c.v) * 1.1) : 3.2,
      ring: c.llc || weak ? 1 : 0, fo: c.llc || weak ? 0.12 : 0.92, so: sel ? 1 : 0.9 }, geometry: { type: "Point", coordinates: c.ll } });
  });
  src.setData({ type: "FeatureCollection", features: feats });
}
function drawNets() {
  const src = map.getSource("nets"); if (!src) return;
  if (!S.nets) { src.setData({ type: "FeatureCollection", features: [] }); return; }
  src.setData({ type: "FeatureCollection", features: N.map((n, i) => n.ll ? { type: "Feature", properties: { i, col: setColor(n.type === "state" ? "conflict" : n.type), s: 0.42 + Math.min(0.5, (n.reach || []).length / 40), o: S.selNet == null || S.selNet === i ? 1 : 0.45 }, geometry: { type: "Point", coordinates: n.ll } } : null).filter(Boolean) });
}
function bearing(a, b) { return Math.atan2(b[0] - a[0], b[1] - a[1]) * 180 / Math.PI - 90; }
function drawLines() {
  const src = map.getSource("lines"); if (!src) return;
  const feats = [], heads = [], ends = [];
  const add = (a, b, col, w, o, sty, t, head, bend) => {
    const coords = bend === 0 ? straight(a, b, 28) : arc(a, b, 36, bend);
    feats.push({ type: "Feature", properties: { col, w, o, sty, t: t || "" }, geometry: { type: "LineString", coordinates: coords } });
    if (head) { const n = coords.length, p = coords[Math.round(n * 0.62)], q = coords[Math.round(n * 0.62) + 1]; heads.push({ type: "Feature", properties: { col, o, rot: bearing(p, q) }, geometry: { type: "Point", coordinates: p } }); }
  };
  // flows
  F.forEach((f) => {
    if (!S.flows.has(f.type) || !f.a || !f.b) return;
    if (!(f.y1 == null && f.y0 == null) && (Math.max(f.y0 || f.y1, f.y1 || f.y0) < S.from || Math.min(f.y0 || f.y1, f.y1 || f.y0) > S.to)) return;
    const on = S.sel && (f.iso_a === S.sel || f.iso_b === S.sel), dim = S.sel && !on;
    const ft = FLOWT.find((x) => x[0] === f.type) || [];
    add(f.a, f.b, flowColor(f.type), on ? 2.4 : 1.3, dim ? 0.18 : 0.8, ft[3] || "solid", "<b>" + esc(f.n) + "</b><br><span class=m>" + esc(ft[1] || f.type) + (f.y0 ? " · " + f.y0 + (f.y1 && f.y1 !== f.y0 ? "–" + f.y1 : "") : "") + (f.size ? " · " + fmt(f.size, 0) + (f.size_note ? " (" + esc(f.size_note) + ")" : "") : "") + "</span>", true, 0.14);
  });
  // a selected network's documented reach
  if (S.selNet != null && S.nets) {
    const n = N[S.selNet];
    if (n.ll) (n.reach || []).forEach((k) => { const b = ptOf(k); if (b && k !== n.iso) add(n.ll, b, setColor(n.type === "state" ? "conflict" : n.type), 1, 0.7, "dot", "<b>" + esc(n.n) + "</b> → " + esc(P[k].n) + "<br><span class=m>documented presence</span>", false, 0.08); });
    if (n.ll) (n.reach_est || []).forEach((k) => { const b = ptOf(k); if (b && k !== n.iso) add(n.ll, b, "#9a98a6", 0.8, 0.5, "dot", "<b>" + esc(n.n) + "</b> → " + esc(P[k].n) + "<br><span class=m>presence likely, not documented</span>", false, 0.08); });
  }
  // the active pattern's documented connections
  const l = layer();
  if (l.pat) (l.pat.links || []).forEach((k) => { if (k.a && k.b) { add(k.a, k.b, "#f0ece4", 1.5, 0.8, "solid", "<b>" + esc(k.from) + " → " + esc(k.to) + "</b>" + (k.label ? "<br>" + esc(k.label) : "") + (k.years ? "<br><span class=m>" + esc(k.years) + "</span>" : ""), true, 0.1); ends.push({ type: "Feature", properties: { col: "#f0ece4" }, geometry: { type: "Point", coordinates: k.a } }, { type: "Feature", properties: { col: "#f0ece4" }, geometry: { type: "Point", coordinates: k.b } }); } });
  src.setData({ type: "FeatureCollection", features: feats });
  map.getSource("heads").setData({ type: "FeatureCollection", features: heads });
  map.getSource("ends").setData({ type: "FeatureCollection", features: ends });
}

/* ---------- paint ---------- */
function paint() {
  if (!map.getLayer("c-fill")) return;
  computeDoc();
  const l = layer(), d = l.kind === "seq" ? dom(l) : null, m = ["match", ["get", "iso3"]], est = [];
  ISOS.forEach((k) => { const r = l.get(P[k]); m.push(k, colorOf(l, r, d)); if (r && r.est) est.push(k); });
  m.push(NODATA);
  map.setPaintProperty("c-fill", "fill-color", m);
  map.setPaintProperty("c-dots", "circle-color", m);
  const plain = S.layer === "none";
  map.setPaintProperty("c-fill", "fill-opacity", plain ? 0 : ["interpolate", ["linear"], ["zoom"], 0, 0.82, 5, 0.7, 8, 0.45]);
  map.setPaintProperty("c-dots", "circle-opacity", plain ? 0 : 1); map.setPaintProperty("c-dots", "circle-stroke-opacity", plain ? 0 : 1);
  map.setPaintProperty("c-line", "line-opacity", plain ? 0.25 : 0.8);
  map.setFilter("c-est", ["in", ["get", "iso3"], ["literal", est]]);
  map.setFilter("c-sel", ["in", ["get", "iso3"], ["literal", S.sel ? [S.sel] : []]]);
  drawCases(); drawNets(); drawLines(); map.triggerRepaint();
}

/* ---------- the key ---------- */
function buildKey() {
  const groups = [...new Set(L.map((l) => l.group))];
  const nset = (k) => C.filter((c) => c.set === k).length;
  $("#keyBody").innerHTML =
    '<div class="psec" style="margin-top:0">Color the countries by</div>' +
    '<select id="layer" aria-label="What to color the countries by">' + groups.map((g) => '<optgroup label="' + esc(g) + '">' + L.filter((l) => l.group === g).map((l) => '<option value="' + l.id + '">' + esc(l.label.trim()) + '</option>').join("") + '</optgroup>').join("") + '</select>' +
    '<div id="ldesc"></div><div id="legend"></div>' +
    '<div class="psec">Years</div><div class="yrs"><label>From <input type="number" id="yFrom" min="' + YMIN + '" max="' + YMAX + '" value="' + S.from + '"></label><label>to <input type="number" id="yTo" min="' + YMIN + '" max="' + YMAX + '" value="' + S.to + '"></label><button type="button" class="btn" id="yAll">All years</button></div>' +
    '<div class="seg" style="margin-top:4px">' + D.ERAS.map((e) => '<button type="button" class="btn era" data-a="' + e[1] + '" data-b="' + e[2] + '">' + esc(e[0]) + '</button>').join("") + '</div>' +
    '<p class="lsrc">Cases, lines and the documented record follow the years chosen. A case counts if any part of it falls inside them; cases with no date always show.</p>' +
    '<div class="psec">Documented cases <span class="mute" style="text-transform:none;letter-spacing:0">(' + C.length + ')</span></div>' +
    '<label class="chk"><input type="checkbox" id="ptsOn" checked> Show the cases on the map</label>' +
    '<div id="setList">' + SETS.map((s) => '<label class="lg" style="cursor:pointer" title="' + esc(s[2]) + '"><input type="checkbox" data-set="' + s[0] + '" checked><span class="sw pt" data-sw="' + s[0] + '"></span>' + esc(s[1]) + '<span class="n">' + nset(s[0]) + '</span></label>').join("") + '</div>' +
    '<label class="chk"><input type="checkbox" id="unpOn" checked> Include press findings, charges and allegations not yet tried</label>' +
    '<label class="chk"><input type="checkbox" id="ringOn" checked> Include cases placed only at a country\'s center</label>' +
    '<div class="lrow"><span class="lsrc" style="flex:1">Filled dot: the town or site. Ring: no town in the source. Grey ring: acquitted, disproved or unproven (not counted in any score). Size: number of children, where known.</span></div>' +
    '<div class="psec">Lines</div>' +
    FLOWT.map((f) => '<div class="lrow"><label class="chk"><input type="checkbox" data-flow="' + f[0] + '"> ' + esc(f[1]) + ' <span class="mute">(' + F.filter((x) => x.type === f[0]).length + ')</span></label><button type="button" class="ib" data-i="fl_' + f[0] + '" title="What is this?" aria-label="About this line">i</button></div><div class="ipop" id="fl_' + f[0] + '">' + esc(f[2]) + '</div>').join("") +
    '<div class="lrow"><label class="chk"><input type="checkbox" id="netOn"> Networks and institutions (headquarters)</label><button type="button" class="ib" data-i="netI" title="What is this?" aria-label="About networks">i</button></div>' +
    '<div class="ipop" id="netI">The organisations, institutions, platforms and armed groups that recur across the cases, each placed at its headquarters and sized by how many countries it is documented in. Click one to draw where it is documented (dotted lines) and where its presence is only likely (grey). Presence is not proof of abuse in that country; the box says which countries have a case.</div>' +
    '<div class="psec">Find a place</div><input id="find" type="search" placeholder="Country, case or network"><div id="plist" class="scroll"></div>';
  $("#layer").value = S.layer;
  $("#layer").addEventListener("change", (e) => { S.layer = e.target.value; const l = layer(); if (l.pat && l.pat.view) fitView(l.pat.view); update(); });
  const setY = () => { let a = +$("#yFrom").value || YMIN, b = +$("#yTo").value || YMAX; a = Math.max(YMIN, Math.min(YMAX, a)); b = Math.max(YMIN, Math.min(YMAX, b)); if (a > b) [a, b] = [b, a]; S.from = a; S.to = b; update(); };
  $("#yFrom").addEventListener("change", setY); $("#yTo").addEventListener("change", setY);
  $("#yAll").addEventListener("click", () => { $("#yFrom").value = YMIN; $("#yTo").value = YMAX; setY(); });
  $("#keyBody").querySelectorAll(".era").forEach((b) => b.addEventListener("click", () => { $("#yFrom").value = b.dataset.a; $("#yTo").value = b.dataset.b; setY(); }));
  $("#ptsOn").addEventListener("change", (e) => { S.pts = e.target.checked; paint(); });
  $("#unpOn").addEventListener("change", (e) => { S.unproven = e.target.checked; update(); });
  $("#ringOn").addEventListener("change", (e) => { S.ring = e.target.checked; paint(); });
  $("#setList").querySelectorAll("[data-set]").forEach((cb) => cb.addEventListener("change", () => { if (cb.checked) S.sets.add(cb.dataset.set); else S.sets.delete(cb.dataset.set); update(); }));
  $("#keyBody").querySelectorAll("[data-flow]").forEach((cb) => cb.addEventListener("change", () => { if (cb.checked) S.flows.add(cb.dataset.flow); else S.flows.delete(cb.dataset.flow); drawLines(); drawLinesLegend(); }));
  $("#netOn").addEventListener("change", (e) => { S.nets = e.target.checked; if (!S.nets) S.selNet = null; paint(); });
  $("#keyBody").querySelectorAll(".ib").forEach((b) => b.addEventListener("click", () => { const el = $("#" + b.dataset.i); el.classList.toggle("open"); b.classList.toggle("on", el.classList.contains("open")); }));
  $("#find").addEventListener("input", (e) => { S.q = e.target.value.toLowerCase(); drawList(); });
}
function drawSwatches() {
  document.querySelectorAll("[data-sw]").forEach((el) => { el.style.background = setColor(el.dataset.sw); });
  drawLinesLegend();
}
function drawLinesLegend() {
  document.querySelectorAll("[data-flow]").forEach((cb) => { const lab = cb.parentElement; let sw = lab.querySelector(".sw"); if (!sw) { sw = document.createElement("span"); lab.insertBefore(sw, cb.nextSibling); } const ft = FLOWT.find((x) => x[0] === cb.dataset.flow); sw.className = "sw " + (ft[3] === "solid" ? "ln" : "dash"); sw.style.cssText = ft[3] === "solid" ? "background:" + flowColor(ft[0]) : "border-color:" + flowColor(ft[0]) + ";border-top-style:" + (ft[3] === "dot" ? "dotted" : "dashed"); });
}
function patExtra(pt) {
  const h = [];
  h.push('<p class="lsrc">' + (pt.cids || []).length + ' cases on the map belong to this pattern · ' + pt.countries.length + ' countries have a role</p>');
  h.push('<label class="chk"><input type="checkbox" id="patOnly"' + (S.patOnly ? " checked" : "") + '> Show only this pattern\'s cases</label>');
  if (pt.series && pt.series.length) {
    const s = pt.series, mx = Math.max(...s.map((x) => x.value), 1), W = 300, H = 70, bw = W / s.length;
    h.push('<div class="psec">' + esc(pt.series_label || "Count per year") + '</div><svg viewBox="0 0 ' + W + ' ' + (H + 14) + '" style="width:100%;display:block">' + s.map((x, i) => '<rect x="' + (i * bw + 0.5).toFixed(1) + '" y="' + (H - H * x.value / mx).toFixed(1) + '" width="' + Math.max(1, bw - 1).toFixed(1) + '" height="' + (H * x.value / mx).toFixed(1) + '" rx="1" fill="var(--accent-hi)"><title>' + esc(x.year) + ': ' + fmt(x.value, 1) + '</title></rect>').join("") + '<text x="0" y="' + (H + 12) + '" fill="#a3a1b4" font-size="10">' + esc(s[0].year) + '</text><text x="' + W + '" y="' + (H + 12) + '" text-anchor="end" fill="#a3a1b4" font-size="10">' + esc(s[s.length - 1].year) + '</text></svg>' + (pt.series_note ? '<p class="lsrc">' + esc(pt.series_note) + '</p>' : ''));
  }
  if (pt.facts && pt.facts.length) h.push('<div class="psec">The record</div>' + pt.facts.map((f) => '<p class="ldesc">' + esc(f.t) + (f.url ? ' <span class="n">' + link("source", f.url) + '</span>' : '') + '</p>').join(""));
  if (pt.links && pt.links.length) h.push('<details class="pd"><summary>Connections drawn (' + pt.links.length + ')</summary>' + pt.links.map((k) => '<div class="lg" style="display:block">' + esc(k.from) + ' → ' + esc(k.to) + (k.label ? ': ' + esc(k.label) : '') + (k.years ? ' <span class="n">' + esc(k.years) + '</span>' : '') + (k.url ? ' ' + link("source", k.url) : '') + '</div>').join("") + '</details>');
  if (pt.timeline && pt.timeline.length) h.push('<details class="pd"><summary>Timeline (' + pt.timeline.length + ')</summary>' + pt.timeline.slice().sort((x, y) => x.year - y.year).map((t) => '<div class="lg" style="display:block"><b>' + esc(t.year) + '</b> ' + esc(t.event) + (t.source_url ? ' ' + link("source", t.source_url) : '') + '</div>').join("") + '</details>');
  if (pt.claims_per_author && pt.claims_per_author.length) h.push('<div class="psec">Claimed, not established</div>' + pt.claims_per_author.map((c) => '<div class="lg" style="display:block">' + esc(c.claim) + ' <span class="n">' + link(c.author_work, c.url) + '</span></div>').join(""));
  if (pt.uncertain) h.push('<p class="lsrc" style="margin-top:6px"><b>Unproven or disputed:</b> ' + esc(pt.uncertain) + '</p>');
  if (pt.confirmed_by && pt.confirmed_by.length) h.push('<p class="lsrc">Sources: ' + pt.confirmed_by.map((c) => link(c.title, c.url)).join(" · ") + '</p>');
  if (pt.implications) h.push('<div class="psec">What this means</div><div class="means">' + esc(pt.implications).split(/\n\n+/).map((x) => '<p>' + x + '</p>').join("") + '</div>');
  return h.join("");
}
function drawLegend() {
  const l = layer();
  $("#ldesc").innerHTML = '<p class="ldesc">' + esc(l.desc) + '</p>' + (l.src ? '<p class="lsrc">Source: ' + esc(l.src) + '</p>' : "");
  if (l.id === "none") { $("#legend").innerHTML = ""; return; }
  const rs = ISOS.map((k) => [k, l.get(P[k])]);
  let h = "";
  if (l.kind === "seq") {
    const d = dom(l), r = ramp();
    h += '<div class="ramp">' + r.map((c) => '<span style="background:' + c + '"></span>').join("") + '</div>' +
      '<div class="rampl"><span>' + l.f(d[0]) + (l.dom ? "" : " (lowest)") + '</span>' + (l.log ? '<span>spaced by powers of ten</span>' : '') + '<span>' + l.f(d[1]) + (l.dom ? "" : " (highest)") + '</span></div>';
    if (l.id === "all") { const n = rs.filter(([, r]) => r && r.est).length; h += '<div class="lg"><span class="sw" style="background:transparent;outline:1px dashed #cfcbd8"></span>Estimate: nothing documented here in these years<span class="n">' + n + '</span></div>'; }
  } else {
    l.classes.forEach((c, i) => { const n = rs.filter(([, r]) => r && r.v === c[0]).length; h += '<div class="lg"><span class="sw" style="background:' + CATC[i] + '"></span>' + esc(c[1]) + '<span class="n">' + n + '</span></div>'; });
    const no = rs.filter(([, r]) => r && r.other).length;
    if (no) h += '<div class="lg"><span class="sw" style="background:' + OTHER + '"></span>' + esc(l.other) + '<span class="n">' + no + '</span></div>';
  }
  const nod = rs.filter(([, r]) => !r || (l.kind === "seq" && r.v == null)).length;
  h += '<div class="lg"><span class="sw" style="background:' + NODATA + ';outline:1px solid #555"></span>' + (l.pat ? "No role in this pattern" : /^(doc|set_|offc|delay)/.test(l.id) ? "Nothing documented in these years" : "No figure from this source") + '<span class="n">' + nod + '</span></div>';
  h += '<div id="cnt">' + (ISOS.length - nod) + ' of ' + ISOS.length + ' places have a value' + (/^(doc|set_|offc|delay|all)/.test(l.id) && (S.from !== YMIN || S.to !== YMAX) ? ' for ' + S.from + '–' + S.to : '') + '.</div>';
  if (l.pat) h += patExtra(l.pat);
  $("#legend").innerHTML = h;
  const po = $("#patOnly"); if (po) po.addEventListener("change", (e) => { S.patOnly = e.target.checked; drawCases(); });
  $("#legend").querySelectorAll("[data-case]").forEach((a) => a.addEventListener("click", (e) => { e.preventDefault(); openCase(+a.dataset.case); }));
}
function drawList() {
  const l = layer(), q = S.q;
  let h = "";
  if (q && q.length > 1) {
    const cs = C.map((c, i) => [c, i]).filter(([c]) => (c.n + " " + (c.who || "") + " " + (c.place || "")).toLowerCase().includes(q)).slice(0, 30);
    const ns = N.map((n, i) => [n, i]).filter(([n]) => n.n.toLowerCase().includes(q)).slice(0, 10);
    if (ns.length) h += ns.map(([n, i]) => '<div class="pi" data-net="' + i + '"><span class="sw" style="background:' + setColor(n.type === "state" ? "conflict" : n.type) + ';transform:rotate(45deg);width:9px;height:9px"></span>' + esc(n.n) + '<span class="v">network</span></div>').join("");
    if (cs.length) h += cs.map(([c, i]) => '<div class="pi" data-case="' + i + '"><span class="sw" style="background:' + setColor(c.set) + ';border-radius:50%;width:9px;height:9px"></span>' + esc(c.n) + '<span class="v">' + esc(yrs(c)) + '</span></div>').join("");
  }
  const rows = ISOS.map((k) => [k, l.get(P[k])]).filter(([k]) => !q || P[k].n.toLowerCase().includes(q));
  if (l.kind === "seq") rows.sort((a, b) => ((b[1] && b[1].v != null ? b[1].v : -1e9) - (a[1] && a[1].v != null ? a[1].v : -1e9)) || P[a[0]].n.localeCompare(P[b[0]].n));
  const d = l.kind === "seq" ? dom(l) : null;
  h += rows.map(([k, r]) => '<div class="pi' + (S.sel === k ? " sel" : "") + '" data-k="' + k + '"><span class="sw" style="background:' + colorOf(l, r, d) + '"></span>' + esc(P[k].n) + (r && r.est ? ' <span class="mute" title="Estimate: nothing documented in these years">·est</span>' : '') + '<span class="v">' + (r && r.v != null ? (l.kind === "seq" ? l.f(r.v) : "") : "") + '</span></div>').join("");
  $("#plist").innerHTML = h;
  $("#plist").querySelectorAll(".pi").forEach((el) => el.addEventListener("click", () => { if (el.dataset.case) openCase(+el.dataset.case, true); else if (el.dataset.net) openNet(+el.dataset.net, true); else select(el.dataset.k, true); }));
}

/* ---------- the basemap box ---------- */
function buildTr() {
  $("#trBody").innerHTML = '<div class="psec" style="margin-top:0">Basemap</div><div class="bases">' + CulpritsBasemaps.list.map((b) => '<label><input type="radio" name="basemap" value="' + b[0] + '"' + (b[0] === BM.current() ? " checked" : "") + '> ' + esc(b[1]) + '</label>').join("") + '</div>' +
    '<div class="psec">View</div><div class="seg"><button type="button" class="btn on" data-proj="globe">Globe</button><button type="button" class="btn" data-proj="mercator">Flat map</button></div>' +
    '<label class="chk" style="margin-top:8px"><input type="checkbox" id="namesOn" checked> Place names</label>';
  $("#trBody").querySelectorAll("input[name=basemap]").forEach((r) => r.addEventListener("change", () => BM.set(r.value)));
  $("#namesOn").addEventListener("change", (e) => { S.names = e.target.checked; if (S.names) BM.set(BM.current()); else hideNames(); });
  $("#trBody").querySelectorAll("[data-proj]").forEach((b) => b.addEventListener("click", () => { proj = b.dataset.proj; map.setProjection({ type: proj }); freeFlat(); $("#trBody").querySelectorAll("[data-proj]").forEach((x) => x.classList.toggle("on", x === b)); wholeWorld(); }));
}

/* ---------- boxes ---------- */
function bars(rows) { return '<div class="bars">' + rows.map((r) => '<span title="' + esc(r[0]) + '">' + esc(r[0]) + '</span><span class="b"><i style="width:' + Math.round(100 * Math.max(0, Math.min(1, r[1]))) + '%"></i></span><span>' + esc(r[2]) + '</span>').join("") + '</div>'; }
function rankOf(id, k) {
  const l = L.find((x) => x.id === id), vals = ISOS.map((i) => [i, l.get(P[i])]).filter(([, r]) => r && r.v != null).sort((a, b) => b[1].v - a[1].v);
  const i = vals.findIndex((x) => x[0] === k); return i < 0 ? "" : ' <span class="note">(' + (i + 1) + ' of ' + vals.length + ')</span>';
}
function caseRow(c, i, open) {
  const st = STAT[c.st] || [c.st, 0];
  return '<details class="cs"' + (open ? " open" : "") + '><summary><span class="sw" style="background:' + (COUNTS(c) ? setColor(c.set) : "transparent") + ';border:1px solid ' + setColor(c.set) + ';border-radius:50%;width:8px;height:8px;display:inline-block;margin-right:6px"></span>' + esc(c.n) + ' <span class="note">' + esc(yrs(c)) + ' · ' + esc(st[0]) + '</span></summary>' + caseBody(c, i) + '</details>';
}
function caseBody(c, i) {
  const st = STAT[c.st] || [c.st, 0, ""], h = [];
  h.push('<p class="note">' + esc(setLabel(c.set)) + (c.kind ? ' · ' + esc(c.kind) : '') + (c.place ? ' · ' + esc(c.place) : '') + (c.iso && P[c.iso] ? ', ' + esc(P[c.iso].n) : '') + ((c.also || []).length ? ' · also ' + c.also.filter((k) => P[k]).map((k) => esc(P[k].n)).join(", ") : '') + '</p>');
  const kv = [];
  if (yrs(c)) kv.push(["Years", yrs(c)]);
  if (c.fr) kv.push(["First complaint on record", c.fr]);
  if (c.yf) kv.push(["Finding, charge or conviction", c.yf + (c.fr && c.yf >= c.fr ? " (" + (c.yf - c.fr) + " years later)" : "")]);
  if (c.v) kv.push(["Children", fmt(c.v, 0) + (c.vn ? " (" + c.vn + ")" : "")]);
  if (c.off) kv.push(["Offenders", fmt(c.off, 0)]);
  kv.push(["Status", st[0]]);
  h.push('<table class="kv">' + kv.map((r) => '<tr><th>' + esc(r[0]) + '</th><td>' + esc(r[1]) + '</td></tr>').join("") + '</table>');
  if (st[2]) h.push('<p class="note">' + esc(st[2]) + '</p>');
  if (c.who) h.push('<p><b>Who:</b> ' + esc(c.who) + '</p>');
  h.push('<p>' + esc(c.d) + '</p>');
  if (c.offc || c.cover) h.push('<p class="flag"><b>' + (c.offc ? "Officials involved or covered it up." : "Cover-up.") + '</b> ' + esc(c.cover || "") + '</p>');
  const pats = PAT.filter((p) => (p.cids || []).includes(i));
  if (pats.length) h.push('<p class="note">Part of: ' + pats.map((p) => '<a href="#" data-pat="' + p.id + '">' + esc(p.title) + '</a>').join(" · ") + '</p>');
  if (c.net != null && N[c.net]) h.push('<p class="note">Network: <a href="#" data-net="' + c.net + '">' + esc(N[c.net].n) + '</a></p>');
  h.push('<p class="hp-src">' + esc(c.cite || "") + ' ' + link("source", c.url) + (c.url2 ? ' · ' + link("second source", c.url2) : '') + (c.wk ? '<br>The link is an encyclopedia summary of the source named above; the original could not be opened for this map.' : '') + '</p>');
  return h.join("");
}
function wireBox() {
  $("#detBody").querySelectorAll("[data-pat]").forEach((a) => a.addEventListener("click", (e) => { e.preventDefault(); showPattern(a.dataset.pat); }));
  $("#detBody").querySelectorAll("[data-net]").forEach((a) => a.addEventListener("click", (e) => { e.preventDefault(); openNet(+a.dataset.net, true); }));
  $("#detBody").querySelectorAll("[data-k]").forEach((a) => a.addEventListener("click", (e) => { e.preventDefault(); select(a.dataset.k, true); }));
  $("#detBody").querySelectorAll("[data-case]").forEach((a) => a.addEventListener("click", (e) => { e.preventDefault(); openCase(+a.dataset.case, true); }));
}
function fitView(v) { try { const fb = freeBox(), pad = { left: fb.L + 20, right: fb.R + 20, top: 30, bottom: 30 }; const cam = map.cameraForBounds(v, { padding: pad }); if (cam && cam.center) map.easeTo(Object.assign(cam, { duration: 900 })); } catch (e) {} }
function showPattern(id) { S.layer = "pat_" + id; $("#layer").value = S.layer; const l = layer(); if (l.pat && l.pat.view) fitView(l.pat.view); update(); const k = $("#key"); if (k.classList.contains("min")) $("#toggleKey").click(); $("#ldesc").scrollIntoView({ behavior: "smooth", block: "start" }); }
function detail(k) {
  const p = P[k], h = [], i = p.ind || {};
  h.push('<div class="hp-k">Country</div><h3>' + esc(p.n) + '</h3>');
  const tipT = i.tip ? "US ranking 2025: " + TIPL[i.tip] : "";
  if (tipT) h.push('<p class="hp-sub">' + esc(tipT) + '</p>');
  const a = allScore(p);
  h.push('<div class="hp-h">Likely scale and impunity</div>');
  if (a) {
    h.push('<p><span class="big">' + fmt(a.v, 0) + '</span> of 100' + rankOf("all", k) + '</p>');
    if (a.est) h.push('<p class="flag"><b>Estimate.</b> Nothing on this map is documented here' + (S.from !== YMIN || S.to !== YMAX ? ' for ' + S.from + '–' + S.to : '') + ', so the score rests on the indicators below: how large the trade is likely to be and how little stops it. No record is not the same as no abuse; see the pattern "Where nobody is counting".</p>');
    const rows = [["Documented record", (a.d || 0) / 100, fmt(a.d || 0, 0)]];
    if (a.m != null) rows.push(["Likely size of the trade", a.m / 100, fmt(a.m, 0)]);
    if (a.s != null) rows.push(["How little stands in the way", a.s / 100, fmt(a.s, 0)]);
    h.push(bars(rows));
  } else h.push('<p class="note">No indicator covers this place and nothing is documented here.</p>');
  if (p.proxy) h.push('<p class="note">' + esc(p.proxy) + '</p>');
  const mp = marketParts(p), sp = shieldParts(p);
  if (mp.length || sp.length) h.push('<details><summary>The indicators</summary>' + (mp.length ? '<p class="note">Size of the trade</p>' + bars(mp) : '') + (sp.length ? '<p class="note">What stands in the way (more = less)</p>' + bars(sp) : '') + (i.ht21 != null && i.ht25 != null ? '<p class="note">GI-TOC trafficking score: ' + fmt(i.ht21, 1) + ' (2021), ' + fmt(i.ht23, 1) + ' (2023), ' + fmt(i.ht25, 1) + ' (2025).</p>' : '') + (i.ncm != null ? '<p class="note">NCMEC CyberTipline reports, 2024: ' + fmt(i.ncm, 0) + '.</p>' : '') + (i.gsin ? '<p class="note">Walk Free estimate: ' + fmt(i.gsin, 0) + ' people in modern slavery (2023).</p>' : '') + '</details>');
  // behind the scenes
  const roles = PAT.map((pt) => [pt, pt.countries.find((c) => c.iso3 === k)]).filter((x) => x[1]);
  if (roles.length) {
    h.push('<div class="hp-h">Behind the scenes: patterns this country is part of</div>');
    roles.forEach(([pt, c]) => h.push('<div class="bts"><a href="#" data-pat="' + pt.id + '">' + esc(pt.title) + '</a> <span class="note">· ' + esc(c.role) + '</span>' + (c.note ? '<p>' + esc(c.note) + '</p>' : '') + '</div>'));
  }
  const cs = casesOf(k).map((c) => [c, C.indexOf(c)]).sort((x, y) => ((y[0].y1 || y[0].yf || y[0].y0 || 0) - (x[0].y1 || x[0].yf || x[0].y0 || 0)));
  const all = C.filter((c) => c.iso === k || (c.also || []).includes(k)).length;
  h.push('<div class="hp-h">Documented cases' + (cs.length ? ' — ' + cs.length : '') + (all > cs.length ? ' <span class="note" style="text-transform:none;letter-spacing:0">(' + (all - cs.length) + ' more outside the chosen years or kinds)</span>' : '') + '</div>');
  if (cs.length) {
    const off = cs.filter(([c]) => c.offc && COUNTS(c)).length, ds = cs.filter(([c]) => COUNTS(c) && c.fr && c.yf && c.yf >= c.fr).map(([c]) => c.yf - c.fr);
    const sc = {}; cs.forEach(([c]) => { sc[c.set] = (sc[c.set] || 0) + 1; });
    h.push('<p class="note">' + Object.keys(sc).sort((x, y) => sc[y] - sc[x]).map((s) => sc[s] + ' ' + esc(setLabel(s).toLowerCase())).join(" · ") + (off ? ' · officials involved or covering up in ' + off : '') + (ds.length ? ' · median ' + fmt(median(ds), 0) + ' years from first complaint to action (' + ds.length + ' cases)' : '') + '</p>');
    cs.forEach(([c, ci]) => h.push(caseRow(c, ci, false)));
  } else h.push('<p class="note">None on this map' + (all ? ' in the chosen years or kinds' : '') + '.</p>');
  const fl = F.filter((f) => f.iso_a === k || f.iso_b === k);
  if (fl.length) h.push('<div class="hp-h">Movements in and out — ' + fl.length + '</div><ul>' + fl.map((f) => '<li><b>' + esc(f.n) + '</b> <span class="note">' + esc((FLOWT.find((x) => x[0] === f.type) || [0, f.type])[1]) + (f.y0 ? ', ' + f.y0 + (f.y1 && f.y1 !== f.y0 ? '–' + f.y1 : '') : '') + '</span>. ' + esc(f.d || "") + ' <span class="note">' + link(f.cite || "source", f.url) + '</span></li>').join("") + '</ul>');
  const ns = N.map((n, ni) => [n, ni]).filter(([n]) => n.iso === k || (n.reach || []).includes(k) || (n.reach_est || []).includes(k));
  if (ns.length) h.push('<div class="hp-h">Networks and institutions here — ' + ns.length + '</div><p class="note">' + ns.map(([n, ni]) => '<a href="#" data-net="' + ni + '">' + esc(n.n) + '</a>' + (n.iso === k ? ' (headquarters)' : (n.reach || []).includes(k) ? '' : ' (likely, not documented)')).join(" · ") + '</p>');
  h.push('<p class="hp-src">Indicators: GI-TOC Global Organized Crime Index 2025; Walk Free Global Slavery Index 2023; NCMEC CyberTipline 2024; US Trafficking in Persons Report 2025. Each case links its own source.</p>');
  $("#detBody").innerHTML = h.join(""); wireBox();
}
function select(k, fly) {
  tip(null); S.sel = k; S.selCase = null; S.selNet = null; detail(k); $("#det").classList.add("open"); $("#det").scrollTop = 0;
  paint(); drawList(); drawCharts();
  if (fly && P[k].pt) { const fb = freeBox(); map.easeTo({ center: P[k].pt, zoom: Math.max(map.getZoom(), proj === "globe" ? 2.2 : 3), padding: { left: fb.L, right: fb.R, top: 10, bottom: 10 }, duration: 800 }); }
}
function openCase(i, fly) {
  const c = C[i]; tip(null); S.selCase = i; S.selNet = null; S.sel = null;
  $("#detBody").innerHTML = '<div class="hp-k">' + esc(setLabel(c.set)) + '</div><h3>' + esc(c.n) + '</h3>' + caseBody(c, i) + (P[c.iso] ? '<p class="note"><a href="#" data-k="' + c.iso + '">Open ' + esc(P[c.iso].n) + '</a></p>' : '');
  wireBox(); $("#det").classList.add("open"); $("#det").scrollTop = 0; paint(); drawCharts();
  if (fly && c.ll) { const fb = freeBox(); map.easeTo({ center: c.ll, zoom: Math.max(map.getZoom(), 3.2), padding: { left: fb.L, right: fb.R, top: 10, bottom: 10 }, duration: 800 }); }
}
function openNet(i, fly) {
  const n = N[i]; tip(null); S.selNet = i; S.selCase = null; S.sel = null;
  if (!S.nets) { S.nets = true; const cb = $("#netOn"); if (cb) cb.checked = true; }
  const cs = C.map((c, ci) => [c, ci]).filter(([c]) => c.net === i).sort((a, b) => (a[0].y0 || 0) - (b[0].y0 || 0));
  const h = ['<div class="hp-k">Network or institution · ' + esc(setLabel(n.type === "state" ? "conflict" : n.type)) + '</div><h3>' + esc(n.n) + '</h3>'];
  h.push('<p class="hp-sub">' + esc([n.hq, P[n.iso] && P[n.iso].n].filter(Boolean).join(", ")) + (n.y0 ? ' · ' + n.y0 + (n.y1 ? '–' + n.y1 : ' to now') : '') + (n.status ? ' · ' + esc(n.status) : '') + '</p>');
  h.push('<p>' + esc(n.d) + '</p>');
  if ((n.reach || []).length) h.push('<p class="note"><b>Documented in ' + n.reach.length + ':</b> ' + n.reach.filter((k) => P[k]).map((k) => '<a href="#" data-k="' + k + '">' + esc(P[k].n) + '</a>').join(", ") + '</p>');
  if ((n.reach_est || []).length) h.push('<p class="note"><b>Likely, not documented (' + n.reach_est.length + '):</b> ' + n.reach_est.filter((k) => P[k]).map((k) => esc(P[k].n)).join(", ") + (n.reach_note ? '. ' + esc(n.reach_note) : '') + '</p>');
  if (cs.length) { h.push('<div class="hp-h">Cases on this map — ' + cs.length + '</div>'); cs.forEach(([c, ci]) => h.push(caseRow(c, ci, false))); }
  h.push('<p class="hp-src">' + esc(n.cite || "") + ' ' + link("source", n.url) + '</p>');
  $("#detBody").innerHTML = h.join(""); wireBox(); $("#det").classList.add("open"); $("#det").scrollTop = 0; paint(); drawCharts();
  if (fly && n.ll) { const fb = freeBox(); map.easeTo({ center: n.ll, padding: { left: fb.L, right: fb.R, top: 10, bottom: 10 }, duration: 800 }); }
}
function deselect() { S.sel = null; S.selCase = null; S.selNet = null; $("#det").classList.remove("open"); paint(); drawList(); drawCharts(); }

/* ---------- chart windows ---------- */
const CHARTS = [["table", "Every place"], ["time", "Through time"], ["delay", "Waiting for action"], ["nets", "Networks"]];
const WINS = {}; let zTop = 950, cascade = 0;
function buildDock() {
  $("#dockBtns").innerHTML = CHARTS.map((c) => '<button type="button" class="tab" data-w="' + c[0] + '">' + esc(c[1]) + '</button>').join("");
  $("#dockBtns").querySelectorAll("[data-w]").forEach((b) => b.addEventListener("click", () => WINS[b.dataset.w] ? closeWin(b.dataset.w) : openWin(b.dataset.w)));
}
function openWin(id) {
  const def = CHARTS.find((c) => c[0] === id), el = document.createElement("div");
  el.className = "win card";
  el.innerHTML = '<div class="wh"><span class="wt">' + esc(def[1]) + '</span><button type="button" class="wm" title="Fill the screen">⤢</button><button type="button" class="wx" title="Close">×</button></div><div class="wb scroll"></div><div class="wfoot"></div>';
  document.body.appendChild(el);
  const small = innerWidth < 760, W = small ? innerWidth - 16 : Math.min(id === "table" ? 1180 : 980, innerWidth - 60), H = small ? Math.min(520, innerHeight - 90) : Math.min(640, innerHeight - 90);
  Object.assign(el.style, { width: W + "px", height: H + "px", left: (small ? 8 : Math.max(8, (innerWidth - W) / 2 + (cascade - 1) * 26)) + "px", top: (small ? 50 : Math.max(8, 40 + cascade * 26)) + "px", zIndex: ++zTop });
  cascade = (cascade + 1) % 4;
  const w = WINS[id] = { id, el, body: el.querySelector(".wb"), foot: el.querySelector(".wfoot"), sort: null, dir: -1, ser: null };
  el.addEventListener("pointerdown", () => { el.style.zIndex = ++zTop; });
  el.querySelector(".wx").addEventListener("click", () => closeWin(id));
  el.querySelector(".wm").addEventListener("click", () => { if (w.prev) { Object.assign(el.style, w.prev); w.prev = null; } else { w.prev = { left: el.style.left, top: el.style.top, width: el.style.width, height: el.style.height }; Object.assign(el.style, { left: "8px", top: "8px", width: (innerWidth - 16) + "px", height: (innerHeight - 16) + "px" }); } });
  const head = el.querySelector(".wh");
  head.addEventListener("pointerdown", (e) => {
    if (e.target.closest("button")) return;
    const r = el.getBoundingClientRect(), dx = e.clientX - r.left, dy = e.clientY - r.top; head.setPointerCapture(e.pointerId);
    const mv = (ev) => { el.style.left = Math.max(-r.width + 80, Math.min(innerWidth - 80, ev.clientX - dx)) + "px"; el.style.top = Math.max(0, Math.min(innerHeight - 36, ev.clientY - dy)) + "px"; };
    const up = () => { head.removeEventListener("pointermove", mv); head.removeEventListener("pointerup", up); };
    head.addEventListener("pointermove", mv); head.addEventListener("pointerup", up);
  });
  let last = ""; w.ro = new ResizeObserver(() => { const kk = w.body.clientWidth + "x" + w.body.clientHeight; if (kk !== last) { last = kk; if (id === "time" || id === "delay") drawWin(id); } }); w.ro.observe(w.body);
  $('#dockBtns [data-w="' + id + '"]').classList.add("on");
  drawWin(id);
}
function closeWin(id) { const w = WINS[id]; if (!w) return; w.ro.disconnect(); w.el.remove(); delete WINS[id]; tip(null); $('#dockBtns [data-w="' + id + '"]').classList.remove("on"); }
function drawCharts() { Object.keys(WINS).forEach(drawWin); }
function drawWin(id) { const w = WINS[id]; if (!w) return; if (id === "table") drawTable(w); else if (id === "time") drawTime(w); else if (id === "delay") drawDelay(w); else drawNetWin(w); }

const TCOLS = [["n", "Place"], ["all", "Combined (0–100)"], ["doc", "Documented (0–100)"], ["cases", "Cases"], ["offc", "Officials involved"], ["delay", "Median delay, years"], ["market", "Size of trade (0–100)"], ["shield", "Little in the way (0–100)"], ["ht25", "Trafficking (GI-TOC)"], ["tip", "US ranking"], ["prev", "Slavery /1,000"], ["ncm", "Online reports /100k"], ["sea", "Officials w/ criminals"], ["pats", "Patterns"]];
function cellVal(id, k) {
  const p = P[k];
  if (id === "n") return p.n;
  if (id === "cases") return casesOf(k).length || null;
  if (id === "pats") return PAT.filter((pt) => pt.countries.some((c) => c.iso3 === k)).length || null;
  if (id === "tip") return p.ind && p.ind.tip ? TIPL[p.ind.tip].replace("Special case (not ranked)", "Special") : null;
  const l = L.find((x) => x.id === id), r = l && l.get(p);
  return r && r.v != null ? r.v : null;
}
function drawTable(w) {
  const keys = ISOS.slice(), s = w.sort;
  if (s) keys.sort((a, b) => { const x = cellVal(s, a), y = cellVal(s, b); if (x == null && y == null) return 0; if (x == null) return 1; if (y == null) return -1; return (typeof x === "number" ? x - y : String(x).localeCompare(String(y))) * w.dir; });
  const cell = (id, k) => { const v = cellVal(id, k); if (v == null) return '<span class="mute">–</span>'; if (typeof v !== "number") return esc(v); const r = id === "all" ? allScore(P[k]) : null; return fmt(v, /^(all|doc|market|shield|delay|cases|offc|pats|ncm)$/.test(id) ? 0 : 1) + (r && r.est ? '<span class="mute">*</span>' : ''); };
  w.body.innerHTML = '<table class="all"><thead><tr>' + TCOLS.map((c) => '<th data-c="' + c[0] + '"' + (s === c[0] ? ' class="on"' : '') + '>' + esc(c[1]) + (s === c[0] ? (w.dir > 0 ? " ▲" : " ▼") : "") + '</th>').join("") + '</tr></thead><tbody>' +
    keys.map((k) => '<tr class="r' + (S.sel === k ? " sel" : "") + '" data-k="' + k + '">' + TCOLS.map((c) => '<td>' + cell(c[0], k) + '</td>').join("") + '</tr>').join("") + '</tbody></table>';
  w.body.querySelectorAll("th").forEach((th) => th.addEventListener("click", () => { const c = th.dataset.c; if (w.sort === c) w.dir = -w.dir; else { w.sort = c; w.dir = c === "n" ? 1 : -1; } drawTable(w); }));
  w.body.querySelectorAll("tr.r").forEach((tr) => tr.addEventListener("click", () => select(tr.dataset.k, true)));
  w.foot.textContent = "Click a heading to sort, a row to open the place. * the combined score is an estimate: nothing documented there in the chosen years. Case counts follow the years and kinds ticked in the key.";
}
function drawTime(w) {
  const Wd = w.body.clientWidth || 800, Ht = Math.max(220, (w.body.clientHeight || 400) - 44), m = { l: 40, r: 16, t: 14, b: 26 };
  const sers = D.SER || [];
  if (w.ser == null) w.ser = "cases";
  let ctl = '<div class="wctl"><select id="serSel"><option value="cases">Cases on this map, by decade and setting</option>' + sers.map((s, i) => '<option value="' + i + '"' + (String(w.ser) === String(i) ? " selected" : "") + '>' + esc(s.title) + '</option>').join("") + '</select></div>';
  let g = "", foot = "";
  if (w.ser === "cases") {
    const dec = {}, sel = S.sel;
    C.forEach((c) => { if (!caseOn(c)) return; if (sel && c.iso !== sel && !(c.also || []).includes(sel)) return; const y = c.y0 || c.yf || c.y1; if (!y) return; const d = Math.floor(y / 10) * 10; dec[d] = dec[d] || {}; dec[d][c.set] = (dec[d][c.set] || 0) + 1; });
    const ds = Object.keys(dec).map(Number).sort((a, b) => a - b);
    if (!ds.length) { w.body.innerHTML = ctl + '<p class="mean" style="padding:12px">No dated cases for this selection.</p>'; wireSer(w); return; }
    const d0 = ds[0], d1 = ds[ds.length - 1], n = (d1 - d0) / 10 + 1, bw = (Wd - m.l - m.r) / n;
    const tot = (d) => Object.values(dec[d] || {}).reduce((a, b) => a + b, 0), mx = Math.max(...ds.map(tot), 1);
    const Y = (v) => m.t + (Ht - m.t - m.b) * (1 - v / mx);
    [0, 0.5, 1].forEach((f) => { const v = Math.round(mx * f); g += '<line class="gl" x1="' + m.l + '" x2="' + (Wd - m.r) + '" y1="' + Y(v) + '" y2="' + Y(v) + '"/><text x="' + (m.l - 6) + '" y="' + (Y(v) + 3) + '" text-anchor="end">' + v + '</text>'; });
    for (let i = 0; i < n; i++) {
      const d = d0 + i * 10; let acc = 0;
      SETK.forEach((s) => { const v = (dec[d] || {})[s] || 0; if (!v) return; const y1 = Y(acc + v), y0 = Y(acc); g += '<rect x="' + (m.l + i * bw + 1).toFixed(1) + '" y="' + y1.toFixed(1) + '" width="' + Math.max(1, bw - 2).toFixed(1) + '" height="' + (y0 - y1).toFixed(1) + '" fill="' + setColor(s) + '"><title>' + d + 's · ' + esc(setLabel(s)) + ': ' + v + '</title></rect>'; acc += v; });
      if (n <= 16 || i % 2 === 0) g += '<text x="' + (m.l + i * bw + bw / 2) + '" y="' + (Ht - 8) + '" text-anchor="middle">' + d + 's</text>';
    }
    foot = (sel ? esc(P[sel].n) + ": " : "") + "Cases by the decade they began, colored by setting. Follows the years and kinds ticked in the key" + (sel ? "; close the country box to see every country." : "; open a country to see its own.") + " The rise in recent decades is partly the rise in looking: most inquiries are recent.";
  } else {
    const s = sers[+w.ser]; const rows = s.rows.filter((r) => r[1] != null);
    const x0 = rows[0][0], x1 = rows[rows.length - 1][0], mx = Math.max(...rows.map((r) => r[1]), 1), n = rows.length, bw = (Wd - m.l - m.r) / n;
    const Y = (v) => m.t + (Ht - m.t - m.b) * (1 - v / mx);
    [0, 0.5, 1].forEach((f) => { const v = mx * f; g += '<line class="gl" x1="' + m.l + '" x2="' + (Wd - m.r) + '" y1="' + Y(v) + '" y2="' + Y(v) + '"/><text x="' + (m.l - 6) + '" y="' + (Y(v) + 3) + '" text-anchor="end">' + (v >= 1e6 ? fmt(v / 1e6, 1) + "m" : v >= 1e3 ? fmt(v / 1e3, 0) + "k" : fmt(v, 0)) + '</text>'; });
    rows.forEach((r, i) => { g += '<rect x="' + (m.l + i * bw + 1).toFixed(1) + '" y="' + Y(r[1]).toFixed(1) + '" width="' + Math.max(1, bw - 2).toFixed(1) + '" height="' + (Y(0) - Y(r[1])).toFixed(1) + '" fill="var(--accent-hi)"><title>' + esc(r[0]) + ': ' + fmt(r[1], 0) + '</title></rect>'; if (n <= 24 || i % Math.ceil(n / 14) === 0) g += '<text x="' + (m.l + i * bw + bw / 2) + '" y="' + (Ht - 8) + '" text-anchor="middle">' + esc(r[0]) + '</text>'; });
    foot = esc(s.note || "") + ' Source: ' + link(s.src, s.url);
  }
  w.body.innerHTML = ctl + '<div class="lc" style="top:40px"><svg>' + g + '</svg></div>';
  w.foot.innerHTML = foot;
  wireSer(w);
}
function wireSer(w) { const s = w.body.querySelector("#serSel"); if (s) { s.value = String(w.ser); s.addEventListener("change", (e) => { w.ser = e.target.value === "cases" ? "cases" : +e.target.value; drawTime(w); }); } }
function drawDelay(w) {
  const rows = C.map((c, i) => [c, i]).filter(([c]) => c.fr && c.yf && c.yf >= c.fr && S.sets.has(c.set) && COUNTS(c)).sort((a, b) => (b[0].yf - b[0].fr) - (a[0].yf - a[0].fr));
  if (!rows.length) { w.body.innerHTML = '<p class="mean" style="padding:12px">No case has both dates yet.</p>'; return; }
  const x0 = Math.min(...rows.map((r) => r[0].fr)), x1 = Math.max(...rows.map((r) => r[0].yf));
  const Wd = w.body.clientWidth || 800, rowH = 15, m = { l: 260, r: 50, t: 22 }, H = m.t + rows.length * rowH + 10;
  const X = (y) => m.l + (Wd - m.l - m.r) * (y - x0) / Math.max(1, x1 - x0);
  let g = "";
  for (let y = Math.ceil(x0 / 10) * 10; y <= x1; y += 10) g += '<line class="gl" x1="' + X(y) + '" x2="' + X(y) + '" y1="' + (m.t - 6) + '" y2="' + H + '"/><text x="' + X(y) + '" y="' + (m.t - 9) + '" text-anchor="middle">' + y + '</text>';
  rows.forEach(([c, i], j) => { const y = m.t + j * rowH + 8, col = setColor(c.set);
    g += '<g class="dr" data-i="' + i + '" style="cursor:pointer"><text x="' + (m.l - 8) + '" y="' + (y + 3.5) + '" text-anchor="end" style="fill:#d6d3df">' + esc(c.n.length > 44 ? c.n.slice(0, 42) + "…" : c.n) + '</text><line x1="' + X(c.fr) + '" x2="' + X(c.yf) + '" y1="' + y + '" y2="' + y + '" stroke="' + col + '" stroke-width="2.4"/><circle cx="' + X(c.fr) + '" cy="' + y + '" r="3" fill="none" stroke="' + col + '"/><circle cx="' + X(c.yf) + '" cy="' + y + '" r="3" fill="' + col + '"/><text x="' + (X(c.yf) + 6) + '" y="' + (y + 3.5) + '">' + (c.yf - c.fr) + ' yrs</text><rect x="0" y="' + (y - 7) + '" width="' + Wd + '" height="' + rowH + '" fill="transparent"><title>' + esc(c.n) + ': first complaint ' + c.fr + ', action ' + c.yf + '</title></rect></g>'; });
  const ds = rows.map((r) => r[0].yf - r[0].fr);
  w.body.innerHTML = '<div style="padding:8px 14px 0"><p class="mean" style="margin:0">' + rows.length + ' cases whose sources date both the first complaint and the first conviction, charge or official finding. Median wait: ' + fmt(median(ds), 0) + ' years; ' + ds.filter((d) => d >= 10).length + ' waited ten years or more. Hollow dot: first complaint. Filled dot: first action. Click a row to open the case.</p></div><svg style="display:block;width:100%;height:' + H + 'px" class="dsvg">' + g + '</svg>';
  w.body.querySelectorAll(".dr").forEach((el) => el.addEventListener("click", () => openCase(+el.dataset.i, true)));
  w.foot.textContent = "Only the kinds ticked in the key, and only cases a court, inquiry, admission, settlement, charge or press investigation established (no allegations, acquittals or disproved claims). A complaint 'on record' means the sources say it reached police, an employer, a church, a school or officials, not that it was acted on.";
}
function drawNetWin(w) {
  const rows = N.map((n, i) => [n, i, C.filter((c) => c.net === i)]).sort((a, b) => (b[0].reach || []).length - (a[0].reach || []).length || b[2].length - a[2].length);
  w.body.innerHTML = '<table class="all"><thead><tr><th>Network or institution</th><th>Setting</th><th>Headquarters</th><th>Years</th><th>Status</th><th>Documented in</th><th>Likely in</th><th>Cases here</th></tr></thead><tbody>' +
    rows.map(([n, i, cs]) => '<tr class="r' + (S.selNet === i ? " sel" : "") + '" data-n="' + i + '"><td style="white-space:normal;min-width:180px;max-width:320px">' + esc(n.n) + '</td><td>' + esc(setLabel(n.type === "state" ? "conflict" : n.type)) + '</td><td style="white-space:normal">' + esc([n.hq, P[n.iso] && P[n.iso].n].filter(Boolean).join(", ")) + '</td><td>' + esc(n.y0 ? n.y0 + "–" + (n.y1 || "") : "") + '</td><td>' + esc(n.status || "") + '</td><td>' + (n.reach || []).length + '</td><td>' + (n.reach_est || []).length + '</td><td>' + cs.length + '</td></tr>').join("") + '</tbody></table>';
  w.body.querySelectorAll("tr.r").forEach((tr) => tr.addEventListener("click", () => openNet(+tr.dataset.n, true)));
  w.foot.textContent = "Sorted by the number of countries each is documented in. Click a row to draw its reach on the map.";
}

/* ---------- the sky ---------- */
function stars() {
  let seed = 1977; const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
  const W = 1400, H = 1000, c = document.createElement("canvas"); c.width = W; c.height = H;
  const g = c.getContext("2d"); g.fillStyle = "#03040a"; g.fillRect(0, 0, W, H);
  [[.22, .30, 520, "48,58,92", .10], [.78, .68, 600, "70,52,86", .08], [.58, .14, 420, "42,74,84", .06]].forEach(([x, y, r, rgb, a]) => { const gr = g.createRadialGradient(x * W, y * H, 0, x * W, y * H, r); gr.addColorStop(0, "rgba(" + rgb + "," + a + ")"); gr.addColorStop(1, "rgba(" + rgb + ",0)"); g.fillStyle = gr; g.fillRect(0, 0, W, H); });
  const tints = ["255,255,255", "214,224,255", "236,232,246", "224,236,240"];
  for (let i = 0; i < 2600; i++) { g.beginPath(); g.arc(rnd() * W, rnd() * H, .25 + rnd() * .55, 0, 7); g.fillStyle = "rgba(" + tints[(rnd() * 4) | 0] + "," + (.15 + rnd() * .55) + ")"; g.fill(); }
  const el = $("#map"); el.style.background = '#03040a url(' + c.toDataURL("image/jpeg", .9) + ') repeat'; el.style.backgroundSize = W + "px " + H + "px";
  const drift = () => { const ct = map.getCenter(), z = map.getZoom(); el.style.backgroundPosition = Math.round(-ct.lng * 3) + "px " + Math.round(ct.lat * 3 + z * 6) + "px"; };
  map.on("move", drift); drift();
}

function update() { computeDoc(); drawLegend(); drawSwatches(); paint(); drawList(); drawCharts(); if (S.sel) detail(S.sel); }
function init() {
  buildKey(); buildTr(); buildDock(); stars(); computeDoc(); drawSwatches();
  fetch(BOUND_URL).then((r) => r.json()).then((geo) => { addLayers(geo); ready = true; update(); }).catch((e) => { console.warn("boundaries", e); });
  $("#detX").addEventListener("click", deselect);
  $("#worldBtn").addEventListener("click", wholeWorld);
  $("#toggleKey").addEventListener("click", () => { const p = $("#key"); p.classList.toggle("min"); $("#toggleKey").textContent = p.classList.contains("min") ? "+" : "−"; });
  $("#toggleTr").addEventListener("click", () => { const p = $("#tr"); p.classList.toggle("min"); $("#toggleTr").textContent = p.classList.contains("min") ? "Basemap +" : "−"; });
  if (innerWidth <= 820) { $("#key").classList.add("min"); $("#toggleKey").textContent = "+"; $("#tr").classList.add("min"); $("#toggleTr").textContent = "Basemap +"; }
  drawLegend(); drawList();
  map.jumpTo({ center: [12, 22], zoom: startZoom(), padding: { left: freeBox().L, right: freeBox().R, top: 0, bottom: 0 } });
}

/* ---------- about and sources ---------- */
const info = $("#info");
info.innerHTML = D.ABOUT;
const btn = $("#infoBtn");
const toggle = (open) => { const on = info.classList.toggle("open", typeof open === "boolean" ? open : undefined); btn.textContent = on ? "Close" : "About and sources"; };
document.addEventListener("keydown", (e) => { if (e.key !== "Escape") return; if (info.classList.contains("open")) toggle(false); else if (S.sel || S.selCase != null || S.selNet != null) deselect(); });
btn.addEventListener("click", toggle);
$("#infoClose").addEventListener("click", () => toggle(false));
btn.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); } });
})();
