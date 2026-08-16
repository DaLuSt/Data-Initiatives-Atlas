---
id: DE-BSI
type: organisation
name: Bundesamt für Sicherheit in der Informationstechnik
alternative_names:
  - BSI
  - Federal Office for Information Security
description: >
  German federal higher authority (Bundesoberbehörde) for information
  security, in the portfolio of the Federal Ministry of the Interior. Its
  remit is set by the BSI-Gesetz: preventive promotion of information and
  cyber security, protection of federal government IT systems, acting as
  the central reporting point for IT security, and improving the protection
  of critical infrastructures.

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
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - DE-BMI
  - DE-BSIG
relationships:
  - type: part-of
    target: DE-BMI
    source: fact
    evidence: "The BSI is a federal higher authority (Bundesoberbehörde) in the portfolio of the Federal Ministry of the Interior (de.wikipedia.org 'Bundesamt für Sicherheit in der Informationstechnik'; bsi.bund.de/DE/Das-BSI/Auftrag). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-BSIG
    source: fact
    evidence: "The scope of the BSI's tasks is defined by the BSI-Gesetz; under § 4 BSIG the BSI acts as the central reporting point for IT security, collecting and evaluating information on vulnerabilities and attack patterns (bsi.bund.de/DE/Das-BSI/Auftrag/Gesetze-und-Verordnungen/BSI-Gesetz). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: produces
    target: DE-IT-GRUNDSCHUTZ
    source: fact
    evidence: "IT-Grundschutz is the methodology developed by the BSI, set out in the BSI-Standards 200-1 to 200-4 and the IT-Grundschutz-Kompendium (de.wikipedia.org 'BSI-Standard'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "BSI — Bundesamt für Sicherheit in der Informationstechnik"
    url: "https://www.bsi.bund.de/"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
  - title: "BSI — Auftrag"
    url: "https://www.bsi.bund.de/DE/Das-BSI/Auftrag/auftrag_node.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
  - title: "Gesetz über das Bundesamt für Sicherheit in der Informationstechnik (BSI-Gesetz — BSIG)"
    url: "https://www.bsi.bund.de/DE/Das-BSI/Auftrag/Gesetze-und-Verordnungen/BSI-Gesetz/bsi-gesetz_node.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
  - title: "Bundesamt für Sicherheit in der Informationstechnik"
    url: "https://de.wikipedia.org/wiki/Bundesamt_f%C3%BCr_Sicherheit_in_der_Informationstechnik"
    publisher: "Wikipedia"
  - title: "Cybersicherheitsrecht: NIS-2-Umsetzungsgesetz ab morgen in Kraft"
    url: "https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2025/251205_NIS-2-Umsetzungsgesetz_in_Kraft.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
---

# Bundesamt für Sicherheit in der Informationstechnik (BSI)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BSI is a **Bundesoberbehörde** — a federal higher authority — in the
portfolio of [[DE-BMI]]. Its remit is set by [[DE-BSIG]].

Its stated goal is the preventive promotion of information and cyber
security so that information and communication technology can be used
securely across society. Concretely the sources describe:

- **protecting federal IT systems**, including defence against viruses,
  trojans and other technical threats to federal administration computers
  and networks;
- acting as the **central reporting point for IT security** under § 4
  BSIG, collecting and evaluating information on vulnerabilities and new
  attack patterns;
- improving the protection of **critical infrastructures (KRITIS)** and
  raising network security in sectors whose failure would have severe
  consequences for the economy, the state and society.

Its tasks and powers were significantly expanded by the IT-Sicherheitsgesetz
which came into force in 2015, and again by [[DE-NIS2UMSUCG]], which took
the number of facilities it supervises from roughly 4,500 to roughly
29,500.

It produces [[DE-IT-GRUNDSCHUTZ]].

## The German counterpart to two Dutch entities at once

The BSI combines functions the Netherlands splits: it is both the national
cybersecurity authority (as the NCSC is, though the NCSC is not yet an
Atlas entity) and the publisher of the government information-security
baseline — the role [[NL-BIO]] fills, but with the BSI writing the baseline
itself rather than a separate body maintaining it.

**No relationship to the Dutch layer is asserted.** The structural
observation matters for the Atlas only as a warning against assuming that
equivalent functions imply equivalent institutions.

## Relationships

- `part-of` [[DE-BMI]].
- `governed-by` [[DE-BSIG]].
- Produces [[DE-IT-GRUNDSCHUTZ]].

The BSI is the best-connected German organisation in this batch after
[[DE-FITKO]], and the only one connected to legislation, a framework and a
parent ministry at once.

## Sources

Listed in frontmatter. Four of the five are BSI pages — the same circular
self-sourcing flagged on [[DE-BMI]].
