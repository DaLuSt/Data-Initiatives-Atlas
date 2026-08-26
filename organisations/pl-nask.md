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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations:
  - PL-MC
related_entities:
  - PL-KSC
  - PL-ABW
  - PL-MC
relationships:
  - type: governed-by
    target: PL-MC
    source: fact
    evidence: "Confirmed by reading archiwum.nask.pl's own 'Kim jesteśmy' page directly (2026-08-26): 'NASK jest państwowym instytutem badawczym nadzorowanym przez Ministerstwo Cyfryzacji' (NASK is a state research institute supervised by the Ministry of Digital Affairs). This closes the relationship this entity previously flagged as not established. The same page dates NASK's founding to 1991 at the University of Warsaw, independence as a research-development unit in 1993, and State Research Institute status from 2017 — none previously carried."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements
    target: PL-KSC
    source: fact
    evidence: "Confirmed by reading nask.pl's own Cybersecurity Centre page directly (2026-08-26): CSIRT NASK acts as a 'CERT of last resort', coordinating incidents from entities not covered by the other two national-level CSIRTs (CSIRT GOV at the Internal Security Agency, CSIRT MON at the Ministry of National Defence) under the Act of 5 July 2018 on the national cybersecurity system. `archiwum.nask.pl`'s dedicated CSIRT NASK page and `cyberpolicy.nask.pl` were not read this pass."
    confidence: medium
    valid_from: 2018-07-05
    valid_until: null

sources:
  - title: "Centrum Cyberbezpieczeństwa NASK"
    url: "https://www.nask.pl/projekty/centrum-cyberbezpieczenstwa-nask"
    publisher: "NASK — Państwowy Instytut Badawczy"
    accessed: "2026-08-26"
  - title: "CSIRT NASK"
    url: "https://archiwum.nask.pl/pl/dzialalnosc/csirt-nask"
    publisher: "NASK — Państwowy Instytut Badawczy"
  - title: "O NASK — Kim jesteśmy"
    url: "https://archiwum.nask.pl/pl/o-nas/kim-jestesmy"
    publisher: "NASK — Państwowy Instytut Badawczy"
    accessed: "2026-08-26"
---

# Naukowa i Akademicka Sieć Komputerowa (NASK)

> **Verified 2026-08-26.** Two of three cited pages were read directly.
> NASK's own page names its supervising ministry — a gap this entity
> previously flagged as unestablished — and gives a founding history not
> previously carried, though only in bare years, so `start_date` stays
> `null` rather than a guessed day and month.

## Description

NASK is a Polish **state research institute**, a data network operator, and
the registry operator for the **.pl** country-code top-level domain. It
conducts **CSIRT NASK**, and publishes the CERT Polska reports. Confirmed
by reading archiwum.nask.pl's own "Kim jesteśmy" page directly: NASK was
established in **1991** at the University of Warsaw, became an
independent research-development unit in **1993**, and reached **State
Research Institute** status in **2017** — none of the three dates precise
enough to set `start_date`.

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

## `governed-by` [[PL-MC]], now sourced

Previously flagged as not established. NASK's own page states directly
that it is "nadzorowany przez Ministerstwo Cyfryzacji" (supervised by the
Ministry of Digital Affairs) — the same ministry [[PL-COI]] answers to,
making NASK the second body in the Atlas under [[PL-MC]]'s supervision.

## Not modelled

- **CERT Polska**, the team within NASK whose reports the sources name.
- The **.pl registry** function, and NASK's research activity.
- **CSIRT MON** and the sectoral CSIRTs.

## Relationships

- `governed-by` [[PL-MC]] — confirmed this pass.
- `implements` [[PL-KSC]].

## Sources

Listed in frontmatter, two of three read directly this pass.
