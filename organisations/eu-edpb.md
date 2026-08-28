---
id: EU-EDPB
type: organisation
name: European Data Protection Board
alternative_names:
  - EDPB
description: >
  Independent EU body with legal personality, established under the GDPR
  (Article 68) to ensure consistent application of the GDPR and the Law
  Enforcement Directive across member states, and to ensure cooperation
  including on enforcement. Per Article 68(3) GDPR, the Board is composed
  of the head of one supervisory authority of each member state and of the
  European Data Protection Supervisor (or their representatives), governed
  through plenaries, subgroups and taskforces, with a dedicated
  secretariat.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-GDPR
  - EU-EDPS
  - NL-AP
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Confirmed by reading edpb.europa.eu's own 'About EDPB' page directly (2026-08-28): the EDPB is 'an independent European body with legal personality' that 'ensure[s] that the General Data Protection Regulation (GDPR) and the Law Enforcement Directive are applied consistently.' Anchor edge under metadata/relationship-types.md §2.3 for an EU-scoped entity."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading gdpr-info.eu's own text of Article 68 GDPR directly (2026-08-28): Article 68(3) states 'The Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives,' and Article 68(4) covers Member States with more than one supervisory authority. This is the GDPR article that establishes the Board, confirmed directly rather than via a secondary description."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "European Data Protection Board — news"
    url: "https://www.edpb.europa.eu/news/news/2026/edpb-and-edps-support-strengthening-eus-cybersecurity-and-easing-compliance-while_en"
    publisher: "European Data Protection Board"
    accessed: "2026-08-28"
  - title: "The Role of the European Data Protection Board (EDPB)"
    url: "https://www.legiscope.com/blog/role-european-data-protection-board.html"
    publisher: "Legiscope"
    accessed: "2026-08-28"
  - title: "About EDPB"
    url: "https://www.edpb.europa.eu/about-edpb_en"
    publisher: "European Data Protection Board"
    accessed: "2026-08-28"
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
    accessed: "2026-08-28"
---

# European Data Protection Board (EDPB)

> **Re-verified 2026-08-28.** This is the first pass to verify the EDPB
> entity itself, as opposed to the `participates-in` edges that FR-CNIL,
> DE-BFDI, BE-APD, ES-AEPD and NL-AP carry pointing at it. Both originally
> cited pages were read directly, and two stronger primary sources were
> added and also read directly: edpb.europa.eu's own "About EDPB" page and
> gdpr-info.eu's text of Article 68 GDPR. `verification` promoted
> `search-only` → `primary-source`; `governed-by` [[EU-GDPR]] moves to
> `confidence: high` since it now rests on the article's own text rather
> than a secondary description.

## Description

Confirmed by reading edpb.europa.eu directly (2026-08-28): the EDPB is "an
independent European body with legal personality" that "ensure[s] that the
[[EU-GDPR|General Data Protection Regulation]] and the Law Enforcement
Directive are applied consistently" and "ensures cooperation, including on
enforcement." It is governed through plenaries, subgroups and taskforces,
supported by a dedicated secretariat.

Confirmed by reading gdpr-info.eu's text of **Article 68 GDPR** directly
(2026-08-28): under Article 68(3), the Board "shall be composed of the head
of one supervisory authority of each Member State and of the European Data
Protection Supervisor, or their respective representatives"; under
Article 68(4), a Member State with more than one supervisory authority
appoints a joint representative. The Commission may participate in Board
activities without voting rights. This is the article establishing the
Board and its composition rule, read directly rather than taken from a
secondary description.

## What this closes, and how far

[[NL-AP]], [[DE-BFDI]], [[BE-APD]], [[ES-AEPD]] and [[FR-CNIL]] each carry a
`participates-in` edge to this entity, sourced (in their own files) to
Article 68(3) GDPR's composition rule. This pass confirms that rule
directly from the Board's own side — reading Article 68 itself rather than
relying on the national files' citations of it — which is the missing half
of that verification. Nothing about those five edges is changed here; they
remain recorded on the national entities per the batch's file-ownership
rule.

`coverage: low`: the Board's guidelines catalogue, the consistency
mechanism procedure, and the details of enforcement coordination under
Articles 63–67 were not researched this pass.

## Relationships

- `part-of` [[EU]] — anchor edge; confirmed via the Board's own "About
  EDPB" description of itself as an independent EU body.
- `governed-by` [[EU-GDPR]] — confirmed via Article 68's own text, which
  establishes the Board and its composition.
- Composed of national supervisory authorities (edges recorded on the
  members, e.g. [[NL-AP]]), plus [[EU-EDPS]].

## Sources

Listed in frontmatter, all four read directly this pass (2026-08-28). The
Legiscope blog is a commercial source and weaker than the other three, but
its description of composition and mandate matches edpb.europa.eu's own
account and Article 68's text, so it is retained as a secondary
corroboration rather than replaced.
