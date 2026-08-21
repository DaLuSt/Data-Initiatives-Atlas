---
id: IT-SPID
type: platform
name: Sistema Pubblico di Identita Digitale
alternative_names:
  - SPID
  - Sistema Pubblico di Identità Digitale
  - Public Digital Identity System
description: >
  Italian public digital identity system, established by Article 64 of the
  Codice dell'Amministrazione Digitale and managed by AgID. It gives
  everyone the right to access the online services of public
  administrations, public service operators and publicly controlled
  companies through their own digital identity, simply and securely, at
  any time and from any device. SPID sits alongside two other accepted
  credentials, the electronic identity card CIE and the national services
  card CNS.

level: national
country: IT
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IT
  - IT-AGID
  - IT-CAD
relationships:
  - type: maintained-by
    target: IT-AGID
    source: fact
    evidence: "AgID manages the public system for managing digital identity for citizens and enterprises (SPID), established by article 64, paragraph 2-bis, of decreto legislativo 82/2005 (agid.gov.it). NOT READ - search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: IT-CAD
    source: fact
    evidence: "SPID is established by Article 64 of decreto legislativo 82/2005; the Code gives everyone the right to access the online services of public administrations through their own digital identity - SPID, CIE or CNS (agid.gov.it 'Guida ai diritti di cittadinanza digitale'). NOT READ - search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SPID - Sistema Pubblico di Identita Digitale"
    url: "https://www.spid.gov.it/"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
  - title: "Guida ai diritti di cittadinanza digitale"
    url: "https://www.agid.gov.it/sites/default/files/repository_files/guida_riepilogo_diritti_cittadinanza_digitale_03-2022.pdf"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
---

# Sistema Pubblico di Identita Digitale

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Italy's public digital identity system, created by statute rather than
by programme.

## Three credentials, one right

[[IT-CAD]] frames access as a **right of the citizen** - to reach public
online services through *their own* digital identity - and then admits
three credentials to exercise it: SPID, the electronic identity card
**CIE**, and the services card **CNS**.

That is a different shape from the identity platforms the Atlas already
holds. [[ES-CLAVE]] and [[FR-FRANCECONNECT]] are systems the state
provides; SPID is one of several ways to exercise an entitlement the
Code confers. Neither CIE nor CNS is modelled.

## Relationships

- `maintained-by` [[IT-AGID]].
- `governed-by` [[IT-CAD]] - specifically its Article 64.

## Sources

Listed in frontmatter.
