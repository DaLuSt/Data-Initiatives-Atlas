---
id: SZ-SZCIRT
type: organisation
name: "Eswatini National Computer Incident Response Team (SzCIRT)"
alternative_names:
  - "SzCIRT"
  - "Eswatini National CIRT"
description: >
  The computer incident response team for Eswatini, a focal point for coordinating cybersecurity incidents for government
  departments, internet service providers and other relevant entities. It monitors incidents, provides early warnings,
  disseminates information and enforces cybersecurity standards and minimum specifications. Its site (ncsirt.org.sz) is linked
  from the Eswatini Communications Commission's menu under Cybersecurity.

level: national
country: SZ
region: null

status: active
organisation_role: executive
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
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - SZ
  - SZ-ESCCOM
relationships:
  - type: part-of
    target: SZ
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The CIRT's Who We Are text (read directly 2026-11-01): 'SzCIRT is the Computer Incident Response Team (CIRT) for Eswatini and acts as a focal point in coordinating cybersecurity incidents for the Government Departments, Internet Service Providers, and other relevant entities within the country.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: SZ-ESCCOM
    source: fact
    evidence: "The Commission's site menu (read directly 2026-11-01) lists 'Cybersecurity' linking to ncsirt.org.sz; the CIRT's hotline is the Commission's number (+268 2406 7000). Which body hosts the team was not read, so the edge is `related-to`."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Eswatini National CIRT — home page"
    url: "https://www.ncsirt.org.sz/"
    publisher: "Eswatini National CIRT"
    accessed: "2026-11-01"
---

# Eswatini National Computer Incident Response Team (SzCIRT)

> **Created 2026-11-01** (roadmap #478). One page read directly; `start_date` and the legal basis were not found.

## Relationships

Part of [[SZ]]; related to [[SZ-ESCCOM]].
