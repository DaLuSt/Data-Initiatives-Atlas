# What should the world map do at about 200 countries?

## Context
Roadmap #508 (open) and #645 (the decision, on the roadmap since 2026-10-15). In the Global Atlas, the "World map" arrangement places each country's cluster by
longitude at 360 px per degree and keeps large clusters apart. The page's minimum zoom is 0.04. Details and
numbers are in `docs/scale-check.md`.

## Evidence found
Measured from node positions on the real Atlas (89 countries, 855 entities) and on a test build (194 countries,
1,087 entities, `tools/scale_fixture.py`): the map spans about 120,000 px and 125,000 px across. At the minimum zoom
the page is 5,000 px wide at most, so the Fit button cannot show the whole map in either build; the first view is a
sparse middle section in which clusters are too small to see. The Grouped layout and the Compare view did not have
this problem.

## Possible interpretations
1. Lower the minimum zoom to about 0.008 so Fit shows everything. Cheap; the clusters are then a pixel across.
2. Scale the map down and draw each country as one dot that opens into its entities on zoom. The option that makes
   the map useful at 195 countries; a design change to a layout that has tests.
3. Keep the map as it is, say on the page that it is a zoom-and-pan view, and point to the Country filter and Compare.

## Why this can't be decided safely from here
It is a choice about what the map is for (an overview, or a place to explore one region), not a defect with one right
fix. Option 2 changes a layout with its own tests and a documented design (`docs/graph-development.md`).

## Recommended next research
Ask a few visitors what they expect from the map (the usability test in #452 is the place), then pick an option and
record it in `docs/graph-development.md`.
