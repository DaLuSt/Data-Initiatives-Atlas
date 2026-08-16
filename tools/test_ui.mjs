/* Browser tests for the Atlas graph UI (brief §28).
 *
 * These are optional and NOT part of the CI gate: they need Playwright and a
 * Chromium build, which the validation workflow deliberately does not install.
 * The Python suite (tools/test_build_graph.py) is the required gate.
 *
 * Run locally:
 *     python -m http.server 8765 --directory site &
 *     npm install playwright && npx playwright install chromium
 *     node tools/test_ui.mjs
 *
 * Override the target with BASE, and the browser binary with CHROME_PATH.
 */

import { chromium } from 'playwright';

const BASE = process.env.BASE || 'http://127.0.0.1:8765';
const results = [];
let failed = 0;

function check(name, ok, extra = '') {
  results.push(`${ok ? 'PASS' : 'FAIL'}  ${name}${extra ? ' — ' + extra : ''}`);
  if (!ok) failed++;
}

const browser = await chromium.launch(
  process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});

async function newPage(vp) {
  const ctx = await browser.newContext({ viewport: vp });
  const page = await ctx.newPage();
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push('PAGEERROR: ' + e.message));
  page.on('requestfailed', r => errors.push('REQFAIL: ' + r.url()));
  return { ctx, page, errors };
}


async function search(page, q) {
  await page.fill('#search', '');
  await page.waitForTimeout(160);
  await page.fill('#search', q);
  await page.waitForFunction(
    (expected) => {
      const box = document.getElementById('search');
      if (box.value !== expected) return false;
      const ul = document.getElementById('suggestions');
      return !ul.hidden && ul.querySelectorAll('li').length > 0;
    }, q, { timeout: 8000 });
  await page.waitForTimeout(60);
}

