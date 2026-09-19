---
id: ES-INDICADORES-ODS
type: framework
name: Indicadores de la Agenda 2030 para el Desarrollo Sostenible
alternative_names:
  - Spanish national SDG indicator set
  - Indicadores ODS España
description: >
  Spain's national indicator set for tracking the UN's 2030 Agenda,
  comprising 234 indicators against the Agenda's 17 goals and 169
  targets, published by the Instituto Nacional de Estadística (INE)
  through a single national dissemination point incorporating data from
  the INE itself and other official sources on an ongoing basis.

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

domains: []
organisations:
  - ES-INE
related_entities:
  - ES-INE
  - UN-SDG-INDICATORS
relationships:
  - type: based-on
    target: UN-SDG-INDICATORS
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #175. Confirmed by reading ine.es's own page directly (2026-09-19): the platform covers '234 indicadores que pueden medirse a través de los datos estadísticos que aquí se recogen' — 234 indicators measurable through the statistical data collected there — tracking all 17 goals and 169 targets of the 2030 Agenda, the same kind of national-selection descent [[DE-NACHHALTIGKEITSINDIKATOREN]], [[FR-INDICATEURS-ODD]], [[BE-INDICATEURS-DEVELOPPEMENT-DURABLE]] and [[NL-MONITOR-BREDE-WELVAART-SDG]] each carry from the same UN list."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: ES-INE
    source: fact
    evidence: "Confirmed by reading ine.es's own page directly (2026-09-19), published as the 'Plataforma Nacional de Difusión de los Indicadores ODS' — the National Dissemination Platform for SDG Indicators — offering 'información tanto del INE como de otras fuentes oficiales que se irán incorporando de forma progresiva' (information from both INE and other official sources incorporated progressively)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Indicadores de la Agenda 2030 para el Desarrollo Sostenible"
    url: "https://www.ine.es/dyngs/ODS/es/index.htm"
    publisher: "Instituto Nacional de Estadística (INE)"
    accessed: "2026-09-19"
---

# Indicadores de la Agenda 2030 para el Desarrollo Sostenible

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #175. Spain is the fifth and last of the Atlas's original countries to
> get a national SDG indicator set modelled, after
> [[DE-NACHHALTIGKEITSINDIKATOREN]], [[FR-INDICATEURS-ODD]],
> [[BE-INDICATEURS-DEVELOPPEMENT-DURABLE]] and
> [[NL-MONITOR-BREDE-WELVAART-SDG]]. Sourced from ine.es, read directly.

## Description

Confirmed by reading INE's own page directly: Spain's national platform
for tracking the UN's 2030 Agenda comprises **234 indicators**, covering
all **17 goals and 169 targets**, published as a single national
dissemination point — the **Plataforma Nacional de Difusión de los
Indicadores ODS**.

## Multi-source, not INE alone

The same page states the platform incorporates "información tanto del INE
como de otras fuentes oficiales que se irán incorporando de forma
progresiva" — data from both INE and other official sources, added
progressively. Which specific other sources contribute, and in what
proportion, was not established this pass; `maintained-by` [[ES-INE]] is
recorded as the publisher of record, not as the sole data source.

## The last of five, and the last shaped differently

With this entity, all five of the Atlas's original countries — Belgium,
Germany, France, the Netherlands and Spain — now have a national SDG
indicator set modelled, closing `discovery/unresolved.md` row #175 for
country coverage even though the row's underlying `EU-SDG-INDICATORS`
`applies-in` question remains unanswered by design (see that entity's own
"The `applies-in` question" section). No relationship is asserted between
any of the five national sets and each other, or between any of them and
[[EU-SDG-INDICATORS]]: each descends independently from the UN list, and
no source read connects the national efforts to one another or to the EU
set specifically.

## Not modelled

- The **specific "other official sources"** the platform draws on beyond
  INE itself.

## Relationships

- `based-on` [[UN-SDG-INDICATORS]] — `confidence: medium`.
- `maintained-by` [[ES-INE]] — `confidence: high`.

## Sources

Listed in frontmatter — a single source, read directly.
