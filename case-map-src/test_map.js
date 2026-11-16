// Headless check for globalization.html.
//
// Two things here are not obvious and both have cost a round:
//
// 1. The completeness figures are computed in the browser, so clicking #infoBtn
//    and taking the text of #info is the only way to read them. Grepping the
//    built file returns the raw <!--COMPLETENESS--> marker.
// 2. The eight-row "How much of all lending does this map cover?" table is in
//    #brief from load, but #brief's PARENT has display:none because S.kindOpen
//    starts false — and innerText returns "" for anything inside a hidden
//    element, while textContent returns it all. Round 37 concluded the brief
//    "was not re-read" on exactly that, and then mis-stated one of its rows from
//    a count of its own instead. Read #brief with textContent. Clicking the kind
//    bar is neither necessary nor sufficient: the content is already there.
//    Read the figures, never compute them — the page's own count of Chinese
//    state lending is 91 where a naive count of lk:"cn" cases gives 93.
const { chromium } = require('playwright');

(async () => {
  const pageErrors = [], consoleErrors = [];
  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  const page = await browser.newPage();

  page.on('pageerror', e => pageErrors.push(String(e.message || e)));
  page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text()); });

  await page.goto('http://localhost:8766/globalization.html', { waitUntil: 'load', timeout: 120000 });
  await page.waitForTimeout(9000);

  const counts = await page.evaluate(() => ({
    cases: (window.CASES || []).length,
    pats: (window.PATS || []).length,
    hyps: (window.HYPS || []).length,
  }));

  // --- About panel ---
  let about = '';
  try {
    await page.evaluate(() => document.querySelector('#infoBtn').click());
    await page.waitForTimeout(3500);
    about = await page.evaluate(() => (document.querySelector('#info') || {}).innerText || '');
    await page.evaluate(() => { const c = document.querySelector('#infoClose'); if (c) c.click(); });
    await page.waitForTimeout(600);
  } catch (e) { about = 'ABOUT READ FAILED: ' + e.message; }

  // --- the lending-coverage brief: textContent, because its parent is hidden ---
  let brief = '';
  try {
    brief = await page.evaluate(() => {
      const el = document.querySelector('#brief');
      return el ? (el.textContent || '') : '';
    });
  } catch (e) { brief = 'BRIEF READ FAILED: ' + e.message; }

  console.log('=== counts ===');
  console.log(JSON.stringify(counts));
  console.log('=== page errors (' + pageErrors.length + ') ===');
  pageErrors.slice(0, 15).forEach(e => console.log('  ' + e));
  console.log('=== console errors (' + consoleErrors.length + ') ===');
  consoleErrors.slice(0, 15).forEach(e => console.log('  ' + e));

  console.log('\n=== About: completeness rows ===');
  console.log(about.split('\n').filter(l => /\bof\s[\d,]+|%|holds [\d,]+ cases/i.test(l)).join('\n').slice(0, 2500));

  console.log('\n=== lending-coverage brief ===');
  const i = brief.indexOf('How much of all lending');
  if (i < 0) {
    console.log('!! section still not reachable; brief length = ' + brief.length);
  } else {
    console.log(brief.slice(i, i + 3000));
  }

  await browser.close();
  process.exit(pageErrors.length + consoleErrors.length > 0 ? 1 : 0);
})();
