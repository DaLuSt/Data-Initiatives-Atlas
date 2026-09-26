---
id: DE-VDE
type: organisation
name: Verband der Elektrotechnik Elektronik Informationstechnik
alternative_names:
  - VDE
  - Association for Electrical, Electronic and Information Technologies
description: >
  German technology association for electrical engineering, electronics
  and information technology, founded in Berlin in January 1893 —
  Germany's oldest electrotechnical association and one of the largest
  technology organisations in Europe, combining standardisation,
  testing, certification and application consulting. Together with DIN,
  it established the Deutsche Kommission Elektrotechnik Elektronik
  Informationstechnik (DKE) in 1970 to combine German electrotechnical
  standardisation work, and holds day-to-day operational and legal
  responsibility for DKE.

level: national
country: DE
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: "1893-01-21"
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-DKE
  - DE-DIN
relationships:
  - type: participates-in
    target: DE-DKE
    source: fact
    evidence: "Closes a gap DE-DKE's own file had flagged ('VDE is not an Atlas entity, so only the DIN half of this joint governance is recorded ... VDE's role is described here in prose'). Confirmed by reading VDE's own 'History' page directly (vde.com/en/about-us/history, 2026-09-26): 'The foundation conference of the VDE takes place in Berlin from January 21 to 22[, 1893]' and, on the same timeline, 'In order to combine electrotechnical standardization work, DIN and VDE establish the \"German Electrotechnical Commission in DIN and VDE\"' (i.e. DKE), with the page separately marking DKE's 50th anniversary in 2020 -- consistent with DE-DKE's own recorded 1970 founding. DE-DKE's own file, already citing din.de directly, states VDE holds 'day-to-day operational and legal responsibility' for DKE -- a substantive governance role, not mere membership, but `participates-in` is used since no source states VDE `governs` or `owns` DKE outright, and DIN remains DKE's own `part-of` anchor on DE-DKE's file."
    confidence: high
    valid_from: "1970-01-01"
    valid_until: null

sources:
  - title: "History of the VDE"
    url: "https://www.vde.com/en/about-us/history"
    publisher: "VDE"
    accessed: "2026-09-26"
---

# Verband der Elektrotechnik Elektronik Informationstechnik (VDE)

> **Created 2026-09-26**, closing a gap [[DE-DKE]]'s own file had
> flagged (graph completion, not a numbered `discovery/unresolved.md`
> row: "VDE is not an Atlas entity"). Sourced from VDE's own official
> history page, read directly.

## Description

VDE is Germany's technology association for electrical engineering,
electronics and information technology — confirmed by reading its own
history page directly: founded at a conference in **Berlin from 21 to
22 January 1893**, making it Germany's oldest electrotechnical
association. It combines standardisation, testing, certification and
application consulting, and is described elsewhere as one of the largest
technology organisations in Europe.

## Co-founder of DKE, and its operational half

The same history page confirms, on its own timeline: "In order to
combine electrotechnical standardization work, DIN and VDE establish the
'German Electrotechnical Commission in DIN and VDE'" — [[DE-DKE]] —
matching that entity's own 1970 founding date (the page separately marks
DKE's 50th anniversary in 2020).

[[DE-DKE]]'s own file, sourced from `din.de` directly, already recorded
that VDE holds **"day-to-day operational and legal responsibility"** for
DKE, while DIN provides its own institutional home. This entity closes
the gap left when that fact could be stated but not linked, because VDE
had no ID of its own.

## Not modelled

- VDE's **membership figures** (reported elsewhere, e.g. "about 36,000
  members including 1,300 companies," but not confirmed by a source read
  directly this pass).
- VDE's **testing and certification arm** (the VDE Institute) as a
  separate entity.

## Relationships

- `participates-in` [[DE-DKE]] — `confidence: high`.

## Sources

Listed in frontmatter, read directly.
