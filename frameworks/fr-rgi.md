---
id: FR-RGI
type: framework
name: Référentiel général d'interopérabilité
alternative_names:
  - RGI
  - General Interoperability Framework
description: >
  French general interoperability framework, published and maintained by
  the Direction interministérielle du numérique. It sets the standards,
  norms and good practices that allow public administration information
  systems to communicate securely, and is structured around
  interoperability profiles grouping standards and recommendations by use
  case. Its legal foundation is ordonnance n° 2005-1516 of 8 December 2005,
  which requires administrative authorities including local authorities to
  comply with technical interoperability rules.

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
organisations:
  - FR-DINUM
related_entities:
  - EU-EIF
  - NL-PAS-TOE-OF-LEG-UIT
relationships:
  - type: maintained-by
    target: FR-DINUM
    source: fact
    evidence: "The RGI is published by the Direction interministérielle du numérique; the evolution of the framework is entrusted to DINUM, which is placed under the authority of the Prime Minister and ensures its strategic steering and coordinates its regular updates (numerique.gouv.fr/offre-accompagnement/reference-interoperabilite-rgi; numerique360.banquedesterritoires.fr). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Référentiel général d'interopérabilité (RGI)"
    url: "https://www.numerique.gouv.fr/offre-accompagnement/reference-interoperabilite-rgi/"
    publisher: "DINUM — numerique.gouv.fr"
  - title: "Référentiel général d'interopérabilité (RGI)"
    url: "https://numerique360.banquedesterritoires.fr/glossaire/referentiel-general-dinteroperabilite-rgi/"
    publisher: "Banque des Territoires — Numérique 360"
  - title: "Référentiel Général d'Interopérabilité — version 1.9.9"
    url: "https://www.april.org/sites/default/files/Referentiel_General_Interoperabilite_V1.9.9.pdf"
    publisher: "April (hosting the DINUM document)"
  - title: "Référentiel général d'interopérabilité"
    url: "https://fr.wikipedia.org/wiki/R%C3%A9f%C3%A9rentiel_g%C3%A9n%C3%A9ral_d'interop%C3%A9rabilit%C3%A9"
    publisher: "Wikipédia"
  - title: "Une nouvelle version du Référentiel général d'interopérabilité"
    url: "https://siaf.hypotheses.org/644"
    publisher: "Service interministériel des Archives de France (SIAF)"
---

# RGI — Référentiel général d'interopérabilité

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The RGI defines the standards, norms and good practices that let French
public administration information systems communicate effectively and
securely, aiming at the compatibility, reusability and security of data
exchanged between state entities.

It is organised around **interoperability profiles** — sets of standards
and recommendations grouped around defined use cases, to make adoption
easier by focusing on a few key uses.

Its legal foundation is **ordonnance n° 2005-1516 of 8 December 2005**,
which requires administrative authorities, **including local authorities**,
to comply with technical interoperability rules. The sources are explicit
that this makes it a **legal obligation, not a recommendation**.

[[FR-DINUM]] publishes it and steers its evolution.

## Binding by law, where the Dutch equivalent is comply-or-explain

The closest Atlas counterpart is [[NL-PAS-TOE-OF-LEG-UIT]] — the Dutch
policy applying a published list of open standards to
(semi-)government organisations. The mechanisms differ in kind:

| | France | Netherlands |
|---|---|---|
| Instrument | **RGI**, under an ordonnance | a **policy** applied to a list |
| Force | legal obligation | **comply or explain** |
| Reaches local government | **yes, explicitly** | yes |

This is the sharpest illustration of the point made on [[FR]]: France is
*more* centralised than the Netherlands, not merely centralised in the same
way. **No relationship between the two is asserted.**

## ⚠ Not asserted to be France's national interoperability framework

The tempting link is `based-on` → [[EU-EIF]], matching [[BE-BELGIF]].

**It is refused.** [[BE-BELGIF]] is sourced *as* Belgium's National
Interoperability Framework and *as* taking the EIF's 12 principles as its
basis. Nothing read about the RGI says either thing — the sources describe
it as a French framework under French law and do not mention the EIF, the
NIF concept, or European interoperability at all.

The RGI is very probably France's NIF. That is exactly why the link is
refused: it is the kind of claim that looks safe because the pattern
elsewhere in the Atlas makes it look expected.

The scoreboard on [[EU-EIF]] is now:

| Country | National framework linked? |
|---|---|
| Belgium | **yes** — [[BE-BELGIF]], sourced |
| Germany | no — [[DE-IT-ARCHITEKTURRICHTLINIEN]] not asserted to be the NIF |
| Netherlands | no — [[NL-NORA]] question open since Batch 7 |
| France | no — this entity |

One of four, and the three refusals are all the same refusal. Logged in
`discovery/unresolved.md`.

## Relationships

- Maintained by [[FR-DINUM]].

## Sources

Listed in frontmatter. Note the third: the RGI document itself is cited
from **april.org**, an advocacy association hosting a copy, because no
numerique.gouv.fr URL for the PDF was returned by search. The specification
text is therefore cited at second hand.
