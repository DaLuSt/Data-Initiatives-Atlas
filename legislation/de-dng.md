---
id: DE-DNG
type: law
name: Datennutzungsgesetz
alternative_names:
  - DNG
  - Gesetz für die Nutzung von Daten des öffentlichen Sektors
description: >
  German federal act on the use of public sector data, enacted as part of
  the "Zweites Open-Data-Gesetz" package and in force from 23 July 2021. It
  implements the EU's Open Data Directive (Richtlinie (EU) 2019/1024) on
  open data and the re-use of public
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
verification: primary-source
start_date: 2021-07-23
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading de.wikipedia.org's 'Datennutzungsgesetz' article (2026-08-22): the DNG 'dient der Umsetzung der PSI-Richtlinie', citing 'Richtlinie (EU) 2019/1024 des Europäischen Parlaments und des Rates vom 20. Juni 2019 über offene Daten und die Weiterverwendung von Informationen des öffentlichen Sektors' directly."
    confidence: medium
    valid_from: 2021-07-23
    valid_until: null
  - type: supersedes
    target: DE-IWG
    source: fact
    evidence: "Confirmed by reading de.wikipedia.org's 'Datennutzungsgesetz' article (2026-08-22): the DNG 'löste das Informationsweiterverwendungsgesetz (IWG) ab', and the statute text itself (gesetze-im-internet.de) confirms entry into force '23. Juli 2021'."
    confidence: medium
    valid_from: 2021-07-23
    valid_until: null

sources:
  - title: "DNG — Gesetz für die Nutzung von Daten des öffentlichen Sektors"
    url: "https://www.gesetze-im-internet.de/dng/DNG.pdf"
    publisher: "Bundesministerium der Justiz / juris (Gesetze im Internet)"
    accessed: "2026-08-22"
  - title: "Datennutzungsgesetz"
    url: "https://de.wikipedia.org/wiki/Datennutzungsgesetz"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Zweites Open-Data-Gesetz und Datennutzungsgesetz"
    url: "https://www.de.digital/Redaktion/DE/Artikel/Service/Gesetzesvorhaben/zweites-open-data-gesetz-und-datennutzungsgesetz.html"
    publisher: "DE.DIGITAL (Bundesministerium für Wirtschaft)"
    accessed: "2026-08-22"
  - title: "Bundesregierung legt Änderung am E-Government-Gesetz und neues Datennutzungsgesetz vor"
    url: "https://www.open-government-deutschland.de/opengov-de/bundesregierung-legt-aenderung-am-e-government-gesetz-und-neues-datennutzungsgesetz-vor-1852186"
    publisher: "Open Government Deutschland (Bundesregierung)"
    accessed: "2026-08-22"
  - title: "Das neue Datennutzungsgesetz"
    url: "https://www.bho-legal.com/en/das-neue-datennutzungsgesetz/"
    publisher: "BHO Legal"
    accessed: "2026-08-22"
---

# Datennutzungsgesetz (DNG)

> **Verified 2026-08-22.** The consolidated statute text at
> gesetze-im-internet.de and de.wikipedia.org's "Datennutzungsgesetz"
> article were read directly and confirmed the claims below.

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
