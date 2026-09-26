---
id: NL-API-STRATEGIE
type: framework
name: API Strategie voor de Nederlandse Overheid
alternative_names:
  - Nederlandse API Strategie
  - NL API Strategy
description: >
  Dutch government API strategy, first published in 2019 by the
  Kennisplatform API's (Knowledge Platform for APIs) with Forum
  Standaardisatie participating in its API Strategy and Policy working
  group. It consists of an informative part covering policy, user needs
  and architecture, and a normative part of design rules and profiles for
  government APIs — split into separate sub-documents, several of which
  (including the NLGov REST API Design Rules) are on the Dutch public
  sector's "pas toe of leg uit" (comply-or-explain) mandatory standards
  list.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2019-01-01
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-ADR
  - NL-FORUM-STANDAARDISATIE
  - NL-GEONOVUM
relationships:
  - type: part-of
    target: NL
    source: fact
    evidence: "NARROWS discovery/unresolved.md row #30. Confirmed by reading forumstandaardisatie.nl's own 'Informatie aanbieden via API's' page directly (2026-09-26): the Kennisplatform API's published the first version of the API Strategie voor de Nederlandse Overheid in 2019, with Forum Standaardisatie 'actief deelnemer' (an active participant) in its API Strategy and Policy working group; the strategy itself is described as 'bestaat uit een informatief deel over beleid, gebruikerswensen, architectuur en een normatief deel met ontwerprichtlijnen voor API's' (consisting of an informative part on policy, user needs, architecture and a normative part with design rules for APIs). docs.geostandaarden.nl's own introductory document, also read directly, independently confirms the strategy is 'further developed and managed by the Knowledge Platform for APIs' and lists its component modules (architecture, user needs, normative standards including the API Design Rules, and modular extensions for geospatial, transport security, access control, naming and hypermedia). Anchor edge under metadata/relationship-types.md §2.3, asserting Dutch national scope via `level: national`, `country: NL`."
    confidence: medium
    valid_from: "2019-01-01"
    valid_until: null

sources:
  - title: "Informatie aanbieden via API's"
    url: "https://www.forumstandaardisatie.nl/onderwerpen/uitwisselingsfundament/informatie-aanbieden-apis"
    publisher: "Forum Standaardisatie"
    accessed: "2026-09-26"
  - title: "API Strategie Algemeen (Inleiding)"
    url: "https://docs.geostandaarden.nl/api/API-Strategie/"
    publisher: "Geonovum / Kennisplatform API's"
    accessed: "2026-09-26"
---

# API Strategie voor de Nederlandse Overheid

> **Created 2026-09-26**, narrowing `discovery/unresolved.md` row #30
> ("Should the Nederlandse API Strategie be its own entity, with the
> ADR `part-of` it?"). Sourced from Forum Standaardisatie's own page and
> the strategy's own introductory document, both read directly. See
> [[NL-ADR]], now updated with a `part-of` edge to this entity.

## Description

The API Strategie voor de Nederlandse Overheid is the Dutch government's
API strategy, first published in **2019** by the **Kennisplatform API's**
(Knowledge Platform for APIs) — a collaboration named on Forum
Standaardisatie's own page as including Forum Standaardisatie itself, the
Chamber of Commerce, VNG Realisatie, [[NL-LOGIUS]], Kadaster and
[[NL-GEONOVUM]].

Confirmed directly on forumstandaardisatie.nl: it "consists of an
informative part about policy, user needs, architecture and a normative
part with design rules for APIs" (translated). The strategy's own
introductory document, read directly, lists its component modules:
architecture and user-needs documents, normative standards (including
[[NL-ADR]], the REST API Design Rules), and modular extensions for
geospatial, transport security, access control, naming conventions and
hypermedia.

## The parent [[NL-ADR]] was missing

[[NL-ADR]]'s own file already stated it "corresponds to part IIa" of this
strategy, and flagged the strategy itself as unmodelled — this entity
closes that gap. [[NL-ADR]] is updated with a `part-of` edge pointing
here.

## Not modelled

- The strategy's other named component standards — the **NL GOV
  Assurance profile for OAuth 2.0**, **OpenID NLGov**, and the **NL GOV
  profile for CloudEvents** — beyond [[NL-ADR]], none is yet researched
  to Atlas standard.
- The **Kennisplatform API's** as a separate organisation entity —
  described here in prose as the strategy's publisher/steward.

## Relationships

- `part-of` [[NL]] (anchor edge, `level: national`).

## Sources

Listed in frontmatter, both read directly.
