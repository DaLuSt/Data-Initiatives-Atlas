---
id: FR-CNIS
type: organisation
name: Conseil national de l'information statistique
alternative_names:
  - Cnis
  - National Council for Statistical Information
description: >
  French forum for dialogue between producers and users of public
  statistics, established in 1984, evolving from an earlier committee
  created under the founding 1951 law on France's public statistical
  system. It organises consultation through thematic commissions
  meeting at least twice yearly, evaluates the relevance of proposed
  statistical operations, and issues opinions on surveys and
  administrative-data-access requests, so that a yearly programme of
  statistical work aligns with stakeholder needs. The Economy
  Modernisation Law (LME) of 4 August 2008 and its implementing decree
  of 3 March 2009 reformed French public-statistics governance, giving
  it an independent three-pillar structure that includes the Cnis.

level: national
country: FR
region: EU

status: active
confidence: high
coverage: low
verification: primary-source
organisation_role: consultative

start_date: 1984-01-01
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - FR-INSEE
  - FR-INDICATEURS-ODD
relationships:
  - type: part-of
    target: FR
    source: fact
    evidence: "Closes a gap FR-INDICATEURS-ODD's own file had flagged (not a numbered discovery/unresolved.md row: 'the Cnis... the body whose consultation produced the indicator selection' was named but not independently researched). Confirmed by reading cnis.fr's own homepage directly (2026-09-26): the Cnis was 'officially established in 1984, evolving from an earlier committee established by the 1951 law governing France's public statistical system,' and describes its role as facilitating 'concertation' between statisticians and the public, evaluating proposed statistical operations and issuing opinions on surveys. insee.fr's own page on the Cnis, also read directly, independently confirms its role coordinating statistics producers and users and describes its two specialised committees (the Comité du label for survey labelling and the Comité du contentieux for non-response sanctions). Both sources confirm the Economy Modernisation Law of 4 August 2008 and its 3 March 2009 implementing decree reformed public-statistics governance into an independent three-pillar structure including the Cnis. Anchor edge under metadata/relationship-types.md §2.3, asserting French national scope via `level: national`."
    confidence: high
    valid_from: "1984-01-01"
    valid_until: null
  - type: related-to
    target: FR-INDICATEURS-ODD
    source: fact
    evidence: "Confirmed on FR-INDICATEURS-ODD's own already-cited source, which names Cnis consultation as producing the SDG indicator set's selection."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Le Cnis"
    url: "https://www.cnis.fr/"
    publisher: "Conseil national de l'information statistique"
    accessed: "2026-09-26"
  - title: "Le Conseil national de l'information statistique (Cnis)"
    url: "https://www.insee.fr/fr/information/2108287"
    publisher: "INSEE"
    accessed: "2026-09-26"
---

# Conseil national de l'information statistique (Cnis)

> **Created 2026-09-26**, closing a gap [[FR-INDICATEURS-ODD]]'s own
> file had flagged (graph completion, not a numbered
> `discovery/unresolved.md` row). Sourced from Cnis's own homepage and
> INSEE's own page on the Cnis, both read directly.

## Description

The Cnis is France's forum for dialogue between **producers and users of
public statistics**, **established in 1984**, evolving from an earlier
committee created under the founding **1951 law** on France's public
statistical system. Confirmed directly on its own homepage: it organises
consultation through **thematic commissions meeting at least twice
yearly**, evaluates proposed statistical operations, and issues opinions
on surveys and administrative-data-access requests, so that a yearly
statistical work programme aligns with stakeholder needs.

## Two specialised committees

Confirmed independently on INSEE's own page: the Cnis operates through
two committees — the **Comité du label des enquêtes statistiques**,
which examines survey projects from public-statistics producers, and the
**Comité du contentieux des enquêtes statistiques obligatoires**, which
issues sanctions for non-response to mandatory surveys.

## The 2008-2009 independence reform

Both sources confirm the **Economy Modernisation Law (LME) of 4 August
2008** and its **implementing decree of 3 March 2009** reformed French
public-statistics governance, giving it an **independent three-pillar
structure** that includes the Cnis alongside [[FR-INSEE]] and the
statistical service more broadly.

## The body behind France's SDG indicator selection

[[FR-INDICATEURS-ODD]]'s own file names Cnis consultation as the process
that produced the French SDG indicator set's selection — the gap this
entity closes.

## Not modelled

- The **Comité du label** and **Comité du contentieux**, the Cnis's two
  specialised committees — described here in prose, not as separate
  entities.
- The 1951 law and its predecessor committee — described here only as
  the Cnis's own institutional origin.

## Relationships

- `part-of` [[FR]] (anchor edge, `level: national`).
- `related-to` [[FR-INDICATEURS-ODD]] — `confidence: medium`.

## Sources

Listed in frontmatter, both read directly.
