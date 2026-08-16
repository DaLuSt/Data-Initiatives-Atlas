---
id: FR-NIS2-LOI
type: law
name: Loi relative à la résilience des infrastructures critiques et au renforcement de la cybersécurité
alternative_names:
  - Loi Résilience
  - French NIS2 transposition law
description: >
  French legislative vehicle transposing the NIS2 Directive, together with
  the Critical Entities Resilience Directive and DORA, into French law. It
  designates ANSSI as the competent national authority for cybersecurity
  and brings roughly 15,000 entities into scope, against about 500 under
  the NIS1 regime. Its status could not be established — see the entity
  body.

level: national
country: FR
region: EU

status: unknown
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - FR-ANSSI
related_entities:
  - EU-NIS2
  - EU-CER
  - BE-NIS2-WET
  - DE-NIS2UMSUCG
  - NL-CBW
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "France is transposing the NIS2 Directive through the 'loi Résilience' relating to the resilience of critical infrastructures and the strengthening of cybersecurity; the draft law transposes three European directives — REC, NIS2 and DORA — and designates ANSSI as the competent national authority (aventris.fr; nis-2-directive.com France; eversheds-sutherland; legiscope.com). NOT READ — search-only. The instrument's status is contested across sources; see the entity body."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Transposition NIS2 en France : loi Résilience, ANSSI et calendrier"
    url: "https://aventris.fr/transposition-anssi"
    publisher: "Aventris"
  - title: "NIS 2 Directive | Transposition in France"
    url: "https://www.nis-2-directive.com/Transposition/France.html"
    publisher: "nis-2-directive.com"
  - title: "France — EU NIS2 Directive"
    url: "https://ezine.eversheds-sutherland.com/eu-nis2-directive/france"
    publisher: "Eversheds Sutherland"
  - title: "Avancement de la transposition de la directive NIS 2"
    url: "https://aide.monespacenis2.cyber.gouv.fr/fr/article/avancement-de-la-transposition-de-la-directive-nis-2-1b3j1da/"
    publisher: "MonEspaceNIS2 (ANSSI)"
  - title: "Transposition de la directive NIS2 en droit français : état des lieux et évolutions"
    url: "https://blog.prodwaregroup.com/fr/cybersecurite/transposition-de-la-directive-nis2-en-droit-francais-etat-des-lieux-et-evolutions/"
    publisher: "Prodware"
---

# Loi Résilience — France's NIS2 transposition

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

France transposes [[EU-NIS2]] through the *loi Résilience*, on the
resilience of critical infrastructures and the strengthening of
cybersecurity. Unusually, one vehicle carries **three EU instruments**:
NIS2, the Critical Entities Resilience directive ([[EU-CER]]) and DORA.

What the sources agree on:

- it designates [[FR-ANSSI]] as the **competent national authority**;
- scope grows from roughly **500 entities under NIS1 to about 15,000**;
- obligations cover cyber risk management, registration and incident
  notification, with sanctions up to **€10 million or 2% of global
  turnover**;
- France **missed the directive's 17 October 2024 transposition deadline**.

## ⚠ `status: unknown` — the sources contradict each other

This is the only entity in the Atlas whose sources directly conflict about
whether the instrument exists in force. Two incompatible accounts were
returned by the same search:

| Account | Source |
|---|---|
| Transposition is by **Law n° 2025-90 of 26 February 2025** | one commentary |
| The bill was **adopted by the Senate on 12 March 2025 and is awaiting promulgation, expected mid-2026** | another commentary |

A law cannot both have been promulgated in February 2025 and be awaiting
promulgation after March 2025. At least one of these is wrong, and **no
source read resolves it** — notably, neither Légifrance nor an ANSSI page
stating the enacted reference was returned.

So:

- `status: unknown` — not `active`, not `planned`.
- `start_date: null` — recording either date would be picking a side.
- **No law number in `alternative_names`**, because the one candidate
  number may belong to a different act.
- `confidence: low` on the entity and on its only relationship.

The alternative was to pick the more official-sounding account and move on.
That would have produced a confident, specific, possibly false record — the
exact failure mode §21 of the original brief names. An honest `unknown` is
worth more than a wrong date.

## Four transpositions of one directive

| Country | Act | In force | Technique |
|---|---|---|---|
| Belgium | [[BE-NIS2-WET]] | **18 Oct 2024** | new act replacing the NIS1 act |
| Germany | [[DE-NIS2UMSUCG]] | 6 Dec 2025 | revises the existing [[DE-BSIG]] |
| Netherlands | [[NL-CBW]] | 15 Aug 2026 | new act superseding [[NL-WBNI]] |
| **France** | **this entity** | **unknown** | one vehicle for NIS2 + CER + DORA |

Belgium met the deadline within a year; France missed it and, on the
evidence available here, may still not have completed it nearly two years
later. The Atlas can now show that spread across four member states — which
is the sort of comparative fact a country-neutral model exists to make
visible, and which no single-country layer could produce.

France is also the only one of the four to bundle three directives into one
act. **No `implements-requirement-from` → [[EU-CER]] is asserted**, even
though the sources say the vehicle transposes it: the relationship would
inherit this entity's unresolved status, and one unreliable relationship is
enough.

**No relationship between the four national acts is asserted.**

## Sources

Listed in frontmatter — **all five are commercial commentary or vendor
blogs** except the ANSSI help-centre page, which is about the transposition's
progress rather than its outcome. For an entity this contested that is a
poor position, and it is the direct cause of the unresolved status. This is
the first French entity that should be re-sourced.
