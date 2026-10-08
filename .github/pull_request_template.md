## What changed and why

<!-- One or two sentences. The title becomes the squash-merge commit and the release note, so make it say what changed. -->

## Roadmap

<!-- `Closes #N` for the roadmap issue this finishes. GitHub closes only the first issue in a single "Closes" line, so write one line per issue. Leave out if there is none. -->

## Sources and checks

- [ ] New or changed facts come from primary sources, and each one is cited in the entity (see `.agent/research-policy.md`); anything I could not read is in `discovery/unresolved.md`
- [ ] `python3 tools/build_graph.py` and `python3 validation/run_all.py` are clean
- [ ] Changed `metadata/schema.json`? I bumped `schema_version` (see `metadata/versioning.md`)
- [ ] I did not edit `CHANGELOG.md` or `metadata/version.yaml` (the release pull request does)
