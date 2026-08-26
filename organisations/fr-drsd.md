---
id: FR-DRSD
type: organisation
name: Direction du renseignement et de la sécurité de la défense
alternative_names:
  - DRSD
  - Directorate of Intelligence and Defence Security
description: >
  France's defence security and counter-intelligence service, attached to
  the Ministry of the Armed Forces and described by that ministry as the
  intelligence service of the Minister for the Armed Forces. It belongs to
  the "premier cercle" of the intelligence community and is authorised to
  implement all the intelligence-gathering techniques governed by the law of
  24 July 2015.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
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
  - FR-DRM
  - FR-CNCTR
relationships:
  - type: governed-by
    target: FR-LOI-RENSEIGNEMENT-2015
    source: fact
    evidence: "Confirmed by reading defense.gouv.fr's own pages directly (2026-08-26): 'La DRSD (Direction du renseignement et de la sécurité de la Défense) est « le service dont dispose le ministre des Armées pour assumer ses responsabilités en matière de sécurité du personnel, des informations, du matériel et des installations sensibles », selon les termes de l'article D3126-5 du code de la Défense' (the DRSD is the service the Minister of the Armed Forces has for assuming responsibilities over the security of personnel, information, equipment and sensitive installations, per Article D3126-5 of the Code de la Défense) — a precise legal citation this entity did not previously carry. defense.gouv.fr's 'nous-connaitre' page, also read, confirms: 'La DRSD a pour cœur de métier la contre-ingérence (CI) défense. Elle fait partie du premier cercle de la communauté nationale du renseignement' (DRSD's core business is defence counter-intelligence; it is part of the first circle of the national intelligence community). afdsd.fr's academic paper, read for FR-DRM, independently confirms the DRSD was renamed from the DPSD by 'Décret n° 2016-1337 du 7 octobre 2016 portant changement d'appellation' — a renaming history this entity did not previously carry. `drsd.defense.gouv.fr` no longer resolves at all (checked https and http) — a dead domain, not a bot-wall."
    confidence: medium
    valid_from: 2015-07-24
    valid_until: null

sources:
  - title: "Le Service de renseignement du ministre des Armées"
    url: "https://www.defense.gouv.fr/drsd/notre-directeur/service-renseignement-du-ministre-armees"
    publisher: "Ministère des Armées et des Anciens combattants"
    accessed: "2026-08-26"
  - title: "Nous connaître — DRSD"
    url: "https://www.defense.gouv.fr/drsd/nous-connaitre"
    publisher: "Ministère des Armées et des Anciens combattants"
    accessed: "2026-08-26"
  - title: "L'organisation administrative du renseignement en France"
    url: "https://www.afdsd.fr/wp-content/uploads/2023/01/AFDSD916dailly.pdf"
    publisher: "Association française de droit de la sécurité et de la défense (AFDSD)"
    accessed: "2026-08-26"
  - title: "Direction du renseignement et de la sécurité de la Défense"
    url: "https://fr.wikipedia.org/wiki/Direction_du_renseignement_et_de_la_s%C3%A9curit%C3%A9_de_la_D%C3%A9fense"
    publisher: "Wikipédia"
    accessed: "2026-08-26"
  - title: "La direction"
    url: "https://www.drsd.defense.gouv.fr/la-direction"
    publisher: "Direction du renseignement et de la sécurité de la défense (DRSD)"
---

# Direction du renseignement et de la sécurité de la défense (DRSD)

> **Verified 2026-08-26.** defense.gouv.fr's own pages were read
> directly and confirm the exact legal citation (Article D3126-5,
> Code de la Défense) for the first time, plus the DRSD's 2016
> renaming from the DPSD. `drsd.defense.gouv.fr` no longer resolves —
> a dead domain, not a bot-wall — so `defense.gouv.fr/drsd/` pages now
> carry the citation load instead.

## Description

Confirmed by reading defense.gouv.fr directly (2026-08-26): the DRSD is
the **defence security and counter-intelligence** service, described
by the Ministry of the Armed Forces as "le service dont dispose le
ministre des Armées pour assumer ses responsabilités en matière de
sécurité du personnel, des informations, du matériel et des
installations sensibles" (the service the Minister of the Armed Forces
uses to assume responsibility for the security of personnel,
information, equipment and sensitive installations), per **Article
D3126-5 of the Code de la Défense** — a precise legal citation this
entity did not previously carry.

Its counterpart in collection is [[FR-DRM]]; the distinction between the two
is set out there.

## Renamed from the DPSD in 2016

Confirmed by reading afdsd.fr's academic paper directly (2026-08-26):
the DRSD's current name dates only to **Décret n° 2016-1337 du 7
octobre 2016** "portant changement d'appellation de la direction de la
protection et de la sécurité de la défense" — before that date the
same service was the Direction de la protection et de la sécurité de la
défense (DPSD). This entity did not previously record the renaming.

## The clearest statement of the French model in the sources

Of the four French service entities, this is the one whose sources state the
legal position most directly: the DRSD is authorised to implement **all**
the intelligence-gathering techniques governed by the July 2015 law —
a claim CNCTR's own services page (read while researching [[FR-DRM]])
does not contradict, unlike DRM and TRACFIN, which that page names as
the two services without full technique access.

That single sentence is the French pattern in miniature. The law does not
constitute the service or define its mission; it defines a **catalogue of
techniques** and says which services may reach into it. A service's powers
are therefore read off [[FR-LOI-RENSEIGNEMENT-2015]] and its authorisation
regime under [[FR-CNCTR]], not off an organic act of its own.

## Relationships

- `governed-by` [[FR-LOI-RENSEIGNEMENT-2015]].

## Sources

Listed in frontmatter. defense.gouv.fr's two pages and afdsd.fr's
paper were read directly this pass; `drsd.defense.gouv.fr` no longer
resolves at all (checked https and http) — a dead domain, not a
bot-wall.
