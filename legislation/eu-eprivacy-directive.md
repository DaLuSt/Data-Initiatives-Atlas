---
id: EU-EPRIVACY-DIRECTIVE
type: directive
name: Directive on privacy and electronic communications
alternative_names:
  - ePrivacy Directive
  - Directive 2002/58/EC
description: >
  Directive 2002/58/EC of 12 July 2002 concerning the processing of personal data and the protection of privacy in the
  electronic communications sector, published in OJ L 201 of 31 July 2002 and in force from that day. Member States must
  ensure the confidentiality of communications and traffic data, allow information to be stored in or read from a
  user's terminal equipment only under conditions, and allow direct marketing by automated calls, fax or e-mail only
  with prior consent. It says it particularises and complements Directive 95/46/EC. The text read is the 2002 original;
  later amendments were not read.

level: regional
country: null
region: EU

status: active
rank: ordinary
confidence: medium
coverage: low
verification: primary-source

start_date: 2002-07-31
end_date: null
last_verified: "2026-11-13"
previous_version: null
successor: null

domains:
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - EU-GDPR
  - EU-DSA
  - EU-DIGITAL-OMNIBUS
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "The Directive's text as published in OJ L 201, 31.7.2002, p. 37, read directly 2026-11-13 from the Publications Office (CELEX 32002L0058, PDF): Article 21, 'This Directive is addressed to the Member States'; Article 17(1), 'Before 31 October 2003 Member States shall bring into force the provisions necessary to comply with this Directive'; Article 20, it enters into force on the day of its publication."
    confidence: high
    valid_from: 2002-07-31
    valid_until: null
  - type: related-to
    target: EU-GDPR
    source: interpretation
    evidence: "Article 1(2) says the Directive's provisions 'particularise and complement Directive 95/46/EC'. That directive is not an Atlas entity; the GDPR is the Atlas's entity for the general data protection regime that followed it. How the GDPR itself treats references to Directive 95/46/EC was not read for this entity, so the edge is the Atlas's own reading and not a statement of either text. The Digital Services Act names the two side by side (Article 2(4)(g))."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Directive 2002/58/EC (Directive on privacy and electronic communications), Official Journal text"
    url: "https://publications.europa.eu/resource/celex/32002L0058"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-13"
---

# Directive on privacy and electronic communications (Directive 2002/58/EC)

> **Created 2026-11-13** (roadmap #771, from the repository scan). The Publications Office serves this act as a PDF of the
> 2002 Official Journal pages; it was downloaded and read directly: the title, Articles 1, 5 (paragraphs 1 to 3, opening),
> 13 (opening), 17(1), 19, 20 and 21. **This is the text as adopted in 2002. Whether and how it was amended afterwards
> was not read**, so `confidence` is medium and nothing here describes the current consolidated wording.

## What the text says

- **Title and dates.** "Directive 2002/58/EC of the European Parliament and of the Council of 12 July 2002 concerning the
  processing of personal data and the protection of privacy in the electronic communications sector (Directive on
  privacy and electronic communications)", OJ L 201, 31.7.2002, p. 37. It entered into force on the day of its
  publication (Article 20); Member States had to comply before 31 October 2003 (Article 17(1)).
- **Relation to general data protection law** (Article 1(2)): its provisions "particularise and complement Directive
  95/46/EC", and also protect the legitimate interests of subscribers who are legal persons. It does not apply to
  activities outside the scope of the Treaty, such as public security, defence and State security (Article 1(3)).
- **Confidentiality** (Article 5(1)): Member States ensure the confidentiality of communications and related traffic
  data and prohibit "listening, tapping, storage or other kinds of interception or surveillance" by others without the
  users' consent, except when legally authorised.
- **Terminal equipment** (Article 5(3)): using electronic communications networks to store information, or to gain access
  to information stored, in a subscriber's or user's terminal equipment is allowed only on condition that the person is
  given clear and comprehensive information; the rest of the paragraph was not read.
- **Unsolicited communications** (Article 13(1)): automated calling machines, fax and electronic mail may be used for
  direct marketing only towards subscribers who have given their prior consent.
- **What it replaced** (Article 19): Directive 97/66/EC, repealed from the transposition date.

## Why it is in the Atlas

Two entities point at it: the [[EU-DIGITAL-OMNIBUS]] proposal would amend it, and the [[EU-DSA]] names it beside the
GDPR among the acts it leaves untouched. The proposed EU KIDS Act does the same (`discovery/candidates.md` C11).

## Not modelled

- **Directive 95/46/EC** and **Directive 97/66/EC** are not Atlas entities.
- National transpositions (for example the telecommunications acts several country entities cite) are not linked: no
  national act was read for a statement that it implements this Directive.
- The amendment the [[EU-DIGITAL-OMNIBUS]] proposes is recorded on that entity, in prose, not as an edge here.

## Sources

Listed in frontmatter, read directly.
