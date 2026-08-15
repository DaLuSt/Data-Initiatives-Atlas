---
id: EU-SEMIC
type: organisation
name: SEMIC
alternative_names:
  - Semantic Interoperability Community
  - SEMIC action
description: >
  European Commission action on semantic interoperability, operating within
  Interoperable Europe. It maintains the DCAT Application Profile for data
  portals in Europe and related semantic specifications, and runs the SEMIC
  Support Centre.

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
  - EU-DCAT-AP
  - EU-EIF
relationships:
  - type: maintained-by
    target: EU-DCAT-AP
    source: interpretation
    evidence: "DCAT-AP is under maintenance by the SEMIC action, Interoperable Europe (interoperable-europe.ec.europa.eu; github.com/SEMICeu/DCAT-AP). Direction expressed SEMIC→DCAT-AP for navigability; the authoritative framing belongs on the DCAT-AP entity."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SEMIC Support Centre — DCAT-AP"
    url: "https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/releases"
    publisher: "European Commission — Interoperable Europe Portal"
  - title: "SEMICeu/DCAT-AP — issue tracker for the maintenance of DCAT-AP"
    url: "https://github.com/SEMICeu/DCAT-AP"
    publisher: "SEMIC (European Commission)"
---

# SEMIC

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

SEMIC is the European Commission's semantic interoperability action,
operating within Interoperable Europe. It maintains [[EU-DCAT-AP]] — openly,
with the specification and its issue tracker on GitHub — and runs the SEMIC
Support Centre.

Its position matters structurally: semantic interoperability is one of the
layers of [[EU-EIF]], and SEMIC is where that layer is actually operated
rather than described. No relationship to the EIF is asserted, because the
sources do not state one.

## Typing note

SEMIC is recorded as an `organisation`, but it is described as an "action"
or "community" rather than a body with legal personality — closer to a
programme within the Commission than an institution. `organisation` is the
best available fit, and the alternative (`programme`) would misrepresent its
ongoing maintenance role. Flagged in `discovery/unresolved.md`.

`coverage: low`: SEMIC's other specifications — the Core Vocabularies, and
the GeoDCAT-AP and StatDCAT-AP extensions named in DCAT-AP sources — were
not researched.

## Relationships

- Maintains [[EU-DCAT-AP]].

## Sources

Listed in frontmatter.
