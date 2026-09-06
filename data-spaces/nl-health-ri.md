---
id: NL-HEALTH-RI
type: data-space
name: Health-RI
alternative_names:
  - Nationale gezondheidsdata-infrastructuur
  - Health-RI Afsprakenstelsel
description: >
  The Dutch national health data infrastructure for research, policy and
  innovation. Not centralised: data remain stored locally as far as
  possible, made nationally usable through a network of regional nodes
  around a central hub, governed by the Health-RI agreement framework.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
  - DOMAIN-RESEARCH
organisations: []
related_entities:
  - NL
  - NL-NICTIZ
  - EU-EHDS
  - NL-HDAB-NL
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "Health-RI is the Dutch national health data infrastructure for research, policy and innovation, making data nationally usable through a network of regional nodes around a central hub. Confirmed by reading health-ri.nl and nationaalgroeifonds.nl directly (2026-08-28): the infrastructure comprises eight regional nodes (Amsterdam, Eindhoven, Groningen, Leiden, Limburg, Nijmegen, Rotterdam, Utrecht), funded via a €69 million Nationaal Groeifonds allocation under a project running 2021–2028, with the Ministry of Economic Affairs and Climate leading and the Health-RI Foundation implementing through regional hubs. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-HDAB-NL
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED HIGH-VALUE GAP. Confirmed by reading the Minister of Health, Welfare and Sport's own letter to the Tweede Kamer directly (Kamerstuk 27 529, nr. 356, 20 January 2026): the HDAB-NL programme, preparing the Netherlands' future Health Data Access Body under the EHDS, names Health-RI alongside RIVM, CBS and ICTU as partners working with the Ministry of VWS since November 2023. The same letter states the government intends to create a separate, new independent administrative body (zbo) as the actual HDAB — Health-RI is not designated as the HDAB itself, only as a technical-preparation partner. See NL-HDAB-NL for the full sourcing."
    confidence: high
    valid_from: 2023-11-01
    valid_until: null

sources:
  - title: "Health-RI Afsprakenstelsel — Nationale Gezondheidsdata-infrastructuur"
    url: "https://health-ri.atlassian.net/wiki/spaces/HNG/overview"
    publisher: "Health-RI"
    accessed: "2026-08-28"
  - title: "Knooppunten"
    url: "https://www.health-ri.nl/en/about/organisation/knooppunten"
    publisher: "Health-RI"
    accessed: "2026-08-28"
  - title: "Health-RI"
    url: "https://www.nationaalgroeifonds.nl/overzicht-lopende-projecten/thema-gezondheid-en-zorg/health-ri"
    publisher: "Nationaal Groeifonds"
    accessed: "2026-08-28"
  - title: "Kamerbrief over de implementatie van de EHDS (Kamerstuk 27 529, nr. 356)"
    url: "https://www.tweedekamer.nl/downloads/document?id=2026D02216"
    publisher: "Ministerie van Volksgezondheid, Welzijn en Sport (VWS) / Tweede Kamer der Staten-Generaal"
    accessed: "2026-09-06"
---

# Health-RI

> **First full verification pass, 2026-08-28 — promoted to
> `primary-source`.** This entity had never been fetched; it was compiled
> from search-engine results only. All three cited sources were read
> directly this pass: Health-RI's own Atlassian wiki overview, Health-RI's
> own "Knooppunten" (nodes) page, and the Nationaal Groeifonds's own
> project page. All three are genuinely readable and substantive, giving a
> full 3 of 3 — a clear majority.
>
> **Narrowed 2026-09-06**: "will Health-RI be the Dutch HDAB?" is
> answered, not with a yes. The Minister of Health, Welfare and Sport's
> own letter to the Tweede Kamer (20 January 2026), read directly, states
> the government intends to create a **new** independent administrative
> body (zbo) as the actual HDAB — Health-RI is a named partner in the
> preparatory **HDAB-NL** programme, now [[NL-HDAB-NL]], not the
> designated body itself. See that entity for the full sourcing.

