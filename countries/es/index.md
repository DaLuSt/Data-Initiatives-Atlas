# Spain — Index

Curated navigation hub for all Spain-scoped (`country: ES`) entities in the
Atlas. This is a human-maintained page, not a generated one — add a wikilink
here whenever a new ES-scoped entity is judged important enough to belong on
the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[ES]]

> **Re-verified 2026-08-26, completed 2026-08-27.** All twenty-two Spain
> entities are now `verification: primary-source`. [[ES-ENI]] and
> [[ES-ESPANA-DIGITAL-2026]] were the last two closed, both by finding
> and reading previously-uncited pages via search rather than by
> re-fetching the sources already on file. [[ES-CLAVE]] followed the
> same route but its eIDAS-specific edge stays `confidence: low` — the
> newly-read pages confirm Spain's eIDAS node in general and that DNIe,
> not Cl@ve, is the notified scheme, but neither states the "Cl@ve is
> the integration path" claim this entity previously carried. One
> genuine correction surfaced in the first pass: [[ES-LOPDGDD]]'s
> transitory-provisions count was wrong (seven, corrected to six) until
> BOE's own preamble was read directly. A genuine, still-open source
> conflict surfaced in the second: official pages disagree with
> widely-syndicated coverage (and this entity's own prior text) on what
> [[ES-ESPANA-DIGITAL-2026]]'s two new strategic axes actually are — see
> the entity itself and `discovery/unresolved.md`.

## Organisations

- [[ES-AEAD]] — Agencia Estatal de Administración Digital _(since Feb 2025)_
  - [[ES-SGAD]] — its predecessor _(`status: superseded`)_
- [[ES-AEPD]] — data protection authority
- [[ES-AESIA]] — **AI supervisory agency — the first in the EU**
- [[ES-INCIBE]] — cybersecurity institute _(society-facing)_
- [[ES-CCN]] — Centro Criptológico Nacional _(public sector)_
- [[ES-INE]] — national statistical office
- [[ES-RED-ES]] — public business entity operating [[ES-DATOS-GOB-ES]]
  _(also the `.es` registry, RedIRIS and ONTSI)_

## Legislation

- [[ES-LOPDGDD]] — Ley Orgánica 3/2018 _(implements [[EU-GDPR]]; adds a
  digital-rights title with no EU counterpart)_
- [[ES-LEY-37-2007]] — public sector information re-use, **as amended in
  2021** _(the standing Spanish re-use regime)_
  - [[ES-RDL-24-2021]] — the omnibus decree-law whose Book Three did the
    amending _(the actual Open Data Directive transposition)_
- [[ES-LCGC]] — NIS2 transposition _(⚠ `status: proposed` — still a draft)_
- [[ES-LEY-39-2015]] — common administrative procedure _(repealed the 2007
  e-government law; added 2026-09-04)_
- [[ES-LEY-40-2015]] — public sector legal regime _(legal form behind
  [[ES-AEAD]]; added 2026-09-04)_

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
| [[EU-OPEN-DATA-DIRECTIVE]] | **[[ES-RDL-24-2021]]** | _(none — see [[FR-LOI-VALTER]])_ | **[[BE-HERGEBRUIK-WET-2023]]** | [[DE-DNG]] | [[NL-WHO]] |
| [[EU-DCAT-AP]] | **[[ES-NTI-RISP]]** | _(none — searched and not found)_ | [[BE-DCAT-AP-BE]] | [[DE-DCAT-AP-DE]] | [[NL-DCAT-AP-NL]] |
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
  and France has a 2007-act equivalent here. The third research-queue batch
  finished the job by giving the amending instrument its own node,
  [[ES-RDL-24-2021]] — the edge had been hanging off a 2007 act that could
  not have transposed a 2019 directive.
- **The first statistics-cluster edge**, recorded as an interpretation
  rather than a fact. See [[ES-INE]].

## Intelligence and security services

Added with the intelligence-services batch. **Spain is the one-service
country**: [[ES-CNI]] covers both the civilian/military and the
domestic/foreign split that every other country here divides between two or
more bodies.

- [[ES-CNI]] — integrated in the **Ministry of Defence** with functional
  autonomy and its own legal personality, reporting to the President of the
  Government.

Legislation — two acts, **same day**, 6 May 2002:

- [[ES-LEY-11-2002]] — the ordinary act creating and regulating the CNI.
- [[ES-LO-2-2002]] — the **organic** act, which does one thing: amend the
  Ley Orgánica del Poder Judicial so that CNI activities touching Articles
  18.2 and 18.3 of the Constitution need **prior judicial authorisation**.

Article 12 of the first required the second. Establishing judicial control
meant amending the judiciary's own organic law, which ordinary legislation
cannot do.

**Spain is the only country in the batch where a judge authorises in
advance.**

## [[ES-CCN]] is part of [[ES-CNI]]

The batch's most consequential Spanish finding. The Centro Criptológico
Nacional — the authority behind [[ES-ENS]], an Atlas entity since the Spain
batch — was created by Real Decreto 421/2004 *adscrito al* CNI, shares its
means and resources, and is governed by [[ES-LEY-11-2002]].

So **Spain's public-sector cyber-security authority is a component of its
intelligence service.** Only the United Kingdom is arranged the same way,
with [[GB-NCSC]] inside [[GB-GCHQ]]. [[ES-INCIBE]] sits outside that
structure entirely.

## Not modelled

- **The seventeen Comunidades Autónomas**, their open data portals and their
  regional data protection authorities. Blocked on the `level` gap.
- **The Centro Nacional de Ciberseguridad** that [[ES-LCGC]] would create.
  It does not exist yet.
- **The European Statistical System**, the entity that would let [[ES-INE]]
  and [[EU-EUROSTAT]] connect properly. Deliberately not created inside a
  country batch.
- **The Spanish organic law on AI**. Queued in
  `discovery/research-queue.md`. Ley 39/2015 and 40/2015 are now
  [[ES-LEY-39-2015]] and [[ES-LEY-40-2015]] (added 2026-09-04).
