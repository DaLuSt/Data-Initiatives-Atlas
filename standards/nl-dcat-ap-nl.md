---
id: NL-DCAT-AP-NL
type: standard
name: DCAT-AP-NL
alternative_names:
  - Metadataprofiel DCAT-AP-NL
description: >
  Dutch application profile of the DCAT metadata standard. It enables
  metadata about datasets and services (APIs) to be exchanged unambiguously
  between Dutch data catalogues and with European data catalogues.
  Management is assigned to Geonovum; version 3.0 has been adopted.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations:
  - NL-GEONOVUM
related_entities:
  - EU-DCAT-AP
  - INTL-DCAT
relationships:
  - type: based-on
    target: EU-DCAT-AP
    source: fact
    evidence: "Confirmed by reading geonovum.nl's own metadataprofiel page directly (2026-08-27): DCAT-AP-NL 'is a further specification based on the application profile of DCAT-AP-3.0 of the EU' and 'incorporat[es] requirements for European High Value Datasets' — compliance with the Dutch profile also satisfies European open-data and HVD requirements. standaarden.overheid.nl, also read directly, corroborates the chain but describes an earlier state (DCAT-AP-EU version 1.0, and a Dutch profile referred to there as 'DCAT-NL'/'IPM voor datasets'), which the geonovum.nl page's 3.0-based description supersedes."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-GEONOVUM
    source: fact
    evidence: "Confirmed by reading geonovum.nl directly (2026-08-27): Geonovum 'serves as the proposed managing organization,' actively managing the standard with changes tracked through a public GitHub repository. Geonovum's own news article, also read directly, confirms it announced the v3.0 metadata model."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Metadataprofiel DCAT-AP-NL"
    url: "https://www.geonovum.nl/geo-standaarden/metadataprofiel-dcat-ap-nl"
    publisher: "Geonovum"
    accessed: "2026-08-27"
  - title: "Metadatamodel DCAT-AP-NL v.3.0 vastgesteld"
    url: "https://www.geonovum.nl/nieuws/metadatamodel-dcat-ap-nl-v30-vastgesteld"
    publisher: "Geonovum"
    accessed: "2026-08-27"
  - title: "DCAT — standaarden.overheid.nl"
    url: "https://standaarden.overheid.nl/dcat"
    publisher: "Overheid.nl"
    accessed: "2026-08-27"
---

# DCAT-AP-NL

> **Verified 2026-08-27.** All three cited pages were read directly.
> `verification` moves from `search-only` to `primary-source`.

## Description

DCAT-AP-NL is the Dutch application profile of DCAT, the metadata standard
for describing datasets originally developed by the W3C. Applying the
generic DCAT-AP-NL standard makes it possible to exchange metadata about
data and services (APIs) unambiguously between different Dutch data
catalogues **and with European data catalogues** — which is what makes this
standard structurally interesting to the Atlas rather than merely
technically interesting.

DCAT is used across several Dutch platforms, including data.overheid.nl —
this specific claim was not re-confirmed by any page read this pass and is
carried over from the prior text.

**Version 3.0's adoption date has two slightly different figures in the
sources read, not fully reconciled.** Geonovum's own news article, read
directly, states the model "was established in December 2024 by the
Programming Council for the National Geo-Information Infrastructure
(PGDI)"; Geonovum's metadataprofiel page, also read directly, separately
gives 15 January 2025 in its own news section. Both are Geonovum's own
pages read this pass, so this is treated as an internal Geonovum
inconsistency (plausibly PGDI adoption in December 2024 vs. formal
publication in January 2025) rather than resolved by picking one;
`start_date` stays `null` rather than guessing which is correct.

## The cross-level chain this standard sits in

DCAT-AP-NL is a national profile of the European DCAT-AP, which is itself a
profile of W3C DCAT:

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (this entity)
```

**Batch 9 completed this chain.** Both upstream entities now exist and the
`based-on` relationship to [[EU-DCAT-AP]] is asserted. This is the first
international → EU → national standards descent the Atlas holds end-to-end,
and the pattern the brief's final relationship pass calls for.

One caveat carries up the chain: [[INTL-DCAT]] itself rests on second-hand
descriptions rather than a W3C source, so the top link is weaker than the
two below it.

## Relationships

- Based on [[EU-DCAT-AP]] — confirmed this pass, geonovum.nl's own text
  names DCAT-AP 3.0 specifically as the basis. Itself based on [[INTL-DCAT]].
- Maintained by [[NL-GEONOVUM]] — confirmed this pass.

## Sources

Listed in frontmatter, all three read directly this pass.
