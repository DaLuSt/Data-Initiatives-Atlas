#!/usr/bin/env python3
"""Run the re-verification pass over an entity's cited sources.

Every entity in this Atlas was compiled from search-engine results: the URLs
in `sources:` were confirmed by a search index to exist and were **not read**.
That is what `verification: search-only` records, and closing it is the
re-verification pass described in `metadata/metadata-schema.md`.

This script does the mechanical half of that pass:

  * fetches each `sources[].url`, honouring HTTPS_PROXY and the system CA
    bundle — it never disables TLS verification;
  * extracts the entity's *checkable claims* — legal identifiers, its name and
    alternative names — and looks for each one in the retrieved page text;
  * reports a verdict per entity;
  * on `--write`, stamps `accessed:` on the sources that were actually
    retrieved, sets `last_verified:`, and flips `verification:` to
    `primary-source`.

It deliberately does **not** do the judgment half. A token appearing in a page
is corroboration, not verification: it says the identifier is on the page, not
that the entity's description of it is right. Nothing is written without an
explicit `--write` on a single entity, and the verdicts are worded to keep
that distinction visible.

Typical use:

    python tools/reverify.py --id NL-KADASTERWET          # report on one
    python tools/reverify.py --path 'legislation/nl-*.md' # report on a set
    python tools/reverify.py --search-only --limit 20     # work the backlog
    python tools/reverify.py --id NL-KADASTERWET --write  # stamp it verified

In an environment whose egress policy blocks outbound HTTPS — which is the
condition every entity in this repository was written under — every fetch
returns BLOCKED, no entity reaches a writable verdict, and the exit code says
so. That is the intended behaviour, not a failure of the tool.
`discovery/reverification-allowlist.md` is the list of hosts to unblock.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import fnmatch
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request
from http.client import InvalidURL
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "validation"))

from common import EntityFile, load_all_entities, parse_entity_file  # noqa: E402

CA_BUNDLE = Path("/root/.ccr/ca-bundle.crt")
USER_AGENT = (
    "Data-Initiatives-Atlas re-verification "
    "(+https://github.com/DaLuSt/Data-Initiatives-Atlas)"
)

# ── verdicts ─────────────────────────────────────────────────────────────
# Ordered worst to best. An entity's verdict is the worst of its sources',
# except that CORROBORATED additionally requires every claim to be found.
BLOCKED = "BLOCKED"            # egress policy refused the connection
UNREACHABLE = "UNREACHABLE"    # the host answered, but not with the page
REVIEW = "NEEDS REVIEW"        # retrieved, but a claim was not found on it
CORROBORATED = "CORROBORATED"  # retrieved, and every claim appears
NO_SOURCES = "NO SOURCES"

_WRITABLE = (REVIEW, CORROBORATED)


# ── claim extraction ─────────────────────────────────────────────────────
# Identifier shapes the Atlas actually keys entities on. Each is a citation
# that resolves to a *different real instrument* when it is wrong, which is
# why they are worth checking mechanically: a wrong BWBR number does not 404,
# it silently returns another act. See discovery/unresolved.md on the
# Kadasterwet / Archiefwet near-miss that motivated this list.
_IDENTIFIER_PATTERNS = (
    r"BWBR\d{7}",                                  # Dutch wetten.overheid.nl
    r"BOE-[A-Z]-\d{4}-\d+",                        # Spanish Boletín Oficial
    r"JORF(?:TEXT|SCTA|DOLE)\d{12}",               # French Légifrance
    r"(?:C?ETS)\s*(?:No\.?\s*)?\d{1,3}\b",         # Council of Europe treaties
    r"S\.?I\.?\s*No\.?\s*\d+\s*/\s*\d{4}",         # Irish statutory instruments
    r"(?:Directive|Regulation)\s*\(EU\)\s*\d{4}/\d+",
    r"Directive\s*\d{4}/\d+/E[CU]",
    r"\b3\d{4}[A-Z]\d{4}\b",                       # EUR-Lex CELEX
    r"Dz\.\s?U\.\s*\d{4}[^\s,;)]*",                # Polish Dziennik Ustaw
    r"Real Decreto(?:-ley)?\s*\d+/\d{4}",
    r"Ley\s*(?:Org[áa]nica\s*)?\d+/\d{4}",
    r"Lei\s*n\.?[ºo]?\s*\d+/\d{4}",
    r"z[áa]kon\s*č?\.?\s*\d+/\d{4}",
)
_IDENTIFIER_RE = re.compile("|".join(f"(?:{p})" for p in _IDENTIFIER_PATTERNS), re.I)

# Names shorter than this are too generic to be evidence of anything.
_MIN_NAME_LEN = 8


def checkable_claims(fm: dict) -> list[str]:
    """The strings whose presence on a page is worth checking.

    Two kinds, and the distinction matters when reading a report:

    * **identifiers** — a legal citation. Its absence from the page the entity
      cites is a real signal, because that is the one string the page is
      certain to contain if the citation is right.
    * **names** — the entity's `name` and `alternative_names`. Absence is weak
      evidence: pages are multilingual, titles get abbreviated, and an
      official page may never spell out its own long-form title.
    """
    claims: list[str] = []

    haystack = " \n".join(
        str(v) for k, v in fm.items()
        if k in ("name", "alternative_names", "description") and v
    )
    for rel in fm.get("relationships") or []:
        if isinstance(rel, dict) and rel.get("evidence"):
            haystack += " \n" + str(rel["evidence"])

    for m in _IDENTIFIER_RE.finditer(haystack):
        token = _normalise(m.group(0))
        if token not in claims:
            claims.append(token)

    for name in [fm.get("name")] + list(fm.get("alternative_names") or []):
        if not name:
            continue
        name = str(name).strip()
        if len(name) >= _MIN_NAME_LEN and _normalise(name) not in claims:
            claims.append(_normalise(name))

    return claims


def _normalise(s: str) -> str:
    """Collapse whitespace and case so 'ETS  No. 108' matches 'ETS No.108'."""
    return re.sub(r"\s+", " ", s).strip().casefold()


def page_contains(page_text: str, claim: str) -> bool:
    return _normalise(claim) in _normalise(page_text)


# ── fetching ─────────────────────────────────────────────────────────────
@dataclass
class FetchResult:
    url: str
    ok: bool
    status: int | None = None
    text: str = ""
    error: str = ""
    blocked: bool = False

    @property
    def label(self) -> str:
        if self.blocked:
            return BLOCKED
        if self.ok:
            return f"{self.status}"
        return UNREACHABLE


def _readable(path: Path | str | None) -> bool:
    """`True` only if the path exists and we are allowed to look at it.

    `Path.exists()` *raises* PermissionError rather than returning False when
    a parent directory is unreadable. The agent proxy's bundle lives under
    `/root/`, which is readable in the container this repository is usually
    worked in and not readable by the `runner` user in CI — so the plain
    `.exists()` call took the whole tool down on a machine that simply does
    not have the file. Extra trust anchors are an optimisation for one
    environment and must never be able to break the tool in another.
    """
    if not path:
        return False
    try:
        return Path(path).is_file()
    except OSError:
        return False


def _ssl_context() -> ssl.SSLContext:
    """Default verification, plus the agent proxy's CA when present.

    Verification is never relaxed here — no unverified context, no hostname
    check disabled, no permissive verify mode. A TLS failure is information
    about the environment and must not be silenced; `tools/test_reverify.py`
    enforces that by inspecting this module's syntax tree.
    """
    ctx = ssl.create_default_context()
    for candidate in (os.environ.get("REQUESTS_CA_BUNDLE"),
                      os.environ.get("SSL_CERT_FILE"),
                      CA_BUNDLE):
        if _readable(candidate):
            try:
                ctx.load_verify_locations(str(candidate))
            except (OSError, ssl.SSLError):
                pass
    return ctx


_BLOCKED_MARKERS = (
    "tunnel connection failed",
    "403",
    "407",
    "proxy",
    "egress",
)


def fetch(url: str, timeout: float) -> FetchResult:
    try:
        # Request construction is inside the guard too: it validates the URL
        # and raises on a malformed one, so leaving it outside made a bad
        # source crash the sweep just as surely as a bad request would.
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout,
                                    context=_ssl_context()) as resp:
            raw = resp.read(2_000_000)
            charset = resp.headers.get_content_charset() or "utf-8"
            return FetchResult(url=url, ok=True, status=resp.status,
                               text=raw.decode(charset, errors="replace"))
    except urllib.error.HTTPError as exc:
        # Not every egress denial arrives as a failed CONNECT. A plain-`http://`
        # URL goes to the proxy as an ordinary forward request, so its refusal
        # comes back as an HTTP *response* — a 403 that looks exactly like the
        # origin turning us away. The first full sweep of this repository
        # reported ten such sources as UNREACHABLE when nine of them were the
        # network policy, which is precisely the distinction this tool exists
        # to keep straight.
        #
        # The agent proxy labels its own refusals with `x-deny-reason`, so that
        # header is the signal. A 403 without it is left as the origin's, and
        # the response body is surfaced so a reader can see for themselves
        # rather than trusting this classification.
        deny = exc.headers.get("x-deny-reason") if exc.headers else None
        try:
            body = exc.read(400).decode("utf-8", "replace").strip().replace("\n", " ")
        except Exception:
            body = ""
        detail = f"HTTP {exc.code} {exc.reason}"
        if deny:
            detail = f"egress policy: {deny} — {body or detail}"
        elif body:
            detail = f"{detail} — {body[:160]}"
        return FetchResult(url=url, ok=False, status=exc.code,
                           error=detail, blocked=bool(deny))
    except urllib.error.URLError as exc:
        detail = str(exc.reason)
        low = detail.casefold()
        blocked = any(m in low for m in _BLOCKED_MARKERS)
        return FetchResult(url=url, ok=False, error=detail, blocked=blocked)
    except Exception as exc:
        # Breadth is deliberate. One unfetchable source must never take down a
        # sweep of four hundred entities — the run is a report, and an entity
        # that could not be checked is a line in it, not a crash.
        #
        # The case that forced this: `http.client.InvalidURL`, raised for a
        # source URL containing a literal space. On Python 3.11 it inherits
        # from HTTPException, *not* from ValueError, so a tidy tuple of
        # expected exception types missed it and the first full sweep died six
        # minutes in. A malformed URL is also the one failure here that is the
        # repository's fault rather than the network's, so it says so.
        kind = type(exc).__name__
        hint = (" — malformed URL in the entity's sources, not a network problem"
                if isinstance(exc, InvalidURL) else "")
        return FetchResult(url=url, ok=False, error=f"{kind}: {exc}{hint}")


def strip_markup(html: str) -> str:
    """Crude tag strip. Good enough to look for an identifier in body text."""
    text = re.sub(r"(?is)<(script|style|head)\b.*?</\1>", " ", html)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = (text.replace("&nbsp;", " ").replace("&amp;", "&")
                .replace("&lt;", "<").replace("&gt;", ">").replace("&#39;", "'")
                .replace("&quot;", '"'))
    return re.sub(r"\s+", " ", text)


# ── per-entity report ────────────────────────────────────────────────────
@dataclass
class SourceReport:
    url: str
    result: FetchResult
    found: list[str] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)


@dataclass
class EntityReport:
    entity_id: str
    rel_path: str
    verification: str
    claims: list[str]
    sources: list[SourceReport] = field(default_factory=list)
    verdict: str = NO_SOURCES

    @property
    def writable(self) -> bool:
        return self.verdict in _WRITABLE

    @property
    def uncorroborated(self) -> list[str]:
        """Claims not found on *any* retrieved source."""
        if not any(s.result.ok for s in self.sources):
            return list(self.claims)
        seen = {c for s in self.sources for c in s.found}
        return [c for c in self.claims if c not in seen]


def decide_verdict(rep: EntityReport) -> str:
    if not rep.sources:
        return NO_SOURCES
    if all(s.result.blocked for s in rep.sources):
        return BLOCKED
    if not any(s.result.ok for s in rep.sources):
        return UNREACHABLE
    # At least one source came back. Any source that did not, or any claim
    # nobody corroborated, keeps this at REVIEW.
    if not all(s.result.ok for s in rep.sources):
        return REVIEW
    return CORROBORATED if not rep.uncorroborated else REVIEW


def review_entity(e: EntityFile, timeout: float, offline: bool) -> EntityReport:
    fm = e.frontmatter or {}
    rep = EntityReport(
        entity_id=fm.get("id", "?"),
        rel_path=e.rel_path,
        verification=fm.get("verification", "(unstated)"),
        claims=checkable_claims(fm),
    )
    for src in fm.get("sources") or []:
        if not isinstance(src, dict) or not src.get("url"):
            continue
        url = src["url"]
        if offline:
            rep.sources.append(SourceReport(
                url=url,
                result=FetchResult(url=url, ok=False, error="not fetched (--offline)"),
            ))
            continue
        result = fetch(url, timeout)
        sr = SourceReport(url=url, result=result)
        if result.ok:
            text = strip_markup(result.text)
            for claim in rep.claims:
                (sr.found if page_contains(text, claim) else sr.missing).append(claim)
        rep.sources.append(sr)
    # Offline never reaches a judgeable verdict: nothing was retrieved, so
    # UNREACHABLE is the truthful answer rather than a pass or a failure.
    rep.verdict = (NO_SOURCES if not rep.sources
                   else UNREACHABLE if offline
                   else decide_verdict(rep))
    return rep


# ── writing back ─────────────────────────────────────────────────────────
def apply_verification(path: Path, retrieved_urls: set[str], today: str) -> list[str]:
    """Stamp the frontmatter after a human has judged the report.

    Edits the raw text rather than round-tripping the YAML, because dumping
    would reflow every hand-written `evidence:` block in the file and bury the
    real change in noise.

    Idempotent: running it twice replaces the `accessed:` date rather than
    adding a second one.

    Returns a list of the changes made, for the caller to print.
    """
    text = path.read_text(encoding="utf-8")
    changes: list[str] = []

    new_text, n = re.subn(r"(?m)^verification:\s*\S+\s*$",
                          "verification: primary-source", text, count=1)
    if n and new_text != text:
        changes.append("verification \u2192 primary-source")
        text = new_text

    if re.search(r"(?m)^last_verified:", text):
        text, n = re.subn(r"(?m)^last_verified:\s*.*$",
                          f'last_verified: "{today}"', text, count=1)
        if n:
            changes.append(f"last_verified \u2192 {today}")

    # `accessed:` goes on the sources that were actually retrieved, and only
    # those: a source that did not come back was not accessed, and saying it
    # was is the exact false claim `verification:` exists to prevent.
    #
    # Done block by block rather than line by line. A line-wise pass cannot
    # tell "insert a new accessed:" from "replace the existing one" without
    # lookahead, and gets both wrong on the second run.
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        out.append(lines[i])
        if not re.match(r"^sources:\s*$", lines[i]):
            i += 1
            continue

        i += 1
        block: list[str] = []
        while i < len(lines) and (lines[i].startswith((" ", "\t", "  - ")) or not lines[i].strip()):
            if lines[i].strip() and not lines[i].startswith(" "):
                break
            block.append(lines[i])
            i += 1

        out.extend(_stamp_source_block(block, retrieved_urls, today, changes))

    text = "\n".join(out)
    path.write_text(text, encoding="utf-8")
    return changes


def _stamp_source_block(block: list[str], retrieved_urls: set[str],
                        today: str, changes: list[str]) -> list[str]:
    """Rewrite one `sources:` list, adding or refreshing `accessed:`."""
    items: list[list[str]] = []
    for line in block:
        if re.match(r"^\s*-\s", line) or not items:
            items.append([])
        items[-1].append(line)

    result: list[str] = []
    for item in items:
        url = None
        for line in item:
            m = re.search(r"url:\s*[\"\']?(\S+?)[\"\']?\s*$", line)
            if m:
                url = m.group(1)
                break
        if url not in retrieved_urls:
            result.extend(item)
            continue

        kept = [l for l in item if not re.match(r"^\s+accessed:", l)]
        indent = "    "
        for line in kept:
            m = re.match(r"^(\s+)\w", line)
            if m and not re.match(r"^\s*-", line):
                indent = m.group(1)
                break
        # Append after the last non-blank field line of the item.
        last = max((j for j, l in enumerate(kept) if l.strip()), default=len(kept) - 1)
        kept.insert(last + 1, f'{indent}accessed: "{today}"')
        changes.append(f"accessed on {url}")
        result.extend(kept)
    return result


CAVEAT_RE = re.compile(r"(?m)^>\s*\*\*Sourcing caveat\.\*\*")


# ── selection and CLI ────────────────────────────────────────────────────
def select(args) -> list[EntityFile]:
    entities = [e for e in load_all_entities() if e.frontmatter]
    picked: list[EntityFile] = []

    if args.id:
        wanted = {i.upper() for i in args.id}
        picked = [e for e in entities if e.frontmatter.get("id") in wanted]
        missing = wanted - {e.frontmatter.get("id") for e in picked}
        if missing:
            print(f"reverify: no such entity id: {', '.join(sorted(missing))}",
                  file=sys.stderr)
    elif args.path:
        picked = [e for e in entities
                  if any(fnmatch.fnmatch(e.rel_path, p) for p in args.path)]
    elif args.search_only:
        picked = [e for e in entities
                  if e.frontmatter.get("verification") in ("search-only", "unverified")]
    else:
        picked = entities

    picked.sort(key=lambda e: e.rel_path)
    return picked[: args.limit] if args.limit else picked


def print_report(rep: EntityReport, verbose: bool) -> None:
    print(f"\n{rep.entity_id}  ({rep.rel_path})  verification: {rep.verification}")
    if not rep.claims:
        print("  no checkable claims — no identifier or long-form name in frontmatter")
    elif verbose:
        print(f"  claims: {', '.join(rep.claims)}")
    else:
        print(f"  {len(rep.claims)} checkable claim(s)")

    for sr in rep.sources:
        print(f"  [{sr.result.label:>11}] {sr.url}")
        if sr.result.error and not sr.result.ok:
            print(f"                {sr.result.error}")
        if sr.found:
            print(f"                ✓ {', '.join(sr.found)}")
        if sr.missing and verbose:
            print(f"                ✗ not on this page: {', '.join(sr.missing)}")

    print(f"  verdict: {rep.verdict}", end="")
    if rep.verdict == BLOCKED:
        print(" — the egress policy refused every source; nothing to judge.")
        print("           See discovery/reverification-allowlist.md for the hosts to allow.")
    elif rep.verdict == CORROBORATED:
        print(" — every source retrieved and every claim appears on one of them.")
        print("           That is corroboration, not verification: read the pages before --write.")
    elif rep.verdict == REVIEW:
        un = rep.uncorroborated
        print(" — retrieved, with something to look at.")
        if un:
            print(f"           uncorroborated: {', '.join(un)}")
    else:
        print()


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Run the re-verification pass over entity sources.",
        epilog="Corroboration is not verification. Read the pages before --write.",
    )
    sel = ap.add_mutually_exclusive_group()
    sel.add_argument("--id", action="append", metavar="ENTITY_ID",
                     help="entity id; repeatable")
    sel.add_argument("--path", action="append", metavar="GLOB",
                     help="repo-relative glob, e.g. 'legislation/nl-*.md'; repeatable")
    sel.add_argument("--search-only", action="store_true",
                     help="every entity still marked search-only or unverified")
    ap.add_argument("--limit", type=int, default=0, help="stop after N entities")
    ap.add_argument("--timeout", type=float, default=20.0, help="per-request seconds")
    ap.add_argument("--offline", action="store_true",
                    help="do not fetch; list what would be checked")
    ap.add_argument("--verbose", "-v", action="store_true",
                    help="list every claim and every miss")
    ap.add_argument("--json", action="store_true", help="machine-readable report")
    ap.add_argument("--write", action="store_true",
                    help="stamp accessed/last_verified/verification. Requires a single "
                         "--id and every source retrieved.")
    ap.add_argument("--force", action="store_true",
                    help="allow --write when some claims were not corroborated")
    args = ap.parse_args()

    if args.write and (not args.id or len(args.id) != 1):
        ap.error("--write applies to exactly one entity: pass a single --id")
    if args.write and args.offline:
        ap.error("--write needs a real fetch; drop --offline")

    entities = select(args)
    if not entities:
        print("reverify: nothing selected", file=sys.stderr)
        return 2

    reports = [review_entity(e, args.timeout, args.offline) for e in entities]

    if args.json:
        print(json.dumps([{
            "id": r.entity_id, "path": r.rel_path, "verdict": r.verdict,
            "verification": r.verification, "claims": r.claims,
            "uncorroborated": r.uncorroborated,
            "sources": [{"url": s.url, "status": s.result.status,
                         "blocked": s.result.blocked, "ok": s.result.ok,
                         "error": s.result.error, "found": s.found}
                        for s in r.sources],
        } for r in reports], indent=2))
    else:
        for rep in reports:
            print_report(rep, args.verbose)

        tally: dict[str, int] = {}
        for r in reports:
            tally[r.verdict] = tally.get(r.verdict, 0) + 1
        print("\n" + "─" * 68)
        print("  ".join(f"{v}: {n}" for v, n in sorted(tally.items())))
        if tally.get(BLOCKED):
            print("\nEvery blocked source is an environment network policy, not a bug "
                  "in\nthis tool or a missing page. `curl \"$HTTPS_PROXY/__agentproxy/status\"`\n"
                  "shows the proxy state; discovery/reverification-allowlist.md is the\n"
                  "list of hosts to request.")

    if args.write:
        rep = reports[0]
        if not rep.writable:
            print(f"\nrefusing to write: verdict is {rep.verdict}.", file=sys.stderr)
            return 1
        if rep.uncorroborated and not args.force:
            print(f"\nrefusing to write: {len(rep.uncorroborated)} claim(s) not found "
                  f"on any retrieved page.\nRe-read them, then pass --force if the "
                  f"entity is right anyway (pages\nabbreviate titles and change "
                  f"wording).", file=sys.stderr)
            return 1
        today = _dt.date.today().isoformat()
        retrieved = {s.url for s in rep.sources if s.result.ok}
        path = REPO_ROOT / rep.rel_path
        changes = apply_verification(path, retrieved, today)
        print(f"\n{rep.rel_path}:")
        for c in changes:
            print(f"  • {c}")
        if CAVEAT_RE.search(parse_entity_file(path).body):
            print("  ⚠ the body still carries its 'Sourcing caveat' blockquote — "
                  "remove it by hand.")

    worst = min((["BLOCKED", "UNREACHABLE", "NEEDS REVIEW", "CORROBORATED",
                  "NO SOURCES"].index(r.verdict) for r in reports), default=4)
    return 0 if worst >= 2 else 1


if __name__ == "__main__":
    sys.exit(main())
