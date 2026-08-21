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
| `amends` | This instrument modifies the text of another instrument, which continues to exist under its own name and date. Distinct from `supersedes`, which retires the target, and from `implements-requirement-from`, which records the EU obligation being discharged. An amending act typically carries both: `amends` the domestic act it edits, `implements-requirement-from` the directive it transposes. Added in the third research-queue batch, where three of the five Open Data Directive transpositions turned out to be amendments to pre-existing national re-use acts rather than standalone instruments |
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
| `cooperates-with` | Two organisations have entered a formal cooperation arrangement — an agreement, a partnership, a memorandum — under which neither implements, governs, contains or is aligned with the other. Symmetric: assert it once, on whichever party the source is about, not twice. Added in the candidate-clearing batch of 2026-08-21 for the UNESCO–European Commission agreement on accelerating implementation of the Recommendation on the Ethics of Artificial Intelligence, where the Commission funds UNESCO to help *other* countries implement an instrument the Commission neither adopts nor is bound by |
| `measures` | This entity assesses, scores or indexes the target — a study, index or benchmark against a country or an organisation. Directional and asymmetric: the measuring entity carries the edge, and being measured implies nothing about the target. Distinct from `applies-to`, which would make a study into a rule, and from `references`, which would suggest citation rather than assessment. Added 2026-08-21 for [[EU-DESI]] and [[EU-EGOV-BENCHMARK]], the Atlas's first `type: publication` entities |

### 2.2 Natural inverse pairs

`implements` / `implemented-by`, `supersedes` / (use `status: superseded` +
`successor` on the superseded entity rather than a separate inverse type),
`maintained-by` / `owned-by` are directional from the "subject" entity. Do
not invent ad hoc inverse types beyond what is listed here; if a batch finds
it genuinely needs one, add it to this table with a definition in the same
commit.

### 2.3 Every entity must reach its scope anchor

**Rule: every entity carries at least one provenanced relationship, in or
out.** An entity that connects to nothing is invisible in the graph, and the
Atlas exists to be a graph.

Where an entity has no substantive relationship yet — because its statutory
basis was not identified, its custodian was not named, or the obvious edge
rests on a page that was found but not read — it takes an **anchor edge** to
the scope it belongs to. Which type depends on what the entity is:

| Entity | Edge | Target |
|---|---|---|
| An instrument — `law`, `regulation`, `directive`, `policy`, `strategy`, `framework`, `standard`, `programme`, `data-space` | `applies-in` | its country |
| A body or platform **of the state** — `organisation`, `platform` | `part-of` | its country |
| A national body that is **not** part of the state (member-owned, a foundation, a private association) | `related-to` | its country |
| An EU-scoped entity | `part-of` | `EU` |
| A UN-scoped entity | `part-of` | `UN` |

These follow the two conventions the repository already had: country anchors
are reached by `applies-in`, and the [[EU]] and [[UN]] anchors by `part-of`.

Three things an anchor edge is **not**:

- **It is not a substitute for research.** It asserts scope and nothing more.
  The substantive edge is still missing, and belongs in
  `discovery/unresolved.md` until it is found.
- **It is not licence to blur a type.** `part-of` means structural
  containment. [[NL-SURF]] is a cooperative owned by its members and
  [[NL-NICTIZ]] is a foundation; neither is part of the Dutch state, so both
  take `related-to` instead. Getting this wrong would turn a filing
  convention into a false claim about ownership.
- **It is not exempt from provenance.** An anchor edge carries evidence like
  any other, and every one in this repository ends with a sentence naming
  itself as an anchor edge so it can be found and revisited.

**Domains are exempt.** `type: domain` entities are classification nodes:
they carry no factual claims, are exempt from the source requirement
(`validate_sources`), and are reached by **association** through every
entity's `domains:` list rather than by typed relationships. They are not
weakly connected — the three largest nodes in the Atlas's association layer
are `DOMAIN-GOVERNMENT` (degree 232), `DOMAIN-NATIONAL-SECURITY` (47) and
`DOMAIN-CYBERSECURITY` (35). Giving them typed edges would mean inventing a
hierarchy that does not exist.

`validate_relationships.py` enforces this rule and names the exemption.

### 2.4 Extending the vocabulary

New relationship types are added only when an existing type cannot express
the connection (README §15: "Add new relationship types only when there is
a clear semantic need"). Document the addition here, including at least one
real example, before using it in an entity file.

**Worked example — `cooperates-with`, and the two cases that were not two
cases.** `discovery/candidates.md` recorded two EU↔UN interactions the
vocabulary could not express and concluded that "two examples is the
threshold §2.3 sets for proposing a new type". Two things were wrong with
that, and both are worth recording because they are easy mistakes to repeat:

1. **The threshold is one, not two.** This section asks for "at least one
   real example". Nothing in §2.3 sets a threshold for new types at all —
   §2.3 is the anchor-edge rule.
2. **The two cases were not instances of the same missing type.** One was a
   cooperation agreement between two organisations. The other was a report
   submitted to a UN process — and that turned out not to need a
   relationship type at all, only the `publication` entity type the ontology
   had defined and nothing had used. It is now
   [[EU-VOLUNTARY-REVIEW-2023]].

So one genuine gap remained, and it is filled by `cooperates-with` on the
strength of the single well-sourced example the type was added for. A count
of unmodellable things is not the same as a count of instances of one
missing type.

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
