---
id: EE-KUBERTURVALISUSE-SEADUS
type: law
name: Küberturvalisuse seadus
alternative_names:
  - Cybersecurity Act
  - Estonian Cybersecurity Act
description: >
  Estonian cybersecurity act, originally enacted in 2018 and amended to
  transpose the EU's NIS2 Directive, with the amendments entering into
  force on 1 January 2026. It expands the number of regulated essential
  and important entities from roughly 3,500 to about 6,500, requires
  regular cybersecurity risk assessment and incident reporting, and is
  overseen centrally by RIA, which acts as national competent authority,
  cybersecurity regulator and coordinator of incident response through
  the national CERT capability, CERT-EE.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-30"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations:
  - EE-RIA
related_entities:
  - EU-NIS2
  - EE-RIA
  - EE-CERT-EE
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Confirmed by reading ria.ee's own news article directly (2026-08-30): the amended Küberturvalisuse seadus took effect '2026. aasta jaanuarist' (from January 2026), described in the article as implementing the EU's NIS2 directive into Estonian law, expanding the number of regulated entities by roughly 3,000 to reach 6,500 total, and giving a three-year general transition period (five years for critical-infrastructure operators). Independently corroborated by reading nis-2-directive.com's Estonia transposition page directly, which states plainly that 'Estonia did not adopt a completely new cybersecurity statute' and instead implemented the directive 'primarily through amendments to the existing Cybersecurity Act', with those amendments entering into force on 1 January 2026, and that RIA 'performs the functions of national competent authority, cybersecurity regulator, and coordinator of incident response through the national CERT capability (CERT-EE)'. Estonia missed the Directive's own 17 October 2024 transposition deadline, triggering a European Commission infringement procedure — confirmed on the same tracker page, not independently verified against a Commission source."
    confidence: high
    valid_from: 2026-01-01
    valid_until: null

sources:
  - title: "Uuest aastast laienes küberturvalisuse seadus"
    url: "https://www.ria.ee/uudised/uuest-aastast-laienes-kuberturvalisuse-seadus"
    publisher: "Riigi Infosüsteemi Amet (RIA)"
    accessed: "2026-08-30"
  - title: "NIS 2 Directive | Transposition in Estonia"
    url: "https://www.nis-2-directive.com/Transposition/Estonia.html"
    publisher: "nis-2-directive.com"
    accessed: "2026-08-30"
---

# Küberturvalisuse seadus (Cybersecurity Act)

> **Added 2026-08-30, `verification: primary-source` from creation.** A
> research-queue item flagged as **Next** since the Estonia batch — Estonia
> had a modelled national layer and no cybersecurity entity at all, unlike
> [[NL]], [[BE]], [[DE]], [[PL]], [[CZ]] and [[PT]] — is now closed. Two
> sources were read directly: RIA's own news article on the amended Act,
> and an independent NIS2-transposition tracker that corroborates it in
> detail.

## Description

Estonia already had a Cybersecurity Act from **2018** — the exact
enactment date was not confirmed by either source read this pass, so
`start_date` records only the amendment that transposes NIS2, not the
original 2018 law. Confirmed by reading `ria.ee`'s own news article
directly, the **amended** Act took effect in **January 2026**, described
there as implementing the EU's [[EU-NIS2]] Directive into Estonian law
rather than replacing the 2018 Act outright — corroborated independently
by `nis-2-directive.com`'s Estonia transposition page, which states plainly
that "Estonia did not adopt a completely new cybersecurity statute."

## What changed

Confirmed by reading `ria.ee` directly:

- The number of regulated entities grew by roughly 3,000, reaching about
  **6,500** essential and important entities — newly covering sectors such
  as aviation, railways, utilities, hospitals and food-processing companies
  above certain size thresholds.
- Regulated entities must **regularly assess their cybersecurity risks**
  and implement protective measures, with increased leadership
  responsibility for incident-detection capability, sensitive-data
  protection and staff training.
- A **three-year transition period** applies generally; critical-
  infrastructure operators get **five years**.
- Penalties reach **€10 million or 2% of annual turnover** for critical
  entities.

## A late transposition

Confirmed by reading `nis-2-directive.com` directly: Estonia missed the
Directive's own **17 October 2024** transposition deadline, which
triggered a European Commission infringement procedure (a reasoned
opinion) — a fact from the tracker page, not independently checked against
a Commission source.

## RIA's central role

Confirmed by reading `nis-2-directive.com` directly: [[EE-RIA]] "performs
the functions of national competent authority, cybersecurity regulator,
and coordinator of incident response through the national CERT capability
(CERT-EE)" — a single agency holding roles that other countries in this
Atlas split across several bodies (compare [[BE-CCB]] and [[DE-BSI]], each
paired with its own NIS2-implementing statute). See [[EE-CERT-EE]], added
alongside this entity.

## Relationships

- `implements-requirement-from` [[EU-NIS2]].

[[EE-RIA]] and [[EE-CERT-EE]] both carry the operational side of this Act;
no relationship is asserted from either to this entity beyond the
descriptive mentions above, since neither source read states one directly
(RIA's oversight role is described in prose on RIA's own entity, not as a
graph edge, consistent with how this Atlas treats NIS2 competent-authority
designations elsewhere — see [[NL-NCSC]]'s `applies-to` [[NL-CBW]] for the
one case where a source states the designation explicitly enough to model
it as an edge).

## Sources

Listed in frontmatter, both read directly.
