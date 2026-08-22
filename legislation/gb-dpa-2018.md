---
id: GB-DPA-2018
type: law
name: Data Protection Act 2018
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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading the DPA 2018's own statute text at legislation.gov.uk (2026-08-22), Part 4, § 82(2): 'In this Part, \"intelligence service\" means— (a) the Security Service; (b) the Secret Intelligence Service; (c) the Government Communications Headquarters.' This is the dedicated intelligence-services processing regime sitting alongside UK GDPR."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Data Protection Act 2018, Part 4"
    url: "https://www.legislation.gov.uk/ukpga/2018/12/part/4"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-08-22"
  - title: "The Data (Use and Access) Act 2025: A New Chapter in the UK's Data Protection Framework"
    url: "https://www.privacyworld.blog/2025/07/the-data-use-and-access-act-2025-a-new-chapter-in-the-uks-data-protection-framework/"
    publisher: "Privacy World (Squire Patton Boggs)"
    accessed: "2026-08-22"
  - title: "UK Data Protection 2025: Key Changes and Compliance Guide"
    url: "https://cms.law/en/gbr/legal-updates/uk-data-protection-what-s-changed-what-s-next"
    publisher: "CMS"
    accessed: "2026-08-22"
  - title: "Data (Use and Access) Act 2025, Part 5"
    url: "https://www.legislation.gov.uk/ukpga/2025/18/part/5"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-08-22"
---

# Data Protection Act 2018

> **Verified 2026-08-22.** The statute text at legislation.gov.uk was found
> and read directly — the entity's own flagged gap ("no legislation.gov.uk
> citation for the Act itself") is now closed.

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

**The legislation.gov.uk gap is now closed.** Its Part 4, read directly
2026-08-22, defines the dedicated intelligence-services processing regime:
"In this Part, 'intelligence service' means— (a) the Security Service;
(b) the Secret Intelligence Service; (c) the Government Communications
Headquarters" (§ 82(2)). This is the same Part 4 regime asserted from the
services' own entities ([[GB-MI5]], [[GB-SIS]], [[GB-GCHQ]]). The Act's
broader structure beyond Part 4 — the general and law-enforcement
processing regimes, most of what makes the Act long — was still not read
this pass, so `coverage: low` stands.

## Relationships

- `applies-in` [[GB]].

[[GB-DUAA]] carries the `related-to` edge pointing here, and [[GB-ICO]] an
`applies-to` edge — the ICO regulates this Act as well as [[GB-UK-GDPR]].

## Sources

Listed in frontmatter.
