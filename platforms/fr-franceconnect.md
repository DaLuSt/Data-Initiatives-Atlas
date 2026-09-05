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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
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
  - FR-FRANCE-IDENTITE
relationships:
  - type: maintained-by
    target: FR-DINUM
    source: fact
    evidence: "Confirmed by reading numerique.gouv.fr's own DINUM page directly (2026-08-26): DINUM 'développe des services et ressources partagées comme le réseau interministériel de l'État, FranceConnect, data.gouv.fr ou api.gouv.fr' (develops shared services and resources including the interministerial state network, FranceConnect, data.gouv.fr and api.gouv.fr) — DINUM's own page, not a secondary source, names FranceConnect directly."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Accueil — FranceConnect"
    url: "https://www.franceconnect.gouv.fr/"
    publisher: "FranceConnect (DINUM)"
    accessed: "2026-08-26"
  - title: "FranceConnect+"
    url: "https://www.franceconnect.gouv.fr/franceconnect-plus/"
    publisher: "FranceConnect (DINUM)"
    accessed: "2026-08-26"
  - title: "S'authentifier à des démarches en ligne avec FranceConnect"
    url: "https://france-identite.gouv.fr/usages/s-authentifier-en-ligne/"
    publisher: "France Identité"
    accessed: "2026-08-26"
  - title: "API FranceConnect | data.gouv.fr"
    url: "https://www.data.gouv.fr/dataservices/api-franceconnect"
    publisher: "data.gouv.fr"
    accessed: "2026-08-26"
  - title: "FranceConnect+ intègre France Identité"
    url: "https://www.interieur.gouv.fr/actualites/communiques-de-presse/franceconnect-integre-france-identite-pour-offrir-plus-de-choix-et"
    publisher: "Ministère de l'Intérieur"
---

# FranceConnect

> **Verified 2026-08-26.** Four of five cited pages were read directly.
> FranceConnect's own homepage confirms the "1 500 services" figure
> verbatim, and France Identité's own page confirms the RNIPP is held
> by **INSEE** — a detail this entity did not previously carry.
> `interieur.gouv.fr` remains genuinely bot-walled (403) even with an
> honest User-Agent.
>
> **Updated 2026-09-05**: France Identité is now its own entity,
> [[FR-FRANCE-IDENTITE]] — see "The eIDAS links" below for why the
> eIDAS/eIDAS2 gap this entity previously flagged is resolved there,
> not here.

## Description

Confirmed by reading franceconnect.gouv.fr directly (2026-08-26):
FranceConnect is a state service that confirms identity and
authenticates a person when they access an online service, letting
them use **an account they already hold** rather than creating
another: "il vous permet d'accéder à plus de 1 500 services en
utilisant un seul identifiant et un seul mot de passe" (it lets you
access more than 1,500 services using a single username and password).

Three parties are involved:

1. the **online service** — for example an administration;
2. an **identity provider** — impots.gouv.fr, ameli.fr, or La Poste's
   Identité Numérique (all confirmed by name on FranceConnect's own
   page, which also names MSA and TrustMe as additional providers);
3. the **RNIPP**, the national register of natural persons, confirmed
   by reading france-identite.gouv.fr directly to be held by
   **INSEE** — "le répertoire national d'identification des personnes
   physiques (RNIPP) de l'INSEE."

**FranceConnect+** is the higher-assurance variant, and
[[FR-FRANCE-IDENTITE]] — a dematerialised national identity card on a
smartphone — acts as an identity provider through it, confirmed to
take the reachable services to **"plus de 1800 services"**.

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

## The eIDAS links — resolved, but not on this entity

[[DE-BUNDID]] carries `implements-requirement-from` → [[EU-EIDAS]], at low
confidence, because a German source states its registration and login
follow the eIDAS Regulation.

**No equivalent is asserted here, and none should be.** Nothing read about
FranceConnect itself mentions eIDAS, cross-border recognition, or the
acceptance of other member states' eIDs. The reason is not that the gap is
unresolved: it is that the eIDAS obligation attaches to the identity scheme
being federated, not the federation broker. That scheme now has its own
entity — **[[FR-FRANCE-IDENTITE]]**, added 2026-09-05, which carries a
high-confidence `implements-requirement-from` → [[EU-EIDAS]] (a direct
Commission notification of 9 September 2024) and a low-confidence one to
[[EU-EUDI-WALLET]] (a Commission designation as France's future wallet,
not yet operational). See that entity for the sourcing.

## Relationships

- Maintained by [[FR-DINUM]].

## Sources

Listed in frontmatter, four of five read directly this pass;
`interieur.gouv.fr` remains genuinely bot-walled (403) even with an
honest User-Agent.
