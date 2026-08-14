---
id: NL-BOMOS
type: framework
name: Beheer- en OntwikkelModel voor Open Standaarden
alternative_names:
  - BOMOS
description: >
  Dutch model describing a layered set of activities relevant to developing
  and managing open standards. Used by Dutch standards-management
  organisations as a common reference for how a standard should be
  developed, governed and maintained.

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
  - NL-FORUM-STANDAARDISATIE
related_entities:
  - NL-GEONOVUM
relationships:
  - type: derived-from
    target: NL-FORUM-STANDAARDISATIE
    source: fact
    evidence: "BOMOS was developed by the NOiV programme bureau based on an earlier report from the Forum Standaardisatie (ecp.nl; forumstandaardisatie.nl BOMOS presentation). NOT READ — search-only."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Beheer- en OntwikkelModel voor Open Standaarden (BOMOS)"
    url: "https://ecp.nl/beheer-en-ontwikkelmodel-voor-open-standaarden-bomos/"
    publisher: "ECP | Platform voor de InformatieSamenleving"
  - title: "BOMOS: The Foundation 3.0.1"
    url: "https://logius-standaarden.github.io/publicatie/bomos/fundament/en/3.0.1/"
    publisher: "Logius"
  - title: "Het Beheer- en Ontwikkelmodel voor Open Standaarden (BOMOS) — presentatie"
    url: "https://www.forumstandaardisatie.nl/vergaderingen/2022/fs-20220608-5-presentatie-bomos"
    publisher: "Forum Standaardisatie"
  - title: "Beheer- en Ontwikkelmodel voor Open Standaarden Versie 2 — deel 1: de basis"
    url: "https://www.forumstandaardisatie.nl/sites/default/files/BFS/4-basisinformatie/publicaties/BOMOS2-deel-1-(de-basis).pdf"
    publisher: "Forum Standaardisatie"
---

# BOMOS

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

BOMOS is described as a tool for and by the standardisation community: it
sets out a layered set of activities relevant to developing and managing
open standards. In effect it is the Dutch meta-standard — a standard for how
to run a standard — which is why it sits at the centre of several other
Atlas entities rather than at the edge.

It was developed by the NOiV programme bureau on the basis of an earlier
report from [[NL-FORUM-STANDAARDISATIE]], drawing on the experience of
parties including Kennisnet/Edustandaard and [[NL-GEONOVUM]]. Version 3.0.0
was published in 2022, and version 3.0.1 of the "Fundament" is published
under Logius standards.

Its practical force shows in [[NL-GEONOVUM]]'s use: Geonovum applies BOMOS
to every standard it manages in order to guarantee those standards are open
by BOMOS's definition, and has held the Forum Standaardisatie designation
"Excellent management process" (uitstekend beheerproces) for its base
standards since December 2014.

**Maintainer uncertainty.** BOMOS's current custodian is genuinely unclear
from the sources: it originates from a Forum Standaardisatie report, was
built by NOiV (a programme bureau that no longer appears active), is hosted
by ECP, and its current version is published under Logius standards. The
`organisations:` list therefore names both [[NL-LOGIUS]] and
[[NL-FORUM-STANDAARDISATIE]] without asserting a `maintained-by`
relationship to either, and the question is recorded in
`discovery/unresolved.md`.

## Relationships

- Derived from an earlier [[NL-FORUM-STANDAARDISATIE]] report (recorded at
  `confidence: low`; "derived from a report by" is a weaker claim than the
  relationship type suggests).
- Applied by [[NL-GEONOVUM]] to all standards it manages.

## Sources

Listed in frontmatter.
