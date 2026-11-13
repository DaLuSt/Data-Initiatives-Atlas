#!/usr/bin/env python3
"""Pick and prepare the next "idea post" for the scheduled LinkedIn workflow.

Used by .github/workflows/linkedin-ideas.yml. The posts live in section 3 of
docs/linkedin-page-posts.md ("### Post N. Title" followed by a ```text block). Twice a week
(Tuesday and Thursday, local time) the workflow runs every 15 minutes; this tool decides
whether the moment has come to post, and which post is next. Nothing here talks to LinkedIn
or to GitHub: the workflow does that, and tools/linkedin_post.py does the posting.

The time of day is drawn once per day, pseudo-randomly, from a hash of the date: a minute
between 08:00 and 22:00 local time. The same date always gives the same minute, so every
15-minute run of that day agrees on it without keeping any state. A run is "due" when the
drawn minute has passed, the day is Tuesday or Thursday, it is before 22:00, and the log
issue holds no entry for today (posted or failed): at most one attempt a day, so a failing
token cannot post or comment every 15 minutes.

What has been posted is kept in the comments of one log issue, one line per attempt:

    Posted idea post 12 on 2026-11-17: https://www.linkedin.com/feed/update/...
    Failed idea post 12 on 2026-11-17: <why>

Only comments by the accounts passed with --trusted count (the Actions bot and the owner),
so a stranger's comment cannot skip a post or block a day. A post is held back (never
posted by the workflow) when its section carries a line that starts with
"*Check before posting" or "*Hold": those are the posts whose facts go stale, or that the
owner has pulled from the rotation.

    python tools/linkedin_ideas.py queue
    python tools/linkedin_ideas.py decide --comments-file comments.json [--now ISO] [--force]
    python tools/linkedin_ideas.py text 12
    python tools/linkedin_ideas.py record posted --number 12 --date 2026-11-17 --text URL

Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from zoneinfo import ZoneInfo

REPO_ROOT = Path(__file__).resolve().parent.parent
BANK = REPO_ROOT / "docs" / "linkedin-page-posts.md"
DEFAULT_TZ = "Europe/Amsterdam"
POST_DAYS = (1, 3)              # Tuesday and Thursday (Monday is 0)
WINDOW_START = 8 * 60           # 08:00, in minutes after midnight
WINDOW_END = 22 * 60            # 22:00: the drawn minute is always before this
BANK_START = "## 3. Idea posts"
HOLD_RE = re.compile(r"^\*(Check before posting|Hold)", re.M)
LEDGER_RE = re.compile(r"^(Posted|Failed) idea post (\d+) on (\d{4}-\d{2}-\d{2}):", re.M)


class IdeaError(Exception):
    """Something is wrong with the bank or the input; the message is safe to print."""


@dataclass(frozen=True)
class Idea:
    number: int
    title: str
    text: str
    hold: bool


def parse_bank(markdown: str) -> list[Idea]:
    """The idea posts in section 3 of the bank, in order."""
    start = markdown.find(BANK_START)
    if start < 0:
        raise IdeaError(f"no section '{BANK_START}' in the bank")
    body = markdown[start + len(BANK_START):]
    end = re.search(r"^## ", body, re.M)
    if end:
        body = body[:end.start()]
    ideas: list[Idea] = []
    parts = re.split(r"^### Post (\d+)\. (.*)$", body, flags=re.M)
    # parts: [preamble, number, title, text, number, title, text, ...]
    for i in range(1, len(parts), 3):
        number, title, chunk = int(parts[i]), parts[i + 1].strip(), parts[i + 2]
        m = re.search(r"```text\n(.*?)\n```", chunk, re.S)
        if not m or not m.group(1).strip():
            raise IdeaError(f"post {number} has no ```text block")
        ideas.append(Idea(number, title, m.group(1).strip() + "\n", bool(HOLD_RE.search(chunk))))
    numbers = [x.number for x in ideas]
    if not ideas:
        raise IdeaError("the bank has no posts")
    if len(set(numbers)) != len(numbers):
        raise IdeaError("the bank has two posts with the same number")
    return ideas


def target_minute(day: dt.date, salt: str = "") -> int:
    """The minute of the day (local), from 08:00 up to 21:59, at which `day`'s post is due."""
    digest = hashlib.sha256(f"{day.isoformat()}|{salt}".encode()).hexdigest()
    return WINDOW_START + int(digest, 16) % (WINDOW_END - WINDOW_START)


def hhmm(minute: int) -> str:
    return f"{minute // 60:02d}:{minute % 60:02d}"


