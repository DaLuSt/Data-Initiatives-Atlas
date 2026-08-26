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
  - EU-EIF
  - BE-DCAT-AP-BE
relationships:
  - type: based-on
    target: EU-EIF
    source: fact
    evidence: "Confirmed by reading belgif.be and github.com/belgif directly (2026-08-26): 'For Belgium, BelgIF is the NIF', and 'The federal government and the regions have agreed to use the 12 principles of the EIF as the basis for defining their interoperability.' Belgium's 47 recommendations derived from those principles are endorsed within BelgIF 'as a valuable foundation for the definition of architecture, applications and solutions for data exchange and interoperability within and between the federal government and the communities and regions.' The github.com/belgif organisation page independently restates the same collaborative-effort description verbatim."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Belgif | EIF 3 — About"
    url: "https://belgif.be/eif3/about.en.html"
    publisher: "Belgian Interoperability Framework (BELGIF)"
    accessed: "2026-08-26"
  - title: "Belgif | EIF 3 — Recommendations"
    url: "https://belgif.be/eif3/recommendations.en.html"
    publisher: "Belgian Interoperability Framework (BELGIF)"
    accessed: "2026-08-26"
  - title: "Specification: DCAT-AP"
    url: "https://belgif.be/page/specification/dcat-ap.en.html"
    publisher: "Belgian Interoperability Framework (BELGIF)"
    accessed: "2026-08-26"
  - title: "BelgIF — Belgian Interoperability Framework (GitHub)"
    url: "https://github.com/belgif"
    publisher: "BELGIF"
    accessed: "2026-08-26"
  - title: "Factsheet: Access to Base Registries in Belgium"
    url: "https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/Belgium%20Factsheet%20Final.pdf"
    publisher: "European Commission — Interoperable Europe"
---

# BELGIF — Belgian Interoperability Framework

> **Verified 2026-08-26.** Four of the five cited sources were read
> directly: both belgif.be EIF pages, the DCAT-AP specification page, and
> the github.com/belgif organisation page, which independently restates the
> same "collaborative effort" description. Only the European Commission
> factsheet PDF was retrieved but not readable as text. `verification:
> primary-source`.

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

Four of five read directly this pass — the belgif.be "About" and
"Recommendations" pages, the DCAT-AP specification page, and the
github.com/belgif organisation page. The European Commission factsheet on
access to base registries in Belgium was retrieved but returned as an
unreadable binary PDF and remains unconfirmed.
