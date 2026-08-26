---
id: FI-SECONDARY-USE-ACT
type: law
name: Act on the Secondary Use of Health and Social Data (552/2019)
alternative_names:
  - Secondary Use Act
  - Laki sosiaali- ja terveystietojen toissijaisesta käytöstä
  - "552/2019"
description: >
  Finnish act of 2019 regulating how health and social data may be used
  outside the purpose for which it was collected — in scientific research,
  statistics, innovation and development, knowledge management, teaching, and
  authority planning and reporting. Its stated purpose is to establish
  conditions for the effective and secure processing of and access to personal
  health and social data for those secondary purposes. It is the basis for the
  social and health data permit authority Findata, established the same year.
  The act is not applied to clinical trials.

level: national
country: FI
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
organisations:
  - FI-FINDATA
related_entities:
  - FI
  - FI-FINDATA
  - EU-EHDS
relationships:
  - type: applies-in
    target: FI
    source: fact
    evidence: "Confirmed by reading findata.fi's own legislation page directly (2026-08-26): the Secondary Use Act (552/2019) 'regulates how health and social data may be used outside their original purpose, for example in scientific research, statistics, and planning and reporting duty of an authority.' The same page states the Act 'entered into force in May 2019' (findata.fi's news item on Findata's own launch, also read directly) — a month-level date, not the placeholder day this entity previously carried. The Act was itself amended by the Act amending the Act on the Secondary Use of Health and Social Data (1159/2025), named on findata.fi's own legislation page: the clinical-trials-related amendments entered into force 1 January 2026, the remainder on 1 May 2026."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Legislation — Findata"
    url: "https://findata.fi/en/services-and-instructions/legislation/"
    publisher: "Findata"
    accessed: "2026-08-26"
  - title: "Secondary use of health and social data"
    url: "https://stm.fi/en/secondary-use-of-health-and-social-data"
    publisher: "Ministry of Social Affairs and Health (Finland)"
    accessed: "2026-08-26"
  - title: "Act on the Secondary Use of Health and Social Data"
    url: "https://www.uef.fi/en/library/act-on-the-secondary-use-of-health-and-social-data"
    publisher: "University of Eastern Finland Library"
    accessed: "2026-08-26"
  - title: "Act on Secondary Use of Health and Social Data will not be applied to clinical trials"
    url: "https://findata.fi/en/news/act-on-secondary-use-of-health-and-social-data-will-not-be-applied-to-clinical-trials/"
    publisher: "Findata"
    accessed: "2026-08-26"
  - title: "A new authority to start operation: faster utilisation of social welfare and health care data resources"
    url: "https://findata.fi/en/news/a-new-authority-to-start-operation-faster-utilisation-of-social-welfare-and-health-care-data-resources/"
    publisher: "Findata"
    accessed: "2026-08-26"
---

# Finnish Secondary Use Act (552/2019)

> **Verified 2026-08-26.** All five cited pages were read directly. The
> Act's own legislation page reveals a 2025 amendment (Act 1159/2025)
> this entity did not previously know about, and the University of
> Eastern Finland's own library page flags its English-translation
> summary as "not up-to-date" — an independent signal the same
> amendment left the entity's original sourcing stale. The guessed
> `start_date: 2019-01-01` is corrected: findata.fi states the Act
> "entered into force in May 2019," a month, not the day this entity
> had fabricated.

## Description

The act that governs **secondary use** of Finnish health and social data —
use outside the purpose for which the data was collected. The listed
secondary purposes are:

| |
|---|
| scientific research |
| statistics |
| innovation and development |
| knowledge management |
| teaching |
| authority planning and reporting |

It is the statutory basis for [[FI-FINDATA]].

## A 2025 amendment, found this pass

findata.fi's own legislation page, read directly, names an amending act
this entity had no knowledge of: the **Act amending the Act on the
Secondary Use of Health and Social Data (1159/2025)**. Its
clinical-trials-related provisions took effect **1 January 2026**; the
rest took effect **1 May 2026** — both inside the last eight months, and
neither reflected anywhere in this entity's prior sourcing. findata.fi
describes one substantive change directly: before the amendment,
"the processing of data permits was largely centralised under Findata"
whenever an application spanned multiple data controllers; after it, "a
distributed permit model was introduced, under which a data permit...
can be applied for either through Findata or separately from individual
data controllers." What exactly changed for clinical trials specifically
is not stated on any page read this pass, so it is not guessed at here.

## An exclusion that defines the boundary

The act is **not applied to clinical trials** — confirmed via a Findata
notice dated 3 June 2020, well before the 2025 amendment, so this
exclusion predates and is distinct from whatever the amendment's
clinical-trials provisions actually changed. That original boundary is
worth recording regardless: it marks where the secondary-use regime
stops and the clinical-research regime begins. A trial collects data
*for* research, so it is not secondary use at all — and the Atlas's
other health entities do not draw that line anywhere.

## The first Finnish health entities, and the fourth country in the domain

[[FI]] gained a national layer in the country-expansion batch and had no
health entity. This act and [[FI-FINDATA]] are its first two.

Counting from [[DOMAIN-HEALTH]]'s position before 2026-08-21 — **one country,
the Netherlands** — the domain now reaches five: [[NL]], [[DE]], [[FR]],
[[FI]] and [[DK]], in that order of addition.

## What the date is, and is not

`start_date` was **2019-01-01** — a fabricated day-of-year with no source
behind it, corrected this pass to **unset**. findata.fi states the Act
"entered into force in May 2019," which is now recorded in the
`applies-in` relationship's evidence text; no source read gives an exact
day, so none is guessed.

## Relationships

- `applies-in` [[FI]] — anchor edge.
- The `governed-by` edge lives on [[FI-FINDATA]], the authority the act
  establishes.

## Sources

Listed in frontmatter, all five read directly this pass — Findata's
legislation page (which surfaced the 2025 amendment), its launch
announcement, its clinical-trials notice, the ministry's account of the
regime, and a university library guide.
