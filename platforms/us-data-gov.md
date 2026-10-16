---
id: US-DATA-GOV
type: platform
name: "Data.gov"
alternative_names:
  - "Data.gov — the U.S. Government's open data site"
description: >
  The United States Government's open data site, launched in 2009 and managed and hosted by the U.S. General Services
  Administration's Technology Transformation Services. It harvests agencies' public data listings (data.json files in the DCAT-US
  schema) into a central catalog, and agencies must keep a single data inventory and a public data listing under the OPEN
  Government Data Act.

level: national
country: US
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
organisations: []
related_entities:
  - US
  - US-EVIDENCE-ACT-2018
relationships:
  - type: applies-in
    target: US
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Data.gov's About page (read 2026-10-16): 'The United States Government's open data site' and 'Data.gov was launched in 2009 and is managed and hosted by the U.S. General Services Administration, Technology Transformation Services'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: implements
    target: US-EVIDENCE-ACT-2018
    source: fact
    evidence: "The same page: datasets are collected 'Under the OPEN Government Data Act, which is Title II of the Foundations for Evidence-Based Policymaking Act'; agencies must create a single agency data inventory and publish a public data listing as data.json in the DCAT-US schema, harvested into the Data.gov catalog."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "About Us — Data.gov"
    url: "https://data.gov/about/"
    publisher: "Data.gov, U.S. General Services Administration (Technology Transformation Services)"
    accessed: "2026-10-16"
---

# Data.gov (United States)

> **Created 2026-10-16** (roadmap #482, United States). Read on Data.gov's About page. The page says it "was launched in 2009"; the day and month are not given, so **no `start_date` is recorded** (the schema takes a full date).

## What the page says

Mission: to "unleash the power of government open data" to inform decisions, drive innovation, achieve agency missions and strengthen open government. Built on open-source technology and developed publicly on GitHub; a "next-generation Data Catalog" at catalog.data.gov is in testing. Agencies keep a single data inventory ("just like they would inventory computers or desk chairs") and publish a public data listing as a `data.json` file at their own domain, in the DCAT-US schema, which Data.gov harvests. "Each agency is responsible for its own data."

## Relationships

Applies in [[US]]; `implements` [[US-EVIDENCE-ACT-2018]] (medium confidence).
