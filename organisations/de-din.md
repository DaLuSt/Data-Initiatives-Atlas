---
id: DE-DIN
type: organisation
name: DIN Deutsches Institut für Normung
alternative_names:
  - DIN
  - German Institute for Standardisation
description: >
  National standards body of the Federal Republic of Germany, founded in
  1917 and headquartered in Berlin. By agreement with the German federal
  government it is the recognised national standards organisation
  representing German interests in European and international
  standardisation. It has been the German member of ISO since 1951 and is a
  member of CEN.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: 1917-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-ISO
  - EU-CEN
relationships:
  - type: participates-in
    target: INTL-ISO
    source: fact
    evidence: "DIN has been the ISO member body for the Federal Republic of Germany since 1951 and is listed as such by ISO (iso.org/member/1511.html; de.wikipedia.org 'Internationale Organisation für Normung'). NOT READ — search-only."
    confidence: medium
    valid_from: 1951-01-01
    valid_until: null
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "DIN became a member of the European Committee for Standardization (CEN), and as a member of ISO and CEN ensures German interests are represented in international and European standardisation processes (quality.de; telusio.com). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "DIN — DIN Deutsches Institut für Normung e.V. (ISO member body)"
    url: "https://www.iso.org/member/1511.html"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Deutsches Institut für Normung (DIN)"
    url: "https://www.quality.de/lexikon/deutsches-institut-fuer-normung/"
    publisher: "Quality.de"
  - title: "Normungsorganisationen im Vergleich: ISO, DIN und EN"
    url: "https://www.telusio.com/normungsorganisationen"
    publisher: "Telusio"
  - title: "Das ist Norm — DIN"
    url: "https://blog.dnb.de/das-ist-norm-din/"
    publisher: "Deutsche Nationalbibliothek (DNB)"
---

# DIN Deutsches Institut für Normung

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

DIN is the national standards body of the Federal Republic of Germany,
founded in **1917** and headquartered in Berlin. By agreement with the
German federal government it is the acknowledged national standards
organisation representing German interests in European and international
standardisation.

It has been the German member of [[INTL-ISO]] since **1951** and is a
member of [[EU-CEN]].

## The most valuable structural entity in the German batch

This entity earns its place less for what it says about DIN than for what
it does to the graph.

Before Germany, the Atlas had **two** international→national descents, both
noted in Batch 15 as "the template for what the UN layer lacks":

```
INTL-DCAT (W3C)            → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL
INTL-ISO-IEC-27001 / -27002 → NL-BIO
```

DIN adds a third shape — not a standards descent but an **institutional
membership chain**, and the first one in the Atlas that runs from a
national body up to both the European and the international standards
layer:

```
DE-DIN ──participates-in──> EU-CEN
       └─participates-in──> INTL-ISO
```

This matters because [[NL-NEN]] is the Dutch equivalent and the Atlas has
**never been able to record its ISO membership**. Batch 14 examined
`INTL-ISO` → `NL-NEN` and refused it for want of a source; that refusal
still stands and is unaffected by this entity. The German membership is
recorded here only because ISO's own member directory page for DIN was
returned by search, giving a citation the Dutch case never got.

The asymmetry is real and should not be tidied away: **the Atlas now
records that Germany is in ISO and does not record that the Netherlands
is**, purely because of what a search index surfaced. That is a sourcing
artefact, not a fact about the world, and it is exactly the kind of
distortion the `verification` field exists to make visible.

## Scope note

`coverage: low`. DIN publishes standards across technology, services and
management; **none of them is an Atlas entity**, and no German DIN standard
is recorded. The German standards recorded in this batch —
[[DE-XOEV]], [[DE-XRECHNUNG]], [[DE-IT-GRUNDSCHUTZ]] — come from
[[DE-KOSIT]] and [[DE-BSI]] rather than from DIN, which reflects that
public-administration IT standards in Germany are set by government bodies
rather than by the national standards institute.

DKE, the German commission for electrical standards and DIN's counterpart
towards [[EU-CENELEC]], is not modelled. Queued in
`discovery/research-queue.md`.

## Relationships

- `participates-in` [[INTL-ISO]] and [[EU-CEN]].

## Sources

Listed in frontmatter. The ISO member-directory page is the strong one;
the other three are commercial or library glossaries, and `confidence` is
capped at medium accordingly. **DIN's own site (din.de) is not cited** — no
search result returned a din.de URL, and composing one would be inventing a
URL.
