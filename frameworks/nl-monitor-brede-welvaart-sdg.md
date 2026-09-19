---
id: NL-MONITOR-BREDE-WELVAART-SDG
type: framework
name: Monitor Brede Welvaart en de Sustainable Development Goals
alternative_names:
  - Monitor Brede Welvaart
  - Broad Prosperity and SDG Monitor
description: >
  The Netherlands' national tracking of the UN Sustainable Development
  Goals, integrated into the CBS "Monitor Brede Welvaart" (Broad
  Prosperity Monitor) as an "SDG-plus" framework of 293 indicators
  covering all 17 goals, with some goals split by perspective. Each
  indicator is assessed for whether it trends towards, away from, or
  neutrally with respect to its goal, with comparisons to other EU
  countries where possible. Published annually by Statistics Netherlands
  (CBS).

level: national
country: NL
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
  - NL-CBS
related_entities:
  - NL-CBS
  - UN-SDG-INDICATORS
relationships:
  - type: based-on
    target: UN-SDG-INDICATORS
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #175. Confirmed by reading cbs.nl's own page directly (2026-09-19): 'De voortgang van Nederland ten aanzien van brede welvaart en de SDG's wordt in deze monitor gemeten' met 293 verschillende indicatoren' — the Netherlands' progress on broad prosperity and the SDGs is measured in this monitor using 293 different indicators across the 17 UN goals, described as 'SDGplus-doelstellingen' (SDG-plus objectives), the same kind of national-selection descent [[DE-NACHHALTIGKEITSINDIKATOREN]], [[FR-INDICATEURS-ODD]] and [[BE-INDICATEURS-DEVELOPPEMENT-DURABLE]] each carry from the same UN list, with the Dutch version distinctively merging the SDGs into a pre-existing domestic well-being framework rather than publishing a standalone SDG dashboard."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-CBS
    source: fact
    evidence: "Confirmed by reading cbs.nl's own page directly (2026-09-19), published under the CBS domain and institutional branding, comparing the Netherlands' position with other EU countries where possible for each indicator's trend assessment (towards, away from, or neutral with respect to its goal)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "SDG's — Monitor Brede Welvaart en de Sustainable Development Goals 2023"
    url: "https://www.cbs.nl/nl-nl/dossier/dossier-brede-welvaart-en-de-sustainable-development-goals/monitor-brede-welvaart-en-de-sustainable-development-goals-2023/sdg-s"
    publisher: "Centraal Bureau voor de Statistiek (CBS)"
    accessed: "2026-09-19"
---

# Monitor Brede Welvaart en de Sustainable Development Goals

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #175. The Netherlands is the fourth national SDG indicator set modelled,
> after [[DE-NACHHALTIGKEITSINDIKATOREN]], [[FR-INDICATEURS-ODD]] and
> [[BE-INDICATEURS-DEVELOPPEMENT-DURABLE]]. Sourced from cbs.nl, read
> directly.

## Description

Confirmed by reading CBS's own page directly: the Netherlands' progress
on the UN's Sustainable Development Goals is measured using **293
different indicators** across the 17 goals — some goals split into
several because they cover distinct perspectives — inside the **Monitor
Brede Welvaart** (Broad Prosperity Monitor), the Dutch government's
existing domestic well-being reporting framework. Each indicator is
assessed for whether it shows "a trend toward the goal, a neutral trend,
or a movement away from the goal," with comparison to other EU countries
where data permits.

## Merged rather than parallel

Unlike Germany's, France's or Belgium's national SDG sets — each a
distinct, standalone dashboard — the Netherlands' approach **merges the
SDGs into a pre-existing domestic framework** rather than publishing a
separate one, described on the same page as producing "SDGplus"
objectives. This is a structurally different answer to the same question
the other three countries' entities record, not a smaller or larger
version of the same thing.

## Not modelled

- The **Monitor Brede Welvaart** itself, as distinct from its SDG
  component — the broader well-being framework predates and extends
  beyond the SDG integration and was not independently researched here.

## Relationships

- `based-on` [[UN-SDG-INDICATORS]] — `confidence: medium`.
- `maintained-by` [[NL-CBS]] — `confidence: high`.

## Sources

Listed in frontmatter — a single source, read directly.
