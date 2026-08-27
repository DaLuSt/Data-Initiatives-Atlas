---
id: NL-NHR
type: platform
name: Handelsregister
alternative_names:
  - NHR
  - Nieuw Handelsregister
  - HR
  - Dutch Business Register
description: >
  The Dutch trade register: a public register containing information about
  businesses and legal entities active in the Netherlands, held by the Kamer
  van Koophandel, and one of the ten registrations in the stelsel van
  basisregistraties. Its identifier, the KvK number, is increasingly carried
  in products of the cadastral base registry for organisations, which is one
  of the documented links between the two registers.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-KVK
related_entities:
  - NL-HANDELSREGISTERWET
  - NL-BASISREGISTRATIES
  - NL-KVK
  - NL-BRK
relationships:
  - type: governed-by
    target: NL-HANDELSREGISTERWET
    source: fact
    evidence: "Confirmed by reading wetten.overheid.nl's own text of BWBR0021777 directly (2026-08-27): 'Wet van 22 maart 2007, houdende regels omtrent een basisregister van ondernemingen en rechtspersonen (Handelsregisterwet 2007)' — rules concerning a basic register of enterprises and legal entities, maintained by the Kamer van Koophandel. This closes the item this entity previously called out as the one register with no statutory basis modelled at all: the Act is confirmed by name, date and content."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading data.overheid.nl's basisregistraties_10 group listing directly (2026-08-27), which names 'Basisregistratie: Handelsregister (HR)' among the ten. digitaleoverheid.nl's dedicated HR page returned a bot-verification wall on two separate attempts this pass and is confirmed genuinely unreadable in this environment, not merely unread."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-KVK
    source: fact
    evidence: "Confirmed by reading catalogus.kadaster.nl's own BRK catalogue page directly (2026-08-27): the Handelsregister is 'gerelateerd aan' (related to) the BRK and defined there as 'a register of enterprises and legal entities,' managed by the Kamer van Koophandel — corroborated by the Handelsregisterwet 2007's own text (Article 2), also read directly this pass, which assigns the register to the Kamer van Koophandel."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Handelsregister | Basisregistratie Kadaster (BRK)"
    url: "https://catalogus.kadaster.nl/brk/nl/page/Handelsregister"
    publisher: "Kadaster"
    accessed: "2026-08-27"
  - title: "Handelsregister (HR) — Stelsel van basisregistraties (confirmed bot-walled, not read)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/hr/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Basisregistraties: de 10 basisregistraties"
    url: "https://data.overheid.nl/community/group/basisregistraties_10"
    publisher: "data.overheid.nl"
    accessed: "2026-08-27"
  - title: "Handelsregisterwet 2007 — official text"
    url: "https://wetten.overheid.nl/BWBR0021777"
    publisher: "Overheid.nl (Basiswettenbestand)"
    accessed: "2026-08-27"
---

# NHR — Handelsregister

> **Verified 2026-08-27.** Three of four cited pages read directly, plus
> the Handelsregisterwet 2007's official text added and read as a fourth
> source. This closes the item this entity previously flagged as the one
> register in the batch with no statutory basis modelled at all.
> digitaleoverheid.nl's HR page is confirmed genuinely bot-walled in this
> environment, not merely unread.

## Description

The Handelsregister is the public Dutch register of businesses and legal
entities, held by [[NL-KVK]]. It is one of the ten registrations in
[[NL-BASISREGISTRATIES]].

The **KvK number** is its identifier, and the Kadaster's own BRK catalogue
records that KvK numbers are increasingly carried in BRK products for
organisations — a concrete, sourced instance of two base registries sharing
a key.

## The statutory basis, now confirmed by the Act's own text

This entity previously flagged itself as the one register in the batch with
**no statutory basis modelled at all**. Reading wetten.overheid.nl's own
text of the Handelsregisterwet 2007 (BWBR0021777) directly this pass closes
that gap: "Wet van 22 maart 2007, houdende regels omtrent een basisregister
van ondernemingen en rechtspersonen" — a basic register of enterprises and
legal entities, assigned to the Kamer van Koophandel.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-KVK]].
- `governed-by` [[NL-HANDELSREGISTERWET]] — confirmed this pass; see above.

**No relationship to [[NL-BRK]] is asserted**, despite the shared KvK
number, for the reason set out on [[NL-BRP]]: the Atlas has no relationship
type for a key-sharing coupling between two registers.

## Sources

Listed in frontmatter, three of four read directly this pass — the BRK
catalogue's Handelsregister page, the data.overheid.nl group listing, and
the Handelsregisterwet 2007's own official text (added this pass).
digitaleoverheid.nl's HR page is confirmed genuinely bot-walled in this
environment on two separate attempts, not merely unread.
