---
id: NO-SIKKERHETSLOVEN
type: law
name: Lov om nasjonal sikkerhet (sikkerhetsloven)
alternative_names:
  - Sikkerhetsloven
  - National Security Act (Norway)
  - "LOV-2018-06-01-24"
description: >
  Norway's National Security Act, enacted 1 June 2018 and in force from
  1 January 2019, repealing the 1998 Act on Preventive Security Services
  (lov 20. mars 1998 nr. 10 om forebyggende sikkerhetstjeneste). It aims
  to protect Norway's sovereignty, territorial integrity and democratic
  governance from security-threatening activities, updating the
  preventive-security framework for evolving threats and technological
  change. The Nasjonal sikkerhetsmyndighet (NSM) operates under it.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2019-01-01
end_date: null
last_verified: "2026-09-12"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - "NO"
  - NO-NSM
relationships:
  - type: applies-in
    target: "NO"
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Confirmed by reading lovdata.no's own text of LOV-2018-06-01-24 directly (2026-09-05, re-confirmed 2026-09-12): 'Lov om nasjonal sikkerhet (sikkerhetsloven),' enacted 1 June 2018, in force from 1 January 2019, its own §12-2 repealing 'lov 20. mars 1998 nr. 10 om forebyggende sikkerhetstjeneste' (the 1998 Act on Preventive Security Services)."
    confidence: high
    valid_from: 2019-01-01
    valid_until: null

sources:
  - title: "Lov om nasjonal sikkerhet (sikkerhetsloven) — LOV-2018-06-01-24"
    url: "https://lovdata.no/dokument/NL/lov/2018-06-01-24"
    publisher: "Lovdata"
    accessed: "2026-09-12"
---

# Lov om nasjonal sikkerhet (sikkerhetsloven)

> **Created 2026-09-12**, closing `discovery/unresolved.md` row #111:
> [[NO-NSM]]'s own statutory basis was named and dated in its file's body
> text (2026-09-05 finding) but never modelled as an entity, so no
> `governed-by` edge could be asserted. `lovdata.no`'s own text of
> LOV-2018-06-01-24 was read directly.

## Description

Confirmed by reading `lovdata.no` — Norway's official legal-text
database — directly: **"Lov om nasjonal sikkerhet (sikkerhetsloven)"**
(the National Security Act), enacted **1 June 2018**, in force from
**1 January 2019**. Its own §12-2 repeals **"lov 20. mars 1998 nr. 10 om
forebyggende sikkerhetstjeneste"** (the 1998 Act on Preventive Security
Services) — the predecessor [[NO-NSM]]'s own file had already identified
via the same source, closing an earlier "which act is current" finding
on that entity.

Per the Act's own stated purpose: to protect Norway's sovereignty,
territorial integrity and democratic governance from
security-threatening activities, updating the preventive-security
framework the 1998 Act provided for evolving threats and technological
change.

## Relationships

- `applies-in` [[NO]] — scope anchor. [[NO-NSM]] carries the inverse
  `governed-by` edge pointing here, recorded on its own file.

## Not modelled

- The 1998 predecessor act, named above only in prose — no `supersedes`
  edge is asserted since it is not itself an Atlas entity.
- The Act's substantive chapters beyond the repeal and purpose recorded
  above — no section-level detail was read this pass.
- **Digitalsikkerhetsloven og -forskriften**, a separate, newer
  digital-security statute NSM's own site lists alongside this Act —
  named on [[NO-NSM]]'s own file, not investigated further here.

## Sources

Listed in frontmatter, read directly 2026-09-12 (carried over from a
2026-09-05 read on [[NO-NSM]]'s own file).
