---
id: EU-NIS
type: directive
name: NIS Directive
alternative_names:
  - Directive (EU) 2016/1148
  - Network and Information Security Directive
description: >
  EU directive on measures for a high common level of security of network
  and information systems across the Union — the first EU-wide cybersecurity
  legislation. Repealed by the NIS2 Directive with effect from 18 October
  2024.

level: regional
country: null
region: EU

status: superseded
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: 2024-10-18
last_verified: null
previous_version: null
successor: EU-NIS2

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - EU-NIS2
  - NL-WBNI
relationships: []

sources:
  - title: "Directive (EU) 2022/2555 (NIS2) — Official Journal, repealing Directive (EU) 2016/1148"
    url: "https://eur-lex.europa.eu/eli/dir/2022/2555/2022-12-27/eng"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "NIS2 Directive"
    url: "https://en.wikipedia.org/wiki/NIS2_Directive"
    publisher: "Wikipedia"
---

# NIS Directive (Directive (EU) 2016/1148)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Directive (EU) 2016/1148 set measures for a high common level of security of
network and information systems across the Union — the EU's first
cross-sector cybersecurity legislation. It was **repealed by [[EU-NIS2]]
with effect from 18 October 2024**, which is recorded as `end_date`.

`coverage: low`: created for structural completeness rather than researched.
Its own content, adoption date and transposition deadline are unrecorded.

## What this entity closes

Batch 3 created [[NL-WBNI]], the Dutch act implementing the original NIS
regime, and left its upstream link dangling because this directive did not
exist as an entity. That gap is now closed — see the relationship recorded
on `NL-WBNI`.

The result is a complete parallel pair of chains:

```
EU-NIS   → NL-WBNI     (original regime, both now ending)
   │supersedes  │supersedes
   ▼            ▼
EU-NIS2  → NL-CBW      (successor regime)
```

Both levels of the supersession happened, at different times and for
different reasons: the EU repeal took effect 18 October 2024, while the
Dutch replacement was delayed until August 2026 — a gap the Netherlands
publicly acknowledged. The Atlas can now represent that lag, which is
precisely the kind of temporal detail the brief's §11 asks for.

## Relationships

- Superseded by [[EU-NIS2]] from 18 October 2024 (recorded on that entity).
- Implemented in the Netherlands by [[NL-WBNI]] (recorded on that entity).

## Sources

Listed in frontmatter. Note both are indirect — the repealing directive and
a secondary article — rather than the directive's own text.
