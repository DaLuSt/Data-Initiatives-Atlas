# Accessibility

This is what the Data Initiatives Atlas does about accessibility, what has
and has not been checked, what is known to be hard, and how to tell us about a
barrier. It describes the interactive site at
<https://dalust.github.io/Data-Initiatives-Atlas/> and, more briefly, the
Markdown files in this repository. Last reviewed **2026-10-08**.

## Our commitment

We want the Atlas to be usable by everyone who has a reason to read it,
including people who use a keyboard, a screen reader, a magnifier, a phone, or
a high-contrast or dark setting. We use **WCAG 2.2 level AA** as the target.

**We do not claim conformance.** The site has had automated checks and a
developer's review, but not a full audit against WCAG and no testing with
disabled users (see "What has been checked"). Until that has happened, treat
this page as a description of effort, not a guarantee. The audit is on the
public roadmap: [issue #497](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/497),
aimed at the 2027.01 release.

The Atlas is an unfunded open-data project, so we cannot promise response
times of the kind a funded service would. What we can promise is that a report
of a barrier is read, answered, and, where it is a defect in our code, put on
the roadmap.

## Supported environments

The site is a static page with no account, no cookies and no tracking. It
needs JavaScript, because the graph is drawn in the browser, and it loads its
only third-party code (Cytoscape.js) from the same address.

| | What we know |
|---|---|
| **Browsers tested** | Chromium (recent, headless) at desktop width (1366 px), phone width (390 px and 320 px), and a width equal to 200 % zoom on a laptop (683 px). Other browsers (Firefox, Safari) have **not** been tested. |
| **Screen readers** | **None tested.** |
| **Keyboard** | Tested by scripted key presses in Chromium. |
| **Colour schemes** | Light and dark follow the operating-system setting. High-contrast modes have **not** been tested. |
| **Motion** | The loading spinner and the sidebar slide-in slow down or stop when the system asks for reduced motion. The graph layouts are not animated; the only movement is a 150 ms re-centre when you select an entity or move to one with the arrow keys. |

## What is in place

- **Not only a graph.** The **List** view (every entity, sortable, with a CSV
  download) and the **Compare** view (instruments against countries, as a real
  table) give the same information without the drawing, and the detail panel for
  an entity is ordinary text.
- **Keyboard.** A "Skip to content" link, the `/` key for search, <kbd>Esc</kbd>
  to close a panel, and, on the graph, the arrow keys to move between entities
  (in alphabetical order, the same as the List) and <kbd>Enter</kbd> to open the
  one in focus.
- **Structure.** One page heading, labelled controls, regions for the filters
  and the content, and status messages announced through live regions (result
  counts, the graph status line, the CSV download, copying a link).
- **Focus.** A visible 3 px focus outline on every control.
- **Touch.** Controls on phones are at least 40 px high.
- **Reflow.** No horizontal scrolling at 320 px or at 200 % zoom on a laptop
  (checked in Chromium on 2026-10-08).
- **Colour.** Light and dark themes; level and type are also named in text in
  the list, the detail panel and the legend, not shown by colour alone in those
  places.

## What has been checked

- **Automated:** axe-core found no violations on 16 combinations of view and
  screen size (bare address, List, Compare, the Explorer, a path between two
  entities, official names, and two layouts, at desktop and phone width) on
  2026-10-08. Automated tools find only a part of the real problems, so this is
  a floor, not a pass.
- **Scripted:** odd addresses, random sequences of clicks and key presses, and
  the CSV download, in Chromium, for errors and broken states.
- **Reviewed by the developer** on 2026-10-06 (`docs/ux-analysis.md`): first
  screen, wording, mobile layout, detail panel.
- **Not done:** a manual WCAG 2.2 audit; testing with NVDA, JAWS, VoiceOver or
  TalkBack; testing in Firefox or Safari; sessions with disabled users.

## Known limitations

1. **The graph drawing is not accessible as a picture.** The canvas is marked as
   an application with instructions, and arrow keys and <kbd>Enter</kbd> move
   through and open entities, but the layout and the lines between entities
   are not conveyed to a screen reader. Use the List and Compare views and an
   entity's "Relationships" section for the same facts.
2. **Reaching the graph by Tab is long without the skip link.** The filters in
   the sidebar come first (about 150 controls). Use "Skip to content", which
   moves focus to the main area of the view you are in.
3. **Colour on the graph carries meaning** (level, type, selection) and its
   contrast has **not been measured**.
4. **Names in many languages.** The page language is English, but entity
   names, and some quotations in the detail panel, are in the languages of the
   sources (Dutch, German, French, Spanish and others) and are not marked with a
   `lang` attribute, so a screen reader may pronounce them with English rules.
   English display names are shown by default where the Atlas has one; the
   official name is always available (the "Names" control).
5. **Dense overview.** The first view draws all entities at once, with labels
   hidden until you zoom in or filter. It is designed to be explored, not read
   in one pass. How to make the first view friendlier is an open design question.
6. **Text sources.** Quotations and titles come from official documents and
   websites and are shown as they are written there; their own accessibility is
   outside our control.
7. **The Markdown files** in this repository are read on GitHub or in a text
   editor, with whatever accessibility those provide. Some entity files contain
   wide tables.

## Reporting a barrier

If something on the site or in this repository stops you from reading,
navigating or using it, please tell us.

- **[Report an accessibility barrier](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/new?template=accessibility-barrier.yml)**
  (a GitHub issue form). It asks what you were trying to do, what happened, the
  address of the page, and the browser and assistive technology you use. You do
  not need to know the cause.
- **If GitHub itself is the barrier,** say so through the owner's profile at
  <https://github.com/DaLuSt> and we will find another way.
- **A wrong or misleading fact** in an entity is a different kind of report:
  use the [data correction form](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/new?template=data-correction.yml).
- **A security problem** goes through `SECURITY.md`, not a public issue.

We aim to reply to a barrier report within **14 days**, say whether we accept
it as a defect, and put accepted defects on the [roadmap](docs/roadmap.md) with
the label `accessibility`. We will say plainly when we cannot fix something.

## How this page is kept honest

Each statement above is something that was checked or read in the code on the
date given. When the audit (issue #497) is done, this page will be rewritten from
its findings: what passes, what fails, and the date. Changes to the site that
affect accessibility should update this file in the same pull request.
