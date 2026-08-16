---
id: BE-DCAT-AP-BE
type: standard
name: DCAT-AP BE
alternative_names:
  - DCAT-BE
  - Federal DCAT-AP
  - Belgian application profile of DCAT
description: >
  Belgian federal application profile of DCAT, developed as a collaboration
  between several federal administrations. It makes certain fields
  mandatory, recommended or optional relative to the W3C DCAT standard and
  the European DCAT-AP, and the federal DCAT-AP 2 profile — developed by
  the federal administrations involved in implementing the INSPIRE
  Directive — also contains a mapping between INSPIRE and DCAT-AP elements.

level: national
country: BE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-DCAT-AP
  - NL-DCAT-AP-NL
  - DE-DCAT-AP-DE
  - EU-INSPIRE
relationships:
  - type: based-on
    target: EU-DCAT-AP
    source: fact
    evidence: "The Belgian federal profile DCAT-BE was developed as a collaboration between several federal administrations and makes certain fields mandatory, recommended and optional compared to the W3C DCAT standard and the European DCAT-AP standard; the DCAT Application profile for data portals (DCAT-AP) is a specification based on W3C's DCAT for describing public sector datasets (dtservices.bosa.be integratie-metadata; belgif.be/page/specification/dcat-ap.en.html). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: BE-DATA-GOV-BE
    source: fact
    evidence: "The DCAT-AP feed is uploaded via the federal open data portal, which is managed by FOD BOSA, and the portal's metadata integration is documented against the Belgian federal DCAT profile (bosa.belgium.be 'Federale open data portaal: integratie metadata'; dtservices.bosa.be). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: references
    target: EU-INSPIRE
    source: fact
    evidence: "Federal DCAT-AP 2 is the profile developed by the Belgian federal administrations involved in the implementation of the INSPIRE Directive, and it contains a mapping between the INSPIRE and DCAT-AP elements (belgif.be/page/specification/dcat-ap.en.html; github.com/belgif/inspire-dcat). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Specification: DCAT-AP"
    url: "https://belgif.be/page/specification/dcat-ap.en.html"
    publisher: "Belgian Interoperability Framework (BELGIF)"
  - title: "Integratie Metadata | DG DT"
    url: "https://dtservices.bosa.be/nl/services/open-data/integratie-metadata"
    publisher: "FOD BOSA — DG Digitale Transformatie"
  - title: "belgif/inspire-dcat — INSPIRE to DCAT-AP mapping"
    url: "https://github.com/belgif/inspire-dcat"
    publisher: "BELGIF"
  - title: "dcat-be — Website of the Belgian application profile of DCAT"
    url: "https://github.com/openknowledgebe/dcat-be"
    publisher: "Open Knowledge Belgium"
  - title: "Federale open data portaal: integratie metadata"
    url: "https://bosa.belgium.be/nl/services/federale-open-data-portaal-integratie-metadata"
    publisher: "FOD Beleid en Ondersteuning (BOSA)"
---

# DCAT-AP BE

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

DCAT-AP BE is the **Belgian federal application profile of DCAT**,
developed as a collaboration between several federal administrations. Like
the other national profiles, it constrains the parent specification —
making certain fields mandatory, recommended or optional relative to W3C
DCAT and to [[EU-DCAT-AP]].

**Federal DCAT-AP 2** was developed by the federal administrations involved
in implementing [[EU-INSPIRE]], and contains a **mapping between INSPIRE
and DCAT-AP elements**. It is published through [[BE-BELGIF]] and applied
in [[BE-DATA-GOV-BE]].

## The DCAT chain now forks three ways

Batch 15 called the DCAT descent *"the template for what the UN layer
lacks"*. It had one national leaf. Germany gave it a second. Belgium gives
it a third:

```
                     INTL-DCAT (W3C)
                           │ based-on
                     EU-DCAT-AP (SEMIC)
              ┌────────────┼────────────┐
        based-on       based-on      based-on
              ▼            ▼            ▼
     NL-DCAT-AP-NL   DE-DCAT-AP-DE  BE-DCAT-AP-BE
      (Geonovum)    (IT-Planungsrat) (federal admins)
```

**One international standard, one European profile, three national
profiles, each recorded once.** This is the strongest available
demonstration that the country-neutral model does what it claims: the
shared layers did not multiply as countries were added, and no country
needed its own copy of DCAT or of DCAT-AP.

The custody contrast, already noted between the Dutch and German profiles,
extends: a geospatial foundation ([[NL-GEONOVUM]]), a Bund-Länder political
resolution ([[DE-IT-PLANUNGSRAT]]), and an inter-administration
collaboration published through the national interoperability framework.
Same standard family, three institutional logics.

**No relationship between the three national profiles is asserted.**

## The INSPIRE link, and what it is not

`references` → [[EU-INSPIRE]] is recorded because the sources state a
concrete artefact: a mapping between INSPIRE and DCAT-AP elements, with a
dedicated `belgif/inspire-dcat` repository.

`references` is used deliberately rather than `implements-requirement-from`
or `based-on`: a metadata mapping is not a transposition, and this profile
is not derived from the directive. It is the weakest of the three available
types and the accurate one.

Note the asymmetry this creates. [[EU-INSPIRE]] now has:

| Country | Link |
|---|---|
| Germany | `applies-in` + [[DE-GEOZG]] transposes it |
| Belgium | `applies-in` + this profile maps to it |
| Netherlands | **nothing** |

The missing Dutch link was flagged when [[EU-INSPIRE]] was created and is
still open. A third country has now touched the directive without closing
it, which makes it harder to keep calling it an oversight rather than a
gap. It remains first-priority in `discovery/unresolved.md`.

## Relationships

- `based-on` [[EU-DCAT-AP]].
- `applies-to` [[BE-DATA-GOV-BE]].
- `references` [[EU-INSPIRE]].

## Sources

Listed in frontmatter.
