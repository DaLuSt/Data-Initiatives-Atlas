---
id: LU-HCPN
type: organisation
name: Haut-Commissariat à la Protection Nationale
alternative_names:
  - HCPN
  - High Commission for National Protection
description: >
  Luxembourg's central government body for national protection, established
  by the loi du 23 juillet 2016 portant création d'un Haut-Commissariat à la
  Protection nationale. It coordinates counter-terrorism, crisis prevention
  and management, and critical infrastructure protection, and hosts the
  Agence nationale de la sécurité des systèmes d'information (ANSSI) as an
  integrated function rather than a separate legal entity — the state's
  information-security authority for classified and unclassified systems,
  created by grand-ducal decree on 21 January 2015 and given statutory basis
  by the 2016 Act. GOVCERT.LU, the CSIRT for the public sector, operates
  under HCPN's authority.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2016-07-23
end_date: null
last_verified: "2026-09-12"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - LU
  - LU-GOVCERT
relationships:
  - type: part-of
    target: LU
    source: fact
    evidence: "Anchor edge under metadata/relationship-types.md §2.3. Confirmed by reading hcpn.gouvernement.lu's own site directly (2026-09-12): HCPN is Luxembourg's central government body for national protection, with missions structured around three pillars including counter-terrorism, crisis prevention/management and critical infrastructure protection. No separate law entity is created for its own founding act, matching the threshold applied elsewhere (e.g. LU-CTIE's founding law)."
    confidence: medium
    valid_from: 2016-07-23
    valid_until: null
sources:
  - title: "Accueil — Haut-Commissariat à la protection nationale"
    url: "https://hcpn.gouvernement.lu/fr.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-09-12"
  - title: "Agence nationale de la sécurité des systèmes d'information (ANSSI)"
    url: "https://hcpn.gouvernement.lu/fr/service/attributions/missions-nationales/anssi.html"
    publisher: "Le gouvernement luxembourgeois"
    accessed: "2026-09-12"
  - title: "Création d'une Agence nationale de la sécurité des systèmes d'information (ANSSI)"
    url: "https://hcpn.gouvernement.lu/fr/actualites/articles0/2015/2015-01-27-creation-anssi.html"
    publisher: "Le gouvernement luxembourgeois"
    accessed: "2026-09-12"
  - title: "Structures gouvernementales en matière de cybersécurité"
    url: "https://infocrise.public.lu/fr/cyber/informations-generales/structures-gouvernementales.html"
    publisher: "Infocrise, Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-09-12"
---

# Haut-Commissariat à la Protection Nationale

> **Created 2026-09-12**, closing part of a gap flagged on [[LU-CTIE]] and
> tracked in `discovery/unresolved.md` row #181: GOVCERT.LU's parent body
> was named but not modelled. Four of HCPN's own government pages were
> read directly.

## Description

Confirmed by reading `hcpn.gouvernement.lu` directly: HCPN is the
Luxembourg government's central body for national protection, with
missions "structured around three pillars," including counter-terrorism,
crisis prevention and management, and critical infrastructure protection.
It was established by the **loi du 23 juillet 2016 portant création d'un
Haut-Commissariat à la Protection nationale** — the same law already
cited on [[LU-ILR]] and [[LU-LOI-NIS2]] research, and confirmed again here
directly on HCPN's own "ANSSI" page.

## ANSSI: a function, not a separate entity

HCPN's own "ANSSI" page states that the **Agence nationale de la sécurité
des systèmes d'information (ANSSI)** is "HCPN's function for information
systems security" — described as operationally integrated into HCPN
rather than a separate legal body. Reading HCPN's own 27 January 2015
news article directly: ANSSI was created by a **grand-ducal decree
adopted by the government council on 21 January 2015**, establishing
"la gouvernance en matière de gestion de la sécurité de l'information,"
predating and then folded into the 2016 statutory HCPN framework. The
same article states, quoted directly, that ANSSI "assurera aussi la
fonction de CERT national ... et gouvernemental" (will also assume the
function of national and governmental CERT) — the origin of what is now
operated as [[LU-GOVCERT]].

Because ANSSI has no separate legal existence from HCPN per HCPN's own
description, no separate `LU-ANSSI` entity is created — the function is
recorded here in prose, distinct from France's identically-abbreviated
but unrelated [[FR-ANSSI]].

## GOVCERT.LU operates under HCPN's authority

Confirmed by reading `infocrise.public.lu` — the Luxembourg government's
own crisis-information portal — directly: "GOVCERT.LU operates under the
authority of the Haut-Commissariat à la Protection nationale," serving as
the national contact point for handling security incidents. See
[[LU-GOVCERT]] for the CSIRT itself.

## Relationships

- `part-of` [[LU]] — anchor edge; no separate founding-law entity is
  created, matching the threshold [[LU-CTIE]] already applied to its own
  founding act.

## Not modelled

- The **loi du 23 juillet 2016** itself as a separate law entity — named
  and dated directly above, but not created here.
- HCPN's other two pillars (counter-terrorism, crisis management) beyond
  the cybersecurity function, which is the only one relevant to this
  Atlas's scope.

## Sources

Listed in frontmatter, all four read directly 2026-09-12.
