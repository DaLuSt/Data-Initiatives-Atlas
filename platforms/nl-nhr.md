---
id: NL-NHR
type: platform
name: Handelsregister
name_en: "Business Register"
alternative_names:
  - NHR
  - Nieuw Handelsregister
  - HR
  - Dutch Business Register
  - "Business Register"
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
last_verified: "2026-09-27"
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
  - EU-BRIS
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
    evidence: "Confirmed by reading data.overheid.nl's basisregistraties_10 group listing directly (2026-08-27), which names 'Basisregistratie: Handelsregister (HR)' among the ten. Confirmed independently 2026-09-27 by reading digitaleoverheid.nl's own HR page directly via its WordPress REST API (www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=hr — the workaround documented in discovery/unresolved.md row #216, the rendered page itself remaining bot-walled): 'Het Handelsregister is de basisregistratie van alle rechtspersonen en ondernemingen in Nederland,' with statutory basis the Handelsregisterwet, in force as a basisregistratie since 1 July 2008."
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
  - title: "Handelsregister (HR) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/hr/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-27"
    note: "The rendered page is genuinely bot-walled (JavaScript verification challenge). Read directly via the site's own WordPress REST API instead (www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=hr) — the workaround documented in discovery/unresolved.md row #216."
  - title: "Basisregistraties: de 10 basisregistraties"
    url: "https://data.overheid.nl/community/group/basisregistraties_10"
    publisher: "data.overheid.nl"
    accessed: "2026-08-27"
  - title: "Handelsregisterwet 2007 — official text"
    url: "https://wetten.overheid.nl/BWBR0021777"
    publisher: "Overheid.nl (Basiswettenbestand)"
    accessed: "2026-08-27"
  - title: "Business Register (English site of the Kamer van Koophandel)"
    url: "https://www.kvk.nl/en/"
    publisher: "Kamer van Koophandel"
    accessed: "2026-10-07"
---

# NHR — Handelsregister

> **Verified 2026-08-27.** Three of four cited pages read directly, plus
> the Handelsregisterwet 2007's official text added and read as a fourth
> source. This closes the item this entity previously flagged as the one
> register in the batch with no statutory basis modelled at all.
> digitaleoverheid.nl's HR page is confirmed genuinely bot-walled in this
> environment, not merely unread.
>
> **Closed 2026-09-06**: the European network this register belongs to,
> previously flagged as unmodelled, is now [[EU-BRIS]], which carries an
> `applies-to` edge to this entity.
>
> **Closed 2026-09-20**: the KvK-number link to [[NL-BRK]] is now a typed
> `carries-identifier-of` edge, recorded on [[NL-BRK]]'s own entity using a
> new relationship type.
>
> **Closed 2026-09-27**: digitaleoverheid.nl's HR page, genuinely
> bot-walled to direct fetch across two prior passes, is now read
> directly via the site's own WordPress REST API (the workaround
> documented in `discovery/unresolved.md` row #216) — 4 of 4 sources now
> read directly. It adds the mandatory-use phase-in schedule, the
> reporting-duty article's status, and named data couplings to [[NL-BRP]]
> and [[NL-BAG]] — see "Mandatory use, reporting duty, and data couplings"
> below.

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

## Mandatory use, reporting duty, and data couplings — read directly 2026-09-27

digitaleoverheid.nl's own HR page, read directly via the WordPress REST API
workaround, adds detail beyond what this entity previously carried:

- **Roles**: Opdrachtgever (commissioning ministry) is the Ministry of
  Economic Affairs and Climate; the KVK is both Toezichthouder (the KVK
  has an accountant audit the Act's execution and the register's accuracy
  once every three years, Handelsregisterwet art. 41) and Bronhouder/
  Verstrekker (arts. 3-4); Afnemers are, in the source's own words,
  "anyone who wants to consult the data" — the register is public.
- **Mandatory use phased in**: from 1 January 2015, use of the register's
  authentic data became mandatory for government bodies in stages; by
  1 January 2021 mandatory use applied to all bestuursorganen.
- **The reporting duty is not yet in force.** Terugmeldplicht
  (Handelsregisterwet art. 32 — the duty for consumers to report suspected
  inaccuracies back to the source) "is nog niet in werking getreden" (has
  not yet entered into force) — a specific, dated statutory gap the Atlas
  had no prior record of.
- **Named data couplings**: HR "uses" [[NL-BRP]] data (complete for
  residents, incomplete for non-residents) and [[NL-BAG]] data (complete),
  and delivers downstream the BSN, addressable-object ID (partial),
  numbering ID (partial) and address data (complete) to other consumers.
  No dependencies on other stelsel facilities are stated.

These couplings are exactly the "authorised use" and "key-sharing" gaps
[[NL-BASISREGISTRATIES]] itself flags as unmodelled vocabulary
(`uses-data-from` exists but is not asserted here, matching that entity's
own caveat that the type is used sparingly and only where a specific
statutory or documentary trigger names it, as with [[NL-RDW]] and
[[NL-BELASTINGDIENST]]); recorded here in prose as sourced detail rather
than as a new edge, since HR's "use" of BRP/BAG is a stelsel-wide data
dependency rather than KVK acting as a distinct downstream consumer for
its own separate purpose.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-KVK]].
- `governed-by` [[NL-HANDELSREGISTERWET]] — confirmed this pass; see above.
- The `applies-to` edge from [[EU-BRIS]] is recorded on that entity: this
  register is one of the national registers the EU-wide interconnection
  system connects.

**A relationship to [[NL-BRK]] is now asserted**, closing the gap set out
on [[NL-BRP]]: a `carries-identifier-of` edge, recorded on [[NL-BRK]]'s own
entity (BRK carries the KvK number, this register's identifier).

## Sources

Listed in frontmatter. **4 of 4 now read directly.** The BRK catalogue's
Handelsregister page, the data.overheid.nl group listing, and the
Handelsregisterwet 2007's own official text (earlier passes); and,
closing this file 2026-09-27, digitaleoverheid.nl's HR page via the
site's own WordPress REST API
(`www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=hr`) — the workaround
documented in `discovery/unresolved.md` row #216. The rendered HTML at
that URL remains genuinely bot-walled.
