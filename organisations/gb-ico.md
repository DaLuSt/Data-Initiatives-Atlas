---
id: GB-ICO
type: organisation
name: Information Commissioner's Office
alternative_names:
  - ICO
  - Information Commissioner
description: >
  The United Kingdom's independent regulator for data protection and
  information rights until 30 September 2026, and the supervisory authority
  under UK GDPR and the Data Protection Act 2018. It was also a competent
  authority under the Network and Information Systems Regulations 2018 in
  relation to relevant digital service providers. On 30 September 2026 the
  office of Information Commissioner was abolished and its functions were
  transferred to the Information Commission (sections 118 and 119 of the Data
  (Use and Access) Act 2025, commenced by SI 2026/1015); see
  GB-INFORMATION-COMMISSION.

level: national
country: GB
region: null

status: superseded
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: 2026-09-30
last_verified: "2026-10-07"
previous_version: null
successor: GB-INFORMATION-COMMISSION

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - GB-INFORMATION-COMMISSION
  - GB-UK-GDPR
  - GB-DPA-2018
  - GB-DUAA
  - GB-NIS-REGULATIONS
  - NL-AP
  - BE-APD
  - DE-BFDI
  - ES-AEPD
  - FR-CNIL
  - PL-UODO
relationships:
  - type: applies-to
    target: GB-DPA-2018
    source: fact
    evidence: "Confirmed by reading ico.org.uk's 'The Information Commission' page and the DUAA 2025 statute text at legislation.gov.uk (2026-08-22), § 117: 'This section abolishes the office of Information Commissioner and replaces it with the Information Commission... It provides that all references to the Information Commissioner in UK law should be taken to mean the Information Commission.'"
    confidence: medium
    valid_from: null
    valid_until: 2026-09-30
  - type: applies-to
    target: GB-UK-GDPR
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org's 'Information Commissioner's Office' article (2026-08-22): 'It is the independent regulatory office (national data protection authority) dealing with the Data Protection Act 2018, the General Data Protection Regulation, and the Privacy and Electronic Communications (EC Directive) Regulations 2003 across the UK.'"
    confidence: medium
    valid_from: null
    valid_until: 2026-09-30

sources:
  - title: "Information Commission succeeds the ICO as UK's data protection regulator"
    url: "https://www.gov.uk/government/news/information-commission-succeeds-the-ico-as-uks-data-protection-regulator"
    publisher: "GOV.UK (Department for Digital, Culture, Media and Sport)"
    accessed: "2026-10-07"
  - title: "The Information Commission"
    url: "https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-duaa-summary-of-the-changes/the-information-commission/"
    publisher: "Information Commissioner's Office (UK)"
    accessed: "2026-08-22"
  - title: "Data (Use and Access) Act 2025, Part 5"
    url: "https://www.legislation.gov.uk/ukpga/2025/18/part/5"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-08-22"
  - title: "Data (Use and Access) Act 2025 — Explanatory Notes, division 11"
    url: "https://www.legislation.gov.uk/ukpga/2025/18/notes/division/11/index.htm"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-08-22"
  - title: "Information Commissioner's Office"
    url: "https://en.wikipedia.org/wiki/Information_Commissioner's_Office"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Receiving personal information from the EEA"
    url: "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/receiving-personal-information-from-the-eea/"
    publisher: "Information Commissioner's Office (UK)"
    accessed: "2026-08-22"
  - title: "The Data (Use and Access) Act 2025 (Commencement No. 9 and Transitional and Saving Provisions) Regulations 2026 (SI 2026/1015)"
    url: "https://www.legislation.gov.uk/uksi/2026/1015/made"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-10-07"
---

# Information Commissioner's Office

> **Re-verified 2026-10-07.** The office this entity describes no longer
> exists: GOV.UK's announcement of 30 September 2026 and the commencement
> regulations (SI 2026/1015) were read directly and confirm that the
> Information Commissioner was abolished and its functions transferred to the
> Information Commission. The sections below keep the history, because the
> reasoning in them is the reason this change is recorded as it is.

## Description

Until 30 September 2026 the ICO was the UK's independent regulator for data
protection and information rights, and the supervisory authority under
[[GB-UK-GDPR]] and [[GB-DPA-2018]]. It was also a **competent authority under
[[GB-NIS-REGULATIONS]]** for relevant digital service providers, one of the few
data protection authorities in the Atlas with a cybersecurity remit in statute.

## Succeeded on 30 September 2026

[[GB-DUAA]] §117 established a body corporate called the Information
Commission; §118 abolished the office of Information Commissioner and §119
transferred its functions, and the commencement regulations (SI 2026/1015,
made 10 September 2026) brought both into force on 30 September 2026. GOV.UK
announced the change that day: "Information Commission succeeds the ICO as UK's
data protection regulator". The successor is [[GB-INFORMATION-COMMISSION]];
this entity is `superseded` with `end_date: 2026-09-30` and the two
`applies-to` edges below are closed on the same date.

### How the Atlas handled the wait

From 2026-08-22 until the change, this file declined to model it, on three
points that turned out to be the right ones to hold:

- `status` stayed `active` while the change was only mandated, not completed;
- **no successor entity was created** while its existence was not established,
  on the same reasoning that refused Spain's *Centro Nacional de Ciberseguridad*
  and Poland's *Agencja Informatyzacji*;
- `Information Commission` was carried as an alias so a reader searching the new
  name found this entity. That alias moved to the successor's own file on
  2026-10-07.

On 2026-09-26 the commencement date was fixed by SI 2026/1015 but had not yet
arrived, so none of this changed until a source dated after 30 September was
read. This was the closest the Atlas had come to a status it cannot express
(a mandated change with an unverified completion date); the vocabulary still
has no value for it, and the question stays open in `progress/backlog.md` and
roadmap issue #457 for the next such case.

## The seventh data protection authority

| Country | Authority | Also carries `implements-requirement-from` on the GDPR? |
|---|---|---|
| Netherlands | [[NL-AP]] | **yes** — the only one |
| Belgium | [[BE-APD]] | no |
| Germany | [[DE-BFDI]] | no |
| Spain | [[ES-AEPD]] | no |
| France | [[FR-CNIL]] | no |
| Poland | [[PL-UODO]] | no |
| **United Kingdom** | **this entity** | **no — and it could not** |

The UK case is the one that makes the existing inconsistency visible. The
Atlas already carries an open question about why [[NL-AP]] alone implements
a requirement from [[EU-GDPR]] — see `progress/backlog.md`. The ICO
**cannot** carry that edge whichever way the question is resolved, because
there is no EU requirement on it to implement. It is a supervisory authority
under a domesticated statute, not under an EU regulation.

The edge asserted here is `applies-to` [[GB-UK-GDPR]] — the regulator's
remit over the instrument — which is a different claim from any of the six.

## Relationships

- `applies-to` [[GB-UK-GDPR]] and [[GB-DPA-2018]] — the ICO regulates both
  halves of the UK data protection framework, so both edges are asserted.

Note that this entity is also a **competent authority under
[[GB-NIS-REGULATIONS]]** for relevant digital service providers, alongside
[[GB-OFCOM]] for digital infrastructure. No edge is asserted for that here:
[[GB-OFCOM]] carries the `applies-to` edge to the Regulations and the ICO's
cyber role is recorded in prose, because asserting it from a data protection
authority would overstate a remit the sources describe as one line in
Schedule 1.

## Sources

Listed in frontmatter. Three are primary in origin (ICO and
legislation.gov.uk), which makes this the best-sourced organisation in the
UK batch — though still unread.
