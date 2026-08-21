---
id: FI-SUOMI-FI
type: platform
name: Suomi.fi
alternative_names:
  - Suomi.fi Web Service
  - Finnish national service portal
description: >
  Finland's national service portal and the front end of its shared
  e-service support services, alongside Suomi.fi Messages for electronic
  messages from authorities and Suomi.fi e-Authorization for acting on
  behalf of another party.

level: national
country: FI
region: EU

status: active
confidence: medium
coverage: low
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
  - FI
  - FI-DVV
relationships:
  - type: part-of
    target: FI
    source: fact
    evidence: "Suomi.fi is a public body of FI; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: FI-DVV
    source: fact
    evidence: "The Digital and Population Data Services Agency develops and maintains the centralised support services for e-services, which include the Suomi.fi Web Service, Suomi.fi Messages and Suomi.fi e-Authorization (dvv.fi 'About the agency'). NOT READ - search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Suomi.fi"
    url: "https://www.suomi.fi/frontpage"
    publisher: "Digital and Population Data Services Agency (DVV)"
  - title: "About the agency"
    url: "https://dvv.fi/en/about-the-agency"
    publisher: "Digital and Population Data Services Agency (DVV)"
---

# Suomi.fi

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Finland's citizen-facing service portal.

## Three services under one name

Suomi.fi is a portal, a **secure messaging channel** between authorities
and citizens, and an **authorisation register** for acting on someone
else's behalf. The Atlas models it as one platform; the mandate register
in particular has no counterpart in any other country here.

## Sources

Listed in frontmatter.
