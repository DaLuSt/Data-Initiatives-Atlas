---
id: NL-WET-BRP
type: law
name: Wet basisregistratie personen
alternative_names:
  - Wet BRP
description: >
  Dutch act forming the basis for the registration of personal data in the
  Basisregistratie Personen. In force since 6 January 2014, it replaced the
  municipal GBA registrations with a single central national registration
  and sets out the requirements on managers and users of the BRP.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2014-01-06
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-BASISREGISTRATIES
relationships:
  - type: applies-to
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading rvig.nl's own legislation page directly (2026-08-27): 'De Wet Basisregistratie Personen (Wet BRP) vormt sinds 2014 de basis voor de registratie van persoonsgegevens' (the Wet BRP has formed the basis for personal-data registration since 2014). A WebSearch cross-check of wetten.overheid.nl's own consolidated-text archive (BWBR0033715) independently confirms the exact commencement date as 6 January 2014 (the archive holds a version keyed '/2014-01-06'). digitaleoverheid.nl's own BRP page, also read directly, corroborates the Wet BRP as the register's statutory foundation. rijksoverheid.nl's own BRP page, also read directly, adds that the Autoriteit Persoonsgegevens oversees GDPR compliance for BRP data but does not itself restate the commencement date."
    confidence: high
    valid_from: 2014-01-06
    valid_until: null

sources:
  - title: "Wetgeving Basisregistratie Personen"
    url: "https://www.rvig.nl/wetgeving-basisregistratie-personen"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
    accessed: "2026-08-27"
  - title: "BRP — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brp/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Basisregistratie Personen (BRP)"
    url: "https://www.rijksoverheid.nl/onderwerpen/privacy-en-persoonsgegevens/basisregistratie-personen-brp"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
---

# Wet basisregistratie personen (Wet BRP)

> **Verified 2026-08-27.** All three cited pages read directly. The 6
> January 2014 commencement date is independently cross-checked against
> wetten.overheid.nl's own consolidated-text archive via WebSearch, which
> keys a version of the Act to that exact date.

## Description

The Wet BRP has formed the basis for the registration of personal data in
the Basisregistratie Personen since it came into effect on 6 January 2014.
It created the foundation for a single central national database of personal
data, replacing the local Gemeentelijke Basisadministraties (GBA). The act
sets out the requirements that managers and users of the BRP must meet, and
the purposes for which BRP information may be used.

Data recorded includes at least: name and first names; date, place and
country of birth; data on parents, marriage or registered partnership, and
children; nationality and, where applicable, residence rights; address; and
the burgerservicenummer (BSN).

BRP personal data are not public. Only organisations performing a societal
task may obtain data from it, and where an organisation does so, that fact
remains visible for twenty years.

The BRP is administered by [[NL-RVIG]] (Rijksdienst voor
Identiteitsgegevens), now a separate Atlas entity re-verified alongside
this one this pass — the description here previously called it unmodelled,
which is no longer accurate.

## Relationships

- Governs the BRP, one of the registrations within
  [[NL-BASISREGISTRATIES]].
- Interacts with [[NL-UAVG]] and [[EU-GDPR]]: rijksoverheid.nl's own BRP
  page, read directly this pass, names the "Algemene Verordening
  Gegevensbescherming" alongside the Wet BRP as the register's legal
  frameworks and the Autoriteit Persoonsgegevens as the compliance
  overseer. That is closer to a sourced link than the prior pass had, but
  still short of naming a specific obligation this Act imposes under the
  GDPR/UAVG; no relationship is asserted, consistent with the prior pass's
  caution.

## Sources

Listed in frontmatter, all three read directly this pass — RvIG's own
legislation page, the digitaleoverheid.nl BRP page, and rijksoverheid.nl's
BRP page.
