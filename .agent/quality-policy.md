# Quality Policy

The bar a change must clear before it merges, and the boundaries no
session — whoever starts it — may cross.

## Validation (must be clean before every commit)

One command runs everything CI runs, with zero errors expected:

```
python3 tools/check_all.py          # about a minute; --fast stops at the first failure
```

It rebuilds nothing you need to commit and includes, in order:

1. `python3 validation/run_all.py` — five structural checks: duplicate/
   invalid IDs, malformed or missing frontmatter fields, invalid
   controlled-vocabulary values, broken internal `[[wikilinks]]`, invalid
   relationship types/targets, missing/malformed source metadata. The
   handful of pre-existing `http://` warnings from `validate_sources.py`
   are known and not a regression signal — only new errors block a
   merge.
2. Every test suite that needs no network: the validators' own tests, the
   graph generator (including a check that the build is deterministic — two
   builds of the same data agree apart from `generated_at`, which is what
   makes not committing the generated files safe), the release tooling, the
   board sync, the LinkedIn tools, the page reader and the rest.
3. `python3 tools/update_counts.py --check` (the README and `state.yaml` numbers
   match the data; fix with `python3 tools/update_counts.py`) and
   `python3 tools/build_graph.py --check`.

`tools/build_graph.py` regenerates `site/graph.json` and `site/details.json`
from the entity files. Never hand-edit these two generated files, and never
commit them: they are gitignored and CI and the Pages deploy rebuild them.

If a change touches `site/`, also run the browser suite (`tools/test_ui.mjs`,
see `docs/graph-development.md`); CI runs it as the required `browser` check.

`.github/workflows/validate.yml` runs the same list (job `validate`) and the browser
suite (job `browser`) on every pull request and every push to `main`; a new push to a
pull request cancels the older run. See `.agent/operating-model.md`'s git workflow for
when a pull request opened by a workflow gets the check.

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
