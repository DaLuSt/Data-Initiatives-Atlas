---
id: GH-NITA
type: organisation
name: "National Information Technology Agency"
alternative_names:
  - "NITA"
  - "NITA Ghana"
description: >
  Ghana's regulator for and main implementer of e-government: established by an Act of Parliament (Act 771) in December 2008,
  succeeding the Ghana ICT Directorate, to regulate, coordinate and promote ICT and digital services, set standards for government ICT,
  run the national ICT backbone and state data centres, license and certify ICT providers and professionals, and secure government
  digital assets.

level: national
country: GH
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - GH
  - GH-ACT-771
  - GH-DPI
  - GH-GOVCERT
relationships:
  - type: part-of
    target: GH
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. NITA's About page (read 2026-10-16): 'the vital regulatory body and the primary implementer of the Government of Ghana's e-Government strategy'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: GH-ACT-771
    source: fact
    evidence: "The same page (read 2026-10-16): 'NITA was established by an Act of Parliament of Ghana (Act 771) in December 2008. NITA succeeded the Ghana ICT Directorate (GICTeD)'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "About NITA"
    url: "https://www.nita.gov.gh/about"
    publisher: "National Information Technology Agency (Ghana)"
    accessed: "2026-10-16"
  - title: "Functions and Responsibilities — NITA"
    url: "https://www.nita.gov.gh/about/functions-responsibilities"
    publisher: "National Information Technology Agency (Ghana)"
    accessed: "2026-10-16"
---

# National Information Technology Agency (Ghana)

> **Created 2026-10-16** (roadmap #481, Ghana). Read on NITA's own site. No `start_date`: the page says "December 2008" for the Act that established it, which is a month, not a date.

## What the pages say

Mandate: "to regulate, coordinate, and promote Ghana's ICT and digital services sector". Four areas on the About page: regulation and standards for government ICT (interoperability, security, efficiency), infrastructure (the National ICT Backbone and state data centres), cybersecurity of government digital assets and public data, and capacity building and advice to government on ICT policy. Its functions page lists regulatory enforcement, monitoring and compliance, IT standards, certification, enterprise architecture, a Security Operations Centre across ministries, departments and agencies, and shared infrastructure. Its "ICT Regulations" page holds NITA's standards (LAN/WAN cabling, IT governance, data centre, records), policies, and acts and bills. Also on its site: a data privacy policy statement and information security policy statement (not read), the Right to Information manual, and digital services including a digital ID, an interoperability bus, PKI and a government cloud.

## Relationships

Part of [[GH]]; `governed-by` [[GH-ACT-771]]; runs [[GH-DPI]] and [[GH-GOVCERT]].
