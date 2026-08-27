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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading forumstandaardisatie.nl directly (2026-08-27): 'Vanaf medio 2020 ligt het beheer van de standaard formeel bij Logius' (since mid-2020 management of the standard formally lies with Logius). gitdocumentatie.logius.nl's own version 1.0 document, also read directly, confirms it is 'published by Logius Standaard,' authored by an API Design Rules Working Group with editors Frank Terpstra and Jan van Gelder from Geonovum, dated 9 July 2020."
    confidence: high
    valid_from: 2020-07-01
    valid_until: null
  - type: part-of
    target: NL-PAS-TOE-OF-LEG-UIT
    source: fact
    evidence: "Confirmed by reading forumstandaardisatie.nl directly (2026-08-27): the standard holds 'Pas toe of leg uit' status, 'making it mandatory for Dutch public sector organizations' when REST APIs are used (it does not itself mandate adopting REST APIs). Current version confirmed as 2.2 on that page; logius-standaarden.github.io's draft page, also read directly, shows a further draft version in development as of July 2026, not yet approved by TO (the standards approval body)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "REST-API Design Rules"
    url: "https://www.forumstandaardisatie.nl/open-standaarden/rest-api-design-rules"
    publisher: "Forum Standaardisatie"
    accessed: "2026-08-27"
  - title: "NLGov REST API Design Rules"
    url: "https://logius-standaarden.github.io/API-Design-Rules/"
    publisher: "Logius"
    accessed: "2026-08-27"
  - title: "REST-API Design Rules (Nederlandse API Strategie IIa) 1.0"
    url: "https://gitdocumentatie.logius.nl/publicatie/api/adr/1.0/"
    publisher: "Logius"
    accessed: "2026-08-27"
  - title: "Handreiking API Design Rules"
    url: "https://www.noraonline.nl/wiki/Handreiking_API_Design_Rules"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-27"
---

# NLGov REST API Design Rules (ADR)

> **Verified 2026-08-27.** All four cited pages were read directly, closing
> both the maintainer date and the current-version gaps. `verification`
> moves from `search-only` to `primary-source`.

## Description

The NLGov REST API Design Rules are a set of agreements developers follow
when building a REST API for the Dutch public sector. Confirmed by reading
forumstandaardisatie.nl directly: they are a mandatory (Pas toe of leg uit)
standard when government uses REST APIs, formally managed by [[NL-LOGIUS]]
**since mid-2020**. The document is the product of an API Design Rules
Working Group — gitdocumentatie.logius.nl's own version 1.0 text, read
directly, names editors Frank Terpstra and Jan van Gelder of [[NL-GEONOVUM]]
and dates that version to **9 July 2020**, licensed under Creative Commons
Attribution 4.0.

The ADR originates from the document *API Strategie voor de Nederlandse
Overheid*, which was split into separate sub-documents; the ADR corresponds
to part IIa of that strategy — confirmed by version 1.0's own text, read
directly, which states the standard was submitted to Forum Standaardisatie
"for inclusion on the Comply or Explain list." **The Nederlandse API
Strategie as a whole is not modelled as a separate entity** — it is a
collection of documents, several of which appear on the comply-or-explain
list. Whether the strategy warrants its own entity, with the ADR as
`part-of` it, is recorded in `discovery/unresolved.md`.

**Version history is now sourced rather than vague.** Confirmed directly:
version 1.0 (9 July 2020) was the original comply-or-explain submission;
the current published version is **2.2** (forumstandaardisatie.nl); a
further draft (dated July 2026 on logius-standaarden.github.io, itself
"could be altered, removed or replaced" and not yet TO-approved) is in
development.

## Relationships

- Maintained by [[NL-LOGIUS]] since mid-2020, confirmed directly with a date.
- Part of the [[NL-PAS-TOE-OF-LEG-UIT]] mandatory standards list, assessed
  through [[NL-FORUM-STANDAARDISATIE]] — confirmed directly.
- Referenced in [[NL-NORA]] guidance — noraonline.nl's own page, read
  directly, describes the ADR's benefits (interoperability, developer
  experience, security) and names supporting tools (ADR Linter, OAS
  Generator) on developer.overheid.nl, without adding new relationship
  facts beyond what is already recorded.

## Sources

Listed in frontmatter, all four read directly this pass.
