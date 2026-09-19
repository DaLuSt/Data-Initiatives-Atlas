---
id: DE-FACTORY-X
type: data-space
name: Factory-X
alternative_names:
  - Factory-X data space
description: >
  German lighthouse project under Manufacturing-X, building a sovereign
  data ecosystem for factory equipment suppliers and their customers in
  the mechanical and industrial engineering sector, built on the
  foundations of Catena-X and the principles of Plattform Industrie 4.0.
  Co-led by SAP and Siemens with 47 partners and ten associated partners,
  funded by the German Federal Ministry for Economic Affairs and Climate
  Protection (BMWK), the consortium project ran from January 2024 and
  concluded on 30 June 2026.

level: sectoral
country: DE
region: EU

status: completed
confidence: medium
coverage: medium
verification: primary-source

start_date: 2024-01-01
end_date: 2026-06-30
last_verified: "2026-09-19"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - DE-MANUFACTURING-X
  - DE-CATENA-X
relationships:
  - type: part-of
    target: DE-MANUFACTURING-X
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #131. Confirmed by reading Fraunhofer IOSB's own Factory-X page and factory-x.org's own page directly (2026-09-19): Fraunhofer ISST's own Manufacturing-X page (already cited on [[DE-MANUFACTURING-X]]) names Factory-X among Manufacturing-X's supported lighthouse projects; factory-x.org's own page states Factory-X 'functions as a lighthouse project within the broader Manufacturing-X initiative,' adding that 'collaboration among the Manufacturing-X projects and within the MX community continues' after Factory-X's own conclusion."
    confidence: high
    valid_from: "2024-01-01"
    valid_until: null
  - type: based-on
    target: DE-CATENA-X
    source: fact
    evidence: "Confirmed by reading factory-x.org's own page directly (2026-09-19), which describes Factory-X as 'an open and collaborative digital ecosystem for factory outfitters and operators, built on the foundations of Catena-X and the principles of Plattform Industrie 4.0.' Fraunhofer IOSB's own page, also read directly, independently corroborates: 'The German Federal Ministry for Economic Affairs and Climate Protection (BMWK) has launched Catena-X, a corresponding data room for the automotive industry. This was followed by the more comprehensive Manufacturing-X initiative,' with Factory-X as its mechanical-engineering-specific lighthouse."
    confidence: high
    valid_from: "2024-01-01"
    valid_until: null

sources:
  - title: "Factory-X — a sovereign data room for mechanical and industrial engineering"
    url: "https://www.iosb.fraunhofer.de/en/projects-and-products/factory-x.html"
    publisher: "Fraunhofer IOSB"
    accessed: "2026-09-19"
  - title: "Factory-X"
    url: "https://factory-x.org/"
    publisher: "Factory-X"
    accessed: "2026-09-19"
---

# Factory-X

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #131 ("Factory-X, Aerospace-X, energy data-X, Plattform Industrie 4.0
> not modelled"). Sourced from Fraunhofer IOSB's own page and factory-x.org's
> own page, both read directly. Aerospace-X, Construct-X, HealthTrack-X
> and Plattform Industrie 4.0 remain unmodelled — see "Not modelled" below.

## Description

Factory-X is a **lighthouse project under [[DE-MANUFACTURING-X]]**,
building a sovereign, open and collaborative data ecosystem for **factory
equipment suppliers and their customers** in the mechanical and industrial
engineering sector. Confirmed by reading factory-x.org's own page
directly: it is "built on the foundations of [[DE-CATENA-X]] and the
principles of Plattform Industrie 4.0."

**Co-led by SAP and Siemens**, per Fraunhofer IOSB's own page, read
directly, with **47 partners and ten associated partners** drawn from
industry, SMEs, associations and research institutions — including BASF,
Trumpf, DMG Mori, Festo, Hilscher, Lenze, Phoenix Contact, Schunk, SICK and
Wittenstein, plus Fraunhofer IOSB and other Fraunhofer institutes as
shareholders. It was **funded by the German Federal Ministry for Economic
Affairs and Climate Protection (BMWK)**, grant number 13MX001F.

## A concluded consortium project, still part of the MX family

The project **ran from January 2024 to 30 June 2026** — confirmed
independently by both sources read this pass, with factory-x.org's own
page stating the consortium project "concluded on June 30, 2026" while
noting that "collaboration among the Manufacturing-X projects and within
the MX community continues." `status: completed` reflects the consortium
project's own end date; it does not mean the underlying data ecosystem or
its technical outputs cease to exist.

Coordination of the cross-project **MX Guidance Board**, which
Factory-X initiated, has since passed to **VDI TZ**.

## Not modelled

- **Aerospace-X**, **Construct-X** and **HealthTrack-X** — the other
  lighthouse/sibling projects named on [[DE-MANUFACTURING-X]]'s own entity,
  not independently researched this pass.
- **Plattform Industrie 4.0** — the concept base Manufacturing-X and
  Factory-X both build on, named repeatedly but not itself modelled.
- The **Factory-X kernel**, the decentralised technical architecture
  Fraunhofer ISST co-developed, and the specific open standards it uses
  (AAS, OPC-UA, EDC) — named in search results but not confirmed by a
  direct read this pass.
- Factory-X's **47 named partners and ten associated partners**
  individually.

## Relationships

- `part-of` [[DE-MANUFACTURING-X]] — `confidence: high`.
- `based-on` [[DE-CATENA-X]] — `confidence: high`.

## Sources

Listed in frontmatter, both read directly.
