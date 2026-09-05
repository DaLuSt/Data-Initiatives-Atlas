---
id: UN-WHO-GHO
type: platform
name: Global Health Observatory
alternative_names:
  - GHO
description: >
  WHO's main international health-data platform — "WHO's gateway to
  health-related statistics for its Member States." Covers more than
  1,000 indicators across 40+ thematic data collections (mortality and
  disease burden, immunization, Sustainable Development Goals, health
  systems, environmental health and more), broken down by country,
  region, age, sex and income group. Accessible via a web interface, an
  OData API, and downloadable datasets.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
organisations:
  - UN-WHO
related_entities:
  - UN-WHO
relationships:
  - type: maintained-by
    target: UN-WHO
    source: fact
    evidence: "Confirmed by reading who.int's own Global Health Observatory page directly (2026-09-05): 'The World Health Organization directly runs and maintains the Global Health Observatory as part of its Data at WHO initiative,' with featured portals developed collaboratively with partner agencies such as UNICEF and UNFPA."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Global Health Observatory"
    url: "https://www.who.int/data/gho"
    publisher: "World Health Organization"
    accessed: "2026-09-05"
---

# Global Health Observatory (GHO)

> **Added 2026-09-05, `verification: primary-source` from creation.**
> Companion entity to [[UN-WHO]], created the same pass to close the
> "UN DESA, UNDP, WHO" candidates-page lead.

## Description

The GHO is WHO's comprehensive international health-data platform.
Reading `who.int`'s own page directly: it organises indicators by major
themes — Universal Health Coverage, Health Emergencies, Health and
Well-Being — tracking mortality, diseases, immunization coverage and
progress toward the Sustainable Development Goals, across **40+
thematic data collections** (HIV, tuberculosis, maternal health,
nutrition, mental health and more), broken down by country, region, age,
sex and income group.

## Access

Confirmed directly: available through a **web interface** (interactive
charts, maps, country filters), an **OData API** for programmatic access,
and downloadable datasets/visualisations.

## Relationships

- `maintained-by` [[UN-WHO]], as part of its "Data at WHO" initiative;
  some featured portals are developed collaboratively with partner
  agencies such as UNICEF and UNFPA (neither modelled here).

## Sources

Listed in frontmatter, read directly this pass.
