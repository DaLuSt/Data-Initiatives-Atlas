---
id: UN-ITU
type: organisation
name: International Telecommunication Union
alternative_names:
  - ITU
description: >
  UN specialised agency for information and communication technologies. It
  promotes shared global use of the radio spectrum, facilitates
  international cooperation in assigning satellite orbits, assists in
  developing and coordinating worldwide technical standards, and works to
  improve telecommunication infrastructure in the developing world.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - UN
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "The ITU is a United Nations specialised agency, with two key sectors for digital standards (itu.int/en/un/Pages/un-agency.aspx). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "ITU as a UN Specialized Agency"
    url: "https://www.itu.int/en/un/Pages/un-agency.aspx"
    publisher: "International Telecommunication Union"
  - title: "International Telecommunication Union — International Regulatory Co-operation"
    url: "https://www.oecd-ilibrary.org/governance/international-regulatory-co-operation/international-telecommunication-union-itu_9789264244047-37-en"
    publisher: "OECD iLibrary"
---

# International Telecommunication Union (ITU)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The ITU is a **UN specialised agency** for information and communication
technologies. It promotes shared global use of the radio spectrum,
facilitates international cooperation in assigning satellite orbits, assists
in developing and coordinating worldwide technical standards, and works to
improve telecommunication infrastructure in developing countries. It has two
sectors central to digital standards.

## Why the UN scope matters here

Batch 13's brief warns explicitly: *"Do not incorrectly classify non-UN
organisations as UN organisations."* The ITU is the case where that warning
bites hardest, because it sits in standards-development listings alongside
[[INTL-ISO]], [[INTL-IEC]], [[INTL-W3C]], [[INTL-IETF]] and [[EU-ETSI]] —
company that makes it look like a peer standards body rather than a UN
organ.

It is nonetheless a UN specialised agency, sourced directly to itu.int, and
therefore carries the **`UN` ID scope** while the others carry `INTL`. One
source describes the ecosystem precisely: formal international bodies based
on national delegation (ISO, IEC, ITU), global organisations with direct
membership (IEEE, IETF, W3C), and European organisations recognised by the
EU (ETSI).

`coverage: low`: no ITU standard is modelled.

## Relationships

- Part of [[UN]] as a specialised agency.

## Sources

Listed in frontmatter.
