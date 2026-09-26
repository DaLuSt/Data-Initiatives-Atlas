# Operating Model

How an autonomous (or human-driven) session picks work, does it, and gets
it merged. See `.agent/mission.md` for why, `.agent/research-policy.md`
for the sourcing rules that apply while doing it, and
`.agent/quality-policy.md` for the bar a change must clear before it
merges.

## Start here, every session

1. Read `.agent/state.yaml` — the authoritative live snapshot (entity
   count, last merged work, open-item counts).
2. Read `.agent/current-task.yaml` — if it names an in-flight task,
   resume it before starting anything new.
3. If idle, pick the next item using the priority order below.

`progress/current-batch.md` and `progress/completed.md` remain the
human-readable historical narrative of past batches, but as of
2026-09-26 they are no longer where "current status" is authoritative —
that's `.agent/state.yaml` and `.agent/current-task.yaml` now. Keep
writing narrative detail to `progress/completed.md` when a batch
finishes; update the two YAML files for anything a future session needs
to check quickly.

## Priority order for autonomous work

1. **Finish incomplete work.** Check `.agent/current-task.yaml`. If a
   previous session left something mid-flight, continue it before
   starting anything new.
2. **Close `discovery/unresolved.md` rows.** This is almost always where
   the highest-value work is: an open, specific, falsifiable question
   about an existing entity. Read a row, research it with primary
   sources, either close it (edit the entity, remove the row) or narrow
   it (record what's now known, what still isn't). See
   `.agent/research-policy.md` before writing anything.
3. **Work `discovery/candidates.md` / `discovery/research-queue.md`.**
   Turn a scoped lead into a real, sourced entity, or fold it into an
   existing one. If both files say "nothing queued" (check before
   assuming there's nothing to do — they are sometimes fully empty,
   which is a legitimate state, not a bug), move on to graph completion.
4. **Graph completion.** Existing entities with missing relationships,
   thin sourcing, or an obvious connection to something researched this
   session. Improve what exists before adding isolated new nodes.
5. **Quality.** Duplicates (`discovery/duplicates.md`), broken links,
   inconsistent frontmatter, stale generated files, contradictions
   between sibling entities. `validation/run_all.py` catches structural
   issues automatically; this priority is for the things it can't check.
6. **New discovery.** Only once the above is genuinely exhausted, go
   looking for new candidates and add them to `discovery/candidates.md`
   — don't turn every new lead straight into a fully-researched entity
   in the same pass unless it's small.

Do not ask a human which of these to do next when the repository already
answers the question. Pick the highest-priority item with real available
work and do it.

## Git workflow

This repository already has a working, PR-based flow — use it exactly,
do not push directly to `main`:

1. `git fetch origin main` (and the shared working branch if one already
   exists remotely — see "Stale shared branches" below).
2. Branch off `origin/main`.
3. Make the change (usually: edit/create entity files, edit
   `discovery/unresolved.md`, regenerate
   `site/graph.json`/`site/details.json` via `tools/build_graph.py`).
4. Validate locally — see `.agent/quality-policy.md`'s three checks. All
   three must be clean before committing.
5. Commit with a clear message describing the actual change, ending with:
   ```
   Co-Authored-By: Claude <noreply@anthropic.com>
   ```
6. Push the branch, open a PR against `main` describing what changed and
   why, with a short test-plan checklist.
7. **Check for real, independent CI before merging — but know when it
   won't appear.** `.github/workflows/validate.yml` runs the same three
   checks independently on every PR, and when a PR was opened by a human
   or by a session authenticated as a normal user/OAuth app (not a
   GitHub Actions job token), that check genuinely fires — wait for it
   (`get_check_runs`, not `get_status`, which does not see Actions
   results) and require it green before merging.
   **Exception, and it matters:** if this session is itself running
   inside a GitHub Actions job (the scheduled `autonomous-agent.yml`
   workflow) and used that job's own `GITHUB_TOKEN` to push/open the PR,
   GitHub's recursion-prevention rule means `validate.yml` will **not**
   fire on that PR at all — don't wait for a check that will never
   appear. In that specific case, step 4's local validation (identical
   checks, run directly) is the authoritative gate instead.
8. **If the gate (real CI, or local validation when CI can't fire per
   above) passes: squash-merge.** If it fails: do not force-merge. Fix
   and re-push once. If it fails again, or the failure isn't something
   you can safely diagnose, stop and write a `.agent/needs-human/` entry
   instead of retrying indefinitely.
9. Sync local `main` (`git fetch && git reset --hard origin/main`),
   delete the local feature branch.
10. Update `.agent/state.yaml` (and `.agent/current-task.yaml` back to
    idle) so the next session doesn't repeat the work, and add an entry
    to `.agent/run-history/`.

**Stale shared branches**: if a prior autonomous run's branch still
exists on the remote at an already-merged (now-stale) tip, don't
force-push over it. Recreate the local branch from the remote's actual
tip, merge `origin/main` into it (a normal merge, not a rebase — resolve
any conflict in generated files, `site/graph.json`/`site/details.json`,
by regenerating them with `tools/build_graph.py` rather than
hand-editing), then continue.

**Never commit directly to `main`, and never `git add .` blindly.** If
an autonomous run is interrupted (timeout, crash) with uncommitted
changes still in the working tree, the recovery step must isolate that
work onto its own branch and open a PR for it — never force it onto
`main`, where it could silently overwrite a human's concurrent commit.
See `.github/workflows/autonomous-agent.yml`'s final step for how this
is implemented.

## Session shape (for a scheduled/unattended run)

```
Read .agent/state.yaml and .agent/current-task.yaml
        ↓
Resume incomplete work, or pick the next item per the priority order above
        ↓
Research (primary sources only) → edit entity files / discovery files
        ↓
Rebuild the graph, validate locally (three checks in quality-policy.md)
        ↓
Commit → push → open PR → wait for CI → merge on green
        ↓
Update .agent/state.yaml, .agent/current-task.yaml, .agent/run-history/
(and progress/backlog.md if a whole planned item closed) so the next
session doesn't repeat the work
        ↓
More time/budget left and more real work available? Continue.
Otherwise: checkpoint and stop cleanly.
```

Stop when: the runner's time budget is nearly exhausted, no genuine work
remains at any priority level, or something requires
`.agent/needs-human/`. Before stopping, make sure the last piece of work
is either fully merged or safely isolated on its own branch/PR — never
leave important work only in an uncommitted working tree.

## Human intervention: `.agent/needs-human/`

When a decision genuinely can't be made safely from the evidence — two
plausible readings with no way to pick, a source that contradicts
another already-cited one, a fact that would require inventing something
to resolve — do not guess and do not leave it silently unresolved
either. Create a file under `.agent/needs-human/` (one per issue, named
`<short-slug>.md`) containing:

```markdown
# <short question>

## Context
<which entity/row this concerns, and why it matters>

## Evidence found
<what was checked, quoting the relevant bit of each source>

## Possible interpretations
<the genuinely live options>

## Why this can't be decided safely from here
<the specific gap — not just "I'm not sure">

## Recommended next research
<what a human, or a future session with different access, could check>
```

Commit it as part of the same PR as any other work from that session. A
human clears it by resolving the question (updating the entity/row and
deleting the file, or leaving instructions for the next session) — the
agent should never delete its own `needs-human` files.
