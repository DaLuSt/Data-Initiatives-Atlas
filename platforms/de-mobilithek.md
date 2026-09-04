---
id: DE-MOBILITHEK
type: platform
name: Mobilithek
alternative_names:
  - "Mobilithek.info"
description: >
  German national platform for exchanging digital mobility information from
  mobility providers, infrastructure operators, traffic authorities and
  information providers, launched 1 July 2022 by the Federal Ministry for
  Digital and Transport. It serves as Germany's National Access Point for
  mobility data under the delegated regulations of the European ITS
  Directive (2010/40/EU), replacing both the Mobility Data Marketplace
  (MDM) and the mCLOUD open-data portal by the end of 2023, and implements
  requirements from the revised Passenger Transport Act
  (Personenbeförderungsgesetz).

level: national
country: DE
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2022-07-01
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - EU-ITS-DIRECTIVE
  - DE-MDS
  - NL-NTM
  - DE-BMV
relationships:
  - type: implements-requirement-from
    target: EU-ITS-DIRECTIVE
    source: fact
    evidence: "Confirmed by reading forschungsinformationssystem.de directly (2026-08-28): 'Mobilithek acts as Germany's national access point under the EU's Intelligent Transport Systems (ITS) Directive (2010/40/EU) and its delegated regulations,' a precise directive citation not previously recorded on this entity, and implements requirements from Germany's revised Passenger Transport Act (Personenbeförderungsgesetz), which mandates public transit operators and charging-infrastructure providers to supply data through designated channels. bmv.de's own page, also read directly, independently confirms Mobilithek's National Access Point role and describes it replacing both the Mobility Data Marketplace and the mCLOUD portal by end of 2023."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Mobilithek — Deutschlands Plattform für Daten, die etwas bewegen"
    url: "https://www.bmv.de/SharedDocs/DE/Artikel/G/mobilithek.html"
    publisher: "Bundesministerium für Verkehr (BMV)"
    accessed: "2026-08-28"
  - title: "Mobilithek.info — Mobilitätsdaten Deutschland"
    url: "https://mobilithek.info/"
    publisher: "Mobilithek"
    accessed: "2026-08-28"
  - title: "Mobilithek"
    url: "https://forschungsinformationssystem.de/servlet/is/Entry.587544.Display/"
    publisher: "Forschungsinformationssystem Mobilität und Verkehr"
    accessed: "2026-08-28"
  - title: "Datenplattform: Die Mobilithek geht an den Start"
    url: "https://its-mobility.de/datenplattform-die-mobilithek-geht-an-den-start/"
    publisher: "ITS mobility"
    accessed: "2026-08-28"
---

# Mobilithek

> **Re-verified 2026-08-28.** All four cited pages fetched; three loaded
> with substantive content (`bmv.de`, which loaded successfully this pass
> unlike its sibling URL cited on [[DE-MDS]]; `forschungsinformationssystem.de`;
> `its-mobility.de`), and `mobilithek.info` returned only a page-title stub.
> `verification: primary-source`; `confidence` raised to `high`; the launch
> date, previously unrecorded, is now sourced.

## Description

The Mobilithek is the German platform for exchanging digital mobility
information between mobility providers, infrastructure operators, traffic
authorities and information providers, **launched on 1 July 2022** by the
Federal Ministry for Digital and Transport — confirmed directly this pass
on its-mobility.de, which quotes then-minister Volker Wissing directly:
"Wir brauchen mehr und bessere verfügbare Daten." Timetable data, real-time
traffic information and the locations of rental bikes are among the
examples given; these can be retrieved centrally and integrated into
information services, and its-mobility.de describes the platform as
infrastructure for third-party app development rather than a
traveller-facing tool itself.

