---
id: EU-OPEN-DATA-DIRECTIVE
type: directive
name: Open Data Directive
alternative_names:
  - Directive (EU) 2019/1024
  - PSI Directive
  - Open data richtlijn
description: >
  EU directive on open data and the re-use of public sector information. It
  governs the re-use of existing documents held by public sector bodies and
  public undertakings of the member states, and provides for high-value
  dataset categories to be made available for re-use.

level: regional
country: null
region: EU

status: active
confidence: low
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
  - NL-WHO
  - EU-DIGITAL-OMNIBUS
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "Transposed into Dutch law via the Wet implementatie Open data richtlijn, which amended the Wet hergebruik van overheidsinformatie (rijksoverheid.nl, eerstekamer.nl dossier 36.382). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: DE
    source: fact
    evidence: "The Datennutzungsgesetz implements the requirements of Directive (EU) 2019/1024 and replaced the Informationsweiterverwendungsgesetz; it came into force on 23 July 2021 (de.wikipedia.org 'Datennutzungsgesetz'; bho-legal.com; de.digital). NOT READ — search-only."
    confidence: medium
    valid_from: 2021-07-23
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "As an EU directive it requires transposition by all member states, Belgium included (EUR-Lex Directive (EU) 2019/1024). NOT READ — search-only. NO Belgian transposing instrument is recorded in this Atlas: the Belgian open data act found by search is the wet van 4 mei 2016, which PREDATES this directive and is sourced as aligning with the earlier PSI Directive instead. See BE-HERGEBRUIK-WET."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: FR
    source: fact
    evidence: "As an EU directive it requires transposition by all member states, France included (EUR-Lex Directive (EU) 2019/1024). NOT READ — search-only. NO French transposing instrument is recorded: the French open data act found by search is the loi pour une Republique numerique of 2016, which PREDATES this directive and sits in the earlier PSI lineage. See FR-LRN. France is the second country in this Atlas with this gap, after Belgium."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Directive - 2019/1024 - EN - psi directive"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019L1024"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "Open Data Richtlijn"
    url: "https://europadecentraal.nl/onderwerp/digitale-overheid/privacy/open-data-richtlijn/"
    publisher: "Europa decentraal"
---

# Open Data Directive (Directive (EU) 2019/1024)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Directive (EU) 2019/1024 concerns open data and the re-use of public sector
information. It governs the re-use of existing documents held by public
sector bodies and public undertakings of the member states. Re-use, in the
directive's sense, means public data — usually processed by government
institutions — being used for a purpose other than that for which it was
originally collected.

Its stated aims include stimulating cross-border re-use of public
information, supporting the development of EU-wide goods and services built
on public information, and preventing distortions of competition in
PSI-related activity. It also provides for categories of high-value
datasets.

As a **directive** rather than a regulation, it requires transposition into
national law — which is precisely the distinction `metadata/taxonomy.md` §2
exists to capture. Its Dutch transposition is recorded on [[NL-WHO]].

## ⚠ A repeal has been proposed

[[EU-DIGITAL-OMNIBUS]], the Commission proposal of 19 November 2025, would
**repeal this directive** and transfer its provisions into
[[EU-DATA-ACT]], together with [[EU-DGA]] and the Free Flow of Non-Personal
Data Regulation.

**`status` remains `active`.** The Omnibus is a proposal before the
Parliament and Council, with adoption reported as expected around end-2026.
The relationship is recorded from the Omnibus side using
`proposes-to-supersede`, a type added in Batch 8 so that pending repeals are
visible without falsely retiring the instruments they target.

If adopted, this would also put [[NL-WHO]] — the Dutch transposition — in an
unusual position, since the directive it transposes would cease to exist as
a separate instrument. That consequence is noted, not modelled.

## Scope note

Created in Batch 3 as a minimal anchor to support the transposition chain,
and reviewed in Batch 8. Its substantive content beyond the high-value
dataset regime is still unresearched (`coverage: low`).

## Relationships

- Applies in [[NL]], [[DE]], [[BE]] and [[FR]] — one entity, four
  countries. Every other member state belongs here too; the
  `applies-in` relationships are added as countries join the Atlas.
- Transposed into Dutch law through [[NL-WHO]], as amended by the Wet
  implementatie Open data richtlijn (2024).

## Sources

Listed in frontmatter.
