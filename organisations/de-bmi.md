---
id: DE-BMI
type: organisation
name: Bundesministerium des Innern
alternative_names:
  - BMI
  - Federal Ministry of the Interior
  - Bundesministerium des Innern und für Heimat
description: >
  German federal interior ministry. Within the scope of the Atlas it is the
  department responsible for administrative modernisation, register
  modernisation and open-government legislation, and the ministry in whose
  portfolio the Bundesamt für Sicherheit in der Informationstechnik and the
  Statistisches Bundesamt sit.

level: national
country: DE
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
  - DE-BMDS
relationships:
  - type: produces
    target: DE-DATENSTRATEGIE
    source: fact
    evidence: "The Nationale Datenstrategie was jointly developed and presented by the BMDV, the BMWK and the BMI (bmi.bund.de press release 'Bundeskabinett beschließt Nationale Datenstrategie'; bmdv.bund.de). NOT READ — search-only. Two of the three co-authoring ministries are not Atlas entities."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: produces
    target: DE-REGMOG
    source: fact
    evidence: "The BMI announced the promulgation of the Registermodernisierungsgesetz and maintains the ministry's FAQ on Registermodernisierung (bmi.bund.de 'Registermodernisierungsgesetz verkündet'; bmi.bund.de FAQ). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: produces
    target: DE-DNG
    source: fact
    evidence: "The BMI ran the legislative procedure for the act amending the E-Government-Gesetz and introducing the act on the use of public sector data (bmi.bund.de Gesetzgebungsverfahren 'zweites-open-data-gesetz'). NOT READ — search-only. The BMWK also presents the package."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Bundeskabinett beschließt Nationale Datenstrategie"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2023/08/nationale-datenstrategie.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Registermodernisierungsgesetz verkündet"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2021/04/registermodernisierungsgesetz-verkuendet.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Gesetz zur Änderung des E-Government-Gesetzes und zur Einführung des Gesetzes für die Nutzung von Daten des öffentlichen Sektors"
    url: "https://www.bmi.bund.de/SharedDocs/gesetzgebungsverfahren/DE/DVI1/zweites-open-data-gesetz.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Upgrade für ein Digitales Deutschland ist da: Das OZG-Änderungsgesetz tritt in Kraft"
    url: "https://www.bmi.bund.de/SharedDocs/kurzmeldungen/DE/2024/07/ozg.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Bund hat seine 115 wichtigsten Verwaltungsleistungen bis Ende 2024 erfolgreich digitalisiert"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2024/12/ozg.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
---

# Bundesministerium des Innern (BMI)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BMI is Germany's federal interior ministry. The Atlas records it for
its role in public-administration digitalisation rather than for its full
portfolio, which is much wider and out of scope here — hence
`coverage: low`.

Within that scope the sources establish that the BMI:

- co-authored the [[DE-DATENSTRATEGIE]] with the BMDV and the BMWK;
- announced the promulgation of the [[DE-REGMOG]] and maintains the
  ministry's Registermodernisierung FAQ;
- ran the legislative procedure for the "second open data act" package that
  amended the [[DE-EGOVG]] and introduced the [[DE-DNG]];
- announced the entry into force of the OZG-Änderungsgesetz and the
  completion of the federal government's 115 priority [[DE-OZG]] services.

[[DE-BSI]] is a Bundesoberbehörde in the BMI's portfolio, and
[[DE-DESTATIS]] sits in its Geschäftsbereich. Those `part-of` links are
recorded on the agencies themselves.

## ⚠ The name and the reorganisation

The ministry has been styled both *Bundesministerium des Innern* and
*Bundesministerium des Innern und für Heimat*; the cited press releases use
the latter, which reflected the 2018–2025 designation. **No source read
states the ministry's current formal name**, and since [[DE-BMDS]] took
over digital competences from six departments including this one in May
2025, the BMI's role in several of the relationships above is historical
rather than current.

The relationships are recorded as facts about who did what at the time,
with `valid_from` left null because no source dates the transfer. They
should not be read as a claim about which ministry owns these files today.
Logged in `discovery/unresolved.md`.

## Relationships

- Produces [[DE-DATENSTRATEGIE]], [[DE-REGMOG]] and [[DE-DNG]].

Each `produces` evidence field names the co-authoring ministries that are
**not** Atlas entities, so the record does not imply sole authorship.

## Sources

Listed in frontmatter — all five are BMI pages, which is circular for an
entity about the BMI. It is the same weakness flagged on
[[EU-PUBLICATIONS-OFFICE]]. The facts they support are administrative
announcements about the ministry's own legislative work, which is the case
where self-sourcing is least troubling, but it is a weakness nonetheless.
