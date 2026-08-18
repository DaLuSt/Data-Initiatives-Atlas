---
id: GB-DATA-GOV-UK
type: platform
name: data.gov.uk
alternative_names:
  - Data.gov.uk
  - UK national open data portal
description: >
  The United Kingdom government's official open data catalogue, publishing
  non-personal public sector data as open data. Launched in closed beta on
  30 September 2009 and publicly in January 2010, it lists datasets from
  government departments, local councils and other public bodies across
  health, education, transport, and crime and justice. It is built on CKAN
  and exposes a CKAN API that requires no API key and applies no rate
  limits. It held over 19,000 datasets in 2015, over 40,000 in 2017 and more
  than 47,000 by 2023.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2010-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - GB-GDS
related_entities:
  - GB
  - NL-DATA-OVERHEID
  - PL-DANE-GOV-PL
  - EU-OPEN-DATA-DIRECTIVE
relationships:
  - type: part-of
    target: GB
    source: fact
    evidence: "data.gov.uk is the United Kingdom government's official open data catalogue, listing datasets from government departments, local councils and other public bodies (data.gov.uk). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Data.gov.uk"
    url: "https://en.wikipedia.org/wiki/Data.gov.uk"
    publisher: "Wikipedia"
  - title: "U.K. National Government Open Data Portal"
    url: "https://www.datopian.com/showcase/data-portals/data-gov-uk"
    publisher: "Datopian"
  - title: "Data.gov.uk — Data Portals"
    url: "https://dataportals.org/portal/data_gov_uk/"
    publisher: "Data Portals"
  - title: "Open Data White Paper: Unleashing the Potential"
    url: "https://assets.publishing.service.gov.uk/media/5a74ab5fe5274a529406937d/Open-Data.doc"
    publisher: "HM Government (UK)"
---

# data.gov.uk

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The UK's national open data catalogue. Closed beta **30 September 2009**,
public launch **January 2010**, CKAN-based, and **over 47,000 datasets** by
2023.

## The oldest national open data portal in the Atlas

| Country | Portal | Launched |
|---|---|---|
| **United Kingdom** | **this platform** | **2010** |
| Netherlands | [[NL-DATA-OVERHEID]] | later |
| Poland | [[PL-DANE-GOV-PL]] | later |

The 2010 launch predates [[EU-OPEN-DATA-DIRECTIVE]] by nine years and the
UK's departure from the EU by ten. It is the only national portal in the
Atlas that was **built before there was any European obligation to have
one** — the Open Data White Paper cited here is a 2012 UK policy document,
not a transposition of anything.

## No Open Data Directive edge, and no substitute for one

The other six countries each connect to [[EU-OPEN-DATA-DIRECTIVE]] through
national legislation — [[NL-WHO]], [[DE-DNG]], [[ES-LEY-37-2007]],
[[PL-OTWARTE-DANE]], with Belgium and France still open. **The UK connects
to it not at all**, and no equivalent UK instrument is modelled.

That is a genuine gap rather than a structural fact. The UK had open data
legislation while a member state — the Re-use of Public Sector Information
Regulations — and whether any of it survives as assimilated law was **not
researched**. Unlike the NIS Regulations, where a source states the position
directly, nothing was found here, so nothing is asserted.

The Open Data Directive row of the Compare view will therefore show the UK
as *"nothing recorded"* while showing four implementations elsewhere. That
is accurate about the Atlas and incomplete about the United Kingdom.

## `coverage: medium`

The dataset counts and launch dates are established. The **operator** is
recorded as [[GB-GDS]] in the `organisations:` list on the strength of GDS
holding the common-platform brief, and **no source states that directly** —
which is why there is no `maintained-by` relationship. The same restraint
was used for [[PL-DANE-GOV-PL]], whose operator was also not established.

## Relationships

None asserted. See above for why the operator is an association rather than
a typed edge.

## Sources

Listed in frontmatter. Only one is a government source and it is a 2012
policy paper; the rest are encyclopaedic or portal directories. **No
data.gov.uk page of its own is cited**, which is the obvious first fetch for
a re-verification pass.
