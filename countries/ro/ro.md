---
id: RO
type: country
name: Romania
alternative_names:
  - Romania
  - România
description: >
  Country anchor entity for Romania, a member state of the European Union
  since 1 January 2007. It is a base anchor: it carries the country's
  position in the European legal and institutional frameworks so that
  entities scoped to it have somewhere to attach, and no national entities
  are modelled yet.

level: national
country: RO
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-20"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Romania is one of the 27 member states of the European Union, having acceded on 1 January 2007; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "RO — Romania (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:RO"
    publisher: "International Organization for Standardization (ISO)"
    accessed: "2026-08-20"
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
    accessed: "2026-08-20"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
    accessed: "2026-08-20"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
    accessed: "2026-08-20"
---

# Romania

> **Verified 2026-08-20.** Every cited source was read and confirmed to
> support what this entity says, including its accession date.
> `verification: primary-source`.

## Description

Romania (ISO 3166-1 alpha-2: **`RO`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No Romania
entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Member state since **1 January 2007** |
| Euro area | No |
| Schengen area | Full member since **1 January 2025** |
| Council of Europe | Member since 1993 |
| EEA | Through EU membership |

> Accession dates in this table were confirmed against the Union's own
> list of member states on 2026-08-20.

## Full Schengen membership in 2025

Romania became a **full Schengen member on 1 January 2025**, with
[[BG]], after joining for air and sea borders only in March 2024 and waiting
thirteen years from first applying.

It is not in the euro area and has no opt-out.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

No EU instrument in the Atlas carries `applies-in` → [[RO]] yet.
That is a gap rather than a finding: as a member state, every
directly applicable EU regulation the Atlas holds does apply here.

## Sources

Listed in frontmatter.
