---
id: IN-DPB
type: organisation
name: "Data Protection Board of India"
alternative_names:
  - "DPB"
  - "Board"
description: >
  The independent body that the Digital Personal Data Protection Act 2023 creates to oversee compliance, inquire into
  breaches and ensure corrective measures. The DPDP Rules 2025 make it a fully digital Board of four members with an
  online complaint portal and mobile application; its decisions are appealed to the Telecom Disputes Settlement and
  Appellate Tribunal (TDSAT). Whether it has been constituted was not found.

level: national
country: IN
region: null

status: planned
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
organisations: []
related_entities:
  - IN
  - IN-DPDP-ACT-2023
  - IN-DPDP-RULES-2025
relationships:
  - type: part-of
    target: IN
    source: fact
    evidence: "The Press Information Bureau's explainer of 17 November 2025 (read directly 2026-11-01) presents the Board as a body of the Government of India's data protection framework."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: IN-DPDP-ACT-2023
    source: fact
    evidence: "The Press Information Bureau's explainer of 17 November 2025 (read directly 2026-11-01): 'A central feature of the Act is the creation of the Data Protection Board of India.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: IN-DPDP-RULES-2025
    source: fact
    evidence: "The Press Information Bureau's explainer of 17 November 2025 (read directly 2026-11-01): 'The Rules establish a fully digital Data Protection Board of India, which will consist of four members.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "DPDP Rules, 2025 Notified: A Citizen-Centric Framework for Privacy Protection and Responsible Data Use (17 November 2025)"
    url: "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf"
    publisher: "Press Information Bureau, Government of India"
    accessed: "2026-11-01"
---

# Data Protection Board of India

> **Created 2026-11-01** (roadmap #470). Known **only** from the PIB's explainer; **whether the Board has been constituted, who its members are and where it sits were not found**, so `status: planned` and no date is recorded. `part-of` India is medium confidence for the same reason.

## What is sourced

"The Board functions as an independent body that oversees compliance, inquires into breaches and ensures that corrective measures are taken. It plays a key role in enforcing the rights granted under the Act." Under the Rules it is "fully digital", has "four members", and complaints can be filed online and tracked "through a dedicated portal and mobile application". Appeals go to TDSAT, "the Appellate Tribunal".

## Relationships

`part-of` India (medium); `governed-by` [[IN-DPDP-ACT-2023]] and [[IN-DPDP-RULES-2025]].

## Sources

Listed in frontmatter, read directly.
