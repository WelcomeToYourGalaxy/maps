
  /* ================= adapter: the rows above, drawn on this map ================= */
  const GEO = new Map();
  function fillGEO() { if (GEO.size || !BOUNDS) return; for (const f of BOUNDS.features) { const p = f.properties; if (p.iso3 && p.iso3 !== "-99") GEO.set(p.iso3, p.name); } }
  const NAMEOF = Object.assign({ CSK: "Czechoslovakia", YUG: "Yugoslavia" }, D.imfc.names, Object.fromEntries(D.wbp.rows.filter((r) => r[0]).map((r) => [r[0], r[1]])));
  const ISONAME = (c) => GEO.get(c) || NAMEOF[c] || c;
__WBCA__
  const MINY = 1947, MAXY = 2030;
  const SECS = { Pat: "Who wins the contracts", All: "Every lender together", IMF: "International Monetary Fund", "World Bank": "World Bank", IDB: "Regional development banks", EU: "European Union and euro area", Gov: "Single governments: China, the Paris Club, Saudi Arabia and Qatar", OECD: "Every lender reporting to the OECD", Flows: "Other money flowing in and out" };
  const ORDER = ["All", "IMF", "World Bank", "IDB", "EU", "Gov", "OECD", "Flows", "Pat"];
  LAYERS.sort((a, b) => ORDER.indexOf(a.lender) - ORDER.indexOf(b.lender));
  const OPTS = {}; for (const l of LAYERS) OPTS[l.id] = { measure: undefined, off: new Set(), _init: false };
  const byId = (id) => LAYERS.find((l) => l.id === id);
  const active = () => (S.layer && S.layer.startsWith("lc:") ? byId(S.layer.slice(3)) : null);
  const rangeOf = (l) => { const a = S.all ? l.span[0] : Math.max(S.y0 || MINY, MINY), b = S.all ? l.span[1] : Math.min(S.y1, MAXY); return [a, b]; };
  let CUR = { id: null, values: new Map(), unplaced: new Map(), noTotal: false, breaks: [] };

  function compute() {
    const l = active(); if (!l) return null; fillGEO();
    const o = OPTS[l.id], [a, b] = rangeOf(l);
    const r = l.values(a, b, o);
    CUR = { id: l.id, values: r.values, unplaced: r.unplaced || new Map(), noTotal: r.noTotal, a, b };
    return CUR;
  }
  const fmtOf = (l, v) => { const o = OPTS[l.id]; return l.fmt ? l.fmt(v, o) : o.measure === "agreed" ? sdr(v) : o.measure === "amt" ? usd(v) : num(v); };
  const NEG = "rgba(150,150,150,.32)";
  function draw() {
    const l = active(); if (!l) return false;
    const r = compute(), vals = [...r.values.entries()].filter(([c, v]) => v != null && GEO.has(c));
    const pos = vals.filter(([, v]) => v > 0).map(([, v]) => v);
    BREAKS = computeBreaks(pos);
    const expr = ["match", ["get", "iso3"]];
    vals.forEach(([c, v]) => expr.push(c, v > 0 ? RAMP[binOf(v)] : NEG));
    expr.push("rgba(0,0,0,0)");
    if (vals.length) {
      map.setFilter("cty-fill", null);
      map.setPaintProperty("cty-fill", "fill-color", expr);
      map.setPaintProperty("cty-fill", "fill-opacity", 0.62);
      map.setLayoutProperty("cty-fill", "visibility", "visible");
    } else map.setLayoutProperty("cty-fill", "visibility", "none");
    drawLines();
    legend(l, pos.length);
    return true;
  }
  function legend(l, n) {
    const el = $("#lyLeg"); if (!el) return;
    const f = (v) => fmtOf(l, v);
    const labs = [];
    for (let i = 0; i <= BREAKS.length; i++) labs.push(i === 0 ? "under " + f(BREAKS[0]) : i === BREAKS.length ? f(BREAKS[i - 1]) + "+" : f(BREAKS[i - 1]) + "–" + f(BREAKS[i]));
    const o = OPTS[l.id];
    const total = [...CUR.values.values()].reduce((s, v) => s + (v || 0), 0) + [...CUR.unplaced.values()].reduce((s, v) => s + (v || 0), 0);
    const outside = CUR.b < l.span[0] || CUR.a > l.span[1];
    el.innerHTML = '<div class="sub" style="margin-top:0">' + (outside ? 'This layer covers ' + l.span[0] + '–' + l.span[1] + '; move the years in the key into that range, or tick "Every year".' : (S.all ? "Every year this source covers, " : "") + CUR.a + "–" + CUR.b + (CUR.noTotal ? "" : ": " + esc(l.unit(total, o)) + " in all") + ".") + '</div>' +
      (BREAKS.length || n ? '<div class="ramp">' + RAMP.slice(0, BREAKS.length + 1).map((c) => '<span style="background:' + c + '"></span>').join("") + '</div><div class="rampl">' + labs.map((t) => '<span>' + esc(t) + '</span>').join("") + '</div>' : "") +
      '<div class="sub">' + n + ' countries above zero.' + ([...CUR.values.values()].some((v) => v != null && v <= 0) ? ' <i style="display:inline-block;width:9px;height:9px;background:' + NEG + ';vertical-align:-1px"></i> zero or less.' : "") + ' Click a country for its record in this layer.</div>' +
      (CUR.unplaced.size ? '<details class="unpl"><summary>Counted but with no shape on the map (' + CUR.unplaced.size + ')</summary><div style="margin:3px 0">These figures belong to places this map has no outline for: regional programmes, groups of countries, or small territories. They are in the total above but cannot be coloured.</div>' + [...CUR.unplaced.entries()].map(([k, v]) => esc(k) + ' (' + esc(f(v)) + ')').join("; ") + '.</details>' : "");
  }
  function hover(iso) {
    const l = active(); if (!l) return null;
    const v = CUR.values.get(iso);
    return esc(l.short || l.title) + ", " + CUR.a + "–" + CUR.b + ": " + (v == null ? "no record" : esc(l.unit(v, OPTS[l.id])));
  }
  function section(iso) {
    const l = active(); if (!l) return "";
    const v = CUR.values.get(iso);
    const body = v == null ? '<div class="note">This source has no record for this country in these years.</div>' : l.popup(iso, CUR.a, CUR.b, OPTS[l.id]);
    return '<div class="lcx"><div class="hp-h">' + esc(l.title) + ' · ' + CUR.a + '–' + CUR.b + '</div>' + body + '</div>';
  }
  const has = (iso) => { const l = active(); return !!(l && CUR.values.has(iso)); };

  // One layer's row, placed under its lender in the left box; the chosen one shows its controls and colours.
  const STRIP = /^(IMF|World Bank|China|Inter-American Development Bank|EU and euro area): /;
  function row(id) {
    const l = byId(id); if (!l) return "";
    const cur = active() === l, t = l.title.replace(STRIP, ""), title = t.charAt(0).toUpperCase() + t.slice(1);
    return '<label><input type="radio" name="layer" value="lc:' + l.id + '"' + (cur ? " checked" : "") + '><span>' + esc(title) + ' <span class="n">' + l.span[0] + '–' + l.span[1] + '</span>' + qm(l.plain || String(l.about || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim().split(/(?<=\.)\s/).slice(0, 2).join(" ")) + '</span></label>' +
      (cur ? '<div class="row lcrow" data-id="' + l.id + '">' + (l.plain ? '<div class="sub">' + esc(l.plain) + '</div>' : "") + l.controls() + legendSlot() + '<details class="lcfine"><summary>Sources and fine print</summary>' + l.about + '</details></div>' : "");
  }
  function wireTr() {
    const row = document.querySelector("#layersBody .lcrow"); if (!row) return;
    const l = byId(row.dataset.id), o = OPTS[l.id];
    row.querySelectorAll("select[data-k]").forEach((s) => { if (!o._init || o[s.dataset.k] == null) o[s.dataset.k] = s.value; else s.value = o[s.dataset.k]; });
    row.querySelectorAll("[data-checks] input").forEach((i) => { i.checked = !o.off.has(i.dataset.v); });
    o._init = true;
    row.addEventListener("change", (e) => {
      if (e.target.matches("select[data-k]")) o[e.target.dataset.k] = e.target.value;
      else if (e.target.matches("[data-checks] input")) e.target.checked ? o.off.delete(e.target.dataset.v) : o.off.add(e.target.dataset.v);
      drawCountries(); if (S.sel && S.sel.t === "country") detailCountry(S.sel.iso);
    });
  }

  // Lines (the contracts layer).
  map.addSource("lc-lines", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
  map.addLayer({ id: "lc-line", type: "line", source: "lc-lines", layout: { "line-cap": "round" }, paint: { "line-color": "#e7e5df", "line-width": ["get", "w"], "line-opacity": 0.75 } });
  IDS.push("lc-line");
  map.on("mousemove", "lc-line", (e) => { const f = e.features[0]; if (f && f.properties.label) tip(esc(f.properties.label), e.originalEvent.clientX, e.originalEvent.clientY); });
  map.on("mouseleave", "lc-line", () => tip(null));
  function drawLines() {
    const src = map.getSource("lc-lines"); if (!src) return;
    const l = active(), sel = S.sel && S.sel.t === "country" ? S.sel.iso : null;
    const L = l && l.lines ? l.lines(CUR.a, CUR.b, OPTS[l.id], sel) : [];
    const max = Math.max(1, ...L.map((x) => x.w || 1));
    src.setData({ type: "FeatureCollection", features: L.filter((x) => x.a && x.b).map((x) => ({ type: "Feature", geometry: { type: "LineString", coordinates: arc(x.a, x.b) }, properties: { label: x.label || "", w: 0.5 + 2.2 * Math.sqrt((x.w || 1) / max) } })) });
  }

  // Places: World Bank and Chinese project sites, every protest, services taken back into public hands.
  const PTN = { wb: ["World Bank project sites, 1995–2014", "Where World Bank loans and grants were spent: towns, districts, roads, dams and so on, as AidData and the World Bank mapped them, for every project approved in 1995–2014. Click a dot for the project."], cn: ["Chinese state-financed project sites, 2000–2021", "Where loans and grants from Chinese state banks and agencies were spent, as AidData traced them on OpenStreetMap: ports, railways, power plants, hospitals and more. Click a dot for the project."], mm: ["Protests against governments, 1990–2020", "Every protest of 50 or more people against a government that the Mass Mobilization Project coded from newspapers, with what protesters demanded and how the state responded. It covers all protests, not only those over loan conditions; the menu narrows it. Each mark sits on the town the record names; protests with no town named sit on the capital. Loads the first time it is turned on. Click a mark for the record."], pf: ["Services taken back into public hands, 2000 on", "Water, power, transport, waste, health and other services that towns, regions or countries took back from private companies, or newly set up as public services, from the Public Futures database (University of Glasgow and the Transnational Institute). Marks are placed from the place name and are approximate. Shown by default: those taken back from a named company in a country where the IMF made selling state firms a loan condition, or from a company that appears in a case here. The menu can show every record instead."] };
  const FOPT = { mm: [["all", "Every protest"], ["price", "Over price rises and taxes"], ["wage", "Over wages and jobs"], ["land", "Over land and farms"], ["imf", "Where its record mentions the IMF or World Bank"], ["kill", "Met with shootings or killings"]], pf: [["rel", "Where the IMF required privatization, or from a company in a case here"], ["priv", "Taken back from a named company, anywhere"], ["all", "Every record"]] };
  S.lcf = S.lcf || { mm: "all", pf: "rel" };
  const MMBIT = { price: 1, wage: 2, land: 4, imf: 8, kill: 16 };
  const ECON = new Set(["price increases, tax policy", "labor wage dispute", "land farm issue"]);
  const underLoan = (iso, y) => { const c = CD[iso]; if (!c) return 0; return (c.m && c.m[y] > 0) || (c.w && ((c.w[y] && c.w[y][2] > 0) || (c.w[y - 1] && c.w[y - 1][2] > 0))) ? 1 : 0; };
  const PTC = { atlas: { wb: "#3E5C76", cn: "#83394A", pf: "#5A4466", mm: "#1F3B4D", edge: "#F2EAD8" }, night: { wb: "#7FB8B4", cn: "#B39BC9", pf: "#9DC0A8", mm: "#C2B2DA", edge: "#05080C" }, hell: { wb: "#D7CEC3", cn: "#9FB2C2", pf: "#A9BBA2", mm: "#C9B9D9", edge: "#1A0606" }, land: { wb: "#9DB4C8", cn: "#C28F9C", pf: "#93B39C", mm: "#B9A7D3", edge: "#0B0F14" } };
  const ptCol = () => PTC[BASEK === "atlas" ? "atlas" : BASEK === "hell" ? "hell" : BASEK === "night" || BASEK === "satellite" ? "night" : "land"];
  S.lcpt = S.lcpt || { wb: false, cn: false, mm: false, pf: false };
  const WP = D.wbsites.projects;
  const CNR = Object.fromEntries(D.cnsites.rows.map((r) => [String(r[2]), r]));
  const PREC = { 1: "exact spot", 2: "within about 25 km", 3: "district", 4: "province or state", 5: "near a province", 6: "whole country", 7: "estimated", 8: "whole country (country-wide project)" };
  const fc = (features) => ({ type: "FeatureCollection", features });
  map.addSource("lcpt-wb", { type: "geojson", data: fc(D.wbsites.points.map(([x, y, id, pc, place]) => ({ type: "Feature", geometry: { type: "Point", coordinates: [x, y] }, properties: { id, pc, place, y: (WP[id] || [])[5] ?? -1 } }))) });
  map.addSource("lcpt-cn", { type: "geojson", data: fc(D.cnsites.rows.map((r) => ({ type: "Feature", geometry: { type: "Point", coordinates: [r[0], r[1]] }, properties: { i: String(r[2]), y: r[5] ?? -1, exact: /^precise(,precise)*$/.test(r[10] || "") ? 1 : 0 } }))) });
  map.addSource("lcpt-pf", { type: "geojson", data: fc(D.pf.rows.map((r, i) => ({ type: "Feature", geometry: { type: "Point", coordinates: [r[0], r[1]] }, properties: { i, y: r[4] ?? r[5] ?? -1, rel: r[21] || 0, pv: r[22] || 0 } }))) });
  map.addSource("lcpt-mm", { type: "geojson", data: fc([]) });
  const PTK = ["wb", "cn", "mm", "pf"];
  const RAD = { wb: [1, 1.1, 4, 2.6, 8, 5.5], cn: [1, 1.1, 4, 2.6, 8, 5.5], mm: [1, 1.5, 4, 2.8, 8, 5.5], pf: [1, 1.8, 4, 3.2, 8, 6] };
  for (const k of PTK) {
    const r = RAD[k];
    map.addLayer({ id: "lcpt-" + k, type: "circle", source: "lcpt-" + k, layout: { visibility: "none" }, paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], r[0], r[1], r[2], r[3], r[4], r[5]], "circle-stroke-width": 0.5, "circle-opacity": 0.85, "circle-stroke-opacity": 0.7, "circle-pitch-alignment": "map" } });
    IDS.push("lcpt-" + k);
    map.on("mouseenter", "lcpt-" + k, () => (map.getCanvas().style.cursor = "pointer"));
    map.on("mouseleave", "lcpt-" + k, () => (map.getCanvas().style.cursor = ""));
  }
  let mmState = 0;
  async function loadMM() {
    if (mmState) return; mmState = 1;
    const n = $("#lcn-mm"); if (n) n.textContent = "loading…";
    try {
      const res = await fetch(D.mm_meta.file); if (!res.ok) throw new Error(res.status);
      D.mm = JSON.parse(await new Response(res.body.pipeThrough(new DecompressionStream("gzip"))).text());
      map.getSource("lcpt-mm").setData(fc(D.mm.rows.map((r, i) => ({ type: "Feature", geometry: { type: "Point", coordinates: [r[0], r[1]] }, properties: { i, y: r[4] ?? -1, f: ((r[12] || []).some((d) => /price increases/.test(d)) ? 1 : 0) | ((r[12] || []).some((d) => /labor wage/.test(d)) ? 2 : 0) | ((r[12] || []).some((d) => /land farm/.test(d)) ? 4 : 0) | (r[17] ? 8 : 0) | ((r[13] || []).some((x) => /shootings|killings/.test(x)) ? 16 : 0) } }))));
      mmState = 2; drawPts(); const m = $("#lcn-mm"); if (m) m.textContent = num(D.mm.rows.length);
    } catch (err) { mmState = 0; const m = $("#lcn-mm"); if (m) m.textContent = "could not load"; }
  }
  function drawPts() {
    if (!map.getLayer("lcpt-wb")) return;
    const c = ptCol(), story = !!(S.pat || S.ent);
    const yr = S.all ? null : ["any", ["==", ["get", "y"], -1], ["all", [">=", ["get", "y"], S.y0], ["<=", ["get", "y"], S.y1]]];
    for (const k of PTK) {
      const id = "lcpt-" + k;
      map.setLayoutProperty(id, "visibility", S.lcpt[k] && !story ? "visible" : "none");
      map.setPaintProperty(id, "circle-color", c[k]); map.setPaintProperty(id, "circle-stroke-color", c.edge);
      const m = S.lcf[k], mf = k === "mm" ? (MMBIT[m] ? [">", ["%", ["floor", ["/", ["get", "f"], MMBIT[m]]], 2], 0] : null) : (k === "wb" || k === "cn") && S.lcex ? (k === "wb" ? ["==", ["get", "pc"], 1] : ["==", ["get", "exact"], 1]) : k === "pf" ? (m === "rel" ? ["==", ["get", "rel"], 1] : m === "priv" ? ["==", ["get", "pv"], 1] : null) : null;
      const fl = [yr, mf].filter(Boolean);
      map.setFilter(id, fl.length === 2 ? ["all", fl[0], fl[1]] : fl[0] || null);
      const d = $("#lcd-" + k); if (d) d.style.background = c[k];
    }
  }
  function ptRow(k) {
    const c = ptCol();
    return '<label class="chk"><input type="checkbox" data-lcpt="' + k + '"' + (S.lcpt[k] ? " checked" : "") + '> <i id="lcd-' + k + '" style="display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:3px;background:' + c[k] + '"></i>' + esc(PTN[k][0]) + ' <span class="n" id="lcn-' + k + '">' + num(k === "wb" ? D.wbsites.points.length : k === "cn" ? D.cnsites.rows.length : k === "pf" ? D.pf.rows.length : D.mm_meta.n) + '</span>' + qm(PTN[k][1]) + '</label>' +
      (FOPT[k] ? '<div style="margin:0 0 4px 22px"><select data-lcf="' + k + '">' + FOPT[k].map(([v, t]) => '<option value="' + v + '"' + (S.lcf[k] === v ? " selected" : "") + '>' + esc(t) + '</option>').join("") + '</select></div>' : "");
  }
  function exactRow() {
    return '<label class="chk" style="margin-left:22px"><input type="checkbox" data-lcex' + (S.lcex ? " checked" : "") + '> Only places pinned to an exact spot' + qm("World Bank sites the mappers placed at the exact location, and Chinese-financed sites traced to a precise spot on OpenStreetMap. Without this, sites placed only at a district, a province or the whole country are shown too, at the middle of that area.") + '</label>';
  }
  function wirePts() {
    document.querySelectorAll("#key [data-lcex]").forEach((i) => i.addEventListener("change", () => { S.lcex = i.checked; drawPts(); }));
    document.querySelectorAll("#key [data-lcpt]").forEach((i) => i.addEventListener("change", () => { const k = i.dataset.lcpt; S.lcpt[k] = i.checked; if (i.checked && typeof leaveStory === "function") leaveStory(); if (k === "mm" && i.checked) loadMM(); drawPts(); syncSw(); }));
    document.querySelectorAll("#key [data-lcf]").forEach((x) => x.addEventListener("change", () => { S.lcf[x.dataset.lcf] = x.value; drawPts(); }));
  }
  function ptHits(pt) {
    const ids = PTK.map((k) => "lcpt-" + k).filter((id) => map.getLayer(id) && map.getLayoutProperty(id, "visibility") !== "none");
    if (!ids.length) return [];
    return map.queryRenderedFeatures([[pt.x - 5, pt.y - 5], [pt.x + 5, pt.y + 5]], { layers: ids }).map((f) => ({ t: "lcp", k: f.layer.id.slice(5), p: f.properties, xy: f.geometry.coordinates }));
  }
  function ptLabel(e) {
    const P = e.p;
    if (e.k === "wb") return [((WP[P.id] || [])[0]) || P.place, "World Bank project site · " + (P.place || "")];
    if (e.k === "cn") { const r = CNR[String(P.i)] || []; return [r[6] || r[4] || "", "Chinese state-financed site · " + (r[5] || "")]; }
    if (e.k === "pf") { const r = D.pf.rows[P.i]; return [r[3] + (r[7] ? ": " + r[7] : ""), "Service taken back into public hands · " + (r[5] || r[4] || "")]; }
    if (e.k === "mm" && D.mm) { const r = D.mm.rows[P.i]; return [(r[7] || r[3]) + ", " + r[3], "Protest against a government · " + (r[5] || r[4])]; }
    return ["", ""];
  }
  const yrsOf = (c) => (c.start == null ? "" : c.start + (c.end == null ? " to now" : c.end !== c.start ? "–" + c.end : ""));
  const para = (t) => (t ? `<p class="cs">${esc(t)}</p>` : "");
  function pfCard(r) {
    const [x, y, cc, place, yImp, yDec, kind, svc, prev, cur, own, actors, actions, gov, org, motiv, approx, id, pop, summary, outc] = r;
    const row = (t, v) => (v ? `<tr><td>${t}</td><td>${esc(v)}</td></tr>` : "");
    return `<div class="hp-k">Service taken back into public hands</div><h3>${esc(place)}</h3><div class="src">Public Futures case ${esc(id)}${approx === 2 ? " · no matching place found, so placed at the middle of the country" : approx ? " · placed from the place name, approximate" : ""}</div>` +
      `<table>${row("What happened", kind)}${row("Service", svc)}${row("Run before by", prev)}${row("Run now by", cur)}${row("Year decided", yDec)}${row("Year carried out", yImp)}${row("Ownership now", own)}${row("Who pushed for it", actors)}${row("How", actions)}${row("Why", motiv)}${row("Results reported", outc)}${row("How it is run", gov)}${row("Kind of public body", org)}${row("People served", pop ? num(pop) : "")}</table>` +
      (summary ? para(summary) : "") + `<div class="note">Source: Public Futures database, University of Glasgow and the Transnational Institute, <a href="https://publicfutures.org/" target="_blank" rel="noopener">publicfutures.org</a>.</div>`;
  }
  const MMPC = { 1: "placed at the town or city the record names", 2: "the record names a region; shown at its largest town", 3: "no town named or matched; shown at the capital" };
  function mmCard(r) {
    const [x, y, iso, country, year, start, end, loc, pc, at, parts, who, dem, res, viol, notes, srcs, imf, id] = r;
    const row = (t, v) => (v ? `<tr><td>${t}</td><td>${esc(v)}</td></tr>` : "");
    return `<div class="hp-k">Protest against a government</div><h3>${esc(loc || country)}</h3><div class="src">${esc(country)} · ${esc(start || year)}${end && end !== start ? " to " + esc(end) : ""} · ${esc(MMPC[pc])}${pc !== 1 ? " (" + esc(at) + ")" : ""}</div>` +
      `<table>${row("Protesters", who)}${row("How many", parts)}${row("Demands", dem.join("; "))}${row("State response", res.join("; "))}${row("Protesters used violence", viol === 1 ? "yes" : viol === 0 ? "no" : "")}</table>` +
      (notes ? para(notes) : "") + (srcs ? `<div class="note">Newspaper sources the coders used: ${esc(srcs)}</div>` : "") +
      `<div class="note">Source: Mass Mobilization Project (Clark and Regan), record ${esc(id)}, <a href="https://doi.org/10.7910/DVN/HTTWYL" target="_blank" rel="noopener">Harvard Dataverse</a>.</div>`;
  }
  function ptCard(e) {
    const P = e.p, k = e.k;
    if (k === "wb") { const p = WP[P.id] || []; return `<div class="hp-k">World Bank project site</div><h3>${esc(P.place)}</h3><div class="src">${esc(PREC[P.pc] || "")}</div><div class="item"><a href="https://projects.worldbank.org/en/projects-operations/project-detail/${esc(P.id)}" target="_blank" rel="noopener">${esc(p[0])}</a><br><span class="m">${esc(P.id)} · ${esc(p[4])} · started ${p[5] || "–"} · ${esc(p[3])}</span><br>${usd(p[2])} committed to the whole project<br><span class="m">${esc(p[1])}</span></div><div class="note">Source: AidData and the World Bank, geocoded research release 1.4.2 (projects approved 1995–2014).</div>`; }
    if (k === "cn") { const r = CNR[String(P.i)] || []; return `<div class="hp-k">Chinese state-financed project site</div><h3>${esc(r[4])}</h3><div class="item">${esc(r[6])}<br><span class="m">${r[5] || "–"} · ${esc(r[8])} · ${esc(r[9])} · ${r[7] != null ? usd(r[7]) + " (2021 dollars)" : "amount not given"}</span><br><span class="m">Located: ${esc(r[10])}${r[11] ? ` · <a href="${esc(String(r[11]).split("|")[0])}" target="_blank" rel="noopener">on OpenStreetMap</a>` : ""} · AidData id ${esc(r[2])}</span></div><div class="note">Source: AidData, Geospatial Global Chinese Development Finance Dataset 3.0.</div>`; }
    if (k === "pf") return pfCard(D.pf.rows[P.i]);
    if (k === "mm") return D.mm ? mmCard(D.mm.rows[P.i]) : "";
    return "";
  }

  return { ready: true, exactRow, loadMM, active, draw, hover, section, has, row, wireTr, ptRow, wirePts, drawPts, ptHits, ptLabel, ptCard, drawLines, name: (iso) => { fillGEO(); return ISONAME(iso); }, layers: LAYERS };
