---
id: VU-DIGITAL-SAFETY-AUTHORITY
type: organisation
name: "Digital Safety Authority (Vanuatu)"
alternative_names:
  - "Deputy Commissioner of Data Protection and Privacy (Vanuatu)"
description: >
  Vanuatu's Digital Safety Authority, a body corporate established by the Digital Safety Authority Act No. 15 of 2024 (section 2; assented 5 December 2024, commencement 2 January 2025 on the Act's cover page), with functions to promote digital safety, coordinate digital-safety activities with government agencies, protect the public against digital harm and represent Vanuatu internationally on data protection and privacy and harmful digital communication (section 3).
  Its Commissioner may, with the Digital Safety Commission's approval, appoint a Deputy Commissioner of Data Protection and Privacy (section 22), who receives and determines complaints about data protection and privacy breaches (section 24) and is the enforcement officer of the Data Protection and Privacy Act No. 13 of 2024.
  Whether the Authority and the Deputy Commissioner are in post was not read.

level: national
country: VU
region: null

status: unknown
organisation_role: regulatory
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - VU
  - VU-DPPA-2024
relationships:
  - type: part-of
    target: VU
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Digital Safety Authority Act No. 15 of 2024 (read directly 2026-11-22 from the copy on cert.gov.vu, Vanuatu's CERT): section 2(1), 'The Digital Safety Authority is established', and 2(2)(a), it is 'a body corporate with perpetual succession'. A statutory body of the Republic of Vanuatu; the Act's 'Minister' is the Minister responsible for information and communications (section 1)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: VU-DPPA-2024
    source: fact
    evidence: "The Data Protection and Privacy Act No. 13 of 2024 (read directly 2026-11-22) defines its enforcement officer: 'Deputy Commissioner means the Deputy Commissioner of Data Protection and Privacy appointed under the Digital Safety Authority Act No. 15 of 2024'. That Act, section 22(1)(b), lets the Authority's Commissioner appoint 'the Deputy Commissioner of Data Protection and Privacy', and section 24(2)(b) gives that Deputy Commissioner the function 'to receive and determine complaints related to data protection and privacy breaches'. `valid_from` is empty: whether the Deputy Commissioner has been appointed was not read."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Digital Safety Authority Act No. 15 of 2024 (copy on cert.gov.vu)"
    url: "https://cert.gov.vu/images/legislation/Digital_Safety_Authority_Act_No15_of_2024-EN.pdf"
    publisher: "Republic of Vanuatu (copy hosted by CERT Vanuatu, cert.gov.vu)"
    accessed: "2026-11-22"
  - title: "Data Protection and Privacy Act No. 13 of 2024 (copy on cert.gov.vu)"
    url: "https://cert.gov.vu/images/legislation/Data_Protection_and_Privacy_Act_No13_of_2024-EN.pdf"
    publisher: "Republic of Vanuatu (copy hosted by CERT Vanuatu, cert.gov.vu)"
    accessed: "2026-11-22"
---

# Digital Safety Authority (Vanuatu)

> **Created 2026-11-22** (scan issue #770: laws with no body). Sourced from the Digital Safety Authority
> Act No. 15 of 2024 and the definition in [[VU-DPPA-2024]], both read directly on cert.gov.vu.
> `status: unknown`: no appointment and no page of the Authority were read.

## One authority, two deputy commissioners

The Authority is a body corporate (section 2) headed by a Commissioner (sections 5 and 6) and overseen by a
Digital Safety Commission (section 13). Under it sit two Deputy Commissioners (section 22): one for harmful
digital communications and one for data protection and privacy. The second is the officer [[VU-DPPA-2024]]
gives its enforcement powers to; section 24(2)(b) of the Authority's Act gives that officer the complaints
about data protection and privacy breaches.

Data protection is thus placed inside an online-safety authority, not in a stand-alone data protection
office. The entity is filed under the Authority because the Deputy Commissioner is an officer appointed
by it, not a separate legal person.

## Not modelled

- The **Digital Safety Authority Act No. 15 of 2024** itself, and the Harmful Digital Communications Act No.
  14 of 2024 that the other Deputy Commissioner serves; both are listed on cert.gov.vu.
- The **Digital Safety Commission** (section 13) as a separate entity.

## Relationships

Part of [[VU]]; governed by [[VU-DPPA-2024]].
