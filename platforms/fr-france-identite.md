---
id: FR-FRANCE-IDENTITE
type: platform
name: France Identité
alternative_names:
  - France Identité+
description: >
  French state digital identity scheme built around the electronic national
  identity card, offered through a companion smartphone app. ANSSI certified
  it at the "high" level of assurance in February 2024, and the European
  Commission notified it in September 2024 as meeting eIDAS's high-level-of-
  assurance requirements. It has since been designated by the Commission as
  France's future European Digital Identity Wallet, and France Titres (the
  operator, not itself an Atlas entity) coordinates the multi-country
  POTENTIAL and APTITUDE pilot consortia testing EUDI Wallet use cases.
  Acts as an identity provider within FranceConnect+.

level: national
country: FR
region: EU

status: active
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
organisations: []
related_entities:
  - FR
  - FR-FRANCECONNECT
  - EU-EIDAS
  - EU-EUDI-WALLET
relationships:
  - type: applies-in
    target: FR
    source: fact
    evidence: "Confirmed by reading france-identite.gouv.fr directly (2026-09-05): the site describes France Identité as the French state's official digital-identity service, built on the electronic national identity card. FR-FRANCECONNECT's own entity, sourced from the same domain, already records France Identité as 'a dematerialised national identity card on a smartphone.' Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md, FR-FRANCECONNECT → EU-EIDAS/EU-EIDAS2). Confirmed by reading france-identite.gouv.fr's own article directly (2026-09-05), 'France Identité franchit une étape majeure pour l'interopérabilité à l'échelle européenne': 'la Commission européenne a notifié le lundi 9 septembre 2024 France Identité comme étant conforme aux exigences relatives au niveau de garantie élevé' (the European Commission notified France Identité, on Monday 9 September 2024, as meeting the requirements for the high level of assurance) — a formal notification under eIDAS's mutual-recognition mechanism for national electronic identification schemes, following ANSSI's own high-level-of-assurance security certification of the app in February 2024, stated on the same page. This is a direct statement of formal Commission notification under the Regulation, not an inference from subject matter — the strongest kind of eIDAS evidence available in this Atlas to date."
    confidence: high
    valid_from: 2024-09-09
    valid_until: null
  - type: implements-requirement-from
    target: EU-EUDI-WALLET
    source: fact
    evidence: "Confirmed by reading france-identite.gouv.fr's own 'Potential & Aptitude' page directly (2026-09-05): 'The France Identité application was designated by the European Commission as France's future digital wallet' to meet eIDAS 2.0's requirement that every member state make a wallet available by the end of 2026. The same page states France Titres (the operator; not itself an Atlas entity) coordinates POTENTIAL — 160 partners from 18 member states plus Ukraine, concluded September 2025 — and its successor APTITUDE — 117 partners from 11 European countries plus Ukraine — the pilot consortia testing wallet use cases (digital travel credentials, bank account opening, driving licences, qualified electronic signatures, cross-border e-prescriptions). Recorded at low confidence because this is a designation of intent, not yet a completed, operational wallet — the same 'prepared, not live' distinction [[DE-BUNDID]] draws for its own EU-EUDI-WALLET edge."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "France Identité"
    url: "https://france-identite.gouv.fr/"
    publisher: "France Identité (France Titres)"
    accessed: "2026-09-05"
  - title: "France Identité franchit une étape majeure pour l'interopérabilité à l'échelle européenne"
    url: "https://france-identite.gouv.fr/actualite/mie_eleve_eidas.html"
    publisher: "France Identité (France Titres)"
    accessed: "2026-09-05"
  - title: "Potential & Aptitude"
    url: "https://france-identite.gouv.fr/potential-aptitude/"
    publisher: "France Identité (France Titres)"
    accessed: "2026-09-05"
---

# France Identité

> **Added 2026-09-05.** `discovery/unresolved.md` had flagged
> FR-FRANCECONNECT → [[EU-EIDAS]]/[[EU-EIDAS2]] as "becoming
> time-critical" with the EUDI Wallet deadline four months away, and
> `countries/fr/index.md` had explicitly listed France Identité as
> deliberately not modelled, "recorded in prose on
> [[FR-FRANCECONNECT]]." Three pages on `france-identite.gouv.fr` were
> read directly this pass and together justify splitting it out: it
> carries its own formal eIDAS notification and its own EUDI Wallet
> designation, neither of which belongs on FranceConnect itself.

## Description

France Identité is the French state's digital-identity scheme built on
the electronic national identity card, accessed through a companion
smartphone app. **ANSSI** — France's cybersecurity agency — certified
the app at the **"high" level of assurance** in February 2024, and on
**9 September 2024** the **European Commission notified** it as
meeting eIDAS's high-level-of-assurance requirements, with (per the
source) unanimous recognition by other member states.

## Why this is not recorded on FranceConnect

[[FR-FRANCECONNECT]] is the identity **federation** — the broker that
lets a person reuse an account from a chosen identity provider.
France Identité is one of those providers, integrated through
FranceConnect+. The eIDAS notification and the EUDI Wallet designation
both concern **the identity scheme itself**, not the federation that
brokers access to it — the same distinction that keeps BundID's own
eIDAS edge off any German federation layer. FranceConnect's own entity
still correctly states "no equivalent is asserted here," because the
sourced edges belong here, on the scheme that was actually notified.

## The EUDI Wallet designation

France Identité is not yet an operational EUDI Wallet — no source read
states one is in production anywhere in the Union (see
[[EU-EUDI-WALLET]]'s own `status: planned`). What is sourced is a
**designation**: the Commission named France Identité as France's
future wallet, and France Titres coordinates two EU-funded pilot
consortia testing wallet use cases under eIDAS 2.0 — **POTENTIAL**
(160 partners, 18 member states plus Ukraine, concluded September
2025) and its successor **APTITUDE** (117 partners, 11 countries plus
Ukraine). `implements-requirement-from` → [[EU-EUDI-WALLET]] is
recorded at `confidence: low` for that reason: real, but prospective.

## Relationships

- `applies-in` [[FR]] — anchor edge.
- `implements-requirement-from` [[EU-EIDAS]], `confidence: high` — a
  direct formal Commission notification.
- `implements-requirement-from` [[EU-EUDI-WALLET]], `confidence: low`
  — a designation, not yet an operational wallet.

`related_entities` also carries [[FR-FRANCECONNECT]], the federation
this scheme is an identity provider within.

## Sources

Listed in frontmatter, all three read directly this pass.
