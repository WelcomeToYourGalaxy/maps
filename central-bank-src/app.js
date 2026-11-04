(function () {
"use strict";
if (typeof navigator !== "undefined" && navigator.userAgent === "node") return;
const $ = (s) => document.querySelector(s);
const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const fmt = (n, d) => n == null ? "" : Number(n).toLocaleString("en-US", { maximumFractionDigits: d == null ? 2 : d, minimumFractionDigits: 0 });
const P = D.P, U = D.U, CUR = D.CUR;
const ISOS = Object.keys(P).sort((a, b) => P[a].n.localeCompare(P[b].n));

/* ---------- colors ---------- */
// Each basemap: [accent, accent-hi, page], and a five-step ramp from that basemap's own tones (low = dark, high = light).
const UI = { night: ["#5600DC", "#a99cff", "#06071a"], satellite: ["#3f6e69", "#9fc9c1", "#0b1017"], atlas: ["#4b6075", "#b9c8d8", "#0b1017"], hell: ["#82303a", "#e0a3a5", "#1e080b"], outlines: ["#38586b", "#a9c2d6", "#0b1017"] };
const RAMPS = {
  night:     ["#2b2452", "#45398a", "#6d5fbb", "#a195e0", "#ddd6fa"],
  outlines:  ["#20364a", "#31546f", "#4d7a9c", "#86aac8", "#cddfee"],
  satellite: ["#1d3836", "#2c5753", "#477d77", "#7fafa7", "#c6e2dc"],
  atlas:     ["#23304a", "#384c6f", "#587198", "#8fa6c6", "#d2ddec"],
  hell:      ["#3a1519", "#5c2229", "#883a43", "#ba6f76", "#ecc3c5"],
};
// Four category colors, checked for color-blind separation as a set; anything past four folds into grey.
const CATC = ["#3a6db8", "#c97585", "#a9cfe6", "#4f8f5a"];
const OTHER = "#8b8996", NODATA = "#3d3e4a";
let BASE = "night";
const ramp = () => RAMPS[BASE] || RAMPS.night;
const hex = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
function mix(a, b, t) { const A = hex(a), B = hex(b); return "#" + A.map((x, i) => Math.round(x + (B[i] - x) * t).toString(16).padStart(2, "0")).join(""); }
function seqColor(t) { const r = ramp(); t = Math.max(0, Math.min(1, t)); const x = t * (r.length - 1), i = Math.min(r.length - 2, Math.floor(x)); return mix(r[i], r[i + 1], x - i); }

/* ---------- reading values ---------- */
const uni = (p) => p.u ? U[p.u] : null;
const atYear = (s, y) => (s && y >= s[0] && y < s[0] + s.length - 1) ? s[y - s[0] + 1] : null;
function own(p, k) { if (p[k] != null) return { o: p[k], via: null }; const u = uni(p); if (u && u[k] != null) return { o: u[k], via: p.u }; return null; }
Object.keys(P).forEach((k) => { P[k].iso = k; });
const curOf = (p) => (p.rc && CUR[p.rc]) ? CUR[p.rc] : null;
const CB_NAMES = { ECB: "the European Central Bank", BCEAO: "the BCEAO", BEAC: "the BEAC", ECCB: "the Eastern Caribbean Central Bank" };

const DIM6 = ["Governor and board", "Policy and conflicts", "Objectives", "Lending to government", "Financial independence", "Reporting and disclosure"];
const DIM4 = ["Governor", "Objectives", "Policy making", "Lending to government"];
const DIM5 = ["Political", "Economic", "Procedural", "Policy", "Operational"];
const COARSE = { 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 3, 13: 4, 14: 5, 15: 6 };

// The layers the key offers.
const L = [];
const REL = [["own", "Owns shares or sits in its governance"], ["corrupt", "Paid, bribed, or got money, favors or leaks from it"], ["people", "Shares its people: revolving door, board seats, forum members"], ["inst", "Belongs to the same institutions: BIS, Financial Stability Board"], ["control", "Pressured, fired, prosecuted or froze its money"], ["service", "Other ties: named in a case, prints its money, audits or manages funds"], ["account", "Investigated, charged or tried its officials"]];
const RELC = (r) => ({ own: CATC[0], corrupt: CATC[1], people: CATC[2], inst: CATC[2], control: CATC[3], account: "#c9c6d6" })[r] || OTHER;
const RELDASH = { inst: "dot", account: "dash" };
const RELMEAN = {
  own: "Holds shares in the central bank. Shareholders receive its dividends and, where its law allows, vote at its shareholder meetings or elect directors.",
  corrupt: "Named in a documented corruption case with the bank: money, contracts, favors or confidential decisions passed between it and the bank's officials.",
  people: "People pass between it and the bank, or sit with the bank's officials in it, carrying contacts and loyalties both ways.",
  inst: "The bank is a member: its officials meet there and agree common rules with other central banks, outside any national parliament.",
  control: "Used power over the bank: pressure, firing or prosecution of its leaders, freezing or seizing its money, or a foreign guarantee of its currency.",
  service: "Works for the bank (printing its money, auditing it, managing its funds) or is named in one of its cases.",
  account: "Investigated, charged or tried the bank's officials: a check on the bank, not influence over it." };
const USA_OWN = " At the Federal Reserve, member banks that hold a Reserve Bank's shares elect six of its nine directors (Class A and B); since 2010 the bankers' three Class A directors no longer vote on choosing its president.";

function seq(id, group, label, o) { L.push(Object.assign({ id, group, label, kind: "seq" }, o)); }
function cat(id, group, label, o) { L.push(Object.assign({ id, group, label, kind: "cat" }, o)); }

const latestOr = (p, k, sk, y, pick) => { const r = own(p, k); if (!r) return null; if (S.latest || !sk) return { v: pick(r.o), via: r.via, y: r.o.y }; const s = own(p, sk); const v = s ? atYear(s.o, y) : null; return v == null ? null : { v, via: s.via, y }; };

// The three summary layers. Each measure runs 0 (shielded) to 1 (exposed). Counts are divided by the highest count anywhere.
// "other" event records (appointments, court rulings) are shown in the box but not counted as moves against the bank
const evN = (p) => (p.ev || []).filter((i) => D.EV[i].kind !== "other").length;
const MAXEV = Math.max(1, ...Object.values(P).map(evN));
const ccN = (p) => (p.cc || []).filter((i) => D.CC[i].status !== "acquitted").length;
const MAXCC = Math.max(1, ...Object.values(P).map(ccN));
const rdN = (p) => (p.rd || []).length;
const MAXRD = Math.max(1, ...Object.values(P).map(rdN));
const avg = (a) => a.reduce((x, y) => x + y, 0) / a.length;
const via = (r) => r.via ? " (" + CB_NAMES[r.via] + ")" : "";
// OUTSIDE: governments and foreign powers steering the bank
function outsideParts(p) {
  const out = [], r = own(p, "r"), g = own(p, "g"), pr = own(p, "p");
  if (r) out.push(["Law lets the government steer it", 1 - r.o.i, "1 − Romelli index " + fmt(r.o.i, 3) + via(r)]);
  else if (g) out.push(["Law lets the government steer it", 1 - g.o.w, "1 − Garriga index " + fmt(g.o.w, 3)]);
  if (pr && pr.o.q) out.push(["Government pressure, 2010–18", pr.o.n / pr.o.q, pr.o.n + " of " + pr.o.q + " quarters"]);
  if (!out.length) return out;
  const n = evN(p); out.push(["Moves against it, 2019–26", n / MAXEV, n + " (most anywhere: " + MAXEV + ")"]);
  const ext = p.arrk === "guarantee" || p.arrk === "foreign" || p.arrk === "board";
  out.push(["Money issued, backed or fixed from abroad", ext ? 1 : 0, ext ? ({ guarantee: "foreign treasury guarantee", foreign: "uses another country's currency", board: "currency board" })[p.arrk] : "no"]);
  return out;
}
// INSIDE: the people and owners inside the bank, and the cover its secrecy gives them
function insideParts(p) {
  const out = [], t = own(p, "t"), n = ccN(p), m = rdN(p);
  if (!t && !n && !m && !p.own) return out;
  out.push(["Corruption cases inside the bank since 1990", n / MAXCC, n + " (most anywhere: " + MAXCC + ")"]);
  out.push(["Officials moving to or from private finance", m / MAXRD, m + " documented (most anywhere: " + MAXRD + ")"]);
  out.push(["Private shareholders inside its governance", p.own ? 1 : 0, p.own ? "yes" : "none found"]);
  if (t) out.push(["Bank keeps the public uninformed", 1 - t.o.ti / 15, "1 − transparency " + fmt(t.o.ti, 1) + "/15" + via(t)]);
  return out;
}
// AROUND: the corruption and secrecy of the country and banking system it sits in
function aroundParts(p) {
  const out = [], cv = [];
  if (p.cpi) cv.push(p.cpi.v); if (p.wgi) cv.push(p.wgi.v);
  if (cv.length) out.push(["Corruption in the country", 1 - avg(cv) / 100, [p.cpi ? "CPI " + fmt(p.cpi.v, 0) : "", p.wgi ? "World Bank " + fmt(p.wgi.v, 0) : ""].filter(Boolean).join(", ") + " (of 100)"]);
  if (p.aml) out.push(["Money-laundering risk in its banks", p.aml.v / 10, "Basel AML " + fmt(p.aml.v, 2) + "/10"]);
  if (p.fsi) out.push(["Country's laws hide who owns money", p.fsi.score / 100, "secrecy score " + fmt(p.fsi.score, 1) + "/100"]);
  return out;
}
const sc = (ps) => ps.length ? { v: 100 * avg(ps.map((x) => x[1])), n: ps.length } : null;
function parts(p) { return outsideParts(p); }
function compScore(p) { return sc(outsideParts(p)); }
function inScore(p) { return sc(insideParts(p)); }
function groups(p) { return [["Outside influence", outsideParts(p)], ["Inside influence", insideParts(p)], ["Corruption and secrecy around it", aroundParts(p)]].filter((x) => x[1].length); }
function allScore(p) { const G = groups(p); if (G.length < 2) return null; return { v: 100 * avg(G.map((x) => avg(x[1].map((y) => y[1])))), n: G.length }; }
seq("none", "Plain", "No country colors", { dom: [0, 1], f: (v) => "", get: () => null, desc: "Countries are left uncolored so the basemap and the lines show clearly. Click any country for its box.", src: "" });
seq("all", "The big picture", "Ulterior influence, all around (everything combined)", {
  dom: "max", f: (v) => fmt(v, 0) + " of 100", get: (p) => allScore(p),
  desc: "How exposed each central bank is to influence serving someone other than the public: the average of the outside-influence and inside-influence scores below and a third for the corruption and secrecy around the bank (corruption in the country, money-laundering risk in its banks, and laws that hide who owns money). Scored where at least two of the three have data. Light means more exposed.",
  src: "All sources on this map; see About and sources." });
seq("comp", "The big picture", "Outside influence (governments and foreign powers)", {
  dom: "max", f: (v) => fmt(v, 0) + " of 100", get: (p) => compScore(p),
  desc: "How far governments and foreign powers can steer the bank: what its law allows the government, reported government pressure 2010–18, documented moves against it 2019–26 (firings, prosecutions, frozen reserves), and money issued, backed or fixed from abroad. Averaged, 0 to 100. Scored where the law or pressure studies cover the bank. Light means more exposed.",
  src: "Romelli; Garriga; Binder; documented events; currency arrangements (see About and sources)." });
seq("inside", "The big picture", "Inside influence (its own officials and owners)", {
  dom: "max", f: (v) => fmt(v, 0) + " of 100", get: (p) => inScore(p),
  desc: "How far people inside the bank have used it, or could use it, for others' ends: documented corruption cases inside the bank since 1990, officials moving between the bank and private finance, private shareholders sitting inside its governance, and how little it tells the public. Averaged, 0 to 100. Scored where the transparency study covers the bank or any case, move or private owner is documented. No documented case means none was found, not that none happened. Light means more exposed.",
  src: "Documented cases and moves; ownership records; Dincer, Eichengreen and Geraats (see About and sources)." });
seq("cbie", "Independence written into law", "Overall independence, 42 rules (Romelli)", {
  years: [1970, 2023], dom: [0, 1], f: (v) => fmt(v, 3), get: (p, y) => latestOr(p, "r", "rs", y, (o) => o.i),
  desc: "How far the central bank's own law shields it from the government, from 0 (no shield) to 1 (full). Averages six parts made of 42 rules: who appoints and can fire the governor and board, who sets policy, the price-stability goal, limits on lending to the government, control of its own money and budget, and duties to report.",
  src: "Romelli, CBIE index, 155 places, laws to 2023 (cbidata.org, 2025 release)." });
DIM6.forEach((nm, i) => seq("cbie" + i, "Independence written into law", "  " + nm + " (Romelli)", {
  dom: [0, 1], f: (v) => fmt(v, 3), get: (p) => { const r = own(p, "r"); return r ? { v: r.o.d[i], via: r.via, y: r.o.y } : null; },
  desc: "One of the six parts of Romelli's index, 0 to 1. Open a country to see every rule in this part.", src: "Romelli, CBIE index, laws to 2023." }));
seq("cwn", "Independence written into law", "Overall independence, Cukierman method (Garriga)", {
  years: [1970, 2023], dom: [0, 1], f: (v) => fmt(v, 3), get: (p, y) => latestOr(p, "g", "gs", y, (o) => o.w),
  desc: "The older, widely used Cukierman–Webb–Neyapti measure, coded for 192 places: the governor's appointment, term and dismissal; the bank's objectives; who makes policy; and limits on lending to the government. 0 to 1, weighted. This is the measure used in most maps like the one it replaces.",
  src: "Garriga, CBI dataset version 3 (2025), 1970–2023." });
DIM4.forEach((nm, i) => seq("cwn" + i, "Independence written into law", "  " + nm + " (Garriga)", {
  dom: [0, 1], f: (v) => fmt(v, 3), get: (p) => { const r = own(p, "g"); return r ? { v: r.o.d[i], via: r.via, y: r.o.y } : null; },
  desc: "One of the four parts of Garriga's coding, 0 to 1.", src: "Garriga (2025), latest year 2023." }));
seq("ti", "What it tells the public", "Transparency, 0–15 (Dincer, Eichengreen and Geraats)", {
  years: [1998, 2019], dom: [0, 15], f: (v) => fmt(v, 1), get: (p, y) => latestOr(p, "t", "ts", y, (o) => o.ti),
  desc: "Fifteen points for publishing its goals, its data and forecasts, how decisions are made (minutes and votes), explanations of decisions, and how well past policy worked. Places in the euro area and the three other currency unions carry their union bank's score.",
  src: "Dincer, Eichengreen and Geraats (2022), 112 central banks, 1998–2019." });
DIM5.forEach((nm, i) => seq("ti" + i, "What it tells the public", "  " + nm + " openness (0–3)", {
  dom: [0, 3], f: (v) => fmt(v, 1), get: (p) => { const r = own(p, "t"); return r ? { v: r.o.d[i], via: r.via, y: r.o.y } : null; },
  desc: "One of the five parts of the transparency index, 0 to 3.", src: "Dincer, Eichengreen and Geraats (2022), 2019." }));
seq("press", "Pressure in practice", "Quarters with reported government pressure, 2010–2018 (Binder)", {
  dom: "max", f: (v) => fmt(v, 0) + "%", get: (p) => { const r = own(p, "p"); return r && r.o.q ? { v: 100 * r.o.n / r.o.q, via: r.via } : null; },
  desc: "Share of quarters in which the Economist Intelligence Unit's country reports describe the government pressuring the central bank, almost always to cut rates or lend more. Light means more pressure.",
  src: "Binder, Political Pressure on Central Banks, 118 central banks, 2010–2018." });
seq("ev", "Pressure in practice", "Documented moves against the bank, 2019–2026", {
  dom: "max", f: (v) => fmt(v, 0), get: (p) => { const n = evN(p); return n ? { v: n } : null; },
  desc: "Firings, forced resignations, attempted dismissals, laws cutting independence, prosecutions, frozen reserves and open pressure campaigns, each with its source. Appointments and court rulings appear in the country box but are not counted.",
  src: "Compiled for this map from central bank, court, government and news-agency reports." });
seq("cc", "Corruption inside and around the bank", "Documented corruption cases at the central bank, since 1990", {
  dom: "max", f: (v) => fmt(v, 0), get: (p) => { const n = ccN(p); return n ? { v: n } : null; },
  desc: "Embezzlement, budget or election financing, leaked decisions, payments through foundations, sham contracts, officials trading on their own policies, bribery (including banknote-printing contracts), cheap foreign currency for insiders, hidden losses or rigged rescues, thefts tied to insiders, and money laundering, each with its source. Acquittals are listed in the box but not counted. Euro-area countries include ECB cases.",
  src: "Compiled for this map from courts, prosecutors, official inquiries and news reports (links in each box)." });
seq("cpi", "Corruption inside and around the bank", "Corruption in the country (Transparency International, 0–100)", {
  years: [2012, 2025], dom: [0, 100], f: (v) => fmt(v, 0), get: (p, y) => { if (!p.cpi) return null; if (S.latest) return { v: p.cpi.v, y: 2025 }; const v = atYear(p.cpi.s, y); return v == null ? null : { v, y }; },
  desc: "How corrupt the public sector is seen to be by experts and business people, 0 (very corrupt) to 100 (very clean). Dark means more corrupt.",
  src: "Transparency International, Corruption Perceptions Index 2025 (and 2012–2024)." });
seq("wgi", "Corruption inside and around the bank", "Control of corruption (World Bank, 0–100)", {
  dom: [0, 100], f: (v) => fmt(v, 0), get: (p) => p.wgi ? { v: p.wgi.v, y: p.wgi.y } : null,
  desc: "How far public power is used for private gain, including capture of the state by elites and private interests, 0 (worst) to 100 (best). Dark means more corrupt.",
  src: "World Bank, Worldwide Governance Indicators, 2025." });
seq("aml", "Corruption inside and around the bank", "Money-laundering risk (Basel AML Index, 0–10)", {
  dom: "max", f: (v) => fmt(v, 2), get: (p) => p.aml ? { v: p.aml.v } : null,
  desc: "Risk that the country's banks and financial system are used to launder money or finance terrorism: weak anti-laundering rules, financial secrecy, corruption, weak courts. The central bank or its sister supervisor oversees these banks. Light means more risk.",
  src: "Basel Institute on Governance, Basel AML Index 2025 (public edition, 177 places)." });
seq("fsi", "Corruption inside and around the bank", "Financial secrecy (Tax Justice Network, 0–100)", {
  dom: "max", f: (v) => fmt(v, 1), get: (p) => p.fsi ? { v: p.fsi.score } : null,
  desc: "How far the country's laws let people hide who owns money, companies and property from tax authorities and courts. Light means more secrecy. The box also gives the country's share of the world's secrecy, which weighs in the size of its offshore finance.",
  src: "Tax Justice Network, Financial Secrecy Index 2025 (141 places)." });
seq("lv", "Corruption inside and around the bank", "Public cost of bank rescues since 1970 (% of GDP)", {
  log: true, f: (v) => fmt(v, 1) + "%", get: (p) => { const c = (p.crises || []).filter((x) => x.fis != null); if (!c.length) return (p.crises || []).length ? { v: null } : null; return { v: c.reduce((a, x) => a + x.fis, 0) }; },
  desc: "Money the government spent rescuing and restructuring banks in each systemic banking crisis since 1970, added up, as a share of one year's output. A rescue is not wrongdoing by itself; documented abuse of rescues is counted in the cases layer. The box lists each crisis and how much the central bank lent to banks.",
  src: "Laeven and Valencia, Systemic Banking Crises Database 1970–2025 (IMF Working Paper 26/94, May 2026)." });
const REL_DESC = { own: "How many outside holders own shares in the central bank. Shareholders can vote on its board or receive its dividends; the box names each and says what their stake allows.",
    corrupt: "How many outside parties paid or bribed the bank's officials, or received money, contracts, favors or leaked decisions from them, in documented cases.",
    people: "How many individual ties: officials who came from or left for private finance (the revolving door), board seats, and members of private forums such as the Group of Thirty who sit with the bank's officials.",
    inst: "How many institutions the bank belongs to alongside other central banks and finance ministries: the Bank for International Settlements (owned by 63 central banks) and the Financial Stability Board.",
    control: "How many outside powers pressured, fired or prosecuted the bank's leaders (courts and prosecutors are counted separately), froze or seized its reserves, or guarantee its currency under a foreign agreement.",
    service: "How many firms print its banknotes, audit it or manage its money, plus other parties named in its cases.",
    account: "How many courts, prosecutors, inspectors and inquiries investigated, charged or tried its officials. This measures accountability, not outside control." };
seq("tiesSel", "Who central banks answer to", "Number of ties of the kinds ticked at right", {
  log: true, f: (v) => fmt(v, 0) + (v === 1 ? " tie" : " ties"), get: (p) => { const n = linksOfCountry(p.iso).filter((l) => S.netRel.has(l.rel)).length; return n ? { v: n } : null; },
  desc: "Each country is shaded by how many documented ties its central bank has to outside parties of the kinds ticked in the box at right (euro-area members include the ECB's). Light means more ties; dark grey means none of those kinds were found.",
  src: "Cases, ownership records, memberships, contracts and reports linked in each box." });
(D.PAT || []).forEach((pt) => {
  const roles = [...new Set(pt.countries.map((c) => c.role))].slice(0, 4);
  const RC = {}; pt.countries.forEach((c) => { RC[c.iso3] = c; });
  L.push({ id: "pat_" + pt.id, group: "Patterns behind the scenes", label: pt.title, kind: "cat", pat: pt,
    classes: roles.map((r) => [r, r]), other: "Other role", get: (p) => { const c = RC[p.iso] || (p.u && RC[p.u === "ECB" ? "EMU" : p.u]); return c ? (roles.includes(c.role) ? { v: c.role, note: c.note } : { v: null, other: true, note: c.note }) : null; },
    desc: pt.summary, src: "" });
});
cat("own", "Who central banks answer to", "Who owns the central bank (type of owners)", {
  classes: [["listed", "Private shareholders, shares traded on an exchange"], ["private", "Private shareholders, shares not traded"], ["mixed", "Shareholders other than the state named, terms in the box"]],
  other: "No private shareholders found", get: (p) => p.own ? { v: p.own.k } : { v: null, other: true },
  desc: "Shown while only 'Who owns it' is ticked at right. Most central banks belong wholly to the state; these are the ones whose statutes or reports name other owners. Each outside shareholder is drawn as a diamond at its head office.",
  src: "Each bank's statute, annual report or exchange listing (links in its box)." });
cat("arr", "Ownership and outside control", "Whose money it is", {
  classes: [["union", "Shares a central bank with other countries"], ["guarantee", "Currency backed by a foreign treasury"], ["foreign", "Uses another country's currency"], ["board", "Currency board"]],
  other: "Own currency and own central bank", get: (p) => p.arrk ? { v: p.arrk } : { v: null, other: true },
  desc: "Where a country's money is issued or backed from outside, or tied by law to a foreign currency.",
  src: "Union and central bank statutes, finance ministries; regime from Ilzetzki, Reinhart and Rogoff (December 2025)." });
cat("reg", "Ownership and outside control", "Exchange-rate regime, December 2025", {
  classes: [[1, "Peg, currency board or no own currency"], [2, "Crawling peg or narrow band"], [3, "Wider band or managed float"], [4, "Free float"]],
  other: "Freely falling, or dual market", get: (p) => p.f == null ? null : (COARSE[p.f] <= 4 ? { v: COARSE[p.f] } : { v: null, other: true }),
  desc: "How the currency actually behaves against its anchor, judged from market rates (including parallel markets), not from what the government declares.",
  src: "Ilzetzki, Reinhart and Rogoff, monthly classification to December 2025 (October 2026 release)." });
cat("anc", "Reach beyond its borders", "Which currency each country follows", {
  classes: [["USD", "US dollar (Federal Reserve)"], ["EUR", "Euro (European Central Bank)"], ["one", "Another single currency"], ["two", "Two currencies or a basket"]],
  other: "No anchor found, or its own", get: (p) => { const a = p.a; if (!a) return null; if (a === "USD" || a === "EUR") return { v: a }; if (/^(AUD|ZAR|INR|CNY|SGD|CHF)$/.test(a)) return { v: "one" }; if (a.includes("-") || a.includes("+") || a === "SDR") return { v: "two" }; return { v: null, other: true }; },
  desc: "The anchor or reference currency each country's exchange rate is measured against, December 2025. Turn on the anchor lines to see the ties; dashed lines are countries that float against their reference.",
  src: "Ilzetzki, Reinhart and Rogoff, anchor currency, December 2025 (October 2026 release)." });
const curv = (k) => (p) => { const c = curOf(p); if (!c || c[k] == null) return null; return { v: c[k], via: c.iss !== p.iso ? c.code : null }; };
seq("fx", "Reach beyond its borders", "Share of world currency trading, April 2025", {
  log: true, f: (v) => fmt(v, 2) + "%", get: curv("fx"),
  desc: "Share of the $9.5 trillion traded each day on foreign exchange markets that involves this currency. Each trade has two sides, so shares add to 200%. Countries using another country's currency carry that currency's share.",
  src: "BIS Triennial Central Bank Survey, April 2025, net-net basis." });
seq("res", "Reach beyond its borders", "Share of governments' foreign reserves, mid-2026", {
  log: true, f: (v) => fmt(v, 2) + "%", get: curv("res"),
  desc: "Share of the world's official foreign-exchange reserves (allocated) held in this currency. The IMF names eight currencies; the rest are pooled as 'other'.",
  src: "IMF COFER, 2026 Q2." });
seq("pay", "Reach beyond its borders", "Share of international payments, June 2026", {
  log: true, f: (v) => fmt(v, 2) + "%", get: curv("pay"),
  desc: "Share by value of payments sent over the Swift network, euro-area payments included. Swift publishes the top 20 currencies.",
  src: "Swift Global Currency Tracker, June 2026 data." });
seq("tied", "Reach beyond its borders", "Countries tied to its currency, December 2025", {
  log: true, f: (v) => fmt(v, 0), get: (p) => { const c = curOf(p); if (!c || !c.tied) return null; const iss = c.iss; if (iss === p.iso || iss === p.u || (p.u && iss === p.u)) return { v: c.tied, via: iss === p.u ? null : null }; return null; },
  desc: "For each currency's issuing country: how many other countries use that currency as their own money, or peg their currency to it or hold it within a band of it, judged from market rates. Their central banks must follow its issuer's interest-rate decisions.",
  src: "Ilzetzki, Reinhart and Rogoff, December 2025; ISO 4217 currency lists." });
seq("bs", "Reach beyond its borders", "Size of the central bank (total assets, US$ billions)", {
  log: true, f: (v) => "$" + fmt(v, 1) + " bn", get: (p) => { const r = own(p, "bs"); return r && r.o.usd != null ? { v: r.o.usd, via: r.via } : null; },
  desc: "Everything the central bank owns, at the end of 2025. For euro-area members this is the national central bank's own balance sheet within the Eurosystem.",
  src: "BIS, central bank total assets (break-adjusted), 2025." });
seq("bsg", "Reach beyond its borders", "Size of the central bank (assets as % of GDP)", {
  log: true, f: (v) => fmt(v, 1) + "%", get: (p) => { const r = own(p, "bs"); return r && r.o.gdp != null ? { v: r.o.gdp, via: r.via } : null; },
  desc: "Total assets compared with the yearly output of the economy.", src: "BIS, central bank total assets, 2025." });
seq("gold", "Reach beyond its borders", "Gold held (tonnes)", {
  log: true, f: (v) => fmt(v, 1) + " t", get: (p) => p.gold ? { v: p.gold.t } : null,
  desc: "Official gold holdings, mostly kept by the central bank.", src: "" });
seq("swaps", "Reach beyond its borders", "Swap lines with other central banks", {
  log: true, f: (v) => fmt(v, 0), get: (p) => { const n = (p.sw || []).filter((i) => D.SW[i].status !== "expired").length; return n ? { v: n } : null; },
  desc: "Agreements to lend each other currency on demand. Count of lines in force (or of unclear status) that this country's central bank, or its union bank, is part of; lapsed lines are listed in the box but not counted. Turn on swap lines to see them drawn.",
  src: "Central bank announcements and reports (links in each box)." });

/* ---------- state ---------- */
const S = { sideOpen: {}, mainLayer: "all", hov: null, names: true, net: false, netRel: new Set(), ent: null, layer: "all", year: 2023, latest: true, sel: null, swaps: false, anchors: false, q: "" };
const layer = () => L.find((l) => l.id === S.layer);
function val(p) { const l = layer(); return l.get(p, S.year); }
// Values and ranges are cached per layer, year and "latest" setting; nothing else changes them.
const CACHE_V = new Map(), CACHE_D = new Map();
L.forEach((l) => { const g = l.get; l.get = (p, y) => { const key = l.id + "|" + (S.latest ? "L" : y) + "|" + (p && p.iso); if (CACHE_V.has(key)) return CACHE_V.get(key); const r = g(p, y); CACHE_V.set(key, r); return r; }; });
function dom(l) { const key = l.id + "|" + (S.latest ? "L" : S.year); if (!CACHE_D.has(key)) CACHE_D.set(key, dom0(l)); return CACHE_D.get(key); }
function dom0(l) {
  if (l.dom && l.dom !== "max") return l.dom;
  if (l.dom === "max") { const vs = ISOS.map((k) => { const r = l.get(P[k], S.year); return r ? r.v : null; }).filter((v) => v != null); return [0, Math.max(1, ...vs)]; }
  const vs = ISOS.map((k) => { const r = l.get(P[k], S.year); return r && r.v > 0 ? r.v : null; }).filter((v) => v != null);
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
const BM = CulpritsBasemaps.create("map", { initial: "night", projection: "globe", plate: window.PLATE_IMG, center: [12, 25], zoom: startZoom(),
  onApply: (k) => { BASE = k; if (!S.names) setTimeout(hideNames, 0); const u = UI[k] || UI.night, rs = document.documentElement.style; rs.setProperty("--accent", u[0]); rs.setProperty("--accent-hi", u[1]); rs.setProperty("--bg", u[2]); if (ready) { order(); update(); } },
  onReady: () => init() });
const map = window.cbMap = BM.maplibre;
// zoom buttons sit in the top-right row, beside Whole world and About and sources
map.once("idle", () => { const a = map.getContainer().querySelector(".maplibregl-ctrl-attrib"); if (a) { a.classList.remove("maplibregl-compact-show"); a.removeAttribute("open"); } });
function panelRight() { try { const r = $("#key").getBoundingClientRect(), w = map.getContainer().clientWidth; if (r.width && r.right < w * 0.6) return r.right + 10; } catch (e) {} return 0; }
function rightBox() { try { const r = $("#rcol").getBoundingClientRect(), w = map.getContainer().clientWidth; if (r.width && r.left > w * 0.5) return w - r.left + 10; } catch (e) {} return 0; }
// Place names: every basemap label layer (symbols and the raster of names), not this map's own layers.
function hideNames() {
  const st = map.getStyle(); if (!st) return; const mine = new Set(IDS);
  st.layers.forEach((l) => { if (!mine.has(l.id) && (l.type === "symbol" || l.id === "labels")) map.setLayoutProperty(l.id, "visibility", "none"); });
}
function wholeWorld() {
  const fb = freeBox(), padding = { left: fb.L, right: fb.R, top: 0, bottom: 0 };
  if (proj === "globe") map.flyTo({ center: [12, 25], zoom: startZoom(), padding, duration: 1200 });
  else { const z = Math.max(0, Math.log2(Math.min(fb.fw - 20, (fb.H - 40) * 1.55) / 512)); map.flyTo({ center: [10, 22], zoom: z, padding, duration: 1200 }); }
}
const IDS = [];
function order() { const st = map.getStyle(); if (!st) return; const mine = new Set(IDS); const first = st.layers.find((l) => !mine.has(l.id) && (l.type === "symbol" || l.id === "labels")); IDS.forEach((id) => { if (map.getLayer(id)) map.moveLayer(id, first ? first.id : undefined); }); }

const tt = $("#ttip");
function tip(html, x, y) { if (!html) { tt.style.display = "none"; return; } tt.innerHTML = html; tt.style.display = "block"; const r = tt.getBoundingClientRect(); let Lx = x + 14, T = y + 12; if (Lx + r.width > innerWidth - 6) Lx = x - r.width - 12; if (T + r.height > innerHeight - 6) T = y - r.height - 10; tt.style.left = Lx + "px"; tt.style.top = T + "px"; }

// Country shapes: the Culprits map's boundaries file, as on the other maps. Kosovo, Somaliland and Northern Cyprus carry no code there and are matched by name.
const BOUND_URL = "https://welcometoyourgalaxy.github.io/culprits/data/boundaries.geojson";
const BYNAME = { "Kosovo": "XKX", "Somaliland": "SOL", "Northern Cyprus": "CYN" };
let SHAPED = new Set();
// Straight lines in longitude and latitude, never crossing the 180° edge; densified so the globe draws them as paths, not chords.
function straight(a, b, n) { n = n || 24; const o = []; for (let i = 0; i <= n; i++) { const t = i / n; o.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t]); } return o; }
function gc(a, b, n) { return straight(a, b, n); }
function gcOld(a, b, n) {   // points along the great circle from a to b (no longer used)
  const r = Math.PI / 180, [l1, p1] = [a[0] * r, a[1] * r], [l2, p2] = [b[0] * r, b[1] * r];
  const v1 = [Math.cos(p1) * Math.cos(l1), Math.cos(p1) * Math.sin(l1), Math.sin(p1)], v2 = [Math.cos(p2) * Math.cos(l2), Math.cos(p2) * Math.sin(l2), Math.sin(p2)];
  const d = Math.acos(Math.max(-1, Math.min(1, v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2])));
  if (d < 1e-6) return [a, b];
  const out = []; let prev = null;
  for (let i = 0; i <= n; i++) {
    const t = i / n, A = Math.sin((1 - t) * d) / Math.sin(d), B = Math.sin(t * d) / Math.sin(d);
    const x = A * v1[0] + B * v2[0], y = A * v1[1] + B * v2[1], z = A * v1[2] + B * v2[2];
    let lng = Math.atan2(y, x) / r; const lat = Math.atan2(z, Math.hypot(x, y)) / r;
    if (prev != null) { while (lng - prev > 180) lng -= 360; while (lng - prev < -180) lng += 360; }
    prev = lng; out.push([lng, lat]);
  }
  return out;
}
function addLayers(geo) {
  geo.features.forEach((f) => { const p = f.properties; if (!p.iso3 || p.iso3 === "-99") p.iso3 = BYNAME[p.name] || ""; });
  SHAPED = new Set(geo.features.map((f) => f.properties.iso3).filter(Boolean));
  map.addSource("ctry", { type: "geojson", data: geo });
  map.addLayer({ id: "c-fill", type: "fill", source: "ctry", filter: ["!=", ["get", "iso3"], ""], paint: { "fill-color": NODATA, "fill-opacity": ["interpolate", ["linear"], ["zoom"], 0, 0.82, 5, 0.7, 8, 0.45] } });
  map.addLayer({ id: "c-line", type: "line", source: "ctry", paint: { "line-color": "#05061a", "line-width": 0.5, "line-opacity": 0.8 } });
  map.addLayer({ id: "c-grp", type: "line", source: "ctry", filter: ["in", ["get", "iso3"], ["literal", []]], paint: { "line-color": "#f0ece4", "line-width": 0.8, "line-opacity": 0.55, "line-dasharray": [2, 2] } });
  map.addLayer({ id: "c-sel", type: "line", source: "ctry", filter: ["in", ["get", "iso3"], ["literal", []]], paint: { "line-color": "#f0ece4", "line-width": 1.6, "line-opacity": 0.95 } });
  // places too small for the shapes file get a dot
  const dots = ISOS.filter((k) => !SHAPED.has(k) && P[k].pt).map((k) => ({ type: "Feature", properties: { iso3: k }, geometry: { type: "Point", coordinates: P[k].pt } }));
  map.addSource("dots", { type: "geojson", data: { type: "FeatureCollection", features: dots } });
  map.addLayer({ id: "c-dots", type: "circle", source: "dots", paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 3.2, 6, 6], "circle-color": NODATA, "circle-stroke-color": "#05061a", "circle-stroke-width": 0.8, "circle-pitch-alignment": "map" } });
  map.addSource("links", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
  map.addLayer({ id: "l-solid", type: "line", source: "links", filter: ["!", ["get", "dash"]], layout: { "line-cap": "round" }, paint: { "line-color": ["get", "col"], "line-width": ["get", "w"], "line-opacity": 0.8 } });
  map.addLayer({ id: "l-dash", type: "line", source: "links", filter: ["get", "dash"], paint: { "line-color": ["get", "col"], "line-width": 0.9, "line-opacity": 0.6, "line-dasharray": [2, 2] } });
  map.addSource("hubs", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
  map.addLayer({ id: "l-hub", type: "circle", source: "hubs", paint: { "circle-radius": 4.5, "circle-color": ["get", "col"], "circle-stroke-color": "#f0ece4", "circle-stroke-width": 1.2, "circle-pitch-alignment": "map" } });
  IDS.push("c-fill", "c-line", "c-grp", "c-dots", "l-dash", "l-solid", "l-hub", "c-sel"); order();
  addNetLayers();
  const hit = (pt) => { const f = map.queryRenderedFeatures([[pt.x - 3, pt.y - 3], [pt.x + 3, pt.y + 3]], { layers: ["c-dots", "c-fill"] }); return f.length ? f[0].properties.iso3 : null; };
  // What is under the pointer: a party's diamond first (8 px around it), then a tie line (6 px band), then a country.
  const under = (pt) => {
    if (S.net && map.getLayer("net-node")) {
      const f = map.queryRenderedFeatures([[pt.x - 8, pt.y - 8], [pt.x + 8, pt.y + 8]], { layers: ["net-node-hot", "net-node"] });
      if (f.length) { let best = f[0], bd = 1e9; f.forEach((x) => { const p = map.project(x.geometry.coordinates), d = Math.hypot(p.x - pt.x, p.y - pt.y); if (d < bd) { bd = d; best = x; } }); return { node: best.properties.i }; }
      const g = map.queryRenderedFeatures([[pt.x - 6, pt.y - 6], [pt.x + 6, pt.y + 6]], { layers: ["net-hit"] });
      if (g.length) return { line: g[0].properties };
    }
    const k = hit(pt); return k && P[k] ? { ctry: k } : {};
  };
  map.on("click", (e) => {
    const u = under(e.point);
    if (u.node != null) { selectEntity(u.node); return; }
    if (u.line) { selectEntity(u.line.n); return; }
    if (u.ctry) select(u.ctry, false);
  });
  let rafPending = null;
  const kindNames = (s) => String(s || "").split(",").filter(Boolean).map((k) => (REL_SHORT[k] || k).split(":")[0].toLowerCase()).join(", ");
  const onMove = (e) => {
    const u = under(e.point), x = e.originalEvent.clientX, y = e.originalEvent.clientY;
    const n = u.node != null ? u.node : u.line ? u.line.n : null;
    if (n !== S.hov) { S.hov = n; setHot(n); }
    if (u.node != null) {
      const nd = NET.nodes[u.node], ls = linksOfNode(u.node).filter((l) => S.netRel.has(l.rel)), c = new Set(ls.filter((l) => l.cb).map((l) => l.cb)).size;
      const top = Object.entries(ls.reduce((o, l) => (o[l.rel] = (o[l.rel] || 0) + 1, o), {})).sort((p, q) => q[1] - p[1])[0];
      map.getCanvas().style.cursor = "pointer";
      tip("<b>" + esc(nd.name) + "</b> · tied to " + c + " central bank" + (c === 1 ? "" : "s") + (top ? "<br><span class=m>" + esc(RELMEAN[top[0]].split(". ")[0]) + ".</span>" : "") + "<br><span class=m>Click for details.</span>", x, y); return;
    }
    if (u.line) {
      const L2 = u.line, far = L2.tn >= 0 ? NET.nodes[L2.tn].name : cbName(L2.cb);
      map.getCanvas().style.cursor = "pointer";
      tip("<b>" + esc(NET.nodes[L2.n].name) + "</b> → " + esc(far) + "<br><span class=m>" + L2.cnt + " tie" + (L2.cnt > 1 ? "s" : "") + ": " + esc(kindNames(L2.kinds)) + ". Click for details.</span>", x, y); return;
    }
    map.getCanvas().style.cursor = u.ctry ? "pointer" : "";
    if (!u.ctry) { tip(null); return; }
    const l = layer(), r = l.get(P[u.ctry], S.year);
    tip("<b>" + esc(P[u.ctry].n) + "</b><br>" + valText(l, r, P[u.ctry]), x, y);
  };
  map.on("mousemove", (e) => { rafPending = e; requestAnimationFrame(() => { if (rafPending) { const ev = rafPending; rafPending = null; onMove(ev); } }); });
  map.on("mouseout", () => { rafPending = null; tip(null); if (S.hov != null) { S.hov = null; setHot(null); } });
}
// Where a value sits among all places, in plain words.
const HIGH_GOOD = new Set(["cbie", "cwn", "ti", "cpi", "wgi"].concat([0, 1, 2, 3, 4, 5].map((i) => "cbie" + i), [0, 1, 2, 3].map((i) => "cwn" + i), [0, 1, 2, 3, 4].map((i) => "ti" + i)));
function plainRank(l, r) {
  if (!r || r.v == null || l.kind !== "seq" || l.id === "none") return "";
  const vs = ISOS.map((k) => { const x = l.get(P[k], S.year); return x && x.v != null ? x.v : null; }).filter((v) => v != null);
  if (vs.length < 5) return "";
  const below = vs.filter((v) => v < r.v).length / vs.length, above = vs.filter((v) => v > r.v).length / vs.length;
  const good = HIGH_GOOD.has(l.id);
  const word = l.id === "cpi" || l.id === "wgi" ? "cleaner than" : good ? "more shielded than" : /^(fx|res|pay|tied|bs|bsg|gold|swaps)$/.test(l.id) ? "more reach than" : /^(ties|tiesAll)/.test(l.id) ? "more ties than" : "more exposed than";
  const share = Math.round(100 * below);
  if (share >= 50) return word + " " + share + "% of the " + vs.length + " places with a figure";
  const opp = { "cleaner than": "more corrupt than", "more shielded than": "less shielded than", "more reach than": "less reach than", "more ties than": "fewer ties than", "more exposed than": "less exposed than" }[word];
  return opp + " " + Math.round(100 * above) + "% of the " + vs.length + " places with a figure";
}
function valText(l, r, p) {
  if (!r) return '<span class="m">No figure from this source</span>';
  let s;
  if (l.kind === "cat") s = r.v == null ? l.other : (l.classes.find((c) => c[0] === r.v) || [0, l.other])[1];
  else s = l.f(r.v);
  if (r.via) s += ' <span class="m">(' + (CUR[r.via] ? esc(CUR[r.via].name) + ", the currency it uses" : esc(CB_NAMES[r.via] || r.via) + "'s figure") + ')</span>';
  if (r.y && !S.latest) s += ' <span class="m">· ' + r.y + '</span>';
  const pr = plainRank(l, r); if (pr) s += '<br><span class="m">' + pr + '</span>';
  if (r.note) s += '<br><span class="m">' + esc(r.note) + '</span>';
  return s;
}

/* ---------- lines: swap lines and anchor ties ---------- */
const PROV = [["USA", "Federal Reserve"], ["ECB", "European Central Bank"], ["CHN", "People's Bank of China"]];
function provColor(iso) { const i = PROV.findIndex((x) => x[0] === iso); return i < 0 ? CATC[3] : CATC[i]; }
const ptOf = (k) => (D.HUB[k]) || (P[k] && P[k].pt) || (U[k] && U[k].pt);
function drawLinks() {
  const feats = [], hubs = new Map();
  if (S.swaps) D.SW.forEach((s) => {
    if (s.status === "expired") return;
    const a = ptOf(s.provider_iso3 === "EMU" ? "ECB" : s.provider_iso3), b = ptOf(s.counterparty_iso3 === "EMU" ? "ECB" : s.counterparty_iso3);
    if (!a || !b) return;
    const col = provColor(s.provider_iso3 === "EMU" ? "ECB" : s.provider_iso3);
    const on = S.sel && (S.sel === s.provider_iso3 || S.sel === s.counterparty_iso3 || (P[S.sel] && P[S.sel].u === "ECB" && (s.provider_iso3 === "EMU" || s.counterparty_iso3 === "EMU")));
    feats.push({ type: "Feature", properties: { col, w: on ? 2.2 : 1.1, dash: false }, geometry: { type: "LineString", coordinates: gc(a, b, 48) } });
    hubs.set(s.provider_iso3, col);
  });
  if (S.anchors) ISOS.forEach((k) => {
    const p = P[k], a = p.a; if (!a || !p.pt) return;
    const iss = { USD: "USD", EUR: "EUR", AUD: "AUD", ZAR: "ZAR", INR: "INR", CNY: "CNY", SGD: "SGD", CHF: "CHF" }[a];
    if (!iss) return;
    const h = D.HUB[iss]; if (!h) return;
    const issIso = CUR[iss] && CUR[iss].iss; if (issIso === k || (iss === "EUR" && p.u === "ECB")) return;
    const col = iss === "USD" ? CATC[0] : iss === "EUR" ? CATC[1] : CATC[2];
    const floats = p.f != null && p.f >= 12;
    feats.push({ type: "Feature", properties: { col, w: S.sel === k ? 2.2 : 1, dash: floats }, geometry: { type: "LineString", coordinates: gc(h, p.pt, 40) } });
    hubs.set(iss, col);
  });
  map.getSource("links").setData({ type: "FeatureCollection", features: feats });
  map.getSource("hubs").setData({ type: "FeatureCollection", features: [...hubs].map(([k, col]) => ({ type: "Feature", properties: { col }, geometry: { type: "Point", coordinates: ptOf(k === "EMU" ? "ECB" : k) || D.HUB[k] } })).filter((f) => f.geometry.coordinates) });
}


/* ---------- networks: who central banks have answered to, dealt with or been corrupt with ---------- */
const NET = D.NET || { nodes: [], links: [] };
const BASEL = [7.59, 47.56];
const cbPt = (cb) => cb === "BIS" ? BASEL : cb === "EMU" ? ptOf("ECB") : ptOf(cb);
const cbName = (cb) => cb === "BIS" ? "Bank for International Settlements" : cb === "EMU" ? "European Central Bank" : (P[cb] ? (P[cb].cb || P[cb].n) + " (" + P[cb].n + ")" : cb);
NET.links.forEach((l, i) => { l.i = i; });
const linksOfNode = (n) => NET.links.filter((l) => l.n === n || l.tn === n);
const endOf = (l) => l.tn != null ? NET.nodes[l.tn].ll : cbPt(l.cb);
const otherName = (l, n) => l.tn != null ? NET.nodes[l.n === n ? l.tn : l.n].name : cbName(l.cb);

// One plain sentence per tie: who did what, to which central bank.
const SAY = {
  "Owns shares": "{P} owns shares in {B}",
  "Bribery or misconduct with the bank": "{P} is named in a bribery or misconduct case involving {B}",
  "Paid or bribed the bank's officials": "{P} paid or bribed officials of {B}",
  "Received leaked information": "{P} received confidential information leaked from {B}",
  "Received money, favors or contracts from the bank": "{P} received money, favors or contracts from {B}",
  "Member and shareholder of the BIS": "{B} is a member and part-owner of {P}",
  "Member of the Financial Stability Board": "{P} sits on the Financial Stability Board alongside {T}",
  "Member of the same forum": "Officials of {B} take part in {P}",
  "Represented in the Group of Thirty": "{P} has a member in {T}, where central bankers also sit",
  "Employed an official before or after (revolving door)": "{P} employed an official of {B} before or after their time there",
  "Sits on the board": "{P} sits on the board of {B}",
  "Audited or investigated": "{P} audited or investigated {B} or its officials",
  "Named in the case": "{P} is named in a documented case involving {B}",
  "Named in the event": "{P} is named in a documented event involving {B}",
  "Pressured, dismissed or prosecuted bank officials": "{P} pressured, dismissed or prosecuted officials of {B}",
  "Froze or seized the bank's reserves": "{P} froze or seized reserves belonging to {B}",
  "Guarantees the currency under a cooperation agreement": "{P} guarantees the currency issued by {B} under a cooperation agreement",
  "Audits its accounts": "{P} audits the accounts of {B}",
  "Manages its reserves or programmes": "{P} manages reserves or funds for {B}",
  "Owned or ran an asset officials held": "{P} owned or ran an asset held by officials of {B}",
  "Prints its banknotes": "{P} prints banknotes for {B}",
  "Other": "{P} has another documented tie to {B}" };
function sayLink(l) {
  const the = (x) => /^(Bank of|Bank for|Central|Reserve|National|Federal|European|Monetary|Swiss|People's|Eastern|Royal|State|Saudi|Qatar|Hong Kong|Maldives|Czech|Prudential|Group of|Financial Stability|International Monetary|World Bank|French Treasury|Serious Fraud)/.test(x) ? "the " + x : x;
  const P = the(NET.nodes[l.n].name), T = l.tn != null ? the(NET.nodes[l.tn].name) : "", B = l.cb ? the(cbName(l.cb)) : T;
  const t = SAY[l.role] || ("{P}: " + l.role.toLowerCase() + " ({B})");
  const out = t.replace("{P}", P).replace("{T}", T).replace("{B}", B).replace(/the the /g, "the ");
  return out.charAt(0).toUpperCase() + out.slice(1) + ".";
}
function srcItem(l, head) {
  let d = (l.detail || "").trim().replace(/Rank (\d+) on list\./, (m, r) => "Number " + r + " on the bank's list of shareholders.").replace(/\bpct computed from/, "Percentage worked out from").replace(/\(([0-9]{4}-[0-9]{2}-[0-9]{2})\)/, "(as of $1)"); if (d && !/[.!?)"']$/.test(d)) d += ".";
  const sent = esc(sayLink(l)), pn = esc(NET.nodes[l.n].name);
  return '<li>' + (head ? '<b>' + esc(head.replace(/\.$/, "")) + '.</b> ' + sent : sent.replace(pn, '<b>' + pn + '</b>')) + (d ? ' ' + esc(d) : '') + ' <span class="note">' + link(l.src_t || "source", l.src_u) + '</span></li>';
}
const linksOfCountry = (k) => NET.links.filter((l) => l.cb === k || (l.cb === "EMU" && P[k] && P[k].u === "ECB"));
function addNetLayers() {
  const c = document.createElement("canvas"); c.width = c.height = 32; const g = c.getContext("2d");
  g.fillStyle = "#fff"; g.beginPath(); g.moveTo(16, 2); g.lineTo(30, 16); g.lineTo(16, 30); g.lineTo(2, 16); g.closePath(); g.fill();
  map.addImage("diamond", { width: 32, height: 32, data: g.getImageData(0, 0, 32, 32).data }, { sdf: true, pixelRatio: 2 });
  map.addSource("net-lines", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
  const lp = { "line-color": ["get", "col"], "line-width": ["get", "w"], "line-opacity": ["get", "o"] };
  map.addLayer({ id: "net-dot", type: "line", source: "net-lines", filter: ["==", ["get", "st"], "dot"], paint: Object.assign({ "line-dasharray": [0.6, 1.8] }, lp) });
  map.addLayer({ id: "net-line", type: "line", source: "net-lines", filter: ["==", ["get", "st"], "solid"], layout: { "line-cap": "round" }, paint: lp });
  map.addLayer({ id: "net-dash", type: "line", source: "net-lines", filter: ["==", ["get", "st"], "dash"], paint: Object.assign({ "line-dasharray": [2, 2] }, lp) });
  // the lit-up ties of the party or line under the pointer
  map.addLayer({ id: "net-hot", type: "line", source: "net-lines", filter: ["==", ["get", "n"], -1], layout: { "line-cap": "round" }, paint: { "line-color": ["get", "col"], "line-width": 2.4, "line-opacity": 0.95 } });
  // a wide invisible band along each line, so a line is easy to point at
  map.addLayer({ id: "net-hit", type: "line", source: "net-lines", paint: { "line-color": "#000", "line-width": 12, "line-opacity": 0.01 } });
  map.addSource("net-nodes", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
  // parties at one address fan out a few screen pixels around it; the point itself stays at the true place at every zoom
  const offs = ["interpolate", ["linear"], ["zoom"], 1, ["get", "off0"], 5, ["get", "off1"]];
  map.addLayer({ id: "net-node", type: "symbol", source: "net-nodes", layout: { "icon-image": "diamond", "icon-size": ["get", "s"], "icon-offset": offs, "icon-allow-overlap": true, "icon-ignore-placement": true, "symbol-sort-key": ["get", "k"] },
    paint: { "icon-color": ["get", "col"], "icon-opacity": ["get", "o"], "icon-halo-color": "#05061a", "icon-halo-width": 1.2 } });
  map.addLayer({ id: "net-node-hot", type: "symbol", source: "net-nodes", filter: ["==", ["get", "i"], -1], layout: { "icon-image": "diamond", "icon-size": ["*", 1.35, ["get", "s"]], "icon-offset": ["interpolate", ["linear"], ["zoom"], 1, ["get", "off0h"], 5, ["get", "off1h"]], "icon-allow-overlap": true, "icon-ignore-placement": true },
    paint: { "icon-color": ["get", "col"], "icon-halo-color": "#f0ece4", "icon-halo-width": 1.6 } });
  map.addLayer({ id: "c-hov", type: "line", source: "ctry", filter: ["in", ["get", "iso3"], ["literal", []]], paint: { "line-color": "#f0ece4", "line-width": 1.6, "line-opacity": 0.95 } });
  IDS.push("c-hov", "net-dot", "net-line", "net-dash", "net-hit", "net-hot", "net-node", "net-node-hot"); order();
}
function netFilterOk(l) { return S.netRel.has(l.rel); }
function drawPattern() {
  if (!map.getSource("pat-lines")) {
    map.addSource("pat-lines", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
    map.addLayer({ id: "pat-line", type: "line", source: "pat-lines", layout: { "line-cap": "round" }, paint: { "line-color": "#f0ece4", "line-width": 1.6, "line-opacity": 0.8 } });
    map.addSource("pat-ends", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
    map.addLayer({ id: "pat-end", type: "circle", source: "pat-ends", paint: { "circle-radius": 3.5, "circle-color": "#f0ece4", "circle-stroke-color": "#05061a", "circle-stroke-width": 1, "circle-pitch-alignment": "map" } });
    IDS.push("pat-line", "pat-end"); order();
  }
  const l = layer(), pt = l.pat, lf = [], ef = [];
  if (pt) (pt.links || []).forEach((k) => { if (k.a && k.b) { lf.push({ type: "Feature", properties: {}, geometry: { type: "LineString", coordinates: straight(k.a, k.b, 24) } }); ef.push({ type: "Feature", properties: {}, geometry: { type: "Point", coordinates: k.a } }, { type: "Feature", properties: {}, geometry: { type: "Point", coordinates: k.b } }); } });
  map.getSource("pat-lines").setData({ type: "FeatureCollection", features: lf });
  map.getSource("pat-ends").setData({ type: "FeatureCollection", features: ef });
}
const cbOfLink = (l) => l.cb === "EMU" ? D.UM.ECB : l.cb === "BIS" || !l.cb ? [] : [l.cb];
// Screen-pixel fan-out for parties sharing one address (rounded to about 1 km); the true point never moves.
let FAN = null;
function fanOut() {
  if (FAN) return FAN;
  const groups = new Map(), deg = new Map();
  NET.links.forEach((l) => { [l.n, l.tn].forEach((m) => { if (m != null) deg.set(m, (deg.get(m) || 0) + 1); }); });
  NET.nodes.forEach((nd, i) => { if (!nd.ll) return; const k = nd.ll[0].toFixed(2) + "," + nd.ll[1].toFixed(2); if (!groups.has(k)) groups.set(k, []); groups.get(k).push(i); });
  FAN = new Map();
  groups.forEach((list) => {
    list.sort((a, b) => (deg.get(b) || 0) - (deg.get(a) || 0));
    list.forEach((i, j) => { if (!j) { FAN.set(i, [0, 0]); return; } const r = Math.sqrt(j), t = j * 2.39996; FAN.set(i, [r * Math.cos(t), r * Math.sin(t)]); });
  });
  return FAN;
}
const linkKey = (l) => l.tn != null ? "n" + l.tn : l.cb;
function drawNet() {
  if (!map.getSource("net-lines")) return;
  if (!S.net) { ["net-lines", "net-nodes"].forEach((s) => map.getSource(s).setData({ type: "FeatureCollection", features: [] })); setHot(null); return; }
  const focus = S.ent != null || S.sel != null;
  const hot = (l) => l.n === S.ent || l.tn === S.ent || (S.sel != null && (l.cb === S.sel || (l.cb === "EMU" && P[S.sel] && P[S.sel].u === "ECB")));
  // one line per party and far end, colored by the main kind of tie between them
  const pairs = new Map(), per = new Map();
  NET.links.forEach((l) => {
    if (!S.netRel.has(l.rel)) return;
    const nd = NET.nodes[l.n], b = l.tn != null ? NET.nodes[l.tn].ll : cbPt(l.cb); if (!nd.ll || !b) return;
    const key = l.n + "|" + linkKey(l);
    const e = pairs.get(key) || { n: l.n, tn: l.tn, cb: l.cb, a: nd.ll, b, rel: {}, cnt: 0, hot: false }; e.cnt++; e.rel[l.rel] = (e.rel[l.rel] || 0) + 1; e.hot = e.hot || hot(l); pairs.set(key, e);
    [l.n, l.tn].forEach((m) => { if (m == null) return; const q = per.get(m) || { cbs: new Set(), rel: {}, hot: false }; if (l.cb) q.cbs.add(l.cb); q.rel[l.rel] = (q.rel[l.rel] || 0) + 1; q.hot = q.hot || hot(l); per.set(m, q); });
  });
  const main = (rel) => Object.entries(rel).sort((x, y) => (x[0] === "account") - (y[0] === "account") || y[1] - x[1])[0][0];
  // the more lines on screen, the fainter each one, so the whole set stays readable
  const base = pairs.size < 120 ? 0.55 : pairs.size < 400 ? 0.32 : 0.17;
  const lf = [];
  pairs.forEach((e) => {
    const r = main(e.rel), kinds = Object.keys(e.rel), st = kinds.length === 1 && RELDASH[r] ? RELDASH[r] : "solid";
    lf.push({ type: "Feature", properties: { n: e.n, tn: e.tn == null ? -1 : e.tn, cb: e.cb || "", st, col: RELC(r), w: (e.hot ? 1.8 : 0.8) + Math.min(1.4, Math.log2(e.cnt) * 0.45), o: focus ? (e.hot ? 0.95 : 0.06) : base, kinds: kinds.join(","), cnt: e.cnt }, geometry: { type: "LineString", coordinates: straight(e.a, e.b, 24) } });
  });
  const fan = fanOut(), nf = [];
  per.forEach((q, n) => {
    const nd = NET.nodes[n], s = q.cbs.size <= 1 ? 0.5 : Math.min(1.3, 0.5 + 0.13 * Math.sqrt(q.cbs.size)), f = fan.get(n) || [0, 0];
    const px = (gap, sz) => [f[0] * gap / sz, f[1] * gap / sz];
    nf.push({ type: "Feature", properties: { i: n, col: RELC(main(q.rel)), s, o: focus ? (q.hot ? 1 : 0.3) : 0.95, k: q.cbs.size, off0: px(4, s), off1: px(9, s), off0h: px(4, s * 1.35), off1h: px(9, s * 1.35) }, geometry: { type: "Point", coordinates: nd.ll } });
  });
  map.getSource("net-lines").setData({ type: "FeatureCollection", features: lf });
  map.getSource("net-nodes").setData({ type: "FeatureCollection", features: nf });
  setHot(S.hov);
}
// Light up one party's ties, diamond and countries by changing filters only (no redraw).
function setHot(n) {
  if (!map.getLayer("net-hot")) return;
  const on = n != null && S.net;
  map.setFilter("net-hot", on ? ["any", ["==", ["get", "n"], n], ["==", ["get", "tn"], n]] : ["==", ["get", "n"], -1]);
  map.setFilter("net-node-hot", on ? ["==", ["get", "i"], n] : ["==", ["get", "i"], -1]);
  let list = [];
  if (on) linksOfNode(n).filter((l) => S.netRel.has(l.rel)).forEach((l) => { list = list.concat(cbOfLink(l)); });
  map.setFilter("c-hov", ["in", ["get", "iso3"], ["literal", [...new Set(list)]]]);
}
function entityBox(n) {
  const nd = NET.nodes[n], ls = linksOfNode(n), h = [];
  const cbs = [...new Set(ls.filter((l) => l.cb).map((l) => l.cb))];
  const kinds = REL.filter((r) => ls.some((l) => l.rel === r[0]));
  h.push('<div class="hp-k">' + esc(nd.type || "") + (nd.parent ? " · part of " + esc(nd.parent) : "") + '</div><h3>' + esc(nd.name) + '</h3>');
  h.push('<p class="hp-sub">' + (nd.city ? esc(nd.city) + ", " : "") + esc(P[nd.iso3] ? P[nd.iso3].n : (nd.iso3 || "place not stated")) + (nd.approx ? ' <span class="note">(marker placed at the country, not the exact office)</span>' : '') + '</p>');
  const others = [...new Set(ls.filter((l) => l.tn != null).map((l) => otherName(l, n)))];
  h.push('<p><span class="big">' + cbs.length + '</span> central bank' + (cbs.length === 1 ? '' : 's') + (others.length ? ' and ' + others.length + ' other part' + (others.length === 1 ? 'y' : 'ies') : '') + ' tied to it.</p>');
  kinds.forEach((r) => {
    const g = ls.filter((l) => l.rel === r[0]);
    const names = [...new Set(g.map((l) => otherName(l, n)))];
    const usa = r[0] === "own" && g.some((l) => l.cb === "USA");
    h.push('<div class="hp-h"><span class="sw" style="display:inline-block;background:' + RELC(r[0]) + ';margin-right:6px"></span>' + esc(r[1]) + '</div>');
    h.push('<p class="note">' + (names.length > 12 ? names.slice(0, 12).map(esc).join(", ") + " and " + (names.length - 12) + " more" : names.map(esc).join(", ")) + '.</p>');
    h.push('<details><summary>What the sources say (' + g.length + ')</summary><ul>' + g.map((l) => srcItem(l, otherName(l, n))).join("") + (usa ? '<li>' + esc(USA_OWN.trim()) + '</li>' : '') + '</ul></details>');
  });
  h.push('<div class="hp-src">A tie is not, by itself, an accusation of wrongdoing. The colored mark says what kind of tie it is.</div>');
  $("#detBody").innerHTML = h.join("");
}
function selectEntity(n) {
  tip(null); S.ent = n; S.sel = null; entityBox(n); $("#det").classList.add("open"); $("#det").scrollTop = 0;
  paint(); drawList(); drawCharts();
  const nd = NET.nodes[n]; if (nd.ll) { const r = $("#det").getBoundingClientRect(), H = map.getContainer().clientHeight, fb = freeBox(); map.easeTo({ center: nd.ll, padding: { left: fb.L, right: fb.R, top: 10, bottom: Math.max(0, Math.min(H - 120, H - r.top + 10)) }, duration: 700 }); }
}
function countryNet(k) {
  const ls = linksOfCountry(k); if (!ls.length && k !== "USA") return "";
  const h = ['<div class="hp-h">Who it has answered to or dealt with</div>'];
  REL.forEach((r) => {
    const g = ls.filter((l) => l.rel === r[0]); if (!g.length) return;
    const names = [...new Set(g.map((l) => l.n))];
    h.push('<p style="margin-top:8px"><span class="sw" style="display:inline-block;background:' + RELC(r[0]) + ';margin-right:6px"></span><b>' + esc(r[1]) + '</b> (' + names.length + ')</p>');
    h.push('<p class="note">' + names.slice(0, 14).map((n) => '<a href="#" class="ent" data-n="' + n + '">' + esc(NET.nodes[n].name) + '</a>').join(", ") + (names.length > 14 ? " and " + (names.length - 14) + " more" : "") + '</p>');
    h.push('<details><summary>What the sources say</summary><ul>' + g.map((l) => srcItem(l, null)).join("") + (r[0] === "own" && k === "USA" ? '<li>' + esc(USA_OWN.trim()) + '</li>' : '') + '</ul></details>');
  });
  if (k === "USA" && NET.hist && NET.hist.length) h.push('<details><summary>Who owned the New York Fed at its founding, and its ties to London</summary><ul>' + NET.hist.map((x) => '<li>' + (x.kind === "confirmed" ? '<b>Confirmed:</b> ' : '<b>Claim per author, not confirmed by primary records:</b> ') + esc(x.claim) + ' <span class="note">' + link(x.source_title, x.source_url) + '</span></li>').join("") + '</ul></details>');
  h.push('<p class="note">Click a name to see everything tied to it on the map (this turns on "All documented ties" in the box at right).</p>');
  return h.join("");
}
function drawNetWin(w) {
  const okR = (l) => !S.netRel.size || S.netRel.has(l.rel);
  const rows = NET.nodes.map((nd, n) => { const ls = linksOfNode(n).filter(okR); return { n, nd, ls, cbs: new Set(ls.filter((l) => l.cb).map((l) => l.cb)).size, rels: [...new Set(ls.map((l) => l.rel))] }; }).filter((r) => r.ls.length).sort((a, b) => b.cbs - a.cbs || b.ls.length - a.ls.length || a.nd.name.localeCompare(b.nd.name));
  const multi = rows.filter((r) => r.cbs > 1), mixed = rows.filter((r) => r.rels.length > 1);
  w.body.innerHTML = '<div style="padding:10px 14px"><p class="mean" style="margin:0 0 8px">' + rows.length + ' parties tied to central banks. ' + multi.length + ' are tied to more than one central bank; ' + mixed.length + ' are tied in more than one way (for example owning shares and also employing former officials). Sorted by how many central banks each is tied to. Click a row to see its ties on the map.</p>' +
    '<table class="all"><colgroup><col style="width:26%"><col style="width:12%"><col style="width:7%">' + REL.map(() => '<col>').join("") + '</colgroup><thead><tr><th>Party</th><th>Based in</th><th>Central banks</th>' + REL.map((r) => '<th title="' + esc(r[1]) + '"><span class="sw" style="display:inline-block;background:' + RELC(r[0]) + '"></span> ' + esc(r[1].split(/[,:]/)[0]) + '</th>').join("") + '</tr></thead><tbody>' +
    rows.map((r) => '<tr class="r' + (S.ent === r.n ? " sel" : "") + '" data-n="' + r.n + '"><td style="white-space:normal;min-width:180px;max-width:340px">' + esc(r.nd.name) + '</td><td style="white-space:normal">' + esc(P[r.nd.iso3] ? P[r.nd.iso3].n : (r.nd.iso3 || "")) + '</td><td>' + r.cbs + '</td>' + REL.map((x) => { const c = r.ls.filter((l) => l.rel === x[0]).length; return '<td>' + (c || '<span class="mute">–</span>') + '</td>'; }).join("") + '</tr>').join("") + '</tbody></table></div>';
  w.body.querySelectorAll("tr.r").forEach((tr) => tr.addEventListener("click", () => { if (!S.net) showAllTies(); selectEntity(+tr.dataset.n); }));
  w.foot.textContent = "Counts only the kinds ticked under 'Who central banks answer to' (all kinds when none are ticked). Ties come from the sources linked in each party's box.";
}

/* ---------- paint ---------- */
function paint() {
  if (!map.getLayer("c-fill")) return;
  const l = layer(), d = l.kind === "seq" ? dom(l) : null, m = ["match", ["get", "iso3"]];
  ISOS.forEach((k) => { m.push(k, colorOf(l, l.get(P[k], S.year), d)); });
  m.push(NODATA);
  map.setPaintProperty("c-fill", "fill-color", m);
  map.setPaintProperty("c-dots", "circle-color", m);
  const plain = S.layer === "none";
  map.setPaintProperty("c-fill", "fill-opacity", plain ? 0 : ["interpolate", ["linear"], ["zoom"], 0, 0.82, 5, 0.7, 8, 0.45]);
  map.setPaintProperty("c-dots", "circle-opacity", plain ? 0 : 1); map.setPaintProperty("c-dots", "circle-stroke-opacity", plain ? 0 : 1);
  map.setPaintProperty("c-line", "line-opacity", plain ? 0.25 : 0.8);
  const sel = S.sel ? [S.sel] : [], grp = S.sel && P[S.sel] && P[S.sel].u ? (D.UM[P[S.sel].u] || []).filter((x) => x !== S.sel) : [];
  map.setFilter("c-sel", ["in", ["get", "iso3"], ["literal", sel]]);
  map.setFilter("c-grp", ["in", ["get", "iso3"], ["literal", grp]]);
  drawLinks(); drawNet(); drawPattern();
}

/* ---------- the key ---------- */
/* ---------- the box at right: who each bank answers to, and the patterns behind the scenes ---------- */
const SIDE_GROUPS = ["Who central banks answer to", "Patterns behind the scenes"];
const sideLayer = (id) => { const l = L.find((x) => x.id === id); return !!l && SIDE_GROUPS.includes(l.group); };
const ALLREL = () => new Set(REL.map((r) => r[0]));
const REL_SHORT = { own: "Who owns it: shareholders and governance seats", corrupt: "Paid, bribed, or got money, favors or leaks from it", people: "Shares its people: revolving door, board seats, forum members", inst: "Belongs to the same institutions: BIS, Financial Stability Board", control: "Pressured, fired, prosecuted or froze its money", service: "Other ties: named in a case, prints its money, audits or manages funds", account: "Investigated, charged or tried its officials" };
function clearCache() { CACHE_V.clear(); CACHE_D.clear(); }
function setNet(on) { S.net = !!on; if (!S.net && S.ent != null) { S.ent = null; $("#det").classList.remove("open"); } }
// What colors the countries while kinds are ticked: the owner type when only ownership is ticked, otherwise the count of ticked ties.
function netColorLayer() { return S.netRel.size === 1 && S.netRel.has("own") ? "own" : "tiesSel"; }
function applyNet() {
  clearCache();
  if (S.netRel.size) { setNet(true); S.layer = netColorLayer(); }
  else { setNet(false); if (S.layer === "tiesSel" || S.layer === "own") S.layer = S.mainLayer || "all"; }
  syncSelect(); update();
}
function toggleKind(k) { if (S.netRel.has(k)) S.netRel.delete(k); else S.netRel.add(k); applyNet(); }
function setKinds(set) { S.netRel = set; applyNet(); }
function choosePattern(id) {
  S.netRel = new Set(); setNet(false); clearCache();
  S.layer = S.layer === id ? (S.mainLayer || "all") : id;
  syncSelect(); update();
}
function syncSelect() { const sel = $("#layer"); if (sel) sel.value = sideLayer(S.layer) ? "" : S.layer; }
function showAllTies() { if (!S.net) setKinds(ALLREL()); }
const relSw = (kind) => '<span class="sw ' + (RELDASH[kind] ? 'dash" style="border-top-style:' + (RELDASH[kind] === "dot" ? "dotted" : "dashed") + ';border-color:' : 'ln" style="background:') + RELC(kind) + '"></span>';
function sideKey() {
  if (!S.netRel.size) return '<p class="note" style="margin:4px 0 2px">Nothing ticked: no parties are drawn.</p>';
  const l = L.find((x) => x.id === S.layer), own = S.layer === "own";
  let h = '<div class="skey"><div class="psec" style="margin-top:2px">What the map shows now</div>';
  if (own) h += '<p class="ldesc"><b>Countries</b> are colored by the type of owners their central bank has (key at left).</p>';
  else { const d = dom(l), r = ramp(); h += '<p class="ldesc"><b>Countries</b> are shaded by how many ties of the ticked kinds their central bank has: from ' + fmt(d[0], 0) + ' (dark) to ' + fmt(d[1], 0) + ' (light). Dark grey: none found.</p><div class="ramp">' + r.map((c) => '<span style="background:' + c + '"></span>').join("") + '</div>'; }
  h += '<p class="ldesc" style="margin-top:6px"><b>Diamonds</b> are the outside parties at their head offices, colored by their main kind of tie; larger ones are tied to more central banks. Several at one address fan out around it.</p>';
  h += '<p class="ldesc"><b>Lines</b> join each party to each central bank it is tied to, one line per pair, colored by the main kind of tie between them. Point at a diamond or line to light up its ties and countries; click for what they mean.</p></div>';
  return h;
}
function buildSide() {
  const open = (g) => !!S.sideOpen[g];
  const counts = {}; NET.links.forEach((x) => { counts[x.rel] = (counts[x.rel] || 0) + 1; });
  const ans = '<p class="ldesc">The outside people, companies, governments and bodies that central banks have answered to or dealt with: their shareholders, those who bribed them or were paid by them, firms that hired their officials, governments that pressured them or froze their money, and others. Tick one or more kinds of tie. The countries are colored by them and the parties and ties are drawn on the map. A tie is not by itself an accusation.</p>' +
    '<div id="sideKey">' + sideKey() + '</div>' +
    '<div class="sbtns" style="margin-top:8px"><button type="button" class="btn" data-k="all">Tick all</button><button type="button" class="btn" data-k="none">Clear</button></div>' +
    REL.map((r) => '<label class="srow' + (S.netRel.has(r[0]) ? ' on' : '') + '" title="' + esc(REL_DESC[r[0]]) + '"><input type="checkbox" data-kind="' + r[0] + '"' + (S.netRel.has(r[0]) ? ' checked' : '') + '>' + relSw(r[0]) + '<span>' + esc(REL_SHORT[r[0]]) + '</span><span class="n">' + (counts[r[0]] || 0) + '</span></label>').join("");
  const pats = '<p class="ldesc">Pick one to color the countries by their role in it and draw its connections. Its summary, what it means, timeline and sources appear in the box at left. Click it again to turn it off.</p>' +
    L.filter((l) => l.group === "Patterns behind the scenes").map((l) => '<button type="button" class="srow' + (S.layer === l.id ? ' on' : '') + '" data-pat="' + l.id + '"><span class="sw" style="background:var(--accent-hi);opacity:.75"></span><span>' + esc(l.label) + '</span></button>').join("");
  const body = { "Who central banks answer to": ans, "Patterns behind the scenes": pats };
  $("#sideBody").innerHTML = SIDE_GROUPS.map((g) => '<div class="sgrp' + (open(g) ? '' : ' min') + '" data-g="' + esc(g) + '"><button type="button" class="shead" aria-expanded="' + open(g) + '">' + esc(g) + '<span class="arr">' + (open(g) ? "▴" : "▾") + '</span></button><div class="sbody">' + body[g] + '</div></div>').join("");
  $("#sideBody").querySelectorAll(".shead").forEach((b) => b.addEventListener("click", () => { const g = b.parentNode.dataset.g; S.sideOpen[g] = !S.sideOpen[g]; buildSide(); }));
  $("#sideBody").querySelectorAll("[data-kind]").forEach((c) => c.addEventListener("change", () => toggleKind(c.dataset.kind)));
  $("#sideBody").querySelectorAll("[data-k]").forEach((b) => b.addEventListener("click", () => setKinds(b.dataset.k === "all" ? ALLREL() : new Set())));
  $("#sideBody").querySelectorAll("[data-pat]").forEach((b) => b.addEventListener("click", () => choosePattern(b.dataset.pat)));
}
function markSide() {
  $("#sideBody").querySelectorAll("[data-kind]").forEach((c) => { c.checked = S.netRel.has(c.dataset.kind); c.parentNode.classList.toggle("on", c.checked); });
  $("#sideBody").querySelectorAll("[data-pat]").forEach((b) => b.classList.toggle("on", b.dataset.pat === S.layer));
  const k = $("#sideKey"); if (k) k.innerHTML = sideKey();
}
function buildKey() {
  const groups = [...new Set(L.map((l) => l.group))].filter((g) => !SIDE_GROUPS.includes(g));
  $("#keyBody").innerHTML =
    '<div class="psec" style="margin-top:0">Color the countries by</div>' +
    '<select id="layer" aria-label="What to color the countries by">' + groups.map((g) => '<optgroup label="' + esc(g) + '">' + L.filter((l) => l.group === g).map((l) => '<option value="' + l.id + '">' + esc(l.label.trim()) + '</option>').join("") + '</optgroup>').join("") + '<option value="" disabled hidden>Chosen in the box at right</option></select>' +
    '<div id="ldesc"></div><div id="legend"></div><div id="yrs"></div>' +
    '<div class="psec">Lines</div>' +
    '<div class="lrow"><label class="chk"><input type="checkbox" id="swOn"> Swap lines between central banks</label><button type="button" class="ib" data-i="swI" title="What is this?" aria-label="About swap lines">i</button></div>' +
    '<div class="ipop" id="swI">A swap line lets one central bank borrow another\'s currency on demand, handing over its own as security, and swap back later. The lending bank picks who gets one. The Federal Reserve keeps standing lines with five central banks (Canada, England, Japan, the ECB, Switzerland); in a dollar shortage they can get dollars and others cannot. Lines in force are drawn; lapsed ones are listed in each country\'s box.</div><div id="swLeg"></div>' +
    '<div class="lrow"><label class="chk"><input type="checkbox" id="anOn"> Ties to anchor currencies</label><button type="button" class="ib" data-i="anI" title="What is this?" aria-label="About anchor ties">i</button></div>' +
    '<div class="ipop" id="anI">Many countries hold their currency fixed to, or within a band of, another one. To keep it there, their central bank has to follow the interest-rate moves of the bank that issues the anchor, so a decision in Washington or Frankfurt changes borrowing costs in their country. Solid lines: pegged or held in a band. Dashed: the country floats, but its rate is measured against that currency.</div><div id="anLeg"></div>' +
    '<div class="psec">Find a place</div><input id="find" type="search" placeholder="Country or central bank"><div id="plist" class="scroll"></div>';
  $("#layer").value = sideLayer(S.layer) ? "" : S.layer;
  $("#layer").addEventListener("change", (e) => { S.layer = S.mainLayer = e.target.value; S.netRel = new Set(); setNet(false); clearCache(); update(); });
  $("#swOn").addEventListener("change", (e) => { S.swaps = e.target.checked; update(); });
  $("#anOn").addEventListener("change", (e) => { S.anchors = e.target.checked; update(); });
  $("#keyBody").querySelectorAll(".ib").forEach((b) => b.addEventListener("click", () => { const el = $("#" + b.dataset.i); el.classList.toggle("open"); b.classList.toggle("on", el.classList.contains("open")); }));
  $("#find").addEventListener("input", (e) => { S.q = e.target.value.toLowerCase(); drawList(); });
}
function patExtra(pt) {
  const h = [];
  if (pt.implications) h.push('<div class="psec">What this means</div><p class="ldesc">' + esc(pt.implications) + '</p>');
  if (pt.series && pt.series.length) {
    const s = pt.series, mx = Math.max(...s.map((x) => x.value), 1), W = 300, H = 70, bw = W / s.length;
    h.push('<div class="psec">' + esc(s[0].label || "Count per year") + '</div><svg viewBox="0 0 ' + W + ' ' + (H + 14) + '" style="width:100%;display:block">' + s.map((x, i) => '<rect x="' + (i * bw + 0.5).toFixed(1) + '" y="' + (H - H * x.value / mx).toFixed(1) + '" width="' + Math.max(1, bw - 1).toFixed(1) + '" height="' + (H * x.value / mx).toFixed(1) + '" rx="1" fill="var(--accent-hi)"><title>' + x.year + ': ' + x.value + '</title></rect>').join("") + '<text x="0" y="' + (H + 12) + '" fill="#a3a1b4" font-size="10">' + s[0].year + '</text><text x="' + W + '" y="' + (H + 12) + '" text-anchor="end" fill="#a3a1b4" font-size="10">' + s[s.length - 1].year + '</text></svg>' + (pt.series_note ? '<p class="lsrc">' + esc(pt.series_note) + '</p>' : ''));
  }
  if (pt.links && pt.links.length) h.push('<div class="psec">Connections drawn</div>' + pt.links.map((k) => '<div class="lg" style="display:block">' + esc(k.from) + ' → ' + esc(k.to) + (k.label ? ': ' + esc(k.label) : '') + (k.years ? ' <span class="n">' + esc(k.years) + '</span>' : '') + '</div>').join(""));
  if (pt.timeline && pt.timeline.length) h.push('<div class="psec">Timeline</div>' + pt.timeline.slice().sort((x, y) => x.year - y.year).map((t) => '<div class="lg" style="display:block"><b>' + t.year + '</b> ' + esc(t.event) + (t.source_url ? ' <a href="' + esc(t.source_url) + '" target="_blank" rel="noopener">source</a>' : '') + '</div>').join(""));
  if (pt.claims_per_author && pt.claims_per_author.length) h.push('<div class="psec">Claims by authors, not confirmed</div>' + pt.claims_per_author.map((c) => '<div class="lg" style="display:block">' + esc(c.claim) + ' <span class="n">' + link(c.author_work, c.url) + '</span></div>').join(""));
  if (pt.uncertain) h.push('<p class="lsrc" style="margin-top:6px"><b>Unproven:</b> ' + esc(pt.uncertain) + '</p>');
  if (pt.confirmed_by && pt.confirmed_by.length) h.push('<p class="lsrc">Sources: ' + pt.confirmed_by.map((c) => link(c.title, c.url)).join(" · ") + '</p>');
  return h.join("");
}
function drawLegend() {
  const l = layer();
  if (l.id === "none") { $("#ldesc").innerHTML = '<p class="ldesc">' + esc(l.desc) + '</p>'; $("#legend").innerHTML = ""; $("#yrs").innerHTML = ""; drawLinesLegend(); return; }
  $("#ldesc").innerHTML = '<p class="ldesc">' + esc(l.desc) + '</p>' + (l.src || l.id === "gold" ? '<p class="lsrc">Source: ' + esc(l.id === "gold" ? (D.META.gold || "") : l.src) + '</p>' : "");
  const rs = ISOS.map((k) => [k, l.get(P[k], S.year)]);
  const nod = rs.filter(([, r]) => !r || (l.kind === "seq" && r.v == null)).length;
  let h = "";
  if (l.kind === "seq") {
    const d = dom(l), r = ramp();
    h += '<div class="ramp">' + r.map((c) => '<span style="background:' + c + '"></span>').join("") + '</div>' +
      '<div class="rampl"><span>' + l.f(d[0]) + (l.dom ? "" : " (lowest)") + '</span>' + (l.log ? '<span>spaced by powers of ten</span>' : '') + '<span>' + l.f(d[1]) + (Array.isArray(l.dom) ? "" : " (highest)") + '</span></div>';
  } else {
    l.classes.forEach((c, i) => { const n = rs.filter(([, r]) => r && r.v === c[0]).length; h += '<div class="lg"><span class="sw" style="background:' + CATC[i] + '"></span>' + esc(c[1]) + '<span class="n">' + n + '</span></div>'; });
    h += '<div class="lg"><span class="sw" style="background:' + OTHER + '"></span>' + esc(l.other) + '<span class="n">' + rs.filter(([, r]) => r && r.other).length + '</span></div>';
  }
  h += '<div class="lg"><span class="sw" style="background:' + NODATA + ';outline:1px solid #555"></span>' + (l.id === "tiesSel" ? "None of the ticked kinds found" : l.kind === "cat" && l.id !== "reg" && l.id !== "anc" ? "No information" : "No figure from this source") + '<span class="n">' + (l.kind === "cat" ? rs.filter(([, r]) => !r).length : nod) + '</span></div>';
  if (rs.some(([, r]) => r && r.via)) h += '<p class="lsrc" style="margin-top:5px">Places in a currency union, or using another country\'s currency, show the figure of the bank or currency they rely on; their boxes say so.</p>';
  $("#legend").innerHTML = h;
  $("#yrs").innerHTML = l.years ? '<div class="tline"><input type="range" id="yr" min="' + l.years[0] + '" max="' + l.years[1] + '" step="1" value="' + Math.min(Math.max(S.year, l.years[0]), l.years[1]) + '" aria-label="Year"' + (S.latest ? " disabled" : "") + '><b id="yrv">' + (S.latest ? "latest" : S.year) + '</b></div><label class="chk"><input type="checkbox" id="lat"' + (S.latest ? " checked" : "") + '> Each place\'s latest year</label>' : "";
  if (l.years) {
    $("#yr").addEventListener("input", (e) => { S.year = +e.target.value; $("#yrv").textContent = S.year; paint(); drawList(); drawLegendCounts(); drawCharts(); });
    $("#lat").addEventListener("change", (e) => { S.latest = e.target.checked; if (!S.latest) S.year = Math.min(Math.max(S.year, l.years[0]), l.years[1]); update(); });
  }
  drawLinesLegend();
  drawLegendCounts();
  if (l.pat) $("#legend").insertAdjacentHTML("beforeend", patExtra(l.pat));
}
function drawLinesLegend() {
  $("#swLeg").innerHTML = S.swaps ? PROV.map((x, i) => '<div class="lg"><span class="sw ln" style="background:' + CATC[i] + '"></span>Lent by the ' + esc(x[1]) + '</div>').join("") + '<div class="lg"><span class="sw ln" style="background:' + CATC[3] + '"></span>Lent by other central banks</div>' : "";
  $("#anLeg").innerHTML = S.anchors ? '<div class="lg"><span class="sw ln" style="background:' + CATC[0] + '"></span>US dollar</div><div class="lg"><span class="sw ln" style="background:' + CATC[1] + '"></span>Euro</div><div class="lg"><span class="sw ln" style="background:' + CATC[2] + '"></span>Rand, rupee, Australian or Singapore dollar, renminbi, Swiss franc</div><div class="lg"><span class="sw dash" style="border-color:#c9c6d6"></span>Dashed: floats against it</div>' : "";
  if ($("#netLeg")) $("#netLeg").innerHTML = S.net ? REL.map((r) => { const c = NET.links.filter((l) => l.rel === r[0]).length; return c ? '<label class="lg" style="cursor:pointer"><input type="checkbox" data-rel="' + r[0] + '"' + (S.netRel.has(r[0]) ? ' checked' : '') + '><span class="sw ' + (RELDASH[r[0]] ? 'dash" style="border-top-style:' + (RELDASH[r[0]] === "dot" ? "dotted" : "dashed") + ';border-color:' : 'ln" style="background:') + RELC(r[0]) + '"></span>' + esc(r[1]) + '<span class="n">' + c + '</span></label>' : ""; }).join("") : "";
  if ($("#netLeg")) $("#netLeg").querySelectorAll("[data-rel]").forEach((cb) => cb.addEventListener("change", () => { if (cb.checked) S.netRel.add(cb.dataset.rel); else S.netRel.delete(cb.dataset.rel); drawNet(); drawCharts(); }));
}
function drawLegendCounts() {
  const l = layer(), n = ISOS.filter((k) => { const r = l.get(P[k], S.year); return r && (r.v != null || r.other); }).length;
  const c = $("#cnt") || Object.assign(document.createElement("div"), { id: "cnt" }); $("#legend").appendChild(c);
  c.textContent = n + " of " + ISOS.length + " places have a value" + (l.years && !S.latest ? " in " + S.year : "") + ".";
}
function drawList() {
  const l = layer();
  const rows = ISOS.map((k) => [k, l.get(P[k], S.year)]).filter(([k]) => !S.q || P[k].n.toLowerCase().includes(S.q) || (P[k].cb || "").toLowerCase().includes(S.q));
  if (l.kind === "seq") rows.sort((a, b) => ((b[1] && b[1].v != null ? b[1].v : -1e9) - (a[1] && a[1].v != null ? a[1].v : -1e9)) || P[a[0]].n.localeCompare(P[b[0]].n));
  $("#plist").innerHTML = rows.map(([k, r]) => '<div class="pi' + (S.sel === k ? " sel" : "") + '" data-k="' + k + '"><span class="sw" style="background:' + colorOf(l, r, l.kind === "seq" ? dom(l) : null) + '"></span>' + esc(P[k].n) + '<span class="v">' + (r && r.v != null ? (l.kind === "seq" ? l.f(r.v) : "") : "") + '</span></div>').join("");
  $("#plist").querySelectorAll(".pi").forEach((el) => el.addEventListener("click", () => select(el.dataset.k, true)));
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

/* ---------- a place's box ---------- */
function bars(names, vals, max, f) { return '<div class="bars">' + names.map((n, i) => '<span>' + esc(n) + '</span><span class="b"><i style="width:' + (vals[i] == null ? 0 : 100 * vals[i] / max) + '%"></i></span><span>' + (vals[i] == null ? "–" : f(vals[i])) + '</span>').join("") + '</div>'; }
function spark(series, lo, hi, label) {
  const s = series.filter(Boolean); if (!s.length) return "";
  let y0 = Infinity, y1 = -Infinity; s.forEach((x) => { y0 = Math.min(y0, x.s[0]); y1 = Math.max(y1, x.s[0] + x.s.length - 2); });
  const W = 300, H = 52, X = (y) => 4 + (W - 8) * (y - y0) / Math.max(1, y1 - y0), Y = (v) => H - 12 - (H - 18) * (v - lo) / (hi - lo);
  let g = '<line x1="4" x2="' + (W - 4) + '" y1="' + Y(lo) + '" y2="' + Y(lo) + '" class="gl" stroke="rgba(255,255,255,.12)"/>';
  s.forEach((x) => { let d = "", pen = false; x.s.slice(1).forEach((v, i) => { if (v == null) { pen = false; return; } d += (pen ? "L" : "M") + X(x.s[0] + i).toFixed(1) + " " + Y(v).toFixed(1); pen = true; }); g += '<path d="' + d + '" fill="none" stroke="' + x.c + '" stroke-width="1.6" stroke-linejoin="round"/>'; });
  g += '<text x="4" y="' + (H - 1) + '" fill="#a3a1b4" font-size="10">' + y0 + '</text><text x="' + (W - 4) + '" y="' + (H - 1) + '" text-anchor="end" fill="#a3a1b4" font-size="10">' + y1 + '</text>';
  return '<div class="spk"><svg viewBox="0 0 ' + W + ' ' + H + '" preserveAspectRatio="none">' + g + '</svg></div>' + (label ? '<p class="note">' + label + '</p>' : "");
}
const link = (t, u) => u ? '<a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(t || u) + '</a>' : esc(t);
function rankOf(id, k) { const was = S.latest; S.latest = true; try { return rankOf0(id, k); } finally { S.latest = was; } }
function rankOf0(id, k) {
  const l = L.find((x) => x.id === id), seen = new Set(), vals = [];
  ISOS.forEach((i) => { const r = l.get(P[i], 9999); if (r && r.v != null) { const key = r.via || i; if (!seen.has(key)) { seen.add(key); vals.push([key, r.v]); } } });
  vals.sort((a, b) => b[1] - a[1]);
  const me = l.get(P[k], 9999); if (!me || me.v == null) return "";
  const key = me.via || k, i = vals.findIndex((x) => x[0] === key);
  return i < 0 ? "" : ' <span class="note">(' + (i + 1) + ' of ' + vals.length + ')</span>';
}
function detail(k) {
  const p = P[k], u = uni(p), A = D.ARR, h = [];
  h.push('<div class="hp-k">' + esc(p.cb || "Central bank") + '</div><h3>' + esc(p.n) + '</h3>');
  const cu = (p.cur || []).map((c) => esc(c) + (CUR[c] ? " (" + esc(CUR[c].name) + ")" : "")).join(", ");
  h.push('<p class="hp-sub">' + (cu ? "Currency: " + cu : "No currency listed") + (u ? '<br>Monetary policy set by ' + esc(CB_NAMES[p.u]) + ' for ' + (D.UM[p.u] || []).length + ' members (outlined).' : '') + '</p>');
  const as = allScore(p), G = groups(p);
  h.push('<div class="hp-h">Ulterior influence, all around</div>');
  if (as) {
    h.push('<p><span class="big">' + fmt(as.v, 0) + '</span> of 100' + rankOf("all", k) + ' <span class="note">· 0 = shielded, 100 = fully exposed</span></p>');
    { const pr = plainRank(L.find((x) => x.id === "all"), as); const gs = G.map((x) => [x[0], avg(x[1].map((y) => y[1]))]).sort((x, y) => y[1] - x[1]);
      const worst = gs[0], wp = G.find((x) => x[0] === worst[0])[1].slice().sort((x, y) => y[1] - x[1]).filter((y) => y[1] > 0).slice(0, 2).map((y) => y[0].toLowerCase());
      h.push('<p>' + (pr ? pr[0].toUpperCase() + pr.slice(1) + '. ' : '') + 'Its weakest side is ' + esc(worst[0].toLowerCase()) + (wp.length ? ', mainly ' + esc(wp.join(' and ')) : '') + '.</p>'); }
    h.push(bars(G.map((x) => x[0]), G.map((x) => avg(x[1].map((y) => y[1]))), 1, (v) => fmt(v * 100, 0)));
    h.push('<details><summary>What each group is made of</summary><table class="kv">' + G.map((x) => '<tr><th colspan="2" style="color:var(--accent-hi);padding-top:6px">' + esc(x[0]) + '</th></tr>' + x[1].map((y) => '<tr><th>' + esc(y[0]) + '<br><span class="note">' + esc(y[2]) + '</span></th><td>' + fmt(y[1] * 100, 0) + '</td></tr>').join("")).join("") + '</table></details>');
  } else h.push('<p class="note">Not scored: fewer than two of outside influence, inside influence, and corruption and secrecy around it have data for this place.</p>');
  // corruption inside and around
  const ccs = (p.cc || []).map((i) => D.CC[i]).sort((a, b) => String(b.years).localeCompare(String(a.years)));
  const rds = (p.rd || []).map((i) => D.RD[i]);
  h.push('<div class="hp-h">Corruption inside and around the bank</div>');
  const crow = [];
  if (p.cpi) crow.push(['Corruption Perceptions Index 2025', fmt(p.cpi.v, 0) + ' of 100' + rankOf("cpi", k).replace("(", "(clean rank ")]);
  if (p.wgi) crow.push(['World Bank control of corruption, ' + p.wgi.y, fmt(p.wgi.v, 0) + ' of 100']);
  if (p.aml) crow.push(['Money-laundering risk, Basel AML 2025', fmt(p.aml.v, 2) + ' of 10 (rank ' + p.aml.rank + ' of 177, 1 = riskiest)']);
  if (p.fsi) crow.push(['Financial secrecy, FSI 2025', fmt(p.fsi.score, 1) + ' of 100 · rank ' + p.fsi.rank + ' of 141 · ' + fmt(p.fsi.share, 2) + '% of world secrecy']);
  if (crow.length) h.push('<table class="kv">' + crow.map((x) => '<tr><th>' + x[0] + '</th><td>' + x[1] + '</td></tr>').join("") + '</table>');
  if (p.cpi) h.push(spark([{ s: p.cpi.s, c: "#c9c3ee" }], 0, 100, "Corruption Perceptions Index, 2012–2025, 0 to 100"));
  if (ccs.length) h.push('<p style="margin-top:8px"><b>' + ccs.length + '</b> documented case' + (ccs.length > 1 ? 's' : '') + ' at the central bank' + (p.u === "ECB" && ccs.some((c) => c.iso3 === "EMU") ? ' (including the ECB)' : '') + ':</p><ul>' + ccs.map((c) => '<li><b>' + esc(c.years) + '</b> · ' + esc(c.category) + ' · <i>' + esc(c.status) + '</i>. ' + esc(c.summary) + ' <span class="note">' + link(c.source_title, c.source_url) + (c.weak_source ? ' (Wikipedia)' : '') + (c.update_url ? ' · ' + link(c.update_title, c.update_url) : '') + '</span></li>').join("") + '</ul>');
  else h.push('<p class="note">No documented case at the central bank was found. That is not proof none happened.</p>');
  if (rds.length) h.push('<details><summary>' + rds.length + ' move' + (rds.length > 1 ? 's' : '') + ' between the bank and private finance or politics</summary><ul>' + rds.map((c) => '<li>' + esc(c.people || "") + ': ' + esc(c.move || "") + '. ' + esc(c.summary || "") + ' <span class="note">' + link(c.source_title, c.source_url) + '</span></li>').join("") + '</ul></details>');
  const cr = (p.crises || []).slice().sort((a, b) => b.start - a.start);
  if (cr.length) h.push('<details><summary>' + cr.length + ' systemic banking crisis' + (cr.length > 1 ? 'es' : '') + ' since 1970</summary><table class="kv"><tr><th>Years</th><td>Public cost · central bank lending to banks</td></tr>' + cr.map((c) => '<tr><th>' + c.start + '–' + (c.end || '') + (c.border ? ' (borderline)' : '') + '</th><td>' + (c.fis == null ? 'cost not given' : fmt(c.fis, 1) + '% of GDP') + ' · ' + (c.liq == null ? '–' : fmt(c.liq, 1) + '% of deposits') + '</td></tr>').join("") + '</table></details>');
  // law
  const r = p.r, g = p.g;
  h.push('<div class="hp-h">Independence written into law</div>');
  if (r) {
    h.push('<p><span class="big">' + fmt(r.i, 3) + '</span> of 1 on Romelli\'s 42 rules' + rankOf("cbie", k) + ' <span class="note">· law as of ' + r.y + ', last changed ' + r.chg + '</span></p>');
    h.push(bars(DIM6, r.d, 1, (v) => fmt(v, 2)));
    const QL = D.QL; let qi = 0, rows = "";
    const parts = [[0, 14], [1, 5], [2, 0], [3, 8], [4, 12], [5, 2]];
    parts.forEach(([di, n]) => {
      rows += '<tr><th colspan="2" style="color:var(--accent-hi);padding-top:6px">' + DIM6[di] + '</th></tr>';
      if (di === 2) rows += '<tr><th>' + esc(QL.obj) + '</th><td>' + fmt(r.d[2], 2) + '</td></tr>';
      for (let j = 0; j < n; j++, qi++) rows += '<tr><th>' + esc(QL.q[qi]) + '</th><td>' + (r.q[qi] == null ? "–" : fmt(r.q[qi], 2)) + '</td></tr>';
    });
    h.push('<details><summary>All 42 rules, each scored 0 (government holds the power) to 1 (bank holds it)</summary><table class="kv">' + rows + '</table></details>');
  }
  if (g) h.push('<p style="margin-top:8px"><span class="big">' + fmt(g.w, 3) + '</span> of 1 on the Cukierman method (Garriga)' + rankOf("cwn", k) + ' <span class="note">· ' + g.y + (g.cr ? ' · bank created ' + g.cr : '') + ' · ' + g.nref + ' reforms since 1970 (' + g.up + ' raised, ' + g.down + ' lowered independence)</span></p>' + bars(DIM4, g.d, 1, (v) => fmt(v, 2)));
  if (p.rs || p.gs) h.push(spark([p.rs && { s: p.rs, c: "#c9c3ee" }, p.gs && { s: p.gs, c: "#7fb0a8" }], 0, 1, (p.rs ? '<span style="color:#c9c3ee">— Romelli</span> ' : '') + (p.gs ? '<span style="color:#7fb0a8">— Garriga</span>' : '') + ', 0 to 1'));
  if (!r && !g) h.push('<p class="note">Neither index codes this place' + (u && (u.r) ? '; ' + esc(CB_NAMES[p.u]) + ' scores ' + fmt(u.r.i, 3) + ' on Romelli\'s index.' : '.') + '</p>');
  if (u && u.r && p.u === "ECB") h.push('<p class="note">The European Central Bank itself scores ' + fmt(u.r.i, 3) + ' on Romelli\'s index (' + u.r.y + ').</p>');
  // openness
  const t = own(p, "t");
  h.push('<div class="hp-h">What it tells the public</div>');
  if (t) h.push('<p><span class="big">' + fmt(t.o.ti, 1) + '</span> of 15' + rankOf("ti", k) + ' <span class="note">· ' + t.o.y + (t.via ? ' · ' + esc(CB_NAMES[t.via]) + '\'s score' : '') + '</span></p>' + bars(DIM5, t.o.d, 3, (v) => fmt(v, 1)) + spark([{ s: (t.via ? u.ts : p.ts), c: "#c9c3ee" }], 0, 15, "Transparency, 0 to 15"));
  else h.push('<p class="note">Not scored.</p>');
  // pressure
  h.push('<div class="hp-h">Pressure in practice</div>');
  const pr = own(p, "p");
  if (pr) { const o = pr.o; h.push('<p>Government pressure reported in <b>' + o.n + '</b> of ' + o.q + ' quarters, 2010–2018' + (pr.via ? ' (' + esc(CB_NAMES[pr.via]) + ')' : '') + '.' + (o.n ? ' Pressing to cut rates or ease: ' + o.ease + '; to tighten: ' + o.tight + '. Threats to replace leaders: ' + o.rep + '; to change the law: ' + o.leg + '; demands to print money: ' + o.print + '; in election periods: ' + o.elec + '.' : '') + '</p>'); }
  else h.push('<p class="note">Not covered by Binder\'s 2010–2018 survey.</p>');
  const ev = (p.ev || []).map((i) => D.EV[i]).sort((a, b) => String(b.date).localeCompare(String(a.date)));
  if (ev.length) h.push('<ul>' + ev.map((e) => '<li><b>' + esc(e.date) + '</b> · ' + esc(e.kind) + '. ' + esc(e.summary) + ' <span class="note">' + link(e.source_title, e.source_url) + '</span></li>').join("") + '</ul>');
  // ownership and arrangements
  if (p.own || (p.arr && p.arr.length) || p.f != null || p.a) {
    h.push('<div class="hp-h">Ownership and outside control</div>');
    if (p.own) { const o = p.own; h.push('<p>' + esc(o.owners) + (o.state_share_pct != null ? ' State share: ' + fmt(o.state_share_pct, 1) + '%.' : '') + (o.exchange ? ' Listed on: ' + esc(o.exchange) + '.' : '') + (o.dividend_or_profit_note ? ' ' + esc(o.dividend_or_profit_note) : '') + ' <span class="note">' + link(o.source_title, o.source_url) + (o.as_of ? ' · ' + esc(o.as_of) : '') + '</span></p>'); }
    (p.arr || []).forEach((i) => { const a = A[i]; h.push('<p><b>' + esc(a.name) + '</b> (' + esc(a.kind) + ')</p><ul>' + a.facts.map((x) => '<li>' + esc(x) + '</li>').join("") + '</ul><p class="note">' + a.sources.map((s) => link(s.title, s.url)).join(" · ") + '</p>'); });
    if (p.f != null || p.a) h.push('<p>Exchange rate, December 2025: ' + (p.f != null ? esc(D.REG[p.f]) : 'not classified') + (p.a ? '; measured against ' + esc(p.a === "n.a." ? "no anchor found" : p.a.replace("Freely_falling", "nothing (freely falling)")) : '') + '.</p>');
  }
  // reach
  h.push('<div class="hp-h">Reach beyond its borders</div>');
  const c = curOf(p), rows = [];
  if (c) {
    const via = c.iss !== k ? ' <span class="note">(' + esc(c.name) + ')</span>' : '';
    if (c.fx != null) rows.push(['Share of world currency trading, Apr 2025', fmt(c.fx, 2) + '%' + rankOf("fx", k) + via]);
    if (c.res != null) rows.push(['Share of foreign reserves, 2026 Q2', fmt(c.res, 2) + '%' + rankOf("res", k) + via]);
    if (c.pay != null) rows.push(['Share of Swift payments, Jun 2026', fmt(c.pay, 2) + '%' + rankOf("pay", k) + via]);
    if (c.users > 1) rows.push(['Places using this currency', String(c.users)]);
    if (c.tied && c.iss === k) rows.push(['Countries tied to its currency, Dec 2025', String(c.tied) + rankOf("tied", k)]);
  }
  const bs = own(p, "bs");
  if (bs && bs.o.usd != null) rows.push(['Total assets, end ' + bs.o.y, '$' + fmt(bs.o.usd, 1) + ' bn' + (bs.o.gdp != null ? ' · ' + fmt(bs.o.gdp, 1) + '% of GDP' : '') + (bs.via ? ' <span class="note">(' + esc(CB_NAMES[bs.via]) + ')</span>' : '')]);
  if (u && u.bs && u.bs.usd != null && p.u === "ECB") rows.push(['Eurosystem total assets, end ' + u.bs.y, '$' + fmt(u.bs.usd, 1) + ' bn']);
  if (p.gold) rows.push(['Gold', fmt(p.gold.t, 1) + ' tonnes' + (p.gold.pct != null ? ' · ' + fmt(p.gold.pct, 1) + '% of reserves' : '') + rankOf("gold", k)]);
  if (rows.length) h.push('<table class="kv">' + rows.map((x) => '<tr><th>' + x[0] + '</th><td>' + x[1] + '</td></tr>').join("") + '</table>');
  const sw = (p.sw || []).map((i) => D.SW[i]);
  if (sw.length) {
    const nm = (iso) => iso === "EMU" ? "European Central Bank" : (P[iso] ? P[iso].n : iso);
    h.push('<details' + (sw.length < 6 ? ' open' : '') + '><summary>' + sw.length + ' swap line' + (sw.length > 1 ? 's' : '') + (p.u === "ECB" && !(p.sw_own) ? ' (through the European Central Bank)' : '') + '</summary><ul>' + sw.map((s) => '<li>' + esc(nm(s.provider_iso3)) + ' → ' + esc(nm(s.counterparty_iso3)) + (s.two_way ? ' (both ways)' : '') + ': ' + esc(s.amount || "amount not stated") + (s.signed_or_renewed ? ', ' + esc(s.signed_or_renewed) : '') + (s.expires ? ', to ' + esc(s.expires) : '') + (s.status !== "active" ? ' [' + esc(s.status) + ']' : '') + ' <span class="note">' + link(s.source_title, s.source_url) + '</span></li>').join("") + '</ul></details>');
  }
  if (!rows.length && !sw.length) h.push('<p class="note">No reach figures published for this place.</p>');
  h.push(countryNet(k));
  h.push('<div class="hp-src">Sources are listed under About and sources. Figures are as each source publishes them; nothing has been dropped or adjusted.</div>');
  $("#detBody").innerHTML = h.join("");
  $("#detBody").querySelectorAll("a.ent").forEach((a) => a.addEventListener("click", (e) => { e.preventDefault(); if (!S.net) showAllTies(); selectEntity(+a.dataset.n); }));
}
function select(k, fly) {
  S.ent = null; S.sel = k; detail(k); $("#det").classList.add("open"); $("#det").scrollTop = 0;
  paint(); drawList(); drawCharts();
  const pi = $('#plist .pi[data-k="' + k + '"]'); if (pi && fly) { const pl = $("#plist"); pl.scrollTop = pi.offsetTop - pl.offsetTop - pl.clientHeight / 2; }
  // the box sits in the middle of the map, so the country is moved into the open space above it
  if (P[k].pt) { const r = $("#det").getBoundingClientRect(), H = map.getContainer().clientHeight, fb = freeBox();
    const padding = { left: fb.L, right: fb.R, top: 10, bottom: Math.max(0, Math.min(H - 120, H - r.top + 10)) };
    if (fly) map.flyTo({ center: P[k].pt, zoom: Math.max(map.getZoom(), proj === "globe" ? 2.4 : 3), padding, duration: 1000 });
    else map.easeTo({ center: P[k].pt, padding, duration: 700 }); }
}
function deselect() { S.sel = null; S.ent = null; $("#det").classList.remove("open"); paint(); drawList(); drawCharts(); }

/* ---------- chart windows ---------- */
const CHARTS = [["table", "Every place"], ["reach", "Reach compared"], ["time", "Independence in law, 1970–2023"], ["net", "Networks"]];
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
  // every chart window opens in the middle of the screen
  const small = innerWidth < 760, W = small ? innerWidth - 16 : Math.min(id === "table" || id === "net" ? 1400 : 1000, innerWidth - 40), H = small ? Math.min(560, innerHeight - 70) : Math.min(id === "table" || id === "net" ? 760 : 660, innerHeight - 60);
  Object.assign(el.style, { width: W + "px", height: H + "px", left: Math.max(8, (innerWidth - W) / 2) + "px", top: Math.max(8, (innerHeight - H) / 2) + "px", zIndex: ++zTop });
  cascade = (cascade + 1) % 4;
  const w = WINS[id] = { id, el, body: el.querySelector(".wb"), foot: el.querySelector(".wfoot"), sort: null, dir: -1 };
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
  let last = ""; w.ro = new ResizeObserver(() => { const kk = w.body.clientWidth + "x" + w.body.clientHeight; if (kk !== last) { last = kk; if (id === "time") drawWin(id); } }); w.ro.observe(w.body);
  $('#dockBtns [data-w="' + id + '"]').classList.add("on");
  drawWin(id);
}
function closeWin(id) { const w = WINS[id]; if (!w) return; w.ro.disconnect(); w.el.remove(); delete WINS[id]; tip(null); $('#dockBtns [data-w="' + id + '"]').classList.remove("on"); }
function drawCharts() { Object.keys(WINS).forEach(drawWin); }
function drawWin(id) { const w = WINS[id]; if (!w) return; if (id === "table") drawTable(w); else if (id === "reach") drawReach(w); else if (id === "net") drawNetWin(w); else drawTime(w); }

const TCOLS = [["n", "Place"], ["all", "Big picture (0–100)"], ["comp", "Outside (0–100)"], ["inside", "Inside (0–100)"], ["cc", "Inside cases"], ["cpi", "CPI (0–100)"], ["aml", "AML risk (0–10)"], ["fsi", "Secrecy (0–100)"], ["cbie", "Law (Romelli, 0–1)"], ["cwn", "Law (Garriga, 0–1)"], ["ti", "Transparency (0–15)"], ["press", "Pressure quarters"], ["ev", "Moves 2019–26"], ["own", "Owners"], ["arr", "Whose money"], ["reg", "Regime"], ["anc", "Anchor"], ["fx", "FX trading %"], ["res", "Reserves %"], ["pay", "Payments %"], ["bs", "Assets $bn"], ["gold", "Gold t"], ["swaps", "Swap lines"]];
function cellVal(id, k) {
  if (id === "n") return P[k].n;
  const l = L.find((x) => x.id === id), r = l.get(P[k], 9999);
  if (!r) return null;
  if (id === "anc") return P[k].a;
  if (id === "reg") return P[k].f != null ? ["", "Peg / none", "Crawl", "Managed", "Float", "Falling", "Dual"][COARSE[P[k].f]] : null;
  const SH = { own: { listed: "Listed", private: "Private, unlisted", mixed: "Other owners", "": "State" }, arr: { union: "Union", guarantee: "Foreign-backed", foreign: "Foreign currency", board: "Currency board", "": "Own" } };
  if (l.kind === "cat") return SH[id][r.v == null ? "" : r.v];
  return r.v;
}
function drawTable(w) {
  const keys = ISOS.slice(), s = w.sort;
  if (s) keys.sort((a, b) => { const x = cellVal(s, a), y = cellVal(s, b); if (x == null && y == null) return 0; if (x == null) return 1; if (y == null) return -1; return (typeof x === "number" ? x - y : String(x).localeCompare(String(y))) * w.dir; });
  const cell = (id, k) => { const v = cellVal(id, k); if (v == null) return '<span class="mute">–</span>'; if (typeof v !== "number") return esc(v); const l = L.find((x) => x.id === id); return id === "press" ? fmt(v, 0) + "%" : l.f(v).replace(" of 100", "").replace(/%$/, "").replace(/^\$/, "").replace(/ (bn|t)$/, ""); };
  w.body.innerHTML = '<table class="all"><colgroup><col style="width:120px">' + TCOLS.slice(1).map(() => '<col>').join("") + '</colgroup><thead><tr>' + TCOLS.map((c) => '<th data-c="' + c[0] + '"' + (s === c[0] ? ' class="on"' : '') + '>' + esc(c[1]) + (s === c[0] ? (w.dir > 0 ? " ▲" : " ▼") : "") + '</th>').join("") + '</tr></thead><tbody>' +
    keys.map((k) => '<tr class="r' + (S.sel === k ? " sel" : "") + '" data-k="' + k + '">' + TCOLS.map((c) => '<td>' + cell(c[0], k) + '</td>').join("") + '</tr>').join("") + '</tbody></table>';
  w.body.querySelectorAll("th").forEach((th) => th.addEventListener("click", () => { const c = th.dataset.c; if (w.sort === c) w.dir = -w.dir; else { w.sort = c; w.dir = c === "n" ? 1 : -1; } drawTable(w); }));
  w.body.querySelectorAll("tr.r").forEach((tr) => tr.addEventListener("click", () => select(tr.dataset.k, true)));
  w.foot.textContent = "Click a heading to sort, a row to open the place. Euro-area and other union members show their union bank's figures where they have none of their own.";
}
function drawReach(w) {
  const curs = Object.keys(CUR);
  const panel = (title, unit, rows, f, mean) => { rows = rows.filter((r) => r[1] != null).sort((a, b) => b[1] - a[1]); const max = Math.max(...rows.map((r) => r[1]), 1e-9);
    return '<div><h4>' + esc(title) + '</h4><div class="u">' + esc(unit) + '</div><p class="mean" style="margin:0 0 7px">' + mean + '</p><div class="hb">' + rows.map((r) => '<span title="' + esc(r[2] || r[0]) + '">' + esc(r[0]) + '</span><span class="b" title="' + esc(r[2] || r[0]) + '"><i style="width:' + (100 * r[1] / max) + '%;background:' + (r[3] ? "#f0ece4" : "var(--accent-hi)") + '"></i></span><span>' + f(r[1]) + '</span>').join("") + '</div></div>'; };
  const selCur = S.sel && curOf(P[S.sel]) ? curOf(P[S.sel]).code : null;
  const cr = (k) => curs.map((c) => [c, CUR[c][k], CUR[c].name, c === selCur]);
  const bsRows = [], goldRows = [], swRows = [];
  ISOS.forEach((k) => { const p = P[k]; if (p.bs && p.bs.usd != null && !p.u) bsRows.push([p.n, p.bs.usd, p.cb, S.sel === k]); if (p.gold) goldRows.push([p.n, p.gold.t, p.cb, S.sel === k]); });
  if (U.ECB && U.ECB.bs) bsRows.push(["Eurosystem", U.ECB.bs.usd, "European Central Bank and the 21 national banks", S.sel && P[S.sel].u === "ECB"]);
  const prov = {}; D.SW.forEach((s) => { if (s.status === "expired") return; prov[s.provider_iso3] = (prov[s.provider_iso3] || 0) + 1; });
  Object.keys(prov).forEach((k) => swRows.push([k === "EMU" ? "Euro area (ECB)" : (P[k] ? P[k].n : k), prov[k], "", S.sel === k]));
  const top = (rows, n) => rows.sort((a, b) => b[1] - a[1]).slice(0, n);
  w.body.innerHTML = '<div class="mult">' +
    panel("World currency trading", "% of daily turnover, April 2025 (sums to 200%)", cr("fx"), (v) => fmt(v, 2),
      "The interest rate a central bank sets moves the price of its currency in every trade it is part of. The dollar is on one side of 89% of trades, so Federal Reserve decisions reach almost every exchange rate.") +
    panel("Foreign reserves held", "% of allocated reserves, 2026 Q2", cr("res"), (v) => fmt(v, 2),
      "Governments keep savings in these currencies to defend their own. Holding them mostly means holding the issuer's government bonds, whose value rides on that issuer's central bank.") +
    panel("International payments", "% of Swift payments by value, June 2026", cr("pay"), (v) => fmt(v, 2),
      "The money cross-border bills are paid in. Payments in a currency settle through banks in its home system, under its laws and its central bank's rules.") +
    panel("Countries tied to it", "countries using it as their money, or pegging or holding a band to it, Dec 2025", curs.map((c) => [c, CUR[c].tied || null, (CUR[c].tiedL || []).join(", "), c === selCur]), (v) => fmt(v, 0),
      "These countries cannot set their own interest rates freely: to keep the tie, they follow the issuing central bank's moves without a say in them. Hover a bar for the list.") +
    panel("Central bank size", "total assets, US$ bn, end 2025 (top 20)", top(bsRows, 20), (v) => fmt(v, 0),
      "Mostly bonds and loans bought with money the bank created. The larger it is, the more created money it has placed into its banks and markets.") +
    panel("Gold", "tonnes (top 20)", top(goldRows, 20), (v) => fmt(v, 0),
      "A reserve no foreign central bank issues. Where it is stored still matters: a 2022 London High Court ruling kept more than $1 billion of Venezuela's gold at the Bank of England out of the Maduro-appointed board's control (see Venezuela's box).") +
    panel("Swap lines given", "lines in force where it lends its own currency", swRows, (v) => fmt(v, 0),
      "Who a central bank will lend its currency to in a crisis. Countries without a line must spend their reserves or borrow from the IMF on its conditions.") +
    '</div>';
  w.foot.textContent = "Each panel has its own scale. The selected place's currency or bank is drawn in white.";
}
function drawTime(w) {
  const Wd = w.body.clientWidth || 800, Ht = w.body.clientHeight || 400, m = { l: 40, r: 16, t: 16, b: 26 };
  const y0 = 1970, y1 = 2023, X = (y) => m.l + (Wd - m.l - m.r) * (y - y0) / (y1 - y0), Y = (v) => m.t + (Ht - m.t - m.b) * (1 - v);
  const med = (sk) => { const out = []; for (let y = y0; y <= y1; y++) { const vs = ISOS.map((k) => atYear(P[k][sk], y)).filter((v) => v != null).sort((a, b) => a - b); out.push(vs.length ? vs[(vs.length - 1) >> 1] : null); } return out; };
  const path = (arr) => arr.map((v, i) => v == null ? "" : (i && arr[i - 1] != null ? "L" : "M") + X(y0 + i).toFixed(1) + " " + Y(v).toFixed(1)).join("");
  const ser = [["Median, Romelli", med("rs"), "#c9c3ee", 2], ["Median, Garriga", med("gs"), "#7fb0a8", 2]];
  if (S.sel) { const p = P[S.sel]; const pick = (sk) => { const a = []; for (let y = y0; y <= y1; y++) a.push(atYear(p[sk], y)); return a; }; if (p.rs) ser.push([p.n + ", Romelli", pick("rs"), "#f0ece4", 2.4]); if (p.gs) ser.push([p.n + ", Garriga", pick("gs"), "#a9cfe6", 2.4]); }
  let g = "";
  [0, .25, .5, .75, 1].forEach((v) => { g += '<line class="gl" x1="' + m.l + '" x2="' + (Wd - m.r) + '" y1="' + Y(v) + '" y2="' + Y(v) + '"/><text x="' + (m.l - 6) + '" y="' + (Y(v) + 3) + '" text-anchor="end">' + v + '</text>'; });
  for (let y = 1970; y <= 2020; y += 10) g += '<text x="' + X(y) + '" y="' + (Ht - 8) + '" text-anchor="middle">' + y + '</text>';
  ser.forEach((s) => { g += '<path d="' + path(s[1]) + '" fill="none" stroke="' + s[2] + '" stroke-width="' + s[3] + '" stroke-linejoin="round"' + (s[0].startsWith("Median") ? '' : ' stroke-dasharray="' + (s[0].endsWith("Garriga") ? "5 3" : "0") + '"') + '/>'; });
  g += '<line id="xh" x1="0" x2="0" y1="' + m.t + '" y2="' + (Ht - m.b) + '" stroke="rgba(255,255,255,.35)" style="display:none"/><rect x="' + m.l + '" y="' + m.t + '" width="' + (Wd - m.l - m.r) + '" height="' + (Ht - m.t - m.b) + '" fill="transparent" id="hz"/>';
  w.body.innerHTML = '<div class="lc"><svg>' + g + '</svg></div>';
  const svg = w.body.querySelector("svg"), xh = svg.querySelector("#xh");
  svg.querySelector("#hz").addEventListener("mousemove", (e) => { const r = svg.getBoundingClientRect(), y = Math.round(y0 + (e.clientX - r.left - m.l) / (Wd - m.l - m.r) * (y1 - y0)); if (y < y0 || y > y1) return; xh.setAttribute("x1", X(y)); xh.setAttribute("x2", X(y)); xh.style.display = ""; tip("<b>" + y + "</b><br>" + ser.map((s) => '<span style="color:' + s[2] + '">●</span> ' + esc(s[0]) + ": " + (s[1][y - y0] == null ? "–" : fmt(s[1][y - y0], 3))).join("<br>"), e.clientX, e.clientY); });
  svg.querySelector("#hz").addEventListener("mouseleave", () => { xh.style.display = "none"; tip(null); });
  w.foot.innerHTML = ser.map((s) => '<span style="color:' + s[2] + '">●</span> ' + esc(s[0])).join(" &nbsp; ") + " · How much independence from government each central bank's law grants on paper, from 0 (none) to 1 (full), each year from 1970 to 2023. The two \"Median\" lines show the middle value across every place coded that year by each of two research teams (Romelli; Garriga). Open a place to add its own lines.";
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

function update() { if ($("#sideBody")) markSide(); drawLegend(); paint(); drawList(); drawCharts(); if (S.sel) detail(S.sel); }
function init() {
  buildKey(); buildTr(); buildDock(); buildSide(); stars();
  fetch(BOUND_URL).then((r) => r.json()).then((geo) => { addLayers(geo); ready = true; update(); }).catch((e) => { console.warn("boundaries", e); });
  $("#detX").addEventListener("click", deselect);
  $("#worldBtn").addEventListener("click", wholeWorld);
  $("#zIn").addEventListener("click", () => map.zoomIn({ duration: 300 }));
  $("#zOut").addEventListener("click", () => map.zoomOut({ duration: 300 }));
  $("#toggleKey").addEventListener("click", () => { const p = $("#key"); p.classList.toggle("min"); $("#toggleKey").textContent = p.classList.contains("min") ? "+" : "−"; });
  $("#toggleTr").addEventListener("click", () => { const p = $("#tr"); p.classList.toggle("min"); $("#toggleTr").textContent = p.classList.contains("min") ? "Basemap +" : "−"; });
  if (innerWidth <= 820) { $("#key").classList.add("min"); $("#toggleKey").textContent = "+"; $("#tr").classList.add("min"); $("#toggleTr").textContent = "Basemap +"; }
  drawLegend(); drawList();
  map.jumpTo({ center: [12, 25], zoom: startZoom(), padding: { left: freeBox().L, right: freeBox().R, top: 0, bottom: 0 } });
}

/* ---------- about and sources ---------- */
const info = $("#info");
info.innerHTML = D.ABOUT;
const btn = $("#infoBtn");
const toggle = (open) => { const on = info.classList.toggle("open", typeof open === "boolean" ? open : undefined); btn.textContent = on ? "Close" : "About and sources"; };
document.addEventListener("keydown", (e) => { if (e.key !== "Escape") return; if (info.classList.contains("open")) toggle(false); else if (S.sel) deselect(); });
btn.addEventListener("click", toggle);
$("#infoClose").addEventListener("click", () => toggle(false));
btn.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); } });
})();
