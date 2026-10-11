---
id: DE-KOSIT
type: organisation
name: Koordinierungsstelle für IT-Standards
name_en: "Coordination Office for IT Standards"
alternative_names:
  - KoSIT
  - Coordination Office for IT Standards
description: >
  German coordination office for IT standards, formally created by
  IT-Planungsrat decision 2010/19 of 24 September 2010, and responsible for
  coordinating the development and operation of IT standards for data
  exchange in public administration. Originally the OSCI-Leitstelle,
  renamed KoSIT on 1 April 2011 as its remit expanded to the XÖV framework.
  It is located organisationally in the e-government unit of the core
  administration of the Free Hanseatic City of Bremen, is brought together
  under the roof of the FITKO, and publishes and maintains the XRechnung
  standard.

level: national
country: DE
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2010-09-24
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-FITKO
  - DE-IT-PLANUNGSRAT
relationships:
  - type: governed-by
    target: DE-IT-PLANUNGSRAT
    source: fact
    evidence: "de.wikipedia.org's dedicated KoSIT article, read directly (2026-08-28): the KoSIT was formally created by IT-Planungsrat decision 2010/19 of 24 September 2010 (as the OSCI-Leitstelle, renamed KoSIT on 1 April 2011), and the IT-Planungsrat assigned it its four responsibilities (XÖV development and operation, coordination and public relations, secure data transport, the standardisation agenda). xoev.de's own page, also read directly, says its creation 'followed constitutional amendments and an IT state treaty'. Recorded 2026-10-11 as the substantive edge in place of the earlier low-confidence part-of FITKO (roadmap #535, unresolved row #17 closed)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: DE-FITKO
    source: fact
    evidence: "Two sourced statements that a single part-of cannot hold together: the KoSIT is located in the e-government unit of Bremen's core administration (xoev.de and Wikipedia, both read directly 2026-08-28), and it is one of the bodies brought together under the FITKO's roof (geodaten.niedersachsen.de, as recorded on DE-IT-PLANUNGSRAT; docs.fitko.de describes FITKO running the FIM/XÖV documentation infrastructure but does not itself state an organisational part-of). Decision 2026-10-11 (roadmap #535, metadata/relationship-types.md §2.6): a Land-hosted office working inside a federal cooperation is recorded by this plain association plus the governance edge above, and the hosting is told in the entity text; part-of is not asserted because neither source says the KoSIT is a unit of the FITKO."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Startseite — Koordinierungsstelle für IT-Standards"
    url: "https://www.xoev.de/startseite-1459"
    publisher: "Koordinierungsstelle für IT-Standards (KoSIT)"
    accessed: "2026-08-28"
  - title: "Koordinierungsstelle für IT-Standards — Betrieb und Support (XRechnung)"
    url: "https://www.xoev.de/xrechnung/betrieb_und_support-16853"
    publisher: "Koordinierungsstelle für IT-Standards (KoSIT)"
  - title: "Koordinierungsstelle für IT-Standards (KoSIT)"
    url: "https://docs.fitko.de/fim-xoev/docs/terms/kosit/"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-08-28"
  - title: "Koordinierungsstelle für IT-Standards"
    url: "https://de.wikipedia.org/wiki/Koordinierungsstelle_f%C3%BCr_IT-Standards"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# Koordinierungsstelle für IT-Standards (KoSIT)

> **Re-verified 2026-08-28.** Three of four cited pages read directly; the
> XRechnung-specific `xoev.de` page (`betrieb_und_support-16853`) now
> 404s and is kept listed with that status rather than dropped.
> `verification: primary-source`; `confidence` raised to `high`; the
> previously-unrecorded formal creation date is now sourced.

## Description

The KoSIT's task is to **coordinate the development and operation of IT
standards for data exchange in public administration** in Germany.
Confirmed directly this pass on its dedicated Wikipedia article: it was
**formally created by IT-Planungsrat decision 2010/19 of 24 September
2010**, originally as the **OSCI-Leitstelle** managing the Online Services
Computer Interface, and **renamed KoSIT on 1 April 2011** as its mandate
expanded to the XÖV framework — a founding date not previously recorded on
this entity. Wikipedia further confirms the IT-Planungsrat assigned KoSIT
four responsibilities in 2010: XÖV development and operations,
coordination and public relations, secure data transport for e-government
services, and the standardisation agenda; KoSIT now also sits on the
federal standardisation board under the IT-Planungsrat.

Organisationally it sits in the unit responsible for e-government in the
core administration of the **Freie Hansestadt Bremen** — confirmed
independently this pass by both xoev.de's own page and its Wikipedia
article. It develops, publishes and maintains [[DE-XRECHNUNG]], and offers
support services for it as part of its operations (the specific
"Betrieb und Support" page cited for this fact previously now 404s).
[[DE-XOEV]] — the XML in der öffentlichen Verwaltung standards family — is
the framework within which XRechnung was developed.

Its role is the closest German analogue to [[NL-LOGIUS]]'s standards
custody and to [[NL-FORUM-STANDAARDISATIE]]'s coordination function. **No
relationship to either is asserted.**

## A Land-hosted office inside a federal cooperation

Two sourced statements sit side by side, and both are kept:

1. The KoSIT is located in the Bremen state administration, confirmed
   directly on two independent pages.
2. The KoSIT is among the institutions brought together *under the roof of*
   the [[DE-FITKO]], a description docs.fitko.de's own page (read directly)
   does not restate in so many words; it describes FITKO operating shared
   technical infrastructure for FIM/XÖV documentation without asserting a
   formal containment.

A Land-hosted office operating within a federal cooperation structure is an
ordinary German arrangement. **Decision, 2026-10-11 (roadmap #535, row #17
closed):** the model needs no second edge type. The office is `governed-by`
the [[DE-IT-PLANUNGSRAT]] that created it (high confidence, sourced) and
`related-to` the [[DE-FITKO]] (medium confidence), and the Bremen hosting is
told here, because the Atlas has no sub-national level (see
`countries/de/index.md`). The earlier `part-of` [[DE-FITKO]] at low
confidence asserted containment that no source states, and
`cooperates-with` would assert a formal agreement between the two that no
source describes either. See `metadata/relationship-types.md` §2.6.

## Relationships

- `governed-by` [[DE-IT-PLANUNGSRAT]] — created by its decision 2010/19.
- `related-to` [[DE-FITKO]] — under its roof, hosted in Bremen; see above.

Inbound: [[DE-XRECHNUNG]] and [[DE-XOEV]] are both `maintained-by` this
entity.

## Sources

Listed in frontmatter. Three of four read directly this pass;
`xoev.de/xrechnung/betrieb_und_support-16853` now returns HTTP 404 and is
kept listed with that status noted here rather than silently dropped.
