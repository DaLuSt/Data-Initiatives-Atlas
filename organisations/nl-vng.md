---
id: NL-VNG
type: organisation
name: Vereniging van Nederlandse Gemeenten
alternative_names:
  - VNG
  - Association of Netherlands Municipalities
description: >
  Association of Dutch municipalities. Within the data/digital ecosystem it
  coordinates joint municipal information management, runs the Common Ground
  programme, and represents municipalities in government-wide digital
  governance bodies.

level: national
country: NL
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
  - NL-OBDO
  - NL-ICTU
relationships:
  - type: maintained-by
    target: NL-COMMON-GROUND
    source: interpretation
    evidence: "Recorded from the VNG side: Common Ground is presented on vng.nl as a VNG programme. Direction expressed as VNG→Common Ground for navigability; the authoritative framing belongs on the Common Ground entity."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-OBDO
    source: fact
    evidence: "VNG is listed among OBDO members alongside ministries, CIO Rijk, IPO and UvW, per digitaleoverheid.nl MIDO governance page. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Common Ground"
    url: "https://vng.nl/onderwerpen/common-ground"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
    accessed: "2026-08-20"
  - title: "Governance Digitale Overheid"
    url: "https://vng.nl/artikelen/governance-digitale-overheid"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
---

# Vereniging van Nederlandse Gemeenten (VNG)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The VNG is the association of Dutch municipalities. It enters the Atlas
through its role in collective municipal information management: it runs the
[[NL-COMMON-GROUND]] programme, through which municipalities jointly
restructure their information provision, and it represents municipalities in
government-wide digital governance, including membership of the [[NL-OBDO]].
With [[NL-BZK]] it co-founded [[NL-ICTU]] in 2001.

`coverage: low` — the VNG's sourcing here is incidental to the Common Ground
and governance research rather than drawn from a general institutional
profile. A re-verification pass should add a primary VNG source about the
association itself.

## Relationships

- Runs [[NL-COMMON-GROUND]].
- Participates in [[NL-OBDO]].
- Co-founder of [[NL-ICTU]], with [[NL-BZK]].

## Sources

Listed in frontmatter.
