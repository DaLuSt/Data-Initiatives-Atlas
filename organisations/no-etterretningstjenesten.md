---
id: NO-ETTERRETNINGSTJENESTEN
type: organisation
name: Etterretningstjenesten
alternative_names:
  - Norwegian Intelligence Service
  - NIS
  - Forsvarets etterretningstjeneste
description: >
  Norway's foreign and military intelligence service, part of the
  Norwegian Armed Forces. It gathers, processes and analyses information
  relating to Norwegian interests in relation to foreign states,
  organisations and individuals, provides intelligence to Norwegian
  decision-makers, monitors threats such as terrorism and weapons of
  mass destruction, and supports Norwegian forces in international
  operations. Governed by the Lov om Etterretningstjenesten of 2020,
  which also clarifies its operational distinction from the Police
  Security Service (PST). Together with PST and the Nasjonal
  sikkerhetsmyndighet it forms Norway's three intelligence, surveillance
  and security services.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - "NO"
  - NO-ETTERRETNINGSTJENESTELOVEN
  - NO-NSM
  - NO-PST
relationships:
  - type: part-of
    target: "NO"
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #112). Anchor edge under metadata/relationship-types.md §2.3, since no Forsvaret (Norwegian Armed Forces) entity is yet modelled to anchor to instead. Confirmed by reading forsvaret.no's own page directly (2026-09-13): the Norwegian Intelligence Service is 'part of the Norwegian Armed Forces,' gathering, processing and analysing information relating to Norwegian interests in relation to foreign states, organisations and individuals."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NO-ETTERRETNINGSTJENESTELOVEN
    source: fact
    evidence: "Confirmed by reading lovdata.no's own text of LOV-2020-06-19-77 directly (2026-09-13): the Act establishes the Norwegian Intelligence Service's mandate, authority and operational framework, replacing the 1998 Intelligence Service Act. Independently corroborated by eos-utvalget.no, the Parliament's own EOS oversight committee."
    confidence: high
    valid_from: 2021-01-01
    valid_until: null

sources:
  - title: "The Norwegian Intelligence Service"
    url: "https://www.forsvaret.no/en/organisation/norwegian-intelligence-service"
    publisher: "Forsvaret (Norwegian Armed Forces)"
    accessed: "2026-09-13"
  - title: "Legal framework — EOS Committee"
    url: "https://eos-utvalget.no/en/home/about-the-eos-committee/legal-framework/"
    publisher: "EOS-utvalget (Norwegian Parliamentary Intelligence Oversight Committee)"
    accessed: "2026-09-13"
---

# Etterretningstjenesten (Norwegian Intelligence Service)

> **Created 2026-09-13**, closing part of `discovery/unresolved.md` row
> #112, flagged 2026-08-18: "Norway has a national security authority
> and no intelligence services, three days after a batch that gave seven
> other countries both." Forsvaret's own page and the EOS Committee's own
> legal-framework page were read directly.

## Description

Confirmed by reading `forsvaret.no` — the Norwegian Armed Forces' own
site — directly: the Norwegian Intelligence Service "is part of the
Norwegian Armed Forces," and "gathers, processes and analyses
information relating to Norwegian interests seen in relation to foreign
states, organisations and individuals." It also provides intelligence to
decision-makers, monitors threats including terrorism and weapons of
mass destruction, supports Norwegian forces in international operations,
and manages the Armed Forces' space activities.

⚠ Forsvaret's own page cites only the **1998** Intelligence Service Act
as the service's legal basis — outdated per `lovdata.no`'s own record,
which confirms the **2020** Act (in force 2021) as current, repealing the
1998 Act. This entity records the current statute; Forsvaret's page is
retained as a source for the organisational description only.

## One of Norway's three security services

Confirmed on [[NO-NSM]]'s own file, sourced from `nsm.no` directly: NSM
states plainly that it forms, together with **Etterretningstjenesten**
and the **Police Security Service (PST)**, "Norges tre
etterretnings- overvåkings- og sikkerhetstjenester" (Norway's three
intelligence, surveillance and security services). All three are now
Atlas entities.

## Relationships

- `part-of` [[NO]] — anchor edge; no Forsvaret (Norwegian Armed Forces)
  entity is yet modelled to anchor to instead.
- `governed-by` [[NO-ETTERRETNINGSTJENESTELOVEN]] — the 2020 Act.

## Not modelled

- **Forsvaret** (the Norwegian Armed Forces), this entity's actual parent
  body, which would be a more precise `part-of` target than the
  country-level anchor used here.
- The **Etterretningsskolen** (Intelligence School), named on the
  service's own site but not investigated further this pass.

## Sources

Listed in frontmatter, both read directly 2026-09-13.
