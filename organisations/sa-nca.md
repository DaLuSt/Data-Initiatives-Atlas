---
id: SA-NCA
type: organisation
name: "National Cybersecurity Authority (Saudi Arabia)"
alternative_names:
  - "NCA"
  - "الهيئة الوطنية للأمن السيبراني"
description: >
  Saudi Arabia's competent authority in charge of cybersecurity and the national reference in its affairs, established under Royal
  Order No. 55775 dated 23 August 2017, with its Statute issued by Royal Order No. 6801 dated 31 October 2017 and amended by Royal
  Order No. 7053 dated 9 September 2021. It has public legal personality, financial and administrative independence and reports
  to the King. It issues cybersecurity controls, frameworks and guidelines, runs the Saudi CERT and training programmes, and
  publishes the National Cybersecurity Strategy.

level: national
country: SA
region: null

status: active
organisation_role: regulatory
confidence: medium
coverage: low
verification: primary-source
start_date: 2017-08-23
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - SA
  - SA-NCA-LEGAL-POWERS-2024
  - SA-NCA-ECC
  - SA-NCA-DCC
  - SA-NCSS
relationships:
  - type: part-of
    target: SA
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Authority's Laws and Regulations page (read directly 2026-11-01): 'The National Cybersecurity Authority (NCA) was established under Royal Order No. (55775) dated 23/8/2017 ... to be the competent authority nationally in charge of cybersecurity in the Kingdom ... shall report to the King'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: SA-NCA-LEGAL-POWERS-2024
    source: fact
    evidence: "The same page: 'The Legal Powers of the National Cybersecurity Authority issued by Royal Decree No. (M/117) dated 22/12/2024. The NCA's Legal Powers include identifying the cybersecurity violations, and the Legal procedures related to cybersecurity violations.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: produces
    target: SA-NCA-ECC
    source: fact
    evidence: "The Authority's Essential Cybersecurity Controls page (read directly 2026-11-01): the Essential Cybersecurity Controls (ECC 2-2024) are published by the Authority."
    confidence: high
    valid_from: null
    valid_until: null
  - type: produces
    target: SA-NCA-DCC
    source: fact
    evidence: "The Authority's Data Cybersecurity Controls page (read directly 2026-11-01): 'NCA has issued the Data Cybersecurity Controls (DCC-1:2022)'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Laws and Regulations — National Cybersecurity Authority"
    url: "https://nca.gov.sa/en/laws-and-regulations/"
    publisher: "National Cybersecurity Authority (NCA), Saudi Arabia"
    accessed: "2026-11-01"
  - title: "National Cybersecurity Authority — home page"
    url: "https://nca.gov.sa/en/"
    publisher: "National Cybersecurity Authority (NCA), Saudi Arabia"
    accessed: "2026-11-01"
---

# National Cybersecurity Authority (Saudi Arabia)

> **Created 2026-11-01** (roadmap #476, country group 7, Saudi Arabia). Two pages of the Authority's own English site read directly. `start_date` is the date of the Royal Order that established it (23 August 2017) as the page gives it; the page's dd/mm/yyyy dates are read as Gregorian. The Statute and the Royal Decree texts were not opened. SDAIA, which holds the personal data law, rejects the agent's requests.

## Relationships

Part of [[SA]]; governed by [[SA-NCA-LEGAL-POWERS-2024]]; issues [[SA-NCA-ECC]] and [[SA-NCA-DCC]]; publishes [[SA-NCSS]].
