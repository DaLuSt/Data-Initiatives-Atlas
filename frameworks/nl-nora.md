---
id: NL-NORA
type: framework
name: Nederlandse Overheid Referentie Architectuur
alternative_names:
  - NORA
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
last_verified: "2026-08-22"
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
  - EU-EIF
relationships:
  - type: maintained-by
    target: NL-ICTU
    source: fact
    evidence: "NORA management is entrusted to ICTU, with BZK as opdrachtgever; the NORA gebruikersraad meets at ICTU (ictu.nl, noraonline.nl). Confirmed again 2026-08-21 in Kamerstuk 26643-128 (Kabinetsbesluit inzake ICT, 2008): 'BZK is namens alle overheden de eigenaar van de NORA en het beheer en de doorontwikkeling ervan is belegd bij Stichting ICTU.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: owned-by
    target: NL-BZK
    source: fact
    evidence: "The Ministry of BZK is described as opdrachtgever for NORA (noraonline.nl, ictu.nl). Confirmed again 2026-08-21 in Kamerstuk 26643-128, which names BZK as owner on behalf of all governments."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: EU-EIF
    source: fact
    evidence: "Confirmed 2026-08-21 on noraonline.nl's 'Positionering NORA' page: 'In de NORA zijn de Europese ontwikkelingen in het kader van het European Interoperability Framework (EIF) verankerd' — European EIF developments are anchored in NORA. The primary source behind that statement, Kamerstuk 26643-128 (Kabinetsbesluit inzake ICT, 2008), is more precise about scope: 'In NORA zijn de Europese ontwikkelingen in het kader van het European Interoperability Framework verankerd voor wat betreft publieke diensten waarbij sprake is van grensoverschrijdende gegevensuitwisseling' — the anchoring is specifically for public services involving cross-border data exchange, not a blanket claim that NORA is the Dutch National Interoperability Framework in full. Answers the 'Open — high value' question in discovery/unresolved.md with that qualification attached."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Positionering NORA"
    url: "https://www.noraonline.nl/wiki/Positionering_NORA"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-22"
  - title: "NORA (Nederlandse Overheid Referentie Architectuur)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/nora/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-22"
  - title: "Overheidsarchitectuur NORA"
    url: "https://www.ictu.nl/diensten/dienstenoverzicht/overheidsarchitectuur-nora/"
    publisher: "ICTU"
    accessed: "2026-08-22"
  - title: "Kabinetsbesluit inzake ICT (Kamerstuk 26643, nr. 128)"
    url: "https://zoek.officielebekendmakingen.nl/kst-26643-128.html"
    publisher: "Rijksoverheid / Tweede Kamer"
    accessed: "2026-08-22"
---

# Nederlandse Overheid Referentie Architectuur (NORA)

> **Verified 2026-08-20, deepened 2026-08-21.** Every cited source was read
> and confirmed to support what this entity says. `verification:
> primary-source`.

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
Both roles are confirmed a second time in Kamerstuk 26643-128, the 2008
Kabinetsbesluit inzake ICT, which also positioned "NORA (versie 3)" as an
interoperability framework in the second half of 2008, on the recommendation
of the College Standaardisatie. The unattested English gloss "Dutch
Government Reference Architecture" — not found on any of the four sources —
has been dropped rather than carried forward unread.

## `based-on` [[EU-EIF]] — the open question answered, with a qualification

`discovery/unresolved.md` flagged "Is NORA formally the Netherlands'
National Interoperability Framework under the EIF?" as **Open — high
value**. The 2008 Kabinetsbesluit answers it, but more narrowly than the
question assumed: *"In NORA zijn de Europese ontwikkelingen in het kader van
het European Interoperability Framework verankerd voor wat betreft publieke
diensten waarbij sprake is van grensoverschrijdende gegevensuitwisseling"* —
EIF developments are anchored in NORA specifically for public services
involving **cross-border data exchange**, not as a blanket "NORA = the Dutch
NIF" designation. `based-on` → [[EU-EIF]] is recorded as a fact on that
narrower, sourced basis.

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
- `based-on` [[EU-EIF]], for the cross-border-interoperability portion of
  NORA's scope (see above).
- Referenced by the Dutch digital-government architecture work governed
  through [[NL-OBDO]] and [[NL-MIDO]].

## Sources

Listed in frontmatter.
