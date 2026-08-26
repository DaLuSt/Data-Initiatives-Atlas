---
id: FR-DRM
type: organisation
name: Direction du renseignement militaire
alternative_names:
  - DRM
  - Directorate of Military Intelligence
description: >
  France's military intelligence service, created by Décret n° 92-523 of
  16 June 1992 and attached to the Chief of Staff of the Armed Forces
  (CEMA) within the Ministry of the Armed Forces. It belongs to the
  "premier cercle" of the French intelligence community and is authorised
  to use the intelligence-gathering techniques governed by the law of 24
  July 2015, codified in Book VIII of the Code de la sécurité intérieure.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 1992-06-16
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - FR-LOI-RENSEIGNEMENT-2015
  - FR-DGSE
  - FR-DGSI
  - FR-DRSD
  - FR-CNCTR
relationships:
  - type: governed-by
    target: FR-LOI-RENSEIGNEMENT-2015
    source: fact
    evidence: "Confirmed by reading cnctr.fr's own services page directly (2026-08-26): 'La direction du renseignement militaire a été créée par un décret du 16 juin 1992. Ses missions sont définies aux articles D.3126-10 et D.3126-14 du code de la défense, et son organisation est fixé par l'arrêté du 30 mars 2016' (the DRM was created by a decree of 16 June 1992; its missions are defined at articles D.3126-10 and D.3126-14 of the Code de la Défense, and its organisation set by the order of 30 March 2016). Independently confirmed by afdsd.fr's academic paper, read directly, which cites the exact decree: 'Décret n° 92-523 du 16 juin 1992 portant création de la direction du renseignement militaire (JORF n° 139 du 17 juin 1992, p. 7900)' and confirms the DRM is 'Rattachée au chef d'état-major des Armées (CEMA)' (attached to the Chief of Staff of the Armed Forces). Both sources also note DRM is one of two first-circle services (with TRACFIN) without access to the full range of intelligence-gathering techniques."
    confidence: medium
    valid_from: 2015-07-24
    valid_until: null

sources:
  - title: "Les principaux services de renseignement"
    url: "https://www.cnctr.fr/services-de-renseignement"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
    accessed: "2026-08-26"
  - title: "L'organisation administrative du renseignement en France"
    url: "https://www.afdsd.fr/wp-content/uploads/2023/01/AFDSD916dailly.pdf"
    publisher: "Association française de droit de la sécurité et de la défense (AFDSD)"
    accessed: "2026-08-26"
  - title: "Renseignement : ce qui se cache derrière les sigles des agences"
    url: "https://www.lejdd.fr/Politique/renseignement-ce-qui-se-cache-derrieres-les-sigles-des-agences-3357239"
    publisher: "Le Journal du Dimanche"
---

# Direction du renseignement militaire (DRM)

> **Verified 2026-08-26, and the founding date finally sourced.**
> cnctr.fr's own page and afdsd.fr's academic paper, both read
> directly, independently confirm the DRM was created by **Décret n°
> 92-523 du 16 juin 1992** — the first specific date this entity has
> carried, closing the gap "coverage: low" previously flagged.
> `lejdd.fr` is genuinely bot-walled (403) even with an honest
> User-Agent.

## Description

Confirmed by reading cnctr.fr and afdsd.fr directly (2026-08-26): the
DRM is France's **military intelligence collection** service, created
by decree on **16 June 1992**, attached to the Chief of Staff of the
Armed Forces (CEMA) rather than to a ministry directly, and belonging
to the first circle of the intelligence community.

## Two military services, two different jobs

France fields both halves of the military intelligence function as separate
directorates, and confusing them is easy:

- **DRM** — intelligence *collection* in support of military operations.
- **[[FR-DRSD]]** — *security* of defence personnel, installations and
  industry; counter-intelligence within the defence sphere.

Germany has only the second of these as a distinct body ([[DE-BAMAD]]),
with foreign collection sitting at [[DE-BND]]. Poland has both, as
[[PL-SWW]] and [[PL-SKW]]. The Netherlands and Belgium fuse the two into a
single military service ([[NL-MIVD]], [[BE-ADIV]]).

## `coverage` upgraded from low to medium: the founding decree, found

This was the thinnest of the four French service entities. No page on
the DRM's own site was ever returned by search, and its founding date
was previously unestablished. Reading cnctr.fr's own page and
afdsd.fr's academic paper directly closes that gap: **Décret n° 92-523
du 16 juin 1992** created the DRM, cited by both sources independently
(the second gives the full Journal officiel reference, "JORF n° 139 du
17 juin 1992, p. 7900"). Its internal structure and precise remit
beyond "military intelligence collection" remain unestablished.

The `governed-by` edge is now the firmest of the four: cnctr.fr — the
body that authorises the techniques — names the DRM among the services
that may use them, and adds that DRM and TRACFIN are the two services
without access to the full range of techniques the others have.

## Relationships

- `governed-by` [[FR-LOI-RENSEIGNEMENT-2015]].

## Sources

Listed in frontmatter. `cnctr.fr` and `afdsd.fr` were read directly
this pass; `lejdd.fr` is genuinely bot-walled (403) even with an
honest User-Agent.