// ─────────────────────────── desktop ───────────────────────────
{
  const { ctx, page, errors } = await newPage({ width: 1440, height: 900 });
  await page.goto(BASE + '/index.html', { waitUntil: 'networkidle' });
  await page.waitForFunction(() => document.getElementById('loading').hidden, null, { timeout: 15000 });

  check('page loads with no console/page errors', errors.length === 0, errors.slice(0, 4).join(' | '));

  const nodeCount = await page.evaluate(() => document.querySelectorAll('#cy canvas').length);
  check('cytoscape canvas rendered', nodeCount > 0, `${nodeCount} canvases`);

  const stats = await page.textContent('#stats');
  check('stats rendered dynamically', /\d/.test(stats));

  const gen = await page.textContent('#generated');
  check('generation date shown', /Atlas generated: \w/.test(gen), gen.trim());

  const status = await page.textContent('#stage-status');
  check('status line reports entity counts', /entities/.test(status), status.trim());

  // facets discovered dynamically
  const countries = await page.$$eval('#f-country .check .cname', els => els.map(e => e.textContent));
  check('countries discovered from data (not hard-coded)',
        countries.includes('Netherlands') && countries.includes('Germany'),
        countries.join(','));

  const levels = await page.$$eval('#f-level .check .cname', els => els.map(e => e.textContent));
  check('geographic levels present', levels.length >= 3, levels.join(','));

  // ── search ──
  await search(page, 'data act');
  const sug = await page.$$eval('#suggestions li[data-id]', els => els.map(e => e.dataset.id));
  check('search returns results', sug.length > 0, sug.slice(0, 3).join(','));
  check('search finds EU-DATA-ACT', sug.includes('EU-DATA-ACT'), sug.slice(0, 5).join(','));

  // search by ID
  await search(page, 'DE-BDSG');
  const byId = await page.$$eval('#suggestions li[data-id]', els => els.map(e => e.dataset.id));
  check('search by ID works', byId[0] === 'DE-BDSG', byId.slice(0, 3).join(','));

  // search by country name
  await search(page, 'Germany');
  const byCountry = await page.$$eval('#suggestions li[data-id]', els => els.map(e => e.dataset.id));
  check('search by country works', byCountry.includes('DE'), byCountry.slice(0, 3).join(','));

  // keyboard nav + select
  await search(page, 'EU Data Act');
  await page.keyboard.press('ArrowDown');
  await page.keyboard.press('Enter');
  await page.waitForSelector('#detail:not([hidden])', { timeout: 5000 });
  check('keyboard search selection opens detail panel', true);

  const title = await page.textContent('.d-title');
  check('detail panel shows entity name', /Data Act/i.test(title), title);

  await page.waitForFunction(() => {
    const d = document.querySelector('.d-desc');
    return d && !d.classList.contains('hint') && d.textContent.length > 40;
  }, null, { timeout: 8000 });
  check('detail description loaded from details.json', true);

  const chips = await page.$$eval('.chips .chip', els => els.map(e => e.textContent));
  check('detail shows type/level/status chips', chips.length >= 3, chips.join(' | '));

  const secs = await page.$$eval('.d-sec h4', els => els.map(e => e.textContent));
  check('detail shows relationships section', secs.some(s => /Relationship/i.test(s)), secs.join(','));
  check('detail shows sources section', secs.some(s => /Sources/i.test(s)), secs.join(','));

  // GitHub link
  const gh = await page.getAttribute('.ghlink', 'href');
  check('GitHub entity link present and well-formed',
        /^https:\/\/github\.com\/[^/]+\/[^/]+\/blob\/[^/]+\/legislation\/eu-data-act\.md$/.test(gh), gh);

  // evidence from details.json
  const ev = await page.$$eval('.evidence', els => els.length);
  check('relationship evidence rendered', ev > 0, `${ev} evidence blocks`);

  // navigate via a related entity button
  const relBtn = await page.$('.rel-target');
  if (relBtn) {
    const targetId = await relBtn.getAttribute('data-goto');
    await relBtn.click();
    await page.waitForTimeout(400);
    const newTitle = await page.textContent('.d-title');
    check('clicking a related entity navigates the panel', newTitle.length > 0, `${targetId} → ${newTitle}`);
  }

  // deep link
  await page.goto(BASE + '/index.html#NL-NORA', { waitUntil: 'networkidle' });
  await page.reload({ waitUntil: 'networkidle' });
  await page.waitForFunction(() => document.getElementById('loading').hidden, null, { timeout: 15000 });
  await page.waitForSelector('#detail:not([hidden])', { timeout: 8000 });
  const dlTitle = await page.textContent('.d-title');
  check('deep link #NL-NORA opens that entity', /NORA|Nederlandse Overheid/i.test(dlTitle), dlTitle);
  const viewPressed = await page.getAttribute('#view-explorer', 'aria-pressed');
  check('deep link switches to Entity Explorer', viewPressed === 'true');

  // explorer neighbourhood is smaller than the whole graph
  const st1 = await page.textContent('#stage-status');
  check('explorer shows a neighbourhood, not everything', /neighbourhood/.test(st1), st1.trim());

  // ── filters ──
  await page.click('#view-atlas');
  await page.waitForTimeout(500);
  const beforeFilter = await page.textContent('#stage-status');
  const m1 = beforeFilter.match(/^([\d,]+) of/);

  await page.click('#f-country label:has-text("Germany")');
  await page.waitForTimeout(600);
  const afterFilter = await page.textContent('#stage-status');
  const m2 = afterFilter.match(/^([\d,]+) of/);
  const n1 = m1 ? +m1[1].replace(/,/g, '') : -1;
  const n2 = m2 ? +m2[1].replace(/,/g, '') : -1;
  check('country filter reduces the graph', n2 > 0 && n2 < n1, `${n1} → ${n2}`);

  await page.click('#reset-filters');
  await page.waitForTimeout(500);
  const afterReset = await page.textContent('#stage-status');
  const m3 = afterReset.match(/^([\d,]+) of/);
  check('reset filters restores the graph', m3 && +m3[1].replace(/,/g, '') === n1, `${n2} → ${m3 && m3[1]}`);

  // level filter
  await page.click('#f-level label:has-text("International")');
  await page.waitForTimeout(500);
  const lvlStatus = await page.textContent('#stage-status');
  const m4 = lvlStatus.match(/^([\d,]+) of/);
  check('level filter works', m4 && +m4[1].replace(/,/g, '') < n1, lvlStatus.trim());
  await page.click('#reset-filters');
  await page.waitForTimeout(400);

  // edge class toggle
  const relOnly = await page.textContent('#stage-status');
  const e1 = +(relOnly.match(/· ([\d,]+) connections/) || [0, '0'])[1].replace(/,/g, '');
  await page.click('#edge-classes label:has-text("Wikilinks")');
  await page.waitForTimeout(700);
  const withWiki = await page.textContent('#stage-status');
  const e2 = +(withWiki.match(/· ([\d,]+) connections/) || [0, '0'])[1].replace(/,/g, '');
  check('edge-class toggle adds wikilink edges', e2 > e1, `${e1} → ${e2}`);
  await page.click('#edge-classes label:has-text("Wikilinks")');
  await page.waitForTimeout(400);

  // relationship type filter
  await page.click('summary:has-text("Relationship types")');
  await page.waitForTimeout(200);
  await page.click('#rel-types label:has-text("applies-in")');
  await page.waitForTimeout(600);
  const relFiltered = await page.textContent('#stage-status');
  const e3 = +(relFiltered.match(/· ([\d,]+) connections/) || [0, '0'])[1].replace(/,/g, '');
  check('relationship-type filter narrows edges', e3 > 0 && e3 < e1, `${e1} → ${e3}`);
  await page.click('#reset-filters');
  await page.waitForTimeout(400);

  // ── domain filter (taxonomy.md §1.1 — the cross-cutting axis) ──
  const domains = await page.$$eval('#f-domain .check .cname', els => els.map(e => e.textContent));
  check('domains discovered from data (not hard-coded)',
    domains.length >= 2 && domains.includes('Cybersecurity'), domains.join(','));

  await page.click('#f-domain label:has-text("Cybersecurity")');
  await page.waitForTimeout(600);
  const domStatus = await page.textContent('#stage-status');
  const m5 = domStatus.match(/^([\d,]+) of/);
  const n5 = m5 ? +m5[1].replace(/,/g, '') : -1;
  check('domain filter narrows the graph to that domain', n5 > 1 && n5 < n1, `${n1} → ${n5}`);

  // The domain entity itself carries no `domains:` of its own; it must
  // survive its own filter, or the tagged entities lose their shared hub.
  await page.click('#view-list');
  await page.waitForTimeout(400);
  const domRows = await page.$$eval('#list-body tr td:first-child', els => els.map(e => e.textContent.trim()));
  check('domain filter keeps the domain entity itself',
    domRows.some(r => /Cybersecurity/i.test(r)), `${domRows.length} rows`);
  check('domain filter keeps entities tagged with it',
    domRows.length === n5 && domRows.length > 2, `${domRows.length} rows vs ${n5} nodes`);
  await page.click('#view-atlas');
  await page.waitForTimeout(400);
  await page.click('#reset-filters');
  await page.waitForTimeout(400);

  // ── provenance and confidence (auditability) ──
  await page.click('summary:has-text("Provenance")');
  await page.waitForTimeout(200);
  const provs = await page.$$eval('#f-provenance .check .cname', els => els.map(e => e.textContent));
  check('provenance facet uses the repository vocabulary',
    provs.includes('fact') && provs.includes('interpretation'), provs.join(','));

  await page.click('#f-provenance label:has-text("interpretation")');
  await page.waitForTimeout(600);
  const provStatus = await page.textContent('#stage-status');
  const e4 = +(provStatus.match(/· ([\d,]+) connections/) || [0, '0'])[1].replace(/,/g, '');
  check('provenance filter isolates the Atlas\'s own interpretations',
    e4 > 0 && e4 < e1, `${e1} → ${e4}`);
  await page.click('#reset-filters');
  await page.waitForTimeout(400);

  await page.click('summary:has-text("Confidence")');
  await page.waitForTimeout(200);
  const confs = await page.$$eval('#f-confidence .check .cname', els => els.map(e => e.textContent));
  check('confidence facet is ordered high → low, not alphabetically',
    confs[0] === 'high' && confs[confs.length - 1] === 'low', confs.join(','));

  await page.click('#f-confidence label:has-text("low")');
  await page.waitForTimeout(600);
  const confStatus = await page.textContent('#stage-status');
  const e5 = +(confStatus.match(/· ([\d,]+) connections/) || [0, '0'])[1].replace(/,/g, '');
  check('confidence filter narrows edges', e5 > 0 && e5 < e1, `${e1} → ${e5}`);
  await page.click('#reset-filters');
  await page.waitForTimeout(400);

  // ── comparison matrix ──
  await page.click('#view-compare');
  await page.waitForSelector('#compareview:not([hidden])');
  const cmpHead = await page.$$eval('#compare-head th', e => e.map(x => x.textContent.trim()));
  check('compare view renders a country column per country',
    cmpHead[0] === 'Instrument' && cmpHead.length >= 3, cmpHead.join(','));

  const cmpRows = await page.$$eval('#compare-body tr', r => r.length);
  check('compare view renders supra-national instruments as rows', cmpRows >= 5, `${cmpRows} rows`);

  const cmpCount = await page.textContent('#compare-count');
  check('compare view reports implemented vs applies-only',
    /\d+ implemented · \d+ applying/.test(cmpCount), cmpCount.trim());

  // The three cell states must all be present and textually distinguishable —
  // the tint alone is not the signal.
  const cellKinds = await page.$$eval('#compare-body td', tds => ({
    implemented: tds.filter(t => t.classList.contains('is-implemented')).length,
    applies: tds.filter(t => t.classList.contains('is-applies')).length,
    none: tds.filter(t => !t.className).length
  }));
  check('compare cells carry all three states',
    cellKinds.implemented > 0 && cellKinds.applies > 0 && cellKinds.none > 0,
    JSON.stringify(cellKinds));
  const appliesText = await page.textContent('#compare-body td.is-applies');
  check('applies-only cells say so in words, not only by colour',
    /none modelled/i.test(appliesText), appliesText.trim());

  // GDPR and NIS2 are the two instruments implemented in all six countries.
  const firstRow = await page.textContent('#compare-body tr:first-child th');
  check('compare rows are ranked by how much each instrument records',
    /General Data Protection|NIS2/i.test(firstRow), firstRow.replace(/\s+/g, ' ').trim());

  // A national implementer with no country of its own (the EU implementing a
  // UN convention) belongs to no column and must not be dropped.
  const rowNotes = await page.$$eval('#compare-body .row-note', e => e.map(x => x.textContent.trim()));
  check('supra-national implementers are reported, not dropped',
    rowNotes.length > 0 && /above the national level/i.test(rowNotes[0]), rowNotes.join(' | '));

  // Rows are instruments with country: null — the country filter must move
  // the columns, not empty the table.
  await page.click('#f-country label:has-text("Germany")');
  await page.waitForTimeout(500);
  const narrowedHead = await page.$$eval('#compare-head th', e => e.map(x => x.textContent.trim()));
  const narrowedRows = await page.$$eval('#compare-body tr', r => r.length);
  check('country filter narrows compare columns, not rows',
    narrowedHead.length === 2 && narrowedRows === cmpRows,
    `${narrowedHead.join(',')} · ${narrowedRows} rows`);
  await page.click('#reset-filters');
  await page.waitForTimeout(400);

  // Domain, by contrast, describes the instruments and must narrow the rows.
  await page.click('#f-domain label:has-text("Cybersecurity")');
  await page.waitForTimeout(500);
  const domRowsCmp = await page.$$eval('#compare-body tr', r => r.length);
  check('domain filter narrows compare rows', domRowsCmp > 0 && domRowsCmp < cmpRows,
    `${cmpRows} → ${domRowsCmp}`);
  await page.click('#reset-filters');
  await page.waitForTimeout(400);

  await page.click('#compare-body .namebtn');
  await page.waitForSelector('#detail:not([hidden])');
  check('clicking a compare cell opens the entity', true);

  // ── list view ──
  await page.fill('#search', '');
  await page.waitForTimeout(250);
  await page.click('#view-list');
  await page.waitForSelector('#listview:not([hidden])');
  const rowCount = await page.$$eval('#list-body tr', r => r.length);
  check('list view renders all entities', rowCount > 100, `${rowCount} rows`);

  const listLinks = await page.$$eval('#list-body a', a => a.map(x => x.href));
  check('list rows link to GitHub Markdown',
        listLinks.length > 100 && listLinks.every(h => /github\.com\/.+\/blob\/.+\.md$/.test(h)),
        listLinks[0]);

  // list respects search
  await page.fill('#search', 'gdpr');
  await page.waitForTimeout(500);
  const filteredRows = await page.$$eval('#list-body tr', r => r.length);
  check('list view respects search', filteredRows > 0 && filteredRows < rowCount, `${rowCount} → ${filteredRows}`);
  await page.fill('#search', '');
  await page.waitForTimeout(300);

  // sorting
  await page.click('.sortbtn[data-sort="rel_degree"]');
  await page.waitForTimeout(300);
  const degs = await page.$$eval('#list-body tr td:nth-child(7)', t => t.slice(0, 5).map(x => +x.textContent));
  check('list sorting works', degs.every((v, i, a) => i === 0 || a[i - 1] >= v), degs.join(','));

  // list → explorer
  await page.click('#list-body .namebtn');
  await page.waitForSelector('#detail:not([hidden])');
  check('clicking a list row opens the entity', true);

  check('no console errors after full interaction', errors.length === 0, errors.slice(0, 4).join(' | '));
  await ctx.close();
}

