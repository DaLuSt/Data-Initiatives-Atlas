#!/usr/bin/env python3
"""Tests for tools/release.py and the release workflows.

Pure functions plus one throw-away git repository; no network, no GitHub.

    python tools/test_release.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))
sys.path.insert(0, str(REPO_ROOT / "validation"))

import release  # noqa: E402


class TestVersions(unittest.TestCase):
    def test_first_release_of_a_month_is_one(self):
        self.assertEqual(release.next_data_version(date(2026, 10, 6), []), "2026.10.1")

    def test_second_release_in_a_month_increments(self):
        tags = ["data-2026.10.1", "data-2026.10.2"]
        self.assertEqual(release.next_data_version(date(2026, 10, 20), tags), "2026.10.3")

    def test_a_new_month_starts_again_at_one(self):
        self.assertEqual(release.next_data_version(date(2026, 11, 2), ["data-2026.10.4"]), "2026.11.1")

    def test_ten_sorts_after_nine(self):
        tags = [f"data-2026.10.{n}" for n in range(1, 11)]
        self.assertEqual(release.next_data_version(date(2026, 10, 30), tags), "2026.10.11")

    def test_other_tags_are_ignored(self):
        tags = ["schema-1.2.0", "v3", "data-latest", "data-2026.13.1", "data-2026.10.0"]
        self.assertEqual(release.next_data_version(date(2026, 10, 6), tags), "2026.10.1")

    def test_semver_parsing(self):
        self.assertEqual(release.semver_tuple("1.10.2"), (1, 10, 2))
        for bad in ("1.0", "01.0.0", "1.0.0-rc1", "", None):
            with self.assertRaises(ValueError):
                release.semver_tuple(bad)


class TestClassify(unittest.TestCase):
    def test_priority_order(self):
        c = release.classify
        self.assertEqual(c(["metadata/schema.json", "site/app.js", "legislation/x.md"]), "schema")
        self.assertEqual(c(["site/app.js", "legislation/x.md", "docs/graph.md"]), "site")
        self.assertEqual(c(["legislation/x.md", "tools/build_graph.py"]), "data")
        self.assertEqual(c(["tools/release.py", "docs/x.md"]), "tooling")
        self.assertEqual(c([".github/workflows/x.yml"]), "tooling")
        self.assertEqual(c(["docs/ux-analysis.md", ".agent/state.yaml"]), "docs")
        self.assertEqual(c(["README.md"]), "docs")
        self.assertEqual(c([".agent/state.yaml", "discovery/candidates.md"]), "housekeeping")
        self.assertEqual(c([]), "housekeeping")

    def test_ontology_counts_as_schema(self):
        self.assertEqual(release.classify(["metadata/ontology.md"]), "schema")

    def test_the_rank_basis_is_data_not_schema(self):
        # it documents how each country's `rank` values were read; the model is unchanged
        self.assertEqual(release.classify(["metadata/rank-basis.md"]), "data")
        self.assertEqual(release.classify(["metadata/rank-basis.md", "docs/x.md", ".agent/state.yaml"]), "data")

    def test_the_rank_basis_does_not_outrank_a_site_change_or_a_real_schema_change(self):
        self.assertEqual(release.classify(["metadata/rank-basis.md", "site/app.js"]), "site")
        self.assertEqual(release.classify(["metadata/rank-basis.md", "metadata/schema.json"]), "schema")
        self.assertEqual(release.classify(["metadata/rank-basis.md", "metadata/ontology.md"]), "schema")

    def test_every_data_folder_in_the_schema_is_a_data_dir(self):
        schema = json.loads((REPO_ROOT / "metadata" / "schema.json").read_text(encoding="utf-8"))
        for folder in set(schema["type_folder_map"].values()):
            self.assertEqual(release.classify([f"{folder}/x.md"]), "data", folder)


class TestLog(unittest.TestCase):
    RAW = (
        "a1\x1fAdd a thing (#12)\x1f2026-10-05T10:00:00+00:00\x1e\n"
        "b2\x1fDirect commit with no number\x1f2026-10-04T10:00:00+00:00\x1e\n"
        "c3\x1fRelease data 2026.10.1 (#13)\x1f2026-10-03T10:00:00+00:00\x1e\n"
        "d4\x1fFix (#14) and more (#15)\x1f2026-10-02T10:00:00+00:00\x1e\n")

    def test_only_numbered_squash_merges_count(self):
        got = release.parse_log(self.RAW)
        self.assertEqual([c["number"] for c in got], [12, 13, 15])
        self.assertEqual(got[0]["title"], "Add a thing")
        self.assertEqual(got[0]["date"], "2026-10-05")
        self.assertEqual(got[2]["title"], "Fix (#14) and more")

    def test_release_pull_requests_are_recognised(self):
        got = release.parse_log(self.RAW)
        self.assertEqual([release.is_release_change(c) for c in got], [False, True, False])


class TestEntry(unittest.TestCase):
    def change(self, n, title, cat):
        return {"number": n, "title": title, "category": cat, "sha": "x", "date": "2026-10-05"}

    def render(self, **kw):
        base = dict(version="2026.10.2", schema="1.1.0", prev_schema="1.0.0", released="2026-10-12",
                    counts={"entities": 750, "relationships": 1600, "countries": 59},
                    prev_counts={"entities": 740, "relationships": 1565, "countries": 58},
                    changes=[], issues=[], baseline=False)
        base.update(kw)
        return release.render_entry(**base)

    def test_heading_schema_and_deltas(self):
        text = self.render()
        self.assertIn("## Data release 2026.10.2 — 2026-10-12", text)
        self.assertIn("**Schema 1.1.0** (changed from 1.0.0)", text)
        self.assertIn("750 entities (+10)", text)
        self.assertIn("1,600 typed relationships (+35)", text)
        self.assertIn("59 countries (+1)", text)

    def test_unchanged_schema_is_said_so(self):
        self.assertIn("(unchanged)", self.render(schema="1.0.0"))

    def test_changes_are_grouped_in_category_order(self):
        text = self.render(changes=[
            self.change(5, "Fix a typo", "docs"), self.change(4, "Add Y", "data"),
            self.change(3, "New panel", "site"), self.change(2, "Add a type", "schema")])
        order = [text.index(h) for h in ("### Schema", "### Site and features", "### Data", "### Documentation")]
        self.assertEqual(order, sorted(order))
        self.assertIn("- New panel (#3)", text)
        self.assertNotIn("### Tooling", text)

    def test_empty_release_says_so(self):
        self.assertIn("No pull requests were merged", self.render())

    def test_baseline_lists_no_pull_requests(self):
        text = self.render(baseline=True, prev_schema=None, prev_counts=None,
                           changes=[self.change(1, "Old", "data")])
        self.assertIn("first tagged release", text)
        self.assertNotIn("(#1)", text)
        self.assertNotIn("(+", text)

    def test_issues_section(self):
        text = self.render(issues=[{"number": 7, "title": "CSV export"}])
        self.assertIn("### Roadmap items completed", text)
        self.assertIn("- CSV export (#7)", text)

    def test_insert_and_extract_round_trip(self):
        log = "# Changelog\n\n" + release.START_MARK + "\n\n" + release.END_MARK + "\n"
        first = self.render(version="2026.10.1", baseline=True, prev_schema=None, prev_counts=None)
        second = self.render(version="2026.10.2", changes=[self.change(5, "X", "data")])
        log = release.insert_entry(log, first)
        log = release.insert_entry(log, second)
        self.assertLess(log.index("2026.10.2"), log.index("2026.10.1"), "newest first")
        self.assertIn("- X (#5)", release.entry_for(log, "2026.10.2"))
        self.assertNotIn("2026.10.1", release.entry_for(log, "2026.10.2"))
        self.assertIn("first tagged release", release.entry_for(log, "2026.10.1"))
        self.assertIsNone(release.entry_for(log, "2026.10.9"))
        self.assertTrue(log.rstrip().endswith(release.END_MARK))

    def test_missing_markers_are_refused(self):
        with self.assertRaises(ValueError):
            release.insert_entry("# Changelog\n", "## x\n")

    def test_the_repository_changelog_has_its_markers(self):
        text = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn(release.START_MARK, text)
        self.assertIn(release.END_MARK, text)


class TestLinkedinDraft(unittest.TestCase):
    ENTRY = (
        "**Schema 1.1.0** (changed from 1.0.0)\n\n"
        "In the Atlas at this release: 745 entities (+5), 1,576 typed relationships (+5), 58 countries (+0).\n\n"
        "### Schema\n\n- Add the rank field (#400)\n\n"
        "### Site and features\n\n- List view: download the rows as CSV (#456)\n\n"
        "### Data\n\n- Add three UK competent authorities (#491)\n- France and the Open Data Directive (#490)\n\n"
        "### Tooling\n\n- Board sync (#488)\n\n"
        "### Documentation\n\n- Roadmap docs (#464)\n\n"
        "### Housekeeping\n\n- Housekeeping: record #1 in state.yaml (#516)\n\n"
        "### Roadmap items completed\n\n- English names for the records still without one (#446)\n"
    )

    def draft(self, entry=None):
        return release.linkedin_draft(entry or self.ENTRY, "2026.11.1")

    def bullets(self, entry=None):
        return [l[2:] for l in self.draft(entry).splitlines() if l.startswith("• ")]

    def test_it_names_the_release_and_links_the_site_and_the_notes(self):
        d = self.draft()
        self.assertIn("data release 2026.11.1", d)
        self.assertIn("https://dalust.github.io/Data-Initiatives-Atlas/", d)
        self.assertIn("/releases/tag/data-2026.11.1", d)

    def test_it_carries_the_counts_from_the_entry(self):
        self.assertIn("745 entities (+5), 1,576 typed relationships (+5), 58 countries (+0)", self.draft())

    def test_pull_request_numbers_are_dropped(self):
        self.assertNotRegex(self.draft(), r"\(#\d+\)")

    def test_site_then_data_then_schema_in_that_order(self):
        self.assertEqual(self.bullets(), [
            "List view: download the rows as CSV",
            "Add three UK competent authorities",
            "France and the Open Data Directive",
            "Add the rank field"])

    def test_tooling_documentation_and_housekeeping_are_never_listed(self):
        d = self.draft()
        for internal in ("Board sync", "Roadmap docs", "Housekeeping"):
            self.assertNotIn(internal, d)

    def test_completed_roadmap_items_only_fill_a_short_list(self):
        self.assertNotIn("English names", self.draft())  # four items already
        entry = ("### Data\n\n- One data change (#1)\n\n### Roadmap items completed\n\n"
                 "- English names for the records still without one (#446)\n")
        self.assertEqual(self.bullets(entry), ["One data change", "English names for the records still without one"])

    def test_roadmap_items_do_not_count_towards_more_when_the_list_is_full(self):
        entry = ("### Data\n\n" + "".join(f"- Change {n} (#{n})\n" for n in range(1, 5)) +
                 "\n### Roadmap items completed\n\n- A roadmap item (#9)\n")
        self.assertNotIn("and more", self.draft(entry))

    def test_the_same_text_in_two_listed_sections_is_listed_once(self):
        entry = "### Site and features\n\n- Same (#1)\n\n### Data\n\n- Same (#2)\n"
        self.assertEqual(self.bullets(entry), ["Same"])

    def test_an_item_that_is_in_two_sections_is_listed_once(self):
        entry = ("### Data\n\n- Same thing (#1)\n\n### Roadmap items completed\n\n- Same thing (#2)\n")
        self.assertEqual(self.bullets(entry), ["Same thing"])

    def test_a_highlights_section_is_used_as_written(self):
        entry = self.ENTRY.replace("### Schema\n", "### Highlights\n\n- 26 more English names for bodies and laws\n"
                                   "- The Information Commission replaces the ICO\n\n### Schema\n", 1)
        self.assertEqual(self.bullets(entry), ["26 more English names for bodies and laws",
                                               "The Information Commission replaces the ICO"])
        self.assertNotIn("and more", self.draft(entry))

    def test_a_short_list_does_not_say_there_is_more(self):
        self.assertNotIn("and more in the release notes", self.draft("### Data\n\n- Only one (#1)\n"))

    def test_a_long_list_is_cut_and_says_so(self):
        entry = "### Data\n\n" + "".join(f"- Item number {n} (#{n})\n" for n in range(1, 10))
        self.assertEqual(len(self.bullets(entry)), release.LINKEDIN_ITEMS)
        self.assertIn("…and more in the release notes.", self.draft(entry))

    def test_there_is_no_markdown(self):
        d = self.draft()
        for mark in ("**", "###", "`", "]("):
            self.assertNotIn(mark, d)

    def test_a_long_item_is_shortened(self):
        line = self.bullets("### Data\n\n- " + "x" * 400 + " (#1)\n")[0]
        self.assertLessEqual(len(line), release.LINKEDIN_ITEM_LIMIT)
        self.assertTrue(line.endswith("…"))

    def test_the_baseline_release_is_called_the_first(self):
        entry = ("In the Atlas at this release: 740 entities.\n\nThis is the first tagged release. The changes "
                 "before it are not listed here: they are in the git history.\n")
        d = self.draft(entry)
        self.assertIn("first tagged release of the Atlas", d)
        self.assertNotIn("• ", d)

    def test_a_release_with_nothing_listed_still_makes_a_post(self):
        d = self.draft("**Schema 1.0.0**\n")
        self.assertIn("data release 2026.11.1", d)
        self.assertNotIn("What changed", d)

    def test_it_stays_inside_linkedins_limit(self):
        entry = "### Highlights\n\n" + "".join(f"- {'y' * 200} (#{n})\n" for n in range(500))
        self.assertLessEqual(len(self.draft(entry)), release.LINKEDIN_LIMIT)

    def test_the_real_changelog_entry_makes_a_draft(self):
        text = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        entry = release.entry_for(text, "2026.10.1")
        d = release.linkedin_draft(entry, "2026.10.1")
        self.assertIn("740 entities", d)
        self.assertIn("first tagged release", d)


class TestSchemaRule(unittest.TestCase):
    def doc(self, version, types=("act",)):
        return json.dumps({"schema_version": version, "types": list(types)})

    def test_model_change_without_bump_is_an_error(self):
        err = release.schema_change_error(self.doc("1.0.0"), self.doc("1.0.0", ("act", "decision")))
        self.assertIn("did not", err)

    def test_model_change_with_bump_is_fine(self):
        self.assertIsNone(release.schema_change_error(self.doc("1.0.0"), self.doc("1.1.0", ("act", "decision"))))

    def test_version_going_backwards_is_an_error(self):
        err = release.schema_change_error(self.doc("1.2.0"), self.doc("1.1.0", ("act", "decision")))
        self.assertIn("backwards", err)

    def test_no_change_is_fine(self):
        self.assertIsNone(release.schema_change_error(self.doc("1.0.0"), self.doc("1.0.0")))

    def test_bump_alone_is_allowed(self):
        self.assertIsNone(release.schema_change_error(self.doc("1.0.0"), self.doc("1.0.1")))

    def test_bad_version_is_an_error(self):
        self.assertIn("MAJOR.MINOR.PATCH", release.schema_change_error(None, self.doc("1.0")))

    def test_first_introduction_of_the_version_is_fine(self):
        old = json.dumps({"types": ["act"]})
        self.assertIsNone(release.schema_change_error(old, self.doc("1.0.0", ("act", "x"))))

    def test_the_repository_schema_has_a_valid_version(self):
        schema = json.loads((REPO_ROOT / "metadata" / "schema.json").read_text(encoding="utf-8"))
        release.semver_tuple(schema["schema_version"])

    def test_every_field_in_use_is_listed_in_the_schema(self):
        # Without this, adding an optional field would not change schema.json
        # and so would slip past the schema-version rule.
        import common
        schema = json.loads((REPO_ROOT / "metadata" / "schema.json").read_text(encoding="utf-8"))
        known = set(schema["required_fields"]) | set(schema["optional_fields"])
        used = set()
        for e in common.load_all_entities():
            if e.frontmatter:
                used |= set(e.frontmatter)
        self.assertEqual(sorted(used - known), [], "frontmatter fields missing from schema.json")


class TestStateText(unittest.TestCase):
    STATE = "updated: x\n\nvalidation_status: clean\n\nlast_merged_prs:\n  - number: 1\n"

    def test_adds_the_block_after_validation_status(self):
        out = release.update_state_text(self.STATE, "2026.10.1", "1.0.0", "2026-10-06")
        self.assertIn('release:\n  data: "2026.10.1"\n  schema: "1.0.0"\n  released: "2026-10-06"\n', out)
        self.assertLess(out.index("validation_status"), out.index("release:"))
        self.assertLess(out.index("release:"), out.index("last_merged_prs"))

    def test_replaces_an_existing_block(self):
        once = release.update_state_text(self.STATE, "2026.10.1", "1.0.0", "2026-10-06")
        twice = release.update_state_text(once, "2026.10.2", "1.1.0", "2026-10-12")
        self.assertEqual(twice.count("release:"), 1)
        self.assertIn('"2026.10.2"', twice)
        self.assertNotIn('"2026.10.1"', twice)
        self.assertIn("last_merged_prs", twice)


class TestGit(unittest.TestCase):
    """changes_since against a real throw-away repository."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.orig = release.REPO_ROOT
        release.REPO_ROOT = self.root
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "t@example.com")
        self.git("config", "user.name", "t")

    def tearDown(self):
        release.REPO_ROOT = self.orig
        self.tmp.cleanup()

    def git(self, *args):
        subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True, text=True)

    def commit(self, subject, path):
        f = self.root / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(subject, encoding="utf-8")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", subject)

    def test_changes_since_a_tag(self):
        self.commit("Old data (#1)", "legislation/a.md")
        self.git("tag", "data-2026.10.1")
        self.commit("New panel (#2)", "site/app.js")
        self.commit("Release data 2026.10.2 (#3)", "metadata/version.yaml")
        self.commit("Add a country (#4)", "countries/xx/xx.md")
        self.commit("Housekeeping: record #4 (#5)", ".agent/state.yaml")
        self.commit("Direct commit", "docs/x.md")
        got = release.changes_since("data-2026.10.1")
        self.assertEqual([(c["number"], c["category"]) for c in got],
                         [(5, "housekeeping"), (4, "data"), (2, "site")])
        self.assertEqual(release.last_data_tag(), "data-2026.10.1")

    def test_no_tag_means_everything(self):
        self.commit("First (#1)", "legislation/a.md")
        self.commit("Second (#2)", "docs/a.md")
        self.assertEqual([c["number"] for c in release.changes_since(None)], [2, 1])
        self.assertIsNone(release.last_data_tag())


