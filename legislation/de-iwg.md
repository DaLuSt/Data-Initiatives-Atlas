---
id: DE-IWG
type: law
name: Informationsweiterverwendungsgesetz
alternative_names:
  - IWG
  - Act on the Re-use of Public Sector Information
description: >
  Former German federal act on the re-use of public sector information,
  modernised and replaced by the Datennutzungsgesetz with effect from
  23 July 2021. Retained in the Atlas as a superseded entity so that the
  German open-data lineage remains traceable.

level: national
country: DE
region: EU

status: superseded
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: 2021-07-23
last_verified: null
previous_version: null
successor: DE-DNG

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-DNG
relationships: []

sources:
  - title: "Datennutzungsgesetz"
    url: "https://de.wikipedia.org/wiki/Datennutzungsgesetz"
    publisher: "Wikipedia"
  - title: "Zweites Open-Data-Gesetz und Datennutzungsgesetz"
    url: "https://www.prosoz.de/zweites-open-data-gesetz-und-datennutzungsgesetz/"
    publisher: "PROSOZ Herten"
  - title: "Mehr Verwaltungsdaten sollen öffentlich zugänglich werden"
    url: "https://www.haufe.de/oeffentlicher-dienst/digitalisierung-transformation/mehr-verwaltungsdaten-sollen-oeffentlich-zugaenglich-werden_524786_536824.html"
    publisher: "Haufe"
---

# Informationsweiterverwendungsgesetz (IWG)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The IWG was Germany's federal act on the re-use of public sector
information. It was **modernised and replaced** by [[DE-DNG]], which came
into force on 23 July 2021.

## Why a nearly empty entity is worth keeping

Almost nothing about this act is recorded: not its enactment date, not its
substance, not which EU instrument it originally transposed. `confidence`
and `coverage` are both `low` and honestly so.

It exists because **§7 of the brief forbids reusing an ID and the Atlas
retains superseded entities rather than deleting them**. Without it,
[[DE-DNG]]'s `previous_version` would dangle and Germany's open-data
lineage would begin in 2021 with no indication that anything preceded it.
The Atlas treats "this was replaced by that" as a fact worth holding even
when the replaced thing is poorly documented.

The same judgement produced [[NL-WOB]], [[NL-EAR]] and [[EU-NIS]] on the
other layers. [[NL-WOB]] is the direct parallel: a superseded national
information-access act retained under a successor.

## What is deliberately not recorded

The IWG was, in all likelihood, Germany's transposition of the **2003 PSI
Directive** and its 2013 revision — the predecessors of
[[EU-OPEN-DATA-DIRECTIVE]]. **No `implements-requirement-from` relationship
is asserted**, for two reasons: no source read says so, and neither
predecessor directive is an Atlas entity, so the relationship would have
nowhere to point.

Creating those directives to give this entity somewhere to point would be
building the graph to suit a guess. Queued in
`discovery/research-queue.md`.

## Relationships

**None asserted.** Reached from [[DE-DNG]] via `supersedes` and
`previous_version`.

## Sources

Listed in frontmatter. All three are sources about the **DNG** that mention
the IWG in passing; **no source specifically about the IWG was found**.
That is the weakest sourcing position of any German entity in this batch,
and it is why `confidence: low` rather than medium.
