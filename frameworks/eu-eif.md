---
id: EU-EIF
type: framework
name: European Interoperability Framework
alternative_names:
  - EIF
description: >
  EU framework setting out principles and recommendations guiding public
  administrations in delivering interoperable digital services across
  systems and borders. Revised in 2017, it comprises 12 principles, 6
  layers, a conceptual model and 47 recommendations, and supports member
  states in designing their national interoperability frameworks.

level: regional
country: null
region: EU

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
organisations: []
related_entities:
  - NL-NORA
  - EU-INTEROPERABLE-EUROPE-ACT
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "The EIF provides support to Member States to design and update their national interoperability frameworks (NIFs); the EIF Toolbox exists to help national administrations align their NIFs with the EIF (interoperable-europe.ec.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: DE
    source: fact
    evidence: "The EIF provides support to Member States to design and update their national interoperability frameworks (NIFs), Germany included, and the EIF Toolbox exists to help national administrations align their NIFs with the EIF (interoperable-europe.ec.europa.eu). NOT READ — search-only. No German NIF is identified: whether the Foederale IT-Architekturrichtlinien serve that role is unsourced and is NOT asserted."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "BelgIF is the National Interoperability Framework (NIF) for Belgium, and the federal government and the regions have agreed to use the 12 principles of the EIF as the basis for defining their interoperability (belgif.be/eif3/about.en.html). NOT READ — search-only. Unlike the Netherlands and Germany above, the Belgian national framework IS identified: see BE-BELGIF, which carries a based-on relationship to this entity."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "European Interoperability Framework (EIF)"
    url: "https://interoperable-europe.ec.europa.eu/collection/iopeu-monitoring/european-interoperability-framework-eif"
    publisher: "European Commission — Interoperable Europe Portal"
  - title: "The European Interoperability Framework in detail"
    url: "https://interoperable-europe.ec.europa.eu/collection/iopeu-monitoring/european-interoperability-framework-detail"
    publisher: "European Commission — Interoperable Europe Portal"
  - title: "European Interoperability Framework (EIF) Toolbox"
    url: "https://interoperable-europe.ec.europa.eu/collection/iopeu-monitoring/solution/european-interoperability-framework-eif-toolbox"
    publisher: "European Commission — Interoperable Europe Portal"
  - title: "New European Interoperability Framework (brochure)"
    url: "https://ec.europa.eu/isa2/sites/default/files/eif_brochure_final.pdf"
    publisher: "European Commission — ISA²"
---

# European Interoperability Framework (EIF)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The EIF sets out principles and recommendations guiding public
administrations in delivering interoperable digital services that work
across systems and borders. The current version was revised in 2017 and
comprises 12 principles, 6 layers, 1 conceptual model with 7 components, and
47 recommendations.

Its objectives are to support European public administrations in designing
and delivering seamless cross-border public services, to support member
states in designing and updating their **national interoperability
frameworks (NIFs)**, and to contribute to the digital single market by
fostering cross-border and cross-sectoral interoperability. The EIF Toolbox
exists specifically to help national administrations align their NIFs with
the EIF.

## The NORA question

[[NL-NORA]] is described in its own sources as "the interoperability
framework for the Dutch government", which makes it the obvious candidate
for the Netherlands' NIF — and would make EIF→NORA one of the cleanest
EU→national framework chains available to the Atlas.

**That relationship is not asserted.** No source located states that NORA is
formally the Dutch NIF submitted under the EIF, and the phrase "the
interoperability framework for the Dutch government" is a description, not a
designation. The `related_entities` link records the association; a
`applies-to` or `based-on` relationship awaits a source that says so.

Confirming or refuting this is queued in `discovery/research-queue.md` and
is one of the higher-value items there: it would connect the EU and Dutch
framework layers directly.

## A revision in flight

The Commission aimed to submit a new version of the EIF to the Interoperable
Europe Board for adoption at the end of 2025 / beginning of 2026. Relative
to this entry's date (August 2026) that revision may already have been
adopted, which would make the "revised in 2017" description stale.
`last_verified` is null and this is flagged in `discovery/unresolved.md`.

Batch 8 added [[EU-INTEROPERABLE-EUROPE-ACT]]. **No relationship between the
Act and this Framework is asserted**, because no source read states how they
relate — whether the Act gives the EIF legal standing, supersedes it, or
provides governance around it. That question determines whether the EU
interoperability layer has one root or two, and is queued. The Interoperable
Europe Board remains uncreated (Batch 9).

## Relationships

- Applies in [[NL]], [[DE]] and [[BE]] through the NIF alignment mechanism.
- **[[BE-BELGIF]] is `based-on` this framework** — the Atlas's first and
  so far only EIF → national-framework descent. The Belgian sources state
  that BELGIF is Belgium's NIF and takes the EIF's 12 principles as its
  basis. No equivalent statement was found for the Netherlands or Germany,
  so neither carries the link; see the NORA question above.
- Associated with [[NL-NORA]] — see the NORA question above.

## Sources

Listed in frontmatter.
