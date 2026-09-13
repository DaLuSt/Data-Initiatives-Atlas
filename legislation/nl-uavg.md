---
id: NL-UAVG
type: law
name: Uitvoeringswet Algemene verordening gegevensbescherming
alternative_names:
  - UAVG
  - GDPR Implementation Act
description: >
  Dutch implementing act for the EU General Data Protection Regulation. In
  force from 25 May 2018, when it replaced the Wet bescherming
  persoonsgegevens (Wbp), it gives national effect to the discretion the
  GDPR leaves to member states and designates the Autoriteit
  Persoonsgegevens as supervisory authority.

level: national
country: NL
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2018-05-25
end_date: null
last_verified: "2026-09-13"
previous_version: NL-WBP
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-AP
related_entities:
  - EU-GDPR
  - NL-WBP
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading the official Staatsblad 2018, 144 text directly at zoek.officielebekendmakingen.nl (2026-08-27): the UAVG's five chapters cover general provisions and scope, the Autoriteit Persoonsgegevens's composition and enforcement powers (including administrative fines), detailed GDPR-implementation exceptions (special data categories, scientific research, journalism), national-security and archival carve-outs, and transitional provisions repealing the prior Wet bescherming persoonsgegevens. Published 22 May 2018, signed 16 May 2018, issued by the Ministry of Justice and Security. eerstekamer.nl dossier 34.851, also read directly, confirms Tweede Kamer adoption 13 March 2018, Eerste Kamer adoption 15 May 2018 (as a hamerstuk), and states plainly: 'De verordening en de Uitvoeringswet zijn op 25 mei 2018 in werking getreden.' autoriteitpersoonsgegevens.nl returned HTTP 403 and was not readable this pass."
    confidence: high
    valid_from: 2018-05-25
    valid_until: null
  - type: supersedes
    target: NL-WBP
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (this file's own 'not yet an Atlas entity' note). Confirmed by reading wetten.overheid.nl's own record for BWBR0011468 directly (2026-09-13): the Wet bescherming persoonsgegevens was repealed 25 May 2018 (Stb. 2018, 298), the same day this entity and the GDPR took effect — matching the Staatsblad 2018, 144 text's own transitional provisions already cited above, which name the Wbp as the act repealed."
    confidence: high
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "Staatsblad 2018, 144 (UAVG, official text)"
    url: "https://zoek.officielebekendmakingen.nl/stb-2018-144.html"
    publisher: "Overheid.nl — Officiële bekendmakingen"
    accessed: "2026-08-27"
  - title: "Uitvoeringswet Algemene verordening gegevensbescherming (34.851)"
    url: "https://www.eerstekamer.nl/wetsvoorstel/34851_uitvoeringswet_algemene"
    publisher: "Eerste Kamer der Staten-Generaal"
    accessed: "2026-08-27"
  - title: "Uitvoeringswet Algemene verordening gegevensbescherming (UAVG)"
    url: "https://www.autoriteitpersoonsgegevens.nl/documenten/uitvoeringswet-algemene-verordening-gegevensbescherming-uavg"
    publisher: "Autoriteit Persoonsgegevens"
  - title: "Aanpassingswet Algemene verordening gegevensbescherming — BWBR0041233"
    url: "https://wetten.overheid.nl/BWBR0041233/"
    publisher: "Overheid.nl (wetten.overheid.nl)"
    accessed: "2026-09-05"
  - title: "Wet bescherming persoonsgegevens — BWBR0011468 (informatie)"
    url: "https://wetten.overheid.nl/BWBR0011468/2016-01-01/0/informatie"
    publisher: "Overheid.nl (wetten.overheid.nl)"
    accessed: "2026-09-13"
---

# Uitvoeringswet AVG (UAVG)

> **Verified 2026-08-27.** Two of three cited pages were read directly this
> pass, closing the previous `search-only` status (never previously
> `last_verified`). `autoriteitpersoonsgegevens.nl` returned HTTP 403 both
> attempts and was not readable — a genuine block, not a silently dropped
> source.
>
> **Closed 2026-09-13.** The Wbp is now [[NL-WBP]], closing this file's own
> "not yet an Atlas entity" gap — found via a routine grep for lingering
> hedge language, not a tracked `discovery/unresolved.md` row. This entity
> now carries `supersedes` → [[NL-WBP]], and `previous_version` is set.

## Description

The UAVG is the Dutch implementing act for the [[EU-GDPR]]. Reading the
**official Staatsblad 2018, 144 text directly** — the strongest possible
citation, not previously read — confirms the act's five-chapter structure:
general provisions (definitions, material and territorial scope, consent
for minors), the Autoriteit Persoonsgegevens (composition, powers,
administrative fines), detailed GDPR-implementation rules (special
categories of data, scientific research, journalism), national-security
and archival exceptions, and transitional provisions repealing the prior
**Wet bescherming persoonsgegevens (Wbp)**. It was signed 16 May 2018 and
published 22 May 2018, issued by the Ministry of Justice and Security.

Its passage, confirmed directly via the Eerste Kamer's own dossier page:
adopted by the **Tweede Kamer on 13 March 2018** and by the **Eerste Kamer
on 15 May 2018** — processed there as a *hamerstuk* (an uncontested,
expedited procedure) — with the PVV faction recorded as filing a formal
objection ("aantekening"). The same page states plainly, in its own words:
"De verordening en de Uitvoeringswet zijn op 25 mei 2018 in werking
getreden," confirming the entry-into-force date independently of the
Staatsblad text.

Article 48a was excepted from the general entry into force and took effect
separately by a later decision (previously recorded as 19 December 2018,
not re-confirmed this pass — neither page read gave that specific detail).

**Closed as a decision, 2026-09-05.** A related *Aanpassingswet Algemene
verordening gegevensbescherming* (Eerste Kamer dossier 34.939, BWBR0041233,
enacted 11 July 2018) adjusts other Dutch legislation to the GDPR/UAVG.
Reading wetten.overheid.nl's own text directly confirms it is a purely
**technical/consequential amendment act**: every one of its articles
reads only "[Red: Wijzigt ...]" (amends ...), modifying references across
more than 80 existing statutes spanning nine ministries rather than
stating any substantive rule of its own. It is **not** modelled as a
separate entity, for the same reason [[NL-WHO]]'s implementing amendment
is folded into that entity rather than split out: an amending act with no
independent substantive content does not meet the bar for its own node.

## Classification

Per `metadata/taxonomy.md` §2 this is **Dutch implementation legislation**:
`type: law`, `level: national`, `country: NL`, `region: EU` — the `region`
field recording that its obligations originate in an EU instrument, with the
`implements-requirement-from` relationship naming which one.

## Relationships

- Implements requirements from [[EU-GDPR]].
- [[NL-AP]] is the supervisory authority operating under it, confirmed
  directly in the official Staatsblad text's own chapter structure.
- **Supersedes** [[NL-WBP]], now modelled (2026-09-13): wetten.overheid.nl's
  own record confirms the Wbp was repealed 25 May 2018, the same day this
  entity and the GDPR took effect — matching the transitional provisions
  already read in the Staatsblad 2018, 144 text above.

## Sources

Two of three read directly this pass, including the strongest possible
citation — the official Staatsblad text itself. `autoriteitpersoonsgegevens.nl`
was attempted and returned HTTP 403 both times; it is a genuine block, not
a silently dropped source. A fourth source, wetten.overheid.nl's own record
for the Wbp, was added and read directly 2026-09-13.
