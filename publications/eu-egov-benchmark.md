---
id: EU-EGOV-BENCHMARK
type: publication
name: eGovernment Benchmark
alternative_names:
  - eGovernment Benchmark report
description: >
  Annual study published by the European Commission evaluating the provision
  and delivery of eGovernment services in 35 countries — the 27 EU member
  states plus Iceland, Norway, Switzerland, Albania, Montenegro, North
  Macedonia, Serbia and Türkiye. The 2025 edition assessed 14,104 government
  websites relating to nine key life events using 20 indicators and 51 survey
  questions, evaluated by an EU-wide network of mystery shoppers in November
  2024, and reports against three dimensions: online service delivery,
  interoperability signifiers, and user-friendly portals. It feeds the
  digital public services measurement used in the Digital Decade monitoring.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - EU-COMMISSION
related_entities:
  - EU
  - EU-COMMISSION
  - EU-DESI
  - EU-DIGITAL-DECADE
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "The eGovernment Benchmark evaluates provision and delivery of eGovernment services in 35 countries across Europe — the 27 EU member states and Iceland, Norway, Switzerland, Albania, Montenegro, North Macedonia, Serbia and Türkiye — and is published by the European Commission (op.europa.eu publication-detail 'eGovernment benchmark 2025'; digital-strategy.ec.europa.eu 'Digital Public Services in DESI'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3 for an EU-scoped entity."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: aligned-with
    target: EU-DESI
    source: fact
    evidence: "The eGovernment Benchmark feeds the digital public services dimension of the Digital Economy and Society Index, which the Commission documents on its 'Digital Public Services in the Digital Economy and Society Index' page (digital-strategy.ec.europa.eu/en/policies/desi-digital-public-services; op.europa.eu 'eGovernment benchmark 2025'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "eGovernment benchmark 2025"
    url: "https://op.europa.eu/en/publication-detail/-/publication/97d9c42d-4742-11f0-85ba-01aa75ed71a1/language-en"
    publisher: "Publications Office of the European Union"
  - title: "Digital Public Services in the Digital Economy and Society Index"
    url: "https://digital-strategy.ec.europa.eu/en/policies/desi-digital-public-services"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "eGovernment Benchmark 2022"
    url: "https://digital-strategy.ec.europa.eu/en/library/egovernment-benchmark-2022"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "eGovernment Benchmark Report 2025: On track for user-friendly online public services"
    url: "https://www.capgemini.com/gb-en/insights/research-library/egovernment-benchmark-report-towards-digital-government/"
    publisher: "Capgemini"
---

# eGovernment Benchmark

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval of
> `op.europa.eu` and `digital-strategy.ec.europa.eu` is blocked by the network
> egress proxy. `verification: search-only`.

## Description

The Commission's annual study of how European public administrations deliver
services online. The **2025 edition** assessed **14,104 government websites**
covering **nine key life events**, using **20 indicators** and **51 survey
questions**, evaluated by an EU-wide network of **mystery shoppers** in
November 2024, and reports against three dimensions:

- online service delivery
- interoperability signifiers
- user-friendly portals

It feeds the **digital public services** measurement that appears in
[[EU-DESI]] and the Digital Decade monitoring.

## The 35 countries are all in this Atlas

The benchmark covers the 27 member states plus **eight non-EU countries**:

| | |
|---|---|
| EEA EFTA and EFTA | [[IS]], [[NO]], [[CH]] |
| Enlargement countries | [[AL]], [[ME]], [[MK]], [[RS]], [[TR]] |

Every one of those thirty-five is an Atlas country anchor, which is a
consequence of the European country expansion rather than a coincidence — the
Atlas took "the Council of Europe member states" as its scope rule, and the
Commission's benchmark scope sits inside it.

That coverage is the reason this entity is worth more than its sources: it is
the first thing in the Atlas whose stated scope is a **set of countries the
Atlas already holds in full**, and it names which of them the Commission
measures together.

## Publisher and contractor

The benchmark is a **Commission publication** — the 2025 edition is in the
Publications Office catalogue — carried out under contract by Capgemini and
partners. The Capgemini page is cited because it is the one page in the
source set that is not behind the blocked publications host, and it is
attributed to Capgemini rather than to the Commission in the `sources:` list.

**No entity is created for Capgemini.** A private contractor named as the
executor of one study is not an Atlas subject, and creating it would put a
commercial organisation into a graph of public bodies on the strength of a
procurement.

## What is deliberately not asserted

As with [[EU-DESI]], **no edge is asserted to any of the 35 countries
measured**. There is no `measures` relationship type, and the alternatives
would all misstate it: `applies-in` would make a study into an instrument,
`references` would suggest citation rather than assessment.

## Relationships

- `part-of` [[EU]] — anchor edge.
- `aligned-with` [[EU-DESI]] — the benchmark supplies the digital public
  services measurement DESI reports. `part-of` would overstate it: the
  benchmark is a study in its own right with its own scope of 35 countries,
  wider than DESI's 27.

## Sources

Listed in frontmatter — the Publications Office record of the 2025 edition,
two Commission pages, and the contractor's report page.
