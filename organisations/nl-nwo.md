---
id: NL-NWO
type: organisation
name: Nederlandse Organisatie voor Wetenschappelijk Onderzoek
alternative_names:
  - NWO
  - Dutch Research Council
  - ZWO
description: >
  Dutch national research funding council, one of the country's most
  important science-funding bodies, investing almost one billion euros
  annually in curiosity-driven research, research related to societal
  challenges, and research infrastructure. It manages nine research
  institutes and facilitates international cooperation, funding more
  than five thousand researchers. It originated in 1950 as ZWO
  (Nederlandse Organisatie voor Zuiver-Wetenschappelijk Onderzoek),
  focused solely on pure scientific research, with applied research
  reserved for TNO. In 1988 its mandate was expanded to include
  strategic and application-oriented research and it was transformed
  into NWO, formalised as a zelfstandig bestuursorgaan under the "Wet
  op de Nederlandse organisatie voor wetenschappelijk onderzoek" of 7
  July 1987, falling under the Ministry of Education, Culture and
  Science.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 1950-01-01
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-RESEARCH
organisations: []
related_entities:
  - NL
  - NL-DANS
relationships:
  - type: part-of
    target: NL
    source: fact
    evidence: "Confirmed by reading nl.wikipedia.org's own NWO article directly (2026-09-04): NWO originated in 1950 as ZWO (Nederlandse Organisatie voor Zuiver-Wetenschappelijk Onderzoek), which did not focus on applied research (reserved for TNO). In 1988 ZWO's mandate expanded to strategic and application-oriented research, prompting the transformation into NWO, formalised under the 'Wet op de Nederlandse organisatie voor wetenschappelijk onderzoek' enacted 7 July 1987, establishing NWO as a zelfstandig bestuursorgaan under the Ministry of Education, Culture and Science (OCW). Corroborated by reading nwo.nl's own 'About NWO' page directly, confirming NWO's current funding role and scale, though that page does not itself state the founding history. OCW is not an Atlas entity, so the anchor edge is asserted at country scope. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: 1950-01-01
    valid_until: null
  - type: cooperates-with
    target: NL-DANS
    source: fact
    evidence: "Confirmed by reading nwo.nl's own page on DANS directly (2026-09-04): DANS operates as an institute of both KNAW and NWO jointly."
    confidence: high
    valid_from: 2005-01-01
    valid_until: null

sources:
  - title: "About NWO"
    url: "https://www.nwo.nl/en/about-nwo"
    publisher: "NWO — Dutch Research Council"
    accessed: "2026-09-04"
  - title: "Nederlandse Organisatie voor Wetenschappelijk Onderzoek"
    url: "https://nl.wikipedia.org/wiki/Nederlandse_Organisatie_voor_Wetenschappelijk_Onderzoek"
    publisher: "Wikipedia (NL)"
    accessed: "2026-09-04"
---

# NWO — Nederlandse Organisatie voor Wetenschappelijk Onderzoek

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged NWO, DANS and RIVM together
> as unresearched since Batch 2. Both cited pages were read directly
> this pass.

## Description

NWO is one of the Netherlands' most important science-funding bodies,
investing almost **one billion euros** annually in curiosity-driven
research, societal-challenge research and research infrastructure. It
manages nine research institutes and funds more than five thousand
researchers.

## From ZWO to NWO

Reading the Dutch Wikipedia article directly: NWO originated in **1950**
as **ZWO** (Nederlandse Organisatie voor Zuiver-Wetenschappelijk
Onderzoek), which deliberately did not fund applied research — that
domain was reserved for **TNO**. In **1988** ZWO's mandate expanded to
include strategic and application-oriented research, prompting its
transformation into NWO. This was formalised under the **"Wet op de
Nederlandse organisatie voor wetenschappelijk onderzoek,"** enacted **7
July 1987**, establishing NWO as a **zelfstandig bestuursorgaan**
(independent administrative body) under the Ministry of Education,
Culture and Science (OCW).

## Joint parent of DANS

NWO jointly runs [[NL-DANS]] together with KNAW, confirmed by reading
`nwo.nl`'s own page on DANS directly.

## Relationships

- `part-of` [[NL]] (anchor edge). OCW is not an Atlas entity, so no
  edge is asserted to it directly.
- `cooperates-with` [[NL-DANS]], which it jointly runs with KNAW.

## Sources

Listed in frontmatter, both read directly this pass.
