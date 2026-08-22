# Switzerland — Index

Curated navigation hub for all Switzerland-scoped (`country: CH`) entities
in the Atlas. This is a human-maintained page, not a generated one — add a
wikilink here whenever a new CH-scoped entity is judged important enough to
belong on the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[CH]]

> **Re-verified 2026-08-22.** Every Swiss entity below now carries
> `verification: primary-source`, and [[CH]] itself does too. **A Fedlex
> citation now exists** for both [[CH-REVDSG]] and [[CH-EMBAG]] — found
> via outbound links on official government pages — though Fedlex renders
> client-side in JavaScript, so neither could be read past retrieval. A
> genuinely new connection was found and sourced this pass:
> [[CH-OPENDATA-SWISS]] `governed-by` [[CH-EMBAG]], via the OGD office's
> own statement that it operates the portal pursuant to the Act.

## Organisations

- [[CH-DVS]] — Digitale Verwaltung Schweiz _(the Atlas's first body
  constituted jointly across **three** levels of government — and the
  clearest illustration of the missing `level: local`)_
- [[CH-EDOEB]] — federal data protection **and** information commissioner
  _(both mandates, like [[DE-BFDI]] and [[GB-ICO]])_
- [[CH-BACS]] — Bundesamt für Cybersicherheit _(a **24-hour** incident
  reporting duty since 1 April 2025, reached **without** NIS2)_
- [[CH-BFS]] — Bundesamt für Statistik _(also **operates the national open
  data portal** — unique in the Atlas)_
- [[CH-SWISSTOPO]] — federal office of topography

## Legislation

- [[CH-REVDSG]] — revised Federal Act on Data Protection, in force
  1 September 2023 _(`aligned-with` [[EU-GDPR]] — **not**
  `implements-requirement-from`)_
- [[CH-EMBAG]] — the «Digitalisierungsgesetz» _(the Atlas's **first
  statutory open-source mandate**: "Public Money – Public Code")_

## Platforms

- [[CH-OPENDATA-SWISS]] — the federal open data portal

---

## EU instruments that apply in Switzerland

**None, and unlike [[NO]] there is no mechanism by which any could.**

Switzerland is neither an EU member state nor a party to the EEA Agreement.
Its relationship with the Union runs through **bilateral agreements**. There
is no Joint Committee incorporation route and no body of assimilated Union
law as in [[GB]].

The Atlas now holds all four possible positions:

| Position | Country | How EU law reaches it |
|---|---|---|
| Member state | [[NL]], [[DE]], [[BE]], [[FR]], [[ES]], [[PL]], [[IE]] | Directly applicable, or transposed |
| Former member state | [[GB]] | Assimilated law, adequacy, extraterritorial scope |
| EEA EFTA state | [[NO]] | Incorporation by Joint Committee decision, then national implementation |
| **Neither** | **Switzerland** | **Autonomous law, plus adequacy and bilateral agreements** |

## Autonomous is not independent

[[CH-REVDSG]] replaced a 1992 act that no longer met the Union's level of
data protection. The revision was driven by the need to keep Switzerland's
**adequacy** under [[EU-GDPR]] Article 45 and to avoid competitive
disadvantage for Swiss companies exchanging data with EU ones.

So Switzerland legislates for itself, aiming at a standard it is measured
against. The pressure is commercial and diplomatic; it is not legal. That is
why the relationship type is **`aligned-with`** — a fourth answer, alongside
`implements-requirement-from`, `derived-from`, and direct applicability.

[[EU-GDPR]] still reaches Swiss businesses through **Article 3
extraterritorial scope**, but that is the Regulation applying to a
*controller*, not applying *in a country*, and the Atlas has no type that
says so.

## Not modelled

- The **EU–Switzerland adequacy decision**. The Atlas holds
  [[EU-UK-ADEQUACY]] and nothing equivalent here.
- The **bilateral agreements** and the framework agreement negotiations.
- The **twenty-six cantons** — each with its own data protection authority
  and its own administration. [[CH-EDOEB]] covers federal bodies and private
  persons only, so a single `country: CH` supervisory authority understates
  the picture by twenty-six. Swiss federalism devolves further than German.
- The **Informationssicherheitsgesetz (ISG)**, [[CH-BACS]]'s likely
  statutory basis, and the **Geoinformationsgesetz**, [[CH-SWISSTOPO]]'s.
- The **Swiss e-ID**, legislated for and not yet an Atlas entity.
- **SNV**, the Swiss national standards body.
