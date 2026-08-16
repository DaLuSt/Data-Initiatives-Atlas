---
id: BE-BELGIF
type: framework
name: Belgian Interoperability Framework
alternative_names:
  - BELGIF
  - Belgif
description: >
  Belgium's national interoperability framework, a collaborative effort of
  the Belgian federal state, the Regions and the language Communities with
  the active support of the six public service integrators and several
  public administrations. The federal government and the regions agreed to
  use the 12 principles of the European Interoperability Framework as the
  basis for defining their interoperability. It publishes a list of
  recommended ICT specifications and a mapping of the EIF recommendations
  to Belgian interoperability initiatives across the legal, organisational,
  semantic and technical levels.

level: national
country: BE
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
  - EU-EIF
  - BE-DCAT-AP-BE
relationships:
  - type: based-on
    target: EU-EIF
    source: fact
    evidence: "BelgIF is the National Interoperability Framework (NIF) for Belgium, and the federal government and the regions have agreed to use the 12 principles of the EIF as the basis for defining their interoperability; the BELGIF portal publishes a mapping of the EIF recommendations to various interoperability initiatives classified by legal, organisational, semantic and technical levels (belgif.be/eif3/about.en.html; belgif.be/eif3/recommendations.en.html). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Belgif | EIF 3 — About"
    url: "https://belgif.be/eif3/about.en.html"
    publisher: "Belgian Interoperability Framework (BELGIF)"
  - title: "Belgif | EIF 3 — Recommendations"
    url: "https://belgif.be/eif3/recommendations.en.html"
    publisher: "Belgian Interoperability Framework (BELGIF)"
  - title: "Specification: DCAT-AP"
    url: "https://belgif.be/page/specification/dcat-ap.en.html"
    publisher: "Belgian Interoperability Framework (BELGIF)"
  - title: "BelgIF — Belgian Interoperability Framework (GitHub)"
    url: "https://github.com/belgif"
    publisher: "BELGIF"
  - title: "Factsheet: Access to Base Registries in Belgium"
    url: "https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/Belgium%20Factsheet%20Final.pdf"
    publisher: "European Commission — Interoperable Europe"
---

# BELGIF — Belgian Interoperability Framework

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

BELGIF is Belgium's **National Interoperability Framework (NIF)**. It is a
collaborative effort of the **Belgian federal state, the Regions and the
language Communities**, with the active support of the **six public service
integrators** — of which [[BE-KSZ]] is one — and several public
administrations.

The federal government and the regions **agreed to use the 12 principles of
the European Interoperability Framework** as the basis for defining their
interoperability. The BELGIF portal publishes:

- a list of **recommended ICT specifications** — open standards and formats
  for data exchange;
- a **mapping of the EIF recommendations** to Belgian interoperability
  initiatives, classified across the EIF's legal, organisational, semantic
  and technical levels.

## This closes a link Germany could not

When Germany gained `applies-in` → `DE` on [[EU-EIF]], the evidence field
had to say so explicitly:

> *"No German NIF is identified: whether the Föderale
> IT-Architekturrichtlinien serve that role is unsourced and is NOT
> asserted."*

Belgium supplies what Germany lacked. BELGIF **is** sourced as the national
interoperability framework, and sourced as taking the EIF's 12 principles
as its basis — so `based-on` → [[EU-EIF]] is recorded as a fact rather than
refused.

This is the Atlas's **first EIF → national-framework descent**, and it
matters structurally: [[EU-EIF]] previously had `applies-in` relationships
to three countries and no national framework beneath it in any of them.

The German question stays open and is now sharper, because there is a
worked example of what closing it would look like. Logged in
`discovery/unresolved.md`.

## The federal structure, visible in the entity itself

BELGIF is the one Belgian entity where the Regions and Communities appear
in the record at all — as **parties to the framework**, named in the
sourced description.

They are named and not modelled. The Atlas has no level for a Belgian
Region (see `countries/be/be.md`), so a framework explicitly co-owned by
the federal state, three Regions and three Communities is recorded as
`country: BE`, `level: national`, with its co-owners visible only in prose.

That is a fair summary of what the Atlas can and cannot say about Belgium.

## Relationships

- `based-on` [[EU-EIF]].

**No relationship to [[NL-NORA]] or [[DE-IT-ARCHITEKTURRICHTLINIEN]] is
asserted.** All three are national architecture or interoperability
instruments; two reference architectures and a national interoperability
framework are not the same kind of thing, and none of the sources connects
them.

## Sources

Listed in frontmatter, including a European Commission factsheet on access
to base registries in Belgium.
