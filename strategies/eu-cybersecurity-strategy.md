---
id: EU-CYBERSECURITY-STRATEGY
type: strategy
name: The EU's Cybersecurity Strategy for the Digital Decade
alternative_names:
  - EU Cybersecurity Strategy
description: >
  Joint Communication of the European Commission and the High Representative
  presented on 16 December 2020, setting out how the EU will shield people,
  businesses and institutions from cyber threats and advance international
  cooperation. Presented as part of a package that also contained the
  proposals for the NIS2 and Critical Entities Resilience directives.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2020-12-16
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-NIS2
  - EU-CER
relationships:
  - type: influences
    target: EU-CER
    source: fact
    evidence: "The December 2020 cybersecurity package comprised the Strategy, the NIS2 proposal and the proposal for the directive on the resilience of critical entities (digital-strategy.ec.europa.eu; encavibs.uni.lu). NOT READ — search-only."
    confidence: medium
    valid_from: 2020-12-16
    valid_until: null
  - type: influences
    target: EU-NIS2
    source: fact
    evidence: "The December 2020 cybersecurity package consisted of three documents: the Cybersecurity Strategy for the Digital Decade, a proposal for the directive on measures for a high common level of cybersecurity across the Union (NIS2), and a proposal for the directive on the resilience of critical entities (digital-strategy.ec.europa.eu; encavibs.uni.lu). NOT READ — search-only."
    confidence: medium
    valid_from: 2020-12-16
    valid_until: null

sources:
  - title: "The EU's Cybersecurity Strategy for the Digital Decade"
    url: "https://digital-strategy.ec.europa.eu/en/library/eus-cybersecurity-strategy-digital-decade"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "EU Cybersecurity Strategy"
    url: "https://digital-strategy.ec.europa.eu/en/policies/cybersecurity-strategy"
    publisher: "European Commission — Shaping Europe's digital future"
---

# The EU's Cybersecurity Strategy for the Digital Decade

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

On 16 December 2020 the European Commission and the High Representative of
the Union for Foreign Affairs and Security Policy presented a new EU
Cybersecurity Strategy. It responds to the cyber-related challenges of
increasing digitalisation, dependence on modern technologies and complex
threats, setting out how the EU will shield its people, businesses and
institutions from cyber threats and how it will advance international
cooperation and lead in securing a global and open internet.

The strategy was one of **three documents in a single cybersecurity
package**, alongside the proposal for the directive on measures for a high
common level of cybersecurity across the Union — which became
[[EU-NIS2]] — and the proposal for the directive on the resilience of
critical entities (CER).

Its content includes integrating cybersecurity into all digital investments,
particularly AI, encryption and quantum computing, and a proposed network of
security operations centres for AI-powered threat intelligence, described as
an EU Cyber Shield.

## This completes a three-level chain

With this entity the Atlas can trace a full policy-to-implementation
descent:

```
EU-CYBERSECURITY-STRATEGY   (strategy, Dec 2020)
        │ influences
        ▼
EU-NIS2                     (directive, Dec 2022)
        │ implemented by
        ▼
NL-CBW                      (Dutch act, in force Aug 2026)
        │ supersedes
        ▼
NL-WBNI                     (predecessor Dutch act)
```

This is the vertical relationship pattern the brief's final relationship
pass calls for, and the first instance in the Atlas that spans strategy,
EU legislation and national implementation together.

The `influences` relationship type is used rather than `produces` because
the strategy and the NIS2 proposal were presented together as a package —
the strategy did not straightforwardly produce the directive, and the
sourced statement is about co-presentation.

## Relationships

- Influences [[EU-NIS2]] and [[EU-CER]].

Batch 8 added [[EU-CER]], so **all three elements of the December 2020
package are now represented**: the strategy itself plus both directives it
was presented alongside. The Dutch counterpart to CER (Wet weerbaarheid
kritieke entiteiten, approved by the Tweede Kamer on 15 April 2026 alongside
the Cyberbeveiligingswet) remains queued from Batch 3.

## Sources

Listed in frontmatter.
