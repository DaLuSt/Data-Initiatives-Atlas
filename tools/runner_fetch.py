#!/usr/bin/env python3
"""Read a few web pages on a machine that can reach them, and keep their text.

Some hosts the Atlas cites cannot be read from the agent's own environment but can be
read from a GitHub-hosted runner (`discovery/unresolved.md` row #235). This is the tool
the workflow "Read pages on a runner" runs: it fetches the pages it is given, writes each
page's visible text (or, for a PDF or other non-text file, the file itself) and a short
index, and nothing else. The files are attached to the workflow run; a person or a later
session reads them from there. It edits no entity.

    python tools/runner_fetch.py --urls "https://efta.int/ https://example.org/a.pdf" --out report

Only https addresses are fetched, at most 25 per run, one at a time with a pause, with the
Atlas's own User-Agent (a browser-like one was worse in the first probe). TLS verification
is never relaxed. A page that cannot be read is a line in the index, not a crash.
"""

from __future__ import annotations

import argparse
import re
import secrets
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import host_probe  # noqa: E402  (classification of an answer)
import reverify  # noqa: E402  (honest User-Agent, TLS context, markup stripping)

MAX_URLS = 25
MAX_BYTES = 5_000_000
LOG_PER_PAGE = 8_000   # characters of one page shown in the job log
LOG_TOTAL = 120_000    # characters of all pages together
TEXT_TYPES = ("text/", "application/xhtml", "application/xml", "application/json")


class FetchError(Exception):
    """A bad request to this tool (not a page that failed to load)."""


@dataclass
class Page:
    url: str
    status: int | None
    content_type: str
    body: bytes
    error: str = ""
    blocked: bool = False


@dataclass
class Saved:
    url: str
    verdict: str
    detail: str
    status: int | None
    file: str
    size: int


def parse_urls(text: str) -> list[str]:
    """The https addresses in `text` (separated by spaces, commas or newlines), in order, once each."""
    out: list[str] = []
    for raw in re.split(r"[\s,]+", text.strip()):
        if not raw:
            continue
        parts = urlsplit(raw)
        if parts.scheme != "https" or not parts.hostname:
            raise FetchError(f"only https addresses are fetched: {raw!r}")
        if raw not in out:
            out.append(raw)
    if not out:
        raise FetchError("no addresses were given")
    if len(out) > MAX_URLS:
        raise FetchError(f"{len(out)} addresses given; the limit is {MAX_URLS} per run")
    return out


def file_stem(index: int, url: str) -> str:
    host = re.sub(r"[^a-z0-9.-]+", "-", (urlsplit(url).hostname or "page").lower()).strip("-")
    return f"{index:02d}-{host}"[:60]


def is_text(content_type: str) -> bool:
    return content_type.lower().startswith(TEXT_TYPES)


