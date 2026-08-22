---
id: DE-EGOVG
type: law
name: E-Government-Gesetz
alternative_names:
  - EGovG
  - Gesetz zur Förderung der elektronischen Verwaltung
description: >
  German federal act promoting electronic administration, enacted as
  Article 1 of the act of 25 July 2013 and largely in force from 1 August
  2013. It removes federal-law obstacles to electronic communication
  between citizens or businesses and authorities and within the
  administration, and regulates electronic access to the administration,
  seal services, electronic payment, electronic invoice receipt, evidence
  retrieval, end-to-end digitalisation and electronic record-keeping.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: "2013-08-01"
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE
  - DE-DNG
  - DE-OZG
relationships:
  - type: applies-in
    target: DE
    source: fact
    evidence: "Confirmed by reading the EGovG statute text at gesetze-im-internet.de (2026-08-22): 'Es ist gem. Art. 31 Abs. 1 dieses G am 1.8.2013 in Kraft getreten' — the act entered into force on 1 August 2013, not 31 August as previously recorded (a handful of individual provisions took effect later, staggered through 2020). Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EGovG — Gesetz zur Förderung der elektronischen Verwaltung"
    url: "https://www.gesetze-im-internet.de/egovg/BJNR274910013.html"
    publisher: "Bundesministerium der Justiz / juris (Gesetze im Internet)"
    accessed: "2026-08-22"
  - title: "E-Government-Gesetz (Deutschland)"
    url: "https://de.wikipedia.org/wiki/E-Government-Gesetz_(Deutschland)"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "EGovG E-Government-Gesetz"
    url: "https://www.buzer.de/gesetz/10833/index.htm"
    publisher: "buzer.de"
    accessed: "2026-08-22"
  - title: "eGovernment Gesetz | Kompass der föderalen IT-Architektur"
    url: "https://docs.fitko.de/kompass/docs/grundlagen-und-rahmen/e-government/"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-08-22"
---

# E-Government-Gesetz (EGovG)

> **Verified 2026-08-22.** The consolidated statute text at
> gesetze-im-internet.de and de.wikipedia.org's "E-Government-Gesetz"
> article were read directly. One date was wrong — see below — and is now
> corrected.

## Description

The EGovG was enacted as **Article 1 of the act of 25 July 2013**,
promulgated in the Bundesgesetzblatt on 25 July 2013 (BGBl. I p. 2749) and
largely in force from **1 August 2013**.

## A date correction

The entity previously recorded the in-force date as 31 August 2013. Reading
the statute text directly (2026-08-22) shows this was wrong: "Es ist gem.
Art. 31 Abs. 1 dieses G am **1.8.2013** in Kraft getreten." A handful of
individual provisions (§ 2 Abs. 1, § 2 Abs. 3 with § 14, § 2 Abs. 2, § 6
Satz 1) took effect later, on a staggered schedule running from 2014 to
2020 — which is likely where the "31 August" figure was conflated from a
secondary source. `start_date` is now **2013-08-01**.

Its purpose is to remove obstacles in federal law to electronic
communication between citizens or businesses and an authority, and equally
to communication *within* the administration.

The matters it regulates, as listed in the sources:

- electronic access to the administration;
- seal services (Siegeldienste);
- information about authorities in publicly accessible networks;
- electronic payment options;
- electronic invoice receipt;
- evidence retrieval (Nachweisabruf);
- end-to-end digitalisation;
- electronic record-keeping (elektronische Aktenführung).

It applies to the public-law administrative activity of federal
authorities, including federal corporations, institutions and foundations
under public law. Its central duties are an obligation on the
administration to open an electronic channel, and — additionally for the
federal administration — a De-Mail access, together with principles of
electronic record-keeping.

The act has been amended repeatedly, most recently by Article 11 of an act
of **2 December 2025**.

## Relation to the other German instruments

The EGovG sits underneath two things the Atlas records separately:

- the *Zweites Open-Data-Gesetz* package **amended this act** and
  introduced [[DE-DNG]] at the same time;
- [[DE-OZG]] built on the electronic-administration base by obliging
  authorities to offer administrative services online through linked
  portals.

**Neither is asserted as a relationship.** The first is a legislative
package fact rather than a statement about what the DNG does to the EGovG,
and the second is a widely-held reading of German e-government law that no
source read states. The EGovG is reached from [[DE-BMI]], which produced
the package that amended it, and from the entities that name it here.

## Sources

Listed in frontmatter, including the consolidated text on Gesetze im
Internet and the FITKO's own architecture-compass page.
