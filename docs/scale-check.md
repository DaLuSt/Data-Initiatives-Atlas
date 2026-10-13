# The site at about 200 countries

Roadmap #508. The Atlas has 89 country anchors; the next-countries plan (#451) takes it towards 195.
This records what was checked on a test build with 194 countries, and what it found.

## How it was checked

`tools/scale_fixture.py` copies the repository to a folder outside it and adds an anchor and one to
five placeholder organisations for each of 105 countries that have no anchor yet, then builds the
graph. The result has 1,087 entities and 194 countries (the real Atlas: 855 and 89). The
placeholders carry no claim about any country and never reach the real data.

```
python tools/scale_fixture.py /tmp/atlas195
python -m http.server 8766 --directory /tmp/atlas195/site
```

It was opened at 1440 × 900 and at 390 × 844 in Chromium, and the layouts were measured from the
node positions, not judged by eye alone.

## Findings

| Part | At 194 countries | Verdict |
|---|---|---|
| Global Atlas, "Grouped by level and country" | 194 country blocks, none overlapping; the whole layout is 8,700 × 9,500 px (7,200 × 8,400 at 89) and still fits on screen at 0.073 zoom (the minimum is 0.04) | Fine. No change. |
| Compare view | Columns that have nothing recorded are hidden by default, so the table only grows with data: 41 columns now, 195 if all are shown. The instrument column and the header row stay in view while scrolling | Fine. No change. Revisit when more than about 100 countries carry data. |
| Country filter | A flat list of 194 in a box five rows tall, 5,000 px of scrolling (2,300 at 89) | **Fixed here:** a "Find a country" box above the list narrows it by name, ignoring case and accents; a ticked country stays in view. |
| World map layout | Spread over about 125,000 px (120,000 at 89), because the layout places countries by longitude at 360 px per degree and keeps the large clusters apart. The page's minimum zoom is 0.04, so **Fit cannot show the whole map**, at 89 countries or at 194: the first view shows a sparse middle part with the clusters too small to see | Not new and not caused by growth, but it makes the map hard to use. Needs a design decision, see below. |
| Load time | First graph 5.2 s on Slow 4G with a 4x CPU slowdown (4.7 s at 855 entities) | Over the 5 s budget in `docs/performance.md`, as that page projects at about 1,000 entities. |

## Decision for the owner: the world map

The map needs one of these; none is done here:

1. Lower the minimum zoom to about 0.008 so Fit shows everything. Cheap, but the clusters are then
   a pixel across and the map is only a way to find where to zoom.
2. Scale the map down: fewer pixels per degree, with each country's cluster drawn smaller (for
   example one dot per country that opens into its entities on zoom).
3. Keep the map as it is and say so on the page, pointing to the Country filter and Compare.

Option 2 is the one that would make the map useful at 195 countries. It is a design change to a
layout that has tests, so it is raised as its own item rather than slipped into this one.

## Where the time went on the first graph

See `docs/performance.md`: the first graph is CPU-bound, and the entity count at which the budget
is missed is also about where the 195-country plan lands.
