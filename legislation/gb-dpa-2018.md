---
id: GB-DPA-2018
type: law
name: Data Protection Act 2018
alternative_names:
  - DPA 2018
description: >
  United Kingdom act which sits alongside UK GDPR and completes the domestic
  data protection framework, covering the areas the Regulation leaves to
  national law and the regimes outside its scope. It was substantially
  amended by the Data (Use and Access) Act 2025, whose main data protection
  provisions came into force on 5 February 2026.

level: national
country: GB
region: null

status: active
confidence: medium
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
  - GB-ICO
related_entities:
  - GB
  - GB-UK-GDPR
  - GB-DUAA
relationships:
  - type: applies-in
    target: GB
    source: fact
    evidence: "The Data Protection Act 2018 sits alongside UK GDPR and completes the United Kingdom's domestic data protection framework (privacyworld.blog 'The Data (Use and Access) Act 2025'; cms.law 'UK Data Protection 2025'; legislation.gov.uk Data (Use and Access) Act 2025 Part 5). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The Data (Use and Access) Act 2025: A New Chapter in the UK's Data Protection Framework"
    url: "https://www.privacyworld.blog/2025/07/the-data-use-and-access-act-2025-a-new-chapter-in-the-uks-data-protection-framework/"
    publisher: "Privacy World (Squire Patton Boggs)"
  - title: "UK Data Protection 2025: Key Changes and Compliance Guide"
    url: "https://cms.law/en/gbr/legal-updates/uk-data-protection-what-s-changed-what-s-next"
    publisher: "CMS"
  - title: "Data (Use and Access) Act 2025, Part 5"
    url: "https://www.legislation.gov.uk/ukpga/2025/18/part/5"
    publisher: "legislation.gov.uk (The National Archives)"
---

# Data Protection Act 2018

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Data Protection Act 2018 sits **alongside** [[GB-UK-GDPR]] rather than
implementing it. Together the two form the UK's data protection framework,
and [[GB-DUAA]] amends both.

## The one part of the UK regime that does look like the other six

[[GB-UK-GDPR]] has no counterpart in the six member states, because
domesticating a regulation is not a technique any of them used. **This act
does have one.** In 2018 the United Kingdom was still a member state, and
the DPA 2018 played the role [[NL-UAVG]], [[DE-BDSG]], [[BE-GDPR-WET]],
[[ES-LOPDGDD]] and [[PL-ODO]] played in their countries: the national act
that fills in what the GDPR leaves to member states and covers the regimes
outside it.

**No `implements-requirement-from` [[EU-GDPR]] edge is asserted**, and that
is a deliberate refusal rather than an oversight. The relationship would
have been defensible in 2018 and is not clearly defensible now: the sources
found describe the Act's present relationship to UK GDPR, not its original
relationship to the EU Regulation. Asserting a historic edge on
present-tense sources would be inventing a date the Atlas does not have.

That is the difference between this entity and [[GB-NIS-REGULATIONS]], which
**does** carry `implements-requirement-from` — there, a source states
directly that the Regulations gave effect to the Directive.

## `coverage: low`, and the reason is specific

Every source found for this act describes it **through the changes the DUAA
makes to it**. Its own structure — the law enforcement and intelligence
services regimes, the exemptions, the schedules that make it long — is not
established at all. This is the same failure mode as [[PL-ODO]], which every
source described through the authority it creates.

⚠ **No legislation.gov.uk citation for the Act itself.** The only official
source here is for the 2025 Act that amends it. That makes the DPA 2018 one
of the two weakest-sourced entities in the UK batch, alongside [[GB-DCMS]],
and the first thing a re-verification pass should fetch.

## Relationships

- `applies-in` [[GB]].

[[GB-DUAA]] carries the `related-to` edge pointing here, and [[GB-ICO]] an
`applies-to` edge — the ICO regulates this Act as well as [[GB-UK-GDPR]].

## Sources

Listed in frontmatter.
