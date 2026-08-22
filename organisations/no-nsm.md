---
id: NO-NSM
type: organisation
name: Nasjonal sikkerhetsmyndighet
alternative_names:
  - NSM
  - Norwegian National Security Authority
description: >
  Norway's national security authority, a directorate that, together with
  the Norwegian Intelligence Service and the Police Security Service
  (PST), forms Norway's three intelligence, surveillance and security
  services. It coordinates preventive security measures and works to
  improve Norway's ability to protect itself against espionage, sabotage,
  terrorism and complex threats. Norway's National Cyber Security Centre
  is part of NSM. NSM is administratively subordinate to the Ministry of
  Justice and Public Security, while the Ministry of Defence has
  instruction authority over NSM in matters within its area of
  responsibility.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed verbatim by reading nsm.no directly (2026-08-22): 'NSM er administrativt underlagt Justis- og beredskapsdepartementet, samtidig som Forsvarsdepartementet har instruksjonsmyndighet overfor NSM i saker på deres ansvarsområde' (NSM is administratively subordinate to the Ministry of Justice and Public Security, while the Ministry of Defence has instruction authority over NSM in matters within its area of responsibility). Independently confirmed on snl.no (Store norske leksikon): 'Direktoratet er administrativt underlagt Justis- og beredskapsdepartementet.' regjeringen.no returned a bot-defense challenge (403) and was not read. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Dette er NSM"
    url: "https://nsm.no/om-oss/dette-er-nsm/"
    publisher: "Nasjonal sikkerhetsmyndighet (NSM)"
    accessed: "2026-08-22"
  - title: "The Norwegian National Security Authority (NSM)"
    url: "https://www.regjeringen.no/en/dep/jd/organisation/etater-ogvirksomheter/the-norwegian-national-security-authority-nsm/id426401/"
    publisher: "Justis- og beredskapsdepartementet (Norwegian Ministry of Justice and Public Security)"
  - title: "Nasjonal sikkerhetsmyndighet"
    url: "https://snl.no/Nasjonal_sikkerhetsmyndighet"
    publisher: "Store norske leksikon"
    accessed: "2026-08-22"
  - title: "Nasjonal sikkerhetsmyndighet — oppgaver og styring"
    url: "https://www.regjeringen.no/contentassets/ab14d01119a248e29010c01643b62a81/no/pdfs/g-0460-b-nasjonal-sikkerhetsmyndighet.pdf"
    publisher: "Justis- og beredskapsdepartementet"
  - title: "About the Norwegian National Security Authority"
    url: "https://nsm.no/en/"
    publisher: "Nasjonal sikkerhetsmyndighet (NSM)"
    accessed: "2026-08-22"
---

# Nasjonal sikkerhetsmyndighet (NSM)

> **Verified 2026-08-22.** nsm.no, its English page and snl.no were read
> directly and confirm the claims below, verbatim in places.
> `regjeringen.no` returned a bot-defense challenge (403) and was not
> read. **A significant finding overturns this entity's previous
> restraint**: see "NSM is one of Norway's three security services — now
> confirmed" below.

## Description

Confirmed verbatim by reading nsm.no directly (2026-08-22): "NSM utgjør
sammen med Etterretningstjenesten og Politiets sikkerhetstjeneste (PST)
Norges tre etterretnings- overvåkings- og sikkerhetstjenester" (NSM
constitutes, together with the Norwegian Intelligence Service and the
Police Security Service, Norway's three intelligence, surveillance and
security services). NSM is Norway's national security authority. Its stated task is to improve
Norway's ability to protect itself against **espionage, sabotage, terrorism
and complex threats**, and it coordinates preventive security measures
across state and municipal administration and private suppliers to the
public sector under security-classified procurement.

Confirmed verbatim on the same page: "Nasjonalt cybersikkerhetssenter
(NCSC) er en del av NSM" (Norway's National Cyber Security Centre is
part of NSM) — independently confirmed on nsm.no's English page, whose
"Cyber Security" section names "National Cyber Security Centre" among
NSM's areas of expertise. NSM is also the **national professional
environment for ICT security** and the national warning and coordination
body for serious cyber attacks.

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

## NSM is one of Norway's three security services — now confirmed

The Atlas's previous restraint here was principled but is now overtaken by
better evidence. It read: *"NSM is not modelled as an intelligence
service. One source describes NSM as part of the Norwegian secret
services; that phrasing appears in an encyclopaedia entry and not in the
government sources, and the Atlas will not classify a body as an
intelligence service on that basis."*

That caution was correctly applied to the evidence available at the
time. It no longer describes the evidence. NSM's own official website —
not an encyclopaedia, not a secondary source — states directly that NSM
is one of Norway's three *etterretnings- overvåkings- og
sikkerhetstjenester* (intelligence, surveillance and security services),
alongside the Norwegian Intelligence Service (Etterretningstjenesten) and
the Police Security Service (PST). The `domains:` field already carried
[[DOMAIN-NATIONAL-SECURITY]] on this basis; the prose above now matches
what the domain assignment already implied.

**Etterretningstjenesten and PST remain unmodelled.** Norway still
appears in the Atlas with one of its three security services and not the
other two — a real gap, just a differently-shaped one than before: it is
now known that NSM's peers exist and are named, not merely suspected.

## No relationships beyond the anchor

NSM's statutory basis is named this pass — snl.no states plainly that
"forebyggende sikkerhetstjeneste er regulert i sikkerhetsloven av 1998"
(the preventive security service is regulated by the Security Act of
1998) — but the *sikkerhetsloven* is **not an Atlas entity**, so there is
still nothing to point a `governed-by` edge at. Whether the 1998 Act is
still the current one is itself unsettled: NSM's own site separately
lists "Sikkerhetsloven og forskrifter" and "Digitalsikkerhetsloven og
-forskriften" as distinct regulatory sections, suggesting a more recent
digital-security statute exists alongside or instead of it, and this
pass did not resolve which.

**Norway's National Cyber Security Centre, confirmed as part of NSM
above, is also not modelled separately.** Unlike [[GB-NCSC]] (part of
[[GB-GCHQ]]) or [[CH-BACS]] (renamed from NCSC), Norway's NCSC has no
Atlas entity of its own; its activities are recorded here, under NSM.

The entity is reachable through the [[NO]] anchor,
[[DOMAIN-CYBERSECURITY]] and [[DOMAIN-NATIONAL-SECURITY]], and through
nothing else.

## Sources

Listed in frontmatter, three of five read directly this pass.
`regjeringen.no` returned a bot-defense challenge and stays cited but
unread.
