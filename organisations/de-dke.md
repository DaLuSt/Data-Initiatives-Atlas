---
id: DE-DKE
type: organisation
name: Deutsche Kommission Elektrotechnik Elektronik Informationstechnik
alternative_names:
  - DKE
  - German Commission for Electrotechnical, Electronic and Information Technologies
description: >
  German standards committee for electrical engineering, electronics
  and information technology, established in 1970 when DIN and VDE
  merged all German electrotechnical associations into it. It is a
  joint organisation of DIN and the VDE (Verband der Elektrotechnik
  Elektronik Informationstechnik), with day-to-day operational and
  legal responsibility held by VDE, and is listed among DIN's own
  standards committees. DKE represents Germany as the national member
  in CENELEC (electrotechnical standardisation), IEC and, for
  telecommunications standards, ETSI as Germany's national
  standardisation organisation.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 1970-01-01
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-DIN
  - EU-CENELEC
  - INTL-ISO
relationships:
  - type: part-of
    target: DE-DIN
    source: fact
    evidence: "Confirmed by reading din.de's own page directly (2026-09-04), which lists DKE among DIN's own standards committees ('Getting involved > Standards committees > DKE') and states DKE is 'a joint organization of DIN German Institute for Standardization and the VDE Association for Electrical, Electronic & Information Technologies', with VDE handling day-to-day operations. dke.de's own 'About us' page, also read directly, confirms DKE was established in 1970 when DIN and VDE merged all German electrotechnical associations into it, and that DKE's legal standing was further formalised five years later through a Standards Agreement between DIN and the Federal Republic of Germany. No Atlas entity exists for VDE, so only the DIN half of DKE's joint governance is recorded as a typed edge."
    confidence: medium
    valid_from: 1970-01-01
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "Confirmed by reading din.de's own page directly (2026-09-04): DKE is 'the German member of' CENELEC, the European Committee for Electrotechnical Standardization, Brussels — alongside equivalent national-member roles for IEC and, for telecommunications standards specifically, ETSI (as Germany's national standardisation organisation)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "DKE"
    url: "https://www.din.de/en/getting-involved/standards-committees/dke"
    publisher: "DIN — Deutsches Institut für Normung"
    accessed: "2026-09-04"
  - title: "The DKE Organization"
    url: "https://www.dke.de/en/about-us/the-dke-organization"
    publisher: "DKE"
    accessed: "2026-09-04"
---

# DKE — Deutsche Kommission Elektrotechnik Elektronik Informationstechnik

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged DKE as [[DE-DIN]]'s
> counterpart towards [[EU-CENELEC]] — one of Germany's largest
> unmodelled standardisation gaps. Both cited pages, DIN's own and
> DKE's own, were read directly this pass.

## Description

DKE is Germany's standards committee for electrical engineering,
electronics and information technology, established in **1970** when
DIN and VDE merged all German electrotechnical associations into it.
Reading `dke.de`'s own "About us" page directly: **"In 1970, DIN and
VDE merged all German electrotechnical associations into the Deutschen
Kommission Elektrotechnik Elektronik Informationstechnik (DKE)."** Its
legal standing was further formalised five years later through a
Standards Agreement between DIN and the Federal Republic of Germany.

## A joint body, one edge recorded

DKE is **jointly** run by [[DE-DIN]] and the **VDE** (Verband der
Elektrotechnik Elektronik Informationstechnik), with day-to-day
operational and legal responsibility held by VDE — confirmed by reading
`din.de`'s own page directly. VDE is not an Atlas entity, so only the
DIN half of this joint governance is recorded as a typed `part-of` edge;
VDE's role is described here in prose.

## Germany's electrotechnical voice in three international bodies

Reading `din.de`'s own page directly, DKE is Germany's national member
in:

- **[[EU-CENELEC]]** — the European Committee for Electrotechnical
  Standardization, Brussels;
- **IEC** — the International Electrotechnical Commission, Geneva;
- **ETSI** — where DKE serves specifically as Germany's national
  standardisation organisation (NSO) for telecommunications standards.

This makes DKE the electrotechnical-standards counterpart to [[DE-DIN]]
itself, which the Atlas already records as Germany's member in
[[EU-CEN]] and [[INTL-ISO]].

## Relationships

- `part-of` [[DE-DIN]].
- `participates-in` [[EU-CENELEC]].

## Sources

Listed in frontmatter, both read directly this pass.
