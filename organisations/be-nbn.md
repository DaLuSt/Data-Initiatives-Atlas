---
id: BE-NBN
type: organisation
name: Bureau de Normalisation / Bureau voor Normalisatie
alternative_names:
  - NBN
  - Bureau de Normalisation
  - Bureau voor Normalisatie
  - Belgian standards body
description: >
  The national standardization body of Belgium, and therefore its national
  member of CEN and its national committee in CENELEC. The national bodies
  operate the technical groups that draw up European Standards, coordinated
  by the CEN-CENELEC Management Centre in Brussels.

level: national
country: BE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-CEN
  - EU-CENELEC
relationships:
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "Confirmed by reading standards.cencenelec.eu's member list directly (2026-08-26): NBN (Bureau de Normalisation/Bureau voor Normalisatie), website www.nbn.be, is explicitly listed as one of CEN's National Members. cencenelec.eu's general page, also read, confirms National Members are the National Standardization Bodies of the EU, UK, North Macedonia, Serbia and Türkiye, plus Iceland, Norway and Switzerland, operating the technical groups that draw up European Standards."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "Confirmed only at the general level this pass: cencenelec.eu's page, read directly, states CENELEC's National Members are the National Committees of the same country set as CEN. The specific member list fetched (standards.cencenelec.eu) confirmed NBN by name for CEN but did not return the corresponding CENELEC list, so NBN's own CENELEC membership rests on the general statement rather than a name-checked list."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "European Standards"
    url: "https://www.cencenelec.eu/european-standardization/european-standards/"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
  - title: "CEN Community — List of members"
    url: "https://standards.cencenelec.eu/ords/f?p=CEN:5"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
  - title: "NBN — Bureau de Normalisation"
    url: "https://www.nbn.be/"
    publisher: "NBN"
---

# Bureau de Normalisation / Bureau voor Normalisatie (NBN)

> **Verified 2026-08-26.** Two of three sources were read directly.
> `nbn.be` itself could not be verified as safe to fetch by the tooling
> used this pass. The CEN member list names NBN explicitly; CENELEC
> membership rests on the general cross-membership statement rather than a
> name-checked list. `verification: primary-source`. ⚠ `coverage: low`.

## Description

NBN is the national standardization body of Belgium, confirmed by name in
CEN's own current member list.

## Belgium's standards body, and what it is not

NBN is Belgium's national standardization body and therefore its CEN member
and CENELEC national committee.

**No `participates-in` [[INTL-ISO]] edge is asserted.** The CEN-CENELEC
sources establish European membership and say nothing about ISO. [[DE-DIN]]
and [[GB-BSI]] carry ISO edges because their own sources state it; NBN's do
not, and the two memberships are not the same fact.

## Not modelled

- Any **standard** NBN maintains. That is now true of **seven** national
  standards bodies in the Atlas — [[DE-DIN]], [[NL-NEN]], [[GB-BSI]],
  [[IE-NSAI]] and the three others added with this one — none of which
  maintains a single document the Atlas holds. The exception is
  [[INTL-IDS-RAM]], which reaches [[DE-DIN]] from the other direction.
- NBN's **relationship to [[EU-ETSI]]**, which only [[GB-BSI]] carries.

## Relationships

- `participates-in` [[EU-CEN]] — confirmed by name in CEN's member list.
- `participates-in` [[EU-CENELEC]] — confirmed only at the general
  cross-membership level, not by a name-checked CENELEC list.

## Sources

Two of three read directly this pass — the general CEN-CENELEC standards
page and the CEN member list, which names NBN. `nbn.be` itself was not
reachable this pass.
