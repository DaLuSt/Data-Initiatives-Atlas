---
id: DE-GDNG
type: law
name: Gesundheitsdatennutzungsgesetz
alternative_names:
  - GDNG
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
verification: primary-source
start_date: "2024-03-26"
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading de.wikipedia.org's 'Gesundheitsdatennutzungsgesetz' article (2026-08-22): the GDNG is a German federal act ('Erlassen am: 22. März 2024, Inkrafttreten am: 26. März 2024'), and the Forschungsdatenzentrum Gesundheit nach § 303d SGB V is named directly among its datenhaltende Stellen (§ 2 Nr. 3 GDNG)."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Digitalisierung im Gesundheitswesen"
    url: "https://www.bundesregierung.de/breg-de/aktuelles/digitalisierung-im-gesundheitswesen-2447110"
    publisher: "Die Bundesregierung"
    accessed: "2026-08-22"
  - title: "Digitale Versorgung und Telematik"
    url: "https://www.vdek.com/vertragspartner/telematik.html"
    publisher: "Verband der Ersatzkassen (vdek)"
    accessed: "2026-08-22"
  - title: "Gesundheitsdatennutzungsgesetz"
    url: "https://de.wikipedia.org/wiki/Gesundheitsdatennutzungsgesetz"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
---

# Gesundheitsdatennutzungsgesetz (GDNG)

> **Verified 2026-08-22.** Egress to gesetze-im-internet.de-adjacent
> sources is no longer blocked in this environment. de.wikipedia.org's
> dedicated GDNG article was found and read directly, resolving the date
> gap flagged below.

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

## The date gap, resolved

The original two sources described the act's effects but not its date.
de.wikipedia.org's dedicated GDNG article, read 2026-08-22, gives it
directly: "Fundstellennachweis: 860-5-86. Erlassen am: 22. März 2024.
Inkrafttreten am: 26. März 2024." `start_date` is now recorded as **26
March 2024**, the date the act entered into force, rather than left null.

## What is deliberately not asserted, and why `coverage: low`

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
digitalisation, the substitute health funds' association page on digital
care and telematics, and now the dedicated Wikipedia article, which is the
best-sourced of the three for this specific act.
