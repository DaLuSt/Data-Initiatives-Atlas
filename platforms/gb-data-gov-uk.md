---
id: GB-DATA-GOV-UK
type: platform
name: data.gov.uk
alternative_names:
  - Data.gov.uk
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
verification: primary-source
start_date: 2010-01-01
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading en.wikipedia.org's 'Data.gov.uk' article (2026-08-22): 'data.gov.uk is a UK Government project to make available non-personal UK government data as open data. It was launched as closed beta in 30 September 2009, and publicly launched in January 2010 ... As of February 2015, it contained over 19,343 datasets, rising to over 40,000 in 2017, and more than 47,000 by 2023.' Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "National Data Library — the home of UK public data"
    url: "https://www.data.gov.uk/"
    publisher: "GOV.UK"
    accessed: "2026-08-22"
  - title: "Data.gov.uk"
    url: "https://en.wikipedia.org/wiki/Data.gov.uk"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "U.K. National Government Open Data Portal"
    url: "https://www.datopian.com/showcase/data-portals/data-gov-uk"
    publisher: "Datopian"
    accessed: "2026-08-22"
  - title: "Data.gov.uk — Data Portals"
    url: "https://dataportals.org/portal/data_gov_uk/"
    publisher: "Data Portals"
    accessed: "2026-08-22"
  - title: "Open Data White Paper: Unleashing the Potential"
    url: "https://assets.publishing.service.gov.uk/media/5a74ab5fe5274a529406937d/Open-Data.doc"
    publisher: "HM Government (UK)"
    accessed: "2026-08-22"
---

# data.gov.uk

> **Verified 2026-08-22.** en.wikipedia.org's "Data.gov.uk" article and
> data.gov.uk itself were read directly and confirmed the launch dates and
> dataset counts below verbatim. A finding worth flagging: the site now
> brands itself the **"National Data Library"** ("The home of UK public
> data") rather than data.gov.uk — a rebrand this entity does not yet
> record and this pass did not chase further.

## Description

Confirmed verbatim on en.wikipedia.org (2026-08-22): "data.gov.uk is a UK
Government project to make available non-personal UK government data as
open data. It was launched as closed beta in 30 September 2009, and
publicly launched in January 2010 ... As of February 2015, it contained
over 19,343 datasets, rising to over 40,000 in 2017, and more than 47,000
by 2023." The UK's national open data catalogue. Closed beta **30 September 2009**,
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
data.gov.uk page of its own was cited** before this pass; it has now been
added and read directly. Its current title, "National Data Library — The
home of UK public data," is a rebrand not otherwise recorded here and
worth a dedicated look in a future pass.
