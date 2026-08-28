---
id: INTL-W3C
type: organisation
name: World Wide Web Consortium
alternative_names:
  - W3C
description: >
  International standards organisation for the World Wide Web, operating on
  direct membership rather than national delegation, and **not** a UN body.
  It publishes the Data Catalog Vocabulary (DCAT) as a W3C Recommendation.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-DCAT
relationships:
  - type: maintained-by
    target: INTL-DCAT
    source: fact
    evidence: "Confirmed by reading both cited pages directly (2026-08-28): w3.org/TR/vocab-dcat-3/ is itself the DCAT 3 Recommendation, dated 22 August 2024, published by the Dataset Exchange Working Group; the w3.org news announcement states 'The Dataset Exchange Working Group published Data Catalog Vocabulary (DCAT) - Version 3 as a W3C Recommendation.' Direction expressed W3C→DCAT for navigability; the authoritative framing belongs on [[INTL-DCAT]], which was independently verified to primary-source in an earlier pass this batch cycle using the same two pages."
    confidence: high
    valid_from: 2024-08-22
    valid_until: null

sources:
  - title: "Data Catalog Vocabulary (DCAT) - Version 3"
    url: "https://www.w3.org/TR/vocab-dcat-3/"
    publisher: "World Wide Web Consortium (W3C)"
    accessed: "2026-08-28"
  - title: "Data Catalog Vocabulary (DCAT) - Version 3 is a W3C Recommendation"
    url: "https://www.w3.org/news/2024/data-catalog-vocabulary-dcat-version-3-is-a-w3c-recommendation/"
    publisher: "World Wide Web Consortium (W3C)"
    accessed: "2026-08-28"
---

# W3C (World Wide Web Consortium)

> **Verified 2026-08-28.** Both cited pages were read directly, confirming
> the DCAT 3 Recommendation and its publication date in W3C's own words.
> `verification` moves from `search-only` to `primary-source`.

## Description

The W3C is the international standards organisation for the World Wide Web.
Unlike [[INTL-ISO]], [[INTL-IEC]] and [[UN-ITU]], which operate on national
delegation, the W3C is a **direct-membership** organisation — a distinction
one source draws explicitly across the standards ecosystem.

Its relevance to this Atlas is concentrated in one output:
[[INTL-DCAT]], published as a W3C Recommendation by the Dataset Exchange
Working Group, which is the root of the Atlas's metadata-standards chain
running down through [[EU-DCAT-AP]] to [[NL-DCAT-AP-NL]].

`INTL` scope, not `UN`.

## Note on the confidence value

The `maintained-by` relationship carries `confidence: high` because it now
rests on both w3.org pages read directly, as direct as sourcing gets short
of the organisation supplying the fact in person. The entity's overall
`confidence` stays `medium` because the organisation itself — its wider
process, membership and governance — was not researched beyond this one
role.

`coverage: low`: the W3C's other standards, its process and its governance
were not researched.

## Relationships

- Publishes [[INTL-DCAT]].

## Sources

Listed in frontmatter — both from w3.org, both read directly this pass.
