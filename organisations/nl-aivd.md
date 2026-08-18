---
id: NL-AIVD
type: organisation
name: Algemene Inlichtingen- en Veiligheidsdienst
alternative_names:
  - AIVD
  - General Intelligence and Security Service
description: >
  The Dutch civilian intelligence and security service, operating under the
  Minister of the Interior and Kingdom Relations. Its tasks, powers and the
  conditions under which it may use them are set by the Wet op de
  inlichtingen- en veiligheidsdiensten 2017, which also subjects it to
  binding prior review by the TIB and retrospective oversight by the CTIVD.

level: national
country: NL
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
  - DOMAIN-NATIONAL-SECURITY
organisations:
  - NL-BZK
related_entities:
  - NL-WIV-2017
  - NL-TWCO
  - NL-MIVD
  - NL-CTIVD
  - NL-TIB
relationships:
  - type: part-of
    target: NL-BZK
    source: fact
    evidence: "The AIVD is the civilian intelligence and security agency of the Netherlands, operating under the Ministry of the Interior and Kingdom Relations (en.wikipedia.org 'General Intelligence and Security Service'; irp.fas.org 'Netherlands — Intelligence and Security Services'; aivd.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-WIV-2017
    source: fact
    evidence: "The Wiv 2017 is the legal framework for the AIVD and the MIVD; the law precisely establishes the tasks of the services and the exercise of their powers, and replaced the Wet op de inlichtingen- en veiligheidsdiensten 2002 (aivd.nl 'Wet op de inlichtingen- en veiligheidsdiensten'; rijksoverheid.nl 'Nieuwe Wet op de inlichtingen- en veiligheidsdiensten (Wiv 2017)'; nl.wikipedia.org). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-01
    valid_until: null
  - type: governed-by
    target: NL-TWCO
    source: fact
    evidence: "The Tijdelijke wet onderzoeken AIVD en MIVD naar landen met een offensief cyberprogramma allows temporary deviation from the regime in the Wiv 2017 for investigations by the AIVD and MIVD into countries with an offensive cyber programme; it entered into force on 1 July 2024 and expires four years after that date (aivd.nl; eerstekamer.nl dossier 36.263; njb.nl 'Tijdelijke wet cyberoperaties'). NOT READ — search-only."
    confidence: medium
    valid_from: 2024-07-01
    valid_until: null

sources:
  - title: "Wet op de inlichtingen- en veiligheidsdiensten"
    url: "https://www.aivd.nl/onderwerpen/wet-op-de-inlichtingen-en-veiligheidsdiensten"
    publisher: "Algemene Inlichtingen- en Veiligheidsdienst (AIVD)"
  - title: "Toetsing, toezicht en controle"
    url: "https://www.aivd.nl/onderwerpen/wet-op-de-inlichtingen--en-veiligheidsdiensten/toetsing-toezicht-en-controle-aivd"
    publisher: "Algemene Inlichtingen- en Veiligheidsdienst (AIVD)"
  - title: "General Intelligence and Security Service"
    url: "https://en.wikipedia.org/wiki/General_Intelligence_and_Security_Service"
    publisher: "Wikipedia"
  - title: "Netherlands — Intelligence and Security Services"
    url: "https://irp.fas.org/world/netherlands/index.html"
    publisher: "Federation of American Scientists, Intelligence Resource Program"
---

# Algemene Inlichtingen- en Veiligheidsdienst (AIVD)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read, because
> the working environment blocks page retrieval. It carries
> `verification: search-only`. See
> `discovery/reverification-allowlist.md`.

## Description

The AIVD is the **civilian** half of the Dutch intelligence and security
apparatus, operating under the Minister of the Interior and Kingdom
Relations. Its military counterpart is [[NL-MIVD]], under the Minister of
Defence.

Everything the service may do is set by [[NL-WIV-2017]]: the sources
describe that act as establishing precisely the tasks of the services and
the exercise of their powers.

## The law it operates under

Two instruments, not one:

- **[[NL-WIV-2017]]** — the standing framework, in force since 1 May 2018.
- **[[NL-TWCO]]** — a *temporary* act, in force since 1 July 2024, which
  deviates from the Wiv 2017 regime for investigations into countries with
  an offensive cyber programme. It expires four years after entry into
  force.

Both are modelled with `governed-by`, and the temporary act is the reason
this entity has two: an entity whose powers are currently defined by a
standing act **as modified by a sunsetting one** is not accurately described
by either alone.

## Two reviewers, doing different jobs

The distinction matters and is easy to get wrong:

- **[[NL-TIB]]** reviews **beforehand**, and only for lawfulness. Its
  decision is **binding**, and it acts after the minister has already
  decided.
- **[[NL-CTIVD]]** reviews **afterwards**, examining how the services
  actually used the powers.

The sources are explicit that the TIB does not investigate how the services
handle their powers — the CTIVD does that. The two hold a standing
*rechtseenheidoverleg* to keep their reading of the Wiv 2017 consistent.

## Why [[NL-AP]] is absent from this entity

The Dutch data protection authority does not supervise the AIVD, and no
relationship is asserted between them. Intelligence processing falls outside
the material scope of [[EU-GDPR]] under Article 2(2)(a), and Article 4(2)
TEU reserves national security to the member states. The Wiv 2017 builds a
separate review structure — TIB and CTIVD — precisely because the ordinary
one does not reach here. See [[DOMAIN-NATIONAL-SECURITY]].

## Not modelled

- The **Joint Sigint Cyber Unit (JSCU)**, the joint AIVD/MIVD signals
  intelligence unit, mentioned in the sources as founded in 2014. It is a
  joint unit rather than a service in its own right and was not researched.
- The **Commissie van Toezicht op de Inlichtingen- en Veiligheidsdiensten's
  klachtbehandeling** — the CTIVD's complaints function is separate from its
  oversight function and is not distinguished here.
- Any **operational** matter. The Atlas records statutory structure.

## Relationships

- `part-of` [[NL-BZK]].
- `governed-by` [[NL-WIV-2017]] and [[NL-TWCO]].

## Sources

Listed in frontmatter.
