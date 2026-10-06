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
| 4 | Statistics came first in the sidebar; the filters people want (country, type, domain) and the legend needed scrolling. | **Done 2026-10-06** (see below) |
| 5 | Mobile: the graph is tiny; the detail sheet covers over half the screen, including the list the visitor chose from; view buttons are 30 px high and checkboxes 13 px. | **Done 2026-10-06** (see below) |
| 6 | Compare listed countries alphabetically, so the first columns (Albania, Andorra, Argentina, Armenia) were empty and the countries with data were off to the right. | **Done 2026-10-06** |
| 7 | The detail panel showed internal research notes ("NOT READ — search-only.") in full for every relationship, "Confidence: Low" with no explanation that it describes the Atlas's certainty and not the law, and dates as "2026 08 21". | **Done 2026-10-06** (see below) |
| 8 | Entity names are official titles in the national language, with no short English display name. Related to `discovery/unresolved.md` row #9 (multilingual names). | **Partly done 2026-10-06** (see below) |
| 9 | Small things: the Re-layout button's aria-label ("Recalculate layout") does not contain its visible text (axe, serious); a custom wheel sensitivity that Cytoscape warns about (measured later: it made zoom sluggish, not abrupt); no "copy link" or "download data" control. | **Done 2026-10-06** (see below) |

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

## Point 4: the sidebar order (2026-10-06)
The sidebar now reads Explorer controls (in that view), Filters, Legend,
Connections shown, Layout, Statistics. Country, Entity type and Domain are open,
with short scrolling lists, so all three are on the first screen (measured:
their headings sit at 42, 223 and 404 px of an 815 px sidebar, where Country
used to be below 600 px and Domain below 900 px); Geographic level, Status and
Region are collapsed. Domain is open because it now carries the sector that
`level: sectoral` used to. Section headings show how many options are ticked
("Country (2 of 58)"), and the top-bar Filters button shows how many groups are
active ("Filters (2)"). Statistics moved to the bottom; the counts are in the
"Start here" card.

## Point 7: the detail panel (2026-10-06)
- **"About this record"** replaces "Metadata". The labels are plain (Sourcing,
  Atlas confidence, Research depth, Last checked), `primary-source` reads "Read
  from primary sources", each has a tooltip, and one visible line says these
  describe how well the Atlas knows the entity, not the entity itself.
- **Dates are ISO** ("2026-08-21"); they were passed through a title-casing
  helper that produced "2026 08 21".
- **Evidence is collapsed** under an "Evidence" link. A hub such as the GDPR has
  52 relationships whose evidence runs to a paragraph each (median 464
  characters, longest 2,202); the panel was about 4,500 px of text.
- **"source not read"** is a small tag beside a relationship whose evidence
  carries the repository's `NOT READ — search-only.` flag (403 of the 1,565; 28
  of the GDPR's 52). The same caveat appears above the evidence when a link is
  tapped on the canvas. The evidence text itself is unchanged.

## Point 5: phones (2026-10-06)
Measured at 390 × 844 with touch emulation, before and after:

| | Before | After |
|---|---|---|
| Top bar | 204 px (24% of the screen), five rows | 145 px: title, Start here, Filters and a ♥ Sponsor button; the four views on one row; search |
| Graph visible with an entity open | 38% of the canvas; the rest sat under the sheet | all of it: 382 px, fitted to what is left |
| Detail panel | a sheet over the canvas, 62% high | a strip under the graph, 40% high, with "Show more" (70%) and "Show less" |
| View buttons and top-bar buttons | 30 px high | 40 px |
| Rows to tick in the filters | 24 px, 13 px checkbox | 40 px, 19 px checkbox |
| Names in the list, relationship links, "Evidence" links | 17 to 19 px | 31 to 32 px |

The panel is stacked in the column instead of floated, so the canvas really
shrinks and the existing resize-and-fit code fits the graph to the space that is
left. The ♥ button keeps its name ("Sponsor") for screen readers and as a tooltip.
The 40 px sizes apply to touch screens (`pointer: coarse`); a narrow desktop
window keeps the compact sizes. Not measured: a real phone, landscape, or
screens narrower than 360 px.

## Point 9: small things (2026-10-06)
- **Re-layout** had `aria-label="Recalculate layout"`, which does not contain
  its visible text (axe, serious: label in name). It is now "Re-layout the
  graph".
- **Zoom.** The custom `wheelSensitivity: 0.25` triggered Cytoscape's own console
  warning that it "will make your app zoom unnaturally when using mainstream
  mice". Measured in headless Chromium, one wheel tick of 100 zoomed by about
  1.1% with the custom value and about 4.5% with Cytoscape's default, so the
  zoom was sluggish rather than abrupt; the setting is removed and the warning
  is gone. How it feels on a real mouse or trackpad was not tested.
- **Copy link and data.** The footer has "Copy link to this view" (the address
  already carries view, focus, depth and filters; the button says "Link copied"
  and announces it) and download links for `graph.json` and `details.json`. If
  the clipboard is not available the address is shown in a prompt instead.
  Not done: a CSV export of the List view.
- **Found while re-running axe** (both existed before): the detail panel's
  section headings jumped from h2 to h4 (now h3), and the List and Compare views
  had no `main` landmark because the only one, the graph, is hidden there (they
  are now `main` elements). axe reports nothing on the Atlas, List, Explorer
  and bare views after the change.

## Point 8: English names (2026-10-06)
About 245 of the 740 entities are named in their own language (a word-list
count, so approximate): "Autoriteit Persoonsgegevens", "Bundesamt für
Sicherheit in der Informationstechnik", "Ley Orgánica 3/2018, de 5 de diciembre,
…". Many files already listed an English name among `alternative_names`, but
nothing marked it as one, so the site could not use it.

- **New optional field `name_en`**, a short English display name
  (`metadata/metadata-schema.md`). It is the Atlas's own label and not
  necessarily an official translation, and the site says so. The validator
  rejects an empty value, stray whitespace, or a value that repeats `name`.
- **Backfilled for 169 entities in the first pass, each from an English name
  the file already listed.** Nothing was translated. A script checked that every value is
  literally one of that entity's alternative names; where the only English
  form was a nickname or ambiguous (for example two Brussels ordonnances shared
  one alias) the entity was left without one.
- **The site shows it by default**: in the graph, list, Compare, search and
  detail panel. A "Names" control in the sidebar switches to official titles
  only (`names=official` in the address). The detail panel gives both names and
  the caveat. Both names stay searchable whichever is shown.
- **Second pass (2026-10-06): 23 more names**, each from the body's own English
  page or an official translation and cited in that file's `sources` (BfDI's
  English page for the German intelligence laws and bodies; the Dutch
  government, NCSC-NL, NCTV and data.overheid.nl pages; the Austrian RIS and
  Fedlex translations; the EDPB members page; and others). The validator now
  also requires `name_en` to be listed in `alternative_names`.
- **Still without an English name: about 38 records**, where no English page
  or official translation could be read (see `discovery/unresolved.md` row #233
  for what was tried). A translation by a session would be a guess presented as
  a name, so they are left. This also stays separate from row #9 (a
  multilingual `name`), which is open.
- A side effect: a graph can now mix English and original names (a node
  without `name_en` keeps its official title), which is why the control exists.

Not tested: how the mixed labels read to a visitor.

## Suggested order for the rest
Nothing from this review is left except the follow-ups above (the remaining
English names, a CSV export of the List view).
