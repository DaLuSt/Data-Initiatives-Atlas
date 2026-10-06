# Usability review of the Atlas site

An expert review of `site/`, carried out on 2026-10-06 in headless Chromium at
1440 × 900 and 390 × 844, with axe-core, keyboard tabbing and a gzip size
count. It is not user research: no real visitors were observed, only Chromium
was tried, no screen reader was used, and slow networks were estimated from
file sizes. Five short sessions with unfamiliar visitors would confirm or
reorder the list below.

## What already works
- **Fast.** About 0.7 MB transferred (graph 99 KB, details 453 KB, app 27 KB,
  Cytoscape 137 KB, gzipped); ready in about 1.2 s locally.
- **Search** suggests entities with type and country.
- **State is in the URL**, so views are shareable.
- **Keyboard and focus:** skip link, visible 3 px focus outline, combobox ARIA.
- **axe-core:** one finding in the whole page.
- The **List** and **Compare** views are usable as they are.

## Findings

| # | Finding | Status |
|---|---|---|
| 1 | The first screen is a hairball of 1,565 lines: no labels, no introduction, no link to the guide. | **Done 2026-10-06** (see below) |
| 2 | Sidebar wording used the repository's internals ("Typed relationships (frontmatter, provenanced)", "Associations", "Wikilinks (Obsidian navigation)"). | **Done 2026-10-06** |
| 3 | Explorer: the hint said "No entity selected" on a deep link; the graph was fitted before the detail panel narrowed the canvas, so its right side was cut off; the default of 2 hops gave 282 unlabelled entities for a hub like the GDPR. | **Done 2026-10-06** |
| 4 | Statistics come first in the sidebar; the filters people want (country, type, domain) and the legend need scrolling. | Open |
| 5 | Mobile: the graph is tiny; the detail sheet covers over half the screen, including the list the visitor chose from; view buttons are 30 px high and checkboxes 13 px. | Open |
| 6 | Compare listed countries alphabetically, so the first columns (Albania, Andorra, Argentina, Armenia) were empty and the countries with data were off to the right. | **Done 2026-10-06** |
| 7 | The detail panel shows internal research notes ("NOT READ — search-only."), "Confidence: Low" with no explanation that it describes the Atlas's certainty and not the law, and dates as "2026 08 21". | Open |
| 8 | Entity names are official titles in the national language, with no short English display name. Related to `discovery/unresolved.md` row #9 (multilingual names). | Open |
| 9 | Small things: the Re-layout button's aria-label ("Recalculate layout") does not contain its visible text (axe, serious); zoom feels abrupt (Cytoscape's custom wheel sensitivity warning); no "copy link" or "download data" control. | Open |

## What the 2026-10-06 change did
- **Explorer (3):** the hint follows the selection; the detail panel is made
  visible before the layout runs, and closing it refits the graph; the depth is
  chosen automatically (the widest of 1 to 3 hops that shows at most 60
  entities) until the visitor picks one, and only a chosen depth is written to
  the URL, so plain `#ENTITY-ID` links stay plain. The GDPR now opens at 1 hop
  (53 entities); the Dutch UAVG stays at 2 hops (54).
- **Wording (2):** the three connection classes are now "Relationships",
  "Shared context" and "Mentions", with one-line explanations; the layout
  options are "Grouped by level and country", "Connected entities together" and
  "World map". `docs/graph.md` keeps the technical names in brackets.
- **Compare (6):** columns are ordered by how much the Atlas records for each
  country, and the 17 countries with nothing recorded are hidden behind a
  checkbox ("Also show 17 countries with nothing recorded", `empty=1` in the
  URL). A country filter overrides the hiding.

## Point 1: the "Start here" card (2026-10-06)
A bare address now opens with a card over the graph that says what the picture
is (with live counts) and offers five ways in, each an ordinary link to a hash
the app already understands: a chain from Convention 108+ to the Dutch data
protection authority, the neighbourhood of the NIS2 Directive, the Compare
matrix, the European Data Protection Board, and Germany as a table. A "Start
here" button in the top bar reopens it; Esc or the close button dismisses it;
any deep link, search pick or view change hides it. The page stores nothing
between visits, so it shows on every bare visit by design. The examples name
their view explicitly because only an explicit hash resets the filters, and a
test checks that every entity they name exists and every chain they promise is
a real path of typed relationships.

## Suggested order for the rest
4 (filters and legend above the statistics), then 7 (plain-language detail
panel), then 5 (mobile) and 8 (short English display names).
