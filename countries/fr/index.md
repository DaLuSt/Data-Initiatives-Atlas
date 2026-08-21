# France — Index

Curated navigation hub for all France-scoped (`country: FR`) entities in
the Atlas. This is a human-maintained page, not a generated one — add a
wikilink here whenever a new FR-scoped entity is judged important enough to
belong on the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[FR]]

> **Sourcing caveat.** Every French entity below was compiled from
> search-engine results only: the cited pages were confirmed to exist but
> were **not read**, because the working environment blocked page
> retrieval. They carry `verification: search-only` and need a
> re-verification pass against primary sources. See
> `discovery/reverification-allowlist.md`.

## Organisations

- [[FR-HEALTH-DATA-HUB]] — Plateforme des données de santé _(GIP of 56 members, created 1 December 2019)_
- [[FR-DINUM]] — Direction interministérielle du numérique _(a service of the Prime Minister)_
  - [[FR-ETALAB]] — open data department _(inside DINUM)_
- [[FR-CNIL]] — data protection authority
- [[FR-ANSSI]] — national cybersecurity authority

## Legislation

- [[FR-LIL]] — Loi Informatique et Libertés, **1978**, amended for the GDPR
  in 2018 _(implements [[EU-GDPR]])_
- [[FR-LOI-VALTER]] — Loi n° 2015-1779 _(public sector information re-use;
  the reason France passed **no** Open Data Directive instrument — see the
  entity)_
- [[FR-LRN]] — Loi pour une République numérique, 2016 _(open data by
  default; **not** the Open Data Directive transposition)_
- [[FR-NIS2-LOI]] — Loi Résilience _(⚠ `status: unknown` — sources conflict)_

## Frameworks and standards

- [[FR-RGI]] — Référentiel général d'interopérabilité _(a legal obligation,
  not comply-or-explain)_

## Platforms

- [[FR-DATA-GOUV]] — national open data portal
- [[FR-FRANCECONNECT]] — identity federation _(federation, not an account)_

---

## EU instruments that apply in France

**No French copy of any EU instrument exists**, and none should be created
(README §"Country-Neutral Architecture"). Each instrument below is a single
Atlas entity now carrying `applies-in` → [[FR]] alongside [[NL]], [[DE]]
and [[BE]]:

[[EU-GDPR]] · [[EU-NIS2]] · [[EU-CER]] · [[EU-DATA-ACT]] · [[EU-DGA]] ·
[[EU-OPEN-DATA-DIRECTIVE]] · [[EU-AI-ACT]] · [[EU-CYBERSECURITY-ACT]] ·
[[EU-EIDAS2]] · [[EU-SDG]] · [[EU-INTEROPERABLE-EUROPE-ACT]] ·
[[EU-ITS-DIRECTIVE]] · [[EU-INSPIRE]] · [[EU-EHDS]] · [[EU-EIF]] ·
[[EU-DIGITAL-DECADE]]

### The four-country picture

| EU instrument | France | Belgium | Germany | Netherlands |
|---|---|---|---|---|
| [[EU-GDPR]] | [[FR-LIL]] | [[BE-GDPR-WET]] | [[DE-BDSG]] | [[NL-UAVG]] |
| [[EU-NIS2]] | [[FR-NIS2-LOI]] ⚠ | [[BE-NIS2-WET]] | [[DE-NIS2UMSUCG]] | [[NL-CBW]] |
| [[EU-DCAT-AP]] | _(none found)_ | [[BE-DCAT-AP-BE]] | [[DE-DCAT-AP-DE]] | [[NL-DCAT-AP-NL]] |
| [[EU-EIF]] | _(refused)_ | **[[BE-BELGIF]]** | _(refused)_ | _(refused)_ |
| [[EU-OPEN-DATA-DIRECTIVE]] | _(not identified)_ | _(not identified)_ | [[DE-DNG]] | [[NL-WHO]] |
| [[EU-INSPIRE]] | ✅ ordonnance 2010 | mapping only | [[DE-GEOZG]] | _(gap)_ |

The blanks are as informative as the entries. Every one is explained in the
entity concerned rather than left to read as absence of fact.

## What France added to the Atlas's understanding

- **The country-neutral model raised no new question.** France is the first
  country whose addition required no caveat about what the ontology cannot
  express — which isolates the federal `level` gap as the single real
  defect. See [[FR]].
- **A third GDPR technique.** France amended a 1978 act in place; the other
  three passed new ones. See [[FR-LIL]].
- **A fourth national DPA, still one EDPB link.** See [[FR-CNIL]].
- **INSPIRE now reaches three of four countries** and still not the
  Netherlands.

## Intelligence and security services

Added with the intelligence-services batch. France legislated the
**techniques**, not the services — which is why all four service entities
point at one instrument.

- [[FR-DGSE]] — external, Armed Forces
- [[FR-DGSI]] — internal, Interior
- [[FR-DRM]] — military intelligence collection _(⚠ `coverage: low`)_
- [[FR-DRSD]] — defence security and counter-intelligence
- [[FR-CNCTR]] — the independent authority controlling the techniques

Legislation:

- [[FR-LOI-RENSEIGNEMENT-2015]] — the law of 24 July 2015, codified as
  **Book VIII of the Code de la sécurité intérieure**. Held as one entity
  for the act and its codified form, the same treatment [[FR-LIL]] gets.

**The CNCTR gives an opinion; the Prime Minister decides.** That is the
sharpest contrast in the batch with [[NL-TIB]], whose decision is binding.
France's counterweight is judicial and after the fact: an appeal to the
Conseil d'État, which can order the **destruction of collected data**.

The *premier cercle* has **six** services. The Atlas holds four — DNRED and
TRACFIN are not modelled — so [[FR-CNCTR]]'s four `applies-to` edges
understate its remit by two.

⚠ **France's parliamentary oversight body, the délégation parlementaire au
renseignement, is not modelled.** France therefore appears here with
independent control and no parliamentary control, which is not an accurate
picture.

## Not modelled

- **INSEE**, the national statistical office — only a passing mention was
  found. Its absence means the statistics cluster stays at three unconnected
  national offices rather than four.
- **A French DCAT profile.** data.gouv.fr certainly exposes DCAT, but no
  source read establishes a named French application profile, so the DCAT
  fork stops at three countries.
- **France Identité** as its own entity; recorded in prose on
  [[FR-FRANCECONNECT]].
- **AFNOR** (national standards body), the RGS and RGAA reference
  frameworks, and the Health Data Hub. All queued in
  `discovery/research-queue.md`.
