# Run History

One structured log entry per session/run, added going forward from
2026-09-26. History from before that date lives in `progress/completed.md`
(human-readable batch narrative) and git log — it is not backfilled here.

## Format

One YAML file per entry, named `<date>-<short-slug>.yaml`:

```yaml
date: "YYYY-MM-DD"
session: "<session identifier, if known>"
summary: >
  What this run did, in a sentence or two.
prs:
  - number: <PR number>
    title: "<PR title>"
outcome: merged | isolated-on-branch | no-op
entity_count_after: <n>
```

Add an entry as part of the same commit that updates `.agent/state.yaml`
at the end of a run (see `.agent/operating-model.md`'s git workflow, step
10). This is a log, not a task queue — `.agent/current-task.yaml` is
where an in-flight task lives; a run-history entry is written once the
run is over.
