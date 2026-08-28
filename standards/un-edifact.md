---
id: UN-EDIFACT
type: standard
name: United Nations rules for Electronic Data Interchange for Administration, Commerce and Transport
alternative_names:
  - UN/EDIFACT
  - EDIFACT
description: >
  International syntax and message standard for electronic data interchange,
  developed and maintained under the United Nations Economic Commission for
  Europe through UN/CEFACT. It is one of the electronic business standards
  UN/CEFACT produces in pursuit of its stated goal of simple, transparent and
  effective processes for global commerce.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations:
  - UN-CEFACT
related_entities:
  - UN-CEFACT
  - UN-UNECE
  - UN-LOCODE
relationships:
  - type: maintained-by
    target: UN-CEFACT
    source: fact
    evidence: "Both cited unece.org pages returned HTTP 403 again this pass — `unece.org` is blocked domain-wide this session (confirmed by testing the bare root domain). Attempted a source-substitution search per this batch's instruction: Wikipedia's EDIFACT article was fetched directly and confirms 'the ongoing maintenance and development falls under UN/CEFACT..., which operates within the UN Economic Commission for Europe', plus the 1987 ISO 9735 approval date. A second attempted alternate (i-effect.com's EDIFACT glossary entry) also returned HTTP 403 and could not be read. That leaves one genuine alternate read against two original dead sources — not a majority even after substitution, so `verification` stays at `search-only` rather than being forced across the line."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UN/CEFACT — United Nations Centre for Trade Facilitation and Electronic Business"
    url: "https://unece.org/trade/uncefact"
    publisher: "United Nations Economic Commission for Europe"
  - title: "Introducing UN/CEFACT"
    url: "https://unece.org/trade/uncefact/introduction"
    publisher: "United Nations Economic Commission for Europe"
  - title: "EDIFACT"
    url: "https://en.wikipedia.org/wiki/EDIFACT"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# UN/EDIFACT

> **Still `search-only` after this pass — attempted, not forced.**
> `unece.org` is blocked domain-wide this session (confirmed via the bare
> root domain). One alternate, Wikipedia's EDIFACT article, was found and
> read directly, corroborating UN/CEFACT's maintainer role under UNECE and
> adding a genuine new fact (ISO 9735 approval in 1987) not previously
> recorded here. A second alternate attempt (i-effect.com) also 403'd. One
> read source against two still-dead originals is not a majority, so this
> entity is honestly left at `search-only` rather than promoted on a
> single corroborating page — per this batch's own discipline that exactly
> half (or less) is not enough.

## Description

The **United Nations rules for Electronic Data Interchange for
Administration, Commerce and Transport**: the international syntax and
message standard for electronic data interchange, maintained under
[[UN-UNECE]] through [[UN-CEFACT]].

`discovery/candidates.md` §2 listed *"UN/EDIFACT, UN/LOCODE, Core Component
Library"* together as *"the actual UN/CEFACT outputs, and exactly the kind of
artefact this Atlas models. None is an entity; none was researched."* Two of
the three now exist.

## What this entity deliberately does not claim

Unlike [[UN-LOCODE]], **UN/EDIFACT has no edge into the European layer here.**
The searches that found UN/LOCODE named in [[EU-EMSWE]] found no comparable
naming of UN/EDIFACT in an instrument the Atlas holds or could source, and
this entity is therefore attached only to the body that maintains it.

That is a weaker entity than UN/LOCODE and it is recorded as such:
`coverage: low`, one relationship. It exists because the cluster is more
legible with the two best-known UN/CEFACT outputs in it than with one, not
because a European connection was found for it. This pass looked again
(Wikipedia's EDIFACT article, read directly, and an EU-regulation search
targeted at EDIFACT specifically) and still found nothing connecting it to
an EU or national instrument — the asymmetry with [[UN-LOCODE]] holds.

The **Core Component Library** is not created. Nothing beyond a name was
found, and a node built on that would be the thin encyclopedic entity the
taxonomy threshold exists to prevent.

## Relationships

- `maintained-by` [[UN-CEFACT]].

## Sources

Listed in frontmatter. Both UNECE pages remain 403-blocked this session;
Wikipedia's EDIFACT article was read directly as a partial substitute but
is one source against two dead ones, short of the majority needed to
promote `verification`.