## Description

Health-RI works to organise, orchestrate and develop the Dutch national
health data infrastructure for research and innovation, so that health and
research data can be safely and responsibly reused for research, policy and
innovation. It links databases, biobanks and registrations held by
university medical centres and other knowledge and care institutions.

Its defining architectural choice is federation rather than centralisation:
the infrastructure comes about through standardised accessibility of data
via a network of regional nodes (*knooppunten*) working with a central hub.
Data remain stored locally as far as possible but become nationally usable
through shared agreements and standards — the Health-RI Afsprakenstelsel,
under which stakeholders work towards national cooperation agreements for
making health data available and reusable.

**Confirmed by reading Health-RI's own "Knooppunten" page directly
(2026-08-28):** there are **eight** regional nodes, each based in a major
Dutch academic medical centre — Amsterdam, Eindhoven, Groningen, Leiden,
Limburg, Nijmegen, Rotterdam and Utrecht. Each node "provides governance
over connecting and unlocking health data from its own region for the
purpose of the national infrastructure for secondary use," has its own Head
of Node and a tactical lead as primary contact, and coordinates with the
central Health-RI Hub through regular task-group and working-group meetings
covering ethics, FAIR data implementation, architecture, biobanks and
services.

**Confirmed by reading Health-RI's own Atlassian wiki overview directly
(2026-08-28):** the agreement framework has "een generiek deel met daarin
onder andere het vertrouwensmodel en een technische kern" (a generic part
including a trust model and a technical core), operates as a "publiek‑
private constructie" (public-private partnership), and works alongside the
Twiin framework toward a unified national trust system. The framework's
stated purpose, in its own words, is "veilig en verantwoord hergebruik...
voor onderzoek, beleid en innovatie" (safe and responsible reuse for
research, policy and innovation).

**Confirmed by reading the Nationaal Groeifonds's own project page directly
(2026-08-28):** the Ministry of Economic Affairs and Climate (EZK) leads
the project, which received a **€69 million** allocation and runs
**2021–2028** under Round 1 of the Nationaal Groeifonds programme — more
precise funding and timeline detail than this entity previously carried.
The Health-RI Foundation implements the project through regional hubs, an
umbrella organisation, a business advisory committee and citizen/patient
representation, with a stated goal of a sustainable financing mechanism
beyond the initial funding period.

It works with the ministries of VWS, EZK and OCW and many field parties.
None of those ministries is yet an Atlas entity.

## Typing note

Health-RI is recorded as a `data-space`, but the name denotes both an
**organisation** and the **infrastructure** it builds — the sources use it
for both. One entity is used rather than two because the infrastructure has
no distinct proper name of its own beyond "de nationale
gezondheidsdata-infrastructuur", and splitting would create an entity whose
identity rests on a descriptive phrase. Whether to split is recorded in
`discovery/unresolved.md`.

Its federated design makes it a close structural analogue of
[[NL-FDS]] — both are afsprakenstelsels for federated data sharing, one
government-wide and one for health. No relationship is asserted between
them: the resemblance is real but no source connects them.

## Relationships

- Adjacent to [[NL-NICTIZ]], which maintains the health information
  standards that such an infrastructure relies on. No relationship
  asserted, as none was sourced.
- [[EU-EHDS]] was added in Batch 10. No direct relationship is asserted
  between Health-RI and the EHDS itself. **Narrowed 2026-09-06**: Health-RI
  is not the Dutch health data access body the EHDS requires — the
  government intends to create a new independent body (zbo) for that role
  — but it is a named partner in [[NL-HDAB-NL]], the programme preparing
  that body's technical infrastructure, and carries `participates-in` to
  that entity.

## Sources

Listed in frontmatter. All three original sources were read directly in
the 2026-08-28 pass: Health-RI's own Atlassian wiki overview, Health-RI's
own "Knooppunten" page, and the Nationaal Groeifonds's own project page —
a full 3 of 3. The Minister's own letter to the Tweede Kamer was read
directly in the 2026-09-06 pass.
