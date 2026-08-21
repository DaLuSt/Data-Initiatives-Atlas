---
id: DE-GDNG
type: law
name: Gesundheitsdatennutzungsgesetz
alternative_names:
  - GDNG
  - Health Data Use Act
description: >
  German federal act on the use of health data. It is one of the instruments
  of the federal government's health-digitalisation package alongside the
  Digitale-Versorgung-und-Pflege-Modernisierungs-Gesetz, and provides for the
  Forschungsdatenzentrum Gesundheit, which receives pseudonymised data from
  the elektronische Patientenakte and links it with billing data where that
  is provided.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
organisations: []
related_entities:
  - DE
  - DE-GEMATIK
  - EU-EHDS
relationships:
  - type: applies-in
    target: DE
    source: fact
    evidence: "The Gesundheitsdatennutzungsgesetz (GDNG) is the German health data utilisation law; the Forschungsdatenzentrum Gesundheit receives pseudonymised data from the elektronische Patientenakte and links it with billing data where provided; the Digital-Versorgung-und-Pflege-Modernisierungs-Gesetz (DVPMG) is one of the key legislative instruments for digital modernisation of care and nursing (bundesregierung.de 'Digitalisierung im Gesundheitswesen'; vdek.com 'Digitale Versorgung und Telematik'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Digitalisierung im Gesundheitswesen"
    url: "https://www.bundesregierung.de/breg-de/aktuelles/digitalisierung-im-gesundheitswesen-2447110"
    publisher: "Die Bundesregierung"
  - title: "Digitale Versorgung und Telematik"
    url: "https://www.vdek.com/vertragspartner/telematik.html"
    publisher: "Verband der Ersatzkassen (vdek)"
---

# Gesundheitsdatennutzungsgesetz (GDNG)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

The German federal act on the **use of health data**. Its most consequential
provision for this Atlas is the **Forschungsdatenzentrum Gesundheit** — the
health research data centre — which receives **pseudonymised data from the
elektronische Patientenakte** and links it with billing data where that is
provided.

That is a secondary-use regime: data collected for treatment, made available
for research under statutory conditions. It is the same problem
[[FI-SECONDARY-USE-ACT]] solves in Finland and [[FR-SNDS]] in France, and it
is what [[EU-EHDS]] is being built to harmonise.

## What is deliberately not asserted, and why `coverage: low`

**No date.** The sources describe the act and its effects and none of them
gives its date of adoption or entry into force. A German federal act's date
is a citable fact and guessing it would be exactly the kind of
plausible-looking error the Atlas's sourcing rules exist to prevent, so
`start_date` is `null`.

**No `implements-requirement-from` edge to [[EU-EHDS]].** The German act and
the European regulation address the same subject and no source in this set
says the first implements the second — and the sequence makes it unlikely in
that direction. Recorded as an open question in prose rather than asserted.

**No entity for the Forschungsdatenzentrum Gesundheit**, nor for the
DVPMG. Both are named here and neither was researched; creating them from a
single passing mention is the thin encyclopedic entity the taxonomy threshold
prevents.

## Relationships

- `applies-in` [[DE]] — anchor edge.

## Sources

Listed in frontmatter — the federal government's overview of health-system
digitalisation and the substitute health funds' association page on digital
care and telematics.
