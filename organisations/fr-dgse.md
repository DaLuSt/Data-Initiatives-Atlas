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
  - FR-DGSI
  - FR-DRM
  - FR-DRSD
  - FR-CNCTR
relationships:
  - type: governed-by
    target: FR-LOI-RENSEIGNEMENT-2015
    source: fact
    evidence: "The first-circle agencies — DGSE, DGSI, DRM, DRSD, DNRED and TRACFIN — hold the fullest legal authority to employ intelligence-gathering techniques under the Internal Security Code, and are authorised to implement the techniques governed by the intelligence law of July 2015; the DGSE marked ten years of the law of 24 July 2015 on its own site (dgse.gouv.fr '10 ans de la loi du 24 juillet 2015 relative au renseignement'; cnctr.fr 'Les principaux services de renseignement'; legifrance.gouv.fr JORFTEXT000030931899). NOT READ — search-only."
    confidence: medium
    valid_from: 2015-07-24
    valid_until: null

sources:
  - title: "10 ans de la loi du 24 juillet 2015 relative au renseignement"
    url: "https://www.dgse.gouv.fr/fr/la-dgse/nos-actualites/10-ans-de-la-loi-du-24-juillet-2015-relative-au-renseignement"
    publisher: "Direction générale de la Sécurité extérieure (DGSE)"
  - title: "Les principaux services de renseignement"
    url: "https://www.cnctr.fr/services-de-renseignement"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
  - title: "LOI n° 2015-912 du 24 juillet 2015 relative au renseignement"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030931899"
    publisher: "Légifrance / Direction de l'information légale et administrative"
  - title: "Direction générale de la Sécurité extérieure"
    url: "https://fr.wikipedia.org/wiki/Direction_g%C3%A9n%C3%A9rale_de_la_S%C3%A9curit%C3%A9_ext%C3%A9rieure"
    publisher: "Wikipédia"
---

# Direction générale de la Sécurité extérieure (DGSE)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

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

Listed in frontmatter.
