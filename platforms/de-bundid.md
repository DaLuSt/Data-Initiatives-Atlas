---
id: DE-BUNDID
type: platform
name: BundID
alternative_names:
  - DeutschlandID
  - Nutzerkonto Bund
  - NKB
description: >
  Central citizen user account for identification and authentication to
  online administrative services of German public institutions at federal,
  Land and municipal level. It supports the online identification function
  of the national identity card, the electronic residence permit, the EU
  citizen card and EU eIDs from other member states, and provides a mailbox
  in which authorities may deposit and legally serve notices. It is
  operated by the Bundesministerium für Digitales und Staatsmodernisierung,
  has its legal basis in the Onlinezugangsgesetz, and is being developed
  into the DeutschlandID as the single nationwide citizen account.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - DE-BMDS
related_entities:
  - DE-OZG
  - EU-EIDAS
  - EU-EUDI-WALLET
relationships:
  - type: governed-by
    target: DE-OZG
    source: fact
    evidence: "Registration and login for BundID follow the provisions of the European eIDAS Regulation, with the legal basis found in the Onlinezugangsgesetz (OZG) (bmds.bund.de/themen/digitaler-staat/digitale-identitaeten/bundid; ozg.brandenburg.de). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "Registration and login for BundID, operated by the Bundesministerium für Digitales und Staatsmodernisierung, follow the provisions of the European eIDAS Regulation; an EU identity (eID) from a European home country is an accepted access method (bmds.bund.de; personalausweisportal.de). NOT READ — search-only."
    confidence: low
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: DE-BMDS
    source: fact
    evidence: "BundID is operated by the Bundesministerium für Digitales und Staatsmodernisierung (bmds.bund.de/themen/digitaler-staat/digitale-identitaeten/bundid). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "BundID"
    url: "https://bmds.bund.de/themen/digitaler-staat/digitale-identitaeten/bundid"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
  - title: "Die BundID"
    url: "https://www.personalausweisportal.de/Webs/PA/DE/buergerinnen-und-buerger/die_bund-id/die_bund_id-node.html"
    publisher: "Personalausweisportal (Bundesministerium des Innern)"
  - title: "Digitale Verwaltung — BundID"
    url: "https://www.digitale-verwaltung.de/Webs/DV/DE/digitale-identitaeten/bundid/bundid-node.html"
    publisher: "Digitale Verwaltung (Bundesministerium des Innern)"
  - title: "BundID (Nutzerkonto) — DeutschlandID"
    url: "https://ozg.brandenburg.de/ozg/de/it-infrastrukturen/it-basiskomponenten/bundid-nutzerkonto-deutschlandid/"
    publisher: "Land Brandenburg"
  - title: "BundID"
    url: "https://de.wikipedia.org/wiki/BundID"
    publisher: "Wikipedia"
---

# BundID

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

BundID — formerly *Nutzerkonto Bund* (NKB) — is the central user account
through which people in Germany identify and authenticate themselves for
online administrative services. With it they can submit online applications
to authorities at **federal, Land and municipal level** and to indirect
administrations, and it provides a **mailbox** in which authorities may,
with the user's consent, deposit issued notices and serve them legally.

Accepted access methods include the **online identification function** of
the national identity card, the electronic residence permit or the EU
citizen card, and an **EU eID from another member state**. The online ID
card is the recommended method because it works with all available online
services.

It is operated by [[DE-BMDS]], its legal basis is in [[DE-OZG]], and
registration and login follow the provisions of the eIDAS Regulation.

## Renaming, not succession

BundID is **being developed into the DeutschlandID**, so that a single
citizen-account solution exists nationwide in future.

**No `successor` entity was created**, and this is a deliberate modelling
choice. The sources describe a continuing service being renamed and
extended, not a new service replacing an old one — the same account, the
same operator, the same legal basis. Creating `DE-DEUTSCHLANDID` with a
`supersedes` relationship would assert a discontinuity the sources do not
describe.

*DeutschlandID* is recorded as an `alternative_name`, which is where the
Atlas puts a name a thing is also known by. If the transition turns out to
involve a genuinely distinct service, this is the entity to revisit.
Logged in `discovery/unresolved.md`.

## ⚠ eIDAS: a relationship recorded at low confidence

`implements-requirement-from` → [[EU-EIDAS]] is the weakest relationship in
the German batch after the BSIG supersession, and for a specific reason.

What the sources say is that BundID's registration and login **"follow the
provisions of"** the eIDAS Regulation, and that EU eIDs are accepted. What
`implements-requirement-from` asserts is that a national instrument
transposes obligations from a higher-level one. A national citizen account
that accepts foreign eIDs is doing something closer to **conforming to**
eIDAS than transposing it — the transposing instrument would be German
legislation, not a portal.

`aligned-with` was the alternative and would arguably be more accurate.
`implements-requirement-from` was chosen because the acceptance of other
member states' eIDs is a concrete cross-border obligation rather than mere
consistency, but the choice is marginal and is flagged rather than buried.

**No relationship to [[EU-EIDAS2]] or [[EU-EUDI-WALLET]] is asserted**,
although eIDAS2 requires all member states to offer European Digital
Identity Wallets by the end of 2026 and BundID is the obvious German
starting point. No source read connects them. This is a live gap that will
matter within months, and it is queued as such.

## Relationships

- `governed-by` [[DE-OZG]].
- `implements-requirement-from` [[EU-EIDAS]] — at low confidence, see above.
- Maintained by [[DE-BMDS]].

## Sources

Listed in frontmatter.
