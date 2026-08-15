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
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - INTL-W3C
related_entities:
  - EU-DCAT-AP
relationships:
  - type: maintained-by
    target: INTL-W3C
    source: fact
    evidence: "DCAT Version 3 was published as a W3C Recommendation on 22 August 2024 by the Dataset Exchange Working Group (w3.org/TR/vocab-dcat-3/; w3.org news). NOT READ — search-only."
    confidence: high
    valid_from: 2024-08-22
    valid_until: null

sources:
  - title: "Data Catalog Vocabulary (DCAT) - Version 3"
    url: "https://www.w3.org/TR/vocab-dcat-3/"
    publisher: "World Wide Web Consortium (W3C)"
  - title: "Data Catalog Vocabulary (DCAT) - Version 3 is a W3C Recommendation"
    url: "https://www.w3.org/news/2024/data-catalog-vocabulary-dcat-version-3-is-a-w3c-recommendation/"
    publisher: "World Wide Web Consortium (W3C)"
  - title: "Data Catalog Vocabulary (DCAT) - Version 2"
    url: "https://www.w3.org/TR/vocab-dcat-2/"
    publisher: "World Wide Web Consortium (W3C)"
---

# DCAT (Data Catalog Vocabulary)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Rebuilt in Batch 14

Batch 9 created this entity from **second-hand descriptions only** — one
European Commission page, one Dutch government page — with no w3.org
citation, and flagged the top of the Atlas's flagship standards chain as its
weakest link. **It has been rebuilt here on W3C material**, and
`confidence` moves from `low` to `medium`.

## Description

DCAT is an **RDF vocabulary**, published by [[INTL-W3C]], purpose-built to
let data catalogues published by different organisations describe their
holdings in a common machine-readable structure so the catalogues can be
harvested, aggregated and searched together.

It enables a publisher to describe datasets and data services in a catalogue
using a standard model and vocabulary, increasing discoverability and
supporting a decentralised approach to publishing catalogues with federated
search across multiple sites.

**Version 3** was published as a W3C Recommendation on **22 August 2024** by
the Dataset Exchange Working Group. DCAT 3 keeps the DCAT namespace and
preserves backward compatibility with DCAT 2 — it relaxes constraints and
adds classes and properties without breaking previous term definitions.
[[EU-DCAT-AP]] 3.0.1 is aligned with DCAT 3.

## Scope note

W3C is an international, non-UN organisation, so this entity takes the
`INTL` ID scope per `metadata/ontology.md` §2.1. [[INTL-W3C]] was added in
Batch 13, so the `maintained-by` relationship — pending since Batch 9 — is
now recorded.

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

- Published by [[INTL-W3C]].
- Basis for [[EU-DCAT-AP]] (recorded on that entity).

## Sources

Listed in frontmatter — now all three from w3.org.
