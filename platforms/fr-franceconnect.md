---
id: FR-FRANCECONNECT
type: platform
name: FranceConnect
alternative_names:
  - FranceConnect+
description: >
  French state identity federation service. It confirms a person's identity
  and authenticates them when they access an online service, letting them
  reuse an account they already hold. It involves three parties — the
  online service, an identity provider, and the RNIPP national register of
  natural persons — and gives access to more than 1500 services. A
  higher-assurance variant, FranceConnect+, integrates the France Identité
  digital identity card.

level: national
country: FR
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
organisations:
  - FR-DINUM
related_entities:
  - EU-EIDAS
  - EU-EIDAS2
  - DE-BUNDID
relationships:
  - type: maintained-by
    target: FR-DINUM
    source: fact
    evidence: "DINUM develops shared services and resources including the interministerial state network, FranceConnect, data.gouv.fr and api.gouv.fr (numerique.gouv.fr/numerique-etat/dinum; transformation.gouv.fr DINUM page). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Accueil — FranceConnect"
    url: "https://www.franceconnect.gouv.fr/"
    publisher: "FranceConnect (DINUM)"
  - title: "FranceConnect+"
    url: "https://www.franceconnect.gouv.fr/franceconnect-plus/"
    publisher: "FranceConnect (DINUM)"
  - title: "S'authentifier à des démarches en ligne avec FranceConnect"
    url: "https://france-identite.gouv.fr/usages/s-authentifier-en-ligne/"
    publisher: "France Identité"
  - title: "FranceConnect+ intègre France Identité"
    url: "https://www.interieur.gouv.fr/actualites/communiques-de-presse/franceconnect-integre-france-identite-pour-offrir-plus-de-choix-et"
    publisher: "Ministère de l'Intérieur"
  - title: "API FranceConnect | data.gouv.fr"
    url: "https://www.data.gouv.fr/dataservices/api-franceconnect"
    publisher: "data.gouv.fr"
---

# FranceConnect

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

FranceConnect is a state service that confirms identity and authenticates a
person when they access an online service, letting them use **an account
they already hold** rather than creating another.

Three parties are involved:

1. the **online service** — for example an administration;
2. an **identity provider** — Impots.gouv, Ameli, or La Poste's Identité
   Numérique;
3. the **RNIPP**, the national register of natural persons.

It gives access to **more than 1500 services**. **FranceConnect+** is the
higher-assurance variant, and **France Identité** — a dematerialised
national identity card on a smartphone — acts as an identity provider
through it, taking the reachable services to over 1800.

## Federation, not an account

The design contrast with [[DE-BUNDID]] is the point of recording this
entity, and it is a genuine architectural difference rather than a naming
one:

| | France | Germany |
|---|---|---|
| Model | **identity federation** — reuse an existing account from a chosen provider | **a central citizen account** the user creates |
| Providers | multiple, including private (La Poste) | the state |
| Register | brokered against the **RNIPP** | — |

France brokers between identity providers it does not own; Germany issues
an account. Both reach the same goal — one login across public services —
by opposite means.

**No relationship between them is asserted.** They are national solutions
to a shared problem, which is not a relationship.

## The eIDAS links, and why only one country has one

[[DE-BUNDID]] carries `implements-requirement-from` → [[EU-EIDAS]], at low
confidence, because a German source states its registration and login
follow the eIDAS Regulation.

**No equivalent is asserted here.** Nothing read about FranceConnect
mentions eIDAS, cross-border recognition, or the acceptance of other member
states' eIDs — even though a national identity federation is precisely the
component eIDAS governs.

Nor is anything asserted to [[EU-EIDAS2]], which requires every member state
to offer a European Digital Identity Wallet by the end of 2026 — a deadline
now four months away, with France Identité the obvious French candidate and
no source read connecting them.

Both are queued. The eIDAS2 gap now spans every country in the Atlas and is
about to become a factual question rather than a modelling one.

## Relationships

- Maintained by [[FR-DINUM]].

## Sources

Listed in frontmatter.
