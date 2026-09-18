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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - FR-DINUM
related_entities:
  - EU-EIF
  - NL-PAS-TOE-OF-LEG-UIT
  - FR-ORDONNANCE-2005-1516
relationships:
  - type: maintained-by
    target: FR-DINUM
    source: fact
    evidence: "Confirmed verbatim by reading numerique.gouv.fr's own RGI page directly (2026-08-26): 'Le RGI est défini dans l'ordonnance n° 2005-1516 du 8 décembre 2005 relative aux échanges électroniques entre les usagers et les autorités administratives et entre les autorités administratives. Dans l'article 11 de cette ordonnance, le RGI fixe les règles techniques permettant d'assurer l'interopérabilité des systèmes d'information' (the RGI is defined in ordonnance n° 2005-1516 of 8 December 2005 ... under Article 11 of that ordinance, the RGI sets the technical rules ensuring interoperability of information systems) — DINUM's own page, not a hosted PDF or Wikipedia, now carries the legal-foundation claim."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: FR-ORDONNANCE-2005-1516
    source: fact
    evidence: "A research-queue pickup (2026-09-04) created the entity for the ordinance this file already quoted verbatim at Article 11, closing the 'legal basis of FR-RGI; not modelled' gap discovery/research-queue.md had recorded."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: EU-EIF
    source: fact
    evidence: "CLOSES A LONG-STANDING REFUSAL (discovery/unresolved.md row #71). The European Commission's own National Interoperability Framework Observatory (NIFO) 'Factsheet — France' (2016 update), read directly, states in its own words: 'The Référentiel Général d'Interopérabilité (RGI) v2.0 ..., which is the French NIF, has been approved on 20 April 2016.' Its 'Alignment NIF/EIF' section states 'The main concepts of the EIF are covered by the French NIF' and 'All the EIF principles are fully covered by the different frameworks of the French NIF,' illustrated with a radar chart comparing EIF and France (MS) across Principles, Conceptual Model, Interoperability Levels, Interoperability Agreements and Interoperability Governance. Unlike the earlier refusal, which found no source connecting RGI to the EIF at all, this is the Commission's own NIFO assessment naming the RGI specifically as France's NIF and stating EIF alignment directly — the same kind of source [[BE-BELGIF]] already carries. `confidence: medium`, not `high`: the factsheet is dated 2016 and describes RGI v2.0's approval as 20 April 2016, one detail apparently in tension with the 2 December 2015 publication date on the document's own cover (already cited in this entity's frontmatter) — not independently reconciled this pass."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Référentiel général d'interopérabilité (RGI)"
    url: "https://www.numerique.gouv.fr/offre-accompagnement/reference-interoperabilite-rgi/"
    publisher: "DINUM — numerique.gouv.fr"
    accessed: "2026-08-26"
  - title: "Référentiel général d'interopérabilité (RGI)"
    url: "https://numerique360.banquedesterritoires.fr/glossaire/referentiel-general-dinteroperabilite-rgi/"
    publisher: "Banque des Territoires — Numérique 360"
    accessed: "2026-08-26"
  - title: "Référentiel général d'interopérabilité"
    url: "https://fr.wikipedia.org/wiki/R%C3%A9f%C3%A9rentiel_g%C3%A9n%C3%A9ral_d'interop%C3%A9rabilit%C3%A9"
    publisher: "Wikipédia"
    accessed: "2026-08-26"
  - title: "Une nouvelle version du Référentiel général d'interopérabilité"
    url: "https://siaf.hypotheses.org/644"
    publisher: "Service interministériel des Archives de France (SIAF)"
    accessed: "2026-08-26"
  - title: "Référentiel Général d'Interopérabilité — version 1.9.9"
    url: "https://www.april.org/sites/default/files/Referentiel_General_Interoperabilite_V1.9.9.pdf"
    publisher: "April (hosting the DINUM document)"
  - title: "Référentiel Général d'Interopérabilité — version 2.0"
    url: "https://www.numerique.gouv.fr/documents/7/Referentiel_General_Interoperabilite_V2.pdf"
    publisher: "DINUM (as DINSIC) — numerique.gouv.fr"
    accessed: "2026-09-06"
  - title: "NIFO Factsheet — France (2016 update)"
    url: "https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/NIFO%20-%20Factsheet%20France_2016_v1_0.pdf"
    publisher: "European Commission — National Interoperability Framework Observatory (NIFO)"
    accessed: "2026-09-18"
