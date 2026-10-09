#!/usr/bin/env python3
"""Probe which of the Atlas's hard-to-read source hosts a given machine can read.

Several hosts the Atlas cites cannot be read from the agent's own environment
(`discovery/unresolved.md` rows #4, #70, #216 to #225): domain-wide 403s, bot-defence
challenges, JavaScript shells. A GitHub-hosted runner has different egress, so some may
simply work there. This tool finds out, and writes a report; it edits nothing.

For each host it fetches the root and up to a few URLs that entities really cite, and
classifies each answer:

    READABLE      2xx with real text on it
    JS_SHELL      2xx, but an empty page that needs JavaScript
    CHALLENGE     a bot-defence page, or 202 with nothing (a challenge in progress)
    DENIED        401/403
    NOT_FOUND     404/410 (the URL moved: a repository problem, not a wall)
    SERVER_ERROR  5xx
    BLOCKED       the network policy refused the connection
    ERROR         DNS, TLS, timeout or anything else

The default User-Agent is the honest one that tools/reverify.py uses. `--browser-ua`
sends an ordinary browser string instead, to show whether a host is only refusing
unknown agents; whether to rely on that is a decision for a person, so the report says
which was used. TLS verification is never relaxed.

    python tools/host_probe.py                          # the default blocked hosts
    python tools/host_probe.py --hosts unece.org,iso.org --per-host 2
    python tools/host_probe.py --list-entities          # ids that cite those hosts
    python tools/host_probe.py --offline                # list the URLs, fetch none
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlsplit

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))
sys.path.insert(0, str(REPO_ROOT / "validation"))

import reverify  # noqa: E402  (its fetch settings: honest User-Agent, TLS context)
from common import load_all_entities  # noqa: E402

# The hosts named in discovery/unresolved.md's known-block rows.
DEFAULT_HOSTS = (
    "coe.int", "rm.coe.int", "iso.org", "oecd.org", "unece.org", "unctad.org",
    "bmi.bund.de", "digitale-verwaltung.de", "geant.org", "eduroam.org",
    "digitaleoverheid.nl", "eur-lex.europa.eu", "efta.int", "web.archive.org",
    "ccb.belgium.be", "bosa.belgium.be", "data.gov.be", "financien.belgium.be",
    "legilux.public.lu", "dre.pt", "diariodarepublica.pt", "fedlex.admin.ch",
    "bizkaia.eus", "legislation.gov.uk",
)
BROWSER_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/124.0 Safari/537.36")

READABLE, JS_SHELL, CHALLENGE, DENIED = "READABLE", "JS_SHELL", "CHALLENGE", "DENIED"
NOT_FOUND, SERVER_ERROR, BLOCKED, ERROR = "NOT_FOUND", "SERVER_ERROR", "BLOCKED", "ERROR"
MIN_TEXT = 300  # characters of visible text below which a 2xx page is not "readable"

CHALLENGE_RE = re.compile(
    r"just a moment|cf-chl|cf-browser-verification|attention required|captcha|"
    r"verify you are (a )?human|checking your browser|enable javascript and cookies|"
    r"please wait while|bot[- ]?(defen[cs]e|protection|detection)|access denied|"
    r"request unsuccessful|incapsula|akamai|px-captcha|awswaf|aws waf", re.I)
JS_RE = re.compile(r"enable javascript|requires javascript|noscript|you need to enable javascript", re.I)


@dataclass
class Probe:
    host: str
    url: str
    status: int | None = None
    verdict: str = ""
    detail: str = ""
    entities: list[str] = field(default_factory=list)


def visible_text(html: str) -> str:
    return reverify.strip_markup(html)


def classify(status: int | None, text: str, error: str = "", blocked: bool = False) -> tuple[str, str]:
    """(verdict, short reason) for one answer."""
    if blocked:
        return BLOCKED, error[:120]
    if status is None:
        return ERROR, error[:120] or "no answer"
    if status in (401, 403):
        if CHALLENGE_RE.search(text or ""):
            return CHALLENGE, f"HTTP {status} with a challenge page"
        return DENIED, f"HTTP {status}"
    if status in (404, 410):
        return NOT_FOUND, f"HTTP {status}"
    if status >= 500:
        if CHALLENGE_RE.search(text or ""):
            return CHALLENGE, f"HTTP {status} with a challenge page"
        return SERVER_ERROR, f"HTTP {status}"
    if 200 <= status < 300:
        body = visible_text(text or "")
        if status == 202 and len(body) < MIN_TEXT:
            return CHALLENGE, "HTTP 202 with no content (a challenge in progress)"
        if CHALLENGE_RE.search(text or "") and len(body) < 2000:
            return CHALLENGE, "a challenge page"
        if len(body) < MIN_TEXT:
            return (JS_SHELL, f"{len(body)} characters of text; needs JavaScript") if JS_RE.search(text or "") \
                else (JS_SHELL, f"only {len(body)} characters of text")
        return READABLE, f"{len(body)} characters of text"
    return ERROR, f"HTTP {status}"


def host_matches(url_host: str, wanted: str) -> bool:
    h = url_host.lower().removeprefix("www.")
    w = wanted.lower().removeprefix("www.")
    return h == w or h.endswith("." + w)


def collect_urls(hosts: tuple[str, ...] | list[str], per_host: int = 3, entities=None) -> dict[str, list[tuple[str, list[str]]]]:
    """For each host: its root, then up to `per_host` cited URLs (with the entity ids citing them).

    Cited URLs are picked to differ in path, in a stable order, so the same inputs always
    probe the same pages.
    """
    entities = entities if entities is not None else load_all_entities(entities_only=True)
    cited: dict[str, dict[str, list[str]]] = {h: {} for h in hosts}
    for e in sorted((x for x in entities if x.frontmatter), key=lambda x: x.frontmatter.get("id", "")):
        for s in e.frontmatter.get("sources") or []:
            url = str(s.get("url") or "") if isinstance(s, dict) else ""
            parts = urlsplit(url)
            if parts.scheme not in ("http", "https") or not parts.hostname:
                continue
            for h in hosts:
                if host_matches(parts.hostname, h):
                    cited[h].setdefault(url, []).append(e.frontmatter["id"])
    out: dict[str, list[tuple[str, list[str]]]] = {}
    for h in hosts:
        picks: list[tuple[str, list[str]]] = [(f"https://{h}/", [])]
        seen_paths: set[str] = set()
        for url, ids in sorted(cited[h].items()):
            path = urlsplit(url).path.rstrip("/") or "/"
            if len(picks) - 1 >= per_host:
                break
            if path in seen_paths or path == "/":
                continue
            seen_paths.add(path)
            picks.append((url, ids))
        out[h] = picks
    return out


def fetch(url: str, ua: str, timeout: float) -> tuple[int | None, str, str, bool]:
    """(status, text, error, blocked). Never raises; verification is never relaxed."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "text/html,*/*;q=0.8"})
        with urllib.request.urlopen(req, timeout=timeout, context=reverify._ssl_context()) as resp:
            raw = resp.read(500_000)
            charset = resp.headers.get_content_charset() or "utf-8"
            return resp.status, raw.decode(charset, errors="replace"), "", False
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read(50_000).decode("utf-8", "replace")
        except Exception:  # noqa: BLE001
            body = ""
        deny = exc.headers.get("x-deny-reason") if exc.headers else None
        return exc.code, body, (f"egress policy: {deny}" if deny else ""), bool(deny)
    except urllib.error.URLError as exc:
        low = str(exc.reason).casefold()
        return None, "", str(exc.reason), any(m in low for m in reverify._BLOCKED_MARKERS)
    except Exception as exc:  # noqa: BLE001  (one bad URL must not end the sweep)
        return None, "", f"{type(exc).__name__}: {exc}", False


def run(hosts, per_host, ua, timeout, delay, entities=None, fetcher=None, sleep=None) -> list[Probe]:
    fetcher = fetcher or fetch  # looked up now, so a test that replaces `fetch` really replaces it
    sleep = sleep or time.sleep
    probes: list[Probe] = []
    for host, urls in collect_urls(hosts, per_host, entities).items():
        for i, (url, ids) in enumerate(urls):
            if i:
                sleep(delay)
            status, text, error, blocked = fetcher(url, ua, timeout)
            verdict, detail = classify(status, text, error, blocked)
            probes.append(Probe(host, url, status, verdict, detail, ids))
    return probes


def host_verdict(probes: list[Probe]) -> str:
    c = Counter(p.verdict for p in probes)
    if c[READABLE] == len(probes):
        return "READABLE"
    if c[READABLE]:
        return "PARTLY READABLE"
    worst = Counter(p.verdict for p in probes if p.verdict != NOT_FOUND).most_common(1)
    return f"NOT READABLE ({worst[0][0]})" if worst else "NOT READABLE (NOT_FOUND)"


def render_markdown(probes: list[Probe], ua_name: str) -> str:
    by_host: dict[str, list[Probe]] = {}
    for p in probes:
        by_host.setdefault(p.host, []).append(p)
    lines = ["# Which hard-to-read hosts can this machine read?", "",
             f"User-Agent used: **{ua_name}**. {len(probes)} URLs on {len(by_host)} hosts; "
             "nothing in the repository was changed.", "",
             "| Host | Verdict | Probes (read of total) | What came back |", "|---|---|---|---|"]
    for host, ps in by_host.items():
        read = sum(1 for p in ps if p.verdict == READABLE)
        what = "; ".join(sorted({f"{p.verdict.lower()} ({p.detail})" for p in ps if p.verdict != READABLE}))[:200]
        lines.append(f"| `{host}` | {host_verdict(ps)} | {read} of {len(ps)} | {what or 'all readable'} |")
    readable = [h for h, ps in by_host.items() if host_verdict(ps) == "READABLE"]
    partly = [h for h, ps in by_host.items() if host_verdict(ps) == "PARTLY READABLE"]
    lines += ["", f"**Readable here:** {', '.join(f'`{h}`' for h in readable) or 'none'}.",
              f"**Partly readable:** {', '.join(f'`{h}`' for h in partly) or 'none'}.", "",
              "## Every URL", "", "| Verdict | URL | Cited by |", "|---|---|---|"]
    for p in probes:
        cited = ", ".join(p.entities[:4]) + (" …" if len(p.entities) > 4 else "")
        lines.append(f"| {p.verdict} | {p.url} | {cited or '(root)'} |")
    return "\n".join(lines) + "\n"


def citing_entities(hosts, entities=None) -> list[str]:
    ids: set[str] = set()
    for urls in collect_urls(hosts, per_host=10**6, entities=entities).values():
        for _, e in urls:
            ids.update(e)
    return sorted(ids)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hosts", help="comma-separated hosts (default: the known-blocked hosts)")
    ap.add_argument("--per-host", type=int, default=3, help="cited URLs to probe per host, besides the root")
    ap.add_argument("--timeout", type=float, default=20.0)
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between requests to one host")
    ap.add_argument("--browser-ua", action="store_true", help="send an ordinary browser User-Agent")
    ap.add_argument("--json", metavar="FILE", help="also write the probes as JSON")
    ap.add_argument("--markdown", metavar="FILE", help="also write the report as Markdown")
    ap.add_argument("--list-entities", action="store_true", help="print the ids of entities citing these hosts")
    ap.add_argument("--offline", action="store_true", help="list the URLs that would be probed")
    args = ap.parse_args(argv)

    hosts = tuple(h.strip() for h in args.hosts.split(",") if h.strip()) if args.hosts else DEFAULT_HOSTS
    if args.list_entities:
        print("\n".join(citing_entities(hosts)))
        return 0
    if args.offline:
        for host, urls in collect_urls(hosts, args.per_host).items():
            for url, ids in urls:
                print(f"{host}\t{url}\t{','.join(ids[:3])}")
        return 0

    ua = BROWSER_UA if args.browser_ua else reverify.USER_AGENT
    probes = run(hosts, args.per_host, ua, args.timeout, args.delay)
    report = render_markdown(probes, "browser-like" if args.browser_ua else "the Atlas's own (honest)")
    print(report)
    if args.json:
        Path(args.json).write_text(json.dumps([p.__dict__ for p in probes], indent=2), encoding="utf-8")
    if args.markdown:
        Path(args.markdown).write_text(report, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
