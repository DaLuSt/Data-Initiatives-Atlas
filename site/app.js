/* Data Initiatives Atlas — interactive knowledge graph.
 *
 * Reads the generated site/graph.json (+ site/details.json, fetched in the
 * background). Nothing here is hand-maintained data: every node, edge, facet
 * and statistic comes from the repository via tools/build_graph.py.
 */
(function () {
  "use strict";

  // ── state ────────────────────────────────────────────────────────────
  var G = null;            // graph.json
  var D = null;            // details.json (may still be loading)
  var cy = null;
  var nodeById = Object.create(null);
  var view = "atlas";      // atlas | explorer | compare | list
  var focusId = null;
  var depth = 2;
  var filters = {          // Set per facet; empty Set = "all"
    level: new Set(), country: new Set(), region: new Set(),
    type: new Set(), status: new Set(), domain: new Set(),
    relType: new Set(), provenance: new Set(), confidence: new Set(),
    edgeClass: new Set(["relationship"])
  };
  var listSort = { key: "label", dir: 1 };
  var sugIndex = -1, sugItems = [];

  // Above this many visible nodes, drop labels.
  var LOD_LABELS = 260;

  var LEVEL_ORDER = ["international", "regional", "national", "sectoral", "local"];
  // Confidence is ordinal, not alphabetical — "high, medium, low" reads as a
  // scale, "high, low, medium" reads as a list of three unrelated words.
  var CONFIDENCE_ORDER = ["high", "medium", "low"];
  var LEVEL_COLOR = {
    international: "--lvl-international", regional: "--lvl-regional",
    national: "--lvl-national", sectoral: "--lvl-sectoral", local: "--lvl-local"
  };
  // Shape carries type, colour carries level — so neither is the only cue.
  var TYPE_SHAPE = {
    organisation: "round-rectangle", country: "star", region: "star",
    law: "diamond", regulation: "diamond", directive: "diamond",
    policy: "vee", strategy: "triangle", standard: "hexagon",
    framework: "pentagon", programme: "octagon", initiative: "ellipse",
    "data-space": "barrel", platform: "rhomboid", technology: "rhomboid",
    domain: "concave-hexagon", publication: "tag"
  };

  var $ = function (id) { return document.getElementById(id); };
  var css = function (name) {
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  };
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function titly(s) {
    return String(s || "").replace(/[-_]/g, " ").replace(/\b\w/g, function (m) {
      return m.toUpperCase();
    });
  }

  // ── boot ─────────────────────────────────────────────────────────────
  function boot() {
    fetch("graph.json", { cache: "no-cache" })
      .then(function (r) {
        if (!r.ok) throw new Error("graph.json — HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        G = data;
        G.nodes.forEach(function (n) { nodeById[n.id] = n; });
        buildChrome();
        initGraph();
        $("loading").hidden = true;
        applyRoute();
        // Detail prose is not on the critical path.
        fetch("details.json", { cache: "no-cache" })
          .then(function (r) { return r.ok ? r.json() : null; })
          .then(function (d) {
            D = d;
            // Fold detail fields onto the node records so search and the
            // list view can use them too.
            if (D && D.nodes) {
              Object.keys(D.nodes).forEach(function (id) {
                if (nodeById[id]) Object.assign(nodeById[id], D.nodes[id]);
              });
            }
            if (focusId && !$("detail").hidden) showDetail(focusId);
          })
          .catch(function () { /* detail panel degrades gracefully */ });
      })
      .catch(function (err) {
        $("loading").hidden = true;
        $("load-error").hidden = false;
        $("load-error-msg").textContent =
          err.message + ". If you are opening this file directly from disk, " +
          "serve the folder over HTTP instead (see docs/graph-development.md).";
      });
  }

  // ── chrome: stats, filters, legend ───────────────────────────────────
  function buildChrome() {
    var s = G.stats;
    var rows = [
      ["Entities", s.entities], ["Relationships", s.relationships],
      ["Associations", s.associations], ["Countries", s.countries],
      ["Regions", s.regions], ["Organisations", s.organisations],
      ["Legislation", s.legislation], ["Standards", s.standards],
      ["Frameworks", s.frameworks], ["Data spaces", s.data_spaces],
      ["Initiatives", s.initiatives], ["Domains", s.domains]
    ];
    $("stats").innerHTML = rows.filter(function (r) { return r[1] != null; })
      .map(function (r) {
        return "<dt>" + esc(r[0]) + "</dt><dd>" + Number(r[1]).toLocaleString() + "</dd>";
      }).join("");

    var when = new Date(G.generated_at);
    $("generated").textContent = "Atlas generated: " + (isNaN(when) ? G.generated_at :
      when.toLocaleDateString(undefined, { day: "numeric", month: "long", year: "numeric" }) +
      " at " + when.toLocaleTimeString(undefined, { hour: "2-digit", minute: "2-digit", timeZone: "UTC" }) + " UTC");

    var repo = G.repository || {};
    if (repo.owner && repo.name) {
      var a = $("repo-link");
      a.href = "https://github.com/" + repo.owner + "/" + repo.name;
      a.textContent = repo.owner + "/" + repo.name;
      a.rel = "noopener";
    }

    // Edge classes — what "connections" means, spelled out.
    var CLASS_LABEL = {
      relationship: "Typed relationships (frontmatter, provenanced)",
      association: "Associations (domains, organisations, related entities, versions)",
      wikilink: "Wikilinks in the entity text (Obsidian navigation)"
    };
    $("edge-classes").innerHTML = (G.vocabularies.edge_classes || []).map(function (c) {
      var n = c === "relationship" ? G.stats.relationships
        : c === "association" ? G.stats.associations : G.stats.wikilinks;
      return check("edgeClass", c, CLASS_LABEL[c] || titly(c), n, filters.edgeClass.has(c));
    }).join("");

    facetInto("rel-types", "relType", G.facets.relationship_types, "reltype-count", { raw: true });
    facetInto("f-provenance", "provenance", G.facets.provenances, "prov-count", { raw: true });
    facetInto("f-confidence", "confidence", G.facets.confidences, "conf-count",
      { raw: true, order: CONFIDENCE_ORDER });
    facetInto("f-level", "level", G.facets.levels, "level-count", { levelOrder: true });
    facetInto("f-country", "country",
      (G.facets.countries || []).map(function (c) {
        return { code: c.code, count: c.count, label: c.label };
      }), "country-count");
    facetInto("f-region", "region", G.facets.regions, "region-count");
    facetInto("f-domain", "domain",
      (G.facets.domains || []).map(function (d) {
        return { code: d.code, count: d.count, label: d.label };
      }), "domain-count");
    facetInto("f-type", "type", G.facets.types, "type-count");
    facetInto("f-status", "status", G.facets.statuses, "status-count");

    $("legend").innerHTML =
      (G.facets.levels || []).map(function (l) {
        return '<li><span class="swatch" style="background:' + css(LEVEL_COLOR[l.code] || "--text-dim") +
          '"></span>' + esc(titly(l.code)) + " — colour</li>";
      }).join("") +
      '<li style="margin-top:.4rem"><span class="shape">◆</span>Legislation</li>' +
      '<li><span class="shape">▭</span>Organisation</li>' +
      '<li><span class="shape">⬡</span>Standard</li>' +
      '<li><span class="shape">★</span>Country / region anchor</li>' +
      '<li style="margin-top:.4rem"><span class="shape">→</span>Arrow shows relationship direction</li>';

    wireChrome();
  }

  function check(group, code, label, count, checked) {
    var id = "chk-" + group + "-" + String(code).replace(/[^a-z0-9]/gi, "_");
    var swatch = group === "level"
      ? '<span class="swatch" style="background:' + css(LEVEL_COLOR[code] || "--text-dim") + '"></span>' : "";
    return '<label class="check" for="' + id + '">' +
      '<input type="checkbox" id="' + id + '" data-group="' + group + '" value="' + esc(code) + '"' +
      (checked ? " checked" : "") + ">" + swatch +
      '<span class="cname">' + esc(label) + "</span>" +
      (count != null ? '<span class="cnum">' + count + "</span>" : "") + "</label>";
  }

  function facetInto(elId, group, facet, countElId, opts) {
    opts = opts || {};
    var items = (facet || []).slice();
    var order = opts.levelOrder ? LEVEL_ORDER : opts.order;
    if (order) {
      items.sort(function (a, b) {
        return order.indexOf(a.code) - order.indexOf(b.code);
      });
    }
    $(elId).innerHTML = items.map(function (f) {
      // Relationship types are a controlled vocabulary — show them verbatim
      // rather than prettified, so the UI names what the repository names.
      var label = f.label || (opts.raw ? f.code : titly(f.code));
      return check(group, f.code, label, f.count, false);
    }).join("") || '<p class="hint">None in this Atlas.</p>';
    if (countElId) $(countElId).textContent = "(" + items.length + ")";
  }

  function wireChrome() {
    document.addEventListener("change", function (ev) {
      var el = ev.target;
      if (el.tagName !== "INPUT" || !el.dataset.group) return;
      var set = filters[el.dataset.group];
      if (el.checked) set.add(el.value); else set.delete(el.value);
      refresh();
    });

    document.addEventListener("click", function (ev) {
      var b = ev.target.closest("button");
      if (!b) return;
      if (b.dataset.all || b.dataset.none) {
        var on = !!b.dataset.all;
        $(b.dataset.all || b.dataset.none).querySelectorAll("input").forEach(function (i) {
          i.checked = on;
          var set = filters[i.dataset.group];
          if (on) set.add(i.value); else set.delete(i.value);
        });
        refresh();
      }
    });

    $("reset-filters").addEventListener("click", resetFilters);
    $("empty-reset").addEventListener("click", resetFilters);

    $("view-atlas").addEventListener("click", function () { setView("atlas"); });
    $("view-explorer").addEventListener("click", function () { setView("explorer"); });
    $("view-compare").addEventListener("click", function () { setView("compare"); });
    $("view-list").addEventListener("click", function () { setView("list"); });

    $("depth").addEventListener("change", function (e) {
      depth = parseInt(e.target.value, 10) || 2;
      if (view === "explorer") refresh();
    });

    $("zoom-in").addEventListener("click", function () { cy.zoom({ level: cy.zoom() * 1.35, renderedPosition: centre() }); });
    $("zoom-out").addEventListener("click", function () { cy.zoom({ level: cy.zoom() / 1.35, renderedPosition: centre() }); });
    $("fit").addEventListener("click", function () { cy.fit(undefined, 40); });
    $("relayout").addEventListener("click", function () { runLayout(true); });

    $("detail-close").addEventListener("click", closeDetail);
    $("filters-toggle").addEventListener("click", function () {
      var open = $("sidebar").classList.toggle("is-open");
      this.setAttribute("aria-expanded", String(open));
    });

    wireSearch();

    document.querySelectorAll(".sortbtn").forEach(function (b) {
      b.addEventListener("click", function () {
        var k = b.dataset.sort;
        listSort.dir = listSort.key === k ? -listSort.dir : 1;
        listSort.key = k;
        renderList();
      });
    });

    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") {
        if ($("suggestions").hidden === false) { hideSuggestions(); return; }
        if (!$("detail").hidden) closeDetail();
      }
      if (ev.key === "/" && document.activeElement !== $("search")) {
        ev.preventDefault(); $("search").focus();
      }
    });

    window.addEventListener("hashchange", applyRoute);
  }

  function centre() {
    var c = $("cy").getBoundingClientRect();
    return { x: c.width / 2, y: c.height / 2 };
  }

  function resetFilters() {
    Object.keys(filters).forEach(function (k) {
      if (k !== "edgeClass") filters[k].clear();
    });
    document.querySelectorAll('input[data-group]').forEach(function (i) {
      i.checked = i.dataset.group === "edgeClass" ? filters.edgeClass.has(i.value) : false;
    });
    refresh();
  }

  // ── graph ────────────────────────────────────────────────────────────
  function initGraph() {
    cy = cytoscape({
      container: $("cy"),
      elements: [],
      wheelSensitivity: 0.25,
      maxZoom: 3,
      minZoom: 0.04,
      textureOnViewport: true,
      hideEdgesOnViewport: true,
      motionBlur: false,
      pixelRatio: 1,
      style: [
        {
          selector: "node",
          style: {
            "background-color": function (n) { return css(LEVEL_COLOR[n.data("level")] || "--text-dim"); },
            "shape": function (n) { return TYPE_SHAPE[n.data("type")] || "ellipse"; },
            "width": function (n) { return 16 + Math.min(26, (n.data("rel_degree") || 0) * 2.2); },
            "height": function (n) { return 16 + Math.min(26, (n.data("rel_degree") || 0) * 2.2); },
            "label": "data(label)",
            "font-size": 9,
            "color": function () { return css("--text"); },
            "text-outline-color": function () { return css("--bg"); },
            "text-outline-width": 2.2,
            "text-valign": "bottom",
            "text-margin-y": 3,
            "text-wrap": "ellipsis",
            "text-max-width": 110,
            // Labels fade out when they would render too small to read, and
            // come back as the user zooms in. This is what keeps a dense
            // default view legible instead of a wall of overlapping text.
            "min-zoomed-font-size": 8,
            "border-width": 0
          }
        },
        { selector: "node.hide-label", style: { "label": "" } },
        {
          selector: "node:selected",
          style: {
            "border-width": 3,
            "border-color": function () { return css("--focus"); },
            "label": "data(label)", "font-size": 11, "z-index": 99
          }
        },
        { selector: "node.focus", style: { "border-width": 4, "border-color": function () { return css("--accent"); }, "z-index": 98 } },
        { selector: "node.dim", style: { "opacity": 0.12, "label": "" } },
        {
          selector: "edge",
          style: {
            "width": 1.1,
            "line-color": function () { return css("--border-strong"); },
            "target-arrow-color": function () { return css("--border-strong"); },
            "target-arrow-shape": "triangle",
            "arrow-scale": 0.75,
            "curve-style": "straight",
            "opacity": 0.55
          }
        },
        {
          selector: 'edge[cls = "relationship"]',
          style: { "width": 1.6, "opacity": 0.8, "line-color": function () { return css("--accent"); }, "target-arrow-color": function () { return css("--accent"); } }
        },
        { selector: 'edge[cls = "association"]', style: { "line-style": "dashed", "target-arrow-shape": "none" } },
        { selector: 'edge[cls = "wikilink"]', style: { "line-style": "dotted", "target-arrow-shape": "none", "opacity": 0.3 } },
        { selector: 'edge[provenance = "interpretation"]', style: { "line-style": "dashed", "line-color": function () { return css("--focus"); }, "target-arrow-color": function () { return css("--focus"); } } },
        { selector: "edge.dim", style: { "opacity": 0.04 } },
        {
          selector: "edge.hl",
          style: {
            "width": 2.6, "opacity": 1, "z-index": 90,
            "line-color": function () { return css("--focus"); },
            "target-arrow-color": function () { return css("--focus"); },
            "label": "data(type)", "font-size": 8,
            "color": function () { return css("--text-dim"); },
            "text-outline-color": function () { return css("--bg"); },
            "text-outline-width": 2, "text-rotation": "autorotate"
          }
        }
      ]
    });

    // Labels are governed by min-zoomed-font-size, so tell the user why the
    // map is unlabelled rather than leaving them to guess.
    var zoomHintTimer = null;
    cy.on("zoom", function () {
      clearTimeout(zoomHintTimer);
      zoomHintTimer = setTimeout(updateStatus, 120);
    });

    cy.on("tap", "node", function (ev) { selectEntity(ev.target.id(), true); });
    cy.on("tap", function (ev) { if (ev.target === cy) closeDetail(); });
    // Keyboard: the canvas itself is not traversable, so the List view and
    // search are the accessible routes. Enter opens the selected node.
    $("cy").addEventListener("keydown", function (ev) {
      if (ev.key === "Enter" && focusId) showDetail(focusId);
    });
  }

  // `ignoreCountry` exists for the comparison matrix, where country selects
  // the columns. Rows there are supra-national instruments with `country:
  // null`, so applying the country filter to them would empty the table.
  function passesNodeFilters(n, ignoreCountry) {
    if (filters.level.size && !filters.level.has(n.level)) return false;
    if (filters.type.size && !filters.type.has(n.type)) return false;
    if (filters.status.size && !filters.status.has(n.status)) return false;
    if (!ignoreCountry &&
        filters.country.size && !(n.country && filters.country.has(n.country))) return false;
    if (filters.region.size && !(n.region && filters.region.has(n.region))) return false;
    // A domain matches an entity tagged with it — and the domain entity
    // itself, which carries no `domains` of its own but is the hub every
    // tagged entity points at. Excluding it would filter the graph down to
    // a set of nodes with their shared centre missing.
    if (filters.domain.size && !filters.domain.has(n.id) &&
        !(n.domains || []).some(function (d) { return filters.domain.has(d); })) return false;
    return true;
  }

  function passesEdgeFilters(e) {
    if (!filters.edgeClass.has(e.class)) return false;
    if (e.class !== "relationship") return true;
    // Provenance and confidence exist only on relationship edges, so they
    // narrow that class alone — an association is neither a fact nor an
    // interpretation and is not silently dropped by these filters.
    if (filters.relType.size && !filters.relType.has(e.type)) return false;
    if (filters.provenance.size && !filters.provenance.has(e.provenance)) return false;
    if (filters.confidence.size && !filters.confidence.has(e.confidence)) return false;
    return true;
  }

  /** Nodes+edges for the current view, filters and focus. */
  function currentElements() {
    var hops = null;
    var okNodes = Object.create(null);
    G.nodes.forEach(function (n) { if (passesNodeFilters(n)) okNodes[n.id] = n; });

    var edges = G.edges.filter(function (e) {
      return passesEdgeFilters(e) && okNodes[e.source] && okNodes[e.target];
    });

    var keep = okNodes;
    if (view === "explorer" && focusId && okNodes[focusId]) {
      // Neighbourhood traversal over the filtered edge set (brief §11/§12).
      var adj = Object.create(null);
      edges.forEach(function (e) {
        (adj[e.source] || (adj[e.source] = [])).push(e.target);
        (adj[e.target] || (adj[e.target] = [])).push(e.source);
      });
      var seen = Object.create(null); seen[focusId] = 0;
      var frontier = [focusId];
      for (var d = 0; d < depth; d++) {
        var next = [];
        frontier.forEach(function (id) {
          (adj[id] || []).forEach(function (nb) {
            if (!(nb in seen)) { seen[nb] = d + 1; next.push(nb); }
          });
        });
        frontier = next;
        if (!frontier.length) break;
      }
      keep = Object.create(null);
      Object.keys(seen).forEach(function (id) { keep[id] = okNodes[id]; });
      edges = edges.filter(function (e) { return keep[e.source] && keep[e.target]; });
      hops = seen;
    }

    var els = [];
    Object.keys(keep).forEach(function (id) {
      var n = keep[id];
      els.push({
        group: "nodes",
        data: {
          id: n.id, label: n.label, type: n.type, level: n.level,
          country: n.country || "", region: n.region || "", scope: n.scope,
          status: n.status, rel_degree: n.rel_degree || 0,
          hop: hops ? (hops[id] || 0) : null
        }
      });
    });
    edges.forEach(function (e, i) {
      els.push({
        group: "edges",
        data: {
          id: "e" + i, source: e.source, target: e.target,
          type: e.type || e.field || "", cls: e.class,
          provenance: e.provenance || ""
        }
      });
    });
    return els;
  }

  /** Deterministic layered layout: rows by geographic level (brief §6/§11). */
  function layeredPositions(nodes) {
    var gapX = 165, gapY = 105;       // spacing between nodes inside a block
    var blockGapX = 110, blockGapY = 70, bandGap = 150;
    var width = Math.max($("cy").clientWidth, 900);

    // Connectivity is measured over the *visible* edges, not the whole Atlas.
    // The ordering should describe the graph actually on screen, so turning
    // wikilinks on re-orders the blocks rather than leaving a stale ranking.
    var deg = Object.create(null);
    if (cy) {
      cy.edges().forEach(function (e) {
        var s = e.data("source"), t = e.data("target");
        deg[s] = (deg[s] || 0) + 1;
        deg[t] = (deg[t] || 0) + 1;
      });
    }

    var rows = Object.create(null);
    nodes.forEach(function (n) {
      var lv = n.data("level") || "unknown";
      (rows[lv] || (rows[lv] = [])).push(n);
    });
    var order = LEVEL_ORDER.filter(function (l) { return rows[l]; })
      .concat(Object.keys(rows).filter(function (l) { return LEVEL_ORDER.indexOf(l) < 0; }));

    var pos = Object.create(null), y = 0;

    order.forEach(function (lv) {
      // ── split the band into blocks, one per scope ──────────────────────
      // For national entities `scope` is the country code, so this is what
      // makes the seven countries read as seven clumps instead of one
      // continuous ribbon wrapped at an arbitrary row width.
      var groups = Object.create(null);
      rows[lv].forEach(function (n) {
        var k = n.data("scope") || "—";
        (groups[k] || (groups[k] = [])).push(n);
      });

      // Largest block first: it packs tighter, and keeps the biggest scope
      // in a band from being split across a wrap.
      var blocks = Object.keys(groups).sort(function (a, b) {
        return groups[b].length - groups[a].length || a.localeCompare(b);
      }).map(function (k) {
        var list = groups[k];
        // Most-connected first, so each block leads with its own hub and
        // its periphery trails behind it.
        list.sort(function (a, b) {
          return (deg[b.id()] || 0) - (deg[a.id()] || 0) ||
            (b.data("rel_degree") || 0) - (a.data("rel_degree") || 0) ||
            (a.data("label") || "").localeCompare(b.data("label") || "");
        });
        var cols = Math.max(2, Math.min(8, Math.ceil(Math.sqrt(list.length * 1.4))));
        return { list: list, cols: cols, rows: Math.ceil(list.length / cols) };
      });

      // ── pack blocks across the band, wrapping when it runs out of room ─
      // The budget scales with the band's own size rather than the viewport:
      // the canvas pans and zooms, so a band holding 171 national entities
      // should be allowed to be wide, and "Fit" brings it into view. Using
      // the viewport width instead stacks every block on its own line.
      var budget = Math.max(width, Math.ceil(Math.sqrt(rows[lv].length)) * gapX * 1.8);
      var lines = [], lineBlocks = [], lineW = 0;
      blocks.forEach(function (b) {
        var bw = b.cols * gapX;
        if (lineBlocks.length && lineW + blockGapX + bw > budget) {
          lines.push({ blocks: lineBlocks, w: lineW });
          lineBlocks = []; lineW = 0;
        }
        lineW += (lineBlocks.length ? blockGapX : 0) + bw;
        lineBlocks.push(b);
      });
      if (lineBlocks.length) lines.push({ blocks: lineBlocks, w: lineW });

      lines.forEach(function (line) {
        var x = -line.w / 2, tallest = 0;
        line.blocks.forEach(function (b) {
          b.list.forEach(function (n, i) {
            pos[n.id()] = {
              x: x + (i % b.cols) * gapX,
              y: y + Math.floor(i / b.cols) * gapY
            };
          });
          x += b.cols * gapX + blockGapX;
          tallest = Math.max(tallest, b.rows);
        });
        y += tallest * gapY + blockGapY;
      });
      y += bandGap;
    });
    return pos;
  }

  function runLayout(force) {
    var n = cy.nodes().length;
    if (!n) return;

    if (view === "explorer" && focusId && cy.getElementById(focusId).length) {
      // Rings by hop distance: focus in the centre, direct links next, and so
      // on — the shape the brief's Entity Explorer sketch describes, and it
      // uses the canvas far better than a fanned-out tree.
      cy.layout({
        name: "concentric",
        concentric: function (node) { return 10 - (node.data("hop") || 0); },
        levelWidth: function () { return 1; },
        minNodeSpacing: 46, padding: 50, fit: true,
        animate: n < 400, animationDuration: 300
      }).run();
      return;
    }

    // Note: there is no size threshold here. `layeredPositions` is O(n log n)
    // arithmetic with no simulation to converge, so it costs the same at 258
    // nodes as at 2,580 — a branch on node count would only ever have chosen
    // between two identical calls. LOD_LABELS still thins labels; see
    // applyLOD().
    var positions = layeredPositions(cy.nodes());
    cy.layout({ name: "preset", positions: positions, fit: true, padding: 50, animate: false }).run();
  }

  function cssEscape(s) { return String(s).replace(/[^a-zA-Z0-9_-]/g, "\\$&"); }

  function applyLOD() {
    var n = cy.nodes().length;
    cy.batch(function () {
      if (n > LOD_LABELS) cy.nodes().addClass("hide-label");
      else cy.nodes().removeClass("hide-label");
    });
  }

  function refresh() {
    if (!cy) return;
    if (view === "list") { renderList(); return; }
    if (view === "compare") { renderCompare(); return; }

    var els = currentElements();
    cy.elements().remove();
    cy.add(els);
    applyLOD();
    runLayout(false);

    updateStatus();
    if (focusId && cy.getElementById(focusId).length) highlight(focusId);
  }

  function updateStatus() {
    if (!cy) return;
    var nn = cy.nodes().length, ne = cy.edges().length;
    $("empty-note").hidden = nn > 0;
    var msg = nn.toLocaleString() + " of " + G.stats.entities.toLocaleString() +
      " entities · " + ne.toLocaleString() + " connections";
    if (view === "explorer" && focusId) {
      var f = nodeById[focusId];
      msg = (f ? f.label : focusId) + " · " + depth + "-hop neighbourhood · " + msg;
    }
    if (nn > LOD_LABELS) {
      msg += " · labels off (filter or use Explorer)";
    } else if (nn && cy.zoom() * 9 < 8) {
      msg += " · zoom in for labels";
    }
    $("stage-status").textContent = msg;
  }

  function highlight(id) {
    var node = cy.getElementById(id);
    cy.batch(function () {
      cy.elements().removeClass("dim hl focus");
      if (!node.length) return;
      node.addClass("focus");
      node.connectedEdges().addClass("hl");
      // In the Global Atlas, dimming is what makes one entity findable in a
      // dense field. In the Explorer the view IS already the neighbourhood,
      // so dimming it would grey out the very thing the user asked to see.
      if (view !== "explorer") {
        cy.elements().difference(node.closedNeighborhood()).addClass("dim");
      }
    });
  }

  // ── selection + detail panel ─────────────────────────────────────────
  function selectEntity(id, fromGraph) {
    if (!nodeById[id]) return;
    focusId = id;
    if (location.hash.slice(1) !== id) {
      history.replaceState(null, "", "#" + id);
    }
    if (view === "explorer") refresh();
    else if (cy && cy.getElementById(id).length) {
      highlight(id);
      if (!fromGraph) {
        cy.animate({ center: { eles: cy.getElementById(id) }, zoom: Math.max(cy.zoom(), 0.9) },
          { duration: 250 });
      }
    }
    showDetail(id);
  }

  function closeDetail() {
    $("detail").hidden = true;
    if (cy) cy.elements().removeClass("dim hl focus");
  }

  function showDetail(id) {
    var n = nodeById[id];
    if (!n) return;
    var d = (D && D.nodes && D.nodes[id]) || {};
    var repo = G.repository || {};
    var url = repo.owner && repo.name && n.path
      ? "https://github.com/" + repo.owner + "/" + repo.name + "/blob/" +
        (repo.branch || "main") + "/" + n.path
      : null;

    var h = [];
    h.push('<h2 class="d-title" id="detail-title">' + esc(n.label) + "</h2>");
    h.push('<div class="d-id">' + esc(n.id) + "</div>");

    var chips = [];
    if (n.level) chips.push('<span class="chip lvl" style="background:' +
      css(LEVEL_COLOR[n.level] || "--text-dim") + '">' + esc(titly(n.level)) + "</span>");
    if (n.type) chips.push('<span class="chip strong">' + esc(titly(n.type)) + "</span>");
    if (n.status) chips.push('<span class="chip">' + esc(titly(n.status)) + "</span>");
    if (n.country) chips.push('<span class="chip">' + esc(countryLabel(n.country)) + "</span>");
    if (n.region) chips.push('<span class="chip">' + esc(n.region) + "</span>");
    h.push('<div class="chips">' + chips.join("") + "</div>");

    if (d.description) h.push('<p class="d-desc">' + esc(d.description) + "</p>");
    else if (!D) h.push('<p class="d-desc hint">Loading description…</p>');

    if (d.aliases && d.aliases.length) {
      h.push(sec("Also known as", "<ul><li>" + d.aliases.map(esc).join("</li><li>") + "</li></ul>"));
    }

    // Only metadata that actually exists (brief §7/§10).
    var meta = [];
    [["Verification", d.verification], ["Confidence", d.confidence],
     ["Coverage", d.coverage], ["Last verified", d.last_verified],
     ["Start date", d.start_date], ["End date", d.end_date]].forEach(function (kv) {
      if (kv[1]) meta.push("<dt>" + kv[0] + "</dt><dd>" + esc(titly(String(kv[1]))) + "</dd>");
    });
    if (meta.length) h.push(sec("Metadata", '<dl class="kv">' + meta.join("") + "</dl>"));

    if (d.domains && d.domains.length) {
      h.push(sec("Domains", "<ul>" + d.domains.map(function (x) {
        return "<li>" + link(x) + "</li>";
      }).join("") + "</ul>"));
    }
    if (d.organisations && d.organisations.length) {
      h.push(sec("Organisations", "<ul>" + d.organisations.map(function (x) {
        return "<li>" + link(x) + "</li>";
      }).join("") + "</ul>"));
    }
    if (d.previous_version || d.successor) {
      var t = [];
      if (d.previous_version) t.push("<li>Previous version: " + link(d.previous_version) + "</li>");
      if (d.successor) t.push("<li>Successor: " + link(d.successor) + "</li>");
      h.push(sec("Version lineage", "<ul>" + t.join("") + "</ul>"));
    }

    var rels = relationsOf(id);
    if (rels.out.length) h.push(sec("Relationships from this entity", relList(rels.out, "→")));
    if (rels.in.length) h.push(sec("Relationships to this entity", relList(rels.in, "←")));
    if (!rels.out.length && !rels.in.length) {
      h.push(sec("Relationships",
        '<p class="hint">No typed relationship in either direction. Enable ' +
        '“Associations” or “Wikilinks” in the sidebar to see softer links.</p>'));
    }

    if (d.sources && d.sources.length) {
      h.push(sec("Sources", "<ul>" + d.sources.map(function (s) {
        var label = esc(s.title || s.url || "Source");
        var body = s.url ? '<a href="' + esc(s.url) + '" rel="noopener nofollow">' + label + "</a>" : label;
        return "<li>" + body + (s.publisher ? ' <span class="rel-dir">— ' + esc(s.publisher) + "</span>" : "") + "</li>";
      }).join("") + "</ul>"));
    }

    if (d.verification && d.verification !== "primary-source") {
      h.push('<p class="caveat">Sourcing caveat: this entity is marked <strong>' +
        esc(d.verification) + "</strong> in the repository — the cited pages were not read. " +
        "See the Markdown source for the full caveat.</p>");
    }

    if (url) h.push('<a class="ghlink" href="' + esc(url) + '" rel="noopener">Open entity on GitHub →</a>');

    $("detail-body").innerHTML = h.join("");
    $("detail").hidden = false;

    $("detail-body").querySelectorAll("[data-goto]").forEach(function (b) {
      b.addEventListener("click", function () { selectEntity(b.dataset.goto, false); });
    });
  }

  function sec(title, inner) {
    return '<div class="d-sec"><h4>' + esc(title) + "</h4>" + inner + "</div>";
  }
  function link(id) {
    var n = nodeById[id];
    return '<button class="rel-target" data-goto="' + esc(id) + '">' +
      esc(n ? n.label : id) + "</button>";
  }
  function countryLabel(code) {
    var f = (G.facets.countries || []).find(function (c) { return c.code === code; });
    return f ? f.label : code;
  }

  function relationsOf(id) {
    var out = [], inn = [];
    G.edges.forEach(function (e) {
      if (e.class !== "relationship") return;
      if (e.source === id) out.push(e);
      else if (e.target === id) inn.push(e);
    });
    return { out: out, in: inn };
  }

  function relList(list, dir) {
    return "<ul>" + list.map(function (e) {
      var other = dir === "→" ? e.target : e.source;
      var key = e.source + "|" + e.target + "|" + (e.type || "");
      var ed = D && D.edges && D.edges[key];
      return "<li>" +
        '<div class="rel-line"><span class="rel-dir">' + dir + "</span>" +
        '<span class="rel-type">' + esc(e.type) + "</span>" + link(other) +
        (e.provenance === "interpretation"
          ? ' <span class="rel-interp" title="Atlas interpretation, not a sourced fact">interpretation</span>' : "") +
        "</div>" +
        (ed && ed.evidence ? '<p class="evidence">' + esc(ed.evidence) + "</p>" : "") +
        "</li>";
    }).join("") + "</ul>";
  }

  // ── search ───────────────────────────────────────────────────────────
  function wireSearch() {
    var box = $("search");
    var t = null;
    box.addEventListener("input", function () {
      clearTimeout(t);
      t = setTimeout(function () { runSearch(box.value); }, 110);
      if (view === "list") renderList();
    });
    box.addEventListener("keydown", function (ev) {
      if ($("suggestions").hidden) return;
      if (ev.key === "ArrowDown") { ev.preventDefault(); moveSug(1); }
      else if (ev.key === "ArrowUp") { ev.preventDefault(); moveSug(-1); }
      else if (ev.key === "Enter") {
        if (sugIndex >= 0 && sugItems[sugIndex]) {
          ev.preventDefault();
          pick(sugItems[sugIndex].id);
        }
      }
    });
    document.addEventListener("click", function (ev) {
      if (!ev.target.closest(".search-wrap")) hideSuggestions();
    });
  }

  function scoreNode(n, q) {
    var hay = [n.label, n.id].concat(n.aliases || []);
    var best = 0;
    for (var i = 0; i < hay.length; i++) {
      var s = String(hay[i]).toLowerCase();
      if (s === q) return 100;
      if (s.indexOf(q) === 0) best = Math.max(best, 80);
      else if (s.indexOf(q) > -1) best = Math.max(best, 55);
    }
    if (!best) {
      var extra = [n.type, n.level, n.status, n.scope, n.country, n.region]
        .concat(n.domains || []).join(" ").toLowerCase();
      if (extra.indexOf(q) > -1) best = 25;
    }
    return best;
  }

  function matches(q) {
    q = String(q || "").trim().toLowerCase();
    if (!q) return [];
    return G.nodes.map(function (n) { return { n: n, s: scoreNode(n, q) }; })
      .filter(function (x) { return x.s > 0; })
      .sort(function (a, b) {
        return b.s - a.s || (b.n.rel_degree || 0) - (a.n.rel_degree || 0) ||
          a.n.label.localeCompare(b.n.label);
      })
      .map(function (x) { return x.n; });
  }

  function runSearch(q) {
    var res = matches(q);
    sugItems = res.slice(0, 12);
    sugIndex = -1;
    var ul = $("suggestions");
    if (!String(q || "").trim()) { hideSuggestions(); return; }
    if (!sugItems.length) {
      ul.innerHTML = '<li class="s-empty" role="option" aria-disabled="true">No entity matches “' + esc(q) + "”</li>";
    } else {
      ul.innerHTML = sugItems.map(function (n, i) {
        return '<li role="option" id="sug-' + i + '" data-id="' + esc(n.id) + '" aria-selected="false">' +
          '<span class="s-name">' + esc(n.label) + "</span>" +
          '<span class="s-meta">' + esc(n.id) + " · " + esc(titly(n.type)) +
          (n.country ? " · " + esc(countryLabel(n.country)) : n.region ? " · " + esc(n.region) : "") +
          "</span></li>";
      }).join("");
      ul.querySelectorAll("li[data-id]").forEach(function (li) {
        li.addEventListener("click", function () { pick(li.dataset.id); });
      });
    }
    ul.hidden = false;
    $("search").setAttribute("aria-expanded", "true");
  }

  function moveSug(delta) {
    var ul = $("suggestions");
    var items = ul.querySelectorAll("li[data-id]");
    if (!items.length) return;
    sugIndex = (sugIndex + delta + items.length) % items.length;
    items.forEach(function (li, i) { li.setAttribute("aria-selected", String(i === sugIndex)); });
    $("search").setAttribute("aria-activedescendant", "sug-" + sugIndex);
    items[sugIndex].scrollIntoView({ block: "nearest" });
  }

  function hideSuggestions() {
    $("suggestions").hidden = true;
    $("search").setAttribute("aria-expanded", "false");
    $("search").removeAttribute("aria-activedescendant");
    sugIndex = -1;
  }

  function pick(id) {
    hideSuggestions();
    if (view === "list" || view === "compare") setView("explorer");
    selectEntity(id, false);
  }

  // ── views ────────────────────────────────────────────────────────────
  function setView(v) {
    view = v;
    [["view-atlas", "atlas"], ["view-explorer", "explorer"],
     ["view-compare", "compare"], ["view-list", "list"]]
      .forEach(function (p) {
        var b = $(p[0]), on = p[1] === v;
        b.classList.toggle("is-active", on);
        b.setAttribute("aria-pressed", String(on));
      });
    $("stage").hidden = v === "list" || v === "compare";
    $("listview").hidden = v !== "list";
    $("compareview").hidden = v !== "compare";
    $("explorer-panel").hidden = v !== "explorer";
    if (v === "explorer" && !focusId) {
      $("explorer-hint").textContent =
        "No entity selected. Search above, or switch to Global Atlas and click a node.";
    }
    refresh();
    if (v !== "list" && v !== "compare" && cy) cy.resize();
  }

  function renderList() {
    var q = $("search").value;
    // Not `.filter(passesNodeFilters)` — Array#filter passes the index as the
    // second argument, which would land in `ignoreCountry`.
    var rows = (q.trim() ? matches(q) : G.nodes.slice())
      .filter(function (n) { return passesNodeFilters(n); });
    var k = listSort.key, dir = listSort.dir;
    rows.sort(function (a, b) {
      if (k === "rel_degree") {
        return (((b.rel_degree || 0) - (a.rel_degree || 0)) * dir) ||
          a.label.localeCompare(b.label);
      }
      return String(a[k] || "").localeCompare(String(b[k] || "")) * dir ||
        a.label.localeCompare(b.label);
    });
    $("list-count").textContent = rows.length.toLocaleString() + " of " +
      G.stats.entities.toLocaleString() + " entities" +
      (q.trim() ? ' matching “' + q.trim() + '”' : "") + ".";

    var repo = G.repository || {};
    $("list-body").innerHTML = rows.map(function (n) {
      var url = repo.owner && n.path
        ? "https://github.com/" + repo.owner + "/" + repo.name + "/blob/" +
          (repo.branch || "main") + "/" + n.path : null;
      return "<tr>" +
        '<td><button class="namebtn" data-goto="' + esc(n.id) + '">' + esc(n.label) + "</button></td>" +
        "<td><code>" + esc(n.id) + "</code></td>" +
        "<td>" + esc(titly(n.type)) + "</td>" +
        "<td>" + esc(titly(n.level)) + "</td>" +
        "<td>" + esc(n.country ? countryLabel(n.country) : (n.region || n.scope)) + "</td>" +
        "<td>" + esc(titly(n.status)) + "</td>" +
        "<td>" + (n.rel_degree || 0) + "</td>" +
        "<td>" + (url ? '<a href="' + esc(url) + '" rel="noopener">Markdown</a>' : "—") + "</td>" +
        "</tr>";
    }).join("");

    $("list-body").querySelectorAll("[data-goto]").forEach(function (b) {
      b.addEventListener("click", function () {
        setView("explorer");
        selectEntity(b.dataset.goto, false);
      });
    });
  }

  // ── comparison matrix ────────────────────────────────────────────────
  // Rows are supra-national instruments, columns are countries, and each cell
  // says what that country did about that instrument. Several entity bodies
  // maintain tables like this by hand, where they go stale; this derives them
  // from `applies-in` and `implements-requirement-from` edges instead.
  function compareModel() {
    // "Supra-national" is whatever the generator says is not a country scope,
    // so a new region or international scope needs no change here.
    var supra = Object.create(null);
    (G.facets.scopes || []).forEach(function (s) {
      if (!s.is_country) supra[s.code] = true;
    });

    var applies = Object.create(null);    // instrument → { country: true }
    var implts = Object.create(null);     // instrument → { country: [ids] }
    var supraImpl = Object.create(null);  // instrument → [ids], no country

    G.edges.forEach(function (e) {
      if (e.class !== "relationship") return;
      var src = nodeById[e.source];
      if (!src || !nodeById[e.target]) return;

      if (e.type === "applies-in" && supra[src.scope]) {
        applies[e.source] = applies[e.source] || Object.create(null);
        applies[e.source][e.target] = true;
      } else if (e.type === "implements-requirement-from") {
        if (src.country) {
          implts[e.target] = implts[e.target] || Object.create(null);
          (implts[e.target][src.country] = implts[e.target][src.country] || []).push(e.source);
        } else {
          // An implementer with no country of its own — the EU implementing a
          // UN convention. It belongs in no column, so it is reported on the
          // row rather than quietly dropped.
          (supraImpl[e.target] = supraImpl[e.target] || []).push(e.source);
        }
      }
    });

    var ids = Object.create(null);
    [applies, implts, supraImpl].forEach(function (map) {
      Object.keys(map).forEach(function (id) { ids[id] = true; });
    });

    return {
      applies: applies, implts: implts, supraImpl: supraImpl,
      rows: Object.keys(ids).map(function (id) { return nodeById[id]; })
        .filter(function (n) { return n && supra[n.scope]; })
    };
  }

  function renderCompare() {
    var m = compareModel();

    // Columns follow the country filter alone. The other filters describe
    // instruments, and applying them to the columns would empty the matrix
    // the moment someone filtered by type or level.
    var cols = G.nodes.filter(function (n) {
      return n.type === "country" && (!filters.country.size || filters.country.has(n.id));
    }).sort(function (a, b) { return a.label.localeCompare(b.label); });

    var rows = m.rows.filter(function (n) { return passesNodeFilters(n, true); });

    function cellState(rowId, countryId) {
      var im = (m.implts[rowId] || {})[countryId];
      if (im && im.length) return { kind: "implemented", ids: im };
      if ((m.applies[rowId] || {})[countryId]) return { kind: "applies" };
      return { kind: "none" };
    }

    // Rank by how much each instrument actually says: implementations first,
    // then recorded applicability.
    var tally = Object.create(null);
    rows.forEach(function (n) {
      var t = { implemented: 0, applies: 0 };
      cols.forEach(function (c) {
        var s = cellState(n.id, c.id);
        if (s.kind === "implemented") t.implemented++;
        else if (s.kind === "applies") t.applies++;
      });
      tally[n.id] = t;
    });
    rows.sort(function (a, b) {
      return (tally[b.id].implemented - tally[a.id].implemented) ||
        (tally[b.id].applies - tally[a.id].applies) ||
        a.label.localeCompare(b.label);
    });

    var totals = { implemented: 0, applies: 0 };
    rows.forEach(function (n) {
      totals.implemented += tally[n.id].implemented;
      totals.applies += tally[n.id].applies;
    });

    // The heading counts countries rather than stating a number, so adding a
    // country cannot leave it saying "six" forever.
    var NUMBER = ["no", "one", "two", "three", "four", "five", "six", "seven",
                  "eight", "nine", "ten"];
    $("compare-h").textContent = "One instrument, " +
      (NUMBER[cols.length] || cols.length) + " countr" +
      (cols.length === 1 ? "y" : "ies");

    $("compare-head").innerHTML = '<th scope="col">Instrument</th>' +
      cols.map(function (c) {
        return '<th scope="col">' + esc(c.label) + "</th>";
      }).join("");

    $("compare-body").innerHTML = rows.map(function (n) {
      var extra = m.supraImpl[n.id] || [];
      var head = '<th scope="row">' +
        '<button class="namebtn" data-goto="' + esc(n.id) + '">' + esc(n.label) + "</button>" +
        '<span class="row-id">' + esc(n.id) + "</span>" +
        (extra.length ? '<span class="row-note">Implemented above the national level by ' +
          extra.map(function (id) {
            return esc((nodeById[id] || {}).label || id);
          }).join(", ") + "</span>" : "") +
        "</th>";

      return "<tr>" + head + cols.map(function (c) {
        var s = cellState(n.id, c.id);
        if (s.kind === "implemented") {
          // The ID is the scannable key in a matrix — several of these
          // entities carry full official titles a dozen words long. The name
          // stays in the accessible name and the tooltip, not in the grid.
          return '<td class="is-implemented">' + s.ids.map(function (id) {
            var e = nodeById[id] || {};
            return '<button class="namebtn cell-entity" data-goto="' + esc(id) + '"' +
              (e.label ? ' title="' + esc(e.label) + '"' : "") + ">" +
              esc(id) + (e.label ? '<span class="sr-only"> — ' + esc(e.label) + "</span>" : "") +
              (e.status ? '<span class="cell-status">' + esc(titly(e.status)) + "</span>" : "") +
              "</button>";
          }).join("") + "</td>";
        }
        if (s.kind === "applies") {
          return '<td class="is-applies"><span class="cell-applies">' +
            "Applies — none modelled</span></td>";
        }
        return '<td><span class="cell-none">—</span></td>';
      }).join("") + "</tr>";
    }).join("");

    $("compare-count").textContent = rows.length
      ? rows.length.toLocaleString() + " instrument" + (rows.length === 1 ? "" : "s") +
        " × " + cols.length + " countr" + (cols.length === 1 ? "y" : "ies") + " · " +
        totals.implemented.toLocaleString() + " implemented · " +
        totals.applies.toLocaleString() + " applying with no national instrument modelled."
      : "No supra-national instrument matches the current filters.";

    // The gap is the point of the view, so it is stated rather than left to
    // be counted off the tinting.
    var fullyImplemented = rows.filter(function (n) {
      return cols.length && tally[n.id].implemented === cols.length;
    });
    $("compare-note").textContent = rows.length
      ? fullyImplemented.length +
        " of " + rows.length + " instruments are implemented in every country shown" +
        (fullyImplemented.length
          ? " (" + fullyImplemented.map(function (n) { return n.label; }).join(", ") + ")"
          : "") +
        ". An empty cell is not a claim that the instrument does not apply — it means " +
        "the Atlas records nothing either way."
      : "";

    $("compare-body").querySelectorAll("[data-goto]").forEach(function (b) {
      b.addEventListener("click", function () {
        setView("explorer");
        selectEntity(b.dataset.goto, false);
      });
    });
  }

  // ── deep links ───────────────────────────────────────────────────────
  function applyRoute() {
    var id = decodeURIComponent(location.hash.slice(1));
    if (id && nodeById[id]) {
      if (view === "atlas") setView("explorer");
      selectEntity(id, false);
    } else {
      refresh();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
