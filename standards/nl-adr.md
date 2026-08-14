---
id: NL-ADR
type: standard
name: NLGov REST API Design Rules
alternative_names:
  - API Design Rules
  - ADR
  - REST-API Design Rules
  - Nederlandse API Strategie IIa
description: >
  Set of design rules that developers follow when building a REST API for
  the Dutch public sector. Part of the Nederlandse API Strategie, managed by
  Logius, and a mandatory standard within Dutch government.

level: national
country: NL
region: null

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
  - NL-LOGIUS
related_entities:
  - NL-PAS-TOE-OF-LEG-UIT
  - NL-FORUM-STANDAARDISATIE
relationships:
  - type: maintained-by
    target: NL-LOGIUS
    source: fact
    evidence: "Logius manages the Design Rules (gitdocumentatie.logius.nl; logius-standaarden.github.io). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-PAS-TOE-OF-LEG-UIT
    source: fact
    evidence: "REST API Design Rules is a mandatory standard within government; it appears in the Forum Standaardisatie open standards register (forumstandaardisatie.nl/open-standaarden/rest-api-design-rules). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "REST-API Design Rules"
    url: "https://www.forumstandaardisatie.nl/open-standaarden/rest-api-design-rules"
    publisher: "Forum Standaardisatie"
  - title: "NLGov REST API Design Rules"
    url: "https://logius-standaarden.github.io/API-Design-Rules/"
    publisher: "Logius"
  - title: "REST-API Design Rules (Nederlandse API Strategie IIa) 1.0"
    url: "https://gitdocumentatie.logius.nl/publicatie/api/adr/1.0/"
    publisher: "Logius"
  - title: "Handreiking API Design Rules"
    url: "https://www.noraonline.nl/wiki/Handreiking_API_Design_Rules"
    publisher: "NORA Online (ICTU)"
---

# NLGov REST API Design Rules (ADR)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The NLGov REST API Design Rules are a set of agreements developers follow
when building a REST API for the Dutch public sector. They are a mandatory
standard within Dutch government, and are managed by [[NL-LOGIUS]]. The
document is the product of an API Design Rules working group rather than of
its named authors alone.

The ADR originates from the document *API Strategie voor de Nederlandse
Overheid*, which was split into separate sub-documents; the ADR corresponds
to part IIa of that strategy. **The Nederlandse API Strategie as a whole is
not modelled as a separate entity** — it is a collection of documents,
several of which appear on the comply-or-explain list. Whether the strategy
warrants its own entity, with the ADR as `part-of` it, is recorded in
`discovery/unresolved.md`.

Multiple versions are in circulation (1.0, 2.0.x), which the Atlas does not
currently distinguish.

## Relationships

- Maintained by [[NL-LOGIUS]].
- Part of the [[NL-PAS-TOE-OF-LEG-UIT]] mandatory standards list, assessed
  through [[NL-FORUM-STANDAARDISATIE]].
- Referenced in [[NL-NORA]] guidance.

## Sources

Listed in frontmatter.
