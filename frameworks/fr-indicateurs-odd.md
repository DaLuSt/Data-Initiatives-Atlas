---
id: FR-INDICATEURS-ODD
type: framework
name: Indicateurs pour le suivi national des objectifs de développement durable
alternative_names:
  - Tableau de bord national des ODD
  - French national SDG indicator dashboard
description: >
  France's national dashboard of 98 indicators for tracking progress
  towards the UN's 17 Sustainable Development Goals, proposed in
  mid-2018 following consultation led by the Conseil national de
  l'information statistique (Cnis) and published and updated annually by
  INSEE. It complements, rather than replaces, France's continued
  participation in the UN's own 231-indicator global reporting framework,
  and is supplemented by regional, departmental and communal
  disaggregations produced jointly with the Service des données et
  études statistiques (SDES).

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2018-01-01
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains: []
organisations:
  - FR-INSEE
related_entities:
  - FR-INSEE
  - UN-SDG-INDICATORS
  - FR-CNIS
relationships:
  - type: based-on
    target: UN-SDG-INDICATORS
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #175. Confirmed by reading insee.fr's own page directly (2026-09-19): the 98-indicator dashboard tracks France's progress on the 17 UN SDGs and was selected as 'pertinent by comparison to French strategies,' complementing rather than replacing France's continued participation in the UN's own 231-indicator global reporting system — the same partial-descent shape [[EU-SDG-INDICATORS]] and [[DE-NACHHALTIGKEITSINDIKATOREN]] both carry from the same UN list, each with a different indicator count and selection basis."
    confidence: medium
    valid_from: "2018-01-01"
    valid_until: null
  - type: maintained-by
    target: FR-INSEE
    source: fact
    evidence: "Confirmed by reading insee.fr's own page directly (2026-09-19): 'À l'issue d'une concertation menée sous l'égide du Conseil national de l'Information statistique (CNIS) a été proposé mi-2018 un tableau de bord de 98 indicateurs' — following consultation led by the Cnis, a 98-indicator dashboard was proposed mid-2018 — and 'c'est ce tableau de bord qui est publié ici. Ses données sont actualisées annuellement' — this dashboard is published on INSEE's own site with data updated annually. The page also names the Service des données et études statistiques (SDES) as a partner supplying regional/departmental/communal disaggregations."
    confidence: high
    valid_from: "2018-01-01"
    valid_until: null

sources:
  - title: "Indicateurs pour le suivi national des objectifs de développement durable"
    url: "https://www.insee.fr/fr/statistiques/2654964"
    publisher: "Institut national de la statistique et des études économiques (INSEE)"
    accessed: "2026-09-19"
---

# Indicateurs pour le suivi national des objectifs de développement durable

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #175 (no national SDG indicator set was modelled for any of the Atlas's
> five original countries). France is the second, after
> [[DE-NACHHALTIGKEITSINDIKATOREN]]. Sourced from insee.fr's own page,
> read directly.

## Description

Confirmed by reading INSEE's own page directly: France's national
dashboard for tracking the UN's Sustainable Development Goals comprises
**98 indicators**, "proposed mid-2018 following consultation led by the
Conseil national de l'Information statistique (CNIS)." INSEE publishes
the dashboard on its own site, with data "updated annually."

## A national selection, not a subset

The same page states the 98 indicators were chosen as "pertinent by
comparison to French strategies" — a national selection exercise, not a
mechanical subset of the UN's own list. France continues to report
separately into the **UN's own 231-indicator global framework**; the
national dashboard sits alongside it rather than replacing it, the same
complementary relationship [[EU-SDG-INDICATORS]] describes for its own
55-of-100 descent from the same UN list.

## Regional disaggregation

INSEE and the **Service des données et études statistiques (SDES)** have
jointly produced territorialised versions of the indicator set, broken
down to regional, departmental and communal level where data permits —
named on the same page but not independently researched or modelled here.

## Not modelled

- The **Service des données et études statistiques (SDES)**, INSEE's
  partner on regional disaggregation — not independently researched.
- The **regional/departmental/communal indicator breakdowns** themselves.

**The Cnis, researched 2026-09-26**: now its own entity, [[FR-CNIS]]
(established 1984), whose consultation produced this indicator set's
selection.

## Relationships

- `based-on` [[UN-SDG-INDICATORS]] — `confidence: medium`.
- `maintained-by` [[FR-INSEE]] — `confidence: high`.

## Sources

Listed in frontmatter — a single source, read directly.
</content>