// ─────────────────────────── mobile ───────────────────────────
{
  const { ctx, page, errors } = await newPage({ width: 390, height: 844 });
  await page.goto(BASE + '/index.html', { waitUntil: 'networkidle' });
  await page.waitForFunction(() => document.getElementById('loading').hidden, null, { timeout: 15000 });

  const noHScroll = await page.evaluate(() =>
    document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1);
  check('mobile: no horizontal page scroll', noHScroll);

  const toggleVisible = await page.isVisible('#filters-toggle');
  check('mobile: filters toggle is shown', toggleVisible);

  const sidebarHidden = await page.evaluate(() => {
    const r = document.getElementById('sidebar').getBoundingClientRect();
    return r.right <= 1;
  });
  check('mobile: sidebar starts off-canvas', sidebarHidden);

  await page.click('#filters-toggle');
  await page.waitForTimeout(350);
  const sidebarOpen = await page.evaluate(() => {
    const r = document.getElementById('sidebar').getBoundingClientRect();
    return r.right > 50;
  });
  check('mobile: filters drawer opens', sidebarOpen);

  await page.click('#filters-toggle');
  await page.waitForTimeout(300);

  // A 7-column matrix is the widest thing the site renders. It must scroll
  // inside its own wrapper, never widen the page.
  await page.click('#view-compare');
  await page.waitForSelector('#compareview:not([hidden])');
  await page.waitForTimeout(300);
  const mCompare = await page.evaluate(() => ({
    page: document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1,
    wrapScrolls: (() => {
      const w = document.querySelector('#compareview .table-wrap');
      return w.scrollWidth > w.clientWidth;
    })()
  }));
  check('mobile: compare matrix scrolls in its wrapper, not the page',
    mCompare.page && mCompare.wrapScrolls, JSON.stringify(mCompare));
  await page.click('#view-atlas');
  await page.waitForTimeout(300);

  await page.fill('#search', 'NORA');
  await page.waitForSelector('#suggestions li[data-id]');
  await page.click('#suggestions li[data-id]');
  await page.waitForSelector('#detail:not([hidden])');
  const mDetail = await page.evaluate(() => {
    const r = document.getElementById('detail').getBoundingClientRect();
    return { w: Math.round(r.width), inView: r.left >= -1 && r.right <= window.innerWidth + 1 };
  });
  check('mobile: detail panel fits the viewport', mDetail.inView, JSON.stringify(mDetail));

  check('mobile: no console errors', errors.length === 0, errors.slice(0, 3).join(' | '));
  await ctx.close();
}

