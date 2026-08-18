# Contributing to Data Initiatives Atlas

Thank you for helping build a connected, evidence-based knowledge graph of
data/digital/governance initiatives. This guide covers how to add and change
entities. Read `metadata/ontology.md`, `metadata/taxonomy.md`,
`metadata/relationship-types.md` and `metadata/metadata-schema.md` first —
this document assumes them.

By taking part you agree to the [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
Two things it says that matter especially here: characterise other countries'
laws and institutions **neutrally**, and treat **fabricated sources or
evidence** as a conduct violation rather than a content slip.

Found a security problem, or a citation that does not support the claim
attached to it? [`SECURITY.md`](SECURITY.md) says where each goes —
vulnerabilities privately, data-integrity problems in a public issue.

## Before you start

1. **Search first.** Check `initiatives/`, `organisations/`, etc. (by name
   and by `alternative_names`) and `discovery/duplicates.md` for anything
   that might already represent what you're about to add.
2. **Don't overwrite existing work.** If a relevant entity already exists,
   improve it — add a source, tighten a relationship, correct a status —
   rather than creating a near-duplicate.
3. **Only add what you can source.** No entity, fact or relationship should
   be invented to fill a gap. If you can't verify something, put it in
   `discovery/unresolved.md` or `discovery/candidates.md` instead of
   guessing.

## Adding a new entity

1. Pick the correct `type` (`metadata/ontology.md` §1).
2. Mint an ID following `metadata/ontology.md` §2. Check it isn't already
   used anywhere in the repo.
3. Copy `templates/entity-template.md` into the folder that `type` maps to
   (`metadata/ontology.md` §3), named `<id-lowercased>.md`.
4. Fill in the frontmatter. Leave fields `null`/empty rather than guessing.
   Every factual claim needs a `sources:` entry with a real URL.
5. Write the body: Description, Relationships (with wikilinks), and an
   "Atlas interpretation" section only if there genuinely is Atlas-derived
   interpretation to record, kept visibly separate from sourced fact.
6. Wire up relationships both ways where useful: add this entity's ID to
   any related entity's `related_entities:`/`organisations:` list or add a
   provenanced entry to its `relationships:` list, and vice versa.
6a. **Make sure it connects to something.** Every entity must carry at
   least one provenanced relationship, in or out — `validate_relationships`
   fails the build otherwise. If you cannot yet source a substantive edge,
   give it an **anchor edge** to its scope (`metadata/relationship-types.md`
   §2.3): `applies-in` its country for an instrument, `part-of` its country
   for a state body or public platform, `part-of` `EU`/`UN` for an
   EU- or UN-scoped entity — and `related-to` rather than `part-of` for a
   national body that is not part of the state. An anchor edge asserts scope
   and nothing more; log the missing substantive edge in
   `discovery/unresolved.md`. `type: domain` entities are exempt.
7. If this entity is NL/EU/UN-scoped, and is important enough to belong on
   that geography's hub page, add a wikilink to `countries/nl/index.md`,
   `regions/eu/index.md` or `international/un/index.md`.
8. Run the validation suite (below) and fix anything it flags.
9. Regenerate the interactive graph and commit the result:

       python tools/build_graph.py

   `site/graph.json` and `site/details.json` are generated — never hand-edit
   them. See `docs/graph-development.md`.

## Changing an existing entity

- Update `last_verified` when you re-confirm sourced facts.
- If something is superseded, don't delete it: set `status: superseded`,
  set `successor:` to the new entity's ID, and set `previous_version:` on
  the new entity pointing back.
- Never change an `id` once an entity has been committed. If an ID was
  minted wrong, add a note to `discovery/unresolved.md` rather than
  silently renaming — renames break every inbound wikilink and relationship.

## Relationship provenance

Use the lightweight `related_entities:`/`organisations:` lists for
straightforward associations, and the provenanced `relationships:` list
whenever the type of connection or its evidence matters — see
`metadata/relationship-types.md` §1. Never present Atlas interpretation as
fact (`source: interpretation` must be used honestly).

**An anchor edge still needs provenance.** It is a real relationship with
real evidence, not a placeholder — every anchor edge in this repository ends
its evidence with a sentence naming itself as one, so they can be found and
revisited when the substantive edge turns up. Do not use an anchor edge to
make a claim the sources do not support: `part-of` means structural
containment, so a member-owned cooperative or a foundation takes
`related-to` instead.

## Validation

```
pip install -r validation/requirements.txt
python validation/run_all.py
```

This checks: duplicate/invalid IDs, malformed or missing frontmatter fields,
invalid controlled-vocabulary values, broken internal `[[wikilinks]]`,
invalid relationship types/targets, and missing/malformed source metadata.
The same suite runs automatically on pull requests via
`.github/workflows/validate.yml`. A PR with failing validation will not be
merged.

## Batch workflow

This repository is populated in scoped batches (see `progress/backlog.md`
for the plan and `progress/current-batch.md` for what's active). If you're
contributing as part of a batch:

1. Keep the batch's scope tight — don't drift into the next batch's topic.
2. Validate before committing.
3. Check for duplicates against everything added so far.
4. Make one meaningful commit per batch (or per clearly separable chunk of
   a large batch), not one commit per file.
5. Update `progress/completed.md`, `progress/current-batch.md` and
   `progress/backlog.md` to reflect what changed and what's next, so another
   contributor (human or agent) can pick up without repeating research.

## Style

- Facts only in `description` and the "Description"/"Relationships" prose;
  interpretation goes in a clearly labelled "Atlas interpretation" section.
- Use `[[ID]]` wikilinks for every entity mentioned in prose so the
  repository stays navigable in Obsidian without additional tooling.
- Prefer official/government/EU/UN/standards-body sources over secondary
  sources (README §12 lists the preference order).
- Write in factual, neutral English regardless of the entity's home
  country.
