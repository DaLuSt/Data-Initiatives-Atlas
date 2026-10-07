---
id: GB-INFORMATION-COMMISSION
type: organisation
organisation_role: regulatory
name: Information Commission
alternative_names:
  - the Information Commission
description: >
  The United Kingdom's independent regulator for data protection and
  information rights since 30 September 2026, when it succeeded the
  Information Commissioner. Section 118 of the Data (Use and Access) Act 2025
  abolished the office of Information Commissioner and section 119
  transferred its functions to the Commission; both, with section 117(4)(a),
  were brought into force on that date by SI 2026/1015. Where the
  Commissioner was a single office-holder, the Commission is a body corporate
  whose members share collective responsibility for its decisions. On the day
  of the change GOV.UK reported it led by an interim chief executive with
  seven newly appointed non-executive members and recruitment for a chair
  still under way.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 2026-09-30
end_date: null
last_verified: "2026-10-07"
previous_version: GB-ICO
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - GB
  - GB-ICO
  - GB-DUAA
  - GB-UK-GDPR
  - GB-DPA-2018
  - GB-NIS-REGULATIONS
relationships:
  - type: supersedes
    target: GB-ICO
    source: fact
    evidence: "Confirmed by reading two primary sources (2026-10-07). GOV.UK, 30 September 2026, headline: 'Information Commission succeeds the ICO as UK's data protection regulator'; the story says the Commission took over the ICO's functions and that 'those functions transfer to the Information Commission', now held by a body corporate rather than one office-holder. legislation.gov.uk, SI 2026/1015 (made 10 September 2026), regulation 2: 'The following provisions of the Data (Use and Access) Act 2025 come into force on 30th September 2026', being section 117(4)(a), section 118 (abolishes the office of Information Commissioner) and section 119 (transfers its functions to the Information Commission)."
    confidence: high
    valid_from: 2026-09-30
    valid_until: null
  - type: applies-to
    target: GB-DPA-2018
    source: fact
    evidence: "The Commission inherits the Commissioner's remit under the Data Protection Act 2018: ico.org.uk's 'The Information Commission' page, read 2026-08-22 and quoted on GB-ICO, states that DUAA 2025 s.117 'provides that all references to the Information Commissioner in UK law should be taken to mean the Information Commission'. GOV.UK (2026-09-30) adds that the transition 'does not change the regulator's role, responsibilities, or powers'. Carried over from GB-ICO's own edge; not re-read in a statute text after 30 September."
    confidence: medium
    valid_from: 2026-09-30
    valid_until: null
  - type: applies-to
    target: GB-UK-GDPR
    source: fact
    evidence: "Same basis as the edge to GB-DPA-2018: references to the Information Commissioner in UK law, which include UK GDPR, are to be read as references to the Information Commission (ico.org.uk, quoting DUAA 2025 s.117, read 2026-08-22), and GOV.UK (2026-09-30) says the transition does not change the regulator's role, responsibilities or powers."
    confidence: medium
    valid_from: 2026-09-30
    valid_until: null
  - type: part-of
    target: GB
    source: fact
    evidence: "Anchor edge, added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor: GOV.UK (2026-09-30) describes it as 'the UK's data protection regulator'. It asserts scope and nothing more."
    confidence: medium
    valid_from: 2026-09-30
    valid_until: null

sources:
  - title: "Information Commission succeeds the ICO as UK's data protection regulator"
    url: "https://www.gov.uk/government/news/information-commission-succeeds-the-ico-as-uks-data-protection-regulator"
    publisher: "GOV.UK (Department for Digital, Culture, Media and Sport)"
    accessed: "2026-10-07"
  - title: "The Data (Use and Access) Act 2025 (Commencement No. 9 and Transitional and Saving Provisions) Regulations 2026 (SI 2026/1015)"
    url: "https://www.legislation.gov.uk/uksi/2026/1015/made"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-10-07"
  - title: "The Information Commission"
    url: "https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-duaa-summary-of-the-changes/the-information-commission/"
    publisher: "Information Commissioner's Office (UK)"
    accessed: "2026-08-22"
---

# Information Commission

> **Verified 2026-10-07.** The GOV.UK announcement of 30 September 2026 and the
> commencement regulations (SI 2026/1015) were read directly. The board's
> composition is as GOV.UK reported it on the day and will change when a chair
> is appointed; it is not tracked here.

## Description

The Information Commission is the UK's data protection and information rights
regulator from **30 September 2026**. It replaced the Information Commissioner
rather than continuing the office: the office was abolished (§118 of
[[GB-DUAA]]) and its functions were transferred to the new body (§119), so the
Commissioner's entity, [[GB-ICO]], is `superseded` with this one as its
`successor`. The transition, GOV.UK says, "does not change the regulator's
role, responsibilities, or powers".

## Why it exists as an entity now

[[GB-ICO]] declined, from 2026-08-22, to create a successor for a body whose
existence was not established, and said so in writing. That condition has been
met: a government announcement dated the day of the change and the commencement
regulations that fix it are both primary. Of the successors this Atlas has
declined to create for want of an established body, this is the first to be
created; Spain's *Centro Nacional de Ciberseguridad* ([[ES-LCGC]]) and Poland's
*Agencja Informatyzacji* are still not entities.

## What is not asserted

- **Names.** Whether the regulator keeps the "ICO" name is not stated by the
  sources read, so it is not recorded as an alias here.
- **Duties carried over.** The Commissioner was a competent authority under
  [[GB-NIS-REGULATIONS]] for relevant digital service providers. The statutory
  rule that references to the Commissioner now mean the Commission implies the
  Commission holds that role; no edge is asserted, for the reason given on
  [[GB-ICO]].
- **Memberships.** The Commissioner's participation in international bodies is
  recorded on [[GB-ICO]]; whether the Commission has taken it over has not been
  checked.
