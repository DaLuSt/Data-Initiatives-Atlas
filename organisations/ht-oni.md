---
id: HT-ONI
type: organisation
name: "Office National d'Identification"
name_en: "National Identification Office"
alternative_names:
  - "ONI"
  - "National Identification Office"
description: >
  Haiti's national identification office. It keeps the Registre National
  d'Identification, issues the national identification number and the
  national identification card (CIN), and is run under the decree of 1 June
  2005; the 1987 decree that created it is cited in that decree.

level: national
country: HT
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 1987-09-21
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - HT
  - HT-DECRET-2005-ID
relationships:
  - type: part-of
    target: HT
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. oni.gouv.ht, read directly (2026-10-11), is the website of the 'Office National d'Identification (ONI)' of the République d'Haïti; its stated mission is 'Garantir le caractère universel et sécuritaire du droit à l'identité'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: HT-DECRET-2005-ID
    source: fact
    evidence: "The decree of 1 June 2005, read directly on the ONI's own site (2026-10-11), sets the ONI's administration (a board with ministry representatives, a Director General appointed by presidential order, articles 19-24), tasks it with registering Haitians at birth in the Registre National d'Identification and with issuing the national identification number, and its preamble cites the decree of 21 September 1987 creating the Office."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Décret (1er juin 2005) — Office National d'Identification (ONI)"
    url: "https://oni.gouv.ht/580-2/"
    publisher: "Office National d'Identification (ONI), République d'Haïti"
    accessed: "2026-10-11"
  - title: "Office National d'Identification (ONI) — accueil"
    url: "https://www.oni.gouv.ht"
    publisher: "Office National d'Identification (ONI), République d'Haïti"
    accessed: "2026-10-11"
---

# Office National d'Identification (ONI)

> **Created 2026-10-11** (roadmap #470, Haiti). The ONI's website and the full text of the 2005 decree on it were read directly. Its page on data protection is empty: nothing there mentions data protection or privacy.

## Description

The ONI is Haiti's national identification office. Its site states its mission as to "garantir le caractère universel et sécuritaire du droit à l'identité" and describes the Carte d'Identification Nationale (CIN), whose design and validation project it dates to 2005, and an article on a move toward a biometric national identity card. The 2005 decree ([[HT-DECRET-2005-ID]]) cites a decree of **21 September 1987** "créant l'Office National d'Identification des personnes physiques", which is where this entity's start date comes from; the date is that citation, and the 1987 decree itself was not read.

Under the 2005 decree the ONI registers Haitians in the Registre National d'Identification from birth, gives each a national identification number for life, and issues the CIN. It is run by a board of ministry representatives and a Director General appointed by presidential order.

## Relationships

`part-of` [[HT]] (anchor edge); `governed-by` [[HT-DECRET-2005-ID]].
