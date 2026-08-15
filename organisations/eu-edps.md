---
id: EU-EDPS
type: organisation
name: European Data Protection Supervisor
alternative_names:
  - EDPS
description: >
  Independent data protection authority supervising the processing of
  personal data by EU institutions and bodies. It appoints a representative
  to the European Data Protection Board and issues opinions, often jointly
  with the Board, on EU legislative proposals.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EDPB
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "The EDPS is the independent authority supervising processing of personal data by EU institutions and bodies (edps.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "The EDPS has the right to appoint one representative to the EDPB, facilitating close cooperation between the two (edpb.europa.eu; edps.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EDPB and EDPS support strengthening EU's cybersecurity — press release"
    url: "https://www.edps.europa.eu/press-publications/press-news/press-releases/2026/edpb-and-edps-support-strengthening-eus-cybersecurity-and-easing-compliance-while-protecting-individuals-personal-data_en"
    publisher: "European Data Protection Supervisor"
---

# European Data Protection Supervisor (EDPS)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The EDPS is an independent data protection authority whose supervisory remit
covers the EU institutions and bodies themselves — as distinct from
[[NL-AP]] and its counterparts, which supervise within member states. It
appoints one representative to [[EU-EDPB]].

In practice the EDPS and the EDPB issue joint opinions on EU legislative
proposals; a 2026 joint opinion on cybersecurity and network and information
security is among the sources here. The EDPS also issued an opinion on
[[EU-DATA-STRATEGY]] in 2020, cited in that entity's research.

`coverage: low`: the supervisory function over EU institutions, and the
EDPS's opinion practice, were not researched.

## Relationships

- Participates in [[EU-EDPB]].

## Sources

Listed in frontmatter — a single source, and a press release rather than an
institutional description.