---

# RGI — Référentiel général d'interopérabilité

> **Verified 2026-08-26, and a frontmatter bug fixed.** DINUM's own RGI
> page was read directly and confirms the ordonnance n° 2005-1516
> legal foundation verbatim, at Article 11. The frontmatter also
> carried a `based-on` [[EU-EIF]] relationship that directly
> contradicted this entity's own body text, which has refused that
> link since creation ("It is refused"). The relationship has been
> removed; `related_entities` still records the association for
> navigation.
>
> **Closed 2026-09-06**: the specification itself, previously cited only
> from an april.org-hosted copy, is now also read directly from its
> official home — `numerique.gouv.fr`'s own PDF, linked from DINUM's own
> RGI page. The document's own cover and footer read "Référentiel
> Général d'Interopérabilité — Version 2.0 – décembre 2015" and
> "RGI v2.0 du 02/12/2015," published under DINSIC (DINUM's predecessor
> name).
>
> **Closed 2026-09-18**: the EIF question this entity has refused since
> creation is resolved — not by inference, but by the European
> Commission's own NIFO factsheet naming the RGI as France's NIF and
> stating EIF alignment directly. See "The EIF link, finally sourced"
> below.

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

## The EIF link, finally sourced — 2026-09-18

For three passes this entity refused `based-on` → [[EU-EIF]], the
tempting link matching [[BE-BELGIF]], because nothing read about the RGI
itself mentioned the EIF, the NIF concept, or European interoperability
at all — refusing the claim precisely because the pattern elsewhere in
the Atlas made it look safe.

That changes with a source of a different kind: not the RGI's own text,
but the European Commission's own **National Interoperability Framework
Observatory (NIFO)**, which tracks and assesses member states'
frameworks against the EIF from the European side. Its "Factsheet —
France" (2016 update), read directly, states in its own words: *"The
Référentiel Général d'Interopérabilité (RGI) v2.0 ..., which is the
French NIF, has been approved on 20 April 2016."* Its "Alignment NIF/EIF"
section states plainly: *"The main concepts of the EIF are covered by
the French NIF"* and *"All the EIF principles are fully covered by the
different frameworks of the French NIF,"* illustrated with a radar chart
scoring France against the EIF across five dimensions (Principles,
Conceptual Model, Interoperability Levels, Interoperability Agreements,
Interoperability Governance).

`confidence: medium`, not `high`, for one loose end: the factsheet gives
20 April 2016 as the RGI v2.0's approval date, which does not obviously
match the 2 December 2015 publication date on the specification
document's own cover (already cited above) — not independently
reconciled this pass. The two dates plausibly describe different steps
(publication vs. formal government approval), but no source read states
that directly.

The scoreboard on [[EU-EIF]] is now:

| Country | National framework linked? |
|---|---|
| Belgium | **yes** — [[BE-BELGIF]], sourced from the framework's own text |
| France | **yes** — this entity, sourced from the Commission's own NIFO factsheet |
| Germany | no — [[DE-IT-ARCHITEKTURRICHTLINIEN]] not asserted to be the NIF |
| Netherlands | no — [[NL-NORA]] question open since Batch 7 |

Two of four now, and the closing move — going to the Commission's own
NIFO assessment rather than the national document alone — is available
for the remaining two refusals as well, not attempted this pass.

## Relationships

- Maintained by [[FR-DINUM]].
- `governed-by` [[FR-ORDONNANCE-2005-1516]] — closed 2026-09-04.
- `based-on` [[EU-EIF]] — closed 2026-09-18, `confidence: medium`. See
  above.

## Sources

Listed in frontmatter. Four read directly in the 2026-08-26 pass; the
RGI specification itself, previously cited only from **april.org** (an
advocacy association's hosted copy), was read directly in the 2026-09-06
pass from its official home on `numerique.gouv.fr`, closing the
second-hand-citation gap the entity had flagged since creation (the
april.org copy, v1.9.9, is kept as a record of the version this entity's
earlier text described). The European Commission's own NIFO factsheet
for France, added and read directly 2026-09-18, closes the EIF-alignment
question.
