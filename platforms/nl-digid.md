---
id: NL-DIGID
type: platform
name: DigiD
alternative_names:
  - Digitale Identiteit
  - Nieuwe Authenticatie Voorziening
description: >
  The Dutch government's digital identity and login system for citizens.
  It lets a person prove who they are once and reuse that single login
  across more than 600 government, healthcare, education and pension-fund
  organisations, rather than each service managing its own credentials.
  Launched in 2003 under the name Nieuwe Authenticatie Voorziening, renamed
  DigiD in 2004, and available to all Dutch citizens from 1 January 2005.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2005-01-01
end_date: null
last_verified: "2026-08-30"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-LOGIUS
related_entities:
  - NL-LOGIUS
relationships:
  - type: maintained-by
    target: NL-LOGIUS
    source: fact
    evidence: "Confirmed by reading logius.nl's own DigiD page directly (2026-08-30): Logius operates DigiD as one of its access ('toegang') services and describes upcoming procurement of platform management ('aanbesteding van het platformbeheer'). Logius's own retrospective article, also read directly, confirms current scale — 'Inmiddels gebruiken meer dan 17 miljoen mensen DigiD' (over 17 million people now use DigiD) across 'ruim 600 overheidsorganisaties' (more than 600 government organisations) — and gives a milestone timeline: two-factor SMS login added in 2006, a mobile app in 2017, and ID-document verification in 2020."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "DigiD — Logius"
    url: "https://www.logius.nl/onze-dienstverlening/toegang/digid"
    publisher: "Logius (Ministerie van Binnenlandse Zaken en Koninkrijksrelaties)"
    accessed: "2026-08-30"
  - title: "Twintig jaar veilig en makkelijk inloggen met DigiD"
    url: "https://www.logius.nl/actueel/twintig-jaar-veilig-en-makkelijk-inloggen-met-digid"
    publisher: "Logius"
    accessed: "2026-08-30"
  - title: "Over DigiD"
    url: "https://www.digid.nl/over-digid"
    publisher: "DigiD (Logius)"
    accessed: "2026-08-30"
  - title: "DigiD"
    url: "https://nl.wikipedia.org/wiki/DigiD"
    publisher: "Wikipedia"
    accessed: "2026-08-30"
---

# DigiD

> **Added 2026-08-30, `verification: primary-source` from creation.** A
> research-queue item flagged as **Next** since the Estonia batch — the
> Netherlands had no digital identity platform entity, while
> [[FR-FRANCECONNECT]], [[ES-CLAVE]] and [[PL-MOBYWATEL]] all did — is now
> closed. Four sources were read directly before this entity was written:
> two `logius.nl` pages, `digid.nl`'s own "About DigiD" page, and Dutch
> Wikipedia's dedicated article, which supplied the launch history none of
> the three government pages stated in full.

## Description

DigiD is the Dutch government's digital identity and login system for
citizens. Confirmed by reading `digid.nl`'s own page directly: "Met uw
DigiD laat u zien wie u bent als u op internet iets regelt" (with your
DigiD, you show who you are when you arrange something online) — used with
government agencies, healthcare providers, educational institutions and
pension funds. Confirmed by reading Logius's own retrospective article
directly, it now reaches **more than 17 million users** across **more than
600 government organisations**.

## A launch history spread across three sources

No single source read gives the full origin story; it was assembled from
Dutch Wikipedia (Logius's own pages describe current operations, not
history):

- **2003** — launched under the name **Nieuwe Authenticatie Voorziening**
  (New Authentication Facility).
- **5 October 2004** — renamed **DigiD**.
- **1 January 2005** — available to **all** Dutch citizens, the date this
  entity records as `start_date`.
- **2006** — two-factor SMS login added (confirmed by Logius's own
  retrospective article).
- **2017** — mobile app introduced.
- **2020** — ID-document verification (ID-check) added.

Wikipedia's account was not independently cross-checked against a primary
government page for the 2003/2004 dates specifically, since neither
`logius.nl` nor `digid.nl` states them; both government sources instead
describe DigiD as existing "meer dan twintig jaar" (more than twenty years)
without giving the founding year directly.

## The fourth national digital-identity platform in the Atlas

| Country | Platform | Model |
|---|---|---|
| France | [[FR-FRANCECONNECT]] | identity **federation** — reuse an account from a chosen provider |
| Spain | [[ES-CLAVE]] | — |
| Poland | [[PL-MOBYWATEL]] | — |
| **Netherlands** | **DigiD** | a **single government-issued** login, not brokered across private providers |

Unlike FranceConnect, which federates identity across multiple providers
including a private one (La Poste), DigiD is issued directly by government
and does not broker against other identity providers. No source read
compares DigiD's architecture to the other three directly, so this row is
an Atlas observation from what each entity's own sources state, not a
sourced claim of its own.

## The eIDAS gap, again

Nothing read about DigiD mentions the eIDAS Regulation, cross-border
recognition, or the European Digital Identity Wallet [[EU-EUDI-WALLET]]
requires every member state to offer by the end of 2026. **No relationship
to [[EU-EIDAS2]] is asserted.** This is the same gap already recorded on
[[FR-FRANCECONNECT]], now extended to a fourth country — the Atlas holds
no confirmed Dutch EUDI Wallet arrangement. Logged in
`discovery/research-queue.md`.

## Relationships

- `maintained-by` [[NL-LOGIUS]].

## Sources

Listed in frontmatter, all four read directly.
