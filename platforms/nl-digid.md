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
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-LOGIUS
related_entities:
  - NL-LOGIUS
  - EU-EIDAS
relationships:
  - type: maintained-by
    target: NL-LOGIUS
    source: fact
    evidence: "Confirmed by reading logius.nl's own DigiD page directly (2026-08-30): Logius operates DigiD as one of its access ('toegang') services and describes upcoming procurement of platform management ('aanbesteding van het platformbeheer'). Logius's own retrospective article, also read directly, confirms current scale — 'Inmiddels gebruiken meer dan 17 miljoen mensen DigiD' (over 17 million people now use DigiD) across 'ruim 600 overheidsorganisaties' (more than 600 government organisations) — and gives a milestone timeline: two-factor SMS login added in 2006, a mobile app in 2017, and ID-document verification in 2020."
    confidence: high
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (this entity's own 'The eIDAS gap, again' section). Confirmed by reading the European Commission's own eID User Community page directly (2026-09-06), 'Overview of pre-notified and notified eID schemes under eIDAS' (ec.europa.eu/digital-building-blocks, maintained by the eID User Community, last updated 2 February 2026): its table lists 'The Kingdom of the Netherlands' / 'DigiD' with assurance levels 'Substantial, High', eID means 'DigiD Substantieel, DigiD Hoog', status 'NOTIFIED', notification date '21 Aug 2020', Official Journal reference 2020/C 276/02. This is a formal notification under eIDAS's Article 9 mutual-recognition mechanism for national electronic identification schemes — the same mechanism [[FR-FRANCE-IDENTITE]]'s own eIDAS edge rests on — not an inference from subject matter. Corroborated by logius.nl's own 'Toegang verlenen aan Europese burgers en bedrijven' page, read directly, which states DigiD and eHerkenning both offer login methods at 'betrouwbaarheidsniveau Substantieel en/of Hoog' and that granting access to European citizens and businesses is mandatory for Dutch service providers accepting those login methods."
    confidence: high
    valid_from: 2020-08-21
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
  - title: "Overview of pre-notified and notified eID schemes under eIDAS"
    url: "https://ec.europa.eu/digital-building-blocks/sites/display/EIDCOMMUNITY/Overview+of+pre-notified+and+notified+eID+schemes+under+eIDAS"
    publisher: "European Commission — eID User Community, Digital Building Blocks"
    accessed: "2026-09-06"
  - title: "Toegang verlenen aan Europese burgers en bedrijven"
    url: "https://www.logius.nl/domeinen/toegang/eidas/documentatie/toegang-verlenen-aan-europese-burgers-en-bedrijven"
    publisher: "Logius (Ministerie van Binnenlandse Zaken en Koninkrijksrelaties)"
    accessed: "2026-09-06"
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
>
> **Updated 2026-09-06**: the "eIDAS gap, again" section below is closed.
> The European Commission's own eID User Community page, read directly,
> lists DigiD as formally notified under eIDAS at Substantial and High
> assurance levels since 21 August 2020.

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

## The eIDAS gap, closed — and why it stops at eIDAS 1.0

The European Commission's own eID User Community page, read directly
(2026-09-06), lists **DigiD** as a formally **notified** eID scheme under
[[EU-EIDAS]]: assurance levels **Substantial and High**, notified
**21 August 2020**, published in the Official Journal at 2020/C 276/02.
This is the same Article 9 mutual-recognition mechanism
[[FR-FRANCE-IDENTITE]]'s own eIDAS edge rests on — a formal Commission
notification, not an inference from subject matter — so
`implements-requirement-from` is recorded at `confidence: high`.
Logius's own eIDAS documentation, also read directly, corroborates the
trust levels and states that Dutch service providers accepting DigiD or
eHerkenning at Substantial/High must grant access to other EU citizens
and businesses.

**No relationship to [[EU-EIDAS2]] or [[EU-EUDI-WALLET]] is asserted.**
Nothing read connects DigiD to the European Digital Identity Wallet every
member state must offer by the end of 2026, and [[EU-EUDI-WALLET]]'s own
entity records the Dutch candidate — the **publieke NL-wallet** — as a
separate, still-in-development effort with no Atlas entity of its own.
The eIDAS-1.0 notification and the EUDI Wallet mandate are distinct
obligations; only the first is sourced here.

## Relationships

- `maintained-by` [[NL-LOGIUS]].
- `implements-requirement-from` [[EU-EIDAS]], `confidence: high` — a
  formal Commission notification, 21 August 2020.

## Sources

Listed in frontmatter, all four original sources read directly, plus two
more read directly this pass: the European Commission's own eID
notification table and Logius's eIDAS access-obligation page.
