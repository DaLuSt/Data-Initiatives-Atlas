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
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading ciberseguridad.com directly (2026-08-26): INCIBE 'depende del Ministerio de Asuntos Económicos y Transformación digital' (a public body dependent on the Ministry of Economic Affairs and Digital Transformation) — a ministry name that has evolved since this entity's original 'Ministry for Digital Transformation and the Civil Service' description; both refer to the same digital-portfolio ministry across different government terms. incibe.es's own page, also read directly, confirms INCIBE's role and structure. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "What is INCIBE"
    url: "https://www.incibe.es/en/incibe/corporate-information/what-is-incibe"
    publisher: "Instituto Nacional de Ciberseguridad (INCIBE)"
    accessed: "2026-08-26"
  - title: "INCIBE — portada"
    url: "https://www.incibe.es/"
    publisher: "Instituto Nacional de Ciberseguridad (INCIBE)"
  - title: "Instituto Nacional de Ciberseguridad de España"
    url: "https://ciberseguridad.com/normativa/espana/organismos/incibe/"
    publisher: "Ciberseguridad.com"
    accessed: "2026-08-26"
  - title: "El Incibe defiende sus competencias en el nuevo Centro Nacional de Ciberseguridad"
    url: "https://www.diariodeleon.es/leon/250115/1778868/incibe-defiende-competencias-nuevo-centro-nacional-ciberseguridad.html"
    publisher: "Diario de León"
    accessed: "2026-08-26"
---

# INCIBE — Instituto Nacional de Ciberseguridad

> **Verified 2026-08-26.** Three of four cited pages were read directly.
> INCIBE's relationship to its predecessor INTECO — previously flagged
> as unrecorded — is now established, and the "defends its competences"
> framing is nuanced by a closer reading of the press report. See below.

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
between Interior, Defence (through the CCN) and Digital Transformation.
**Nuanced this pass**: reading the cited Diario de León article directly
shows a more procedural picture than "defending its competences" implied
— INCIBE is reported preparing formal *alegaciones* (submissions) during
the bill's development phase, alongside other affected bodies, and would
retain INCIBE-CERT's private-sector role within the new structure, rather
than contesting the reform outright.

**No relationship is asserted between INCIBE and [[ES-LCGC]] or
[[ES-CCN]].** The reporting describes an institutional process over a bill
that is not in force, and a submission process is not a relationship. The
Atlas records what the arrangement is, not what it is being argued about;
when the law passes, the arrangement becomes modellable.

## INTECO, now on the record

Previously flagged as unrecorded. Confirmed by reading ciberseguridad.com
directly: INCIBE "fue creado en el 2006 con el nombre de Instituto
Nacional de Tecnologías de la Comunicación (INTECO)" (was created in 2006
under the name INTECO), refocused exclusively on cybersecurity in 2012,
and was renamed INCIBE in 2014. This is a continuous institution renamed
twice, not a succession between distinct bodies — no `previous_version`
or `successor` field is warranted, unlike [[ES-SGAD]] → [[ES-AEAD]].

## `coverage: medium`, up from `low`

INCIBE's founding instrument (a specific decree for the 2006 creation)
and its CERT role (INCIBE-CERT) relative to CCN-CERT remain unrecorded.
What is now established: the founding year and name history, and the
current ministry attachment.

## Relationships

None asserted — see above.

## Sources

Listed in frontmatter, three of four read directly this pass.
