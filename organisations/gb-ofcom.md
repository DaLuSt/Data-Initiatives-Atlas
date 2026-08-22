---
id: GB-OFCOM
type: organisation
name: Ofcom
alternative_names:
  - Office of Communications
description: >
  United Kingdom regulator for communications, named in Schedule 1 to the
  Network and Information Systems Regulations 2018 as the competent
  authority for digital infrastructure. It is one of several sectoral
  competent authorities under those Regulations, which take a
  sector-by-sector approach rather than appointing a single central
  authority.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - GB-NIS-REGULATIONS
  - GB-NCSC
  - GB-ICO
relationships:
  - type: applies-to
    target: GB-NIS-REGULATIONS
    source: fact
    evidence: "Confirmed by reading the statute text at legislation.gov.uk (2026-08-22), Schedule 1: 'Digital Infrastructure — Digital Infrastructure — Office of Communications (United Kingdom).' Ofcom is designated by its full statutory name as the sole competent authority for the digital-infrastructure subsector."
    confidence: medium
    valid_from: 2018-05-10
    valid_until: null

sources:
  - title: "The Network and Information Systems Regulations 2018"
    url: "https://www.legislation.gov.uk/uksi/2018/506"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-08-22"
  - title: "The Network and Information Systems Regulations 2018: how will they apply in practice?"
    url: "https://www.osborneclarke.com/insights/the-network-and-information-systems-regulations-2018-how-will-they-apply-in-practice"
    publisher: "Osborne Clarke"
    accessed: "2026-08-22"
  - title: "UK NIS Regulations 2018: scope, duties and enforcement"
    url: "https://www.lexisnexis.com/en-gb/legal/guidance/the-network-information-systems-regulations-2018"
    publisher: "LexisNexis UK"
    accessed: "2026-08-22"
---

# Ofcom

> **Verified 2026-08-22.** The NIS Regulations 2018 statute text at
> legislation.gov.uk was read directly, confirming Schedule 1's exact
> wording for Ofcom's designation.

## Description

Confirmed verbatim in Schedule 1 of the NIS Regulations 2018, read directly
at legislation.gov.uk (2026-08-22): "Digital Infrastructure — Office of
Communications (United Kingdom)." Ofcom is the UK communications regulator, and within this Atlas's scope it is
the **competent authority for digital infrastructure** under
[[GB-NIS-REGULATIONS]] Schedule 1.

## The point of adding it: the UK's cyber regulation has no single centre

[[GB-NCSC]] records that the UK is the only country in
[[DOMAIN-CYBERSECURITY]] whose national cyber authority is **explicitly not**
the regulator. That claim was made with only one of the actual regulators
modelled — [[GB-ICO]], for digital service providers. Ofcom is the second,
and with two of them present the distributed arrangement is visible in the
graph rather than only in prose:

```
        GB-NIS-REGULATIONS
          ▲              ▲
   applies-to        applies-to
          │              │
      GB-ICO         GB-OFCOM          GB-NCSC — coordinates, regulates nothing
 (digital service   (digital
   providers)      infrastructure)
```

**Both regulators reach the same instrument from different sectors**, and
neither is the cyber authority. No other country in the Atlas has that shape.

⚠ Schedule 1 names more competent authorities than these two — the
departments responsible for **energy, transport, health and drinking water**
— and none of those is modelled. The Atlas therefore shows two of a longer
list, which is better than the one it showed before and still incomplete.

## `coverage: low`

Ofcom's founding, its statutory basis, and its far larger remit outside this
Atlas's scope — broadcasting, telecoms, post, and online safety under the
Online Safety Act — are **entirely unrecorded**. This entity is deliberately
scoped to the NIS competent-authority role, which is the part that connects
to something the Atlas already holds.

That scoping is the same judgement made for [[GB-DCMS]]: an entity may exist
to make a sourced relationship expressible, provided its `coverage` says how
little of it is here.

## Relationships

- `applies-to` [[GB-NIS-REGULATIONS]] — the pattern [[GB-ICO]],
  [[BE-APD]], [[DE-BFDI]], [[ES-AEPD]], [[FR-CNIL]] and [[PL-UODO]] all use
  for a regulator and its instrument.

## Sources

Listed in frontmatter.
