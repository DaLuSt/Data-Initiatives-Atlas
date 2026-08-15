---
id: DE-IT-ARCHITEKTURRICHTLINIEN
type: framework
name: Föderale IT-Architekturrichtlinien
alternative_names:
  - Föderale IT-Architekturrichtlinie
  - Federal IT Architecture Guidelines
description: >
  Architecture guidelines for the German federal IT landscape, defined and
  developed by the federal IT architecture board and adopted by the
  IT-Planungsrat. They apply to all ongoing and new projects and
  undertakings that affect the federal IT landscape. Version 1.9.0 was
  adopted by IT-Planungsrat decision 2025/17.

level: national
country: DE
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
  - DE-FITKO
  - DE-IT-PLANUNGSRAT
related_entities:
  - DE-DEUTSCHLAND-STACK
relationships:
  - type: maintained-by
    target: DE-FITKO
    source: fact
    evidence: "Strategic steering of federal IT architecture management lies with the federal IT architecture board, which defines the federal IT architecture guidelines and develops them further; the board is chaired by the FITKO and made up of representatives of the FITKO, the Länder, the Bund and the municipal sector (fitko.de/foederale-koordination/gremienarbeit/foederales-it-architekturboard; fitko.de/foederale-it-architektur). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Föderale IT-Architekturrichtlinien | Dokumentation zur Föderalen IT"
    url: "https://docs.fitko.de/fit/policies/foederale-it-architekturrichtlinien/"
    publisher: "Föderale IT-Kooperation (FITKO)"
  - title: "Föderales IT-Architekturboard"
    url: "https://www.fitko.de/foederale-koordination/gremienarbeit/foederales-it-architekturboard"
    publisher: "Föderale IT-Kooperation (FITKO)"
  - title: "Föderale Architekturrichtlinien — Version 1.0"
    url: "https://www.fitko.de/fileadmin/fitko/foederale-koordination/gremienarbeit/Foederales_IT-Architekturboard/Foederale_IT-Architekturrichtlinien_V1.0.pdf"
    publisher: "Föderale IT-Kooperation (FITKO)"
  - title: "Kompass der föderalen IT-Architektur"
    url: "https://docs.fitko.de/resources/kompass/"
    publisher: "Föderale IT-Kooperation (FITKO)"
  - title: "FITKO | Föderale IT-Architektur"
    url: "https://www.fitko.de/foederale-it-architektur"
    publisher: "Föderale IT-Kooperation (FITKO)"
---

# Föderale IT-Architekturrichtlinien

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Föderale IT-Architekturrichtlinien are the architecture guidelines for
the German federal IT landscape. The **föderales IT-Architekturboard**
defines them and develops them further; strategic steering of federal IT
architecture management sits with that board, which is made up of
representatives of [[DE-FITKO]], the Länder, the Bund and the municipal
sector, and is **chaired by the FITKO**.

They **apply to all ongoing and new projects and undertakings that affect
the federal IT landscape**. [[DE-IT-PLANUNGSRAT]] adopts them: decision
**2025/17** adopted version **1.9.0**.

They sit within a wider documentation set, the **Kompass der föderalen
IT-Architektur**, which covers administrative-law and political questions,
access portals, base services, data standards and transport systems.

## Germany's NORA-shaped entity, with one important difference

This is the closest German counterpart to [[NL-NORA]]: the reference
architecture governing public-sector IT, maintained by a central
coordinating body, sitting above a family of standards.

The difference is in binding force, and it is worth stating because it is
the kind of thing an Atlas flattens if it is not careful. The Dutch model
binds through [[NL-PAS-TOE-OF-LEG-UIT]] — a comply-or-explain policy
applied to a published list of open standards. The German guidelines bind
by their own terms, applying to *all* projects affecting the federal IT
landscape, adopted by a Bund-Länder council.

**No relationship to [[NL-NORA]] is asserted.** Two reference
architectures are not related merely by being reference architectures.

## What is not recorded

The **content** of the guidelines. No source read states what version 1.9.0
requires, what principles the guidelines set out, or how compliance is
assessed. `coverage: medium` reflects that this entity records the
guidelines' existence, custody, governance and versioning but not their
substance.

The version number is recorded in prose rather than in a field, because the
Atlas has no version field and `previous_version` is reserved for
superseded *entities*, not for revisions of a living document. Nine
versions preceded 1.9.0 and none is an Atlas entity — correctly, since
they are revisions rather than distinct instruments.

## Relationships

- Maintained by [[DE-FITKO]].

Inbound: [[DE-IT-PLANUNGSRAT]] `produces` this framework — the council
adopts, the board drafts, and both facts are recorded on the side that
states them.

## Sources

Listed in frontmatter — all five are FITKO pages. Self-sourcing again,
though for a framework the maintaining body publishes, the maintainer's own
documentation is the primary source rather than a substitute for one.
