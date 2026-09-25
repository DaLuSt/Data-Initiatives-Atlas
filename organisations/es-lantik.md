---
id: ES-LANTIK
type: organisation
name: Lantik
alternative_names:
  - LANTIK
  - Lantik Sociedad Anónima Medio Propio
description: >
  Provincial IT company for Bizkaia, in the Basque Country, constituted
  in 1981 by the Diputación Foral de Bizkaia as a sociedad anónima. It
  holds the status of medio propio (personified own-resource) for the
  Diputación Foral de Bizkaia, ascribed to its Department of Public
  Administration and Institutional Relations, providing information
  systems and technology services to the provincial government, its
  dependent bodies, and Bizkaia's municipalities. Reported as the fourth
  of four public IT companies — with EJIE, CCASA and IZFE — that
  jointly constitute the Interoperability and Security Node of the
  Administrations of Euskadi (NISAE).

level: subnational
country: ES
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-25"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES
  - ES-EJIE
  - ES-CCASA
  - ES-IZFE
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "The Diputación Foral de Bizkaia's own bizkaia.eus domain family (lantik.bizkaia.eus, www.bizkaia.eus, gardentasuna.bizkaia.eus) returned HTTP 503 on every attempt this pass (five distinct URLs, 2026-09-25), matching the block already logged in discovery/unresolved.md row #175 (first found 2026-09-20, 503 on six URLs) — no government-side source could be read directly despite the retry. Two independent sources were read directly instead: tdigitaleuskadi.wikitoki.org (a Basque civic-tech/digital-transition site), which states Lantik is a 'sociedad mercantil foral' constituted in 1981, holding the status of 'Medio Propio personificado' (personified own-resource) of the Diputación Foral de Bizkaia, ascribed to its Department of Public Administration and Institutional Relations; and axesor.es, a commercial-registry information service, which independently confirms the Sociedad Anónima legal form, CIF A48119820, and a Bilbao registered address. A second registry aggregator (empresia.es) corroborates the legal form but gives no incorporation date; axesor.es and a search-indexed registry snippet disagree on the exact incorporation day (22 vs 27 August 1981), so only the year is asserted, not the day. Anchor edge under metadata/relationship-types.md §2.3, asserting Biscayan (provincial/foral) sub-federal scope via `level: subnational` — completing the fourth and last of the four NISAE Basque provincial-level IT companies in this Atlas, alongside [[ES-EJIE]] (Basque Government), [[ES-IZFE]] (Gipuzkoa) and [[ES-CCASA]] (Álava). `confidence: medium`, one tier below its three siblings' `high`, since neither source read this pass is the entity's own page or its owning government's page — the persistent bizkaia.eus block leaves no government-side citation available for this entity specifically."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Lantik — Transición Digital en Euskadi"
    url: "https://tdigitaleuskadi.wikitoki.org/lantik/"
    publisher: "Wikitoki"
    accessed: "2026-09-25"
  - title: "Lantik S. A Medio Propio — Informe Mercantil, Financiero y de Riesgo"
    url: "https://www.axesor.es/Informes-Empresas/275981/LANTIK_SOCIEDAD_ANONIMA_MEDIO_PROPIO.html"
    publisher: "Axesor"
    accessed: "2026-09-25"
---

# Lantik

> **Created 2026-09-25**, closing `discovery/unresolved.md` item #5's
> last open Basque NISAE gap — the fourth and final of the four
> provincial IT companies, after [[ES-EJIE]], [[ES-CCASA]] and
> [[ES-IZFE]]. `bizkaia.eus` remained fully blocked on a fresh attempt
> (five URLs, all HTTP 503); sourced instead from an independent
> civic-tech site and a commercial company registry, both read directly.

## Description

Lantik is **Bizkaia's** own provincial IT company, constituted in
**1981** as a *sociedad anónima* by the **Diputación Foral de Bizkaia**.
It holds the status of ***medio propio* personificado** (personified
own-resource) for the Diputación, ascribed to its Department of Public
Administration and Institutional Relations, and provides information
systems and technology services to the provincial government, its
dependent bodies, and Bizkaia's municipalities.

## `bizkaia.eus` remains fully blocked

Every URL in the `bizkaia.eus` domain family tried this pass —
`lantik.bizkaia.eus/es/conocenos`, `lantik.bizkaia.eus`,
`www.bizkaia.eus/es/lantik`, a `www.bizkaia.eus` budget-memoria PDF, and
`gardentasuna.bizkaia.eus` — returned **HTTP 503**, the same result
`discovery/unresolved.md` row #175 already recorded on 2026-09-20. This
is now confirmed blocked across two separate sessions five days apart,
strengthening the case that it is a genuine, sustained outage or block
rather than a transient one. No workaround was found.

## Sourced from independent registry and civic-tech sites instead

With the government-side source unavailable, two independently reachable
sources supplied the entity's facts. **tdigitaleuskadi.wikitoki.org**, a
Basque civic-tech site tracking the region's digital transition, states
Lantik is a "sociedad mercantil foral" — a public mercantile company —
holding *medio propio personificado* status for the Diputación Foral de
Bizkaia. **axesor.es**, a commercial mercantile-registry information
service, independently confirms the *Sociedad Anónima* legal form, CIF
`A48119820`, and a Bilbao registered address. Two registry aggregators
disagree on the exact incorporation day within August 1981 (22nd vs.
27th), so `start_date` is left `null` rather than guessed — only the
year is asserted.

Because neither source is Lantik's own page or its owning government's
page, this entity carries `confidence: medium`, one tier below
[[ES-EJIE]], [[ES-CCASA]] and [[ES-IZFE]]'s `high` — an honest reflection
of the weaker sourcing tier the persistent block leaves available, not a
claim about the facts' likely accuracy.

## The fourth of four Basque NISAE companies

[[ES-EJIE]], [[ES-CCASA]] and [[ES-IZFE]] each independently describe
Lantik as their remaining co-member in the **Nodo de Interoperabilidad y
Seguridad de las Administraciones de Euskadi (NISAE)**, the platform
joining the Basque Government and all three Provincial Councils (Álava,
Bizkaia, Gipuzkoa). This entity's own attempt to re-verify that fact
directly against euskadi.eus's NISAE documentation page this pass did
not surface a sentence naming Lantik specifically — the page loaded but
its visible content named only EJIE's supporting infrastructure — so the
NISAE-membership claim is recorded here only as what the three sibling
entities already state, not as a fact independently re-confirmed by this
entity's own sources.

## Relationships

- `part-of` [[ES]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, both read directly.
