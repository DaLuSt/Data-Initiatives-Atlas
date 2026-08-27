---
id: PL-DANE-GOV-PL
type: platform
name: dane.gov.pl
alternative_names:
  - Portal Otwartych Danych
  - Polish Open Data Portal
description: >
  Polish national open data portal. The Act of 11 August 2021 on open data
  and the re-use of public sector information establishes a data portal as a
  database of public sector information resources, alongside the categories
  of high-value and dynamic data, access to dynamic data through APIs, and
  the opening of publicly funded research data for re-use.

level: national
country: PL
region: EU

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
organisations: []
related_entities:
  - PL-OTWARTE-DANE
  - PL-MC
  - NL-DATA-OVERHEID
  - DE-GOVDATA
  - ES-DATOS-GOB-ES
  - FR-DATA-GOUV
relationships:
  - type: maintained-by
    target: PL-MC
    source: fact
    evidence: "Confirmed by reading gov.pl's own 'Portal danych (Dane.gov.pl)' page directly (2026-08-27): 'Za system odpowiada Minister Cyfryzacji' (the Minister of Digitisation is responsible for the system), closing this entity's previously-flagged 'operator not identified' gap. The same page states the service has been operating 'od maja 2014 r.' (since May 2014) — a bare month, not a specific date, so `start_date` stays `null` rather than being padded to a fabricated day."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: PL-OTWARTE-DANE
    source: fact
    evidence: "Confirmed by reading gov.pl's own Portal Interoperacyjności i Architektury page directly (2026-08-27): the Act of 11 August 2021 on open data and re-use of public sector information establishes a data portal as a database of public sector information resources, alongside the high-value and dynamic data categories, API access to dynamic data and the opening of publicly funded research data. `isap.sejm.gov.pl` remains genuinely CAPTCHA-blocked; `nim.gov.pl`'s cited page now returns HTTP 404 (dead link). dane.gov.pl's own homepage could not be read this pass either — it is a JavaScript-rendered application with no static content for an automated fetch to retrieve. CAVEAT unchanged: the sources establish that the Act provides for a data portal; that dane.gov.pl is that portal is the Atlas connecting the provision to the operating site."
    confidence: low
    valid_from: 2021-12-08
    valid_until: null

sources:
  - title: "Nowa ustawa o otwartych danych — Portal Interoperacyjności i Architektury"
    url: "https://www.gov.pl/web/ia/nowa-ustawa-o-otwartych-danych"
    publisher: "Portal Gov.pl"
    accessed: "2026-08-27"
  - title: "Portal danych (Dane.gov.pl) — Ministerstwo Cyfryzacji"
    url: "https://www.gov.pl/web/cyfryzacja/portal-danych-danegovpl"
    publisher: "Portal Gov.pl — Ministerstwo Cyfryzacji"
    accessed: "2026-08-27"
  - title: "Ustawa z dnia 11 sierpnia 2021 r. o otwartych danych i ponownym wykorzystywaniu informacji sektora publicznego (Dz.U. 2021 poz. 1641) — currently CAPTCHA-blocked"
    url: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20210001641"
    publisher: "Internetowy System Aktów Prawnych (ISAP) — Sejm RP"
  - title: "Nowa ustawa o otwartych danych i ponownym wykorzystywaniu informacji sektora publicznego (dead link, HTTP 404)"
    url: "https://nim.gov.pl/aktualnosci/nowa-ustawa-o-otwartych-danych-i-ponownym-wykorzystywaniu-informacji-sektora-publicznego.html"
    publisher: "Narodowy Instytut Muzealnictwa (NIM)"
---

# dane.gov.pl

> **Verified 2026-08-27.** A second gov.pl page — the Ministry of
> Digitisation's own "Portal danych (Dane.gov.pl)" page, not previously
> cited — was found via search and read directly, closing the
> long-standing "operator not identified" gap. Two of four cited pages
> are now read directly; `isap.sejm.gov.pl` remains genuinely
> CAPTCHA-blocked and `nim.gov.pl`'s page is a dead link (404).
> dane.gov.pl's own homepage remains a JavaScript-rendered application
> with no static content an automated fetch can retrieve, so the
> portal's own voice was reached through the Ministry's page about it
> rather than the portal itself.

## Description

dane.gov.pl is Poland's national open data portal. Confirmed by reading
gov.pl's own page directly: **"Za system odpowiada Minister Cyfryzacji"**
(the Minister of Digitisation is responsible for the system), and the
service has been operating **since May 2014** — a bare month, not a
specific date, so `start_date` stays `null`.

[[PL-OTWARTE-DANE]] **establishes a data portal** as a database of public
sector information resources — one of the changes that act brought
alongside the high-value and dynamic data categories, API access, and the
opening of publicly funded research data.

## The `governed-by` edge is `confidence: low`, deliberately

The sources establish that the 2021 Act **provides for a data portal**. That
dane.gov.pl **is** that portal is the Atlas joining the statutory provision
to the operating site — a short step, and still a step the sources do not
take.

This is the same discipline applied to [[ES-DATOS-GOB-ES]], whose
`applies-to` edge is marked `source: interpretation` because the sources
show the portal publishing a norm's documentation rather than stating that
the norm governs it.

The difference is that here the *statutory* basis is direct, so the edge is
`source: fact` with the caveat in its evidence, rather than an
interpretation.

## Six national open data portals

| Country | Portal | Custodian modelled? |
|---|---|---|
| Netherlands | [[NL-DATA-OVERHEID]] | **no** |
| Germany | [[DE-GOVDATA]] | yes — [[DE-FITKO]] |
| France | [[FR-DATA-GOUV]] | yes — [[FR-DINUM]] |
| Spain | [[ES-DATOS-GOB-ES]] | yes — [[ES-RED-ES]] |
| **Poland** | **dane.gov.pl** | **yes — [[PL-MC]]** |

Spain's and Poland's custodian gaps have both since closed — [[ES-RED-ES]]
was created in the Spain re-verification pass, and this entity's own
`maintained-by` edge to [[PL-MC]] closes here. Only the Dutch portal now
has no custodian in the graph, because it was never researched.

`coverage` moves from `low` to **medium**: the portal's operator and
approximate launch date (since May 2014) are now recorded. Its exact
launch date, dataset count and relationship to [[PL-COI]]'s systems
remain unrecorded.

## Not asserted

**No relationship to a Polish DCAT profile.** [[EU-DCAT-AP]] has four
national children in the Atlas; whether Poland has a fifth was not
researched. Queued.

**No relationship to the other five portals.** They are national solutions
to a shared problem, which is not a relationship.

## Relationships

- `maintained-by` [[PL-MC]] — confirmed this pass via gov.pl's own page;
  `confidence: medium`.
- `governed-by` [[PL-OTWARTE-DANE]] — low confidence, see above.

## Sources

Listed in frontmatter, two of four read directly this pass. Neither read
page is the portal's own site — `dane.gov.pl` itself remains a
JavaScript-rendered application with no static content to fetch — but
one is the Ministry of Digitisation's own page naming itself as
operator, which is the portal's own institutional voice at one remove.
