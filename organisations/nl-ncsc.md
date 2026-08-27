---
id: NL-NCSC
type: organisation
name: Nationaal Cyber Security Centrum
alternative_names:
  - NCSC
  - NCSC-NL
  - Versterkt NCSC
  - Dutch National Cyber Security Centre
description: >
  The Netherlands' national cyber security centre, operating under the
  Ministry of Justice and Security. On 1 January 2026 the Digital Trust
  Center was merged into it, creating a single strengthened NCSC that is
  the point of contact for digital resilience for all Dutch organisations —
  some 2.4 million, from sole traders to multinationals — with round-the-
  clock availability. Since the Cyberbeveiligingswet entered into force on
  15 August 2026 it also functions as the sectoral CSIRT for organisations
  registered under that act.

level: national
country: NL
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - NL-CBW
  - EU-NIS2
relationships:
  - type: applies-to
    target: NL-CBW
    source: fact
    evidence: "Corrected and upgraded this pass (2026-08-27). Reading ncsc.nl's own 'Cyberbeveiligingswet (NIS2)' page directly shows the Cbw entered into force on 15 August 2026 ('De Cyberbeveiligingswet is in werking getreden op 15 augustus 2026') and states in as many words that registered organisations 'sluit je aan op de dienstverlening van het NCSC als jouw sectorale CSIRT' — they connect to the NCSC's services AS THEIR SECTORAL CSIRT. nctv.nl's own page, also read directly, corroborates the same in-force date and describes a sector-dependent 'doorverwijsboom' (routing tree) of competent authorities and CSIRTs, of which the NCSC is one. This closes the previous `interpretation`/`confidence: low` gap: the NCSC's CSIRT role under the Cbw is now a directly-read fact, not an Atlas inference — though it remains only ONE of several sectoral CSIRTs/competent authorities under the act, not a government-wide single point, so `applies-to` (rather than a stronger claim of sole authority) is retained."
    confidence: high
    valid_from: 2026-08-15
    valid_until: null

sources:
  - title: "Versterkt NCSC"
    url: "https://www.ncsc.nl/over-ons/versterkt-ncsc"
    publisher: "Nationaal Cyber Security Centrum (NCSC)"
    accessed: "2026-08-27"
  - title: "DTC en NCSC vanaf 2026 verder als versterkt NCSC"
    url: "https://www.ncsc.nl/nieuws/dtc-en-ncsc-vanaf-2026-verder-als-versterkt-ncsc"
    publisher: "Nationaal Cyber Security Centrum (NCSC)"
    accessed: "2026-08-27"
  - title: "Versterkt NCSC: alle Nederlandse organisaties krijgen één aanspreekpunt voor digitale weerbaarheid"
    url: "https://www.ncsc.nl/nieuws/versterkt-ncsc-alle-nederlandse-organisaties-krijgen-een-aanspreekpunt-voor-digitale-weerbaarheid"
    publisher: "Nationaal Cyber Security Centrum (NCSC)"
    accessed: "2026-08-27"
  - title: "Cyberbeveiligingswet (NIS2)"
    url: "https://www.ncsc.nl/cyberbeveiligingswet-nis2"
    publisher: "Nationaal Cyber Security Centrum (NCSC)"
    accessed: "2026-08-27"
  - title: "DTC en NCSC fuseren tot één Nederlandse cybersecurityorganisatie"
    url: "https://www.techzine.nl/nieuws/security/570635/dtc-en-ncsc-fuseren-tot-een-nederlandse-cybersecurityorganisatie/"
    publisher: "Techzine"
---

# Nationaal Cyber Security Centrum (NCSC)

> **Verified 2026-08-27.** Four of five cited pages were read directly this
> pass; `techzine.nl` was not re-fetched. This is a **promotion with a real
> correction**: the previous entity recorded the NCSC's link to
> [[NL-CBW]] as `source: interpretation` at `confidence: low`, explicitly
> because "no source read states that the NCSC is the competent authority
> or the CSIRT designated under that act." Reading `ncsc.nl`'s own
> Cyberbeveiligingswet page directly this pass finds exactly that statement
> in the NCSC's own words — the gap this entity flagged is now closed.

## Description

The NCSC is the Netherlands' national cyber security centre, operating
under the **Ministry of Justice and Security** (confirmed via ncsc.nl's own
Cbw page, read directly — a parent-ministry detail not previously recorded).
Since **1 January 2026** it is the *versterkt NCSC* — the **strengthened**
NCSC, created by merging the **Digital Trust Center** into it. Reading
ncsc.nl's own merger announcement directly confirms the date in the NCSC's
own words: "Per 1 januari 2026 gaat het Digital Trust Center (DTC) verder
onder de vlag van het versterkte Nationaal Cyber Security Centrum (NCSC)."

The merger changed who it serves. The NCSC's remit had been critical
infrastructure and central government; the DTC's was business, particularly
smaller firms. The merged body is the single point of contact for digital
resilience for **all** Dutch organisations — confirmed directly at
**2.4 million**, per the NCSC's own news item, with 24/7 availability.

## The gap this closes

`discovery/research-queue.md` has recorded since the **Belgium batch** that
[[NL-CBW]] is a NIS2 act with **no authority attached**, while Belgium had
[[BE-CCB]] and Germany [[DE-BSI]]. That observation was made in 2026-08-15
terms and carried in every structural review since — including the previous
pass on this entity, which found the NCSC's role but could not confirm the
CSIRT designation.

**That designation is now confirmed.** Reading ncsc.nl's own
Cyberbeveiligingswet page directly, dated after the act's 15 August 2026
entry into force, states plainly that organisations registering under the
Cbw connect to "de dienstverlening van het NCSC als jouw sectorale CSIRT" —
the NCSC's services **as your sectoral CSIRT**. nctv.nl's own page,
independently read, corroborates the same in-force date and describes a
sector-by-sector "doorverwijsboom" (routing tree) of competent authorities
and CSIRTs — the NCSC is one node in that tree, not a sole government-wide
authority, which is why the relationship stays `applies-to` rather than
being upgraded to a stronger exclusive-authority claim.

## Comparison table, updated

| Country | Authority | Edge to the act |
|---|---|---|
| Belgium | [[BE-CCB]] | `governed-by` **and** `produces` [[BE-NIS2-WET]] |
| France | [[FR-ANSSI]] | `applies-to` [[FR-NIS2-LOI]] |
| Germany | [[DE-BSI]] | `governed-by` [[DE-BSIG]] |
| **Netherlands** | **NCSC** | **`applies-to` [[NL-CBW]] — now `fact`, `confidence: high`** |

## Not modelled

- The **Digital Trust Center**, now absorbed. It is the second body in the
  Atlas's orbit to stop existing after [[GB-DSIT]], and unlike DSIT it is
  not modelled at all — so the merger is described here and cannot be
  shown.
- The full **doorverwijsboom** — which sectoral CSIRTs and competent
  authorities cover which of the roughly 8,000 organisations under the Cbw
  (confirmed via ncsc.nl and nctv.nl, both read directly).
- The **NCTV** and the Ministry of Justice and Security more broadly, the
  NCSC's parent.

## Relationships

- `applies-to` [[NL-CBW]] — now `fact`, `confidence: high`.

## Sources

Four of five read directly this pass: both `ncsc.nl` merger pages, the
2.4-million-organisations news item, and the NCSC's own Cbw page.
`techzine.nl` was not re-fetched.
