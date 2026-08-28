---
id: EU-GREEN-DEAL-DATA-SPACE
type: data-space
name: Green Deal Data Space
alternative_names:
  - GDDS
  - European Green Deal Data Space
description: >
  One of the common European data spaces, intended to integrate
  cross-sectoral data in support of European Green Deal priority actions —
  biodiversity, zero pollution, circular economy, climate change, forestry
  services, smart mobility and environmental compliance.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - EU-INSPIRE
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Confirmed by reading digital-strategy.ec.europa.eu's own 'Common European data spaces' overview directly (2026-08-28): the Green Deal data space is listed among the fourteen. The Commission's own Environment page 'Green Data', read directly, confirms the Green Deal Data Space (GDDS) as 'a shared digital platform open to businesses, public entities, academia, civil society, and citizens' enabling environmental data sharing, led by the Commission through the Digital Europe Programme."
    confidence: high
    valid_from: null
    valid_until: null
  - type: references
    target: EU-INSPIRE
    source: fact
    evidence: "Confirmed by reading environment.ec.europa.eu's own 'Green Data' page directly (2026-08-28): the Green Deal Data Space 'integrates with existing frameworks like the INSPIRE Directive (under revision for Q4 2025 adoption)' as part of its technical foundation. No detail on the nature of the integration beyond this statement was found."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "Green Data"
    url: "https://environment.ec.europa.eu/law-and-governance/green-data_en"
    publisher: "European Commission — Environment"
    accessed: "2026-08-28"
  - title: "What is the Green Deal Data Space?"
    url: "https://ad4gd.eu/what-is-the-green-deal-data-space/"
    publisher: "AD4GD project"
    accessed: "2026-08-28"
  - title: "European Green Deal Data Space"
    url: "https://errin.eu/calls/european-green-deal-data-space"
    publisher: "ERRIN"
---

# Green Deal Data Space

> **Re-verified 2026-08-28.** Three of four cited sources were read
> directly, including a new Commission Environment page found this pass
> that gives the space a governance anchor (Digital Europe Programme) and
> a newly-sourced, if thin, connection to [[EU-INSPIRE]]. `errin.eu`
> returned HTTP 403 and was not read. `verification` moves from
> `search-only` to `primary-source`.

## Description

The Green Deal Data Space is one of the fourteen common European data
spaces. It is described as integrating large volumes of cross-sectoral data
in support of European Green Deal priority actions: biodiversity, zero
pollution, circular economy, climate change, forestry services, smart
mobility and environmental compliance. Confirmed by reading the
Commission's own Environment page directly: it is "a shared digital
platform open to businesses, public entities, academia, civil society, and
citizens" for sharing, exchanging and trading environmental data, led by
the Commission through the **Digital Europe Programme**, and intended to
simplify corporate compliance reporting (e.g. under the Corporate
Sustainability Reporting Directive) alongside its research and innovation
purposes.

Its breadth is its distinguishing feature — unlike the health or mobility
spaces it is defined by a policy programme rather than a sector, and cuts
across several of the others.

`confidence: medium`, `coverage: medium` — up from `low`/`low`: purpose and
a governance anchor are now confirmed from a Commission source read
directly, though responsible organisations, standards and detailed
infrastructure remain unresearched. `ad4gd.eu`, also read directly,
confirms the same seven priority actions and frames the space's three
pillars as trust/security, FAIR principles, and data sovereignty.

## A thin but sourced connection to INSPIRE

The Commission's Environment page states, in its own words, that the GDDS
"integrates with existing frameworks like the INSPIRE Directive (under
revision for Q4 2025 adoption)." That is enough to record a `references`
edge to [[EU-INSPIRE]] — an EU legislation entity in this same
re-verification batch — but not enough to say more: no detail on the
mechanism of integration was found, and the claimed INSPIRE revision was
not itself researched here.

## No domain tagged

`domains:` is empty. An Environment domain would be the natural tag, but it
would currently connect this entity alone — below the two-entity threshold
in `metadata/taxonomy.md` §1. This is the same treatment given to
[[NL-DSGO]] and to Health before [[NL-HEALTH-RI]] existed. Queued.

The European Green Deal itself is not an Atlas entity; it is a policy
programme well outside the data/digital scope, and pulling it in would widen
the Atlas considerably. Noted rather than done.

## Relationships

- Part of [[EU-COMMON-DATA-SPACES]].
- `references` [[EU-INSPIRE]] (new this pass).

## Sources

Listed in frontmatter, three of four read directly this pass. `errin.eu`
returned HTTP 403 and was not read.
