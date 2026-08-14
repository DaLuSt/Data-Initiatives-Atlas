# Ontology

This document defines the entity model of the Data Initiatives Atlas: what
kinds of things the Atlas records, how each kind is identified, and where it
lives in the repository. It is the authoritative reference for Batch 0 and
every batch after it. If a later batch needs a concept this document does not
cover, extend this document first, then use the new concept.

The ontology is deliberately **country-neutral**: nothing here is defined in
terms of Dutch government structures. The Netherlands is the first dataset
loaded into a model designed to hold any country.

---

## 1. Entity types

Every entity in the Atlas has exactly one `type`, drawn from this controlled
vocabulary:

| Type | Meaning | Example |
|---|---|---|
| `initiative` | A named effort, project or programme-like activity that does not fit a more specific type below | `NL-COMMON-GROUND` |
| `organisation` | A body: ministry, agency, standards body, research institute, international organisation | `NL-FORUM-STANDAARDISATIE` |
| `country` | A national geographic/jurisdictional anchor node | `NL` |
| `region` | A regional geographic/jurisdictional anchor node (e.g. the EU) | `EU` |
| `policy` | A non-binding policy position or plan adopted by an organisation | |
| `law` | Primary national legislation | `NL-GDPR-UITVOERINGSWET` |
| `regulation` | A binding EU regulation (directly applicable) or national regulation | `EU-DATA-ACT` |
| `directive` | An EU directive (requires national transposition) | `EU-OPEN-DATA-DIRECTIVE` |
| `strategy` | A published strategic plan | `NL-IBDS` |
| `standard` | A technical or semantic standard | `EU-DCAT-AP` |
| `framework` | An architecture or governance framework that organises standards/policies | `NL-NORA` |
| `programme` | A funded, time-bound programme that delivers initiatives | |
| `data-space` | A federated data-sharing ecosystem for a sector | `EU-HEALTH-DATA-SPACE` |
| `platform` | A concrete technical platform or system | |
| `technology` | A named technology, protocol or technical building block referenced by other entities | |
| `domain` | A subject-matter domain used to classify other entities (Mobility, Health, ...) | `DOMAIN-MOBILITY` |
| `publication` | An independently significant document (report, study) that is not itself an initiative | |

`law`, `regulation` and `directive` are all filed under `legislation/` (see
§3). They are kept as separate `type` values because Batch 3 requires
distinguishing EU regulations, EU directives, Dutch implementation
legislation and Dutch national legislation from one another, and folding them
into a single `legislation` type would lose that distinction. Use `country`
+ `region` on the entity, and `implements` / `implements-requirement-from`
relationships (§ relationship-types.md), to express the EU → national
transposition chain — never a new `type` per country.

Do not invent a new `type` casually. If a batch believes a new type is
needed, add it here with a definition and a folder mapping (§3) in the same
commit that introduces the first entity of that type.

---

## 2. Identifiers

### 2.1 Format

```
<SCOPE>-<SLUG>
```

- `SCOPE` is one of:
  - `UN` — United Nations and UN-system bodies/initiatives
  - `EU` — European Union
  - `<ISO2>` — a national scope, using the ISO 3166-1 alpha-2 code (`NL`, `DE`, `BE`, ...)
  - `INTL` — international/global entities that are not UN-system (e.g. ISO, W3C, IETF, OECD)
  - `DOMAIN` — subject-matter domain entities (`metadata/taxonomy.md` §1),
    which are cross-cutting classification nodes rather than entities
    belonging to any one geography
- `SLUG` is an uppercase, hyphen-separated short form of the entity's name,
  stable once assigned.

Examples: `NL-IBDS`, `NL-FORUM-STANDAARDISATIE`, `EU-DATA-ACT`,
`UN-DATA-STRATEGY`, `INTL-ISO`.

The three geographic anchor entities are the exception: their `id` is just
the scope itself — `NL`, `EU`, `UN` — since they *are* the scope, not
something scoped within it.

### 2.2 Rules

1. **IDs are permanent.** Never reuse an ID, even after an entity is archived
   or superseded. A superseded entity keeps its ID and gets `status:
   superseded` plus a `successor` field pointing at the new entity's ID.
2. **One ID, one file.** No entity may be represented by more than one file.
3. **Country-neutral entities are never re-scoped per country.** `EU-DATA-ACT`
   is one entity. Do not create `NL-EU-DATA-ACT`. Applicability to a country
   is a relationship (`applies-in`), not a new entity (README §16, and see
   §5 below for the one legitimate exception: genuine national
   implementation legislation).
4. IDs are case-insensitive for comparison but written in upper case in
   frontmatter and prose. The filename is the lower-case form.

### 2.3 Filenames

A file's name is always `<id-lowercased>.md`, e.g. `id: NL-IBDS` →
`initiatives/nl-ibds.md`. This makes the mapping between a wikilink
`[[NL-IBDS]]` and its file mechanical, and lets `validation/validate_ids.py`
detect drift between an `id` field and its filename.

