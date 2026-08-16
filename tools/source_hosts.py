#!/usr/bin/env python3
"""Extract every host the Atlas cites, as a worklist for the re-verification pass.

Every entity in this Atlas carries `sources:` URLs that have never been
fetched (see `discovery/unresolved.md`). Reading them needs outbound HTTPS to
the hosts below — which, in a network-restricted environment, means an egress
allowlist.

This script derives that list from the repository, so it stays correct as
countries and entities are added. Regenerate with:

    python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md

Like `site/graph.json`, the generated file is an artefact — do not hand-edit it.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "validation"))

from common import load_all_entities  # noqa: E402

_HOST_RE = re.compile(r"^https?://([^/\s]+)", re.I)

# Suffixes where the registrable domain needs three labels, not two.
_THREE_LABEL = ("co.uk", "gov.uk", "ac.uk", "fgov.be", "just.fgov.be",
                "org.uk", "com.au", "co.nz")

# Hosts that are institutional rather than commentary. Used only to sort the
# report so the ones that matter appear first; nothing is excluded.
_INSTITUTIONAL = (
    ".europa.eu", ".un.org", ".int", ".gov", "gov.uk", "gov.be",
    ".bund.de", ".belgium.be", "fgov.be", "overheid.nl", "rijksoverheid.nl",
    "iso.org", "w3.org", "cencenelec.eu", "destatis.de", "fitko.de",
    "it-planungsrat.de", "belgif.be", "gdi-de.org", "logius.nl",
    "forumstandaardisatie.nl", "noraonline.nl", "geonovum.nl",
)


def registrable(host: str) -> str:
    h = host.lower().removeprefix("www.")
    for suf in _THREE_LABEL:
        if h.endswith("." + suf) or h == suf:
            parts = h.split(".")
            n = len(suf.split(".")) + 1
            return ".".join(parts[-n:]) if len(parts) >= n else h
    parts = h.split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else h


def is_institutional(domain: str) -> bool:
    return any(k.lstrip(".") in domain for k in _INSTITUTIONAL)


def collect():
    entities = load_all_entities(entities_only=True)
    host_counts: Counter[str] = Counter()
    domain_counts: Counter[str] = Counter()
    domain_entities: defaultdict[str, set[str]] = defaultdict(set)
    total_urls = 0
    unread = 0

    for e in entities:
        if not e.frontmatter:
            continue
        if e.frontmatter.get("verification") in ("search-only", "unverified"):
            unread += 1
        for s in e.frontmatter.get("sources") or []:
            if not isinstance(s, dict):
                continue
            m = _HOST_RE.match(str(s.get("url") or ""))
            if not m:
                continue
            total_urls += 1
            host = m.group(1).lower()
            host_counts[host] += 1
            d = registrable(host)
            domain_counts[d] += 1
            domain_entities[d].add(e.frontmatter["id"])

    return {
        "entities": len(entities),
        "unread": unread,
        "total_urls": total_urls,
        "hosts": host_counts,
        "domains": domain_counts,
        "domain_entities": domain_entities,
    }


def render_markdown(d: dict) -> str:
    inst = sorted(x for x in d["domains"] if is_institutional(x))
    other = sorted(x for x in d["domains"] if not is_institutional(x))
    top = d["domains"].most_common(20)

    out = []
    w = out.append
    w("# Re-verification Allowlist")
    w("")
    w("> **Generated file — do not hand-edit.** Regenerate with")
    w("> `python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md`")
    w("")
    w(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}")
    w("")
    w("## Why this exists")
    w("")
    w(f"**{d['unread']} of the Atlas's {d['entities']} entities have never had a "
      f"cited source read.** Their `sources:` URLs were confirmed to exist by a "
      f"search index and nothing more, which is what `verification: search-only` "
      f"records.")
    w("")
    w("Closing that debt — the re-verification pass — needs outbound HTTPS to the "
      "hosts those URLs point at. In an environment with a restricted egress "
      "policy, this is the allowlist to request. A denial shows up as "
      "`403 to CONNECT` from the proxy, which is an environment-level network "
      "policy and cannot be changed from inside a session. See "
      "`discovery/unresolved.md` for the standing record of the sourcing debt.")
    w("")
    w(f"The Atlas currently cites **{d['total_urls']} source URLs** across "
      f"**{len(d['hosts'])} hosts**, collapsing to **{len(d['domains'])} "
      f"registrable domains**.")
    w("")
    w("## Highest value first")
    w("")
    w("Allowing just these covers the bulk of the pass:")
    w("")
    w("| Domain | URLs | Entities |")
    w("|---|---|---|")
    for dom, n in top:
        w(f"| `{dom}` | {n} | {len(d['domain_entities'][dom])} |")
    w("")
    w("## Institutional domains")
    w("")
    w("Government, EU, UN and standards-body sources — the ones that carry "
      "evidential weight.")
    w("")
    w("```")
    for x in inst:
        w(x)
    w("```")
    w("")
    w("## Remaining domains")
    w("")
    w("Trade press, law firms, encyclopedias and vendor pages. Lower value, but "
      "cited somewhere in the Atlas — several entities rest on them entirely and "
      "say so in their own bodies.")
    w("")
    w("```")
    for x in other:
        w(x)
    w("```")
    w("")
    w("## After the pass")
    w("")
    w("For each entity whose sources have been read: confirm or correct the "
      "claims, then set `verification: primary-source`, populate `last_verified`, "
      "and add per-source `accessed:` dates. Close the corresponding rows in "
      "`discovery/unresolved.md`. Then re-run Batches 6, 11 and 15, which "
      "`validation/reports.md` records as **partial by necessity** for exactly "
      "this reason.")
    w("")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--markdown", action="store_true", help="render the report")
    ap.add_argument("--domains", action="store_true", help="print domains, one per line")
    ap.add_argument("-o", "--out", type=Path, help="write to this path instead of stdout")
    args = ap.parse_args()

    d = collect()
    if args.markdown:
        text = render_markdown(d)
    elif args.domains:
        text = "\n".join(sorted(d["domains"])) + "\n"
    else:
        text = "\n".join(sorted(d["hosts"])) + "\n"

    if args.out:
        out = args.out if args.out.is_absolute() else (Path.cwd() / args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"source_hosts: {d['unread']}/{d['entities']} entities unread; "
              f"{d['total_urls']} URLs, {len(d['hosts'])} hosts, "
              f"{len(d['domains'])} domains")
        try:
            shown = out.resolve().relative_to(REPO_ROOT)
        except ValueError:
            shown = out
        print(f"source_hosts: wrote {shown}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
