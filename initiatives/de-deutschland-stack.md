---
id: DE-DEUTSCHLAND-STACK
type: initiative
name: Deutschland-Stack
alternative_names:
  - Germany Stack
description: >
  German national initiative to build a sovereign technology platform of
  shared, interoperable digital components ("Basiskomponenten") for the
  federal government, the Länder and the municipalities, targeted at a
  secure and interoperable ecosystem for digital applications by 2028. It
  is driven by the Bundesministerium für Digitales und Staatsmodernisierung
  through a dedicated department and has been developed through public
  consultation.

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
  - DE-BMDS
related_entities:
  - DE-MODERNISIERUNGSAGENDA-BUND
relationships:
  - type: maintained-by
    target: DE-BMDS
    source: fact
    evidence: "Implementation of the Deutschland-Stack is driven by the BMDS, whose department 'DS' is to develop the stack across three dimensions — technology, governance and policy (bmds.bund.de/themen/digitaler-staat/deutschland-stack; netzpolitik.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Deutschland-Stack"
    url: "https://bmds.bund.de/themen/digitaler-staat/deutschland-stack"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
  - title: "Deutschland-Stack Sachstand"
    url: "https://bmds.bund.de/fileadmin/BMDS/Dokumente/260129_Deutschland-Stack_Standard_barrierefrei.pdf"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
  - title: "Deutschland-Stack: Was ist drin, im Baukasten für die digitale Verwaltung?"
    url: "https://netzpolitik.org/2025/deutschland-stack-was-ist-drin-im-baukausten-fuer-die-digitale-verwaltung/"
    publisher: "netzpolitik.org"
  - title: "2. Konsultation zum Deutschland-Stack durch das BMDS"
    url: "https://www.security-insider.de/umsetzung-deutschland-stack-bmds-analyse-konsultation-a-0b3f4294ba36bae4c3e30e1658660253/"
    publisher: "Security-Insider"
---

# Deutschland-Stack

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Deutschland-Stack is described as a **national, sovereign technology
platform** intended to serve as the foundation for digital modernisation
across the Bund, the Länder and the Kommunen, with a target of a secure,
interoperable ecosystem for digital applications **by 2028**.

Its stated design principles are sovereign, European-compatible and
interoperable digital components built on **open international standards**,
with an ecosystem of open innovation and the integration of existing
national and European building blocks rather than replacement of them.

The federal government calls the foundational services **Basiskomponenten**
and intends to provide them itself for the first time, so that Land and
municipal administrations can reuse them. Named examples in the sources
include base services for payments, cloud solutions and digitalisation
platforms.

[[DE-BMDS]] drives implementation through a department designated **DS**,
tasked with working the stack out in three dimensions: technology,
governance and policy.

## Why `status: active` rather than `planned`

The stack itself does not exist — the target date is 2028. But `planned` in
this Atlas means adopted-but-not-started, and that would understate what is
sourced: a dedicated BMDS department established in August 2025, at least
two public consultations, and a published Sachstand ("state of play")
document. The programme of work is running even though the artefact is not
built. This is the same judgement made for other in-flight initiatives, and
it is the field most worth re-checking when sources become readable.

## Relation to the Dutch layer

The Deutschland-Stack's "Basiskomponenten" concept is the closest German
analogue to the Dutch [[NL-GDI]] (Generieke Digitale Infrastructuur) and to
[[NL-COMMON-GROUND]]'s component-based model. **No relationship is
asserted** — the resemblance is an Atlas observation and no source connects
them.

The same caution applies more sharply to a tempting link that was
**refused**: the stack's commitment to "existing national and European
building blocks" and "open international standards" reads like a reference
to the EU interoperability agenda ([[EU-EIF]],
[[EU-INTEROPERABLE-EUROPE-ACT]]), but no source read names either.

## Relationships

- Maintained by [[DE-BMDS]].

## Sources

Listed in frontmatter. Note that two of the four are trade or advocacy
press (netzpolitik.org, Security-Insider) rather than government sources —
secondary, and low in the README's preference order. The two BMDS sources
carry the weight here.
