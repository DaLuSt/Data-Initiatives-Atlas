---
id: GB-DSIT
type: organisation
name: Department for Science, Innovation and Technology
alternative_names:
  - DSIT
description: >
  Former United Kingdom ministerial department, created in February 2023 by
  bringing together technology, digital, science and innovation
  responsibilities from across government, and abolished on 21 July 2026
  following the appointment of a new Prime Minister. Its functions were
  divided three ways: business, innovation, science and trade to a new
  Department for Business, Innovation, Science and Trade; digital
  transformation, online harms, cyber security, digital identity and the
  Government Digital Service to the Department for Culture, Media and Sport;
  and artificial intelligence policy to the Cabinet Office.

level: national
country: GB
region: null

status: superseded
confidence: medium
coverage: low
verification: search-only

start_date: 2023-02-07
end_date: 2026-07-21
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - GB-GDS
  - GB-DCMS
relationships: []

sources:
  - title: "DSIT to be scrapped with 'strengthened DCMS to take responsibility for digital transformation'"
    url: "https://www.publictechnology.net/2026/07/21/government-and-politics/dsit-to-be-scrapped-with-strengthened-dcms-to-take-responsibility-for-digital-transformation/"
    publisher: "PublicTechnology"
  - title: "DSIT scrapped as Burnham government reshapes Whitehall tech functions"
    url: "https://www.ukauthority.com/articles/dsit-scrapped-as-burnham-government-reshapes-whitehall-tech-functions"
    publisher: "UKAuthority"
  - title: "Government abolishes DSIT as AI gains a seat at the Cabinet table"
    url: "https://www.thinkdigitalpartners.com/news/2026/07/21/government-abolishes-dsit-as-ai-gains-a-seat-at-the-cabinet-table/"
    publisher: "THINK Digital Partners"
  - title: "DSIT Accounting Officer system statement 2024"
    url: "https://www.gov.uk/government/publications/dsit-accounting-officer-system-statement-2024/dsit-accounting-officer-system-statement-2024-html"
    publisher: "GOV.UK"
---

# Department for Science, Innovation and Technology

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

DSIT was created in **February 2023** to concentrate technology, digital,
science and innovation responsibilities in one department, and **abolished
on 21 July 2026**, the day after a change of Prime Minister. It lasted
around three and a half years.

## The first abolition in the Atlas

The Atlas has recorded three institutional transformations before this one,
and all three were **continuations**:

| | What happened | How the Atlas models it |
|---|---|---|
| [[ES-SGAD]] → [[ES-AEAD]] | directorate became a state agency, 2025 | `successor`, completed |
| [[PL-COI]] → *Agencja Informatyzacji* | draft law in consultation | not modelled — does not exist yet |
| GIODO → [[PL-UODO]] | only *part* of competencies transferred | no succession asserted |
| **DSIT** | **abolished; functions split three ways** | **`status: superseded`, `successor: null`** |

This is the first entity in the Atlas to **stop existing**. It is also the
first whose functions went to *more than one* place.

## `successor: null`, and why that is a schema finding rather than a gap

DSIT's functions were divided three ways:

- **business, innovation, science and trade** → a new *Department for
  Business, Innovation, Science and Trade* (DBIST);
- **digital transformation, online harms, cyber security, digital identity
  and [[GB-GDS]]** → [[GB-DCMS]];
- **artificial intelligence policy and public-sector AI adoption** → the
  Cabinet Office.

`metadata/metadata-schema.md` gives each entity a **single** `successor`
field, described as a way to *"chain superseded entities together without
ever deleting or reusing an ID"*. A chain is exactly the wrong shape here:
this is a one-to-three split, and naming any one of the three as *the*
successor would assert something false about the other two.

So `successor` is **null**, and the split is recorded in prose. Two of the
three destinations are not Atlas entities at all — DBIST and the Cabinet
Office were not researched — so even a list-valued field would be only
one-third populated.

**A fan-out succession is not expressible.** That is now in
`progress/backlog.md`, alongside the amendment relationship type that four
batches have wanted.

## Why it is here at all

An abolished department could simply have been left out, and the batch would
have been one entity smaller. It is included because **[[GB-GDS]]'s parent
changed**, and an organisation whose governance moved in the last month of
the Atlas's coverage is worth being able to see. The `governed-by` edge on
GDS points at DCMS and is dated 21 July 2026; without DSIT there is nothing
to say what it pointed at before.

## `coverage: low`

Nothing about DSIT's internal structure, its predecessor arrangements, or
the legal instrument effecting the abolition is recorded. Three of the four
sources are trade press. **No machinery-of-government order was located** —
the abolition is reported, not cited.

## Relationships

None asserted. [[GB-GDS]] carries the `governed-by` edge, pointing at
[[GB-DCMS]] rather than here.

## Sources

Listed in frontmatter.
