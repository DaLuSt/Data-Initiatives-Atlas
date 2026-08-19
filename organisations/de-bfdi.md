---
id: DE-BFDI
type: organisation
name: Bundesbeauftragte für den Datenschutz und die Informationsfreiheit
alternative_names:
  - BfDI
  - Federal Commissioner for Data Protection and Freedom of Information
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
verification: search-only

start_date: null
end_date: null
last_verified: null
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
    evidence: "Article 68(3) GDPR provides that the European Data Protection Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives; Article 68(3) further provides that where in a Member State more than one supervisory authority is responsible for monitoring the application of the Regulation, a joint representative shall be appointed in accordance with that Member State's law — which is the arrangement that applies to Germany, with a federal commissioner and seventeen authorities in total (gdpr-info.eu 'Art. 68 GDPR — European Data Protection Board'; gdprhub.eu 'Article 68 GDPR'; edpb.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-BDSG
    source: fact
    evidence: "The BfDI is the independent supreme federal authority for data protection and freedom of information in Germany and the data-protection supervisory authority for all federal public bodies, certain social security institutions, the fiscal authorities and telecommunications and postal undertakings; the Bundesdatenschutzgesetz is the federal act under which that supervision is exercised (bfdi.bund.de 'Aufgaben des BfDI'; de.wikipedia.org 'Bundesbeauftragter fuer den Datenschutz und die Informationsfreiheit'; wirtschaftslexikon.gabler.de). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-IFG
    source: fact
    evidence: "Among the BfDI's tasks is helping persons who consider their fundamental right of access to information under the IFG to have been violated (bfdi.bund.de 'Aufgaben und Befugnisse der BfDI'; de.wikipedia.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
  - title: "Aufgaben und Befugnisse der BfDI"
    url: "https://www.bfdi.bund.de/DE/BfDI/Inhalte/BfDI/AufgabenBFDI.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
  - title: "Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
    url: "https://www.bfdi.bund.de/DE/BfDI/Inhalte/Datenschutzpfad/BfDI.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
  - title: "Bundesbeauftragter für den Datenschutz und die Informationsfreiheit"
    url: "https://de.wikipedia.org/wiki/Bundesbeauftragter_f%C3%BCr_den_Datenschutz_und_die_Informationsfreiheit"
    publisher: "Wikipedia"
  - title: "Bundesbeauftragter für den Datenschutz und die Informationsfreiheit (BfDI)"
    url: "https://wirtschaftslexikon.gabler.de/definition/bundesbeauftragter-fuer-den-datenschutz-und-die-informationsfreiheit-bfdi-31020"
    publisher: "Gabler Wirtschaftslexikon"
---

# Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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

- `applies-to` [[DE-IFG]].

## Sources

Listed in frontmatter.
