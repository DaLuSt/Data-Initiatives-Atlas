---
id: IT-AGID
type: organisation
name: Agenzia per l'Italia Digitale
alternative_names:
  - AgID
  - Agency for Digital Italy
description: >
  Italian agency responsible for promoting digital innovation in the
  country and the use of digital technologies in public administration and
  in the relationship between administration, citizens and enterprises. It
  manages the public digital identity system for citizens and businesses,
  SPID, established by Article 64 of the Codice dell'Amministrazione
  Digitale.

level: national
country: IT
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IT
  - IT-CAD
  - IT-SPID
relationships:
  - type: part-of
    target: IT
    source: fact
    evidence: "AgID is a public body of IT; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: IT-CAD
    source: fact
    evidence: "AgID manages the public system for managing digital identity for citizens and enterprises (SPID), established by article 64, paragraph 2-bis, of decreto legislativo 82/2005 - the Codice dell'Amministrazione Digitale (agid.gov.it; it.wikipedia.org 'Agenzia per l'Italia digitale'). NOT READ - search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Agenzia per l'Italia Digitale"
    url: "https://www.agid.gov.it/"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
  - title: "Agenzia per l'Italia digitale"
    url: "https://it.wikipedia.org/wiki/Agenzia_per_l%27Italia_digitale"
    publisher: "Wikipedia"
---

# Agenzia per l'Italia Digitale

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Italy's digital government agency, and the operator of [[IT-SPID]].

## The largest member state the Atlas had left

Italy was **first on the country-expansion shortlist** and had carried
only its anchor since the European country batch. AgID is the entry
point: it holds the digital identity system, the technical rules under
[[IT-CAD]], and the *Piano triennale* for public-administration IT.

## Relationships

- `governed-by` [[IT-CAD]] - the Code is AgID's operating statute as
  well as Italy's digital administration law.
- `part-of` [[IT]] (anchor edge).

## Sources

Listed in frontmatter.
