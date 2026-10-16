---
id: BR-ANPD
type: organisation
name: "Agência Nacional de Proteção de Dados"
name_en: "National Data Protection Agency (ANPD)"
alternative_names:
  - "National Data Protection Agency (ANPD)"
  - "ANPD"
description: >
  Brazil's data protection authority, a regulatory agency linked to the Ministry of Justice and Public Security. It oversees the
  General Data Protection Law (LGPD) and the Digital Statute of Children and Adolescents (ECA Digital), and under decrees of 20 May 2026
  it also supervises internet application providers under the regulation of the Marco Civil da Internet. It was turned into a
  regulatory agency by a provisional measure of 17 September 2025, converted into law in February 2026.

level: national
country: BR
region: null

status: active
organisation_role: regulatory
confidence: high
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
  - BR
  - BR-LGPD
  - BR-ECA-DIGITAL
  - BR-LEI-15352-2026
relationships:
  - type: part-of
    target: BR
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Agency's Institucional page (read 2026-10-16): 'A Agência Nacional de Proteção de Dados (ANPD) é uma Agência Reguladora vinculada ao Ministério da Justiça e Segurança Pública'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: BR-LGPD
    source: fact
    evidence: "The same page (read 2026-10-16): its mission is 'zelar pela proteção de dados pessoais orientada pela Lei nº 13.709, de 14 de agosto de 2018, a Lei Geral de Proteção de Dados (LGPD)'; its competences are in art. 55-J of that law (Competências page, same day)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Institucional — ANPD"
    url: "https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional"
    publisher: "Agência Nacional de Proteção de Dados (Brasil)"
    accessed: "2026-10-16"
    note: "Page modified 5 October 2026."
  - title: "Competências — ANPD"
    url: "https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/competencias"
    publisher: "Agência Nacional de Proteção de Dados (Brasil)"
    accessed: "2026-10-16"
---

# Agência Nacional de Proteção de Dados (Brazil)

> **Created 2026-10-16** (roadmap #481, Brazil). Read on the Agency's own pages on gov.br, which quote the laws and decrees. `start_date` is not recorded: the Agency's creation (before its conversion into a regulatory agency) is not dated on the pages read.

## What the pages say

- **Status.** A regulatory agency ("Agência Reguladora") linked to the Ministry of Justice and Public Security. It was transformed into one by Provisional Measure No. 1.317 of 17 September 2025, converted into Law No. 15.352 of 25 February 2026 ([[BR-LEI-15352-2026]]), which put it on the list of agencies in Law 13.848 of 25 June 2019. Its structure is in Decree No. 12.881 of 18 March 2026 and CD/ANPD Resolution No. 33 of 6 April 2026.
- **Duties.** Protect personal data under [[BR-LGPD]]; apply [[BR-ECA-DIGITAL]] as the autonomous administrative authority for protecting children and adolescents in digital environments; and exercise the powers given by Decrees No. 12.975 and 12.976 of 20 May 2026 (regulating the Marco Civil da Internet and protecting women in the digital environment): supervising internet application providers.
- **Competences (art. 55-J LGPD, quoted).** Among them: protect personal data; draw up guidelines for the National Policy on Personal Data Protection and Privacy; supervise and sanction non-compliance through an administrative process with a right of defence.
- **Constitutional footing.** The Agency's page notes that Constitutional Amendment No. 115 of 10 February 2022 made personal data protection a fundamental right.
- **Home page, 2026.** A public consultation on a regulation for the calculation and application of sanctions ("Regulamento de Dosimetria"), a second partial report on the regulatory sandbox on artificial intelligence, a dedicated complaints page for the new Marco Civil decrees, and a notice that the Agency's site and social media are restricted until the end of the elections.

## Relationships

Part of [[BR]]; `governed-by` [[BR-LGPD]].
