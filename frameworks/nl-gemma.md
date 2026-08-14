---
id: NL-GEMMA
type: framework
name: Gemeentelijke Model Architectuur
alternative_names:
  - GEMMA
  - Gemeentelijke ModelArchitectuur
description: >
  Reference architecture for Dutch municipalities. A coherent collection of
  architecture products that builds further on international standards and
  the Nederlandse Overheid Referentie Architectuur, developed and managed by
  the Architecture Knowledge Centre of VNG Realisatie together with
  municipalities, suppliers and chain partners.

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
  - DOMAIN-GOVERNMENT
organisations:
  - NL-VNG
related_entities:
  - NL-NORA
  - NL-COMMON-GROUND
relationships:
  - type: based-on
    target: NL-NORA
    source: fact
    evidence: "GEMMA consists of a coherent collection of architecture products and builds further on international standards and the Nederlandse Overheid Referentie Architectuur (vng.nl; noraonline.nl GEMMA page). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-VNG
    source: fact
    evidence: "The Kenniscentrum Architectuur, part of VNG Realisatie, develops and manages GEMMA together with municipalities, suppliers and chain partners (vng.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Gemeentelijke Model Architectuur (GEMMA)"
    url: "https://vng.nl/projecten/gemeentelijke-model-architectuur-gemma"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
  - title: "GEMMA (Gemeentelijke ModelArchitectuur)"
    url: "https://www.noraonline.nl/wiki/GEMMA_(Gemeentelijke_ModelArchitectuur)"
    publisher: "NORA Online (ICTU)"
  - title: "GEMMA Online — Gemeentelijke modelarchitectuur"
    url: "https://vng.nl/kennisbank-grip-op-informatie/gemma-online-gemeentelijke-modelarchitectuur"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
---

# GEMMA (Gemeentelijke Model Architectuur)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

GEMMA is the reference architecture for all Dutch municipalities. It is a
coherent collection of architecture products that builds further on
international standards and on [[NL-NORA]] — making it the municipal
domain-specific extension of the government-wide reference architecture.

Its purpose is to give municipalities overview and insight for steering
developments in which business operations and IT interact, to help
municipalities collaborate, and to keep solutions aligned with one another.

GEMMA includes theme architectures covering subjects such as Security and
Privacy, Case Management (zaakgericht werken) and [[NL-COMMON-GROUND]], plus
supporting products including the GEMMA Concept Framework and the GEMMA
Standards List. It is published at gemmaonline.nl and the ArchiMate model is
maintained openly on GitHub.

**VNG Realisatie**, whose Kenniscentrum Architectuur develops and manages
GEMMA, is not yet a separate Atlas entity — the `maintained-by`
relationship therefore points at [[NL-VNG]], which is a simplification.
VNG Realisatie is queued in `discovery/research-queue.md`, and this
relationship should be re-pointed once it exists.

## Relationships

- Based on [[NL-NORA]].
- Maintained by [[NL-VNG]] (via VNG Realisatie — see above).
- Includes a theme architecture for [[NL-COMMON-GROUND]], connecting the
  municipal architecture to the municipal information-management programme.

## Sources

Listed in frontmatter.
