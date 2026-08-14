#!/usr/bin/env python3
"""Run every validation/validate_*.py check and aggregate the result.

Used locally (`python validation/run_all.py`) and by
.github/workflows/validate.yml on every pull request.
"""

from __future__ import annotations

import sys

import validate_frontmatter
import validate_ids
import validate_links
import validate_relationships
import validate_sources

CHECKS = [
    validate_ids,
    validate_frontmatter,
    validate_links,
    validate_relationships,
    validate_sources,
]


def main() -> int:
    exit_codes = [check.main() for check in CHECKS]
    failed = sum(1 for code in exit_codes if code != 0)
    print(f"\n{'=' * 40}")
    if failed:
        print(f"validate: {failed}/{len(CHECKS)} check(s) reported errors.")
    else:
        print(f"validate: all {len(CHECKS)} checks passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
