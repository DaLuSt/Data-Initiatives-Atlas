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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading gdpr-info.eu's own text of Article 68(3) GDPR directly (2026-08-27): 'The Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives.' The AP is the Netherlands' GDPR supervisory authority (confirmed by rijksoverheid.nl, read directly). This is the same general-composition-rule basis on which the identical edge was confirmed as `source: fact` for FR-CNIL, DE-BFDI, BE-APD and ES-AEPD in their re-verification passes; applied here for consistency rather than the stricter prior standard."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-UAVG
    source: fact
    evidence: "Confirmed by reading rijksoverheid.nl's own contactgids page directly (2026-08-27): the AP's 'tasks and powers are established in the General Data Protection Regulation (GDPR) and the GDPR Implementation Act (UAVG)'. noraonline.nl, also read directly, confirms the AP was 'established and designated as a supervisor' for the AVG and the Uitvoeringswet AVG (UAVG)."
    confidence: high
    valid_from: 2018-05-25
    valid_until: null
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading rijksoverheid.nl directly (2026-08-27), same citation as above: the AP's tasks and powers derive from the GDPR. The GDPR requires every member state to designate an independent supervisory authority; the AP is that authority for the Netherlands."
    confidence: high
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "Autoriteit Persoonsgegevens (AP) — Contactgids"
    url: "https://www.rijksoverheid.nl/service/contact/contactgids/a/autoriteit-persoonsgegevens"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
  - title: "AP (Autoriteit Persoonsgegevens)"
    url: "https://www.noraonline.nl/wiki/AP_(Autoriteit_Persoonsgegevens)"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-27"
  - title: "Privacyregels beschermen persoonsgegevens"
    url: "https://www.rijksoverheid.nl/onderwerpen/privacy-en-persoonsgegevens/privacyregels-beschermen-persoonsgegevens"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
    accessed: "2026-08-27"
---

# Autoriteit Persoonsgegevens (AP)

> **Verified 2026-08-27.** All three originally-cited pages were read
> directly, plus a fourth (gdpr-info.eu's text of Article 68(3) GDPR) added
> to close the `participates-in` [[EU-EDPB]] gap on the same basis already
> accepted elsewhere in the Atlas for [[FR-CNIL]], [[DE-BFDI]], [[BE-APD]]
> and [[ES-AEPD]]. `verification` moves from `search-only` to
> `primary-source`.

## Description

The AP is the Netherlands' independent supervisory authority for the
protection of personal data. Confirmed by reading rijksoverheid.nl directly:
it is "the independent supervisory authority in the Netherlands that
promotes and monitors the protection of personal data," and its "tasks and
powers are established in the General Data Protection Regulation (GDPR) and
the GDPR Implementation Act (UAVG)." noraonline.nl, also read directly,
describes it as "a self-governing administrative body with its own legal
personality" (zelfstandig bestuursorgaan), operating on four core values:
independence, openness, expertise and effectiveness.

Its tasks derive from [[EU-GDPR]], under which every member state must
designate an independent supervisory authority. Per rijksoverheid.nl, the AP
"can intervene if things go wrong" and may impose fines. Its independence is
structural: in performing its tasks and exercising its powers it may neither
seek nor accept instructions from others.

## Relationships

- Governed by [[NL-UAVG]] and [[EU-GDPR]] together — both cited by name in
  the AP's own contactgids page as the source of its tasks and powers.
  Together with [[NL-UAVG]] → [[EU-GDPR]] they form the Atlas's vertical
  chain: EU regulation → national implementing act → national authority.
- `participates-in` [[EU-EDPB]] — closed this pass via gdpr-info.eu's text
  of Article 68(3) GDPR, which states plainly that the Board comprises one
  supervisory authority per Member State. The AP is undisputedly that
  authority for the Netherlands, per the AP's own description. This applies
  the same reasoning that closed the identical gap for [[FR-CNIL]],
  [[DE-BFDI]], [[BE-APD]] and [[ES-AEPD]] — a general composition rule
  stated directly, not an inference from something adjacent, and the prior
  text's stricter refusal (requiring a source to name the AP specifically)
  is corrected here for Atlas-wide consistency.

Still outstanding: the Wet bescherming persoonsgegevens (Wbp), which the
GDPR regime replaced, and the AP's relationship to [[EU-EDPB]]'s Dutch
predecessor body (if any) — not established from any source read.

## Sources

Listed in frontmatter, all four read directly this pass.
