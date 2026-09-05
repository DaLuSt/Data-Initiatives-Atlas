---
id: NL-GDI
type: platform
name: Generieke Digitale Infrastructuur
alternative_names:
  - GDI
description: >
  The Netherlands' generic digital infrastructure: the set of shared digital
  facilities, standards and services used across government and by
  organisations with a public task. Services within it are operated by
  Logius; its modernisation is programmed through MIDO.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-LOGIUS
  - NL-BZK
related_entities:
  - NL-MIDO
relationships:
  - type: maintained-by
    target: NL-LOGIUS
    source: fact
    evidence: "GDI services are described as managed by Logius; from 2023 several moved to central BZK budget (logius.nl, rijksfinancien.nl)."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Facturatie GDI-diensten 2023 is veranderd"
    url: "https://www.logius.nl/actueel/facturatie-gdi-diensten-2023-veranderd"
    publisher: "Logius"
    accessed: "2026-08-20"
  - title: "Stelsel van het heden (Stelseldiensten ter ondersteuning)"
    url: "https://www.noraonline.nl/wiki/Stelsel_van_het_heden_(Stelseldiensten_ter_ondersteuning)"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-20"
  - title: "Wat is het MIDO?"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/wat-is-het-mido/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-20"
  - title: "Generieke Digitale Infrastructuur (GDI)"
    url: "https://www.digitaleoverheid.nl/mido/generieke-digitale-infrastructuur-gdi/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-05"
  - title: "GDI: Gezamenlijke Digitale Infrastructuur"
    url: "https://ibestuur.nl/artikel/gdi-gezamenlijke-digitale-infrastructuur/"
    publisher: "iBestuur"
    accessed: "2026-09-05"
    note: "A 2017 opinion piece proposing 'Gezamenlijke' as a deliberate reframing away from the official 'Generieke' name, not evidence of an alternate official name — see body."
---

# Generieke Digitale Infrastructuur (GDI)

> **Verified 2026-08-20.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.
>
> **Updated 2026-09-05**: the "Generieke" vs "Gezamenlijke" name question
> is resolved. See below.

## Description

The GDI is the Netherlands' generic digital infrastructure: shared digital
facilities, standards and services reused across government rather than
rebuilt per organisation. Services commonly named as part of it include
DigiD, DigiD Machtigen and MijnOverheid, operated by [[NL-LOGIUS]]. From
2023 the funding model for several of these changed, with the services
moving to a central budget managed by [[NL-BZK]] instead of being invoiced
to using organisations.

Its modernisation is programmed through [[NL-MIDO]].

`coverage: low`: the individual GDI services are not yet Atlas entities, and
the boundary of what counts as "in" the GDI has not been established from a
source.

## The name, resolved 2026-09-05

digitaleoverheid.nl's own dedicated GDI page, read directly, uses
**"Generieke Digitale Infrastructuur"** exclusively and never
"Gezamenlijke." The "Gezamenlijke" rendering traces to a single source: an
iBestuur opinion piece from **20 September 2017**, titled "GDI:
Gezamenlijke Digitale Infrastructuur," which opens by arguing the official
"Generieke" framing contains a *"denkfout"* (conceptual flaw) and
deliberately proposes "Gezamenlijke" instead, to emphasise cooperative
governance over technical standardisation. That is a policy argument for
a rename, made once in 2017, not evidence the name changed or that
"Gezamenlijke" was ever official. The government's own current usage is
unambiguous: **"Generieke Digitale Infrastructuur"** is correct, and
`alternative_names` is not expanded to include "Gezamenlijke."

The typing as `platform` is an Atlas judgement: the GDI is a collection of
systems and agreements rather than a single system, so `platform` and
`framework` are both partly apt. Flagged for review.

## Relationships

- Services operated by [[NL-LOGIUS]]; funded/steered via [[NL-BZK]].
- Modernised through [[NL-MIDO]].

## Atlas interpretation

Entity typing and the scope boundary of the GDI are Atlas interpretations.

## Sources

Listed in frontmatter.
