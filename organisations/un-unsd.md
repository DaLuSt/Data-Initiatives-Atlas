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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading both cited unstats.un.org pages directly (2026-08-28). The FPOS page is maintained by UNSD and states the Division's role in stewarding the Principles; the methods page describes UNSD's coordination role across international statistical activities. Neither page is a dedicated UNSD 'about' page, so the claim is corroborated rather than quoted verbatim — the same limitation this entity's `coverage: low` already flags."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: UN-UNSC
    source: fact
    evidence: "Confirmed via [[UN-UNSC]]'s own re-verification this pass (2026-08-28): un.org/en/desa's 'Shaping the future of global statistics' page, read directly, states the Statistics Division of DESA 'supports the Commission's work by serving as its secretariat.' unstats.un.org/UNSDWebsite/statcom/ was fetched but returned only a bare page-title shell with no readable body content; officialstatistics.org §17.3 returned HTTP 403 and was not read."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Fundamental Principles of Official Statistics"
    url: "https://unstats.un.org/fpos/"
    publisher: "United Nations Statistics Division"
    accessed: "2026-08-28"
  - title: "Principles governing international statistical activities"
    url: "https://unstats.un.org/unsd/methods/statorg/principles_stat_activities/principles_stat_activities.asp"
    publisher: "United Nations Statistics Division"
    accessed: "2026-08-28"
---

# United Nations Statistics Division (UNSD)

> **Verified 2026-08-28.** Both cited pages were read directly. Neither is a
> dedicated "about UNSD" page — they are the FPOS and methods pages this
> entity shares with [[UN-FPOS]] — so the promotion rests on corroboration
> across UNSD's own published material rather than a single definitive
> "about us" statement. The `governed-by` [[UN-UNSC]] edge is additionally
> confirmed via that entity's own re-verification this pass.

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

Listed in frontmatter, both read directly this pass.
