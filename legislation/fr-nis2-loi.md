---
id: FR-NIS2-LOI
type: law
name: Loi relative à la résilience des infrastructures critiques et au renforcement de la cybersécurité
alternative_names:
  - Loi Résilience
  - French NIS2 transposition law
description: >
  French legislative vehicle transposing the NIS2 Directive, together with
  the Critical Entities Resilience Directive and DORA, into French law. It
  will designate ANSSI as the competent national authority for cybersecurity
  and bring roughly 15,000 entities into scope, against about 500 under
  the NIS1 regime. Still a bill as of August 2026, not yet promulgated —
  see the entity body for how the sources' earlier contradiction was
  resolved.

level: national
country: FR
region: EU

status: planned
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - FR-ANSSI
related_entities:
  - EU-NIS2
  - EU-CER
  - BE-NIS2-WET
  - DE-NIS2UMSUCG
  - NL-CBW
  - LU-LOI-NIS2
  - CZ-ZAKON-264-2025
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Confirmed by reading three independent sources directly (2026-08-26). ANSSI's own MonEspaceNIS2 help page: the bill 'relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité' was presented to the Council of Ministers on 15 October 2024, adopted by the Senate on 11-12 March 2025, and passed a special-committee vote in the National Assembly on 10 September 2025 — still short of final adoption. nis-2-directive.com states plainly: 'the parliamentary procedure had not been completed and no final transposition law had been promulgated by 6 August 2026 ... the legislative process was still active.' Eversheds Sutherland's own tracker, read independently, agrees: 'France has not transposed NIS2 yet ... the legislative process is still ongoing.' All three confirm the bill transposes NIS2 together with CER and DORA and designates ANSSI as the competent authority once in force."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Avancement de la transposition de la directive NIS 2"
    url: "https://aide.monespacenis2.cyber.gouv.fr/fr/article/avancement-de-la-transposition-de-la-directive-nis-2-1b3j1da/"
    publisher: "MonEspaceNIS2 (ANSSI)"
    accessed: "2026-08-26"
  - title: "NIS 2 Directive | Transposition in France"
    url: "https://www.nis-2-directive.com/Transposition/France.html"
    publisher: "nis-2-directive.com"
    accessed: "2026-08-26"
  - title: "France — EU NIS2 Directive"
    url: "https://ezine.eversheds-sutherland.com/eu-nis2-directive/france"
    publisher: "Eversheds Sutherland"
    accessed: "2026-08-26"
  - title: "Transposition de la directive NIS2 en droit français : état des lieux et évolutions"
    url: "https://blog.prodwaregroup.com/fr/cybersecurite/transposition-de-la-directive-nis2-en-droit-francais-etat-des-lieux-et-evolutions/"
    publisher: "Prodware"
    accessed: "2026-08-26"
  - title: "Transposition NIS2 en France : loi Résilience, ANSSI et calendrier"
    url: "https://aventris.fr/transposition-anssi"
    publisher: "Aventris"
    accessed: "2026-08-26"
  - title: "Projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité — Dossier législatif"
    url: "https://www.assemblee-nationale.fr/dyn/17/dossiers/DLR5L17N50731"
    publisher: "Assemblée nationale"
    accessed: "2026-09-05"
---

# Loi Résilience — France's NIS2 transposition (still a bill)

> **Verified 2026-08-26, and the contradiction resolved.** ANSSI's own
> MonEspaceNIS2 page, nis-2-directive.com and Eversheds Sutherland were
> all read directly. All three agree: the bill had not been promulgated
> as of 6 August 2026, twenty days before this pass. The "Law n°
> 2025-90 of 26 February 2025" account — found only on aventris.fr,
> and not corroborated by any other source read — is contradicted by
> three independent sources and is not recorded as fact. `status`
> moves from `unknown` to `planned`.
>
> **Re-checked 2026-09-05**: the Assemblée nationale's own dossier
> législatif page, read directly, confirms the same status this entity
> already recorded — first reading, no final adoption — giving this
> entity its first genuinely official-source citation rather than only
> commentary. See below.

## Description

France transposes [[EU-NIS2]] through the *loi Résilience*, on the
resilience of critical infrastructures and the strengthening of
cybersecurity — still a **bill**, not yet promulgated. Unusually, one
vehicle carries **three EU instruments**: NIS2, the Critical Entities
Resilience directive ([[EU-CER]]) and DORA.

