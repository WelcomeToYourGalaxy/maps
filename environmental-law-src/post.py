# -*- coding: utf-8 -*-
# Second edition engine changes. Runs inside build.py (uses sub() and h).
# 1. the atlas cartouche, lettered for this map
a = h.index('window.PLATE_IMG = "data:image/webp;base64,') + len('window.PLATE_IMG = "data:image/webp;base64,'); b = h.index('"', a)
h = h[:a] + base64.b64encode(open("/home/claude/work/plate/plate.webp", "rb").read()).decode() + h[b:]

# 2. lines never take the short way across the Pacific: they run across the Atlantic and Eurasia, so nothing is split between the two edges of the flat map
sub("  while (x2 - x1 > 180) x2 -= 360; while (x2 - x1 < -180) x2 += 360;\n", "")

# 3. no closing box: the story stops on its last slide
sub("""  TL.phase = "outro"; TL.playing = false; $("#slide").classList.remove("on"); chapBox("end"); drawTL();
  const n = STORY.steps.length; if (n) paintStory(n - 1, 1); TL.free = false; fitFlow(f);""", """  TL.playing = false; setPlayIcon(); drawTL();""")

# 4. the bodies most responsible: a switch in the key, the closing slide, and the reason on each card
sub("""const vis = PLAY.filter((p) => !S.off[p.t] && !(S.bigOnly && p.sm && !STORY.f));""",
    """const vis = PLAY.filter((p) => !S.off[p.t] && !(S.bigOnly && p.sm && !STORY.f) && !(((S.topOnly && !STORY.f) || TOPSTEP) && !p.top));""")
sub("""function playerFeatures() {""", """let TOPSTEP = false;
function playerFeatures() {""")
sub("""  TL.seg = k; const s = STORY.steps[k]; lastPaint = "";""", """  TL.seg = k; const s = STORY.steps[k]; lastPaint = "";
  if (!!s.top !== TOPSTEP) { TOPSTEP = !!s.top; setPlayers(); }""")
sub("""  STEPDATA.k = null; STEPDATA.net = null; $("#slide").classList.remove("on");""", """  STEPDATA.k = null; STEPDATA.net = null; $("#slide").classList.remove("on");
  if (TOPSTEP) { TOPSTEP = false; setPlayers(); }""")
sub("""    '<label class="chk sub2"><input type="checkbox" data-lay="bigOnly"'""", """    '<label class="chk sub2"><input type="checkbox" data-lay="topOnly"' + (S.topOnly ? " checked" : "") + '>Show only the bodies most responsible <span class="n" style="margin-left:auto">' + PLAY.filter((p) => p.top).length + '</span></label>' +
    '<div class="desc" style="margin:0 0 4px 22px">The largest fossil fuel producers, the banks and shareholders behind them, the trade associations that speak for the regulated industries, the bodies that run the investors\\' courts and the trade and shipping rules, and the private certifiers that stand in for enforcement, whether or not the story names them. A judgement from published rankings and this map\\'s evidence, not a ranking. Click a point for the reason.</div>' +
    '<label class="chk sub2"><input type="checkbox" data-lay="bigOnly"'""")
sub("""'<div class="hp-desc">' + p.d + '</div>';""", """'<div class="hp-desc">' + p.d + '</div>' + (p.why ? '<div class="note"><b>Counted among the bodies most responsible.</b> ' + esc(p.why) + '</div>' : '');""")

# 5. the law atlas: each country's laws and the international instruments, listed on request
sub("""  const own = c.players.map((k) => PBY[k]);""", """  h += lawBlock(c.iso, name);
  const own = c.players.map((k) => PBY[k]);""")
sub("""  $$("[data-ex]", root).forEach(""", """  $$("[data-laws]", root).forEach((a) => a.addEventListener("click", (e) => { e.preventDefault(); openLaws(a.dataset.laws, a.dataset.lawname); }));
  $$("[data-ex]", root).forEach(""")
sub("""else if (s[0] === "e") openExample(s[1], false); }""", """else if (s[0] === "e") openExample(s[1], false); else if (s[0] === "l") { const q = String(s[1]).split("|"); openLaws(q[0], q.slice(1).join("|")); } }""")
sub("""const NAVNAME = { f: "chapter", p: "organisation", c: "country", e: "record" };""", """const NAVNAME = { f: "chapter", p: "organisation", c: "country", e: "record", l: "list of laws" };""")
sub("""  $("#legBody").innerHTML = h;""", """  if (LAWS) h += '<div class="psec">The law atlas</div><div class="desc" style="margin-top:0">' + LAWS.tot[0].toLocaleString("en") + ' national laws from ' + LAWS.tot[3] + ' countries and territories, ' + LAWS.tot[1].toLocaleString("en") + ' from ' + LAWS.tot[4] + ' states and provinces, and ' + LAWS.tot[2].toLocaleString("en") + ' international and regional instruments, from FAOLEX and Climate Change Laws of the World. Click any country on the map to list its laws.</div>' +
    '<button type="button" class="btn" data-laws="' + LAWS.glob.id + '" data-lawname="International and regional instruments">List the international instruments</button> ' +
    LAWS.other.map((o) => '<button type="button" class="btn" data-laws="' + esc(o[0]) + '" data-lawname="' + esc(o[1]) + '">' + esc(o[1]) + ' · ' + o[2].toLocaleString("en") + '</button>').join(" ") +
    '<div class="desc"><a href="' + LAWS.full + '" target="_blank" rel="noopener">Open the full law atlas in its own map</a></div>';
  $("#legBody").innerHTML = h; wireCard($("#legBody"));""")
