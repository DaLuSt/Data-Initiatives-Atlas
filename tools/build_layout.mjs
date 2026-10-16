/* Lay the whole Atlas out once, at build time, and store the result.
 *
 * The force layout is the one thing the page cannot do cheaply: about 12 s of
 * CPU at 900 entities, on the visitor's device, every visit. The result is the
 * same every time for the same graph, so it is computed here instead and the
 * page just draws it (roadmap #508, docs/performance.md).
 *
 *     python tools/build_graph.py        # first: this reads site/graph.json
 *     node tools/build_layout.mjs        # writes site/layout.json
 *     node tools/build_layout.mjs OUT GRAPH   # other paths (the tests use this)
 *
 * Same Cytoscape (site/vendor) and same tuning (site/force-options.js) as the
 * page. The graph is every entity and every typed relationship, which is what
 * the page shows with its default "Connections shown". The page uses the stored
 * positions only when `fingerprint` equals graph.json's `layout_fingerprint`,
 * and falls back to its own simulation otherwise, so a stale file is never
 * shown, only unused.
 *
 * Reproducible: Math.random is replaced by a seeded generator for the run, so
 * two builds of the same data give the same file (tools/test_build_graph.py
 * checks it).
 */

import { createRequire } from 'node:module';
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const here = dirname(fileURLToPath(import.meta.url));
const site = join(here, '..', 'site');
const out = process.argv[2] || join(site, 'layout.json');
const graphPath = process.argv[3] || join(site, 'graph.json');

const cytoscape = require(join(site, 'vendor', 'cytoscape.min.js'));
const force = require(join(site, 'force-options.js'));
const graph = JSON.parse(readFileSync(graphPath, 'utf8'));

function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const elements = [];
for (const n of graph.nodes) elements.push({ group: 'nodes', data: { id: n.id } });
graph.edges.forEach((e, i) => {
  if (e.class !== 'relationship') return;
  elements.push({
    group: 'edges',
    data: {
      id: 'e' + i, source: e.source, target: e.target, cls: e.class,
      provenance: e.provenance || '', confidence: e.confidence || ''
    }
  });
});

const cy = cytoscape({ headless: true, styleEnabled: false, elements });
const realRandom = Math.random;
Math.random = mulberry32(20261016);
const t0 = Date.now();
try {
  cy.layout({ ...force.options(true), fit: false, animate: false }).run();
} finally {
  Math.random = realRandom;
}

const positions = {};
cy.nodes().forEach(n => {
  const p = n.position();
  positions[n.id()] = [Math.round(p.x), Math.round(p.y)];
});
const doc = { fingerprint: graph.layout_fingerprint, nodes: cy.nodes().length, positions };
writeFileSync(out, JSON.stringify(doc) + '\n');
console.log(`build_layout: ${doc.nodes} entities laid out in ${((Date.now() - t0) / 1000).toFixed(1)} s -> ${out}`);
