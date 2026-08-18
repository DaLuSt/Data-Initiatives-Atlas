---
id: ES-ESPANA-DIGITAL-2026
type: strategy
name: España Digital 2026
alternative_names:
  - Agenda España Digital
  - Spain Digital 2026
description: >
  Spain's national digital transformation roadmap, an update to the strategy
  launched in July 2020, revised for the 2026 horizon to align with the
  Recovery Plan. It acts in three dimensions — infrastructure and
  technology, economy, and people — and keeps the ten strategic axes of its
  initial version while adding two new cross-cutting axes: strategic
  high-impact projects through public-private collaboration, and
  co-governance between the State and the Autonomous Communities. Its
  principal areas are connectivity, digital skills, cybersecurity,
  digitalisation of businesses and public services, and the use of emerging
  technologies.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2022-07-05
end_date: 2026-12-31
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - ES-AEAD
related_entities:
  - ES
  - ES-AEAD
  - ES-SGAD
  - ES-AESIA
  - EU-DIGITAL-DECADE
  - NL-DIGIBETER
  - DE-DIGITALSTRATEGIE
relationships:
  - type: applies-in
    target: ES
    source: fact
    evidence: "España Digital 2026 is Spain's national digital transformation roadmap, an update to the strategy launched in July 2020, including an axis on co-governance between the State and the Autonomous Communities (digital.gob.es; lamoncloa.gob.es). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "España Digital 2026 | Portal MTDFP"
    url: "https://digital.gob.es/ministerio/programas/programas-avance-digital/espana-digital-2026"
    publisher: "Ministerio para la Transformación Digital y de la Función Pública"
  - title: "El Gobierno actualiza la Agenda España Digital para el horizonte 2026 y acelera el despliegue de sus inversiones"
    url: "https://planderecuperacion.gob.es/noticias/el-gobierno-actualiza-la-agenda-espana-digital-para-el-horizonte-2026-y-acelera-el-despliegue-de-sus-inversiones"
    publisher: "Plan de Recuperación, Transformación y Resiliencia — Gobierno de España"
  - title: "España Digital 2026 (documento)"
    url: "https://espanadigital.gob.es/sites/espanadigital/files/2022-07/Espa%C3%B1aDigital_2026.pdf"
    publisher: "Gobierno de España"
  - title: "¿En qué consiste la nueva agenda España Digital 2026?"
    url: "https://www.incibe.es/emprendimiento/publicaciones/blog/en-que-consiste-la-nueva-agenda-espana-digital-2026-y-en-que-afecta-los-nuevos"
    publisher: "Instituto Nacional de Ciberseguridad (INCIBE)"
---

# España Digital 2026

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

España Digital 2026 is Spain's national digital transformation roadmap. It
is an **update of the strategy launched in July 2020**, revised in July 2022
for the 2026 horizon, aligned with the Recovery Plan and taking stock after
two years.

It acts in **three dimensions** — infrastructure and technology, economy,
people — and keeps the **ten strategic axes** of the original while adding
**two new cross-cutting axes**:

1. strategic high-impact projects through public-private collaboration
   (PERTE, and the Retech initiative);
2. **co-governance between the State and the Autonomous Communities**.

Its principal areas are connectivity, digital skills, cybersecurity,
digitalisation of businesses and public services, and emerging technologies.

## The second new axis is the one the Atlas cannot model

*Cogobernanza del Estado y las Comunidades Autónomas* is not a footnote —
it is one of two axes added when the strategy was revised, which makes
state–regional co-governance an **explicit, named structural element** of
Spain's digital policy.

The Atlas can record that the axis exists, in this prose. It cannot model a
single one of the parties on the other side of it, because there is no
`level` term between `national` and `local`. See [[ES]].

This is the sharpest form the federal modelling gap has taken across three
affected countries. In Germany the gap hid sixteen Land acts; in Belgium it
hid a Flemish programme. Here it hides **half of a named axis of the
national strategy** — the graph shows the strategy, and shows nothing of the
co-governance the strategy is half about.

## No relationship to the Digital Decade is asserted

[[EU-DIGITAL-DECADE]] sets 2030 targets that member state roadmaps are
expected to serve, and the Spanish strategy is aligned with the Recovery
Plan, which is an EU instrument. It would be easy to draw an edge.

**None is drawn.** No source read connects España Digital 2026 to
[[EU-DIGITAL-DECADE]], and the same refusal was made for
[[NL-DIGIBETER]] and [[DE-DIGITALSTRATEGIE]]. Three national digital
strategies, three refusals, one consistent standard.

The Recovery Plan alignment is likewise not modelled: the Plan is not an
entity in the Atlas, and creating it inside a country batch would put a
major EU instrument into the shared layer on evidence gathered while
researching one member state.

## Relationships

None asserted.

## Sources

Listed in frontmatter — the ministry programme page, the Recovery Plan
announcement of the update, the strategy document itself, and INCIBE's
summary of what it means for cybersecurity.
