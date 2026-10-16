/* The force layout's tuning, shared by the page (site/app.js, which runs the
 * simulation live when it has to) and the build step (tools/build_layout.mjs,
 * which runs it once for the whole graph and writes site/layout.json). One
 * file so the two cannot drift: build_graph.py hashes this file into the
 * layout's fingerprint, so changing a number here makes every stored layout
 * stale and the page falls back to the live simulation until it is rebuilt.
 *
 * Edges are Cytoscape edges whose data carries `cls` (relationship |
 * association | wikilink), `provenance` and `confidence`, as the page builds
 * them in currentElements().
 */
(function (root) {
  "use strict";

  /** Edge weight drives distance — "strongly connected nodes closer".
   *
   *  Rest lengths follow the Atlas's own hierarchy of evidence. Two things
   *  about how much of that actually survives the simulation, both measured
   *  rather than assumed:
   *
   *  - **It works where the spring is strong.** Typed relationships are the
   *    tightest class (mean 72px against 132px for associations with every
   *    edge class on), and low-confidence relationships sit visibly further
   *    apart than medium ones — 203px against 166px, over 27 edges and 317.
   *  - **A slack spring is not a long one.** Wikilinks are given almost no
   *    elasticity so 1,392 of them cannot reshape the graph; the cost is that
   *    they do not hold their rest length either. They float at whatever
   *    ambient spacing the other forces produce (~82px), *shorter* than
   *    associations. Springs pull; they do not push.
   *
   *  `confidence: high` has no visible effect and no claim is made for it:
   *  only 2 of 354 typed relationships carry it, so any mean over them is
   *  noise. See progress/backlog.md — the field is close to a constant.
   */
  function idealEdgeLength(edge) {
    var cls = edge.data("cls");
    if (cls === "wikilink") return 420;
    if (cls === "association") return 230;
    if (edge.data("provenance") === "interpretation") return 140;
    var c = edge.data("confidence");
    return c === "high" ? 40 : c === "low" ? 130 : 70;
  }

  function options(randomize) {
    return {
      name: "cose",
      // The page seeds the simulation from the grouped layout (randomize:
      // false); the build step has no grouped layout and passes true, with a
      // seeded random-number generator, so its result is reproducible.
      randomize: !!randomize,
      animate: false, fit: true, padding: 50,
      // The default view is 44 disconnected components. Without generous
      // spacing they are flung apart and the canvas becomes mostly whitespace.
      componentSpacing: 130,
      nodeOverlap: 14,
      nodeRepulsion: function (node) {
        // Damp the mega-hubs. DOMAIN-GOVERNMENT touches 206 of 258 entities;
        // at uniform repulsion it drags the entire graph into a ball around
        // itself. Letting repulsion grow with degree makes a hub hold its
        // neighbours at arm's length instead of swallowing them.
        return 9000 + Math.min(node.degree(), 60) * 2600;
      },
      idealEdgeLength: idealEdgeLength,
      edgeElasticity: function (edge) {
        // Only typed relationships get to pull hard; the other two classes
        // are navigational and should not reshape the graph.
        var cls = edge.data("cls");
        return cls === "relationship" ? 160 : cls === "association" ? 20 : 5;
      },
      gravity: 40, numIter: 900,
      initialTemp: 200, coolingFactor: 0.95, minTemp: 1
    };
  }

  var api = { idealEdgeLength: idealEdgeLength, options: options };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.AtlasForce = api;
})(typeof window !== "undefined" ? window : globalThis);
