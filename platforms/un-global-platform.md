---
id: UN-GLOBAL-PLATFORM
type: platform
name: UN Global Platform
alternative_names: []
description: >
  Cloud-based collaborative infrastructure for the international official
  statistics community — "a global community of statisticians and
  developers working on and sharing Big Data resources together in the
  cloud." Hosts collaborative projects and training, and maintains
  regional hubs in Brazil, Indonesia, Rwanda, China, the UAE and Spain.
  Managed by the UN Statistics Division, and governed strategically by
  the UN Committee of Experts on Big Data and Data Science for Official
  Statistics (UN-CEBD), which oversees its task teams and regional hubs.

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
  - DOMAIN-GOVERNMENT
organisations:
  - UN-UNSD
related_entities:
  - UN-UNSD
relationships:
  - type: maintained-by
    target: UN-UNSD
    source: fact
    evidence: "Confirmed by reading unstats.un.org's own Big Data page directly (2026-09-05): 'The United Nations Statistics Division, operating under the Department of Economic and Social Affairs, manages these operations,' referring to the Global Platform's regional-hub infrastructure. The same page describes the UN Committee of Experts on Big Data and Data Science for Official Statistics (UN-CEBD) as providing governance and strategic direction, with the Global Platform as the operational infrastructure implementing it — UN-CEBD is not a separate Atlas entity, so this is recorded in prose rather than as a relationship."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UN Global Platform"
    url: "https://unstats.un.org/bigdata/"
    publisher: "United Nations Statistics Division"
    accessed: "2026-09-05"
---

# UN Global Platform

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/candidates.md` had flagged this as "a second, independent
> attachment point for national statistical offices, alongside
> [[EU-ESS]]" — a weak lead based on unopened `ggim.un.org` and
> `unstats.un.org` pages. This pass opened and read `unstats.un.org`'s
> own Big Data page directly.

## Description

The UN Global Platform is, in the source's own words, "a global community
of statisticians and developers working on and sharing Big Data resources
together in the cloud." It provides cloud-based infrastructure and tools
for the international statistical community: hosting collaborative
projects and training programmes, facilitating knowledge-sharing on
methodologies, and supporting capacity-building in emerging data-science
techniques for national statistical offices (NSOs).

## Governance and operations

Reading `unstats.un.org` directly: **[[UN-UNSD]]**, operating under DESA,
**manages** the platform's operations, including **regional hubs** in
Brazil, Indonesia, Rwanda, China, the UAE and Spain. Strategic direction
and governance come from the **UN Committee of Experts on Big Data and
Data Science for Official Statistics (UN-CEBD)**, which oversees the
platform's task teams and regional hubs — UN-CEBD is not itself a
separate Atlas entity, so this governance relationship is recorded in
prose rather than as a typed edge.

## A second attachment point for NSOs

This is a genuinely separate structure from the statistical chain already
recorded on [[UN-UNSD]]'s own file (UN Statistical Commission →
EU-Eurostat/[[EU-ESS]] → national statistical offices): the Global
Platform is a cloud/data-science-capacity initiative, not a governance
hierarchy, and no source read this pass connects it to [[EU-ESS]] or any
national statistics agency by name. No such relationship is asserted.

## Relationships

- `maintained-by` [[UN-UNSD]].

## Sources

Listed in frontmatter, read directly this pass.