class TestWorkflows(unittest.TestCase):
    WF = REPO_ROOT / ".github" / "workflows"

    def test_workflows_parse_and_call_real_subcommands(self):
        import yaml
        for name in ("release-pr.yml", "release-publish.yml", "validate.yml"):
            text = (self.WF / name).read_text(encoding="utf-8")
            yaml.safe_load(text)
            for sub in re.findall(r"tools/release\.py (\S+)", text):
                self.assertIn(sub, {"plan", "prepare", "notes", "tags", "check-schema", "linkedin-draft"}, f"{name}: {sub}")

    def test_the_release_workflow_never_publishes(self):
        text = (self.WF / "release-pr.yml").read_text(encoding="utf-8")
        for forbidden in ("gh release create", "git push origin main", 'git push origin "$tag"'):
            self.assertTrue(forbidden not in text, f"release-pr.yml must not contain {forbidden!r}")
        # reading tags is fine; creating one is not
        self.assertIsNone(re.search(r"git tag (?!--list)", text), "release-pr.yml creates a tag")

    def test_publishing_runs_only_when_the_version_file_changes_on_main(self):
        import yaml
        wf = yaml.safe_load((self.WF / "release-publish.yml").read_text(encoding="utf-8"))
        push = wf[True]["push"]  # PyYAML reads the key `on` as True
        self.assertEqual(push["branches"], ["main"])
        self.assertEqual(push["paths"], ["metadata/version.yaml"])

    def test_the_release_title_matches_what_the_tool_skips(self):
        text = (self.WF / "release-pr.yml").read_text(encoding="utf-8")
        self.assertIn('--title "Release data $version"', text)
        self.assertTrue(release.is_release_change({"title": "Release data 2026.10.1"}))

    def test_the_roadmap_label_is_the_same_everywhere(self):
        template = (REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "roadmap-item.yml").read_text(encoding="utf-8")
        workflow = (self.WF / "release-pr.yml").read_text(encoding="utf-8")
        docs = (REPO_ROOT / "docs" / "roadmap.md").read_text(encoding="utf-8")
        self.assertIn('labels: ["roadmap"]', template)
        self.assertIn("--label roadmap", workflow)
        self.assertIn("`roadmap`", docs)
        for ref in ("docs/roadmap.md", "metadata/versioning.md"):
            self.assertTrue((REPO_ROOT / ref).exists(), ref)
            self.assertIn(ref, (REPO_ROOT / ".agent" / "operating-model.md").read_text(encoding="utf-8") +
                          (REPO_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8"))

    def test_the_linkedin_step_only_opens_an_issue_and_never_posts(self):
        text = (self.WF / "release-publish.yml").read_text(encoding="utf-8")
        self.assertIn("tools/release.py linkedin-draft", text)
        self.assertIn("gh issue create", text)
        self.assertNotIn("api.linkedin.com", text)
        self.assertNotRegex(text, r"secrets\.\w*LINKEDIN")
        self.assertRegex(text, r"issues:\s*write")

    def test_the_release_pull_request_tells_the_reviewer_about_highlights(self):
        text = (self.WF / "release-pr.yml").read_text(encoding="utf-8")
        self.assertIn("### Highlights", text)

    def test_the_linkedin_step_is_idempotent(self):
        text = (self.WF / "release-publish.yml").read_text(encoding="utf-8")
        self.assertIn('grep -Fxq "$title"', text)

    def test_the_data_correction_form_asks_for_what_a_fix_needs_and_is_linked(self):
        import yaml
        form = yaml.safe_load((REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "data-correction.yml").read_text(encoding="utf-8"))
        self.assertEqual(form["labels"], ["data-correction"])
        required = {b["id"] for b in form["body"] if b.get("validations", {}).get("required")}
        self.assertTrue({"entity", "says", "should", "source"} <= required, required)
        for doc in ("SECURITY.md", "CONTRIBUTING.md"):
            self.assertIn("issues/new?template=data-correction.yml", (REPO_ROOT / doc).read_text(encoding="utf-8"), doc)

    def test_ci_checks_the_schema_version_on_pull_requests(self):
        text = (self.WF / "validate.yml").read_text(encoding="utf-8")
        self.assertIn("check-schema --base-ref", text)
        shared = (REPO_ROOT / ".github" / "actions" / "checks" / "action.yml").read_text(encoding="utf-8")
        self.assertIn("test_release.py", shared)

    def test_the_release_pr_gets_the_required_validate_check(self):
        """main requires `validate`; a PR opened with GITHUB_TOKEN never triggers it,
        so the release workflow must start it on the branch itself."""
        rel = (self.WF / "release-pr.yml").read_text(encoding="utf-8")
        self.assertIn("actions: write", rel)
        self.assertIn('gh workflow run validate.yml --ref "$branch"', rel)
        self.assertLess(rel.index("gh pr create"), rel.index("gh workflow run validate.yml"))
        val = (self.WF / "validate.yml").read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", val)
        self.assertRegex(val, r"(?m)^  validate:$")  # the job name main requires

    def test_pull_requests_and_deploys_run_the_same_checks(self):
        for name in ("validate.yml", "pages.yml"):
            text = (self.WF / name).read_text(encoding="utf-8")
            self.assertIn("uses: ./.github/actions/checks", text, name)

    def test_every_test_file_is_in_the_shared_checks(self):
        shared = (REPO_ROOT / ".github" / "actions" / "checks" / "action.yml").read_text(encoding="utf-8")
        tests = sorted(p.name for p in (REPO_ROOT / "tools").glob("test_*.py")) + \
            sorted(p.name for p in (REPO_ROOT / "validation").glob("test_*.py"))
        self.assertTrue(tests)
        for name in tests:
            self.assertIn(name, shared, f"{name} is not run by .github/actions/checks")

    def test_no_workflow_uses_an_action_known_to_run_on_node_20(self):
        # Warned about on 2026-10-08 (roadmap #493); these are the Node 24 majors.
        node20 = ("actions/checkout@v4", "actions/setup-python@v5", "actions/setup-node@v4",
                  "actions/configure-pages@v5", "actions/upload-pages-artifact@v3", "actions/deploy-pages@v4")
        for path in sorted(self.WF.glob("*.yml")):
            text = path.read_text(encoding="utf-8")
            for old in node20:
                self.assertNotIn(old, text, f"{path.name} still uses {old}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
