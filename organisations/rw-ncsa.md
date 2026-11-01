---
id: RW-NCSA
type: organisation
name: "National Cyber Security Authority (Rwanda)"
alternative_names:
  - "NCSA"
  - "Rwanda NCSA"
description: >
  Rwanda's authority for cybersecurity, whose mission is to build the skills and capabilities needed to secure Rwanda's cyberspace
  for economic and social development. Its site lists four areas: cyber defence and resilience (the RW-CSIRT, 24/7), cybersecurity
  standards and policies, data protection and privacy (it says it enforces the Law on Personal Data Protection and Privacy, with a
  DPO unit and compliance tools on a separate site), and cybersecurity coordination. It publishes minimum cybersecurity standards for
  essential service providers, an information security policy template and application software security directives.

level: national
country: RW
region: null

status: active
organisation_role: regulatory
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
  - RW
  - RW-LAW-058-2021
relationships:
  - type: part-of
    target: RW
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Authority's home page (read directly 2026-11-01): 'The mission of the National Cyber Security Authority (NCSA) is to build skills and capabilities necessary to secure Rwanda's cyberspace in order to sustain economic and social development.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: RW-LAW-058-2021
    source: fact
    evidence: "The same page, under 'Data Protection and Privacy': 'Enforce Rwanda's Law on Personal Data Protection and Privacy'; the Law's definition of 'supervisory authority' is 'a public authority in charge of cyber security'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "National Cyber Security Authority — home page"
    url: "https://cyber.gov.rw/home/"
    publisher: "National Cyber Security Authority (NCSA), Rwanda"
    accessed: "2026-11-01"
  - title: "Law relating to the protection of personal data and privacy, Official Gazette n° Special of 15/10/2021"
    url: "https://cyber.gov.rw/fileadmin/Cyber/Documents/OG_Special_of_15.10.2021_Amakuru_bwite.pdf"
    publisher: "National Cyber Security Authority (NCSA), Rwanda"
    accessed: "2026-11-01"
---

# National Cyber Security Authority (Rwanda)

> **Created 2026-11-01** (roadmap #479). The Authority's home page read directly. `start_date` is empty: the page gives no founding date or instrument. The data protection office (`dpo.gov.rw`) and the standards documents were not opened.

## Relationships

Part of [[RW]]; enforces [[RW-LAW-058-2021]].
