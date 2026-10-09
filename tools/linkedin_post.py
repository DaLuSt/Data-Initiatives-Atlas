#!/usr/bin/env python3
"""Post a data release to LinkedIn (used by .github/workflows/linkedin-post.yml).

Reads the text to post from a file, posts it as a public text post with the
member's token, and prints the link to the post. It talks to LinkedIn's Posts API
(POST https://api.linkedin.com/rest/posts) and to nothing else.

    LINKEDIN_ACCESS_TOKEN   the token from tools/linkedin_auth.py        (secret)
    LINKEDIN_AUTHOR_URN     urn:li:person:<id>                           (secret)
    LINKEDIN_TOKEN_EXPIRES  YYYY-MM-DD, from tools/linkedin_auth.py      (optional)
    LINKEDIN_API_VERSION    YYYYMM of the Posts API (default: last month) (optional)

    python tools/linkedin_post.py post --text-file post.txt [--dry-run]
    python tools/linkedin_post.py extract --issue-body-file issue.md   # the draft in an issue

Exit status: 0 posted (or a dry run), 1 the post failed, 2 refused before sending
(bad input, token expired). Nothing secret is ever printed. Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request

POSTS_URL = "https://api.linkedin.com/rest/posts"
FEED_URL = "https://www.linkedin.com/feed/update/"
LIMIT = 3000  # characters; the same limit the draft is built to (tools/release.py)
WARN_DAYS = 14
# Characters LinkedIn's "little text" format reserves; each must carry a backslash to
# be shown as itself (Microsoft Learn, Posts API > little text format).
RESERVED = "\\|{}@[]()<>#*_~"
AUTHOR_RE = re.compile(r"^urn:li:(person|organization):[A-Za-z0-9_-]+$")


class PostError(Exception):
    """The post was refused or failed; the message is safe to print."""

    def __init__(self, message: str, code: int = 1):
        super().__init__(message)
        self.code = code


def escape_commentary(text: str) -> str:
    """Escape LinkedIn's reserved characters, but keep #hashtags working.

    A "#" followed by a letter at the start of a word stays a hashtag; "#459" and
    every other reserved character are shown as written.
    """
    out = "".join("\\" + ch if ch in RESERVED else ch for ch in text)
    return re.sub(r"(?<![^\s])\\#(?=[A-Za-z])", "#", out)


def extract_draft(issue_body: str) -> str:
    """The text in the issue's first ```text block (what the owner may have edited)."""
    m = re.search(r"```text\r?\n(.*?)\r?\n```", issue_body, re.S)
    if not m or not m.group(1).strip():
        raise PostError("the issue has no ```text block with a draft in it", 2)
    return m.group(1).strip() + "\n"


def default_version(today: dt.date | None = None) -> str:
    """Last month as YYYYMM: LinkedIn publishes each version, then supports it a year."""
    today = today or dt.date.today()
    first = today.replace(day=1)
    last = first - dt.timedelta(days=1)
    return f"{last.year}{last.month:02d}"


def days_left(expires: str, today: dt.date | None = None) -> int | None:
    """Days until the token's recorded expiry date; None when it is not recorded."""
    if not expires:
        return None
    try:
        when = dt.date.fromisoformat(expires.strip())
    except ValueError:
        raise PostError(f"LINKEDIN_TOKEN_EXPIRES is not a YYYY-MM-DD date: {expires!r}", 2) from None
    return (when - (today or dt.date.today())).days


def build_request(text: str, author: str, token: str, version: str) -> urllib.request.Request:
    body = {
        "author": author,
        "commentary": escape_commentary(text),
        "visibility": "PUBLIC",
        "distribution": {"feedDistribution": "MAIN_FEED", "targetEntities": [],
                         "thirdPartyDistributionChannels": []},
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }
    return urllib.request.Request(
        POSTS_URL, data=json.dumps(body).encode("utf-8"), method="POST",
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json",
                 "X-Restli-Protocol-Version": "2.0.0",
                 "Linkedin-Version": version})


