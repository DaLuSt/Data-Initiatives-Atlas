---
id: ES-INE
type: organisation
name: Instituto Nacional de Estadística
alternative_names:
  - INE
  - Spanish National Statistics Institute
description: >
  Spanish national statistical office. An autonomous administrative body
  with its own legal personality and assets, attached to the Ministry of
  Economy, Commerce and Business, governed principally by Ley 12/1989 on the
  public statistical function and by the statute approved by Real Decreto
  803/2022. It carries out large-scale statistical operations including
  demographic and economic censuses, prepares the National Statistical Plan,
  proposes norms on statistical concepts and classifications, and manages
  statistical relations with international organisations including Eurostat.

level: national
country: ES
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
  - EU-EUROSTAT
relationships:
  - type: related-to
    target: EU-EUROSTAT
    source: interpretation
    evidence: "Ley 12/1989 assigns the INE responsibility for, among other functions, managing statistical relations with international organisations such as Eurostat; separately, the European Statistical System is described as comprising Eurostat, the statistical offices of all EU member states and other bodies producing European statistics, with the European Statistical System Committee made up of Eurostat and the presidents of member states' national statistical institutes (ine.es 'Qué es el SEE y cómo funciona'; ine.es 'El Instituto Nacional de Estadística'; eur-lex.europa.eu summary 'Estadísticas europeas'). ATLAS INTERPRETATION: the sources describe a three-party structure — INE and Eurostat both within the European Statistical System — not a direct bilateral relationship. NOT READ — search-only."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "BOE-A-1989-10767 Ley 12/1989, de 9 de mayo, de la Función Estadística Pública"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-1989-10767"
    publisher: "Boletín Oficial del Estado (BOE)"
  - title: "El Instituto Nacional de Estadística"
    url: "https://www.ine.es/dyngs/INE/index.htm?cid=498"
    publisher: "Instituto Nacional de Estadística (INE)"
  - title: "Qué es el SEE y cómo funciona"
    url: "https://www.ine.es/ss/Satellite?L=es_ES&c=Page&cid=1254735905268&p=1254735905268&pagename=INE/INELayout"
    publisher: "Instituto Nacional de Estadística (INE)"
  - title: "Estadísticas europeas: cómo funciona el Sistema Estadístico Europeo"
    url: "https://eur-lex.europa.eu/ES/legal-content/summary/european-statistics-how-the-european-statistical-system-works.html"
    publisher: "EUR-Lex — Publications Office of the European Union"
---

# INE — Instituto Nacional de Estadística

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The INE is Spain's national statistical office: an **autonomous
administrative body** with its own legal personality and assets, attached to
the Ministry of Economy, Commerce and Business.

It is governed by **Ley 12/1989 on the public statistical function** —
amended in 2022 — and by the statute approved by Real Decreto 803/2022. The
1989 law established it as an autonomous body and provided for coordination
with the autonomous communities, the National Statistical Plan, and
relations with the European Union in statistical matters.

Its functions include large-scale statistical operations (demographic and
economic censuses, social and economic statistics, business directories),
preparing the National Statistical Plan with the ministries and the Bank of
Spain, proposing norms on statistical concepts and classifications, and
**managing statistical relations with international organisations such as
Eurostat**.

## The statistics cluster gets its first edge — and it is an interpretation

`discovery/unresolved.md` has carried a cluster of **five refused links**
across four countries: [[UN-UNSD]] → [[EU-EUROSTAT]], [[NL-CBS]] and
[[DE-DESTATIS]] to Eurostat, and [[DE-BSTATG]] and [[NL-WET-CBS]] to
[[UN-FPOS]]. Every one was refused for want of a source. Four national
statistical offices sat in the Atlas and none connected upward to anything.

Spain is the first country where a source connects the two. It is recorded,
and it is recorded honestly as **`source: interpretation`, `confidence:
low`**, because what the sources actually describe is not a bilateral
relationship:

> The European Statistical System comprises **Eurostat, the statistical
> offices of all member states, and other bodies** producing European
> statistics. The ESS Committee is made up of Eurostat and the presidents of
> the member states' national statistical institutes.

That is a **three-party structure**. INE and Eurostat are both inside the
European Statistical System; neither is described as related to the other
directly. The accurate model is:

```
                 EU-ESS  (European Statistical System)   ← does not exist
                  ▲                    ▲
             part-of                part-of
                  │                    │
              ES-INE            EU-EUROSTAT
```

**The ESS entity was not created**, for the same reason no sub-national
`level` was invented: creating a supra-national entity inside a country
batch, on evidence gathered while researching that country, is how
country-shaped assumptions get baked into shared layers. It is queued in
`discovery/research-queue.md` as the correct fix, and it would let all four
national statistical offices connect at once.

So the edge that exists here is deliberately the **weakest type the
vocabulary offers**, `related-to`, marked as the Atlas's own inference. It
records that a connection exists without claiming to know its shape.

## Why this does not lower the standard

The earlier five were refused because **no source said anything**. This one
is asserted because a source says something — just not quite the thing the
edge expresses. The provenance fields carry that difference explicitly:
`source: interpretation` and an `evidence` string that states what the
sources describe and what the Atlas concluded from it.

A reader can therefore tell this edge apart from a `source: fact` edge
without reading the sources, which is the entire purpose of the field.

## Relationships

- `related-to` [[EU-EUROSTAT]] — Atlas interpretation, low confidence.

## Sources

Listed in frontmatter — the BOE text of Ley 12/1989, two INE pages including
its explanation of the European Statistical System, and the EUR-Lex summary
of how that system works.
