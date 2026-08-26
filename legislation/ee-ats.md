---
id: EE-ATS
type: law
name: Avaliku teabe seadus
alternative_names:
  - Public Information Act
  - AvTS
  - RT I 2000, 92, 597
description: >
  Estonian Public Information Act, cited as the legal basis — together
  with a special regulation — for RIHA, the administration system for the
  state information system. Its Riigi Teataja citation is recorded as RT I
  2000, 92, 597.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EE
  - EE-RIHA
  - EU-OPEN-DATA-DIRECTIVE
relationships:
  - type: applies-in
    target: EE
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org's RIHA article directly (2026-08-26), which cites the Public Information Act (Riigikogu, RT I 2000, 92, 597) as regulating RIHA. No source read gives an exact enactment day beyond the year embedded in the Riigi Teataja citation, so `start_date` is left unset rather than guessed — the entity previously carried a fabricated 2000-01-01. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Administration system for the state information system RIHA"
    url: "https://en.wikipedia.org/wiki/Administration_system_for_the_state_information_system_RIHA"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
  - title: "Open Source Software Country Intelligence Report Estonia 2025"
    url: "https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/OSS%20Country%20Intelligence%20Report%20Estonia%202025.pdf"
    publisher: "European Commission — Interoperable Europe"
---

# Avaliku teabe seadus

> **Verified 2026-08-26.** Wikipedia's RIHA article was read directly.
> The Interoperable Europe PDF now 404s at its cited URL — the
> Commission appears to have reorganised or removed the report, and no
> replacement URL for it was found this pass; the domain itself is
> reachable. The fabricated `start_date: 2000-01-01` is corrected to
> unset — no source gives an exact day, only the year embedded in the
> Riigi Teataja citation (RT I 2000, 92, 597).

## Description

Estonia's **Public Information Act** — the statutory basis given for
[[EE-RIHA]], and the act that carries Estonian public-sector information
re-use.

## The one Estonian statutory anchor found

Sources name it plainly as the regulator of RIHA, together with a special
regulation. Beyond that, what this act does — how it structures access,
whether it is also the Open Data Directive vehicle — is **not established by
anything read**.

That matters because Estonia is the eighteenth Atlas country and the
seventeenth whose Open Data Directive position is unrecorded. No
`implements-requirement-from` edge to [[EU-OPEN-DATA-DIRECTIVE]] is asserted
here: Estonia was **not** among the nineteen member states served with
letters of formal notice in September 2021, which suggests it notified on
time, but that is an inference and the instrument is unidentified.

## Sources

Listed in frontmatter.

