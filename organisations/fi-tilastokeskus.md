---
id: FI-TILASTOKESKUS
type: organisation
name: Statistics Finland
alternative_names:
  - Tilastokeskus
  - Statistikcentralen
description: >
  Finland's national statistical institute and the national authority
  within the European Statistical System.

level: national
country: FI
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - FI
  - EU-ESS
relationships:
  - type: part-of
    target: FI
    source: fact
    evidence: "Confirmed by reading stat.fi's own 'About us' page directly (2026-08-26): 'Statistics Finland is Finland's national statistical institute that produces impartial statistics on Finnish society' — anchor edge under metadata/relationship-types.md §2.3, asserting no more than national scope."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Upgraded from the composition-rule tier to a direct statement: stat.fi's own 'National and international cooperation — European Statistical System' page, read directly (2026-08-26), states 'Statistics Finland and several other Finnish government agencies produce statistics for the policy needs of the European Union in accordance with the requirements of the European Union's Statistical Programme and the European Statistical System (ESS)' and names the ESS's actors directly: Eurostat, the national statistical authorities of EU member states, and the statistical authorities of the EEA and EFTA. This is Statistics Finland's own page naming its ESS participation, the same strong-evidence tier set for [[PL-GUS]], [[EE-STATISTIKAAMET]] and [[IT-ISTAT]]."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Statistics Finland"
    url: "https://www.stat.fi/index_en.html"
    publisher: "Tilastokeskus / Statistics Finland"
    accessed: "2026-08-26"
  - title: "About us — Statistics Finland"
    url: "https://stat.fi/en/about-us"
    publisher: "Tilastokeskus / Statistics Finland"
    accessed: "2026-08-26"
  - title: "European Statistical System — Statistics Finland"
    url: "https://stat.fi/en/about-us/cooperation/european-statistical-system"
    publisher: "Tilastokeskus / Statistics Finland"
    accessed: "2026-08-26"
  - title: "European Statistical System (ESS)"
    url: "https://ec.europa.eu/eurostat/web/european-statistical-system"
    publisher: "Eurostat"
    accessed: "2026-08-26"
---

# Statistics Finland

> **Verified 2026-08-26.** All four cited pages were read directly.
> Statistics Finland's own "European Statistical System" page names its
> ESS participation directly — an upgrade from the composition-rule
> tier most Atlas statistical offices carry.

## Description

Finland's national statistical institute - the **thirteenth** on
[[EU-ESS]] - confirmed via its own homepage as producing "impartial
statistics on Finnish society."

## Relationships

- `part-of` [[FI]] — anchor edge.
- `part-of` [[EU-ESS]], confirmed in Statistics Finland's own words
  rather than inferred from the composition rule.

## Sources

Listed in frontmatter, all four read directly this pass.
