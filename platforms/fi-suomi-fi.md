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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading suomi.fi's own frontpage directly (2026-08-26), a government-operated service: anchor edge under metadata/relationship-types.md §2.3, asserting no more than national scope."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: FI-DVV
    source: fact
    evidence: "Confirmed verbatim by reading suomi.fi's own frontpage directly (2026-08-26): 'The service is being developed by the Digital and Population Data Services Agency' — stated in Suomi.fi's own 'in brief' summary, not a secondary source."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Suomi.fi"
    url: "https://www.suomi.fi/frontpage"
    publisher: "Digital and Population Data Services Agency (DVV)"
    accessed: "2026-08-26"
  - title: "About the agency"
    url: "https://dvv.fi/en/about-the-agency"
    publisher: "Digital and Population Data Services Agency (DVV)"
    accessed: "2026-08-26"
---

# Suomi.fi

> **Verified 2026-08-26.** Both cited pages were read directly.
> Suomi.fi's own homepage confirms the `maintained-by` edge in its own
> words.

## Description

Finland's citizen-facing service portal. Confirmed by reading
suomi.fi directly: "Suomi.fi Web Service helps citizens and
entrepreneurs in different situations... After identification into
Suomi.fi, you can communicate with different organisations, grant and
request mandates and check the data registered on you."

## Three services under one name

Suomi.fi is a portal, a **secure messaging channel** between authorities
and citizens, and an **authorisation register** for acting on someone
else's behalf. The Atlas models it as one platform; the mandate register
in particular has no counterpart in any other country here.

## Relationships

- `part-of` [[FI]] — anchor edge.
- `maintained-by` [[FI-DVV]].

## Sources

Listed in frontmatter, both read directly this pass.
