---
id: EU-DSSC
type: organisation
name: Data Spaces Support Centre
alternative_names:
  - DSSC
description: >
  EU support body for the creation of common European data spaces. It
  explores the needs of data space initiatives, defines common requirements
  and establishes best practices, and publishes the DSSC Blueprint together
  with a toolbox, glossary and help centre for the data spaces community.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - EU-DSSC-BLUEPRINT
  - EU-GAIA-X
relationships:
  - type: produces
    target: EU-DSSC-BLUEPRINT
    source: fact
    evidence: "The DSSC publishes the blueprint alongside a glossary, starters kit and help centre on its support platform, confirmed 2026-08-21 on digital-strategy.ec.europa.eu and toolbox.dssc.eu."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The Data Spaces Support Centre"
    url: "https://digital-strategy.ec.europa.eu/en/news/data-spaces-support-centre"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-21"
  - title: "DSSC Toolbox"
    url: "https://toolbox.dssc.eu/?pane=co-creation"
    publisher: "Data Spaces Support Centre"
    accessed: "2026-08-21"
---

# Data Spaces Support Centre (DSSC)

> **Verified 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.

## Description

The DSSC contributes to creating [[EU-COMMON-DATA-SPACES]], which
collectively are intended to form a sovereign, interoperable and trustworthy
data-sharing environment enabling data reuse within and across sectors.

Its function is horizontal rather than sectoral: it explores the needs of
data space initiatives, defines common requirements, and establishes best
practices to accelerate the formation of data spaces. Its support platform
carries a collection of assets — glossary, starters kit,
[[EU-DSSC-BLUEPRINT]] — plus a Help Centre for the data spaces community.

`coverage: low`: the DSSC's own governance, funding and legal form were not
established. Whether it is a project, a consortium or a standing body is
unclear from the sources, which is why `organisation` is used with the same
reservations noted on [[EU-SEMIC]].

## Relationships

- Produces [[EU-DSSC-BLUEPRINT]].
- Supports [[EU-COMMON-DATA-SPACES]].
- [[EU-GAIA-X]] `participates-in` this consortium — closes
  `discovery/unresolved.md` row #55 (2026-09-19); the edge and its sourcing
  are recorded on [[EU-GAIA-X]], where it was discovered.

## Sources

Listed in frontmatter. Fraunhofer ISST's own DSSC page, naming Gaia-X
among the consortium partners, was read directly on [[EU-GAIA-X]]
2026-09-19, not re-fetched here.
