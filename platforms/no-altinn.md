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
last_verified: "2026-09-13"
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
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #110). Upgraded from `source: interpretation` (a publisher footer alone) by reading no.wikipedia.org's own Brønnøysundregistrene article directly (2026-09-13), which states explicitly: 'Brønnøysundregistrene hadde frem til 1. januar 2020 forvaltningsansvar for Altinn. Da ble Altinn en del av Digitaliseringsdirektoratet sammen med tidligere Direktoratet for forvaltning og IKT' (Brønnøysundregistrene held administrative responsibility for Altinn until 1 January 2020, when Altinn became part of Digitaliseringsdirektoratet together with the former Directorate for Administration and ICT). This is an explicit operating-transfer statement, not an inference from a footer, though it rests on a secondary (Wikipedia) rather than primary source — `confidence: medium` rather than `high`. Independently, altinn.no's own footer (read 2026-08-22) already named Digdir as publisher, and brreg.no's own history page, read directly this pass, does not contradict the transfer (it only dates Altinn's 2003 founding and does not itself discuss the 2020 change)."
    confidence: medium
    valid_from: 2020-01-01
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
  - title: "Brønnøysundregistrene"
    url: "https://no.wikipedia.org/wiki/Br%C3%B8nn%C3%B8ysundregistrene"
    publisher: "Wikipedia (Norwegian)"
    accessed: "2026-09-13"
  - title: "Our history"
    url: "https://www.brreg.no/en/about-us-2/this-is-us/our-history/"
    publisher: "Brønnøysundregistrene"
    accessed: "2026-09-13"
    note: "Confirms Altinn's 2003 founding; does not itself discuss the 2020 operational transfer, so does not independently corroborate it."
---

# Altinn

> **Verified 2026-08-22.** Both cited pages were read directly. A finding
> changes this entity's previous conclusion: see "A custodian found after
> all" below.
>
> **Updated 2026-09-13**: the `maintained-by` edge is upgraded to
> `source: fact`, closing `discovery/unresolved.md` row #110 — see below.

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

That distinction still held as of the 2026-08-22 pass; no source read
then stated in a sentence that Digdir operates Altinn, only that
altinn.no's own footer publisher block reads "Digdir
Digitaliseringsdirektoratet, Postboks 1382 Vika, 0114 Oslo. Org.nr. 991
825 827" — real evidence, but not an explicit operating statement.

**Closed 2026-09-13**: reading `no.wikipedia.org`'s own Brønnøysundregistrene
article directly supplies the explicit statement. It says plainly:
"Brønnøysundregistrene hadde frem til 1. januar 2020 forvaltningsansvar
for Altinn. Da ble Altinn en del av Digitaliseringsdirektoratet sammen
med tidligere Direktoratet for forvaltning og IKT" (Brønnøysundregistrene
held administrative responsibility for Altinn until 1 January 2020, when
Altinn became part of Digitaliseringsdirektoratet together with the
former Directorate for Administration and ICT). Brønnøysundregistrene's
own "Our history" page, also read directly, confirms Altinn's 2003
founding without contradicting the transfer — it simply does not discuss
it. `maintained-by` [[NO-DIGDIR]] is upgraded to `source: fact`,
`confidence: medium` (a secondary rather than primary source, but an
explicit statement rather than an inferred one), with `valid_from`
2020-01-01.

## Not modelled

- **Brønnøysundregistrene**, the register centre — which would also be
  Norway's entry point into the business-register layer where [[NL-NHR]]
  sits. It retains no sourced ongoing role in Altinn since the 2020
  transfer.
- Altinn's **service catalogue** and its authorisation model.

## Relationships

- `part-of` [[NO]].
- `maintained-by` [[NO-DIGDIR]] — since 1 January 2020, upgraded to
  `source: fact` 2026-09-13.

## Sources

Listed in frontmatter. The original two were read directly in the
2026-08-22 pass; the Wikipedia article and Brønnøysundregistrene's own
history page were added and read directly 2026-09-13.
