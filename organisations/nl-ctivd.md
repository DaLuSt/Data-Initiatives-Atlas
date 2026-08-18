---
id: NL-CTIVD
type: organisation
name: Commissie van Toezicht op de Inlichtingen- en Veiligheidsdiensten
alternative_names:
  - CTIVD
  - Review Committee on the Intelligence and Security Services
description: >
  The Dutch oversight body for the AIVD and MIVD. It reviews, after the
  fact, whether the services have complied with the law, and examines how
  they have actually exercised the powers the Wet op de inlichtingen- en
  veiligheidsdiensten 2017 gives them. It is distinct from the TIB, which
  reviews the lawfulness of intended deployments beforehand.

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
organisations: []
related_entities:
  - NL-WIV-2017
  - NL-AIVD
  - NL-MIVD
  - NL-TIB
relationships:
  - type: applies-to
    target: NL-AIVD
    source: fact
    evidence: "The CTIVD reviews whether the AIVD and MIVD comply with the law; the TIB does not investigate how the services handle their powers, the CTIVD does that (ctivd.nl; aivd.nl 'Toetsing, toezicht en controle'; tib-ivd.nl 'Taken en bevoegdheden'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: NL-MIVD
    source: fact
    evidence: "The CTIVD reviews whether the AIVD and MIVD comply with the law; the Ministry of Defence describes the CTIVD as part of the review, oversight and control arrangements applying to the MIVD (ctivd.nl; defensie.nl 'Toetsing, toezicht en controle'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-WIV-2017
    source: fact
    evidence: "The Wiv 2017 regulates prior assessment by the Toetsingscommissie Inzet Bevoegdheden and subsequent oversight by the Commissie van Toezicht op de Inlichtingen- en Veiligheidsdiensten (nl.wikipedia.org 'Wet op de inlichtingen- en veiligheidsdiensten 2017'; rijksoverheid.nl; ctivd.nl). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-01
    valid_until: null

sources:
  - title: "Rechtseenheidoverleg"
    url: "https://www.ctivd.nl/over-ctivd/rechtseenheidoverleg"
    publisher: "Commissie van Toezicht op de Inlichtingen- en Veiligheidsdiensten (CTIVD)"
  - title: "Toetsing, toezicht en controle"
    url: "https://www.aivd.nl/onderwerpen/wet-op-de-inlichtingen--en-veiligheidsdiensten/toetsing-toezicht-en-controle-aivd"
    publisher: "Algemene Inlichtingen- en Veiligheidsdienst (AIVD)"
  - title: "Wet op de inlichtingen- en veiligheidsdiensten 2017"
    url: "https://nl.wikipedia.org/wiki/Wet_op_de_inlichtingen-_en_veiligheidsdiensten_2017"
    publisher: "Wikipedia"
---

# Commissie van Toezicht op de Inlichtingen- en Veiligheidsdiensten (CTIVD)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The CTIVD is the **retrospective** oversight body for [[NL-AIVD]] and
[[NL-MIVD]]. It reviews whether the services have complied with the law and
examines how they have used the powers [[NL-WIV-2017]] gives them.

## The division of labour with [[NL-TIB]]

The Dutch model splits review in two, and the split is by **time**, not by
subject:

| | [[NL-TIB]] | CTIVD |
|---|---|---|
| When | Before deployment | After the fact |
| Question | Is the intended deployment lawful? | Did the service comply, and how did it use the power? |
| Effect | **Binding** | Reports |

The sources state the boundary in as many words: the TIB does not
investigate how the services handle their powers — the CTIVD does. To keep
the two readings of the same statute consistent, the bodies hold a standing
*rechtseenheidoverleg*, a "legal-unity consultation".

## Why this is an `applies-to`, not a `governed-by`

The CTIVD is not a superior of the services and does not direct them; it
examines their compliance. `applies-to` is the Atlas type for "a rule,
standard or framework applies to a class of entities", and the oversight
relation is closer to that than to ownership or governance. The edge from
the service side is to the **act**, not to the reviewer.

## Not modelled

- The **complaints function**. The CTIVD handles complaints as well as
  conducting oversight investigations; the two are not distinguished here.
- The **binding force of CTIVD findings**, which changed under the Wiv 2017
  and again under [[NL-TWCO]]. The temporary act is described by its
  sources as strengthening binding oversight, but no source read states
  precisely how, so no relationship to [[NL-TWCO]] is asserted.

## Relationships

- `applies-to` [[NL-AIVD]] and [[NL-MIVD]].
- `governed-by` [[NL-WIV-2017]].

## Sources

Listed in frontmatter.
