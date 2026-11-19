---
id: NL-NWO
type: organisation
name: Nederlandse Organisatie voor Wetenschappelijk Onderzoek
name_en: "Dutch Research Council"
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

start_date: null
end_date: null
last_verified: "2026-11-19"
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
    evidence: "Anchor edge under metadata/relationship-types.md §2.3. nwo.nl's own 'Bestuur en organisatie' page, read directly 2026-11-19: 'NWO is een zelfstandig bestuursorgaan met wettelijk vastgelegde taken. De organisatie valt onder de verantwoordelijkheid van het ministerie van Onderwijs, Cultuur en Wetenschap.' OCW is not an Atlas entity, so the anchor is asserted at country scope. The founding history (ZWO in 1950, the 1987 NWO Act) is in the prose and comes from Wikipedia; this edge no longer rests on it (roadmap #767)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: cooperates-with
    target: NL-DANS
    source: fact
    evidence: "Confirmed by reading nwo.nl's own page on DANS directly (2026-09-04): DANS operates as an institute of both KNAW and NWO jointly."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Bestuur en organisatie"
    url: "https://www.nwo.nl/organisatie"
    publisher: "NWO (nwo.nl)"
    accessed: "2026-11-19"
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

## Year only (2026-11-17)

The sources read give the year 1950, not a day. `start_date` was `1950-01-01`, a placeholder for "in 1950" that `metadata/metadata-schema.md` rules out, and is now empty; so are the 1 `valid_from` dates that repeated it. The year stays in the description and the text above.

## Edge dates (2026-11-17)

The `valid_from` of `cooperates-with` [[NL-DANS]] was 2005-01-01, a placeholder for the year 2005 that `metadata/metadata-schema.md` rules out; no source read gives the day, so it is now empty. The year is in the edge's evidence or the text above.

## Sources

Listed in frontmatter, both read directly this pass.
