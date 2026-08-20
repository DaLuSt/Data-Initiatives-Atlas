---
id: NL-NORA
type: framework
name: Nederlandse Overheid Referentie Architectuur
alternative_names:
  - NORA
  - Dutch Government Reference Architecture
description: >
  Reference architecture and interoperability framework for the Dutch
  government. NORA translates legislation, policy and standards into
  architectural principles, descriptions and models, to help public bodies
  design coherent, reliable and accessible digital services. Commissioned by
  the Ministry of the Interior and Kingdom Relations, managed by ICTU.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-ICTU
  - NL-BZK
related_entities:
  - NL-GEMMA
  - NL-EAR
  - NL-RORA
  - NL-PETRA
  - NL-ROSA
relationships:
  - type: maintained-by
    target: NL-ICTU
    source: fact
    evidence: "NORA management is entrusted to ICTU, with BZK as opdrachtgever; the NORA gebruikersraad meets at ICTU (ictu.nl, noraonline.nl)."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: owned-by
    target: NL-BZK
    source: fact
    evidence: "The Ministry of BZK is described as opdrachtgever for NORA (noraonline.nl, ictu.nl)."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Positionering NORA"
    url: "https://www.noraonline.nl/wiki/Positionering_NORA"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-20"
  - title: "NORA (Nederlandse Overheid Referentie Architectuur)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/nora/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-20"
  - title: "Overheidsarchitectuur NORA"
    url: "https://www.ictu.nl/diensten/dienstenoverzicht/overheidsarchitectuur-nora/"
    publisher: "ICTU"
    accessed: "2026-08-20"
---

# Nederlandse Overheid Referentie Architectuur (NORA)

> **Verified 2026-08-20.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.

## Description

NORA is the reference architecture for the Dutch government: a body of
frameworks and agreements for organising information management, described
as the interoperability framework for the Dutch public sector. Its function
is translational — it takes legislation, policy and standards and expresses
them as architectural principles, descriptions and models, so that public
bodies can design digital services that are coherent, reliable and
accessible, and that remain aligned with legal requirements, societal
expectations and technological change.

[[NL-BZK]] is the contracting authority (opdrachtgever); management
(beheer) is entrusted to [[NL-ICTU]], where the NORA user council meets.

NORA sits at the top of a family of Dutch reference architectures, added in
Batch 4:

| Tier | Architecture |
|---|---|
| Municipalities | [[NL-GEMMA]] |
| Central government | [[NL-EAR]] → [[NL-RORA]] (successor since 2024) |
| Provinces | [[NL-PETRA]] |
| Education sector | [[NL-ROSA]] |
| Water authorities | WILMA — not yet an entity, queued |

Only [[NL-GEMMA]] carries a sourced `based-on` relationship to NORA. For the
others the derivation is likely but was not sourced, so it is **not**
asserted — the family membership is recorded through `related_entities`
instead, which claims association without claiming derivation.

## Relationships

- Maintained by [[NL-ICTU]].
- Commissioned/owned by [[NL-BZK]].
- Referenced by the Dutch digital-government architecture work governed
  through [[NL-OBDO]] and [[NL-MIDO]].

## Sources

Listed in frontmatter.
