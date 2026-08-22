---
id: NO-ID-PORTEN
type: platform
name: ID-porten
alternative_names: []
description: >
  Norway's common public-sector login solution, providing electronic
  identification for access to national and municipal digital services. It
  is one of the national common solutions whose operation, development and
  management sit with Digitaliseringsdirektoratet.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NO-DIGDIR
related_entities:
  - NO-DIGDIR
  - NO-ALTINN
relationships: []

sources:
  - title: "ID-porten"
    url: "https://samarbeid.digdir.no/id-porten/id-porten/23"
    publisher: "Digitaliseringsdirektoratet (Digdir)"
    accessed: "2026-08-22"
  - title: "Kva er Digitaliseringsdirektoratet?"
    url: "https://www.digdir.no/digdir/kva-er-digitaliseringsdirektoratet/703"
    publisher: "Digitaliseringsdirektoratet (Digdir)"
    accessed: "2026-08-22"
  - title: "Kraftig vekst i bruk av digitale fellesløsningar"
    url: "https://www.digdir.no/digdir/kraftig-vekst-i-bruk-av-felleslosninger/1206"
    publisher: "Digitaliseringsdirektoratet (Digdir)"
    accessed: "2026-08-22"
---

# ID-porten

> **Verified 2026-08-22.** All three cited pages were fetched; two were
> read directly (`digdir.no`'s "Kva er Digitaliseringsdirektoratet?" and
> "Kraftig vekst" pages) and confirm ID-porten by name. The
> `samarbeid.digdir.no` collaboration-portal page returned only
> navigation and cookie-banner text for ID-porten's specific section —
> the substantive page content did not load as fetched — so it is
> retained as a source without being the basis for any claim here. The
> unattested alternative name "ID-porten eID" has been removed.

## Description

Confirmed by reading digdir.no directly (2026-08-22): "Bare det siste
året har antall tjenester som benytter ID-porten økt med 77 prosent"
(the number of services using ID-porten grew 77% in the last year alone).
ID-porten is Norway's common public-sector login solution — the national
electronic identification gateway for public digital services.

## ⚠ No eIDAS relationship is asserted, in either direction

Every EU member state in the Atlas has an identity platform tied to
[[EU-EIDAS]] in some way: [[ES-CLAVE]] carries
`implements-requirement-from`, and [[EU-EIDAS]] now carries `applies-in` to
six member states.

Norway is an EEA EFTA state. Whether eIDAS was incorporated into the EEA
Agreement, when, and whether ID-porten is a **notified scheme** under it,
were all **not established** in this batch.

The temptation here is obvious and specific: eIDAS notification is exactly
the kind of fact that looks safe to assume and is not. [[ES-CLAVE]] already
carries `confidence: low` precisely because "operates an eIDAS node" and
"has a notified scheme" are different claims. Making the *same* mistake
across an EEA boundary would be worse.

[[GB-ONE-LOGIN]] is recorded with "**no eIDAS relationship in either
direction**" for the parallel reason. ID-porten now joins it.

## Relationships

None asserted here. The `maintained-by` edge is asserted on
[[NO-DIGDIR]] — the Atlas never mirrors a relationship onto both ends.

## Sources

Listed in frontmatter — see the caveat above for which were read
directly.
