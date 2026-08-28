---
id: DE-IT-ARCHITEKTURRICHTLINIEN
type: framework
name: Föderale IT-Architekturrichtlinien
alternative_names:
  - Föderale IT-Architekturrichtlinie
  - Federal IT Architecture Guidelines
description: >
  Architecture guidelines for the German federal IT landscape, defined and
  developed by the federal IT architecture board (established by
  IT-Planungsrat decision of 22 February 2021) and adopted by the
  IT-Planungsrat, which made their application binding by decision 2021/37
  and later adopted version 1.9.0 by decision 2025/17. They apply to all
  ongoing and new projects and undertakings that affect the federal IT
  landscape.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading three FITKO/FITKO-documentation pages directly (2026-08-28): fitko.de's own 'Föderales IT-Architekturboard' page states FITKO chairs the board and initiated its establishment, with membership from FITKO, the federal government (BMDS), the Länder and municipal peak associations; fitko.de/foederale-it-architektur confirms the board was established by IT-Planungsrat decision on 22 February 2021 and is responsible for describing and continuing the guidelines, 'mit Führung durch die FITKO' (led by FITKO); docs.fitko.de's own policy page confirms the current version is 1.9.0, adopted by IT-Planungsrat decision 2025/17, and that mandatory application of the guidelines was made binding by IT-Planungsrat decision 2021/37 — a fact not previously recorded on this entity."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Föderale IT-Architekturrichtlinien | Dokumentation zur Föderalen IT"
    url: "https://docs.fitko.de/fit/policies/foederale-it-architekturrichtlinien/"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-08-28"
  - title: "Föderales IT-Architekturboard"
    url: "https://www.fitko.de/foederale-koordination/gremienarbeit/foederales-it-architekturboard"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-08-28"
  - title: "Föderale Architekturrichtlinien — Version 1.0"
    url: "https://www.fitko.de/fileadmin/fitko/foederale-koordination/gremienarbeit/Foederales_IT-Architekturboard/Foederale_IT-Architekturrichtlinien_V1.0.pdf"
    publisher: "Föderale IT-Kooperation (FITKO)"
  - title: "Kompass der föderalen IT-Architektur"
    url: "https://docs.fitko.de/resources/kompass/"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-08-28"
  - title: "FITKO | Föderale IT-Architektur"
    url: "https://www.fitko.de/foederale-it-architektur"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-08-28"
---

# Föderale IT-Architekturrichtlinien

> **Re-verified 2026-08-28.** Four of five cited pages were read directly.
> The fifth, the Version 1.0 PDF, returned only encoded binary to the
> fetch tool and could not be read as text this pass; the four HTML pages
> read directly are internally consistent and add a previously-unrecorded
> fact (Decision 2021/37 making the guidelines binding, distinct from the
> 2025/17 decision that adopted version 1.9.0). `verification:
> primary-source`.

## Description

The Föderale IT-Architekturrichtlinien are the architecture guidelines for
the German federal IT landscape — "decision-making aids for designing and
developing IT architectures," per docs.fitko.de's own policy page, read
directly this pass, meant to streamline recurring architectural choices and
prevent repeated foundational discussions.

The **föderales IT-Architekturboard** — confirmed directly this pass to
have been **established by IT-Planungsrat decision on 22 February 2021** —
defines them and develops them further. FITKO's own page on the board,
read directly, confirms it is made up of representatives of FITKO, the
federal government (now the Bundesministerium für Digitales und
Staatsmodernisierung), the Länder, and one representative plus one deputy
from the municipal peak associations, and that it meets roughly every
eight weeks. FITKO both chairs the board and initiated its establishment.

Two separate IT-Planungsrat decisions are now recorded, not one:
**decision 2021/37** made the guidelines' application **binding** on all
ongoing and new projects affecting the federal IT landscape, and
**decision 2025/17** later adopted the current **version 1.9.0**. The
earlier text recorded only the second decision; the first was found this
pass on docs.fitko.de's own policy page.

They sit within a wider documentation set, the **Kompass der föderalen
IT-Architektur** — confirmed directly this pass to give "an overview over
all essential components of the federal IT architecture: from
administrative law and political questions, via access portals, basic
services to data standards and transport systems," and built as a
collaboratively maintained resource.

## Germany's NORA-shaped entity, with one important difference

This is the closest German counterpart to [[NL-NORA]]: the reference
architecture governing public-sector IT, maintained by a central
coordinating body, sitting above a family of standards.

The difference is in binding force, and it is worth stating because it is
the kind of thing an Atlas flattens if it is not careful. The Dutch model
binds through [[NL-PAS-TOE-OF-LEG-UIT]] — a comply-or-explain policy
applied to a published list of open standards. The German guidelines bind
by their own terms — now sourced to a specific decision, 2021/37 — applying
to *all* projects affecting the federal IT landscape, adopted by a
Bund-Länder council.

**No relationship to [[NL-NORA]] is asserted.** Two reference
architectures are not related merely by being reference architectures.

## What is not recorded

The **content** of the guidelines. Even with four of five sources now read
directly, no page states what version 1.9.0 requires substantively, only
that the Architekturboard "describes and continues" them.
`coverage: medium` reflects that this entity records the guidelines'
existence, custody, governance and versioning in more depth than before
this pass, but still not their substance.

The version number is recorded in prose rather than in a field, because the
Atlas has no version field and `previous_version` is reserved for
superseded *entities*, not for revisions of a living document. Multiple
versions preceded 1.9.0 (the PDF cited is itself version 1.0, from 29
October 2021 per its own fetch metadata) and none is an Atlas entity —
correctly, since they are revisions rather than distinct instruments.

## Relationships

- Maintained by [[DE-FITKO]] — confirmed directly this pass,
  `confidence: high`.

Inbound: [[DE-IT-PLANUNGSRAT]] `produces` this framework — the council
adopts (and, per this pass's finding, separately made binding), the board
drafts, and both facts are recorded on the side that states them.

## Sources

Listed in frontmatter — all five are FITKO pages. Self-sourcing again,
though for a framework the maintaining body publishes, the maintainer's own
documentation is the primary source rather than a substitute for one. Four
of five were read as HTML text this pass; the PDF returned only binary to
the fetch tool.
