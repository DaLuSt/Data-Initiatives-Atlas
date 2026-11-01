---
id: QA-CRA
type: organisation
name: "Communications Regulatory Authority (Qatar)"
alternative_names:
  - "CRA"
  - "هيئة تنظيم الاتصالات"
description: >
  Qatar's communications regulator, established by Emiri Decree 42 of 2014, which regulates the telecommunications and
  information technology sector, the postal sector and access to digital media. Its site publishes the telecommunications law
  and by-law, policies (including a cloud policy), regulatory decisions and consultations, and runs the national trust
  services framework as the supervisory body for trust service providers, publishing the Qatar trusted list.

level: national
country: QA
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - QA
  - QA-CSP-REGULATION
relationships:
  - type: part-of
    target: QA
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Authority's About page (read directly 2026-11-01): 'Communications Regulatory Authority (CRA) is the communications regulator of the State of Qatar established by virtue of the Emiri Decree 42 of 2014.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: QA-CSP-REGULATION
    source: fact
    evidence: "The Trust Services introduction (read directly 2026-11-01): 'The CRA has been designated as the national supervisory body, in accordance with Article 33 of the Regulation for Certification Service Providers.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "About CRA — Communications Regulatory Authority, State of Qatar"
    url: "https://cra.gov.qa/en/about-us"
    publisher: "Communications Regulatory Authority (CRA), State of Qatar"
    accessed: "2026-11-01"
  - title: "Trust Services: Introduction — CRA"
    url: "https://cra.gov.qa/en/Services/Trust-Services/Introduction"
    publisher: "Communications Regulatory Authority (CRA), State of Qatar"
    accessed: "2026-11-01"
---

# Communications Regulatory Authority (Qatar)

> **Created 2026-11-01** (roadmap #473, country group 4, Qatar). Three pages of the Authority's own English site read directly. `start_date` is empty: the page gives the Emiri Decree's number and year (2014), not its date, and the Decree itself was not opened (its page on the site returned 404). The telecommunications law (34 of 2006 by the site's own menu path), the by-law, the cloud policy and the decisions were not read.

## Relationships

Part of [[QA]]; supervises under [[QA-CSP-REGULATION]].
