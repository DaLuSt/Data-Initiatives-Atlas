---
id: NL-ENSIA
type: framework
name: Eenduidige Normatiek Single Information Audit
alternative_names:
  - ENSIA
description: >
  Dutch accountability system for information security at
  municipalities, based on the Baseline Informatiebeveiliging Overheid
  (BIO). It implements a "single information, single audit" principle:
  a municipality completes one annual self-evaluation questionnaire,
  used both for horizontal accountability to its own municipal council
  and for vertical accountability to central-government departments,
  submitted by 30 April of the following year. It emerged from a joint
  initiative of the Ministry of the Interior and Kingdom Relations, the
  Ministry of Infrastructure and the Environment, the Ministry of
  Social Affairs and Employment, and the Vereniging van Nederlandse
  Gemeenten (VNG), and was implemented on 1 July 2017. Seven
  information systems currently use ENSIA's accountability
  methodology, including BRP, DigiD and BAG.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2017-07-01
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - NL-BIO
  - NL-VNG
  - NL-BZK
relationships:
  - type: based-on
    target: NL-BIO
    source: fact
    evidence: "Confirmed by reading digitaleoverheid.nl's own ENSIA page directly (2026-09-04): ENSIA's objective is 'an effective and efficient accountability system for information security, based on the Baseline Informatiebeveiliging Overheid (BIO)', implemented 1 July 2017 from a joint initiative of the Ministry of the Interior and Kingdom Relations, the Ministry of Infrastructure and the Environment, the Ministry of Social Affairs and Employment, and VNG. Seven information systems, including BRP, DigiD and BAG, use ENSIA's methodology, and it also supports oversight under the Cyberbeveiligingswet."
    confidence: high
    valid_from: 2017-07-01
    valid_until: null

sources:
  - title: "ENSIA"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/ensia/"
    publisher: "Digitale Overheid"
    accessed: "2026-09-04"
---

# ENSIA — Eenduidige Normatiek Single Information Audit

> **Added 2026-09-04, `verification: primary-source` from creation.**
> [[NL-BIO]]'s own file had already flagged ENSIA as "the accountability
> system paired with the BIO... not yet an entity; queued." Its own
> `digitaleoverheid.nl` page was read directly this pass.

## Description

ENSIA is the Dutch accountability system for information security at
municipalities, based on [[NL-BIO]]. Reading `digitaleoverheid.nl`'s own
page directly: it implements a **"single information, single audit"**
principle — a municipality completes one annual self-evaluation
questionnaire, serving both **horizontal accountability** to its own
municipal council and **vertical accountability** to central-government
departments, submitted by **30 April** of the following year.

## Origin and scope

ENSIA emerged from a joint initiative of the **Ministry of the Interior
and Kingdom Relations**, the **Ministry of Infrastructure and the
Environment**, the **Ministry of Social Affairs and Employment**, and
[[NL-VNG]], and was implemented on **1 July 2017**. It currently covers
**seven** information systems, including BRP, DigiD and BAG, and also
supports oversight obligations under the Cyberbeveiligingswet.

## Relationships

- `based-on` [[NL-BIO]].

## Sources

Listed in frontmatter, read directly this pass.
