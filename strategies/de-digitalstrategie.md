---
id: DE-DIGITALSTRATEGIE
type: strategy
name: Digitalstrategie der Bundesregierung
alternative_names:
  - Digitalstrategie Deutschland
  - "Digitalstrategie – Gemeinsam digitale Werte schöpfen"
description: >
  Federal government digital strategy adopted on 31 August 2022 under the
  title "Digitalstrategie – Gemeinsam digitale Werte schöpfen", setting the
  overarching framework for German digital policy to 2025. It sets
  priorities across 25 fields of action, and takes a place in the top ten
  of the European Digital Economy and Society Index (DESI) by 2025 as an
  explicit target.

level: national
country: DE
region: null

status: unknown
confidence: medium
coverage: medium
verification: search-only

start_date: 2022-08-31
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-DATENSTRATEGIE
  - EU-DIGITAL-DECADE
relationships:
  - type: references
    target: EU-DIGITAL-DECADE
    source: interpretation
    evidence: "The strategy sets a target of reaching the top ten of the European Digital Economy and Society Index (DESI) by 2025; DESI is the EU's digital performance index and was integrated into Digital Decade reporting. The strategy's use of DESI as its headline benchmark is sourced (bundesrechnungshof.de; de.wikipedia.org), but no source read states that the strategy references the Digital Decade policy programme itself. Recorded as an Atlas reading."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Digitalstrategie der Bundesregierung — Ausrichtung und Ziele"
    url: "https://www.bundesrechnungshof.de/SharedDocs/Downloads/DE/Berichte/2024/digitalstrategie-volltext.pdf?__blob=publicationFile&v=2"
    publisher: "Bundesrechnungshof"
  - title: "Bulletin der Bundesregierung Nr. 117-1 vom 22. September 2022 — Digitalstrategie"
    url: "https://www.bundesregierung.de/resource/blob/975954/2129092/6877582efe8ae4cd15692dce82494a25/117-1-bmdv-digitalstrategie-bt-data.pdf?download=1"
    publisher: "Presse- und Informationsamt der Bundesregierung"
  - title: "Bundesregierung legt Digitalstrategie vor"
    url: "https://www.bundestag.de/presse/hib/kurzmeldungen-909556"
    publisher: "Deutscher Bundestag"
  - title: "Kritik an schwammigen Zielen der Digitalstrategie"
    url: "https://www.bundestag.de/dokumente/textarchiv/2022/kw38-de-digitalstrategie-909088"
    publisher: "Deutscher Bundestag"
---

# Digitalstrategie Deutschland

> **Sourcing caveat, updated 2026-08-22.** The Bundesrechnungshof's own
> report on the strategy and two Bundestag textarchiv articles were read
> directly (via `pdftotext` for the PDF) and confirmed the claims below,
> including the exact adoption date and the DESI top-ten target. This
> entity stays `verification: search-only` regardless: `tools/reverify.py`
> fetches sources as raw bytes and cannot extract text from a PDF, so it
> cannot corroborate a claim that only the Bundesrechnungshof PDF states
> verbatim, and the entity's exact quoted title doesn't otherwise appear on
> the two HTML sources. Forcing the write past that refusal was
> deliberately not done. The content below is genuinely verified; the
> field is not.

## Description

Confirmed directly in the Bundesrechnungshof's report (2026-08-22): "Die
Bundesregierung beschloss am 31. August 2022 ihre 'Digitalstrategie –
Gemeinsam digitale Werte schöpfen'." On 31 August 2022 the federal
government adopted *Digitalstrategie – Gemeinsam digitale Werte schöpfen*, creating the overarching framework for
German digital policy through 2025. It sets priorities across **25 fields
of action** (Handlungsfelder), with the stated goal of improving the
conditions for digitalisation so that civil society, business, education
and science can better use its opportunities.

Search results describe four areas of concentration: connectivity (5G and
fibre coverage), digital skills in the population, use of digital
technologies and AI in business, and provision of digital public services.

Its headline quantitative target was for Germany to enter the **top ten of
the European Digital Economy and Society Index (DESI) by 2025** —
confirmed verbatim in the Bundesrechnungshof report: "mindestens Platz 10
im DESI-Ranking." Confirmed on bundestag.de's "Kritik an schwammigen
Zielen" article (2026-08-22): then-minister Wissing himself cited Germany's
13th-place DESI standing as unacceptable ("Dass die Bundesrepublik im Index
für die digitale Wirtschaft und Gesellschaft (DESI) auf Platz 13 liege, sei
etwas, das Deutschland sich nicht leisten könne").

## Why `status: unknown`

The strategy set a framework explicitly bounded by the year 2025, and this
entry is written in August 2026. That its period has elapsed is sourced;
what happened to it is not.

The options were each rejected in turn:

- **`completed`** would assert the strategy achieved its aims. Two of the
  cited sources are critical — a Bundesrechnungshof report and a Bundestag
  debate item headed *"Kritik an schwammigen Zielen"* — and a fifth search
  result reports Germany missing core targets. Asserting completion would
  be asserting the opposite of what the sources suggest.
- **`superseded`** would need a successor. Germany has since adopted the
  [[DE-MODERNISIERUNGSAGENDA-BUND]] and created [[DE-BMDS]], but **no
  source read states that either replaces this strategy**, so no
  `successor` is recorded and no `supersedes` relationship is asserted from
  the other side.
- **`active`** would claim a 2022–2025 framework is still running a year
  past its horizon.

`unknown` is the honest remainder. `end_date` is left null rather than set
to a fabricated `2025-12-31`.

## Relationships

The single relationship — `references` [[EU-DIGITAL-DECADE]] — is marked
`source: interpretation` at `confidence: low`. The strategy's use of DESI
as its benchmark is sourced; that DESI sits inside the Digital Decade
policy programme is Atlas knowledge, not a statement in any source read.
It is recorded rather than omitted because it is one of only two EU→DE
policy-level connections available, and it is labelled so a reader can
discount it.

## Sources

Listed in frontmatter.
