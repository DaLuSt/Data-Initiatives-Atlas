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
    evidence: "The Information Commissioner's Office is the UK's independent regulator for data protection and information rights and the supervisory authority under the UK GDPR and the Data Protection Act 2018 (ico.org.uk 'The Information Commission'; en.wikipedia.org 'Information Commissioner's Office'; legislation.gov.uk Data (Use and Access) Act 2025 Part 5). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-UK-GDPR
    source: fact
    evidence: "The Information Commissioner's Office is the UK's independent regulator for data protection and information rights and the supervisory authority under the UK GDPR and the Data Protection Act 2018; the Data (Use and Access) Act 2025 refers throughout to the Information Commission's functions under those instruments (ico.org.uk 'The Information Commission'; legislation.gov.uk Data (Use and Access) Act 2025 Part 5; en.wikipedia.org 'Information Commissioner's Office'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The Information Commission"
    url: "https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-duaa-summary-of-the-changes/the-information-commission/"
    publisher: "Information Commissioner's Office (UK)"
  - title: "Data (Use and Access) Act 2025, Part 5"
    url: "https://www.legislation.gov.uk/ukpga/2025/18/part/5"
    publisher: "legislation.gov.uk (The National Archives)"
  - title: "Data (Use and Access) Act 2025 — Explanatory Notes, division 11"
    url: "https://www.legislation.gov.uk/ukpga/2025/18/notes/division/11/index.htm"
    publisher: "legislation.gov.uk (The National Archives)"
  - title: "Information Commissioner's Office"
    url: "https://en.wikipedia.org/wiki/Information_Commissioner's_Office"
    publisher: "Wikipedia"
  - title: "Receiving personal information from the EEA"
    url: "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/receiving-personal-information-from-the-eea/"
    publisher: "Information Commissioner's Office (UK)"
---

# Information Commissioner's Office

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The ICO is the UK's independent regulator for data protection and
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

This entity is dated 17 August 2026. The Atlas therefore **cannot establish
whether the change has happened**, and it does not guess:

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
