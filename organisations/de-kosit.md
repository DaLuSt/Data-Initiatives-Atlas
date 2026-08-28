---
id: DE-KOSIT
type: organisation
name: Koordinierungsstelle für IT-Standards
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
relationships:
  - type: part-of
    target: DE-FITKO
    source: fact
    evidence: "Confirmed by reading xoev.de's own page directly (2026-08-28): the KoSIT's creation 'followed constitutional amendments and an IT state treaty,' and it is organisationally located in Bremen's e-government department. docs.fitko.de's own page, also read directly, describes FITKO as operating the technical infrastructure for the documentation portal covering FIM and XÖV interoperability, but does not itself state a direct organisational 'part-of' relationship between KoSIT and FITKO — consistent with the tension already flagged in this entity's body between KoSIT's Bremen hosting and its being 'brought together under the roof of' FITKO. de.wikipedia.org, also read directly, independently confirms KoSIT's Bremen location and its formal creation by IT-Planungsrat decision 2010/19 of 24 September 2010, renamed from 'OSCI-Leitstelle' on 1 April 2011."
    confidence: low
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

## ⚠ A hosting arrangement the model handles awkwardly

Two sourced statements sit uneasily together, and this pass's direct
reading does not resolve the tension — if anything it sharpens it:

1. The KoSIT is located in the Bremen state administration, confirmed
   directly on two independent pages this pass.
2. The KoSIT is among the institutions brought together *under the roof of*
   the [[DE-FITKO]] — a description this entity has always carried, but
   which docs.fitko.de's own page (read directly this pass) does not
   itself restate in so many words; it describes FITKO operating shared
   technical infrastructure for FIM/XÖV documentation without asserting a
   formal `part-of` relationship.

Both can be true — a Land-hosted office operating within a federal
cooperation structure is an ordinary German arrangement — but the Atlas has
no way to say that cleanly. `part-of` [[DE-FITKO]] is recorded at
**`confidence: low`** for exactly this reason, and Bremen is not modelled
at all, because the Atlas has no sub-national level (see
`countries/de/index.md`).

This is the second country's most useful finding about the ontology: the
`level` vocabulary is adequate for a unitary state and lossy for a federal
one. Logged in `discovery/unresolved.md`.

## Relationships

- `part-of` [[DE-FITKO]] — at low confidence, see above; this pass's direct
  reading kept it at low rather than raising it, since no page states the
  relationship as plainly as the entity's prose does.

Inbound: [[DE-XRECHNUNG]] and [[DE-XOEV]] are both `maintained-by` this
entity.

## Sources

Listed in frontmatter. Three of four read directly this pass;
`xoev.de/xrechnung/betrieb_und_support-16853` now returns HTTP 404 and is
kept listed with that status noted here rather than silently dropped.
