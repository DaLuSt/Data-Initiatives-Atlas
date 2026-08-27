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
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-AP
related_entities:
  - EU-GDPR
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading the official Staatsblad 2018, 144 text directly at zoek.officielebekendmakingen.nl (2026-08-27): the UAVG's five chapters cover general provisions and scope, the Autoriteit Persoonsgegevens's composition and enforcement powers (including administrative fines), detailed GDPR-implementation exceptions (special data categories, scientific research, journalism), national-security and archival carve-outs, and transitional provisions repealing the prior Wet bescherming persoonsgegevens. Published 22 May 2018, signed 16 May 2018, issued by the Ministry of Justice and Security. eerstekamer.nl dossier 34.851, also read directly, confirms Tweede Kamer adoption 13 March 2018, Eerste Kamer adoption 15 May 2018 (as a hamerstuk), and states plainly: 'De verordening en de Uitvoeringswet zijn op 25 mei 2018 in werking getreden.' autoriteitpersoonsgegevens.nl returned HTTP 403 and was not readable this pass."
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
---

# Uitvoeringswet AVG (UAVG)

> **Verified 2026-08-27.** Two of three cited pages were read directly this
> pass, closing the previous `search-only` status (never previously
> `last_verified`). `autoriteitpersoonsgegevens.nl` returned HTTP 403 both
> attempts and was not readable — a genuine block, not a silently dropped
> source.

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

A related *Aanpassingswet* AVG (Eerste Kamer dossier 34.939) adjusted other
Dutch legislation to the GDPR; it is not modelled separately here, and
whether it warrants its own entity is queued in
`discovery/research-queue.md`.

## Classification

Per `metadata/taxonomy.md` §2 this is **Dutch implementation legislation**:
`type: law`, `level: national`, `country: NL`, `region: EU` — the `region`
field recording that its obligations originate in an EU instrument, with the
`implements-requirement-from` relationship naming which one.

## Relationships

- Implements requirements from [[EU-GDPR]].
- [[NL-AP]] is the supervisory authority operating under it, confirmed
  directly in the official Staatsblad text's own chapter structure.
- The Wbp, which the GDPR/UAVG regime replaced, is not yet an Atlas entity;
  queued for temporal completeness.

## Sources

Two of three read directly this pass, including the strongest possible
citation — the official Staatsblad text itself. `autoriteitpersoonsgegevens.nl`
was attempted and returned HTTP 403 both times; it is a genuine block, not
a silently dropped source.
