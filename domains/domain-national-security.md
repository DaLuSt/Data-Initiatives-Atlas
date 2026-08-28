---
id: DOMAIN-NATIONAL-SECURITY
type: domain
name: National security and intelligence
alternative_names:
  - Intelligence and security
  - National security
  - Statutory intelligence oversight
description: >
  Subject-matter domain covering the statutory intelligence and security
  services of the Atlas's countries, the acts of parliament that constitute
  them and define their powers, and the bodies those acts create to
  authorise and review the use of those powers. It is the one domain whose
  entities sit largely outside EU data law, because Article 4(2) TEU
  reserves national security to the member states.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources:
  - title: "Consolidated version of the Treaty on European Union — Article 4"
    url: "https://www.legislation.gov.uk/eut/teu/article/4/data.htm?view=plain"
    publisher: "UK National Archives (legislation.gov.uk), consolidated EU treaty text"
    accessed: "2026-08-28"
  - title: "General Data Protection Regulation — Article 2(2)(a)"
    url: "https://gdpr-info.eu/art-2-gdpr/"
    publisher: "gdpr-info.eu (GDPR text mirror)"
    accessed: "2026-08-28"
  - title: "General Data Protection Regulation — Recital 16"
    url: "https://gdpr-info.eu/recitals/no-16/"
    publisher: "gdpr-info.eu (GDPR text mirror)"
    accessed: "2026-08-28"
---

# National security and intelligence

> **Verified 2026-08-28.** This is a classification node and carries no
> factual claims of its own about any single entity, but its central legal
> argument — that Article 4(2) TEU and GDPR Article 2(2)(a)/Recital 16 carve
> national security out of EU data law — rests on two provisions that can be
> read directly rather than left as an assertion. Both were read this pass:
> the consolidated TEU text (via legislation.gov.uk, an official mirror of
> the treaty text) and the GDPR's own Article 2(2)(a) and Recital 16 (via
> gdpr-info.eu, the standard GDPR text mirror). `verification` moves from
> `search-only` to `primary-source` on that basis, following the precedent
> of [[DOMAIN-GOVERNMENT]] and its siblings, which hold `primary-source`
> with no sources at all because they carry no claims requiring one — this
> domain now holds it because its one claim was actually checked.

## Description

Classification node for the statutory intelligence and security services of
the seven countries in the Atlas, the legislation constituting them, and the
authorisation and review bodies that legislation creates.

The domain exists because the entities in it satisfy the two-entity
threshold many times over — it is created holding **46 entities across
seven countries** — but also because it marks a *legal* boundary, not only a
topical one.

## Why this domain is not like the others

Every other domain in the Atlas groups entities that sit **inside** EU data
law. [[DOMAIN-HEALTH]] entities are shaped by [[EU-GDPR]];
[[DOMAIN-CYBERSECURITY]] entities are shaped by [[EU-NIS2]] and
[[EU-CYBERSECURITY-ACT]]; [[DOMAIN-GEOSPATIAL]] entities by
[[EU-INSPIRE]].

This domain groups entities that are **carved out of it**.

- **Article 4(2) TEU** provides, in its own words (confirmed by reading the
  consolidated treaty text directly, 2026-08-28): "It shall respect their
  essential State functions, including ensuring the territorial integrity
  of the State, maintaining law and order and safeguarding national
  security. In particular, national security remains the sole
  responsibility of each Member State."
- **[[EU-GDPR]] Article 2(2)(a)** excludes from the Regulation's material
  scope "processing of personal data in the course of an activity which
  falls outside the scope of Union law" (confirmed by reading the article
  text directly, 2026-08-28), and **Recital 16** names national security
  among such activities: "This Regulation does not apply to issues of
  protection of fundamental rights and freedoms or the free flow of
  personal data related to activities which fall outside the scope of
  Union law, such as activities concerning national security" (also
  confirmed by reading the recital text directly, 2026-08-28).

The practical consequence for this repository is specific and worth stating
plainly: **no EU instrument in the Atlas carries `applies-in` to the
services in this domain, and none should be added.** [[NL-AIVD]] is not
supervised by [[NL-AP]]; [[DE-BND]] is not supervised by [[DE-BFDI]] in the
way [[DE-BDSG]] arranges for ordinary federal bodies. Each country builds
its own review machinery instead — [[NL-CTIVD]], [[DE-UKR]], [[BE-COMITE-I]],
[[FR-CNCTR]], [[GB-IPCO]] — and those bodies answer to national statute, not
to [[EU-EDPB]].

An empty EU column against these entities is therefore a **finding**, not a
gap in the research.

## What the domain does *not* claim

Membership of this domain is not a claim that an entity is exempt from all
law, nor that the carve-out is total. The boundary is contested and
litigated — the Court of Justice has repeatedly held that a member state
invoking national security does not thereby escape review of whether the
invocation was proper. The Atlas records the statutory position as its
sources state it, and does not adjudicate the boundary.

## Sources

Listed in frontmatter — the two treaty/regulation provisions this domain's
argument rests on, both read directly on 2026-08-28. The service entities
and [[EU-GDPR]] itself carry their own sourcing for their own claims; this
domain's classification-node status is otherwise unchanged.
