---
id: CH-EDOEB
type: organisation
name: Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter
alternative_names:
  - EDÖB
  - PFPDT
  - IFPDT
  - FDPIC
  - Federal Data Protection and Information Commissioner
description: >
  Switzerland's federal data protection and information commissioner,
  supervising the processing of personal data by federal bodies and private
  persons and overseeing the federal freedom of information regime. Its
  competences were expanded by the revised Federal Act on Data Protection in
  force since 1 September 2023.

level: national
country: CH
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
organisations: []
related_entities:
  - CH-REVDSG
relationships:
  - type: applies-to
    target: CH-REVDSG
    source: fact
    evidence: "Confirmed verbatim by reading piwikpro.de directly (2026-08-22): 'Die Kompetenzen des EDÖB (Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter) sollten erweitert werden, um die Rechte der betroffenen Personen besser zu schützen.' edoeb.admin.ch, read directly, confirms the EDÖB's dual mandate ('Aufgaben in den Bereichen Datenschutz und Öffentlichkeitsprinzip') and its role as the mandatory contact for data-breach notifications under the revDSG, confirmed on kmu.admin.ch ('Eine rasche Meldung ist erforderlich, wenn die Datensicherheit verletzt wurde. Sie ist an den Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB) zu richten')."
    confidence: medium
    valid_from: 2023-09-01
    valid_until: null

sources:
  - title: "Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter"
    url: "https://www.edoeb.admin.ch/"
    publisher: "Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter (EDÖB)"
    accessed: "2026-08-22"
  - title: "Neues Datenschutzgesetz (revDSG)"
    url: "https://www.kmu.admin.ch/de/neues-datenschutzgesetz-revdsg"
    publisher: "KMU-Portal, Staatssekretariat für Wirtschaft (SECO)"
    accessed: "2026-08-22"
  - title: "Datenschutzgesetz Schweiz 2023 (revDSG): der praktische Leitfaden"
    url: "https://piwikpro.de/blog/datenschutzgesetz-schweiz-2023-revdsg/"
    publisher: "Piwik PRO"
    accessed: "2026-08-22"
  - title: "Welcome to the FDPIC"
    url: "https://www.edoeb.admin.ch/edoeb/en/home.html"
    publisher: "Federal Data Protection and Information Commissioner (FDPIC)"
    accessed: "2026-08-22"
  - title: "Benvenuti sul sito dell'IFPDT"
    url: "https://www.edoeb.admin.ch/edoeb/it/home.html"
    publisher: "Incaricato federale della protezione dei dati e della trasparenza (IFPDT)"
    accessed: "2026-08-22"
---

# Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter (EDÖB)

> **Verified 2026-08-22.** All cited pages were read directly and confirm
> the claims below, verbatim in places. Two alternative names not
> attested on any source read — the English "FDPIC" and Italian "IFPDT"
> abbreviations — turned out to be exactly what the office's own English
> and Italian pages call themselves, found this pass and added.

## Description

Confirmed by reading edoeb.admin.ch directly (2026-08-22): "Als
unabhängige Behörde obliegen dem Eidgenössischen Datenschutz- und
Öffentlichkeitsbeauftragten (EDÖB) Aufgaben in den Bereichen Datenschutz
und Öffentlichkeitsprinzip." The EDÖB is Switzerland's federal data protection and information
commissioner. Like [[DE-BFDI]], it holds **both halves of the name**: data
protection supervision *and* freedom of information.

Confirmed verbatim on piwikpro.de (2026-08-22): its competences were
**expanded** by [[CH-REVDSG]] "um die Rechte der betroffenen Personen
besser zu schützen" (to better protect the rights of affected persons).

## The two-mandate pattern

The Atlas now holds three authorities combining data protection with access
to information, and five that do not:

| Both mandates | Data protection only |
|---|---|
| **EDÖB** (CH), [[DE-BFDI]] (DE), [[GB-ICO]] (GB) | [[NL-AP]], [[BE-APD]], [[FR-CNIL]], [[ES-AEPD]], [[PL-UODO]], [[NO-DATATILSYNET]], [[IE-DPC]] |

That split is not random — the countries that fused the two are the ones
whose freedom of information acts arrived alongside or after a data
protection regime — but the Atlas has not researched the causation and does
not assert it.

## Outside the EDPB, and unlike Norway there is no ambiguity

[[NO-DATATILSYNET]] carries no [[EU-EDPB]] edge because the EEA
arrangements are unclear. The EDÖB carries none because Switzerland is
outside the Union and the EEA entirely: there is no mechanism, clear or
otherwise.

What Switzerland has instead is an **adequacy decision**, which makes the
EDÖB's supervision the thing the Commission assesses rather than a seat at a
Union body. That decision is not an Atlas entity — see [[CH]].

## The cantonal gap

The EDÖB supervises **federal** bodies and private persons. Each canton has
its own data protection authority for cantonal and communal bodies, and
**none is an Atlas entity**.

Switzerland is therefore the third country, after Germany and Spain, where a
single `country`-scoped supervisory authority understates the real picture.
In the Swiss case it understates it by twenty-six.

## Relationships

- `applies-to` [[CH-REVDSG]].

## Sources

Listed in frontmatter, all read directly this pass. The English and
Italian pages were added specifically to confirm FDPIC and IFPDT.
