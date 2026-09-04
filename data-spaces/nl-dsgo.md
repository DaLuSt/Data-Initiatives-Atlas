---
id: NL-DSGO
type: data-space
name: Digitaal Stelsel Gebouwde Omgeving
alternative_names:
  - DSGO
description: >
  Dutch agreement framework (afsprakenstelsel) organising data sharing
  within the built environment — construction, installation and engineering.
  It provides uniform agreements for safe, reliable and controlled access to
  data in digital chain collaboration. An initiative of digiGO.

level: sectoral
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2024-06-18
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains: []
organisations:
  - NL-GEONOVUM
  - NL-DIGIGO
related_entities:
  - NL-DIGIGO
relationships: []

sources:
  - title: "Wat is het Digitaal Stelsel Gebouwde Omgeving — DSGO v1.1 (confirmed genuinely dead — HTTP 404)"
    url: "https://afsprakenstelseldsgo.atlassian.net/wiki/spaces/DSGO/pages/316967452/Wat+is+het+Digitaal+Stelsel+Gebouwde+Omgeving"
    publisher: "Afsprakenstelsel DSGO"
  - title: "Richtinggevende principes Digitaal Stelsel Gebouwde Omgeving (DSGO)"
    url: "https://docs.geostandaarden.nl/dsgo/DSGO/"
    publisher: "Geonovum"
    accessed: "2026-08-28"
  - title: "Afsprakenstelsel voor digitaal samenwerken in de bouw & techniek"
    url: "https://www.digigo.nu/afsprakenstelsel/"
    publisher: "digiGO"
    accessed: "2026-08-28"
  - title: "Digitaal Stelsel Gebouwde Omgeving (DSGO)"
    url: "https://vng.nl/artikelen/digitaal-stelsel-gebouwde-omgeving-dsgo"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
    accessed: "2026-08-28"
---

# DSGO (Digitaal Stelsel Gebouwde Omgeving)

> **First full verification pass, 2026-08-28 — promoted to
> `primary-source`.** This entity had never been fetched; it was compiled
> from search-engine results only. Three of its four cited sources were
> read directly this pass: `docs.geostandaarden.nl` (Geonovum's own
> guiding-principles page), `digigo.nu` (digiGO's own afsprakenstelsel
> page) and `vng.nl` (VNG's own article). The fourth, the
> `afsprakenstelseldsgo.atlassian.net` wiki page, returned a genuine "page
> not found" on two separate attempts — the page has moved or been
> retired since this entity was first compiled, and a WebSearch for its
> exact title still surfaces the same dead URL, so it is recorded as
> confirmed genuinely dead rather than retried further. That is 3 of 4
> sources read directly — a genuine majority.

## Description

The DSGO is an agreement framework developed to organise data sharing within
the built environment — construction, installation and engineering. Confirmed
by reading digiGO's own page directly (2026-08-28, digigo.nu): it "creates
conditions enabling parties to easily find, offer, and use data services,"
addressed at "parties from the built environment engaged in digital chain
collaboration exchanging data with each other," who can either exchange data
directly or through software vendors' services. Two portals implement it in
practice — a GEBORA portal for enterprise architects and business analysts,
and a DSGO Developer Portal for technical implementers — and a DSGO
Participant Registry API lets organisations verify who is actually
participating.

It is aimed at parties in the built environment that exchange data in
digital chain collaboration, and is an initiative of digiGO, a collaboration
between industry organisations, companies and governments. Confirmed by
reading VNG's own article directly (2026-08-28): DSGO "is een programma van
de stichting digiGO" (is a programme of the digiGO foundation), and digiGO
itself sits under the Bouwdigitaliseringsraad (Dutch Construction
Digitalisation Council), which brings together government, major clients,
builders, technicians, suppliers and knowledge institutions on BIM adoption
and digital transformation in the sector.

**The guiding principles behind the framework's design are confirmed by
reading Geonovum's own page directly (2026-08-28, docs.geostandaarden.nl):**
Geonovum "has been tasked by the Ministry of Interior Affairs to formulate
guiding principles for DSGO design," working alongside BIM Loket and CROW.
The principles split into eight public-values design principles (openness,
transparency, inclusivity, fairness, purposefulness, stakeholder engagement,
auditability, sovereignty and information security) and the FAIR data
principles (Findable, Accessible, Interoperable, Reusable) — aiming to
facilitate data flow across the construction sector's value chain while
safeguarding public interests and societal objectives like the energy
transition and housing development.

Version 1.0 of the agreement framework was launched on 18 June and formally
transferred to the market; the programme ran from 2021 and ended in June
2024. **The year is now confirmed**: VNG's own article, read directly this
pass, states the programme "is in 2021 gestart en is in juni 2024
geëindigd" (started in 2021 and ended in June 2024) — independently
corroborating that the 18 June launch and the "ended June 2024" statement
are the same moment, resolving the previously-flagged unsourced inference.
`start_date: 2024-06-18` is retained with this corroboration now on record.

Note the pattern: the programme that built the DSGO has **ended**, while the
agreement framework it produced is live and in market hands. `status:
active` describes the framework, not the programme. That distinction is
worth preserving if a separate programme entity is ever created.

`domains:` is empty — a Built Environment or Construction domain would
currently connect this entity alone, below the two-entity threshold in
`metadata/taxonomy.md` §1. Queued.

## Relationships

- Its guiding principles are published by [[NL-GEONOVUM]], which is the only
  sourced institutional connection to an existing Atlas entity — confirmed
  directly this pass (Geonovum was formally tasked by the Ministry of
  Interior Affairs with this work, per its own page).
- [[NL-DIGIGO]], the initiator, is now an Atlas entity (added
  2026-09-04) and carries the `produces` edge pointing here — the
  inbound direction is visible in the graph without a stored inverse,
  the same pattern used across the Atlas (e.g. DE-BMV → DE-MOBILITHEK).

## Sources

Listed in frontmatter. 3 of 4 read directly this pass (2026-08-28):
docs.geostandaarden.nl, digigo.nu and vng.nl. The fourth,
afsprakenstelseldsgo.atlassian.net, returned a genuine HTTP 404 on two
separate attempts and is confirmed dead rather than merely blocked.