---

## 3. Directory structure and placement rule

```
data-initiatives-atlas/
├── initiatives/
├── legislation/        # law, regulation, directive
├── policies/
├── strategies/
├── standards/
├── frameworks/
├── programmes/
├── organisations/
├── data-spaces/
├── platforms/
├── publications/
├── domains/
├── countries/
│   └── nl/              # one sub-folder per participating country
├── regions/
│   └── eu/               # one sub-folder per participating region
├── international/
│   └── un/               # one sub-folder per international system/body treated as an anchor
├── metadata/
├── templates/
├── discovery/
├── validation/
└── progress/
```

**Placement is by `type`, not by geography.** An entity's home folder is
determined solely by its `type`, using this fixed map (also encoded
machine-readably in `metadata/schema.json` as `type_folder_map`):

| `type` | Folder |
|---|---|
| `initiative` | `initiatives/` |
| `law`, `regulation`, `directive` | `legislation/` |
| `policy` | `policies/` |
| `strategy` | `strategies/` |
| `standard` | `standards/` |
| `framework` | `frameworks/` |
| `programme` | `programmes/` |
| `organisation` | `organisations/` |
| `data-space` | `data-spaces/` |
| `platform` | `platforms/` |
| `technology` | `platforms/` (technologies are filed alongside platforms; split out a `technology/` folder only if volume later justifies it) |
| `publication` | `publications/` |
| `domain` | `domains/` |
| `country` | `countries/<iso2>/` |
| `region` | `regions/<code>/` |

A Dutch initiative and a UN initiative both live in `initiatives/`, side by
side, distinguished by their `level`, `country` and `region` metadata — never
by a parallel folder tree. This is what keeps the ontology country-neutral
and lets a new country be added without restructuring anything (README
§"Country-Neutral Architecture").

### 3.1 What `countries/`, `regions/` and `international/` are for

These folders are **not** a second copy of the entity tree. They hold two
things only, per participating geography:

1. **The anchor entity itself** — the `country` or `region` node, e.g.
   `countries/nl/nl.md` (`id: NL`, `type: country`), `regions/eu/eu.md`
   (`id: EU`, `type: region`). `international/un/un.md` holds the UN as an
   `organisation` at `level: international`, anchoring the international
   layer the same way.
2. **A curated `index.md`** per geography — a human-maintained hub page of
   wikilinks into the flat type folders, e.g. `countries/nl/index.md` lists
   the key NL-scoped initiatives, legislation, organisations, etc. This
   exists because the canonical store is plain Markdown/YAML with no live
   query engine (README §"Source of Truth"), so a geography's "table of
   contents" has to be maintained as a real page to stay navigable in
   Obsidian and on GitHub.

Do not put entity files themselves inside `countries/nl/`,
`regions/eu/` or `international/un/` beyond the anchor + index described
above.

### 3.2 Domains

`domains/` holds `domain` entities (Mobility, Health, Government, ...) used
to classify other entities via the `domains:` frontmatter field. Only create
a domain when it is actually used to connect two or more other entities
(README Batch 5: "Only create domains where they provide useful graph
relationships").

---

## 4. Geographic model

`level` (controlled vocabulary): `international`, `regional`, `national`,
`sectoral`, `local`.

- `country`: ISO 3166-1 alpha-2 code, or `null` for EU/UN/international
  entities that are not scoped to one country.
- `region`: a region code such as `EU`, used to tag an entity's regional
  scope. Never used as a substitute for `country`.

## 5. National implementation entities

Per README §"Country-Neutral Architecture", a national implementation is its
own entity **only when a genuine national implementation act, decree or
programme exists** — not merely to mirror an EU entity. When it does exist,
it gets its own `<ISO2>-...` ID and is connected back with `implements` /
`implements-requirement-from` (target: the EU entity), never by embedding
the EU entity's slug into a national ID.

---

## 6. Design decisions recorded here (Batch 0)

- Added `platforms/` and `publications/` folders, not present in the
  original README diagram, to give the `platform`/`technology` and
  `publication` types (defined in README §"What is being mapped?") a home
  without overloading `domains/` or `data-spaces/`. README.md's structure
  diagram has been updated to match.
- `law`, `regulation` and `directive` share the `legislation/` folder but
  remain distinct `type` values, required by Batch 3's EU/national
  distinction.
- Relationship provenance is carried in a `relationships:` frontmatter list
  (see `metadata/relationship-types.md`), which adds an explicit `target`
  field to the block sketched in the brief — without a target, a relationship
  entry cannot be resolved to another entity.
- Country/region/UN anchor entities use their bare scope code as `id`
  (`NL`, `EU`, `UN`) rather than a `<SCOPE>-SLUG` form, since they are the
  scope.
