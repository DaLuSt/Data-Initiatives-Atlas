# Taxonomy

Where `metadata/ontology.md` defines *what kinds of entities exist*, this
document defines the *classification schemes* used to tag and group those
entities: domains and the legislation classification. Taxonomy values are
applied through frontmatter fields (`domains:`, and the `type` +
country/region combination for legislation) — they are not entity types in
their own right, except `domain`, which is both a taxonomy value and an
entity (see §1.2).

---

## 1. Domains

### 1.1 Purpose

`domains:` on any entity is a list of `domain` entity IDs that says "this
entity is relevant to these subject-matter areas." Domains are the
cross-cutting axis of the graph: they let you ask "what connects to
Mobility?" regardless of type, level or country.

### 1.2 Domains are entities

Each domain is itself a `domain`-typed entity living in `domains/`, with its
own ID of the form `DOMAIN-<SLUG>`, e.g. `DOMAIN-MOBILITY`. This lets a
domain carry a description and its own sources, and lets other entities
reference it with an ordinary relationship (`related-to`, `part-of`) in
addition to the `domains:` shorthand list.

### 1.3 Starting domain list

The following domains are anticipated by README/Batch 5. None of them are
created in Batch 0 — this list exists so later batches use a consistent slug
instead of inventing near-duplicates (`DOMAIN-HEALTH` vs `DOMAIN-HEALTHCARE`,
etc.). Create the `domain` entity file the first time a batch actually needs
to link something to it (README §5: "Only create domains where they provide
useful graph relationships").

| Slug | Domain |
|---|---|
| `DOMAIN-GOVERNMENT` | Government |
| `DOMAIN-MOBILITY` | Mobility |
| `DOMAIN-HEALTH` | Health |
| `DOMAIN-FINANCE` | Finance |
| `DOMAIN-GEOSPATIAL` | Geospatial |
| `DOMAIN-CYBERSECURITY` | Cybersecurity |
| `DOMAIN-ENVIRONMENT` | Environment |
| `DOMAIN-ENERGY` | Energy |
| `DOMAIN-EDUCATION` | Education |
| `DOMAIN-JUSTICE` | Justice |
| `DOMAIN-PUBLIC-SAFETY` | Public Safety |
| `DOMAIN-ECONOMY` | Economy |
| `DOMAIN-AGRICULTURE` | Agriculture |
| `DOMAIN-SOCIAL-SECURITY` | Social Security |
| `DOMAIN-RESEARCH` | Research |
| `DOMAIN-INFRASTRUCTURE` | Infrastructure |

This list is not closed. Add a row here (with slug) in the same commit that
first creates the domain entity, so the table always reflects what exists.

---

## 2. Legislation classification

Batch 3 requires clearly distinguishing several kinds of legally/normatively
binding text. This is expressed with **two orthogonal fields**, not a single
flat category:

1. `type` — `law`, `regulation`, `directive` (from the ontology's entity
   type vocabulary), or, for non-binding instruments, `policy`,
   `framework`, `standard`.
2. `level` + `country`/`region` — where it comes from and applies.

Combined, this reproduces the exact classification the brief asks for:

| Classification | `type` | `level` | `country` | `region` | Notes |
|---|---|---|---|---|---|
| EU legislation (regulation) | `regulation` | `regional` | `null` | `EU` | Directly applicable in all member states; use `applies-in` per country |
| EU legislation (directive) | `directive` | `regional` | `null` | `EU` | Requires national transposition; the transposing act is a separate `law` entity linked with `implements-requirement-from` |
| Dutch implementation legislation | `law` | `national` | `NL` | `EU` | The `region` field records which EU instrument's obligations it transposes; also set an explicit `implements-requirement-from` relationship to that EU entity |
| Dutch national legislation | `law` | `national` | `NL` | `null` | No EU origin |
| Policy | `policy` | any | as applicable | as applicable | Non-binding |
| Guideline | `standard` or `framework` | any | as applicable | as applicable | Use `standard` for a technical/normative guideline, `framework` for a broader governance guideline |
| Standard | `standard` | any | as applicable | as applicable | |
| Framework | `framework` | any | as applicable | as applicable | |

Do not classify every EU digital regulation as a data initiative by default
— Batch 8 explicitly requires assessing relevance before adding an entity.

---

## 3. Extending the taxonomy

Both the domain list and the legislation classification table are living
documents. When a later batch needs a new domain or finds a legislative
instrument that does not fit the table above, update this file in the same
commit, with a one-line rationale, rather than silently improvising a new
value.
