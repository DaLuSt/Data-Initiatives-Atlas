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
verification: search-only

start_date: null
end_date: null
last_verified: null
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
    source: interpretation
    evidence: "DCAT Version 3 was published as a W3C Recommendation by the Dataset Exchange Working Group (w3.org/TR/vocab-dcat-3/). Direction expressed W3C→DCAT for navigability; the authoritative framing belongs on the DCAT entity."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Data Catalog Vocabulary (DCAT) - Version 3"
    url: "https://www.w3.org/TR/vocab-dcat-3/"
    publisher: "World Wide Web Consortium (W3C)"
  - title: "Data Catalog Vocabulary (DCAT) - Version 3 is a W3C Recommendation"
    url: "https://www.w3.org/news/2024/data-catalog-vocabulary-dcat-version-3-is-a-w3c-recommendation/"
    publisher: "World Wide Web Consortium (W3C)"
---

# W3C (World Wide Web Consortium)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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

The `maintained-by` relationship carries `confidence: high` — the only such
value in this batch — because it rests on w3.org's own publication of DCAT 3
as a Recommendation, which is as direct as sourcing gets short of reading
the page. The entity's overall `confidence` stays `medium` because the
organisation itself was not researched beyond this role.

Note that `confidence: high` on a relationship is permitted; the validation
rule prohibiting `confidence: high` applies to the **entity-level** field on
`verification: search-only` entities.

`coverage: low`: the W3C's other standards, its process and its governance
were not researched.

## Relationships

- Publishes [[INTL-DCAT]].

## Sources

Listed in frontmatter — both from w3.org.
