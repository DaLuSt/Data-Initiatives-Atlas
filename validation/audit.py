#!/usr/bin/env python3
"""Deep graph audit for the validation batches (6, 11, 15).

`run_all.py` enforces the hard rules — schema conformance, resolvable links,
controlled vocabularies. This script answers the *analytical* questions the
validation batches ask: are there duplicates, orphans, unsupported
relationships, weakly-sourced entities, missing cross-level chains, and
country-specific assumptions leaking into the ontology?

It reports findings; it does not fail a build. Run:

    python validation/audit.py            # whole graph
    python validation/audit.py --scope NL # one layer
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict

import common

# Source domains that sit low in the README's preference order. Presence is
# not an error — it is a signal for the re-verification pass.
WEAK_SOURCE_PATTERNS = [
    ("grokipedia.com", "AI-generated encyclopedia"),
    ("wikipedia.org", "encyclopedia"),
    ("blog", "blog"),
    ("lexology.com", "legal marketing"),
    ("taylorwessing.com", "law firm"),
    ("whitecase.com", "law firm"),
    ("kennedyslaw.com", "law firm"),
    ("osborneclarke.com", "law firm"),
    ("skadden.com", "law firm"),
    ("ey.com", "consultancy"),
    ("namirial.com", "vendor"),
    ("legiscope.com", "commercial"),
    ("medialaws.eu", "commentary"),
    ("sva.nl", "law firm"),
]

AUTHORITATIVE_HINTS = ("europa.eu", ".gov", "overheid.nl", "un.org", "iso.org",
                       "w3.org", "itu.int", "oecd.org", "rijksoverheid.nl",
                       "eerstekamer.nl", "tweedekamer.nl", "unstats.un.org")


def scope_of(entity_id: str) -> str:
    if entity_id in ("NL", "EU", "UN"):
        return entity_id
    head = entity_id.split("-")[0]
    return head if head in ("UN", "EU", "INTL", "DOMAIN") else head


def normalise_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(name).lower()).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope", help="Restrict to an ID scope, e.g. NL, EU, UN, INTL")
    args = ap.parse_args()

    entities = [e for e in common.load_all_entities() if e.frontmatter]
    by_id = {e.frontmatter["id"]: e for e in entities}

    if args.scope:
        selected = {i for i in by_id if scope_of(i) == args.scope.upper()}
    else:
        selected = set(by_id)

    print(f"\n{'='*66}\nATLAS AUDIT — {args.scope.upper() if args.scope else 'WHOLE GRAPH'}")
    print(f"{len(selected)} of {len(by_id)} entities in scope\n{'='*66}")

    # ---------- composition ----------
    print("\n## Composition")
    by_scope = Counter(scope_of(i) for i in selected)
    for s, n in sorted(by_scope.items(), key=lambda kv: -kv[1]):
        print(f"  {s:<8} {n}")
    types = Counter(by_id[i].frontmatter.get("type") for i in selected)
    print("  types:", ", ".join(f"{t}={n}" for t, n in sorted(types.items())))

    # ---------- verification / confidence ----------
    print("\n## Evidence posture")
    for field in ("verification", "confidence", "coverage", "status"):
        c = Counter(by_id[i].frontmatter.get(field) for i in selected)
        print(f"  {field:<13}", ", ".join(f"{k}={v}" for k, v in sorted(c.items(), key=lambda kv: str(kv[0]))))

    # ---------- duplicates ----------
    print("\n## Duplicate detection")
    names = defaultdict(list)
    for i in selected:
        fm = by_id[i].frontmatter
        for n in [fm.get("name")] + (fm.get("alternative_names") or []):
            if n:
                names[normalise_name(n)].append(i)
    dupes = {k: v for k, v in names.items() if len(set(v)) > 1}
    if dupes:
        for k, v in sorted(dupes.items()):
            print(f"  ⚠ '{k}' → {sorted(set(v))}")
    else:
        print("  none — no name or alias is shared by two entities")

    # ---------- orphans ----------
    print("\n## Connectivity")
    outbound = defaultdict(set)
    inbound = defaultdict(set)
    for e in entities:
        fm = e.frontmatter
        src = fm["id"]
        targets = set()
        for rel in fm.get("relationships") or []:
            if isinstance(rel, dict) and rel.get("target"):
                targets.add(rel["target"])
        for field in ("related_entities", "organisations", "domains"):
            for t in fm.get(field) or []:
                targets.add(t)
        for t in targets:
            outbound[src].add(t)
            inbound[t].add(src)

    orphans = [i for i in sorted(selected) if not outbound[i] and not inbound[i]]
    if orphans:
        print(f"  ⚠ {len(orphans)} fully disconnected: {orphans}")
    else:
        print("  no fully disconnected entities")

    no_rel = [i for i in sorted(selected)
              if not (by_id[i].frontmatter.get("relationships") or [])]
    print(f"  {len(no_rel)} entities carry no provenanced relationship of their own")

    # ---------- relationship provenance ----------
    print("\n## Relationship provenance")
    rel_types, rel_source, low_conf, missing_ev = Counter(), Counter(), [], []
    total = 0
    for i in selected:
        for rel in by_id[i].frontmatter.get("relationships") or []:
            if not isinstance(rel, dict):
                continue
            total += 1
            rel_types[rel.get("type")] += 1
            rel_source[rel.get("source")] += 1
            if rel.get("confidence") == "low":
                low_conf.append((i, rel.get("type"), rel.get("target")))
            if not rel.get("evidence"):
                missing_ev.append((i, rel.get("type")))
    print(f"  {total} provenanced relationships in scope")
    print("  by source:", ", ".join(f"{k}={v}" for k, v in sorted(rel_source.items(), key=lambda kv: str(kv[0]))))
    print("  by type:  ", ", ".join(f"{k}={v}" for k, v in sorted(rel_types.items(), key=lambda kv: (-kv[1], str(kv[0])))))
    if missing_ev:
        print(f"  ⚠ {len(missing_ev)} relationships without evidence: {missing_ev}")
    if low_conf:
        print(f"  {len(low_conf)} at confidence: low —")
        for r in low_conf:
            print(f"      {r[0]} --{r[1]}--> {r[2]}")

    # ---------- source quality ----------
    print("\n## Source quality")
    nosrc, weak = [], []
    for i in sorted(selected):
        fm = by_id[i].frontmatter
        srcs = fm.get("sources") or []
        if not srcs:
            if fm.get("type") != "domain":
                nosrc.append(i)
            continue
        urls = [str(s.get("url", "")) for s in srcs if isinstance(s, dict)]

        def is_weak(u: str) -> bool:
            return any(pat in u.lower() for pat, _ in WEAK_SOURCE_PATTERNS)

        # An entity is flagged only when EVERY source is weak. A weak source
        # alongside an official one is normal and not a finding — the earlier
        # heuristic (an allow-list of authoritative domains) produced false
        # positives for organisations citing their own site, e.g. nen.nl.
        strong = [u for u in urls if not is_weak(u)]
        hits = {label for pat, label in WEAK_SOURCE_PATTERNS if any(pat in u.lower() for u in urls)}
        if hits and not strong:
            weak.append((i, sorted(hits), len(urls)))
    if nosrc:
        print(f"  ⚠ {len(nosrc)} non-domain entities with NO sources: {nosrc}")
    else:
        print("  every non-domain entity has at least one source")
    if weak:
        print(f"  ⚠ {len(weak)} entities relying ONLY on weak sources:")
        for i, labels, n in weak:
            print(f"      {i:<28} {n} source(s) — {', '.join(labels)}")

    # ---------- cross-level chains ----------
    if not args.scope:
        print("\n## Cross-level structure")
        cross = Counter()
        for e in entities:
            a = scope_of(e.frontmatter["id"])
            for rel in e.frontmatter.get("relationships") or []:
                if not isinstance(rel, dict) or not rel.get("target"):
                    continue
                b = scope_of(rel["target"])
                if a != b:
                    cross[f"{a} → {b}"] += 1
        for k, v in sorted(cross.items(), key=lambda kv: -kv[1]):
            print(f"  {k:<16} {v}")

        # country-neutrality: an EU/INTL concept must not be re-scoped per country
        print("\n## Country-neutrality")
        offenders = [i for i in by_id
                     if re.match(r"^[A-Z]{2}-(EU|UN|INTL)-", i)]
        if offenders:
            print(f"  ⚠ country-scoped copies of supra-national entities: {offenders}")
        else:
            print("  no country-scoped copies of EU/UN/INTL entities (README §16 holds)")

        applies_in = [(e.frontmatter["id"], rel["target"])
                      for e in entities
                      for rel in (e.frontmatter.get("relationships") or [])
                      if isinstance(rel, dict) and rel.get("type") == "applies-in"]
        print(f"  {len(applies_in)} applies-in relationships carry supra-national applicability")
        print(f"  targets: {sorted({t for _, t in applies_in})}")

    print(f"\n{'='*66}\naudit complete — findings above are advisory, not build failures\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
