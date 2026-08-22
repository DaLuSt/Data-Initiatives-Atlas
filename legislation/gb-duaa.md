---
id: GB-DUAA
type: law
name: Data (Use and Access) Act 2025
alternative_names:
  - DUAA
description: >
  United Kingdom act which received Royal Assent on 19 June 2025 and makes
  the most significant changes to the UK data protection regime since UK
  GDPR was adopted. It amends UK GDPR and the Data Protection Act 2018,
  broadening automated decision-making and permitting reliance on legitimate
  interests, creating a right for data subjects to complain directly to
  controllers, allowing consent for an area of scientific research, aligning
  PECR enforcement with UK GDPR penalties of seventeen and a half million
  pounds or four per cent of global turnover, and establishing smart data
  schemes. Section 117 establishes an Information Commission to replace the
  Information Commissioner's Office. Enhanced notice powers commenced on 19
  August 2025 and the majority of the data protection provisions on 5
  February 2026.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 2025-06-19
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - GB-ICO
related_entities:
  - GB
  - GB-UK-GDPR
  - GB-DPA-2018
  - DE-NIS2UMSUCG
  - PL-KSC
relationships:
  - type: applies-in
    target: GB
    source: fact
    evidence: "Confirmed by reading the DUAA 2025 statute text at legislation.gov.uk (2026-08-22), enacted [19th June 2025], and Clifford Chance's commentary: 'Key provisions of the Data (Use and Access) Act (DUA Act) came into effect on 5 February 2026 under The Data (Use and Access) Act 2025 (Commencement No. 6 and Transitional and Saving Provisions) Regulations 2026.'"
    confidence: medium
    valid_from: 2025-06-19
    valid_until: null
  - type: related-to
    target: GB-UK-GDPR
    source: fact
    evidence: "Confirmed by reading privacyworld.blog and privacymatters.dlapiper.com (2026-08-22): both confirm the automated decision-making changes permitting reliance on legitimate interests, and the GBP 17.5 million / 4% PECR-enforcement alignment; commencement of the majority of provisions on 5 February 2026 is confirmed on cliffordchance.com. CAVEAT: recorded as related-to because the Atlas has no relationship type for amendment; see progress/backlog.md."
    confidence: medium
    valid_from: 2026-02-05
    valid_until: null
  - type: related-to
    target: GB-DPA-2018
    source: fact
    evidence: "Confirmed by reading legislation.gov.uk (2026-08-22), § 117: 'The Data Protection Act 2018 is amended in accordance with subsections (2) to (5)... After section 114 insert— \"The Information Commission ... 114A The Information Commission (1) A body corporate called the Information Commission is established.\"' This is a direct textual amendment of the 2018 Act. CAVEAT: recorded as related-to because the Atlas has no relationship type for amendment."
    confidence: medium
    valid_from: 2026-02-05
    valid_until: null

sources:
  - title: "Data (Use and Access) Act 2025, Part 5"
    url: "https://www.legislation.gov.uk/ukpga/2025/18/part/5"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-08-22"
  - title: "The Data (Use and Access) Act 2025: A New Chapter in the UK's Data Protection Framework"
    url: "https://www.privacyworld.blog/2025/07/the-data-use-and-access-act-2025-a-new-chapter-in-the-uks-data-protection-framework/"
    publisher: "Privacy World (Squire Patton Boggs)"
    accessed: "2026-08-22"
  - title: "Key aspects of the Data (Use and Access) Act take effect"
    url: "https://www.cliffordchance.com/insights/resources/blogs/talking-tech/en/articles/2026/02/key-aspects-of-the-data--use-and-access--act-take-effect.html"
    publisher: "Clifford Chance"
    accessed: "2026-08-22"
  - title: "UK: Commencement of the data protection provisions in the Data (Use and Access) Act"
    url: "https://privacymatters.dlapiper.com/2026/02/uk-commencement-of-the-data-protection-provisions-in-the-data-use-and-access-act/"
    publisher: "DLA Piper"
    accessed: "2026-08-22"
  - title: "UK's Data (Use and Access) Act 2025 – What Does It Change?"
    url: "https://www.alston.com/en/insights/publications/2026/01/uk-data-use-and-access-act-2025"
    publisher: "Alston & Bird"
    accessed: "2026-08-22"
