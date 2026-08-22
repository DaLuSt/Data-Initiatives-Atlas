---
id: GB-ICO
type: organisation
name: Information Commissioner's Office
alternative_names:
  - ICO
  - Information Commissioner
  - Information Commission
description: >
  The United Kingdom's independent regulator for data protection and
  information rights, and the supervisory authority under UK GDPR and the
  Data Protection Act 2018. It is also a competent authority under the
  Network and Information Systems Regulations 2018 in relation to relevant
  digital service providers. Section 117 of the Data (Use and Access) Act
  2025 establishes an Information Commission to replace it, replacing the
  single Information Commissioner with a board comprising a chair, a chief
  executive and seven non-executive directors, with the change reported as
  expected during 2026.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
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
    valid_until: null
  - type: applies-to
    target: GB-UK-GDPR
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org's 'Information Commissioner's Office' article (2026-08-22): 'It is the independent regulatory office (national data protection authority) dealing with the Data Protection Act 2018, the General Data Protection Regulation, and the Privacy and Electronic Communications (EC Directive) Regulations 2003 across the UK.'"
    confidence: medium
    valid_from: null
    valid_until: null

sources:
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
---

# Information Commissioner's Office

> **Verified 2026-08-22.** ico.org.uk's own "The Information Commission"
> page, the DUAA 2025 statute text (§ 117) and en.wikipedia.org's ICO
> article were read directly and confirmed the claims below. The board
> composition detail (chair, chief executive, seven non-executive
> directors) and the "expected in 2026" timing were not independently
> re-confirmed this pass and are retained from the original sourcing.

## Description

Confirmed by reading legislation.gov.uk's DUAA 2025 text (2026-08-22),
§ 117: "This section abolishes the office of Information Commissioner and
replaces it with the Information Commission... It provides that all
references to the Information Commissioner in UK law should be taken to
mean the Information Commission." The ICO is the UK's independent regulator for data protection and
information rights, and the supervisory authority under [[GB-UK-GDPR]] and
[[GB-DPA-2018]]. It is also a **competent authority under
[[GB-NIS-REGULATIONS]]** for relevant digital service providers — one of the
few data protection authorities in the Atlas with a cybersecurity remit in
statute.

## A transformation the Atlas deliberately does not model

**Section 117 of [[GB-DUAA]] establishes an *Information Commission* to
replace the ICO**, swapping the single Information Commissioner for a board
of a chair, a chief executive and seven non-executive directors, with new
powers to compel witnesses and request technical reports. The sources
describe the move as **"expected in spring/summer 2026"**.

This entity is dated 17 August 2026, and re-verified 2026-08-22. One weak
signal, not a confirmation: en.wikipedia.org's infobox for the ICO lists
the Information Commissioner as **"Vacant"** as of this reading, consistent
with a transition in progress but not proof one has completed — a vacancy
could equally mean an ordinary gap between appointments. The Atlas
therefore still **cannot establish whether the change has happened**, and
it does not guess:

- `status` stays **`active`** — the regulator exists either way;
- **no successor entity was created**, on the same reasoning that refused
  Spain's *Centro Nacional de Ciberseguridad* and Poland's *Agencja
  Informatyzacji*: a body whose existence is not established does not get an
  ID;
- **`Information Commission` is carried in `alternative_names`**, so a
  reader searching the new name finds this entity.

That last decision is a judgement, and it cuts the other way from the first
two. If the Commission is now constituted, this entity is filed under a name
that no longer applies. The alternative — creating an entity for a body that
may not yet exist — would have been worse, and the Atlas has refused it
three times before.

⚠ **This is the closest the Atlas has come to a `status` it cannot express.**
[[FR-NIS2-LOI]] is `unknown` because sources contradict each other;
[[ES-LCGC]] is `proposed` because it is a draft. Here the *instrument* is in
force and the *institutional change it mandates* has an unverified
completion date. None of the three vocabulary values says that.

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
