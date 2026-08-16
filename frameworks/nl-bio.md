---
id: NL-BIO
type: framework
name: Baseline Informatiebeveiliging Overheid
alternative_names:
  - BIO
  - BIO2
description: >
  The common information security framework for all tiers of Dutch
  government — central government, municipalities, provinces and water
  authorities. It sets the minimum security requirements and measures, and
  is aligned to the NEN-EN-ISO/IEC 27001 and 27002 standards.

level: national
country: NL
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
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - NL-NEN
  - INTL-ISO-IEC-27001
  - INTL-ISO-IEC-27002
relationships:
  - type: based-on
    target: INTL-ISO-IEC-27001
    source: fact
    evidence: "BIO2 is based on NEN-EN-ISO/IEC 27001:2023, applied to formulate requirements for establishing and implementing an information security management system (bio-overheid.nl BIO2). NOTE: BIO2 cites the 2023 NEN-EN adoption; the ISO edition located is 27001:2022 — very likely the same standard under its Dutch designation, but the equivalence is inferred. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: INTL-ISO-IEC-27002
    source: fact
    evidence: "BIO2 is based on NEN-EN-ISO/IEC 27002:2022, applied in a risk-driven manner to formulate appropriate control measures (bio-overheid.nl BIO2). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: NL
    source: fact
    evidence: "The BIO is the basic framework for information security within all government tiers: Rijk, gemeenten, provincies and waterschappen (digitaleoverheid.nl BIO page; bio-overheid.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Baseline Informatiebeveiliging Overheid (BIO)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/baseline-informatiebeveiliging-overheid/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Home NL — bio-overheid"
    url: "https://www.bio-overheid.nl/"
    publisher: "BIO-overheid"
  - title: "Baseline Informatiebeveiliging Overheid 2 (BIO2) v1.3 def"
    url: "https://www.bio-overheid.nl/media/dr4inbhc/20260109-baseline-informatiebeveiliging-overheid-2-bio2-v13-def.pdf"
    publisher: "BIO-overheid"
  - title: "Baseline Informatiebeveiliging Overheid (BIO) & NEN-ISO/IEC 27001 en 27002"
    url: "https://www.communicatierijk.nl/vakkennis/rijkswebsites/verplichte-richtlijnen/baseline-informatiebeveiliging-rijksdienst"
    publisher: "CommunicatieRijk"
---

# BIO (Baseline Informatiebeveiliging Overheid)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BIO is the common basic framework for information security across all
tiers of Dutch government — central government, municipalities, provinces
and water authorities. Within Dutch government it forms the basis for
information security, containing the minimum requirements and security
measures.

## Versions

**BIO2** is the current major revision. It reflects NEN-EN-ISO/IEC
27001:2023 and NEN-EN-ISO/IEC 27002:2022, and replaces the earlier BIO's
categorisation into three Basis Beveiligingsniveaus (BBN) with an explicitly
risk-driven approach. Under BIO2, ISO 27001 is applied to formulate
requirements for establishing an information security management system, and
ISO 27002 is applied in a risk-driven way to select control measures; where
control measures follow from assessed risk, government organisations are at
minimum obliged to apply the government measures from BIO2. Where BIO1 was
often used as a checklist, BIO2 is described as requiring genuine
risk-driven working and active governance.

A BIO2 document dated 9 January 2026 was located, which suggests BIO2 is
current, though the formal date on which BIO2 replaced BIO1 was not
established.

## Modelling note

BIO and BIO2 are modelled as **one entity with versions**, unlike
[[NL-WOB]]/[[NL-WOO]] or [[NL-ARCHIEFWET-1995]]/[[NL-ARCHIEFWET-2026]],
which are separate entities. The reasoning: those are distinct statutes with
distinct official titles, whereas BIO2 is a new version of a continuously
named baseline. This is a judgement call, and if re-verification shows BIO2
is treated as a distinct instrument it should be split out — recorded in
`discovery/unresolved.md`.

## Relationships

- Applies in [[NL]] across all government tiers.
- Based on [[INTL-ISO-IEC-27001]] and [[INTL-ISO-IEC-27002]], added in
  Batch 14, closing the gap this entity carried since Batch 4. This gives a
  second international → national standards chain alongside the DCAT one.
  Note the edition caveat recorded in the relationship evidence: BIO2 cites
  the NEN-EN 2023/2022 adoptions, and the equivalence to the ISO editions is
  inferred rather than sourced.
- Published in the Netherlands by [[NL-NEN]].
- ENSIA, the accountability system paired with the BIO in its
  digitaleoverheid.nl placement, is not yet an entity; queued.

## Sources

Listed in frontmatter.
