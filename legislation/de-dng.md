---
id: DE-DNG
type: law
name: Datennutzungsgesetz
alternative_names:
  - DNG
  - Gesetz für die Nutzung von Daten des öffentlichen Sektors
  - German Data Usage Act
description: >
  German federal act on the use of public sector data, enacted as part of
  the "Zweites Open-Data-Gesetz" package and in force from 23 July 2021. It
  implements Directive (EU) 2019/1024 on open data and the re-use of public
  sector information, replaces the Informationsweiterverwendungsgesetz,
  establishes an "open by default" principle for data within its scope,
  guarantees equal usage conditions for all actors, and extends the scope
  for the first time to public undertakings in water, transport and energy.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2021-07-23
end_date: null
last_verified: null
previous_version: DE-IWG
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-OPEN-DATA-DIRECTIVE
  - DE-IWG
  - NL-WHO
relationships:
  - type: implements-requirement-from
    target: EU-OPEN-DATA-DIRECTIVE
    source: fact
    evidence: "The Datennutzungsgesetz implements the requirements of Directive (EU) 2019/1024 — the Open Data and Public Sector Information Directive of 2019 (de.wikipedia.org 'Datennutzungsgesetz'; bho-legal.com; de.digital). NOT READ — search-only."
    confidence: medium
    valid_from: 2021-07-23
    valid_until: null
  - type: supersedes
    target: DE-IWG
    source: fact
    evidence: "With the new Datennutzungsgesetz the Informationsweiterverwendungsgesetz was modernised and replaced; the DNG replaced the IWG (de.wikipedia.org 'Datennutzungsgesetz'; prosoz.de; haufe.de). NOT READ — search-only."
    confidence: medium
    valid_from: 2021-07-23
    valid_until: null

sources:
  - title: "DNG — Gesetz für die Nutzung von Daten des öffentlichen Sektors"
    url: "https://www.gesetze-im-internet.de/dng/DNG.pdf"
    publisher: "Bundesministerium der Justiz / juris (Gesetze im Internet)"
  - title: "Datennutzungsgesetz"
    url: "https://de.wikipedia.org/wiki/Datennutzungsgesetz"
    publisher: "Wikipedia"
  - title: "Zweites Open-Data-Gesetz und Datennutzungsgesetz"
    url: "https://www.de.digital/Redaktion/DE/Artikel/Service/Gesetzesvorhaben/zweites-open-data-gesetz-und-datennutzungsgesetz.html"
    publisher: "DE.DIGITAL (Bundesministerium für Wirtschaft)"
  - title: "Bundesregierung legt Änderung am E-Government-Gesetz und neues Datennutzungsgesetz vor"
    url: "https://www.open-government-deutschland.de/opengov-de/bundesregierung-legt-aenderung-am-e-government-gesetz-und-neues-datennutzungsgesetz-vor-1852186"
    publisher: "Open Government Deutschland (Bundesregierung)"
  - title: "Das neue Datennutzungsgesetz"
    url: "https://www.bho-legal.com/en/das-neue-datennutzungsgesetz/"
    publisher: "BHO Legal"
---

# Datennutzungsgesetz (DNG)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The DNG is Germany's act on the use of public sector data. It was passed by
the federal cabinet on **10 February 2021** as part of the *Zweites
Open-Data-Gesetz und Datennutzungsgesetz* package — which also amended
[[DE-EGOVG]] — and came into force on **23 July 2021**.

It implements [[EU-OPEN-DATA-DIRECTIVE]] and replaces [[DE-IWG]].

Its substantive features, as the sources describe them:

- data within its scope is to be created and provided, as far as possible,
  according to the principle **"open by default"**;
- **equal usage conditions** are guaranteed for all actors;
- the scope is extended **for the first time to public undertakings** in
  water, transport and energy.

## The third national transposition pair in the Atlas

[[EU-OPEN-DATA-DIRECTIVE]] is one entity implemented by two national acts —
[[NL-WHO]] in the Netherlands and the DNG in Germany. As with
[[EU-GDPR]] and [[EU-NIS2]], no `DE-EU-*` duplicate was created and no
relationship is asserted between the two national acts.

## A cleaner temporal chain than the cybersecurity one

The DNG → [[DE-IWG]] supersession is recorded with full confidence in both
directions:

- this entity carries `previous_version: DE-IWG` and a `supersedes`
  relationship;
- [[DE-IWG]] carries `successor: DE-DNG` and `status: superseded`.

That is what a genuine replacement looks like in this Atlas, and it is
worth contrasting with [[DE-NIS2UMSUCG]] → [[DE-BSIG]] a few files away,
where the same relationship type is used at `confidence: low` for an
amendment and the two entities deliberately do **not** agree. The German
batch contains both patterns, which makes the difference legible in a way
no single case would.

It parallels [[NL-WOB]] → [[NL-WOO]] on the Dutch side exactly.

## Relationships

- Implements requirements from [[EU-OPEN-DATA-DIRECTIVE]].
- Supersedes [[DE-IWG]].

Inbound: [[DE-BMI]] `produces` this act.

## Sources

Listed in frontmatter — and unusually for this batch, one of them is the
**consolidated statutory text on Gesetze im Internet**, the strongest
citation available for a German federal law. It was returned by search
rather than composed. Most German legislation entities in this batch lack
an equivalent.
