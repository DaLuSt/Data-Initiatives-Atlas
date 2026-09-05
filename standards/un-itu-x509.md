---
id: UN-ITU-X509
type: standard
name: "ITU-T Recommendation X.509 | ISO/IEC 9594-8"
alternative_names:
  - X.509
  - ITU-T X.509
description: >
  International standard defining frameworks for public-key
  infrastructure (PKI) and privilege management infrastructure (PMI),
  specifying public-key certificates, attribute certificates, certificate
  revocation lists (CRLs) and attribute certificate revocation lists
  (ACRLs), certificate/CRL extensions, and principles for certificate
  validation and certificate policy. Jointly published as an identical
  text by ITU-T and ISO/IEC, as ISO/IEC 9594-8. The most widely deployed
  format for public-key certificates, underlying TLS/HTTPS and most PKI
  used for digital identity and trust services.

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
  - DOMAIN-CYBERSECURITY
organisations:
  - UN-ITU
related_entities:
  - UN-ITU
  - INTL-ISO
relationships:
  - type: maintained-by
    target: UN-ITU
    source: fact
    evidence: "Confirmed by reading itu.int's own recommendation page directly (2026-09-05): the current edition is 'X.509 (10/2019),' marked 'In force,' with Amendment 1 (10/2024) and Corrigendum 3 (07/2026), maintained by ITU-T Study Group 17."
    confidence: high
    valid_from: null
    valid_until: null
  - type: aligned-with
    target: INTL-ISO
    source: fact
    evidence: "Confirmed by reading itu.int's own recommendation page directly (2026-09-05), titled 'Recommendation ITU-T X.509 | ISO/IEC 9594-8' — the page states this is an identical text jointly published by both bodies. `aligned-with` is used because the two publishing bodies keep the text identical by agreement, rather than one deriving from or being based on the other."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Recommendation ITU-T X.509"
    url: "https://www.itu.int/ITU-T/recommendations/rec.aspx?rec=X.509"
    publisher: "International Telecommunication Union"
    accessed: "2026-09-05"
---

# ITU-T Recommendation X.509 | ISO/IEC 9594-8

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/candidates.md` §4 and [[UN-ITU]]'s own file had both flagged
> "no ITU standard is modelled" as an open gap. This pass read
> `itu.int`'s own recommendation page directly and found its
> best-known standard.

## Description

X.509 defines the frameworks for **public-key infrastructure (PKI)** and
**privilege management infrastructure (PMI)** that underlie most digital
certificate systems in use today, including TLS/HTTPS. Reading
`itu.int`'s own page directly: it specifies "public-key certificate,
attribute certificate, certificate revocation list (CRL) and attribute
certificate revocation list (ACRL)," certificate and CRL extensions, a
directory schema for storing PKI/PMI data, entity types (certification
authorities, attribute authorities, trust anchors), and principles for
certificate validation and certificate policy.

## Jointly published with ISO/IEC

Confirmed directly: the Recommendation is titled **"Recommendation
ITU-T X.509 | ISO/IEC 9594-8"** — an identical text jointly published by
[[UN-ITU]]'s ITU-T sector and [[INTL-ISO]]/IEC. The current edition is
**X.509 (10/2019)**, "In force," with Amendment 1 (10/2024) and
Corrigendum 3 (07/2026), maintained by **ITU-T Study Group 17**.

## Closes a flagged gap

[[UN-ITU]]'s own file recorded `coverage: low` explicitly because "no ITU
standard is modelled." This closes that gap with the ITU's most
consequential and widely deployed standard, and simultaneously closes the
`discovery/candidates.md` carried lead making the same observation.

No sourced connection to a specific EU or national PKI/digital-identity
instrument (e.g. [[EU-EIDAS]] trust services) was found this pass, so
none is asserted; X.509 underlies such systems as a matter of general
technical knowledge, which is not the same as a sourced statement that a
specific instrument names it.

## Relationships

- `maintained-by` [[UN-ITU]] (ITU-T Study Group 17).
- `aligned-with` [[INTL-ISO]] — identical joint text with ISO/IEC 9594-8.

## Sources

Listed in frontmatter, read directly this pass.
