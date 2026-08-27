---
id: NL-CTIVD
type: organisation
name: Commissie van Toezicht op de Inlichtingen- en Veiligheidsdiensten
alternative_names:
  - CTIVD
  - Review Committee on the Intelligence and Security Services
description: >
  The Dutch oversight body for the AIVD and MIVD. It reviews, during and
  after the fact, whether the services have complied with the law, and
  examines how they have actually exercised the powers the Wet op de
  inlichtingen- en veiligheidsdiensten 2017 gives them. It is distinct from
  the TIB, which reviews the lawfulness of intended deployments beforehand.

level: national
country: NL
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading ctivd.nl's own page on the rechtseenheidoverleg directly (2026-08-27): the CTIVD conducts post-facto assessment of whether the AIVD and MIVD comply with the law, and 'can go deeper [than the TIB] because it has independent access to the systems and staff of the AIVD and MIVD'. aivd.nl's own oversight page, also read directly, confirms the CTIVD 'houdt toezicht tijdens en na afloop van de inzet van bevoegdheden' (oversees during and after the use of powers)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: applies-to
    target: NL-MIVD
    source: fact
    evidence: "Confirmed by reading defensie.nl's own oversight page directly (2026-08-27): the CTIVD supervises MIVD activities during and after operations, can investigate and make recommendations (though these are not binding in the way TIB's prior approval is), and handles complaints and misconduct reports."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-WIV-2017
    source: fact
    evidence: "Confirmed by reading nl.wikipedia.org's 'Wet op de inlichtingen- en veiligheidsdiensten 2017' article directly (2026-08-27): the Wiv 2017 established the CTIVD's current form, expanding it to include separate audit and complaint-handling divisions. ctivd.nl, also read directly, describes the commission's function under that act."
    confidence: high
    valid_from: 2018-05-01
    valid_until: null

sources:
  - title: "Rechtseenheidoverleg"
    url: "https://www.ctivd.nl/over-ctivd/rechtseenheidoverleg"
    publisher: "Commissie van Toezicht op de Inlichtingen- en Veiligheidsdiensten (CTIVD)"
    accessed: "2026-08-27"
  - title: "Toetsing, toezicht en controle"
    url: "https://www.aivd.nl/onderwerpen/wet-op-de-inlichtingen--en-veiligheidsdiensten/toetsing-toezicht-en-controle-aivd"
    publisher: "Algemene Inlichtingen- en Veiligheidsdienst (AIVD)"
    accessed: "2026-08-27"
  - title: "Wet op de inlichtingen- en veiligheidsdiensten 2017"
    url: "https://nl.wikipedia.org/wiki/Wet_op_de_inlichtingen-_en_veiligheidsdiensten_2017"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
---

# Commissie van Toezicht op de Inlichtingen- en Veiligheidsdiensten (CTIVD)

> **Verified 2026-08-27.** All three cited pages were read directly this
> pass, closing the previous `search-only` status. No factual correction
> was needed; the entity's description was confirmed and sharpened in
> several places (see below).

## Description

The CTIVD is the **retrospective and ongoing** oversight body for
[[NL-AIVD]] and [[NL-MIVD]]. It reviews whether the services have complied
with the law and examines how they have used the powers [[NL-WIV-2017]]
gives them. ctivd.nl's own page, read directly, states the CTIVD "can go
deeper" than [[NL-TIB]] "because it has independent access to the systems
and staff of the AIVD and MIVD" — direct, unmediated access is the
mechanism, not just a broader remit.

## The division of labour with [[NL-TIB]]

The Dutch model splits review in two, and the split is by **time**, not by
subject:

| | [[NL-TIB]] | CTIVD |
|---|---|---|
| When | Before deployment (after in emergencies) | During and after |
| Question | Is the intended deployment lawful? | Did the service comply, and how did it use the power? |
| Effect | **Binding** | Findings and recommendations, generally not binding |

aivd.nl's own oversight page, read directly, states the boundary in as many
words: the TIB "beoordeelt of de toestemming rechtmatig is" (assesses
whether the authorisation is lawful) before the fact, while the CTIVD
"houdt toezicht tijdens en na afloop van de inzet van bevoegdheden"
(oversees during and after the use of powers). To keep the two readings of
the same statute consistent, the bodies hold a standing
*rechtseenheidoverleg* — "though not formally codified in law", per
ctivd.nl's own page, both institutions "share responsibility for
maintaining legal consistency". When they agree, the joint position goes to
parliament as a *rechtseenheidbrief*, published on both organisations'
websites.

Under [[NL-TWCO]], part of this balance shifts for certain powers towards
real-time CTIVD monitoring with binding authority to halt an operation
immediately — see [[NL-AIVD]] and [[NL-TWCO]].

## Why this is an `applies-to`, not a `governed-by`

The CTIVD is not a superior of the services and does not direct them; it
examines their compliance. `applies-to` is the Atlas type for "a rule,
standard or framework applies to a class of entities", and the oversight
relation is closer to that than to ownership or governance. The edge from
the service side is to the **act**, not to the reviewer.

## Not modelled

- The **complaints function**. The CTIVD handles complaints as well as
  conducting oversight investigations; the two are not distinguished here.
- The precise **binding force** of CTIVD findings, which the sources
  describe as strengthened under [[NL-TWCO]] for the powers it covers,
  without stating the general rule outside that act.

## Relationships

- `applies-to` [[NL-AIVD]] and [[NL-MIVD]].
- `governed-by` [[NL-WIV-2017]].

## Sources

All three read directly this pass: ctivd.nl's own rechtseenheidoverleg
page, aivd.nl's oversight page, and the Dutch Wikipedia article on the
Wiv 2017.
