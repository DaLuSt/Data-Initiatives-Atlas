---
id: LU-GOVCERT
type: organisation
name: GOVCERT.LU
alternative_names:
  - Government Computer Emergency Response Team Luxembourg
description: >
  Luxembourg's CSIRT (Computer Security Incident Response Team) for the
  public sector, operating under the authority of the Haut-Commissariat à
  la Protection nationale. It is Luxembourg's official point of contact
  for security incidents affecting public entities and critical
  infrastructure operators, handling phishing notification, malware
  analysis and vulnerability alerts, with its director sitting on the
  national crisis cell. Designated as one of Luxembourg's two CSIRTs
  under the country's NIS2 transposition act.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-12"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - LU-HCPN
  - LU-LOI-NIS2
relationships:
  - type: part-of
    target: LU-HCPN
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #181; LU-CTIE, LU-LOI-NIS2). Confirmed by reading infocrise.public.lu — the Luxembourg government's own crisis-information portal — directly (2026-09-12): 'GOVCERT.LU operates under the authority of the Haut-Commissariat à la Protection nationale,' serving as the national contact point for handling security incidents. GOVCERT.LU's own 'À propos de nous' page, read directly, confirms its incident-response role and states only 'conformément à la loi nationale' without naming HCPN, so the organisational link rests on the government's own crisis-portal page rather than GOVCERT.LU's own site."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "À propos de nous — GOVCERT.LU"
    url: "https://govcert.lu/fr/a-propos/"
    publisher: "GOVCERT.LU"
    accessed: "2026-09-12"
  - title: "Structures gouvernementales en matière de cybersécurité"
    url: "https://infocrise.public.lu/fr/cyber/informations-generales/structures-gouvernementales.html"
    publisher: "Infocrise, Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-09-12"
  - title: "NIS 2 au Luxembourg : loi du 5 mai 2026, ILR, GOVCERT.LU et CIRCL"
    url: "https://nisd2.eu/fr/wiki/timelines-and-status/nis2-status-luxembourg"
    publisher: "nisd2.eu"
    accessed: "2026-09-12"
---

# GOVCERT.LU

> **Created 2026-09-12**, closing part of `discovery/unresolved.md` row
> #181 and the gap [[LU-CTIE]] first flagged 2026-09-05: Luxembourg's
> public-sector CSIRT was named in secondary sourcing but unmodelled.
> GOVCERT.LU's own page and the government's own crisis-information
> portal were read directly.

## Description

Confirmed by reading `govcert.lu`'s own "À propos de nous" page directly:
GOVCERT.LU is Luxembourg's official point of contact for security
incidents affecting the public sector, handling phishing notification,
malware analysis and vulnerability alerts. Its own page states only that
it acts "conformément à la loi nationale" (in accordance with national
law) without naming a specific instrument or parent body.

## Parent body, confirmed via a government portal rather than GOVCERT.LU's own site

Reading `infocrise.public.lu` — the Luxembourg government's own
crisis-information portal, a primary source distinct from GOVCERT.LU's
own site — directly: "GOVCERT.LU operates under the authority of the
Haut-Commissariat à la Protection nationale" ([[LU-HCPN]]). [[LU-HCPN]]'s
own pages trace this further: GOVCERT.LU's function originates in the
**Agence nationale de la sécurité des systèmes d'information (ANSSI)**,
an HCPN function (not a separate entity) created by grand-ducal decree in
2015 explicitly to "assurer ... la fonction de CERT national ... et
gouvernemental."

## One of Luxembourg's two CSIRTs under NIS2

Per `nisd2.eu`'s tracking page (a secondary, non-primary source, used
here only to corroborate the CSIRT designation already implied by
GOVCERT.LU's own public-sector remit): GOVCERT.LU is Luxembourg's CSIRT
for the public sector, with [[LU-CIRCL]] covering the private sector,
municipalities and non-governmental entities under [[LU-LOI-NIS2]].

## Relationships

- `part-of` [[LU-HCPN]] — its parent body and the authority under which
  it operates, per the government's own crisis-portal page.

## Not modelled

- The exact legal provision GOVCERT.LU's own page alludes to ("la loi
  nationale") — not named specifically on any page read this pass.

## Sources

Listed in frontmatter. GOVCERT.LU's own page and the government's
crisis-information portal were read directly 2026-09-12; the nisd2.eu
page is secondary and used only for the NIS2 CSIRT-designation
corroboration.
