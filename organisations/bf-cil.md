---
id: BF-CIL
type: organisation
name: "Commission de l'Informatique et des Libertés"
name_en: "Commission of Informatics and Liberties (CIL)"
alternative_names:
  - "Commission of Informatics and Liberties (CIL)"
  - "CIL"
  - "CIL Burkina Faso"
description: >
  Burkina Faso's data protection authority: an independent administrative authority with administrative and management autonomy,
  created by article 45 of law 001-2021/AN to see that the law is respected, to inform data subjects and controllers of their rights and
  obligations and to control the use of ICT in personal data processing. In August 2026 the National Assembly also passed an organic law
  on a communication and data protection regulator, whose effect on the CIL was not read.

level: national
country: BF
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
  - BF
  - BF-LOI-001-2021
  - BF-LOI-ORG-038-2026
relationships:
  - type: part-of
    target: BF
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Art. 45 of law 001-2021/AN (read 2026-10-17): the CIL is an 'autorité administrative indépendante' whose organisation is set by decree in the Council of Ministers; its site (cil.bf) is that of the Burkinabè authority."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: BF-LOI-001-2021
    source: fact
    evidence: "Art. 45 of the law (read 2026-10-17): the CIL 'est l'autorité de contrôle chargée de veiller au respect des dispositions de la présente loi'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Loi n°001-2021/AN portant protection des personnes à l'égard du traitement des données à caractère personnel"
    url: "https://cil.bf/wp-content/uploads/2026/10/loi-n°001.pdf"
    publisher: "Commission de l'Informatique et des Libertés (Burkina Faso)"
    accessed: "2026-10-16"
    note: "Read as text, 36 pages; adopted 30 March 2021."
  - title: "Lois — CIL Burkina Faso"
    url: "https://cil.bf/?page_id=1017"
    publisher: "Commission de l'Informatique et des Libertés (Burkina Faso)"
    accessed: "2026-10-16"
    note: "A list of laws and decrees to download. The two 2026 decrees are scanned images with no extractable text; the 2021 law was read as text."
---

# CIL (Burkina Faso)

> **Created 2026-10-17** (roadmap #477, Burkina Faso). Read in the 2021 law and on the CIL's site (cil.bf). **No `start_date`**: the law that creates it is dated 30 March 2021 and the decree that organised it was not read. Whether the organic law of August 2026 ([[BF-LOI-ORG-038-2026]]) replaces or absorbs the CIL is not established, so the status stays `active`.

## What the sources say

Art. 45-: independent administrative authority; nine members (one designated by the President of Faso among others), five-year terms; regulatory and sanctioning power. The site's news (2026) shows ordinary sessions of its College of Commissioners examining processing files, a role at the Grand Salon de la Data en Afrique in Ouagadougou and the SIPEN-UEMOA regional meeting, and public awareness work on children and digital habits.

## Relationships

Part of [[BF]]; `governed-by` [[BF-LOI-001-2021]].
