---
id: DE-CONSTRUCT-X
type: data-space
name: Construct-X
alternative_names:
  - Construct-X data space
description: >
  German lighthouse project under Manufacturing-X, developing open-source
  data spaces, a cloud-based reference architecture and cloud-edge
  applications for the construction industry, aiming to improve
  productivity, efficiency and transparency on construction sites. Led by
  Fraunhofer ISST with around 40 partners from construction, skilled
  trades, IT, research and industry associations, funded by the German
  Federal Ministry for Economic Affairs and Energy (BMWE) and the EU's
  Important Project of Common European Interest for Next Generation
  Cloud Infrastructure and Services (IPCEI-CIS), the project runs from
  1 March 2025 to 29 February 2028.

level: sectoral
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2025-03-01
end_date: 2028-02-29
last_verified: "2026-09-25"
previous_version: null
successor: null

domains:
  - DOMAIN-MANUFACTURING
organisations: []
related_entities:
  - DE-MANUFACTURING-X
  - DE-CATENA-X
  - DE-FACTORY-X
  - DE-AEROSPACE-X
relationships:
  - type: part-of
    target: DE-MANUFACTURING-X
    source: fact
    evidence: "Confirmed by reading Fraunhofer ISST's own Construct-X page directly (2026-09-20): the project 'operates within the Manufacturing-X project family,' emphasising connection with related data space initiatives including Catena-X, Factory-X, Aerospace-X and HealthTrack-X, as well as domain-agnostic initiatives such as the Eclipse Dataspace Working Group."
    confidence: high
    valid_from: "2025-03-01"
    valid_until: null
  - type: based-on
    target: DE-CATENA-X
    source: fact
    evidence: "Confirmed by reading Fraunhofer ISST's own page directly (2026-09-20), which lists Catena-X among the sibling initiatives Construct-X aims to stay connected and compatible with. Recorded as `based-on` [[DE-CATENA-X]] on the same basis [[DE-FACTORY-X]] and [[DE-AEROSPACE-X]] already carry, since Catena-X is the family's own originating data space in the Atlas."
    confidence: medium
    valid_from: "2025-03-01"
    valid_until: null

sources:
  - title: "Construct-X: Simplified information processing on construction sites"
    url: "https://www.isst.fraunhofer.de/en/departments/industrial-manufacturing/projects/construct-x.html"
    publisher: "Fraunhofer ISST"
    accessed: "2026-09-20"
  - title: "Construct-X: Fraunhofer IFF Is Strengthening Digital Collaboration in the Construction Industry"
    url: "https://www.iff.fraunhofer.de/en/press/2025/construct-x-fraunhofer-iff-is-strengthening-digital-collaboration-in-the-construction-industry.html"
    publisher: "Fraunhofer IFF"
    accessed: "2026-09-20"
---

# Construct-X

> **Created 2026-09-20**, further narrowing `discovery/unresolved.md` row
> #131 ("Factory-X, Aerospace-X, energy data-X, Plattform Industrie 4.0
> not modelled" — the row's original wording; Factory-X and Aerospace-X
> closed in PR #276 and #285). Sourced from Fraunhofer ISST's own page
> and Fraunhofer IFF's own press release, both read directly.
> HealthTrack-X and Plattform Industrie 4.0 remain unmodelled.
>
> **Domain added 2026-09-25**: [[DOMAIN-MANUFACTURING]], created because
> "Vervaardiging" is one of the Dutch Cyberbeveiligingswet's own named
> sectors.

## Description

Construct-X is a **lighthouse project under [[DE-MANUFACTURING-X]]**,
developing **open-source data spaces**, a cloud-based reference
architecture, and **cloud-edge applications** for the construction
industry. Confirmed by reading Fraunhofer ISST's own page directly: its
goal is to increase productivity, efficiency and transparency on
construction sites, including technologies for a "multi-provider cloud
edge continuum" enabling latency-free, secure on-site data processing.

**Led by Fraunhofer ISST**, per its own page, with roughly **40
partners** — Fraunhofer IFF's own press release, read directly, specifies
these span "construction, skilled trades, IT, research and industry
associations." Fraunhofer IFF itself leads two named use cases:
**Connected Design** (helping architects incorporate prefabricated
components more easily) and **Digital Progress Reporting** (sensor- and
AI-driven monitoring of construction-site conditions against the design).

## Funding: national and EU

Confirmed by reading Fraunhofer IFF's own press release directly:
Construct-X is funded by the German **Federal Ministry for Economic
Affairs and Energy (BMWE)** and by the **European Union**, specifically
as part of the EU's **Important Project of Common European Interest for
Next Generation Cloud Infrastructure and Services (IPCEI-CIS)** — the
first Atlas entity in the Manufacturing-X family whose sourcing names an
EU-level funding instrument alongside the national one.

## Timeline

Fraunhofer ISST's own page, read directly, gives **1 March 2025 to
29 February 2028** — a three-year run, matching Fraunhofer IFF's press
release description of "a three-year project."

## Not modelled

- **HealthTrack-X**, the remaining named sibling on [[DE-MANUFACTURING-X]]'s
  own entity, not independently researched this pass.
- **Plattform Industrie 4.0**, the concept base the whole family builds on.
- Construct-X's **individual named partners**.
- The **Eclipse Dataspace Working Group** and other "domain-agnostic"
  initiatives Construct-X names as connection points.

## Relationships

- `part-of` [[DE-MANUFACTURING-X]] — `confidence: high`.
- `based-on` [[DE-CATENA-X]] — `confidence: medium`.

## Sources

Listed in frontmatter, both read directly.
