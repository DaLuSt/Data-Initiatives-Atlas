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
last_verified: "2026-10-01"
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
    evidence: "Confirmed by reading de.wikipedia.org's 'BundID' article (2026-08-22): 'Die gesetzliche Grundlage der BundID findet sich im Onlinezugangsgesetz (OZG).' **Corroborated 2026-10-01** by a primary source, digitale-verwaltung.de's own BundID page (read directly via the cookie-jar workaround, discovery/unresolved.md row #217): the BundID is provided 'als Basisdienst im OZG-Kontext', identity data is stored under '§ 8 OZG', and a transitional rule in '§3 OZGÄndG' keeps the Länder accounts running until they can switch to the BundID."
    confidence: high
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "Confirmed by reading de.wikipedia.org's 'BundID' article (2026-08-22): 'Anmeldung und Registrierung der ... von der Bundesministerium für Digitales und Staatsmodernisierung betriebenen BundID erfolgen nach den Vorgaben der europäischen eIDAS-Verordnung.' bmds.bund.de confirms EU eIDs from other member states are an accepted access method. **Corroborated 2026-10-01** by a government primary source: digitale-verwaltung.de's BundID page (read directly, row #217) says 'Registrierung und Anmeldung bei der BundID erfolgen nach den Vorgaben der europäischen Verordnung über elektronische Identifizierung und Vertrauensdienste (eIDAS-VO)' and lists the admitted means, including 'gemäß eIDAS-VO zugelassene Identifizierungsmittel der EU-Mitgliedstaaten'. Raised from low to medium, not high: the source states conformity with eIDAS requirements, not that BundID transposes the regulation."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: DE-BMDS
    source: fact
    evidence: "Confirmed by reading de.wikipedia.org's 'BundID' article (2026-08-22): the article names the Bundesministerium für Digitales und Staatsmodernisierung as the operator, and bmds.bund.de's own 'BundID' page is published under the ministry's domain. **Corroborated 2026-10-01** by digitale-verwaltung.de's own BundID page (read directly, row #217): 'Die BundID wird als Basisdienst im Sinne des Onlinezugangsgesetzes (OZG) zentral vom Bundesministerium für Digitales und Staatsmodernisierung betrieben und weiterentwickelt' — operated and further developed centrally by the BMDS, stated by a government source rather than inferred from Wikipedia and a domain name."
    confidence: high
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-EUDI-WALLET
    source: fact
    evidence: "Confirmed by reading bmds.bund.de's 'BundID' page (2026-08-22): 'Im Kontext der novellierten eIDAS-Verordnung wird die Anbindung der BundID an die EU Digital Identity Wallet (EUDI-Wallet) ... vorbereitet. Ziel ist eine sichere und nutzendenfreundliche Integration in die BundID.' The connection is described as being prepared, not yet live — recorded at low confidence for that reason. This closes a gap the entity previously flagged as unsourced. **Dated 2026-10-01** by a second government source, personalausweisportal.de's own BundID page (read directly via the cookie-jar workaround, row #217): 'Ab Januar 2027 steht außerdem die staatliche EUDI-Wallet „d-you\" als sichere Zugangsart zur Verfügung' (from January 2027 the state EUDI-Wallet \"d-you\" will also be available as a secure means of access), and 'Für das höchste Vertrauensniveau ist eine Registrierung mit der staatlichen EUDI-Wallet „d-you\" (ab Januar 2027), dem Online-Ausweis oder einer Europäischen ID erforderlich.' This gives the planned connection a date but not an operational status — still a plan, so the edge stays at low and carries no `valid_from`."
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
    accessed: "2026-10-01"
    note: "Read directly via a cookie-jar-aware fetch; the HTTP 400 recorded on 2026-08-22 was a missing session cookie, not a genuine block (discovery/unresolved.md row #217)."
  - title: "Digitale Verwaltung — BundID"
    url: "https://www.digitale-verwaltung.de/Webs/DV/DE/digitale-identitaeten/bundid/bundid-node.html"
    publisher: "Digitale Verwaltung (Bundesministerium des Innern)"
    accessed: "2026-10-01"
    note: "Read directly via a cookie-jar-aware fetch (discovery/unresolved.md row #217)."
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
>
> **Closed 2026-10-01** (row #217): that 400 was a missing session cookie
> too. The page is now read directly. It lists the four ways to register
> (username and password with two-factor authentication, ELSTER
> certificate, Online-Ausweis, European ID), says the state EUDI-Wallet
> "d-you" becomes a fifth, highest-trust option **from January 2027**, and
> records that eleven Länder — Berlin, Brandenburg, Bremen, Hessen,
> Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Saarland,
> Sachsen, Sachsen-Anhalt and Thüringen — have already switched fully to
> the BundID or connected to it, as the OZG-Änderungsgesetz requires of
> all Länder within a transition period.
>
> **Closed 2026-10-01** (`discovery/unresolved.md` row #217): the
> `digitale-verwaltung.de` BundID page, cited but never read, is now read
> directly. It states that the BundID is operated centrally by the BMDS as
> an OZG *Basisdienst*; that the then lead ministry, the BMI, provided it
> in **September 2019**; that it had **over 4.5 million accounts in June
> 2025** and was connected to **over 1,700** online services, platforms
> or portals; and that the OZG-Änderungsgesetz envisages developing it into
> the central German citizen account. Three edges are raised accordingly.
> `start_date` stays `null`: the source gives only a month.

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
