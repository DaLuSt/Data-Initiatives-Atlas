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
last_verified: "2026-09-19"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NO-DIGDIR
related_entities:
  - NO-DIGDIR
  - NO-ALTINN
  - EU-EIDAS
  - INTL-EEA-JCD-22-2018
relationships:
  - type: aligned-with
    target: EU-EIDAS
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #109. The European Commission's own eID User Community page ('Overview of pre-notified and notified eID schemes under eIDAS', digital-building-blocks.ec.europa.eu — a domain genuinely different from the blocked efta.int/EUR-Lex EEA-supplement pages), read directly (2026-09-18), lists two Norwegian schemes as formally NOTIFIED (not merely pre-notified) as of 24 October 2022: 'Norwegian eID scheme BankID' and 'Norwegian eID scheme Buypass ID', both at assurance level High. `type: aligned-with` rather than `implements-requirement-from`: BankID and Buypass ID, not ID-porten itself, are the notified schemes — ID-porten is the login gateway that lets citizens authenticate using them, alongside other means, so it does not itself carry the notification. UPDATED 2026-09-19: the EEA Joint Committee Decision incorporating eIDAS is now identified and read directly — [[INTL-EEA-JCD-22-2018]] (No 22/2018 of 9 February 2018), found via a working efta.int document-store path rather than the blocked eea-lex viewer. See below."
    confidence: medium
    valid_from: "2022-10-24"
    valid_until: null

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
  - title: "Overview of pre-notified and notified eID schemes under eIDAS"
    url: "https://ec.europa.eu/digital-building-blocks/sites/spaces/EIDCOMMUNITY/pages/48762251/Overview+of+pre-notified+and+notified+eID+schemes+under+eIDAS"
    publisher: "European Commission — eID User Community, Digital Building Blocks"
    accessed: "2026-09-18"
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
>
> **Partially closed 2026-09-18** (`discovery/unresolved.md` row #109):
> the Commission's own eIDAS notification page confirms two of the eID
> schemes ID-porten integrates, BankID and Buypass ID, are formally
> notified — not merely pre-notified. See "eIDAS notification, half
> answered" below.
>
> **Closed 2026-09-19**: the other half of row #109 — the specific EEA
> Joint Committee Decision incorporating eIDAS — is now sourced. See
> "eIDAS notification, fully answered" below.

## Description

Confirmed by reading digdir.no directly (2026-08-22): "Bare det siste
året har antall tjenester som benytter ID-porten økt med 77 prosent"
(the number of services using ID-porten grew 77% in the last year alone).
ID-porten is Norway's common public-sector login solution — the national
electronic identification gateway for public digital services.

## eIDAS notification, fully answered — 2026-09-19

The first question this row asked — the specific EEA Joint Committee
Decision incorporating eIDAS — is now sourced: [[INTL-EEA-JCD-22-2018]],
Decision No 22/2018 of 9 February 2018, read directly via a working
`efta.int` document-store path (`efta.int/sites/default/files/documents/...`)
rather than the still-blocked `eea-lex` viewer or homepage. It incorporates
Regulation (EU) No 910/2014 into Annex XI of the EEA Agreement, entering
into force **10 February 2018**. That confirms directly what the notified
BankID/Buypass ID status below could previously only support indirectly.

## eIDAS notification, half answered — 2026-09-18

Every EU member state in the Atlas has an identity platform tied to
[[EU-EIDAS]] in some way: [[ES-CLAVE]] carries
`implements-requirement-from`, and [[EU-EIDAS]] now carries `applies-in` to
six member states.

Norway is an EEA EFTA state, and this row asked two things: whether eIDAS
was incorporated into the EEA Agreement, and whether ID-porten is tied to
a **notified scheme** under it.

The second is now answered, with a distinction worth keeping precise. The
Commission's own eID User Community page, read directly, lists two
Norwegian schemes as formally **NOTIFIED** (not merely pre-notified) as of
**24 October 2022**: *Norwegian eID scheme BankID* and *Norwegian eID
scheme Buypass ID*, both at assurance level **High**. These are two of
the authentication means ID-porten lets citizens use — ID-porten itself is
the login gateway, not one of the notified schemes, the same distinction
[[ES-CLAVE]] already draws for Spain. `aligned-with` is recorded on that
basis rather than a stronger type.

The first question — the specific EEA Joint Committee Decision
incorporating eIDAS — is answered above: [[INTL-EEA-JCD-22-2018]],
read directly 2026-09-19. Formal eIDAS notification under Article 9 being
open to EEA states only *after* incorporation is no longer needed as
indirect evidence; the incorporating decision itself is now cited.

The temptation this section warned about — treating "operates an eIDAS
node" and "has a notified scheme" as the same claim — is avoided: the
notified schemes are named specifically, and ID-porten is not folded into
that status by association.

[[GB-ONE-LOGIN]] is recorded with "no eIDAS relationship in either
direction" for the parallel reason it still applies to ID-porten itself,
even though the schemes it aggregates are no longer disconnected from
eIDAS.

## Relationships

- `aligned-with` [[EU-EIDAS]] — `confidence: medium`. See above.

The `maintained-by` edge is asserted on [[NO-DIGDIR]] — the Atlas never
mirrors a relationship onto both ends. [[INTL-EEA-JCD-22-2018]] carries
the `applies-in` edges for the underlying EEA-incorporation chain; this
entity's own `aligned-with` [[EU-EIDAS]] edge is the effect that chain
produces at the platform level.

## Sources

Listed in frontmatter — see the caveat above for which of the original
three were read directly. The Commission's own eIDAS notification page
was added and read directly 2026-09-18. EEA Joint Committee Decision No
22/2018 was found and read directly 2026-09-19, closing the row's other
half — see [[INTL-EEA-JCD-22-2018]] for the full text and its own sourcing
notes on the working `efta.int` document-store path.
