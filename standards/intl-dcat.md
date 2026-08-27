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
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading w3.org's own DCAT 3 specification and its own news announcement directly (2026-08-27): 'The Dataset Exchange Working Group published Data Catalog Vocabulary (DCAT) - Version 3 as a W3C Recommendation' on 22 August 2024. The specification's own text states DCAT 3 'maintains the DCAT namespace as its terms preserve backward compatibility with DCAT 2', relaxing constraints and adding classes and properties 'but these changes do not break the definition of previous terms.'"
    confidence: high
    valid_from: 2024-08-22
    valid_until: null

sources:
  - title: "Data Catalog Vocabulary (DCAT) - Version 3"
    url: "https://www.w3.org/TR/vocab-dcat-3/"
    publisher: "World Wide Web Consortium (W3C)"
    accessed: "2026-08-27"
  - title: "Data Catalog Vocabulary (DCAT) - Version 3 is a W3C Recommendation"
    url: "https://www.w3.org/news/2024/data-catalog-vocabulary-dcat-version-3-is-a-w3c-recommendation/"
    publisher: "World Wide Web Consortium (W3C)"
    accessed: "2026-08-27"
  - title: "Data Catalog Vocabulary (DCAT) - Version 2"
    url: "https://www.w3.org/TR/vocab-dcat-2/"
    publisher: "World Wide Web Consortium (W3C)"
---

# DCAT (Data Catalog Vocabulary)

> **Verified 2026-08-27.** Two of three cited w3.org pages were read
> directly, closing a frontmatter/body drift: Batch 14 had already
> rebuilt this entity on W3C citations, but `verification` still read
> `search-only` and every evidence string still said "NOT READ." Both
> now genuinely confirmed; `confidence` moves from `medium` to `high`.

## Rebuilt in Batch 14, verified 2026-08-27

Batch 9 created this entity from **second-hand descriptions only** — one
European Commission page, one Dutch government page — with no w3.org
citation, and flagged the top of the Atlas's flagship standards chain as its
weakest link. Batch 14 **rebuilt it on W3C material** but never actually
read the pages it cited. Both are now read directly: w3.org's own DCAT 3
specification and its own news announcement, both confirming the
Recommendation date and backward-compatibility claim in the specification's
own words.

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

Listed in frontmatter, two of three read directly this pass — the DCAT 3
specification and the news announcement. The DCAT 2 specification was
not re-fetched.