---

# Data (Use and Access) Act 2025

> **Verified 2026-08-22.** The statute text at legislation.gov.uk
> (including § 117 directly) and three law-firm commentaries were read
> directly and confirmed the claims below.

## Description

Confirmed directly on legislation.gov.uk (2026-08-22): Royal Assent
**[19th June 2025]**. Confirmed on cliffordchance.com: "Key provisions of
the Data (Use and Access) Act (DUA Act) came into effect on 5 February
2026 under The Data (Use and Access) Act 2025 (Commencement No. 6 and
Transitional and Saving Provisions) Regulations 2026." The majority of the data protection
provisions in force from **5 February 2026**, with enhanced notice and
document-request powers from **19 August 2025**. It is described as the most
significant change to the UK regime since UK GDPR was adopted.

What it does, from the sources found:

- **automated decision-making** broadened, including reliance on legitimate
  interests where special category data is not involved;
- a **right to complain directly to the controller**, alongside the existing
  right to complain to the regulator;
- **scientific research** consent may cover an *area* of research where not
  all purposes can be identified at collection;
- **cookie and PECR enforcement** aligned with UK GDPR, raising maximum
  penalties to **£17.5 million or 4% of worldwide turnover**;
- **smart data schemes** for portability and sharing of customer and
  business data with authorised third parties;
- **section 117** establishes the **Information Commission** to replace
  [[GB-ICO]].

## The amendment question, for the fourth time

The Atlas still has no relationship type for *"amends"*, and this is the
fourth batch to want one.

| Batch | Amending instrument | What the Atlas did |
|---|---|---|
| Germany | [[DE-NIS2UMSUCG]] amends [[DE-BSIG]] | `supersedes`, `confidence: low` |
| France | [[FR-LIL]] amended a 1978 act | amendment absorbed — one entity, no edge |
| Poland | *nowelizacja* amends the 2018 KSC act | absorbed into [[PL-KSC]]; no separate entity |
| **United Kingdom** | **this act amends two others** | **`related-to` ×2, amendment in the evidence** |

The UK case is the one that makes absorption impossible. Germany's amending
act could be `supersedes`-d because it has its own name; France's and
Poland's could be folded into the amended entity because the amendment had
no independent identity. **This act amends two separate instruments and is
famous in its own right** — it cannot be folded into either, and
`supersedes` would be false twice over, since both [[GB-UK-GDPR]] and
[[GB-DPA-2018]] remain in force.

So the Atlas has now handled amendment **four different ways in four
batches**. `progress/backlog.md` has carried *"decide on an amendment
relationship type"* since the German batch; this is the strongest case yet,
because it is the first where every existing workaround is unavailable.

## Section 117, and a status the vocabulary cannot carry

Confirmed verbatim by reading § 117 directly at legislation.gov.uk
(2026-08-22): "A body corporate called the Information Commission is
established." The Act **establishes** the Information Commission. Whether that body is yet
constituted is not established — see [[GB-ICO]], where the reasoning for not
creating a successor entity is set out. The `related-to` edges here point at
the two instruments, not at the institutional change.

## Relationships

- `applies-in` [[GB]].
- `related-to` [[GB-UK-GDPR]] — amendment, from 5 February 2026.
- `related-to` [[GB-DPA-2018]] — amendment, from 5 February 2026.

[[EU-UK-ADEQUACY]] carries a `references` edge pointing here: the European
Commission renewed the UK's adequacy **after** this Act, having satisfied
itself the changes did not break equivalence.

Both carry the amendment in the `evidence` string because the type does not
carry it.

## Sources

Listed in frontmatter. One official (legislation.gov.uk); the remaining four
are law-firm commentary, which is why `confidence` is medium and why the
commencement dates in particular want a primary citation.
