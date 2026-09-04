---
id: NL-DIGIMELDING
type: platform
name: Digimelding
alternative_names:
  - Digimelding BLT
description: >
  Dutch government facility, one of the four stelselvoorzieningen of the
  Stelsel van Basisregistraties, that lets an organisation with a statutory
  obligation to use authentic data report suspected inaccuracies back to
  the register that holds it. It connects via Digikoppeling and requires
  eHerkenning or a PKIoverheid certificate for access. Reporting back is
  one of the mechanisms used to maintain the quality of the base
  registrations.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-LOGIUS
related_entities:
  - NL-LOGIUS
  - NL-BASISREGISTRATIES
  - NL-DIGIKOPPELING
  - NL-BRP
  - NL-NHR
  - NL-BAG
relationships:
  - type: maintained-by
    target: NL-LOGIUS
    source: fact
    evidence: "Confirmed by reading logius.nl's own Digimelding pages directly (2026-09-04): the main service page states 'Met Digimelding kunt u, namens uw organisatie, mogelijke onjuistheden in de gegevens van een (basis)registratie uniform, betrouwbaar en efficiënt terugmelden' (with Digimelding you can, on behalf of your organisation, report suspected inaccuracies in the data of a base registration back to source, uniformly, reliably and efficiently), and describes it as a service Logius provides. A second page, Logius's own connection conditions ('Aansluitvoorwaarden Digimelding'), independently confirms Logius as the service provider: 'Deze voorwaarden vormen een aanvulling op de Algemene Voorwaarden Logius' (these conditions supplement Logius's General Terms)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading Logius's own 'Stelselvoorzieningen' page directly in an earlier pass on NL-BASISREGISTRATIES (2026-08-28), which names Digimelding as one of four system facilities ('stelselvoorzieningen') supporting the Stelsel van Basisregistraties, alongside Digikoppeling, Digilevering and Stelselcatalogus. Confirmed again this pass by reading logius.nl's own dedicated Digimelding page directly: reporting inaccuracies back is described as 'één van de instrumenten om de kwaliteit van basisregistraties te waarborgen' (one of the instruments to safeguard the quality of base registrations)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: depends-on
    target: NL-DIGIKOPPELING
    source: fact
    evidence: "Confirmed by reading logius.nl's own connection conditions for Digimelding directly (2026-09-04): connecting organisations 'Must connect via Digikoppeling' for webservice access, alongside authentication via eHerkenning (minimum trust level 2) or a valid PKIoverheid certificate with OIN."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Digimelding — Logius"
    url: "https://www.logius.nl/onze-dienstverlening/gegevensuitwisseling/digimelding"
    publisher: "Logius (Ministerie van Binnenlandse Zaken en Koninkrijksrelaties)"
    accessed: "2026-09-04"
  - title: "Aansluitvoorwaarden Digimelding — Logius"
    url: "https://www.logius.nl/onze-dienstverlening/gegevensuitwisseling/digimelding/documentatie/voorwaarden-digimelding"
    publisher: "Logius"
    accessed: "2026-09-04"
  - title: "Digimelding — standaarden.logius.nl"
    url: "https://www.logius.nl/standaarden/digimelding/"
    publisher: "Logius"
  - title: "Digimelding BLT — NORA Online"
    url: "https://www.noraonline.nl/wiki/Digimelding_BLT"
    publisher: "NORA Online"
---

# Digimelding

> **Added 2026-09-04, `verification: primary-source` from creation.** A
> research-queue item flagged as **Next** since the register batch —
> Digimelding was "named in one sentence of one source" on
> [[NL-BASISREGISTRATIES]], not yet its own entity — is now closed. Two
> `logius.nl` pages were read directly before this entity was written.

## Description

Digimelding is the Dutch government facility for **terugmelden**
(reporting back): confirmed by reading `logius.nl`'s own page directly, it
lets an organisation with a legal obligation to use a base registration's
authentic data report suspected inaccuracies back to the registration that
holds it — "uniform, betrouwbaar en efficiënt" (uniform, reliable and
efficient). It can be used embedded within an organisation's own
applications, or as a standalone web portal that also shows the status of
earlier reports.

## One of four stelselvoorzieningen

Digimelding is one of the four system facilities (stelselvoorzieningen)
that support the [[NL-BASISREGISTRATIES]] — alongside [[NL-DIGIKOPPELING]]
(secure exchange between government bodies), Digilevering (event-based
change notifications) and Stelselcatalogus (the integrated concept and
data overview) — confirmed on `logius.nl`'s dedicated "Stelselvoorzieningen"
page in an earlier pass on [[NL-BASISREGISTRATIES]] and corroborated again
this pass on Digimelding's own page. Neither Digilevering nor
Stelselcatalogus has an Atlas entity of its own yet; this closes one of
three, leaving two still queued.

## How it connects

Confirmed by reading Logius's own connection conditions directly:
organisations connect to Digimelding **via [[NL-DIGIKOPPELING]]** for
webservice access, and authenticate either through **eHerkenning**
(minimum trust level 2) for portal access or a valid **PKIoverheid
certificate** with an OIN for webservice access. Connection and use are
free of charge.

## What is confirmed connected, and what is not

WebSearch surfaced two further `logius.nl` news-page titles — "Den Haag
meldt onjuiste gegevens met Digimelding" and "Politie Nederland meldt nu
ook terug via Logius Digimelding-portaal" — suggesting the municipality of
The Hague and the national police both use the service, but neither page
was fetched this pass, so this is noted as an unconfirmed lead rather than
a sourced fact. `noraonline.nl`'s own wiki page on "Digimelding BLT"
(also not fetched this pass, cited from its title and the earlier
register-batch mention only) describes Digimelding covering the [[NL-BRP]],
[[NL-NHR]] (Handelsregister) and [[NL-BAG]] specifically — a narrower scope
than the "any base registration" framing on Logius's own current,
directly-read pages. Both readings are recorded rather than one asserted
over the other, since the narrower list may simply be the original
connected set before later expansion.

## What remains unrecorded

`coverage: low`, deliberately. Not established by anything read this pass:
Digimelding's launch date, the number of organisations currently
connected as reporters (the "over 400 government organisations" figure
found via WebSearch was not independently confirmed by a page read
directly), and its relationship to Digilevering and Stelselcatalogus, the
two sibling facilities still without Atlas entities.

## Relationships

- `maintained-by` [[NL-LOGIUS]].
- `part-of` [[NL-BASISREGISTRATIES]], as one of its four stelselvoorzieningen.
- `depends-on` [[NL-DIGIKOPPELING]] for webservice connections.

## Sources

Listed in frontmatter. Two of four read directly this pass — Logius's main
service page and its connection-conditions page. The standards page and
NORA Online's wiki page are cited for the narrower three-register scope
description but were not independently fetched this pass.