sub("""/* ---------- published figures: format, classes, legend ---------- */""", r"""/* ---------- the law atlas: lists fetched when asked for ---------- */
const LAWS = D.laws || null, LAWCACHE = {};
function lawBlock(iso, name) {
  if (!LAWS) return "";
  const n = LAWS.nat[iso], subs = LAWS.sub[iso] || [];
  let h = '<div class="hp-h">Environmental Law on Record</div>';
  if (!n) return h + '<div class="desc" style="margin-top:0">The law atlas holds no national record for this country.</div>';
  h += '<div class="note"><b>' + n.n.toLocaleString("en") + '</b> national laws, regulations and policies on the environment, natural resources, farming and food are catalogued for this country, dated ' + n.y[0] + ' to ' + n.y[1] + '. The count shows how much has been written and catalogued, not how much is applied.</div>' +
    '<div class="desc" style="margin-top:0">Largest subjects: ' + n.s.map((x) => esc(x[0]) + ' ' + x[1].toLocaleString("en")).join(" · ") + '</div>' +
    '<button type="button" class="btn" data-laws="' + esc(n.id) + '" data-lawname="' + esc(name) + '">List all ' + n.n.toLocaleString("en") + ' national laws</button>';
  if (subs.length) h += '<div class="desc">States and provinces with their own records — ' + subs.length + '</div><div class="chips">' + subs.map((x) => '<span data-laws="' + esc(x[0]) + '" data-lawname="' + esc(x[1] + ", " + name) + '">' + esc(x[1]) + ' · ' + x[2].toLocaleString("en") + '</span>').join("") + '</div>';
  return h;
}
function openLaws(id, name) {
  const sel = ["l", id + "|" + name];
  const draw = (rows) => {
    let q = "", shown = 200;
    const body = () => {
      const m = q ? rows.filter((r) => (r.name + " " + r.year + " " + r.type + " " + r.sector + " " + (r.sub || "")).toLowerCase().includes(q)) : rows;
      return '<div class="desc" style="margin-top:4px">' + m.length.toLocaleString("en") + (q ? ' of ' + rows.length.toLocaleString("en") : '') + ' entries, newest first.</div>' +
        m.slice(0, shown).map((r) => '<div class="rec"><div class="rh" style="cursor:default"><b><a href="' + esc(r.url) + '" target="_blank" rel="noopener" style="color:inherit">' + esc(r.name) + '</a></b><span class="n">' + esc(r.year || "") + '</span></div>' +
          '<div class="desc" style="margin:0 0 0 0">' + esc([r.type, r.sector, r.sub].filter(Boolean).join(" · ")) + ' · ' + (r.source === "cclw" ? "Climate Change Laws of the World" : "FAOLEX") + '</div></div>').join("") +
        (m.length > shown ? '<button type="button" class="btn" id="lawMore" style="margin-top:8px">Show ' + Math.min(200, m.length - shown) + ' more</button>' : '');
    };
    show('<div class="hp"><div class="hp-k">The law atlas</div><h3>' + esc(name) + '</h3>' +
      '<div class="hp-sub">Every entry the atlas holds for this jurisdiction. Each title links to its record at the source.</div>' +
      '<input class="inp" id="lawFind" type="search" placeholder="Filter by word, year, type or subject" style="width:100%" autocomplete="off"><div id="lawList">' + body() + '</div>' +
      '<div class="hp-src">FAOLEX, Food and Agriculture Organization of the United Nations; Climate Change Laws of the World, Grantham Research Institute and Climate Policy Radar (CC BY). Compiled in the <a href="' + LAWS.full + '" target="_blank" rel="noopener">Environmental Law Atlas</a>.</div></div>', sel);
    const redraw = () => { $("#lawList").innerHTML = body(); const b = $("#lawMore"); if (b) b.addEventListener("click", () => { shown += 200; redraw(); }); };
    $("#lawFind").addEventListener("input", (e) => { q = e.target.value.trim().toLowerCase(); shown = 200; redraw(); });
    redraw();
  };
  if (LAWCACHE[id]) { draw(LAWCACHE[id]); return; }
  show('<div class="hp"><div class="hp-k">The law atlas</div><h3>' + esc(name) + '</h3><div class="desc">Loading the list…</div></div>', sel);
  fetch(LAWS.base + encodeURIComponent(id) + ".json").then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then((rows) => { LAWCACHE[id] = rows; if (S.sel && S.sel[0] === "l" && S.sel[1] === sel[1]) draw(rows); })
    .catch(() => { if (S.sel && S.sel[0] === "l" && S.sel[1] === sel[1]) $("#detBody").innerHTML = '<div class="hp"><div class="hp-k">The law atlas</div><h3>' + esc(name) + '</h3><div class="desc">The list could not be loaded. It is kept online with the law atlas and needs a connection.</div></div>'; });
}

/* ---------- published figures: format, classes, legend ---------- */""")
