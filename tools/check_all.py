#!/usr/bin/env python3
"""Every check that needs no network, in one command: the validation suite, each test suite and
the two consistency checks. CI runs exactly this (.github/actions/checks, used by validate.yml
and pages.yml), and so can a session or a contributor:

    python tools/check_all.py            # run everything, then say what failed
    python tools/check_all.py --fast     # stop at the first failure
    python tools/check_all.py --list     # print the checks and exit

A new test file is added to CHECKS below, once. tools/test_release.py fails when a test file is
missing from the list.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# (title, command, folder to run in). Titles say what is covered; commands are relative to the repo.
CHECKS: list[tuple[str, list[str], str]] = [
    # YAML parses · IDs unique · relationships resolve · links resolve · sources present
    ("Validation suite", ["python", "run_all.py"], "validation"),
    # The validators' own rules: each is shown to fire on a defect and to stay quiet on a good entity.
    ("Test the validators", ["python", "validation/test_validators.py"], "."),
    # Parsing, node/edge generation, direction preservation, refusal behaviour, the size budget.
    ("Test the graph generator", ["python", "tools/test_build_graph.py"], "."),
    # The re-verification runner. Pure functions, no network.
    ("Test the re-verification runner", ["python", "tools/test_reverify.py"], "."),
    # The release tooling: version arithmetic, change classification, the CHANGELOG entry, the
    # schema-version rule, and how the workflows are wired.
    ("Test the release tooling", ["python", "tools/test_release.py"], "."),
    # The roadmap board sync (tools/project_board.py), against an in-memory fake of GitHub's API.
    ("Test the board sync", ["python", "tools/test_project_board.py"], "."),
    # The LinkedIn authorisation script, with LinkedIn replaced by fakes.
    ("Test the LinkedIn authorisation script", ["python", "tools/test_linkedin_auth.py"], "."),
    # The LinkedIn poster and the properties of linkedin-post.yml (protected environment, no double post).
    ("Test the LinkedIn poster", ["python", "tools/test_linkedin_post.py"], "."),
    # The blocked-host probe (tools/host_probe.py) and probe-blocked-hosts.yml.
    ("Test the blocked-host probe", ["python", "tools/test_host_probe.py"], "."),
    # Reading pages on a runner (tools/runner_fetch.py) and fetch-pages.yml.
    ("Test the page reader", ["python", "tools/test_runner_fetch.py"], "."),
    # The board's token watch (tools/board_health.py) and the issue steps in project-board.yml.
    ("Test the board's token watch", ["python", "tools/test_board_health.py"], "."),
    # The age report for `last_verified` (tools/verification_age.py, roadmap #510).
    ("Test the verification age report", ["python", "tools/test_verification_age.py"], "."),
    # How the browser suite is wired into CI. No browser here.
    ("Test the browser suite's CI wiring", ["python", "tools/test_browser_ci.py"], "."),
    # The headline numbers in README.md and .agent/state.yaml: the rewriting rules, and that they match the data.
    ("Test the count updater", ["python", "tools/test_update_counts.py"], "."),
    # Fails when a change to the data left the README or state.yaml numbers behind. Fix: python tools/update_counts.py
    ("Check the headline numbers", ["python", "tools/update_counts.py", "--check"], "."),
    # Proves the graph can still be generated from this data (the generated files are not committed).
    ("Check the graph builds", ["python", "tools/build_graph.py", "--check"], "."),
]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fast", action="store_true", help="stop at the first failing check")
    ap.add_argument("--list", action="store_true", help="print the checks and exit")
    args = ap.parse_args(argv)

    if args.list:
        for title, cmd, folder in CHECKS:
            print(f"{title}: {' '.join(cmd)}" + ("" if folder == "." else f"   (in {folder}/)"))
        return 0

    in_ci = os.environ.get("GITHUB_ACTIONS") == "true"
    failed: list[str] = []
    rows: list[tuple[str, float, bool]] = []
    for title, cmd, folder in CHECKS:
        # On a runner the log folds each check under its title; elsewhere it is a plain heading.
        print(f"::group::{title}" if in_ci else f"\n=== {title}", flush=True)
        began = time.monotonic()
        exe = [sys.executable if cmd[0] == "python" else cmd[0], *cmd[1:]]
        ok = subprocess.run(exe, cwd=REPO / folder).returncode == 0
        rows.append((title, time.monotonic() - began, ok))
        if in_ci:
            print("::endgroup::", flush=True)
            if not ok:
                print(f"::error title={title}::{title} failed", flush=True)
        if not ok:
            failed.append(title)
            if args.fast:
                break

    print("\n" + "\n".join(f"{'ok  ' if ok else 'FAIL'} {secs:6.1f}s  {title}" for title, secs, ok in rows))
    if failed:
        print(f"\n{len(failed)} of {len(rows)} checks failed: " + "; ".join(failed))
        return 1
    print(f"\nall {len(rows)} checks passed in {sum(s for _, s, _ in rows):.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
