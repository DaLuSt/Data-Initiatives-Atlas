---
id: EE-RIHA
type: platform
name: RIHA — administration system for the state information system
alternative_names:
  - RIHA
  - Riigi infosüsteemi haldussüsteem
description: >
  Estonian administration system in which the databases of the state
  information system are described and registered, regulated by the Public
  Information Act and a special regulation. Before the Estonian data
  portal was established, data descriptions for state databases were
  published here while open data was published in the separate open data
  portal.

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
  - EE-ATS
  - NL-BASISREGISTRATIES
relationships:
  - type: governed-by
    target: EE-ATS
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org's RIHA article directly (2026-08-26): 'It is regulated by the Public Information Act and a special regulation.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: EE-RIA
    source: fact
    evidence: "Confirmed by reading ria.ee's own Estonian data portal page directly (2026-08-26): RIHA 'is currently still in use, but it is expected to be decommissioned at the end of 2026 when the legislative amendments come into force' — RIA's own page, describing its own successor system, treats RIHA as still live and still theirs to operate as of this reading."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Administration system for the state information system RIHA"
    url: "https://en.wikipedia.org/wiki/Administration_system_for_the_state_information_system_RIHA"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
  - title: "Estonian data portal | RIA"
    url: "https://www.ria.ee/en/state-information-system/data-based-governance-and-reuse-data/estonian-data-portal"
    publisher: "Riigi Infosüsteemi Amet (RIA)"
    accessed: "2026-08-26"
---

# RIHA — administration system for the state information system

> **Verified 2026-08-26.** Both cited pages were read directly. RIA's
> own page gives RIHA an expiry date this entity did not have: expected
> decommissioning "at the end of 2026," with its data folded into
> [[EE-ANDMEPORTAAL]] once "legislative amendments come into force." As
> of this reading RIHA is still live, still governed by [[EE-ATS]], and
> still RIA's to operate. Note: `ria.ee` was read successfully via a
> direct `curl` fetch with the honest User-Agent, but
> `tools/reverify.py`'s own fetcher (Python's `urllib`) reproducibly
> gets a Cloudflare "Just a moment..." challenge on the same URL with
> the identical UA string — expect `tools/reverify.py --id EE-RIHA` to
> report it UNREACHABLE despite the page being genuinely readable.

## Description

The **administration system for the state information system** — Estonia's
catalogue of the databases the state runs, and the closest thing in the
Atlas to a register *of registers*. Confirmed by reading its own
Wikipedia article directly: RIHA "serves as the national registry of
systems, components, services, data models, semantic assets," its use
is **mandatory for state agencies**, and it operates on principles
including legality, unity, use of basic data, traceability, and use of
up-to-date technology.

## A system on notice

RIHA is not being wound down quietly. ria.ee's own page, read directly,
states RIHA "is currently still in use, but it is expected to be
decommissioned at the end of 2026 when the legislative amendments come
into force" — meaning this entity is likely to need a `status` change
and a `successor` pointer to [[EE-ANDMEPORTAAL]] within months of this
re-verification, not years.

## The Dutch comparison it invites, and does not quite fit

[[NL-BASISREGISTRATIES]] is a *stelsel* of ten authentic registrations with
a legal duty to use them. RIHA is not that: it is the administration system
in which state databases are described and registered. One is a set of
authoritative data sources; the other is the index that says which systems
exist.

**No relationship between them is asserted.** They are the same shape at a
distance and different things up close, which is exactly the case where the
Atlas records the comparison in prose rather than inventing an edge.

## Legal basis

The **[[EE-ATS]]** (Public Information Act) and a special regulation. That
is the one clear statutory anchor found for any part of the Estonian data
infrastructure, which is why the `governed-by` edge sits here rather than on
[[EE-X-TEE]].

## Sources

Listed in frontmatter, both read directly this pass.

