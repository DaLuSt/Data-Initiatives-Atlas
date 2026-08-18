---
id: FR-DRM
type: organisation
name: Direction du renseignement militaire
alternative_names:
  - DRM
  - Directorate of Military Intelligence
description: >
  France's military intelligence service, attached to the Ministry of the
  Armed Forces. It belongs to the "premier cercle" of the French
  intelligence community and is authorised to use the intelligence-gathering
  techniques governed by the law of 24 July 2015, codified in Book VIII of
  the Code de la sécurité intérieure.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
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
    evidence: "The DRM is attached to the Ministry of Defence and is one of the six services of the first circle of the intelligence community, alongside the DGSE, DGSI, DRSD, DNRED and TRACFIN; the first-circle agencies hold the fullest legal authority to employ intelligence-gathering techniques under the Internal Security Code, as governed by the law of 24 July 2015 (cnctr.fr 'Les principaux services de renseignement'; defense.gouv.fr; afdsd.fr 'L'organisation administrative du renseignement en France'). NOT READ — search-only."
    confidence: medium
    valid_from: 2015-07-24
    valid_until: null

sources:
  - title: "Les principaux services de renseignement"
    url: "https://www.cnctr.fr/services-de-renseignement"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
  - title: "L'organisation administrative du renseignement en France"
    url: "https://www.afdsd.fr/wp-content/uploads/2023/01/AFDSD916dailly.pdf"
    publisher: "Association française de droit de la sécurité et de la défense (AFDSD)"
  - title: "Renseignement : ce qui se cache derrière les sigles des agences"
    url: "https://www.lejdd.fr/Politique/renseignement-ce-qui-se-cache-derrieres-les-sigles-des-agences-3357239"
    publisher: "Le Journal du Dimanche"
---

# Direction du renseignement militaire (DRM)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The DRM is France's **military intelligence collection** service, attached to
the Ministry of the Armed Forces and belonging to the first circle of the
intelligence community.

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

## ⚠ `coverage: low`

This is the thinnest of the four French service entities. No page on the
DRM's own site was returned by search; the entity rests on the CNCTR's list
of intelligence services, an academic paper on the administrative
organisation of French intelligence, and a press explainer. Its founding
date, internal structure and precise remit are all unestablished.

The `governed-by` edge is nonetheless as firm as the other three: the CNCTR
— the body that authorises the techniques — names the DRM among the services
that may use them.

## Relationships

- `governed-by` [[FR-LOI-RENSEIGNEMENT-2015]].

## Sources

Listed in frontmatter.
