---
id: NL-NEN
type: organisation
name: Stichting Koninklijk Nederlands Normalisatie Instituut
alternative_names:
  - NEN
  - Royal Netherlands Standardization Institute
description: >
  The Dutch national standardisation institute. A non-profit foundation
  holding the Royal predicate, NEN develops and manages national standards
  and administers the internationally (ISO, IEC) and European (EN) accepted
  standards recognised in the Netherlands.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-FORUM-STANDAARDISATIE
  - EU-CEN
relationships:
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "CEN brings together the national standardisation bodies of 33 European countries; NEN is the standardisation institute of the Netherlands. Membership follows from the sourced composition rule rather than from a source naming NEN. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Over NEN"
    url: "https://www.nen.nl/over-nen"
    publisher: "NEN"
  - title: "NEN (Stichting Koninklijk Nederlands Normalisatie Instituut)"
    url: "https://www.noraonline.nl/wiki/NEN_(Stichting_Koninklijk_Nederlands_Normalisatie_Instituut)"
    publisher: "NORA Online (ICTU)"
  - title: "NEN"
    url: "https://nl.wikipedia.org/wiki/NEN"
    publisher: "Wikipedia"
---

# NEN

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

NEN is the standardisation institute of the Netherlands: a foundation
without profit motive, holding the Royal predicate, which brings
stakeholders together to reach agreements recorded in standards and
guidelines.

It manages a reported 34,000+ standards, comprising the international (ISO,
IEC), European (EN) and national (NEN) standards recognised in the
Netherlands, and works closely with ISO and CEN so that Dutch standards
align with international ones. NEN was a co-founder of ISO in 1947.

"NEN" abbreviates *NEderlandse Norm*, and since 8 May 2000 has also been the
name of the close cooperation between the Stichting Koninklijk Nederlands
Normalisatie Instituut and the Stichting Koninklijk Nederlands
Elektrotechnisch Comité (NEC), the latter specialising in electrical
engineering, information technology and telecommunications standardisation.
The `name` field records the foundation; the NEC and the combined
arrangement are not separately modelled, which may need revisiting.

## Relationships

- Complementary to [[NL-FORUM-STANDAARDISATIE]]: NEN operates the formal
  national standards infrastructure, while Forum Standaardisatie governs
  which open standards public bodies must apply. No relationship is
  asserted between them, as none was sourced.
- Participates in [[EU-CEN]], added in Batch 9. As with [[NL-AP]] and the
  EDPB, the evidence is a composition rule rather than a source naming NEN.
- ISO and IEC remain unmodelled (Batch 13), so those relationships are still
  unassertable. [[EU-CENELEC]] is the European counterpart of the Dutch NEC,
  with which NEN has cooperated since 2000 — see the open modelling question
  about whether NEC warrants its own entity.

## Sources

Listed in frontmatter.