def fetch(url: str, timeout: float = 30.0) -> Page:
    """Never raises; verification is never relaxed."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": reverify.USER_AGENT,
                                                   "Accept": "text/html,application/pdf,*/*;q=0.8"})
        with urllib.request.urlopen(req, timeout=timeout, context=reverify._ssl_context()) as resp:
            ctype = resp.headers.get_content_type() or ""
            return Page(url, resp.status, ctype, resp.read(MAX_BYTES + 1)[:MAX_BYTES])
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read(50_000)
        except Exception:  # noqa: BLE001
            body = b""
        ctype = exc.headers.get_content_type() if exc.headers else ""
        deny = exc.headers.get("x-deny-reason") if exc.headers else None
        return Page(url, exc.code, ctype, body, f"egress policy: {deny}" if deny else "", bool(deny))
    except urllib.error.URLError as exc:
        low = str(exc.reason).casefold()
        return Page(url, None, "", b"", str(exc.reason), any(m in low for m in reverify._BLOCKED_MARKERS))
    except Exception as exc:  # noqa: BLE001  (one bad page must not end the run)
        return Page(url, None, "", b"", f"{type(exc).__name__}: {exc}")


def charset_of(body: bytes) -> str:
    """The charset a page declares in its first 2 KB (`<meta charset="...">`), else UTF-8."""
    m = re.search(rb"charset=[\"']?([A-Za-z0-9_-]+)", body[:2048])
    return (m.group(1).decode("ascii") if m else "utf-8")


def save(page: Page, index: int, out: Path) -> Saved:
    """Write what was read; return one index row."""
    text_like = is_text(page.content_type) or (page.status is not None and not page.content_type and page.body[:1] == b"<")
    stem = file_stem(index, page.url)
    if text_like:
        try:
            html = page.body.decode(charset_of(page.body), errors="replace")
        except LookupError:
            html = page.body.decode("utf-8", errors="replace")
        verdict, detail = host_probe.classify(page.status, html, page.error, page.blocked)
        if verdict == host_probe.READABLE:
            name = stem + ".txt"
            (out / name).write_text(f"{page.url}\n\n{reverify.strip_markup(html)}\n", encoding="utf-8")
            return Saved(page.url, verdict, detail, page.status, name, len(page.body))
        return Saved(page.url, verdict, detail, page.status, "", len(page.body))
    if page.status is not None and 200 <= page.status < 300 and page.body:
        ext = ".pdf" if page.content_type == "application/pdf" or page.body[:5] == b"%PDF-" else ".bin"
        name = stem + ext
        (out / name).write_bytes(page.body)
        return Saved(page.url, host_probe.READABLE, f"a {page.content_type or 'binary'} file, {len(page.body)} bytes",
                     page.status, name, len(page.body))
    verdict, detail = host_probe.classify(page.status, "", page.error, page.blocked)
    return Saved(page.url, verdict, detail, page.status, "", len(page.body))


def flag_repeats(saved: list[Saved], out: Path) -> None:
    """One address answered many times with the same text is a shell: say so, drop the files."""
    seen: dict[str, list[Saved]] = {}
    for s in saved:
        if s.file.endswith(".txt"):
            body = (out / s.file).read_text(encoding="utf-8").split("\n\n", 1)[-1]
            seen.setdefault(body, []).append(s)
    for group in seen.values():
        hosts = {urlsplit(s.url).hostname for s in group}
        if len(group) > 1 and len(hosts) == 1:
            for s in group:
                (out / s.file).unlink()
                s.verdict, s.file = host_probe.JS_SHELL, ""
                s.detail = f"the same text as {len(group) - 1} other page(s) on this host: a shell"


def render_log(saved: list[Saved], out: Path, per_page: int = LOG_PER_PAGE, total: int = LOG_TOTAL,
               token: str | None = None) -> str:
    """The text of the pages that were read, for the job log, so it can be read without downloading
    the artifact. The text comes from the open web, so it is wrapped in `::stop-commands::` : without
    that, a page containing a line such as `::set-output ...` or `::error::` would be run as a
    workflow command. Each page is cut at `per_page` characters and the whole at `total`."""
    token = token or secrets.token_hex(16)
    lines = [f"::stop-commands::{token}"]
    used = 0
    for i, s in enumerate(saved, 1):
        if not s.file.endswith(".txt"):
            lines.append(f"===== {i}. {s.verdict}: {s.url} ({s.detail})")
            continue
        body = (out / s.file).read_text(encoding="utf-8")
        text = body.split("\n\n", 1)[-1]
        room = min(per_page, max(total - used, 0))
        shown = text[:room]
        used += len(shown)
        cut = f" [cut: {len(shown)} of {len(text)} characters]" if len(shown) < len(text) else ""
        lines.append(f"===== {i}. {s.verdict}: {s.url}{cut}")
        lines.append(shown)
    lines.append(f"::{token}::")
    return "\n".join(lines)


def render_index(saved: list[Saved]) -> str:
    lines = ["# Pages read on this machine", "",
             f"{len(saved)} address(es); the Atlas's own User-Agent; nothing in the repository was changed.", "",
             "| # | Verdict | Status | File | Address | Note |", "|---|---|---|---|---|---|"]
    for i, s in enumerate(saved, 1):
        lines.append(f"| {i} | {s.verdict} | {s.status or ''} | {('`' + s.file + '`') if s.file else ''} | {s.url} | {s.detail} |")
    return "\n".join(lines) + "\n"


def run(urls: list[str], out: Path, delay: float = 1.0, fetcher=None, sleep=None) -> list[Saved]:
    fetcher = fetcher or fetch
    sleep = sleep or time.sleep
    out.mkdir(parents=True, exist_ok=True)
    saved: list[Saved] = []
    for i, url in enumerate(urls, 1):
        if i > 1:
            sleep(delay)
        saved.append(save(fetcher(url), i, out))
    flag_repeats(saved, out)
    (out / "index.md").write_text(render_index(saved), encoding="utf-8")
    return saved


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--urls", required=True, help="https addresses separated by spaces or commas (max 25)")
    ap.add_argument("--out", default="report", help="directory for the files (default: report)")
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between pages")
    ap.add_argument("--log", action="store_true",
                    help="also print the text of the pages read (cut per page), guarded against workflow commands")
    args = ap.parse_args(argv)
    try:
        urls = parse_urls(args.urls)
    except FetchError as err:
        print(f"error: {err}", file=sys.stderr)
        return 2
    saved = run(urls, Path(args.out), args.delay)
    print(render_index(saved))
    if args.log:
        print(render_log(saved, Path(args.out)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
