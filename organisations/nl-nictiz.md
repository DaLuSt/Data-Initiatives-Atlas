---
id: NL-NICTIZ
type: organisation
name: Nictiz
alternative_names:
  - Nationaal ICT Instituut in de Zorg
description: >
  Dutch knowledge organisation for digital information provision in
  healthcare, founded in 2002 as a foundation financed almost entirely by
  the Ministry of Health, Welfare and Sport. Nictiz develops and manages
  the information standards that allow health information to be recorded,
  exchanged and reused unambiguously.

level: sectoral
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
organisations: []
related_entities:
  - NL
relationships:
  - type: related-to
    target: NL
    source: fact
    evidence: "Confirmed by reading nictiz.nl's own 'Wat we doen' page directly (2026-08-27): Nictiz develops and manages standards enabling health information to be 'recorded and exchanged unambiguously', working with healthcare organisations, umbrella bodies, ICT suppliers and policymakers. nl.wikipedia.org's Nictiz article, also read directly, confirms Nictiz was established in 2002 (search corroborates 'Stichting NICTIZ', decided 12 November 2001, established 1 January 2002, though the exact founding day is not independently confirmed by the two primary pages read) and is financed by the Ministry of Health, Welfare and Sport (VWS), with a board independent of the ministry. `related-to` and not `part-of`: Nictiz is a foundation, not a body of the Dutch state, so structural containment is not claimed. Anchor edge — added under metadata/relationship-types.md §2.3."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Wat we doen"
    url: "https://www.nictiz.nl/wat-we-doen/"
    publisher: "Nictiz"
    accessed: "2026-08-27"
  - title: "Standaarden voor zorgdata en uitwisseling"
    url: "https://www.nictiz.nl/standaarden/"
    publisher: "Nictiz"
    accessed: "2026-08-27"
  - title: "Zorginformatiestelsel: standaarden en databeschikbaarheid"
    url: "https://www.nictiz.nl/wat-we-doen/zorginformatiestelsel/"
    publisher: "Nictiz"
    accessed: "2026-08-27"
  - title: "Informatiestandaarden: basis voor gegevensuitwisseling in de zorg"
    url: "https://nictiz.nl/app/uploads/2022/08/Informatiestandaarden-basis-voor-gegevensuitwisseling-in-de-zorg.pdf"
    publisher: "Nictiz"
  - title: "Nictiz"
    url: "https://nl.wikipedia.org/wiki/Nictiz"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
---

# Nictiz

> **Verified 2026-08-27.** Four of five cited pages were read directly
> this pass, closing the previous `search-only` status (never previously
> `last_verified`). The 2022 PDF was not re-fetched.

## Description

Nictiz is the Dutch knowledge organisation for digital information
provision in healthcare. It develops and manages the standards that make
health information unambiguously recordable, exchangeable and reusable,
and advises and shares knowledge on digital information provision in
healthcare both domestically and internationally.

**Founding, now sourced.** Previously this entity recorded no founding
information at all. `nl.wikipedia.org`'s own article, read directly,
confirms Nictiz was established in **2002** as a foundation ("stichting"),
financed almost entirely by the **Ministry of Health, Welfare and Sport**
(VWS), with a supervisory board operating independently of the ministry.
`start_date` is left `null`: sources agree on the year but a search turned
up a secondary claim of 1 January 2002 (following a 12 November 2001
decision) that was not independently confirmed by either primary page read
this pass, so only the year is asserted in prose.

Its instrument is the information standard (informatiestandaard): a set of
agreements established with parties from the healthcare sector, acting as a
bridge between care providers, care processes and IT systems. Reading
nictiz.nl's own standards page directly confirms **HL7 FHIR** is listed
among Nictiz's core standards alongside SNOMED and LOINC; HL7 CDA and the
ZIBs (zorginformatiebouwstenen) are confirmed via the "Wat we doen" and
"Zorginformatiestelsel" pages, both read directly, which also describe the
current healthcare information system as needing restructuring for
capacity and affordability reasons — Nictiz frames its architecture work as
addressing that directly.

Nictiz is recorded at `level: sectoral` rather than `national` — it is a
national organisation, but its authority is bounded to the healthcare
sector rather than government-wide, which the `sectoral` level expresses
more accurately.

## Relationships

Tagged [[DOMAIN-HEALTH]]. Nictiz's relationships to HL7 and to the
European Health Data Space remain unassertable — neither is yet an Atlas
entity.

## Sources

Four of five read directly this pass: all three `nictiz.nl` pages plus the
Dutch Wikipedia article (used for the founding-year confirmation). The 2022
information-standards PDF was not re-fetched.
