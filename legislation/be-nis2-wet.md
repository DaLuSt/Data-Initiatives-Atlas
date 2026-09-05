---
id: BE-NIS2-WET
type: law
name: NIS2-wet
alternative_names:
  - Wet van 26 april 2024
  - Wet tot vaststelling van een kader voor de cyberbeveiliging van netwerk- en informatiesystemen van algemeen belang voor de openbare veiligheid
  - Loi du 26 avril 2024
  - Belgian NIS2 Act
description: >
  Belgian act of 26 April 2024 establishing a framework for the
  cybersecurity of network and information systems of general interest for
  public security. It transposes the NIS2 Directive into Belgian law and
  replaces the NIS1 act of 7 April 2019. Published in the Belgisch
  Staatsblad on 17 May 2024 and in force, together with its implementing
  royal decree, from 18 October 2024.

level: national
country: BE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2024-10-18
end_date: null
last_verified: "2026-09-05"
previous_version: BE-NIS1-WET
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - BE-CCB
related_entities:
  - EU-NIS2
  - NL-CBW
  - DE-NIS2UMSUCG
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Confirmed by reading four independent sources directly (2026-08-26): eubelius.com and vbo-feb.be both confirm the act's date and 18 October 2024 entry into force; kpmglaw.be and prebes.be both confirm publication in the Belgisch Staatsblad on 17 May 2024 and quote the act's own title. prebes.be states directly: 'De wet van 26 april 2024 ... werd op vrijdag 17 mei gepubliceerd in het Belgisch Staatsblad', and that it 'vervangt de wet van 7 april 2019' — transposing Directive (EU) 2022/2555. CCB's own three cited pages remain bot-walled (403) even with an honest User-Agent."
    confidence: high
    valid_from: 2024-10-18
    valid_until: null
  - type: supersedes
    target: BE-NIS1-WET
    source: fact
    evidence: "Confirmed by reading prebes.be and kpmglaw.be directly (2026-08-26): prebes.be states the 2024 act 'vervangt de wet van 7 april 2019 tot vaststelling van een kader voor de beveiliging van netwerk- en informatiesystemen van algemeen belang voor de openbare veiligheid (de \"NIS1-wet\")' (replaces the NIS1-wet), and kpmglaw.be independently states 'De NIS2-wet zal dus vanaf 18 oktober 2024 de NIS1-wet vervangen.'"
    confidence: high
    valid_from: 2024-10-18
    valid_until: null

sources:
  - title: "De NIS2-wet"
    url: "https://ccb.belgium.be/nl/nis2"
    publisher: "Centrum voor Cybersecurity België (CCB)"
  - title: "Publicatie van de NIS2-wet in het Belgisch Staatsblad"
    url: "https://ccb.belgium.be/nl/news/publicatie-van-de-nis2-wet-het-belgisch-staatsblad"
    publisher: "Centrum voor Cybersecurity België (CCB)"
  - title: "Entry into force of Belgian acts transposing NIS2: what you need to know"
    url: "https://www.eubelius.com/en/news/entry-into-force-of-belgian-acts-transposing-nis2-what-you-need-to-know"
    publisher: "Eubelius"
    accessed: "2026-08-26"
  - title: "Administratieve maatregelen en boetes onder NIS2"
    url: "https://ccb.belgium.be/nl/news/administratieve-maatregelen-en-boetes-onder-nis2"
    publisher: "Centrum voor Cybersecurity België (CCB)"
  - title: "Inwerkingtreding van de NIS 2-wet: bent u er klaar voor?"
    url: "https://www.vbo-feb.be/nl/nieuws/inwerkingtreding-van-de-nis-2-wet-ben-u-er-klaar-voor/"
    publisher: "VBO-FEB (Verbond van Belgische Ondernemingen)"
    accessed: "2026-08-26"
  - title: "NIS2-wet in werking sinds 18 oktober 2024"
    url: "https://www.kpmglaw.be/nl/nieuws/nis2-wet-in-werking-sinds-18-oktober-2024/"
    publisher: "KPMG Law Belgium"
    accessed: "2026-08-26"
  - title: "Publicatie NIS2-wet in Belgisch Staatsblad"
    url: "https://www.prebes.be/nl/nieuws/2024/05/publicatie-nis2-wet-in-belgisch-staatsblad"
    publisher: "Prebes vzw"
    accessed: "2026-08-26"
  - title: "26 APRIL 2024. - Wet tot vaststelling van een kader voor de cyberbeveiliging van netwerk- en informatiesystemen van algemeen belang voor de openbare veiligheid (Justel)"
    url: "https://www.ejustice.just.fgov.be/eli/wet/2024/04/26/2024202344/justel"
    publisher: "Belgisch Staatsblad / Moniteur belge (ejustice.just.fgov.be)"
    accessed: "2026-09-05"
