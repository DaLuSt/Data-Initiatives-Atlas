---
id: DE-NFDI
type: organisation
name: Nationale Forschungsdateninfrastruktur e.V.
alternative_names:
  - NFDI
  - National Research Data Infrastructure (Germany)
description: >
  German national research data infrastructure, established in October
  2020 as a non-profit association (NFDI e.V.) based in Karlsruhe, with
  the federal government and all 16 Länder as founding members. It is a
  federation of 26 funded discipline-specific consortia plus the
  Base4NFDI shared services, drawing over 300 member institutions, and is
  funded through the Deutsche Forschungsgemeinschaft (up to roughly €85
  million per year during the development phase, with continuation funding
  of up to €98.7 million per year agreed for 2029-2038). It coordinates the
  development of research data infrastructures and services and the
  standardisation of research data management in Germany, with the stated
  mission of making research data findable, accessible, interoperable and
  reusable across disciplines. NFDI e.V. is a Mandated Organisation member
  of the EOSC Association.

level: national
country: DE
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2020-10-01
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-RESEARCH
organisations: []
related_entities:
  - DE
  - EU-EOSC
  - NL-SURF
relationships:
  - type: related-to
    target: DE
    source: fact
    evidence: "Confirmed by reading nfdi.de's own homepage and association page directly (2026-08-28): NFDI e.V. was established in October 2020 as a non-profit association based in Karlsruhe, with the federal government and all 16 German states as founding members, and over 300 member institutions. dfg.de's own funding-initiative page, also read directly, confirms DFG and Germany's Joint Science Conference jointly govern the funding, with up to roughly €85 million per year (of which about 22% is indirect programme allowance) supporting 26-27 consortia during the development phase. Anchor edge under metadata/relationship-types.md §2.3: a registered association (e.V.) funded by but not part of the state takes `related-to`, the same treatment NL-SURF and NL-NICTIZ have."
    confidence: high
    valid_from: 2020-10-01
    valid_until: null
  - type: participates-in
    target: EU-EOSC
    source: fact
    evidence: "Confirmed by reading eosc.eu's own members page directly (2026-08-28): 'Nationale Forschungsdateninfrastruktur (NFDI) e.V.' is listed with 'Mandated Organisation' status in the EOSC Association, with named delegate (York Sure-Vetter) and deputy delegate (Wilma Wolf), described as 'a service provider for research' based in Germany."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "NFDI — Nationale Forschungsdateninfrastruktur e.V."
    url: "https://www.nfdi.de/?lang=en"
    publisher: "Nationale Forschungsdateninfrastruktur e.V."
    accessed: "2026-08-28"
  - title: "Association | NFDI"
    url: "https://www.nfdi.de/association/?lang=en"
    publisher: "Nationale Forschungsdateninfrastruktur e.V."
    accessed: "2026-08-28"
  - title: "National Research Data Infrastructure"
    url: "https://www.dfg.de/en/research-funding/funding-initiative/nfdi"
    publisher: "Deutsche Forschungsgemeinschaft (DFG)"
    accessed: "2026-08-28"
  - title: "Nationale Forschungsdateninfrastruktur (NFDI) e.V. — EOSC Association member"
    url: "https://eosc.eu/members/nationale-forschungsdateninfrastruktur-nfdi-ev"
    publisher: "EOSC Association"
    accessed: "2026-08-28"
---

# NFDI — Nationale Forschungsdateninfrastruktur

> **Re-verified 2026-08-28.** All four cited pages read directly.
> `verification: primary-source`; `confidence` raised to `high`; the
> founding date, previously unrecorded, is now sourced to the month.

## Description

Germany's national research data infrastructure: established in **October
2020** as the non-profit association **NFDI e.V.**, based in **Karlsruhe**
— confirmed directly this pass on nfdi.de's own pages, which also confirm
the **federal government and all 16 Länder are founding members** and that
over **300 institutions** now participate. It is a federation of **26
funded discipline-specific consortia** (six in humanities/social sciences,
five in engineering, eight in life sciences, seven in natural sciences)
plus the **Base4NFDI** shared services.

Funding runs through the **DFG**: dfg.de's own page, read directly, gives
up to roughly **€85 million per year** during the development phase (about
22% of which is an indirect programme allowance), with individual consortia
typically receiving €2-5 million each, and the DFG and Germany's Joint
Science Conference jointly deciding awards. nfdi.de's own homepage,
read directly, adds a previously-unrecorded fact: a July 2024 Joint Science
Conference agreement approved **continuation funding of up to €98.7 million
per year for 2029-2038**.

Its mission is stated in FAIR terms — research data findable, accessible,
interoperable and reusable across disciplines. Its governance runs through
five bodies — General Assembly, Board of Trustees, Scientific Senate,
Consortia Assembly and Directorate — confirmed directly this pass on
nfdi.de's own association page, which also names the current leadership
(Prof. Dr. York Sure-Vetter as director).

## The second country in `DOMAIN-RESEARCH`

Before 2026-08-21 the domain reached **one** country: the Netherlands, through
[[NL-TNO]] and [[NL-SURF]]. That was true in an Atlas that holds
[[EU-EOSC]], the European Open Science Cloud.

NFDI closes it at the level that matters, because the connection is
**sourced**, and this pass strengthens the sourcing further: eosc.eu's own
members page, read directly, confirms NFDI e.V. holds **"Mandated
Organisation"** status in the EOSC Association, with a named delegate and
deputy delegate — a more specific membership category than the generic
"member" the entity previously recorded.

## Why `related-to` and not `part-of`

NFDI is an **e.V.** — a registered association — funded by the state but not
part of it, even though the state (federal government plus all 16 Länder)
are its founding members. `metadata/relationship-types.md` §2.3 is explicit
that a national body which is not part of the state takes `related-to`, and
names [[NL-SURF]] and [[NL-NICTIZ]] as the precedent. NFDI is the same
shape as SURF: a member-driven body carrying national infrastructure.

## The federal structure is visible and not modelled

26 consortia, funded jointly by the **Bund and the Länder**, with all
16 Länder as founding association members — confirmed directly this pass,
sharper than the earlier "funded jointly" description. Neither the
consortia nor the Länder themselves have an entity: `level: subnational`
exists in the vocabulary, and nothing in this entity uses it, because no
source here names individual Länder roles beyond "founding member."

## Relationships

- `related-to` [[DE]] — anchor edge, confirmed directly this pass with a
  precise founding date, `confidence: high`.
- `participates-in` [[EU-EOSC]] — confirmed directly this pass as a
  "Mandated Organisation," `confidence: high`.

## Sources

Listed in frontmatter — NFDI's own site and association page, the DFG
funding page, and the EOSC Association's member record, all read directly
this pass.
