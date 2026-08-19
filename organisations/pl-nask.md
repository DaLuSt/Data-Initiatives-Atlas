---
id: PL-NASK
type: organisation
name: Naukowa i Akademicka Sieć Komputerowa
alternative_names:
  - NASK
  - NASK — Państwowy Instytut Badawczy
  - Research and Academic Computer Network
description: >
  Polish state research institute, data network operator and registry
  operator for the .pl country-code top-level domain. It conducts CSIRT
  NASK, one of the three Computer Security Incident Response Teams operating
  at national level under the Act of 5 July 2018 on the national
  cybersecurity system, alongside CSIRT GOV at the Internal Security Agency
  and CSIRT MON at the Ministry of National Defence.

level: national
country: PL
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
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - PL-KSC
  - PL-ABW
relationships:
  - type: implements
    target: PL-KSC
    source: fact
    evidence: "On the basis of the law of 5 July 2018 on the national cybersecurity system, the roles of national-level CSIRT were taken by the Internal Security Agency (CSIRT GOV), NASK — State Research Institute (CSIRT NASK) and the Ministry of National Defence (CSIRT MON); the tasks of CSIRT NASK were determined on the basis of that act, and together the three ensure a coherent risk management system at national level and coordinate the handling of reported incidents (nask.pl 'Centrum Cyberbezpieczeństwa NASK'; archiwum.nask.pl 'CSIRT NASK'; cyberpolicy.nask.pl). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-07-05
    valid_until: null

sources:
  - title: "Centrum Cyberbezpieczeństwa NASK"
    url: "https://www.nask.pl/projekty/centrum-cyberbezpieczenstwa-nask"
    publisher: "NASK — Państwowy Instytut Badawczy"
  - title: "CSIRT NASK"
    url: "https://archiwum.nask.pl/pl/dzialalnosc/csirt-nask"
    publisher: "NASK — Państwowy Instytut Badawczy"
  - title: "O NASK — Kim jesteśmy"
    url: "https://archiwum.nask.pl/pl/o-nas/kim-jestesmy"
    publisher: "NASK — Państwowy Instytut Badawczy"
---

# Naukowa i Akademicka Sieć Komputerowa (NASK)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

NASK is a Polish **state research institute**, a data network operator, and
the registry operator for the **.pl** country-code top-level domain. It
conducts **CSIRT NASK**, and publishes the CERT Polska reports.

## Poland's three national CSIRTs, now two of them modelled

The Act of **5 July 2018** on the national cybersecurity system — [[PL-KSC]]
— assigns the national-level CSIRT role to three bodies:

| CSIRT | Conducted by | In the Atlas |
|---|---|---|
| **CSIRT GOV** | the Internal Security Agency | [[PL-ABW]] `implements` [[PL-KSC]] |
| **CSIRT NASK** | NASK — State Research Institute | **this entity** |
| **CSIRT MON** | the Ministry of National Defence | **not modelled** |

Together they are described as ensuring a coherent, comprehensive risk
management system at national level, countering cross-sectoral and
transboundary threats and coordinating the handling of reported incidents.

The intelligence batch asserted the ABW edge and recorded the other two as
open. This closes one of them. **CSIRT MON remains unmodelled**, because the
Polish Ministry of National Defence is not an Atlas entity — the same
coverage limit that keeps [[PL-SKW]] and [[PL-SWW]] without a ministry
parent.

## Not a security agency

NASK is worth distinguishing from the bodies added in the intelligence batch.
It is a **research institute** that also runs a CSIRT and the national domain
registry — closer to [[NL-SURF]] in institutional type than to [[PL-ABW]],
even though the two share a statutory role.

That is why it carries [[DOMAIN-CYBERSECURITY]] and **not**
[[DOMAIN-NATIONAL-SECURITY]].

## `implements`, not `governed-by`

[[PL-KSC]] does not constitute NASK — NASK long predates it, and its research
and registry functions sit outside the act entirely. What the act does is
assign it a role, which NASK **operationalises**. This mirrors the edge
[[PL-ABW]] carries, and for the same reason.

## Not modelled

- **CERT Polska**, the team within NASK whose reports the sources name.
- The **.pl registry** function, and NASK's research activity.
- **CSIRT MON** and the sectoral CSIRTs.
- **NASK's relationship to [[PL-MC]]**, the ministry it is supervised by.

## Relationships

- `implements` [[PL-KSC]].

## Sources

Listed in frontmatter.