---

# NIS2-wet (Belgium)

> **Verified 2026-08-26.** CCB's own three cited pages are genuinely
> bot-walled (403) even with an honest User-Agent — the same pattern found
> across most `ccb.belgium.be`, `bosa.belgium.be`, `data.gov.be` and
> `statbel.fgov.be` pages this pass. Four independent external sources
> (a law firm, an employers' federation, another law firm, and a
> professional association) were read directly and jointly confirm every
> claim this entity makes: the act's date, publication date, entry into
> force, and its replacement of [[BE-NIS1-WET]]. `verification:
> primary-source`.
>
> **Updated 2026-09-05**: the previously-flagged gap — no Belgisch
> Staatsblad ELI URI cited — is now closed. See below.

## Description

The act of **26 April 2024** establishes a framework for the cybersecurity
of network and information systems of general interest for public security.
It transposes [[EU-NIS2]] and **replaces [[BE-NIS1-WET]]**, the act of
7 April 2019.

- Published in the **Belgisch Staatsblad on 17 May 2024**.
- In force, together with its implementing **royal decree**, from
  **18 October 2024**.
- Coordinated by [[BE-CCB]] and the Prime Minister's office; the royal
  decree designates the CCB as national cybersecurity authority and
  national CSIRT, supported by sectoral authorities.

## Three transpositions of one directive — the Atlas's best comparison

[[EU-NIS2]] is one entity. It now has three national implementations, and
they differ in **date**, in **legislative technique** and in **how cleanly
the Atlas can model them**:

| | Belgium | Germany | Netherlands |
|---|---|---|---|
| Act | [[BE-NIS2-WET]] | [[DE-NIS2UMSUCG]] | [[NL-CBW]] |
| In force | **18 Oct 2024** | 6 Dec 2025 | 15 Aug 2026 |
| Technique | **new act replacing** the NIS1 act | **revises** the existing [[DE-BSIG]] | **new act superseding** [[NL-WBNI]] |
| Predecessor | [[BE-NIS1-WET]] `superseded` | [[DE-BSIG]] stays `active` | [[NL-WBNI]] `superseded` |
| Modelled with | `supersedes`, confidence medium | `supersedes`, **confidence low** | `supersedes`, confidence medium |

Two of the three are clean supersessions the Atlas records without strain.
The German one is an **amending act**, which the Atlas has no relationship
type for — it is recorded as `supersedes` at low confidence with the two
entities deliberately disagreeing, and that remains the batch's principal
open modelling question. Belgium does not resolve it; it does show that the
German case is the exception rather than the norm, which is useful when
deciding whether a new relationship type is worth adding.

The spread of dates is a real finding in itself: **Belgium transposed
NIS2 nearly two years before the Netherlands.** The Atlas can now show
that at a glance, which it could not with one country.

**No relationship between the three national acts is asserted.**

## The ELI URI, found 2026-09-05

The previously-flagged gap — no Belgisch Staatsblad ELI URI cited, unlike
[[BE-GDPR-WET]] — is now closed. Reading
`ejustice.just.fgov.be/eli/wet/2024/04/26/2024202344/justel` directly: the
act's own title page reads *"26 APRIL 2024. — Wet tot vaststelling van een
kader voor de cyberbeveiliging van netwerk- en informatiesystemen van
algemeen belang voor de openbare veiligheid"* — matching this entity's own
recorded title verbatim — with **publication in the Belgisch Staatsblad on
17 May 2024** and official number **2024202344**, both matching the four
independent secondary sources already cited. The publication date now
rests on the statute's own text via Justel, not only on secondary
reporting.

## Sources

Five of eight read directly — eubelius.com, vbo-feb.be, kpmglaw.be,
prebes.be and now ejustice.just.fgov.be's own Justel page all confirm the
act's date, its 17 May 2024 publication, its 18 October 2024 entry into
force, and its replacement of [[BE-NIS1-WET]]. CCB's own three pages
remain bot-walled.
