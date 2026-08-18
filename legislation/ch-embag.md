---
id: CH-EMBAG
type: law
name: Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben
alternative_names:
  - EMBAG
  - EMBaG
  - Digitalisierungsgesetz
  - Federal Act on the Use of Electronic Means to Perform Official Tasks
description: >
  Swiss federal act creating the legal basis for the digital transformation
  of the federal administration and for collaboration between authorities at
  different levels of government and with third parties. It establishes
  legal foundations for open government data and open source software,
  requiring federal authorities to release new software developments as open
  source. In force for central administrative units from 1 January 2024 and
  for decentralised units from May 2025.

level: national
country: CH
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2024-01-01
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CH
  - CH-OPENDATA-SWISS
  - CH-DVS
relationships:
  - type: applies-in
    target: CH
    source: fact
    evidence: "The EMBAG is a Swiss federal act creating the legal basis for the digital transformation of the federal administration; it came into force for central administrative units on 1 January 2024 and for decentralised units in May 2025 (digital.swiss; netzwoche.ch). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)"
    url: "https://digital.swiss/de/aktionsplan/massnahme/bundesgesetz-uber-den-einsatz-elektronischer-mittel-zur-erfullung-von-behordenaufgaben-embag"
    publisher: "digital.swiss / Bundeskanzlei"
  - title: "Bundesrat setzt E-Gov-Gesetz auf Anfang 2024 in Kraft"
    url: "https://www.netzwoche.ch/news/2023-11-23/update-bundesrat-setzt-e-gov-gesetz-auf-anfang-2024-in-kraft"
    publisher: "Netzwoche"
  - title: "EMBAG macht Open Source Software zur Norm"
    url: "https://app.ch/blog/embag-macht-open-source-software-zur-norm-chance-und-verpflichtung-fuer-die-bundesverwaltung"
    publisher: "APP Unternehmensberatung AG"
  - title: "EMBAG: Ja zu Open Source Software und Open Government Data"
    url: "https://parldigi.ch/de/embag/"
    publisher: "Parlamentarische Gruppe Digitale Nachhaltigkeit (Parldigi)"
---

# EMBAG — das «Digitalisierungsgesetz»

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The EMBAG creates the legal basis for the digital transformation of the
Swiss federal administration and for collaboration between authorities at
different levels of government and with third parties. Its stated principle
is **"digital first"** for federal business processes.

## The Atlas's first statutory open-source mandate

This is why the entity matters beyond Switzerland.

The EMBAG requires federal authorities to make **new software developments
available as open source software** — the *"Public Money – Public Code"*
principle, written into a national statute rather than into a policy or a
strategy.

The Atlas holds open data instruments for every country: [[EU-OPEN-DATA-DIRECTIVE]]
and its transpositions ([[NL-WHO]], [[DE-DNG]], [[BE-HERGEBRUIK-WET]]). It
holds **no other law that obliges a public administration to publish its
software.** Open data and open *code* are different obligations, and until
now the Atlas only recorded the first.

## Two commencement dates

| Date | Scope |
|---|---|
| **1 January 2024** | Central administrative units of the federal government |
| **May 2025** | Decentralised units |

`start_date` records the first. Staged commencement by *organisational
scope* rather than by subject matter is unusual in this Atlas — compare
[[GB-DUAA]], staged by provision, and [[NL-TWCO]], which is time-limited.

## No relationships asserted

The obvious edges are to [[CH-OPENDATA-SWISS]] — the federal open data
portal, which this act's open government data provisions plainly concern —
and to [[CH-DVS]]. **Neither is asserted.** The sources describe the act's
purpose and its open source obligation; none read connects it to the portal
by name or states which body administers it under the act.

Both are in `related_entities` so the connection is discoverable, and both
are logged in `discovery/unresolved.md`.

## Not modelled

- **EMBAV**, the accompanying ordinance.
- The act's **collaboration provisions** between Confederation, cantons and
  communes — the part most relevant to the `level: local` question the Atlas
  has open.

## Sources

Listed in frontmatter. **No Fedlex citation** was returned by search; the
digital.swiss federal page is the strongest source here, with trade press
and an advocacy group's page supporting it.
