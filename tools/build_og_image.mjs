#!/usr/bin/env node
// Renders docs/assets/og-card.html to site/og-image.png (1200 x 630), the picture a shared
// link to the Atlas shows on LinkedIn and in chats (roadmap #772). Run it by hand when the
// card changes; the PNG is committed, so the Pages build does not need a browser for it.
//
//   CHROME_PATH=/path/to/chrome node tools/build_og_image.mjs
//
// It needs playwright-core (or playwright) installed where Node can find it, as tools/test_ui.mjs does.
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const require = createRequire(import.meta.url);
let chromium;
try { ({ chromium } = require('playwright-core')); } catch { ({ chromium } = require('playwright')); }
const browser = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
await page.goto('file://' + path.join(root, 'docs', 'assets', 'og-card.html'));
await page.screenshot({ path: path.join(root, 'site', 'og-image.png'), type: 'png' });
await browser.close();
console.log('wrote site/og-image.png (1200 x 630)');
