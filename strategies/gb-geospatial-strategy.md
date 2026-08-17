---
id: GB-GEOSPATIAL-STRATEGY
type: strategy
name: UK Geospatial Strategy 2030
alternative_names:
  - UK's Geospatial Strategy
  - Geospatial Strategy 2030
description: >
  United Kingdom government strategy for location data, published by the
  Geospatial Commission, setting the direction for the country's geospatial
  ecosystem. An earlier UK Geospatial Strategy preceded it, and the 2030
  edition is the current statement of national geospatial policy.

level: national
country: GB
region: null

status: active
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations:
  - GB-OS
  - GB-GDS
related_entities:
  - GB-OS
  - DOMAIN-GEOSPATIAL
relationships:
  - type: applies-in
    target: GB
    source: fact
    evidence: "The UK Geospatial Strategy 2030 is published on GOV.UK as United Kingdom government policy for location data, following an earlier UK Geospatial Strategy published by the Geospatial Commission (gov.uk 'UK Geospatial Strategy 2030'; assets.publishing.service.gov.uk Geospatial_Strategy.pdf). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UK Geospatial Strategy 2030"
    url: "https://www.gov.uk/government/publications/uk-geospatial-strategy-2030/uk-geospatial-strategy-2030"
    publisher: "GOV.UK"
  - title: "UK's Geospatial Strategy"
    url: "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/894755/Geospatial_Strategy.pdf"
    publisher: "Geospatial Commission (UK)"
---

# UK Geospatial Strategy 2030

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The UK government's strategy for **location data**, published by the
Geospatial Commission and setting the direction for the national geospatial
ecosystem.

## `confidence: low` and `coverage: low` — and the reason is the batch's own

This is the thinnest entity added in this batch, and it is included for one
reason: it is the **policy layer** above [[GB-OS]], and without it the UK's
geospatial presence in the Atlas is an agency with no stated national
direction — which is exactly the shape the other countries do not have.

What is **not** established:

- its **publication date**, and therefore whether the 2030 edition supersedes
  the earlier strategy or restates it. `previous_version` is `null` for that
  reason, and both documents are cited rather than one;
- its **missions or pillars** — the substance a reader would want;
- which body owns it now. It was published by the **Geospatial Commission**,
  which was merged into [[GB-GDS]] in January 2025 and no longer exists
  independently, so the `organisations:` list names both GDS and [[GB-OS]]
  as associations and **no `maintained-by` edge is asserted**.

That last point is the honest core of it: the Atlas can say this strategy
exists and applies in the UK, and cannot currently say who is responsible
for it.

## Relationships

- `applies-in` [[GB]].

No relationship to [[GB-OS]] is asserted. A strategy setting national
direction and the agency delivering it are obviously connected, but none of
the sources found states the relationship, and `governed-by` or `produces`
would both be guesses about which way it runs.

## Sources

Listed in frontmatter. Both are UK government publications and neither was
read.
