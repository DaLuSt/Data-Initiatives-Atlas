---
id: NL-WBNI
type: law
name: Wet beveiliging netwerk- en informatiesystemen
alternative_names:
  - Wbni
description: >
  Dutch act on the security of network and information systems,
  implementing the original EU NIS Directive. Superseded by the
  Cyberbeveiligingswet, which implements NIS2 and entered into force on
  15 August 2026.

level: national
country: NL
region: EU

status: superseded
confidence: high
coverage: low
verification: primary-source

start_date: 2018-11-09
end_date: 2026-08-15
last_verified: "2026-09-05"
previous_version: null
successor: NL-CBW

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - NL-CBW
  - EU-NIS
relationships:
  - type: implements-requirement-from
    target: EU-NIS
    source: fact
    evidence: "Confirmed by reading the Wbni's own official text directly on wetten.overheid.nl (2026-08-28, BWBR0041515): the law's own preamble states it is 'necessary to establish legal provisions to promote the security of network and information systems' in accordance with EU Directive 2016/1148, and its full title names 'richtlijn (EU) 2016/1148' directly. This is the Wbni's own text confirming its own basis — the strongest possible source for this edge, resolving what the prior pass could not find. The page also confirms the law's own repeal: 'Deze regeling is ingetrokken. Dit is geen geldige regeling meer' (this regulation has been withdrawn, it is no longer valid), with 15 August 2026 as the date it ceased to have effect."
    confidence: high
    valid_from: null
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
  - title: "Wet beveiliging netwerk- en informatiesystemen — BWBR0041515"
    url: "https://wetten.overheid.nl/BWBR0041515"
    publisher: "Overheid.nl (wetten.overheid.nl)"
    accessed: "2026-08-28"
  - title: "Staatsblad 2018, 389 — commencement decree"
    url: "https://zoek.officielebekendmakingen.nl/stb-2018-389.html"
    publisher: "Overheid.nl (officiële bekendmakingen)"
    accessed: "2026-09-05"
---

# Wet beveiliging netwerk- en informatiesystemen (Wbni)

> **Promoted to `primary-source` 2026-08-28.** The Wbni's own official
> text was found and read directly this pass on wetten.overheid.nl
> (BWBR0041515) — exactly the citation the prior pass could not locate.
> Its own preamble confirms it implements EU Directive 2016/1148 (the
> original NIS Directive), and the page confirms the law's repeal, in its
> own words, effective 15 August 2026. The page's own Article 35 leaves
> the law's commencement to a royal decree "to be determined," without
> stating the actual date the decree set — recorded as an unconfirmed
> lead for a future pass.
>
> **That lead is now closed, 2026-09-05.** The commencement decree itself
> — Staatsblad 2018, 389, read directly — states verbatim: *"Met ingang
> van 9 november 2018 treden in werking: a. de Wet beveiliging netwerk- en
> informatiesystemen..."* (with effect from 9 November 2018, the following
> enter into force: a. the Wet beveiliging netwerk- en informatiesystemen).
> `start_date` is set to **2018-11-09** accordingly; a small number of
> CSIRT/digital-service-provider-specific provisions commenced later, on 1
> January 2019, per the same decree — not adopted as the entity's own
> `start_date` since it describes specific provisions, not the Act as a
> whole. `confidence` raised to `high`.

## Description

The Wbni was the Dutch act on the security of network and information
systems. It was the predecessor regime to [[NL-CBW]]: organisations covered
by the Wbni kept their rights and obligations under it until the
Cyberbeveiligingswet entered into force, at which point the Wbni was
withdrawn. Both `ncsc.nl` and `nctv.nl`, read directly this pass, confirm
in their own words that "De Cbw vervangt de oude Wet beveiliging netwerk-
en informatiesystemen (Wbni)" and that the Cbw is now in force.

`coverage: low` deliberately, and still. This entity exists chiefly to make
the supersession chain expressible — a superseded instrument must be
retained, not deleted, for the Atlas to reconstruct the landscape at a past
point in time (brief §11).

**Confirmed by reading the Wbni's own text directly this pass (2026-08-28,
wetten.overheid.nl, BWBR0041515):** the law's own preamble states it is
"necessary to establish legal provisions to promote the security of network
and information systems" in accordance with EU Directive 2016/1148 — the
original NIS Directive — and its full title names that directive directly.
The original NIS Directive is not yet an Atlas entity in its own right
([[EU-NIS]] is referenced as a placeholder target for this edge); this is
still the first time this entity's own basis has been confirmed from its
own text rather than inferred from its successor's documentation. The
page's own Article 35 left the law's commencement to a royal decree without
stating the date that decree set. **That decree is now read directly
(2026-09-05)**: Staatsblad 2018, 389 states verbatim "Met ingang van 9
november 2018 treden in werking: a. de Wet beveiliging netwerk- en
informatiesystemen..." `start_date` is set to **2018-11-09** on that
basis; a small number of CSIRT/digital-service-provider-specific
provisions in the same decree commenced later, on 1 January 2019.

`status: superseded` with `end_date: 2026-08-15` now records, rather than
merely schedules, the end of the Wbni's operative period — corrected this
pass from the previous `status: active` / `end_date: 2026-08-15`
("scheduled to end") once [[NL-CBW]]'s entry into force was confirmed
directly.

## Relationships

- Superseded by [[NL-CBW]] (recorded on that entity, with `successor` set
  here) — confirmed in force from 15 August 2026.

## Sources

All four listed sources read directly. `ncsc.nl` and `nctv.nl` (2026-08-27)
describe the successor act; `wetten.overheid.nl`'s BWBR0041515 (2026-08-28)
is the Wbni's own official text, confirming its own basis in EU Directive
2016/1148 and its own repeal date; Staatsblad 2018, 389 (2026-09-05) is the
commencement decree, confirming the Act's own entry-into-force date in its
own words.
