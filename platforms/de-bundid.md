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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading de.wikipedia.org's 'BundID' article (2026-08-22): 'Die gesetzliche Grundlage der BundID findet sich im Onlinezugangsgesetz (OZG).'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "Confirmed by reading de.wikipedia.org's 'BundID' article (2026-08-22): 'Anmeldung und Registrierung der ... von der Bundesministerium für Digitales und Staatsmodernisierung betriebenen BundID erfolgen nach den Vorgaben der europäischen eIDAS-Verordnung.' bmds.bund.de confirms EU eIDs from other member states are an accepted access method."
    confidence: low
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: DE-BMDS
    source: fact
    evidence: "Confirmed by reading de.wikipedia.org's 'BundID' article (2026-08-22): the article names the Bundesministerium für Digitales und Staatsmodernisierung as the operator, and bmds.bund.de's own 'BundID' page is published under the ministry's domain."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-EUDI-WALLET
    source: fact
    evidence: "Confirmed by reading bmds.bund.de's 'BundID' page (2026-08-22): 'Im Kontext der novellierten eIDAS-Verordnung wird die Anbindung der BundID an die EU Digital Identity Wallet (EUDI-Wallet) ... vorbereitet. Ziel ist eine sichere und nutzendenfreundliche Integration in die BundID.' The connection is described as being prepared, not yet live — recorded at low confidence for that reason. This closes a gap the entity previously flagged as unsourced."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "BundID"
    url: "https://bmds.bund.de/themen/digitaler-staat/digitale-identitaeten/bundid"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
    accessed: "2026-08-22"
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
    accessed: "2026-08-22"
---

# BundID

> **Verified 2026-08-22.** de.wikipedia.org's "BundID" article and
> bmds.bund.de's own "BundID" page were read directly. One gap the entity
> previously flagged as unsourced — a connection to the EUDI-Wallet — is
> now closed with a source; see below. `personalausweisportal.de` no
> longer resolves (400) and was not re-read.

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

**The EUDI-Wallet gap is now closed.** bmds.bund.de's own BundID page, read
2026-08-22, states directly: "Im Kontext der novellierten eIDAS-Verordnung
wird die Anbindung der BundID an die EU Digital Identity Wallet
(EUDI-Wallet) ... vorbereitet." The connection is described as being
*prepared*, not live, so the new `implements-requirement-from` →
[[EU-EUDI-WALLET]] edge is recorded at `confidence: low` — it is real, but
not yet operational. No relationship to [[EU-EIDAS2]] specifically (the
amending Regulation itself, as distinct from the Wallet it establishes) is
asserted, because no source read names it separately from the Wallet.

## Relationships

- `governed-by` [[DE-OZG]].
- `implements-requirement-from` [[EU-EIDAS]] — at low confidence, see above.
- `implements-requirement-from` [[EU-EUDI-WALLET]] — at low confidence, an
  in-preparation connection.
- Maintained by [[DE-BMDS]].

## Sources

Listed in frontmatter.
