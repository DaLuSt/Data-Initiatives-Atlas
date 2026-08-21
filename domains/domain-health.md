---
id: DOMAIN-HEALTH
type: domain
name: Health
alternative_names:
  - Healthcare
  - Zorg
  - Gezondheid
description: >
  Subject-matter domain covering health and healthcare: health data,
  information standards for care, and the infrastructures through which
  health and research data are shared and reused.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-14"
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources: []
---

# Health

## Description

Classification node for health and healthcare. Created in Batch 5 now that
it connects two entities, meeting the threshold in `metadata/taxonomy.md`
§1: [[NL-NICTIZ]] and [[NL-HEALTH-RI]].

It was withheld in Batch 2, when [[NL-NICTIZ]] would have been its only
member; that entity's explanatory note is now resolved.

Like [[DOMAIN-GOVERNMENT]], this is a taxonomy node rather than a
researched entity: it carries no factual claims and therefore no sources.

## From one country to five

For most of the Atlas's life this node reached entities in **one country** —
the Netherlands — while the Atlas held [[EU-EHDS]], the European Health Data
Space. `discovery/candidates.md` measured that as the single largest
correction available: fifty-seven of fifty-eight countries with no health
entity at all.

The batch of **2026-08-21** took it to five:

| Country | Entities | Shape of the national regime |
|---|---|---|
| [[NL]] | [[NL-NICTIZ]], [[NL-HEALTH-RI]] | standards body plus a research data infrastructure |
| [[DE]] | [[DE-GEMATIK]], [[DE-GDNG]] | statute creates a research data centre; a separate company runs the exchange infrastructure |
| [[FR]] | [[FR-HEALTH-DATA-HUB]], [[FR-SNDS]] | a public-interest grouping of 56 members holds the platform |
| [[FI]] | [[FI-FINDATA]], [[FI-SECONDARY-USE-ACT]] | a statutory **permit authority** licenses access to data others hold |
| [[DK]] | [[DK-SUNDHEDSDATASTYRELSEN]] | the authority **holds the registers itself** |

The three distinct shapes — pool, license, custody — are the reason this
classification node is worth more than a label. Every one of these countries
has "a national health data body"; they do materially different jobs, and only
placing them side by side shows it.

## Relationships

Reached by association through the `domains:` list of every entity above,
plus [[EU-EHDS]]. Domains carry no typed edges — see
`metadata/relationship-types.md` §2.3, which exempts them.
