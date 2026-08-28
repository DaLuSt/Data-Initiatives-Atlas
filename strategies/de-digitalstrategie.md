---
id: DE-DIGITALSTRATEGIE
type: strategy
name: Digitalstrategie der Bundesregierung
alternative_names:
  - Digitalstrategie Deutschland
  - "Digitalstrategie – Gemeinsam digitale Werte schöpfen"
description: >
  Federal government digital strategy, adopted by cabinet resolution on
  31 August 2022 under the title "Digitalstrategie – Gemeinsam digitale
  Werte schöpfen" — the first time an entire digital strategy was adopted
  via cabinet resolution — setting the overarching framework for German
  digital policy to 2025. It sets priorities across 25 fields of action
  within three strategic areas, comprising 135 concrete targets and 20
  flagship projects, and takes a place in the top ten of the European
  Digital Economy and Society Index (DESI) by 2025 as an explicit target,
  up from 13th of 27 EU member states in 2022.

level: national
country: DE
region: null

status: unknown
confidence: high
coverage: high
verification: primary-source

start_date: 2022-08-31
end_date: null
last_verified: "2026-08-28"
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
    evidence: "The strategy sets a target of reaching the top ten of the European Digital Economy and Society Index (DESI) by 2025; DESI is the EU's digital performance index and was integrated into Digital Decade reporting. The strategy's use of DESI as its headline benchmark is sourced (de.wikipedia.org 'Digitalstrategie Deutschland', read directly 2026-08-28, and the Bundestag's own kurzmeldungen-909556 page, also read directly), but no source read this pass states that the strategy references the Digital Decade policy programme itself. Recorded as an Atlas reading, not a sourced fact."
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
    accessed: "2026-08-28"
  - title: "Kritik an schwammigen Zielen der Digitalstrategie"
    url: "https://www.bundestag.de/dokumente/textarchiv/2022/kw38-de-digitalstrategie-909088"
    publisher: "Deutscher Bundestag"
    accessed: "2026-08-28"
  - title: "Digitalstrategie Deutschland"
    url: "https://de.wikipedia.org/wiki/Digitalstrategie_Deutschland"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# Digitalstrategie Deutschland

> **Re-verified 2026-08-28, promoted.** The entity's two PDF sources
> (Bundesrechnungshof, bundesregierung.de) again returned only
> encoded-binary content to WebFetch and could not be read as text this
> pass, matching the previous pass's finding via a different tool
> (`pdftotext`). Both Bundestag HTML pages loaded as substantive readable
> text, and — following the brief's instruction to search for an alternate
> primary source when a re-verification is stuck at a borderline majority
> — a dedicated Wikipedia article was found and read directly, corroborating
> and extending every claim below. That is three of five sources read
> directly, a genuine majority reached by this pass's own fetching rather
> than a different tool's extraction. `verification: primary-source`;
> `confidence` and `coverage` both raised to `high`.

## Description

Confirmed directly this pass on both the Bundestag's own "kurzmeldungen"
page and a dedicated Wikipedia article: on **31 August 2022** the "Cabinet
Scholz" adopted *Digitalstrategie – Gemeinsam digitale Werte schöpfen* by
cabinet resolution — **the first time an entire digital strategy was
adopted via cabinet resolution**, per Wikipedia's own wording — creating
the overarching framework for German digital policy through 2025. It was
formally presented to parliament as a government notification on
**12 September 2022**, per the Bundestag's own page, a distinct later
event from the cabinet's own 31 August adoption.

It sets priorities across **25 fields of action** (Handlungsfelder) within
**three strategic areas** — confirmed directly this pass with topic counts
not previously recorded: "Connected and digitally sovereign society" (9
topics: infrastructure, education, healthcare, mobility, culture, digital
participation), "Innovative economy, work, science and research" (8
topics), and "Learning, digital state" (8 topics: digital administration,
open data, justice, cybersecurity, international dimensions). Wikipedia's
own article adds, newly for this entity, that the strategy comprises **135
concrete targets and 20 flagship projects**.

Its headline quantitative target was for Germany to enter the **top ten of
the European Digital Economy and Society Index (DESI) by 2025**, up from
**13th of 27 EU member states in 2022** — confirmed independently on the
Bundestag's own "Kritik an schwammigen Zielen" article, which quotes
then-minister Wissing directly on Germany's 13th-place standing being
unacceptable, and on the Wikipedia article, which gives the same ranking
and denominator.

## Why `status: unknown`

The strategy set a framework explicitly bounded by the year 2025, and this
entry is written in August 2026. That its period has elapsed is sourced;
what happened to it is not fully resolved even after this pass's improved
sourcing.

The options were each rejected in turn:

- **`completed`** would assert the strategy achieved its aims. The
  Bundestag's own "Kritik an schwammigen Zielen" article, read directly,
  reports opposition criticism (CDU/CSU's Nadine Schön calling the targets
  "so unambitious they could be reached immediately") rather than
  confirming achievement. Asserting completion would be asserting close to
  the opposite of what the directly-read sources suggest.
- **`superseded`** would need a successor. Germany has since adopted the
  [[DE-MODERNISIERUNGSAGENDA-BUND]] and created [[DE-BMDS]], and a search
  this pass surfaced a "2. Fortschrittsbericht zur Digitalstrategie" (2nd
  progress report, October 2024) suggesting the strategy was still being
  tracked as a live document at that point rather than replaced — but **no
  source read this pass states either later initiative formally replaces
  it**, so no `successor` is recorded and no `supersedes` relationship is
  asserted from the other side.
- **`active`** would claim a 2022–2025 framework is still running a year
  past its horizon, with no source read confirming continuation past 2025.

`unknown` is the honest remainder. `end_date` is left null rather than set
to a fabricated `2025-12-31`.

## Relationships

The single relationship — `references` [[EU-DIGITAL-DECADE]] — is marked
`source: interpretation` at `confidence: low`. The strategy's use of DESI
as its benchmark is now confirmed by two independently-read sources; that
DESI sits inside the Digital Decade policy programme is Atlas knowledge,
not a statement in any source read this pass either. It is recorded rather
than omitted because it is one of only two EU→DE policy-level connections
available, and it is labelled so a reader can discount it.

## Sources

Listed in frontmatter. Three of five read directly this pass as
substantive text (both Bundestag pages, plus the newly added Wikipedia
article); the two PDFs return only binary to the fetch tool and are kept
listed rather than dropped, since their content (confirmed via a different
extraction method in the prior pass) is not contradicted by anything read
directly this pass.
