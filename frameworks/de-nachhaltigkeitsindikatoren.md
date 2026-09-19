---
id: DE-NACHHALTIGKEITSINDIKATOREN
type: framework
name: Indikatorensatz der Deutschen Nachhaltigkeitsstrategie
alternative_names:
  - German Sustainability Strategy indicator set
  - Deutschlands SDG-Indikatoren
description: >
  Germany's national indicator set for measuring progress on the German
  Sustainability Strategy, incorporating at least one indicator for each
  of the UN's 17 Sustainable Development Goals. The Federal Statistical
  Office (Destatis) has been tasked, since 2006, with measuring the
  national indicators independently using official statistics, and
  publishes a biennial Indikatorenbericht. Data has been available on a
  dedicated online platform since February 2020.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2006-01-01
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains: []
organisations:
  - DE-DESTATIS
related_entities:
  - DE-DESTATIS
  - UN-SDG-INDICATORS
relationships:
  - type: based-on
    target: UN-SDG-INDICATORS
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #175. Confirmed by reading destatis.de's own page directly (2026-09-19): 'mindestens ein Indikator zu jedem der 17 Ziele in die Deutsche Nachhaltigkeitsstrategie mitaufgenommen' — at least one indicator for each of the 17 UN Sustainable Development Goals was incorporated into the German Sustainability Strategy's indicator set, the same kind of partial, qualitative descent [[EU-SDG-INDICATORS]] carries from the UN list, though without a quantified count comparable to that entity's '55 of 100'."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: DE-DESTATIS
    source: fact
    evidence: "Confirmed by reading destatis.de's own page directly (2026-09-19): 'Das Statistische Bundesamt ist damit beauftragt, die Messung der nationalen Indikatoren, fachlich unabhängig, mit eigenen Daten aus der amtlichen Statistik zu stützen' — the Federal Statistical Office has been tasked, since 2006, with measuring the national indicators independently using its own official statistical data, and publishes an Indikatorenbericht for the strategy every two years ('im zweijährigen Rhythmus')."
    confidence: high
    valid_from: "2006-01-01"
    valid_until: null

sources:
  - title: "Das Indikatorenset — Entstehung und Weiterentwicklung"
    url: "https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Nachhaltigkeitsindikatoren/Deutsche-Nachhaltigkeit/entstehung-entwicklung.html"
    publisher: "Statistisches Bundesamt (Destatis)"
    accessed: "2026-09-19"
---

# Indikatorensatz der Deutschen Nachhaltigkeitsstrategie

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #175 ("no national SDG indicator set is modelled... for any of the five
> [original] countries"). Sourced from Destatis's own page, read directly.

## Description

Germany's own indicator set for measuring progress on the **German
Sustainability Strategy**, incorporating "at least one indicator for each
of the 17 [UN Sustainable Development] Goals" — confirmed by reading
destatis.de directly. Unlike [[EU-SDG-INDICATORS]]'s quantified "55 of
100" descent from the UN list, the German set's alignment is described
only qualitatively in the source read this pass: goal-by-goal coverage,
not a counted overlap.

## Maintained independently since 2006

The **Statistisches Bundesamt (Destatis)** — [[DE-DESTATIS]] — has been
tasked "since 2006" with measuring the national indicators "fachlich
unabhängig" (independently, on professional/technical grounds) using its
own official statistics, confirmed by reading the same Destatis page
directly. It publishes a biennial **Indikatorenbericht** for the strategy,
and the underlying data has been available on a dedicated online platform
since **February 2020**.

## One of five, still four to go

`discovery/unresolved.md` row #175 flagged that no national SDG indicator
set was modelled for any of the Atlas's five original countries (Belgium,
Germany, France, the Netherlands, Spain). This closes Germany's. The
other four remain unresearched — this is a first instance, not a
systematic sweep.

## Not modelled

- The **German Sustainability Strategy** itself, as distinct from its
  indicator set — the strategy document and its goal targets were not
  independently researched this pass.
- The **Indikatorenbericht** publications and the **dns-indikatoren.de** /
  **sdg-indikatoren.de** platforms as separate entities.

## Relationships

- `based-on` [[UN-SDG-INDICATORS]] — `confidence: medium`.
- `maintained-by` [[DE-DESTATIS]] — `confidence: high`.

## Sources

Listed in frontmatter — a single source, read directly.
