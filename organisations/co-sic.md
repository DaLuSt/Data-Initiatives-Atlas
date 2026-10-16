---
id: CO-SIC
type: organisation
name: "Superintendencia de Industria y Comercio"
name_en: "Superintendency of Industry and Commerce (SIC)"
alternative_names:
  - "Superintendency of Industry and Commerce (SIC)"
  - "SIC"
description: >
  Colombian supervisory authority which, under art. 19 of Statutory Law 1581 of 2012, through a Delegatura for the Protection of
  Personal Data, supervises that the principles, rights, guarantees and procedures of the personal data law are respected in the
  processing of personal data. It does much else (competition, consumer protection); only its data protection role is recorded.

level: national
country: CO
region: null

status: active
organisation_role: regulatory
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
  - CO
  - CO-LEY-1581-2012
relationships:
  - type: part-of
    target: CO
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Art. 19 of Law 1581 of 2012 (read 2026-10-16) assigns the role to a Colombian national supervisory authority, the Superintendency of Industry and Commerce, which the Government was to structure with a Delegate Superintendent's office."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: CO-LEY-1581-2012
    source: fact
    evidence: "Art. 19 of the law (read 2026-10-16): the Superintendency 'ejercerá la vigilancia para garantizar que en el Tratamiento de datos personales se respeten los principios, derechos, garantías y procedimientos previstos en la presente ley'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Ley Estatutaria 1581 de 2012 (Secretaría del Senado, base de datos de leyes)"
    url: "http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html"
    publisher: "Secretaría del Senado de la República (Colombia)"
    accessed: "2026-10-16"
    note: "Read as text; the page was last updated 30 September 2026 and carries the Constitutional Court's conditional-constitutionality notes."
---

# Superintendencia de Industria y Comercio (Colombia)

> **Created 2026-10-16** (roadmap #483, Colombia). Known only from the law that designates it; the Superintendency's own site (sic.gov.co) did not answer, so its structure, decisions and the National Database Register are not described, and no founding date is recorded.

## What is sourced

Art. 19 of [[CO-LEY-1581-2012]]: the Superintendency is the data protection authority, acting through a Delegatura for the Protection of Personal Data; the Government was to create a Delegate Superintendent's office for the Authority's functions within six months of the law taking effect.

## Relationships

Part of [[CO]]; `governed-by` [[CO-LEY-1581-2012]].
