---
id: DE-MODERNISIERUNGSAGENDA-FOEDERAL
type: strategy
name: Föderale Modernisierungsagenda
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
coverage: medium
verification: primary-source
start_date: 2025-12-04
end_date: null
last_verified: "2026-09-06"
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
    evidence: "Confirmed by reading bmds.bund.de's 'Modernisierungsagenda Föderal' page (2026-08-22): 'haben Bund und Länder bei der Ministerpräsidentenkonferenz am 4. Dezember 2025 die \"Föderale Modernisierungsagenda\" gestartet. Sie umfasst über 200 Maßnahmen in fünf Handlungsfeldern.' The page is published under the BMDS's domain. Note this covers publication and stewardship only: the agenda was adopted jointly by the Bund and the Länder at the Ministerpräsidentenkonferenz, not by the BMDS."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Modernisierungsagenda Föderal"
    url: "https://bmds.bund.de/themen/staatsmodernisierung/modernisierungsagenda-foederal"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
    accessed: "2026-09-06"
  - title: "Föderale Modernisierungsagenda"
    url: "https://www.bundesregierung.de/breg-de/aktuelles/foederale-modernisierungsagenda-2397632"
    publisher: "Presse- und Informationsamt der Bundesregierung"
    accessed: "2026-08-22"
  - title: "Bund und Länder verabschieden Föderale Modernisierungsagenda"
    url: "https://www.digitale-verwaltung.de/SharedDocs/kurzmeldungen/Webs/DV/DE/2025/12_modernisierungsagenda.html"
    publisher: "Digitale Verwaltung (Bundesministerium des Innern)"
  - title: "Bund und Länder verabschieden Modernisierungsagenda"
    url: "https://bmds.bund.de/aktuelles/pressemitteilungen/detail/bund-und-laender-verabschieden-modernisierungsagenda"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
    accessed: "2026-08-22"
---

# Föderale Modernisierungsagenda

> **Verified 2026-08-22.** bmds.bund.de's "Modernisierungsagenda Föderal"
> page was read directly and confirmed the date, measure count and field
> count below verbatim. `digitale-verwaltung.de` no longer resolves (400)
> and was not re-read.
>
> **Closed 2026-09-06**: the same bmds.bund.de page names the five fields
> of action, confirmed by two independent fetches agreeing verbatim.

## Description

Confirmed verbatim on bmds.bund.de (2026-08-22): "haben Bund und Länder bei
der Ministerpräsidentenkonferenz am 4. Dezember 2025 die 'Föderale
Modernisierungsagenda' gestartet. Sie umfasst über 200 Maßnahmen in fünf
Handlungsfeldern." (A bonus figure on the same page, not previously
recorded: the agenda targets a 25% reduction in bureaucracy costs through
reduced reporting obligations — "Einsparung von 25 Prozent bei den
Bürokratiekosten".) The Bund and the Länder launched the *Föderale
Modernisierungsagenda* at
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

**The five fields of action, closed 2026-09-06** — confirmed verbatim on
bmds.bund.de, read directly (two independent fetches agreeing):

1. **Weniger Bürokratie – weniger Behördengänge** (less bureaucracy — fewer trips to the authorities)
2. **Schnellere Verfahren – schnellere Genehmigungen** (faster procedures — faster approvals)
3. **Resiliente Strukturen – effizienter Staat** (resilient structures — a more efficient state)
4. **Datensparsame Verfahren – digitaler Staat** (data-sparing procedures — a digital state)
5. **Bessere Rechtsetzung – klarere Regeln** (better lawmaking — clearer rules)

`coverage` moves from `low`: the date, measure count, field count and now
the fields themselves are established. The content of the 200+ individual
measures within each field remains unresearched.

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

Listed in frontmatter. bmds.bund.de's own page was read directly in
both the 2026-08-22 and 2026-09-06 passes.
