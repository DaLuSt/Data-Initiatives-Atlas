---
id: NL-WBNI
type: law
name: Wet beveiliging netwerk- en informatiesystemen
alternative_names:
  - Wbni
description: >
  Dutch act on the security of network and information systems, implementing
  the original EU NIS Directive. Due to be withdrawn and replaced by the
  Cyberbeveiligingswet, which implements NIS2.

level: national
country: NL
region: EU

status: active
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: 2026-08-15
last_verified: null
previous_version: null
successor: NL-CBW

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-CBW
  - EU-NIS
relationships:
  - type: implements-requirement-from
    target: EU-NIS
    source: fact
    evidence: "The Wbni is the Dutch act on security of network and information systems implementing the original EU NIS regime; NIS2 (which the Cyberbeveiligingswet implements) repealed Directive (EU) 2016/1148. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Cyberbeveiligingswet (NIS2)"
    url: "https://www.ncsc.nl/cyberbeveiligingswet-nis2"
    publisher: "Nationaal Cyber Security Centrum (NCSC)"
  - title: "Cyberbeveiligingswet"
    url: "https://www.nctv.nl/onderwerpen/c/cyberbeveiligingswet"
    publisher: "Nationaal Coördinator Terrorismebestrijding en Veiligheid (NCTV)"
---

# Wet beveiliging netwerk- en informatiesystemen (Wbni)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Wbni is the Dutch act on the security of network and information
systems. It is the predecessor regime to [[NL-CBW]]: organisations covered
by the Wbni keep their rights and obligations under it until the
Cyberbeveiligingswet enters into force, at which point the Wbni is
withdrawn.

`coverage: low` deliberately. This entity exists chiefly to make the
supersession chain expressible — a superseded instrument must be retained,
not deleted, for the Atlas to reconstruct the landscape at a past point in
time (brief §11). Its own content, commencement date and relationship to the
original NIS Directive have not been researched; the original NIS Directive
is not yet an Atlas entity.

`status: active` with `end_date: 2026-08-15` records that, as at the date of
writing, the Wbni is still the operative regime and is scheduled to end.
Once the Cbw commences, `status` should become `superseded`.

## Relationships

- Superseded by [[NL-CBW]] (recorded on that entity, with `successor` set
  here).

## Sources

Listed in frontmatter.