// ─────────────────────────── a11y basics ───────────────────────────
{
  const { ctx, page, errors } = await newPage({ width: 1280, height: 800 });
  await page.goto(BASE + '/index.html', { waitUntil: 'networkidle' });
  await page.waitForFunction(() => document.getElementById('loading').hidden, null, { timeout: 15000 });

  const a11y = await page.evaluate(() => {
    const out = {};
    out.lang = document.documentElement.lang;
    out.title = document.title;
    out.h1 = document.querySelectorAll('h1').length;
    out.skip = !!document.querySelector('.skip-link');
    out.searchLabelled = !!document.querySelector('label[for="search"]');
    out.imgsWithoutAlt = document.querySelectorAll('img:not([alt])').length;
    out.btnsWithoutName = [...document.querySelectorAll('button')]
      .filter(b => !b.textContent.trim() && !b.getAttribute('aria-label')).length;
    out.liveRegions = document.querySelectorAll('[aria-live]').length;
    return out;
  });
  check('a11y: lang set', a11y.lang === 'en');
  check('a11y: single h1', a11y.h1 === 1);
  check('a11y: skip link present', a11y.skip);
  check('a11y: search input has a label', a11y.searchLabelled);
  check('a11y: every button has an accessible name', a11y.btnsWithoutName === 0, String(a11y.btnsWithoutName));
  check('a11y: live regions for status', a11y.liveRegions >= 1);

  // keyboard: Tab reaches the view buttons and "/" focuses search
  await page.keyboard.press('/');
  const focused = await page.evaluate(() => document.activeElement.id);
  check('a11y: "/" focuses search', focused === 'search');

  await ctx.close();
}

await browser.close();
console.log(results.join('\n'));
console.log(`\n${results.length - failed}/${results.length} UI checks passed`);
process.exit(failed ? 1 : 0);
