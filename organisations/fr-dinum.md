---
id: FR-DINUM
type: organisation
name: Direction interministérielle du numérique
alternative_names:
  - DINUM
  - Interministerial Digital Directorate
description: >
  French interministerial digital directorate, a service of the Prime
  Minister placed under the authority of the minister responsible for
  transformation and the civil service. It develops the state's digital
  strategy and steers its implementation, supports ministries in their
  digital transformation, advises the government, and builds shared
  services and resources including the interministerial state network,
  FranceConnect, data.gouv.fr and api.gouv.fr.

level: national
country: FR
region: null

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
  - FR-ETALAB
relationships: []

sources:
  - title: "La direction interministérielle du numérique (DINUM)"
    url: "https://www.numerique.gouv.fr/numerique-etat/dinum/"
    publisher: "DINUM — numerique.gouv.fr"
  - title: "Direction Interministérielle du Numérique (DINUM)"
    url: "https://www.transformation.gouv.fr/le-ministere/directions/dinum"
    publisher: "Ministère de la Transformation et de la Fonction publiques"
  - title: "Direction interministérielle du numérique"
    url: "https://www.economie.gouv.fr/direction-interministerielle-du-numerique"
    publisher: "Ministère de l'Économie et des Finances"
  - title: "Organisation — Direction interministérielle du numérique"
    url: "https://www.data.gouv.fr/organizations/direction-interministerielle-du-numerique"
    publisher: "data.gouv.fr"
  - title: "Interministerial Digital Directorate (DINUM)"
    url: "https://en.wikipedia.org/wiki/Interministerial_Digital_Directorate"
    publisher: "Wikipedia"
---

# DINUM — Direction interministérielle du numérique

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

DINUM is a **service of the Prime Minister**, placed under the authority of
the minister responsible for transformation and the civil service. Its
mission is to develop the state's digital strategy and steer its
implementation.

It:

- accompanies ministries in their digital transformation;
- advises the government;
- develops shared services and resources, including the interministerial
  state network, [[FR-FRANCECONNECT]], [[FR-DATA-GOUV]] and api.gouv.fr;
- publishes and maintains [[FR-RGI]].

It comprises six departments and four missions, one of which is
[[FR-ETALAB]].

## The most centralised digital-government body in the Atlas

Four countries now have a central digital-government organisation, and they
are constituted very differently:

| Country | Body | Sits where |
|---|---|---|
| France | **DINUM** | a service of the **Prime Minister** |
| Germany | [[DE-BMDS]] | a dedicated **federal ministry** |
| Belgium | [[BE-BOSA]] | a federal **horizontal support service** |
| Netherlands | [[NL-LOGIUS]] / [[NL-BZK]] | an **executive agency** under a ministry |

DINUM is the only one attached directly to the head of government, and the
only one that both sets strategy and runs the national open-data portal and
identity service through its own department.

**No relationship between the four is asserted.** They occupy the same
position in four national systems, which is an observation about states,
not a relationship between organisations.

## Relationships

**None asserted from this entity.** It is reached from [[FR-ETALAB]]
(`part-of`), [[FR-RGI]] and [[FR-DATA-GOUV]] and [[FR-FRANCECONNECT]] (all
`maintained-by`).

That direction is deliberate. `metadata/relationship-types.md` §2.1 defines
`maintained-by` as *"the target organisation maintains this entity"*, so the
edge belongs on the maintained thing pointing at the maintainer. Writing it
here — DINUM `maintained-by` → the RGI — would assert that the framework
maintains the directorate.

The first draft of this file did exactly that. It is the same inversion the
German batch made twice, and it is worth recording that the error recurred
even with the rule written down: it survives validation untouched, because
the graph stays connected while the meaning reverses.

## Sources

Listed in frontmatter.
