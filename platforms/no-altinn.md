---
id: NO-ALTINN
type: platform
name: Altinn
description: >
  Norway's national platform for digital dialogue between public agencies,
  businesses and citizens, providing shared services for forms, reporting,
  authorisation and messaging. It is one of the society-critical common
  solutions Digitaliseringsdirektoratet is modernising.

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
  - "NO"
  - NO-DIGDIR
  - NO-ID-PORTEN
relationships:
  - type: part-of
    target: "NO"
    source: fact
    evidence: "Confirmed by reading altinn.no directly (2026-08-22), whose homepage carries the Digdir logo throughout and identifies its publisher in the footer as 'Digdir Digitaliseringsdirektoratet, Postboks 1382 Vika, 0114 Oslo. Org.nr. 991 825 827.' digdir.no independently names Altinn among the society-critical common solutions Digitaliseringsdirektoratet is modernising. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NO-DIGDIR
    source: interpretation
    evidence: "altinn.no's own site footer, read directly (2026-08-22), identifies the publisher as 'Digdir Digitaliseringsdirektoratet, Postboks 1382 Vika, 0114 Oslo. Org.nr. 991 825 827' — Digdir's own organisation number and address, appearing on Altinn's own site rather than in a third-party description. This is new evidence this pass: the entity previously found no source naming Altinn's current operator, only its historical association with Brønnøysundregistrene. A site's own publisher footer is not the same claim as an explicit 'Digdir operates Altinn' sentence, hence `source: interpretation` rather than `fact`."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Altinn"
    url: "https://www.altinn.no/"
    publisher: "Altinn / Digitaliseringsdirektoratet"
    accessed: "2026-08-22"
  - title: "Kraftig vekst i bruk av digitale fellesløsningar"
    url: "https://www.digdir.no/digdir/kraftig-vekst-i-bruk-av-felleslosninger/1206"
    publisher: "Digitaliseringsdirektoratet (Digdir)"
    accessed: "2026-08-22"
---

# Altinn

> **Verified 2026-08-22.** Both cited pages were read directly. A finding
> changes this entity's previous conclusion: see "A custodian found after
> all" below.

## Description

Confirmed by reading altinn.no directly (2026-08-22). Altinn is Norway's national platform for digital dialogue between public
agencies, businesses and citizens. The sources name it, alongside
[[NO-ID-PORTEN]], among the **society-critical common solutions**
[[NO-DIGDIR]] is modernising.

## A custodian found after all — at low confidence

This entity previously concluded that no source named Altinn's current
operator: Digdir's own page lists what it has *responsibility for
operation, development and management* of — ID-porten, the contact and
reservation register, the digital mailbox, eSignering, ELMA, eInnsyn,
eFormidling — and Altinn is not on that list, appearing instead in a
sentence about solutions Digdir *modernises*.

That distinction still holds; no source states in a sentence that Digdir
operates Altinn. But reading altinn.no's own site directly this pass
found something the earlier search-only compile could not: the site's
own footer publisher block reads "Digdir Digitaliseringsdirektoratet,
Postboks 1382 Vika, 0114 Oslo. Org.nr. 991 825 827" — Digdir's own
address and organisation number, on Altinn's own page. `maintained-by`
[[NO-DIGDIR]] is now asserted on that basis, at `confidence: low` and
`source: interpretation` — a publisher footer is real evidence of who
currently runs a site, but it is not the same claim as an explicit
operating statement.

Altinn was historically operated by the Brønnøysund Register Centre
(Brønnøysundregistrene). Whether that arrangement has formally ended, or
Digdir now operates the technical platform under a continuing
Brønnøysundregistrene role, was not established.

## Not modelled

- **Brønnøysundregistrene**, the register centre — which would also be
  Norway's entry point into the business-register layer where [[NL-NHR]]
  sits.
- Altinn's **service catalogue** and its authorisation model.

## Relationships

- `part-of` [[NO]].
- `maintained-by` [[NO-DIGDIR]], at `confidence: low` — see above.

## Sources

Listed in frontmatter, both read directly this pass.
