---
id: INTL-SIECA
type: organisation
name: "Secretariat for Central American Economic Integration (SIECA)"
alternative_names:
  - "SIECA"
  - "Secretaría de Integración Económica Centroamericana"
description: >
  The technical and administrative organ of the Central American economic integration process, with legal personality under
  international law and functional autonomy, which links the secretariats of the economic subsystem and coordinates with the
  General Secretariat of the Central American Integration System (SICA). It hosts and manages the Central American Digital Trade
  Platform (PDCC), and publishes statistics through an economic intelligence observatory.

level: regional
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - INTL-PDCC
  - INTL-COMTELCA
relationships:
  - type: related-to
    target: INTL-COMTELCA
    source: fact
    evidence: "SIECA's home page (read directly 2026-11-01) describes SIECA as coordinating with the General Secretariat of SICA; COMTELCA's page calls COMTELCA a specialised body of the same system. The edge records membership of one system, not a direct tie between the two."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Secretaría de Integración Económica Centroamericana — home page"
    url: "https://www.sieca.int/"
    publisher: "Secretaría de Integración Económica Centroamericana (SIECA)"
    accessed: "2026-11-01"
---

# SIECA

> **Created 2026-11-01** (roadmap #546). The home page and the PDCC page of SIECA's own site read directly. Its founding date, member states, the Guatemala Protocol and its statistics observatory were not read, so no country edge exists. The edge to [[INTL-COMTELCA]] is `low` confidence for the reason in its evidence.

## Relationships

Hosts [[INTL-PDCC]]; same integration system as [[INTL-COMTELCA]].
