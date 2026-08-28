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
coverage: medium
verification: primary-source

start_date: 2016-07-06
end_date: 2024-10-18
last_verified: "2026-08-28"
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
  - title: "The Directive on security of network and information systems (NIS Directive)"
    url: "https://digital-strategy.ec.europa.eu/en/library/directive-security-network-and-information-systems-nis-directive"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "NIS2 Directive"
    url: "https://en.wikipedia.org/wiki/NIS2_Directive"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Directive (EU) 2022/2555 (NIS2) — Official Journal, repealing Directive (EU) 2016/1148"
    url: "https://eur-lex.europa.eu/eli/dir/2022/2555/2022-12-27/eng"
    publisher: "EUR-Lex (Publications Office of the European Union)"
---

# NIS Directive (Directive (EU) 2016/1148)

> **Re-verified 2026-08-28.** A new Commission source was found and read
> directly — the Commission's own library page on the original NIS
> Directive — closing this entity's previously-flagged gap of an
> unrecorded adoption date and transposition timeline. Wikipedia's NIS2
> article was also read directly and confirms the repeal date. The
> repealing directive's own EUR-Lex ELI record returned empty content,
> consistent with every other EUR-Lex attempt made across this batch, and
> was not read. `verification` moves from `search-only` to
> `primary-source`; `coverage` moves from `low` to `medium`.

## Description

Directive (EU) 2016/1148 set measures for a high common level of security of
network and information systems across the Union — the EU's first
cross-sector cybersecurity legislation. Confirmed by reading the
Commission's own library page directly: it was **adopted by the European
Parliament on 6 July 2016** (recorded here as `start_date`, closing this
entity's previous gap) with the aim of "bring[ing] cybersecurity
capabilities at the same level of development in all the EU Member
States." Member states had **21 months to transpose** it into national
law, plus **6 further months** to identify operators of essential services
— placing the transposition deadline at 9 May 2018, corroborated via a
WebSearch cross-check of independent legal trackers rather than a source
read directly, and not added to frontmatter on that weaker basis.

It was **repealed by [[EU-NIS2]] with effect from 18 October 2024**, which
is recorded as `end_date` — confirmed by reading Wikipedia's NIS2 article
directly: "the earlier NIS Directive was repealed on 18 October 2024."

`coverage: medium`, up from `low`: adoption date and the outline of the
transposition timetable are now confirmed from a Commission source read
directly, though the directive's substantive obligations (security
requirements, incident-notification thresholds, national competent
authorities) remain unresearched.

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

Listed in frontmatter, two of three read directly this pass — the
Commission's own library page on the original NIS Directive, and
Wikipedia's NIS2 article. The repealing directive's EUR-Lex ELI record
returned empty content and was not read; still listed as the authoritative
citation for the repeal itself.
