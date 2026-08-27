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
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: 2026-08-15
last_verified: "2026-08-27"
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
    evidence: "The Wbni is the Dutch act on security of network and information systems implementing the original EU NIS regime; NIS2 (which the Cyberbeveiligingswet implements) repealed Directive (EU) 2016/1148. NOT READ this pass — no page specific to the Wbni's own text or its relationship to the original NIS Directive was fetched; the two sources this entity cites (ncsc.nl and nctv.nl) were read directly but both describe the Cbw/NIS2 side of the supersession, not the Wbni's own content or its NIS-Directive basis."
    confidence: medium
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
---

# Wet beveiliging netwerk- en informatiesystemen (Wbni)

> **Re-verified 2026-08-27, still `search-only`.** Both cited pages were
> read directly this pass, and both confirm the Wbni's **supersession has
> now happened** — the Cbw entered into force on 15 August 2026, per each
> page's own current text — which corrects `status` from `active` to
> `superseded`. But neither page describes the Wbni's **own** content,
> commencement date, or its relationship to the original NIS Directive:
> both sources are written from the Cbw/NIS2 side of the transition. A
> majority of this entity's own two sources were read, but what was read
> does not supply what this entity most needs — a source on the Wbni
> itself — so it stays `search-only` rather than being promoted on the
> strength of confirming only the supersession date.

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
point in time (brief §11). Its own content, commencement date and
relationship to the original NIS Directive remain unresearched this pass;
the original NIS Directive is not yet an Atlas entity, and no source
specific to the Wbni's own text (rather than to its successor) was located
or fetched.

`status: superseded` with `end_date: 2026-08-15` now records, rather than
merely schedules, the end of the Wbni's operative period — corrected this
pass from the previous `status: active` / `end_date: 2026-08-15`
("scheduled to end") once [[NL-CBW]]'s entry into force was confirmed
directly.

## Relationships

- Superseded by [[NL-CBW]] (recorded on that entity, with `successor` set
  here) — confirmed in force from 15 August 2026.

## Sources

Both listed sources read directly this pass, but both describe the
successor act rather than the Wbni itself — hence `search-only` is
retained rather than promoted. A future pass should look specifically for
the Wbni's own text (a `wetten.overheid.nl` BWBR citation was not located
this pass) and its citation to the original EU NIS Directive.
