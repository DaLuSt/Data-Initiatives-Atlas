#!/usr/bin/env python3
"""Tests for how the browser suite (tools/test_ui.mjs) is wired into CI.

The browser itself runs in the `browser` job of validate.yml; these tests only read files.

    python tools/test_browser_ci.py
"""

from __future__ import annotations

import re
import shutil
import subprocess
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SUITE = (REPO_ROOT / "tools" / "test_ui.mjs").read_text(encoding="utf-8")


class TestSuiteSource(unittest.TestCase):
    def test_it_parses(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        r = subprocess.run([node, "--check", str(REPO_ROOT / "tools" / "test_ui.mjs")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_it_uses_the_client_library_only(self):
        self.assertIn("from 'playwright-core'", SUITE)
        self.assertNotIn("from 'playwright'", SUITE)

    def test_a_crashing_section_is_a_failed_check_not_the_end_of_the_run(self):
        self.assertIn("function crash(", SUITE)
        self.assertGreaterEqual(SUITE.count("} catch (e) { crash("), 15)
        # Every block opened with try { has its catch: the braces balance (node --check) and
        # the two counts agree.
        # (pickLayout() has a try of its own, with a different catch: it adds the control's
        # state to the error, then rethrows into the section's crash().)
        helpers_with_a_try = SUITE.count("async function pickLayout")
        self.assertEqual(SUITE.count("\n  try {") - helpers_with_a_try, SUITE.count("} catch (e) { crash("))

    def test_a_stale_selector_fails_fast(self):
        self.assertIn("setDefaultTimeout(6000)", SUITE)

    def test_no_entity_count_is_frozen_in_the_suite(self):
        # 652 was the number of entities when the suite was written; the data moves on.
        code = "\n".join(l for l in SUITE.splitlines() if not l.lstrip().startswith(("//", "*", "/*")))
        self.assertNotRegex(code, r"(===|<|>)\s*(6[0-9]{2}|7[0-9]{2})\b")
        self.assertIn("g.stats.entities", SUITE)

    def test_it_knows_the_current_markup(self):
        self.assertNotIn(".d-sec h4", SUITE)          # the detail sections are h3 now
        self.assertNotIn('has-text("Wikilinks")', SUITE)  # the sidebar says "Mentions"
        self.assertIn("openFilter(", SUITE)           # collapsed filter groups are opened first

    def test_the_selectors_it_uses_exist_in_the_site(self):
        html = (REPO_ROOT / "site" / "index.html").read_text(encoding="utf-8")
        ids = set(re.findall(r"#([a-z][a-z0-9-]*)\b", SUITE))
        # Only ids that are written in the markup itself (the rest are built by app.js).
        static = {i for i in ids if f'id="{i}"' in html}
        for must in ("search", "view-atlas", "view-explorer", "layout-mode", "f-level", "f-provenance",
                     "f-confidence", "edge-classes", "stage-status", "detail-close"):
            self.assertIn(must, static, must)
        js = (REPO_ROOT / "site" / "app.js").read_text(encoding="utf-8")
        for i in ids:
            self.assertTrue(f'id="{i}"' in html or f'"{i}"' in js or f"'{i}'" in js or f"#{i}" in js or f'id="{i}' in js,
                            f"#{i} is used by the browser suite but appears nowhere in the site")


class TestWorkflow(unittest.TestCase):
    TEXT = (REPO_ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")

    @classmethod
    def setUpClass(cls):
        import yaml
        cls.wf = yaml.safe_load(cls.TEXT)
        cls.job = cls.wf["jobs"]["browser"]
        cls.shell = "\n".join(s.get("run", "") for s in cls.job["steps"])

    def test_the_required_job_is_unchanged_and_the_browser_job_is_separate(self):
        self.assertIn("validate", self.wf["jobs"])
        self.assertIn("browser", self.wf["jobs"])
        self.assertNotIn("needs", self.job)

    def test_the_graph_is_built_before_the_site_is_served(self):
        self.assertLess(self.shell.index("build_graph.py"), self.shell.index("http.server"))

    def test_the_client_library_is_pinned_and_no_browser_is_downloaded(self):
        self.assertRegex(self.shell, r"playwright-core@\d+\.\d+\.\d+")
        self.assertNotIn("playwright install", self.shell)
        self.assertIn("google-chrome", self.shell)

    def test_the_suite_is_run_against_the_local_server(self):
        self.assertIn("node tools/test_ui.mjs", self.shell)
        self.assertIn("--directory site", self.shell)
        self.assertIn("8765", self.shell)

    def test_it_has_a_time_limit_and_no_secrets(self):
        self.assertIn("timeout-minutes", self.job)
        self.assertNotIn("secrets.", self.TEXT)

    def test_the_workflow_still_only_reads(self):
        self.assertEqual(self.wf["permissions"], {"contents": "read"})

    def test_actions_are_current(self):
        for step in self.job["steps"]:
            if step.get("uses", "").startswith(("actions/checkout", "actions/setup-python")):
                self.assertRegex(step["uses"], r"@v[7-9]")

    def test_node_modules_is_ignored(self):
        self.assertIn("node_modules/", (REPO_ROOT / ".gitignore").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
