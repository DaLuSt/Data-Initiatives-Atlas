---
id: DE-REGMOG
type: law
name: Registermodernisierungsgesetz
alternative_names:
  - RegMoG
  - Gesetz zur Einführung und Verwendung einer Identifikationsnummer in der öffentlichen Verwaltung
  - Register Modernisation Act
description: >
  German federal act of 28 March 2021 introducing the use of an
  identification number in public administration. It makes the tax
  identification number under § 139b Abgabenordnung a change-resistant
  ordering feature for assigning administrative data to the correct person
  across registers, and is the legal basis on which Germany implements the
  once-only principle.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2021-03-28
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-SDG
relationships: []

sources:
  - title: "Registermodernisierungsgesetz verkündet"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2021/04/registermodernisierungsgesetz-verkuendet.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "FAQs zum Registermodernisierungsgesetz"
    url: "https://www.bmi.bund.de/SharedDocs/faqs/DE/themen/moderne-verwaltung/registermodernisierung/registermodernisierung-faq-liste.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Registermodernisierungsgesetz — Mit dem 'once-only'-Prinzip zur digitalen und bürgerfreundlichen Verwaltung"
    url: "https://www.walhalla.de/news/registermodernisierungsgesetz-once-only-prinzip-zur-digitalen-und-buergernahen-verwaltung"
    publisher: "Walhalla Fachverlag"
  - title: "Die Steuer-ID als behördenübergreifend verwendbare Personenkennziffer"
    url: "https://www.rehm-verlag.de/neues-datenschutzrecht-fuer-bayern/aktuelle-beitraege-datenschutz/die-steuer-id-als-behoerdenuebergreifend-verwendbare-personenkennziffer/"
    publisher: "rehm Verlag"
  - title: "Registermodernisierung: Automatisierung auf Kosten der Sicherheit"
    url: "https://netzpolitik.org/2023/registermodernisierung-automatisierung-auf-kosten-der-sicherheit/"
    publisher: "netzpolitik.org"
---

# Registermodernisierungsgesetz (RegMoG)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The RegMoG dates from **28 March 2021**. It introduces the use of an
identification number in public administration, so that administrative data
can be assigned to the correct person securely and in conformity with data
protection law using a **change-resistant ordering feature** — the tax
identification number, formally the Identifikationsnummer under **§ 139b
Abgabenordnung**.

The sources describe the consequence bluntly: over the following years the
Steuer-ID takes on the function of a **general personal identifier**
(allgemeine Personenkennziffer), to be stored in roughly **50 further
places** including the residents' register, the driving licence and weapons
registers, and with pension and health insurance funds.

Its purpose is the **once-only principle**: data and documentation already
held in registers should not have to be submitted repeatedly. Citizens,
businesses and organisations supply their data once, and authorities
retrieve it for each subsequent administrative process.

## The German counterpart to the Dutch base registers

This is the German analogue of [[NL-BASISREGISTRATIES]] and of the
identity infrastructure the Dutch stelsel rests on — the same problem
(authoritative person data reused across government) solved by a
different mechanism (one existing tax number pressed into service as a
cross-domain key, rather than a system of designated authentic
registrations).

**No relationship to the Dutch entities is asserted**, and the difference
is instructive enough to be worth stating: functionally equivalent
national programmes need not be structurally comparable, and the Atlas
should not imply they are.

## Two relationships considered and refused

- **`implements-requirement-from` → [[EU-SDG]].** The once-only principle
  is the organising idea of the Single Digital Gateway Regulation, and the
  RegMoG is Germany's once-only vehicle. But **no source read connects
  them**, and the RegMoG is domestic register law rather than a
  transposition instrument. `related_entities` records the association for
  navigation without asserting a relationship.
- **A link to the Steuer-ID or the Abgabenordnung.** Neither is an Atlas
  entity, and creating a tax statute to hang this on would be building the
  graph around a single reference.

## Contested, and recorded as such

One cited source is a **critical piece from netzpolitik.org** on the
security implications of automating register access. It is included
deliberately. A general personal identifier is constitutionally contentious
in Germany for well-known historical reasons, and an Atlas entry that cited
only the responsible ministry's own FAQ would present a contested measure
as settled.

The Atlas records no position on the merits. It records that the measure is
contested, because that is a fact about the initiative.

## Relationships

**None asserted.** Reached from [[DE-BMI]], which `produces` it.

## Sources

Listed in frontmatter — two BMI pages, two legal publishers and one
critical outlet. **No statutory text**; no Gesetze-im-Internet URL was
returned by search.
