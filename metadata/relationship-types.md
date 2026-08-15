# Relationship Model

Relationships are first-class information in the Atlas (README §13). This
document defines the controlled relationship vocabulary, how relationships
are recorded with provenance, and how facts are kept separate from Atlas
interpretation.

---

## 1. Two ways to record a connection

### 1.1 `related_entities:` / `organisations:` — lightweight references

Plain frontmatter lists of entity IDs:

```yaml
organisations:
  - NL-FORUM-STANDAARDISATIE
related_entities:
  - NL-NORA
```

Use these for straightforward, low-stakes associations where provenance
doesn't need to be argued — e.g. "this standard is maintained by this
organisation" when that fact is stated on the entity's own page with a
source. They imply an unqualified `related-to`-strength connection in the
direction of the list owner.

### 1.2 `relationships:` — provenanced relationships

Use this whenever the *type* of connection matters (implements, supersedes,
governed-by, ...) or the relationship itself needs to be traceable to
evidence:

```yaml
relationships:
  - type: implements-requirement-from
    target: EU-DATA-ACT
    source: fact                # "fact" | "interpretation"
    evidence: "Explanatory memorandum, Kamerstuk XX-XX, section 2"
    confidence: high
    valid_from: 2024-09-24
    valid_until: null
  - type: related-to
    target: NL-FEDERATIEF-DATASTELSEL
    source: interpretation
    evidence: "Both concern federated public-sector data exchange; no single authoritative source states this link directly"
    confidence: medium
    valid_from: null
    valid_until: null
```

Field reference:

| Field | Required | Meaning |
|---|---|---|
| `type` | yes | One value from §2 below |
| `target` | yes | The `id` of the other entity |
| `source` | yes | `fact` if directly stated by an authoritative source, `interpretation` if derived by the Atlas (§3) |
| `evidence` | yes if `source: fact` | Citation (section, page, or matching entry in that entity's `sources:` list) or, for interpretation, a one-line rationale |
| `confidence` | yes | `high`, `medium`, `low` — confidence in the relationship itself, independent of the entity's own `confidence` field |
| `valid_from` / `valid_until` | no | ISO date, when the relationship is time-bounded (e.g. an `applies-in` relationship that ends when a regulation is repealed for that country) |

Relationships are recorded on the entity where they are most naturally
authored (usually the "downstream" entity, e.g. the national law records
`implements-requirement-from` pointing at the EU regulation) and should not
be duplicated in reverse on the target unless the reverse direction is
independently useful for navigation — in that case use the paired inverse
type from §2.2.

---

## 2. Controlled relationship types

### 2.1 Vocabulary

| Type | Meaning |
|---|---|
| `related-to` | General association, no stronger semantics apply |
| `influences` | One entity shapes another without a formal dependency |
| `implements` | One entity carries out or operationalises another (e.g. a programme implements a strategy) |
| `implemented-by` | Inverse of `implements` |
| `depends-on` | One entity requires another to function or be meaningful |
| `derived-from` | One entity was produced by adapting another |
| `based-on` | One entity's design follows another's, more loosely than `derived-from` |
| `references` | One entity cites another without a structural dependency |
| `supersedes` | This entity has formally replaced another (see also `status: superseded` + `successor` on the old entity) |
| `replaces` | Synonym of `supersedes`, used when "replace" is the natural English for the domain (e.g. a platform replacing another) |
| `proposes-to-supersede` | A **pending** instrument (typically `status: proposed`) that would supersede or repeal the target *if adopted*. Distinct from `supersedes`, which asserts that supersession has actually happened. Use this so that proposals are visible in the graph without falsely retiring the instruments they target — the target keeps `status: active` until adoption is sourced. Added in Batch 8 for the EU Digital Omnibus proposal, which would repeal the Data Governance Act and the Open Data Directive |
| `part-of` | Structural containment (a program is part of a strategy; a domain is part of a broader domain) |
| `governed-by` | This entity's operation is governed by the target (usually an organisation or framework) |
| `applies-to` | A rule, standard or framework applies to a class of entities |
| `applies-in` | A regulation, standard or initiative is applicable within a given country/region (the primary mechanism for country-neutral applicability, README §16) |
| `produces` | An organisation or programme produces the target (e.g. a standard) |
| `maintained-by` | The target organisation maintains this entity |
| `owned-by` | The target organisation owns/is accountable for this entity |
| `participates-in` | An organisation or country participates in a programme, data space or initiative |
| `aligned-with` | Two entities are deliberately kept consistent without one implementing the other |
| `implements-requirement-from` | A national legal instrument transposes/implements obligations from an EU (or other higher-level) legal instrument — the specific case of `implements` used for the EU→national legislative chain (README §"Cross-Border Relationships" and Batch 3) |

### 2.2 Natural inverse pairs

`implements` / `implemented-by`, `supersedes` / (use `status: superseded` +
`successor` on the superseded entity rather than a separate inverse type),
`maintained-by` / `owned-by` are directional from the "subject" entity. Do
not invent ad hoc inverse types beyond what is listed here; if a batch finds
it genuinely needs one, add it to this table with a definition in the same
commit.

### 2.3 Extending the vocabulary

New relationship types are added only when an existing type cannot express
the connection (README §15: "Add new relationship types only when there is
a clear semantic need"). Document the addition here, including at least one
real example, before using it in an entity file.

---

## 3. Facts vs. Atlas interpretation

- **Fact**: a directly sourced statement — "the initiative is maintained by
  Organisation X" — with a citation in `evidence` pointing at an
  authoritative source.
- **Atlas interpretation**: a relationship or classification the Atlas
  derives by analysis and that is not directly stated anywhere — "these two
  initiatives are both about federated data governance." Mark these
  `source: interpretation` and give a one-line `evidence` rationale.

Never present an interpretation as a fact. When in doubt, use
`source: interpretation` and `confidence: low` or `medium`, and record the
uncertainty in `discovery/unresolved.md` if it needs a second look.

---

## 4. Obsidian navigability

Every relationship recorded in `relationships:`, `organisations:` or
`related_entities:` should also be reachable from the entity's prose body via
a `[[TARGET-ID]]` wikilink at least once, so the graph stays browsable
directly in Obsidian/GitHub without tooling. `validation/validate_links.py`
checks that wikilinks resolve to a real ID, but does not currently enforce
that every frontmatter relationship has a matching wikilink — treat that as
a house style, not (yet) a hard validation rule.
