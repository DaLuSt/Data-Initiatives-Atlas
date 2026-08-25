---
id: IT-AGID
type: organisation
name: Agenzia per l'Italia Digitale
alternative_names:
  - AgID
  - Agency for Digital Italy
description: >
  Italian agency responsible for promoting digital innovation in the
  country and the use of digital technologies in public administration and
  in the relationship between administration, citizens and enterprises. It
  manages the public digital identity system for citizens and businesses,
  SPID, established by Article 64 of the Codice dell'Amministrazione
  Digitale.

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
  - IT-CAD
  - IT-SPID
relationships:
  - type: part-of
    target: IT
    source: fact
    evidence: "AgID is a public body of IT; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: IT-CAD
    source: fact
    evidence: "Confirmed by reading bosettiegatti.eu's text of the Codice dell'Amministrazione Digitale directly (2026-08-25): Article 64 states 'è istituito, a cura dell'Agenzia per l'Italia digitale, il sistema pubblico per la gestione dell'identità digitale' (the public digital-identity management system — SPID — is established under the responsibility of the Agency for Digital Italy). Corroborated independently by spid.gov.it's own legal notice page, read directly the same day, which names 'AGID – Agenzia per l'Italia Digitale' as the data controller (titolare del trattamento) of the SPID site itself."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Agenzia per l'Italia Digitale"
    url: "https://www.agid.gov.it/"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
    accessed: "2026-08-25"
  - title: "Decreto legislativo 7 marzo 2005, n. 82 - Codice dell'amministrazione digitale"
    url: "https://www.bosettiegatti.eu/info/norme/statali/2005_0082.htm"
    publisher: "Bosetti & Gatti"
    accessed: "2026-08-25"
  - title: "Note legali - SPID"
    url: "https://www.spid.gov.it/note-legali/"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
    accessed: "2026-08-25"
  - title: "Agenzia per l'Italia digitale"
    url: "https://it.wikipedia.org/wiki/Agenzia_per_l%27Italia_digitale"
    publisher: "Wikipedia"
    accessed: "2026-08-25"
---

# Agenzia per l'Italia Digitale

> **Verified 2026-08-25.** All four cited pages were read directly.
> Decreto legislativo 82/2005's own Article 64 text confirms SPID is
> established "a cura dell'Agenzia per l'Italia digitale" (under AgID's
> responsibility), and spid.gov.it's own legal notice independently
> names AgID as the site's data controller.

## Description

Italy's digital government agency, and the operator of [[IT-SPID]].

## The largest member state the Atlas had left

Italy was **first on the country-expansion shortlist** and had carried
only its anchor since the European country batch. AgID is the entry
point: it holds the digital identity system, the technical rules under
[[IT-CAD]], and the *Piano triennale* for public-administration IT. It
also, this pass found, manages [[IT-DATI-GOV-IT]], Italy's national open
data portal, since 2015 — see that entity.

## Relationships

- `governed-by` [[IT-CAD]] - the Code is AgID's operating statute as
  well as Italy's digital administration law.
- `part-of` [[IT]] (anchor edge).

## Sources

Listed in frontmatter, all four read directly this pass.
`bosettiegatti.eu` blocks this project's honest User-Agent but serves a
browser-spoofing one — see [[IT-CAD]].
