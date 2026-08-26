---
id: EE-ANDMEPORTAAL
type: platform
name: Estonian data portal
alternative_names:
  - avaandmed.eesti.ee
  - Eesti andmeportaal
description: >
  Estonia's national data portal, established in 2025 on the basis of the
  previous open data portal, giving an overview of government-held data as
  a single information point for public and third sector data grouped by
  dataset. It consolidates what were previously two environments: open
  data in the former portal and database descriptions in RIHA.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2025-01-01
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
  - EE-RIHA
  - EU-OPEN-DATA-DIRECTIVE
relationships:
  - type: maintained-by
    target: EE-RIA
    source: fact
    evidence: "Confirmed verbatim by reading ria.ee's own Estonian data portal page directly (2026-08-26): 'Estonian Data Portal provides an overview of the government-held data, its descriptions and possibilities for reuse. It is Estonian single information point that allows anyone interested to find public and third sector data, grouped by datasets... The Data Portal was established in 2025, building on the previous open data portal, to support the reuse of data and promote data economy.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: replaces
    target: EE-RIHA
    source: fact
    evidence: "Confirmed by reading ria.ee's own Estonian data portal page directly (2026-08-26), which corrects and dates this edge more precisely than the entity previously had it: 'Prior to this, the data collected by the state and the related descriptions were published in two environments'... 'The latter [RIHA] is currently still in use, but it is expected to be decommissioned at the end of 2026 when the legislative amendments come into force. Descriptions of the databases held by RIHA will then be added to the Data Portal.' The replacement is therefore a transition in progress, not yet complete as of this reading, with an official target date (end of 2026) this entity did not previously have."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Estonian data portal | RIA"
    url: "https://www.ria.ee/en/state-information-system/data-based-governance-and-reuse-data/estonian-data-portal"
    publisher: "Riigi Infosüsteemi Amet (RIA)"
    accessed: "2026-08-26"
  - title: "Administration system for the state information system RIHA"
    url: "https://en.wikipedia.org/wiki/Administration_system_for_the_state_information_system_RIHA"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
---

# Estonian data portal

> **Verified 2026-08-26.** Both cited pages were read directly. RIA's
> own page corrects a real gap: this entity's `replaces` edge treated
> [[EE-RIHA]]'s handover as already settled, but RIA's own page says
> RIHA "is currently still in use" and is only "expected to be
> decommissioned at the end of 2026" — a transition in progress, not a
> completed fact, with an official target date this entity did not
> previously carry. Note: `ria.ee` was read successfully via a direct
> `curl` fetch with the honest User-Agent, but `tools/reverify.py`'s own
> fetcher (Python's `urllib`) reproducibly gets a Cloudflare "Just a
> moment..." challenge on the same URL with the identical UA string —
> expect `tools/reverify.py --id EE-ANDMEPORTAAL` to report it
> UNREACHABLE despite the page being genuinely readable.

## Description

Estonia's national data portal, **established in 2025**, and the newest
national open data portal in the Atlas by several years.

## A transition still in progress, not a completed replacement

Before the portal existed, Estonian state data lived in two places:
**open data** in the previous open data portal, and **descriptions of
the databases** in [[EE-RIHA]]. Confirmed by reading ria.ee directly,
this split is not yet fully closed: RIHA "is currently still in use,
but it is expected to be decommissioned at the end of 2026 when the
legislative amendments come into force. Descriptions of the databases
held by RIHA will then be added to the Data Portal." The portal is also
integrated with **RIHAKE**, a data management application named on the
same page that lets organisations publish datasets automatically into
the Data Portal — a component this entity did not previously carry and
does not yet warrant its own entity.

That split is not an Estonian peculiarity. It is the ordinary arrangement
everywhere else in the Atlas: [[NL-DATA-OVERHEID]] and
[[NL-BASISREGISTRATIES]] are separate things, as are
[[ES-DATOS-GOB-ES]]/[[ES-NTI-RISP]] and [[FR-DATA-GOUV]]. Estonia merging
the catalogue of *datasets* with the catalogue of *systems* is a design
choice the Atlas can now show, because it holds both halves — and, as of
this pass, is watching the merge actually complete on a public timeline.

## Relationships

- `maintained-by` [[EE-RIA]].
- `replaces` [[EE-RIHA]]'s data-description role, a transition RIA's
  own page dates to "the end of 2026."

## Sources

Listed in frontmatter, both read directly this pass.

