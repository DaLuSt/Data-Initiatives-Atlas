# Spain — Index

Curated navigation hub for all Spain-scoped (`country: ES`) entities in the
Atlas. This is a human-maintained page, not a generated one — add a wikilink
here whenever a new ES-scoped entity is judged important enough to belong on
the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[ES]]

> **Sourcing caveat.** Every Spanish entity below was compiled from
> search-engine results only: the cited pages were confirmed to exist but
> were **not read**, because the working environment blocked page
> retrieval. They carry `verification: search-only` and need a
> re-verification pass against primary sources. See
> `discovery/reverification-allowlist.md`.

## Organisations

- [[ES-AEAD]] — Agencia Estatal de Administración Digital _(since Feb 2025)_
  - [[ES-SGAD]] — its predecessor _(`status: superseded`)_
- [[ES-AEPD]] — data protection authority
- [[ES-AESIA]] — **AI supervisory agency — the first in the EU**
- [[ES-INCIBE]] — cybersecurity institute _(society-facing)_
- [[ES-CCN]] — Centro Criptológico Nacional _(public sector)_
- [[ES-INE]] — national statistical office

## Legislation

- [[ES-LOPDGDD]] — Ley Orgánica 3/2018 _(implements [[EU-GDPR]]; adds a
  digital-rights title with no EU counterpart)_
- [[ES-LEY-37-2007]] — public sector information re-use, **as amended in
  2021** _(the Open Data Directive transposition)_
- [[ES-LCGC]] — NIS2 transposition _(⚠ `status: proposed` — still a draft)_

## Frameworks and standards

- [[ES-ENI]] — Esquema Nacional de Interoperabilidad _(royal decree, with
  mandatory technical norms beneath it)_
- [[ES-ENS]] — Esquema Nacional de Seguridad _(reaches suppliers, not just
  administrations)_
- [[ES-NTI-RISP]] — the re-use technical norm, carrying **DCAT-AP-ES**

## Platforms

- [[ES-DATOS-GOB-ES]] — national open data portal
- [[ES-CLAVE]] — electronic identification _(identification and signature
  kept separate)_

## Strategy

- [[ES-ESPANA-DIGITAL-2026]] — national digital roadmap

---

## EU instruments that apply in Spain

**No Spanish copy of any EU instrument exists**, and none should be created
(README §"Country-Neutral Architecture"). Each instrument below is a single
Atlas entity now carrying `applies-in` → [[ES]] alongside [[NL]], [[DE]],
[[BE]] and [[FR]]:

[[EU-GDPR]] · [[EU-NIS2]] · [[EU-CER]] · [[EU-DATA-ACT]] · [[EU-DGA]] ·
[[EU-OPEN-DATA-DIRECTIVE]] · [[EU-AI-ACT]] · [[EU-CYBERSECURITY-ACT]] ·
[[EU-EIDAS2]] · [[EU-SDG]] · [[EU-INTEROPERABLE-EUROPE-ACT]] ·
[[EU-ITS-DIRECTIVE]] · [[EU-INSPIRE]] · [[EU-EHDS]] · [[EU-EIF]] ·
[[EU-DIGITAL-DECADE]]

### The five-country picture

| EU instrument | Spain | France | Belgium | Germany | Netherlands |
|---|---|---|---|---|---|
| [[EU-GDPR]] | [[ES-LOPDGDD]] | [[FR-LIL]] | [[BE-GDPR-WET]] | [[DE-BDSG]] | [[NL-UAVG]] |
| [[EU-NIS2]] | [[ES-LCGC]] ⚠ draft | [[FR-NIS2-LOI]] ⚠ unknown | [[BE-NIS2-WET]] | [[DE-NIS2UMSUCG]] | [[NL-CBW]] |
| [[EU-OPEN-DATA-DIRECTIVE]] | **[[ES-LEY-37-2007]]** | _(not identified)_ | _(not identified)_ | [[DE-DNG]] | [[NL-WHO]] |
| [[EU-DCAT-AP]] | **[[ES-NTI-RISP]]** | _(none found)_ | [[BE-DCAT-AP-BE]] | [[DE-DCAT-AP-DE]] | [[NL-DCAT-AP-NL]] |
| [[EU-AI-ACT]] | **[[ES-AESIA]]** | _(none)_ | _(none)_ | _(none)_ | _(none)_ |
| [[EU-EIF]] | _(refused)_ | _(refused)_ | **[[BE-BELGIF]]** | _(refused)_ | _(refused)_ |
| [[EU-INSPIRE]] | _(not identified)_ | ✅ ordonnance 2010 | mapping only | [[DE-GEOZG]] | _(gap)_ |

The blanks are as informative as the entries. Every one is explained in the
entity concerned rather than left to read as absence of fact.

## What Spain added to the Atlas's understanding

- **The model is not western-European-shaped.** Spain is the first country
  outside the founding-six / Benelux-DACH group, and it required no ontology
  change either. See [[ES]].
- **A third shape for the federal gap.** Comunidades Autónomas are neither
  Länder nor Regions, and the Atlas fails on all three identically — which
  localises the defect in the `level` vocabulary rather than in any
  country's constitution. See [[ES]].
- **The first AI Act link.** [[ES-AESIA]] existed before the regulation it
  is designated under.
- **The Open Data Directive gap closes on the third attempt.** See
  [[ES-LEY-37-2007]], and note that the 2016-act trap that caught Belgium
  and France has a 2007-act equivalent here.
- **The first statistics-cluster edge**, recorded as an interpretation
  rather than a fact. See [[ES-INE]].

## Not modelled

- **The seventeen Comunidades Autónomas**, their open data portals and their
  regional data protection authorities. Blocked on the `level` gap.
- **Red.es**, the public business entity operating [[ES-DATOS-GOB-ES]] —
  cited but too thinly sourced to create, which is why that portal has no
  `maintained-by` edge.
- **The Centro Nacional de Ciberseguridad** that [[ES-LCGC]] would create.
  It does not exist yet.
- **The European Statistical System**, the entity that would let [[ES-INE]]
  and [[EU-EUROSTAT]] connect properly. Deliberately not created inside a
  country batch.
- **The Spanish organic law on AI**, and Ley 39/2015 and 40/2015 on
  electronic administration. Queued in `discovery/research-queue.md`.
