---
id: NL-CBW
type: law
name: Cyberbeveiligingswet
alternative_names:
  - Cbw
  - Dutch Cybersecurity Act
description: >
  Dutch implementing act for the EU NIS2 Directive. It obliges organisations
  in critical sectors to meet cybersecurity requirements, report incidents
  under a staged notification regime, and register with the supervisory
  authority. It replaces the Wet beveiliging netwerk- en informatiesystemen.

level: national
country: NL
region: EU

status: planned
confidence: low
coverage: medium
verification: search-only

start_date: 2026-08-15
end_date: null
last_verified: null
previous_version: NL-WBNI
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-NIS2
  - NL-WBNI
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "The Cyberbeveiligingswet is the Dutch implementation of the European NIS2 directive (ncsc.nl/cyberbeveiligingswet-nis2; nctv.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: supersedes
    target: NL-WBNI
    source: fact
    evidence: "The Cbw replaces the Wet beveiliging netwerk- en informatiesystemen; rights and obligations under the Wbni continue until the Cbw enters into force and the Wbni is withdrawn (ncsc.nl). NOT READ — search-only."
    confidence: medium
    valid_from: 2026-08-15
    valid_until: null

sources:
  - title: "Cyberbeveiligingswet (NIS2)"
    url: "https://www.ncsc.nl/cyberbeveiligingswet-nis2"
    publisher: "Nationaal Cyber Security Centrum (NCSC)"
  - title: "Cyberbeveiligingswet"
    url: "https://www.nctv.nl/onderwerpen/c/cyberbeveiligingswet"
    publisher: "Nationaal Coördinator Terrorismebestrijding en Veiligheid (NCTV)"
  - title: "Tweede Kamer stemt in met wetsvoorstellen Cyberbeveiligingswet en Wet weerbaarheid kritieke entiteiten"
    url: "https://www.rijksoverheid.nl/actueel/nieuws/2026/04/15/tweede-kamer-stemt-in-met-wetsvoorstellen-cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten"
    publisher: "Rijksoverheid"
  - title: "Implementatie NIS2 en CER in Nederland vertraagd, wat betekent dat voor u?"
    url: "https://www.rijksoverheid.nl/actueel/nieuws/2024/10/23/implementatie-nis2-en-cer-in-nederland-vertraagd-wat-betekent-dat-voor-u"
    publisher: "Rijksoverheid"
  - title: "Cyberbeveiligingswet (NIS2-richtlijn)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cyberbeveiligingswet/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
---

# Cyberbeveiligingswet (Cbw)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Cyberbeveiligingswet is the Dutch implementation of [[EU-NIS2]]. It
requires organisations in critical sectors to meet cybersecurity
requirements, to report incidents, and to register with the supervisory
authority. Its notification regime is staged: an early warning within 24
hours of becoming aware of a significant incident, an incident report with
an initial assessment within 72 hours, and a final report within one month.

It replaces [[NL-WBNI]]. Organisations already covered by the Wbni retain
their rights and obligations under that act until the Cbw enters into force
and the Wbni is withdrawn.

The Dutch transposition was late: the government publicly acknowledged in
October 2024 that implementation of NIS2 and CER had been delayed. The
Tweede Kamer approved the bill on 15 April 2026.

## Temporal note

`status: planned` with `start_date: 2026-08-15`. Search results state the
Cbw enters into force on 15 August 2026 — **the day after this entry was
written** (2026-08-14). It is therefore recorded as adopted-but-not-yet-in-
force, which is what `planned` denotes here.

This entry will be wrong within a day if the date holds and nobody updates
it, which makes it a good illustration of why `last_verified` exists and why
`status` must never be inferred from a stale snapshot. Anyone reading this
after 15 August 2026 should verify and, if confirmed, move `status` to
`active` and set [[NL-WBNI]] to `superseded`.

## Classification

Dutch implementation legislation per `metadata/taxonomy.md` §2:
`type: law`, `level: national`, `country: NL`, `region: EU`.

## Relationships

- Implements requirements from [[EU-NIS2]].
- Supersedes [[NL-WBNI]] (from the date it enters into force).

## Sources

Listed in frontmatter.
