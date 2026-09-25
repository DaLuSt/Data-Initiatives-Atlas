---
id: DOMAIN-FOOD
type: domain
name: Food
alternative_names:
  - Levensmiddelen
  - Food production and distribution
description: >
  Subject-matter domain covering the production, processing and
  distribution of food. "Levensmiddelen" is one of the seven
  important-entity sectors listed in Bijlage 2 of the Dutch
  Cyberbeveiligingswet (Cbw), the national implementation of the EU NIS2
  Directive, which incorporates Regulation (EC) No 178/2002's definition
  of a food business — extending the sector to primary agricultural
  production as well as processing and distribution.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-25"
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources: []
---

# Food

## Description

Classification node for food production, processing and distribution.
Created 2026-09-25 at the user's request to add domains reflecting the
sector list in the Dutch Cyberbeveiligingswet (Cbw) — "Levensmiddelen" is
one of the seven important-entity sectors in the Cbw's own Bijlage 2,
confirmed by reading `ncsc.nl`'s "Valt mijn organisatie onder de
Cyberbeveiligingswet (NIS2)?" page directly (2026-09-25), which lists the
same seven sectors as Directive (EU) 2022/2555's (NIS2) Annex II. Annex II
point 5 itself incorporates Regulation (EC) No 178/2002's definition of a
food business, which is not limited to processing and distribution — it
reaches primary production too. This is used, deliberately, as the reason
[[EU-AGRI-DATA-SPACE]] is tagged here rather than to a separate
Agriculture domain: the Atlas has no entity yet that needs farming
distinguished from the wider food-supply-chain sector NIS2 defines.

Like [[DOMAIN-GOVERNMENT]], this is a taxonomy node rather than a
researched entity: it carries no factual claims and therefore no sources.
The sourced claim that Food is an important sector lives on [[NL-CBW]]
and [[EU-NIS2]], not here.

## Relationships

Used by [[NL-CBW]] and [[EU-NIS2]] (important-sector scope), and by
[[EU-AGRI-DATA-SPACE]], one of the common European data spaces, intended
to allow comparative analyses between farms.
