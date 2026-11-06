---
id: VE-CONATEL
type: organisation
name: "National Telecommunications Commission (CONATEL, Venezuela)"
alternative_names:
  - "CONATEL"
  - "Comisión Nacional de Telecomunicaciones"
description: >
  Venezuela's telecommunications regulator ('ente regulador'). Its site covers spectrum management, universal service, user protection, operator authorisation ('habilitación'), the .ve domain registry (NIC.VE) and public consultations, and publishes the National Telecommunications Plan 2025-2031 and the National IPv6 Plan 2025.
  Its Marco Legal page cites article 37(1) of the Ley Orgánica de Telecomunicaciones as its competence to issue the telecommunications norms and plans. Its own establishment date and instrument were not read.

level: national
country: VE
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
  - VE
  - VE-LOTEL
relationships:
  - type: part-of
    target: VE
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. CONATEL's home page and Marco Legal page (read 2026-11-06 through a summarising fetch tool): the regulator ('ente regulador'), competent under article 37 of the LOTEL."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: VE-LOTEL
    source: fact
    evidence: "CONATEL's Marco Legal page: article 37, numeral 1 of the Ley Orgánica de Telecomunicaciones (LOTEL) gives it competence to issue telecommunications norms and plans."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "CONATEL (Comisión Nacional de Telecomunicaciones), home page"
    url: "https://conatel.gob.ve/"
    publisher: "CONATEL, Venezuela"
    accessed: "2026-11-01"
  - title: "CONATEL, Leyes (Marco Legal)"
    url: "https://conatel.gob.ve/leyes/"
    publisher: "CONATEL, Venezuela"
    accessed: "2026-11-01"
---

# National Telecommunications Commission (CONATEL)

> **Created 2026-11-06** (roadmap #481). From the regulator's own pages through a summarising fetch tool. `start_date` empty: no establishment instrument was read.

## Relationships

Part of [[VE]]; governed by [[VE-LOTEL]]; the Info-Government and cybercrime laws it lists are recorded in `discovery/unresolved/other.md` row 249, not modelled.
