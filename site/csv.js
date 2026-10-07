/* CSV for the List view's download. Pure functions, no DOM, so they can be
 * tested under Node (tools/test_build_graph.py runs them).
 *
 * Two things beyond quoting:
 *  - a cell that starts with = + - @ (or a tab or carriage return) is prefixed
 *    with an apostrophe, because a spreadsheet would otherwise run it as a
 *    formula; the data is names and URLs, so the apostrophe costs nothing;
 *  - the text starts with a byte-order mark, so Excel reads the accents in
 *    "Autoriteit Persoonsgegevens" and "Agência para a Modernização" as UTF-8.
 */
(function (root) {
  "use strict";

  var FORMULA_START = /^[=+\-@\t\r]/;

  function cell(value) {
    var s = value === null || value === undefined ? "" : String(value);
    if (FORMULA_START.test(s)) s = "'" + s;
    return /[",\r\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
  }

  /** header: array of column titles; rows: array of arrays. */
  function toCsv(header, rows) {
    var lines = [header.map(cell).join(",")];
    rows.forEach(function (r) { lines.push(r.map(cell).join(",")); });
    return "\uFEFF" + lines.join("\r\n") + "\r\n";
  }

  var api = { cell: cell, toCsv: toCsv };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.AtlasCsv = api;
})(typeof window !== "undefined" ? window : globalThis);
