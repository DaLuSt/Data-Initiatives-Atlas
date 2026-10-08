# Versioning and releases

The Atlas has **two version numbers**, because two different kinds of people
depend on it. Someone reusing the data needs to know when its *shape* changes;
someone reading the Atlas needs to know *which snapshot* they are looking at.

| Track | Format | Changes when | Where it lives |
|---|---|---|---|
| **Schema version** | SemVer, `MAJOR.MINOR.PATCH` | the data model changes | `schema_version` in `metadata/schema.json` |
| **Data release** | `YYYY.MM.N`, N = the release's number within that month (`2026.10.1`, `2026.10.2`, `2026.11.1`) | a release is made from the pull requests merged since the last one | `metadata/version.yaml`, `CHANGELOG.md`, the git tags |

Every data release states the schema version it conforms to.

## The schema version

The data model is `metadata/schema.json` (types, levels, statuses, relationship
types, the required and optional frontmatter fields, rank values) together with
the documents that explain it. Bump `schema_version` **in the pull request that
changes the model**, by these rules:

| Bump | When | Examples |
|---|---|---|
| **MAJOR** | A value or field that existing data could use stops being valid, or changes meaning. Anyone reading the data has to adapt. | Removing or renaming a type, level, status or relationship type; making an optional field required; changing the ID format; moving entities to a different type |
| **MINOR** | Something is added and nothing existing breaks. | A new type, relationship type, level, status or rank value; a new optional field |
| **PATCH** | The schema file changes without changing what is valid. | Fixing a mistake in a vocabulary entry's wording, reordering, a clarified constraint that existing data already met |

A pull request that changes `metadata/schema.json` but not `schema_version`
fails CI (`python tools/release.py check-schema --base-ref origin/main`), and so
does a version that goes backwards. Adding a field to the documents but not to
`optional_fields` in `schema.json` is how a model change slips past that check,
so list new fields there too; a test fails if the repository uses a field the
schema does not list.

## Data releases

A data release is a snapshot of the whole repository: the entities, the
site, the tools. It is made from the **pull requests squash-merged into `main`
since the previous release**.

1. **A release pull request is opened automatically**
   (`.github/workflows/release-pr.yml`, weekly, or by hand with *Run workflow*).
   It runs `python tools/release.py prepare`, which writes `metadata/version.yaml`,
   a new entry at the top of `CHANGELOG.md` and the `release:` block in
   `.agent/state.yaml`. The entry lists the merged pull requests under *Schema*,
   *Site and features*, *Data*, *Tooling*, *Documentation* and *Housekeeping*
   (by the files each one touched), the closed roadmap issues, and the counts of
   entities, relationships and countries with the change since the last release.
   It is skipped when nothing but housekeeping was merged, or when a release pull
   request is already open.
2. **You review and merge it.** Nothing is tagged or published before that.
   Edit the CHANGELOG entry in the pull request if the wording needs it.
3. **Merging creates the tags and the GitHub Release**
   (`.github/workflows/release-publish.yml`): the tag `data-2026.10.1` and a
   GitHub Release whose notes are the CHANGELOG entry, plus the tag
   `schema-1.0.0` the first time that schema version is released.
4. **The same workflow opens an issue with a LinkedIn post draft** (label
   `linkedin`, title "Post data release X on LinkedIn"): plain text built from the
   CHANGELOG entry by `python tools/release.py linkedin-draft X`, with the counts,
   up to four changes (completed roadmap items first) and links to the site and the
   release notes. The reviewer of the release pull request can add a
   `### Highlights` section (plain-language bullets) under the counts line of the
   CHANGELOG entry; the draft then uses exactly those. Without one it lists the
   Site and features, Data and Schema changes, never Tooling, Documentation or
   Housekeeping, and uses completed roadmap items only to fill a short list. A
   person reads the draft, edits it, posts it by hand and closes the
   issue. Nothing is sent to LinkedIn by the repository; re-running the workflow
   does not open a second issue.

The first release is a baseline: it records the counts and lists no pull requests,
because the history before it is in git and in `.agent/run-history/`.

Tags are named `data-YYYY.MM.N` and `schema-X.Y.Z` so the two tracks never
collide. The site's footer shows the data release and schema version it was built
from, linked to the changelog.

## Schema history before versioning

The schema was not numbered before 2026-10-06, so these changes have no version.
They are listed, with the bump the rules above would have given, so the
history is not lost. **Version 1.0.0 is the schema as of the first release.**

| Date | Pull request | Change | Would have been |
|---|---|---|---|
| 2026-09-20 | #293 | `uses-data-from` and `carries-identifier-of` relationship types | MINOR |
| 2026-09-20 | #294 | `referred-to-cjeu-over` relationship type | MINOR |
| 2026-09-20 | #295 | `referred-to-cjeu-over` renamed `referred-to-court-over` | MAJOR |
| 2026-09-26 | #345 | optional `organisation_role` field | MINOR |
| 2026-10-02 | #404 | `type: law` split into `act`, `decision`, `subordinate-legislation`, `agreement` | MAJOR |
| 2026-10-02 | #406 | `soft-law` type | MINOR |
| 2026-10-02 | #408 | optional `rank` field | MINOR |
| 2026-10-03 | #423 | `level: sectoral` retired | MAJOR |
| 2026-10-06 | #439 | optional `name_en` field | MINOR |

Taken together that is three breaking changes in about three weeks, which is why
the schema now has a version.

## For a Claude Code session

If your change touches `metadata/schema.json`, bump `schema_version` in the same
pull request and add a line under *Schema history* only if you are recording
something from before this file existed. Do not edit `metadata/version.yaml` or
`CHANGELOG.md` by hand; the release pull request does.
