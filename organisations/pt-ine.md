---
id: PT-INE
type: organisation
name: Instituto Nacional de Estatística (Portugal)
alternative_names:
  - INE
  - INE Portugal
  - Statistics Portugal
description: >
  Portugal's national statistical institute, responsible for the production
  and dissemination of official statistics and Portugal's national
  statistical institute within the European Statistical System.

level: national
country: PT
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
  - PT
  - EU-ESS
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "Confirmed by reading ine.pt's own homepage directly (2026-08-26): the portal identifies itself as the official statistics portal for Portugal ('Statistics Portugal'), covering population, labour, environment, economic and social statistics. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Confirmed by reading ec.europa.eu/eurostat's own European Statistical System page directly (2026-08-26): 'The ESS is the partnership between the EU statistical authority, which is the Commission (Eurostat), the National Statistical Institutes (NSIs), and Other National Authorities (ONAs) in each EU country.' ine.pt's own homepage, also read directly, carries a dedicated 'European Statistical System' section, confirming INE's participation as Portugal's NSI."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "INE — Instituto Nacional de Estatística"
    url: "https://www.ine.pt/xportal/xmain?xpgid=ine_main&xpid=INE"
    publisher: "Instituto Nacional de Estatística (Portugal)"
    accessed: "2026-08-26"
  - title: "European Statistical System (ESS)"
    url: "https://ec.europa.eu/eurostat/web/european-statistical-system"
    publisher: "Eurostat / European Commission"
    accessed: "2026-08-26"
---

# Instituto Nacional de Estatística (Portugal)

> **Verified 2026-08-26.** Both cited pages were read directly.

## Description

INE is Portugal's national statistical institute.

## ⚠ Two INEs

Spain's statistical office is **also** called INE — [[ES-INE]], the Instituto
Nacional de Estadística. The two are unrelated bodies with near-identical
names in near-identical languages, and the Atlas holds both.

The scoped ID convention keeps them apart (`PT-INE` and `ES-INE`) and the
`name` fields disambiguate. Anyone searching "INE" gets two results, and
that is correct — it is a genuine ambiguity in the world, not in the Atlas.

## The ninth member of [[EU-ESS]]

Nine national statistical institutes plus [[EU-EUROSTAT]]. Every EU member
state in the Atlas is represented; the three non-member states are not, each
for its own reason.

## Relationships

- `part-of` [[PT]] — anchor edge, confirmed this pass.
- `part-of` [[EU-ESS]].

## Sources

Listed in frontmatter, both read directly this pass.
