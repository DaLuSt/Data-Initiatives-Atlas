---
id: INTL-DCAT
type: standard
name: Data Catalog Vocabulary
alternative_names:
  - DCAT
description: >
  W3C vocabulary for describing datasets in data catalogues, designed to
  make datasets from multiple catalogues findable and comparable. It is the
  base specification from which the European DCAT-AP and its national
  profiles derive.

level: international
country: null
region: null

status: active
confidence: low
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
  - EU-DCAT-AP
relationships: []

sources:
  - title: "Get started with DCAT-AP (describing DCAT-AP as based on W3C's DCAT)"
    url: "https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/news/get-started-dcat-ap"
    publisher: "European Commission — Interoperable Europe Portal"
  - title: "DCAT — standaarden.overheid.nl (describing DCAT as a W3C metadata standard)"
    url: "https://standaarden.overheid.nl/dcat"
    publisher: "Overheid.nl"
---

# DCAT (Data Catalog Vocabulary)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

DCAT is the W3C's vocabulary for describing datasets in data catalogues. It
is the root of the metadata-standards chain the Atlas has been assembling
across three batches: [[EU-DCAT-AP]] is a specification based on it, and
[[NL-DCAT-AP-NL]] is the Dutch profile of that. DCAT 3 is the recommendation
[[EU-DCAT-AP]] 3.0.1 is aligned with.

## ⚠ No W3C source was located

`confidence: low` for a specific reason: **neither source below is from the
W3C.** Both are second-hand descriptions — one European Commission, one
Dutch government — that characterise DCAT as a W3C standard. No w3.org
citation was returned by any search in this batch.

For a standard this structurally important, that is unsatisfactory. The
entity is created anyway because the alternative was leaving the top of the
chain missing while both derived profiles exist. **Batch 14 should rebuild
it on W3C material**, in the same way Batch 8 rebuilt [[EU-EIDAS2]].

## Scope note

W3C is an international, non-UN organisation, so this entity takes the
`INTL` ID scope per `metadata/ontology.md` §2.1 — the first `INTL` entity in
the Atlas. The W3C itself is not yet modelled (Batch 13), so no
`maintained-by` relationship is asserted.

Creating this in Batch 9 is a small scope stretch — DCAT is international
rather than EU — but Batch 9's brief names DCAT explicitly in its standards
list, and the chain is only meaningful with its root present.

## The completed chain

```
INTL-DCAT        (W3C)              ← this entity
     │ based-on
EU-DCAT-AP       (SEMIC)
     │ based-on
NL-DCAT-AP-NL    (Geonovum)
```

This is the international → EU → national standards descent the brief's
final relationship pass calls for, and the first one the Atlas holds
end-to-end.

## Relationships

- Basis for [[EU-DCAT-AP]] (recorded on that entity).

## Sources

Listed in frontmatter — both indirect.
