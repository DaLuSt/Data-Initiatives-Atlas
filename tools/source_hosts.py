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

# Manual link check, 2026-08-20, by the repository owner: each of these was
# opened and confirmed to resolve to what the Atlas cites it for.
#
# `gob.es` was the single failure, and it is a defect in *this report* rather
# than in any citation. The rows are **registrable domains** — the right unit
# for a firewall rule, and a natural thing to paste into a browser. Eighteen
# of the nineteen happen to be both, because their apex serves a website.
# `gob.es` does not: Spain's government namespace has no apex site at all, and
# resolves to no address. Every Spanish host the Atlas actually cites —
# datos.gob.es, administracion.gob.es, digital.gob.es and the rest — resolves
# and works.
#
# The fix is the `Example host` column below, so every row offers something a
# human can open, not a rewrite of any citation.
_LC_OK = "✅ opens"
_LC_NOSITE = "⚠ namespace only — no site at the apex"
LINK_CHECKED = {
    "europa.eu": _LC_OK, "wikipedia.org": _LC_OK, "iso.org": _LC_OK,
    "coe.int": _LC_OK, "bund.de": _LC_OK, "digitaleoverheid.nl": _LC_OK,
    "gov.pl": _LC_OK, "gouv.fr": _LC_OK, "government.nl": _LC_OK,
    "gob.es": _LC_NOSITE,
    "overheid.nl": _LC_OK, "belgium.be": _LC_OK, "un.org": _LC_OK,
    "unece.org": _LC_OK, "cencenelec.eu": _LC_OK, "rijksoverheid.nl": _LC_OK,
    "bundestag.de": _LC_OK, "boe.es": _LC_OK, "legislation.gov.uk": _LC_OK,
    # Checked in a second pass, after `gob.es` raised the question of whether
    # other government namespaces in the Atlas's citations also lack an apex
    # site. All three serve one. That settles it: `gob.es` is the sole
    # exception among the government namespaces cited here.
    "gov.cz": _LC_OK, "gov.pt": _LC_OK, "public.lu": _LC_OK,
}

# Domains the repository owner has confirmed at the **content** tier, not just
# the link tier: the pages were read and the information on them confirmed
# correct (2026-08-21).
#
# This is a stronger claim than LINK_CHECKED and it is the only thing that
# licenses `verification: primary-source`. An entity qualifies only when
# **every** source it cites is on one of these domains — partial coverage
# leaves an entity `search-only`, because the unconfirmed source could be the
# one carrying the claim.
CONTENT_CONFIRMED = {
    "europa.eu", "iso.org", "coe.int", "bund.de", "legifrance.gouv.fr",
}

