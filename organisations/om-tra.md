---
id: OM-TRA
type: organisation
name: "Telecommunications Regulatory Authority (Oman)"
alternative_names:
  - "TRA"
  - "هيئة تنظيم الاتصالات"
description: >
  The body that implements telecommunications sector regulation policy in Oman, established in 2002 under the
  Telecommunications Regulation Law (Royal Decree 30/2002) as an independent authority. Its Arabic site describes its sectors as
  telecommunications, which includes supervision of IT infrastructure, cybersecurity and digital services in support of the
  digital transformation and smart-city initiatives, and the radio spectrum, and publishes a legal framework of laws,
  licences, guidelines and regulations (235 documents listed), open data and public consultations.

level: national
country: OM
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
  - OM
  - OM-TELECOM-LAW-2002
relationships:
  - type: part-of
    target: OM
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Authority's About page (read directly 2026-11-01, Arabic): 'هيئة تنظيم الاتصالات (TRA) هي الجهة المنفذة لسياسات تنظيم قطاع الاتصالات في عُمان. تأسست عام 2002 بموجب قانون تنظيم الاتصالات (المرسوم السلطاني 30/2002)' (the TRA is the body implementing telecommunications regulation policy in Oman, established in 2002 under the Telecommunications Regulation Law, Royal Decree 30/2002)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: OM-TELECOM-LAW-2002
    source: fact
    evidence: "The same page: the Authority was 'established in 2002 under the Telecommunications Regulation Law (Royal Decree 30/2002)'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "About the Authority (Arabic) — Telecommunications Regulatory Authority, Oman"
    url: "https://www.tra.gov.om/about"
    publisher: "Telecommunications Regulatory Authority (TRA), Oman"
    accessed: "2026-11-01"
  - title: "Legal framework (Arabic) — Telecommunications Regulatory Authority, Oman"
    url: "https://www.tra.gov.om/legal-framework"
    publisher: "Telecommunications Regulatory Authority (TRA), Oman"
    accessed: "2026-11-01"
---

# Telecommunications Regulatory Authority (Oman)

> **Created 2026-11-01** (roadmap #483, country group 14, Oman). Two Arabic pages of the Authority's own site read directly; the English address needs JavaScript. `start_date` is empty: the page gives the year (2002) of establishment, not a day. The English wording of the description is this session's reading of the Arabic and the Authority's own bilingual page title (Telecommunications Regulatory Authority); the legal framework list's documents (laws, regulations, licences) were not opened.

## Relationships

Part of [[OM]]; governed by [[OM-TELECOM-LAW-2002]].
