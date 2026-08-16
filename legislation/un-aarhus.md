---
id: UN-AARHUS
type: law
name: Convention on Access to Information, Public Participation in Decision-making and Access to Justice in Environmental Matters
alternative_names:
  - Aarhus Convention
  - UNECE Aarhus Convention
description: >
  UNECE convention adopted on 25 June 1998 in Aarhus, Denmark, at the Fourth
  Ministerial Conference in the 'Environment for Europe' process, and in
  force since 30 October 2001. It rests on three pillars — access to
  information, public participation in decision-making, and access to
  justice in environmental matters — and Article 1 requires Parties to
  guarantee those rights. As of April 2023 it had 49 Parties: 48 states and
  the European Union. The European Union and all 27 of its member states are
  Parties.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2001-10-30
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - UN-UNECE
related_entities:
  - UN-UNECE
  - EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE
  - EU
relationships:
  - type: maintained-by
    target: UN-UNECE
    source: fact
    evidence: "The Convention is the UNECE Convention on Access to Information, Public Participation in Decision-making and Access to Justice in Environmental Matters, adopted at the Fourth Ministerial Conference in the 'Environment for Europe' process; UNECE publishes its introduction, content and implementation guide, and hosts the Aarhus Clearinghouse (unece.org/environment-policy/public-participation/aarhus-convention/introduction; unece.org .../content; aarhusclearinghouse.unece.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: NL
    source: fact
    evidence: "The EU and its 27 Member States are all Parties to the Aarhus Convention, the UNECE Convention on access to information, public participation in decision-making and access to justice in environmental matters (environment.ec.europa.eu/law-and-governance/aarhus_en). NOT READ — search-only. No Dutch instrument of ratification is cited and none is asserted."
    confidence: medium
    valid_from: 2001-10-30
    valid_until: null
  - type: applies-in
    target: DE
    source: fact
    evidence: "The EU and its 27 Member States are all Parties to the Aarhus Convention (environment.ec.europa.eu/law-and-governance/aarhus_en; environment.ec.europa.eu/law-and-governance/aarhus_de). NOT READ — search-only. No German instrument of ratification is cited and none is asserted."
    confidence: medium
    valid_from: 2001-10-30
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "The EU and its 27 Member States are all Parties to the Aarhus Convention (environment.ec.europa.eu/law-and-governance/aarhus_en). NOT READ — search-only. No Belgian instrument of ratification is cited and none is asserted."
    confidence: medium
    valid_from: 2001-10-30
    valid_until: null
  - type: applies-in
    target: FR
    source: fact
    evidence: "The EU and its 27 Member States are all Parties to the Aarhus Convention (environment.ec.europa.eu/law-and-governance/aarhus_en). NOT READ — search-only. No French instrument of ratification is cited and none is asserted."
    confidence: medium
    valid_from: 2001-10-30
    valid_until: null
  - type: applies-in
    target: ES
    source: fact
    evidence: "The EU and its 27 Member States are all Parties to the Aarhus Convention (environment.ec.europa.eu/law-and-governance/aarhus_en). NOT READ — search-only. No Spanish instrument of ratification is cited and none is asserted."
    confidence: medium
    valid_from: 2001-10-30
    valid_until: null

sources:
  - title: "Introduction: Aarhus Convention"
    url: "https://unece.org/environment-policy/public-participation/aarhus-convention/introduction"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "Content of the Convention"
    url: "https://unece.org/environment-policy/public-participation/aarhus-convention/content"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "Convention on Access to Information, Public Participation in Decision-making and Access to Justice in Environmental Matters (text)"
    url: "https://unece.org/DAM/env/pp/documents/cep43e.pdf"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "The Aarhus Convention and the EU"
    url: "https://environment.ec.europa.eu/law-and-governance/aarhus_en"
    publisher: "European Commission — Environment"
  - title: "The Aarhus Convention — an implementation guide"
    url: "https://www.unece.org/fileadmin/DAM/env/pp/implementation%20guide/english/part1.pdf"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
---

# Aarhus Convention

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Aarhus Convention was adopted on **25 June 1998** in Aarhus, Denmark, at
the Fourth Ministerial Conference in the *Environment for Europe* process,
and entered into force on **30 October 2001**.

It rests on **three pillars**:

1. **access to information**,
2. **public participation** in decision-making,
3. **access to justice** in environmental matters.

Article 1 requires Parties to guarantee those rights. As of April 2023 it
had **49 Parties: 48 states and the European Union.**

## This is the Atlas's first UN → national relationship

Every `applies-in` relationship in the Atlas until now has run from an **EU**
instrument to a country. This one runs from a **UN** instrument to five
countries, because the EU and all 27 member states are Parties in their own
right.

That single fact does something the statistics bridge does not: it puts UN
instruments and EU instruments on the same footing in the graph. A reader
filtering by `applies-in` now sees national applicability descending from
two levels, not one.

The Convention is also the **oldest instrument in the Atlas after
[[BE-KSZ-WET]] (1990) and [[FR-LIL]] (1978)** — a 1998 treaty that the EU's
own access-to-information law was written to satisfy.

## The chain it completes

```
   UN-AARHUS  (UNECE convention, 1998 / in force 2001)
        │  implements-requirement-from
        ▼
   EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE  (2003/4/EC)
        │  applies-in
        ▼
   NL · DE · BE · FR · ES
```

Batch 15 called the DCAT descent *"the template for what the UN layer
lacks"* — an international standard, a European profile, national
adaptations. This is that template in **law** rather than metadata, and it
reaches one level higher: DCAT starts at [[INTL-DCAT]], a W3C
recommendation. This starts at a UN treaty.

## What is deliberately not asserted

- **No national ratification instruments.** The claim sourced here is
  "the EU and all 27 member states are Parties", which supports
  `applies-in`. It does **not** identify the Dutch, German, Belgian, French
  or Spanish instrument of ratification, and none is named. Each evidence
  string says so explicitly.
- **No relationship to [[EU-OPEN-DATA-DIRECTIVE]] or [[EU-INSPIRE]].**
  Environmental information access is adjacent to both — INSPIRE is a
  geospatial environmental data directive, and the open data directive
  governs re-use of public sector information. `discovery/candidates.md`
  flagged the adjacency as *"a reason to research, not a finding"*, and it
  is left exactly there. Nothing read connects them.
- **The two pillars beyond information are not modelled separately.** Public
  participation and access to justice are recorded in this description and
  have no entities of their own; the Atlas's scope is data and information
  governance, and only the first pillar sits inside it.

## Relationships

- `maintained-by` [[UN-UNECE]].
- `applies-in` [[NL]], [[DE]], [[BE]], [[FR]], [[ES]].

## Sources

Listed in frontmatter — three UNECE pages including the Convention text and
implementation guide, and the European Commission's own page on the
Convention and the EU.
