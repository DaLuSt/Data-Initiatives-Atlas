---
id: NL-DIGIGO
type: organisation
name: digiGO
alternative_names:
  - Stichting digiGO
description: >
  Dutch foundation for digital collaboration in the built environment —
  the design, construction and technical (installation) sector — built
  by and for chain partners in that sector. It is the initiator of the
  Bestuursakkoord Digitale Gebouwde Omgeving (Administrative Agreement
  on the Digital Built Environment) and, together with construction-
  sector parties, drew up the policy measures underlying it. It runs
  the Digitaal Stelsel Gebouwde Omgeving (DSGO) as one of its
  programmes.

level: sectoral
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-DSGO
  - NL-GEONOVUM
relationships:
  - type: produces
    target: NL-DSGO
    source: fact
    evidence: "Confirmed by reading digigo.nu's own page directly (2026-09-04): 'digiGO is the initiator of the Administrative Agreement and, together with parties from the construction sector, has drawn up the policy measures underlying the agreement.' NL-DSGO's own entity, verified 2026-08-28, already states in its own words (also from digigo.nu, read directly) that DSGO 'is een programma van de stichting digiGO' (is a programme of the digiGO foundation)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Wat is het Bestuursakkoord Digitale Gebouwde Omgeving '27?"
    url: "https://www.digigo.nu/wat-is-het-bestuursakkoord-27/"
    publisher: "digiGO"
    accessed: "2026-09-04"
---

# digiGO

> **Added 2026-09-04, `verification: primary-source` from creation.**
> [[NL-DSGO]]'s own file had already found and quoted that DSGO "is een
> programma van de stichting digiGO" but could not assert a
> `maintained-by`-style edge because digiGO itself was not yet an Atlas
> entity. `digigo.nu`'s own page was read directly this pass. A 2019
> founding date reported by secondary construction-sector press
> (`bouwendnederland.nl`) was not confirmed by any page read directly
> this pass, so `start_date` is left `null` rather than asserted.

## Description

digiGO is a Dutch foundation ("stichting") for digital collaboration in
the design, construction and technical (installation) sector, built by
and for that sector's chain partners. Reading `digigo.nu`'s own page
directly: **"digiGO is the initiator of the Administrative Agreement
and, together with parties from the construction sector, has drawn up
the policy measures underlying the agreement"** — the Bestuursakkoord
Digitale Gebouwde Omgeving.

## Runs DSGO as a programme

digiGO's own page, combined with [[NL-DSGO]]'s own sourcing, establishes
that the **Digitaal Stelsel Gebouwde Omgeving** is one of digiGO's
programmes, not a separate initiative. [[NL-DSGO]]'s own `related_entities`
and body text can now carry a direct link to this entity rather than
naming digiGO only in prose.

## Relationships

- `produces` [[NL-DSGO]].

## Sources

Listed in frontmatter, read directly this pass.
