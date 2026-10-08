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

Spotted a wrong claim but not sure how to fix it? Use the
[data correction form](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/new?template=data-correction.yml);
it asks for the entity ID, the claim, and the page that contradicts it.

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
9. Build the interactive graph to check it still generates:

       python tools/build_graph.py

   `site/graph.json` and `site/details.json` are generated and **not
   committed** (they are gitignored; CI and the Pages deploy rebuild them) —
   never hand-edit them. See `docs/graph-development.md`.

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
python tools/build_graph.py
python validation/run_all.py
python tools/test_build_graph.py
python tools/test_reverify.py
python tools/test_release.py
```

`run_all.py` checks: duplicate/invalid IDs, malformed or missing frontmatter
fields, invalid controlled-vocabulary values, broken internal `[[wikilinks]]`,
invalid relationship types/targets, and missing/malformed source metadata. The
test scripts cover the generator, the re-verification tool and the release
tooling. The same checks run automatically on pull requests via
`.github/workflows/validate.yml`. A PR with failing validation will not be
merged.

## Versions and releases

The Atlas has a **schema version** (in `metadata/schema.json`) and dated **data
releases** (`YYYY.MM.N`), described in `metadata/versioning.md` and listed in
`CHANGELOG.md`. Two rules for contributors:

- If your pull request changes `metadata/schema.json` (a type, level, status,
  relationship type, rank value or field), bump `schema_version` in the same
  pull request: MAJOR for a removal or rename, MINOR for an addition, PATCH for a
  clarification. CI fails a schema change without a bump. List a new optional
  field in `optional_fields` too.
- Do not edit `CHANGELOG.md` or `metadata/version.yaml`. A release pull request
  is opened automatically from the merged pull requests; the owner merges it.

## Planned work

What is planned next is tracked as GitHub issues labelled `roadmap`, shown on
the public [Atlas roadmap board](https://github.com/users/DaLuSt/projects/1);
[`docs/roadmap.md`](docs/roadmap.md) explains how it works. To take an item,
comment on its issue; to propose one, use the "Roadmap item" issue template.
Reference the issue in your pull request (`Closes #N`).

## Batch workflow

This repository is populated in scoped batches (see `progress/backlog.md`
for the older plan and `progress/current-batch.md` for the batch narrative; the
roadmap issues above are the current plan). If you're contributing as part of
a batch:

1. Keep the batch's scope tight — don't drift into the next batch's topic.
2. Validate before committing.
3. Check for duplicates against everything added so far.
4. Make one meaningful commit per batch (or per clearly separable chunk of
   a large batch), not one commit per file.
5. Record what changed and what's next, so another contributor (human or
   agent) can pick up without repeating research: open questions go in
   `discovery/unresolved.md`, and the plan lives in the roadmap issues. If you
   are a Claude Code session, also add a run-history file and update the
   snapshot in `.agent/state.yaml` (see `AGENTS.md`).

## Branches and merging

- **Trunk-based.** `main` is the only long-lived branch. Work happens on a
  short-lived branch cut from `origin/main`, named for the change
  (`claude/...` for Claude Code sessions, anything clear for a person), and
  nothing is committed to `main` directly.
- **One pull request per item, squash-merged.** The `validate` check must be
  green first. Squash keeps one commit per item, which the release notes are
  built from. Delete the branch after merging.
- **Releases are tags**, prepared by the automatic release pull request and
  never by hand; there are no release or `develop` branches.
- **Settings that back this up** (owner, *Settings → General* and *Rules*; the
  ruleset on `main` currently only blocks deletion and force-pushes, so the
  rest is convention until these are set): require a pull request before
  merging; require the `validate` status check; allow squash merging only;
  delete head branches automatically after merge.
- **Keep branches short.** If a branch has fallen behind `main`, merge `main`
  into it (no rebase of a branch someone else may have pulled).

## Claude Code sessions

Sessions started by the owner follow the operating model in `AGENTS.md` and
`.agent/`: the same branch, validate, commit and PR workflow, with the
repository as the session's memory. See `AGENTS.md` for the priority order
and safety rules, including `.agent/needs-human/` for questions a session
couldn't resolve on its own. There is no scheduled or unattended agent.

## Style

- Facts only in `description` and the "Description"/"Relationships" prose;
  interpretation goes in a clearly labelled "Atlas interpretation" section.
- Use `[[ID]]` wikilinks for every entity mentioned in prose so the
  repository stays navigable in Obsidian without additional tooling.
- Prefer official/government/EU/UN/standards-body sources over secondary
  sources (`.agent/research-policy.md` lists the preference order).
- Write in factual, neutral English regardless of the entity's home
  country.