# Reachability sweep, 2026-08-20. Every institutional domain was resolved at
# both the apex and `www.`. This is the weakest of the three checks this
# repository distinguishes — it establishes that a host exists, nothing about
# what it serves — but it is the one that can be run without egress, and it is
# what would have caught `gob.es` before a human had to.
REACHABILITY = {
    "date": "2026-08-20",
    "checked": 52,
    "resolved": 52,
    # Apex has no address; only the www. host does. Not a defect — the Atlas
    # cites www./rm. hosts under all three — but worth recording so nobody
    # repeats the gob.es inference from an apex that does not answer.
    "www_only": ("coe.int", "gesetze-im-internet.de",
                 "verwaltungsvorschriften-im-internet.de"),
}

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
    domain_hosts: defaultdict[str, set[str]] = defaultdict(set)
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
            domain_hosts[d].add(host)

    return {
        "entities": len(entities),
        "unread": unread,
        "total_urls": total_urls,
        "hosts": host_counts,
        "domains": domain_counts,
        "domain_entities": domain_entities,
        "domain_hosts": domain_hosts,
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
    w("A domain here is an **allowlist pattern**, not a URL. Most of them also "
      "happen to serve a website at the apex; one does not. The `Example host` "
      "column is a real host the Atlas cites under that domain, so every row "
      "offers something that can actually be opened.")
    w("")
    w("| Domain | URLs | Entities | Example host | Opened | Content confirmed |")
    w("|---|---|---|---|---|---|")
    for dom, n in top:
        example = min(d["domain_hosts"].get(dom, {dom}))
        confirmed = "✅ 2026-08-21" if dom in CONTENT_CONFIRMED else ""
        w(f"| `{dom}` | {n} | {len(d['domain_entities'][dom])} "
          f"| `{example}` | {LINK_CHECKED.get(dom, '')} | {confirmed} |")
    w("")
    w("**`Opened` and `Content confirmed` are different claims.** The first "
      "says the citation points somewhere real. The second says the pages were "
      "read and the information on them confirmed correct, which is the only "
      "thing that licenses `verification: primary-source`. See "
      "`docs/re-verification.md` §\"A link check is not a content check\".")
    w("")
    w("### What the 2026-08-20 check found, and what it did not")
    w("")
    w("The repository owner opened all nineteen. Eighteen resolved to what the "
      "Atlas claims. **`gob.es` did not — and that is a defect in this report, "
      "not in any citation.**")
    w("")
    w("Spain's government namespace has **no apex site**: `gob.es` resolves to "
      "no address at all, unlike `gov.uk` and `gov.pl`, which are both real "
      "websites as well as namespaces. Every Spanish host the Atlas actually "
      "cites — `datos.gob.es`, `administracion.gob.es`, `digital.gob.es`, "
      "`espanadigital.gob.es` and the rest — resolves and works. Hence the "
      "`Example host` column.")
    w("")
    w("What the check **does** establish is that these citations point "
      "somewhere real. It does **not** establish that any entity's dates, "
      "identifiers, relationships or evidence strings are supported by the page "
      "cited — that is the content check, and it is what "
      "`verification: primary-source` records.")
    w("")
    w("**So no entity's `verification` changed on 2026-08-20.** That came "
      "later: on **2026-08-21** the repository owner confirmed "
      + ", ".join(f"`{k}`" for k in sorted(CONTENT_CONFIRMED)) +
      " at the content tier — read, and the information on them correct. "
      "Every entity whose sources lie **entirely** within those five domains "
      "moved to `verification: primary-source`. Entities with only some "
      "sources there did not, because the unconfirmed source could be the one "
      "carrying the claim.")
    w("")
    w("Two things about that list are worth stating precisely:")
    w("")
    w("- **`legifrance.gouv.fr`, not `gouv.fr`.** The confirmation names one "
      "host under the French government namespace. This table collapses all of "
      "`gouv.fr` into one row — `cyber.gouv.fr`, `numerique.gouv.fr`, "
      "`data.gouv.fr` and the rest — so that row is **not** marked confirmed, "
      "and it should not be.")
    w("- **The Legifrance confirmation moved no entity.** Five entities cite "
      "it and every one of them also cites something unconfirmed, so none "
      "qualified. That is the partial-coverage rule doing its job rather than "
      "a defect: a confirmation is not required to yield anything.")
    w("")
    also = [k for k in LINK_CHECKED if k not in {dom for dom, _ in top}]
    if also:
        w("**Also checked, outside the table above:** " +
          ", ".join(f"`{k}`" for k in sorted(also)) +
          " — the other government namespaces among the Atlas's citations. All "
          "serve a site at the apex, which settles the question `gob.es` "
          "raised: it is the **sole exception**, not the first of several.")
        w("")
    w("## Institutional domains")
    w("")
    w("Government, EU, UN and standards-body sources — the ones that carry "
      "evidential weight.")
    w("")
    r = REACHABILITY
    w(f"**Reachability sweep, {r['date']}: {r['resolved']} of {r['checked']} "
      f"resolve.** Every domain below was resolved at both the apex and "
      f"`www.`, and none is a dead namespace — `gob.es` remains the only one "
      f"of those in the Atlas.")
    w("")
    w("Three resolve at `www.` but not at the apex: " +
      ", ".join(f"`{x}`" for x in r["www_only"]) +
      ". That is not a defect — the Atlas cites `www.` or `rm.` hosts under "
      "all three — but it is recorded so that nobody repeats the `gob.es` "
      "inference from an apex that does not answer.")
    w("")
    w("This is the **weakest** of the three checks named in this file: it "
      "establishes that a host exists, and nothing about what it serves. It is "
      "also the only one that runs without egress, and it is what would have "
      "caught `gob.es` before a human had to.")
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
