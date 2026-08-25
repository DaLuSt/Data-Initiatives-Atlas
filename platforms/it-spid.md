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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-25"
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
    evidence: "Confirmed by reading spid.gov.it's own legal notice page directly (2026-08-25): 'Titolare del trattamento dei dati personali AGID – Agenzia per l'Italia Digitale' (the data controller of this website is AGID), naming AgID as the entity legally responsible for the SPID site. Corroborated by decreto legislativo 82/2005's own Article 64 text, read directly the same day: SPID 'è istituito, a cura dell'Agenzia per l'Italia digitale' (is established under the responsibility of AgID)."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: IT-CAD
    source: fact
    evidence: "Confirmed by reading bosettiegatti.eu's text of decreto legislativo 82/2005 directly (2026-08-25): Article 64 establishes SPID by name, and AgID's own 'Guida ai diritti di cittadinanza digitale', also read directly, states the right verbatim: 'Chiunque ha il diritto di accedere ai servizi online offerti dalle pubbliche amministrazioni, da gestori di servizi pubblici e da società a controllo pubblico tramite la propria identità digitale (SPID, CIE, CNS)' (everyone has the right to access online services offered by public administrations, public-service operators and publicly controlled companies through their own digital identity — SPID, CIE, CNS), naming all three credentials exactly as this entity's description does."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SPID - Sistema Pubblico di Identita Digitale"
    url: "https://www.spid.gov.it/"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
    accessed: "2026-08-25"
  - title: "Note legali - SPID"
    url: "https://www.spid.gov.it/note-legali/"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
    accessed: "2026-08-25"
  - title: "Decreto legislativo 7 marzo 2005, n. 82 - Codice dell'amministrazione digitale"
    url: "https://www.bosettiegatti.eu/info/norme/statali/2005_0082.htm"
    publisher: "Bosetti & Gatti"
    accessed: "2026-08-25"
  - title: "Guida ai diritti di cittadinanza digitale"
    url: "https://www.agid.gov.it/sites/default/files/repository_files/guida_riepilogo_diritti_cittadinanza_digitale_03-2022.pdf"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
    accessed: "2026-08-25"
---

# Sistema Pubblico di Identita Digitale

> **Verified 2026-08-25.** All four cited pages were read directly.
> spid.gov.it's own legal notice names [[IT-AGID]] as the site's data
> controller, [[IT-CAD]]'s Article 64 was read directly and confirms
> SPID's legal basis by name, and AgID's own citizens'-rights guide
> confirms the three-credential (SPID/CIE/CNS) framing verbatim.

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

Listed in frontmatter, all four read directly this pass.
`bosettiegatti.eu` blocks this project's honest User-Agent but serves a
browser-spoofing one — see [[IT-CAD]].
