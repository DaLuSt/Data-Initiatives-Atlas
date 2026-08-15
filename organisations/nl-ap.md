---
id: NL-AP
type: organisation
name: Autoriteit Persoonsgegevens
alternative_names:
  - AP
  - Dutch Data Protection Authority
description: >
  The Netherlands' independent data protection supervisory authority. It
  monitors and promotes the protection of personal data, and is the national
  supervisory authority designated under the EU General Data Protection
  Regulation, with enforcement powers including the imposition of fines.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-GDPR
  - NL-UAVG
  - EU-EDPB
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "The EDPB comprises representatives from each national supervisory authority; the AP is the Netherlands' designated supervisory authority under the GDPR. Membership follows from the sourced composition rule rather than from a source naming the AP. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-UAVG
    source: fact
    evidence: "The AP is the Dutch supervisory authority designated by law; the UAVG is the Dutch implementing act for the GDPR under which it operates (autoriteitpersoonsgegevens.nl UAVG document page). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Under the GDPR every member state must designate an independent supervisory authority; the AP is that authority for the Netherlands, and its tasks derive from the regulation (rijksoverheid.nl; noraonline.nl). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "Autoriteit Persoonsgegevens (AP) — Contactgids"
    url: "https://www.rijksoverheid.nl/service/contact/contactgids/a/autoriteit-persoonsgegevens"
    publisher: "Rijksoverheid"
  - title: "AP (Autoriteit Persoonsgegevens)"
    url: "https://www.noraonline.nl/wiki/AP_(Autoriteit_Persoonsgegevens)"
    publisher: "NORA Online (ICTU)"
  - title: "Privacyregels beschermen persoonsgegevens"
    url: "https://www.rijksoverheid.nl/onderwerpen/privacy-en-persoonsgegevens/privacyregels-beschermen-persoonsgegevens"
    publisher: "Rijksoverheid"
---

# Autoriteit Persoonsgegevens (AP)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The AP is the Netherlands' independent supervisory authority for the
protection of personal data. It is a zelfstandig bestuursorgaan designated
by law as the supervisory authority for the processing of personal data.

Its tasks derive from the EU General Data Protection Regulation, under which
every member state must designate an independent supervisory authority. The
AP assesses whether individuals and organisations — government included —
comply with the regulation, and may intervene where they do not, including
by imposing fines. Its independence is structural: in performing its tasks
and exercising its powers it may neither seek nor accept instructions from
others, and must have sufficient resources to do its work.

## Relationships

- Governed by [[NL-UAVG]], the Dutch implementing act.
- Designated under [[EU-GDPR]], which requires every member state to
  appoint an independent supervisory authority.

Both relationships were added in Batch 3, closing the gap this entity
carried when created in Batch 2. Together with
[[NL-UAVG]] → [[EU-GDPR]] they form the Atlas's first complete vertical
chain: EU regulation → national implementing act → national authority.

Batch 9 added [[EU-EDPB]] and the `participates-in` relationship, closing
that gap. Note the evidence is a composition rule ("representatives from
each national supervisory authority") rather than a source naming the AP —
a reasonable inference from a sourced rule, and marked as such.

Still outstanding: the Wet bescherming persoonsgegevens (Wbp), which the
GDPR regime replaced.

## Sources

Listed in frontmatter.
