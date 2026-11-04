
(async function () {
  "use strict";
  const bin = Uint8Array.from(atob(LC_DATA_GZ), (c) => c.charCodeAt(0));
  const D = JSON.parse(await new Response(new Blob([bin]).stream().pipeThrough(new DecompressionStream("gzip"))).text());
  const $ = (s, r = document) => r.querySelector(s);
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const num = (n, d = 0) => (n == null ? "–" : Number(n).toLocaleString("en-US", { maximumFractionDigits: d, minimumFractionDigits: d }));
  const usd = (n) => (n == null ? "amount not given" : Math.abs(n) >= 1e9 ? `US$${num(n / 1e9, 2)} billion` : Math.abs(n) >= 1e5 || n === 0 ? `US$${num(n / 1e6, 1)} million` : `US$${num(n / 1e3, 0)} thousand`);
  const sdr = (k) => (k == null ? "amount not given" : k >= 1e6 ? `SDR ${num(k / 1e6, 2)} billion` : `SDR ${num(k / 1e3, 1)} million`);
  const yr = (s) => (s ? +String(s).slice(0, 4) : null);

  /* ------------------------------------------------------------ the rows */
  const AREA = {
    DEB: "External debt: debt management and arrears",
    FIN: "Financial sector, monetary policy and central bank",
    FP: "Fiscal: spending, budgets and the fiscal balance",
    RTP: "Revenue and taxation",
    EXT: "External sector: trade, exchange rates, capital flows",
    SOE: "State-owned enterprises: reform, subsidies and prices",
    PRI: "Privatization of state-owned enterprises",
    LAB: "Labour: wages, jobs, pensions, social security",
    INS: "Institutional reforms (courts, competition, business rules)",
    ENV: "Environment and access to commons",
    SP: "Social policies",
    POV: "Poverty reduction (strategy papers, social spending floors, safety nets)",
    OTH: "Other",
  };
  const KIND = {
    QPCsTOT: "Quantitative performance criteria (binding numeric targets)",
    PAsTOT: "Prior actions (binding: must be done before the loan is approved)",
    SPCsTOT: "Structural performance criteria (binding reforms)",
    IBsTOT: "Indicative benchmarks (numeric targets, not binding)",
    SBsTOT: "Structural benchmarks (reforms, not binding)",
  };
  const IC = D.imfc.cols, ix = (c) => IC.indexOf(c);

  // Ramps run from dim (few) to bright (many), so the heaviest countries
  // stand out on the dark backgrounds. Each lender has its own hue; the
  // Bioluminescent and Hell backgrounds get ramps in their own colours.
  const RAMPS = {
    rose:  ["#3B2329", "#55303A", "#71404C", "#8E5260", "#A96877", "#C38591", "#DBAAB2"],
    plum:  ["#2B2436", "#3D3150", "#52436B", "#685887", "#8270A1", "#9F8EBB", "#C1B3D5"],
    slate: ["#1E2937", "#28394D", "#344B65", "#43607F", "#587A99", "#7697B2", "#A2BCD0"],
    teal:  ["#1C2E30", "#243F42", "#2F5256", "#3D676A", "#527E80", "#719A99", "#9CBDBA"],
    sage:  ["#252C21", "#323C2C", "#435039", "#57654A", "#6E7D5E", "#8C9878", "#B2BB9F"],
    stone: ["#2C2826", "#3E3835", "#544C47", "#6C625B", "#877C73", "#A69A90", "#CBC0B5"],
    moss:  ["#1E2A1D", "#2A3A27", "#384C32", "#4A6040", "#5F7651", "#7A8F69", "#A0B38A"],
    night: ["#0E1A36", "#16295A", "#22407E", "#3A5F9E", "#5E86BC", "#91B2D6", "#D2E2EE"],
    hell:  ["#2A1B1C", "#3E2526", "#573233", "#734446", "#93605E", "#B78A84", "#DCC3B8"],
  };
  const NONE = "rgba(150,150,150,.13)";

  const LAYERS = [];
  const rowOf = (id) => LAYERS.find((l) => l.id === id);

  // IMF conditions, from the IMF Monitor country-year file.
  LAYERS.push({
    id: "imfc", lender: "IMF", ramp: "rose", span: D.imfc.years,
    title: "IMF: conditions written into its loans",
    plain: "The IMF lends to governments in trouble only if they change policies it chooses: cut spending, raise taxes, sell state companies, free up trade and more. Each demand is a \"condition\". This counts them for each country.",
    short: "IMF conditions",
    controls: () => `<select data-k="measure">
        <option value="BA1TOT">Every condition</option>
        <option value="BA2TOT">Binding conditions only</option>
        <optgroup label="By kind of condition">${Object.entries(KIND).map(([k, t]) => `<option value="${k}">${esc(t)}</option>`).join("")}</optgroup>
        <optgroup label="By policy area, every condition">${Object.entries(AREA).map(([k, t]) => `<option value="BA1${k}">${esc(t)}</option>`).join("")}</optgroup>
        <optgroup label="By policy area, binding only">${Object.entries(AREA).map(([k, t]) => `<option value="BA2${k}">${esc(t)} (binding)</option>`).join("")}</optgroup>
      </select>`,
    unit: (v) => `${num(v)} condition${v === 1 ? "" : "s"}`,
    values(from, to, o) {
      const k = ix(o.measure || "BA1TOT"), out = new Map();
      for (const c of D.imfc.countries_in_dataset) out.set(c, 0);
      for (const [c, ys] of Object.entries(D.imfc.data)) {
        let s = 0; for (const [y, r] of Object.entries(ys)) if (+y >= from && +y <= to) s += r[k];
        out.set(c, s);
      }
      return { values: out, unplaced: [] };
    },
    popup(c, from, to, o) {
      const ys = D.imfc.data[c] || {}, k = ix(o.measure || "BA1TOT");
      const sum = (col) => { let s = 0; for (const [y, r] of Object.entries(ys)) if (+y >= from && +y <= to) s += r[ix(col)]; return s; };
      const series = []; for (let y = Math.max(from, D.imfc.years[0]); y <= Math.min(to, D.imfc.years[1]); y++) series.push([y, ys[y] ? ys[y][k] : 0]);
      const tot = sum("BA1TOT");
      let h = `<div class="big">${num(sum(o.measure || "BA1TOT"))} conditions</div><div class="note">Counting: ${esc(optionText("imfc", o.measure))}</div>`;
      h += bars(series, "#C38591");
      if (tot) {
        h += `<h4>By kind</h4><table>${Object.entries(KIND).map(([kk, t]) => `<tr><td>${esc(t)}${tip(kk)}</td><td class="n">${num(sum(kk))}</td></tr>`).join("")}<tr><td>Every condition${tip("every")}</td><td class="n">${num(tot)}</td></tr></table>`;
        h += `<h4>By policy area</h4><table><tr><td></td><td class="n">every${tip("every")}</td><td class="n">binding${tip("binding")}</td></tr>${Object.entries(AREA).map(([kk, t]) => `<tr><td>${esc(t)}${tip("BA1" + kk)}</td><td class="n">${num(sum("BA1" + kk))}</td><td class="n">${num(sum("BA2" + kk))}</td></tr>`).join("")}</table>`;
      }
      return h;
    },
    srcLine: "IMF Monitor conditionality dataset v2.0 (Kentikelenis and Stubbs)",
    about: `<p>Every condition the IMF attached to its lending programs, counted for each country and year from the IMF's own loan documents (Letters of Intent, Memoranda of Economic and Financial Policies and staff reports). Binding conditions must be met for money to keep flowing: quantitative performance criteria (numeric targets such as limits on spending, borrowing or money supply), prior actions (done before a loan is approved) and structural performance criteria. Benchmarks are tracked but are not binding.</p>
<p>Coverage: ${D.imfc.years[0]} to ${D.imfc.years[1]}, the years the dataset covers. Total in the file: ${num(D.meta.imfc_total)} conditions. The project's own site gives 65,894 for 1980 to 2019 and its book gives 65,707; this map uses the published country-year file, which sums to ${num(D.meta.imfc_total)}. The file gives policy areas as short codes; their names here follow the categories in the authors' book (for example its "fiscal issues, revenues and taxation" is the sum of the FP and RTP codes).</p>
<p>Countries in the dataset with no condition in the chosen years are shaded grey.</p>
<p>Source: Kentikelenis, A. and Stubbs, T. (2023), <i>A Thousand Cuts: Social Protection in the Age of Austerity</i>, Oxford University Press; replication data, IMF Monitor Dataverse, <a href="https://doi.org/10.7910/DVN/DPV99L" target="_blank" rel="noopener">doi:10.7910/DVN/DPV99L</a> (IMFBOOK_Dataset). Methods: Kentikelenis, Stubbs and King (2016), "IMF conditionality and development policy space, 1985–2014", <i>Review of International Political Economy</i> 23(4). Project site: <a href="https://www.imfmonitor.org/conditionality" target="_blank" rel="noopener">imfmonitor.org</a>.</p>
<p>After 2019: the IMF publishes the conditions of programs from 2002 onward in its Monitoring of Fund Arrangements (MONA) database. It is not on this map yet; the IMF loan row below covers the arrangements themselves through 2026.</p>`,
  });

  // IMF arrangements, every one the IMF lists plus the additions the dataset documents.
  const FAC_GROUP = {
    "Extended Credit Facility": "Concessional (low-interest)", "Structural Adjustment Facility Commitment": "Concessional (low-interest)",
    "Standby Credit Facility": "Concessional (low-interest)", "Exogenous Shock Facility": "Concessional (low-interest)",
    "Standby Arrangement": "Non-concessional", "Extended Fund Facility": "Non-concessional", "Flexible Credit Line": "Non-concessional",
    "Resilience and Sustainability Facility": "Non-concessional", "Precautionary and Liquidity Line": "Non-concessional", "Short-Term Liquidity Line": "Non-concessional",
    "Rapid Credit Facility": "Rapid payouts and outright purchases", "Rapid Financing Instrument": "Rapid payouts and outright purchases",
    "Systemic Transformation Facility": "Rapid payouts and outright purchases", "Emergency Natural Disaster Assistance": "Rapid payouts and outright purchases",
    "Emergency Post-Conflict Assistance": "Rapid payouts and outright purchases",
  };
  const A = D.imfa.rows.map((r) => ({ c: r[0], cn: r[1], fac: r[2], ap: r[3], ex: r[4], agreed: r[5], drawn: r[6], out: r[7], src: r[8], note: r[9] }));
  const facs = [...new Set(A.map((a) => a.fac))];
  const imfaKeep = (a, o) => !o.off || !o.off.has(a.fac);
  const inForce = (a, from, to) => yr(a.ap) <= to && (yr(a.ex) || yr(a.ap)) >= from;
  LAYERS.push({
    id: "imfa", lender: "IMF", ramp: "plum", span: [1952, Math.max(...A.map((a) => yr(a.ap)))],
    title: "IMF: loan arrangements",
    plain: "Every loan deal the IMF has signed with a country since 1952, with how much was agreed, how much was paid out and how much is still owed. Each one came with conditions.",
    short: "IMF loan arrangements",
    controls: () => `<select data-k="measure">
        <option value="approved">Arrangements approved in these years</option>
        <option value="force">Arrangements in force at any time in these years</option>
        <option value="agreed">Amount agreed, approved in these years (SDR)</option>
      </select>` + checks("fac", groupBy(facs, (f) => FAC_GROUP[f] || "Other"), (f) => `${f} (${A.filter((a) => a.fac === f).length})`),
    unit: (v, o) => (o.measure === "agreed" ? sdr(v) : `${num(v)} arrangement${v === 1 ? "" : "s"}`),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const a of A) {
        if (!imfaKeep(a, o)) continue;
        const hit = o.measure === "force" ? inForce(a, from, to) : yr(a.ap) >= from && yr(a.ap) <= to;
        if (!hit) continue;
        const v = o.measure === "agreed" ? a.agreed || 0 : 1;
        if (a.c && GEO.has(a.c)) out.set(a.c, (out.get(a.c) || 0) + v); else unplaced.set(a.cn, (unplaced.get(a.cn) || 0) + v);
      }
      for (const c of new Set(A.map((a) => a.c))) if (c && !out.has(c)) out.set(c, 0);
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = A.filter((a) => a.c === c && imfaKeep(a, o) && (o.measure === "force" ? inForce(a, from, to) : yr(a.ap) >= from && yr(a.ap) <= to))
        .sort((a, b) => (b.ap || "").localeCompare(a.ap || ""));
      const series = []; for (let y = Math.max(from, 1952); y <= Math.min(to, 2026); y++) series.push([y, A.filter((a) => a.c === c && imfaKeep(a, o) && yr(a.ap) === y).length]);
      let h = `<div class="big">${list.length} arrangement${list.length === 1 ? "" : "s"} ${o.measure === "force" ? "in force" : "approved"}</div>` + bars(series, "#9F8EBB", "approved per year");
      h += list.map((a) => `<div class="item"><b>${esc(a.fac)}</b>${tip("ck_" + a.fac.toLowerCase().replace(/[^a-z]/g, "")) || tip(FAC_GROUP[a.fac] === "Rapid payouts and outright purchases" ? "rapid" : /^Concessional/.test(FAC_GROUP[a.fac] || "") ? "concessional" : "nonconcessional")}<br><span class="m">Approved ${esc(a.ap || "–")}, ${a.ex ? "expires or expired " + esc(a.ex) : "no expiry given"}</span><br>Agreed ${sdr(a.agreed)}${tip("sdr")}; drawn ${sdr(a.drawn)}${a.out != null ? `; still owed ${sdr(a.out)} at ${esc(D.imfa.as_of)}` : ""}${a.note ? `<br><span class="m">${esc(a.note)}</span>` : ""}</div>`).join("");
      return h;
    },
    srcLine: "IMF History of Lending Commitments, via the IMF Monitor Programs Dataset",
    about: `<p>Every IMF lending arrangement since 1952: the facility, the date the IMF board approved it, when it expires, and the amounts agreed, drawn and still owed, in Special Drawing Rights (the IMF's unit of account). Each of these loans comes with conditions; the rapid payouts carry fewer. Untick a facility to leave it out.</p>
<p>Coverage: arrangements approved from 1952 to ${esc(A.reduce((m, a) => (a.ap > m ? a.ap : m), ""))}, as listed by the IMF on ${esc(D.imfa.as_of)}. ${A.length} rows: the IMF's own list, plus 102 the dataset adds with evidence (outright purchases and one arrangement the IMF no longer lists).</p>
<p>Source: Stubbs, T. (2026), IMF Programs Dataset, 1952–2025 (version October 2026), IMF Monitor, <a href="https://doi.org/10.7910/DVN/V4V1BA" target="_blank" rel="noopener">doi:10.7910/DVN/V4V1BA</a> (IMFMonitor_Programs_Raw), scraped from the IMF's History of Lending Commitments.</p>`,
  });

  // IMF Resilience and Sustainability Facility reform measures, 2022 onward (Kentikelenis and Stubbs).
  const R = D.rsf.rows.map((r) => ({ c: r[0], cn: r[1], ad: r[2], dur: r[3], amt: r[4], doc: r[5], text: r[6], mon: r[7], y: r[8], arealong: r[9], area: r[10], mdoc: r[11], mtext: r[12], mmon: r[13], my: r[14] }));
  const rAreas = [...new Set(R.map((x) => x.area))];
  const rKeep = (x, o) => !o.off || !o.off.has(x.area);
  const rYear = (x, o) => (o.measure === "approved" ? yr(x.ad) : x.y);
  LAYERS.push({
    id: "rsf", lender: "IMF", ramp: "rose", span: [Math.min(...R.map((x) => yr(x.ad))), Math.max(...R.map((x) => x.y))],
    title: "IMF: conditions on its climate loans (Resilience and Sustainability Facility)",
    plain: "Since 2022 the IMF has offered loans for climate and pandemic preparedness. These are the reforms it required in return, word for word.",
    short: "IMF climate-loan conditions",
    controls: () => `<select data-k="measure">
        <option value="due">Reform measures due in these years</option>
        <option value="approved">Reform measures on loans approved in these years</option>
      </select>` + checks("area", { "Policy area, as the researchers group them": rAreas }, (k) => `${k.charAt(0) + k.slice(1).toLowerCase()} (${R.filter((x) => x.area === k).length})`),
    unit: (v) => `${num(v)} reform measure${v === 1 ? "" : "s"}`,
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const x of R) {
        if (!rKeep(x, o)) continue;
        const y = rYear(x, o); if (y < from || y > to) continue;
        if (GEO.has(x.c)) out.set(x.c, (out.get(x.c) || 0) + 1); else unplaced.set(x.cn, (unplaced.get(x.cn) || 0) + 1);
      }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = R.filter((x) => x.c === c && rKeep(x, o) && rYear(x, o) >= from && rYear(x, o) <= to).sort((a, b) => a.y - b.y);
      if (!list.length) return `<div class="note">No reform measures in these years.</div>`;
      const a = list[0];
      let h = `<div class="big">${list.length} reform measure${list.length === 1 ? "" : "s"}</div><div class="note">Climate loan approved ${esc(a.ad)}, ${a.dur} months, SDR ${num(a.amt, 1)} million.</div>`;
      h += list.map((x) => `<div class="item">${esc(x.text)}<br><span class="m">Due ${esc(x.mon || "")} ${x.y} · ${esc(x.arealong || x.area)} · IMF document ${esc(x.doc || "–")}</span>${x.mtext ? `<br><span class="m">Changed later (${esc(x.mdoc || "")}, due ${esc(x.mmon || "")} ${esc(x.my || "")}):</span> ${esc(x.mtext)}` : ""}</div>`).join("");
      return h;
    },
    srcLine: "Greening the IMF dataset (Kentikelenis and Stubbs)",
    about: `<p>Every reform measure attached to the IMF's climate loans, the Resilience and Sustainability Facility the IMF started in 2022, with the wording from the IMF's own country reports, the date each was due, and the policy area. Where a later IMF review changed a measure, the changed wording is shown too. These are the only IMF conditions after 2019 on this map so far (see the first IMF row).</p>
<p>Coverage: ${R.length} reform measures in ${new Set(R.map((x) => x.c)).size} countries, on climate loans approved from ${esc(R.reduce((m, x) => (x.ad < m ? x.ad : m), "9999"))} to ${esc(R.reduce((m, x) => (x.ad > m ? x.ad : m), ""))}, due from ${Math.min(...R.map((x) => x.y))} to ${Math.max(...R.map((x) => x.y))}. Choose whether a measure counts in the year it was due or the year its loan was approved.</p>
<p>Source: Kentikelenis, A. and Stubbs, T., <i>Greening the International Monetary Fund</i>, replication data, IMF Monitor Dataverse, <a href="https://doi.org/10.7910/DVN/8BSKWO" target="_blank" rel="noopener">doi:10.7910/DVN/8BSKWO</a> (GREENBOOK_Ch2_RSFConditions).</p>`,
  });

  // IMF programs: whether conditions were met (Reinsberg, Stubbs and Kentikelenis).
  const G = D.gove.rows.map((r) => ({ c: r[0], y: r[1], doc: r[2], fac: r[3], dur: r[4], bind: r[5], waiv: r[6], fb: r[7], fn: r[8], ip: r[9], it: r[10], iy: r[11], sdr: r[12], drawn: r[13] }));
  const GM = {
    waiv: ["Waivers: binding conditions missed that the IMF board excused", (x) => x.waiv],
    perm: ["Programs stopped for good before they ended", (x) => (x.ip ? 1 : 0)],
    temp: ["Programs held up for a time", (x) => (x.it ? 1 : 0)],
    fn: ["Conditions not met, narrow count (programs the authors coded in detail)", (x) => x.fn],
    fb: ["Conditions not met, broad count (programs the authors coded in detail)", (x) => x.fb],
    bind: ["Binding conditions in these programs", (x) => x.bind],
    progs: ["Programs", () => 1],
  };
  LAYERS.push({
    id: "gove", lender: "IMF", ramp: "plum", span: [Math.min(...G.map((x) => x.y)), Math.max(...G.map((x) => x.y))],
    title: "IMF: conditions missed, waived, and programs stopped",
    plain: "What happened after the conditions were set: how often countries missed them, how often the IMF let it slide, and how often the money was cut off.",
    short: "IMF programs: conditions missed and programs stopped",
    controls: () => `<select data-k="measure">${Object.entries(GM).map(([k, [t]]) => `<option value="${k}">${esc(t)}</option>`).join("")}</select>`,
    unit: (v, o) => `${num(v)} ${o.measure === "waiv" ? "waiver" + (v === 1 ? "" : "s") : o.measure === "fn" || o.measure === "fb" || o.measure === "bind" ? "condition" + (v === 1 ? "" : "s") : "program" + (v === 1 ? "" : "s")}`,
    values(from, to, o) {
      const f = GM[o.measure || "waiv"][1], out = new Map(), unplaced = new Map();
      for (const x of G) {
        if (x.y < from || x.y > to) continue;
        const v = f(x); if (v == null) continue;
        if (GEO.has(x.c)) out.set(x.c, (out.get(x.c) || 0) + v); else unplaced.set(NAMEOF[x.c] || x.c, (unplaced.get(NAMEOF[x.c] || x.c) || 0) + v);
      }
      for (const x of G) if (GEO.has(x.c) && !out.has(x.c) && x.y >= from && x.y <= to) out.set(x.c, 0);
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = G.filter((x) => x.c === c && x.y >= from && x.y <= to).sort((a, b) => b.y - a.y);
      const v = (n) => (n == null ? "not coded" : num(n));
      let h = `<div class="big">${list.length} program${list.length === 1 ? "" : "s"} approved in these years</div>`;
      h += list.map((x) => `<div class="item"><b>${esc(x.fac || "Facility not given")}</b>, approved ${x.y} (IMF board meeting ${esc(x.doc)}), ${x.dur != null ? num(x.dur) + " months" : "length not given"}, SDR ${num(x.sdr, 1)} million agreed, ${num(x.drawn, 1)} million drawn<br>
        <span class="m">Binding conditions${tip("binding")} ${v(x.bind)} · waivers${tip("waiver")} ${v(x.waiv)} · not met (narrow / broad)${tip("notmet")} ${v(x.fn)} / ${v(x.fb)}</span><br>
        ${x.ip ? `Stopped for good${tip("stopped")}${x.iy ? " in " + x.iy : ""}` : x.it ? `Held up for a time${tip("held")}${x.iy ? " in " + x.iy : ""}` : "Not interrupted"}</div>`).join("");
      return h;
    },
    srcLine: "Reinsberg, Stubbs and Kentikelenis, IMF compliance data",
    about: `<p>For each IMF program, what happened to its conditions: how many binding conditions the IMF board waived after a country missed them, whether the program was stopped for good or held up for a time, and, for the programs the authors coded condition by condition, how many conditions were not met (counted narrowly and broadly).</p>
<p>Coverage: ${G.length} programs approved from ${Math.min(...G.map((x) => x.y))} to ${Math.max(...G.map((x) => x.y))}. The condition-by-condition counts exist for ${G.filter((x) => x.fn != null).length} of them; elsewhere they show as "not coded". Counted in the year each program was approved.</p>
<p>Source: Reinsberg, B., Stubbs, T. and Kentikelenis, A., "Unimplementable by design? Understanding (non-)compliance with International Monetary Fund policy conditionality", <i>Governance</i>; replication data, IMF Monitor Dataverse, <a href="https://doi.org/10.7910/DVN/QTFOGF" target="_blank" rel="noopener">doi:10.7910/DVN/QTFOGF</a>.</p>`,
  });

  // World Bank policy-based loans, from the World Bank projects database.
  const W = D.wbp.rows.map((r) => ({ c: r[0], cn: r[1], id: r[2], name: r[3], ins: r[4], ap: r[5], amt: r[6], st: r[7] }));
  const wins = [...new Set(W.map((w) => w.ins))];
  const wKeep = (w, o) => !o.off || !o.off.has(w.ins);
  const wDone = (w) => !!w.ap && w.st !== "Pipeline" && w.st !== "Dropped";
  const wLast = W.reduce((m, w) => (wDone(w) && w.ap > m ? w.ap : m), "");
  LAYERS.push({
    id: "wbp", lender: "World Bank", ramp: "slate", span: [1947, yr(wLast)],
    title: "World Bank: policy-based loans",
    plain: "World Bank loans paid straight into a government\u2019s budget once it makes policy changes the Bank asks for, rather than paying for a road or a school.",
    short: "World Bank policy-based loans",
    controls: () => `<select data-k="measure">
        <option value="count">Loans approved in these years</option>
        <option value="amt">Amount committed (US$)</option>
      </select>` + checks("ins", { "Lending instrument, as the World Bank names it": wins }, (i) => `${i} (${W.filter((w) => w.ins === i).length})`),
    unit: (v, o) => (o.measure === "amt" ? usd(v) : `${num(v)} loan${v === 1 ? "" : "s"}`),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const w of W) {
        if (!wKeep(w, o) || !wDone(w) || yr(w.ap) < from || yr(w.ap) > to) continue;
        const v = o.measure === "amt" ? w.amt || 0 : 1;
        if (w.c && GEO.has(w.c)) out.set(w.c, (out.get(w.c) || 0) + v); else unplaced.set(w.cn, (unplaced.get(w.cn) || 0) + v);
      }
      for (const c of new Set(W.map((w) => w.c))) if (c && !out.has(c)) out.set(c, 0);
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const mine = W.filter((w) => w.c === c && wKeep(w, o));
      const list = mine.filter((w) => wDone(w) && yr(w.ap) >= from && yr(w.ap) <= to).sort((a, b) => b.ap.localeCompare(a.ap));
      const undated = mine.filter((w) => !wDone(w));
      const series = []; for (let y = Math.max(from, 1947); y <= Math.min(to, yr(wLast)); y++) series.push([y, mine.filter((w) => wDone(w) && yr(w.ap) === y).length]);
      let h = `<div class="big">${list.length} loan${list.length === 1 ? "" : "s"}, ${usd(list.reduce((s, w) => s + (w.amt || 0), 0))}</div>` + bars(series, "#7697B2", "approved per year");
      h += list.map(wItem).join("");
      if (undated.length) h += `<h4>Not counted: dropped, still planned, or undated</h4>` + undated.map(wItem).join("");
      return h;
    },
    srcLine: "World Bank projects database",
    about: `<p>Every World Bank loan, credit or grant made as budget support in return for policy changes: structural and sector adjustment loans (1980s and 1990s), poverty reduction support credits, and development policy loans (from 2004). The conditions are the "prior actions" and earlier "tranche conditions" listed in each loan's program document, linked from each project's page.</p>
<p>Coverage: ${W.length} operations, approved from 1947 to ${esc(wLast)}. Dropped loans and those still being prepared are not counted on the map but are listed in each country's box (a planned loan's date is only its target date).</p>
<p>After ${esc(D.meta.wbp_v2_last)}: the version of the World Bank's projects index that names each loan's lending instrument stops at that date. Loans approved since then come from the World Bank's newer index, which has no instrument field, so they are included only when the World Bank's own project name calls them a development policy operation (DPF, DPO, DPL, DPC, Cat DDO, policy-based guarantee and so on); they are marked "Named as a development policy operation". Tested on 2005 to 2024, where the instrument is known, this rule picked up no loan that was not policy-based but missed about one in five that were, because their names do not say so. Counts for 2025 and 2026 are therefore low by roughly that much.</p>
<p>The text of a loan's conditions, where the researchers below extracted it from the signed legal agreement, opens from the loan in each country's box (${num(Object.keys(D.wbtext).length)} loans). It is the agreement's wording as extracted, including some surrounding schedules.</p>
<p>Counted by this map, not published by the World Bank: for ${num(Object.values(D.wbown).filter((v) => v != null).length)} of the ${num(Object.keys(D.wbown).length)} loans with agreement text, the box gives a count of conditions. The rule: find each heading of the required-actions list in the text ("Actions Taken", "Prior Actions", "Program Actions", "Conditions of Release", "Tranche Release Conditions" and similar), skip the ones that are only definitions, stop at the repayment and procurement schedules, and count the numbered items, or the lettered ones if there are more. The other loans' texts have no list this rule can read, and are left uncounted. Checked against the researchers' own counts for the ${num(473)} loans both cover: this rule counts fewer on average (8.5 against 10.9), is within two of theirs for ${num(204)} loans, and the two agree only loosely (correlation 0.33), so treat it as a rough guide, not a figure from the World Bank.</p>
<p>Sources: World Bank projects database, <a href="https://search.worldbank.org/api/v2/projects" target="_blank" rel="noopener">projects index (with lending instrument)</a> and <a href="https://search.worldbank.org/api/v3/projects" target="_blank" rel="noopener">newer projects index</a>. Agreement texts: Winter, Cormier, Kramarz and Manger (2025), replication data <a href="https://doi.org/10.7910/DVN/AF3EZP" target="_blank" rel="noopener">doi:10.7910/DVN/AF3EZP</a> (conditions_to_share_full).</p>`,
  });

  // World Bank conditions counted in loan agreements (Winter, Cormier, Kramarz and Manger).
  const C = D.wbc.rows.map((r) => ({ c: r[0], id: r[1], y: r[2], ins: r[3], pol: r[4], n: r[5], topic: r[6], dt: r[7], amt: r[8] }));
  const TOPIC = { X1_Financial_Reform: "Financial reform", X2_Trade_and_Investment: "Trade and investment", X3_Fiscal_Reform: "Fiscal reform", X4_Governance: "Governance", X5_Social_Spending: "Social spending", X6_Borrower_Ownership: "Borrower ownership" };
  const wName = Object.fromEntries(W.map((w) => [w.id, w.name]));
  const cKeep = (x, o) => !o.off || !o.off.has(x.pol ? "Policy-based (adjustment) loans" : "Investment and other loans");
  LAYERS.push({
    id: "wbc", lender: "World Bank", ramp: "teal", span: [Math.min(...C.map((x) => x.y)), Math.max(...C.map((x) => x.y))],
    title: "World Bank: conditions counted in loan agreements",
    plain: "How many conditions were written into the signed contracts of World Bank loans, counted by university researchers.",
    short: "World Bank loan-agreement conditions",
    controls: () => `<select data-k="measure">
        <option value="n">Conditions</option>
        <option value="loans">Loans with conditions</option>
      </select>` + checks("pol", { "Kind of loan": ["Policy-based (adjustment) loans", "Investment and other loans"] }, (k) => `${k} (${C.filter((x) => (x.pol ? "Policy-based (adjustment) loans" : "Investment and other loans") === k).length} loans)`),
    unit: (v, o) => (o.measure === "loans" ? `${num(v)} loan${v === 1 ? "" : "s"}` : `${num(v)} condition${v === 1 ? "" : "s"}`),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const x of C) {
        if (!cKeep(x, o) || x.y < from || x.y > to) continue;
        const v = o.measure === "loans" ? 1 : x.n;
        if (GEO.has(x.c)) out.set(x.c, (out.get(x.c) || 0) + v); else unplaced.set(NAMEOF[x.c] || x.c, (unplaced.get(NAMEOF[x.c] || x.c) || 0) + v);
      }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = C.filter((x) => x.c === c && cKeep(x, o) && x.y >= from && x.y <= to).sort((a, b) => b.dt.localeCompare(a.dt));
      const series = []; for (let y = Math.max(from, this.span[0]); y <= Math.min(to, this.span[1]); y++) series.push([y, C.filter((x) => x.c === c && cKeep(x, o) && x.y === y).reduce((s, x) => s + x.n, 0)]);
      let h = `<div class="big">${num(list.reduce((s, x) => s + x.n, 0))} conditions in ${list.length} loan${list.length === 1 ? "" : "s"}</div>` + bars(series, "#719A99", "conditions per year");
      h += list.map((x) => `<div class="item"><a href="https://projects.worldbank.org/en/projects-operations/project-detail/${esc(x.id)}" target="_blank" rel="noopener">${esc(wName[x.id] || x.id)}</a><br><span class="m">${esc(x.id)} · ${esc(x.ins)} · document dated ${esc(x.dt)}</span><br>${num(x.n)} condition${x.n === 1 ? "" : "s"}${x.topic ? `; main topic as the authors classify it: ${esc(TOPIC[x.topic] || x.topic)}` : ""}</div>`).join("");
      return h;
    },
    srcLine: "Winter, Cormier, Kramarz and Manger, loan-agreement conditions",
    about: `<p>The number of loan-specific conditions written into the legal agreements of World Bank loans, read from the agreements by the researchers. This covers every kind of loan whose agreement they could obtain, not just policy-based ones; for investment loans the conditions are mostly about how the project is run. Untick a kind of loan to leave it out.</p>
<p>Coverage: ${C.length} loans with ${num(C.reduce((s, x) => s + x.n, 0))} conditions, documents dated ${Math.min(...C.map((x) => x.y))} to ${Math.max(...C.map((x) => x.y))}. These are counts from the legal agreements; they are a different measure from the IMF counts above and should not be added to them.</p>
<p>Source: Winter, Cormier, Kramarz and Manger (2025), "Reassessing World Bank conditionality: beyond count measures", <i>Political Science Research and Methods</i>, <a href="https://doi.org/10.1017/psrm.2025.19" target="_blank" rel="noopener">doi:10.1017/psrm.2025.19</a>; replication data <a href="https://doi.org/10.7910/DVN/AF3EZP" target="_blank" rel="noopener">doi:10.7910/DVN/AF3EZP</a> (data_wb_conditions). The texts of the conditions are published in the same files and in Cormier and Manger's <a href="https://doi.org/10.7910/DVN/60XKHH" target="_blank" rel="noopener">dataset of 1,242 agreements</a>.</p>`,
  });

  // World Bank Privatization Database: every sale it recorded, 1988-2008.
  const PV = D.wbpriv.rows.map((r) => ({ c: r[0], cn: r[1], co: r[2], y: r[3], sec: r[4] || "Not given", deal: r[5], sub: r[6], amt: r[7], real: r[8], rel: r[9] }));
  const pvSecs = [...new Set(PV.map((x) => x.sec))].sort((a, b) => PV.filter((x) => x.sec === b).length - PV.filter((x) => x.sec === a).length);
  const pvKeep = (x, o) => !o.off || !o.off.has(x.sec);
  const pvMil = (v) => (v == null ? "amount not given" : usd(v));
  LAYERS.push({
    id: "wbpriv", lender: "World Bank", ramp: "slate", span: [Math.min(...PV.map((x) => x.y)), Math.max(...PV.map((x) => x.y))],
    title: "Sales of state firms and services, as the World Bank recorded them",
    short: "sales of state firms and services",
    plain: "Each time a government in a low- or middle-income country sold, leased or handed over a state company or public service (banks, power, phones, mines, factories, hotels and more), the World Bank logged it with the price paid. IMF and World Bank loans often required such sales (the IMF conditions row counts them under “Privatization”). This row shows the sales themselves, not which ones a condition required.",
    controls: () => `<select data-k="measure">
        <option value="n">Number of sales recorded</option>
        <option value="amt">Money the government received (US$)</option>
      </select>` + checks("sec", { "Sector, as the World Bank labelled it": pvSecs }, (k) => `${k} (${num(PV.filter((x) => x.sec === k).length)})`),
    unit: (v, o) => (o.measure === "amt" ? usd(v) : `${num(v)} sale${v === 1 ? "" : "s"}`),
    fmt: (v, o) => (o.measure === "amt" ? usd(v) : num(v)),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const x of PV) {
        if (!pvKeep(x, o) || x.y < from || x.y > to) continue;
        const v = o.measure === "amt" ? x.amt || 0 : 1;
        if (x.c && GEO.has(x.c)) out.set(x.c, (out.get(x.c) || 0) + v); else unplaced.set(x.cn, (unplaced.get(x.cn) || 0) + v);
      }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = PV.filter((x) => x.c === c && pvKeep(x, o) && x.y >= from && x.y <= to).sort((a, b) => b.y - a.y || (b.amt || 0) - (a.amt || 0));
      const series = []; for (let y = Math.max(from, this.span[0]); y <= Math.min(to, this.span[1]); y++) series.push([y, list.filter((x) => x.y === y).length]);
      const tot = list.reduce((s, x) => s + (x.amt || 0), 0);
      return `<div class="big">${num(list.length)} sale${list.length === 1 ? "" : "s"}, ${usd(tot)} received</div>` + bars(series, "#7697B2", "sales per year") +
        list.map((x) => `<div class="item"><b>${esc(x.co || "Name not given")}</b><br><span class="m">${x.y} · ${esc(x.sec)}${x.real ? " · " + esc(x.real) : ""}${x.deal ? " · " + esc(x.deal) : ""}${x.sub ? " (" + esc(x.sub) + ")" : ""}</span><br>${pvMil(x.amt)}</div>`).join("");
    },
    srcLine: "World Bank Privatization Database",
    about: `<p>Every record in the World Bank's two privatization files: ${num(PV.filter((x) => x.rel === 1).length)} for 1988 to 1999 and ${num(PV.filter((x) => x.rel === 2).length)} for 2000 to 2008. Each gives the company or asset, the year, the sector, how it was sold (auction, share offer, concession, management contract and so on, in the World Bank's own mixed wording) and what the government received. The files cover low- and middle-income countries only. The World Bank describes the 2000 to 2008 file as deals of at least US$1 million (5 rows in it are below that) and the earlier file as also including smaller deals and voucher sales. Two rows in the files read "No privatization"; they are shown as given.</p>
<p>The two files label sectors differently ("Manufacturing & Services" in the first, "Competitive" in the second, for example); the labels are shown exactly as written. Sales listed under "Serbia and Montenegro" have no shape on this map and are counted under the key.</p>
<p>Coverage: ${num(PV.length)} records, ${new Set(PV.map((x) => x.cn)).size} countries, ${usd(PV.reduce((s, x) => s + (x.amt || 0), 0))} in all.</p>
<p>Source: World Bank, Privatization Database (files PrivatizationData88_99.xls and PrivatizationData00_08.xls, formerly at rru.worldbank.org/Privatization), as archived by OpenSpending at <a href="https://github.com/pudo/dpkg-wb-privatization" target="_blank" rel="noopener">github.com/pudo/dpkg-wb-privatization</a>. The World Bank's own summaries: <a href="https://documents.worldbank.org/curated/en/2007/02/7458990/privatization-trends" target="_blank" rel="noopener">Privatization Trends (2007)</a>.</p>`,
  });

  // IDB policy-based loans and guarantees.
  const I = D.idb.rows.map((r) => ({ c: r[0], cn: r[1], id: r[2], name: r[3], ap: r[4], amt: r[5], st: r[6], mod: r[7], ins: r[8], sec: r[9] }));
  const iKind = (x) => x.mod || x.ins || "Not given";
  const iKinds = [...new Set(I.map(iKind))];
  const iKeep = (x, o) => !o.off || !o.off.has(iKind(x));
  const iLast = I.reduce((m, x) => (x.ap && x.ap > m ? x.ap : m), "");
  LAYERS.push({
    id: "idb", lender: "IDB", ramp: "sage", span: [yr(I.reduce((m, x) => (x.ap && x.ap < m ? x.ap : m), "9999")), yr(iLast)],
    title: "Inter-American Development Bank: policy-based loans",
    plain: "The Inter-American Development Bank\u2019s loans to Latin American and Caribbean governments, paid into the budget once agreed policy changes are made.",
    short: "IDB policy-based loans",
    controls: () => `<select data-k="measure">
        <option value="count">Loans approved in these years</option>
        <option value="amt">Amount approved (US$)</option>
      </select>` + checks("mod", { "Kind, as the IDB names it": iKinds }, (k) => `${k} (${I.filter((x) => iKind(x) === k).length})`),
    unit: (v, o) => (o.measure === "amt" ? usd(v) : `${num(v)} loan${v === 1 ? "" : "s"}`),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const x of I) {
        if (!iKeep(x, o) || !x.ap || yr(x.ap) < from || yr(x.ap) > to) continue;
        const v = o.measure === "amt" ? x.amt || 0 : 1;
        if (x.c && GEO.has(x.c)) out.set(x.c, (out.get(x.c) || 0) + v); else unplaced.set(x.cn, (unplaced.get(x.cn) || 0) + v);
      }
      for (const c of new Set(I.map((x) => x.c))) if (c && !out.has(c)) out.set(c, 0);
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const mine = I.filter((x) => x.c === c && iKeep(x, o));
      const list = mine.filter((x) => x.ap && yr(x.ap) >= from && yr(x.ap) <= to).sort((a, b) => b.ap.localeCompare(a.ap));
      const series = []; for (let y = Math.max(from, this.span[0]); y <= Math.min(to, this.span[1]); y++) series.push([y, mine.filter((x) => yr(x.ap) === y).length]);
      let h = `<div class="big">${list.length} loan${list.length === 1 ? "" : "s"}, ${usd(list.reduce((s, x) => s + (x.amt || 0), 0))}</div>` + bars(series, "#8C9878", "approved per year");
      h += list.map((x) => `<div class="item"><a href="https://www.iadb.org/en/project/${esc(x.id)}" target="_blank" rel="noopener">${esc(x.name)}</a><br><span class="m">${esc(x.id)} · ${esc(iKind(x))} · ${esc(x.sec)} · approved ${esc(x.ap)} · ${esc(x.st)}</span><br>${usd(x.amt)}</div>`).join("");
      return h;
    },
    srcLine: "IDB projects list (IDB open data)",
    about: `<p>Every loan and guarantee the Inter-American Development Bank lists as policy-based: money paid to a government's budget once agreed policy reforms are made. Each project's page lists its policy conditions in the loan proposal. Untick a kind to leave it out.</p>
<p>Coverage: ${I.length} operations approved from ${esc(I.reduce((m, x) => (x.ap && x.ap < m ? x.ap : m), "9999"))} to ${esc(iLast)}, in Latin America and the Caribbean (the IDB's borrowers), including those cancelled or still in preparation. Operations the IDB files under "Regional" have no single country and are listed under this row.</p>
<p>Source: Inter-American Development Bank, <a href="https://data.iadb.org/dataset/idb-projects-dataset" target="_blank" rel="noopener">IDB Projects Dataset</a> (English list), every row whose lending instrument is "Policy-Based Loan" or whose modality is a policy-based loan, programmatic policy-based loan, deferred drawdown policy-based loan or policy-based guarantee.</p>`,
  });

  // ---------------------------------------------------------------- OECD: budget support from every lender that reports to the OECD
  const O = D.crs.rows.map((r) => ({ c: r[0], dn: r[1], y: r[2], mod: r[3], kind: r[4], v: r[5], title: r[6], ag: r[7], id: r[8] }));
  const ON = D.crs.names;
  const oGroup = (code) => (/^5IMF/.test(code) ? "IMF" : /^5WB/.test(code) ? "World Bank" : /^5IDB/.test(code) ? "Inter-American Development Bank" : /^4EU/.test(code) ? "European Union institutions"
    : /^(5|9OTH)/.test(code) ? "Other development banks and funds" : /^1UN/.test(code) ? "United Nations agencies" : /^9PRIV/.test(code) ? "Private foundations" : "Governments");
  const oDonors = [...new Set(O.map((x) => x.dn))].sort((a, b) => (ON[a] || a).localeCompare(ON[b] || b));
  const oKeep = (x, o) => !o.off || !o.off.has(ON[x.dn] || x.dn);
  LAYERS.push({
    id: "oecd", lender: "OECD", ramp: "slate", span: [Math.min(...O.map((x) => x.y)), Math.max(...O.map((x) => x.y))],
    title: "Every lender: money paid straight into government budgets",
    short: "budget support from every lender reporting to the OECD",
    plain: `Money a lender pays straight into a government's budget, instead of paying for a set project. Lenders nearly always tie this kind of money to policy changes. This row covers ${oDonors.length} lenders that report to the OECD: governments such as Japan, the United States, Germany and Saudi Arabia, the EU, and the development banks of Asia, Africa, Latin America and the Middle East.`,
    controls: () => `<select data-k="measure">
        <option value="usd">Amount committed (US$)</option>
        <option value="n">Number of payments</option>
      </select>` + checks("donor", groupBy(oDonors, oGroup), (d) => `${ON[d] || d} (${O.filter((x) => x.dn === d).length})`, (d) => ON[d] || d),
    unit: (v, o) => (o.measure === "n" ? `${num(v)} payment${v === 1 ? "" : "s"}` : usd(v * 1e6)),
    fmt: (v, o) => (o.measure === "n" ? num(v) : usd(v * 1e6)),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const x of O) {
        if (!oKeep(x, o) || x.y < from || x.y > to) continue;
        const v = o.measure === "n" ? 1 : x.v;
        if (GEO.has(x.c)) out.set(x.c, (out.get(x.c) || 0) + v); else unplaced.set(ON[x.c] || x.c, (unplaced.get(ON[x.c] || x.c) || 0) + v);
      }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = O.filter((x) => x.c === c && oKeep(x, o) && x.y >= from && x.y <= to);
      const series = []; for (let y = Math.max(from, this.span[0]); y <= Math.min(to, this.span[1]); y++) series.push([y, list.filter((x) => x.y === y).reduce((s, x) => s + x.v, 0)]);
      const by = groupBy(list, (x) => x.dn);
      let h = `<div class="big">${usd(list.reduce((s, x) => s + x.v, 0) * 1e6)} in ${num(list.length)} payments</div>` + bars(series.map(([y, v]) => [y, Math.round(v)]), "#7697B2", "US$ million per year");
      h += Object.entries(by).sort((a, b) => b[1].reduce((s, x) => s + x.v, 0) - a[1].reduce((s, x) => s + x.v, 0)).map(([dn, xs]) =>
        `<details class="tx"><summary>${esc(ON[dn] || dn)}: ${usd(xs.reduce((s, x) => s + x.v, 0) * 1e6)}, ${xs.length} payment${xs.length === 1 ? "" : "s"}</summary>` +
        xs.sort((a, b) => b.y - a.y).map((x) => `<div class="item">${esc(x.title || "No title given")}<br><span class="m">${x.y} · ${x.mod === "A01" ? "General budget support" + tip("general") : "Sector budget support" + tip("sector")} · ${esc(x.kind)} · ${usd(x.v * 1e6)}${x.ag ? " · " + esc(x.ag) : ""}${x.id ? " · OECD id " + esc(x.id) : ""}</span></div>`).join("") + `</details>`).join("");
      return h;
    },
    srcLine: "OECD Creditor Reporting System",
    about: `<p>Every activity that a lender reported to the OECD as budget support (general or for one sector), committed from ${Math.min(...O.map((x) => x.y))} to ${Math.max(...O.map((x) => x.y))}, in US dollars at the prices of each year. These are the records the lenders themselves report; the OECD does not record the conditions attached. Untick a lender to leave it out.</p>
<p>Coverage: ${num(O.length)} activity-years from ${oDonors.length} lenders. Lenders that do not report to the OECD, or report no budget support, are not here: China (see the China rows), the Islamic Development Bank and the European Bank for Reconstruction and Development among them. Payments to a region rather than a country are listed under this row.</p>
<p>Source: OECD, Creditor Reporting System (CRS), dataflow DSD_CRS@DF_CRS version 1.7, project-level commitments with aid type A01 (general budget support) or A02 (sector budget support), read through the <a href="https://sdmx.oecd.org/dcd-public/rest/" target="_blank" rel="noopener">OECD data API</a> on 23 October 2026.</p>`,
  });

  // ---------------------------------------------------------------- EU and euro-area rescue and assistance programmes
  const E = D.eu.rows.map((r) => ({ c: r[0], cn: r[1], d: r[2], ins: r[3], form: r[4], amt: r[5], disb: r[6], ref: r[7], note: r[8], src: r[9], url: r[10] }));
  const eKind = (x) => (/macro-financial/i.test(x.ins) ? "EU macro-financial assistance (neighbouring countries)" : /balance-of-payments/i.test(x.ins) ? "EU balance-of-payments loans (EU members outside the euro)" : "Euro-area rescue programmes (Greece, Ireland, Portugal, Spain, Cyprus)");
  const eKinds = [...new Set(E.map(eKind))];
  const eKeep = (x, o) => !o.off || !o.off.has(eKind(x));
  const eur = (m) => (m == null ? "amount not given" : m >= 1000 ? `€${num(m / 1000, 2)} billion` : `€${num(m, 1)} million`);
  LAYERS.push({
    id: "eu", lender: "EU", ramp: "plum", span: [1990, Math.max(...E.map((x) => yr(x.d)))],
    title: "EU and euro area: rescue loans paid in stages for reforms",
    short: "EU and euro-area programmes",
    plain: "Loans from the EU and euro-area countries to governments in crisis. The money comes in instalments, and each instalment is paid only after the government carries out reforms written into an agreement (a memorandum of understanding).",
    controls: () => `<select data-k="measure">
        <option value="n">Programmes agreed in these years</option>
        <option value="amt">Amount made available (€)</option>
      </select>` + checks("kind", { "Kind of programme": eKinds }, (k) => `${k} (${E.filter((x) => eKind(x) === k).length})`),
    unit: (v, o) => (o.measure === "amt" ? eur(v) : `${num(v)} programme${v === 1 ? "" : "s"}`),
    fmt: (v, o) => (o.measure === "amt" ? eur(v) : num(v)),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const x of E) {
        if (!eKeep(x, o) || yr(x.d) < from || yr(x.d) > to) continue;
        const v = o.measure === "amt" ? x.amt || 0 : 1;
        if (GEO.has(x.c)) out.set(x.c, (out.get(x.c) || 0) + v); else unplaced.set(x.cn, (unplaced.get(x.cn) || 0) + v);
      }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = E.filter((x) => x.c === c && eKeep(x, o) && yr(x.d) >= from && yr(x.d) <= to).sort((a, b) => b.d.localeCompare(a.d));
      return `<div class="big">${list.length} programme${list.length === 1 ? "" : "s"}</div>` + list.map((x) => `<div class="item"><b>${esc(x.ins)}</b>${tip(/macro/i.test(x.ins) ? "mfa" : /balance/i.test(x.ins) ? "bop" : /ESM|EFSF|EFSM|Greek Loan/i.test(x.ins) ? "esm" : "mou")}<br>
        <span class="m">${esc(x.d)} · ${esc(x.form)}${x.ref ? " · decision " + esc(x.ref) : ""}</span><br>Made available ${eur(x.amt)}${x.disb != null ? `; paid out ${eur(x.disb)}` : ""}${x.note ? `<br><span class="m">${esc(x.note)}</span>` : ""}<br><a href="${esc(x.url)}" target="_blank" rel="noopener">Source</a></div>`).join("");
    },
    srcLine: "European Commission and EU Council documents",
    about: `<p>Every EU macro-financial assistance decision since 1990 (loans and grants to neighbouring countries, paid in tranches against conditions in a memorandum of understanding and only alongside an IMF programme), the EU's balance-of-payments loans to Hungary, Latvia and Romania, and the euro-area rescue programmes for Greece, Ireland, Portugal, Spain and Cyprus. Amounts are the European part only; the IMF's share is in the IMF rows.</p>
<p>Coverage: ${E.length} decisions and programmes, ${Math.min(...E.map((x) => yr(x.d)))} to ${Math.max(...E.map((x) => yr(x.d)))}. Some programmes were agreed in a named month with no day given; they show the month. Where one decision covered several countries, each country's share is listed under it.</p>
<p>The European Stability Mechanism publishes each condition of its programmes, with whether it was met, in a <a href="https://www.esm.europa.eu/financial-assistance/programme-database/conditionality" target="_blank" rel="noopener">conditionality dashboard</a>; it cannot be read from here and is not yet on this map.</p>
<p>Sources: European Commission, report on the implementation of macro-financial assistance in 2025, Annex 2 (<a href="https://data.consilium.europa.eu/doc/document/ST-11024-2026-ADD-1/en/pdf" target="_blank" rel="noopener">Council document ST 11024/26 ADD 1</a>); European Commission, <a href="https://economy-finance.ec.europa.eu/eu-financial-assistance_en" target="_blank" rel="noopener">EU financial assistance</a> country pages.</p>`,
  });

  // ---------------------------------------------------------------- Paris Club agreements
  const PC = D.pc.rows.map((r) => ({ c: r[0], cn: r[1], d: r[2], tr: r[3], st: r[4] }));
  const pcY = (x) => +x.d.slice(-4);
  const pcTr = [...new Set(PC.map((x) => x.tr))].sort();
  const pcKeep = (x, o) => !o.off || !o.off.has(x.tr);
  LAYERS.push({
    id: "pc", lender: "Gov", ramp: "stone", span: [Math.min(...PC.map(pcY)), Math.max(...PC.map(pcY))],
    title: "Paris Club: debt deals with creditor governments",
    short: "Paris Club debt agreements",
    plain: "The Paris Club is a group of creditor governments (the United States, Japan, France, Germany and others) that renegotiate together when a country cannot pay them. They only make a deal if the country is under an IMF programme, so the IMF's conditions come with every agreement.",
    controls: () => checks("tr", { "Kind of deal (“treatment”)": pcTr }, (k) => `${k} (${PC.filter((x) => x.tr === k).length})`),
    unit: (v) => `${num(v)} agreement${v === 1 ? "" : "s"}`,
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const x of PC) {
        if (!pcKeep(x, o) || pcY(x) < from || pcY(x) > to) continue;
        if (x.c && GEO.has(x.c)) out.set(x.c, (out.get(x.c) || 0) + 1); else unplaced.set(x.cn, (unplaced.get(x.cn) || 0) + 1);
      }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = PC.filter((x) => x.c === c && pcKeep(x, o) && pcY(x) >= from && pcY(x) <= to).sort((a, b) => pcY(b) - pcY(a));
      return `<div class="big">${list.length} agreement${list.length === 1 ? "" : "s"}</div>` + list.map((x) => `<div class="item"><b>${esc(x.tr)}</b>${tip("pc_" + x.tr.toLowerCase().replace(/[^a-z]/g, ""))}<br><span class="m">${esc(x.d)} · ${esc(x.st)}</span></div>`).join("");
    },
    srcLine: "Paris Club Secretariat, agreements by debtor country",
    about: `<p>Every agreement the Paris Club lists with each debtor country since 1956: the date, the kind of treatment (the terms, from plain rescheduling to cancelling most of the debt) and whether it has been repaid. The Paris Club's rule of conditionality means each deal is tied to an IMF programme.</p>
<p>Coverage: ${PC.length} agreements with ${new Set(PC.map((x) => x.cn)).size} countries, ${Math.min(...PC.map(pcY))} to ${Math.max(...PC.map(pcY))}. Agreements with the former Yugoslavia are listed under this row.</p>
<p>Source: Paris Club Secretariat (French Treasury), <a href="https://bercy1.applis.finances.gouv.fr/en/agreements-concluded-with-the-paris-club" target="_blank" rel="noopener">Agreements concluded with the Paris Club</a>, by debtor country, read 23 October 2026.</p>`,
  });

  // ---------------------------------------------------------------- China: AidData's record of Chinese official finance
  const CN = D.cn.rows.map((r) => ({ c: r[0], cn: r[1], y: r[2], title: r[3], flow: r[4], cls: r[5], st: r[6], amt: r[7], agg: r[8], col: r[9], ins: r[10], gua: r[11], resc: r[12], bop: r[13], rate: r[14], mat: r[15], grace: r[16], ag: r[17], id: r[18] }));
  const cnFlows = [...new Set(CN.map((x) => x.flow))];
  const cnKeep = (x, o) => (!o.off || !o.off.has(x.flow)) && (!o.only || o.only === "all" || (o.only === "col" ? x.col === "Yes" : o.only === "resc" ? x.resc === "Yes" : o.only === "bop" ? x.bop === "Yes" : x.agg === "Yes"));
  LAYERS.push({
    id: "cn", lender: "Gov", ramp: "rose", span: [Math.min(...CN.filter((x) => x.y).map((x) => x.y)), Math.max(...CN.filter((x) => x.y).map((x) => x.y))],
    title: "China: loans and grants from Chinese state lenders",
    short: "Chinese official lending",
    plain: "Loans and grants from Chinese government banks and agencies to other countries, tracked one by one by the research lab AidData. Chinese loans rarely come with policy conditions like the IMF's; instead many are secured on a country's oil, mining or other income. Use the menu to show only those secured loans, or rescue loans.",
    controls: () => `<select data-k="measure">
        <option value="n">Number of records</option>
        <option value="usd">Amount (US$)</option>
      </select><select data-k="only">
        <option value="all">Every record AidData publishes</option>
        <option value="agg">Only those AidData recommends for totals</option>
        <option value="col">Only loans secured with collateral</option>
        <option value="resc">Only rescue loans</option>
        <option value="bop">Only foreign-exchange and balance-of-payments loans</option>
      </select>` + checks("flow", { "Kind of finance": cnFlows }, (k) => `${k} (${CN.filter((x) => x.flow === k).length})`),
    unit: (v, o) => (o.measure === "usd" ? usd(v) : `${num(v)} record${v === 1 ? "" : "s"}`),
    fmt: (v, o) => (o.measure === "usd" ? usd(v) : num(v)),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const x of CN) {
        if (!cnKeep(x, o) || !x.y || x.y < from || x.y > to) continue;
        const v = o.measure === "usd" ? x.amt || 0 : 1;
        if (x.c && GEO.has(x.c)) out.set(x.c, (out.get(x.c) || 0) + v); else unplaced.set(x.cn, (unplaced.get(x.cn) || 0) + v);
      }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = CN.filter((x) => x.c === c && cnKeep(x, o) && x.y && x.y >= from && x.y <= to).sort((a, b) => b.y - a.y || (b.amt || 0) - (a.amt || 0));
      const series = []; for (let y = Math.max(from, this.span[0]); y <= Math.min(to, this.span[1]); y++) series.push([y, list.filter((x) => x.y === y).length]);
      const yes = (v) => v === "Yes";
      let h = `<div class="big">${num(list.length)} records, ${usd(list.reduce((s, x) => s + (x.amt || 0), 0))}</div>` + bars(series, "#C38591", "records per year");
      h += `<table><tr><td>Secured with collateral${tip("collateral")}</td><td class="n">${list.filter((x) => yes(x.col)).length}</td></tr><tr><td>Rescue loans${tip("rescue")}</td><td class="n">${list.filter((x) => yes(x.resc)).length}</td></tr><tr><td>Insurance required${tip("insurance")}</td><td class="n">${list.filter((x) => yes(x.ins)).length}</td></tr></table>`;
      h += list.map((x) => `<div class="item"><a href="https://china.aiddata.org/projects/${x.id}" target="_blank" rel="noopener">${esc(x.title)}</a><br><span class="m">${x.y} · ${esc(x.flow)} · ${esc(x.st)} · ${x.amt != null ? usd(x.amt) : "amount not given"}${x.rate != null ? ` · interest ${num(x.rate, 2)}%` : ""}${x.mat != null ? ` · ${num(x.mat, 1)} years to repay` : ""}${yes(x.col) ? " · secured with collateral" : ""}${yes(x.resc) ? " · rescue loan" : ""}${x.ag ? " · " + esc(x.ag) : ""}</span></div>`).join("");
      return h;
    },
    srcLine: "AidData, Global Chinese Development Finance Dataset 3.0",
    about: `<p>Every record in AidData's dataset of Chinese government-financed loans and grants to ${new Set(CN.map((x) => x.cn)).size} countries and regions, committed from ${Math.min(...CN.filter((x) => x.y).map((x) => x.y))} to ${Math.max(...CN.filter((x) => x.y).map((x) => x.y))}, with amount, status, lender, terms and whether the loan was secured with collateral or was a rescue loan. AidData marks some records as not for adding up (for example pledges and duplicates of umbrella agreements); the menu can show only the ones it recommends for totals. Amounts are in US dollars at the prices of each year (AidData's adjusted amount where given).</p>
<p>Coverage: ${num(CN.length)} records. Each title links to its AidData page with the sources.</p>
<p>Source: AidData's Global Chinese Development Finance Dataset, Version 3.0 (released 7 November 2023); Custer, S. et al. (2023), <i>Tracking Chinese Development Finance: An Application of AidData's TUFF 3.0 Methodology</i>, AidData at William &amp; Mary; <a href="https://www.aiddata.org/data/aiddatas-global-chinese-development-finance-dataset-version-3-0" target="_blank" rel="noopener">aiddata.org</a>.</p>`,
  });

  // ---------------------------------------------------------------- How China Lends 2.0: clauses in 371 contracts
  const HC = D.hcl.rows.map((r) => Object.fromEntries(D.hcl.cols.map((k, i) => [k, r[i]])));
  const HCM = {
    n: ["Contracts", () => 1], collateral: ["Contracts secured with collateral", (x) => x.collateral === 1],
    confidentiality_general: ["Contracts with a secrecy clause", (x) => x.confidentiality_general === 1],
    paris_clause: ["Contracts that keep the loan out of group debt relief (“no Paris Club”)", (x) => x.paris_clause === 1],
    cross_default: ["Contracts with a cross-default clause", (x) => x.cross_default === 1],
    escrow_account: ["Contracts with an escrow account the lender controls", (x) => x.escrow_account === 1],
  };
  LAYERS.push({
    id: "hcl", lender: "Gov", ramp: "rose", span: [Math.min(...HC.filter((x) => x.year).map((x) => +x.year)), Math.max(...HC.filter((x) => x.year).map((x) => +x.year))],
    title: "China: what its loan contracts require (371 contracts)",
    short: "clauses in Chinese loan contracts",
    plain: "The fine print of 371 loan contracts between Chinese state lenders and borrowers in 60 countries, read clause by clause by researchers. Many require secrecy, let China demand repayment if the country falls out with China or defaults to anyone else, and keep the loan out of any group debt relief.",
    controls: () => `<select data-k="measure">${Object.entries(HCM).map(([k, [t]]) => `<option value="${k}">${esc(t)}</option>`).join("")}</select>`,
    unit: (v) => `${num(v)} contract${v === 1 ? "" : "s"}`,
    values(from, to, o) {
      const f = HCM[o.measure || "n"][1], out = new Map(), unplaced = new Map();
      for (const x of HC) {
        if (!x.year || +x.year < from || +x.year > to) continue;
        const v = f(x) ? 1 : 0;
        if (x.iso3 && GEO.has(x.iso3)) out.set(x.iso3, (out.get(x.iso3) || 0) + v); else unplaced.set(x.borrower_country, (unplaced.get(x.borrower_country) || 0) + v);
      }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = HC.filter((x) => x.iso3 === c && x.year && +x.year >= from && +x.year <= to).sort((a, b) => +b.year - +a.year);
      const yn = (v) => (v === 1 ? "yes" : v === 0 ? "no" : "not known");
      return `<div class="big">${list.length} contract${list.length === 1 ? "" : "s"}</div>` + list.map((x) => `<div class="item"><b>${esc(x.project_title || x.contract_category || x.contract_id)}</b><br>
        <span class="m">${esc(x.year)} · ${esc(x.creditor_name)} to ${esc(x.borrower_name)} · ${x.commitment_USD != null ? usd(+x.commitment_USD) : "amount not given"}</span><br>
        Collateral${tip("collateral")}: ${yn(x.collateral)} · Escrow account${tip("escrow")}: ${yn(x.escrow_account)} · Secrecy clause${tip("secrecy")}: ${yn(x.confidentiality_general)} · No Paris Club${tip("noparis")}: ${yn(x.paris_clause)} · Cross-default${tip("crossdefault")}: ${yn(x.cross_default)}${x.governing_law ? ` · Governing law: ${esc(x.governing_law)}` : ""}
        ${x.paris_clause_des ? `<br><span class="m">No Paris Club clause: ${esc(x.paris_clause_des)}</span>` : ""}${x["cross-default_des"] ? `<br><span class="m">Cross-default: ${esc(x["cross-default_des"])}</span>` : ""}${x.confidentiality_des_borrower ? `<br><span class="m">Secrecy: ${esc(x.confidentiality_des_borrower)}</span>` : ""}
        ${x.source ? `<br><a href="${esc(x.source)}" target="_blank" rel="noopener">The contract</a>` : ""}</div>`).join("");
    },
    srcLine: "AidData, How China Lends Dataset 2.0",
    about: `<p>${HC.length} debt contracts between Chinese state-owned lenders and borrowers abroad, coded clause by clause: collateral and escrow accounts, secrecy (confidentiality) clauses, "no Paris Club" clauses, cross-default clauses, penalty interest, governing law and arbitration. Each links to the contract itself.</p>
<p>Coverage: contracts signed from ${Math.min(...HC.filter((x) => x.year).map((x) => +x.year))} to ${Math.max(...HC.filter((x) => x.year).map((x) => +x.year))}. Counted in the year signed.</p>
<p>Source: Gelpern, A., Haddad, O., Horn, S., Kintzinger, P., Parks, B.C. and Trebesch, C. (2025), <i>How China Lends 2.0: Introducing an extended dataset of 371 debt contracts</i>, AidData at William &amp; Mary; and Gelpern, A., Horn, S., Morris, S., Parks, B. and Trebesch, C. (2023), "How China Lends: A Rare Look into 100 Debt Contracts with Foreign Governments", <i>Economic Policy</i> 38(114): 345–416. Data: <a href="https://www.aiddata.org/data/how-china-lends-dataset-version-2-0" target="_blank" rel="noopener">aiddata.org</a>.</p>`,
  });

  // ---------------------------------------------------------------- Together: every conditional deal on this map, counted
  const ALLK = ["IMF arrangements", "World Bank policy-based loans", "IDB policy-based loans", "EU and euro-area programmes", "Paris Club agreements", "Chinese state loans (AidData)", "Budget support from other lenders (OECD)"];
  const OTHER = (x) => !/^(5IMF|5WB|5IDB|4EU)/.test(x.dn);
  const SRC = [
    (c, f, t) => A.filter((a) => (c === null || a.c === c) && yr(a.ap) >= f && yr(a.ap) <= t).map((a) => [a.c, a.cn]),
    (c, f, t) => W.filter((w) => (c === null || w.c === c) && wDone(w) && yr(w.ap) >= f && yr(w.ap) <= t).map((w) => [w.c, w.cn]),
    (c, f, t) => I.filter((x) => (c === null || x.c === c) && x.ap && yr(x.ap) >= f && yr(x.ap) <= t).map((x) => [x.c, x.cn]),
    (c, f, t) => E.filter((x) => (c === null || x.c === c) && yr(x.d) >= f && yr(x.d) <= t).map((x) => [x.c, x.cn]),
    (c, f, t) => PC.filter((x) => (c === null || x.c === c) && pcY(x) >= f && pcY(x) <= t).map((x) => [x.c, x.cn]),
    (c, f, t) => CN.filter((x) => (c === null || x.c === c) && x.flow === "Loan" && x.y && x.y >= f && x.y <= t).map((x) => [x.c, x.cn]),
    (c, f, t) => O.filter((x) => (c === null || x.c === c) && OTHER(x) && x.y >= f && x.y <= t).map((x) => [x.c, ON[x.c] || x.c]),
  ];
  LAYERS.push({
    id: "all", lender: "All", ramp: "stone", span: [1947, 2026],
    title: "Every lender: deals that came with strings attached",
    short: "conditional deals from every lender",
    plain: "Every loan, rescue or debt deal on this map that came with strings attached, from every lender, added up for each country. Lighter means more deals. Untick a lender to leave it out, and pick any other row for the details.",
    controls: () => checks("lender", { "Count these": ALLK }, (k) => k),
    unit: (v) => `${num(v)} deal${v === 1 ? "" : "s"}`,
    values(from, to, o) {
      const out = new Map(), unplaced = new Map(), on = (k) => !o.off || !o.off.has(k);
      ALLK.forEach((k, i) => { if (!on(k)) return; for (const [c, cn] of SRC[i](null, from, to)) { if (c && GEO.has(c)) out.set(c, (out.get(c) || 0) + 1); else unplaced.set(cn, (unplaced.get(cn) || 0) + 1); } });
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const on = (k) => !o.off || !o.off.has(k);
      const p = ALLK.map((k, i) => (on(k) ? SRC[i](c, from, to).length : 0));
      return `<div class="big">${num(p.reduce((s, v) => s + v, 0))} deals</div><table>${ALLK.map((k, i) => `<tr><td>${k}${tip("all_" + i)}</td><td class="n">${num(p[i])}</td></tr>`).join("")}</table><div class="note">Pick a lender's own row for the list of deals and their conditions.</div>`;
    },
    srcLine: "every lender's row below, added together",
    about: `<p>One count per deal: each IMF arrangement, World Bank policy-based loan, IDB policy-based loan, EU or euro-area programme, Paris Club agreement and Chinese state loan, plus each budget-support payment that other lenders reported to the OECD (Japan, the United States, Germany, Saudi Arabia, the Asian and African Development Banks and the rest; the IMF, World Bank, IDB and EU entries there are left out so they are not counted twice). Untick any of them.</p>
<p>This adds up deals, not conditions: the lenders count conditions in different ways, and most do not publish them at all. The World Bank part ends in December 2024 for loans whose names do not say they are policy loans (see its row); the OECD part covers 2000 to 2025, the Chinese part 2000 to 2021.</p>`,
  });

  // ---------------------------------------------------------------- IMF before 1980: this map's own coding of the board papers
  const EA = D.imfearly.rows.map((r) => Object.fromEntries(D.imfearly.cols.map((k, i) => [k, r[i]])));
  const EKIND = { QPC: "Binding number to hit (a ceiling or floor)", SPC: "Binding policy step or rule", "IB/SB": "Watched target: missing it means talks, not a stop" };
  const eaKeep = (c, o) => !o.off || (!o.off.has(EKIND[c[0]]) && !o.off.has(AREA[c[1]] || c[1]));
  LAYERS.push({
    id: "imfearly", lender: "IMF", ramp: "rose", span: [1952, 1981],
    title: "IMF before 1980: conditions read from its board papers",
    short: "IMF conditions before 1980 (this map's own count)",
    plain: "No database lists the IMF's conditions before 1980, so this map read them from the IMF's own board papers: for each loan, the clause that says when the money stops, and the targets it points to. Counted by this map, not by the IMF.",
    controls: () => checks("ek", { "Kind of condition": Object.values(EKIND), "Policy area": [...new Set(EA.flatMap((a) => a.conds.map((c) => AREA[c[1]] || c[1])))].sort() }, (k) => k),
    unit: (v) => `${num(v)} condition${v === 1 ? "" : "s"}`,
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const a of EA) {
        const y = +a.approved.slice(0, 4); if (y < from || y > to) continue;
        const n = a.conds.filter((c) => eaKeep(c, o)).length;
        if (a.iso3 && GEO.has(a.iso3)) out.set(a.iso3, (out.get(a.iso3) || 0) + n); else unplaced.set(a.country, (unplaced.get(a.country) || 0) + n);
      }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = EA.filter((a) => a.iso3 === c && +a.approved.slice(0, 4) >= from && +a.approved.slice(0, 4) <= to).sort((a, b) => b.approved.localeCompare(a.approved));
      const tot = list.reduce((s, a) => s + a.conds.filter((x) => eaKeep(x, o)).length, 0);
      return `<div class="big">${num(tot)} conditions in ${list.length} loan${list.length === 1 ? "" : "s"}</div><div class="note">Counted by this map from the IMF's board papers${tip("early")}</div>` +
        list.map((a) => `<div class="item"><b>${esc(a.facility)}</b>, approved ${esc(a.approved)}<br><span class="m">${esc(a.status === "Coded" ? "Conditions found in the papers" : a.status)}${a.conds.length ? ` · ${a.conds.filter((x) => eaKeep(x, o)).length} conditions` : ""}</span>` +
          (a.conds.length ? `<table>${a.conds.filter((x) => eaKeep(x, o)).map((x) => `<tr><td>${esc(EKIND[x[0]] || x[0])}${tip("e_" + x[0].replace("/", ""))}<br><span class="m">${esc(AREA[x[1]] || x[1])}${x[2] != null ? ` · paragraph ${x[2]}` : ""}</span></td></tr><tr><td class="m">${esc(x[3])}</td></tr>`).join("")}</table>` : "") +
          (a.clause ? `<details class="tx"><summary>The clause that stops the money, as written</summary><div class="txt">${esc(a.clause)}</div></details>` : "") +
          a.docs.map((d) => `<a href="${esc(d[2])}" target="_blank" rel="noopener">${esc(d[0])}: ${esc(d[1])}</a>`).join("<br>") + `</div>`).join("");
    },
    srcLine: "IMF Archives, Executive Board papers; counted by this map",
    about: `<p>The IMF's own condition records (the MONA database, and the IMF Monitor data on the other IMF row) start in 1980 or later. For the ${num(EA.length)} IMF loans approved from 1952 to 1979 that this row covers, this map found the IMF Executive Board papers in the IMF Archives (the request paper with the government's letter, and the final text of the arrangement) and read the conditions from them. This is the map's own coding, not the IMF's.</p>
<p>The rule. Each arrangement's text has a clause saying when the government may not draw more money, or must first consult the IMF: "During any period of the stand-by arrangement in which (1) the ceilings on credit … are exceeded, or (2) … ". Each item in that clause, and each paragraph of the government's letter it points to, counts as one condition. Items in a clause that stops the money are binding: a number to hit (a ceiling, a floor, a target) or a policy rule (no new exchange restrictions, a reform carried out). Items in a clause that only calls for talks are counted as watched targets. Each condition's policy area comes from the words of the item, or from the opening of the paragraph it points to. Loans in the first credit tranche carried no such clause, by IMF policy then, and show none.</p>
<p>How far to trust it. The papers are typewritten scans read by machine, so some wording is garbled, and the rule can miss or misplace items. Every loan lists the clause as written and links the papers, so each count can be checked. ${num(EA.filter((a) => /^Papers found/.test(a.status)).length)} loans have papers that set out no list this rule can count (they are listed, with their papers, for reading); ${num(EA.filter((a) => /^No board/.test(a.status)).length)} have no papers found in the archive.</p>
<p>Source: International Monetary Fund Archives, Executive Board documents (EBS series), <a href="https://archivescatalog.imf.org/" target="_blank" rel="noopener">archivescatalog.imf.org</a>, read October 2026.</p>`,
  });

  // ---------------------------------------------------------------- IMF: MONA, every structural condition and prior action with whether it was met
  const MO = D.mona.rows.map((r) => Object.fromEntries(D.mona.cols.map((k, i) => [k, r[i]])));
  const MSTAT = { M: "Met", NM: "Not met", PM: "Partially met", DL: "Delayed", PC: "Still outstanding at the review", SB: "Still outstanding at the review", PA: "Still outstanding at the review", W: "Waived", MOD: "Modified" };
  const mStat = (s) => (MSTAT[s] ? MSTAT[s] : /^W?MOD/.test(s) ? (s[0] === "W" ? "Waived and modified" : "Modified") : s);
  const mGroup = (s) => (s === "M" ? "Met" : s === "NM" ? "Not met" : s === "PM" ? "Partially met" : s === "W" ? "Waived" : /MOD/.test(s) ? "Modified (date or type changed)" : ["SB", "PC", "PA"].includes(s) ? "Still outstanding" : "Other codes, as the IMF gives them (" + s + ")");
  const mKinds = { SB: "Structural benchmark", PA: "Prior action", SPC: "Structural performance criterion", SAC: "SAC (code as the IMF gives it; not defined in its labels)" };
  const mGroups = [...new Set(MO.map((x) => mGroup(x.status)))].sort();
  const mAreas = [...new Set(MO.map((x) => x.area))].sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
  const mKeep = (x, o) => (!o.off || (!o.off.has(mKinds[x.kind] || x.kind) && !o.off.has(mGroup(x.status)))) && (!o.area || o.area === "all" || o.area === x.area);
  LAYERS.push({
    id: "mona", lender: "IMF", ramp: "rose", span: D.mona.years,
    title: "IMF: every reform condition since 2000, and whether it was met",
    short: "IMF reform conditions (MONA)",
    plain: "Every reform the IMF required in its programs from 2000 to now, word for word, with what happened at each later check: met, not met, partly met, put off, waived or changed. These are the reform conditions (laws, privatizations, tax and budget changes), not the numeric targets.",
    controls: () => `<select data-k="area"><option value="all">Every policy area</option>${mAreas.map((a) => `<option value="${esc(a)}">${esc(a)}</option>`).join("")}</select>` +
      checks("kind", { "Kind of condition": Object.keys(mKinds).filter((k) => MO.some((x) => x.kind === k)) }, (k) => `${mKinds[k]} (${MO.filter((x) => x.kind === k).length})`, (k) => mKinds[k]) +
      checks("status", { "What happened (last check)": mGroups }, (g) => `${g} (${MO.filter((x) => mGroup(x.status) === g).length})`),
    unit: (v) => `${num(v)} condition${v === 1 ? "" : "s"}`,
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const x of MO) {
        if (!mKeep(x, o) || x.year < from || x.year > to) continue;
        if (x.iso3 && GEO.has(x.iso3)) out.set(x.iso3, (out.get(x.iso3) || 0) + 1); else unplaced.set(x.country, (unplaced.get(x.country) || 0) + 1);
      }
      for (const x of MO) if (x.iso3 && GEO.has(x.iso3) && !out.has(x.iso3) && x.year >= from && x.year <= to) out.set(x.iso3, 0);
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = MO.filter((x) => x.iso3 === c && mKeep(x, o) && x.year >= from && x.year <= to).sort((a, b) => b.year - a.year);
      const series = []; for (let y = Math.max(from, this.span[0]); y <= Math.min(to, this.span[1]); y++) series.push([y, list.filter((x) => x.year === y).length]);
      const cnt = groupBy(list, (x) => mGroup(x.status));
      let h = `<div class="big">${num(list.length)} conditions</div>` + bars(series, "#C38591", "conditions due per year");
      h += `<table>${Object.entries(cnt).sort((a, b) => b[1].length - a[1].length).map(([g, xs]) => `<tr><td>${esc(g)}${tip("ms_" + g.slice(0, 6).toLowerCase().replace(/[^a-z]/g, ""))}</td><td class="n">${xs.length}</td></tr>`).join("")}</table>`;
      h += list.map((x) => `<div class="item">${esc(x.text)}<br><span class="m">${esc(mKinds[x.kind] || x.kind)}${tip({ SB: "SBsTOT", PA: "PAsTOT", SPC: "SPCsTOT" }[x.kind])} · due ${esc(x.due)} · ${esc(x.area)} · ${esc(x.arrtype)} approved ${esc(x.approved)}</span><br>Last check: <b>${esc(mStat(x.status))}</b> <span class="m">(${esc(x.status)})</span><details class="tx"><summary>Status at each review</summary><div class="m">${esc(x.history)}</div>${x.comment ? `<div class="m">IMF comment: ${esc(x.comment)}</div>` : ""}</details></div>`).join("");
      return h;
    },
    srcLine: "IMF, Monitoring of Fund Arrangements (MONA)",
    about: `<p>Every structural performance criterion, prior action and structural benchmark in the IMF's MONA database, which covers arrangements approved from 2000 onward. MONA repeats each condition at every review, with its status then; this map shows each condition once, with its wording, its type, its due date as the IMF writes it, its status at the last review that lists it, and its status at every review (open "Status at each review"). Conditions whose type changed (for example a benchmark made a prior action) appear under each type.</p>
<p>Coverage: ${num(MO.length)} conditions, from ${num(D.mona.rows_in_file)} rows in the file, due ${D.mona.years[0]} to ${D.mona.years[1]}. Counted in the year due; where there is no date (prior actions, "continuous") or the date is mistyped in the file (two rows), in the year of the IMF board meeting where the condition first appears.</p>
<p>Status codes: the IMF defines M (met), NM (not met), PM (partially met), DL (delayed), and PC or SB (still outstanding at the review); for numeric targets it defines W (waived) and MOD (modified). Other codes in the file (such as MD, CAN, AC, WC) are not defined in the IMF's labels and are shown as given.</p>
<p>Source: International Monetary Fund, Monitoring of Fund Arrangements (MONA) database, "Combined SPC PA SB" table, full dataset 2002 to current, <a href="https://www.imf.org/mona/arrangements" target="_blank" rel="noopener">imf.org/mona</a>, downloaded 24 October 2026; column definitions from the IMF's MONA labels and descriptions page.</p>`,
  });

  // ---------------------------------------------------------------- country-by-year series (World Bank, OECD)
  const SER = D.ser;
  function aggOf(s, from, to, agg) {
    if (!s) return null;
    let sum = 0, n = 0, last = null, ly = null;
    for (const [y, v] of Object.entries(s)) { const yy = +y; if (yy < from || yy > to) continue; sum += v; n++; if (ly === null || yy > ly) { ly = yy; last = v; } }
    if (!n) return null;
    return agg === "sum" ? { v: sum, n } : agg === "mean" ? { v: sum / n, n } : { v: last, y: ly };
  }
  const fmtU = (u, v) => (u === "pct" ? `${num(v, 1)}%` : usd(v));
  function seriesLayer(cfg) {
    const M = Object.fromEntries(cfg.measures.map((m) => [m.key, m]));
    return Object.assign({
      span: cfg.span, cont: true,
      controls: () => `<select data-k="measure">${cfg.measures.map((m) => `<option value="${m.key}">${esc(m.label)}</option>`).join("")}</select>` + (cfg.moreControls ? cfg.moreControls() : ""),
      unit: (v, o) => fmtU(M[o.measure || cfg.measures[0].key].unit, v),
      fmt: (v, o) => fmtU(M[o.measure || cfg.measures[0].key].unit, v),
      values(from, to, o) {
        const m = M[o.measure || cfg.measures[0].key], s = SER[m.key] || {}, out = new Map();
        for (const [c, ys] of Object.entries(s)) { const a = aggOf(ys, from, to, m.agg); if (a && GEO.has(c)) out.set(c, a.v); }
        return { values: out, unplaced: new Map(), noTotal: m.agg !== "sum" };
      },
      popup(c, from, to, o) {
        const m = M[o.measure || cfg.measures[0].key], s = (SER[m.key] || {})[c] || {};
        const series = []; for (let y = Math.max(from, cfg.span[0]); y <= Math.min(to, cfg.span[1]); y++) series.push([y, s[y] != null ? Math.max(0, s[y]) : 0]);
        const a = aggOf(s, from, to, m.agg);
        let h = `<div class="big">${a ? fmtU(m.unit, a.v) : "No figure in these years"}</div><div class="note">${esc(m.label)}${a ? (m.agg === "sum" ? `, added up over ${a.n} year${a.n === 1 ? "" : "s"}` : m.agg === "mean" ? `, average of ${a.n} year${a.n === 1 ? "" : "s"}` : `, in ${a.y}`) : ""}</div>`;
        h += bars(series.map(([y, v]) => [y, Math.round(m.unit === "pct" ? v * 10 : v / 1e6) / (m.unit === "pct" ? 10 : 1)]), "#7697B2", m.unit === "pct" ? "% per year" : "US$ million per year");
        h += `<table>${cfg.measures.map((mm) => { const aa = aggOf((SER[mm.key] || {})[c], from, to, mm.agg); return `<tr><td>${esc(mm.label)}${tip(mm.tip || "")}</td><td class="n">${aa ? fmtU(mm.unit, aa.v) + (mm.agg === "last" ? ` (${aa.y})` : "") : "–"}</td></tr>`; }).join("")}</table>`;
        if (cfg.extraPopup) h += cfg.extraPopup(c, from, to, o);
        return h;
      },
    }, cfg);
  }
  const wdiSrc = (codes) => `World Bank, World Development Indicators and International Debt Statistics, series ${codes.map((c) => `<a href="https://data.worldbank.org/indicator/${c}" target="_blank" rel="noopener">${c}</a>`).join(", ")}, read through the World Bank data API on 24 October 2026 (data last updated ${esc((D.ser_meta[codes[0]] || {}).updated || "")}).`;
  const AGGNOTE = "Over a range of years, flows (money moving in a year) are added up, shares are averaged over the years with figures, and debts owed are shown for the latest year in the range.";

  // Foreign direct investment
  LAYERS.push(seriesLayer({
    id: "fdi", lender: "Flows", ramp: "slate", span: [1970, 2025],
    title: "Private investment: foreign companies buying in (FDI)",
    short: "foreign direct investment",
    plain: "Foreign direct investment is when a company from abroad buys at least a tenth of a business here, or builds one, and gets a say in running it. Your page puts it at about half of all money going into poorer countries.",
    measures: [
      { key: "BX.KLT.DINV.CD.WD", label: "Investment coming in from abroad (US$)", agg: "sum", unit: "usd", tip: "fdi_in" },
      { key: "BX.KLT.DINV.WD.GD.ZS", label: "Investment coming in, as a share of the economy (% of GDP)", agg: "mean", unit: "pct", tip: "gdp" },
      { key: "BM.KLT.DINV.CD.WD", label: "Investment going out: this country's companies buying abroad (US$)", agg: "sum", unit: "usd", tip: "fdi_out" },
    ],
    srcLine: "World Bank, World Development Indicators",
    about: `<p>Net foreign direct investment coming into each country, and going out of it, by year, in US dollars at the prices of each year, from balance-of-payments figures. "Net" means new investment minus investment pulled out, so a year can be negative. ${AGGNOTE}</p>
<p>Profits that foreign owners take back out are not shown here; the World Bank does not publish them by country in this series. For where investment is routed through tax havens, see the Offshore FDI atlas linked on your page.</p><p>Source: ${wdiSrc(["BX.KLT.DINV.CD.WD", "BX.KLT.DINV.WD.GD.ZS", "BM.KLT.DINV.CD.WD"])}</p>`,
  }));

  // Aid received, with grants by donor
  const GD = D.grants.donors, GBR = D.grants.by_recipient;
  LAYERS.push(seriesLayer({
    id: "aid", lender: "Flows", ramp: "sage", span: [1960, 2024],
    title: "Grants and gifts: aid received from governments and agencies",
    short: "aid received",
    plain: "Official aid a country received: grants that never have to be paid back, and cheap loans, from foreign governments, the EU, the UN and development banks. Click a country to see which donors gave it grants.",
    measures: [
      { key: "DT.ODA.ODAT.CD", label: "Aid received, after repayments (US$)", agg: "sum", unit: "usd", tip: "oda" },
      { key: "DT.ODA.ODAT.GN.ZS", label: "Aid received as a share of national income (% of GNI)", agg: "mean", unit: "pct", tip: "gni" },
      { key: "BX.GRT.EXTA.CD.WD", label: "Grants, not counting technical help (US$)", agg: "sum", unit: "usd" },
      { key: "BX.GRT.TECH.CD.WD", label: "Grants paid as technical help and advisers (US$)", agg: "sum", unit: "usd", tip: "tc" },
    ],
    extraPopup(c, from, to) {
      const rows = (GBR[c] || []).filter((r) => r[1] >= from && r[1] <= to);
      if (!rows.length) return `<div class="note">No grants by donor recorded for these years (the OECD's donor-by-donor figures start in 2002).</div>`;
      const by = {}; for (const [d, , v] of rows) by[d] = (by[d] || 0) + v;
      return `<h4>Grants by donor, ${Math.max(from, 2002)} to ${Math.min(to, 2024)}${tip("grants_by_donor")}</h4><table>${Object.entries(by).sort((a, b) => b[1] - a[1]).map(([d, v]) => `<tr><td>${esc(GD[d][1])}</td><td class="n">${usd(v * 1e6)}</td></tr>`).join("")}</table>`;
    },
    srcLine: "World Bank, World Development Indicators; OECD Creditor Reporting System",
    about: `<p>Net official development assistance received (grants plus cheap loans, minus loan repayments), and grants alone, by year. ${AGGNOTE} Each country's box lists the grants it received from each donor government and agency, from the OECD's records (2002 onward, grants paid out, US dollars at the prices of each year).</p>
<p>Source: ${wdiSrc(["DT.ODA.ODAT.CD", "DT.ODA.ODAT.GN.ZS", "BX.GRT.EXTA.CD.WD", "BX.GRT.TECH.CD.WD"])} Grants by donor: OECD Creditor Reporting System, ODA grants (measure 11), gross disbursements, all sectors, read through the <a href="https://sdmx.oecd.org/dcd-public/rest/" target="_blank" rel="noopener">OECD data API</a> on 24 October 2026; groups of donors are left out so nothing is counted twice.</p>`,
  }));

  // Tied aid, by donor country
  const TD = D.tied.by_donor, TN = D.tied.names;
  const tiedSum = (d, from, to, k) => { let s = 0, n = 0; for (const [y, v] of Object.entries(TD[d] || {})) if (+y >= from && +y <= to && v[k] != null) { s += v[k]; n++; } return n ? s : null; };
  LAYERS.push({
    id: "tied", lender: "Flows", ramp: "plum", span: [1979, 2022], cont: true,
    title: "Grants and gifts: aid tied to buying from the donor",
    short: "tied aid, by donor country",
    plain: "Tied aid must be spent on the donor country's own goods and services, so much of the money goes back home to its companies. This map colours the donor countries, by the share of their aid that came tied.",
    controls: () => `<select data-k="measure"><option value="tied">Share tied (% of aid committed)</option><option value="partial">Share partly tied (% of aid committed)</option><option value="tiedusd">Amount tied (US$)</option></select>`,
    unit: (v, o) => (o.measure === "tiedusd" ? usd(v * 1e6) : `${num(v, 1)}%`),
    fmt: (v, o) => (o.measure === "tiedusd" ? usd(v * 1e6) : `${num(v, 1)}%`),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const d of Object.keys(TD)) {
        const all = tiedSum(d, from, to, "74_500"), t = tiedSum(d, from, to, "74_530"), p = tiedSum(d, from, to, "74_520");
        if (all == null) continue;
        const v = o.measure === "tiedusd" ? t || 0 : o.measure === "partial" ? (all ? (100 * (p || 0)) / all : null) : (all ? (100 * (t || 0)) / all : null);
        if (v == null) continue;
        if (GEO.has(d)) out.set(d, v); else if (o.measure === "tiedusd") unplaced.set(TN[d] || d, v);
      }
      return { values: out, unplaced, noTotal: o.measure !== "tiedusd" };
    },
    popup(c, from, to) {
      const ys = Object.entries(TD[c] || {}).filter(([y]) => +y >= from && +y <= to).sort((a, b) => b[0] - a[0]);
      if (!ys.length) return `<div class="note">This country is not a donor in the OECD's tied-aid records for these years.</div>`;
      return `<div class="note">Bilateral aid committed, US$ million, by whether it is tied${tip("tied")}</div><table><tr><td>Year</td><td class="n">All</td><td class="n">Untied</td><td class="n">Partly untied</td><td class="n">Tied</td></tr>${ys.map(([y, v]) => `<tr><td>${y}</td><td class="n">${num(v["74_500"], 1)}</td><td class="n">${num(v["74_510"], 1)}</td><td class="n">${num(v["74_520"], 1)}</td><td class="n">${num(v["74_530"], 1)}</td></tr>`).join("")}</table>`;
    },
    srcLine: "OECD, DAC7b: tying status of aid",
    about: `<p>For each donor country that reports to the OECD, how much of the bilateral aid it committed was untied, partly untied or tied, by year. The shares are worked out here from the OECD's figures: tied (or partly untied) commitments divided by all bilateral commitments in the chosen years. ${"Technical co-operation and administrative costs are included or not as the OECD reports them."}</p>
<p>Source: OECD, DAC7b, Aid (ODA) tying status (dataflow DSD_DAC1@DF_DAC7B 1.1), current prices, read through the <a href="https://sdmx.oecd.org/public/rest/" target="_blank" rel="noopener">OECD data API</a> on 24 October 2026.</p>`,
  });

  // Private foundations
  const PD = D.ppfd.donors, PBR = D.ppfd.by_recipient;
  const pKeep = (d, o) => !o.off || !o.off.has(PD[d][1]);
  LAYERS.push({
    id: "found", lender: "Flows", ramp: "sage", span: [2009, 2024], cont: true,
    title: "Grants and gifts: private foundations",
    short: "private foundations' grants",
    plain: "Grants from private foundations, such as the Gates Foundation and the Mastercard Foundation, to each country, as the foundations report them to the OECD. Untick a foundation to leave it out.",
    controls: () => checks("fd", { "Foundations": PD.map((p, i) => i) }, (i) => PD[i][1], (i) => PD[i][1]),
    unit: (v) => usd(v * 1e6), fmt: (v) => usd(v * 1e6),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const [c, rows] of Object.entries(PBR)) { let s = 0; for (const [d, y, v] of rows) if (y >= from && y <= to && pKeep(d, o)) s += v; if (s && GEO.has(c)) out.set(c, s); }
      for (const [n, rows] of Object.entries(D.ppfd.unplaced)) { let s = 0; for (const [d, y, v] of rows) if (y >= from && y <= to && pKeep(d, o)) s += v; if (s) unplaced.set(n, s); }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const rows = (PBR[c] || []).filter((r) => r[1] >= from && r[1] <= to && pKeep(r[0], o));
      const by = {}; for (const [d, , v] of rows) by[d] = (by[d] || 0) + v;
      return `<div class="big">${usd(rows.reduce((s, r) => s + r[2], 0) * 1e6)}</div><table>${Object.entries(by).sort((a, b) => b[1] - a[1]).map(([d, v]) => `<tr><td>${esc(PD[d][1])}</td><td class="n">${usd(v * 1e6)}</td></tr>`).join("")}</table>`;
    },
    srcLine: "OECD, Private Philanthropy for Development",
    about: `<p>Grants paid by the private foundations that report to the OECD, to each country, by year, in US dollars at the prices of each year. Grants to regions or to many countries at once are listed under this row.</p>
<p>Source: OECD, Private Philanthropy for Development (dataflow DSD_PPFD@DF_PPFD 1.7), all sectors, total, disbursements, current prices, read through the <a href="https://sdmx.oecd.org/dcd-public/rest/" target="_blank" rel="noopener">OECD data API</a> on 24 October 2026.</p>`,
  });

  // Private loans and bilateral loans: debt by kind of lender
  const DEBTM = [
    { key: "DT.DOD.PRVT.CD", label: "Owed by the government to private lenders (US$)", agg: "last", unit: "usd", tip: "ppg" },
    { key: "DT.DOD.PBND.CD", label: "… of which bonds (US$)", agg: "last", unit: "usd", tip: "bonds" },
    { key: "DT.DOD.PCBK.CD", label: "… of which commercial banks (US$)", agg: "last", unit: "usd" },
    { key: "DT.DOD.PROP.CD", label: "… of which other private lenders (US$)", agg: "last", unit: "usd" },
    { key: "DT.DOD.DPNG.CD", label: "Owed by private companies abroad, without a government guarantee (US$)", agg: "last", unit: "usd", tip: "png" },
    { key: "DT.TDS.PRVT.CD", label: "Paid to private lenders: repayments plus interest (US$)", agg: "sum", unit: "usd" },
    { key: "DT.INT.PRVT.CD", label: "Interest paid to private lenders (US$)", agg: "sum", unit: "usd" },
  ];
  const BILM = [
    { key: "DT.DOD.BLAT.CD", label: "Owed by the government to other governments (US$)", agg: "last", unit: "usd", tip: "bilateral" },
    { key: "DT.TDS.BLAT.CD", label: "Paid to other governments: repayments plus interest (US$)", agg: "sum", unit: "usd" },
    { key: "DT.INT.BLAT.CD", label: "Interest paid to other governments (US$)", agg: "sum", unit: "usd" },
    { key: "DT.DOD.MLAT.CD", label: "For comparison: owed to the IMF, World Bank and other multilateral lenders (US$)", agg: "last", unit: "usd", tip: "multilateral" },
    { key: "DT.TDS.MLAT.CD", label: "For comparison: paid to multilateral lenders (US$)", agg: "sum", unit: "usd" },
    { key: "DT.TDS.DECT.GN.ZS", label: "All foreign debt payments as a share of national income (% of GNI)", agg: "mean", unit: "pct", tip: "gni" },
  ];
  LAYERS.push(seriesLayer({
    id: "priv", lender: "Flows", ramp: "rose", span: [1970, 2024],
    title: "Private loans: debt owed to banks and bondholders",
    short: "debt owed to private lenders",
    plain: "Money the government (and private companies) owe abroad to banks, investment funds and bondholders. These loans cost more than official ones, and are enforced in rich countries' courts. Covers the low- and middle-income countries the World Bank tracks.",
    measures: DEBTM,
    srcLine: "World Bank, International Debt Statistics",
    about: `<p>Long-term foreign debt owed to private lenders by the government and the bodies it guarantees, split into bonds, commercial banks and other private lenders, plus debt owed by private companies without a government guarantee; and what was paid each year to private lenders. ${AGGNOTE} Only the low- and middle-income countries that report to the World Bank's Debtor Reporting System are covered.</p><p>Source: ${wdiSrc(DEBTM.map((m) => m.key))}</p>`,
  }));
  LAYERS.push(seriesLayer({
    id: "bilat", lender: "Flows", ramp: "plum", span: [1970, 2024],
    title: "Bilateral loans: debt owed to other governments",
    short: "debt owed to other governments",
    plain: "Loans from one government straight to another (from China, Japan, France, Saudi Arabia and so on), as opposed to loans through the IMF or World Bank. Click a country to see which governments it owes, where the World Bank publishes it.",
    measures: BILM,
    extraPopup(c, from, to) {
      const B = D.bilat && D.bilat[c]; if (!B) return "";
      let ly = null; for (const r of B) if (r[1] <= to && r[1] >= from && (ly === null || r[1] > ly)) ly = r[1];
      if (ly === null) return "";
      const rows = B.filter((r) => r[1] === ly).sort((a, b) => b[2] - a[2]);
      return `<h4>Owed to each government, ${ly}</h4><table>${rows.map((r) => `<tr><td>${esc(D.bilatNames[r[0]] || r[0])}</td><td class="n">${usd(r[2])}</td></tr>`).join("")}</table>`;
    },
    srcLine: "World Bank, International Debt Statistics",
    about: `<p>Long-term foreign debt the government and the bodies it guarantees owe to other governments and their agencies, and what was paid to them each year, with debt to multilateral lenders shown for comparison. ${AGGNOTE} Where the World Bank publishes it, each country's box lists how much is owed to each creditor government in the latest year of the range. Only the low- and middle-income countries in the World Bank's Debtor Reporting System are covered.</p><p>Source: ${wdiSrc(BILM.map((m) => m.key))}</p>`,
  }));

  // Interest compared with health and education
  LAYERS.push(seriesLayer({
    id: "interest", lender: "Flows", ramp: "rose", span: [1972, 2025],
    title: "Debt payments against health and education",
    short: "interest compared with health and education spending",
    plain: "How much of the government's spending goes on interest, next to how much goes on health and on schools. Your page cites the UN finding that 3.4 billion people live in countries that spend more on interest than on health or education.",
    measures: [
      { key: "GC.XPN.INTP.ZS", label: "Interest, as a share of government spending (%)", agg: "mean", unit: "pct", tip: "interest_exp" },
      { key: "SH.XPD.GHED.GE.ZS", label: "Health, as a share of government spending (%)", agg: "mean", unit: "pct" },
      { key: "SE.XPD.TOTL.GB.ZS", label: "Education, as a share of government spending (%)", agg: "mean", unit: "pct" },
    ],
    srcLine: "World Bank, World Development Indicators",
    about: `<p>Three shares of government spending, each averaged over the years with figures in the chosen range: interest payments (as a share of government expense), the government's own health spending (share of general government spending) and education spending (share of government spending). They come from different collections (the IMF, the WHO and UNESCO through the World Bank) and are measured slightly differently, so set them side by side, not to the decimal.</p><p>Source: ${wdiSrc(["GC.XPN.INTP.ZS", "SH.XPD.GHED.GE.ZS", "SE.XPD.TOTL.GB.ZS"])}</p>`,
  }));

  // Remittances
  LAYERS.push(seriesLayer({
    id: "remit", lender: "Flows", ramp: "sage", span: [1970, 2025],
    title: "Money sent home by people working abroad",
    short: "remittances received",
    plain: "Money that people working in other countries send home to their families. For many poor countries it is bigger than aid and foreign investment together.",
    measures: [
      { key: "BX.TRF.PWKR.CD.DT", label: "Money sent home (US$)", agg: "sum", unit: "usd" },
      { key: "BX.TRF.PWKR.DT.GD.ZS", label: "Money sent home, as a share of the economy (% of GDP)", agg: "mean", unit: "pct", tip: "gdp" },
    ],
    srcLine: "World Bank, World Development Indicators",
    about: `<p>Personal remittances received: money sent home by workers abroad and by people who moved abroad, by year. ${AGGNOTE}</p><p>Source: ${wdiSrc(["BX.TRF.PWKR.CD.DT", "BX.TRF.PWKR.DT.GD.ZS"])}</p>`,
  }));

  // Saudi Arabia and Qatar
  const TU = D.tuff.rows.map((r) => Object.fromEntries(D.tuff.cols.map((k, i) => [k, r[i]])));
  const tuDon = [...new Set(TU.map((x) => x.donor))], tuFlow = [...new Set(TU.map((x) => x.flow))];
  const tuKeep = (x, o) => !o.off || (!o.off.has(x.donor) && !o.off.has(x.flow));
  LAYERS.push({
    id: "tuff", lender: "Gov", ramp: "stone", span: [Math.min(...TU.filter((x) => x.year).map((x) => x.year)), Math.max(...TU.filter((x) => x.year).map((x) => x.year))],
    title: "Saudi Arabia and Qatar: aid and loans tracked by AidData",
    short: "Saudi and Qatari official finance",
    plain: "Aid, loans and gifts from Saudi Arabia and Qatar, which report little to the OECD, pieced together one record at a time by AidData from news reports and government sources.",
    controls: () => `<select data-k="measure"><option value="n">Number of records</option><option value="usd">Amount (US$)</option></select>` + checks("d", { Donor: tuDon, "Kind of finance": tuFlow }, (k) => `${k} (${TU.filter((x) => x.donor === k || x.flow === k).length})`),
    unit: (v, o) => (o.measure === "usd" ? usd(v) : `${num(v)} record${v === 1 ? "" : "s"}`),
    fmt: (v, o) => (o.measure === "usd" ? usd(v) : num(v)),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map();
      for (const x of TU) {
        if (!tuKeep(x, o) || !x.year || x.year < from || x.year > to) continue;
        const v = o.measure === "usd" ? x.usd || 0 : 1;
        if (x.iso3 && GEO.has(x.iso3)) out.set(x.iso3, (out.get(x.iso3) || 0) + v); else unplaced.set(x.recipient, (unplaced.get(x.recipient) || 0) + v);
      }
      return { values: out, unplaced };
    },
    popup(c, from, to, o) {
      const list = TU.filter((x) => x.iso3 === c && tuKeep(x, o) && x.year && x.year >= from && x.year <= to).sort((a, b) => b.year - a.year);
      return `<div class="big">${list.length} record${list.length === 1 ? "" : "s"}</div>` + list.map((x) => `<div class="item">${esc(x.title)}<br><span class="m">${esc(x.donor)} · ${x.year}${x.year_uncertain ? " (year uncertain)" : ""} · ${esc(x.flow)} · ${esc(x.status)} · ${x.usd != null ? usd(x.usd) : "amount not given"} · ${esc(x.sector)} · AidData id ${esc(x.id)}</span></div>`).join("");
    },
    srcLine: "AidData, TUFF donor datasets (Saudi Arabia, Qatar)",
    about: `<p>Every record in AidData's Saudi Arabia and Qatar donor datasets (Level 1, version 1.0), built with its Tracking Underreported Financial Flows (TUFF) method: title, year, kind of finance, status, amount where known, and sector. Records shared among several countries are listed under this row.</p>
<p>Coverage: ${TU.length} records. Source: AidData at William &amp; Mary, <a href="https://www.aiddata.org/data/saudi-arabia-tuff-donor-dataset-level-1-v1-0" target="_blank" rel="noopener">Saudi Arabia TUFF Donor Dataset</a> and <a href="https://www.aiddata.org/data/qatar-tuff-donor-dataset-level-1-v1-0" target="_blank" rel="noopener">Qatar TUFF Donor Dataset</a>.</p>`,
  });


  /* ------------------------------------------------------------ plain-language explanations, shown on hover or tap */
  const TERMS = {
    QPCsTOT: "A number the government must hit by a set date, such as a cap on borrowing or a minimum level of reserves. If it is missed, the money stops unless the IMF board excuses it.",
    PAsTOT: "A step the government must take before the IMF board will even approve the loan or the next payment, such as passing a law or raising a price.",
    SPCsTOT: "A reform the government must finish by a set date for payments to continue. The IMF stopped using these in 2009.",
    IBsTOT: "A number the IMF watches, such as a spending level, but missing it does not stop the money by itself.",
    SBsTOT: "A reform the IMF watches, such as drafting a law, but missing it does not stop the money by itself.",
    binding: "Binding conditions are the ones that stop the money if they are missed, unless the lender's board excuses them.",
    every: "Every condition counts both kinds: the binding ones and the benchmarks the IMF only watches.",
    BA1DEB: "Conditions on paying and managing the country's foreign debt, including clearing unpaid debts.", BA1FIN: "Conditions on banks, interest rates, the central bank and the amount of money in the economy.",
    BA1FP: "Conditions on government spending, budgets and the budget deficit.", BA1RTP: "Conditions on taxes: what is taxed, how much, and how taxes are collected.",
    BA1EXT: "Conditions on trade, the exchange rate, foreign reserves and money moving in and out of the country.", BA1SOE: "Conditions on companies the state owns: restructuring them, cutting their subsidies, raising the prices they charge.",
    BA1PRI: "Conditions to sell state-owned companies to private owners, or close them.", BA1LAB: "Conditions on wages, public-sector jobs, pensions and social security.",
    BA1INS: "Conditions on courts, competition rules, business rules, land titles and how government works.", BA1ENV: "Conditions touching the environment and access to shared land, water or forests.",
    BA1SP: "Conditions on social policies such as health and education, other than poverty programmes.", BA1POV: "Conditions meant to protect the poor: minimum social spending, safety-net programmes, poverty plans.", BA1OTH: "Conditions that fit no other group.",
    sdr: "The IMF's own unit of money, made from a basket of the world's main currencies (the dollar, euro, yuan, yen and pound).",
    concessional: "Low-interest loans with long repayment times, for the poorest countries.", nonconcessional: "Loans at the IMF's regular interest rate, for middle- and high-income countries.",
    rapid: "Quick one-off payouts for emergencies (disasters, pandemics, wars). They come with few or no conditions.",
    waiver: "When a country misses a binding condition and the IMF board decides to keep paying anyway.",
    stopped: "The program ended early and the remaining money was never paid, usually because conditions were not met.",
    held: "Payments were delayed for a while, usually because a review found conditions had not been met, then started again.",
    notmet: "Conditions the government did not carry out on time. The narrow count includes only clear failures; the broad count also includes ones only partly met.",
    policyloan: "Money paid into the government's budget once it has made agreed policy changes, instead of paying for a building project.",
    prior: "The World Bank's conditions: policy steps the government must take before the World Bank board approves the money.",
    pipeline: "A loan still being prepared; the date shown is only its planned date.", dropped: "A loan that was planned but never approved.",
    named: "Approved after the World Bank's labelled database stops (December 2024); included because the World Bank's own name for it says it is a policy loan.",
    general: "Money for the government's whole budget, to spend as it decides within the agreed conditions.", sector: "Money for one area of the budget, such as health or education.",
    mfa: "EU loans or grants to a neighbouring country in crisis. Each payment is released only when agreed reforms are done, and only if the country also has an IMF program.",
    bop: "EU loans to an EU member outside the euro whose foreign payments are in crisis, released in stages as reforms are done.",
    esm: "Euro-area rescue funds (the EFSM, EFSF and ESM, and the 2010 Greek Loan Facility). Money came in stages tied to reforms written into a memorandum of understanding.",
    mou: "The memorandum of understanding: the written list of reforms a government agrees to in return for the money.",
    collateral: "The loan is backed by something the lender can take, often the country's oil, mineral or other income paid into an account.",
    escrow: "An account, often held abroad, where the borrower must keep money the lender can take if a payment is missed.",
    secrecy: "A clause that forbids the borrowing government from revealing the terms, or even that the loan exists.",
    noparis: "A clause that keeps this loan out of any group debt deal with other creditor governments (the Paris Club), so it must be paid in full.",
    crossdefault: "If the country misses a payment to any other lender, or in some contracts takes action against Chinese interests, the Chinese lender can demand the whole loan back at once.",
    rescue: "A loan to help a country in financial trouble pay its other debts or keep its currency stable.",
    insurance: "The borrower had to buy insurance on the loan from China's state export insurer (Sinosure).",
    pc_classic: "Payments due are postponed and spread over more years, at market interest rates. No debt is cancelled.",
    pc_houston: "Terms from 1990 for lower-middle-income countries: longer repayment, and some debt can be swapped for other uses.",
    pc_toronto: "Terms from 1988 for the poorest countries: the first deals that cancelled part of the debt (up to a third).",
    pc_london: "Terms from 1991 for the poorest countries: up to half of the debt payments cancelled.",
    pc_naples: "Terms from 1994 for the poorest countries: half to two-thirds of the debt cancelled.", pc_naples: "Terms from 1994 for the poorest countries: half to two-thirds of the debt cancelled.",
    pc_lyon: "Terms from 1996 for the poorest, most indebted countries: up to 80% cancelled.", pc_cologne: "Terms from 1999 under the Heavily Indebted Poor Countries initiative: up to 90% or more cancelled.",
    pc_hipcinitiativeexit: "The final deal when a country completes the Heavily Indebted Poor Countries initiative: most of the remaining debt cancelled.",
    pc_adhoc: "A one-off deal on terms made for that country.", pc_dssi: "The 2020-21 pause on debt payments for the poorest countries during the pandemic (the Debt Service Suspension Initiative).",
    pc_commonframework: "The 2020 G20 plan, including China, for treating the debts of the poorest countries together.",
    all_0: "Each IMF lending arrangement since 1952.", all_1: "Each World Bank loan paid into a government's budget for policy changes.", all_2: "Each Inter-American Development Bank policy-based loan.",
    all_3: "Each EU or euro-area rescue or assistance programme.", all_4: "Each Paris Club debt agreement; every one requires an IMF program.", all_5: "Each loan from a Chinese state lender in AidData's records (grants left out).",
    all_6: "Each budget-support payment other lenders reported to the OECD (Japan, the United States, Saudi Arabia, the regional development banks and others).",
  };
  // Facility names and other labels used in the boxes
  Object.assign(TERMS, {
    "ck_extendedcreditfacility": "The IMF's main low-interest loan for poor countries, over three to five years.", "ck_standbyarrangement": "The IMF's standard loan for a short-term crisis, usually one to two years.",
    "ck_extendedfundfacility": "An IMF loan over three to four years for deeper problems, with more reforms required.", "ck_structuraladjustmentfacilitycommitment": "The IMF's 1986-1995 low-interest loan for poor countries, the start of 'structural adjustment'.",
    "ck_flexiblecreditline": "A credit line for countries the IMF judges sound; it has no conditions after approval.", "ck_resilienceandsustainabilityfacility": "The IMF's climate and pandemic-preparedness loans since 2022, with their own reform measures.",
    "ck_rapidcreditfacility": "A quick low-interest emergency loan with few conditions.", "ck_rapidfinancinginstrument": "A quick emergency loan with few conditions.",
  });
  Object.assign(TERMS, {
    ms_met: "The government did it, by the due date.", ms_notme: "The government did not do it.", ms_partia: "The government did part of it.",
    ms_waived: "The government missed it, but the IMF board agreed to keep paying anyway.", ms_modifi: "The IMF changed the condition before it fell due: a new date, new wording, or a different type of condition.",
    ms_stillo: "Not yet due, or not yet assessed, at the last review that lists it.", ms_otherc: "A code the IMF uses in this file without defining it in its labels; shown exactly as given.",
    fdi_in: "Money foreign companies put into businesses here, minus what they pulled out that year, so it can be below zero.", fdi_out: "Money this country's companies put into businesses abroad.",
    gdp: "GDP is the value of everything the country produces in a year.", gni: "GNI is the country's yearly income: what it produces plus income from abroad.",
    oda: "Official development assistance: grants and cheap loans from governments and agencies, minus loan repayments.", tc: "Grants spent on paying advisers, experts and training, much of it to people and firms from the donor country.",
    grants_by_donor: "Grants only, never loans, as each donor reported them to the OECD.", tied: "Untied: can be spent anywhere. Partly untied: in the donor country or other poor countries. Tied: only on the donor country's goods and services.",
    ppg: "Debt owed by the government, or by others with the government promising to pay if they cannot.", bonds: "Loans raised by selling bonds to investors, such as investment funds.",
    png: "Debt of private companies with no government promise behind it.", bilateral: "Loans from one government (or its state bank) straight to another.",
    multilateral: "Loans from bodies owned by many governments, such as the IMF and the World Bank.", interest_exp: "Interest is what a borrower pays the lender on top of paying the loan back.",
    early: "This map's own count, read from the IMF's board papers of the time. The IMF published no list of conditions for these years.",
    e_QPC: "A number the government had to keep to, such as a ceiling on bank credit or a floor on reserves. Missing it stopped the money until the IMF agreed new terms.",
    e_SPC: "A rule or step the government had to keep to, such as adding no new limits on paying for imports, or carrying out a promised measure. Breaking it stopped the money.",
    e_IBSB: "A target the IMF watched. Missing it meant the government had to talk with the IMF about new measures, but the money did not stop by itself.",
    owncount: "Counted by this map, not by the World Bank: the numbered items under the agreement's list of required actions. A rough guide; see the World Bank row's fine print.",
  });
  function tip(key) { const t = TERMS[key]; return t ? `<span class="q" tabindex="0" role="button" aria-label="What this means" data-tip="${esc(t)}">?</span>` : ""; }

  /* ------------------------------------------------------------ helpers for the rows */
  function groupBy(list, f) { const g = {}; for (const x of list) (g[f(x)] = g[f(x)] || []).push(x); return g; }
  function checks(key, groups, label, value) {
    return `<div data-checks="${key}">` + Object.entries(groups).map(([g, items]) => `<div class="grp">${esc(g)}</div>` +
      items.map((it) => `<label class="ck"><input type="checkbox" checked data-v="${esc(value ? value(it) : it)}"> <span>${esc(label(it))}</span>${tip("ck_" + String(value ? value(it) : it).toLowerCase().replace(/[^a-z]/g, ""))}</label>`).join("")).join("") + `</div>`;
  }
  function optionText(id, v) {
    const s = document.querySelector(`.row[data-id="${id}"] select[data-k="measure"]`);
    const o = s && [...s.options].find((x) => x.value === v);
    return o ? o.textContent.charAt(0).toLowerCase() + o.textContent.slice(1) : "";
  }
  function bars(series, colour, label) {
    if (series.length < 2) return "";
    const W_ = 300, H = 52, max = Math.max(1, ...series.map((s) => s[1])), bw = W_ / series.length;
    const rects = series.map(([y, v], i) => `<rect x="${(i * bw).toFixed(1)}" y="${(H - (v / max) * H).toFixed(1)}" width="${Math.max(1, bw - 1).toFixed(1)}" height="${((v / max) * H).toFixed(1)}" fill="${colour}"><title>${y}: ${v}</title></rect>`).join("");
    return `<svg viewBox="0 0 ${W_} ${H + 14}" width="100%" role="img" aria-label="Per year">${rects}<text x="0" y="${H + 12}" fill="#8A939D" font-size="10">${series[0][0]}</text><text x="${W_}" y="${H + 12}" fill="#8A939D" font-size="10" text-anchor="end">${series[series.length - 1][0]}</text><text x="${W_ / 2}" y="${H + 12}" fill="#8A939D" font-size="10" text-anchor="middle">${label || "per year"}, highest ${num(max)}</text></svg>`;
  }
  function wItem(w) {
    const t = D.wbtext[w.id];
    const txt = t ? t.map((d) => `<details class="tx"><summary>Text of its conditions: ${esc(d[0])}, ${esc(d[1])}</summary><div class="txt">${esc(d[3])}</div>${d[2] ? `<a href="${esc(d[2])}" target="_blank" rel="noopener">The signed agreement (PDF)</a>` : ""}</details>`).join("") : "";
    const when = w.st === "Pipeline" ? `planned for ${esc(w.ap || "–")}` : w.st === "Dropped" ? `dropped${w.ap ? " (was set for " + esc(w.ap) + ")" : ""}` : w.ap ? "approved " + esc(w.ap) : "no approval date";
    return `<div class="item"><a href="https://projects.worldbank.org/en/projects-operations/project-detail/${esc(w.id)}" target="_blank" rel="noopener">${esc(w.name)}</a><br><span class="m">${esc(w.id)} · ${esc(w.ins)}${tip(/^Named/.test(w.ins) ? "named" : "policyloan")} · ${when}${w.st === "Pipeline" ? tip("pipeline") : w.st === "Dropped" ? tip("dropped") : ""} · ${esc(w.st || "")}</span><br>${usd(w.amt)}${D.wbown[w.id] != null ? ` · ${D.wbown[w.id]} condition${D.wbown[w.id] === 1 ? "" : "s"} counted by this map${tip("owncount")}` : ""}${txt}</div>`;
  }

  /* ------------------------------------------------------------ patterns behind the scenes */
  // Each pattern colours countries by their role in it and draws its documented links.
  const ISONAME = (c) => GEO.get(c) || NAMEOF[c] || c;
  for (const pt of D.pats || []) {
    const roles = pt.roles || [...new Set(pt.countries.map((c) => c.role))];
    const top = roles.slice(0, 4);
    const RC = {}; for (const c of pt.countries) RC[c.iso3] = c;
    const yrs = (pt.timeline || []).map((t) => +t.year).filter((y) => y > 0);
    const linkYears = (x) => { const m = String(x.years || "").match(/\d{4}/g); return m ? [+m[0], +m[m.length - 1]] : null; };
    const ser = pt.series && pt.series.length ? pt.series : null;
    const det = (t, n, body) => (n ? `<details class="pat"><summary>${esc(t)} (${n})</summary>${body}</details>` : "");
    LAYERS.push({
      id: "pat_" + pt.id, lender: "Pat", ramp: "stone", cat: top, pat: pt,
      span: ser ? [ser[0].year, ser[ser.length - 1].year] : yrs.length ? [Math.min(...yrs), Math.max(...yrs)] : [1947, 2030],
      title: pt.title, short: "the pattern “" + pt.title + "”",
      plain: pt.summary, lineNote: pt.links && pt.links.length ? "Documented connections (hover a line)" : "",
      srcLine: { axis: "an axis of power", club: "a club", bloc: "a bloc", chain: "a chain of people or money", scheme: "a scheme", wave: "a wave over time" }[pt.kind] || pt.kind,
      controls: () => (ser ? bars(ser.map((x) => [x.year, x.value]), "#9DB0CC", ser[0].label) + (pt.series_note ? `<p class="plain" style="font-size:11.5px">${esc(pt.series_note)}</p>` : "") : "") +
        det("Dated timeline", (pt.timeline || []).length, (pt.timeline || []).slice().sort((a, b) => a.year - b.year).map((t) => `<div class="tl"><b>${esc(t.year)}</b> ${esc(t.event)}${t.source_url ? ` <a href="${esc(t.source_url)}" target="_blank" rel="noopener">source</a>` : ""}</div>`).join("")) +
        det("Connections drawn on the map", (pt.links || []).length, (pt.links || []).map((x) => `<div class="tl">${esc(x.from)} → ${esc(x.to)}: ${esc(x.label)}${x.years ? ` <span class="m">(${esc(x.years)})</span>` : ""}</div>`).join("")) +
        det("Statistical studies", (pt.statistical_studies || []).length, (pt.statistical_studies || []).map((x) => `<div class="tl"><b>${x.url ? `<a href="${esc(x.url)}" target="_blank" rel="noopener">${esc(x.study)}</a>` : esc(x.study)}</b><br><span class="m">Sample: ${esc(x.sample)}</span><br>${esc(x.finding)}</div>`).join("")) +
        det("One author's claims, not confirmed by records", (pt.claims_per_author || []).length, (pt.claims_per_author || []).map((c) => `<div class="tl"><b>${esc(c.author)}</b>, <i>${esc(c.work)}</i>: ${esc(c.claim)}${c.status ? `<br><span class="m">What the record shows: ${esc(c.status)}</span>` : ""}</div>`).join("")) +
        det("Still unproven or disputed", (pt.uncertain || []).length, (pt.uncertain || []).map((u) => `<div class="tl">${esc(u)}</div>`).join("")),
      unit: (v) => (v === 5 ? "other role" : top[v - 1] || ""),
      values() {
        const out = new Map();
        for (const c of pt.countries) if (GEO.has(c.iso3)) out.set(c.iso3, top.includes(c.role) ? top.indexOf(c.role) + 1 : 5);
        return { values: out, unplaced: new Map() };
      },
      popup(c) {
        const r = RC[c]; if (!r) return "";
        const L = (pt.links || []).filter((x) => x.from_iso3 === c || x.to_iso3 === c);
        return `<div class="big">${esc(r.role)}</div>${para(r.note)}` + (L.length ? `<h4>Connections</h4>` + L.map((x) => `<div class="item">${esc(x.from)} → ${esc(x.to)}<br><span class="m">${esc(x.label)}${x.years ? " · " + esc(x.years) : ""}</span></div>`).join("") : "") +
          `<div class="note">The pattern's summary, timeline and sources are in its row on the left.</div>`;
      },
      lines: () => (pt.links || []).map((x) => ({ a: x.a, b: x.b, label: `${x.from} → ${x.to}: ${x.label}${x.years ? " (" + x.years + ")" : ""}` })),
      about: `<p>${esc(pt.summary)}</p>` + ((pt.confirmed_by || []).length ? `<p><b>Confirmed by</b></p>` + pt.confirmed_by.map((c) => `<div class="tl">${c.url ? `<a href="${esc(c.url)}" target="_blank" rel="noopener">${esc(c.title)}</a>` : esc(c.title)}</div>`).join("") : "") +
        (pt.method ? `<p>${esc(pt.method)}</p>` : "") + `<p>Researched for this map from the sources listed. Claims from one author that records have not confirmed are kept apart and labelled as that author's.</p>`,
    });
  }

  // World Bank-financed contracts: whose firms won them.
  const WC = (D.wbca && D.wbca.flows || []).map((r) => ({ b: r[0], s: r[1], y: r[2], cat: r[3], usd: r[4], n: r[5] }));
  const wcCats = [...new Set(WC.map((x) => x.cat))];
  const wcKeep = (x, o, from, to) => x.y >= from && x.y <= to && (!o.off || !o.off.has(x.cat));
  const CAP = D.cap || {};
  if (WC.length) LAYERS.push({
    id: "wbca", lender: "Pat", ramp: "slate", span: D.wbca.fy, linesFollowClick: true, money: true,
    title: "Who wins the contracts the World Bank pays for",
    short: "World Bank-financed contracts",
    plain: "When a World Bank loan pays for a road, a dam, medicines or advisers, the borrowing government signs contracts with firms. The World Bank publishes each contract and the home country of the firm that won it. This row shows where that money went: to firms from the borrowing country itself or to firms from abroad, and which countries' firms won the most. Lines run from the borrowing country to the countries whose firms won its contracts. Years are the World Bank's fiscal years.",
    controls: () => `<select data-k="measure">
        <option value="won">Money this country's firms won in other countries (US$)</option>
        <option value="abroad">Money from this country's contracts that went to foreign firms (US$)</option>
        <option value="share">Share of this country's contract money that went to foreign firms (%)</option>
        <option value="home">Money from this country's contracts that went to its own firms (US$)</option>
      </select>` + checks("cat", { "Kind of contract": wcCats }, (k) => k),
    unit: (v, o) => (o.measure === "share" ? `${num(v, 1)}%` : usd(v)),
    fmt: (v, o) => (o.measure === "share" ? `${num(v, 0)}%` : usd(v)),
    values(from, to, o) {
      const out = new Map(), unplaced = new Map(), tot = new Map(), fo = new Map();
      for (const x of WC) {
        if (!wcKeep(x, o, from, to)) continue;
        const foreign = x.s !== x.b && x.s !== "UNK" && x.b !== "REG";
        if (o.measure === "won") { if (foreign) out.set(x.s, (out.get(x.s) || 0) + x.usd); }
        else if (o.measure === "abroad") { if (foreign) out.set(x.b, (out.get(x.b) || 0) + x.usd); }
        else if (o.measure === "home") { if (x.s === x.b) out.set(x.b, (out.get(x.b) || 0) + x.usd); }
        else if (x.b !== "REG" && x.s !== "UNK") { tot.set(x.b, (tot.get(x.b) || 0) + x.usd); if (foreign) fo.set(x.b, (fo.get(x.b) || 0) + x.usd); }
      }
      if (o.measure === "share") for (const [c, t] of tot) if (t > 0) out.set(c, (100 * (fo.get(c) || 0)) / t);
      for (const c of [...out.keys()]) if (!GEO.has(c)) { unplaced.set(ISONAME(c), out.get(c)); out.delete(c); }
      return { values: out, unplaced, noTotal: o.measure === "share" };
    },
    popup(c, from, to, o) {
      const asB = WC.filter((x) => x.b === c && wcKeep(x, o, from, to)), asS = WC.filter((x) => x.s === c && x.b !== c && wcKeep(x, o, from, to));
      const sum = (L) => L.reduce((s, x) => s + x.usd, 0), cnt = (L) => L.reduce((s, x) => s + x.n, 0);
      const by = (L, k) => { const m = new Map(); for (const x of L) m.set(x[k], (m.get(x[k]) || 0) + x.usd); return [...m.entries()].sort((a, b) => b[1] - a[1]); };
      const home = asB.filter((x) => x.s === c), fore = asB.filter((x) => x.s !== c && x.s !== "UNK"), unk = asB.filter((x) => x.s === "UNK");
      let h = `<h4>As the borrower</h4><table><tr><td>All contracts</td><td class="n">${usd(sum(asB))} · ${num(cnt(asB))}</td></tr><tr><td>Won by its own firms</td><td class="n">${usd(sum(home))}</td></tr><tr><td>Won by foreign firms</td><td class="n">${usd(sum(fore))}</td></tr>${unk.length ? `<tr><td>Firm's country not given</td><td class="n">${usd(sum(unk))}</td></tr>` : ""}</table>`;
      if (fore.length) h += `<h4>Foreign firms' home countries</h4><table>${by(fore, "s").slice(0, 15).map(([k, v]) => `<tr><td>${esc(ISONAME(k))}</td><td class="n">${usd(v)}</td></tr>`).join("")}</table>`;
      h += `<h4>Its firms abroad</h4><table><tr><td>Won in other countries</td><td class="n">${usd(sum(asS))} · ${num(cnt(asS))} contracts</td></tr>${by(asS.filter((x) => x.b !== "REG"), "b").slice(0, 12).map(([k, v]) => `<tr><td>in ${esc(ISONAME(k))}</td><td class="n">${usd(v)}</td></tr>`).join("")}</table>`;
      const F = (D.wbca.firms || []).filter((f) => f[1] === c).slice(0, 10);
      if (F.length) h += `<h4>Its firms that won most abroad, all years</h4>` + F.map((f) => `<div class="item">${esc(f[0])}<br><span class="m">${usd(f[2])} · ${num(f[3])} contracts in ${num(f[4])} countr${f[4] === 1 ? "y" : "ies"}</span></div>`).join("");
      return h + `<div class="note">Lines on the map now show this country's contract money going to foreign firms' home countries.</div>`;
    },
    lines(from, to, o, sel) {
      const m = new Map();
      for (const x of WC) {
        if (!wcKeep(x, o, from, to) || x.s === x.b || x.s === "UNK" || x.b === "REG") continue;
        if (sel && x.b !== sel && x.s !== sel) continue;
        const k = x.b + ">" + x.s; m.set(k, (m.get(k) || 0) + x.usd);
      }
      return [...m.entries()].sort((a, b) => b[1] - a[1]).slice(0, sel ? 40 : 60).map(([k, v]) => { const [b, s2] = k.split(">"); return { a: CAP[b], b: CAP[s2], w: v, label: `${ISONAME(b)} → firms from ${ISONAME(s2)}: ${usd(v)}` }; });
    },
    lineNote: "",
    srcLine: "World Bank, contract awards in project financing",
    about: `<p>Every contract in the World Bank's three published files of contracts signed under its investment projects: fiscal years 2001 to 2016, 2017 to 2019, and 2020 on (${num(D.wbca.rows_in_files)} contracts, ${usd(D.wbca.usd_in_files)}). Each row gives the borrowing country, the firm, the firm's home country as the World Bank records it, the kind of contract and the amount. Firms' names are shown as written in the files, so one firm can appear under several spellings.</p>
<p>${num(D.wbca.regional_rows)} contracts (${usd(D.wbca.regional_usd)}) belong to regional projects with no single borrowing country; they count toward the winning firms' totals but not toward any borrower. ${num(D.wbca.no_supplier_country_rows)} contracts (${usd(D.wbca.no_supplier_country_usd)}) give no home country for the firm; they count only in a borrower's total. With no country selected, the map draws the 60 largest flows to foreign firms in the chosen years; click a country to draw its own.</p>
<p>These files start in fiscal 2001. Contracts from earlier decades, when the World Bank reported that most foreign contract money went to firms from its largest shareholders, are not in them.</p>
<p>Sources: World Bank Finances One, <a href="https://financesone.worldbank.org/contract-awards-in-investment-project-financing-since-fy-2001-fy-2016/DS01004" target="_blank" rel="noopener">Contract Awards in Investment Project Financing, FY2001–FY2016</a>, <a href="https://financesone.worldbank.org/contract-awards-in-investment-project-financing-since-fy-2017-fy-2019/DS04691" target="_blank" rel="noopener">FY2017–FY2019</a> and <a href="https://financesone.worldbank.org/d/DS00005" target="_blank" rel="noopener">since FY2020</a>, read 25 October 2026. Map points for countries are their capitals (GeoNames).</p>`,
  });

  /* ------------------------------------------------------------ the panel */
  const MINY = 1947, MAXY = 2030;
  const state = { active: "all", from: MINY, to: MAXY, opts: {}, base: "land" };
  for (const l of LAYERS) state.opts[l.id] = { measure: undefined, off: new Set() };
  const panel = $("#panel");
  const SECS = { Pat: "Patterns behind the scenes", All: "Together", IMF: "International Monetary Fund", "World Bank": "World Bank", IDB: "Regional development banks", EU: "European Union and euro area", Gov: "Single governments", OECD: "Every lender reporting to the OECD", Flows: "Other money flowing in and out" };
  const ORDER = ["All", "Pat", "IMF", "World Bank", "IDB", "EU", "Gov", "OECD", "Flows"];
  LAYERS.sort((a, b) => ORDER.indexOf(a.lender) - ORDER.indexOf(b.lender));
  let lastSec = "";
  panel.innerHTML = LAYERS.map((l) => {
    const sec = l.lender !== lastSec ? `<div class="sec">${esc(SECS[l.lender])}</div>` : ""; lastSec = l.lender;
    return sec + `<div class="row" data-id="${l.id}"><div class="head"><label class="pick"><input type="radio" name="row" value="${l.id}"><span><span class="t">${esc(l.title)}</span><span class="span">${l.span[0]} to ${l.span[1]} · ${esc(l.srcLine)}</span></span></label>${l.plain ? `<span class="q big" tabindex="0" role="button" aria-label="What this row shows" data-tip="${esc(l.plain)}">?</span>` : ""}</div>
      <div class="body">${l.plain ? `<p class="plain">${esc(l.plain)}</p>` : ""}${l.controls()}<div class="legend" id="leg-${l.id}"></div><div class="unplaced" id="un-${l.id}"></div>
      <details><summary>Sources and fine print</summary>${l.about}</details></div></div>`;
  }).join("");
  for (const l of LAYERS) for (const s of document.querySelectorAll(`.row[data-id="${l.id}"] select[data-k]`)) state.opts[l.id][s.dataset.k] = s.value;
  panel.addEventListener("change", (e) => {
    const row = e.target.closest(".row"); if (!row) return;
    const id = row.dataset.id, o = state.opts[id];
    if (e.target.name === "row") { state.active = id; }
    else if (e.target.matches("select[data-k]")) o[e.target.dataset.k] = e.target.value;
    else if (e.target.matches("[data-checks] input")) { e.target.checked ? o.off.delete(e.target.dataset.v) : o.off.add(e.target.dataset.v); }
    redraw();
  });

  // Years
  const yF = $("#yFrom"), yT = $("#yTo");
  for (const s of [yF, yT]) { s.min = MINY; s.max = MAXY; s.step = 1; }
  yF.value = state.from; yT.value = state.to;
  const showYears = () => {
    $("#yFromL").textContent = state.from; $("#yToL").textContent = state.to;
    const p = (v) => ((v - MINY) / (MAXY - MINY)) * 100;
    const f = $("#yFill"); f.style.left = `calc(7px + (100% - 14px) * ${p(state.from) / 100})`; f.style.width = `calc((100% - 14px) * ${(p(state.to) - p(state.from)) / 100})`;
  };
  let yTimer = null;
  const onYears = (e) => {
    let a = +yF.value, b = +yT.value;
    if (a > b) { if (e.target === yF) b = a; else a = b; yF.value = a; yT.value = b; }
    state.from = a; state.to = b; showYears();
    clearTimeout(yTimer); yTimer = setTimeout(redraw, 60);
  };
  yF.addEventListener("input", onYears); yT.addEventListener("input", onYears);
  showYears();

  // Explanations: shown while hovering or focusing a "?" mark; a tap toggles them on touch screens.
  const qtip = $("#qtip");
  function showQ(el) {
    qtip.textContent = el.dataset.tip; qtip.style.display = "block";
    const r = el.getBoundingClientRect(), w = qtip.offsetWidth, h = qtip.offsetHeight;
    let x = Math.min(window.innerWidth - w - 8, Math.max(8, r.left + r.width / 2 - w / 2)), y = r.bottom + 6;
    if (y + h > window.innerHeight - 8) y = r.top - h - 6;
    qtip.style.left = x + "px"; qtip.style.top = y + "px";
  }
  const hideQ = () => { qtip.style.display = "none"; };
  document.addEventListener("mouseover", (e) => { const q = e.target.closest && e.target.closest(".q[data-tip]"); if (q) showQ(q); });
  document.addEventListener("mouseout", (e) => { const q = e.target.closest && e.target.closest(".q[data-tip]"); if (q) hideQ(); });
  document.addEventListener("focusin", (e) => { const q = e.target.closest && e.target.closest(".q[data-tip]"); if (q) showQ(q); });
  document.addEventListener("focusout", hideQ);
  document.addEventListener("click", (e) => { const q = e.target.closest && e.target.closest(".q[data-tip]"); if (q) { e.preventDefault(); e.stopPropagation(); qtip.style.display === "block" ? hideQ() : showQ(q); } else hideQ(); }, true);

  /* ------------------------------------------------------------ the map */
  const BOUND = "https://raw.githubusercontent.com/WelcomeToYourGalaxy/culprits/main/map/data/boundaries.geojson";
  const NIGHT = {
    tiles: "https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/VIIRS_Black_Marble/default/2016-01-01/GoogleMapsCompatible_Level8/{z}/{y}/{x}.png",
    ramp: [[0, "#02040C"], [14, "#050918"], [34, "#0B1430"], [62, "#17295A"], [100, "#2E5390"], [145, "#5E8DC2"], [190, "#A5C7E2"], [230, "#DCE8F0"], [255, "#F1F4F6"]],
    shade: { "hillshade-method": "multidirectional", "hillshade-illumination-direction": [315, 270, 0, 225], "hillshade-illumination-altitude": [35, 30, 30, 45],
      "hillshade-highlight-color": ["rgba(170,196,230,0.12)", "rgba(170,196,230,0.05)", "rgba(170,196,230,0.05)", "rgba(170,196,230,0.03)"],
      "hillshade-shadow-color": ["rgba(0,1,6,0.45)", "rgba(0,1,6,0.25)", "rgba(0,1,6,0.25)", "rgba(0,1,6,0.15)"],
      "hillshade-accent-color": "rgba(0,1,6,0.15)", "hillshade-exaggeration": 0.8, "hillshade-illumination-anchor": "map" },
    road: ["rgba(150,186,222,0.30)", "rgba(170,202,232,0.45)", "rgba(206,226,240,0.70)"], roadGlow: "#2D5C96",
    seaGlow: ["interpolate", ["linear"], ["elevation"], -9000, "rgba(31,79,126,0)", -150, "rgba(31,79,126,0)", -60, "rgba(31,79,126,0.28)", -15, "rgba(31,79,126,0.55)",
      -3, "rgba(74,154,182,0.85)", 0, "rgba(74,154,182,0)", 9000, "rgba(74,154,182,0)"],
    border: "rgba(120,140,196,0.32)",
  };
  // Hell: the Culprits map's basemap of that name (map/app.js, HELL and
  // hellLayers, round 144h), copied: an oxblood sea, darker in the deeps;
  // basalt-black land darkening into scorched oxblood up the slopes; cold
  // blue-grey relief light; lakes as dark blood, rivers as thin red veins
  // with a faint glow, graveyards in dull red close in; towns in dark ash,
  // roads in maroon, borders faint red; place names in EB Garamond from the
  // Culprits map's letter files (round nh13, asked 19 October).
  const HELL = {
    sheet: "#1E080B",
    ground: ["interpolate", ["linear"], ["elevation"],
      -8000, "#110407", -5000, "#18060A", -3000, "#20070C", -1500, "#2A0A0F", -500, "#360C11",
      -120, "#481116", -20, "#57151A", -1, "#5F181D",
      0, "#131215", 200, "#151215", 600, "#1A1214", 1200, "#1F1416", 2000, "#241418",
      3000, "#2B151A", 4200, "#33161C", 5600, "#3B171E"],
    shade: { "hillshade-method": "multidirectional", "hillshade-illumination-direction": [315, 270, 0, 225], "hillshade-illumination-altitude": [40, 35, 35, 50],
      "hillshade-highlight-color": ["rgba(150,164,186,0.2)", "rgba(150,164,186,0.08)", "rgba(150,164,186,0.08)", "rgba(150,164,186,0.04)"],
      "hillshade-shadow-color": ["rgba(0,0,0,0.8)", "rgba(0,0,0,0.45)", "rgba(0,0,0,0.45)", "rgba(0,0,0,0.25)"],
      "hillshade-accent-color": "rgba(0,0,0,0.3)", "hillshade-exaggeration": 1, "hillshade-illumination-anchor": "map" },
    coast: "#521419", lake: "#3A0C11", lakeEdge: "#5E171C", river: "#9C252B", riverGlow: "#6A1318",
    grave: "#561519", graveEdge: "#74202A", town: "#1C1719", townWork: "#221C1E",
    road: ["#2B1C1E", "#3A2124", "#4C2529"], rail: "#3A3034", building: "#201B1D", border: "rgba(170,58,62,0.32)",
    font: { regular: ["EBGaramond-Regular"], bold: ["EBGaramond-SemiBold"], italic: ["EBGaramond-Italic"] },
    name: { country: "#A9504C", state: "#8C4A47", city: "#CDBDB4", town: "#B4A39B", minor: "#9A8B85", water: "#B0605F", peak: "#958680",
      halo: "rgba(8,4,5,0.85)", haloWater: "rgba(24,6,9,0.8)" },
    glyphs: "https://welcometoyourgalaxy.github.io/culprits/glyphs/{fontstack}/{range}.pbf",
  };
  // The Jurassic basemap's relief, as the Culprits map has it (SAT_RELIEF).
  const JURASSIC = {
    colour: ["interpolate", ["linear"], ["elevation"],
      -8000, "rgba(10,22,42,0.8)", -3500, "rgba(12,28,50,0.72)", -1200, "rgba(16,40,60,0.6)",
      -200, "rgba(26,70,86,0.38)", -40, "rgba(40,96,102,0.22)", 0, "rgba(40,90,90,0.1)",
      1, "rgba(46,52,34,0.32)", 400, "rgba(48,54,36,0.3)", 1000, "rgba(64,70,44,0.28)",
      1700, "rgba(108,100,66,0.26)", 2500, "rgba(118,90,60,0.3)", 3300, "rgba(110,80,62,0.32)",
      4300, "rgba(102,92,84,0.3)", 5500, "rgba(132,128,122,0.2)"],
    seabed: ["interpolate", ["linear"], ["elevation"],
      -8000, "rgba(10,22,42,0.8)", -3500, "rgba(12,28,50,0.72)", -1200, "rgba(16,40,60,0.6)",
      -200, "rgba(26,70,86,0.38)", -40, "rgba(40,96,102,0.22)", -1, "rgba(40,90,90,0.1)", 0, "rgba(0,0,0,0)"],
    sea: ["interpolate", ["linear"], ["elevation"],
      -8000, "rgba(10,22,42,0.6)", -3000, "rgba(12,26,46,0.55)", -1500, "rgba(14,32,52,0.42)",
      -400, "rgba(20,48,64,0.2)", -80, "rgba(20,48,64,0)", 0, "rgba(0,0,0,0)"],
    shade: { "hillshade-method": "multidirectional", "hillshade-illumination-direction": [315, 270, 0, 225], "hillshade-illumination-altitude": [40, 35, 35, 50],
      "hillshade-highlight-color": ["rgba(240,236,222,0.1)", "rgba(240,236,222,0.04)", "rgba(240,236,222,0.04)", "rgba(240,236,222,0.02)"],
      "hillshade-shadow-color": ["rgba(18,24,14,0.78)", "rgba(18,24,14,0.42)", "rgba(18,24,14,0.42)", "rgba(18,24,14,0.2)"],
      "hillshade-accent-color": "rgba(18,24,14,0.3)", "hillshade-exaggeration": 1, "hillshade-illumination-anchor": "map" },
    depth: { "hillshade-method": "standard", "hillshade-illumination-direction": 315, "hillshade-illumination-anchor": "map",
      "hillshade-highlight-color": "rgba(240,236,222,0.04)", "hillshade-shadow-color": "rgba(12,18,10,0.55)", "hillshade-accent-color": "rgba(12,18,10,0)", "hillshade-exaggeration": 0.6 },
  };
  // This map's copy of the Culprits map's painted plate for the Atlas basemap: its cartouche
  // reads "Loan Conditions Map", and the half compass roses at its two ends, which met
  // out of line in the Pacific, are painted over with open sea. The Culprits plate is the fallback.
  const PLATE = { url: "https://welcometoyourgalaxy.github.io/maps/loan-conditions-atlas-plate.webp?v=1",
    fallback: "https://welcometoyourgalaxy.github.io/culprits/atlas-plate.webp?v=207", top: 85.05112877980659, bottom: -80.55, fadeIn: 3, fadeOut: 5 };
  const toPng = async (cv) => (cv.convertToBlob ? await cv.convertToBlob({ type: "image/png" }) : await new Promise((r) => cv.toBlob(r, "image/png"))).arrayBuffer();
  const canvas = (w, h) => (typeof OffscreenCanvas !== "undefined" ? new OffscreenCanvas(w, h) : Object.assign(document.createElement("canvas"), { width: w, height: h }));
  // Black Marble's sodium-orange lights redrawn by brightness in navy, cobalt, ice and bone.
  let nightTable = null;
  maplibregl.addProtocol("nhnight", async (params, ac) => {
    const m = params.url.match(/^nhnight:\/\/(\d+)\/(\d+)\/(\d+)$/);
    const r = await fetch(NIGHT.tiles.replace("{z}", m[1]).replace("{y}", m[2]).replace("{x}", m[3]), { signal: ac && ac.signal });
    if (!r.ok) throw new Error(`GIBS ${r.status}`);
    const img = await createImageBitmap(await r.blob());
    if (!nightTable) {
      const hex = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
      nightTable = new Uint8Array(768);
      for (let v = 0; v < 256; v++) {
        let k = 0; while (k < NIGHT.ramp.length - 2 && v > NIGHT.ramp[k + 1][0]) k++;
        const [v0, c0] = NIGHT.ramp[k], [v1, c1] = NIGHT.ramp[k + 1], f = Math.max(0, Math.min(1, (v - v0) / (v1 - v0))), a = hex(c0), b = hex(c1);
        for (let i = 0; i < 3; i++) nightTable[v * 3 + i] = Math.round(a[i] + (b[i] - a[i]) * f);
      }
    }
    const cv = canvas(img.width, img.height), cx = cv.getContext("2d");
    cx.drawImage(img, 0, 0);
    const d = cx.getImageData(0, 0, img.width, img.height), px = d.data;
    for (let i = 0; i < px.length; i += 4) {
      const v = Math.round(0.5 * Math.max(px[i], px[i + 1], px[i + 2]) + 0.5 * (0.3 * px[i] + 0.59 * px[i + 1] + 0.11 * px[i + 2]));
      px[i] = nightTable[v * 3]; px[i + 1] = nightTable[v * 3 + 1]; px[i + 2] = nightTable[v * 3 + 2]; px[i + 3] = 255;
    }
    cx.putImageData(d, 0, 0);
    return { data: await toPng(cv) };
  });
  // The Atlas's painted plate, cut into map squares.
  let plateImg = null;
  const merc = (lat) => (1 - Math.log(Math.tan(Math.PI / 4 + lat * Math.PI / 360)) / Math.PI) / 2;
  maplibregl.addProtocol("nhplate", async (params) => {
    const [z, x, y] = params.url.replace("nhplate://", "").split("/").map(Number);
    if (!plateImg) {
      const get = (u) => fetch(u).then((r) => { if (!r.ok) throw new Error(String(r.status)); return r.blob(); }).then((b) => createImageBitmap(b));
      plateImg = get(PLATE.url).catch(() => get(PLATE.fallback));
      plateImg.catch(() => { plateImg = null; });
    }
    const img = await plateImg;
    const n = 2 ** z, top = merc(PLATE.top), bot = merc(PLATE.bottom), y0 = y / n, y1 = (y + 1) / n;
    const cv = canvas(256, 256), cx = cv.getContext("2d");
    const a = Math.max(y0, top), b = Math.min(y1, bot);
    if (b > a) { cx.imageSmoothingQuality = "high"; cx.drawImage(img, x / n * img.width, (a - top) / (bot - top) * img.height, img.width / n, (b - a) / (bot - top) * img.height, 0, (a - y0) * n * 256, 256, (b - a) * n * 256); }
    return { data: await toPng(cv) };
  });


  const style = { version: 8, sources: { land: { type: "geojson", data: BOUND } },
    layers: [
      { id: "sea", type: "background", paint: { "background-color": "#0A1119" } },
      { id: "land", type: "fill", source: "land", paint: { "fill-color": "#1B1D1F", "fill-opacity": 1 } },
      { id: "land-edge", type: "line", source: "land", paint: { "line-color": "#4A4F55", "line-width": ["interpolate", ["linear"], ["zoom"], 1, 0.35, 6, 0.9], "line-opacity": 0.75 } },
    ], projection: { type: "globe" } };
  const HOME = { center: [10, 12], zoom: 1.9 };
  const map = new maplibregl.Map({ container: "map", style, center: HOME.center, zoom: HOME.zoom, minZoom: 0, maxZoom: 12, attributionControl: false, renderWorldCopies: false });
  map.addControl(new maplibregl.AttributionControl({ compact: true }), window.innerWidth > 720 ? "bottom-right" : "top-left");
  const foldCredits = () => { const a = document.querySelector(".maplibregl-ctrl-attrib"); if (a) { a.classList.remove("maplibregl-compact-show"); a.removeAttribute("open"); } };
  let creditsAsked = false;
  document.addEventListener("click", (e) => { if (e.target.closest && e.target.closest(".maplibregl-ctrl-attrib-button")) creditsAsked = true; }, true);
  for (const ev of ["idle", "sourcedata"]) map.on(ev, () => { if (!creditsAsked) foldCredits(); });
  map.addControl(new maplibregl.NavigationControl({ visualizePitch: false }), "top-right");
  $("#world").addEventListener("click", () => map.easeTo(Object.assign({ bearing: 0, pitch: 0, duration: 900 }, HOME)));
  // Globe or flat map.
  let flat = false;
  $("#proj").addEventListener("click", (e) => {
    flat = !flat;
    map.setProjection({ type: flat ? "mercator" : "globe" });
    e.target.textContent = flat ? "Globe" : "Flat map";
    freeFlat(); syncSheets();
  });
  // On the flat map the world can be dragged freely, with stars around it.
  function freeFlat() {
    try {
      if (flat) map.setTransformConstrain((ll, z) => ({ center: new maplibregl.LngLat(Math.max(-360, Math.min(360, ll.lng)), Math.max(-84, Math.min(84, ll.lat))), zoom: Math.max(0, z) }));
      else map.setTransformConstrain(null);
    } catch (err) {}
    map.setMinZoom(0);
  }
  // Background layers fill the whole screen on a flat map, which would hide the stars.
  // On the flat map each one is swapped for the same colour filling only the world.
  const SHEET = { type: "FeatureCollection", features: [] };
  for (let x = -180; x < 180; x += 10) {
    const ring = []; for (let y = -85.05; y <= 85.05; y += 5) ring.push([x, Math.min(y, 85.05)]);
    ring.push([x, 85.05]); for (let y = 85.05; y >= -85.05; y -= 5) ring.push([x + 10, Math.max(y, -85.05)]); ring.push([x + 10, -85.05], [x, -85.05]);
    SHEET.features.push({ type: "Feature", properties: {}, geometry: { type: "Polygon", coordinates: [ring] } });
  }
  function syncSheets() {
    if (!map.getStyle()) return;
    if (!map.getSource("world-sheet")) map.addSource("world-sheet", { type: "geojson", data: SHEET });
    const cur = typeof BASES !== "undefined" && BASES[state.base] ? new Set(BASES[state.base]().layers.map((x) => x.id)) : new Set();
    for (const l of map.getStyle().layers) {
      if (l.type !== "background") continue;
      const fid = l.id + "-flat", active = l.id === "sea" || cur.has(l.id);
      if (!map.getLayer(fid)) map.addLayer({ id: fid, type: "fill", source: "world-sheet", layout: { visibility: "none" }, paint: { "fill-color": map.getPaintProperty(l.id, "background-color") || "#0A1119", "fill-antialias": false } }, l.id);
      map.setLayoutProperty(l.id, "visibility", active && !flat ? "visible" : "none");
      map.setLayoutProperty(fid, "visibility", active && flat ? "visible" : "none");
    }
  }
  // Stars behind the globe: a fixed, seeded field so it looks the same on every visit.
  function drawStars() {
    const c = $("#stars"), dpr = Math.min(2, window.devicePixelRatio || 1), w = innerWidth, h = innerHeight;
    c.width = w * dpr; c.height = h * dpr; const g = c.getContext("2d"); g.scale(dpr, dpr);
    g.fillStyle = "#06090D"; g.fillRect(0, 0, w, h);
    let s = 20261024; const rnd = () => ((s = (s * 1103515245 + 12345) % 2147483648) / 2147483648);
    for (const [x, y, r, col] of [[0.72, 0.28, 0.42, "rgba(60,74,104,0.16)"], [0.25, 0.8, 0.38, "rgba(84,62,92,0.12)"], [0.9, 0.85, 0.3, "rgba(46,70,84,0.12)"]]) {
      const gr = g.createRadialGradient(x * w, y * h, 0, x * w, y * h, r * Math.max(w, h)); gr.addColorStop(0, col); gr.addColorStop(1, "rgba(0,0,0,0)"); g.fillStyle = gr; g.fillRect(0, 0, w, h);
    }
    const cols = ["233,228,216", "201,211,224", "175,192,214", "214,204,222"];
    const n = Math.round((w * h) / 1500);
    for (let i = 0; i < n; i++) {
      const big = rnd() > 0.985, r = big ? 0.9 + rnd() * 0.8 : 0.25 + rnd() * 0.6;
      g.fillStyle = `rgba(${cols[Math.floor(rnd() * cols.length)]},${(big ? 0.75 : 0.2) + rnd() * 0.5})`;
      g.beginPath(); g.arc(rnd() * w, rnd() * h, r, 0, Math.PI * 2); g.fill();
    }
  }
  drawStars(); window.addEventListener("resize", drawStars);
  const pad = () => map.setPadding({ left: window.innerWidth > 720 ? 396 : 0, top: 0, right: 0, bottom: window.innerWidth > 720 ? 0 : Math.round(window.innerHeight * 0.5) });
  pad(); window.addEventListener("resize", pad);
  window.loanConditionsMap = map;

  const GEO = new Map(); // iso3 -> name, for every shape on the map
  const NAMEOF = Object.assign({ CSK: "Czechoslovakia", YUG: "Yugoslavia" }, D.imfc.names, Object.fromEntries(D.wbp.rows.filter((r) => r[0]).map((r) => [r[0], r[1]])));
  let ready = false, current = new Map();

  map.on("load", async () => {
    const g = await fetch(BOUND).then((r) => r.json());
    for (const f of g.features) {
      if (f.properties.iso3 === "-99" && f.properties.name === "Kosovo") f.properties.iso3 = "XKX";
      if (f.properties.iso3 !== "-99") GEO.set(f.properties.iso3, f.properties.name);
    }
    map.addSource("lc", { type: "geojson", data: g, promoteId: "iso3" });
    map.addLayer({ id: "lc-fill", type: "fill", source: "lc", paint: { "fill-color": "rgba(0,0,0,0)", "fill-opacity": 0.9 } });
    map.addLayer({ id: "lc-line", type: "line", source: "lc", paint: { "line-color": ["case", ["boolean", ["feature-state", "hover"], false], "#F2EEE4", "rgba(12,14,18,.55)"],
      "line-width": ["case", ["boolean", ["feature-state", "hover"], false], 1.6, 0.4] } });
    setupPoints();
    ready = true;
    redraw();
  });

  /* ------------------------------------------------------------ point layers: where the money was spent */
  // Dot colours follow the background map, so they read well on each one.
  const PTCOL = { land: { wb: "#9DB4C8", cn: "#C28F9C", cs: "#ECE6DA", pf: "#93B39C", mm: "#B9A7D3", edge: "#0B0F14" }, night: { wb: "#7FB8B4", cn: "#B39BC9", cs: "#EDE4D6", pf: "#9DC0A8", mm: "#C2B2DA", edge: "#05080C" },
    atlas: { wb: "#3E5C76", cn: "#83394A", cs: "#2A2730", pf: "#5A4466", mm: "#1F3B4D", edge: "#F2EAD8" }, jurassic: { wb: "#2E4A5E", cn: "#74303F", cs: "#2B2420", pf: "#523D5E", mm: "#1E3542", edge: "#E6E0C8" }, hell: { wb: "#D7CEC3", cn: "#9FB2C2", cs: "#F2EADF", pf: "#A9BBA2", mm: "#C9B9D9", edge: "#1A0606" } };
  const PT = { wb: { on: false }, cn: { on: false }, cs: { on: false }, pf: { on: false }, mm: { on: false } };
  const PTK = ["wb", "cn", "cs", "pf", "mm"];
  const CSKIND = { privatization: "Sale or handover of a public firm or service", austerity: "Price, tax, pay, job or spending cuts", trade: "Trade opening", law: "A required change in the law" };
  const csOff = new Set();
  function setupPoints() {
    const WP = D.wbsites.projects;
    const wbf = D.wbsites.points.map(([x, y, id, pc, place]) => ({ type: "Feature", geometry: { type: "Point", coordinates: [x, y] },
      properties: { id, pc, place, y: (WP[id] || [])[5] ?? -1 } }));
    const CC = D.cnsites.cols;
    const cnf = D.cnsites.rows.map((r) => ({ type: "Feature", geometry: { type: "Point", coordinates: [r[0], r[1]] },
      properties: { i: r[2], y: r[5] ?? -1, exact: /^precise(,precise)*$/.test(r[10] || "") ? 1 : 0 } }));
    map.addSource("pt-wb", { type: "geojson", data: { type: "FeatureCollection", features: wbf } });
    map.addSource("pt-cn", { type: "geojson", data: { type: "FeatureCollection", features: cnf } });
    for (const k of ["wb", "cn"]) map.addLayer({ id: "pt-" + k, type: "circle", source: "pt-" + k, layout: { visibility: "none" },
      paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 1.1, 4, 2.6, 8, 5.5], "circle-stroke-width": ["interpolate", ["linear"], ["zoom"], 1, 0.3, 6, 0.8], "circle-opacity": 0.85, "circle-stroke-opacity": 0.8 } });
    $("#n-wb").textContent = num(wbf.length); $("#n-cn").textContent = num(cnf.length);
    // Cases where a condition led to harm; contested ones are drawn as rings.
    const csf = D.cases.map((c, i) => ({ type: "Feature", geometry: { type: "Point", coordinates: [c.lng, c.lat] },
      properties: { i, k: c.mechanism, a: c.start ?? -1, b: c.end ?? 9999, ct: c.confidence === "contested" ? 1 : 0 } }));
    map.addSource("pt-cs", { type: "geojson", data: { type: "FeatureCollection", features: csf } });
    map.addLayer({ id: "pt-cs", type: "circle", source: "pt-cs", layout: { visibility: "none" },
      paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 3.4, 4, 5, 8, 8], "circle-stroke-width": ["case", ["==", ["get", "ct"], 1], 2, 1.1], "circle-opacity": ["case", ["==", ["get", "ct"], 1], 0, 0.95], "circle-stroke-opacity": 1 } });
    $("#n-cs").textContent = num(csf.length);
    $("#cs-kinds").innerHTML = Object.entries(CSKIND).map(([k, t]) => `<label><input type="checkbox" checked data-csk="${k}"><span>${esc(t)} (${D.cases.filter((c) => c.mechanism === k).length})</span></label>`).join("");
    $("#cs-kinds").addEventListener("change", (e) => { const k = e.target.dataset.csk; if (!k) return; e.target.checked ? csOff.delete(k) : csOff.add(k); updatePoints(); });
    // Public Futures cases.
    const PF = D.pf.rows;
    const pff = PF.map((r, i) => ({ type: "Feature", geometry: { type: "Point", coordinates: [r[0], r[1]] }, properties: { i, y: r[4] ?? r[5] ?? -1 } }));
    map.addSource("pt-pf", { type: "geojson", data: { type: "FeatureCollection", features: pff } });
    map.addLayer({ id: "pt-pf", type: "circle", source: "pt-pf", layout: { visibility: "none" },
      paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 1.8, 4, 3.2, 8, 6], "circle-stroke-width": ["interpolate", ["linear"], ["zoom"], 1, 0.2, 6, 0.5], "circle-opacity": 0.95, "circle-stroke-opacity": 0.8 } });
    $("#n-pf").textContent = num(pff.length);
    // Mass Mobilization protests: kept in a separate file and loaded the first time the layer is switched on.
    map.addSource("pt-mm", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
    map.addLayer({ id: "pt-mm", type: "circle", source: "pt-mm", layout: { visibility: "none" },
      paint: { "circle-radius": ["interpolate", ["linear"], ["zoom"], 1, 1.5, 4, 2.8, 8, 5.5], "circle-stroke-width": ["interpolate", ["linear"], ["zoom"], 1, 0.2, 6, 0.5], "circle-opacity": 0.85, "circle-stroke-opacity": 0.7 } });
    $("#n-mm").textContent = num(D.mm_meta.n);
    $("#mm-only").addEventListener("change", updatePoints);
    $("#points").addEventListener("change", (e) => { const k = e.target.dataset.pts; if (k) PT[k].on = e.target.checked; if (k === "mm" && PT.mm.on) loadMM(); updatePoints(); });
    const CN = Object.fromEntries(D.cnsites.rows.map((r) => [String(r[2]), r]));
    const PREC = { 1: "exact spot", 2: "within about 25 km", 3: "district", 4: "province or state", 5: "near a province", 6: "whole country", 7: "estimated", 8: "whole country (country-wide project)" };
    for (const k of PTK) {
      map.on("mouseenter", "pt-" + k, () => (map.getCanvas().style.cursor = "pointer"));
      map.on("mouseleave", "pt-" + k, () => (map.getCanvas().style.cursor = ""));
      map.on("click", "pt-" + k, (e) => {
        const f = e.features[0], P = f.properties; let h;
        if (k === "wb") {
          const p = WP[P.id] || [];
          h = `<h3>${esc(P.place)}</h3><div class="src">World Bank project site · ${esc(PREC[P.pc] || "")}</div><div class="item"><a href="https://projects.worldbank.org/en/projects-operations/project-detail/${esc(P.id)}" target="_blank" rel="noopener">${esc(p[0])}</a><br><span class="m">${esc(P.id)} · ${esc(p[4])} · started ${p[5] || "–"} · ${esc(p[3])}</span><br>${usd(p[2])} committed to the whole project<br><span class="m">${esc(p[1])}</span></div><div class="note">Source: AidData and the World Bank, geocoded research release 1.4.2 (projects approved 1995–2014).</div>`;
        } else if (k === "cs") {
          h = caseCard(D.cases[P.i]);
        } else if (k === "pf") {
          h = pfCard(D.pf.rows[P.i]);
        } else if (k === "mm") {
          h = mmCard(D.mm.rows[P.i]);
        } else {
          const r = CN[String(P.i)] || [];
          h = `<h3>${esc(r[4])}</h3><div class="src">Chinese state-financed project site</div><div class="item">${esc(r[6])}<br><span class="m">${r[5] || "–"} · ${esc(r[8])} · ${esc(r[9])} · ${r[7] != null ? usd(r[7]) + " (2021 dollars)" : "amount not given"}</span><br><span class="m">Located: ${esc(r[10])}${r[11] ? ` · <a href="${esc(String(r[11]).split("|")[0])}" target="_blank" rel="noopener">on OpenStreetMap</a>` : ""} · AidData id ${esc(r[2])}</span></div><div class="note">Source: AidData, Geospatial Global Chinese Development Finance Dataset 3.0.</div>`;
        }
        if (!popup) popup = new maplibregl.Popup({ className: "lc-pop", maxWidth: "360px", focusAfterOpen: false });
        popup.setMaxWidth(k === "cs" ? "420px" : "360px");
        popup.setLngLat(f.geometry.coordinates).setHTML(h).addTo(map); popup._lc = null; popup._pt = true;
      });
    }
  }
  const yrsOf = (c) => (c.start == null ? "" : c.start + (c.end == null ? " to now" : c.end !== c.start ? "–" + c.end : ""));
  const para = (t) => (t ? `<p class="cs">${esc(t)}</p>` : "");
  function caseCard(c) {
    let h = `<h3>${esc(c.title)}</h3><div class="src">${esc(c.place)} · ${esc(yrsOf(c))}</div>`;
    h += `<span class="flag">${esc(CSKIND[c.mechanism] || c.mechanism)}</span>${c.confidence === "contested" ? `<span class="flag">Link disputed</span>` : ""}${c.killed ? `<span class="flag">${num(c.killed)} killed</span>` : ""}`;
    if (c.confidence === "contested" && c.confidence_note) h += `<h4>Why it is disputed</h4>${para(c.confidence_note)}`;
    if (c.lenders && c.lenders.length) h += `<h4>The lenders and what they did</h4>` + c.lenders.map((l) => `<p class="cs"><b>${esc(l.name)}</b>: ${esc(l.role)}</p>`).join("");
    if (c.conditions) h += `<h4>The condition</h4>${para(c.conditions)}`;
    if (c.companies && c.companies.length) h += `<h4>Companies</h4>` + c.companies.map((x) => `<p class="cs"><b>${esc(x.name)}</b>${x.hq ? ` (${esc(x.hq)})` : ""}: ${esc(x.role)}</p>`).join("");
    if (c.community) h += `<h4>What happened to people and land</h4>${para(c.community)}`;
    if (c.suppression) h += `<h4>How resistance was put down</h4>${para(c.suppression)}`;
    if (c.killed_note) h += `<h4>Deaths, and who counted them</h4>${para(c.killed_note)}`;
    if (c.outcome) h += `<h4>What happened next</h4>${para(c.outcome)}`;
    h += `<h4>Sources</h4>` + (c.sources || []).map((s) => `<div class="item">${s.url ? `<a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title || s.url)}</a>` : esc(s.title)}<br><span class="m">${esc(s.publisher || "")}${s.year ? " · " + s.year : ""}</span></div>`).join("");
    if (c.point) h += `<div class="note">The mark stands on: ${esc(c.point)}.</div>`;
    return h;
  }
  function pfCard(r) {
    const [x, y, cc, place, yImp, yDec, kind, svc, prev, cur, own, actors, actions, gov, org, motiv, approx, id, pop, summary, outc] = r;
    const row = (t, v) => (v ? `<tr><td>${t}</td><td>${esc(v)}</td></tr>` : "");
    return `<h3>${esc(place)}</h3><div class="src">Public Futures case ${esc(id)}${approx === 2 ? " · no matching place found, so placed at the middle of the country" : approx ? " · placed from the place name, approximate" : ""}</div>` +
      `<table>${row("What happened", kind)}${row("Service", svc)}${row("Run before by", prev)}${row("Run now by", cur)}${row("Year decided", yDec)}${row("Year carried out", yImp)}${row("Ownership now", own)}${row("Who pushed for it", actors)}${row("How", actions)}${row("Why", motiv)}${row("Results reported", outc)}${row("How it is run", gov)}${row("Kind of public body", org)}${row("People served", pop ? num(pop) : "")}</table>` +
      (summary ? para(summary) : "") +
      `<div class="note">Source: Public Futures database, University of Glasgow and the Transnational Institute, <a href="https://publicfutures.org/" target="_blank" rel="noopener">publicfutures.org</a>.</div>`;
  }
  let mmState = 0; // 0 not loaded, 1 loading, 2 loaded
  async function loadMM() {
    if (mmState) return; mmState = 1;
    const n = $("#n-mm"); n.textContent = "loading…";
    try {
      const res = await fetch(D.mm_meta.file); if (!res.ok) throw new Error(res.status);
      D.mm = JSON.parse(await new Response(res.body.pipeThrough(new DecompressionStream("gzip"))).text());
      const mmf = D.mm.rows.map((r, i) => {
        const dm = r[12].join("|"), rs = r[13].join("|");
        const f = (/price increases/.test(dm) ? 1 : 0) | (/labor wage/.test(dm) ? 2 : 0) | (/land farm/.test(dm) ? 4 : 0) | (r[17] ? 8 : 0) | (/shootings|killings/.test(rs) ? 16 : 0);
        return { type: "Feature", geometry: { type: "Point", coordinates: [r[0], r[1]] }, properties: { i, y: r[4] ?? -1, f } };
      });
      map.getSource("pt-mm").setData({ type: "FeatureCollection", features: mmf });
      mmState = 2; n.textContent = num(mmf.length);
    } catch (err) { mmState = 0; n.textContent = "could not load"; }
  }
  const MMPC = { 1: "placed at the town or city the record names", 2: "the record names a region; shown at its largest town", 3: "no town named or matched; shown at the capital" };
  function mmCard(r) {
    const [x, y, iso, country, year, start, end, loc, pc, at, parts, who, dem, res, viol, notes, srcs, imf, id] = r;
    const row = (t, v) => (v ? `<tr><td>${t}</td><td>${esc(v)}</td></tr>` : "");
    return `<h3>${esc(loc || country)}</h3><div class="src">${esc(country)} · ${esc(start || year)}${end && end !== start ? " to " + esc(end) : ""} · ${esc(MMPC[pc])}${pc !== 1 ? " (" + esc(at) + ")" : ""}</div>` +
      `<table>${row("Protesters", who)}${row("How many", parts)}${row("Demands", dem.join("; "))}${row("State response", res.join("; "))}${row("Protesters used violence", viol === 1 ? "yes" : viol === 0 ? "no" : "")}</table>` +
      (notes ? para(notes) : "") + (srcs ? `<div class="note">Newspaper sources the coders used: ${esc(srcs)}</div>` : "") +
      `<div class="note">Source: Mass Mobilization Project (Clark and Regan), record ${esc(id)}, <a href="https://doi.org/10.7910/DVN/HTTWYL" target="_blank" rel="noopener">Harvard Dataverse</a>.</div>`;
  }
  function updatePoints() {
    if (!map.getLayer("pt-wb")) return;
    const c = PTCOL[state.base] || PTCOL.land, exact = $("#pts-exact").checked;
    const yr = ["any", ["==", ["get", "y"], -1], ["all", [">=", ["get", "y"], state.from], ["<=", ["get", "y"], state.to]]];
    {
      const m = { all: 0, price: 1, wage: 2, land: 4, imf: 8, kill: 16 }[$("#mm-only").value];
      map.setLayoutProperty("pt-mm", "visibility", PT.mm.on ? "visible" : "none");
      map.setPaintProperty("pt-mm", "circle-color", c.mm); map.setPaintProperty("pt-mm", "circle-stroke-color", c.edge);
      $("#dot-mm").style.background = c.mm;
      map.setFilter("pt-mm", m ? ["all", yr, [">", ["%", ["floor", ["/", ["get", "f"], m]], 2], 0]] : yr);
    }
    for (const k of ["cs", "pf"]) {
      map.setLayoutProperty("pt-" + k, "visibility", PT[k].on ? "visible" : "none");
      map.setPaintProperty("pt-" + k, "circle-color", k === "cs" ? c.cs : c.pf);
      map.setPaintProperty("pt-" + k, "circle-stroke-color", k === "cs" ? ["case", ["==", ["get", "ct"], 1], c.cs, c.edge] : c.edge);
      $("#dot-" + k).style.background = c[k]; $("#dot-" + k).style.borderColor = k === "cs" ? c.edge : "";
      map.setFilter("pt-" + k, k === "cs" ? ["all", ["<=", ["get", "a"], state.to], [">=", ["get", "b"], state.from], ["!", ["in", ["get", "k"], ["literal", [...csOff]]]]] : yr);
    }
    for (const k of ["wb", "cn"]) {
      map.setLayoutProperty("pt-" + k, "visibility", PT[k].on ? "visible" : "none");
      map.setPaintProperty("pt-" + k, "circle-color", c[k]); map.setPaintProperty("pt-" + k, "circle-stroke-color", c.edge);
      $("#dot-" + k).style.background = c[k];
      map.setFilter("pt-" + k, exact ? ["all", yr, k === "wb" ? ["==", ["get", "pc"], 1] : ["==", ["get", "exact"], 1]] : yr);
      map.moveLayer("pt-" + k);
    }
    map.moveLayer("pt-mm"); map.moveLayer("pt-pf"); map.moveLayer("pt-cs");
  }

  // Breaks: seven classes from the spread of the non-zero values now shown,
  // rounded to plain numbers.
  function nice(v) { if (v <= 10) return Math.ceil(v); const p = 10 ** Math.floor(Math.log10(v)); for (const m of [1, 1.5, 2, 2.5, 3, 4, 5, 6, 7.5, 8, 10]) if (m * p >= v) return m * p; return 10 * p; }
  function breaksOf(vals) {
    const v = vals.filter((x) => x > 0).sort((a, b) => a - b);
    if (!v.length) return [];
    const out = [];
    for (let i = 1; i < 7; i++) { const q = v[Math.min(v.length - 1, Math.floor((i / 7) * v.length))]; const n = nice(q); if (!out.length || n > out[out.length - 1]) out.push(n); }
    if (out[out.length - 1] >= v[v.length - 1]) out.pop();
    return out;
  }
  // Each background has a ramp in its own colours: earthy greens on the Atlas and Jurassic.
  const rampFor = (l) => RAMPS[state.base === "night" ? "night" : state.base === "hell" ? "hell" : state.base === "atlas" || state.base === "jurassic" ? "moss" : l.ramp];

  function redraw() {
    if (!ready) return;
    const l = rowOf(state.active), o = state.opts[l.id];
    for (const r of document.querySelectorAll(".row")) r.classList.toggle("on", r.dataset.id === l.id);
    const radio = $(`.row[data-id="${l.id}"] input[type=radio]`); if (radio) radio.checked = true;
    const { values, unplaced, noTotal } = l.values(state.from, state.to, o);
    current = values;
    drawLines(l, o);
    if (l.cat) { drawCat(l, o, values); return; }
    const br = breaksOf([...values.values()]), ramp = rampFor(l);
    const cols = ramp.slice(ramp.length - (br.length + 1));
    for (const c of GEO.keys()) map.setFeatureState({ source: "lc", id: c }, { v: values.has(c) ? values.get(c) : null });
    const step = br.length ? ["step", ["feature-state", "v"], cols[0], ...br.flatMap((b, i) => [b, cols[i + 1]])] : cols[0];
    map.setPaintProperty("lc-fill", "fill-color", ["case", ["==", ["typeof", ["feature-state", "v"]], "number"],
      ["case", ["<=", ["feature-state", "v"], 0], NONE, step], "rgba(0,0,0,0)"]);
    map.setPaintProperty("lc-fill", "fill-opacity", state.base === "atlas" || state.base === "jurassic" ? 0.85 : 0.92);
    // Key
    const fmt = (v) => (l.fmt ? l.fmt(v, o) : o.measure === "agreed" ? sdr(v) : o.measure === "amt" ? usd(v) : num(v));
    const total = [...values.values()].reduce((s, v) => s + v, 0) + [...unplaced.values()].reduce((s, v) => s + v, 0);
    const shown = [...values.entries()].filter(([c, v]) => v > 0 && GEO.has(c)).length;
    let leg = `<div class="tot">${state.from} to ${state.to}: ${noTotal ? "" : esc(l.unit(total, o)) + " in all, "}${shown} countr${shown === 1 ? "y" : "ies"} on the map</div>`;
    const edges = [1, ...br];
    const money = l.cont || l.money || o.measure === "amt" || o.measure === "agreed" || o.measure === "usd";
    leg += cols.map((col, i) => {
      const lo = edges[i], hi = br[i];
      let txt;
      if (!br.length) txt = "Any number above none";
      else if (hi == null) txt = `${fmt(lo)} or more`;
      else if (money) txt = i === 0 ? `Under ${fmt(hi)}` : `${fmt(lo)} to under ${fmt(hi)}`;
      else txt = lo === hi - 1 ? fmt(lo) : `${fmt(lo)} to ${fmt(hi - 1)}`;
      return `<div class="k"><span class="sw" style="background:${col}"></span>${esc(txt)}</div>`; }).join("");
    leg += `<div class="k"><span class="sw" style="background:${NONE}"></span>${l.cont ? "Zero or less in these years" : "None recorded in these years"}</div>${l.cont ? `<div class="k"><span class="sw" style="background:transparent;border:1px solid #8A939D"></span>No figure published</div>` : ""}`;
    $(`#leg-${l.id}`).innerHTML = leg;
    for (const x of LAYERS) if (x.id !== l.id) { $(`#leg-${x.id}`).innerHTML = ""; $(`#un-${x.id}`).innerHTML = ""; }
    $(`#un-${l.id}`).innerHTML = unplaced.size ? `Counted in the total but with no shape on this map: ${[...unplaced.entries()].map(([n, v]) => `${esc(n)} (${esc(fmt(v))})`).join("; ")}.` : "";
    const outside = state.from > l.span[1] || state.to < l.span[0];
    $("#cover").textContent = outside ? `This row covers ${l.span[0]} to ${l.span[1]}; move the years into that range.` : `This row covers ${l.span[0]} to ${l.span[1]}.`;
    $("#now").textContent = `On the map now: ${l.short}${o.measure && l.id !== "all" ? ` (${optionText(l.id, o.measure)})` : ""}, ${state.from} to ${state.to}.`;
    if (popup && popup.isOpen() && popup._lc) openPopup(popup._lc, popup.getLngLat());
    updatePoints();
  }

  // Pattern rows colour countries by their role in the pattern.
  const CATCOL = { dark: ["#B9A6C9", "#8FB3B0", "#C79A9E", "#9DB0CC"], light: ["#5B476B", "#2F5E5A", "#7A3B45", "#3C5378"], hell: ["#CDB8D6", "#A9C4BE", "#E0C2B8", "#B7C6DA"] };
  const LINECOL = { land: "#E9E4D8", night: "#E9E4D8", atlas: "#2A2730", jurassic: "#2B2420", hell: "#F2EADF" };
  function drawCat(l, o, values) {
    const pal = CATCOL[state.base === "atlas" || state.base === "jurassic" ? "light" : state.base === "hell" ? "hell" : "dark"];
    for (const c of GEO.keys()) map.setFeatureState({ source: "lc", id: c }, { v: values.has(c) ? values.get(c) : null });
    map.setPaintProperty("lc-fill", "fill-color", ["match", ["coalesce", ["feature-state", "v"], -1], 1, pal[0], 2, pal[1], 3, pal[2], 4, pal[3], 5, "#8A8F96", "rgba(0,0,0,0)"]);
    map.setPaintProperty("lc-fill", "fill-opacity", state.base === "atlas" || state.base === "jurassic" ? 0.8 : 0.85);
    const n = (k) => [...values.values()].filter((v) => v === k).length;
    let leg = `<div class="tot">${values.size} countr${values.size === 1 ? "y" : "ies"} in this pattern</div>` + l.cat.map((t, i) => `<div class="k"><span class="sw" style="background:${pal[i]}"></span>${esc(t)} (${n(i + 1)})</div>`).join("");
    if (n(5)) leg += `<div class="k"><span class="sw" style="background:#8A8F96"></span>Other role (${n(5)})</div>`;
    if (l.lineNote) leg += `<div class="k"><span class="sw" style="background:transparent;border-top:2px solid ${LINECOL[state.base] || "#E9E4D8"};height:0;margin-top:6px"></span>${esc(l.lineNote)}</div>`;
    $(`#leg-${l.id}`).innerHTML = leg;
    for (const x of LAYERS) if (x.id !== l.id) { $(`#leg-${x.id}`).innerHTML = ""; $(`#un-${x.id}`).innerHTML = ""; }
    $(`#un-${l.id}`).innerHTML = "";
    $("#cover").textContent = `This pattern covers ${l.span[0]} to ${l.span[1]}. Its colours do not change with the years.`;
    $("#now").textContent = `On the map now: ${l.short}.`;
    if (popup && popup.isOpen() && popup._lc) openPopup(popup._lc, popup.getLngLat());
    updatePoints();
  }
  // Lines: great-circle arcs between the places a pattern connects.
  function arc(a, b) {
    const R = Math.PI / 180, [x1, y1] = [a[0] * R, a[1] * R], [x2, y2] = [b[0] * R, b[1] * R];
    const d = 2 * Math.asin(Math.sqrt(Math.sin((y2 - y1) / 2) ** 2 + Math.cos(y1) * Math.cos(y2) * Math.sin((x2 - x1) / 2) ** 2));
    if (d < 1e-6) return [a, b];
    const pts = [];
    for (let i = 0; i <= 48; i++) {
      const f = i / 48, A = Math.sin((1 - f) * d) / Math.sin(d), B = Math.sin(f * d) / Math.sin(d);
      const x = A * Math.cos(y1) * Math.cos(x1) + B * Math.cos(y2) * Math.cos(x2), y = A * Math.cos(y1) * Math.sin(x1) + B * Math.cos(y2) * Math.sin(x2), z = A * Math.sin(y1) + B * Math.sin(y2);
      pts.push([Math.atan2(y, x) / R, Math.atan2(z, Math.sqrt(x * x + y * y)) / R]);
    }
    for (let i = 1; i < pts.length; i++) { while (pts[i][0] - pts[i - 1][0] > 180) pts[i][0] -= 360; while (pts[i][0] - pts[i - 1][0] < -180) pts[i][0] += 360; }
    return pts;
  }
  function drawLines(l, o) {
    const src = map.getSource("pat-lines"); if (!src) return;
    const L = l.lines ? l.lines(state.from, state.to, o, popup && popup.isOpen() ? popup._lc : null) : [];
    const max = Math.max(1, ...L.map((x) => x.w || 1));
    src.setData({ type: "FeatureCollection", features: L.filter((x) => x.a && x.b).map((x) => ({ type: "Feature", geometry: { type: "LineString", coordinates: arc(x.a, x.b) }, properties: { label: x.label || "", w: 0.6 + 2.4 * Math.sqrt((x.w || 1) / max) } })) });
    map.setPaintProperty("pat-line", "line-color", LINECOL[state.base] || "#E9E4D8");
    map.moveLayer("pat-line");
  }
  map.on("load", () => {
    map.addSource("pat-lines", { type: "geojson", data: { type: "FeatureCollection", features: [] } });
    map.addLayer({ id: "pat-line", type: "line", source: "pat-lines", layout: { "line-cap": "round" }, paint: { "line-color": "#E9E4D8", "line-width": ["*", 1.3, ["get", "w"]], "line-opacity": 0.85 } });
    map.on("mousemove", "pat-line", (e) => { const f = e.features[0]; if (!f || !f.properties.label) return; hoverTip.textContent = f.properties.label; hoverTip.style.display = "block"; hoverTip.style.left = e.point.x + 14 + "px"; hoverTip.style.top = e.point.y + 10 + "px"; });
  });

  // Click and hover
  let popup = null, hovered = null;
  const hoverTip = $("#tip");
  function openPopup(c, lngLat) {
    const l = rowOf(state.active), o = state.opts[l.id];
    const v = current.get(c);
    const html = `<h3>${esc(GEO.get(c) || c)}</h3><div class="src">${esc(l.title)} · ${state.from} to ${state.to}</div>` +
      (v == null ? `<div class="note">This source has no record for this country.</div>` : l.popup(c, state.from, state.to, o));
    if (!popup) popup = new maplibregl.Popup({ className: "lc-pop", maxWidth: "360px", focusAfterOpen: false });
    popup.setLngLat(lngLat).setHTML(html).addTo(map); popup._lc = c;
    if (l.linesFollowClick) drawLines(l, o);
  }
  map.on("click", "lc-fill", (e) => { if (map.queryRenderedFeatures(e.point, { layers: ["pt-wb", "pt-cn", "pt-cs", "pt-pf", "pt-mm"].filter((l) => map.getLayer(l)) }).length) return; const f = e.features && e.features[0]; if (f && f.properties.iso3 !== "-99") openPopup(f.properties.iso3, e.lngLat); });
  map.on("mousemove", "lc-fill", (e) => {
    const f = e.features && e.features[0]; if (!f) return;
    const c = f.properties.iso3;
    if (hovered !== c) { if (hovered) map.setFeatureState({ source: "lc", id: hovered }, { hover: false }); hovered = c !== "-99" ? c : null; if (hovered) map.setFeatureState({ source: "lc", id: hovered }, { hover: true }); }
    map.getCanvas().style.cursor = "pointer";
    const l = rowOf(state.active), v = current.get(c);
    hoverTip.innerHTML = `${esc(f.properties.name)}: ${v == null ? "no record" : esc(l.unit(v, state.opts[l.id]))}`;
    hoverTip.style.display = "block"; hoverTip.style.left = e.point.x + 14 + "px"; hoverTip.style.top = e.point.y + 10 + "px";
  });
  map.on("mouseleave", "lc-fill", () => { if (hovered) map.setFeatureState({ source: "lc", id: hovered }, { hover: false }); hovered = null; hoverTip.style.display = "none"; map.getCanvas().style.cursor = ""; });

  /* ------------------------------------------------------------ backgrounds */
  // Each basemap's layers, added the first time it is chosen, under every
  // layer the rows draw.
  const OFM = { type: "vector", url: "https://tiles.openfreemap.org/planet", attribution: '<a href="https://openfreemap.org" target="_blank" rel="noopener">OpenFreeMap</a> © OpenStreetMap contributors' };
  const RELIEF = { type: "raster-dem", tiles: ["https://tiles.mapterhorn.com/{z}/{x}/{y}.webp"], encoding: "terrarium", tileSize: 512, maxzoom: 12, attribution: '<a href="https://mapterhorn.com/attribution" target="_blank" rel="noopener">© Mapterhorn</a>' };
  const SEA = { type: "raster-dem", tiles: ["https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"], encoding: "terrarium", tileSize: 256, maxzoom: 12, attribution: '<a href="https://registry.opendata.aws/terrain-tiles/" target="_blank" rel="noopener">AWS Terrain Tiles</a>' };
  const ESRI = { type: "raster", tiles: ["https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"], tileSize: 256, maxzoom: 18, attribution: "Imagery © Esri, Maxar, Earthstar Geographics and the GIS user community" };
  const BASES = {
    night: () => {
      const road = (w) => ["interpolate", ["exponential", 1.4], ["zoom"], 6, w * .3, 10, w, 16, w * 5];
      const kind = (list) => ["match", ["get", "class"], list, true, false];
      const fade = (z0, z1, a) => ["interpolate", ["linear"], ["zoom"], z0, 0, z1, a];
      return { sources: { "b-night": { type: "raster", tiles: ["nhnight://{z}/{y}/{x}"], tileSize: 256, maxzoom: 8,
          attribution: '<a href="https://earthobservatory.nasa.gov/features/NightLights" target="_blank" rel="noopener">NASA Black Marble 2016</a> via GIBS' }, "b-relief": RELIEF, "b-sea": SEA, "b-osm": OFM },
        layers: [
          { id: "b-night-sheet", type: "background", paint: { "background-color": "#02040C" } },
          { id: "b-night-lights", type: "raster", source: "b-night", paint: { "raster-fade-duration": 200 } },
          { id: "b-night-shade", type: "hillshade", source: "b-relief", paint: NIGHT.shade },
          { id: "b-night-sea-glow", type: "color-relief", source: "b-sea", paint: { "color-relief-color": NIGHT.seaGlow, "color-relief-opacity": 1 } },
          { id: "b-night-road-glow", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 7, filter: kind(["motorway", "trunk", "primary"]),
            layout: { "line-cap": "round", "line-join": "round" }, paint: { "line-color": NIGHT.roadGlow, "line-width": road(3), "line-blur": road(2.5), "line-opacity": fade(7, 10, .35) } },
          { id: "b-night-road-minor", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 11, filter: kind(["minor", "service", "street", "street_limited"]),
            paint: { "line-color": NIGHT.road[0], "line-width": road(.4), "line-opacity": fade(11, 13, 1) } },
          { id: "b-night-road", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 9, filter: kind(["secondary", "tertiary"]),
            paint: { "line-color": NIGHT.road[1], "line-width": road(.5), "line-opacity": fade(9, 11, 1) } },
          { id: "b-night-road-major", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 7, filter: kind(["motorway", "trunk", "primary"]),
            layout: { "line-cap": "round", "line-join": "round" }, paint: { "line-color": NIGHT.road[2], "line-width": road(.6), "line-opacity": fade(7, 9, 1) } },
          { id: "b-night-border", type: "line", source: "land", paint: { "line-color": NIGHT.border, "line-width": ["interpolate", ["linear"], ["zoom"], 2, .4, 6, .8] } },
        ] };
    },
    atlas: () => ({
      sources: { "b-esri": ESRI,
        "b-hill": { type: "raster", tiles: ["https://services.arcgisonline.com/arcgis/rest/services/Elevation/World_Hillshade/MapServer/tile/{z}/{y}/{x}"], tileSize: 256, maxzoom: 16, attribution: "Hillshade © Esri" },
        "b-plate": { type: "raster", tiles: ["nhplate://{z}/{x}/{y}"], tileSize: 256, maxzoom: 3, bounds: [-180, PLATE.bottom, 180, PLATE.top], attribution: "Painted atlas: Welcome to Your Galaxy" },
        "b-labels": { type: "raster", tiles: ["https://a.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}@2x.png?key=cb1_494p_1_eebbbfcb65bc573e54783d42"], tileSize: 256, attribution: "Labels © CARTO, © OpenStreetMap" } },
      layers: [
        { id: "b-atlas-sea", type: "background", paint: { "background-color": "#0B1017" } },
        { id: "b-atlas-img", type: "raster", source: "b-esri", paint: { "raster-brightness-min": .03, "raster-brightness-max": 1, "raster-saturation": .15, "raster-contrast": .05, "raster-hue-rotate": -6 } },
        { id: "b-atlas-hill", type: "raster", source: "b-hill", paint: { "raster-opacity": ["interpolate", ["linear"], ["zoom"], 4, .18, 9, .34, 13, .46] } },
        { id: "b-atlas-plate", type: "raster", source: "b-plate", paint: { "raster-opacity": ["interpolate", ["linear"], ["zoom"], PLATE.fadeIn, 1, PLATE.fadeOut, 0], "raster-fade-duration": 0 } },
        { id: "b-atlas-labels", type: "raster", source: "b-labels", paint: { "raster-opacity": ["interpolate", ["linear"], ["zoom"], PLATE.fadeIn, 0, PLATE.fadeOut, .92] } },
      ] }),
    // Jurassic: the Culprits map's basemap of that name (its Satellite
    // imagery basemap, map/app.js BASE_GRADE.satellite, SAT_RELIEF and
    // addSatelliteRelief): Esri's photographs lightly muted, a see-through
    // palette by height (deep green lowlands, olive, ochre and sienna slopes,
    // grey-brown rock; navy deeps and blue-green shelves at sea), Swiss-style
    // shading from four lights and a second north-west light, a calm navy
    // over the deep sea, and grey place names (round nh12, asked 19 October).
    // Its 3D terrain, grain and frame are not copied.
    jurassic: () => ({
      sources: { "b-esri": ESRI, "b-relief": RELIEF, "b-sea": SEA,
        "b-labels": { type: "raster", tiles: ["https://a.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}@2x.png?key=cb1_494p_1_eebbbfcb65bc573e54783d42"], tileSize: 256, attribution: "Labels © CARTO, © OpenStreetMap" } },
      layers: [
        { id: "b-jur-sea", type: "background", paint: { "background-color": "#0B1017" } },
        { id: "b-jur-img", type: "raster", source: "b-esri", paint: { "raster-brightness-min": 0.02, "raster-brightness-max": 0.92, "raster-saturation": 0.12, "raster-contrast": 0.06, "raster-hue-rotate": 0 } },
        { id: "b-jur-colour", type: "color-relief", source: "b-relief", paint: { "color-relief-color": JURASSIC.colour, "color-relief-opacity": 1 } },
        { id: "b-jur-seabed", type: "color-relief", source: "b-sea", paint: { "color-relief-color": JURASSIC.seabed, "color-relief-opacity": 1 } },
        { id: "b-jur-shade", type: "hillshade", source: "b-relief", paint: JURASSIC.shade },
        { id: "b-jur-depth", type: "hillshade", source: "b-relief", paint: JURASSIC.depth },
        { id: "b-jur-calm", type: "color-relief", source: "b-sea", paint: { "color-relief-color": JURASSIC.sea, "color-relief-opacity": 1 } },
        { id: "b-jur-labels", type: "raster", source: "b-labels", paint: { "raster-opacity": 0.8, "raster-saturation": -1 } },
      ] }),
    hell: () => {
      const road = (w) => ["interpolate", ["exponential", 1.4], ["zoom"], 4, w * .25, 10, w, 16, w * 6];
      const kind = (list) => ["match", ["get", "class"], list, true, false];
      const fade = (z0, z1, a) => ["interpolate", ["linear"], ["zoom"], z0, 0, z1, a];
      const nm = ["coalesce", ["get", "name_en"], ["get", "name:latin"], ["get", "name"]];
      const zs = (...a) => ["interpolate", ["linear"], ["zoom"], ...a];
      const halo = (c, w) => ({ "text-halo-color": c, "text-halo-width": w, "text-halo-blur": 0.6 });
      const N = HELL.name, F = HELL.font;
      return { sources: { "b-relief": RELIEF, "b-sea": SEA, "b-osm": OFM },
        layers: [
          { id: "b-hell-sheet", type: "background", paint: { "background-color": HELL.sheet } },
          { id: "b-hell-ground", type: "color-relief", source: "b-sea", paint: { "color-relief-color": HELL.ground, "color-relief-opacity": 1 } },
          { id: "b-hell-shade", type: "hillshade", source: "b-relief", paint: HELL.shade },
          { id: "b-hell-coast", type: "fill", source: "b-osm", "source-layer": "water", minzoom: 7, filter: ["==", ["get", "class"], "ocean"],
            paint: { "fill-color": HELL.coast, "fill-opacity": fade(7, 9, 1) } },
          { id: "b-hell-lake", type: "fill", source: "b-osm", "source-layer": "water", filter: ["!=", ["get", "class"], "ocean"],
            paint: { "fill-color": HELL.lake, "fill-outline-color": HELL.lakeEdge } },
          { id: "b-hell-town", type: "fill", source: "b-osm", "source-layer": "landuse", minzoom: 6, filter: kind(["residential", "commercial", "industrial", "retail", "suburb", "neighbourhood"]),
            paint: { "fill-color": ["match", ["get", "class"], "industrial", HELL.townWork, HELL.town], "fill-opacity": fade(6, 8, .9) } },
          { id: "b-hell-grave", type: "fill", source: "b-osm", "source-layer": "landuse", minzoom: 9, filter: ["==", ["get", "class"], "cemetery"],
            paint: { "fill-color": HELL.grave, "fill-outline-color": HELL.graveEdge, "fill-opacity": fade(9, 11, .8) } },
          { id: "b-hell-river-glow", type: "line", source: "b-osm", "source-layer": "waterway", minzoom: 3, filter: ["==", ["get", "class"], "river"],
            layout: { "line-cap": "round", "line-join": "round" }, paint: { "line-color": HELL.riverGlow, "line-width": road(4), "line-blur": road(3), "line-opacity": .45 } },
          { id: "b-hell-river", type: "line", source: "b-osm", "source-layer": "waterway", minzoom: 3, layout: { "line-cap": "round", "line-join": "round" },
            paint: { "line-color": HELL.river,
              "line-width": ["interpolate", ["exponential", 1.4], ["zoom"], 4, ["match", ["get", "class"], "river", .25, .11], 10, ["match", ["get", "class"], "river", 1, .45], 16, ["match", ["get", "class"], "river", 6, 2.7]],
              "line-opacity": ["interpolate", ["linear"], ["zoom"], 8, ["match", ["get", "class"], "river", .9, 0], 11, ["match", ["get", "class"], "river", .9, .7]] } },
          { id: "b-hell-rail", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 9, filter: kind(["rail", "transit"]),
            paint: { "line-color": HELL.rail, "line-width": 1, "line-dasharray": [3, 2] } },
          { id: "b-hell-road-minor", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 11, filter: kind(["minor", "service", "track", "street", "street_limited"]),
            paint: { "line-color": HELL.road[0], "line-width": road(.45) } },
          { id: "b-hell-road", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 7, filter: kind(["secondary", "tertiary"]),
            paint: { "line-color": HELL.road[1], "line-width": road(.6) } },
          { id: "b-hell-road-major", type: "line", source: "b-osm", "source-layer": "transportation", minzoom: 4, filter: kind(["motorway", "trunk", "primary"]),
            paint: { "line-color": HELL.road[2], "line-width": road(.8), "line-opacity": fade(4, 6, 1) } },
          { id: "b-hell-buildings", type: "fill", source: "b-osm", "source-layer": "building", minzoom: 13, paint: { "fill-color": HELL.building, "fill-opacity": .9 } },
          { id: "b-hell-border", type: "line", source: "land", paint: { "line-color": HELL.border, "line-width": ["interpolate", ["linear"], ["zoom"], 2, .5, 5, .9] } },
          { id: "b-hell-name-ocean", type: "symbol", source: "b-osm", "source-layer": "water_name", filter: kind(["ocean", "sea"]),
            layout: { "text-field": nm, "text-font": F.italic, "text-size": zs(1, 11, 6, 16), "text-letter-spacing": 0.22, "text-max-width": 6 },
            paint: Object.assign({ "text-color": N.water }, halo(N.haloWater, 1)) },
          { id: "b-hell-name-water", type: "symbol", source: "b-osm", "source-layer": "water_name", minzoom: 5, filter: ["!", kind(["ocean", "sea"])],
            layout: { "text-field": nm, "text-font": F.italic, "text-size": zs(5, 11, 14, 14), "text-letter-spacing": 0.08, "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.water }, halo(N.haloWater, 1)) },
          { id: "b-hell-name-river", type: "symbol", source: "b-osm", "source-layer": "waterway", minzoom: 9,
            layout: { "text-field": nm, "text-font": F.italic, "text-size": zs(9, 11, 15, 14), "symbol-placement": "line", "text-letter-spacing": 0.1 },
            paint: Object.assign({ "text-color": N.water }, halo(N.haloWater, 1)) },
          { id: "b-hell-name-peak", type: "symbol", source: "b-osm", "source-layer": "mountain_peak", minzoom: 9,
            layout: { "text-field": nm, "text-font": F.italic, "text-size": 12, "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.peak }, halo(N.halo, 1.1)) },
          { id: "b-hell-name-village", type: "symbol", source: "b-osm", "source-layer": "place", minzoom: 11, filter: kind(["village", "hamlet", "suburb", "neighbourhood", "quarter"]),
            layout: { "text-field": nm, "text-font": F.regular, "text-size": zs(11, 11, 16, 14), "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.minor }, halo(N.halo, 1.2)) },
          { id: "b-hell-name-town", type: "symbol", source: "b-osm", "source-layer": "place", minzoom: 7, filter: kind(["town"]),
            layout: { "text-field": nm, "text-font": F.regular, "text-size": zs(7, 11, 14, 16), "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.town }, halo(N.halo, 1.2)) },
          { id: "b-hell-name-state", type: "symbol", source: "b-osm", "source-layer": "place", minzoom: 4, maxzoom: 9, filter: kind(["state", "province"]),
            layout: { "text-field": nm, "text-font": F.italic, "text-size": zs(4, 10, 8, 13), "text-transform": "uppercase", "text-letter-spacing": 0.15, "text-max-width": 8 },
            paint: Object.assign({ "text-color": N.state, "text-opacity": 0.9 }, halo(N.halo, 1)) },
          { id: "b-hell-name-city", type: "symbol", source: "b-osm", "source-layer": "place", minzoom: 3, filter: kind(["city"]),
            layout: { "text-field": nm, "text-font": F.bold, "text-size": zs(3, 11, 8, 15, 14, 20), "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.city }, halo(N.halo, 1.3)) },
          { id: "b-hell-name-country", type: "symbol", source: "b-osm", "source-layer": "place", maxzoom: 8, filter: kind(["country"]),
            layout: { "text-field": nm, "text-font": F.bold, "text-size": zs(1, 10, 3, 13, 6, 17), "text-transform": "uppercase", "text-letter-spacing": 0.26, "text-max-width": 7 },
            paint: Object.assign({ "text-color": N.country }, halo(N.halo, 1.3)) },
        ] };
    },
  };

  const added = new Set();
  function setBase(kind) {
    if (BASES[kind] && !added.has(kind)) {
      const b = BASES[kind]();
      if (kind === "hell" && map.setGlyphs && !map.getGlyphs()) map.setGlyphs(HELL.glyphs);
      for (const [k, v] of Object.entries(b.sources)) if (!map.getSource(k)) map.addSource(k, v);
      for (const l of b.layers) map.addLayer(Object.assign({}, l, { layout: Object.assign({}, l.layout || {}, { visibility: "none" }) }), l.type === "symbol" ? undefined : "land-edge");
      added.add(kind);
    }
    for (const k of added) for (const l of BASES[k]().layers) if (map.getLayer(l.id)) map.setLayoutProperty(l.id, "visibility", k === kind ? "visible" : "none");
    map.setLayoutProperty("land", "visibility", kind === "land" ? "visible" : "none");
    map.setLayoutProperty("land-edge", "visibility", kind === "land" ? "visible" : "none");
    state.base = kind;
    syncSheets();
    redraw();
  }
  $("#basemap").addEventListener("click", (e) => {
    const b = e.target.closest("button[data-base]"); if (!b) return;
    const go = () => setBase(b.dataset.base);
    if (ready) go(); else map.once("load", go);
    for (const x of document.querySelectorAll("#basemap button")) x.classList.toggle("on", x === b);
  });
  $("#fold").addEventListener("click", (e) => {
    const s = $("#side"); s.classList.toggle("folded");
    e.target.textContent = s.classList.contains("folded") ? "Open ▾" : "Fold up ▴";
  });
})();
