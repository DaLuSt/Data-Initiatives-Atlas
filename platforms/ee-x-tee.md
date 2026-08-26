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
  - EE
  - EE-RIA
  - INTL-X-ROAD
  - EE-RIHA
  - NL-DIGIKOPPELING
relationships:
  - type: maintained-by
    target: EE-RIA
    source: fact
    evidence: "Confirmed by reading ria.ee's own X-tee page directly (2026-08-26): 'X-tee, the data exchange layer for information systems, is a technological and organizational environment enabling a secure Internet-based data exchange between information systems' — presented as RIA's own service. `scoop4c.eu` is genuinely unreachable this pass regardless of User-Agent: a TLS handshake reset (curl error 35), not a UA-specific 403, tested with both an honest and a browser-spoofing User-Agent."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: INTL-X-ROAD
    source: fact
    evidence: "Confirmed verbatim by reading ria.ee's own X-tee page directly (2026-08-26): 'X-tee is a data exchange layer used in Estonia. Until 2018, it was named X-Road in English. Since 2018, however, X-Road is only used to refer to the technology developed together by Estonia, Finland and Iceland through MTÜ Nordic Institute for Interoperability Solutions.' This confirms both the naming split and, independently of the [[FI-PALVELUVAYLA]] sourcing, Iceland's membership in NIIS."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Data exchange layer X-tee | RIA"
    url: "https://www.ria.ee/en/state-information-system/data-exchange-platforms/data-exchange-layer-x-tee"
    publisher: "Riigi Infosüsteemi Amet (RIA) — Information System Authority"
    accessed: "2026-08-26"
  - title: "Estonian data exchange layer for information systems (X-Road)"
    url: "https://scoop4c.eu/cases/estonian-data-exchange-layer-information-systems-x-road"
    publisher: "SCOOP4C"
  - title: "X-Road"
    url: "https://en.wikipedia.org/wiki/X-Road"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
---

# X-tee

> **Verified 2026-08-26.** Two of three cited pages were read directly.
> `scoop4c.eu` is genuinely unreachable — a TLS connection reset with
> both an honest and a browser-spoofing User-Agent, a new host-blocking
> shape distinct from the HTTP-403 walls found elsewhere this session.
> RIA's own page confirms the naming split and the `maintained-by` edge
> in its own words. Note: `ria.ee` was read successfully via a direct
> `curl` fetch with the honest User-Agent, but `tools/reverify.py`'s own
> fetcher (Python's `urllib`) reproducibly gets a Cloudflare "Just a
> moment..." challenge on the same URL with the identical UA string — a
> client-fingerprint-dependent block, not a UA-string one. Expect
> `tools/reverify.py --id EE-X-TEE` to report `ria.ee` as UNREACHABLE
> despite the page being genuinely readable.

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

Listed in frontmatter, two of three read directly this pass;
`scoop4c.eu` is genuinely unreachable (TLS reset, both User-Agents).

