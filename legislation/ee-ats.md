---
id: EE-ATS
type: act
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
rank: ordinary
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
organisations:
  - EE-RIA
related_entities:
  - EE
  - EE-RIHA
  - EU-OPEN-DATA-DIRECTIVE
relationships:
  - type: applies-in
    target: EE
    source: fact
    evidence: "The Information System Authority's own RIHA page (ria.ee), read directly 2026-11-22, lists the 'Public Information Act' among RIHA's legal acts and links to its consolidated English text on Riigi Teataja (ELI 522032022002); the same page says that the Data Protection Inspectorate, in the RIHA approval process, checks whether planned data processing corresponds to the principles of the Constitution, the Personal Data Protection Act and the Public Information Act. The original publication reference (RT I 2000, 92, 597) still rests on an encyclopedia, because Riigi Teataja itself needs JavaScript (roadmap #767). No source read gives an exact day of entry into force, so `start_date` stays unset. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "RIHA and RIHAKE — Information System Authority"
    url: "https://www.ria.ee/en/state-information-system/data-based-governance-and-reuse-data/administration-system-riha-and-rihake"
    publisher: "Information System Authority (RIA)"
    accessed: "2026-11-22"
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

## Which body

[[EE-RIA]] is listed under `organisations` because it maintains [[EE-RIHA]], which this instrument governs (the edges are on [[EE-RIHA]]). That is an association drawn from edges the Atlas already holds, not a statement of the instrument's text: which authority supervises compliance with it was not read. (Added 2026-11-14, roadmap #770.)

## Sources

Listed in frontmatter.

