---
id: DE-GDNG
type: act
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
rank: ordinary
confidence: medium
coverage: low
verification: primary-source
start_date: "2024-03-27"
end_date: null
last_verified: "2026-11-22"
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
    evidence: "The Federal Law Gazette text, read directly 2026-11-22 on recht.bund.de (BGBl. 2024 I Nr. 102): 'Gesetz zur verbesserten Nutzung von Gesundheitsdaten. Vom 22. März 2024', 'Ausgegeben zu Bonn am 26. März 2024'; Article 1 is the 'Gesundheitsdatennutzungsgesetz – GDNG', whose § 2 Nr. 3 names among the 'datenhaltende Stellen' 'das Forschungsdatenzentrum Gesundheit nach § 303d des Fünften Buches Sozialgesetzbuch'; Article 6(1), 'Dieses Gesetz tritt vorbehaltlich des Absatzes 2 am Tag nach der Verkündung in Kraft', so on 27 March 2024 (Article 6(2): three points of Article 3 on 31 March 2024). A German federal act; replaces an encyclopedia citation that gave 26 March 2024 as the day of entry into force (roadmap #767)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Gesetz zur verbesserten Nutzung von Gesundheitsdaten, BGBl. 2024 I Nr. 102"
    url: "https://www.recht.bund.de/bgbl/1/2024/102/VO.html"
    publisher: "Bundesgesetzblatt (Bundesministerium der Justiz und für Verbraucherschutz, recht.bund.de)"
    accessed: "2026-11-22"
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
An encyclopedia article, read 2026-08-22, gave "Erlassen am: 22. März 2024. Inkrafttreten am: 26. März 2024",
and `start_date` was set to 26 March 2024.

> **Corrected 2026-11-22.** The Federal Law Gazette itself (BGBl. 2024 I Nr. 102, read directly on
> recht.bund.de) was issued on 26 March 2024 ("Ausgegeben zu Bonn am 26. März 2024"), and Article 6(1)
> puts the Act in force "am Tag nach der Verkündung": **27 March 2024**, now the `start_date`. 26 March
> is the day of promulgation, not of entry into force. Article 6(2) brings three points of Article 3
> (amendments to SGB V) into force on 31 March 2024.

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
