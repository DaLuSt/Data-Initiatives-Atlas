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
last_verified: "2026-08-21"
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
    evidence: "UN/CEFACT serves as the focal point within the UN Economic and Social Council for trade facilitation recommendations and electronic business standards, and maintains the UN/EDIFACT standard directories; its work covers standardising and harmonising the core information used in trade documents and electronic business (unece.org/trade/uncefact; unece.org/trade/uncefact/introduction). NOT READ — search-only."
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
---

# UN/EDIFACT

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval of `unece.org`
> is blocked by the network egress proxy. `verification: search-only`.

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
`coverage: low`, one relationship, two sources. It exists because the cluster
is more legible with the two best-known UN/CEFACT outputs in it than with one,
not because a European connection was found for it.

The **Core Component Library** is not created. Nothing beyond a name was
found, and a node built on that would be the thin encyclopedic entity the
taxonomy threshold exists to prevent.

## Relationships

- `maintained-by` [[UN-CEFACT]].

## Sources

Listed in frontmatter — two UNECE pages on UN/CEFACT and its outputs.
