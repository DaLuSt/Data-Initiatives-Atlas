---
id: DK-KLIMADATASTYRELSEN
type: organisation
name: Klimadatastyrelsen
alternative_names:
  - Agency for Climate Data
  - Danish Agency for Climate Data
description: >
  Danish agency delivering the data and digital solutions that underpin
  Denmark's green transition, climate protection and security, acting on
  behalf of the Minister for Climate, Energy and Utilities. It operates
  Datafordeleren, the single national channel through which Danish basic
  data is distributed, and holds full or partial responsibility for four
  acts: the Act on Geographically Referenced Information, the Danish Act
  transposing the INSPIRE Directive, the Utility Owner Register Act and
  the Address Act. Headed by Director Rikke Hougaard Zeberg since 1 June
  2023.

level: national
country: DK
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - DK
  - DK-DATAFORDELER
  - EU-INSPIRE
  - EU-EUROGEOGRAPHICS
relationships:
  - type: part-of
    target: DK
    source: fact
    evidence: "Confirmed by reading klimadatastyrelsen.dk's own 'Lovstof' page directly (2026-08-25): 'Bekendtgørelsen fastsætter hvilke beføjelser i ovennævnte love, Klimadatastyrelsen udøver på vegne af klima-, energi- og forsyningsministeren' (the executive order sets out which powers under the above acts Klimadatastyrelsen exercises on behalf of the Minister for Climate, Energy and Utilities) — a Danish state agency acting on ministerial authority. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EUROGEOGRAPHICS
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #50. EuroGeographics' own member profile page (eurogeographics.org/member/agency-for-data-supply-and-infrastructure/), read directly 2026-09-19, states 'Member status: Full', 'National name: Klimadatastyrelsen', 'English spelling: Agency for Climate Data', with the agency's own Copenhagen postal address. This is a direct membership statement on EuroGeographics' own site, not the composition-rule inference the other five member edges rest on."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Om Klimadatastyrelsen"
    url: "https://klimadatastyrelsen.dk/om-klimadatastyrelsen/om-os"
    publisher: "Klimadatastyrelsen"
    accessed: "2026-08-25"
  - title: "Organisation"
    url: "https://klimadatastyrelsen.dk/om-klimadatastyrelsen/organisation"
    publisher: "Klimadatastyrelsen"
    accessed: "2026-08-25"
  - title: "Lovstof"
    url: "https://klimadatastyrelsen.dk/om-klimadatastyrelsen/lovstof"
    publisher: "Klimadatastyrelsen"
    accessed: "2026-08-25"
  - title: "Agency for Climate Data — member profile"
    url: "https://eurogeographics.org/member/agency-for-data-supply-and-infrastructure/"
    publisher: "EuroGeographics"
    accessed: "2026-09-19"
---

# Klimadatastyrelsen

> **Closes a gap named on [[DK-DATAFORDELER]] since it was created.**
> "Klimadatastyrelsen, which operates it, is not modelled." All three
> cited pages were read directly this pass.
>
> **Partially closes discovery/unresolved.md row #50, 2026-09-19**:
> EuroGeographics' own member profile confirms this agency's full
> membership. See "A EuroGeographics member, found" below.

## Description

Confirmed by reading klimadatastyrelsen.dk's own "Om os" page directly
(2026-08-25): "Klimadatastyrelsen leverer de data og digitale løsninger,
der danner fundamentet for Danmarks grønne omstilling, klimasikring og
sikkerhed" — Klimadatastyrelsen delivers the data and digital solutions
that form the foundation of Denmark's green transition, climate
protection and security. Confirmed by reading the "Organisation" page
directly: it is headed by Director **Rikke Hougaard Zeberg**, in post
since **1 June 2023**, previously director of Digitaliseringsstyrelsen
([[DK-DIGST]]) from 2017 to 2021.

## It operates the office that runs Datafordeleren

Confirmed by reading klimadatastyrelsen.dk's own "Organisation" page
directly (2026-08-25): the agency's internal structure includes a
dedicated "**Kontor for Datafordeleren**" (Office for the Data
Distributor), covering "Datafordeleren, Grunddata-governance" and headed
by Kontorchef Nanna Barndorff. This is a direct organisational
confirmation, from the agency's own published structure, of the
`maintained-by` edge [[DK-DATAFORDELER]] now carries.

## Four acts, one with an incidental find for [[EU-INSPIRE]]

Confirmed by reading klimadatastyrelsen.dk's own "Lovstof" page directly
(2026-08-25): "Klimadatastyrelsen har helt eller delvist ansvar for
følgende love: Lov om stedbestemt information [Act on Geographically
Referenced Information, Act No. 380 of 26 April 2017], Lov om
infrastruktur for geografisk information i den Europæiske Union
(INSPIRE) [the Danish INSPIRE transposition act], Lov om
Ledningsejerregistret (LER-loven) [Utility Owner Register Act] og
Adresseloven [Address Act]."

The same page names the INSPIRE act precisely: "Lov om infrastruktur for
geografisk information i Den Europæiske Union (INSPIRE-loven). Loven
gennemfører INSPIRE direktivet i dansk ret ... Lbk. nr. 746 af
15.06.2017" — Denmark's INSPIRE transposition, Consolidated Act
(Lovbekendtgørelse) No. 746 of 15 June 2017. [[EU-INSPIRE]] carried no
Danish `applies-in` edge before this pass; it now does, sourced to this
citation.

## Not modelled

- The **four acts named above** as separate law entities. Only the
  INSPIRE act's citation was added as a relationship (on [[EU-INSPIRE]]
  itself); the Act on Geographically Referenced Information, the Utility
  Owner Register Act and the Address Act are named and dated here but no
  entity was created for any of them, matching the threshold this Atlas
  applies elsewhere (e.g. [[PL-GUS]]'s Act on Public Statistics).
- `retsinformation.dk`, Denmark's official legal-text portal, cited on
  the Lovstof page for every act — it is a JavaScript single-page
  application returning no static content ("You need to enable
  JavaScript to run this app"), so none of the underlying legal texts
  were read directly; every citation here is as Klimadatastyrelsen's own
  page quotes it.
- The agency's **predecessor names** — Danish government geodata bodies
  have been renamed and reorganised repeatedly (as, separately,
  [[DK-DIGST]]'s own director came from), and no founding date or
  organisational history was established this pass, hence `start_date:
  null`.

## A EuroGeographics member, found — 2026-09-19

`discovery/unresolved.md` row #50 asks which of EuroGeographics' roughly
60 member organisations are Atlas entities. EuroGeographics' own member
profile page, read directly, confirms Klimadatastyrelsen as a **full
member**, under the English spelling "Agency for Climate Data" — the
agency's former name, retained on the profile despite the 2023 rename
recorded elsewhere on this entity. `participates-in` [[EU-EUROGEOGRAPHICS]]
is recorded at `confidence: high`, since the source is EuroGeographics'
own membership directory rather than the composition-rule inference the
other five member edges rest on.

## Relationships

- `part-of` [[DK]] — anchor edge.
- `participates-in` [[EU-EUROGEOGRAPHICS]] — see above.

[[DK-DATAFORDELER]] carries the `maintained-by` edge pointing here.
[[EU-INSPIRE]] carries the `applies-in` [[DK]] edge this pass's Lovstof
reading supports.

## Sources

Listed in frontmatter. The first three pages were read directly in the
2026-08-25 pass; `retsinformation.dk` was tried and found genuinely
unreadable (a JavaScript single-page application). The EuroGeographics
member profile was added and read directly 2026-09-19.
