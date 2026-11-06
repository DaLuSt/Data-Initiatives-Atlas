---
id: LS-LCA
type: organisation
name: "Lesotho Communications Authority (LCA)"
alternative_names:
  - "LCA"
description: >
  Lesotho's communications regulator. Its site calls it 'a statutory body, established in June 2000' that regulates the communications sector, including granting licences to operators and promoting fair competition.
  Its Legislation page lists the Communications Act 2012 as the principal legislation, with subsidiary rules (licensing classification and fees rules 2023 and 2025, quality of service rules 2023, broadcasting code 2022, universal access fund rules 2009 and others) and links to a Cyber Security section and the COMCSIRT site; no data protection or cybercrime instrument is listed there.

level: national
country: LS
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
  - LS
  - LS-COMMUNICATIONS-ACT-2012
relationships:
  - type: part-of
    target: LS
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The LCA's home page (read 2026-11-01 through a summarising fetch tool): a statutory body, established in June 2000, regulating Lesotho's communications sector."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: LS-COMMUNICATIONS-ACT-2012
    source: fact
    evidence: "The LCA's Legislation page: the Communications Act 2012 is listed as its principal legislation, with the subsidiary rules made under it."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Lesotho Communications Authority, home page"
    url: "https://www.lca.org.ls"
    publisher: "Lesotho Communications Authority"
    accessed: "2026-11-01"
  - title: "Lesotho Communications Authority, Legislation"
    url: "https://lca.org.ls/legislation/"
    publisher: "Lesotho Communications Authority"
    accessed: "2026-11-01"
---

# Lesotho Communications Authority (LCA)

> **Created 2026-11-06** (roadmap #481). From the regulator's own pages through a summarising fetch tool. `start_date` empty: the site gives 'June 2000' only.

## Relationships

Part of [[LS]]; governed by [[LS-COMMUNICATIONS-ACT-2012]].
