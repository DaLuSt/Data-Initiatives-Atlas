---
id: SZ-ESCCOM
type: organisation
name: "Eswatini Communications Commission (ESCCOM)"
alternative_names:
  - "ESCCOM"
  - "Swaziland Communications Commission"
  - "Eswatini Data Protection Authority (EDPA)"
description: >
  Eswatini's regulator of the communications sector (telecommunications services and networks, broadcasting, postal services and the use
  and allocation of radio spectrum), which derives its mandate from the Swaziland Communications Commission Act no. 10 of 2013 and became
  operational on 31 July 2013, taking over regulatory powers from the Eswatini Posts and Telecommunications Corporation and Eswatini
  Television Authority. The Data Protection Act, 2022 designates it as the national Data Protection Authority (the Eswatini Data
  Protection Authority, EDPA), with registration of controllers and processors, breach reporting, complaints and enforcement decisions.

level: national
country: SZ
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: 2013-07-31
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - SZ
  - SZ-DPA-2022
relationships:
  - type: part-of
    target: SZ
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. ESCCOM's About page (read directly 2026-11-01): 'The regulatory body responsible for regulating the communications sector in Eswatini'; 'It derives its mandate from the Swaziland Communications Commission Act no. 10 of 2013. The Commission became operational on the 31st July 2013'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: SZ-DPA-2022
    source: fact
    evidence: "The EDPA home page (read directly 2026-11-01): 'The Act designates the Eswatini Communications Commission as the National Data Protection Authority (EDPA) to regulate how personal information is handled, investigate breaches ... and resolve any complaints'."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "About the ESCCOM — Eswatini Communications Commission"
    url: "https://esccom.org.sz/about/"
    publisher: "Eswatini Communications Commission (ESCCOM)"
    accessed: "2026-11-01"
  - title: "Eswatini Data Protection Authority — home page"
    url: "https://www.edpa.org.sz/"
    publisher: "Eswatini Communications Commission (ESCCOM)"
    accessed: "2026-11-01"
---

# Eswatini Communications Commission (ESCCOM)

> **Created 2026-11-01** (roadmap #478, country group 9, Eswatini). The Commission's About page and its data protection and cybersecurity sites read directly. `start_date` is the date it became operational (31 July 2013), as its page gives it. The Acts' texts were not read: the Data Protection Act PDF resets the connection and its old address on esccom.org.sz returns 404.

## Relationships

Part of [[SZ]]; the Data Protection Authority under [[SZ-DPA-2022]]; established under [[SZ-ESCCOM-ACT-2013]]; runs [[SZ-SZCIRT]].
