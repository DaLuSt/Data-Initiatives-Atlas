---
id: NL-CBW
type: law
name: Cyberbeveiligingswet
alternative_names:
  - Cbw
  - Dutch Cybersecurity Act
description: >
  Dutch implementing act for the EU NIS2 Directive, in force since 15 August
  2026. It obliges roughly 8,000 organisations in critical and important
  sectors to register, meet cybersecurity requirements, and report
  incidents under a staged notification regime. It replaces the Wet
  beveiliging netwerk- en informatiesystemen.

level: national
country: NL
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2026-08-15
end_date: null
last_verified: "2026-08-27"
previous_version: NL-WBNI
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - EU-NIS2
  - NL-WBNI
  - NL-NCSC
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Confirmed by reading ncsc.nl's own 'Cyberbeveiligingswet (NIS2)' page directly (2026-08-27): 'De Cyberbeveiligingswet (Cbw) is de Nederlandse implementatie van de Europese NIS2-richtlijn.' nctv.nl's own page, also read directly, corroborates."
    confidence: high
    valid_from: 2026-08-15
    valid_until: null
  - type: supersedes
    target: NL-WBNI
    source: fact
    evidence: "Confirmed by reading both ncsc.nl and nctv.nl directly (2026-08-27): 'De Cbw vervangt de oude Wet beveiliging netwerk- en informatiesystemen (Wbni)', which the Cbw's own entry into force on 15 August 2026 confirms has now happened, not merely 'is scheduled to happen'."
    confidence: high
    valid_from: 2026-08-15
    valid_until: null

sources:
  - title: "Cyberbeveiligingswet (NIS2)"
    url: "https://www.ncsc.nl/cyberbeveiligingswet-nis2"
    publisher: "Nationaal Cyber Security Centrum (NCSC)"
    accessed: "2026-08-27"
  - title: "Cyberbeveiligingswet"
    url: "https://www.nctv.nl/onderwerpen/c/cyberbeveiligingswet"
    publisher: "Nationaal Coördinator Terrorismebestrijding en Veiligheid (NCTV)"
    accessed: "2026-08-27"
  - title: "Tweede Kamer stemt in met wetsvoorstellen Cyberbeveiligingswet en Wet weerbaarheid kritieke entiteiten"
    url: "https://www.rijksoverheid.nl/actueel/nieuws/2026/04/15/tweede-kamer-stemt-in-met-wetsvoorstellen-cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
  - title: "Implementatie NIS2 en CER in Nederland vertraagd, wat betekent dat voor u?"
    url: "https://www.rijksoverheid.nl/actueel/nieuws/2024/10/23/implementatie-nis2-en-cer-in-nederland-vertraagd-wat-betekent-dat-voor-u"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
  - title: "Cyberbeveiligingswet (NIS2-richtlijn)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cyberbeveiligingswet/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
---

# Cyberbeveiligingswet (Cbw)

> **Verified 2026-08-27.** Four of five cited pages were read directly this
> pass; `digitaleoverheid.nl` returned a bot-verification interstitial with
> no substantive content and was not readable. This is a **major status
> correction**: the previous entry recorded `status: planned` because it
> was written one day before the act's stated entry-into-force date and
> could not confirm the date had held. Reading `ncsc.nl`'s and `nctv.nl`'s
> own current pages directly, both dated well after 15 August 2026, confirm
> in as many words that the Cbw **has** entered into force on that date. It
> is promoted to `status: active` accordingly, and [[NL-WBNI]] to
> `superseded`.

## Description

The Cyberbeveiligingswet is the Dutch implementation of [[EU-NIS2]]. Both
`ncsc.nl` and `nctv.nl`, read directly, state without qualification: "De
Cyberbeveiligingswet is in werking getreden op 15 augustus 2026." It
requires organisations in critical and important sectors to:

1. **Register** in the entity registry via MijnNCSC.
2. Exercise a **duty of care**: map the risks to their network and
   information systems' security.
3. Meet a **staged incident-reporting** obligation: an early warning within
   24 hours of becoming aware of a significant incident, an incident report
   with an initial assessment within 72 hours, and a final report within
   one month.
4. Ensure **board-level responsibility**: management must approve
   cybersecurity measures, oversee implementation, and hold adequate
   knowledge to identify risks.

Both pages read directly give the scope as **roughly 8,000 organisations**,
determined by sector and by size criteria (employee count, turnover,
balance-sheet total).

It replaces [[NL-WBNI]]. Organisations already covered by the Wbni retained
their rights and obligations under that act until the Cbw's entry into
force — which, per the sources read this pass, has now happened.

The Dutch transposition was late: the government publicly acknowledged in
October 2024 that implementation of NIS2 and CER had been delayed, at that
point targeting Q3 2025. The Tweede Kamer approved the bill (alongside the
Wet weerbaarheid kritieke entiteiten) on 15 April 2026, with the Eerste
Kamer's subsequent approval and the government's Q2-2026 target for
simultaneous entry into force of both acts. The eventual in-force date —
15 August 2026 — slipped past that Q2 target but is now confirmed directly.

## Competent authorities and the NCSC

Oversight is distributed sector-by-sector through a "doorverwijsboom"
(routing tree) of competent authorities and CSIRTs, per `nctv.nl`, read
directly. [[NL-NCSC]] is confirmed — also directly, on its own
Cyberbeveiligingswet page — to be the **sectoral CSIRT** that registered
organisations connect to for incident-reporting services; it is not
described as the sole government-wide authority. See [[NL-NCSC]] for the
relationship, upgraded this pass from `interpretation` to `fact`.

## Temporal note, resolved

The previous pass recorded this entity the day before its stated
entry-into-force date, deliberately flagging that the date might not hold.
It has now held: two independent official pages, both read directly and
both dated after 15 August 2026, confirm the act is in force. `status` is
updated to `active`, `start_date` remains `2026-08-15`, and [[NL-WBNI]]'s
`status` is updated to `superseded` with `end_date: 2026-08-15` accordingly.

## Classification

Dutch implementation legislation per `metadata/taxonomy.md` §2:
`type: law`, `level: national`, `country: NL`, `region: EU`.

## Relationships

- Implements requirements from [[EU-NIS2]].
- Supersedes [[NL-WBNI]] (confirmed in force from 15 August 2026).
- [[NL-NCSC]] applies to it as sectoral CSIRT.

## Sources

Four of five read directly this pass: both `ncsc.nl` and `nctv.nl` current
pages, and both `rijksoverheid.nl` news items. `digitaleoverheid.nl` was
blocked by a bot-verification interstitial and returned no readable
content.
