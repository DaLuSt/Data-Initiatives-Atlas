---
id: DE-REGMOG
type: law
name: Registermodernisierungsgesetz
alternative_names:
  - RegMoG
  - Gesetz zur Einführung und Verwendung einer Identifikationsnummer in der öffentlichen Verwaltung
  - Register Modernisation Act
description: >
  German federal act dated 28 March 2021 (published 6 April 2021 as
  BGBl. I S. 591) introducing the use of an identification number in
  public administration. It makes the tax identification number under
  § 139b Abgabenordnung a change-resistant ordering feature for assigning
  administrative data to the correct person across roughly 51 registers,
  on a phased implementation timeline running into at least 2025-2026,
  and is the legal basis on which Germany implements the once-only
  principle.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2021-03-28
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-SDG
relationships: []

sources:
  - title: "Registermodernisierungsgesetz — Mit dem 'once-only'-Prinzip zur digitalen und bürgerfreundlichen Verwaltung"
    url: "https://www.walhalla.de/news/registermodernisierungsgesetz-once-only-prinzip-zur-digitalen-und-buergernahen-verwaltung"
    publisher: "Walhalla Fachverlag"
    accessed: "2026-08-28"
  - title: "Die Steuer-ID als behördenübergreifend verwendbare Personenkennziffer"
    url: "https://www.rehm-verlag.de/neues-datenschutzrecht-fuer-bayern/aktuelle-beitraege-datenschutz/die-steuer-id-als-behoerdenuebergreifend-verwendbare-personenkennziffer/"
    publisher: "rehm Verlag"
    accessed: "2026-08-28"
  - title: "Registermodernisierung: Automatisierung auf Kosten der Sicherheit"
    url: "https://netzpolitik.org/2023/registermodernisierung-automatisierung-auf-kosten-der-sicherheit/"
    publisher: "netzpolitik.org"
    accessed: "2026-08-28"
  - title: "RegMoG Registermodernisierungsgesetz"
    url: "https://www.buzer.de/RegMoG.htm"
    publisher: "buzer.de"
    accessed: "2026-08-28"
  - title: "Registermodernisierungsgesetz verkündet"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2021/04/registermodernisierungsgesetz-verkuendet.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "FAQs zum Registermodernisierungsgesetz"
    url: "https://www.bmi.bund.de/SharedDocs/faqs/DE/themen/moderne-verwaltung/registermodernisierung/registermodernisierung-faq-liste.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
---

# Registermodernisierungsgesetz (RegMoG)

> **Re-verified 2026-08-28.** Both `bmi.bund.de` pages return HTTP 400 Bad
> Request on every attempt this pass — consistent with the same domain
> being unreachable across other entities in this batch ([[DE-OZG]]). The
> three non-government sources (Walhalla, rehm-Verlag, netzpolitik.org)
> all loaded directly, and `buzer.de`, a legal-database mirror, was added
> and read directly to confirm the statute's own date and Bundesgesetzblatt
> citation. Three (now four) of six is a genuine majority.
> `verification: primary-source`.

## Description

The RegMoG is dated **28 March 2021** and was published on **6 April 2021**
as **BGBl. I S. 591** — the exact citation confirmed directly this pass via
buzer.de, closing the "no statutory text" gap flagged in the entity's
earlier text (the official `gesetze-im-internet.de` copy itself returned
HTTP 503 on this pass's one attempt and was not pursued further given the
majority already reached).

It introduces the use of an identification number in public administration,
so that administrative data can be assigned to the correct person securely
and in conformity with data protection law using a **change-resistant
ordering feature** — the tax identification number, formally the
Identifikationsnummer under **§ 139b Abgabenordnung**.

The sources describe the consequence bluntly: the Steuer-ID takes on the
function of a **general personal identifier** (allgemeine Personenkennziffer),
confirmed directly this pass to be stored as an "additional ordering
characteristic" (zusätzliches Ordnungsmerkmal) in **51 registers**
(rehm-Verlag's own figure, read directly, updating the entity's earlier
"roughly 50" from a source not specific about the count) — including the
residents' register, the driving licence and weapons registers, and with
pension and health insurance funds. walhalla.de, read directly, adds
context this entity did not previously carry: the reform addresses
fragmentation across roughly **220** central and decentralised registers.

**Timeline, now sourced with appropriate uncertainty rather than a single
figure**: rehm-Verlag's page (read directly) describes a "five-year
implementation window from the law's 2021 enactment," implying an
end-2026 horizon for full register integration; buzer.de (read directly)
instead describes a genuinely **phased** rollout with different provisions
taking effect at different times (immediately on 7 April 2021, then August
2023, November 2023, 2024 and 2025, with later announcements referencing
May 2026), gated in most cases on the Federal Interior Ministry declaring
the technical prerequisites met under Article 22 of the act, rather than
running to one fixed deadline. Both are recorded rather than picking
one arbitrarily, since they describe a genuinely staggered process rather
than contradicting each other outright.

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
  RegMoG is Germany's once-only vehicle. But **no source read this pass
  connects them either**, and the RegMoG is domestic register law rather
  than a transposition instrument. `related_entities` records the
  association for navigation without asserting a relationship.
- **A link to the Steuer-ID or the Abgabenordnung.** Neither is an Atlas
  entity, and creating a tax statute to hang this on would be building the
  graph around a single reference.

## Contested, and recorded as such

One cited source is a **critical piece from netzpolitik.org**, read
directly this pass, on the security implications of automating register
access. It is included deliberately, and this pass's direct reading
sharpens what it says rather than merely confirming it existed: it reports
the government **rejected a "Domain-ID Model"** — separate identifiers per
sector, which would have prevented centralised profiling — as "too
expensive" and "very difficult to implement." It also reports a specific
Bundesrat concern, read directly: the technical system for protecting
people who have filed an Auskunftssperre (information block, e.g. abuse
victims) "cannot effectively prevent" staff misuse given the large number
of employees with register access.

A general personal identifier is constitutionally contentious in Germany
for well-known historical reasons, and an Atlas entry that cited only the
responsible ministry's own material would present a contested measure as
settled — especially now that the ministry's own pages cannot even be
fetched this pass.

The Atlas records no position on the merits. It records that the measure is
contested, and specifically how, because that is a fact about the
initiative.

## Relationships

**None asserted.** Reached from [[DE-BMI]], which `produces` it.

## Sources

Listed in frontmatter — three of the original five plus one added mirror
were read directly this pass; `bmi.bund.de`'s two pages return HTTP 400 on
every attempt and are kept listed with that status noted here rather than
silently dropped.
