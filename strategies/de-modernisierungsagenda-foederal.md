---
id: DE-MODERNISIERUNGSAGENDA-FOEDERAL
type: strategy
name: Föderale Modernisierungsagenda
alternative_names:
  - Federal-Länder Modernisation Agenda
description: >
  Joint modernisation agenda of the German federal government and the
  Länder, adopted at the Ministerpräsidentenkonferenz on 4 December 2025.
  It comprises more than 200 measures across five fields of action and is
  the Bund-Länder counterpart to the federal Modernisierungsagenda adopted
  in October 2025.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: 2025-12-04
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - DE-BMDS
related_entities:
  - DE-MODERNISIERUNGSAGENDA-BUND
relationships:
  - type: maintained-by
    target: DE-BMDS
    source: fact
    evidence: "The agenda is published by the BMDS under its Staatsmodernisierung theme, and the BMDS issued the press release announcing its adoption by the Bund and the Länder (bmds.bund.de/themen/staatsmodernisierung/modernisierungsagenda-foederal; bmds.bund.de press release). NOT READ — search-only. Note this covers publication and stewardship only: the agenda was adopted jointly by the Bund and the Länder at the Ministerpräsidentenkonferenz, not by the BMDS."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Modernisierungsagenda Föderal"
    url: "https://bmds.bund.de/themen/staatsmodernisierung/modernisierungsagenda-foederal"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
  - title: "Föderale Modernisierungsagenda"
    url: "https://www.bundesregierung.de/breg-de/aktuelles/foederale-modernisierungsagenda-2397632"
    publisher: "Presse- und Informationsamt der Bundesregierung"
  - title: "Bund und Länder verabschieden Föderale Modernisierungsagenda"
    url: "https://www.digitale-verwaltung.de/SharedDocs/kurzmeldungen/Webs/DV/DE/2025/12_modernisierungsagenda.html"
    publisher: "Digitale Verwaltung (Bundesministerium des Innern)"
  - title: "Bund und Länder verabschieden Modernisierungsagenda"
    url: "https://bmds.bund.de/aktuelles/pressemitteilungen/detail/bund-und-laender-verabschieden-modernisierungsagenda"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
---

# Föderale Modernisierungsagenda

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Bund and the Länder launched the *Föderale Modernisierungsagenda* at
the Ministerpräsidentenkonferenz on **4 December 2025**. It comprises more
than **200 measures across five fields of action**.

It follows [[DE-MODERNISIERUNGSAGENDA-BUND]], adopted by the federal
cabinet on 1 October 2025, and extends the modernisation programme from the
federal administration to the federal-state relationship.

## Why this entity matters structurally

Germany's public administration is federal. The Bund cannot digitalise the
services that the Länder and Kommunen actually deliver, which is why
[[DE-IT-PLANUNGSRAT]] and [[DE-FITKO]] exist as standing coordination
machinery and why this agenda needed a separate Bund-Länder adoption at all.

The Atlas cannot yet model that layer properly — its `level` vocabulary
runs `international / regional / national / sectoral / local` with nothing
between `national` and `local` for a Land. This entity is recorded at
`level: national` because it is a national instrument agreed *between*
levels, which is the closest available fit and not an exact one. See
`countries/de/de.md` and `discovery/unresolved.md`.

`coverage: low`: only the date, the measure count and the number of fields
of action were established. **The five fields of action themselves are not
recorded, because no source read names them.**

## Relationships

- Maintained by [[DE-BMDS]] — at `confidence: low`, and deliberately so.
  What is sourced is that the BMDS publishes the agenda and announced its
  adoption. The agenda itself was adopted **jointly by the Bund and the
  Länder** at the Ministerpräsidentenkonferenz, so `maintained-by` captures
  stewardship, not authorship. The evidence field says this explicitly
  rather than leaving a reader to assume the ministry owns the document.

**No relationship to [[DE-MODERNISIERUNGSAGENDA-BUND]] is asserted**
despite the obvious sequence — see that entity for the reasoning.

## Sources

Listed in frontmatter.
