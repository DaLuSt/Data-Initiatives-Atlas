---
id: KI-DTO
type: organisation
name: "Digital Transformation Office (Kiribati)"
alternative_names:
  - "DTO"
description: >
  The Kiribati office established under the Digital Government Act 2023. The Data Protection Act 2025 makes it 'the Office' that
  promotes the protection of personal data, oversees the Act's implementation and is responsible for its enforcement throughout Kiribati,
  and the Cybersecurity Act 2026 refers to it (as the DTO) for coordination by operators of critical infrastructure. Known only through those two Acts.

level: national
country: KI
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
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - KI
  - KI-DPA-2025
  - KI-CYBERSECURITY-ACT-2026
  - KI-DIGITAL-GOVERNMENT-ACT-2023
relationships:
  - type: part-of
    target: KI
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Data Protection Act 2025 (read as text 2026-11-01), section 3: 'Office' means the Digital Transformation Office established under the Digital Government Act 2023; section 8: the Office shall promote the protection of personal data, oversee the implementation of this Act and be responsible for its enforcement throughout Kiribati."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: KI-DIGITAL-GOVERNMENT-ACT-2023
    source: fact
    evidence: "The Data Protection Act 2025, section 3 (read 2026-11-01): the Office is 'established under the Digital Government Act 2023'. That Act was not read."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Data Protection Act 2025 (PDF)"
    url: "https://www.mict.gov.ki/sites/default/files/publications/Data%20Protection%20Act%202025.pdf"
    publisher: "Ministry of Information, Communication and Transport (MICT), Kiribati"
    accessed: "2026-11-01"
  - title: "Cybersecurity Act 2026 (PDF)"
    url: "https://www.mict.gov.ki/sites/default/files/publications/Kiribati_Cybersecurity_Act_2026.pdf"
    publisher: "Ministry of Information, Communication and Transport (MICT), Kiribati"
    accessed: "2026-11-01"
---

# Digital Transformation Office (Kiribati)

> **Created 2026-11-01** (roadmap #477, country group 8, Kiribati). Known only from the two Acts' provisions; its own pages, head and the Digital Government Act 2023 were not read. `start_date` is empty. The Data Protection Act's own administration clause (section 4) puts the Act under the direction of the Secretary of the Ministry, while section 8 gives the Office the mandate; how the two fit was not resolved.

## Relationships

Part of [[KI]]; established under [[KI-DIGITAL-GOVERNMENT-ACT-2023]]; enforces [[KI-DPA-2025]].
