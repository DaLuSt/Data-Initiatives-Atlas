---
id: GB-UK-GDPR
type: regulation
name: UK General Data Protection Regulation
alternative_names:
  - UK GDPR
  - Assimilated Regulation (EU) 2016/679
description: >
  The United Kingdom's general data protection regime, consisting of the
  text of Regulation (EU) 2016/679 as carried into United Kingdom domestic
  law at the end of the Brexit transition period and amended since. It was
  known as retained EU law until the Retained EU Law (Revocation and Reform)
  Act 2023 renamed that category to assimilated law with effect from 1
  January 2024. It operates alongside the Data Protection Act 2018 and was
  substantially amended by the Data (Use and Access) Act 2025, whose main
  data protection provisions came into force on 5 February 2026.

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
organisations:
  - GB-ICO
related_entities:
  - EU-GDPR
  - GB-DPA-2018
  - GB-DUAA
  - NL-UAVG
  - DE-BDSG
  - BE-GDPR-WET
  - FR-LIL
  - ES-LOPDGDD
  - PL-ODO
relationships:
  - type: derived-from
    target: EU-GDPR
    source: fact
    evidence: "UK GDPR is the United Kingdom's version of the General Data Protection Regulation, carried into domestic law as retained EU law; the Retained EU Law (Revocation and Reform) Act 2023 renamed retained EU law to assimilated law with effect from 1 January 2024, and retained direct EU legislation most notably including the UK GDPR continued to take priority under that Act (legislation.gov.uk REUL Act 2023 explanatory notes; commonslibrary.parliament.uk CBP-9841; gov.scot 'Assimilated law (Retained EU law)'; hoganlovells.com). NOT READ — search-only. CAVEAT: the sources establish the derivation and the renaming; the precise commencement instrument and the extent of divergence since are not established."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Retained EU Law (Revocation and Reform) Act 2023 — Explanatory Notes"
    url: "https://www.legislation.gov.uk/ukpga/2023/28/notes/division/7/index.htm"
    publisher: "legislation.gov.uk (The National Archives)"
  - title: "Retained EU Law (Revocation and Reform) Act 2023 — research briefing CBP-9841"
    url: "https://commonslibrary.parliament.uk/research-briefings/cbp-9841/"
    publisher: "House of Commons Library"
  - title: "Assimilated law (Retained EU law)"
    url: "https://www.gov.scot/policies/europe/retained-eu-law/"
    publisher: "Scottish Government"
  - title: "UK — Retained EU Law (Revocation and Reform) Act 2023 – quick guide on the key points"
    url: "https://www.hoganlovells.com/en/publications/uk-retained-eu-law-revocation-and-reform-act-2023-quick-guide-on-the-key-points"
    publisher: "Hogan Lovells"
---

# UK GDPR

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

UK GDPR is **not a transposition of the GDPR. It is the GDPR** — the text of
Regulation (EU) 2016/679, carried into UK domestic law at the end of the
transition period, and amended domestically ever since, most recently and
most substantially by [[GB-DUAA]].

It was *retained EU law* until the **Retained EU Law (Revocation and Reform)
Act 2023** renamed that whole category to **assimilated law** with effect
from **1 January 2024**.

## The GDPR technique table, seventh entry — and a different column

Six batches built this table. The UK does not fit the column it has.

| Country | Instrument | Technique |
|---|---|---|
| France | [[FR-LIL]] | amended a 1978 act in place |
| Netherlands | [[NL-UAVG]] | new implementing act |
| Germany | [[DE-BDSG]] | new act, replacing the earlier one |
| Belgium | [[BE-GDPR-WET]] | new act, repealing the 1992 privacy law |
| Spain | [[ES-LOPDGDD]] | new organic law, carrying digital rights further |
| Poland | [[PL-ODO]] | new act, timed to the GDPR's application date |
| **United Kingdom** | **this entity** | **no technique — the Regulation itself was domesticated** |

Every one of the six *wrote something* to give effect to an EU regulation
that already applied to them directly. The UK wrote nothing of the kind: the
instrument **is** the European text, held in domestic law by a different
constitutional mechanism, and now drifting.

## `derived-from`, and why no new relationship type was needed

Six batches have each added to a running list of *"sourced connections the
relationship vocabulary cannot express"* — now six items long, from
authorised register use to Poland's failed eIDAS 2.0 obligation.

**This is not a seventh.** `metadata/relationship-types.md` defines
`derived-from` as *"one entity was produced by adapting another"*, and that
is precisely, unglamorously, what assimilated law is. The vocabulary written
for a Dutch-and-EU Atlas turned out to describe a post-Brexit legal
relationship it was never designed for, without amendment.

What `derived-from` does **not** say is anything about equivalence, adequacy
or divergence. It says the UK text came from the EU text. Everything after
that — how far the two have moved apart, and whether the Commission still
considers them essentially equivalent — is not in the structured data. See
[[GB]] for the adequacy decisions, which are recorded in prose and refused
as edges.

## What the Data (Use and Access) Act changed

[[GB-DUAA]] amends this instrument rather than replacing it. Among the
changes, from the sources found: automated decision-making is broadened and
may rest on legitimate interests; data subjects gain a right to complain
directly to controllers; consent for scientific research may cover an *area*
of research rather than enumerated purposes; and cookie and PECR enforcement
is aligned with UK GDPR penalties of **£17.5 million or 4% of global
turnover**.

The main data protection provisions commenced on **5 February 2026**.

## `coverage: medium`, and what is missing

The extent of **divergence** from [[EU-GDPR]] is the substance a reader
would most want, and it is only partially established. The sources describe
the DUAA's changes; they do not enumerate where UK GDPR and EU GDPR now
differ in text. Nor is the commencement instrument that carried the
Regulation into domestic law identified by name.

## Relationships

- `derived-from` [[EU-GDPR]].

[[GB-ICO]] carries the `applies-to` edge pointing here.

## Sources

Listed in frontmatter. Two are official (legislation.gov.uk and the
Commons Library), one is a devolved government page, one is legal
commentary.
