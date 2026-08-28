---
id: EU-DSSC-BLUEPRINT
type: framework
name: DSSC Blueprint
alternative_names:
  - Data Spaces Blueprint
description: >
  Europe's shared reference architecture for building, governing and scaling
  data spaces, published by the Data Spaces Support Centre (DSSC), which is
  funded under the EU's Digital Europe Programme (grant agreement
  101083412). It comprises business, governance, legal and technical
  building blocks, and introduces the data space governance framework and
  rulebook model.

level: regional
country: null
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading blueprint.dssc.eu's own home page directly (2026-08-28): the Blueprint 'serves as Europe's shared reference architecture for building, governing and scaling data spaces,' supports alignment with EU regulations (Data Act, Data Governance Act), and facilitates interoperability between different data space initiatives — the same programme this Atlas records as EU-COMMON-DATA-SPACES."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: EU-DSSC
    source: fact
    evidence: "Confirmed by reading blueprint.dssc.eu's own home page directly (2026-08-28): the Blueprint is published by the Data Spaces Support Centre (DSSC), which is funded under the EU's Digital Europe Programme (grant agreement nº 101083412)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "DSSC Blueprint"
    url: "https://blueprint.dssc.eu/"
    publisher: "Data Spaces Support Centre"
    accessed: "2026-08-28"
  - title: "DSSC Blueprint — Introduction and key concepts of data spaces"
    url: "https://blueprint.dssc.eu/?intro=introduction-key-concepts-of-data-spaces&pane=intro"
    publisher: "Data Spaces Support Centre"
    accessed: "2026-08-28"
  - title: "DSSC Blueprint — Technical Building Blocks"
    url: "https://blueprint.dssc.eu/?pane=technical"
    publisher: "Data Spaces Support Centre"
    accessed: "2026-08-28"
---

# DSSC Blueprint

> **Re-verified 2026-08-28.** All three cited `blueprint.dssc.eu` pages
> were read directly. `verification` promoted `search-only` →
> `primary-source`; `confidence` moves `medium` → `high` for the entity and
> for the `maintained-by` edge, since the DSSC's identity and EU funding
> are now confirmed from the Blueprint's own text.

## Description

Confirmed by reading blueprint.dssc.eu's own home page directly
(2026-08-28): the DSSC Blueprint is Europe's shared reference architecture
for building, governing and scaling data spaces, representing the
consolidated knowledge of the [[EU-DSSC|Data Spaces Support Centre]] — an
organisation funded under the EU's Digital Europe Programme (grant
agreement nº 101083412). It is organised into **business**, **governance**
and **legal** building blocks, plus **technical** building blocks
specifying open standards and protocols, and supplies templates and best
practices alongside the architecture itself. It is also stated to support
alignment with EU regulations including the Data Act and Data Governance
Act.

Two concepts from it matter for how the Atlas models data spaces, both
confirmed by reading the Blueprint's "Introduction and key concepts" page
directly:

- **Data space governance framework** — the structure defining and managing
  the rules of a data space; a data space itself is defined there as "an
  interoperable framework, based on common governance principles,
  standards, practices and enabling services, that enables trusted data
  transactions between participants."
- **Rulebook** — the document produced by that framework, specifying the
  legal, business and technical requirements participants must follow
  (semantic standards, cost-sharing arrangements, required contracts,
  decision-making procedures). A participant may hold membership in
  several data spaces at once, each governed by its own rulebook, and
  rulebooks may reference or connect to one another. A **Data Space
  Governance Authority** administers the rulebook.

Confirmed by reading the "Technical Building Blocks" page directly: this
building block covers data models and vocabulary services, data exchange
protocols, provenance/traceability (W3C standards), metadata description
via DCAT, and publication/discovery mechanisms — the closest point of
contact with [[EU-DCAT-AP]], though no source read states a relationship
between the two entities and none is asserted here.

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

Listed in frontmatter, all three read directly this pass (2026-08-28).
