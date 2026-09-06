---
id: NL-BNC-SDG
type: organisation
name: Bureau Nationaal Coördinator Single Digital Gateway
alternative_names:
  - bNC-SDG
  - Nationaal Coördinator Single Digital Gateway
description: >
  The Dutch coordinating body for implementation of the EU Single Digital
  Gateway Regulation. It coordinates execution of the regulation on behalf
  of the Netherlands, supporting Dutch government organisations — which
  remain individually responsible for their own procedures and information
  — and liaising with the European Commission and other member states.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-SDG
  - NL
relationships:
  - type: implements-requirement-from
    target: EU-SDG
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP. Confirmed by reading digitaleoverheid.nl's own dedicated Single Digital Gateway page directly (2026-09-06): 'In Nederland coördineert het Bureau Nationaal Coördinator Single Digital Gateway (bNC-SDG) de uitvoering van de SDG-verordening' (in the Netherlands, the Bureau National Coordinator Single Digital Gateway coordinates implementation of the SDG regulation)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The same page states responsibility for executing the regulation is split between two ministries — 'onder verantwoordelijkheid van het ministerie van Binnenlandse Zaken en Koninkrijksrelaties en het ministerie van Economische Zaken' — neither of which the source names as the bureau's sole host, so no `part-of` edge to a single ministry entity is asserted."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Single Digital Gateway"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/europa/single-digitale-gateway/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-06"
---

# bNC-SDG — Bureau Nationaal Coördinator Single Digital Gateway

> **Created 2026-09-06**, closing part of a gap [[EU-SDG]] flagged: "the
> Dutch implementation of the gateway is likewise unresearched." Reading
> digitaleoverheid.nl's own dedicated SDG page directly confirms a national
> coordinating body, the bNC-SDG, but does **not** name [[NL-LOGIUS]] or
> [[NL-GDI]] anywhere on the page — the "plausible connection" [[EU-SDG]]'s
> own text speculated about remains unconfirmed and is not asserted here.

## Description

Confirmed by reading digitaleoverheid.nl's own page directly: "In Nederland
coördineert het Bureau Nationaal Coördinator Single Digital Gateway
(bNC-SDG) de uitvoering van de SDG-verordening" — in the Netherlands, the
Bureau National Coordinator Single Digital Gateway coordinates
implementation of the SDG regulation, [[EU-SDG]].

The same page states that "Nederlandse overheidsorganisaties zijn in
beginsel zelf verantwoordelijk voor de uitvoering van de SDG-verordening" —
Dutch government organisations are in principle themselves responsible for
implementing the regulation's obligations — with the bureau's role being
coordination rather than direct execution. Municipalities, provinces and
water boards are described as using shared "SDG-voorzieningen" (SDG
facilities) via umbrella organisations, rather than building their own.

Execution of the regulation is carried out "onder verantwoordelijkheid van
het ministerie van Binnenlandse Zaken en Koninkrijksrelaties en het
ministerie van Economische Zaken" — under the responsibility of the
Ministry of the Interior and Kingdom Relations and the Ministry of Economic
Affairs. The page does not state which of the two hosts the bureau itself,
so no `part-of` edge to either ministry is asserted; see Relationships.

## No sourced link to Logius or the GDI

[[EU-SDG]]'s own text previously speculated: "a plausible connection to
[[NL-GDI]] and [[NL-LOGIUS]] exists but is not sourced." digitaleoverheid.nl's
SDG page — a direct, current account of the Dutch implementation — names
neither. No relationship between this entity and either is asserted. The
speculative language is removed from [[EU-SDG]]'s own text accordingly,
since the specific gap it described (Dutch implementation entirely
unresearched) is now closed, even though the Logius/GDI connection itself
was not confirmed.

## Relationships

- `implements-requirement-from` [[EU-SDG]].
- `part-of` [[NL]] — anchor; responsibility is split between two ministries
  and neither is named as the bureau's host.

## Sources

Listed in frontmatter, read directly 2026-09-06.
