---
id: DE-BSI
type: organisation
name: Bundesamt für Sicherheit in der Informationstechnik
alternative_names:
  - BSI
  - Federal Office for Information Security
description: >
  German federal higher authority (Bundesoberbehörde) for information
  security, established 1 January 1991 by the BSI-Errichtungsgesetz and in
  the portfolio of the Federal Ministry of the Interior. Its remit is set
  by the BSI-Gesetz (in its current form since 20 August 2009): preventive
  promotion of information and cyber security, protection of federal
  government IT systems, acting as the central reporting point for IT
  security, and improving the protection of critical infrastructures.

level: national
country: DE
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 1991-01-01
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading de.wikipedia.org's dedicated BSI article directly (2026-08-28): the BSI is 'a German federal superior authority responsible for IT security' that 'reports to the Bundesministerium des Innern (Federal Ministry of the Interior)' as 'a subordinate agency within this ministry's administrative jurisdiction.' bsi.bund.de's own 'Auftrag' page, also read directly, confirms the BSI is a federal authority (Bundesamt) without itself naming the parent ministry on that specific page."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-BSIG
    source: fact
    evidence: "Confirmed by reading bsi.bund.de's own BSI-Gesetz page and Auftrag page directly (2026-08-28): the scope of the BSI's tasks is defined by the BSI-Gesetz, and under § 4 BSIG the BSI acts as the central reporting point for IT security, collecting and evaluating information on vulnerabilities and attack patterns. The BSI's own page confirms the current BSIG entered into force 20 August 2009, superseding the 1991 BSI-Errichtungsgesetz that originally created the office."
    confidence: high
    valid_from: null
    valid_until: null
  - type: produces
    target: DE-IT-GRUNDSCHUTZ
    source: fact
    evidence: "Confirmed by reading bsi.bund.de's own 'BSI-Standards' and 'IT-Grundschutz' pages directly (2026-08-28): IT-Grundschutz is the methodology developed and maintained by the BSI, set out in the BSI-Standards 200-1 to 200-4 and the IT-Grundschutz-Kompendium."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "BSI — Bundesamt für Sicherheit in der Informationstechnik"
    url: "https://www.bsi.bund.de/"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
    accessed: "2026-08-28"
  - title: "BSI — Auftrag"
    url: "https://www.bsi.bund.de/DE/Das-BSI/Auftrag/auftrag_node.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
    accessed: "2026-08-28"
  - title: "Gesetz über das Bundesamt für Sicherheit in der Informationstechnik (BSI-Gesetz — BSIG)"
    url: "https://www.bsi.bund.de/DE/Das-BSI/Auftrag/Gesetze-und-Verordnungen/BSI-Gesetz/bsi-gesetz_node.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
    accessed: "2026-08-28"
  - title: "Bundesamt für Sicherheit in der Informationstechnik"
    url: "https://de.wikipedia.org/wiki/Bundesamt_f%C3%BCr_Sicherheit_in_der_Informationstechnik"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Cybersicherheitsrecht: NIS-2-Umsetzungsgesetz ab morgen in Kraft"
    url: "https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2025/251205_NIS-2-Umsetzungsgesetz_in_Kraft.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
    accessed: "2026-08-28"
---

# Bundesamt für Sicherheit in der Informationstechnik (BSI)

> **Re-verified 2026-08-28.** All five cited pages read directly this pass
> (as part of the wider re-verification of [[DE-BSIG]] and
> [[DE-IT-GRUNDSCHUTZ]], both of which cite overlapping BSI pages).
> `verification: primary-source`; `confidence` raised to `high`; the
> founding date, previously unrecorded, is now sourced.

## Description

The BSI is a **Bundesoberbehörde** — a federal higher authority — in the
portfolio of [[DE-BMI]], confirmed directly this pass on its dedicated
Wikipedia article, which also confirms it was **established 1 January
1991** by the BSI-Errichtungsgesetz. Its current remit is set by
[[DE-BSIG]], whose own page (read directly) confirms the current BSI-Gesetz
has been in force since **20 August 2009**, superseding the 1991
establishment act.

Its stated goal, per its own site, is the preventive promotion of
information and cyber security so that information and communication
technology can be used securely across society. Concretely the sources
describe:

- **protecting federal IT systems**, including defence against viruses,
  trojans and other technical threats to federal administration computers
  and networks;
- acting as the **central reporting point for IT security** under § 4
  BSIG, collecting and evaluating information on vulnerabilities and new
  attack patterns;
- improving the protection of **critical infrastructures (KRITIS)** and
  raising network security in sectors whose failure would have severe
  consequences for the economy, the state and society;
- consumer-facing initiatives such as **IT security labelling**, confirmed
  directly this pass on the BSI's own "Auftrag" page and not previously
  recorded on this entity.

Its tasks and powers were significantly expanded by the IT-Sicherheitsgesetz
(2015) and IT-Sicherheitsgesetz 2.0 (2021), and again by
[[DE-NIS2UMSUCG]], which took the number of facilities it supervises from
roughly 4,500 to roughly 29,500 — all confirmed directly this pass on the
BSI's own press release.

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

- `part-of` [[DE-BMI]] — confirmed directly this pass, `confidence: high`.
- `governed-by` [[DE-BSIG]] — confirmed directly this pass, `confidence:
  high`.
- Produces [[DE-IT-GRUNDSCHUTZ]] — confirmed directly this pass,
  `confidence: high`.

The BSI is the best-connected German organisation in this batch after
[[DE-FITKO]], and the only one connected to legislation, a framework and a
parent ministry at once.

## Sources

Listed in frontmatter, all five read directly this pass. Four of the five
are BSI pages — the same circular self-sourcing flagged on [[DE-BMI]], now
at least confirmed by direct reading rather than search snippets, and
corroborated independently by Wikipedia on the ministry link and founding
date.
