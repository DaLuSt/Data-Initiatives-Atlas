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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
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
    accessed: "2026-08-26"
  - title: "Direction Interministérielle du Numérique (DINUM)"
    url: "https://www.transformation.gouv.fr/le-ministere/directions/dinum"
    publisher: "Ministère de la Transformation et de la Fonction publiques"
    accessed: "2026-08-26"
  - title: "Organisation — Direction interministérielle du numérique"
    url: "https://www.data.gouv.fr/organizations/direction-interministerielle-du-numerique"
    publisher: "data.gouv.fr"
    accessed: "2026-08-26"
  - title: "Interministerial Digital Directorate (DINUM)"
    url: "https://en.wikipedia.org/wiki/Interministerial_Digital_Directorate"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
  - title: "Direction interministérielle du numérique"
    url: "https://www.economie.gouv.fr/direction-interministerielle-du-numerique"
    publisher: "Ministère de l'Économie et des Finances"
---

# DINUM — Direction interministérielle du numérique

> **Verified 2026-08-26.** Four of five cited pages were read directly.
> numerique.gouv.fr's and transformation.gouv.fr's own pages confirm
> DINUM's mission and shared-services list verbatim, though they name
> the co-authority minister with two slightly different titles — see
> below. `economie.gouv.fr` is genuinely bot-walled (403) even with an
> honest User-Agent.

## Description

Confirmed verbatim by reading numerique.gouv.fr directly (2026-08-26):
"La direction interministérielle du numérique (DINUM) a pour mission
d'élaborer la stratégie numérique de l'État et de piloter sa mise en
œuvre" (DINUM's mission is to develop the State's digital strategy and
steer its implementation) — a **service of the Prime Minister**, placed
under the joint authority of the Prime Minister and a co-authority
minister.

It:

- accompanies ministries in their digital transformation;
- advises the government;
- develops shared services and resources, confirmed verbatim by reading
  transformation.gouv.fr directly: "le réseau interministériel de
  l'État, FranceConnect, data.gouv.fr ou api.gouv.fr" — the
  interministerial state network, [[FR-FRANCECONNECT]],
  [[FR-DATA-GOUV]] and api.gouv.fr;
- publishes and maintains [[FR-RGI]], confirmed directly on that entity.

It comprises six departments and four missions, one of which is
[[FR-ETALAB]].

## ⚠ Two government pages, two names for the co-authority minister

numerique.gouv.fr's own page (checked 2026-08-26) places DINUM under
"l'autorité conjointe du Premier ministre et du ministre de l'Action et
des Comptes publics." transformation.gouv.fr's own page, read the same
day, places it under "l'autorité conjointe du Premier ministre et du
ministre de l'Action publique, de la Fonction publique et de la
Simplification." Both are current government pages naming a real
ministry; the discrepancy most likely reflects a portfolio renamed
between the two pages' last updates, not an error on either side. The
Atlas does not model French ministries as entities, so no relationship
is affected — recorded here because a reader comparing the two
citations would otherwise wonder which is wrong.

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

Listed in frontmatter, four of five read directly this pass;
`economie.gouv.fr` is genuinely bot-walled (403) even with an honest
User-Agent.
