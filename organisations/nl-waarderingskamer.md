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
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-WOZ
  - NL-KADASTER
relationships: []

sources:
  - title: "Catalogus Basisregistratie WOZ versie 1.8"
    url: "https://www.waarderingskamer.nl/documenten/03.-Voor-gemeenten/04.-Gegevensbeheer/Catalogus-Basisregistratie-WOZ-versie-1.8.pdf"
    publisher: "Waarderingskamer"
  - title: "Landelijke Voorziening WOZ"
    url: "https://www.waarderingskamer.nl/voor-gemeenten/gegevensbeheer/lv-woz"
    publisher: "Waarderingskamer"
  - title: "IMWOZ — informatiemodel"
    url: "https://www.waarderingskamer.nl/documenten/imwoz-models/IMWOZ-model-03.12/cat/index.html"
    publisher: "Waarderingskamer"
  - title: "Catalogus WOZ-gegevens voor afnemers versie 1.8"
    url: "https://www.waarderingskamer.nl/uploads/documents/03.-Voor-gemeenten/04.-Gegevensbeheer/Catalogus-WOZ-gegevens-voor-afnemers-versie-1.8.pdf"
    publisher: "Waarderingskamer"
---

# Waarderingskamer

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Waarderingskamer supervises whether municipalities properly implement
the **Wet WOZ**, and supervises the implementation of [[NL-WOZ]].

It is also the **functional manager of the Landelijke Voorziening WOZ**, and
it publishes the specifications that define the register: the *Catalogus
Basisregistratie WOZ*, the *Catalogus WOZ-gegevens voor afnemers*, and the
**IMWOZ** information model. IMWOZ is the basis for the content of the base
registry, the content of the national facility, and the further registration
municipalities keep.

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

## `coverage: low`

Its legal form, composition, founding date and funding are unrecorded; all
four sources are its own publications about the WOZ.

## Relationships

None asserted from this entity. [[NL-WOZ]] carries the `maintained-by` edge
pointing here.

## Sources

Listed in frontmatter.
