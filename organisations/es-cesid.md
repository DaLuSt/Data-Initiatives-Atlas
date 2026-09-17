---
id: ES-CESID
type: organisation
name: Centro Superior de Información de la Defensa
alternative_names:
  - CESID
  - Higher Centre for Defence Information
description: >
  Spain's national intelligence service from 1977 to 2002, created by Real
  Decreto 1558/1977 reporting directly to the Ministry of Defence, and
  suppressed by Ley 11/2002 when its functions passed to the newly created
  Centro Nacional de Inteligencia (CNI).

level: national
country: ES
region: null

status: superseded
confidence: high
coverage: low
verification: primary-source

start_date: "1977-07-04"
end_date: "2002-05-06"
last_verified: "2026-09-17"
previous_version: null
successor: ES-CNI

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - ES-CNI
  - ES-LEY-11-2002
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Confirmed by reading the BOE's own text of Real Decreto 1558/1977 directly (2026-09-17), Article 2.5: 'Bajo la dependencia directa del titular del Departamento se crea el Centro Superior de Información de la Defensa' (created under the direct dependence of the head of the Department — the Ministry of Defence)."
    confidence: high
    valid_from: "1977-07-04"
    valid_until: "2002-05-06"

sources:
  - title: "Real Decreto 1558/1977, de 4 de julio, por el que se reestructuran determinados Órganos de la Administración Central del Estado (BOE-A-1977-15200)"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-1977-15200"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-09-17"
  - title: "Ley 11/2002, de 6 de mayo, reguladora del Centro Nacional de Inteligencia (BOE-A-2002-8628)"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2002-8628"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-09-17"
---

# Centro Superior de Información de la Defensa (CESID)

> **Created 2026-09-17**, closing a gap named on [[ES-CNI]]'s and
> [[ES-LEY-11-2002]]'s own files: both cited es.wikipedia.org for CESID's
> existence but left "the 2002 reform's substance... not researched."
> Two BOE texts, read directly, close it with the strongest possible
> citation — the creating and suppressing acts themselves.

## Description

Confirmed by reading the BOE's own text of **Real Decreto 1558/1977, de 4
de julio** directly: Article 2.5 creates the Centro Superior de
Información de la Defensa "bajo la dependencia directa del titular del
Departamento" (Ministry of Defence). The decree restructures several
central government bodies at once and does not itself name which prior
information services CESID absorbed — secondary sources (not read
directly this pass) describe it as replacing the Presidencia del
Gobierno's Servicio Central de Documentación (SECED) and the high
command's Tercera Sección de Información (SIAEM/SIAM), but that claim is
not asserted here on the strength of an unread source.

## Suppressed by name, in [[ES-LEY-11-2002]]'s own text

Confirmed by reading **Ley 11/2002**'s own text directly at boe.es
(BOE-A-2002-8628): its **Disposición adicional segunda** states, in its
own words, "Queda suprimido el Centro Superior de Información de la
Defensa" (the CESID is hereby suppressed), followed immediately by "El
Centro Nacional de Inteligencia sucederá al Centro Superior de
Información de la Defensa en el ejercicio de sus funciones" (the CNI
shall succeed the CESID in the exercise of its functions) — explicit
statutory succession language, not merely a shared subject-matter
resemblance. `end_date` is set to 2002-05-06, [[ES-CNI]]'s own
`start_date`, matching this Act's own date.

## Relationships

- `part-of` [[ES]] — scope anchor.

[[ES-CNI]] now carries `supersedes` → this entity and
`previous_version: ES-CESID`, matching the Atlas's succession
convention.

## Not modelled

- The predecessor bodies CESID itself is reported (via secondary sources,
  not read directly) to have absorbed — SECED and SIAEM/SIAM — one layer
  further back than this pass researched.
- CESID's own internal history and any amending decrees across its
  25-year existence.

## Sources

Two of two read directly: the BOE's own texts of the creating decree
(1977) and the suppressing/succession act (2002).
