---
id: EE-X-TEE
type: platform
name: X-tee
alternative_names:
  - X-Road (Estonia)
  - Estonian data exchange layer
description: >
  Estonia's data exchange layer, operated by the Information System
  Authority, enabling public agencies to share data securely with one
  another. Data is not held in a central repository: it flows directly
  from source to recipient. It is Estonia's deployment of the X-Road
  software, and was named X-Road in English until 2018.

level: national
country: EE
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
  - EE
  - EE-RIA
  - INTL-X-ROAD
  - EE-RIHA
  - NL-DIGIKOPPELING
relationships:
  - type: maintained-by
    target: EE-RIA
    source: fact
    evidence: "The Information System Authority (RIA) is the national competence centre responsible for managing the technological infrastructure underpinning Estonia's e-government system, and publishes X-tee as one of its data exchange platforms (ria.ee 'Data exchange layer X-tee'; scoop4c.eu 'Estonian data exchange layer for information systems (X-Road)'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: INTL-X-ROAD
    source: fact
    evidence: "X-tee is the data exchange layer used in Estonia, previously named X-Road in English until 2018; X-Road is released under the MIT open source licence and is developed by NIIS for its member states (ria.ee 'Data exchange layer X-tee'; en.wikipedia.org 'X-Road'; niis.org 'History'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Data exchange layer X-tee | RIA"
    url: "https://www.ria.ee/en/state-information-system/data-exchange-platforms/data-exchange-layer-x-tee"
    publisher: "Riigi Infosüsteemi Amet (RIA) — Information System Authority"
  - title: "Estonian data exchange layer for information systems (X-Road)"
    url: "https://scoop4c.eu/cases/estonian-data-exchange-layer-information-systems-x-road"
    publisher: "SCOOP4C"
  - title: "X-Road"
    url: "https://en.wikipedia.org/wiki/X-Road"
    publisher: "Wikipedia"
---

# X-tee

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

## Description

Estonia's data exchange layer: the thing every description of Estonian
digital government is actually describing.

## Why the Atlas was distorted without it

The Netherlands layer is the Atlas's deepest, and it is built around
[[NL-BASISREGISTRATIES]] and [[NL-DIGIKOPPELING]] — a set of authentic
registers plus a standard for exchanging between them. X-tee is the direct
counterpart, and until this batch the graph held the Dutch version of the
idea and not the Estonian one, while Estonia is the more cited of the two
internationally.

The architectural difference is the interesting part: **data never sits in a
central repository — it flows directly from source to recipient.** The Dutch
stelsel is also decentralised in law, with each register having its own
bronhouder, but the Atlas records no equivalent statement about the *wire*.

## Legal basis

Recorded as the **[[EE-ATS]]** (Avaliku teabe seadus, the Public Information
Act) together with a special regulation, which is the basis sources give for
[[EE-RIHA]]. Whether the Act is equally the basis of the exchange layer
itself, or only of the register of systems that use it, is **not established
by anything read** — so `governed-by` is asserted from [[EE-RIHA]] and not
from here.

## Not the same entity as the software

[[INTL-X-ROAD]] is the open-source product, owned by [[INTL-NIIS]] and run
in several countries. This entity is Estonia's deployment. The names diverge
too: **X-tee** in Estonian, **X-Road** internationally.

## Sources

Listed in frontmatter.

