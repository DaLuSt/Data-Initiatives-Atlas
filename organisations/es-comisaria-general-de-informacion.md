---
id: ES-COMISARIA-GENERAL-DE-INFORMACION
type: organisation
name: Comisaría General de Información
alternative_names:
  - CGI
  - General Commissariat of Information
description: >
  The Spanish National Police's information and counter-terrorism
  intelligence directorate, part of the Dirección General de la Policía.
  Its statutory function is the capture, reception, processing and
  development of information of interest for public order and public
  security within the scope of the Dirección General's functions, and its
  operational exploitation, especially in counter-terrorism matters,
  domestically and internationally. Its own internal composition is set
  by a classified "Orden Comunicada" rather than a published order, under
  Council of Ministers agreements dating to 1986, 1996 and 2014, governed
  by the Ley de Secretos Oficiales.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - ES-CNI
  - ES
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #193. Confirmed by reading the BOE's own consolidated text of Real Decreto 734/2020 directly (boe.es/diario_boe/txt.php?id=BOE-A-2020-9138, 2026-09-19), Article 3.3.a): 'A la Comisaría General de Información, la captación, recepción, tratamiento y desarrollo de la información de interés para el orden y la seguridad pública en el ámbito de las funciones de la Dirección General, así como su explotación o aprovechamiento operativo, especialmente en materia antiterrorista, tanto en el ámbito nacional como en el internacional' — capture, reception, processing and development of information of interest for public order and public security, and its operational exploitation, especially in counter-terrorism matters, nationally and internationally. The BOE's own text of Orden INT/859/2023, also read directly, Article 5, confirms the Comisaría General de Información 'asume las funciones contempladas en el artículo 3.3.a) del Real Decreto 734/2020' and states its internal composition is fixed by a classified Orden Comunicada under Council of Ministers agreements of 1986, 1996 and 2014, governed by the Ley de Secretos Oficiales — the same secrecy regime other Atlas intelligence bodies' governance sits behind. Scope anchor under metadata/relationship-types.md §2.3: the Dirección General de la Policía itself is not an Atlas entity, so the edge targets the country."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Real Decreto 734/2020, de 4 de agosto, por el que se desarrolla la estructura orgánica básica del Ministerio del Interior"
    url: "https://www.boe.es/diario_boe/txt.php?id=BOE-A-2020-9138"
    publisher: "Agencia Estatal Boletín Oficial del Estado (BOE)"
    accessed: "2026-09-19"
  - title: "Orden INT/859/2023, de 21 de julio, por la que se desarrolla la estructura orgánica y funciones de los servicios centrales y territoriales de la Dirección General de la Policía"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2023-17072"
    publisher: "Agencia Estatal Boletín Oficial del Estado (BOE)"
    accessed: "2026-09-19"
---

# Comisaría General de Información (National Police)

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #193 (the National Police's and Guardia Civil's information services,
> flagged as unresearched on both [[ES-CNI]] and [[ES-CIFAS]]). Sourced
> from the BOE's own texts of Real Decreto 734/2020 and Orden INT/859/2023,
> both read directly.

## Description

The Comisaría General de Información is the National Police's own
information and counter-terrorism intelligence directorate, within the
**Dirección General de la Policía**. Confirmed by reading the BOE's own
consolidated text of **Real Decreto 734/2020** directly, Article 3.3.a):
it is responsible for "the capture, reception, processing and development
of information of interest for public order and public security... and its
operational exploitation, especially in counter-terrorism matters, both
domestically and internationally."

## A composition the law does not publish

**Orden INT/859/2023**, read directly, Article 5, confirms the
Comisaría General "assumes the functions contemplated in Article 3.3.a) of
Real Decreto 734/2020" but goes no further: its internal structure is set
by a classified **Orden Comunicada**, under Council of Ministers agreements
dating to **1986, 1996 and 2014**, governed by the **Ley de Secretos
Oficiales** (Official Secrets Act). This is not a retrieval gap — the
composition is deliberately unpublished, the same kind of statutory
opacity other Atlas intelligence bodies' governing texts show in other
ways.

## Not modelled

- The **common inspection regime** [[ES-CNI]]'s own entity says covers
  Spain's intelligence bodies generally — not researched this pass.
- The **Dirección General de la Policía** itself as an organisation
  entity.
- The classified **Orden Comunicada** and the 1986/1996/2014 Council of
  Ministers agreements it rests on — unpublished by design.

## Relationships

- `part-of` [[ES]] — anchor; the Dirección General de la Policía itself
  is not an Atlas entity.

## Sources

Listed in frontmatter, both read directly.
