---
id: UN-IMO
type: organisation
name: International Maritime Organization
alternative_names:
  - IMO
description: >
  UN specialised agency responsible for the safety and security of
  shipping and the prevention of marine and atmospheric pollution by
  ships — the global standard-setting authority for the safety, security
  and environmental performance of international shipping. Regulates
  ship design, construction, equipment, manning, operation and disposal.
  Maintains GISIS, its integrated shipping-information database.

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
organisations: []
related_entities:
  - UN
  - UN-IMO-GISIS
  - UN-LOCODE
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Confirmed by reading imo.org's own 'About' page directly (2026-09-05): 'The IMO is the United Nations specialized agency with responsibility for the safety and security of shipping and the prevention of marine and atmospheric pollution by ships,' described as 'the global standard-setting authority for the safety, security and environmental performance of international shipping.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "About IMO"
    url: "https://www.imo.org/en/About/Pages/Default.aspx"
    publisher: "International Maritime Organization"
    accessed: "2026-09-05"
---

# International Maritime Organization (IMO)

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/candidates.md` had explicitly declined to create IMO "to
> carry one code list," calling that a thin entity. This pass read
> `imo.org`'s own "About" page directly and found IMO's substantive
> mandate as a full UN specialised agency, which clears that bar —
> the entity now exists on its own merits, not to carry the code list.

## Description

Reading `imo.org`'s own page directly: IMO is the **UN specialised
agency** responsible for the **safety and security of shipping** and the
**prevention of marine and atmospheric pollution by ships** — "the global
standard-setting authority for the safety, security and environmental
performance of international shipping." Its regulatory scope covers "ship
design, construction, equipment, manning, operation and disposal," aiming
to create "a level playing-field so that ship operators cannot address
their financial issues by simply cutting corners."

## GISIS and UN/LOCODE

IMO maintains **GISIS** (Global Integrated Shipping Information System),
now a separate Atlas entity: [[UN-IMO-GISIS]]. `discovery/candidates.md`
had separately noted that [[EU-EMSWE]]'s common location database holds
[[UN-LOCODE]] alongside IMO port-facility codes registered in GISIS — a
genuine cross-body code-sharing arrangement, though no source read this
pass states IMO maintains UN/LOCODE itself, so no relationship beyond
`related_entities` is asserted there.

## Relationships

- Part of [[UN]] as a specialised agency.
- `maintained-by` edge (IMO as target) recorded on [[UN-IMO-GISIS]]'s
  own file.

## Sources

Listed in frontmatter, read directly this pass.
