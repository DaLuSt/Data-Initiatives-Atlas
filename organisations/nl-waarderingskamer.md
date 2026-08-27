---
id: NL-WAARDERINGSKAMER
type: organisation
name: Waarderingskamer
alternative_names:
  - Netherlands Council for Real Estate Assessment
description: >
  Dutch supervisory body that controls whether municipalities properly
  implement the Wet WOZ and supervises the implementation of the
  Basisregistratie WOZ. It is also the functional manager of the Landelijke
  Voorziening WOZ, and publishes the Catalogus Basisregistratie WOZ and the
  IMWOZ information model, which specify the content of the base registry,
  the content of the national facility, and the further registration
  municipalities keep for the implementation of the Wet WOZ.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-WOZ
  - NL-KADASTER
relationships:
  - type: applies-to
    target: NL-WET-WOZ
    source: fact
    evidence: "Confirmed by reading waarderingskamer.nl's own pages directly (2026-08-27): 'De taken en bevoegdheden van de Waarderingskamer zijn afgeleid van artikel 4 van de Wet WOZ' (the Waarderingskamer's tasks and powers derive from Article 4 of the Wet WOZ), and separately, 'De Waarderingskamer houdt toezicht op de uitvoering van de Wet waardering onroerende zaken (Wet WOZ) door gemeenten.' rijksoverheid.nl's contact-guide entry, also read directly, confirms the Waarderingskamer falls under the Ministerie van Financiën."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Catalogus Basisregistratie WOZ versie 1.8 (fetched; binary PDF, not machine-readable)"
    url: "https://www.waarderingskamer.nl/documenten/03.-Voor-gemeenten/04.-Gegevensbeheer/Catalogus-Basisregistratie-WOZ-versie-1.8.pdf"
    publisher: "Waarderingskamer"
  - title: "Landelijke Voorziening WOZ (503 error this pass, not read)"
    url: "https://www.waarderingskamer.nl/voor-gemeenten/gegevensbeheer/lv-woz"
    publisher: "Waarderingskamer"
  - title: "IMWOZ — informatiemodel (confirmed dead, HTTP 404)"
    url: "https://www.waarderingskamer.nl/documenten/imwoz-models/IMWOZ-model-03.12/cat/index.html"
    publisher: "Waarderingskamer"
  - title: "Catalogus WOZ-gegevens voor afnemers versie 1.8 (fetched; binary PDF, not machine-readable)"
    url: "https://www.waarderingskamer.nl/uploads/documents/03.-Voor-gemeenten/04.-Gegevensbeheer/Catalogus-WOZ-gegevens-voor-afnemers-versie-1.8.pdf"
    publisher: "Waarderingskamer"
  - title: "Over ons"
    url: "https://www.waarderingskamer.nl/over-ons"
    publisher: "Waarderingskamer"
    accessed: "2026-08-27"
  - title: "Wie zijn wij — onafhankelijke toezichthouder op de Wet WOZ"
    url: "https://www.waarderingskamer.nl/over-ons/wie-zijn-wij"
    publisher: "Waarderingskamer"
    accessed: "2026-08-27"
  - title: "Wat wij doen"
    url: "https://www.waarderingskamer.nl/over-ons/wat-wij-doen"
    publisher: "Waarderingskamer"
    accessed: "2026-08-27"
  - title: "Ons toezicht"
    url: "https://www.waarderingskamer.nl/over-ons/ons-toezicht"
    publisher: "Waarderingskamer"
    accessed: "2026-08-27"
  - title: "Waarderingskamer — Rijksoverheid contactgids"
    url: "https://www.rijksoverheid.nl/contact/contactgids/waarderingskamer"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
---

# Waarderingskamer

> **Verified 2026-08-27.** All four originally cited pages proved
> unreadable this pass — two Waarderingskamer PDFs are binary with no
> extractable text, the LV-WOZ page returned a 503, and the IMWOZ page
> returns HTTP 404 — so five replacement pages from waarderingskamer.nl and
> rijksoverheid.nl were found and read directly, establishing a genuine
> majority (5 of 9 total sources) where the original four could not.

## Description

The Waarderingskamer is an **independent administrative body (zbo)** under
the Ministerie van Financiën, confirmed by reading its own "wie zijn wij"
page and rijksoverheid.nl's contact-guide entry directly this pass. Its
tasks and powers derive from **Article 4 of the Wet WOZ**: it supervises
whether municipalities properly implement the Act, advises the State
Secretary of Finance, arbitrates disputes between municipalities and WOZ
data users (named on its own page as the Tax Authority and the water
boards), and provides a consultation platform for stakeholders.

Its own "ons toezicht" page, read directly this pass, describes a
risk-based inspection regime: roughly 80 municipalities receive direct
inspection visits each year, others are assessed by questionnaire, and
municipalities with weaker valuation quality receive intensified oversight
and mandatory improvement plans.

The four originally cited Waarderingskamer publications — the WOZ catalogue,
the LV-WOZ page, the IMWOZ model and the afnemers catalogue — describe it
additionally as the **functional manager of the Landelijke Voorziening WOZ**
and the publisher of the IMWOZ information model, but none of the four was
readable this pass (see the Verified banner). Those claims are carried over
from the prior pass's sourcing and corroborated indirectly by kadaster.nl's
own LV-WOZ page (read for [[NL-WOZ]] this pass), which independently states
the Waarderingskamer is "functioneel beheerder van de LV-WOZ."

## A supervisor that is also a specification author

Most base registries in the stelsel separate the supervisor from the party
that defines the data. The WOZ does not: the Waarderingskamer both
**supervises** municipalities' implementation and **authors the information
model** they must implement.

That is why this entity is `maintained-by` on [[NL-WOZ]] rather than
something weaker. The Atlas's `maintained-by` means the target maintains the
entity, and the specification role is what makes it apt here — even though
the *data* comes from municipalities and the *technical* national facility
is run by [[NL-KADASTER]].

The WOZ is the clearest case in the stelsel of **three organisations having
distinct roles in one register**, and it is the reason `digitaleoverheid.nl`
describes the stelsel in terms of separate roles — initiator, supervisor,
provider, holder — rather than a single owner per register. See [[NL-WOZ]].

## `coverage: low`, narrower now

Its legal form (zbo) and ministerial home (Financiën) are now confirmed.
Its composition, founding date and funding remain unrecorded — nothing read
this pass gave a founding date for the body itself, as distinct from the
1995 Wet WOZ that created its role.

## Relationships

- `applies-to` [[NL-WET-WOZ]] — confirmed this pass: the Act is the direct
  statutory source of the Waarderingskamer's own tasks and powers (Article
  4), not merely a law the WOZ register happens to sit under.

[[NL-WOZ]] separately carries the `maintained-by` edge pointing here.

## Sources

Listed in frontmatter. All four originally cited pages are confirmed
unreadable this pass (two binary PDFs, one 503, one HTTP 404) — noted
explicitly rather than silently dropped. Five replacement pages from
waarderingskamer.nl and rijksoverheid.nl were found via WebSearch and read
directly, establishing this entity's majority.
