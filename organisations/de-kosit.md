---
id: DE-KOSIT
type: organisation
name: Koordinierungsstelle für IT-Standards
name_en: "Coordination Office for IT Standards"
alternative_names:
  - KoSIT
  - "Institut für IT-Standardisierung"
  - Coordination Office for IT Standards
description: >
  German coordination office for IT standards, formally created by
  IT-Planungsrat decision 2010/19 of 24 September 2010, and responsible for
  coordinating the development and operation of IT standards for data
  exchange in public administration. Originally the OSCI-Leitstelle,
  renamed KoSIT on 1 April 2011 as its remit expanded to the XÖV framework.
  It is located organisationally in a unit of Department 4 of Bremen's
  Senator for Finance, works for the FITKO under a framework agreement made
  on behalf of the IT-Planungsrat, and publishes and maintains the XRechnung
  standard. FITKO's own page calls it the "Institut für IT-Standardisierung –
  Koordinierungsstelle für IT-Standards für den Bund und die Länder".

level: national
country: DE
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2010-09-24
end_date: null
last_verified: "2026-11-22"
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
    evidence: "Read directly 2026-11-22. FITKO's own page on federal IT standards (fitko.de): 'Das Institut für IT-Standardisierung – Koordinierungsstelle für IT-Standards für den Bund und die Länder (KoSIT) betreibt die IT-Standards des IT-Planungsrats', and 'Die Rahmenvereinbarung zwischen FITKO und KoSIT regelt die grundsätzliche Beziehung zwischen beiden Institutionen im Auftrag des IT-Planungsrats.' The IT-Planungsrat's own standards page (it-planungsrat.de) names the KoSIT as the operator ('Betreiber') of the XÖV framework, which 'wird von der Koordinierungsstelle für IT-Standards (KoSIT) betrieben und weiterentwickelt'. xoev.de, read directly 2026-08-28, says its creation 'followed constitutional amendments and an IT state treaty'. The founding details (IT-Planungsrat decision 2010/19 of 24 September 2010, as the OSCI-Leitstelle, renamed KoSIT on 1 April 2011) still rest on an encyclopedia (roadmap #767). Recorded 2026-10-11 as the substantive edge in place of the earlier low-confidence part-of FITKO (roadmap #535)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: DE-FITKO
    source: fact
    evidence: "FITKO's own page on federal IT standards (fitko.de), read directly 2026-11-22: the KoSIT 'berät bei Standardisierungsvorhaben im Auftrag der FITKO'; 'Das Institut ist verwaltungsorganisatorisch beim Referat der Abteilung 4 der Senatorin für Finanzen der Freien Hansestadt Bremen angesiedelt'; 'Die Rahmenvereinbarung zwischen FITKO und KoSIT regelt die grundsätzliche Beziehung zwischen beiden Institutionen im Auftrag des IT-Planungsrats. Die konkreten Aufgaben der KoSIT werden in Einzelvereinbarungen zwischen der FITKO und der KoSIT geregelt'; and FITKO commissions partners 'wie z.B. die Koordinierungsstelle für IT-Standards (KoSIT)' to maintain recognised standards. So the KoSIT is a Bremen-hosted institution that works for the FITKO under a framework agreement, not a unit of it: this plain association (metadata/relationship-types.md §2.6, decided 2026-10-11 under roadmap #535) plus the governance edge above, with the hosting told in the entity text."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Föderale IT-Standards — FITKO"
    url: "https://www.fitko.de/foederale-it-architektur/standards"
    publisher: "FITKO (Föderale IT-Kooperation)"
    accessed: "2026-11-22"
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

FITKO's own page on federal IT standards, read directly 2026-11-22, now
states the arrangement in one place: the KoSIT is "verwaltungsorganisatorisch
beim Referat der Abteilung 4 der Senatorin für Finanzen der Freien
Hansestadt Bremen angesiedelt", it advises "im Auftrag der FITKO", and a
framework agreement between FITKO and KoSIT, made "im Auftrag des
IT-Planungsrats", governs the relationship, with individual agreements for
specific tasks. That replaces the earlier pair of statements (Bremen
hosting from xoev.de and an encyclopedia; "under the roof of" the FITKO
from geodaten.niedersachsen.de), and confirms that the KoSIT is not a unit
of the [[DE-FITKO]].

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
