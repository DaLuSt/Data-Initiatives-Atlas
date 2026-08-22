---
id: GB-GEOSPATIAL-STRATEGY
type: strategy
name: UK Geospatial Strategy 2030
alternative_names:
  - UK’s Geospatial Strategy
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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading the GOV.UK publication page directly (2026-08-22): 'UK Geospatial Strategy 2030 ... Department for Science, Innovation & Technology, Geospatial Commission ... Policy paper ... Updated 3 August 2023.' The ministerial foreword states verbatim: 'This updated UK Geospatial Strategy builds on the approach set out in the 2020 Strategy.' Three missions are named: 'Mission 1: Embrace enabling technologies to accelerate geospatial innovation', 'Mission 2: Drive greater use of geospatial applications and insights across the economy', 'Mission 3: Build confidence in the future geospatial ecosystem.'"
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UK Geospatial Strategy 2030"
    url: "https://www.gov.uk/government/publications/uk-geospatial-strategy-2030/uk-geospatial-strategy-2030"
    publisher: "GOV.UK"
    accessed: "2026-08-22"
  - title: "UK's Geospatial Strategy"
    url: "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/894755/Geospatial_Strategy.pdf"
    publisher: "Geospatial Commission (UK)"
    accessed: "2026-08-22"
---

# UK Geospatial Strategy 2030

> **Verified 2026-08-22.** The GOV.UK publication page was read directly
> and confirmed the claims below verbatim. The Geospatial_Strategy.pdf
> (the earlier, 2020 strategy) was fetched but not text-extracted this
> pass; the 2030 edition's own foreword, read on the GOV.UK page, was
> sufficient to confirm the "builds on the 2020 Strategy" relationship.

## Description

Confirmed by reading the GOV.UK publication page directly (2026-08-22):
"UK Geospatial Strategy 2030 ... published under the 2022 to 2024 Sunak
Conservative government ... Updated 3 August 2023." The UK government's strategy for **location data**, published by the
Geospatial Commission and setting the direction for the national geospatial
ecosystem. Its ministerial foreword states verbatim: "This updated UK
Geospatial Strategy builds on the approach set out in the 2020 Strategy."

## `confidence: low` and `coverage: low` — and the reason is the batch's own

This is the thinnest entity added in this batch, and it is included for one
reason: it is the **policy layer** above [[GB-OS]], and without it the UK's
geospatial presence in the Atlas is an agency with no stated national
direction — which is exactly the shape the other countries do not have.

This pass established the **publication date** (updated 3 August 2023, under
the 2022–2024 government) and the three **missions**: embracing enabling
technologies, driving wider use of geospatial applications, and building
confidence in the geospatial ecosystem. `previous_version` is left `null`
regardless — the strategy's own foreword says it "builds on" the 2020
strategy, which is a looser relationship than supersession, and the 2020
document was not itself Atlas-modelled to point `previous_version` at.

What is still **not** established:

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

Listed in frontmatter. Both are UK government publications; the GOV.UK
publication page was read directly this pass, the 2020-strategy PDF was
fetched but not text-extracted.