Confirmed by reading ANSSI's own MonEspaceNIS2 help page directly
(2026-08-26): the bill was presented to the Council of Ministers on 15
October 2024, adopted by the Senate on 11-12 March 2025, and passed a
special-committee vote in the National Assembly on 10 September 2025.
nis-2-directive.com, read independently, confirms the process was
still active as of **6 August 2026**: "the parliamentary procedure had
not been completed and no final transposition law had been
promulgated." Eversheds Sutherland's own tracker agrees: "France has
not transposed NIS2 yet."

What the sources agree on:

- it will designate [[FR-ANSSI]] as the **competent national authority**;
- scope grows from roughly **500 entities under NIS1 to about 15,000**;
- obligations cover cyber risk management, registration and incident
  notification, with sanctions up to **€10 million or 2% of global
  turnover**;
- France **missed the directive's 17 October 2024 transposition deadline**.

## The sources' contradiction, resolved

Two incompatible accounts existed in this entity's original sourcing:

| Account | Source |
|---|---|
| Transposition is by **Law n° 2025-90 of 26 February 2025** | aventris.fr only |
| The bill was **adopted by the Senate on 12 March 2025** and remained a bill | nis-2-directive.com, Eversheds Sutherland, Prodware, ANSSI's own page |

A law cannot be promulgated in February 2025 and still be a bill in the
Senate the following month. Reading all four commentary sources plus
ANSSI's own page directly resolves it decisively: **three independent
sources, including the designated competent authority's own site,
place the bill in active parliamentary process through September 2025
and confirm it was still unpromulgated on 6 August 2026** — twenty
days before this entity was re-verified. Only aventris.fr asserts the
Law n° 2025-90 account, uncorroborated anywhere else read. That account
is not recorded.

`status: planned` — a bill in active process, not yet an instrument.
`start_date: null` remains, because the bill has not entered into
force. **No law number in `alternative_names`**, because the bill has
none yet; "loi Résilience" is the colloquial name multiple independent
sources use for it. `confidence: medium` — up from `low`, now that
three independent sources agree rather than one uncorroborated claim
standing against another.

## Confirmed against the Assemblée nationale's own record, 2026-09-05

The commentary sources above are corroborated, not merely repeated, by the
Assemblée nationale's own *dossier législatif* page for the bill
(DLR5L17N50731), read directly: it shows "Texte adopté" for the Senate on
**12 March 2025**, transmission to the National Assembly the next day, and
a commission report and revised text filed **10 September 2025** — first
reading, no final adoption recorded. This matches every date already in
this entity and adds an official parliamentary-record citation to what
was previously commercial commentary and ANSSI's own help page alone. A
WebSearch cross-check the same day found no more recent development: the
bill's floor examination was reported as expected "no earlier than
September 2026," consistent with `status: planned` remaining correct.

## Six transpositions of one directive

| Country | Act | In force | Technique |
|---|---|---|---|
| Belgium | [[BE-NIS2-WET]] | **18 Oct 2024** | new act replacing the NIS1 act |
| Germany | [[DE-NIS2UMSUCG]] | 6 Dec 2025 | revises the existing [[DE-BSIG]] |
| Luxembourg | [[LU-LOI-NIS2]] | 10 May 2026 | new act replacing the NIS1-era act |
| Czechia | [[CZ-ZAKON-264-2025]] | 1 Nov 2025 | new act replacing Act No. 181/2014 Sb. |
| Netherlands | [[NL-CBW]] | 15 Aug 2026 | new act superseding [[NL-WBNI]] |
| **France** | **this entity** | **not yet — still a bill on 6 Aug 2026** | one vehicle for NIS2 + CER + DORA |

Belgium met the deadline within a year; France missed it and, on the
evidence read this pass, still has not completed it nearly two years
later. The Atlas can now show that spread across six member states — which
is the sort of comparative fact a country-neutral model exists to make
visible, and which no single-country layer could produce.

France is also the only one of the six to bundle three directives into one
act. **No `implements-requirement-from` → [[EU-CER]] is asserted**, even
though the sources say the vehicle transposes it: the bill is still not in
force, and the DORA/CER details were not independently confirmed this pass.

**No relationship between the four national acts is asserted.**

## Sources

Listed in frontmatter, six of the six now read directly across two
passes. Most are commercial commentary, a vendor blog, or ANSSI's own
help-centre page — still not a Légifrance citation for a promulgated
act, since none exists yet — but the Assemblée nationale's own dossier
législatif page, added and read 2026-09-05, is the first genuinely
official parliamentary-record citation on this entity.
