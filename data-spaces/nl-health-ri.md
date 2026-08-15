---
id: NL-HEALTH-RI
type: data-space
name: Health-RI
alternative_names:
  - Nationale gezondheidsdata-infrastructuur
  - Health-RI Afsprakenstelsel
description: >
  The Dutch national health data infrastructure for research, policy and
  innovation. Not centralised: data remain stored locally as far as
  possible, made nationally usable through a network of regional nodes
  around a central hub, governed by the Health-RI agreement framework.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
  - DOMAIN-RESEARCH
organisations: []
related_entities:
  - NL-NICTIZ
  - EU-EHDS
relationships: []

sources:
  - title: "Health-RI Afsprakenstelsel — Nationale Gezondheidsdata-infrastructuur"
    url: "https://health-ri.atlassian.net/wiki/spaces/HNG/overview"
    publisher: "Health-RI"
  - title: "Knooppunten"
    url: "https://www.health-ri.nl/en/about/organisation/knooppunten"
    publisher: "Health-RI"
  - title: "Health-RI"
    url: "https://www.nationaalgroeifonds.nl/overzicht-lopende-projecten/thema-gezondheid-en-zorg/health-ri"
    publisher: "Nationaal Groeifonds"
---

# Health-RI

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Health-RI works to organise, orchestrate and develop the Dutch national
health data infrastructure for research and innovation, so that health and
research data can be safely and responsibly reused for research, policy and
innovation. It links databases, biobanks and registrations held by
university medical centres and other knowledge and care institutions.

Its defining architectural choice is federation rather than centralisation:
the infrastructure comes about through standardised accessibility of data
via a network of regional nodes (*knooppunten*) working with a central hub.
Data remain stored locally as far as possible but become nationally usable
through shared agreements and standards — the Health-RI Afsprakenstelsel,
under which stakeholders work towards national cooperation agreements for
making health data available and reusable.

It works with the ministries of VWS, EZK and OCW and many field parties, and
is funded via the Nationaal Groeifonds. None of those ministries is yet an
Atlas entity.

## Typing note

Health-RI is recorded as a `data-space`, but the name denotes both an
**organisation** and the **infrastructure** it builds — the sources use it
for both. One entity is used rather than two because the infrastructure has
no distinct proper name of its own beyond "de nationale
gezondheidsdata-infrastructuur", and splitting would create an entity whose
identity rests on a descriptive phrase. Whether to split is recorded in
`discovery/unresolved.md`.

Its federated design makes it a close structural analogue of
[[NL-FDS]] — both are afsprakenstelsels for federated data sharing, one
government-wide and one for health. No relationship is asserted between
them: the resemblance is real but no source connects them.

## Relationships

- Adjacent to [[NL-NICTIZ]], which maintains the health information
  standards that such an infrastructure relies on. No relationship
  asserted, as none was sourced.
- [[EU-EHDS]] was added in Batch 10. **No relationship is asserted.**
  Health-RI is the obvious candidate to become or host the Dutch health data
  access body the EHDS requires, but no source says so, and the member-state
  HDAB designation phase runs 2027–2029 — after this entry was written.
  Recorded as a high-value open question rather than a guess.

## Sources

Listed in frontmatter.
