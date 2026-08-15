# validation/

Two tools with different jobs.

## `run_all.py` — hard rules, fails the build

Runs the five `validate_*.py` checks: duplicate/invalid IDs, frontmatter
schema and controlled vocabularies, broken internal wikilinks, relationship
types and targets, source metadata. Wired into CI via
`.github/workflows/validate.yml`; a PR with errors will not be merged.

```
pip install -r validation/requirements.txt
python validation/run_all.py
```

## `audit.py` — analytical, advisory

Answers the questions the validation batches (6, 11, 15) ask but the hard
rules cannot: duplicates by name and alias, disconnected entities,
relationship provenance distribution, weak-source reliance, cross-level
chain census, and country-neutrality breaches. Reports findings; never fails
a build.

```
python validation/audit.py                # whole graph
python validation/audit.py --scope NL     # one layer: NL | EU | UN | INTL
```

Findings from the last run are written up in `validation/reports.md`.

## What neither tool can check

Both operate purely on repository contents. Neither can verify that a cited
URL resolves, that a source says what an entity claims, or that a `status`
is current. That requires reading primary sources — see the sourcing debt
described in `progress/current-batch.md`.
