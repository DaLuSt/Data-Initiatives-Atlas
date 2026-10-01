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
last_verified: "2026-10-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - DE-BMDS
related_entities:
  - DE-MODERNISIERUNGSAGENDA-BUND
  - DE-DEUTSCHLAND-STACK
  - EU-EUDI-WALLET
relationships:
  - type: maintained-by
    target: DE-BMDS
    source: fact
    evidence: "Confirmed by reading bmds.bund.de's 'Modernisierungsagenda Föderal' page (2026-08-22): 'haben Bund und Länder bei der Ministerpräsidentenkonferenz am 4. Dezember 2025 die \"Föderale Modernisierungsagenda\" gestartet. Sie umfasst über 200 Maßnahmen in fünf Handlungsfeldern.' The page is published under the BMDS's domain. Note this covers publication and stewardship only: the agenda was adopted jointly by the Bund and the Länder at the Ministerpräsidentenkonferenz, not by the BMDS. **Qualified further 2026-10-01** by digitale-verwaltung.de's own announcement of the adoption (read directly via the cookie-jar workaround, discovery/unresolved.md row #217), which says the agenda was 'Koordiniert vom Bundeskanzleramt und unter aktiver Mitwirkung des Bundesministeriums für Digitales und Staatsmodernisierung (BMDS), des Bundesministeriums der Finanzen (BMF), des Bundesministeriums für Arbeit und Soziales (BMAS) und des Bundesministeriums des Innern (BMI)' — so the BMDS was one of four participating ministries, and the coordinating body was the Chancellery. The edge stays at low: it records that the BMDS publishes and stewards the agenda, not that it leads it."
    confidence: low
    valid_from: null
    valid_until: null
  - type: references
    target: DE-DEUTSCHLAND-STACK
    source: fact
    evidence: "Confirmed 2026-10-01 by reading digitale-verwaltung.de's announcement of the agenda's adoption directly (cookie-jar workaround, row #217), under the field of action 'Datensparsame Verfahren – digitaler Staat': 'Mit dem Aufbau des D-Stack entsteht ein gemeinsames digitales Betriebssystem für Bund, Länder und Kommunen, das offene Standards wie ELSTER nutzt und souverän europäisch anschlussfähig ist.' The agenda cites the D-Stack as one of its measures. `references` rather than `implements`: the source says the agenda includes building it, not that the Stack initiative was created by or under the agenda."
    confidence: high
    valid_from: 2025-12-04
    valid_until: null
  - type: references
    target: EU-EUDI-WALLET
    source: fact
    evidence: "Confirmed 2026-10-01 by reading digitale-verwaltung.de's announcement of the agenda's adoption directly (row #217), under the same field of action: 'Die EUDI-Wallet ermöglicht Ausweise, Nachweise und Bescheide direkt und sicher auf dem Smartphone.' The agenda names the EU Digital Identity Wallet as part of its digital-state measures."
    confidence: high
    valid_from: 2025-12-04
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
    accessed: "2026-10-01"
    note: "Read directly via a cookie-jar-aware fetch (discovery/unresolved.md row #217); the HTTP 400 recorded on 2026-08-22 was a missing session cookie, not a genuine block."
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
> **Closed 2026-10-01** (`discovery/unresolved.md` row #217): that 400 was
> a missing session cookie. The `digitale-verwaltung.de` announcement is
> now read directly; it matches the date, measure count and five fields
> verbatim, adds that the agenda was **coordinated by the Bundeskanzleramt**
> with four ministries participating and was negotiated in **11 working
> groups**, and names the D-Stack and the EUDI-Wallet among its measures.
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

## Who coordinated it — added 2026-10-01

The digitale-verwaltung.de announcement, read directly, says the agenda was
"koordiniert vom Bundeskanzleramt" (coordinated by the Federal Chancellery)
"unter aktiver Mitwirkung" (with the active participation) of the BMDS, the
BMF, the BMAS and the BMI, and that 11 working groups reviewed "alle
Bereiche der föderalen Zusammenarbeit von Daseinsvorsorge bis
Cybersicherheit" (all areas of federal cooperation from public services to
cybersecurity). The Chancellery is not an Atlas entity, so this is recorded
here and in the `maintained-by` caveat rather than as an edge. It also
corroborates the five fields above and several measures the page lists:
a 25% reduction in bureaucracy costs, a *Genehmigungsfiktion* (approvals
deemed granted if an authority has not decided within three months), the
**D-Stack** ([[DE-DEUTSCHLAND-STACK]]), the once-only principle and the
**EUDI-Wallet** ([[EU-EUDI-WALLET]]).

## Relationships

- References [[DE-DEUTSCHLAND-STACK]] and [[EU-EUDI-WALLET]] — both named as
  measures on the adoption announcement, `confidence: high`.
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
both the 2026-08-22 and 2026-09-06 passes, and digitale-verwaltung.de's
announcement — previously unreadable — on 2026-10-01.
