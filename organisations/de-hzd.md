---
id: DE-HZD
type: organisation
name: Hessische Zentrale für Datenverarbeitung
alternative_names:
  - HZD
description: >
  Hesse's central IT service provider, established when the Hessisches
  Datenverarbeitungsverbundgesetz (Hessian Data-Processing Association
  Act) came into force in 1970, initially as a data-processing authority
  under the Hessian State Chancellery (moved to the Interior Ministry's
  administration in 1977). Became a Landesbetrieb (state enterprise)
  under §26 of the Hessische Landeshaushaltsordnung (Hessian State
  Budget Ordinance) in 1989, ending state subsidies and making its
  services fee-based. It is the state's full-service IT provider,
  covering infrastructure, software development, project management,
  IT security, training and consulting for Hesse's state administration.

level: subnational
country: DE
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
  - DE
  - DE-IT-NRW
  - DE-AKDB
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Confirmed by reading hzd.hessen.de's own '55 Jahre HZD' chronicle pages directly (2026-09-20): a formal contract between the Land and municipal parties was signed 12 May 1969 proposing the organisational vehicle, and the Hessisches Datenverarbeitungsverbundgesetz came into force in 1970 establishing HZD (de.wikipedia.org, also read directly, independently confirms the statute's name and 1970 date, and adds that HZD 'wurde Landesbetrieb nach §26 der Hessischen Landeshaushaltsordnung' in 1989). hzd.hessen.de's own chronicle separately confirms the Landesbetrieb transition occurred around 1989 ('Leonhard Ermer kehrte 1989 zurück' as the director who shaped HZD 'as a Landesbetrieb') and that its current mandate derives from 'dem Datenverarbeitungsverbundgesetz, der Betriebsordnung der HZD und den Vorgaben der Landesregierung.' Same Landesbetrieb legal form as [[DE-IT-NRW]] (formed 2009) — 'a legally dependent, organisationally separated part of the state administration' — making `part-of` a direct fit. Anchor edge under metadata/relationship-types.md §2.3, asserting Hessian sub-federal scope via `level: subnational`."
    confidence: high
    valid_from: 1970-01-01
    valid_until: null

sources:
  - title: "Konsequenter Weg in Richtung Zukunft — Über uns"
    url: "https://hzd.hessen.de/ueber-uns"
    publisher: "Hessische Zentrale für Datenverarbeitung (HZD)"
    accessed: "2026-09-20"
  - title: "55 Jahre HZD — Kapitel 1: Absolut visionär"
    url: "https://hzd.hessen.de/medienraum/hzd-chronik/55-jahre-hzd-kapitel-1"
    publisher: "Hessische Zentrale für Datenverarbeitung (HZD)"
    accessed: "2026-09-20"
  - title: "55 Jahre HZD — Kapitel 4: Wettbewerbsfähiger Landesbetrieb"
    url: "https://hzd.hessen.de/medienraum/hzd-chronik/55-jahre-hzd-kapitel-4"
    publisher: "Hessische Zentrale für Datenverarbeitung (HZD)"
    accessed: "2026-09-20"
  - title: "Hessische Zentrale für Datenverarbeitung"
    url: "https://de.wikipedia.org/wiki/Hessische_Zentrale_f%C3%BCr_Datenverarbeitung"
    publisher: "Wikipedia (German)"
    accessed: "2026-09-20"
---

# Hessische Zentrale für Datenverarbeitung (HZD)

> **Created 2026-09-20**, further narrowing `discovery/unresolved.md`
> item #5 — Hesse's own IT service provider, alongside North
> Rhine-Westphalia's [[DE-IT-NRW]] and Bavaria's [[DE-AKDB]]. Sourced
> from HZD's own "55 Jahre HZD" chronicle pages and German Wikipedia,
> both read directly.

## Description

HZD is Hesse's central IT service provider. Its own chronicle, read
directly, describes a formal contract between the Land and municipal
parties signed **12 May 1969**, followed by the **Hessisches
Datenverarbeitungsverbundgesetz** (Hessian Data-Processing Association
Act) coming into force in **1970** — the statute establishing HZD.
Wikipedia's own article, read directly, independently confirms the
statute's name and 1970 date.

## A Landesbetrieb since 1989, like IT.NRW

HZD's own chronicle and Wikipedia both confirm HZD **became a
Landesbetrieb (state enterprise) in 1989**, specifically under **§26 of
the Hessische Landeshaushaltsordnung** (Hessian State Budget Ordinance)
— ending state subsidies and making its services fee-based. This is the
same legal form as [[DE-IT-NRW]] (North Rhine-Westphalia's own IT
provider, formed 2009): "a legally dependent, organisationally separated
part of the state administration," oriented toward cost recovery rather
than a separate legal person. HZD's own page states its current mandate
derives from "dem Datenverarbeitungsverbundgesetz, der Betriebsordnung
der HZD und den Vorgaben der Landesregierung."

Before 1977 HZD sat under the Hessian **State Chancellery**; from 1977 it
moved to the administration of the **Interior Ministry** — a
ministry-attachment history not further researched this pass.

## `start_date` left `null`

Per the convention formalised 2026-09-20 (`metadata/metadata-schema.md`):
only the year (1970) is confirmed by any source read; no page gives the
exact day the Datenverarbeitungsverbundgesetz took effect, so
`start_date` stays `null` rather than a `1970-01-01` placeholder. The
`part-of` edge's own `valid_from` is likewise a year-level approximation.

## Not modelled

- The exact date the Datenverarbeitungsverbundgesetz entered into force
  in 1970 — only the year is sourced.
- HZD's second location in Hünfeld (established 1990) and its full
  service catalogue — described here in prose only.

## Relationships

- `part-of` [[DE]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, all four read directly.
