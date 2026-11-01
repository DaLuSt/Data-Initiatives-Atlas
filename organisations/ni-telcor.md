---
id: NI-TELCOR
type: organisation
name: "Nicaraguan Institute of Telecommunications and Post (TELCOR)"
alternative_names:
  - "TELCOR"
  - "Instituto Nicaragüense de Telecomunicaciones y Correos"
description: >
  Nicaragua's state 'regulatory authority' for telecommunications and postal services, responsible for the standard-setting, regulation,
  technical planning, supervision and enforcement of the laws and rules governing the installation, interconnection, operation and
  provision of those services, and for administering the radio spectrum and granting the enabling titles. Its site lists as its legal
  framework Law 1223 (General Law on Converging Telecommunications), Decree-Law 1053 (its organic law) and consumer and competition laws.

level: national
country: NI
region: null

status: active
organisation_role: regulatory
confidence: high
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
  - NI
  - NI-LEY-1223
relationships:
  - type: part-of
    target: NI
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. TELCOR's ¿Quienes Somos? page (read directly 2026-11-01, Spanish): 'El Instituto Nicaragüense de Telecomunicaciones y Correos (TELCOR) es la «Autoridad Reguladora» de los servicios de telecomunicaciones y servicios postales, una institución estatal'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NI-LEY-1223
    source: fact
    evidence: "TELCOR's Marco Legal page (read directly 2026-11-01) lists 'LEY NÚMERO 1223 – LEY GENERAL DE TELECOMUNICACIONES CONVERGENTES' first among the laws, beside 'DECRETO LEY 1053 LEY ORGANICA DE TELCOR'; the relation between them was not read."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "¿Quienes Somos? — TELCOR"
    url: "https://www.telcor.gob.ni/quienes-somos/"
    publisher: "Instituto Nicaragüense de Telecomunicaciones y Correos (TELCOR)"
    accessed: "2026-11-01"
  - title: "Marco Legal — TELCOR"
    url: "https://www.telcor.gob.ni/institucional/marco-legal/"
    publisher: "Instituto Nicaragüense de Telecomunicaciones y Correos (TELCOR)"
    accessed: "2026-11-01"
---

# Nicaraguan Institute of Telecommunications and Post (TELCOR)

> **Created 2026-11-01** (roadmap #475, country group 6, Nicaragua). Two pages of TELCOR's own Spanish site read directly. English wording is this session's rendering. `start_date` is empty. The organic law (Decree-Law 1053) and the other listed laws were not opened; only Law 1223 is modelled, as the sector's general law.

## Relationships

Part of [[NI]]; its legal framework starts with [[NI-LEY-1223]].