def ledger(comments: list[dict], trusted: set[str]) -> tuple[set[int], set[dt.date]]:
    """(numbers posted, days on which an attempt was logged) from the log issue's comments."""
    posted: set[int] = set()
    days: set[dt.date] = set()
    for c in comments:
        author = ((c.get("author") or {}).get("login") or "").lower()
        if author not in trusted:
            continue
        for kind, number, day in LEDGER_RE.findall(c.get("body") or ""):
            days.add(dt.date.fromisoformat(day))
            if kind == "Posted":
                posted.add(int(number))
    return posted, days


@dataclass(frozen=True)
class Decision:
    due: bool
    number: int | None
    reason: str
    date: str
    target: str


def decide(ideas: list[Idea], comments: list[dict], now: dt.datetime, *, trusted: set[str],
           force: bool = False, salt: str = "") -> Decision:
    """Is a post due at `now` (a timezone-aware local time), and which one?"""
    day = now.date()
    target = target_minute(day, salt)
    posted, attempted = ledger(comments, trusted)
    eligible = [i for i in ideas if not i.hold and i.number not in posted]
    nxt = eligible[0].number if eligible else None

    def d(due: bool, reason: str) -> Decision:
        return Decision(due, nxt if due else None, reason, day.isoformat(), hhmm(target))

    if not eligible:
        return d(False, "the queue is empty: every post is posted or held")
    if force:
        return d(True, "a manual run: posting the next one now")
    if day.weekday() not in POST_DAYS:
        return d(False, "not a Tuesday or Thursday")
    if day in attempted:
        return d(False, "already tried today")
    minute = now.hour * 60 + now.minute
    if minute < target:
        return d(False, f"too early: today's time is {hhmm(target)}")
    if minute >= WINDOW_END:
        return d(False, f"missed: today's time was {hhmm(target)} and the window closed at 22:00")
    return d(True, f"today's time ({hhmm(target)}) has passed")


def record_line(kind: str, number: int, day: str, text: str) -> str:
    if kind not in ("posted", "failed"):
        raise IdeaError("kind must be posted or failed")
    dt.date.fromisoformat(day)
    text = re.sub(r"\s+", " ", text).strip()[:300]
    return f"{kind.capitalize()} idea post {number} on {day}: {text}"


def load_bank(path: Path = BANK) -> list[Idea]:
    return parse_bank(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bank", default=str(BANK))
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("queue", help="print the posts, which are held, and the next one")
    d = sub.add_parser("decide", help="print key=value lines: due, number, date, target, reason")
    d.add_argument("--comments-file", required=True, help="JSON list of the log issue's comments (gh issue view --json comments)")
    d.add_argument("--now", help="ISO time to use instead of the clock (tests); naive means local")
    d.add_argument("--tz", default=DEFAULT_TZ)
    d.add_argument("--trusted", default="github-actions,github-actions[bot]")
    d.add_argument("--force", action="store_true")
    t = sub.add_parser("text", help="print the text of one post")
    t.add_argument("number", type=int)
    r = sub.add_parser("record", help="print the log line for the issue comment")
    r.add_argument("kind", choices=["posted", "failed"])
    r.add_argument("--number", type=int, required=True)
    r.add_argument("--date", required=True)
    r.add_argument("--text", required=True)
    args = ap.parse_args(argv)
    try:
        if args.cmd == "record":
            print(record_line(args.kind, args.number, args.date, args.text))
            return 0
        ideas = load_bank(Path(args.bank))
        if args.cmd == "text":
            hit = next((i for i in ideas if i.number == args.number), None)
            if not hit:
                raise IdeaError(f"no post {args.number}")
            sys.stdout.write(hit.text)
            return 0
        if args.cmd == "queue":
            nxt = next((i for i in ideas if not i.hold), None)
            for i in ideas:
                mark = "HELD  " if i.hold else ("next  " if nxt and i is nxt else "queued")
                print(f"{mark} {i.number:>3}  {i.title}")
            print(f"\n{sum(not i.hold for i in ideas)} of {len(ideas)} posts are in the rotation.")
            return 0
        comments = json.loads(Path(args.comments_file).read_text(encoding="utf-8") or "[]")
        if isinstance(comments, dict):
            comments = comments.get("comments", [])
        tz = ZoneInfo(args.tz)
        now = dt.datetime.fromisoformat(args.now) if args.now else dt.datetime.now(tz)
        now = now.replace(tzinfo=tz) if now.tzinfo is None else now.astimezone(tz)
        trusted = {x.strip().lower() for x in args.trusted.split(",") if x.strip()}
        dec = decide(ideas, comments, now, trusted=trusted, force=args.force)
        print(f"due={'true' if dec.due else 'false'}")
        print(f"number={dec.number if dec.number is not None else ''}")
        print(f"date={dec.date}")
        print(f"target={dec.target}")
        print(f"reason={dec.reason}")
        return 0
    except (IdeaError, OSError, ValueError, KeyError) as err:
        print(f"error: {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
