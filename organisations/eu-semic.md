---
id: EU-SEMIC
type: organisation
name: SEMIC
alternative_names:
  - Semantic Interoperability Community
  - SEMIC action
description: >
  The Semantic Interoperability Community (SEMIC), a European Commission
  action operating within Interoperable Europe. Per the Interoperable
  Europe Portal's own glossary, SEMIC "develops solutions to help European
  public administrations perform seamless and meaningful cross-border and
  cross-domain data exchanges"; it began under the former ISA/ISA² Programme,
  which evolved into Interoperable Europe. It maintains the DCAT Application
  Profile for data portals in Europe and related semantic specifications,
  and runs the SEMIC Support Centre.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-DCAT-AP
  - EU-EIF
relationships:
  - type: part-of
    target: EU-COMMISSION
    source: fact
    evidence: "Confirmed by reading interoperable-europe.ec.europa.eu's own glossary directly (2026-08-28): 'The Semantic Interoperability Community (SEMIC) develops solutions to help European public administrations perform seamless and meaningful cross-border and cross-domain data exchanges'; SEMIC began under the former ISA/ISA² Programme, a European Commission programme, which evolved into the Interoperable Europe initiative."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: EU-DCAT-AP
    source: interpretation
    evidence: "Confirmed by reading interoperable-europe.ec.europa.eu's own DCAT-AP releases page and github.com/SEMICeu/DCAT-AP directly (2026-08-28): DCAT-AP is published through the SEMIC Support Centre, whose GitHub repository serves as the specification's official issue tracker. Direction expressed SEMIC→DCAT-AP for navigability; the authoritative framing belongs on the DCAT-AP entity."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SEMIC Support Centre — DCAT-AP"
    url: "https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/releases"
    publisher: "European Commission — Interoperable Europe Portal"
    accessed: "2026-08-28"
  - title: "SEMICeu/DCAT-AP — issue tracker for the maintenance of DCAT-AP"
    url: "https://github.com/SEMICeu/DCAT-AP"
    publisher: "SEMIC (European Commission)"
    accessed: "2026-08-28"
  - title: "Glossary — SEMIC"
    url: "https://interoperable-europe.ec.europa.eu/collection/portal/glossary/term/semic"
    publisher: "European Commission — Interoperable Europe Portal"
    accessed: "2026-08-28"
---

# SEMIC

> **Re-verified 2026-08-28.** Both originally cited pages were read
> directly — the Interoperable Europe Portal's DCAT-AP releases page and
> the SEMICeu/DCAT-AP GitHub repository — and a third, stronger source was
> added: the Portal's own glossary entry for SEMIC, which gives the
> clearest primary statement of what SEMIC is. `verification` promoted
> `search-only` → `primary-source`.

## Description

Confirmed by reading interoperable-europe.ec.europa.eu's own glossary
directly (2026-08-28): "The Semantic Interoperability Community (SEMIC)
develops solutions to help European public administrations perform
seamless and meaningful cross-border and cross-domain data exchanges."
SEMIC began under the former ISA/ISA² Programme and now operates within
Interoperable Europe. It maintains [[EU-DCAT-AP]] — openly, with the
specification and its issue tracker on GitHub, both confirmed by reading
the DCAT-AP releases page and the SEMICeu/DCAT-AP repository directly — and
runs the SEMIC Support Centre, which the releases page describes as the
current publisher of DCAT-AP versions.

Its position matters structurally: semantic interoperability is one of the
layers of [[EU-EIF]], and SEMIC is where that layer is actually operated
rather than described. No relationship to the EIF is asserted, because the
sources read this pass do not state one.

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

Listed in frontmatter, all three read directly this pass (2026-08-28).
