/* Measure how long the site takes to show its first graph on a slow connection.
 *
 * Not a CI check (timings depend on the machine); the size budget in
 * tools/test_build_graph.py (TestLoadBudget) is the guard that runs in CI. This is how the
 * numbers in docs/performance.md were taken, so they can be taken again.
 *
 *     python tools/build_graph.py
 *     npm install playwright-core
 *     CHROME_PATH=/path/to/chrome node tools/measure_load.mjs
 *
 * It serves site/ itself with gzip (GitHub Pages compresses text files, a bare
 * `python -m http.server` does not), then loads the page in a fresh browser context under
 * Chrome DevTools' network and CPU throttling, three times per profile, and prints the
 * median time until the loading notice is gone and a canvas is drawn ("first graph") and
 * until details.json has arrived. Throttling is emulated by Chrome, so a profile is a
 * model of a slow phone, not a phone.
 *
 * SITE=/path/to/a/copy measures another folder (a scaled-up test copy, for example);
 * PROFILE=<regex> keeps only the profiles whose name matches (PROFILE='Slow 4G|Fast 3G').
 */

import { chromium } from 'playwright-core';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import { fileURLToPath } from 'node:url';

const SITE = path.resolve(process.env.SITE || path.join(path.dirname(fileURLToPath(import.meta.url)), '..', 'site'));
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json' };

const server = http.createServer((req, res) => {
  const file = path.join(SITE, req.url.split('?')[0] === '/' ? 'index.html' : req.url.split('?')[0]);
  if (!file.startsWith(SITE) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) { res.writeHead(404); return res.end(); }
  const ext = path.extname(file);
  let body = fs.readFileSync(file);
  const headers = { 'Content-Type': TYPES[ext] || 'application/octet-stream', 'Cache-Control': 'no-cache' };
  if (TYPES[ext] && /gzip/.test(req.headers['accept-encoding'] || '')) { body = zlib.gzipSync(body, { level: 6 }); headers['Content-Encoding'] = 'gzip'; }
  headers['Content-Length'] = body.length;
  res.writeHead(200, headers); res.end(body);
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const base = `http://127.0.0.1:${server.address().port}`;

const profiles = [
  { name: 'No throttling', down: -1, up: -1, rtt: 0, cpu: 1 },
  { name: 'Slow 4G, 4x CPU (1.6 Mbps, 150 ms)', down: 1.6e6 / 8, up: 0.75e6 / 8, rtt: 150, cpu: 4 },
  { name: 'Fast 3G, 4x CPU (1.6 Mbps, 562 ms)', down: 1.6e6 / 8, up: 0.75e6 / 8, rtt: 562, cpu: 4 },
  { name: 'Slow 3G, 6x CPU (0.4 Mbps, 2 s)', down: 0.5e6 / 8, up: 0.4e6 / 8, rtt: 2000, cpu: 6 },
];
const only = process.env.PROFILE ? new RegExp(process.env.PROFILE) : null;
const median = a => [...a].sort((x, y) => x - y)[Math.floor(a.length / 2)];

const browser = await chromium.launch({ executablePath: process.env.CHROME_PATH, args: ['--no-sandbox'] });
console.log('| Profile | First graph (s) | details.json arrived (s) |\n|---|---|---|');
for (const p of profiles) {
  if (only && !only.test(p.name)) continue;
  const first = [], details = [];
  for (let i = 0; i < 3; i++) {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const page = await ctx.newPage();
    const cdp = await ctx.newCDPSession(page);
    await cdp.send('Network.enable');
    await cdp.send('Network.emulateNetworkConditions', { offline: false, latency: p.rtt, downloadThroughput: p.down, uploadThroughput: p.up });
    await cdp.send('Emulation.setCPUThrottlingRate', { rate: p.cpu });
    const t0 = Date.now();
    await page.goto(base + '/index.html', { waitUntil: 'commit' });
    await page.waitForFunction(() => { const l = document.getElementById('loading'); return l && l.hidden && document.querySelectorAll('canvas').length > 0; }, null, { timeout: 180000 });
    first.push(Date.now() - t0);
    await page.waitForFunction(() => { const e = performance.getEntriesByName(location.origin + '/details.json'); return e.length > 0 && e[0].responseEnd > 0; }, null, { timeout: 180000 });
    details.push(Date.now() - t0);
    await ctx.close();
  }
  console.log(`| ${p.name} | ${(median(first) / 1000).toFixed(1)} | ${(median(details) / 1000).toFixed(1)} |`);
}
await browser.close();
server.close();
