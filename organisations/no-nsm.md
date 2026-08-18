---
id: NO-NSM
type: organisation
name: Nasjonal sikkerhetsmyndighet
alternative_names:
  - NSM
  - Norwegian National Security Authority
description: >
  Norway's national security authority, a directorate that coordinates
  preventive security measures and works to improve Norway's ability to
  protect itself against espionage, sabotage, terrorism and complex threats.
  It is the national professional environment for ICT security and the
  national warning and coordination body for serious cyber attacks. It is
  administratively subordinate to the Ministry of Justice and Public
  Security and reports on a technical line to the Ministry of Defence for
  the military sector.

level: national
country: "NO"
region: null

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
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - "NO"
relationships:
  - type: part-of
    target: "NO"
    source: fact
    evidence: "Nasjonal sikkerhetsmyndighet is a Norwegian directorate, administratively subordinate to the Ministry of Justice and Public Security and reporting on a technical line to the Ministry of Defence for the military sector (nsm.no; regjeringen.no). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Dette er NSM"
    url: "https://nsm.no/om-oss/dette-er-nsm/"
    publisher: "Nasjonal sikkerhetsmyndighet (NSM)"
  - title: "The Norwegian National Security Authority (NSM)"
    url: "https://www.regjeringen.no/en/dep/jd/organisation/etater-ogvirksomheter/the-norwegian-national-security-authority-nsm/id426401/"
    publisher: "Justis- og beredskapsdepartementet (Norwegian Ministry of Justice and Public Security)"
  - title: "Nasjonal sikkerhetsmyndighet"
    url: "https://snl.no/Nasjonal_sikkerhetsmyndighet"
    publisher: "Store norske leksikon"
  - title: "Nasjonal sikkerhetsmyndighet — oppgaver og styring"
    url: "https://www.regjeringen.no/contentassets/ab14d01119a248e29010c01643b62a81/no/pdfs/g-0460-b-nasjonal-sikkerhetsmyndighet.pdf"
    publisher: "Justis- og beredskapsdepartementet"
---

# Nasjonal sikkerhetsmyndighet (NSM)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

NSM is Norway's national security authority. Its stated task is to improve
Norway's ability to protect itself against **espionage, sabotage, terrorism
and complex threats**, and it coordinates preventive security measures
across state and municipal administration and private suppliers to the
public sector under security-classified procurement.

It is also the **national professional environment for ICT security** and
the national warning and coordination body for serious cyber attacks.

## Two ministries, one directorate

The reporting arrangement is worth recording precisely:

- **Administratively** subordinate to the Ministry of Justice and Public
  Security.
- On a **technical line** to the **Ministry of Defence** for tasks in the
  military sector, and to the Ministry of Justice for the civil sector.

No other body in the Atlas is described this way. [[DE-BSI]] sits in one
ministry ([[DE-BMI]]); [[GB-NCSC]] sits inside an intelligence agency
([[GB-GCHQ]]); [[ES-CCN]] inside [[ES-CNI]]. Norway splits the line by
*sector* instead of by *organisation*.

## Why it carries both domains

This is the only entity outside the intelligence batch to hold
[[DOMAIN-CYBERSECURITY]] and [[DOMAIN-NATIONAL-SECURITY]] together, and the
reason is that NSM genuinely occupies both roles: preventive security in the
classified sense, and the national cyber warning function.

**It is not modelled as an intelligence service.** One source describes NSM
as part of the Norwegian secret services; that phrasing appears in an
encyclopaedia entry and not in the government sources, and the Atlas will
not classify a body as an intelligence service on that basis. Norway's
actual intelligence services — the Etterretningstjenesten and PST — are
**not modelled**, so the country appears here with a national security
authority and no services, which is not a complete picture. See
`discovery/unresolved.md`.

## No relationships asserted

NSM's statutory basis is the *sikkerhetsloven* (the Security Act), which is
**not an Atlas entity** and was not researched in this batch. Without it
there is nothing to point a `governed-by` edge at, and no source read
connects NSM to any entity the Atlas holds.

The entity is reachable through [[DOMAIN-CYBERSECURITY]] and
[[DOMAIN-NATIONAL-SECURITY]] and through the [[NO]] country index, and
through nothing else. That is recorded rather than patched with a guess.

## Sources

Listed in frontmatter — three of four are official.
