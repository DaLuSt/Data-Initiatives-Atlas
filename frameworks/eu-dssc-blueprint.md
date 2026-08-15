---
id: EU-DSSC-BLUEPRINT
type: framework
name: DSSC Blueprint
alternative_names:
  - Data Spaces Blueprint
description: >
  Europe's shared reference architecture for building, governing and scaling
  data spaces, published by the Data Spaces Support Centre. It comprises
  business, organisational, legal and technical building blocks, and
  introduces the data space governance framework and rulebook model.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - EU-DSSC
related_entities:
  - EU-COMMON-DATA-SPACES
relationships:
  - type: applies-to
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "The blueprint serves as Europe's shared reference architecture for building, governing and scaling data spaces; the DSSC contributes to the creation of common European data spaces (blueprint.dssc.eu; digital-strategy.ec.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: EU-DSSC
    source: fact
    evidence: "The blueprint serves as Europe's shared reference architecture for building, governing and scaling data spaces, published by the DSSC (blueprint.dssc.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "DSSC Blueprint"
    url: "https://blueprint.dssc.eu/"
    publisher: "Data Spaces Support Centre"
  - title: "DSSC Blueprint — Introduction and key concepts of data spaces"
    url: "https://blueprint.dssc.eu/?intro=introduction-key-concepts-of-data-spaces&pane=intro"
    publisher: "Data Spaces Support Centre"
  - title: "DSSC Blueprint — Technical Building Blocks"
    url: "https://blueprint.dssc.eu/?pane=technical"
    publisher: "Data Spaces Support Centre"
---

# DSSC Blueprint

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The DSSC Blueprint is described as Europe's shared reference architecture
for building, governing and scaling data spaces. It is organised into
building blocks — business and organisational, legal, and technical — and
supplies templates and best practices alongside the architecture itself.

Two concepts from it matter for how the Atlas models data spaces:

- **Data space governance framework** — the structure defining and managing
  the rules of a data space.
- **Rulebook** — the document collecting those rules for a given data
  space, which each participant adheres to.

## The most structurally interesting entity in Batch 10

The Blueprint is the closest EU-level analogue to the Dutch
*afsprakenstelsel* pattern that recurs throughout the Netherlands layer:
[[NL-FDS]], [[NL-DSGO]], [[NL-ISHARE]] and [[NL-HEALTH-RI]] are all
agreement systems with rulebook-like governance. The Blueprint's rulebook
model is what those would map onto in EU terms.

**No relationship to any of them is asserted.** No source connects the Dutch
afsprakenstelsels to the DSSC Blueprint, and the resemblance — however
striking — is an Atlas observation. It is recorded here as such and queued
as a research question, because confirming it would connect the Dutch and EU
data-space layers structurally rather than merely thematically.

Note that [[NL-ISHARE]] already has a documented route into this world: its
trust framework is used by data spaces, and the IDSA has incorporated it
into the IDS architecture. Neither the IDSA nor IDS is an Atlas entity yet,
so that route is also unmodelled.

## Relationships

- Maintained by [[EU-DSSC]].
- Reference architecture for [[EU-COMMON-DATA-SPACES]].

## Atlas interpretation

The parallel between the Blueprint's rulebook model and the Dutch
afsprakenstelsel pattern is an Atlas observation, not a sourced claim.

## Sources

Listed in frontmatter.
