---
id: DE-MOBILITHEK
type: platform
name: Mobilithek
alternative_names:
  - "Mobilithek.info"
description: >
  German national platform for exchanging digital mobility information from
  mobility providers, infrastructure operators, traffic authorities and
  information providers. It serves as Germany's National Access Point for
  mobility data, replacing the Mobility Data Marketplace, and implements
  requirements from the delegated regulations under the European ITS
  Directive and from the revised Passenger Transport Act.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - EU-ITS-DIRECTIVE
  - DE-MDS
  - NL-NTM
relationships:
  - type: implements-requirement-from
    target: EU-ITS-DIRECTIVE
    source: fact
    evidence: "The Mobilithek replaced the Mobility Data Marketplace (MDM) as the National Access Point for mobility data and implements requirements from the delegated regulations on the European ITS Directive and the revised Passenger Transport Act (bmv.de 'Mobilithek — Deutschlands Plattform für Daten, die etwas bewegen'; forschungsinformationssystem.de). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Mobilithek — Deutschlands Plattform für Daten, die etwas bewegen"
    url: "https://www.bmv.de/SharedDocs/DE/Artikel/G/mobilithek.html"
    publisher: "Bundesministerium für Verkehr (BMV)"
  - title: "Mobilithek.info — Mobilitätsdaten Deutschland"
    url: "https://mobilithek.info/"
    publisher: "Mobilithek"
  - title: "Mobilithek"
    url: "https://forschungsinformationssystem.de/servlet/is/Entry.587544.Display/"
    publisher: "Forschungsinformationssystem Mobilität und Verkehr"
  - title: "Datenplattform: Die Mobilithek geht an den Start"
    url: "https://its-mobility.de/datenplattform-die-mobilithek-geht-an-den-start/"
    publisher: "ITS mobility"
---

# Mobilithek

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Mobilithek is the German platform for exchanging digital mobility
information between mobility providers, infrastructure operators, traffic
authorities and information providers. Timetable data, real-time traffic
information and the locations of rental bikes are among the examples given;
these can be retrieved centrally and integrated into information services.

It is Germany's **National Access Point** for mobility data and plays a
central role in a wider mobility data ecosystem. It **replaced the Mobility
Data Marketplace (MDM)** in that role, and implements requirements from the
delegated regulations under [[EU-ITS-DIRECTIVE]] and from the revised
Passenger Transport Act (Personenbeförderungsgesetz).

Its full link with [[DE-MDS]], the Mobility Data Space, was established in
the first half of 2025.

## Two National Access Points, one directive

[[EU-ITS-DIRECTIVE]] is the fourth EU instrument in the Atlas with two
national implementations, and the most exact parallel of the four:

```
                 EU-ITS-DIRECTIVE
                  │            │
    implements-requirement-from
                  ▼            ▼
            NL-NTM        DE-MOBILITHEK
      (part-of NL-NDW)    (replaced MDM)
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
fairly while preserving intellectual property rights.

Their 2025 linkage is recorded in prose. **No relationship is asserted** —
"full link established" describes a technical integration whose nature no
source read specifies, and the Atlas has no relationship type for "was
connected to" that would not overstate it.

## The `MDM` predecessor is not an entity

The Mobility Data Marketplace was replaced by the Mobilithek in the
National Access Point role. Unlike [[DE-IWG]], **no superseded entity was
created for it**, because nothing beyond its replacement is established —
not its operator, not its dates, not its scope. [[DE-IWG]] cleared the bar
because the DNG carries a sourced `previous_version` relationship to it;
the MDM does not. Queued in `discovery/research-queue.md`.

## Relationships

- Implements requirements from [[EU-ITS-DIRECTIVE]].

## Sources

Listed in frontmatter. Note the ministry is cited as **BMV**
(Bundesministerium für Verkehr); the same ministry appears elsewhere in
this batch as BMDV. The German transport ministry has been renamed and its
digital competences moved to [[DE-BMDS]]. The publisher field records the
name on the cited URL rather than reconciling the two.
