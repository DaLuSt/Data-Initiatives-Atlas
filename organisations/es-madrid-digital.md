---
id: ES-MADRID-DIGITAL
type: organisation
name: Agencia para la Administración Digital de la Comunidad de Madrid
alternative_names:
  - Madrid Digital
  - Informática de la Comunidad de Madrid
  - ICM
  - Agencia de Informática y Comunicaciones de la Comunidad de Madrid
  - Empresa Provincial de Informática de Madrid
  - EPIMSA
  - Servicios Provinciales de Informática
  - SERPI
description: >
  Madrid's own regional IT and digital-transformation agency, tracing a
  continuous institutional line from the Madrid Provincial Council's
  Servicios Provinciales de Informática (SERPI, 1980) through Empresa
  Provincial de Informática de Madrid (EPIMSA, 1982, transferred to the
  newly-created Autonomous Community of Madrid in 1983), Informática de
  la Comunidad de Madrid (ICM, renamed 1990, converted to an Organismo
  Autónomo in 1997), the Agencia de Informática y Comunicaciones de la
  Comunidad de Madrid (established as an "ente público" by Ley 7/2005,
  de 23 de diciembre, de medidas fiscales y administrativas), and
  finally Madrid Digital, its current name. It manages IT infrastructure,
  digital services, cybersecurity and innovation across all of the
  Comunidad de Madrid's regional government departments.

level: subnational
country: ES
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES
  - ES-AOC
  - ES-EJIE
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "Confirmed by reading comunidad.madrid's own 'Madrid Digital' page directly (2026-09-20), which gives the full institutional chain: Servicios Provinciales de Informática (SERPI), created by the Madrid Provincial Council in 1980; transformed into Empresa Provincial de Informática de Madrid, S.A. (EPIMSA) in 1982; transferred to the newly-created Autonomous Community of Madrid's control in 1983 (the Provincial Council having been dissolved and its responsibilities assumed by the Community); renamed Informática de la Comunidad de Madrid (ICM) in 1990; converted into an Organismo Autónomo in 1997; established as an ente público, the Agencia de Informática y Comunicaciones de la Comunidad de Madrid, in 2005; renamed Madrid Digital as its current form. boe.es's own text of Ley 7/2005, de 23 de diciembre, de medidas fiscales y administrativas (read directly, 2026-09-20), corroborates the 2005 transformation in its Article 10 (now substantially amended by later laws but confirming the agency's creation as a public entity with its own legal capacity for managing digital administration, technology and communications). Anchor edge under metadata/relationship-types.md §2.3, asserting Madrid (Comunidad Autónoma) sub-federal scope via `level: subnational` — the fourth Spanish Comunidad-level or provincial IT body in this Atlas after [[ES-AOC]] (Catalonia), [[ES-EJIE]] (Basque Country) and [[ES-IZFE]]/[[ES-CCASA]] (Gipuzkoa/Álava, sub-Comunidad provincial bodies)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Madrid Digital — Comunidad de Madrid"
    url: "https://www.comunidad.madrid/servicios/sede-electronica/madrid-digital"
    publisher: "Comunidad de Madrid"
    accessed: "2026-09-20"
  - title: "BOE-A-2006-3668 Ley 7/2005, de 23 de diciembre, de medidas fiscales y administrativas"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2006-3668"
    publisher: "Agencia Estatal Boletín Oficial del Estado (BOE)"
    accessed: "2026-09-20"
---

# Agencia para la Administración Digital de la Comunidad de Madrid (Madrid Digital)

> **Created 2026-09-20**, further narrowing `discovery/unresolved.md`
> item #5 — the fourth Spanish sub-national digital-government body in
> this Atlas, alongside [[ES-AOC]], [[ES-EJIE]], [[ES-IZFE]] and
> [[ES-CCASA]]. Sourced from the Comunidad de Madrid's own "Madrid
> Digital" page and the BOE's own text of Ley 7/2005, both read
> directly.

## Description

Madrid Digital is the Comunidad de Madrid's own regional IT and
digital-transformation agency — the longest and most heavily-renamed
institutional history of any entity in this Atlas's sub-national batch.
Confirmed directly on the Comunidad's own page, the chain runs:

| Year | Name / status |
|---|---|
| 1980 | **SERPI** (Servicios Provinciales de Informática), created by the Madrid Provincial Council |
| 1982 | **EPIMSA** (Empresa Provincial de Informática de Madrid, S.A.) |
| 1983 | Transferred to the newly-created **Autonomous Community of Madrid** |
| 1990 | Renamed **ICM** (Informática de la Comunidad de Madrid) |
| 1997 | Converted into an **Organismo Autónomo** |
| 2005 | Established as an **ente público**, the Agencia de Informática y Comunicaciones de la Comunidad de Madrid, by **Ley 7/2005** |
| current | Renamed **Madrid Digital** |

## One entity, not several

Six names across 45 years is more than any other entity in this Atlas's
German or Spanish sub-national batch, but the Comunidad's own account
describes continuous institutional succession — the same organisation
changing legal form and name, not a series of distinct bodies replacing
each other. Matching the treatment already given to [[DE-BUNDID]]
(rename, not succession) and [[ES-CNI]] (a genuine `supersedes` case, by
contrast, where the predecessor was explicitly dissolved by name), this
entity is modelled once, with the full name chain in
`alternative_names` and the history in prose, rather than split into six
nodes.

## `start_date` left `null`

Per the convention formalised 2026-09-20
(`metadata/metadata-schema.md`): no single date cleanly answers "when was
this entity founded" across six transformations, several of which
(1983, 1997, "current") are given only by year. Rather than pick one
transformation arbitrarily as the `start_date`, it is left `null` and
the full table above carries the precision the sources actually support.

## Confirmed directly on the law itself

BOE's own text of **Ley 7/2005, de 23 de diciembre, de medidas fiscales
y administrativas**, read directly, corroborates the 2005 transformation
in its Article 10 — now substantially amended by later Madrid laws
(reflecting the subsequent renaming to Madrid Digital), but confirming
the 2005 creation of a public entity with its own legal capacity for
digital administration, technology and communications.

## Not modelled

- The exact law renaming the Agencia de Informática y Comunicaciones to
  Madrid Digital — not independently confirmed this pass; the current
  name is sourced from the Comunidad's own page only.
- Madrid Digital's internal organisation and specific digital-service
  portfolio.

## Relationships

- `part-of` [[ES]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, both read directly.
