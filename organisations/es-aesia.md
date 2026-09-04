---
id: ES-AESIA
type: organisation
name: Agencia Española de Supervisión de la Inteligencia Artificial
alternative_names:
  - AESIA
  - Spanish Agency for the Supervision of Artificial Intelligence
description: >
  Spanish public agency that applies national and European artificial
  intelligence rules through supervision, advice and training of public and
  private entities, with inspection, certification and sanctioning powers.
  Established by Real Decreto 729/2023 of 22 August 2023, whose statute was
  published on 2 September 2023, making Spain the first European Union
  member state with a body dedicated to the supervision of artificial
  intelligence — ahead of the entry into force of the EU AI Regulation. It
  acts as Spain's AI market surveillance authority and single point of
  contact, and manages the mandatory regulatory sandbox. Headquartered in
  A Coruña, beginning in-person activity on 14 February 2025.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2023-08-22
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-AI-ACT
  - ES-ESPANA-DIGITAL-2026
  - ES-LEY-40-2015
relationships:
  - type: governed-by
    target: EU-AI-ACT
    source: fact
    evidence: "Confirmed by reading boe.es's own text of Real Decreto 729/2023 directly (2026-08-26, BOE-A-2023-18911): AESIA's statute grounds it in Law 40/2015 and Law 28/2022 and positions it to assume obligations under the then-forthcoming EU AI Regulation, exercising 'functions of authority responsible for supervision, and where applicable sanction, of AI systems'. protecciondata.es, also read directly, confirms AESIA now operates 'como autoridad de vigilancia del mercado' under Regulation (EU) 2019/1020 and is governed by Regulation (EU) 2024/1689. lamoncloa.gob.es's press release, also read directly, gives no legal citation but confirms AESIA develops functions assigned by the EU AI Regulation and coordinates with European authorities."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: ES-LEY-40-2015
    source: fact
    evidence: "A research-queue pickup (2026-09-04) followed up the 'Law 40/2015' mention this file's own EU-AI-ACT evidence string already carried but had not turned into an edge. Reading Real Decreto 729/2023 directly: Article 1.1 states 'La Agencia Española de Supervisión de Inteligencia Artificial es una entidad de derecho público regulada en los artículos 108 bis a 108 sexies de la Ley 40/2015' (AESIA is a public-law entity regulated under articles 108 bis to 108 sexies of Ley 40/2015), and Article 3.1 adds 'La Agencia se rige por la Ley 40/2015, de 1 de octubre' (the Agency is governed by Ley 40/2015). This is the same 'agencia estatal' legal form [[ES-AEAD]] carries, though cited by article range here rather than by the section number RD 1118/2024 used for AEAD — both point to the same Título II, Capítulo III, Sección 4.ª of the law."
    confidence: high
    valid_from: 2023-09-03
    valid_until: null

sources:
  - title: "Real Decreto 729/2023, de 22 de agosto, por el que se aprueba el Estatuto de la Agencia Española de Supervisión de Inteligencia Artificial"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2023-18911"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
  - title: "AESIA | España Digital 2026"
    url: "http://espanadigital.gob.es/en/measure/aesia"
    publisher: "España Digital 2026"
  - title: "Escrivá: «La Agencia Española de Supervisión de la Inteligencia Artificial es pionera en Europa»"
    url: "https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/transformacion-digital-y-funcion-publica/paginas/2024/190624-escriva-aesia-ia.aspx"
    publisher: "La Moncloa — Gobierno de España"
    accessed: "2026-08-26"
  - title: "Presentación AESIA — A Coruña"
    url: "https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/transformacion-digital-y-funcion-publica/Documents/2024/190624-Presentaci%C3%B3n-AESIA-Coru%C3%B1a.pdf"
    publisher: "La Moncloa — Gobierno de España"
  - title: "Agencia Española de Supervisión de la Inteligencia Artificial (AESIA)"
    url: "https://protecciondata.es/agencia-espanola-supervision-inteligencia-artificial-aesia/"
    publisher: "Protección Data"
    accessed: "2026-08-26"
  - title: "Aprobado el Estatuto de la Agencia Española de Supervisión de la Inteligencia Artificial (AESIA)"
    url: "https://www.juntadeandalucia.es/datosabiertos/portal/actualidad/detalle/1636"
    publisher: "Junta de Andalucía — Portal de datos abiertos"
---

# AESIA — Agencia Española de Supervisión de la Inteligencia Artificial

> **Verified 2026-08-26; second legal basis added 2026-09-04.** boe.es's
> own text of Real Decreto 729/2023 (BOE-A-2023-18911) was read directly,
> along with protecciondata.es and the lamoncloa.gob.es press release —
> closing the previous gap where the statute's own BOE identifier had not
> been found. A research-queue pickup then turned this file's own passing
> "grounds it in Law 40/2015" line into a sourced `governed-by` edge, once
> [[ES-LEY-40-2015]] became an Atlas entity.

