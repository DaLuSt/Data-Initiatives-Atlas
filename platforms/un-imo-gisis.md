---
id: UN-IMO-GISIS
type: platform
name: Global Integrated Shipping Information System
alternative_names:
  - GISIS
description: >
  IMO's centralised repository for maritime information, providing 30+
  specialised modules covering vessel and company data, safety and
  security, environmental compliance, port and cargo operations, treaty
  ratification and certification status, and emergency response. Allows
  member states, maritime authorities, ship operators and the public to
  access standardised international maritime information supplied to the
  IMO Secretariat by maritime administrations and port authorities.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - UN-IMO
related_entities:
  - UN-IMO
relationships:
  - type: maintained-by
    target: UN-IMO
    source: fact
    evidence: "Confirmed by reading gisis.imo.org's own page directly (2026-09-05): 'The IMO (International Maritime Organization), a United Nations specialized agency, operates and maintains GISIS.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Global Integrated Shipping Information System (GISIS)"
    url: "https://gisis.imo.org/Public/Default.aspx"
    publisher: "International Maritime Organization"
    accessed: "2026-09-05"
---

# Global Integrated Shipping Information System (GISIS)

> **Added 2026-09-05, `verification: primary-source` from creation.**
> Companion entity to [[UN-IMO]], created the same pass. Closes the
> `discovery/candidates.md` lead on "IMO, GISIS and the SafeSeaNet
> codes."

## Description

Reading `gisis.imo.org`'s own page directly: GISIS is IMO's "comprehensive
database" and centralised repository for maritime information, providing
**30+ specialised modules** — vessel and company data (searchable by IMO
number), safety and security, environmental compliance (ballast water,
fuel-consumption reporting), port and cargo operations, treaty
ratification/certification status, and emergency response (search and
rescue, incident reporting, piracy).

## Relationship to UN/LOCODE and SafeSeaNet

`discovery/candidates.md` had flagged that [[EU-EMSWE]]'s common location
database holds [[UN-LOCODE]] **alongside** the SafeSeaNet codes and IMO
port-facility codes registered in GISIS. That observation is preserved on
[[UN-IMO]]'s own file rather than repeated here as a relationship, since
no source read this pass states a direct edge between GISIS and either
UN/LOCODE or SafeSeaNet.

## Relationships

- `maintained-by` [[UN-IMO]].

## Sources

Listed in frontmatter, read directly this pass.
