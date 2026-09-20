---
id: DE-HEALTHTRACK-X
type: data-space
name: HealthTrack-X
alternative_names:
  - HealthTrack-X data space
description: >
  German lighthouse project under Manufacturing-X, building an open,
  decentralised data ecosystem for the healthcare sector to digitise
  supply chains for medical products and track goods through
  standardised electronic documentation, based on Gaia-X principles and
  components (Cross Federation Services Components, Eclipse Dataspace
  Components). Coordinated by Fraunhofer ISST with eight partners
  including Roche and Siemens Healthineers, funded by the German Federal
  Ministry for Economic Affairs and Energy (BMWE), the project ran from
  May 2024 to June 2026.

level: sectoral
country: DE
region: EU

status: completed
confidence: medium
coverage: medium
verification: primary-source

start_date: 2024-05-01
end_date: 2026-06-30
last_verified: "2026-09-20"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - DE-MANUFACTURING-X
  - EU-GAIA-X
relationships:
  - type: part-of
    target: DE-MANUFACTURING-X
    source: fact
    evidence: "Confirmed by reading Fraunhofer ISST's own Manufacturing-X overview page directly (already cited on [[DE-MANUFACTURING-X]], 2026-08-28), which names HealthTrack-X among Manufacturing-X's supported projects. HealthTrack-X's own dedicated page, also read directly (2026-09-20), does not itself mention Manufacturing-X by name, but its funding code (13MX007D) shares the same 'MX' prefix as Factory-X (13MX001F), Aerospace-X (13MX004F/13MX004A) and Construct-X's national funding line — consistent with a shared Manufacturing-X funding programme, though this pattern alone is not treated as proof and the `part-of` edge rests on the overview page's direct naming."
    confidence: medium
    valid_from: "2024-05-01"
    valid_until: null
  - type: based-on
    target: EU-GAIA-X
    source: fact
    evidence: "Confirmed by reading Fraunhofer ISST's own HealthTrack-X page directly (2026-09-20): the ecosystem 'builds on Gaia-X principles and components,' specifically Cross Federation Services Components (XFSC) and Eclipse Dataspace Components (EDC)."
    confidence: high
    valid_from: "2024-05-01"
    valid_until: null

sources:
  - title: "HealthTrack-X"
    url: "https://www.isst.fraunhofer.de/en/departments/healthcare/projects/HealthTrack-X.html"
    publisher: "Fraunhofer ISST"
    accessed: "2026-09-20"
---

# HealthTrack-X

> **Created 2026-09-20**, closing the last named sibling on
> `discovery/unresolved.md` row #131. Sourced from Fraunhofer ISST's own
> dedicated page, read directly. Note this entity's `part-of` edge to
> [[DE-MANUFACTURING-X]] is sourced from the *other* entity's own page,
> not this one's — HealthTrack-X's own page does not mention
> Manufacturing-X by name. See "The one-directional source" below.

## Description

HealthTrack-X builds an **open, decentralised data ecosystem for the
healthcare sector**. Confirmed by reading Fraunhofer ISST's own page
directly: its focus is digitising supply chains for **medical
products**, developing "uniform standards that allow physical goods and
their routes along the supply chain to be digitally recorded and
tracked" through standardised electronic documentation.

**Coordinated by Fraunhofer ISST**, with **Florian Lauf** (Group Manager,
"Personal Data Ecosystems") as primary contact. Eight named partners:
**Roche, Bundesverband der Deutschen Industrie e.V. (BDI), adesso SE,
adesso as a service GmbH, Gesundheitsforen, Siemens Healthineers, Rote
Liste** and **W2healthcare**.

## Built on Gaia-X, not Manufacturing-X's own architecture

Unlike Factory-X, Aerospace-X and Construct-X, which the Atlas records as
`based-on` [[DE-CATENA-X]], HealthTrack-X's own page states it "builds on
**Gaia-X** principles and components" directly — specifically Cross
Federation Services Components (XFSC) and Eclipse Dataspace Components
(EDC) — without mentioning Catena-X. `based-on` [[EU-GAIA-X]] is recorded
instead, rather than assuming the same Catena-X lineage the other three
siblings carry.

## The one-directional source

Fraunhofer ISST's own **Manufacturing-X overview page**, already read
directly and cited on [[DE-MANUFACTURING-X]], names HealthTrack-X among
Manufacturing-X's supported projects — the source for this entity's
`part-of` edge. HealthTrack-X's **own dedicated page**, read directly
this pass, does **not** itself mention Manufacturing-X. The funding code
it carries, **13MX007D**, shares the "MX" prefix pattern with Factory-X
(13MX001F), Aerospace-X (13MX004F/13MX004A) and Construct-X's grant line
— consistent with, but not independent proof of, a shared Manufacturing-X
funding programme. The `part-of` edge is recorded at `confidence: medium`
on the strength of the overview page alone.

## Funding and timeline

Funded by the German **Federal Ministry for Economic Affairs and Energy
(BMWE)**, funding code 13MX007D. Ran **May 2024 – June 2026**, per
Fraunhofer ISST's own page, read directly.

## Not modelled

- HealthTrack-X's **eight named partner organisations** individually.
- **XFSC** and **EDC**, the specific Gaia-X components it builds on.
- The **Fraunhofer Medical Data Space** and **HEALTH-X dataLOFT**, two
  adjacent Fraunhofer ISST healthcare-data-space projects named in search
  results alongside HealthTrack-X but not independently researched or
  confirmed related to it this pass.

## Relationships

- `part-of` [[DE-MANUFACTURING-X]] — `confidence: medium`.
- `based-on` [[EU-GAIA-X]] — `confidence: high`.

## Sources

Listed in frontmatter, read directly.
