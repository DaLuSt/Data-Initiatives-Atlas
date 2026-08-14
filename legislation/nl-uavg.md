---
id: NL-UAVG
type: law
name: Uitvoeringswet Algemene verordening gegevensbescherming
alternative_names:
  - UAVG
  - GDPR Implementation Act
description: >
  Dutch implementing act for the EU General Data Protection Regulation. In
  force from 25 May 2018, when it replaced the Wet bescherming
  persoonsgegevens (Wbp), it gives national effect to the discretion the
  GDPR leaves to member states.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2018-05-25
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-AP
related_entities:
  - EU-GDPR
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "The UAVG implements the GDPR in the Netherlands; it entered into force on 25 May 2018, the date the GDPR became applicable (autoriteitpersoonsgegevens.nl; Eerste Kamer dossier 34.851). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "Uitvoeringswet Algemene verordening gegevensbescherming (UAVG)"
    url: "https://www.autoriteitpersoonsgegevens.nl/documenten/uitvoeringswet-algemene-verordening-gegevensbescherming-uavg"
    publisher: "Autoriteit Persoonsgegevens"
  - title: "Uitvoeringswet Algemene verordening gegevensbescherming (34.851)"
    url: "https://www.eerstekamer.nl/wetsvoorstel/34851_uitvoeringswet_algemene"
    publisher: "Eerste Kamer der Staten-Generaal"
  - title: "Staatsblad 2018, 144"
    url: "https://zoek.officielebekendmakingen.nl/stb-2018-144.html"
    publisher: "Overheid.nl — Officiële bekendmakingen"
---

# Uitvoeringswet AVG (UAVG)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The UAVG is the Dutch implementing act for the [[EU-GDPR]]. It entered into
force on 25 May 2018 — the date the GDPR became applicable — and on that
date the GDPR replaced the Wet bescherming persoonsgegevens (Wbp) as the
governing data protection regime in the Netherlands.

Its passage: adopted by the Tweede Kamer on 13 March 2018 and by the Eerste
Kamer on 15 May 2018. Article 48a was excepted from the general entry into
force and took effect separately by decision of 19 December 2018.

A related *Aanpassingswet* AVG (Eerste Kamer dossier 34.939) adjusted other
Dutch legislation to the GDPR; it is not modelled separately here, and
whether it warrants its own entity is queued in
`discovery/research-queue.md`.

## Classification

Per `metadata/taxonomy.md` §2 this is **Dutch implementation legislation**:
`type: law`, `level: national`, `country: NL`, `region: EU` — the `region`
field recording that its obligations originate in an EU instrument, with the
`implements-requirement-from` relationship naming which one.

## Relationships

- Implements requirements from [[EU-GDPR]].
- [[NL-AP]] is the supervisory authority operating under it.
- The Wbp, which the GDPR/UAVG regime replaced, is not yet an Atlas entity;
  queued for temporal completeness.

## Sources

Listed in frontmatter.
