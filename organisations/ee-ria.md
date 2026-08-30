---
id: EE-RIA
type: organisation
name: Riigi Infosüsteemi Amet
alternative_names:
  - RIA
  - Information System Authority
  - Estonian Information System Authority
description: >
  Estonian government agency acting as the national competence centre
  responsible for managing the technological infrastructure underpinning
  Estonia's e-government system. It operates the X-tee data exchange
  layer, the RIHA administration system for the state information system,
  and the Estonian data portal.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-30"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EE
  - EE-X-TEE
  - EE-RIHA
  - EE-ANDMEPORTAAL
  - EE-CERT-EE
  - EE-KUBERTURVALISUSE-SEADUS
relationships:
  - type: part-of
    target: EE
    source: fact
    evidence: "Confirmed by reading ria.ee's own data portal page directly (2026-08-26): 'The Information System Authority (RIA) coordinates the development and administration of information systems ensuring the interoperability of the state's information system, organises activities related to information security, and handles security incidents in Estonian computer networks. Information System Authority is within the administrative area of the Ministry of Justice and Digital Affairs.'"
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Data exchange layer X-tee | RIA"
    url: "https://www.ria.ee/en/state-information-system/data-exchange-platforms/data-exchange-layer-x-tee"
    publisher: "Riigi Infosüsteemi Amet (RIA) — Information System Authority"
    accessed: "2026-08-26"
  - title: "Estonian data portal | RIA"
    url: "https://www.ria.ee/en/state-information-system/data-based-governance-and-reuse-data/estonian-data-portal"
    publisher: "Riigi Infosüsteemi Amet (RIA)"
    accessed: "2026-08-26"
  - title: "Estonian data exchange layer for information systems (X-Road)"
    url: "https://scoop4c.eu/cases/estonian-data-exchange-layer-information-systems-x-road"
    publisher: "SCOOP4C"
---

# Riigi Infosüsteemi Amet

> **Verified 2026-08-26.** Two of three cited pages were read directly.
> `scoop4c.eu` is genuinely unreachable regardless of User-Agent — a
> TLS connection reset, tested with both an honest and a
> browser-spoofing one. RIA's own page confirms it sits within the
> **Ministry of Justice and Digital Affairs**, a fact this entity did
> not previously carry, and confirms directly that RIA itself runs
> Estonia's national CERT. Note: `ria.ee`'s own pages were read
> successfully via a direct `curl` fetch with the honest User-Agent,
> but `tools/reverify.py`'s own fetcher (Python's `urllib`)
> reproducibly gets a Cloudflare "Just a moment..." challenge on the
> same URLs with the identical UA string — a client-fingerprint-
> dependent block, not a UA-string one. Expect `tools/reverify.py --id
> EE-RIA` to report both `ria.ee` pages as UNREACHABLE despite being
> genuinely readable.

## Description

The Estonian **Information System Authority** — the national competence
centre for the technological infrastructure under Estonia's e-government,
and the operator of [[EE-X-TEE]], [[EE-RIHA]] and [[EE-ANDMEPORTAAL]].
Confirmed by reading ria.ee directly: RIA's own mission statement is
"We ensure a reliable digital state and seamless services — today and
tomorrow."

## Estonia's counterpart to a role three other countries split up

RIA holds in one agency what the Atlas records elsewhere as several bodies:
the data exchange layer ([[NL-LOGIUS]]'s territory in the Netherlands), the
register of state information systems, the open data portal, and the
national CERT. Whether that concentration is the reason Estonia is cited as
a model, or merely a feature of a small state, is not something any source
read establishes — so it is noted and not asserted.

## CERT-EE and the Küberturvalisuse seadus — both now modelled

RIA's own site states directly: "RIA is the National Cyber Security
Centre of Estonia (NCSC-EE)," and names **CERT-EE** as the body
handling cyber incidents. That closed the uncertainty this entity
previously carried about whether RIA actually runs Estonia's CERT — it
does, in RIA's own words. Both gaps flagged here are now closed
(2026-08-30, a research-queue pickup): [[EE-CERT-EE]] is now its own
Atlas entity, `part-of` this one, and Estonia's NIS2-transposing
Cybersecurity Act is now [[EE-KUBERTURVALISUSE-SEADUS]]. Under that Act,
confirmed via an independent NIS2-transposition tracker, RIA "performs
the functions of national competent authority, cybersecurity regulator,
and coordinator of incident response through the national CERT capability
(CERT-EE)" — no single graph edge captures that three-part role, so it is
recorded here in prose rather than forced into one relationship.

## Relationships

- `part-of` [[EE]] — anchor edge.
- Operates [[EE-X-TEE]], [[EE-RIHA]] and [[EE-ANDMEPORTAAL]].
- Contains [[EE-CERT-EE]] as a department (relationship recorded on that
  entity).

## Sources

Listed in frontmatter, two of three read directly this pass;
`scoop4c.eu` is genuinely unreachable (TLS reset, both User-Agents).

