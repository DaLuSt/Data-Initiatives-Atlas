---
id: ES-CIFAS
type: organisation
name: Centro de Inteligencia de las Fuerzas Armadas
alternative_names:
  - CIFAS
  - Armed Forces Intelligence Centre
description: >
  Spain's military intelligence service, part of the Estado Mayor de la
  Defensa (EMAD). It provides the Minister of Defence, through the Jefe
  de Estado Mayor de la Defensa (JEMAD), and military authorities with
  military intelligence, and is the sole joint authority on military
  intelligence and electronic warfare at the strategic and operational
  levels. Its Director must be a General Officer from the Armed Forces
  or the Navy.

level: national
country: ES
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2005-04-19
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - ES-ORDEN-DEF-1076-2005
  - ES-CNI
  - ES
relationships:
  - type: governed-by
    target: ES-ORDEN-DEF-1076-2005
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP. Confirmed by reading the BOE's own text of Orden DEF/1076/2005 directly (2026-09-06): its Article Sexto is dedicated entirely to CIFAS, describing its functions, joint character ('carácter conjunto, será único en materia de información e inteligencia militar en los niveles estratégico y operacional'), and the rule that its Director must be a General Officer from the Armed Forces or the Navy ('perteneciente a los Ejércitos o la Armada')."
    confidence: high
    valid_from: 2005-04-19
    valid_until: null
  - type: part-of
    target: ES
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. CIFAS sits within the Estado Mayor de la Defensa, which is not itself an Atlas entity, so the anchor targets the country. Confirmed by reading defensa.gob.es's own organigrama page directly (2026-09-06): CIFAS reports through the JEMAD to the Minister of Defence."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Centro de Inteligencia de las Fuerzas Armadas"
    url: "https://www.defensa.gob.es/ministerio/organigrama/emad/cifas/"
    publisher: "Ministerio de Defensa de España"
    accessed: "2026-09-06"
  - title: "Orden DEF/1076/2005, de 19 de abril, por la que se desarrolla la estructura del Estado Mayor de la Defensa"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2005-6655"
    publisher: "Agencia Estatal Boletín Oficial del Estado (BOE)"
    accessed: "2026-09-06"
  - title: "Centro de Inteligencia de las Fuerzas Armadas"
    url: "https://es.wikipedia.org/wiki/Centro_de_Inteligencia_de_las_Fuerzas_Armadas"
    publisher: "Wikipedia"
    accessed: "2026-09-06"
---

# Centro de Inteligencia de las Fuerzas Armadas (CIFAS)

> **Created 2026-09-06**, closing a gap [[ES-CNI]]'s own entity flagged
> under "Not modelled": "CIFAS, the armed forces' intelligence centre...
> none was researched." Spain's national-security picture now has two
> services — [[ES-CNI]] for general national intelligence and CIFAS for
> military intelligence — the same civilian/military split every other
> Atlas country in the intelligence-services batch carries, which
> [[ES-CNI]]'s own entity had previously called out as a genuine
> exception.

## Description

Confirmed by reading defensa.gob.es's own page directly: CIFAS is "el
órgano responsable de facilitar a la persona titular del Ministerio de
Defensa, a través del jefe de Estado Mayor de la Defensa, y a las
autoridades militares, la inteligencia militar precisa" — the body
responsible for providing the Defence Minister, through the JEMAD, and
military authorities with military intelligence. It advises the JEMAD
and the Chiefs of Staff of the Armed Forces on military
counter-intelligence.

Confirmed by reading the BOE's own text of Orden DEF/1076/2005 directly:
CIFAS has "carácter conjunto, será único en materia de información e
inteligencia militar en los niveles estratégico y operacional" — a joint
character, the sole authority on military intelligence at the strategic
and operational levels — and directs the exploitation of joint and
specific intelligence and electronic-warfare systems. Its Director must
be a General Officer from the Armed Forces or the Navy.

## Not the 1973 body of the same acronym

A distinct, older "Comisión Informática de las Fuerzas Armadas" also used
the acronym CIFAS, created by Decreto 2908/1973 and transferred to the
Ministry of Defence in 1979 (Orden of 21 April 1979, BOE-A-1979-11035).
That body is unrelated to this entity — a computing commission, not an
intelligence service — and is not modelled here.

## Relationships

- `governed-by` [[ES-ORDEN-DEF-1076-2005]].
- `part-of` [[ES]] — anchor; its immediate parent, the Estado Mayor de la
  Defensa, is not an Atlas entity.

## Not modelled

- The **Estado Mayor de la Defensa (EMAD)** itself.
- The information services of the **National Police** and **Guardia
  Civil**, and the common inspection regime [[ES-CNI]]'s own entity
  mentions covering all of Spain's intelligence bodies — not researched
  this pass.

## Sources

Listed in frontmatter, all three read directly 2026-09-06.
