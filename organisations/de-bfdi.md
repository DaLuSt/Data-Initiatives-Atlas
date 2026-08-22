---
id: DE-BFDI
type: organisation
name: Bundesbeauftragte für den Datenschutz und die Informationsfreiheit
alternative_names:
  - BfDI
description: >
  Independent supreme federal authority for data protection and freedom of
  information in Germany, seated in Bonn. It is the data-protection
  supervisory authority for all federal public bodies, certain social
  security institutions, the fiscal authorities and telecommunications and
  postal undertakings, and it also handles complaints about access to
  information under the Informationsfreiheitsgesetz.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EDPB
  - DE-BDSG
  - DE-IFG
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Confirmed by reading gdpr-info.eu's text of Article 68(3) GDPR (2026-08-22): 'the European Data Protection Board shall be composed of the head of one supervisory authority of each Member State ... Where in a Member State more than one supervisory authority is responsible for monitoring the application of the provisions pursuant to this Regulation, a joint representative shall be appointed in accordance with that Member State's law.' Germany has seventeen data-protection supervisory authorities (the BfDI plus one per Land), so this joint-representative mechanism is the basis for the BfDI's participation. Which authority currently holds that role was not established."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-BDSG
    source: fact
    evidence: "Confirmed by reading bfdi.bund.de's 'Aufgaben und Befugnisse der BfDI' page (2026-08-22): 'Die BfDI ist die datenschutzrechtliche Aufsichtsbehörde über alle öffentlichen Stellen des Bundes wie auch für bestimmte Träger der sozialen Sicherung. Außerdem beaufsichtigt sie die Finanzbehörden und die Telekommunikations- und Postdienstunternehmen.' de.wikipedia.org confirms the office is bound by §11 and §12 BDSG (term of office and remuneration), which is the BfDI's own statutory basis under the Bundesdatenschutzgesetz."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-IFG
    source: fact
    evidence: "Confirmed by reading bfdi.bund.de's 'Aufgaben und Befugnisse der BfDI' page (2026-08-22): 'Die BfDI gibt Auskunft, wenn eine der Aufsicht der BfDI unterliegende Stelle ihre Rechte in den Bereichen Datenschutz oder Informationsfreiheit verletzt hat.'"
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
    accessed: "2026-08-22"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
    accessed: "2026-08-22"
  - title: "Aufgaben und Befugnisse der BfDI"
    url: "https://www.bfdi.bund.de/DE/BfDI/Inhalte/BfDI/AufgabenBFDI.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
    accessed: "2026-08-22"
  - title: "Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
    url: "https://www.bfdi.bund.de/DE/BfDI/Inhalte/Datenschutzpfad/BfDI.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
    accessed: "2026-08-22"
  - title: "Bundesbeauftragter für den Datenschutz und die Informationsfreiheit"
    url: "https://de.wikipedia.org/wiki/Bundesbeauftragter_f%C3%BCr_den_Datenschutz_und_die_Informationsfreiheit"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Bundesbeauftragter für den Datenschutz und die Informationsfreiheit (BfDI)"
    url: "https://wirtschaftslexikon.gabler.de/definition/bundesbeauftragter-fuer-den-datenschutz-und-die-informationsfreiheit-bfdi-31020"
    publisher: "Gabler Wirtschaftslexikon"
    accessed: "2026-08-22"
---

# Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)

> **Verified 2026-08-22.** The BfDI's own task pages
> (`AufgabenBFDI.html`, `Datenschutzpfad/BfDI.html`), gdpr-info.eu's text of
> Article 68(3) GDPR, and de.wikipedia.org were read directly and confirmed
> the claims below. `gdprhub.eu` returned a bot-defense challenge page
> rather than content and was not read; it remains listed as a source but
> nothing here is attributed to it alone.

## Description

The BfDI is an **independent supreme federal authority** (unabhängige
eigenständige oberste Bundesbehörde) for data protection and freedom of
information, seated in Bonn.

As a supervisory authority it covers all federal public bodies, certain
social security institutions, the fiscal authorities, and
telecommunications and postal undertakings, checking whether data
protection law is implemented and observed at those bodies. The sources
describe it as the guardian of the fundamental right to informational
self-determination.

Its tasks span both halves of its name:

- **Data protection** — supervising and advising federal authorities and
  other federal public bodies.
- **Freedom of information** — helping people who consider their right of
  access to information under [[DE-IFG]] to have been violated, and
  advising and checking on access to environmental information at federal
  public bodies.

The office-holder is proposed by the federal government, elected by the
Bundestag, and serves a five-year term.

## ⚠ The federal supervisory landscape is not modelled

Germany does not have one data protection authority. The BfDI supervises
**federal** bodies; each Land has its own supervisory authority for the
public bodies and, in most cases, the private sector within it. **None of
those authorities is an Atlas entity**, for the same reason no Land is: the
Atlas has no sub-national level.

This makes the German entry structurally different from the Dutch one in a
way worth stating plainly. [[NL-AP]] is *the* Dutch supervisory authority;
the BfDI is *one of seventeen* German ones. Anyone reading `country: DE`
plus `type: organisation` plus "data protection authority" and inferring
national coverage would be wrong.

## Two relationships that are not asserted

- **`implements` or `governed-by` → [[DE-BDSG]].** The BfDI is plainly the
  authority the BDSG constitutes and empowers, and the BDSG's own sources
  discuss the supervisory regime. But no source read states the connection
  in terms the Atlas can cite, and the BfDI's own task page describes
  powers without being quoted on their statutory basis.
The `participates-in` → [[EU-EDPB]] refusal that used to stand here is
**now closed** — see below.

The remaining one is logged in `discovery/unresolved.md`.

## The EDPB refusal, and how it was closed

An earlier version of this entity refused `participates-in` [[EU-EDPB]]. The
reasoning was that the German federal and Land authorities are certainly
represented on the Board, that no source read said so, and that **the German
representation arrangement — which authority represents Germany, and how —
was precisely the kind of detail that should not be guessed at.**

That refusal was right, and the answer turned out to be in the Regulation
itself.

**[[EU-GDPR]] Article 68(3)** composes the Board of *the head of one
supervisory authority of each Member State and of the European Data
Protection Supervisor, or their respective representatives* — and then adds
the sentence that resolves exactly the German question:

> where in a Member State more than one supervisory authority is responsible
> for monitoring the application of the provisions pursuant to this
> Regulation, **a joint representative shall be appointed in accordance with
> that Member State's law**.

So the multi-authority case is not an obstacle to the edge; it is anticipated
by the provision that creates the Board. The edge is now asserted, and the
`joint representative` mechanism is named in its evidence rather than
glossed over.

Which German authority holds that role in practice is **still not
established**, and the entity does not claim to know.

## Relationships

- `applies-to` [[DE-IFG]] and [[DE-BDSG]].
- `participates-in` [[EU-EDPB]].

## Sources

Listed in frontmatter.