It is Germany's **National Access Point** for mobility data under the
**EU's ITS Directive, 2010/40/EU**, and its delegated regulations — a
precise directive citation confirmed directly this pass on
forschungsinformationssystem.de, sharper than the entity's previous
unspecific reference to "the delegated regulations under the European ITS
Directive." It **replaced both the Mobility Data Marketplace (MDM) and the
mCLOUD open-data portal** by the end of 2023 — the mCLOUD predecessor is a
fact newly confirmed this pass and not previously recorded here — and
implements requirements from the revised Passenger Transport Act
(Personenbeförderungsgesetz).

Its full link with [[DE-MDS]], the Mobility Data Space, was established in
the first half of 2025.

## Two National Access Points, one directive

[[EU-ITS-DIRECTIVE]] is the fourth EU instrument in the Atlas with two
national implementations, and the most exact parallel of the four:

```
                 EU-ITS-DIRECTIVE (2010/40/EU)
                  │            │
    implements-requirement-from
                  ▼            ▼
            NL-NTM        DE-MOBILITHEK
      (part-of NL-NDW)    (replaced MDM + mCLOUD)
```

Both are National Access Points required by the same delegated regulations.
Neither country's version is a copy of the directive; the directive is one
entity applying in both.

This one is worth dwelling on because of how it arrived. Batch 5 could not
name the instrument behind [[NL-NTM]] and recorded the gap; Batch 8 found
[[EU-ITS-DIRECTIVE]] and closed it with a citation. The German batch then
attached a second country to the same node without touching either
existing entity. That is the country-neutral model paying back the
discipline of the earlier refusal.

**No relationship between [[NL-NTM]] and this entity is asserted.**

## Two German mobility platforms, deliberately kept apart

The Mobilithek and [[DE-MDS]] are distinct entities because the sources
distinguish them: the Mobilithek primarily makes **open and legally
published data** available, while the Mobility Data Space is a **data
marketplace** where mobility-relevant data can be traded securely and
fairly while preserving intellectual property rights — confirmed
independently this pass via [[DE-MDS]]'s own re-verification.

Their 2025 linkage is recorded in prose. **No relationship is asserted** —
"full link established" describes a technical integration whose nature no
source read specifies, and the Atlas has no relationship type for "was
connected to" that would not overstate it.

## The `MDM` and `mCLOUD` predecessors are not entities

The Mobility Data Marketplace and the mCLOUD portal were both replaced by
the Mobilithek in the National Access Point / open-data role — the mCLOUD
predecessor confirmed for the first time this pass. Unlike [[DE-IWG]], **no
superseded entity was created for either**, because nothing beyond their
replacement is established — not their operators in detail, not exact
dates, not scope beyond what is stated above. [[DE-IWG]] cleared the bar
because the DNG carries a sourced `previous_version` relationship to it;
neither predecessor here does. Queued in `discovery/research-queue.md`.

## ✅ The BMV/BMDV naming inconsistency, resolved

A research-queue pickup on 2026-09-04 closed the gap this entity's own
Sources section used to flag. [[DE-BMV]] is now an Atlas entity: the
Bundesministerium für Digitales und Verkehr (BMDV) was renamed the
Bundesministerium für Verkehr (BMV) on 6 May 2025, the same date its
digital competences transferred to [[DE-BMDS]]. Mobilithek — a
transport-sector platform — stayed with the renamed transport ministry
rather than moving to the new digital ministry, which is why `bmv.de`
(current) and `bmdv.bund.de`-attributed sources (pre-2025) both describe
the same platform without contradiction.

## Relationships

- Implements requirements from [[EU-ITS-DIRECTIVE]] — confirmed directly
  this pass with a precise directive citation, `confidence: high`.

[[DE-BMV]] carries the `produces` edge pointing here, added 2026-09-04.

## Sources

Listed in frontmatter. Three of four loaded with substantive content this
pass; `mobilithek.info` returned only a bare page title. The ministry is
cited as **BMV** on current sources and **BMDV** on pre-2025 ones — no
longer an unreconciled inconsistency; see [[DE-BMV]].
