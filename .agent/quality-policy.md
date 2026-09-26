# Quality Policy

The bar a change must clear before it merges, and the boundaries no
session — human or autonomous — may cross.

## Validation (must be clean before every commit)

Three checks, run in order, all with zero errors:

1. `python3 tools/build_graph.py` — regenerates `site/graph.json` and
   `site/details.json` from the entity files. Never hand-edit these two
   generated files.
2. `python3 validation/run_all.py` — five structural checks: duplicate/
   invalid IDs, malformed or missing frontmatter fields, invalid
   controlled-vocabulary values, broken internal `[[wikilinks]]`, invalid
   relationship types/targets, missing/malformed source metadata. The
   handful of pre-existing `http://` warnings from `validate_sources.py`
   are known and not a regression signal — only new errors block a
   merge.
3. `python3 tools/test_build_graph.py` — the unit test suite (45 tests as
   of 2026-09-26), including a check that the committed `graph.json`
   doesn't drift from the entity files that generate it.

`.github/workflows/validate.yml` runs the same three checks independently
on every human/external-token PR — see `.agent/operating-model.md`'s git
workflow for when that check does and doesn't fire.

## Quality issues validation can't catch

Structural checks don't catch: suspected duplicate entities
(`discovery/duplicates.md`), a stale claim in one entity's prose that a
sibling entity's own update has since contradicted (the recurring "stale
country anchor" bug found repeatedly across country batches — see
`discovery/unresolved.md`'s history), or a citation that no longer
resolves. Treat these as real defects at the same priority as a
validation error, per `.agent/operating-model.md`'s priority order item
5.

## Safety boundaries

Never:

- Fabricate a source, entity, date, or relationship.
- Delete large parts of the repository without being asked.
- Rewrite Git history.
- Force-push to `main`.
- Bypass the validation gate.
- Commit secrets.
- Silently discard what looks like a human's in-progress or uncommitted
  change — stash and flag it instead, per the Git Safety Protocol a
  human operator's own tooling already enforces.

When genuinely uncertain, preserve what's there and write a
`.agent/needs-human/` entry (see `.agent/operating-model.md`) rather than
guessing.
