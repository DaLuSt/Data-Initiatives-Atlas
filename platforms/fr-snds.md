---
id: FR-SNDS
type: platform
name: Système national des données de santé
alternative_names:
  - SNDS
  - French National Health Data System
description: >
  France's national health data system. Its major strategic orientations are
  set by the State and in particular the health ministry, and are implemented
  by the Plateforme des données de santé. It is the data resource that the
  Plateforme makes available to authorised project holders.

level: national
country: FR
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
organisations: []
related_entities:
  - FR
  - FR-HEALTH-DATA-HUB
relationships:
  - type: part-of
    target: FR
    source: fact
    evidence: "Confirmed by reading drees.solidarites-sante.gouv.fr's own page directly (2026-08-26), the same page read for [[FR-HEALTH-DATA-HUB]]: it describes the Plateforme des données de santé as implementing the strategic orientations the State sets for the Système national des données de santé. `sante.gouv.fr`'s press release remains genuinely blocked by a JavaScript bot-defense challenge regardless of User-Agent. Anchor edge under metadata/relationship-types.md §2.3: a national data system whose orientations are set by the State is part of the state."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Plateforme des données de santé"
    url: "https://drees.solidarites-sante.gouv.fr/sources-outils-et-enquetes/plateforme-des-donnees-de-sante"
    publisher: "DREES — Direction de la recherche, des études, de l'évaluation et des statistiques"
    accessed: "2026-08-26"
  - title: "Le Health Data Hub est officiellement créé — communiqué de presse, 2 décembre 2019"
    url: "https://sante.gouv.fr/IMG/pdf/191202_-_cp_-_health_data_hub.pdf"
    publisher: "Ministère des Solidarités et de la Santé"
---

# SNDS — Système national des données de santé

> **Verified 2026-08-26.** DREES's own page was read directly.
> `sante.gouv.fr`'s press release remains genuinely blocked by a
> JavaScript bot-defense challenge regardless of User-Agent. The
> underlying thinness this entity has always flagged — no source about
> the SNDS itself, only sources about the Plateforme that mention it in
> passing — is unchanged by reading the page; that is a coverage limit,
> not a verification one.

## Description

France's national health data system, and the resource
[[FR-HEALTH-DATA-HUB]] exists to make available. The State — and in
particular the health ministry — sets its **strategic orientations**; the
Plateforme implements them.

## Why this is `coverage: low` and stays that way for now

Everything above comes from sources **about the Plateforme**, which describe
the SNDS only in the course of explaining what the Plateforme does. Nothing
here rests on a source about the SNDS itself.

That means the Atlas does not know, from what it has read, what data the SNDS
holds, what statute created it, who its controller is, or when it started.
Those are the first four things anyone would want, and the entity has none of
them.

**It exists anyway, because the alternative was worse.** Without it,
[[FR-HEALTH-DATA-HUB]]'s relationship to the thing it administers could only
be stated in prose, and the French health layer would have a platform with no
data behind it. A thin node that is honestly labelled thin is better than a
missing one — but it is on the edge of the taxonomy threshold, not clear of
it.

## Relationships

- `part-of` [[FR]] — anchor edge.
- The `governed-by` edge from [[FR-HEALTH-DATA-HUB]] lives on the Plateforme
  and is marked `source: interpretation` there.

## Sources

Listed in frontmatter. `drees.solidarites-sante.gouv.fr` was read
directly this pass and remains, as before, a Plateforme source rather
than an SNDS source — the limitation described above. `sante.gouv.fr`
remains genuinely blocked by a JavaScript challenge.
