---
id: FR-DGSE
type: organisation
name: Direction générale de la Sécurité extérieure
alternative_names:
  - DGSE
  - Directorate-General for External Security
description: >
  France's external intelligence service, placed under the authority of a
  director general reporting to the Minister of the Armed Forces. It belongs
  to the "premier cercle" of the French intelligence community and is
  authorised to use the intelligence-gathering techniques governed by the
  intelligence law of 24 July 2015, codified in Book VIII of the Code de la
  sécurité intérieure.

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
  - FR-DGSI
  - FR-DRM
  - FR-DRSD
  - FR-CNCTR
relationships:
  - type: governed-by
    target: FR-LOI-RENSEIGNEMENT-2015
    source: fact
    evidence: "Confirmed by reading dgse.gouv.fr's own tenth-anniversary page directly (2026-08-26): 'Il y a 10 ans, le 24 juillet 2015, la France s'est dotée d'un cadre juridique afin d'encadrer les activités de ses services de renseignement' (ten years ago, on 24 July 2015, France adopted a legal framework governing its intelligence services' activities), naming the precise codification — 'Art. L. 811-3 du code de la sécurité intérieure (CSI)' for the purposes and 'Titre V du livre VIII du CSI' for the techniques. Confirmed independently by cnctr.fr's own services page, which names DGSE among the six first-circle services. `legifrance.gouv.fr`'s JORF text of the law is genuinely bot-walled (403) even with an honest User-Agent."
    confidence: medium
    valid_from: 2015-07-24
    valid_until: null

sources:
  - title: "10 ans de la loi du 24 juillet 2015 relative au renseignement"
    url: "https://www.dgse.gouv.fr/fr/la-dgse/nos-actualites/10-ans-de-la-loi-du-24-juillet-2015-relative-au-renseignement"
    publisher: "Direction générale de la Sécurité extérieure (DGSE)"
    accessed: "2026-08-26"
  - title: "Les principaux services de renseignement"
    url: "https://www.cnctr.fr/services-de-renseignement"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
    accessed: "2026-08-26"
  - title: "Direction générale de la Sécurité extérieure"
    url: "https://fr.wikipedia.org/wiki/Direction_g%C3%A9n%C3%A9rale_de_la_S%C3%A9curit%C3%A9_ext%C3%A9rieure"
    publisher: "Wikipédia"
    accessed: "2026-08-26"
  - title: "LOI n° 2015-912 du 24 juillet 2015 relative au renseignement"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030931899"
    publisher: "Légifrance / Direction de l'information légale et administrative"
---

# Direction générale de la Sécurité extérieure (DGSE)

> **Verified 2026-08-26.** All three cited pages were read directly.
> DGSE's own page gives a more precise codification than this entity
> previously carried — Article L.811-3 for the purposes and Title V of
> Book VIII for the techniques. `legifrance.gouv.fr` remains genuinely
> bot-walled.

## Description

The DGSE is France's **external** intelligence service, under a director
general reporting to the Minister of the Armed Forces. Its domestic
counterpart is [[FR-DGSI]], under the Minister of the Interior.

## France does not have one act per service

This is the structural difference between France and every other country in
this batch, and it is why all four French service entities carry the *same*
`governed-by` target.

Germany gives each service its own statute ([[DE-BNDG]], [[DE-BVERFSCHG]],
[[DE-MADG]]). The UK gives one act to [[GB-MI5]] and another to
[[GB-SIS]] and [[GB-GCHQ]] jointly. France instead legislated the
**techniques**, not the services: [[FR-LOI-RENSEIGNEMENT-2015]], codified as
Book VIII of the Code de la sécurité intérieure, governs what
intelligence-gathering techniques may be used, by whom, for which purposes
and under what authorisation — and the services are designated as the
bodies permitted to use them.

The consequence for the graph is that the French cluster is a **star** around
one instrument, where the German cluster is a set of parallel pairs. Both are
faithful to their country's law.

## The "premier cercle"

The sources name six services in the first circle: the DGSE, [[FR-DGSI]],
[[FR-DRM]], [[FR-DRSD]], the DNRED (customs intelligence) and TRACFIN
(financial intelligence).

**Only four are modelled.** DNRED and TRACFIN are specialised financial and
customs bodies whose primary function is not intelligence, and neither was
researched. Their absence is a scoping decision, not a finding — the first
circle is six, and the Atlas holds four of them.

## Not modelled

- The **CNRLT** (Coordination nationale du renseignement et de la lutte
  contre le terrorisme), which the sources place around the President of the
  Republic and which coordinates the services.
- The **second circle** of the intelligence community.
- The **decree of 12 May 2014, revised 14 June 2017**, which the sources say
  defines the intelligence community. It is a decree rather than an act and
  was not researched.
- The **law of 30 July 2021** on the prevention of terrorist acts and on
  intelligence, which amended the 2015 regime.

## Relationships

- `governed-by` [[FR-LOI-RENSEIGNEMENT-2015]].

## Sources

Listed in frontmatter, three read directly this pass; `legifrance.gouv.fr`
remains genuinely bot-walled.
