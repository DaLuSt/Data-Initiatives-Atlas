---
id: GB-DWQR
type: organisation
name: Drinking Water Quality Regulator for Scotland
alternative_names:
  - DWQR
  - Scottish Drinking Water Quality Regulator
description: >
  Scotland's drinking water quality regulator, a role created by section 7 of
  the Water Industry (Scotland) Act 2002 according to the regulator's own
  website. Schedule 1 to the Network and Information Systems Regulations 2018
  names it as competent authority for drinking water supply and distribution
  in Scotland.

level: subnational
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
  - DOMAIN-WATER
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
    evidence: "Confirmed by reading legislation.gov.uk's Schedule 1 directly (2026-10-08): Drinking water supply and distribution, Scotland - 'The Drinking Water Quality Regulator for Scotland'. Sole competent authority for Scotland; England, Wales and Northern Ireland are assigned elsewhere in the Schedule."
    confidence: medium
    valid_from: 2018-05-10
    valid_until: null

sources:
  - title: "The Network and Information Systems Regulations 2018, Schedule 1"
    url: "https://www.legislation.gov.uk/uksi/2018/506/schedule/1"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-10-08"
  - title: "About us - Drinking Water Quality Regulator for Scotland"
    url: "https://dwqr.scot/about-us/"
    publisher: "Drinking Water Quality Regulator for Scotland"
    accessed: "2026-10-08"
---

# Drinking Water Quality Regulator for Scotland (DWQR)

> **Verified 2026-10-08.** Schedule 1 to the NIS Regulations 2018 was read
> directly at legislation.gov.uk. The regulator's About page was read directly.

## Description

The regulator's own About page says it "exists to ensure that drinking water in
Scotland is safe to drink", that it "acts independently of Ministers", and cites
section 7 of the Water Industry (Scotland) Act 2002 as having "created the role
of Drinking Water Quality Regulator". The page also says the Regulator is
assisted by a team within the Drinking Water Quality Division of the Scottish
Government. `level: subnational`, since its remit is Scotland.

Under [[GB-NIS-REGULATIONS]] Schedule 1 it is the competent authority for
drinking water supply and distribution in Scotland.

## Not asserted

- The text of section 7 of the 2002 Act, which was not read: the statutory basis
  is the regulator's own account.
- Any cyber-security function: the About page mentions neither the NIS
  Regulations nor cyber security.
- The English, Welsh and Northern Irish authorities for drinking water, which
  Schedule 1 gives to ministers and a department.

## Relationships

- `applies-to` [[GB-NIS-REGULATIONS]], valid from 10 May 2018.