## Description

AESIA applies national and European AI rules through supervision, advice and
training of public and private entities, and holds **inspection,
certification and sanctioning** powers. Its stated mission is to foster an
environment of trust in which technological progress respects fundamental
rights, privacy, equal treatment and democratic values.

Under [[EU-AI-ACT]] it is Spain's:

- **market surveillance authority** for AI systems,
- **single point of contact**, and
- manager of the mandatory **regulatory sandbox**.

It is based in **A Coruña** — not Madrid — and began in-person activity on
14 February 2025, occupying Casa Veeduría while the permanent building is
refurbished.

## Spain got there before the regulation did

With AESIA's creation Spain became **the first European Union member state
with a body dedicated to supervising artificial intelligence**, ahead of the
entry into force of the EU AI Regulation. The statute was approved on
**22 August 2023** and published on **2 September 2023** — the AI Act was
still in trilogue. Confirmed by reading boe.es directly: Real Decreto
729/2023 entered into force on **3 September 2023**, and its President —
the Secretary of State for Digitalisation and AI — is designated to
"participate in activities and meetings of the AIDA [the EU AI Board] as
common representative of the Spanish State," a forward-looking role
written into the statute before that Board itself existed.

That ordering is the reason this entity matters to the Atlas rather than
just to Spain. Every other national body modelled here was created to
implement something that already existed. AESIA was created first and
*then* designated under Article 70 of a regulation that had not yet been
adopted.

The Atlas records this as a `governed-by` relationship, not `implements` or
`implements-requirement-from`:

- `implements-requirement-from` is reserved for **national legal
  instruments** transposing higher-level obligations
  (`metadata/relationship-types.md` §2.1). AESIA is an organisation, not an
  instrument.
- The sources say AESIA *se rige por* — is governed by — Regulation (EU)
  2024/1689, which is the definition of `governed-by`.

**The temporal oddity is not modelled, and cannot be.** The relationship
carries `valid_from: null` because no source read gives a date on which the
designation took effect, and the schema has no way to say "this body
predates the instrument that governs it". That is recorded here in prose
rather than forced into a field.

## The first national link to the AI Act

[[EU-AI-ACT]] has been in the Atlas since Batch 8 with `applies-in`
relationships and no national implementing body of any kind. Four countries
were added without one:

| Country | AI supervisory body in the Atlas |
|---|---|
| Netherlands | none identified |
| Germany | none identified |
| Belgium | none identified |
| France | none identified |
| **Spain** | **AESIA** |

The asymmetry is real rather than an artefact. Spain genuinely was first;
the other four designations, wherever they now stand, were not found in
search results during their batches and were not invented.

## Not modelled

The Spanish **organic law on artificial intelligence** has advanced since
this file first queued it: reading `lamoncloa.gob.es`'s own Council of
Ministers press release directly (2026-09-04) confirms the Proyecto de
Ley Orgánica para el buen uso y la gobernanza de la Inteligencia
Artificial was approved for submission to Congress on **26 May 2026**,
and secondary legal reporting places it at Congress under **BOCG Serie
A, No. 97-1** (published 12 June 2026), still in parliamentary process
as an organic law requiring an absolute majority.

**Still no entity was created**, and the reason has sharpened rather
than resolved: `lamoncloa.gob.es`'s own release names AESIA as "the
central body," while separate legal-sector reporting on the bill's
Congress text describes a **General Directorate of Artificial
Intelligence** as the notifying authority under the EU AI Regulation
and **eight** state-level market surveillance authorities — a
materially different picture of who holds authority, from sources this
pass did not reconcile by reading the bill's own BOCG text. This is the
same shape of contradiction the Atlas already declined to resolve on
[[FR-NIS2-LOI]] rather than force. Queued in
`discovery/research-queue.md` with the sharper detail carried forward.

## The same legal form as AEAD

Reading Real Decreto 729/2023 directly finds AESIA is, like [[ES-AEAD]],
an **agencia estatal** under [[ES-LEY-40-2015]] — Article 1.1 places it
under "los artículos 108 bis a 108 sexies" of that law, and Article 3.1
states plainly "La Agencia se rige por la Ley 40/2015." Two of the
Atlas's national AI links now share the same domestic legal chassis:
AESIA is governed both by the EU instrument it supervises compliance
with, and by the Spanish statute defining what kind of body it is.

## Relationships

- `governed-by` [[EU-AI-ACT]].
- `governed-by` [[ES-LEY-40-2015]] — closed 2026-09-04.

## Sources

Listed in frontmatter. Three of six read directly in the 2026-08-26 pass:
BOE's own text of Real Decreto 729/2023 (BOE-A-2023-18911, closing the
previously-flagged missing-citation gap), protecciondata.es, and the La
Moncloa press release. Real Decreto 729/2023's Articles 1.1 and 3.1 were
read again in the 2026-09-04 pass that closed the Ley 40/2015 gap.
