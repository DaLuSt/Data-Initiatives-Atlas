---
id: PL-PSIE
type: platform
name: Publiczny System Identyfikacji Elektronicznej
alternative_names:
  - PSIE
  - Public Electronic Identification System
  - Profil Zaufany
  - Profil Osobisty
description: >
  Poland's eIDAS-notified national electronic identification scheme,
  comprising two electronic identification means: profil zaufany (trusted
  profile), a free login-and-signature credential for public e-services,
  and profil osobisty (personal profile), the certificate embedded in the
  e-dowód electronic identity card chip. Notified to the European
  Commission and published in the Official Journal of the EU on 19 April
  2023, at Substantial and High assurance levels respectively — distinct
  from the mObywatel application, which is a separate government platform
  that can be used to authenticate into it.

level: national
country: PL
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2023-04-19
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - PL-MC
related_entities:
  - EU-EIDAS
  - PL-MC
  - PL-MOBYWATEL
relationships:
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #155: 'Poland's actual eIDAS-notified scheme... a different, currently unmodelled entity, distinct from mObywatel'). Confirmed by reading the European Commission's own eID User Community page directly (2026-09-13), 'Overview of pre-notified and notified eID schemes under eIDAS': its table lists Poland's scheme as 'Public Electronic Identification System', eID means 'Trusted profile, personal profile', assurance level 'Substantial, High', status 'NOTIFIED', notification date '19 Apr 2023', Official Journal reference '2023/C 136/02'. A formal notification under eIDAS's Article 9 mutual-recognition mechanism, not an inference from subject matter."
    confidence: high
    valid_from: 2023-04-19
    valid_until: null
  - type: maintained-by
    target: PL-MC
    source: fact
    evidence: "Confirmed by reading gov.pl's own Ministry of Digital Affairs page on profil zaufany directly (2026-09-13): 'Za rozwój i utrzymanie serwisu odpowiada Minister Cyfryzacji' (the Minister of Digital Affairs is responsible for the service's development and maintenance). Independently corroborated by the Ministry's own press release announcing the scheme's successful eIDAS notification, read directly, and by web-search-level corroboration (not independently read this pass) that the minister competent for digitisation matters (the same office) administers the national electronic identification scheme and the national eIDAS node under the Act of 5 September 2016 on trust services and electronic identification, Chapter 4."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Overview of pre-notified and notified eID schemes under eIDAS"
    url: "https://ec.europa.eu/digital-building-blocks/sites/display/EIDCOMMUNITY/Overview+of+pre-notified+and+notified+eID+schemes+under+eIDAS"
    publisher: "European Commission — eID User Community"
    accessed: "2026-09-13"
  - title: "Profil zaufany"
    url: "https://www.gov.pl/web/cyfryzacja/profil-zaufany"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-09-13"
  - title: "Strona główna — Profil zaufany"
    url: "https://www.gov.pl/web/profilzaufany"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-09-13"
  - title: "Polska z sukcesem zakończyła proces notyfikacji Publicznego Systemu Identyfikacji Elektronicznej"
    url: "https://www.gov.pl/web/cyfryzacja/polska-z-sukcesem-zakonczyla-proces-notyfikacji-publicznego-systemu-identyfikacji-elektronicznej"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-09-13"
  - title: "e-Dowód"
    url: "https://www.gov.pl/web/e-dowod"
    publisher: "Ministerstwo Spraw Wewnętrznych i Administracji"
    accessed: "2026-09-13"
---

# Publiczny System Identyfikacji Elektronicznej (PSIE)

> **Created 2026-09-13**, closing `discovery/unresolved.md` row #155 —
> flagged 2026-09-06 as "a different, currently unmodelled entity,
> distinct from mObywatel." Four gov.pl pages and the European
> Commission's own eID notification table were read directly.

## Description

Poland's eIDAS-notified national electronic identification scheme.
Confirmed by reading the Ministry of Digital Affairs' own press release
directly: the **Publiczny System Identyfikacji Elektronicznej** ("Public
Electronic Identification System") comprises two electronic
identification means:

- **profil zaufany** (trusted profile) — a free credential for logging
  into and signing documents on public e-service portals such as ePUAP,
  PUE ZUS and CEIDG, confirmed by reading gov.pl's own dedicated page
  directly;
- **profil osobisty** (personal profile) — the certificate embedded in
  the chip of the **e-dowód** electronic identity card, confirmed by
  reading gov.pl's own e-dowód page directly, which cites Article 10a(4)
  of the Act on Identity Documents as its legal basis.

## Notified under eIDAS, two means at two assurance levels

Confirmed by reading the European Commission's own eID User Community
page directly: Poland's "Public Electronic Identification System" is
listed with eID means "Trusted profile, personal profile," assurance
level **Substantial** (trusted profile) and **High** (personal profile),
status **NOTIFIED**, notification date **19 April 2023**, Official
Journal reference **2023/C 136/02**. The Ministry's own press release,
read directly, independently confirms the same date and Official Journal
citation and adds that the scheme complies with Commission Implementing
Regulations (EU) 2015/1501 and 2015/1502.

## Distinct from mObywatel

This entity answers the question [[PL-MOBYWATEL]]'s own file left open:
which Polish system, if any, is actually eIDAS-notified is **not**
mObywatel — no Atlas source has found mObywatel itself listed in the
Commission's notification table. It is this scheme. Press reporting
(rp.pl, forsal.pl; not independently confirmed against a ministry
source this pass) describes the trusted profile as increasingly
operated *through* the mObywatel app — for example, confirming
trusted-profile logins by push notification instead of an SMS code —
and states an intention for profil zaufany to become "a function within
mObywatel" rather than a separate destination. That functional overlap
is recorded here in prose only; no relationship edge is asserted between
the two entities, consistent with the Atlas's treatment of national
identity architectures generally (see [[PL-MOBYWATEL]]'s "four national
identity architectures" comparison, which asserts no edges between
France's, Germany's, Spain's and Poland's own systems either).

## Not modelled

- **profil zaufany** and **profil osobisty** as separate entities in
  their own right — the Atlas models the notified scheme they jointly
  constitute, matching how [[PT-CMD]] and [[PT-CARTAO-CIDADAO]] are
  instead modelled as two *separate* notified schemes for Portugal. This
  is a genuine structural difference, not an inconsistency: Portugal's
  two means were notified as two schemes; Poland's two means were
  notified as one.
- **e-dowód**, the physical electronic identity card that carries the
  profil osobisty certificate, and the **Act on Identity Documents**
  that establishes it.
- The **Act of 5 September 2016 on trust services and electronic
  identification**, whose Chapter 4 ("krajowy schemat identyfikacji
  elektronicznej") is understood — via secondary corroboration, not an
  independently-read primary text this pass; `isap.sejm.gov.pl` remains
  CAPTCHA-blocked, matching the block already logged in row #160 — to
  assign the national scheme and node to the minister competent for
  digitisation. Not modelled as its own legislation entity.

## Relationships

- `implements-requirement-from` [[EU-EIDAS]], valid from 19 April 2023.
- `maintained-by` [[PL-MC]] — the Ministry of Digital Affairs, per its
  own statement on the profil zaufany page.

## Sources

Listed in frontmatter, all four read directly 2026-09-13.
