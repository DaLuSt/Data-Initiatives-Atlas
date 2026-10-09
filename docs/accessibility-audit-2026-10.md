# Accessibility audit, October 2026

The scripted part of roadmap #497: the site checked against WCAG 2.2 level AA in a real browser.
**It is not a full audit and not a conformance claim.** What needs a person is listed at the end.
Done 2026-10-09 in Chromium (headless, 1.63 client), on the site as built from `main`.
`ACCESSIBILITY.md` is the public statement; this page is the evidence behind it.

## What was run

| Check | How | Result |
|---|---|---|
| Automated rules | axe-core, tags `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, `wcag22aa`, `best-practice`; 5 views (Global Atlas, List, Compare, Explorer, Explorer with a path) in 4 setups (desktop light, desktop dark, phone light, desktop with forced colours): 20 runs | **Before: 2 rule violations** (below). **After the fixes: 0 violations in 20 runs.** |
| Text contrast (1.4.3) | axe, plus the browser suite's new checks on the active view button and the level chips in both colour schemes | Failed before (below); fixed |
| Graph colours (1.4.11) | the five level colours as drawn on the graph, against the canvas, both themes | All at least 3:1 (lowest 4.57:1 light, 6.78:1 dark, after the olive was darkened) |
| Keyboard focus (2.4.7) | Tab through the whole page: 380 tab stops, each checked for an outline or shadow | All 380 show an indicator (its contrast is not measured) |
| Pointer target size (2.5.8) | every button, link, field and disclosure at desktop and phone width; axe's rule | Two small controls failed (below), fixed; native checkboxes are 13 px but sit inside a larger clickable label, which the criterion allows |
| Reflow (1.4.10) | 320 x 640 and 320 x 256 (400 % zoom on a 1280 px screen), 4 views | No horizontal scrolling |
| Text spacing (1.4.12) | line height 1.5, letter spacing 0.12 em, word spacing 0.16 em, paragraph spacing 2 em, 4 views | Nothing clipped (only the intentionally hidden screen-reader text) |
| Structure | headings, landmarks, page language | One `h1`; one visible `main` per view; `lang="en"`; headings in order |
| Reduced motion (2.3.3 is AAA) | `prefers-reduced-motion: reduce` | Transitions removed; the loading spinner still turns, slowed to 3 s |
| Forced colours | Chromium's `forced-colors: active`, 5 views, axe | No violations; not looked at by eye |

## Defects found, and fixed

1. **White text on the light accent colour in the dark theme.** The active view button was 2.55:1,
   and the level chips 1.9 to 2.7:1; 4.5:1 is needed. A new `--on-accent` colour is white in the
   light theme and near-black in the dark one (7.3:1 on the accent), used by the active view button,
   the level chips and the GitHub link button.
2. **The "subnational" colour in the light theme.** White text on it was 3.72:1. It is darker now
   (`#5f7a20`, 4.89:1 with white text, 4.57:1 against the page, so also better on the graph).
3. **Two controls under 24 px**: the evidence disclosure in the detail panel (16.6 px high) and the
   small buttons such as "Clear path" (23 px). Both reach 24 px.

Eight new checks in the browser suite (`tools/test_ui.mjs`, in CI) hold these fixed in both colour
schemes; against the old CSS five of them fail.

## Not a defect, but worth knowing

- **Not measured:** the contrast of the focus indicator (only that there is one), of text laid over
  the canvas, and of the graph's softer edges, which are drawn at reduced opacity (the optional
  "Shared context" and "Mentions" lines are meant to be faint).
- **axe could not decide** (it needs a person): 20 colour-contrast items (text over the canvas and
  gradients) and 12 "label in name" items, which are the icon buttons whose visible label is a
  symbol (`+`, `−`, `✕`) while the accessible name is words ("Zoom in"). A speech-input user who says
  "click plus" may not reach them; it is a real question, not a failure.
- **The page title** is the same in every view (the criterion only asks for a descriptive title, so
  it passes); naming the view or the entity in it would help screen-reader users and browser tabs.
- **Names in other languages** carry no `lang` attribute (known limitation 4 in `ACCESSIBILITY.md`).

## Not done: needs a person

A screen reader (NVDA, JAWS, VoiceOver, TalkBack); Firefox and Safari; real keyboard-only use of the
whole site by someone who does not know it; Windows High Contrast looked at by eye; 2.4.11 (focus not
obscured) and 3.2.6; sessions with disabled users (roadmap #452).
