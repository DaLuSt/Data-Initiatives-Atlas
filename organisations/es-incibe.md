---
id: ES-INCIBE
type: organisation
name: Instituto Nacional de Ciberseguridad
alternative_names:
  - INCIBE
  - Spanish National Cybersecurity Institute
description: >
  Spanish national cybersecurity body, belonging to the Ministry for Digital
  Transformation and the Civil Service through the State Secretariat for
  Telecommunications and Digital Infrastructures, and headquartered in León.
  Its work rests on three pillars — threat prevention, incident detection
  and response to cyber attacks — and it strengthens cybersecurity and
  privacy protection across information-society services through research,
  service provision and collaboration with other organisations.

level: national
country: ES
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - ES
  - ES-LCGC
  - ES-CCN
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "INCIBE is the Spanish national cybersecurity body, belonging to the Ministry for Digital Transformation and the Civil Service through the State Secretariat for Telecommunications and Digital Infrastructures (incibe.es). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "What is INCIBE"
    url: "https://www.incibe.es/en/incibe/corporate-information/what-is-incibe"
    publisher: "Instituto Nacional de Ciberseguridad (INCIBE)"
  - title: "INCIBE — portada"
    url: "https://www.incibe.es/"
    publisher: "Instituto Nacional de Ciberseguridad (INCIBE)"
  - title: "Instituto Nacional de Ciberseguridad de España"
    url: "https://ciberseguridad.com/normativa/espana/organismos/incibe/"
    publisher: "Ciberseguridad.com"
  - title: "El Incibe defiende sus competencias en el nuevo Centro Nacional de Ciberseguridad"
    url: "https://www.diariodeleon.es/leon/250115/1778868/incibe-defiende-competencias-nuevo-centro-nacional-ciberseguridad.html"
    publisher: "Diario de León"
---

# INCIBE — Instituto Nacional de Ciberseguridad

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

INCIBE is Spain's national cybersecurity institute, part of the Ministry for
Digital Transformation and the Civil Service through the State Secretariat
for Telecommunications and Digital Infrastructures. It is based in **León**.

Its work rests on three pillars — **prevention** of threats, **detection**
of incidents, and **response** to attacks — with early detection and
coordination with other national and international institutions. It runs an
annual Cybersecurity Summer BootCamp in León with the Organization of
American States, training CERT technicians and law-enforcement officers.

## Spain splits cybersecurity across three bodies, and is about to split it again

Unlike [[FR-ANSSI]] or [[DE-BSI]], Spain has **no single national
cybersecurity authority**. The functions modelled here sit across:

- **INCIBE** — society-facing: citizens, business, research, awareness;
- **[[ES-CCN]]** — the public sector, under the national intelligence
  centre, and technical authority for [[ES-ENS]];
- the Ministry of the Interior and Ministry of Defence, holding further
  competences.

[[ES-LCGC]], the pending NIS2 transposition, would create a **Centro
Nacional de Ciberseguridad** on top of this and redistribute competences
between Interior, Defence (through the CCN) and Digital Transformation. One
cited source reports INCIBE publicly defending its competences in the
proposed new centre.

**No relationship is asserted between INCIBE and [[ES-LCGC]] or
[[ES-CCN]].** The reporting describes an institutional dispute over a bill
that is not in force, and a dispute is not a relationship. The Atlas records
what the arrangement is, not what it is being argued about; when the law
passes, the arrangement becomes modellable.

## Why this is `coverage: low`

INCIBE's founding instrument, its legal form, its relationship to the
earlier INTECO, and its CERT role (INCIBE-CERT) relative to CCN-CERT are all
unrecorded. No source read establishes them, and three of the four
citations here are the organisation's own front matter or press coverage
rather than a constituting document.

## Relationships

None asserted — see above.

## Sources

Listed in frontmatter.
