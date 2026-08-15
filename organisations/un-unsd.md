---
id: UN-UNSD
type: organisation
name: United Nations Statistics Division
alternative_names:
  - UNSD
description: >
  Division of the UN Secretariat that coordinates international statistical
  activities and supports the UN Statistical Commission, the apex entity of
  the global statistical system. It maintains the Fundamental Principles of
  Official Statistics and compiles the SDG indicator dataset.

level: international
country: null
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
  - UN
  - UN-FPOS
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "The UN Statistics Division facilitates coordination of international statistical activities and supports the functioning of the UN Statistical Commission as the apex entity of the global statistical system (unstats.un.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Fundamental Principles of Official Statistics"
    url: "https://unstats.un.org/fpos/"
    publisher: "United Nations Statistics Division"
  - title: "Principles governing international statistical activities"
    url: "https://unstats.un.org/unsd/methods/statorg/principles_stat_activities/principles_stat_activities.asp"
    publisher: "United Nations Statistics Division"
---

# United Nations Statistics Division (UNSD)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The UNSD coordinates international statistical activities and supports the
**UN Statistical Commission**, described as the apex entity of the global
statistical system. It maintains [[UN-FPOS]] and compiles the SDG indicator
dataset from officially recognised international sources.

**The UN Statistical Commission is not modelled separately.** It is the
intergovernmental body; UNSD is the secretariat serving it. Splitting them
would be more accurate but rests on a single sourced sentence, so they are
folded into one entity with the distinction noted here. Queued as a
modelling question — the same treatment given to [[NL-HEALTH-RI]]
(organisation vs infrastructure) and [[EU-EHDS]] (regulation vs data space).

`coverage: low`.

## Position in the statistical chain

```
UN-UNSD / Statistical Commission   (global apex)
     ↓  (relationship unsourced)
EU-EUROSTAT / European Statistical System
     ↓  participates-in
NL-CBS
```

The lower link is recorded; **the upper one is not**, because no source read
connects the European Statistical System to the UN statistical system. This
is one of the clearest remaining gaps in the Atlas's vertical structure.

## Relationships

- Part of [[UN]].
- Maintains [[UN-FPOS]].

## Sources

Listed in frontmatter.
