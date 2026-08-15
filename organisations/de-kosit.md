---
id: DE-KOSIT
type: organisation
name: Koordinierungsstelle für IT-Standards
alternative_names:
  - KoSIT
  - Coordination Office for IT Standards
description: >
  German coordination office for IT standards, responsible for coordinating
  the development and operation of IT standards for data exchange in public
  administration. It is located organisationally in the e-government unit
  of the core administration of the Free Hanseatic City of Bremen, is
  brought together under the roof of the FITKO, and publishes and maintains
  the XRechnung standard.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: medium
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
  - DE-FITKO
relationships:
  - type: part-of
    target: DE-FITKO
    source: fact
    evidence: "Institutions such as the KoSIT, the FIM and the GovData portal are brought together under the roof of the FITKO (de.wikipedia.org 'Föderale IT-Kooperation'; docs.fitko.de/fim-xoev/docs/terms/kosit). NOT READ — search-only. Note the tension with the KoSIT's organisational placement in the Bremen administration, discussed in the entity body."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Startseite — Koordinierungsstelle für IT-Standards"
    url: "https://www.xoev.de/startseite-1459"
    publisher: "Koordinierungsstelle für IT-Standards (KoSIT)"
  - title: "Koordinierungsstelle für IT-Standards — Betrieb und Support (XRechnung)"
    url: "https://www.xoev.de/xrechnung/betrieb_und_support-16853"
    publisher: "Koordinierungsstelle für IT-Standards (KoSIT)"
  - title: "Koordinierungsstelle für IT-Standards (KoSIT)"
    url: "https://docs.fitko.de/fim-xoev/docs/terms/kosit/"
    publisher: "Föderale IT-Kooperation (FITKO)"
  - title: "Koordinierungsstelle für IT-Standards"
    url: "https://de.wikipedia.org/wiki/Koordinierungsstelle_f%C3%BCr_IT-Standards"
    publisher: "Wikipedia"
---

# Koordinierungsstelle für IT-Standards (KoSIT)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The KoSIT's task is to **coordinate the development and operation of IT
standards for data exchange in public administration** in Germany.

Organisationally it sits in the unit responsible for e-government in the
core administration of the **Freie Hansestadt Bremen**. It develops,
publishes and maintains [[DE-XRECHNUNG]], which it has operated since
1 January 2019, and offers support services for it as part of its
operations. [[DE-XOEV]] — the XML in der öffentlichen Verwaltung standards
family — is the framework within which XRechnung was developed.

Its role is the closest German analogue to [[NL-LOGIUS]]'s standards
custody and to [[NL-FORUM-STANDAARDISATIE]]'s coordination function. **No
relationship to either is asserted.**

## ⚠ A hosting arrangement the model handles awkwardly

Two sourced statements sit uneasily together:

1. The KoSIT is located in the Bremen state administration.
2. The KoSIT is among the institutions brought together *under the roof of*
   the [[DE-FITKO]].

Both can be true — a Land-hosted office operating within a federal
cooperation structure is an ordinary German arrangement — but the Atlas has
no way to say that. `part-of` [[DE-FITKO]] is recorded at
**`confidence: low`** for exactly this reason, and Bremen is not modelled
at all, because the Atlas has no sub-national level (see
`countries/de/de.md`).

This is the second country's most useful finding about the ontology: the
`level` vocabulary is adequate for a unitary state and lossy for a federal
one. Logged in `discovery/unresolved.md`.

## Relationships

- `part-of` [[DE-FITKO]] — at low confidence, see above.

Inbound: [[DE-XRECHNUNG]] and [[DE-XOEV]] are both `maintained-by` this
entity.

## Sources

Listed in frontmatter.
