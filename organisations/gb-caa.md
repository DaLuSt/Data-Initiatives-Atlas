---
id: GB-CAA
type: organisation
name: Civil Aviation Authority
alternative_names:
  - CAA
  - UK Civil Aviation Authority
description: >
  The United Kingdom's aviation regulator: a body corporate that section 2 of
  the Civil Aviation Act 1982 provides shall continue to exist. Schedule 1 to
  the Network and Information Systems Regulations 2018 names it, acting jointly
  with the Secretary of State for Transport, as competent authority for air
  transport across the United Kingdom.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-08"
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - GB-NIS-REGULATIONS
  - GB-OFCOM
  - GB-NCSC
relationships:
  - type: applies-to
    target: GB-NIS-REGULATIONS
    source: fact
    evidence: "Confirmed by reading legislation.gov.uk's Schedule 1 directly (2026-10-08): Transport, Air Transport - 'The Secretary of State for Transport and The Civil Aviation Authority (acting jointly)', territory United Kingdom. The Authority is a joint, not sole, competent authority."
    confidence: medium
    valid_from: 2018-05-10
    valid_until: null

sources:
  - title: "The Network and Information Systems Regulations 2018, Schedule 1"
    url: "https://www.legislation.gov.uk/uksi/2018/506/schedule/1"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-10-08"
  - title: "Civil Aviation Act 1982, section 2: Constitution of CAA"
    url: "https://www.legislation.gov.uk/ukpga/1982/16/section/2"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-10-08"
  - title: "About us - Civil Aviation Authority"
    url: "https://www.caa.co.uk/about-us/"
    publisher: "Civil Aviation Authority"
    accessed: "2026-10-08"
---

# Civil Aviation Authority (CAA)

> **Verified 2026-10-08.** Schedule 1 to the NIS Regulations 2018 and section 2
> of the Civil Aviation Act 1982 were read directly at legislation.gov.uk.
> The CAA's About page was read directly.

## Description

Section 2(1) of the **Civil Aviation Act 1982** provides: "There shall continue
to be a body corporate called the Civil Aviation Authority". Subsection (4) says
the CAA is not to be regarded as "the servant or agent of the Crown". The CAA's
own About page describes its roles as "protecting people and enabling
aerospace, from safety and security to passenger rights".

Under [[GB-NIS-REGULATIONS]] Schedule 1 it is a **joint competent authority**
with the Secretary of State for Transport for air transport, for the whole
United Kingdom.

## Not asserted

- Any cyber-security function beyond what Schedule 1 names: the CAA's About
  page, read directly, mentions neither the NIS Regulations nor cyber security.
- A start date: section 2 says the body "shall continue", so the 1982 Act is not
  its founding.
- The Secretary of State's own role, a ministerial office.

## Relationships

- `applies-to` [[GB-NIS-REGULATIONS]], valid from 10 May 2018.

