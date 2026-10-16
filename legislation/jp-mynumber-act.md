---
id: JP-MYNUMBER-ACT
type: act
name: "Act on the Use of Numbers to Identify a Specific Individual in Administrative Procedures"
name_en: "Act on the Use of Numbers to Identify a Specific Individual in Administrative Procedures (My Number Act)"
alternative_names:
  - "Act on the Use of Numbers to Identify a Specific Individual in Administrative Procedures (My Number Act)"
  - "My Number Act"
  - "マイナンバー法"
description: >
  The Japanese statute behind the My Number identification number, named on the Personal Information Protection Commission's page as
  one of the two Acts the Commission supervises (for 'specific personal information') and for which the Digital Agency is responsible.
  The Act's text, number and date were not read.

level: national
country: JP
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - JP-PPC
  - JP-DIGITAL-AGENCY
related_entities:
  - JP
  - JP-PPC
  - JP-DIGITAL-AGENCY
relationships:
  - type: applies-in
    target: JP
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Commission's Roles page (read 2026-10-16) lists 'Act on the Use of Numbers to Identify a Specific Individual in Administrative Procedures' among the Acts it covers, with the Digital Agency responsible."
    confidence: high
    valid_from: null
    valid_until: null
  - type: references
    target: JP-DIGITAL-AGENCY
    source: fact
    evidence: "The same page: 'The Digital Agency is responsible for the above Act.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Roles and Responsibilities — Personal Information Protection Commission"
    url: "https://www.ppc.go.jp/en/aboutus/roles/"
    publisher: "Personal Information Protection Commission (Japan)"
    accessed: "2026-10-16"
---

# My Number Act (Japan)

> **Created 2026-10-16** (roadmap #482, Japan). Known only from one page of the Commission; neither the Act's number nor its date was read, so **no date is recorded**.

## What is sourced

The Commission's Roles page lists it beside [[JP-APPI]]. The Commission performs "specific personal information protection assessment" (an assessment report submitted by entities that handle My Number data) and supervises; [[JP-DIGITAL-AGENCY]] is responsible for the Act. The Agency's page says J-LIS issues the My Number Card and runs the systems behind it.

## Relationships

Applies in [[JP]]; `references` [[JP-DIGITAL-AGENCY]].
