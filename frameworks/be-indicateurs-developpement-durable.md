---
id: BE-INDICATEURS-DEVELOPPEMENT-DURABLE
type: framework
name: Indicateurs de développement durable
alternative_names:
  - Belgian sustainable development indicators
  - indicators.be
description: >
  Belgium's national set of 84 indicators for tracking progress towards
  the UN's 17 Sustainable Development Goals, published on the
  indicators.be website by the Bureau fédéral du Plan. The indicators
  were selected by the Institut interfédéral de la Statistique, and each
  is classified and numbered by the SDG it tracks, with accompanying time
  series and methodological information.

level: national
country: BE
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
  - BE-BUREAU-FEDERAL-DU-PLAN
related_entities:
  - BE-BUREAU-FEDERAL-DU-PLAN
  - UN-SDG-INDICATORS
relationships:
  - type: based-on
    target: UN-SDG-INDICATORS
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #175. Confirmed by reading indicators.be's own page directly (2026-09-19): 'Le site internet présente 84 indicateurs, classés et numérotés par SDG' — the site presents 84 indicators, classified and numbered by SDG, covering all 17 UN Sustainable Development Goals with time series and methodological information for each — the same partial national-selection shape [[DE-NACHHALTIGKEITSINDIKATOREN]] and [[FR-INDICATEURS-ODD]] both carry from the same UN list, each with its own indicator count."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: BE-BUREAU-FEDERAL-DU-PLAN
    source: fact
    evidence: "Confirmed by reading indicators.be's own page directly (2026-09-19): 'Sur www.indicators.be le Bureau fédéral du Plan présente des indicateurs de développement durable' — the Federal Planning Bureau presents the indicators on indicators.be. The same page states 'Tous ces indicateurs ont été sélectionnés par l'Institut interfédéral de statistique' (all indicators were selected by the Institut interfédéral de la Statistique), a separate coordinating body not independently researched this pass."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Indicateurs de développement durable"
    url: "https://www.indicators.be/fr/t/SDG/Indicateurs_de_d%C3%A9veloppement_durable"
    publisher: "Bureau fédéral du Plan"
    accessed: "2026-09-19"
---

# Indicateurs de développement durable (Belgium)

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #175. Belgium is the third national SDG indicator set modelled, after
> [[DE-NACHHALTIGKEITSINDIKATOREN]] and [[FR-INDICATEURS-ODD]]. Sourced
> from indicators.be, read directly.

## Description

Confirmed by reading indicators.be's own page directly: Belgium's national
indicator set comprises **84 indicators**, "classified and numbered by
SDG," published by the **Bureau fédéral du Plan** ([[BE-BUREAU-FEDERAL-DU-PLAN]])
on the indicators.be site, each with time series and methodological
information.

## Selected by a different body than the one that publishes it

The same page states the 84 indicators "were selected by the **Institut
interfédéral de la Statistique**" — a coordinating statistical body
distinct from the Federal Planning Bureau that publishes them and from
[[BE-STATBEL]], the federal statistical office. The Institut interfédéral
de la Statistique is not independently researched or modelled here.

## Not modelled

- The **Institut interfédéral de la Statistique**, which selected the
  indicators.
- The **indicators.be** platform itself as distinct from the indicator
  set it publishes.

## Relationships

- `based-on` [[UN-SDG-INDICATORS]] — `confidence: medium`.
- `maintained-by` [[BE-BUREAU-FEDERAL-DU-PLAN]] — `confidence: high`.

## Sources

Listed in frontmatter — a single source, read directly.
