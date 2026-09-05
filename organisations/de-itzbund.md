---
id: DE-ITZBUND
type: organisation
name: Informationstechnikzentrum Bund
alternative_names:
  - ITZBund
description: >
  Central IT service provider of the German federal administration.
  Established 1 January 2016 as the first outcome of federal IT
  consolidation, and transformed on 1 January 2021 into an Anstalt des
  öffentlichen Rechts (institution under public law), in the business area
  of the Federal Ministry of Finance. Works across departments federal-wide
  on infrastructure, software development and digital-innovation
  initiatives, and certifies XÖV standard conformity.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2016-01-01
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-XOEV
  - DE-KOSIT
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Anchor edge (metadata/relationship-types.md §2.3): ITZBund is a body of the German federal state. Confirmed by reading itzbund.de's own 'Über uns' page directly (2026-09-05): established 1 January 2016 as a federal authority, transformed 1 January 2021 into an Anstalt des öffentlichen Rechts (institution under public law) in the business area of the Federal Ministry of Finance. No Bundesministerium der Finanzen entity exists yet in the Atlas to carry a more specific `part-of` edge."
    confidence: high
    valid_from: 2016-01-01
    valid_until: null
  - type: applies-to
    target: DE-XOEV
    source: fact
    evidence: "Confirmed already on DE-XOEV's own file, reading itzbund.de directly (2026-08-28): ITZBund certifies XÖV standard conformity, distinct from KoSIT's role of developing and maintaining the standards themselves."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Über das Informationstechnikzentrum Bund"
    url: "https://www.itzbund.de/DE/dasitzbund/ueber-uns/ueber-uns.html"
    publisher: "Informationstechnikzentrum Bund (ITZBund)"
    accessed: "2026-09-05"
---

# Informationstechnikzentrum Bund (ITZBund)

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had named ITZBund alongside Bundesdruckerei
> as unmodelled, noting it was "already cited as a source on
> [[DE-XOEV]]." Its own "Über uns" page was read directly this pass.

## Description

ITZBund is the **central IT service provider of the German federal
administration**. Reading `itzbund.de`'s own page directly: it digitises
government operations across sectors including taxation, customs,
personnel management and security, working across departments for the
entire federal administration — roughly **4,600 employees at 12
locations**, a budget of **€1.59 billion**, managing some 148,000 end
devices and over one million users.

## Establishment and legal form

Confirmed directly: ITZBund was established **1 January 2016**, the first
outcome of IT consolidation at federal level. On **1 January 2021** it was
transformed into an **Anstalt des öffentlichen Rechts** (institution under
public law) — a more autonomous legal form than its original federal-
authority status — remaining in the **business area of the Federal
Ministry of Finance**. No Bundesministerium der Finanzen entity exists yet
in the Atlas, so `part-of` [[DE]] is recorded as an anchor edge rather than
a more specific ministry-level relationship.

## Role in the XÖV standards ecosystem

[[DE-XOEV]]'s own file already established, from the same `itzbund.de`
page read in an earlier pass: ITZBund **certifies XÖV standard
conformity**, distinct from [[DE-KOSIT]]'s role of developing and
maintaining the standards themselves. That relationship is carried
forward here rather than re-derived.

## Relationships

- `part-of` [[DE]] — anchor edge; no Bundesministerium der Finanzen entity
  exists yet to carry a more specific one.
- `applies-to` [[DE-XOEV]] — certifies conformity to the standard.

## Sources

Listed in frontmatter, read directly this pass.
