# Load time on slow networks

Roadmap #507. The question: how long does a visitor on a slow connection or an
older phone wait for the first graph, and what happens as the Atlas grows?

## How the page loads

1. `index.html`, `app.css`, `app.js`, `csv.js` and `vendor/cytoscape.min.js`.
2. `graph.json` (nodes and edges). The first graph is drawn when it arrives.
3. `details.json` (the long evidence text). It is fetched **after** the first
   graph, so the detail panel fills in a moment later. `TestLoadBudget` checks
   that the boot code does not wait for it.

GitHub Pages sends text files gzipped, so sizes below are gzipped.

## Measured, 2026-10-13 (855 entities)

| File | Raw | Gzipped |
|---|---|---|
| everything on the first-graph path except `graph.json` | 0.6 MB (mostly Cytoscape) | 182 KB |
| `graph.json` | 1.2 MB | 112 KB |
| first-graph path in total | | 294 KB |
| `details.json` | 2.0 MB | 489 KB |

Time until the first graph is drawn, median of 3 runs, taken with
`tools/measure_load.mjs` (Chrome DevTools network and CPU throttling):

| Profile | First graph | `details.json` arrived |
|---|---|---|
| No throttling | 0.7 s | 0.9 s |
| Slow 4G, 4x CPU slowdown | 4.7 s | 7.4 s |
| Fast 3G, 4x CPU slowdown | 5.9 s | 9.1 s |
| Slow 3G, 6x CPU slowdown | 15.0 s | 25.1 s |

The "phone" here is emulated by slowing this machine's CPU, not a real phone.
Treat the numbers as a model: good for comparing one build with another, not
a promise about any device.

## What the time is made of

CPU, more than bytes. With the network unthrottled and only the 4x CPU slowdown
the first graph takes 3.0 s, against 0.7 s without any throttling. Most of that
is building the graph and running the layout. The bytes add the rest: about
1.7 s on Slow 4G.

## Projection

Scaled test copies of the site (the real data duplicated, so edges are
over-counted, which is the cautious direction):

| Entities | `graph.json` gz | `details.json` gz | First graph, Slow 4G + 4x CPU | 4x CPU only |
|---|---|---|---|---|
| 855 (now) | 112 KB | 489 KB | 4.6 s | 3.0 s |
| 1,710 (2x) | 219 KB | 976 KB | 7.5 s | 5.8 s |
| 4,275 (5x) | 540 KB | 2.4 MB | 12.7 s | 8.7 s |

A direct measurement on the 194-country test build of `docs/scale-check.md` (1,087 entities) gave 5.2 s,
in line with this table. Growth is roughly linear in entities. Going from 89 to about 195 country
anchors (#508) adds about 100 entities, roughly 12%; the entities written for
each country add more over time.

## The budget

| Measure | Budget | Now |
|---|---|---|
| First graph, Slow 4G + 4x CPU | 5 s | 4.7 s |
| `graph.json`, gzipped | 250 KB | 112 KB |
| `details.json`, gzipped | 1 MB | 489 KB |
| Page + scripts + `graph.json`, gzipped | 450 KB | 294 KB |

The three size lines are enforced by `TestLoadBudget` in
`tools/test_build_graph.py`; they fail at about twice today's size. The time
line is not a CI check (timings depend on the machine); re-measure with
`tools/measure_load.mjs` at about 950 entities and at each further 250.

**The time budget is met, with little room.** The size budget leaves room to
double, but reading the table above, the time budget is reached at about 1,000
entities, because time is dominated by CPU, not bytes. That is the first thing
to fix when it comes, not the file sizes.

## The hover card

The hover card (roadmap #640) finds the node under the pointer by scanning the visible nodes once per animation
frame while the pointer moves over the graph, because on a hub the lines drawn over a node take the pointer's
hit-test from Cytoscape. Measured: 1.1 ms per pointer move over 872 nodes (2.3 ms with the 4x CPU slowdown) and 3.0 ms
over the 1,087-node test copy. Nothing runs at boot and nothing runs when the pointer is still.

## What to do when the budget is missed

In order of expected effect:

1. Lay out less at boot: show the country and supranational level first and
   add detail when a visitor asks for it, or cut the force layout's iterations
   for the first draw.
2. Split `graph.json` by level so the first draw reads a smaller file.
3. Drop fields the first draw does not use from `graph.json` and move them to
   `details.json`.

Compression, the usual first fix, is already in place on GitHub Pages.

## Measuring again

```
python tools/build_graph.py
npm install playwright-core
CHROME_PATH=/path/to/chrome node tools/measure_load.mjs
```

`SITE=<folder>` measures another copy of the site; `PROFILE=<regex>` keeps only
the profiles whose name matches.
