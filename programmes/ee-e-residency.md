---
id: EE-E-RESIDENCY
type: programme
name: e-Residency of Estonia
alternative_names:
  - e-Residency
  - Estonian e-Residency programme
description: >
  Estonian programme launched on 1 December 2014 allowing non-Estonians
  access to Estonian services including company formation, banking,
  payment processing and taxation, through a state-issued digital identity
  that carries no residence or citizenship rights.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2014-12-01
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EE
  - EE-RIA
  - EU-EIDAS2
relationships:
  - type: part-of
    target: EE
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org's e-Residency article directly (2026-08-26): 'e-Residency of Estonia... is a program launched by Estonia on 1 December 2014. The program allows non-Estonians access to Estonian services such as company formation, banking, payment processing, and taxation.' Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "E-Residency of Estonia"
    url: "https://en.wikipedia.org/wiki/E-Residency_of_Estonia"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
  - title: "case study — e-Estonia: digital society & open data"
    url: "https://urbact.eu/sites/default/files/2024-07/E-Estonia%20Case%20Study.pdf"
    publisher: "URBACT"
    accessed: "2026-08-26"
---

# e-Residency of Estonia

> **Verified 2026-08-26.** Both cited pages were read directly.
> Wikipedia's article confirms the launch date verbatim and adds real
> operational detail this entity did not previously carry. No page
> read mentions eIDAS or the European Digital Identity Wallet, so the
> entity's own "what the Atlas cannot say" caveat below stands
> unchanged.

## Description

Estonia's programme giving **non-Estonians** access to Estonian digital
services — company formation, banking, payment processing and taxation —
launched on **1 December 2014**. Confirmed by reading Wikipedia's
article directly: the first e-resident was British journalist Edward
Lucas; a digital ID smart card, issued by the Estonian Police and
Border Guard Board in Estonia or at an embassy, is used to access
services; the certificate is valid for **five years**, up from three
when the programme was first announced; and e-Residency itself "does
not have an effect on income taxation — neither does it establish an
income tax liability in Estonia nor does it relieve from income
taxation in the resident's home country."

## The one thing in the Atlas that decouples service from territory

Every other national entity here is scoped to the people and bodies inside a
country. [[FR-FRANCECONNECT]], [[ES-CLAVE]] and [[PL-MOBYWATEL]] all identify
residents to their own state. (The Netherlands would belong in that list too,
but **DigiD is not an Atlas entity** — a gap this comparison exposed, now
queued.)

e-Residency does not. It issues a state-backed digital identity to people
with **no residence, presence or citizenship** in the issuing country, for
use with that country's services. That is a different proposition from
digital identity as the Atlas otherwise models it, and it is why Estonia
appears in discussions of digital government far out of proportion to its
size.

## ⚠ What the Atlas cannot say about it

The interesting questions are all outside the model: what legal status an
e-resident has, how the identity interacts with [[EU-EIDAS2]] and the
European Digital Identity Wallet, and whether other states have copied it.
None was established by anything read, and the `level` vocabulary has no
term for a service whose users are deliberately not in the country.

## Relationships

- `part-of` [[EE]] — anchor edge.

## Sources

Listed in frontmatter, both read directly this pass.

