---
id: GB-OS
type: organisation
name: Ordnance Survey
alternative_names:
  - OS
  - Ordnance Survey Limited
description: >
  The national mapping agency for Great Britain, providing the country's
  geospatial infrastructure for emergency response, land-use planning,
  transport and environmental protection. It leads and coordinates United
  Kingdom involvement in the United Nations Committee of Experts on Global
  Geospatial Information Management, acting as Secretariat for the UK
  delegation and as Head of Delegation at Committee of Experts meetings on
  behalf of the Geospatial Commission, and has agreed to lead a review for
  UN-GGIM in collaboration with its Secretariat and the UN-GGIM Europe
  Regional Committee.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - UN-GGIM
  - GB-GEOSPATIAL-STRATEGY
  - GB-ONS
  - NL-KADASTER
  - EU-EUROGEOGRAPHICS
relationships:
  - type: participates-in
    target: UN-GGIM
    source: fact
    evidence: "Confirmed verbatim by reading gdsgeospatial.blog.gov.uk's 'The UN-GGIM 14th session: flying the flag' post (2026-08-22): 'Ordnance Survey acts as the Secretariat for the UK Delegation, leads and coordinates UK involvement, and acts as Head of UK Delegation during the Committee of Expert meetings on behalf of the Geospatial Commission.' The 11th Session statement (ggim.un.org, read 2026-08-22) is delivered by 'David Henderson, Chief Geospatial Officer, Ordnance Survey, Head of UK Delegation', confirming the Head-of-Delegation role independently at an earlier session."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EUROGEOGRAPHICS
    source: fact
    evidence: "EuroGeographics is the membership association for the European National Mapping, Cadastral and Land Registry Authorities, an international not-for-profit association (AISBL/IVZW under Belgian law, BCE 833 607 112) bringing together 63 organisations from 46 countries covering the whole of geographical Europe (eurogeographics.org/our-members/; eurogeographics.org). NOT READ — search-only. Membership follows from the sourced composition rule rather than from a source naming this authority, the same basis on which the national standardisation bodies were attached to EU-CEN. This entity is Great Britain's national mapping agency."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Ordnance Survey — Great Britain's national mapping service"
    url: "https://www.ordnancesurvey.co.uk/"
    publisher: "Ordnance Survey"
    accessed: "2026-08-22"
  - title: "UN-GGIM 11th Session — Agenda item 3, United Kingdom"
    url: "https://ggim.un.org/meetings/GGIM-committee/11th-Session/documents/Agenda_item-3%20-%20UK.pdf"
    publisher: "United Nations Committee of Experts on Global Geospatial Information Management (UN-GGIM)"
    accessed: "2026-08-22"
  - title: "The UN-GGIM 14th session: flying the flag"
    url: "https://gdsgeospatial.blog.gov.uk/2024/09/19/the-un-ggim-14th-session-flying-the-flag/"
    publisher: "Geospatial Commission / Government Digital Service (UK)"
    accessed: "2026-08-22"
  - title: "An ambitious partnership programme between ONS and OS — memorandum of understanding"
    url: "https://www.ons.gov.uk/news/statementsandletters/anambitiouspartnershipprogrammebetweenonsandosmemorandumofunderstanding"
    publisher: "Office for National Statistics (UK)"
    accessed: "2026-08-22"
---

# Ordnance Survey

> **Verified 2026-08-22.** gdsgeospatial.blog.gov.uk's UN-GGIM session
> report, the 11th-session UK statement PDF and ordnancesurvey.co.uk's own
> homepage were read directly and confirmed the claims below, verbatim in
> places. `eurogeographics.org`'s members page was fetched but its member
> list did not render as extractable text, so that relationship's
> composition-rule basis is unchanged rather than newly confirmed.

## Description

Confirmed verbatim on ordnancesurvey.co.uk (2026-08-22): "Ordnance Survey |
Great Britain's national mapping service." Ordnance Survey is the
**national mapping agency for Great Britain** and the
provider of its geospatial infrastructure. Internationally it **leads the UK
delegation to [[UN-GGIM]]**, acting as Secretariat and Head of Delegation on
behalf of the Geospatial Commission — confirmed verbatim on
gdsgeospatial.blog.gov.uk.

## Closing the Atlas's most conspicuous UK gap

[[GB]] and `countries/gb/index.md` both recorded that **the United Kingdom
joined the Atlas with no geospatial entity at all** — the only country in
[[DOMAIN-GEOSPATIAL]] with none — because the Geospatial Commission had been
merged into [[GB-GDS]] in January 2025 and Ordnance Survey was not
researched. This entity closes that.

## A second route to the UN layer, and it is not the statistical one

[[GB-ONS]] reaches the international layer through [[UN-CES]] because the UK
cannot use [[EU-ESS]]. Ordnance Survey does the same thing in a different
domain, through [[UN-GGIM]] — and here there is **no EU alternative to be
excluded from**, because UN-GGIM is a UN committee that member and non-member
states join alike.

So the UK now has two independent upward links, both to the **UN** rather
than the EU:

| Domain | UK body | Reaches |
|---|---|---|
| Statistics | [[GB-ONS]] | [[UN-CES]] |
| Geospatial | **this entity** | **[[UN-GGIM]]** |

For a country with no regional parent, the UN layer is turning out to be the
one that carries the connections — which is the opposite of the six member
states, whose upward links run through the EU.

## `coverage: low`

Ordnance Survey's legal form, its ownership, the OS MasterMap and OS Open
Data products, its licensing model and the National Geographic Database are
**all unrecorded**. So is the ONS partnership, whose memorandum of
understanding is cited here but produced no asserted relationship.

⚠ **The name is a trap the Atlas should not fall into twice.** Ordnance
Survey maps **Great Britain**, not the United Kingdom: Northern Ireland is
mapped by Ordnance Survey of Northern Ireland, which is not modelled. This
entity carries `country: GB`, and for once the ISO code and the actual
coverage coincide exactly — unlike every other GB entity, where `GB` is the
alpha-2 code for a state that includes Northern Ireland.

## Not modelled

- **The Geospatial Commission** as an independent body — merged into
  [[GB-GDS]] in January 2025.
- **Ordnance Survey of Northern Ireland**, and the resulting UK-wide gap.
- **OS MasterMap**, the National Geographic Database and the OS Open Data
  products — the things a reader would most want linked to
  [[DOMAIN-GEOSPATIAL]].
- **The UN-GGIM Europe Regional Committee**, named in the evidence and not an
  Atlas entity, although [[UN-GGIM-EUROPE]] does exist — see below.

## Relationships

- `participates-in` [[UN-GGIM]].

No edge to [[UN-GGIM-EUROPE]] is asserted. The sources say the UK's review
work is *supported by* the Europe Regional Committee, which is not the same
as membership of it, and the Atlas does not have the second claim.

## Sources

Listed in frontmatter.