def send(req: urllib.request.Request) -> tuple[int, dict, str]:
    """(status, lower-cased headers, body) for any HTTP status."""
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, {k.lower(): v for k, v in resp.headers.items()}, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as err:
        return err.code, {k.lower(): v for k, v in err.headers.items()}, err.read().decode("utf-8", "replace")
    except urllib.error.URLError as err:
        raise PostError(f"could not reach LinkedIn: {err.reason}") from None


def explain(status: int, body: str) -> str:
    snippet = re.sub(r"\s+", " ", body)[:300]
    hints = {
        401: "the token is expired or revoked: run tools/linkedin_auth.py again and update the "
             "LINKEDIN_ACCESS_TOKEN secret and the LINKEDIN_TOKEN_EXPIRES variable",
        403: "LinkedIn refused the permission: is 'Share on LinkedIn' (w_member_social) on the app, "
             "and does LINKEDIN_AUTHOR_URN belong to the person who authorised the token?",
        422: "LinkedIn rejected the text or the request",
        426: "LinkedIn does not accept this API version: set LINKEDIN_API_VERSION to a current "
             "YYYYMM (see the versions listed in LinkedIn's migration guide)",
        429: "LinkedIn's rate limit was reached: try again later",
    }
    return f"HTTP {status}: {hints.get(status, 'unexpected reply')}. LinkedIn said: {snippet}"


def post(text: str, author: str, token: str, *, version: str | None = None, expires: str = "",
         dry_run: bool = False, today: dt.date | None = None, sender=send, say=print) -> str | None:
    """Post `text`. Returns the post's link, or None for a dry run."""
    text = text.strip() + "\n"
    if len(text) > LIMIT:
        raise PostError(f"the post is {len(text)} characters; LinkedIn's limit is {LIMIT}", 2)
    if not text.strip():
        raise PostError("the post is empty", 2)
    if not AUTHOR_RE.match(author or ""):
        raise PostError("LINKEDIN_AUTHOR_URN must look like urn:li:person:<id>", 2)
    if not token and not dry_run:
        raise PostError("LINKEDIN_ACCESS_TOKEN is not set", 2)
    left = days_left(expires, today)
    if left is not None and left < 0:
        raise PostError(f"the token expired {-left} day(s) ago ({expires}): run tools/linkedin_auth.py "
                        "again and update the secret and the variable", 2)
    if left is not None and left <= WARN_DAYS:
        say(f"warning: the token runs out in {left} day(s) ({expires}); run tools/linkedin_auth.py soon")
    version = version or default_version(today)
    if dry_run:
        say(f"dry run: would post {len(text)} characters as {author} (API version {version}):")
        say(text)
        return None
    status, headers, body = sender(build_request(text, author, token, version))
    if status != 201:
        raise PostError(explain(status, body))
    ident = headers.get("x-restli-id", "")
    if not ident:
        raise PostError("LinkedIn accepted the post but returned no post ID, so the link is unknown; "
                        "check the profile before posting again")
    return FEED_URL + ident + "/"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("post", help="post the text in a file")
    p.add_argument("--text-file", required=True)
    p.add_argument("--dry-run", action="store_true", help="show what would be posted; send nothing")
    e = sub.add_parser("extract", help="print the draft from an issue body")
    e.add_argument("--issue-body-file", required=True)
    args = ap.parse_args(argv)

    try:
        if args.cmd == "extract":
            with open(args.issue_body_file, encoding="utf-8") as fh:
                sys.stdout.write(extract_draft(fh.read()))
            return 0
        with open(args.text_file, encoding="utf-8") as fh:
            text = fh.read()
        link = post(text, os.environ.get("LINKEDIN_AUTHOR_URN", "").strip(),
                    os.environ.get("LINKEDIN_ACCESS_TOKEN", "").strip(),
                    version=os.environ.get("LINKEDIN_API_VERSION", "").strip() or None,
                    expires=os.environ.get("LINKEDIN_TOKEN_EXPIRES", "").strip(), dry_run=args.dry_run)
        if link:
            print(f"posted: {link}")
        return 0
    except PostError as err:
        print(f"error: {err}", file=sys.stderr)
        return err.code
    except OSError as err:
        print(f"error: {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
