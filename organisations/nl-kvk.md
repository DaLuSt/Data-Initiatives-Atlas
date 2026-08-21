---
id: NL-KVK
type: organisation
name: Kamer van Koophandel
alternative_names:
  - KVK
  - Netherlands Chamber of Commerce
description: >
  Dutch chamber of commerce. Its principal statutory task within the Atlas's
  scope is operating the Handelsregister, the national business register,
  which forms one of the base registrations in the Stelsel van
  Basisregistraties.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-KADASTER
relationships:
  - type: participates-in
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "KVK operates the Handelsregister, referenced as a base registration cross-linked from the BRK, confirmed 2026-08-21 on digitaleoverheid.nl's list of the ten base registrations."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Kamer van Koophandel"
    url: "https://en.wikipedia.org/wiki/Kamer_van_Koophandel"
    publisher: "Wikipedia"
    accessed: "2026-08-21"
  - title: "10 basisregistraties — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-21"
  - title: "KVK — Netherlands Chamber of Commerce"
    url: "https://www.kvk.nl/en/"
    publisher: "Kamer van Koophandel"
    accessed: "2026-08-21"
---

# Kamer van Koophandel (KVK)

> **Verified 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.

## Description

The KVK is the Dutch chamber of commerce. Its relevance to the Atlas is its
statutory operation of the Handelsregister, the national business register,
which is one of the registrations within the [[NL-BASISREGISTRATIES]].
Businesses must register with the KVK, and the register is cross-referenced
from other base registrations — the Kadaster relates the BRK to the
Handelsregister, and [[NL-RDW]] vehicle registration interacts with KVK
registration status.

`confidence` raised from `low` to `medium` on this pass: the KVK's own site
(`kvk.nl/en`) has now been added and read, confirming the English name. It
still names itself only in passing rather than describing its statutory
basis in the detail its peers get, so `coverage: low` stands, and the
Handelsregisterwet (Batch 3, [[NL-HANDELSREGISTERWET]]) is the fuller
statutory source, not this entity.

## Relationships

- Participates in [[NL-BASISREGISTRATIES]] as operator of the
  Handelsregister.

## Sources

Listed in frontmatter.
