#!/usr/bin/env python3
"""Is the roadmap-board sync still able to work? (used by .github/workflows/project-board.yml)

The sync needs the repository secret PROJECT_TOKEN, a personal access token that expires.
GitHub cannot tell a workflow when a token runs out, so the owner records the date in the
repository variable PROJECT_TOKEN_EXPIRES (YYYY-MM-DD); and once the board is set up, the
variable BOARD_SYNC_ENABLED is "true", which makes a missing secret an error instead of
the quiet "not set up yet" it is before that. docs/credentials.md has the plan (#496).

    python tools/board_health.py --secret-present true --expires 2027-01-05 --enabled true

Prints GitHub annotations (::notice::, ::warning::, ::error::) and, when GITHUB_OUTPUT is
set, `warn=true` when the token is near expiry. Exit status 1 means the sync must not run
and the run should fail (so the failure issue opens). Nothing is read from or sent to any
service. Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import sys

WARN_DAYS = 14


def check(secret_present: bool, expires: str, enabled: bool, today: dt.date | None = None) -> tuple[list[tuple[str, str]], bool, bool]:
    """([(level, message)], failed, warn). Levels: notice, warning, error."""
    today = today or dt.date.today()
    msgs: list[tuple[str, str]] = []
    failed = warn = False
    if not secret_present:
        if enabled:
            msgs.append(("error", "The PROJECT_TOKEN secret is not set, but BOARD_SYNC_ENABLED is true: the board "
                                  "has stopped updating. Restore the secret (docs/credentials.md, rotation steps)."))
            failed = True
        else:
            msgs.append(("notice", "The PROJECT_TOKEN repository secret is not set, so the board was not touched. "
                                   "See docs/roadmap.md."))
        return msgs, failed, warn
    expires = (expires or "").strip()
    if not expires:
        msgs.append(("notice", "PROJECT_TOKEN_EXPIRES is not set, so the token's expiry cannot be watched. "
                               "Set the variable to the token's expiry date (YYYY-MM-DD)."))
        return msgs, failed, warn
    try:
        when = dt.date.fromisoformat(expires)
    except ValueError:
        msgs.append(("error", f"PROJECT_TOKEN_EXPIRES is not a YYYY-MM-DD date: {expires!r}."))
        return msgs, True, warn
    left = (when - today).days
    if left < 0:
        msgs.append(("error", f"The PROJECT_TOKEN expired on {expires} ({-left} day(s) ago). Rotate it "
                              "(docs/credentials.md, section 1) and update PROJECT_TOKEN_EXPIRES."))
        failed = True
    elif left <= WARN_DAYS:
        msgs.append(("warning", f"The PROJECT_TOKEN expires on {expires} ({left} day(s) from now). "
                                "Rotate it before then (docs/credentials.md, section 1)."))
        warn = True
    return msgs, failed, warn


def truthy(value: str) -> bool:
    return (value or "").strip().lower() == "true"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--secret-present", required=True, help="true when the PROJECT_TOKEN secret has a value")
    ap.add_argument("--expires", default="", help="PROJECT_TOKEN_EXPIRES, YYYY-MM-DD (may be empty)")
    ap.add_argument("--enabled", default="", help="BOARD_SYNC_ENABLED (true once the board is set up)")
    args = ap.parse_args(argv)
    msgs, failed, warn = check(truthy(args.secret_present), args.expires, truthy(args.enabled))
    for level, text in msgs:
        print(f"::{level}::{text}")
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(f"warn={'true' if warn else 'false'}\n")
            fh.write(f"failed={'true' if failed else 'false'}\n")
            if msgs and msgs[0][0] in ("warning", "error"):
                fh.write(f"message={msgs[0][1]}\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
