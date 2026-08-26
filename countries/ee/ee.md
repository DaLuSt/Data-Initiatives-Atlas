---
id: EE
type: country
name: Estonia
alternative_names:
  - Republic of Estonia
  - Eesti
  - Eesti Vabariik
description: >
  Country anchor entity for Estonia, a member state of the European Union
  since 1 May 2004. It is a base anchor: it carries the country's position
  in the European legal and institutional frameworks so that entities
  scoped to it have somewhere to attach, and no national entities are
  modelled yet.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Estonia is one of the 27 member states of the European Union, having acceded on 1 May 2004; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EE — Estonia (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:EE"
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
  - title: "Timeline — Joining the euro area"
    url: "https://www.consilium.europa.eu/en/policies/join-the-euro-area/timeline-joining-the-euro-area/"
    publisher: "Council of the European Union"
    accessed: "2026-08-20"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
    accessed: "2026-08-20"
---

# Estonia

> **Verified 2026-08-26.** EU-membership sourcing unchanged since
> 2026-08-20. This pass fixed two stale claims below: the anchor said
> no Estonia entity was modelled and separately said X-Road and
> e-Residency were unmodelled gaps — both stopped being true once
> [[EE-AKI]], [[EE-ANDMEPORTAAL]], [[EE-ATS]], [[EE-E-RESIDENCY]],
> [[EE-IKS]], [[EE-RIA]], [[EE-RIHA]], [[EE-STATISTIKAAMET]] and
> [[EE-X-TEE]] were all added, none of which had updated the anchor.

## Description

Estonia (ISO 3166-1 alpha-2: **`EE`**) is a **base country anchor**. It
now anchors nine entities: a data exchange layer, a data portal and its
predecessor system, a digital-identity programme with no territorial
requirement, two data protection and statistics authorities, their
governing acts, and the agency operating the infrastructure layer.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Member state since **1 May 2004** |
| Euro area | Since **1 January 2011** |
| Schengen area | Member |
| Council of Europe | Member since 1993 |
| EEA | Through EU membership |

> Accession dates in this table were confirmed against the Union's own
> list of member states on 2026-08-20.

## A gap this batch once exposed, now closed

Estonia is the most frequently cited digital-government model in Europe.
When this anchor was created, the Atlas held nothing about it: neither
**X-Road** — the distributed data exchange layer that connects Estonian
public registries, and the direct conceptual counterpart of
[[NL-DIGIKOPPELING]] and the Dutch [[NL-BASISREGISTRATIES]] stelsel —
nor **e-Residency**, which has no counterpart anywhere else in the
Atlas. Both are now modelled, as [[EE-X-TEE]] and [[EE-E-RESIDENCY]]
respectively, and both are re-verified as of this pass.

## What this anchor does not yet carry

No general interoperability framework attached to this entity, though
[[EE-X-TEE]] and [[EE-RIHA]] together cover much of that ground.

No EU instrument in the Atlas carries `applies-in` → [[EE]] yet.
That is a gap rather than a finding: as a member state, every
directly applicable EU regulation the Atlas holds does apply here.

## Sources

Listed in frontmatter.
